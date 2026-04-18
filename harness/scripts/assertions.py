import json


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


def decision_contract_assert(output: str, context: dict) -> dict:
    vars_dict = context.get("vars", {})
    try:
        data = json.loads(output)
    except json.JSONDecodeError as exc:
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
        if data.get(key) != expected:
            failures.append(f"{key}: expected {expected!r}, got {data.get(key)!r}")

    references = data.get("references", [])
    notes = data.get("notes", [])
    if not isinstance(references, list) or not all(isinstance(item, str) for item in references):
        failures.append("references must be a list of strings")
    if not isinstance(notes, list) or not all(isinstance(item, str) for item in notes):
        failures.append("notes must be a list of strings")
    if isinstance(notes, list) and not (1 <= len(notes) <= 5):
        failures.append("notes must contain 1-5 items")

    expected_references = vars_dict.get("expected_references")
    if expected_references is not None and references != expected_references:
        failures.append(
            f"references: expected {expected_references!r}, got {references!r}"
        )

    expected_note_keywords = vars_dict.get("expected_note_keywords")
    if expected_note_keywords is not None:
        notes_blob = _normalize_text_list(notes)
        missing_keywords = [
            keyword for keyword in expected_note_keywords
            if keyword.lower() not in notes_blob
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
