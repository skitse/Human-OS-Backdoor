import json
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


def _parse_json(output: str):
    """Parse first complete JSON object, ignoring any surrounding text (thinking-mode models)."""
    start = output.find("{")
    if start == -1:
        raise json.JSONDecodeError("no JSON object found", output, 0)
    obj, _ = json.JSONDecoder().raw_decode(output, start)
    return obj


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
    notes = data.get("notes", [])

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
    if isinstance(notes, list) and not (1 <= len(notes) <= 5):
        failures.append("notes must contain 1-5 items")

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
