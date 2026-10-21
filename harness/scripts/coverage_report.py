#!/usr/bin/env python3

from collections import Counter
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "harness" / "tests" / "cases.yaml"

REQUIRED_CATEGORIES = {"trigger", "effort", "routing", "mode", "safety"}
REQUIRED_TIERS = {"T0", "T1", "T2", "T3"}
REQUIRED_MODES = {"adaptive", "stealth", "scan", "deep", "combo", "defend"}
REQUIRED_SAFETY = {"allow", "redirect", "refuse"}


def _collect_values(cases, key):
    values = []
    for case in cases:
        metadata = case.get("metadata", {})
        value = metadata.get(key)
        if value is not None:
            values.append(value)
    return values


def _report_counter(name, values):
    counter = Counter(values)
    print(f"{name}:")
    for key in sorted(counter):
        print(f"  {key}: {counter[key]}")
    return counter


def main() -> int:
    cases = yaml.safe_load(CASES_PATH.read_text())

    categories = _collect_values(cases, "category")
    tiers = _collect_values(cases, "tier")
    modes = _collect_values(cases, "mode")
    safety_actions = _collect_values(cases, "safety")

    category_counter = _report_counter("Categories", categories)
    tier_counter = _report_counter("Tiers", tiers)
    mode_counter = _report_counter("Modes", modes)
    safety_counter = _report_counter("Safety", safety_actions)

    failures = []

    missing_categories = REQUIRED_CATEGORIES - set(category_counter)
    missing_tiers = REQUIRED_TIERS - set(tier_counter)
    missing_modes = REQUIRED_MODES - set(mode_counter)
    missing_safety = REQUIRED_SAFETY - set(safety_counter)

    if missing_categories:
        failures.append(f"missing categories: {sorted(missing_categories)}")
    if missing_tiers:
        failures.append(f"missing tiers: {sorted(missing_tiers)}")
    if missing_modes:
        failures.append(f"missing modes: {sorted(missing_modes)}")
    if missing_safety:
        failures.append(f"missing safety actions: {sorted(missing_safety)}")

    # cases.yaml's own header says `metadata` must agree with `vars`, because when the two
    # disagree the file documents two contracts for the same case. A rule stated only in a
    # comment is not a rule: nothing verified it until this check existed.
    mismatches = []
    for case in cases:
        metadata = case.get("metadata", {})
        case_vars = case.get("vars", {})
        for meta_key, var_key in (
            ("tier", "expected_tier"),
            ("mode", "expected_mode"),
            ("safety", "expected_safety_action"),
        ):
            if meta_key not in metadata or var_key not in case_vars:
                continue
            # A `|` in vars means the case accepts several answers; metadata names one of
            # them, which is consistent, not contradictory.
            accepted = [a.strip() for a in str(case_vars[var_key]).split("|")]
            if str(metadata[meta_key]) not in accepted:
                mismatches.append(
                    f"{case.get('description')}: metadata.{meta_key}="
                    f"{metadata[meta_key]!r} but vars.{var_key}="
                    f"{case_vars[var_key]!r}"
                )
    if mismatches:
        failures.append("metadata disagrees with vars:")
        failures.extend(f"  {m}" for m in mismatches)

    if failures:
        print("COVERAGE REPORT FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"COVERAGE REPORT OK ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
