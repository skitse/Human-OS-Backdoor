# Human OS: Backdoor

**Behavioral Design Skill · Built for Claude Code**

> Humans run an OS. This skill is the reverse engineering tool.

[中文](README.md)

---

## What this is

When you're designing a flow, writing copy, or auditing a product, the behavioral layer is usually handled by instinct. This skill makes it explicit — naming the mechanisms, showing how they interact, flagging when they're being misused.

It works as a **Claude Code skill**: drop it in, and Claude routes behavioral design tasks through a structured reference system instead of relying on vibes.

Use for: onboarding, conversion, retention, pricing, content, community, growth.

Don't use for: proofreading, translation, debugging, or tasks with no human decision design component.

---

## Install

```bash
git clone https://github.com/skitse/Human-OS-Backdoor ~/.claude/skills/human-os
```

The repo root is the skill itself — clone it wherever you want to load it from.

Claude Code picks it up automatically on the next session.

---

## Usage

The skill activates automatically when a task involves human decision design. You can also invoke modes explicitly:

| Mode | Trigger | Effect |
|------|---------|--------|
| Adaptive | *(none)* | Light touch for small tasks, full stack for complex ones |
| `/stealth` | `/stealth` | Applies the skill silently, no visible mechanics |
| `/scan` | `/scan` | Shows the behavioral scan before designing |
| `/deep` | `/deep` | Full drill: scan + mechanisms + risks + rollout notes |
| `/combo` | `/combo` | Focuses on mechanism combinations and interaction effects |
| `/defend` | `/defend` | Adds abuse checks and trust-preserving alternatives |

**Examples:**

```
Design an onboarding flow for a habit-tracking app /deep
```

```
Critique this pricing page /scan
```

```
Rewrite this CTA for loss aversion /stealth
```

```
Audit this retention loop for dark patterns /defend
```

---

## Knowledge base

### Cognitive models (`references/models/`)

9 model files holding 71 mechanism records, each carrying a full v2 field set (evidence
grade with its source, mechanism chain, dose band, time dynamics, moderators, failure
signals, measurable proxies, interactions, boundary conditions):

| File | Contents |
|------|----------|
| `cognitive-architecture` | Dual process, cognitive load, predictive coding |
| `heuristics-biases` | Anchoring, loss aversion, defaults, decoy, sunk cost |
| `social-dynamics` | Social proof, reciprocity, authority, conformity |
| `affective-dynamics` | Zeigarnik, curiosity, variable reward, flow |
| `motivation-regulation` | Habits, identity, implementation intentions, streaks |
| `perception-attention` | Fluency, pattern interrupt, visual hierarchy |
| `attention-economics` | Notification budgets, channel fatigue, novelty decay |
| `trust-architecture` | Trust formation, digital credibility signals, repair |
| `pricing-economic-decisions` | Payment pain, mental accounting, willingness-to-pay |

### Domain playbooks (`references/domain-playbooks/`)

14 applied contexts:

`saas-products` · `social-commerce` · `viral-growth-loops` · `games-gamification` · `community-social` · `content-hooks` · `video-content-psychology` · `linguistic-triggers` · `cultural-psychology` · `sales-psychology` · `interpersonal-persuasion` · `meme-engineering` · `behavioral-finance` · `dark-patterns`

### Refused domains (`references/refused-domains/`)

Four domains the pack documents for **recognition, audit and defence**, never as a build
guide. Each record carries the mechanism, its harm profile, detection signals, defensive
actions at individual/platform/regulator level, and the regulation that already covers it.

`manufactured-urgency` · `compulsion-loops` · `narrative-control` · `stakeholder-pressure`

### Supporting references

| File | Purpose |
|------|---------|
| `_schema.md` | The v2 record contract every mechanism must satisfy, plus the migration recipe |
| `combo-patterns` | 17 high-leverage mechanism combinations with real product examples |
| `anti-patterns` | Adaptive traits misread as biases, and design moves that backfire |
| `scan-protocol` | Behavioral opportunity scan used in `/scan` and `/deep` modes |
| `model-index` | Generated index of every mechanism record that actually exists |
| `dialogues/` | Cross-disciplinary debates (neuroscience × growth; sales × narrative) |

---

## Task tiers

Every request is classified before any output:

| Tier | Scope | Example |
|------|-------|---------|
| T0 | No behavioral layer needed | Fix a typo |
| T1 | One narrow decision point | Rewrite a single CTA |
| T2 | One bounded flow or artifact | Onboarding sequence, pricing page |
| T3 | Multi-step system or high-stakes context | Full retention loop, fintech product |

Effort scales with tier. T1 gets one mechanism and a short note. T3 gets the full scan, risks, and rollout considerations.

---

## Safety gate

Every request goes through a gate before any output is produced.

Refused or redirected: fake scarcity, fake social proof, hidden consent, deliberate addiction loops, coercion of vulnerable users. When the goal is legitimate but the tactic isn't, it rewrites into a transparent alternative.

High-stakes domains — health, finance, children, crisis — get extra scrutiny regardless of tier.

See `references/anti-patterns.md` and `references/domain-playbooks/dark-patterns.md`.

---

## Eval harness

The `harness/` directory contains a [promptfoo](https://promptfoo.dev)-based evaluation suite:

```bash
# Static checks (no API key needed)
python3 harness/scripts/run_all_checks.py

# Verify skill is correctly packaged
python3 harness/scripts/check_packaged_skill.py

# Full eval (requires OPENROUTER_API_KEY, or ANTHROPIC_API_KEY / OPENAI_API_KEY)
python3 harness/scripts/run_eval.py openrouter   # or openai / anthropic
```

Tests cover: tier classification, mode behavior, safety gate decisions, reference routing,
and v2 field completeness — 22 labeled cases.

Three hard rules. Break any one and the suite goes back to "all green, nothing measured":

1. **Every case value is a scalar, never a YAML list.** promptfoo expands a list-valued
   variable into a cartesian product of separate runs, so one case silently becomes N rows
   that each check one item. This repo's old "50/50 pass" was 18 cases spread over 50 rows.
   Scalars keep one case to one run, so the denominator cannot be inflated.
2. **Fixtures are generated by `build_replay_fixtures.py` from a real eval record**, never
   hand-written. Hand-written fixtures are all positive examples and cannot distinguish
   "the contract is satisfied" from "the assertions always pass".
3. **The replay gate self-tests with negative cases.** It breaks each fixture against the
   contract (flip `trigger`, corrupt `tier`, empty `notes`, …) and requires the assertion
   layer to reject every single mutation. One mutation surviving turns the gate red,
   because it means the assertions have a hole. Currently 195 mutations are all rejected.

`run_eval.py` pins the promptfoo version and forces `--no-cache`: a floating version makes
two runs incomparable, and the cache re-grades a previous run's model output, passing off
old text's score as the current text's.

---

## What this is not

- Not a prompt injection tool
- Not a dark pattern generator
- Not a replacement for actually understanding your users
- Not a guarantee that any of this works on your specific product

Behavioral science gives you the mechanism. Whether it applies to your context is still a judgment call.

---

## Structure

```
.
├── SKILL.md                    # Skill definition (Claude Code entry point)
├── references/
│   ├── model-index.md
│   ├── scan-protocol.md
│   ├── anti-patterns.md
│   ├── combo-patterns.md
│   ├── models/                 # 9 model files / 71 mechanism records
│   ├── domain-playbooks/       # 14 applied context files
│   └── dialogues/              # 2 cross-disciplinary debate files
└── harness/                    # Eval suite
    ├── tests/
    ├── scripts/
    └── promptfooconfig.yaml
```
