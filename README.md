# Human OS: Backdoor

A Claude Code skill for behavioral design — built on the idea that humans run an OS, and you can reverse-engineer it.

Not a manipulation toolkit. A structured way to apply behavioral science where it actually matters: onboarding, conversion, retention, pricing, content, community, and growth.

---

## What this is

When you're designing a flow, writing copy, or auditing a product, the behavioral layer is usually handled by instinct. This skill makes it explicit — naming the mechanisms, showing how they interact, flagging when they're being misused.

It works as a **Claude Code skill**: drop it in, and Claude routes behavioral design tasks through a structured reference system instead of relying on vibes.

---

## Install

```bash
# Clone into your Claude Code skills directory
git clone https://github.com/yourname/human-os-backdoor ~/.claude/skills/human-os
```

Or copy `skills/human-os/` into wherever you keep your Claude Code skills.

Claude Code will pick it up automatically on the next session.

---

## Usage

The skill activates automatically when a task involves human decision design. You can also invoke modes explicitly:

| Mode | What it does |
|------|-------------|
| *(none)* | Adaptive — light touch for small tasks, full stack for complex ones |
| `/stealth` | Applies the skill silently, no visible mechanics |
| `/scan` | Shows the behavioral scan before designing |
| `/deep` | Full drill: scan + mechanisms + risks + rollout notes |
| `/combo` | Focuses on mechanism combinations and interaction effects |
| `/defend` | Adds abuse checks and trust-preserving alternatives |

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

## What's inside

### Cognitive models (`references/models/`)

Nine models covering how people actually process, decide, and act:

- `cognitive-architecture` — dual process, cognitive load, predictive coding
- `heuristics-biases` — anchoring, loss aversion, defaults, decoy, sunk cost
- `social-dynamics` — social proof, reciprocity, authority, conformity
- `affective-dynamics` — Zeigarnik, curiosity, variable reward, flow
- `motivation-regulation` — habits, identity, implementation intentions, streaks
- `perception-attention` — fluency, pattern interrupt, visual hierarchy
- `attention-economics` — notification budgets, channel fatigue, novelty decay
- `trust-architecture` — trust formation, digital credibility signals, repair
- `pricing-economic-decisions` — payment pain, mental accounting, willingness-to-pay

### Domain playbooks (`references/domain-playbooks/`)

Fourteen applied contexts:

`saas-products` · `social-commerce` · `viral-growth-loops` · `games-gamification` · `community-social` · `content-hooks` · `video-content-psychology` · `linguistic-triggers` · `cultural-psychology` · `sales-psychology` · `interpersonal-persuasion` · `meme-engineering` · `behavioral-finance` · `dark-patterns`

### Supporting references

- `combo-patterns` — 17 high-leverage mechanism combinations with real product examples
- `anti-patterns` — what looks like a bias but isn't, and design moves that backfire
- `scan-protocol` — the behavioral opportunity scan used in `/scan` and `/deep` modes
- `model-index` — fast candidate selection when you know the domain but not the mechanism
- `dialogues/` — cross-disciplinary debates (neuroscience × growth, sales × narrative)

---

## Task tiers

The skill classifies every task before doing anything:

| Tier | Scope | Example |
|------|-------|---------|
| T0 | No behavioral layer needed | "fix this typo" |
| T1 | One narrow decision point | rewrite a single CTA |
| T2 | One bounded flow or artifact | onboarding sequence, pricing page |
| T3 | Multi-step system or high-stakes context | full retention loop, fintech product |

Effort scales with tier. T1 gets one mechanism and a short note. T3 gets the full scan, risks, and safe rollout considerations.

---

## Safety gate

Every request goes through a gate before any output is produced.

The skill refuses or redirects requests that involve fake scarcity, fake social proof, hidden consent, deliberate addiction loops, or coercion of vulnerable users. When the goal is legitimate but the tactic isn't, it rewrites into a transparent alternative.

High-stakes domains — health, finance, children, crisis — get extra scrutiny regardless of tier.

This isn't decorative. See `references/anti-patterns.md` and `references/domain-playbooks/dark-patterns.md` for what gets flagged and why.

---

## Eval harness

The `harness/` directory contains a [promptfoo](https://promptfoo.dev)-based evaluation suite:

```bash
# Run smoke checks (no API key needed)
python3 harness/scripts/run_all_checks.py

# Verify the skill is correctly packaged
python3 harness/scripts/check_packaged_skill.py

# Full eval (requires ANTHROPIC_API_KEY or OPENAI_API_KEY)
python3 harness/scripts/run_eval.py
```

The harness tests tier classification, mode behavior, safety gate decisions, and reference routing against ~30 labeled cases.

---

## What this is not

- Not a prompt injection tool
- Not a dark pattern generator
- Not a replacement for actually understanding your users
- Not a guarantee that any of this will work on your specific product

Behavioral science gives you the mechanism. Whether it applies to your context is still a judgment call.

---

## Structure

```
.
├── SKILL.md                        # Skill definition (entry point for Claude Code)
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
