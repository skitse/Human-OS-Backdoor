#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]

COMMANDS = [
    ["python3", "harness/scripts/static_checks.py"],
    ["python3", "harness/scripts/check_packaged_skill.py"],
    ["python3", "harness/scripts/replay_checks.py"],
    ["python3", "harness/scripts/coverage_report.py"],
    ["python3", "harness/scripts/check_eval_readiness.py"],
]


def main() -> int:
    for command in COMMANDS:
        print(f"$ {' '.join(command)}")
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode != 0:
            print(f"FAILED: {' '.join(command)}")
            return result.returncode

    print("ALL HARNESS CHECKS OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
