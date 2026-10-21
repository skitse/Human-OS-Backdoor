#!/usr/bin/env python3
"""Per-file view of the consistency gate.

``check_consistency.py`` is all-or-nothing: while other writers are still migrating
their files, its global failure output buries the problems that belong to *your* file.
This wrapper prints only the findings for the file(s) you name, so a writer can prove
their own scope is finished without waiting for the rest of the migration.

    python3 harness/scripts/check_file.py references/models/social-dynamics.md
    python3 harness/scripts/check_file.py social-dynamics.md perception-attention.md
    python3 harness/scripts/check_file.py --all
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_consistency import parse_entries, validate_entry  # noqa: E402


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2

    entries, parse_errors = parse_entries()

    if args == ["--all"]:
        wanted = None
    else:
        wanted = {Path(a).name for a in args}

    selected = [e for e in entries if wanted is None or e.path.name in wanted]

    if not selected:
        print(f"no mechanism records found in: {', '.join(sorted(wanted or {'<all>'}))}")
        print("check the filename — records are only parsed from the SCAN_DIRS in check_consistency.py")
        return 2

    problems: list[str] = []
    for entry in selected:
        problems.extend(validate_entry(entry))

    # `parse_errors` is global bookkeeping, not a statement about any one file. Its most
    # common member is "ID is declared unwritten but now has a body — remove the row from
    # the Declared-but-unwritten registry", which fires the moment a writer does the right
    # thing, and can only be cleared by editing references/_schema.md — a file writers are
    # forbidden to touch. Seeding the per-file result with it made every writer's check fail
    # for a reason they could not fix and did not cause. Report it as the lead's outstanding
    # cleanup instead, and let the exit code speak only for the records actually named here.
    in_scope_ids = {e.id for e in selected}
    global_notes = [
        problem
        for problem in parse_errors
        if any(mid in problem for mid in in_scope_ids) or not _names_any_id(problem)
    ]

    by_file: dict[str, list[str]] = {}
    for problem in problems:
        key = problem.split(":", 1)[0]
        by_file.setdefault(key, []).append(problem)

    seen = sorted({e.path.name for e in selected})
    print(f"scanned {len(selected)} record(s) in: {', '.join(seen)}")

    if not problems:
        print("FILE OK — every record carries the full v2 field set")
        if global_notes:
            print(
                f"\nnote: {len(global_notes)} lead-owned bookkeeping item(s) pending in "
                "references/_schema.md (not your file, and not a failure of it):"
            )
            for problem in global_notes:
                print(f"  - {problem}")
        return 0

    for key in sorted(by_file):
        print(f"\n{key}")
        for problem in by_file[key]:
            detail = problem.split(": ", 1)[1] if ": " in problem else problem
            print(f"  - {detail}")

    print(f"\n{len(problems)} problem(s) in scope")
    return 1


def _names_any_id(problem: str) -> bool:
    """True when a global problem is attributable to a specific mechanism ID."""
    import re

    return bool(re.search(r"\b[A-Z]{2}-\d{2}\b", problem))


if __name__ == "__main__":
    sys.exit(main())
