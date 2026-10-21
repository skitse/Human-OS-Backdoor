import json
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _normalize_text_list(items):
    if not isinstance(items, list):
        return ""
    return " ".join(str(item).lower() for item in items)


def smoke_assert(output: str, context: dict) -> dict:
    user_request = context.get("vars", {}).get("user_request", "")
    required_fragments = [
        "Return JSON only with this schema",
        "<human_os_skill>",
        user_request,
    ]
    missing = [frag for frag in required_fragments if frag not in output]
    passed = not missing
    return {
        "pass": passed,
        "score": 1.0 if passed else 0.0,
        "reason": "prompt rendered correctly" if passed else f"missing fragments: {missing}",
    }


CONTRACT_KEYS = ("trigger", "tier", "mode", "safety_action", "visible_stack", "full_scan")


def _parse_json(output: str):
    """Parse the answer's JSON contract object, ignoring reasoning text around it.

    NOT simply "the first JSON object in the output": a thinking-mode model reasons in prose
    and may sketch a fragment mid-thought — a real run emitted
    ``Stack: [{"id": "LT-01", "dose": "中", ...}]`` while deliberating, 6 kB before the
    answer. `raw_decode` from the first `{` returned that fragment, so every contract key
    read ``None`` and the case was reported as a total contract failure with a reason that
    described nothing the model actually did. A wrong reason is worse than a wrong score.

    The contract object is identified by its keys instead: take the first object that carries
    the full key set. Fall back to the widest object found if none matches, so a genuinely
    malformed answer still fails with its own fields visible.
    """
    decoder = json.JSONDecoder()
    best = None
    index = output.find("{")
    while index != -1:
        try:
            obj, _ = decoder.raw_decode(output, index)
        except json.JSONDecodeError:
            index = output.find("{", index + 1)
            continue
        if isinstance(obj, dict):
            if all(key in obj for key in CONTRACT_KEYS):
                return obj
            if best is None or len(obj) > len(best):
                best = obj
        index = output.find("{", index + 1)
    if best is None:
        raise json.JSONDecodeError("no JSON object found", output, 0)
    return best


@lru_cache(maxsize=1)
def _known_ids() -> frozenset[str]:
    """Every mechanism ID that exists: record ids plus COMBO ids.

    Read from the same sources the checker uses. Kept local rather than imported because
    promptfoo runs this file in its own process, where harness/scripts is not on sys.path.
    """
    known: set[str] = set()
    index = ROOT / "references" / "model-index.md"
    if index.exists():
        known.update(re.findall(r"\b[A-Z]{2}-\d{2}\b", index.read_text(encoding="utf-8")))
    combos = ROOT / "references" / "combo-patterns.md"
    if combos.exists():
        known.update(re.findall(r"\bCOMBO-\d{2}\b", combos.read_text(encoding="utf-8")))
    return frozenset(known)


@lru_cache(maxsize=1)
def _same_mechanism_groups() -> tuple[dict, ...]:
    """Read the same-mechanism groups declared in references/_schema.md.

    Parsed here rather than imported from check_consistency so the assertion stays usable
    from promptfoo's own process, where the harness scripts are not on sys.path.
    """
    schema = ROOT / "references" / "_schema.md"
    if not schema.exists():
        return ()
    row = re.compile(
        r"^\|\s*`?([A-Z]{2}-\d{2}(?:\s*[+·]\s*[A-Z]{2}-\d{2})*)`?\s*\|"
        r"\s*`?([A-Z]{2}-\d{2})`?\s*\|"
    )
    groups: list[dict] = []
    in_section = False
    for line in schema.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = "Same-mechanism" in line
            continue
        if not in_section:
            continue
        match = row.match(line)
        if match:
            groups.append(
                {
                    "members": [m.strip() for m in re.split(r"[+·]", match.group(1)) if m.strip()],
                    "cite": match.group(2).strip(),
                }
            )
    return tuple(groups)


def decision_contract_assert(output: str, context: dict) -> dict:
    vars_dict = context.get("vars", {})
    try:
        data = _parse_json(output)
    except (json.JSONDecodeError, ValueError) as exc:
        return {
            "pass": False,
            "score": 0.0,
            "reason": f"output is not valid JSON: {exc}",
        }

    checks = [
        ("trigger", vars_dict.get("expected_trigger")),
        ("tier", vars_dict.get("expected_tier")),
        ("mode", vars_dict.get("expected_mode")),
        ("safety_action", vars_dict.get("expected_safety_action")),
        ("visible_stack", vars_dict.get("expected_visible_stack")),
        ("full_scan", vars_dict.get("expected_full_scan")),
    ]

    # A parsed object with none of the contract keys is a fragment the model sketched while
    # reasoning, not an answer. Reported as a contract mismatch it produces six
    # "expected X, got None" lines that describe nothing the model did; name the real
    # problem so the next reader debugs the right thing.
    if not any(key in data for key in CONTRACT_KEYS):
        return {
            "pass": False,
            "score": 0.0,
            "reason": (
                "output contains no JSON object with the contract keys "
                f"{list(CONTRACT_KEYS)} — found only {sorted(data)[:8]}, which is a "
                "reasoning fragment rather than an answer"
            ),
        }

    failures = []
    for key, expected in checks:
        if expected is None:
            continue
        # `a|b` in a scalar expectation means both are defensible answers under SKILL.md.
        # Where the contract genuinely fixes one value the case states one value; where a
        # careful reader could argue for two, the test must not grade the tie-break.
        alternatives = [alt.strip() for alt in str(expected).split("|")]
        if str(data.get(key)) not in alternatives:
            failures.append(f"{key}: expected {expected!r}, got {data.get(key)!r}")

    references = data.get("references", [])
    stack = data.get("stack", [])
    notes = data.get("notes", [])

    # The mechanics stack is where the DESIGN lives, so it is where the v2 contract is
    # actually graded. Until `stack` existed the harness could only see routing decisions,
    # and every attempt to grade a design obligation through `notes` degenerated into
    # vocabulary matching (a correct answer failing for calling a refusal an "honest
    # alternative" instead of a "refusal"). These checks grade the stack's structure, not
    # its prose.
    if not isinstance(stack, list):
        failures.append("stack must be a list")
        stack = []
    else:
        for index, item in enumerate(stack):
            if not isinstance(item, dict):
                failures.append(f"stack[{index}] must be an object")
                continue
            missing = [k for k in ("id", "dose", "evidence", "stop") if not item.get(k)]
            if missing:
                failures.append(
                    f"stack[{index}] ({item.get('id', '?')}) is missing {missing} — every "
                    "stack line carries the record's own id, dose band, evidence grade and "
                    "failure signal"
                )
            # The record's 可证伪条件 is the claim's way of being wrong. A stack line that
            # carries a dose and a stop signal but no falsifier is the shape the v2 upgrade
            # exists to eliminate, so it is graded rather than merely recommended.
            if not item.get("falsified_by"):
                failures.append(
                    f"stack[{index}] ({item.get('id', '?')}) has no falsified_by — a mechanism "
                    "line must carry the record's **可证伪条件**, the test that would refute it"
                )
            grade = item.get("evidence")
            if grade and str(grade).strip().upper()[:1] not in ("A", "B", "C"):
                failures.append(
                    f"stack[{index}] has evidence {grade!r} — must be an A/B/C grade"
                )

        # Grade the DESIGN here rather than through `notes`. `notes` records routing, so a
        # design obligation asserted there degenerates into vocabulary matching; the stack is
        # the channel that actually carries which mechanisms were chosen.
        cited = [str(item.get("id", "")).strip() for item in stack if isinstance(item, dict)]
        # Deliberately NOT a list of mechanisms the answer must contain. Which mechanisms
        # suit a flow is design judgment, and a whitelist here would fail a defensible answer
        # for choosing SD-04 over SD-03 — the vocabulary trap relocated into a new channel.
        # What IS contract: a visible stack must exist and be coherent with `full_scan`.
        if data.get("visible_stack") is True and not cited:
            failures.append(
                "visible_stack is true but the stack is empty — the stack is the design"
            )
        # NOT a coherence rule: `stack` records the mechanisms the answer USED, while
        # `visible_stack` says whether the user is shown them. A T1 or /stealth answer
        # applies levers silently — an earlier version of this check failed exactly that
        # correct behaviour by treating the two as one field. Only a refusal has no design,
        # and `expected_stack_empty` grades that.
        # A refusal has no design to show; a redirect does. This is the one place the
        # refuse/redirect distinction becomes mechanically testable, because the two branches
        # differ in whether an artifact exists to build.
        expected_empty = vars_dict.get("expected_stack_empty")
        if expected_empty is not None:
            want_empty = str(expected_empty).strip().lower() == "true"
            if want_empty and cited:
                failures.append(
                    f"stack must be empty for a refusal, got {sorted(set(cited))}"
                )
            if not want_empty and not cited:
                failures.append("stack must not be empty for an allowed or redirected request")
        # A cited mechanism ID must name a record that exists. SKILL.md's first output
        # principle is "map it to a concrete mechanism by ID, from a file that exists", and
        # real runs invented LT-01 / TA-03 / DP-01 / CP-03 — playbook abbreviations dressed
        # as mechanism IDs. An invented ID carries an evidence grade and a stop signal, so it
        # reads exactly like a grounded citation while pointing at nothing.
        unknown_ids = [mid for mid in cited if mid and mid not in _known_ids()]
        if unknown_ids:
            failures.append(
                f"stack cites mechanism IDs that do not exist: {sorted(set(unknown_ids))} — "
                "ids must come from a record file, and a COMBO must be prefixed COMBO-"
            )

        # One mechanism is one line. Citing two members of a declared same-mechanism group
        # counts one lever twice and borrows the higher grade from whichever member states
        # it better; the registry in references/_schema.md names the member to cite.
        for group in _same_mechanism_groups():
            hit = [mid for mid in group["members"] if mid in cited]
            if len(hit) > 1 and group["cite"] in hit:
                failures.append(
                    f"stack cites {hit} — these are one lever (same-mechanism group in "
                    f"references/_schema.md); cite {group['cite']} once"
                )

    # Every cited path must exist. A model that invents `references/fake-urgency.md` is
    # not "close enough" — it is reporting evidence it never read, and the SKILL.md
    # contract says every reference must be a file that exists. Without this check the
    # eval happily passes output citing files that were never written.
    if isinstance(references, list):
        invented = [
            ref for ref in references
            if isinstance(ref, str) and ref.strip() and not (ROOT / ref).exists()
        ]
        if invented:
            failures.append(f"references cite paths that do not exist: {invented!r}")
    if not isinstance(references, list) or not all(isinstance(item, str) for item in references):
        failures.append("references must be a list of strings")
    if not isinstance(notes, list) or not all(isinstance(item, str) for item in notes):
        failures.append("notes must be a list of strings")
    # `notes` is a reporting channel for the harness — it is not part of SKILL.md's contract
    # at all. The bound exists to catch runaway output, not to grade the design, so it is
    # deliberately loose: a run that writes six accurate short notes has not violated
    # anything the skill promises, and failing it here would report a skill defect that does
    # not exist (this happened: a substantively perfect combo answer failed on item count).
    if isinstance(notes, list) and not (1 <= len(notes) <= 8):
        failures.append("notes must contain 1-8 items")

    expected_references = vars_dict.get("expected_references")
    if expected_references is not None:
        # Cases declare this as a `;`-separated STRING, not a YAML list. promptfoo turns
        # every list-valued var into a Cartesian product of separate runs, so a list here
        # silently multiplied one case into N runs that each checked one reference — the
        # headline "50/50" was 50 rows over 18 cases. A scalar keeps one case = one run.
        # Within one `;`-slot, `|` separates acceptable alternatives: where two files are
        # both defensible routes under SKILL.md, the test must accept either, or it grades
        # a preference the contract never fixed.
        if isinstance(expected_references, str):
            slots = [s.strip() for s in expected_references.split(";") if s.strip()]
        else:
            slots = [str(s) for s in expected_references]
        missing_refs = [
            slot for slot in slots
            if not any(alt.strip() in references for alt in slot.split("|"))
        ]
        if missing_refs:
            failures.append(
                f"references: expected {slots!r}, got {references!r}"
            )

    expected_note_keywords = vars_dict.get("expected_note_keywords")
    if expected_note_keywords is not None:
        # Also a `;`-separated scalar for the same expansion reason as references.
        # Within one phrase, `a|b` means either alternative satisfies it: the contract
        # fixes the DECISION, so the test must not grade the model's vocabulary.
        if isinstance(expected_note_keywords, str):
            phrases = [p.strip() for p in expected_note_keywords.split(";") if p.strip()]
        else:
            phrases = list(expected_note_keywords)
        notes_blob = _normalize_text_list(notes)
        missing_keywords = [
            phrase for phrase in phrases
            if not any(
                all(word in notes_blob for word in alternative.lower().split())
                for alternative in phrase.split("|")
            )
        ]
        if missing_keywords:
            failures.append(
                f"notes missing keywords: {missing_keywords!r}"
            )

    passed = not failures
    return {
        "pass": passed,
        "score": 1.0 if passed else 0.0,
        "reason": "decision contract matched" if passed else "; ".join(failures),
    }
