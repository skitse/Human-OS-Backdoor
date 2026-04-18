---
name: human-os
description: >-
  Behavioral design overlay applying psychology, cognitive bias, and behavioral economics to
  product, content, offer, UX, community, and growth tasks. Use when designing or optimizing
  onboarding, conversion, retention, pricing, social loops, engagement mechanics, messaging,
  trust signals, nudges, or persuasion mechanics — or when auditing behavioral levers, dark
  patterns, or growth hacking tactics in an existing plan. Covers user psychology, habit
  formation, attention economics, social dynamics, and choice architecture. Do not use for
  simple rewriting, translation, pure coding/debugging, factual Q&A, or tasks without
  meaningful human decision design. Modes: /stealth, /scan, /deep, /combo, /defend.
---

# Human OS

Apply behavioral design when it materially improves the user's outcome.
Optimize for transparent, user-benefiting, durable behavior change.
Prefer leverage and clarity over theatrical "behavioral" commentary.

## Activation Gate

Trigger this skill only when all of the following are true:

1. The user is designing, auditing, or optimizing a human-facing flow, message, offer, system, or strategy.
2. The task materially depends on choice architecture, motivation, trust, habit, attention, pricing, social dynamics, or persuasion.
3. A behavioral lens would change the recommendation, not merely decorate the answer.

Do not trigger this skill when any of the following are true:

- The request is simple rewriting, proofreading, summarization, or translation.
- The request is pure implementation, debugging, refactoring, or infrastructure work with no meaningful human-decision component.
- The request is factual Q&A, explanation, or research with no design decision to make.
- The request is too small to justify behavioral overhead, unless the user explicitly asks for a behavioral layer.

## Task Tiers

Classify the task before reading references or choosing an output format.

### T0 - No Trigger

Use no Human OS overlay.

Examples:
- grammar polish
- plain translation
- "what does this term mean?"
- pure code fix

### T1 - Micro Design

Use a light overlay for one narrow decision point.

Examples:
- one CTA
- one headline
- one notification rewrite
- one onboarding step
- one social proof block

### T2 - Scoped Design

Use a standard overlay for one bounded flow or artifact.

Examples:
- landing page section
- onboarding sequence
- pricing page critique
- referral mechanic
- retention email sequence
- checkout reassurance section
- cultural or market-specific adaptation of a flow
- trust or credibility redesign for a single surface
- referral loop design for a single product
- single-domain behavioral audit (e.g. "audit our onboarding")

### T3 - System or Risky Design

Use a full overlay for multi-step systems, high-stakes persuasion, or requests with meaningful abuse risk.

Examples:
- full conversion funnel
- retention loop architecture
- pricing system redesign
- community incentive system
- finance, health, children, addiction, politics, or other trust-sensitive contexts
- any request involving fake scarcity, fake urgency, deceptive defaults, or dark patterns
- any request to design for a vulnerable or captive population
- audit or defense of a potentially manipulative system

## Effort Policy

Match effort to tier. Do not default to maximum output.

### T1 Rules

- Read at most 1 directly relevant reference file.
- Skip the full scan unless the user explicitly asks for `/scan` or `/deep`.
- Name at most 1-2 mechanisms.
- Do not emit the full visible mechanics stack unless the user asked for it or a mode keyword forces it.
- Keep the behavioral reasoning compact and subordinate to the actual answer.

### T2 Rules

- Read 1-2 relevant references.
- Run a compact scan mentally or explicitly.
- Name 2-4 mechanisms.
- Show the visible mechanics stack by default unless `/stealth` is active.
- Include at least one boundary condition if pressure, trust, or tradeoffs matter.

### T3 Rules

- Run the safety gate first.
- Read 2-4 relevant references, including `references/anti-patterns.md` whenever pressure, scarcity, habit, or social pressure appears.
- Run the full scan from `references/scan-protocol.md`.
- Include boundary conditions, failure modes, and a safe rollout or testing note.
- Prefer transparent alternatives when high-pressure tactics are unnecessary.

Promote the task upward when any of the following are true:

- The user requests a full behavioral audit across an entire product or funnel.
- The design coordinates multiple independent flows or cross-channel systems.
- Trust, consent, or social pressure becomes the central design problem (not just one element).
- The request enters a high-stakes domain (health, finance, legal, children, crisis, addiction).
- The safety gate would trigger (fake scarcity, deceptive defaults, coercive patterns) → **always T3**.
- The word "funnel," "architecture," or "retention loop" describes the entire task scope.

Demote the task downward when the answer only needs one localized improvement.

**T3 fast-track signals** (skip lower tiers, go directly to T3):
- Any request involving deception, dark patterns, or fake social proof
- Any request to design manipulation for a trust-sensitive population

## Mode Contract

Interpret modes after tiering.

| Keyword | Mode | Contract |
|---------|------|----------|
| `(none)` | Adaptive Dual Track | Follow tier rules. Only show the visible stack when T2/T3 or clearly helpful. |
| `/stealth` `隐身` | Invisible | Apply the skill silently. Do not expose mechanics unless the user later asks. |
| `/scan` `扫描` | Scan First | Show the scan before design, even for smaller tasks. |
| `/deep` `深度` | Full Drill | Expand to T3-style depth: scan, mechanism selection, implementation notes, risks. |
| `/combo` `组合` | Combo Focus | Center the answer on mechanism combinations and interaction effects. |
| `/defend` `防御` | Defense | Add abuse checks, mitigation, and trust-preserving alternatives for each strong lever. |

## Safety Gate

Run this gate before producing any design.

### Refuse or Redirect

**Refuse** (not redirect) when the request itself IS the harmful pattern — i.e. the user is asking to build deceptive content, fake social proof, or coercive mechanics directly.

**Redirect** when the user has a legitimate goal but reaches for an unsafe tactic — convert to a safe alternative instead.

Refuse or redirect the request when it asks for, or clearly depends on:

- fake scarcity, fake social proof, fake queues, fake urgency, or fabricated popularity
- hidden consent, pre-checked marketing consent, deceptive defaults, or cancellation traps
- coercion, manipulation of vulnerable users, exploitation of children, or deliberate addiction loops
- pressure tactics for health, finance, legal, crisis, or other high-stakes decisions
- astroturfing, manufactured controversy, ideological radicalization, or deceptive narrative control

### Rewrite Into Safe Alternatives

When the user's goal is legitimate but the tactic is unsafe, convert it to:

- real scarcity instead of fake scarcity
- transparent recommendation instead of hidden nudging
- healthy engagement loops instead of compulsive loops
- opt-in consent instead of silent consent
- trust-building proof instead of fabricated proof

### High-Stakes Rule

For health, finance, legal, children, crisis, or other high-stakes contexts:

- favor clarity, autonomy, and reversibility
- avoid dark patterns and pressure framing
- explicitly mention risk, trust, and failure conditions

## Workflow

1. Classify the task into T0-T3.
2. Resolve the mode keyword, if any.
3. Run the safety gate.
4. Choose the smallest reference set that can answer the task well.
5. Run the compact or full scan according to tier and mode.
6. Draft the practical answer first.
7. Add behavioral annotation only to the depth required by tier and mode.

## Output Contract

### T1 Default Output

Deliver the practical answer first.
Optionally append a short `Behavioral Notes` block with 1-2 levers when useful.

### T2 Default Output

Use this structure:

```text
[Design / Critique / Plan]

━━ BEHAVIORAL MECHANICS STACK ━━━━━━━━━━━━━━━━━━━━━━━━
⟐ [Model] [conf] -> [how it helps here]
⟐ [Model] [conf] -> [how it helps here]
⚡ COMBO: [Model A] x [Model B] -> [interaction]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### T3 Default Output

Use this structure:

```text
[Behavioral Opportunity Scan]

[Design / Critique / Plan]

[Risks, Boundary Conditions, Safe Rollout Notes]

━━ BEHAVIORAL MECHANICS STACK ━━━━━━━━━━━━━━━━━━━━━━━━
⟐ [Model] [conf] -> [how it helps here]
⟐ [Model] [conf] -> [how it helps here]
⚡ COMBO: [Model A] x [Model B] -> [interaction]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Confidence levels:

- `★★★` = high confidence
- `★★☆` = medium confidence
- `★☆☆` = lower but still usable confidence

Do not emit pseudo-precise leverage scores by default.
Rank interventions as `High`, `Medium`, or `Low` priority unless the user explicitly asks for quantified experimentation.

## Reference Routing

Use `references/model-index.md` only as a lookup index — do **not** cite it as a reference in your output. Always navigate to and cite the specific model or playbook file.
Read only the files needed for the active tier.

### Core Models

- `references/models/cognitive-architecture.md`
  Use for cognitive load, System 1 vs System 2, prediction error, embodiment, attention limits.
- `references/models/attention-economics.md`
  Use when notification frequency, feed pacing, interruption cost, channel fatigue, or attention budgeting is central.
- `references/models/heuristics-biases.md`
  Use for defaults, anchoring, loss aversion, scarcity, framing, decoys.
- `references/models/social-dynamics.md`
  Use for social proof, reciprocity, conformity, authority, signaling, trust transfer.
- `references/models/trust-architecture.md`
  Use when reassurance, credibility, integrity, consent, or trust repair is the core design problem.
- `references/models/affective-dynamics.md`
  Use for Zeigarnik, emotional contagion, curiosity, flow, variable reward.
- `references/models/motivation-regulation.md`
  Use for habits, identity, implementation intentions, progress, precommitment.
- `references/models/perception-attention.md`
  Use for fluency, pattern interruption, visual hierarchy, contrast, attention capture.
- `references/models/pricing-economic-decisions.md`
  Use for pricing architecture, transaction utility, payment pain, mental accounting, willingness-to-pay shaping.

### Mandatory Safeguards

- `references/anti-patterns.md`
  Read whenever the design uses pressure, habit loops, default effects, urgency, or other strong levers.
- `references/domain-playbooks/dark-patterns.md`
  Read when auditing manipulative UX, replacing deceptive conversion tactics, or handling requests involving consent traps, cancellation traps, fake urgency, or other dark-pattern risk.
- `references/scan-protocol.md`
  Read for `/scan`, `/deep`, and all T3 work.
- `references/combo-patterns.md`
  Read when combinations are central, but treat high-leverage combos as optional tools, not default recommendations.

### Domain Playbooks

- `references/domain-playbooks/saas-products.md`
- `references/domain-playbooks/social-commerce.md`
- `references/domain-playbooks/cultural-psychology.md`
- `references/domain-playbooks/content-hooks.md`
- `references/domain-playbooks/linguistic-triggers.md`
- `references/domain-playbooks/games-gamification.md`
- `references/domain-playbooks/community-social.md`
- `references/domain-playbooks/viral-growth-loops.md`
- `references/domain-playbooks/sales-psychology.md`
- `references/domain-playbooks/interpersonal-persuasion.md`
- `references/domain-playbooks/meme-engineering.md`
- `references/domain-playbooks/video-content-psychology.md`
- `references/domain-playbooks/behavioral-finance.md`

Choose one playbook when the domain is clear. Avoid reading many playbooks at once.
Prefer `references/domain-playbooks/linguistic-triggers.md` for copy-level tasks where wording is the main leverage point.
Prefer `references/domain-playbooks/cultural-psychology.md` when market context, especially China vs Western defaults, changes the right behavioral lever.
Use `references/domain-playbooks/video-content-psychology.md` only for video retention and pacing problems, not generic content work.
Use `references/domain-playbooks/meme-engineering.md` only for remixable social formats, not for ordinary content strategy.
Use `references/domain-playbooks/behavioral-finance.md` only for fintech and money-decision product flows, not generic SaaS or macro commentary.

### Extension Planning Only

- `references/_build-status.md`
  Read only when extending the knowledge base or planning missing coverage.
- `references/dialogues/neuroscience-x-growth-debate.md`
  Read only when you want cross-disciplinary synthesis, not for normal task execution.
- `references/dialogues/sales-x-narrative-debate.md`
  Read only when you want deeper synthesis about trust, storytelling, objections, and meaning framing, not for normal task execution.

## Quality Bar

For every recommendation:

1. Map it to a concrete mechanism.
2. Explain the trigger -> cognitive process -> behavioral output chain when the extra detail matters.
3. State at least one boundary condition when the lever is strong or risky.
4. Prefer implementable guidance over abstract theory.
5. Prefer transparent influence over covert manipulation.
