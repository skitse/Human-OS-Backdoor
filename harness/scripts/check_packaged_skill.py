#!/usr/bin/env python3
"""Verify the skill is complete AND that the installed copy matches this checkout.

Two distinct failures this guards against:

1. The repo is missing a file the skill needs at runtime.
2. The repo is fine, but `.agents/skills/human-os/` — the copy an agent actually loads —
   is stale. That copy is gitignored and is refreshed by an external install step, so it
   silently drifts: new reference files never arrive, edited files keep their old text, and
   every other check still passes because they all read the repo.

Failure 2 is the dangerous one: the skill looks healthy in CI and is wrong in the session
where it is used. So a present copy must match the repo byte for byte; an absent copy is
fine (fresh clone, CI) and only prints a note.
"""

from pathlib import Path
import hashlib
import sys


ROOT = Path(__file__).resolve().parents[2]
INSTALLED_COPY = ROOT / ".agents" / "skills" / "human-os"

REQUIRED_PATHS = [
    "SKILL.md",
    "references/_schema.md",
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
    "references/refused-domains/manufactured-urgency.md",
    "references/refused-domains/compulsion-loops.md",
    "references/refused-domains/narrative-control.md",
    "references/refused-domains/stakeholder-pressure.md",
]

# Directories swept for parity. Anything a runtime read can reach must be listed here,
# or drift in it goes unnoticed.
PARITY_DIRS = ["references"]
IGNORED_NAMES = {".DS_Store", "__pycache__"}
IGNORED_SUFFIXES = {".pyc"}


def is_skill_file(path: Path) -> bool:
    if path.name in IGNORED_NAMES or path.suffix in IGNORED_SUFFIXES:
        return False
    return not any(part in IGNORED_NAMES for part in path.parts)


def skill_files(base: Path) -> set[str]:
    """Every shippable file of the skill, relative to its own root."""
    found = set()
    for name in ["SKILL.md"] + PARITY_DIRS:
        target = base / name
        if target.is_file():
            found.add(name)
        elif target.is_dir():
            for path in target.rglob("*"):
                if path.is_file() and is_skill_file(path):
                    found.add(str(path.relative_to(base)))
    return found


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_installed_copy(failures: list[str]) -> list[str]:
    """Return notes describing copy state; append real drift to failures."""
    if not INSTALLED_COPY.is_dir():
        return [f"no installed copy at {INSTALLED_COPY.relative_to(ROOT)} — parity not checked"]

    notes = []
    repo_set = skill_files(ROOT)
    copy_set = skill_files(INSTALLED_COPY)

    missing = sorted(repo_set - copy_set)
    orphan = sorted(copy_set - repo_set)
    for rel in missing:
        failures.append(f"installed copy is missing: {rel}")
    for rel in orphan:
        failures.append(f"installed copy has a file the repo does not: {rel}")

    changed = []
    for rel in sorted(repo_set & copy_set):
        if sha256(ROOT / rel) != sha256(INSTALLED_COPY / rel):
            changed.append(rel)
    for rel in changed:
        failures.append(f"installed copy is stale: {rel}")

    if not (missing or orphan or changed):
        notes.append(f"installed copy matches repo ({len(repo_set)} files)")
    else:
        notes.append(
            "installed copy has drifted — re-install/re-sync the skill so agents load "
            "the current text (the copy is gitignored and will not update by itself)"
        )
    return notes


def main() -> int:
    failures = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            failures.append(f"missing required file: {rel}")

    # Only meaningful once the repo itself is complete; otherwise the parity report is
    # just a restatement of the same gap.
    if not failures:
        for note in check_installed_copy(failures):
            print(f"note: {note}")
    else:
        print("note: skipping installed-copy parity (repo is incomplete)")

    if failures:
        print("PACKAGED SKILL CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PACKAGED SKILL CHECK OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
