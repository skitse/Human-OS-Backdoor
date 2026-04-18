#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import sys

import yaml

# Load .env if present (never required — env vars can also be set externally)
ROOT = Path(__file__).resolve().parents[2]
_env_file = ROOT / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())
HARNESS = ROOT / "harness"
CASES_PATH = HARNESS / "tests" / "cases.yaml"

CONFIGS = {
    "openai": HARNESS / "promptfooconfig.openai.yaml",
    "anthropic": HARNESS / "promptfooconfig.anthropic.yaml",
}

FILTER_KEYS = {"category", "tier", "mode", "safety"}
ENV_REQUIREMENTS = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
}


def load_cases():
    return yaml.safe_load(CASES_PATH.read_text())


def filter_cases(cases, filter_key=None, filter_value=None):
    if filter_key is None:
        return cases
    filtered = []
    for case in cases:
        metadata = case.get("metadata", {})
        if metadata.get(filter_key) == filter_value:
            filtered.append(case)
    return filtered


def write_temp_cases(cases):
    temp_path = HARNESS / "tests" / ".tmp-filtered-cases.yaml"
    temp_path.write_text(yaml.safe_dump(cases, sort_keys=False, allow_unicode=True))
    return temp_path


def main(argv):
    if len(argv) < 2 or argv[1] not in CONFIGS:
        print("Usage: python3 harness/scripts/run_eval.py <openai|anthropic> [filter_key] [filter_value]")
        print("filter_key must be one of: category, tier, mode, safety")
        return 1

    provider = argv[1]
    filter_key = argv[2] if len(argv) >= 4 else None
    filter_value = argv[3] if len(argv) >= 4 else None

    if filter_key is not None and filter_key not in FILTER_KEYS:
        print(f"Invalid filter_key: {filter_key}")
        return 1

    env_var = ENV_REQUIREMENTS[provider]
    if not os.environ.get(env_var):
        print(f"Missing required environment variable: {env_var}")
        return 1

    cases = load_cases()
    selected_cases = filter_cases(cases, filter_key, filter_value)
    if not selected_cases:
        print("No cases matched the requested filter")
        return 1

    temp_cases = write_temp_cases(selected_cases)
    config_path = CONFIGS[provider]

    command = [
        "npx",
        "promptfoo@latest",
        "eval",
        "--config",
        str(config_path),
        "--tests",
        str(temp_cases),
    ]

    try:
        return subprocess.run(command, cwd=ROOT).returncode
    finally:
        if temp_cases.exists():
            temp_cases.unlink()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
