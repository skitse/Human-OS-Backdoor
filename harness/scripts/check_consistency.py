#!/usr/bin/env python3
"""Consistency gate for the Human OS knowledge base.

Enforces three things that v1 of this repo got wrong by construction:

1. **Record completeness** — every mechanism entry in ``references/models/`` and
   ``references/manipulation-anatomy/`` must carry the full v2 field set defined in
   ``references/_schema.md``.
2. **Index/body agreement** — ``references/model-index.md`` is generated from the bodies,
   so the index cannot drift away from what actually exists.
3. **Reference routing** — every ``references/...`` path cited by SKILL.md, the scan
   protocol and the README must resolve to a real file.

Run with ``--write-index`` to regenerate the index region in place (the fix for a
drift failure), and without it to check (the CI form).

    python3 harness/scripts/check_consistency.py
    python3 harness/scripts/check_consistency.py --write-index
"""

from __future__ import annotations

import argparse
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SCAN_DIRS = [
    "references/models",
    "references/refused-domains",
]
SCHEMA_PATH = ROOT / "references" / "_schema.md"
COMBO_PATH = ROOT / "references" / "combo-patterns.md"
INDEX_PATH = ROOT / "references" / "model-index.md"
INDEX_BEGIN = "<!-- GENERATED:BEGIN"
INDEX_END = "<!-- GENERATED:END -->"
ALIAS_ROW_RE = re.compile(r"^\|\s*([A-Z]{2}-\d{2})\s*\|\s*([A-Z]{2}-\d{2})\s*\|")
DECLARED_ROW_RE = re.compile(
    r"^\|\s*([A-Z]{2}-\d{2})\s*\|\s*([^|]+?)\s*\|\s*([A-Z]{2})\s*\|"
)

# Files whose `references/...` citations must resolve.
LINK_CHECK_FILES = ["SKILL.md", "references/scan-protocol.md", "README.md", "README.en.md"]

HEADING_RE = re.compile(r"^##\s+([A-Z]{2}-\d{2})\s*·\s*(.+?)\s*$")

BASE_FIELDS = [
    "Tier",
    "Evidence",
    "Effect",
    "机制链",
    "剂量",
    "时间动态",
    "调节变量",
    "失效信号",
    "可测代理",
    "交互",
    "边界",
]
CM_FIELDS = ["危害画像", "检测信号", "防御动作", "监管环境"]

TIER_VALUES = {"核心", "常用", "情境"}
EVIDENCE_GRADES = {"A", "B", "C"}

# A field's value is a single line; sub-clauses use these separators.
CLAUSE_SEP = re.compile(r"[；;]")
# Any numeric confidence claim, bare or bold. The bold form is the one v1 actually used
# (`**Confidence**: 0.92`), so a pattern permitting only the bare form never fires.
FABRICATED_CONFIDENCE = re.compile(r"\*{0,2}Confidence\*{0,2}\s*[:：]\s*0\.\d")
# The v1 metadata *field* specifically, used against preserved prose: a bare mention is
# legitimate there — a record that downgrades its own v1 score ("v1 的 Confidence 0.74 已属
# 高估") is doing the right thing and must not be flagged. Only the surviving field line,
# which re-asserts precision the v2 Evidence grade replaced, is a contract violation.
V1_CONFIDENCE_FIELD = re.compile(r"\*\*Confidence\*\*\s*[:：]\s*0\.\d")
LINK_RE = re.compile(r"`(references/[A-Za-z0-9_./-]+\.md)`")


@lru_cache(maxsize=1)
def known_combos() -> frozenset[str]:
    """Combo ids actually defined in combo-patterns.md (read once per process)."""
    if not COMBO_PATH.exists():
        return frozenset()
    text = COMBO_PATH.read_text(encoding="utf-8")
    return frozenset(re.findall(r"^###\s+(COMBO-\d{2})", text, re.MULTILINE))


class Entry:
    def __init__(self, mid: str, name: str, path: Path, lineno: int):
        self.id = mid
        self.name = name
        self.path = path
        self.lineno = lineno
        self.fields: dict[str, str] = {}
        # Lines under this heading that are not v2 field declarations: the author's
        # preserved prose plus any leftover v1 metadata. Kept separate from `fields` so
        # checks can tell "this is the v2 field" from "this is historical text".
        self.prose: list[str] = []

    @property
    def family(self) -> str:
        return self.id.split("-")[0]

    def where(self) -> str:
        return f"{self.path.relative_to(ROOT)}:{self.lineno}"


def parse_entries() -> tuple[list[Entry], list[str]]:
    """Parse mechanism records out of the scanned directories."""
    entries: list[Entry] = []
    errors: list[str] = []

    for rel in SCAN_DIRS:
        directory = ROOT / rel
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith("_"):
                continue
            lines = path.read_text(encoding="utf-8").splitlines()
            current: Entry | None = None
            for i, line in enumerate(lines, start=1):
                if line.startswith("## "):
                    match = HEADING_RE.match(line)
                    current = None
                    if match:
                        current = Entry(match.group(1), match.group(2), path, i)
                        entries.append(current)
                    continue
                if current is None:
                    continue
                captured = False
                for key in BASE_FIELDS + CM_FIELDS:
                    token = f"**{key}**:"
                    if token in line:
                        # Value runs to end of line; on the Tier line, cut at the next field.
                        value = line.split(token, 1)[1].strip()
                        value = re.split(r"\s\|\s\*\*", value)[0].strip()
                        current.fields[key] = value
                        captured = True
                        break
                # Everything else under the heading is preserved v1 prose. Keep it: a
                # field-only view cannot see the fake-precision lines that survived the
                # migration (they are not v2 fields), so they would otherwise go unchecked.
                if not captured and line.strip():
                    current.prose.append(line)

    ids: dict[str, list[Entry]] = {}
    for entry in entries:
        ids.setdefault(entry.id, []).append(entry)
    for mid, dupes in sorted(ids.items()):
        if len(dupes) > 1:
            locations = ", ".join(d.where() for d in dupes)
            errors.append(f"duplicate mechanism id {mid}: {locations}")

    errors.extend(validate_aliases(entries))
    errors.extend(validate_declared(entries))

    return entries, errors


def parse_aliases() -> dict[str, str]:
    """Read the alias registry table from ``references/_schema.md``."""
    if not SCHEMA_PATH.exists():
        return {}
    aliases: dict[str, str] = {}
    for line in SCHEMA_PATH.read_text(encoding="utf-8").splitlines():
        match = ALIAS_ROW_RE.match(line)
        if match:
            aliases[match.group(1)] = match.group(2)
    return aliases


def parse_declared() -> dict[str, str]:
    """Read the declared-but-unwritten registry from ``references/_schema.md``.

    These IDs are named and intended but intentionally have no body yet. Holding them
    in a registry instead of in the index is what stops the index from advertising
    coverage that does not exist.
    """
    if not SCHEMA_PATH.exists():
        return {}
    declared: dict[str, str] = {}
    in_section = False
    for line in SCHEMA_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = "Declared-but-unwritten" in line
            continue
        if not in_section:
            continue
        match = DECLARED_ROW_RE.match(line)
        if match:
            declared[match.group(1)] = match.group(2).strip()
    return declared


def validate_declared(entries: list[Entry]) -> list[str]:
    """A declared ID must have no body and must not also be an alias."""
    problems: list[str] = []
    declared = parse_declared()
    real_ids = {e.id for e in entries}
    aliases = parse_aliases()
    for mid in sorted(declared):
        if mid in real_ids:
            problems.append(
                f"{mid} is declared unwritten but now has a body — remove the row from "
                "the Declared-but-unwritten registry"
            )
        if mid in aliases:
            problems.append(f"{mid} is both declared-unwritten and an alias — pick one")
    return problems


def validate_aliases(entries: list[Entry]) -> list[str]:
    """An alias must point at a real record and must not shadow a real record."""
    problems: list[str] = []
    aliases = parse_aliases()
    real_ids = {e.id for e in entries}
    for alias, canonical in sorted(aliases.items()):
        if alias == canonical:
            problems.append(f"alias {alias} points at itself")
        if alias in real_ids:
            problems.append(
                f"alias {alias} also exists as a full record — a mechanism must be either "
                "a canonical body or an alias, never both"
            )
        if canonical not in real_ids:
            problems.append(f"alias {alias} points at {canonical}, which has no body")
    return problems


def parse_combo_ids() -> set[str]:
    if not COMBO_PATH.exists():
        return set()
    text = COMBO_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"^###\s+(COMBO-\d{2})", text, re.MULTILINE))


def validate_entry(entry: Entry) -> list[str]:
    problems: list[str] = []
    required = list(BASE_FIELDS) + (CM_FIELDS if entry.family == "CM" else [])

    for field in required:
        if field not in entry.fields:
            problems.append(f"{entry.where()} {entry.id}: missing field **{field}**")

    # v1 metadata (e.g. `**Confidence**: 0.92 | **Effect Size**: Large`) is preserved as
    # historical prose, but a numeric confidence is banned by _schema.md: it was fabricated,
    # not measured. Left in place it sits directly under the record's honest Evidence grade
    # and re-asserts the fake precision the grade replaced — two contradictory authority
    # claims in one record. The field must go (or be relabelled as a v1 note), even though
    # the surrounding prose stays.
    if any(V1_CONFIDENCE_FIELD.search(line) for line in entry.prose):
        problems.append(
            f"{entry.where()} {entry.id}: v1 numeric confidence survived alongside the v2 "
            "**Evidence** grade — numeric confidence is banned (_schema.md); remove it or "
            "relabel it as a v1 note"
        )

    tier = entry.fields.get("Tier", "")
    if tier and tier not in TIER_VALUES:
        problems.append(
            f"{entry.where()} {entry.id}: Tier must be one of {sorted(TIER_VALUES)}, got {tier!r}"
        )

    evidence = entry.fields.get("Evidence", "")
    if evidence:
        grade = evidence.split("—")[0].strip().split()[0] if evidence.strip() else ""
        if grade not in EVIDENCE_GRADES:
            problems.append(
                f"{entry.where()} {entry.id}: Evidence must start with a grade A/B/C, got {evidence[:40]!r}"
            )
        if FABRICATED_CONFIDENCE.search(evidence):
            problems.append(
                f"{entry.where()} {entry.id}: Evidence carries a fabricated numeric confidence; "
                "cite a named source instead"
            )

    chain = entry.fields.get("机制链", "")
    if chain and chain.count("→") != 2:
        problems.append(
            f"{entry.where()} {entry.id}: 机制链 must have exactly 3 stages (2 arrows), "
            f"found {chain.count('→')}"
        )

    dose = entry.fields.get("剂量", "")
    if dose:
        missing_bands = [b for b in ("弱", "中", "强", "过载") if b not in dose]
        if missing_bands:
            problems.append(
                f"{entry.where()} {entry.id}: 剂量 missing band(s) {missing_bands}"
            )

    timing = entry.fields.get("时间动态", "")
    if timing:
        missing_clocks = [c for c in ("起效", "衰减", "饱和") if c not in timing]
        if missing_clocks:
            problems.append(
                f"{entry.where()} {entry.id}: 时间动态 missing clock(s) {missing_clocks}"
            )

    moderators = entry.fields.get("调节变量", "")
    if moderators:
        missing_mods = [m for m in ("个体", "文化", "情境") if m not in moderators]
        if missing_mods:
            problems.append(
                f"{entry.where()} {entry.id}: 调节变量 missing moderator(s) {missing_mods}"
            )

    signals = entry.fields.get("失效信号", "")
    if signals and len([c for c in CLAUSE_SEP.split(signals) if c.strip()]) < 2:
        problems.append(
            f"{entry.where()} {entry.id}: 失效信号 needs at least 2 observable signals "
            "(separate them with ；)"
        )

    interaction = entry.fields.get("交互", "")
    if interaction:
        for combo in sorted(set(re.findall(r"COMBO-\d{2}", interaction))):
            if combo not in known_combos():
                problems.append(
                    f"{entry.where()} {entry.id}: 交互 cites {combo}, which does not exist "
                    "in references/combo-patterns.md"
                )

    return problems


def check_combo_coverage(entries: list[Entry]) -> list[str]:
    """Every combo must be grounded in at least one mechanism record, and vice versa.

    A combo nobody cites is a dead cross-reference; a combo cited by records but
    absent from the file is the drift this check exists to catch.
    """
    problems: list[str] = []
    cited: set[str] = set()
    for entry in entries:
        cited |= set(re.findall(r"COMBO-\d{2}", entry.fields.get("交互", "")))

    for combo in sorted(known_combos() - cited):
        problems.append(
            f"{combo} is defined in combo-patterns.md but no mechanism record cites it "
            "in **交互**; ground the combo in its constituent mechanisms"
        )
    for combo in sorted(cited - known_combos()):
        problems.append(f"{combo} is cited by records but not defined")
    return problems


def build_index(entries: list[Entry], aliases: dict[str, str]) -> str:
    """Render the generated index region from the parsed bodies."""
    by_family: dict[str, list[Entry]] = {}
    for entry in entries:
        by_family.setdefault(entry.family, []).append(entry)

    out: list[str] = []
    out.append(
        "<!-- GENERATED:BEGIN — do not edit by hand. "
        "Edit the mechanism bodies, then run "
        "`python3 harness/scripts/check_consistency.py --write-index` -->"
    )
    out.append("")
    out.append(
        f"**{len(entries)} mechanism records** in {len({e.path for e in entries})} files, "
        f"each carrying the full _schema.md v2 field set. "
        f"{len(aliases)} alias ID(s) resolve to a canonical body."
    )
    out.append("")
    out.append(
        "Every row below is generated from a real record. If an ID is missing here, "
        "the mechanism does not exist — add the body, not the row."
    )
    out.append("")

    for family in sorted(by_family):
        group = sorted(by_family[family], key=lambda e: e.id)
        out.append(f"### {family} · {len(group)} mechanisms")
        out.append("")
        out.append("| ID | Name | Tier | Evidence | Effect (abridged) |")
        out.append("|----|------|------|----------|-------------------|")
        for entry in group:
            effect = entry.fields.get("Effect", "")
            effect = re.split(r"[；;。]", effect)[0].strip()
            if len(effect) > 90:
                effect = effect[:87].rstrip() + "..."
            name = entry.name.replace("|", "/")
            out.append(
                f"| {entry.id} | {name} | {entry.fields.get('Tier', '?')} "
                f"| {entry.fields.get('Evidence', '?').split('—')[0].strip()} | {effect} |"
            )
        out.append("")

    if aliases:
        out.append(f"### Aliases · {len(aliases)} non-canonical IDs")
        out.append("")
        out.append(
            "These IDs appear in existing content but are not separate mechanisms. "
            "They resolve to the canonical record named here."
        )
        out.append("")
        out.append("| Alias | Canonical |")
        out.append("|-------|-----------|")
        for alias, canonical in sorted(aliases.items()):
            out.append(f"| {alias} | {canonical} |")
        out.append("")

    out.append("<!-- GENERATED:END -->")
    return "\n".join(out)


def read_generated_region(text: str) -> str | None:
    start = text.find(INDEX_BEGIN)
    end = text.find(INDEX_END)
    if start == -1 or end == -1:
        return None
    return text[start : end + len(INDEX_END)]


def check_index(entries: list[Entry], aliases: dict[str, str], write: bool) -> list[str]:
    expected = build_index(entries, aliases)
    if not INDEX_PATH.exists():
        if write:
            INDEX_PATH.write_text(expected + "\n", encoding="utf-8")
            return []
        return [f"missing {INDEX_PATH.relative_to(ROOT)}"]

    text = INDEX_PATH.read_text(encoding="utf-8")
    actual = read_generated_region(text)

    if actual == expected:
        return []

    if write:
        if actual is None:
            new_text = expected + "\n\n" + text
        else:
            new_text = text[: text.find(INDEX_BEGIN)] + expected + text[
                text.find(INDEX_END) + len(INDEX_END) :
            ]
        INDEX_PATH.write_text(new_text, encoding="utf-8")
        return []

    if actual is None:
        return [
            "model-index.md has no generated region; run with --write-index to build it"
        ]

    actual_ids = set(re.findall(r"^\|\s*([A-Z]{2}-\d{2})\s*\|", actual, re.MULTILINE))
    expected_ids = {e.id for e in entries} | set(aliases)
    problems: list[str] = []
    missing = sorted(expected_ids - actual_ids)
    stale = sorted(actual_ids - expected_ids)
    if missing:
        problems.append(f"model-index.md is missing {len(missing)}: {missing}")
    if stale:
        problems.append(
            f"model-index.md lists {len(stale)} IDs with no body and no alias: {stale}"
        )
    if not problems:
        problems.append(
            "model-index.md generated region is stale; "
            "run `python3 harness/scripts/check_consistency.py --write-index`"
        )
    return problems


def check_links() -> list[str]:
    problems: list[str] = []
    for rel in LINK_CHECK_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for target in LINK_RE.findall(line):
                if not (ROOT / target).exists():
                    problems.append(f"{rel}:{lineno} cites missing path {target}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="regenerate the model-index.md generated region instead of failing on drift",
    )
    args = parser.parse_args()

    entries, errors = parse_entries()
    aliases = parse_aliases()

    if not entries:
        errors.append(
            "no mechanism records found — check SCAN_DIRS and the `## ID · Name` heading format"
        )

    for entry in entries:
        errors.extend(validate_entry(entry))

    errors.extend(check_combo_coverage(entries))
    errors.extend(check_index(entries, aliases, args.write_index))
    errors.extend(check_links())

    if errors:
        print("CONSISTENCY CHECK FAILED")
        for problem in errors:
            print(f"- {problem}")
        print(f"\n{len(errors)} problem(s) across {len(entries)} mechanism records")
        return 1

    print("CONSISTENCY CHECK OK")
    print(f"- {len(entries)} mechanism records, all v2 fields present")
    print(f"- {len(aliases)} alias ID(s) resolve to real bodies")
    print(f"- {len(known_combos())} combo pattern(s), each grounded in a record")
    print("- model-index.md matches the bodies")
    print("- all cited references/ paths resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
