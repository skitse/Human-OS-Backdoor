#!/usr/bin/env python3

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "SKILL.md"

REQUIRED_SECTIONS = [
    "## Activation Gate",
    "## Task Tiers",
    "## Effort Policy",
    "## Mode Contract",
    "## Safety Gate",
    "## Reference Routing",
]

FORBIDDEN_PHRASES = [
    "ANY task involving human interaction",
    "You don't need to ask — it happens automatically.",
    "Leverage Score = Effect Size × Conf × Domain Fit × Implementation Ease",
]

REQUIRED_FILES = [
    ROOT / "harness" / "promptfooconfig.openai.yaml",
    ROOT / "harness" / "promptfooconfig.anthropic.yaml",
    ROOT / "harness" / "promptfooconfig.yaml",
    ROOT / "harness" / "promptfooconfig.smoke.yaml",
    ROOT / "harness" / "fixtures" / "replay_outputs.json",
    ROOT / "harness" / "prompts" / "system.md",
    ROOT / "harness" / "tests" / "cases.yaml",
    ROOT / "harness" / "tests" / "smoke-cases.yaml",
    ROOT / "harness" / "scripts" / "assertions.py",
    ROOT / "harness" / "scripts" / "check_eval_readiness.py",
    ROOT / "harness" / "scripts" / "check_packaged_skill.py",
    ROOT / "harness" / "scripts" / "coverage_report.py",
    ROOT / "harness" / "scripts" / "replay_checks.py",
    ROOT / "harness" / "scripts" / "run_all_checks.py",
    ROOT / "harness" / "scripts" / "run_eval.py",
    ROOT / "references" / "domain-playbooks" / "linguistic-triggers.md",
    ROOT / "references" / "domain-playbooks" / "cultural-psychology.md",
    ROOT / "references" / "domain-playbooks" / "dark-patterns.md",
    ROOT / "references" / "dialogues" / "sales-x-narrative-debate.md",
    ROOT / "references" / "models" / "attention-economics.md",
    ROOT / "references" / "models" / "trust-architecture.md",
]


def main() -> int:
    text = SKILL.read_text()
    failures = []

    if len(text.splitlines()) > 500:
        failures.append("SKILL.md exceeds 500 lines")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"missing section: {section}")

    for phrase in FORBIDDEN_PHRASES:
        if phrase in text:
            failures.append(f"forbidden phrase still present: {phrase}")

    frontmatter_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not frontmatter_match:
        failures.append("missing YAML frontmatter")

    for path in REQUIRED_FILES:
        if not path.exists():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")

    if failures:
        print("STATIC CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("STATIC CHECK OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
