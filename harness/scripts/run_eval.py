#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import sys

import yaml

# Load .env if present — .env always wins for config vars, shell wins for API keys.
ROOT = Path(__file__).resolve().parents[2]
_env_file = ROOT / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            key, value = key.strip(), value.strip()
            if not value or value.startswith("sk-ant-...") or value.startswith("sk-...") or value.startswith("sk-or-..."):
                continue
            if key.endswith("_API_KEY"):
                if not os.environ.get(key):
                    os.environ[key] = value
            else:
                os.environ[key] = value

HARNESS = ROOT / "harness"
CASES_PATH = HARNESS / "tests" / "cases.yaml"

CONFIGS = {
    "openai":      HARNESS / "promptfooconfig.openai.yaml",
    "anthropic":   HARNESS / "promptfooconfig.anthropic.yaml",
    "openrouter":  HARNESS / "promptfooconfig.openrouter.yaml",
}

FILTER_KEYS = {"category", "tier", "mode", "safety"}
ENV_REQUIREMENTS = {
    "openai":      "OPENAI_API_KEY",
    "anthropic":   "ANTHROPIC_API_KEY",
    "openrouter":  "OPENROUTER_API_KEY",
}


def load_cases():
    return yaml.safe_load(CASES_PATH.read_text())


def filter_cases(cases, filter_key=None, filter_value=None):
    if filter_key is None:
        return cases
    return [c for c in cases if c.get("metadata", {}).get(filter_key) == filter_value]


def write_temp_cases(cases):
    temp_path = HARNESS / "tests" / ".tmp-filtered-cases.yaml"
    temp_path.write_text(yaml.safe_dump(cases, sort_keys=False, allow_unicode=True))
    return temp_path


def main(argv):
    if len(argv) < 2 or argv[1] not in CONFIGS:
        print("Usage: python3 harness/scripts/run_eval.py <openai|anthropic|openrouter> [filter_key] [filter_value]")
        print("filter_key must be one of: category, tier, mode, safety")
        return 1

    provider = argv[1]
    filter_key   = argv[2] if len(argv) >= 4 else None
    filter_value = argv[3] if len(argv) >= 4 else None

    if filter_key is not None and filter_key not in FILTER_KEYS:
        print(f"Invalid filter_key: {filter_key}")
        return 1

    env_var = ENV_REQUIREMENTS[provider]
    if not os.environ.get(env_var):
        print(f"Missing required environment variable: {env_var}")
        print("Tip: copy .env.example to .env and fill in your key.")
        return 1

    if provider == "openrouter":
        # promptfoo openai provider reads OPENAI_API_KEY
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = os.environ["OPENROUTER_API_KEY"]
        model = os.environ.get("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct:free")
        print(f"Provider : OpenRouter  model={model}")

    if provider == "anthropic":
        model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
        print(f"Provider : Anthropic  model={model}")

    if provider == "openai":
        model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
        print(f"Provider : OpenAI  model={model}")

    cases = load_cases()
    selected_cases = filter_cases(cases, filter_key, filter_value)
    if not selected_cases:
        print("No cases matched the requested filter")
        return 1

    temp_cases = write_temp_cases(selected_cases)
    config_path = CONFIGS[provider]

    command = ["npx", "promptfoo@latest", "eval",
               "--config", str(config_path),
               "--tests",  str(temp_cases)]

    try:
        return subprocess.run(command, cwd=ROOT).returncode
    finally:
        if temp_cases.exists():
            temp_cases.unlink()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
