#!/usr/bin/env python3

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_PATHS = [
    "SKILL.md",
    "references/anti-patterns.md",
    "references/combo-patterns.md",
    "references/model-index.md",
    "references/scan-protocol.md",
    "references/_build-status.md",
    "references/models/affective-dynamics.md",
    "references/models/attention-economics.md",
    "references/models/cognitive-architecture.md",
    "references/models/heuristics-biases.md",
    "references/models/motivation-regulation.md",
    "references/models/perception-attention.md",
    "references/models/pricing-economic-decisions.md",
    "references/models/social-dynamics.md",
    "references/models/trust-architecture.md",
    "references/domain-playbooks/behavioral-finance.md",
    "references/domain-playbooks/community-social.md",
    "references/domain-playbooks/content-hooks.md",
    "references/domain-playbooks/cultural-psychology.md",
    "references/domain-playbooks/dark-patterns.md",
    "references/domain-playbooks/games-gamification.md",
    "references/domain-playbooks/interpersonal-persuasion.md",
    "references/domain-playbooks/linguistic-triggers.md",
    "references/domain-playbooks/meme-engineering.md",
    "references/domain-playbooks/saas-products.md",
    "references/domain-playbooks/sales-psychology.md",
    "references/domain-playbooks/social-commerce.md",
    "references/domain-playbooks/video-content-psychology.md",
    "references/domain-playbooks/viral-growth-loops.md",
    "references/dialogues/neuroscience-x-growth-debate.md",
    "references/dialogues/sales-x-narrative-debate.md",
]


def main() -> int:
    failures = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            failures.append(f"missing required file: {rel}")

    if failures:
        print("PACKAGED SKILL CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PACKAGED SKILL CHECK OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
