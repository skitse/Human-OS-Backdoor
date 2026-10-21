#!/usr/bin/env python3
"""Regenerate harness/fixtures/replay_outputs.json from a REAL recorded eval.

Why this script exists
----------------------
The fixtures used to be hand-written examples that only ever showed the passing shape.
They were also frozen at the init commit while `cases.yaml` kept being recalibrated, so
the replay gate was permanently red at HEAD and nobody noticed, because a suite made
entirely of positive examples cannot tell "the contract is satisfied" from "the
assertions always pass".

This script copies model output verbatim out of a promptfoo eval export. The fixtures are
therefore evidence of what a model actually did, not a restatement of what we hoped.

Usage
-----
    python3 harness/scripts/build_replay_fixtures.py [EVAL_JSON]

Default EVAL_JSON is results/human-os-eval-openrouter.json. For each case description it
takes the LAST run recorded for that case (most recent sample of the same prompt) and
writes the parsed JSON contract object. Cases with no recorded run are an error, not a
silent omission — a missing fixture must be loud.
"""

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "harness" / "tests" / "cases.yaml"
FIXTURES_PATH = ROOT / "harness" / "fixtures" / "replay_outputs.json"
DEFAULT_EVAL = ROOT / "results" / "human-os-eval-openrouter.json"

CONTRACT_KEYS = (
    "trigger",
    "tier",
    "mode",
    "safety_action",
    "visible_stack",
    "full_scan",
    "references",
    "stack",
    "notes",
)


def extract_contract(raw: str) -> dict:
    """Pull the contract JSON object out of a model response (tolerates prose preamble).

    Identified by its key set rather than by "the first `{`": a thinking-mode model sketches
    JSON fragments while deliberating, and one real run's reasoning contained
    ``{"id": "LT-01", ...}`` thousands of characters before the answer. Taking the first
    object froze that fragment as the fixture — a fixture that then asserts nothing about
    the contract, since none of the contract keys are in it.
    """
    decoder = json.JSONDecoder()
    best = None
    index = raw.find("{")
    while index != -1:
        try:
            obj, _ = decoder.raw_decode(raw, index)
        except json.JSONDecodeError:
            index = raw.find("{", index + 1)
            continue
        if isinstance(obj, dict):
            if all(key in obj for key in CONTRACT_KEYS):
                return obj
            if best is None or len(obj) > len(best):
                best = obj
        index = raw.find("{", index + 1)
    if best is None:
        raise ValueError("no JSON object in model output")
    return best


def response_text(run: dict) -> str:
    """promptfoo stores either a raw string or {output: str} depending on version."""
    resp = run.get("response")
    if isinstance(resp, dict):
        return resp.get("output", "")
    return resp or ""


def main() -> int:
    eval_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVAL
    if not eval_path.exists():
        print(f"BUILD FIXTURES FAILED: eval file not found: {eval_path}")
        return 1

    cases = yaml.safe_load(CASES_PATH.read_text())
    payload = json.loads(eval_path.read_text())
    runs = payload["results"]["results"]

    # Last run per case wins: later runs of the same prompt are the fresher sample.
    latest: dict[str, dict] = {}
    for run in runs:
        latest[run["testCase"]["description"]] = run

    fixtures: dict[str, dict] = {}
    problems: list[str] = []

    for case in cases:
        description = case["description"]
        run = latest.get(description)
        if run is None:
            problems.append(f"no recorded run for case: {description}")
            continue
        try:
            contract = extract_contract(response_text(run))
        except ValueError as exc:
            problems.append(f"{description}: {exc}")
            continue
        missing = [k for k in CONTRACT_KEYS if k not in contract]
        if missing:
            problems.append(f"{description}: recorded output lacks {missing}")
            continue
        fixtures[description] = {k: contract[k] for k in CONTRACT_KEYS}

    if problems:
        print("BUILD FIXTURES FAILED")
        for problem in problems:
            print(f"- {problem}")
        return 1

    FIXTURES_PATH.parent.mkdir(parents=True, exist_ok=True)
    FIXTURES_PATH.write_text(
        json.dumps(fixtures, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    )

    source = payload["metadata"].get("evaluationCreatedAt", "unknown")
    print(
        f"BUILD FIXTURES OK — {len(fixtures)} fixtures from {eval_path.name} "
        f"(eval created {source})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
