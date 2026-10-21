#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]

COMMANDS = [
    ["python3", "harness/scripts/check_consistency.py"],
    ["python3", "harness/scripts/static_checks.py"],
    ["python3", "harness/scripts/check_packaged_skill.py"],
    ["python3", "harness/scripts/replay_checks.py"],
    ["python3", "harness/scripts/coverage_report.py"],
    ["python3", "harness/scripts/check_eval_readiness.py"],
]


# Every gate must print at least one of these, or it is not a gate. This guard exists
# because `replay_checks.py` once shipped without its `main()`: the file ran, printed
# nothing, exited 0, and this runner reported ALL HARNESS CHECKS OK. A gate that exits 0
# without saying anything is indistinguishable from a gate that passed, so it is not
# enough for a check to run — it has to answer.
MUST_ANNOUNCE = ("OK", "FAILED", "PASS", "found", "scanned", "note:")


def main() -> int:
    silent: list[str] = []
    for command in COMMANDS:
        name = " ".join(command)
        print(f"$ {name}")
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
        if result.stderr:
            print(result.stderr, end="" if result.stderr.endswith("\n") else "\n")
        if result.returncode != 0:
            print(f"FAILED: {name}")
            return result.returncode
        if not any(marker in result.stdout for marker in MUST_ANNOUNCE):
            silent.append(name)

    if silent:
        print("HARNESS CHECK HAS NO RESULT TO REPORT")
        for name in silent:
            print(f"- {name} exited 0 but printed no verdict — it may not be running at all")
        return 1

    print("ALL HARNESS CHECKS OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
