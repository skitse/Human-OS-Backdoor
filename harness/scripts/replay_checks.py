#!/usr/bin/env python3

import json
from pathlib import Path

import yaml

from assertions import decision_contract_assert


ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "harness" / "tests" / "cases.yaml"
FIXTURES_PATH = ROOT / "harness" / "fixtures" / "replay_outputs.json"


def main() -> int:
    cases = yaml.safe_load(CASES_PATH.read_text())
    fixtures = json.loads(FIXTURES_PATH.read_text())

    failures = []

    for case in cases:
        description = case["description"]
        fixture = fixtures.get(description)
        if fixture is None:
            failures.append(f"missing fixture for case: {description}")
            continue

        result = decision_contract_assert(
            json.dumps(fixture),
            {"vars": case["vars"]},
        )

        if not result["pass"]:
            failures.append(f"{description}: {result['reason']}")

    if failures:
        print("REPLAY CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"REPLAY CHECK OK ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
