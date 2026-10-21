#!/usr/bin/env python3
"""Replay the recorded model outputs against the assertion layer.

Two things this gate must do, because doing only the first is how this repo shipped a
replay suite that could not fail:

1. REPLAY — every fixture must satisfy its case. Fixtures are generated from a real eval
   export by `build_replay_fixtures.py`, never hand-written.

2. SELF-TEST — for every case, mutate the fixture in ways that VIOLATE the contract and
   assert the assertion layer rejects each mutation. A positive-only suite cannot tell
   "the contract is satisfied" from "the assertions always pass"; the self-test is what
   makes the green replay result meaningful. If a mutation ever passes, the assertion
   layer has a hole and this gate goes red on purpose.

Run: python3 harness/scripts/replay_checks.py
"""

import copy
import re
from functools import lru_cache
import json
from pathlib import Path

import yaml

from assertions import decision_contract_assert


ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "harness" / "tests" / "cases.yaml"
FIXTURES_PATH = ROOT / "harness" / "fixtures" / "replay_outputs.json"


@lru_cache(maxsize=1)
def _same_mechanism_groups() -> tuple[dict, ...]:
    """Read the same-mechanism groups from references/_schema.md (see assertions.py)."""
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
            groups.append({
                "members": [m.strip() for m in re.split(r"[+·]", match.group(1)) if m.strip()],
                "cite": match.group(2).strip(),
            })
    return tuple(groups)


def mutations_for(fixture: dict, vars_dict: dict) -> list[tuple[str, dict]]:
    """Contract violations derived from the fixture, limited to fields the case pins.

    A mutation is only a violation if the case actually asserts that field. Three cases
    legitimately expect NO references (`expected_references: ""`), so emptying their
    references list is legal output — demanding a rejection there would be the self-test
    inventing a rule the contract does not have. Gate each mutation on the case's own
    expectation, never on the field merely existing in the fixture.
    """
    out: list[tuple[str, dict]] = []

    def mutate(label: str, **changes):
        broken = copy.deepcopy(fixture)
        broken.update(changes)
        out.append((label, broken))

    if "expected_trigger" in vars_dict:
        mutate("trigger flipped", trigger=not fixture.get("trigger"))
    if "expected_tier" in vars_dict:
        mutate("tier wrong", tier="T0" if fixture.get("tier") != "T0" else "T3")
    if "expected_mode" in vars_dict:
        mutate(
            "mode wrong",
            mode="stealth" if fixture.get("mode") != "stealth" else "combo",
        )
    if "expected_safety_action" in vars_dict:
        mutate(
            "safety_action wrong",
            safety_action="allow" if fixture.get("safety_action") != "allow" else "refuse",
        )
    if "expected_visible_stack" in vars_dict:
        mutate("visible_stack flipped", visible_stack=not fixture.get("visible_stack"))
    if "expected_full_scan" in vars_dict:
        mutate("full_scan flipped", full_scan=not fixture.get("full_scan"))
    # Only when the case demands at least one reference.
    if str(vars_dict.get("expected_references", "")).strip():
        mutate("references emptied", references=[])
    # notes must always be 1-5 items, so this is a violation for every case.
    mutate("notes emptied", notes=[])
    # Keyword coverage needs its OWN mutation. Emptying notes trips the 1-5 length rule
    # first, so the keyword check never runs and a broken keyword check would go unseen.
    # A valid-length note that carries none of the expected vocabulary isolates it.
    if str(vars_dict.get("expected_note_keywords", "")).strip():
        mutate("notes valid but off-vocabulary", notes=["Okay."])

    # The stack assertions are new, so the self-test must prove they can reject. Without
    # these mutations a broken stack check would pass every fixture that happens to omit it.
    stack = fixture.get("stack")
    if isinstance(stack, list) and stack:
        # Only a VISIBLE stack must be non-empty. Where `visible_stack` is false the stack
        # is the answer's private bookkeeping and emptying it changes nothing the contract
        # grades — asserting a rejection there would be the self-test inventing a rule.
        if fixture.get("visible_stack") is True:
            mutate("stack emptied while visible", stack=[])
        broken = copy.deepcopy(fixture)
        first = broken["stack"][0]
        first.pop("stop", None)
        out.append(("stack line loses its stop signal", broken))
        broken2 = copy.deepcopy(fixture)
        broken2["stack"][0]["evidence"] = "high"
        out.append(("stack line carries a non-grade evidence value", broken2))
        # A stack line with no falsifier is the shape the v2 upgrade exists to eliminate.
        broken4 = copy.deepcopy(fixture)
        broken4["stack"][0].pop("falsified_by", None)
        out.append(("stack line loses its falsification condition", broken4))
        # Double-counting a same-mechanism group: append the group's other member.
        for group in _same_mechanism_groups():
            cited = [str(item.get("id", "")).strip() for item in stack if isinstance(item, dict)]
            if group["cite"] in cited:
                other = [m for m in group["members"] if m != group["cite"]]
                if other:
                    broken3 = copy.deepcopy(fixture)
                    broken3["stack"] = broken3["stack"] + [
                        {"id": other[0], "dose": "中", "evidence": "B", "stop": "x"}
                    ]
                    out.append(("stack counts one lever twice", broken3))
                break

    return out


def main() -> int:
    cases = yaml.safe_load(CASES_PATH.read_text())
    fixtures = json.loads(FIXTURES_PATH.read_text())

    failures: list[str] = []

    # ---- 1. REPLAY ---------------------------------------------------------------
    for case in cases:
        description = case["description"]
        fixture = fixtures.get(description)
        if fixture is None:
            failures.append(f"missing fixture for case: {description}")
            continue
        result = decision_contract_assert(json.dumps(fixture), {"vars": case["vars"]})
        if not result["pass"]:
            failures.append(f"REPLAY {description}: {result['reason']}")

    # ---- 2. SELF-TEST ------------------------------------------------------------
    # A mutation is only meaningful when the case pins that field. Otherwise the
    # mutation is legal output and demanding a rejection would be wrong.
    checked = 0
    for case in cases:
        description = case["description"]
        fixture = fixtures.get(description)
        if fixture is None:
            continue
        for label, broken in mutations_for(fixture, case["vars"]):
            result = decision_contract_assert(json.dumps(broken), {"vars": case["vars"]})
            if result["pass"]:
                failures.append(
                    f"SELF-TEST HOLE {description}: {label} was accepted — "
                    f"the assertion layer does not check this field"
                )
            else:
                checked += 1

    if failures:
        print("REPLAY CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"REPLAY CHECK OK ({len(cases)} cases replayed; "
        f"{checked} contract violations correctly rejected)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
