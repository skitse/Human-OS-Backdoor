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

Or copy `skills/human-os/` into your Claude Code skills directory.

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

9 models covering how people process, decide, and act:

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

### Supporting references

| File | Purpose |
|------|---------|
| `combo-patterns` | 17 high-leverage mechanism combinations with real product examples |
| `anti-patterns` | Adaptive traits misread as biases, and design moves that backfire |
| `scan-protocol` | Behavioral opportunity scan used in `/scan` and `/deep` modes |
| `model-index` | Fast candidate selection index |
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

# Full eval (requires ANTHROPIC_API_KEY or OPENAI_API_KEY)
python3 harness/scripts/run_eval.py
```

Tests cover: tier classification, mode behavior, safety gate decisions, reference routing — ~30 labeled cases.

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
├── SKILL.md                        # Skill definition (Claude Code entry point)
├── skills/
│   └── human-os/
│       ├── SKILL.md
│       └── references/
│           ├── model-index.md
│           ├── scan-protocol.md
│           ├── anti-patterns.md
│           ├── combo-patterns.md
│           ├── models/             # 9 cognitive model files
│           ├── domain-playbooks/   # 14 applied context files
│           └── dialogues/          # 2 cross-disciplinary debate files
└── harness/                        # Eval suite
    ├── tests/
    ├── scripts/
    └── promptfooconfig.yaml
```
