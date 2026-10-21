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
SYNGROUP_ROW_RE = re.compile(
    r"^\|\s*`?([A-Z]{2}-\d{2}(?:\s*[+·]\s*[A-Z]{2}-\d{2})*)`?\s*\|"
    r"\s*`?([A-Z]{2}-\d{2})`?\s*\|\s*([^|]+?)\s*\|"
)

# Files whose `references/...` citations must resolve.
# Files that only ever ROUTE a reader to a mechanism. They must not name an id that
# has no body, because a name in these files is an instruction to go read it.
ROUTING_FILES = ["SKILL.md", "references/scan-protocol.md"]

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
    "可证伪条件",
]
CM_FIELDS = ["危害画像", "检测信号", "防御动作", "监管环境"]

# A falsification condition is not decoration: it names an observation and the sentence
# the record would lose. Without a floor on substance it degrades into "if it does not
# work, it does not work", which passes a presence check and carries nothing.
FALSIFY_OUTCOME = re.compile(r"不成立|不显著|无差异|无显著|失败|降级|删除|推翻|证伪|回落|不优于")
FALSIFY_MIN_CHARS = 30

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
        # The verbatim line each field was read from. Needed to detect a second field token
        # written on the same line: the parsed value has already been truncated at the ` | `,
        # so only the raw line still shows that a field was swallowed.
        self.raw_lines: dict[str, str] = {}
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
                        # Keep the raw line too. The value above has already had any
                        # trailing `| **Other**: …` cut off, so the value alone cannot show
                        # that a second field was written on the same line and swallowed.
                        current.raw_lines[key] = line
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
    errors.extend(validate_routing_targets())

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


def parse_syngroups() -> list[dict]:
    """Read the same-mechanism groups from ``references/_schema.md``.

    Returns ``[{"members": [...], "cite": "ID", "why": "..."}]``.

    Two records can describe one mechanism at different levels of abstraction
    (``HB-13`` hyperbolic discounting and ``CA-05`` temporal discounting) or with one
    file owning the applied depth (``HB-09`` and ``PE-04``). Both bodies stay useful, so
    neither becomes an alias — but counting them as two independent supports inflates a
    mechanics stack with a lever it does not actually have twice. A group declares that
    these IDs are one lever for accounting purposes, while each keeps its own body.
    """
    if not SCHEMA_PATH.exists():
        return []
    groups: list[dict] = []
    in_section = False
    for line in SCHEMA_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = "Same-mechanism" in line
            continue
        if not in_section:
            continue
        match = SYNGROUP_ROW_RE.match(line)
        if match:
            groups.append(
                {
                    "members": [m.strip() for m in re.split(r"[+·]", match.group(1)) if m.strip()],
                    "cite": match.group(2).strip(),
                    "why": match.group(3).strip(),
                }
            )
    return groups


def validate_syngroups(entries: list[Entry]) -> list[str]:
    """Every member must have a body, and a group must name at least two of them."""
    problems: list[str] = []
    real_ids = {e.id for e in entries}
    aliases = parse_aliases()
    seen: set[str] = set()
    for group in parse_syngroups():
        members = group["members"]
        if len(members) < 2:
            problems.append(f"same-mechanism group {members} names fewer than two IDs")
        if group["cite"] not in members:
            problems.append(
                f"same-mechanism group {members} says to cite {group['cite']}, which is not "
                "one of its members"
            )
        for mid in members:
            if mid not in real_ids:
                problems.append(
                    f"same-mechanism group names {mid}, which has no body — a group "
                    "accounts for existing records, it does not create them"
                )
            if mid in aliases:
                problems.append(
                    f"{mid} is both a same-mechanism group member and an alias — an alias "
                    "already collapses the ID, so grouping it again double-counts the fix"
                )
            if mid in seen:
                problems.append(
                    f"{mid} appears in more than one same-mechanism group — merge the groups"
                )
            seen.add(mid)
    return problems


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


def validate_routing_targets() -> list[str]:
    """A routing file must not send a reader to an id that has no body.

    ``_schema.md`` states this rule ("The scan protocol and SKILL.md must not route to a
    declared-only ID") but nothing enforced it, and a rule stated only in prose is not a
    rule. A declared-only id named in SKILL.md reads as an instruction to go read a file
    that does not exist — and the model then cites the id, which is how ``HB-07`` kept
    appearing in stacks before its body was written.
    """
    problems: list[str] = []
    declared = parse_declared()
    if not declared:
        return problems
    for rel in ROUTING_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for mid in re.findall(r"\b[A-Z]{2}-\d{2}\b", line):
                if mid in declared:
                    problems.append(
                        f"{rel}:{lineno} routes to {mid}, which is declared-but-unwritten "
                        f"(no body) — write the body or drop the mention"
                    )
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
        if field in entry.fields:
            continue
        # A field is "shadowed" when its token appears on a raw line that was captured for a
        # DIFFERENT field: the parser read the first token, truncated the value at the next
        # ` | `, and never saw this one.
        shadowers = [
            other
            for other, raw in entry.raw_lines.items()
            if other != field and f"**{field}**:" in raw
        ]
        if shadowers:
            problems.append(
                f"{entry.where()} {entry.id}: missing field **{field}** — it is sharing a "
                f"line with **{', '.join(shadowers)}**. The parser reads the first field "
                "token on a line and stops, so everything after ` | ` is swallowed. One "
                "field = one line (_schema.md, Line discipline); in particular Tier, "
                "Evidence and Effect go on three separate lines."
            )
        elif any(f"**{field}**:" in line for line in entry.prose):
            problems.append(
                f"{entry.where()} {entry.id}: **{field}** appears in the preserved prose "
                "below but is not parsed as a field — it is probably sharing a line with "
                "another field token. One field = one line."
            )
        else:
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

    # **可证伪条件** — what observation would show this mechanism does not hold here.
    # Required because a record that can never be wrong is not a finding, it is a slogan,
    # and because SKILL.md already tells the reader to "say what would falsify it" for
    # grade B while supplying no field to say it in.
    # The same check closes a hole the body authors found: `Evidence` could promise
    # "可证伪条件见本记录下方独立一行" and the line could be dropped by a renderer that
    # iterates only the canonical field list, with every check still green.
    falsify = entry.fields.get("可证伪条件", "").strip()
    if falsify:
        if len(falsify) < FALSIFY_MIN_CHARS:
            problems.append(
                f"{entry.where()} {entry.id}: 可证伪条件 is too thin ({len(falsify)} chars) — "
                "name the observation AND the sentence the record would lose"
            )
        if not FALSIFY_OUTCOME.search(falsify):
            problems.append(
                f"{entry.where()} {entry.id}: 可证伪条件 states no consequence — say what "
                "would be shown false and what the record would then lose "
                f"(expected one of {FALSIFY_OUTCOME.pattern})"
            )
    elif "可证伪条件" in entry.fields.get("Evidence", ""):
        problems.append(
            f"{entry.where()} {entry.id}: the Evidence line promises a falsification "
            "condition but the **可证伪条件** field is absent — a promise with no field "
            "behind it is exactly the defect this field exists to stop"
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


def build_index(
    entries: list[Entry], aliases: dict[str, str], groups: list[list[str]] | None = None
) -> str:
    """Render the generated index region from the parsed bodies."""
    by_family: dict[str, list[Entry]] = {}
    by_id: dict[str, Entry] = {}
    for entry in entries:
        by_family.setdefault(entry.family, []).append(entry)
        by_id[entry.id] = entry

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
        # The column header names the field the stack reads, so a model looking up an ID
        # can tell that this column is what `falsified_by` must be copied from.
        out.append(
            "| ID | Name | Tier | Evidence | Effect (abridged) | Falsifier (可证伪条件, abridged) |"
        )
        out.append(
            "|----|------|------|----------|-------------------|----------------------------------|"
        )
        for entry in group:
            effect = entry.fields.get("Effect", "")
            effect = re.split(r"[；;。]", effect)[0].strip()
            if len(effect) > 90:
                effect = effect[:87].rstrip() + "..."
            name = entry.name.replace("|", "/")
            # The falsifier is abridged for the same reason Effect is: the index is a
            # lookup table, not the record. It is rendered at all because the stack line
            # must carry the record's own 可证伪条件, and a value the reader cannot look
            # up here is a value the reader has to invent.
            # Unlike Effect, the falsifier is NOT split at its first clause. For a
            # falsifier the consequence is the point, and splitting on `；` keeps the
            # observation while dropping the claim it costs — which turns every row into
            # a sentence that could be pasted onto any other record. A writer hit exactly
            # that: their source said the right thing and the index showed half of it.
            # Keep both clauses and truncate the whole line instead.
            falsifier = entry.fields.get("可证伪条件", "")
            falsifier = re.sub(r"\s+", " ", falsifier).strip()
            # 240 keeps every condition in the repo intact today (longest is 221 chars);
            # the abridgement exists as a safety valve, not as a routine cut.
            if len(falsifier) > 240:
                falsifier = falsifier[:237].rstrip() + "..."
            out.append(
                f"| {entry.id} | {name} | {entry.fields.get('Tier', '?')} "
                f"| {entry.fields.get('Evidence', '?').split('—')[0].strip()} | {effect} "
                f"| {falsifier} |"
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

    if groups:
        body_count = sum(len(g["members"]) for g in groups)
        out.append(
            f"### Same-mechanism groups · {len(groups)} levers, {body_count} records"
        )
        out.append("")
        out.append(
            "Each group is **one lever for accounting**. The records in it keep separate "
            "bodies because each carries depth the other does not, but a mechanics stack "
            "must cite the group once — citing two members counts one support twice and "
            "borrows the higher evidence grade. See `references/_schema.md`."
        )
        out.append("")
        out.append("| One lever | Bodies | Cite as |")
        out.append("|-----------|--------|----------|")
        for group in groups:
            members = group["members"]
            names = " · ".join(sorted(members))
            canonical = by_id.get(group["cite"])
            cite = f"{group['cite']} ({canonical.name})" if canonical else group["cite"]
            out.append(f"| {names} | {len(members)} | {cite} |")
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
    expected = build_index(entries, aliases, parse_syngroups())
    if not INDEX_PATH.exists():
        if write:
            INDEX_PATH.write_text(expected + "\n", encoding="utf-8")
            return []
        return [f"missing {INDEX_PATH.relative_to(ROOT)}"]

    text = INDEX_PATH.read_text(encoding="utf-8")
    actual = read_generated_region(text)

    # Rows OUTSIDE the generated region are the dangerous ones: they look like the index,
    # they are never regenerated, and nothing used to compare them to the bodies. The v1
    # hand-written index survived the v2 migration this way and kept advertising 34 IDs
    # that have no body, complete with star ratings and 0.9x confidence decimals.
    outside = text
    if INDEX_BEGIN in text and INDEX_END in text:
        outside = (
            text[: text.find(INDEX_BEGIN)] + text[text.find(INDEX_END) + len(INDEX_END) :]
        )
    stray_rows = re.findall(r"^\|\s*([A-Z]{2}-\d{2})\s*\|", outside, re.MULTILINE)
    if stray_rows:
        return [
            f"model-index.md has {len(stray_rows)} index row(s) outside the generated "
            f"region ({sorted(set(stray_rows))[:6]}…) — delete them; the index is generated "
            f"from the bodies, and a hand-written copy beside it drifts silently"
        ]

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


def check_schema_agrees_with_checker() -> list[str]:
    """The contract document must not contradict the contract implementation.

    ``references/_schema.md`` is what every writer copies. When its template or its
    gold-standard example teaches a record shape this checker rejects, the doc is the bug,
    and the failures it causes look like author mistakes. That already happened once: the
    template and the worked example both wrote ``**Tier**: … | **Evidence**: …`` on one
    line — the exact shape the parser truncates — while a paragraph directly below called
    that form wrong. Writers hit the trap independently.

    Three things are checked, all mechanically decidable:
      1. the field list in the ```markdown template equals ``BASE_FIELDS``;
      2. the field table's required rows equal ``BASE_FIELDS``;
      3. neither the template nor the worked example contains a field line the parser would
         truncate (a second field token after `` | `` on the same line), except inside the
         explicitly-marked WRONG example.
    """
    problems: list[str] = []
    if not SCHEMA_PATH.exists():
        return [f"missing {SCHEMA_PATH.relative_to(ROOT)} — the record contract does not exist"]

    text = SCHEMA_PATH.read_text(encoding="utf-8")

    blocks = re.findall(r"```markdown\n(.*?)```", text, re.DOTALL)
    if not blocks:
        problems.append("references/_schema.md: no ```markdown record template found")
    else:
        template = blocks[0]
        template_fields = re.findall(r"^\*\*([^*]+)\*\*:", template, re.MULTILINE)
        missing = [f for f in BASE_FIELDS if f not in template_fields]
        extra = [f for f in template_fields if f not in BASE_FIELDS]
        if missing:
            problems.append(
                f"references/_schema.md template omits required field(s) {missing} — a writer "
                "copying it produces a record this checker rejects"
            )
        if extra:
            problems.append(
                f"references/_schema.md template lists unknown field(s) {extra} — they are "
                "not in BASE_FIELDS, so they will never be parsed"
            )

    table_required = set(
        re.findall(r"^\|\s*`\*\*([^*]+)\*\*`\s*\|\s*yes\s*\|", text, re.MULTILINE)
    )
    if table_required != set(BASE_FIELDS):
        only_doc = sorted(table_required - set(BASE_FIELDS))
        only_code = sorted(set(BASE_FIELDS) - table_required)
        problems.append(
            "references/_schema.md field table disagrees with BASE_FIELDS in "
            f"check_consistency.py — documented-only {only_doc}, code-only {only_code}"
        )

    # 3. A second field token after ` | ` on one line is silently swallowed. The WRONG
    # example is allowed to show it; every other ```markdown block and the surrounding doc
    # must not, because those are the lines writers copy. The WRONG line is marked by an
    # `<!-- WRONG` comment on the line above it, and is always followed by its RIGHT
    # counterpart — so an unmarked occurrence is the defect, not the demonstration.
    for index, block in enumerate(blocks):
        block_lines = block.splitlines()
        for lineno, line in enumerate(block_lines, start=1):
            if not re.match(r"^\*\*([^*]+)\*\*:.*\|\s*\*\*[^*]+\*\*:", line):
                continue
            marked_wrong = "WRONG" in "\n".join(block_lines[max(0, lineno - 3) : lineno - 1])
            if not marked_wrong:
                problems.append(
                    f"references/_schema.md markdown block {index + 1} line {lineno} teaches a "
                    "truncating field line (two field tokens on one line): "
                    f"{line[:60]!r} — only a line marked `<!-- WRONG` may show that shape"
                )
    return problems


# --- duplicate-mechanism detection -------------------------------------------------
# The v2 migration was written by six agents on disjoint files, so nothing ever compared
# records to each other. Four mechanisms ended up with two bodies apiece, each carrying
# its own evidence grade, and the index advertised both as separate levers.
#
# First attempt used text overlap on the mechanism chain. It was the wrong signal and it
# is worth recording why: it MISSED both real duplicates (AD-01/MR-12 and HB-13/CA-05
# describe one mechanism at different abstraction levels, so their wording barely
# overlaps — 0.20 and 0.12) and it FALSE-POSITIVED on every base-mechanism/abuse-form
# pair (HB-02 vs CM-14, SD-01 vs CM-03), which are legitimately two records because one
# is the mechanism and the other is its commercial misapplication. A detector scoring
# 0/2 on the known cases is the dead-linter trap again.
#
# The reliable signal is the one the records already state: a record that participates in
# a duplicate says so in its own 交互 field ("二者属同一机制的不同表述，计功时不可叠加").
# So: read the DECLARED relationship, and additionally flag any same-family or
# cross-family pair whose names collide and that no registry accounts for — because a
# name collision is a human-visible symptom even when the prose words differ.
SAME_MECHANISM_PHRASES = re.compile(
    r"同一机制|同一个机制|不同表述|不同抽象层|不可叠加|不要重复计数|重复计数|同一杠杆|同一个杠杆"
)
# ...but a clause that says a *component* shares a structure is composition, not
# duplication: CM-34 (anchoring + deadline in negotiation) legitimately contains CM-01's
# deadline structure while being its own mechanism. Sharing a part is what a COMBO is.
# Without this, the detector's own first run flagged CM-34 as a duplicate of CM-01.
COMPOSITION_MARKER = re.compile(r"结构|组件|子机制|环节|成分|组成部分")


def _content_tokens(text: str) -> set[str]:
    """Latin words and CJK bigrams — enough to compare two record names."""
    text = text.lower()
    tokens = {w for w in re.findall(r"[a-z]{4,}", text)}
    for run in re.findall(r"[\u4e00-\u9fff]+", text):
        tokens.update(run[i : i + 2] for i in range(len(run) - 1))
    return tokens


def _overlap(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


DUP_NAME_THRESHOLD = 0.80


def _accounted_for() -> set[frozenset[str]]:
    """Pairs already resolved by the alias or same-mechanism registries."""
    pairs: set[frozenset[str]] = set()
    for alias, canonical in parse_aliases().items():
        pairs.add(frozenset({alias, canonical}))
    for group in parse_syngroups():
        members = group["members"]
        for i, first in enumerate(members):
            for second in members[i + 1 :]:
                pairs.add(frozenset({first, second}))
    return pairs


def find_duplicate_mechanisms(entries: list[Entry]) -> list[str]:
    """Flag one mechanism wearing two bodies, in either of the two ways it shows up.

    (a) A record that DECLARES the collision in prose but no registry accounts for it —
        the strongest signal available, because the author already worked it out.
    (b) A pair whose NAMES collide (overlap >= DUP_NAME_THRESHOLD) — the symptom a reader
        sees in the index even when the two bodies are worded differently.

    A base-mechanism/abuse-form pair (a CM record named after the mechanism it misuses) is
    not a duplicate: one is the mechanism and one is its commercial misapplication, and
    they carry different evidence grades on purpose. Those are reported as a note, not a
    failure, so the list stays worth reading.
    """
    problems: list[str] = []
    notes: list[str] = []
    accounted = _accounted_for()
    by_id = {e.id: e for e in entries}

    def suggest(left: Entry, right: Entry) -> str:
        return (
            f"add a same-mechanism group row in references/_schema.md "
            f"(`| {left.id} + {right.id} | <why> |`), or make one an alias if it is a "
            "pure duplicate"
        )

    # (a) declared in prose, unregistered
    for entry in entries:
        for field in ("交互", "边界", "Effect"):
            for clause in re.split(r"[；;]", entry.fields.get(field, "")):
                if not SAME_MECHANISM_PHRASES.search(clause):
                    continue
                if COMPOSITION_MARKER.search(clause):
                    continue
                for other_id in re.findall(r"\b([A-Z]{2}-\d{2})\b", clause):
                    other = by_id.get(other_id)
                    if other is None or other.id == entry.id:
                        continue
                    if frozenset({entry.id, other.id}) in accounted:
                        continue
                    problems.append(
                        f"{entry.id} declares it is the same mechanism as {other.id} "
                        f"({clause.strip()[:70]}…) but no registry accounts for them — "
                        f"{suggest(entry, other)}"
                    )

    # (b) name collision, unregistered
    for i, left in enumerate(entries):
        for right in entries[i + 1 :]:
            if frozenset({left.id, right.id}) in accounted:
                continue
            name = _overlap(_content_tokens(left.name), _content_tokens(right.name))
            if name < DUP_NAME_THRESHOLD:
                continue
            if (left.family == "CM") != (right.family == "CM"):
                notes.append(
                    f"{left.id} and {right.id} share a name across the base/abuse split — "
                    "expected (one is the mechanism, the other its misapplication); "
                    "no action unless the bodies actually duplicate"
                )
                continue
            problems.append(
                f"{left.id} ({left.name}) and {right.id} ({right.name}) have colliding names "
                f"(overlap {name:.2f}) and no registry accounts for them — {suggest(left, right)}"
            )

    # dedupe (a) and (b) reporting the same pair
    seen: set[frozenset[str]] = set()
    unique: list[str] = []
    for problem in problems:
        ids = frozenset(re.findall(r"\b([A-Z]{2}-\d{2})\b", problem))
        if ids in seen:
            continue
        seen.add(ids)
        unique.append(problem)
    return unique


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

    errors.extend(validate_syngroups(entries))
    errors.extend(find_duplicate_mechanisms(entries))
    errors.extend(check_combo_coverage(entries))
    errors.extend(check_index(entries, aliases, args.write_index))
    errors.extend(check_links())
    errors.extend(check_schema_agrees_with_checker())

    if errors:
        print("CONSISTENCY CHECK FAILED")
        for problem in errors:
            print(f"- {problem}")
        print(f"\n{len(errors)} problem(s) across {len(entries)} mechanism records")
        return 1

    print("CONSISTENCY CHECK OK")
    print(f"- {len(entries)} mechanism records, all v2 fields present")
    print(f"- {len(aliases)} alias ID(s) resolve to real bodies")
    print(f"- {len(parse_syngroups())} same-mechanism group(s) declared")
    print(f"- {len(known_combos())} combo pattern(s), each grounded in a record")
    print("- model-index.md matches the bodies")
    print("- all cited references/ paths resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
