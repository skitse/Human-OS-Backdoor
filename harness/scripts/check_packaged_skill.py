#!/usr/bin/env python3

from pathlib import Path
import filecmp
import sys


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "skills" / "human-os"


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

    if not PACKAGE.exists():
        failures.append("missing packaged skill directory: skills/human-os")
    else:
        for rel in REQUIRED_PATHS:
            if not (PACKAGE / rel).exists():
                failures.append(f"missing packaged file: skills/human-os/{rel}")

    if PACKAGE.exists():
        root_skill = ROOT / "SKILL.md"
        packaged_skill = PACKAGE / "SKILL.md"
        if packaged_skill.exists() and root_skill.read_text() != packaged_skill.read_text():
            failures.append("packaged SKILL.md differs from root SKILL.md")

        root_refs = ROOT / "references"
        packaged_refs = PACKAGE / "references"
        if packaged_refs.exists():
            diff = [
                item
                for item in filecmp.dircmp(root_refs, packaged_refs).left_only
                if not item.startswith(".")
            ]
            if diff:
                failures.append(
                    f"packaged references missing top-level entries from root references: {sorted(diff)}"
                )

    if failures:
        print("PACKAGED SKILL CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PACKAGED SKILL CHECK OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
