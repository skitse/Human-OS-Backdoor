#!/usr/bin/env python3
"""Mirror this checkout into the installed skill copy that agents actually load.

`.agents/skills/human-os/` is gitignored and refreshed by an external install step, so it
drifts silently: new reference files never arrive and edited files keep their old text,
while every other check passes because they all read the repo. This script is the remedy
half of that pair — `check_packaged_skill.py` detects the drift and fails, this makes the
copy match again.

    python3 harness/scripts/sync_installed_skill.py --dry-run   # show the plan
    python3 harness/scripts/sync_installed_skill.py             # apply

Mirroring is exact: missing files are copied, changed files are overwritten, and files the
repo no longer has are pruned (pass --no-prune to keep them). `.DS_Store` and __pycache__
are neither copied nor pruned.
"""

from pathlib import Path
import argparse
import hashlib
import shutil
import sys


ROOT = Path(__file__).resolve().parents[2]
INSTALLED_COPY = ROOT / ".agents" / "skills" / "human-os"
PARITY_DIRS = ["references"]
IGNORED_NAMES = {".DS_Store", "__pycache__"}
IGNORED_SUFFIXES = {".pyc"}


def is_skill_file(path: Path) -> bool:
    if path.name in IGNORED_NAMES or path.suffix in IGNORED_SUFFIXES:
        return False
    return not any(part in IGNORED_NAMES for part in path.parts)


def skill_files(base: Path) -> set[str]:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="show the plan, change nothing")
    parser.add_argument("--no-prune", action="store_true", help="keep files the repo no longer has")
    args = parser.parse_args()

    if not ROOT.joinpath("SKILL.md").is_file():
        print(f"SYNC FAILED: no SKILL.md at {ROOT}", file=sys.stderr)
        return 1

    repo_set = skill_files(ROOT)
    copy_set = skill_files(INSTALLED_COPY) if INSTALLED_COPY.is_dir() else set()

    to_add = sorted(repo_set - copy_set)
    to_update = sorted(
        rel for rel in (repo_set & copy_set) if sha256(ROOT / rel) != sha256(INSTALLED_COPY / rel)
    )
    to_prune = [] if args.no_prune else sorted(copy_set - repo_set)

    verb = "would" if args.dry_run else ""
    for rel in to_add:
        print(f"  + {rel}")
    for rel in to_update:
        print(f"  ~ {rel}")
    for rel in to_prune:
        print(f"  - {rel}")

    if not (to_add or to_update or to_prune):
        print(f"installed copy already matches repo ({len(repo_set)} files) — nothing to do")
        return 0

    action = "planned" if args.dry_run else "applied"
    print(
        f"\n{len(to_add)} added, {len(to_update)} updated, {len(to_prune)} pruned "
        f"({action}) -> {INSTALLED_COPY}"
    )

    if args.dry_run:
        return 0

    for rel in to_add + to_update:
        dest = INSTALLED_COPY / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dest)
    for rel in to_prune:
        (INSTALLED_COPY / rel).unlink()

    # Drop directories emptied by pruning, deepest first, so the copy keeps no dead limbs.
    for path in sorted(INSTALLED_COPY.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()

    print("SYNC OK — installed copy now matches this checkout")
    return 0


if __name__ == "__main__":
    sys.exit(main())
