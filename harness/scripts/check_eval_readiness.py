#!/usr/bin/env python3

from pathlib import Path
import os
import sys


ROOT = Path(__file__).resolve().parents[2]
HARNESS = ROOT / "harness"


def main() -> int:
    files = [
        HARNESS / "promptfooconfig.openai.yaml",
        HARNESS / "promptfooconfig.anthropic.yaml",
        HARNESS / "scripts" / "run_eval.py",
    ]
    missing = [str(path.relative_to(ROOT)) for path in files if not path.exists()]
    if missing:
        print("EVAL READINESS FAILED")
        for item in missing:
            print(f"- missing file: {item}")
        return 1

    print("Eval configs:")
    print(f"  OpenAI key present: {'yes' if bool(os.environ.get('OPENAI_API_KEY')) else 'no'}")
    print(f"  Anthropic key present: {'yes' if bool(os.environ.get('ANTHROPIC_API_KEY')) else 'no'}")
    print("Suggested commands:")
    print("  python3 harness/scripts/run_eval.py openai")
    print("  python3 harness/scripts/run_eval.py anthropic")
    print("  python3 harness/scripts/run_eval.py openai mode stealth")
    print("  python3 harness/scripts/run_eval.py anthropic safety refuse")
    print("EVAL READINESS OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
