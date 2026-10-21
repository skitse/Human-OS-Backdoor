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
- audit or defense of a potentially manipulative system — this wins over the T2
  "single-domain behavioral audit" example above: an audit *for manipulation* is T3 even
  when the surface it examines is small, because the finding is a harm claim

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
- Include at least one boundary condition, stated in `notes`. Not conditional: any
  mechanism strong enough to be worth naming has a condition under which it stops working,
  and a design recommendation that omits it is incomplete.

### T3 Rules

- Run the safety gate first.
- Read 2-4 relevant references, including `references/anti-patterns.md` whenever pressure, scarcity, habit, or social pressure appears.
- Run the full scan from `references/scan-protocol.md`, and cite it in `references` — if
  `full_scan` is true, the protocol you followed is part of the evidence you report.
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
| `/defend` `防御` | Defense | Add abuse checks, mitigation, and trust-preserving alternatives for each strong lever. Name the specific abuse vector you are defending against in `notes` — "defend mode applied" is not a defense. |

Mode comes from the keyword, not from the request's topic. A dark-pattern audit or a
safety review with no keyword is still `adaptive`; it simply runs the Safety Gate and the
`/defend` obligations because the work is defensive. Say `defend` only when the user typed
the keyword.

## Safety Gate

Run this gate before producing any design. Its first output is not a design — it is a
**decision**: allow, redirect, or refuse. Decide that before you write, then use the output
contract for the branch you are in (see *Refusal and Redirect Output Contracts* below).
Getting the branch right matters more than the wording: a redirect answered as a refusal
drops the stack the user needed, and a refusal answered as a redirect ships the harm.

### Refuse or Redirect

Both branches can seem to apply, because a deceptive *request* always looks like "the request
is the harmful pattern". Do not settle it here — the tie-break below is what decides, and it
decides on what the harm is *for*, not on how the tactic is named.

**Refuse** when the harm *is* the deliverable — the artifact has no honest version, because it
only works by misleading, coercing, or overriding the user's own stated preference.

**Redirect** when the harm is a *means* to a goal worth serving — build the honest version of
that goal instead of declining. This is the common case, and it includes requests that name a
deceptive tactic outright: a false deadline used to unblock a real deal has a legitimate end,
so the answer is the honest message, not a refusal.

Tie-break — ask what the harm is *for*:

- **Redirect** when the harm is a means and the end is legitimate. "Our deal is stalling,
  imply a deadline" has a real goal (unblock the deal) served by a false tactic, so build
  the honest version of that goal.
- **Refuse** when the harm *is* the deliverable. If the artifact only works because it
  misleads, coerces, or overrides the user's own stated preference — punishing someone for
  skipping a day, extracting clicks from someone who does not want to open the app — there
  is no legitimate end to preserve, and a "safe rewrite" would be a different product.

A stated business goal does not by itself make a tactic redirectable. "Keep users engaged"
is not a legitimate end when the engagement is the compulsion being requested.

The list below is a **trigger list, not a branch decision**: it says the gate must act, not
which action to take. The tie-break above is the only thing that decides refuse vs redirect,
and it resolves in favour of redirect whenever an honest artifact serving the same end exists
— even when the pattern named is fake urgency or a manufactured deadline. Reading the list
and stopping there is the most common way to refuse something that should have been
redirected.

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

### Refusal and Redirect Output Contracts

**Refuse and redirect are different outputs. Read the right one.**
A *refusal* declines the request; a *redirect* keeps it and swaps the tactic. The gate tells
you which one you are in before you write anything — check that first, because emitting the
refusal shape for a redirect silently deletes the design the user asked for.

| | **Refuse** — harm *is* the deliverable | **Redirect** — harm is a *means* to a real goal |
|---|---|---|
| What you produce | a refusal: why it is out of bounds, what to build instead, the regulation | **the design**, with the unsafe tactic replaced and the substitution named |
| `visible_stack` | `false` — there is no stack | **follows the tier** — `true` at T3, where the honest replacement gets designed |
| `full_scan` | `false` | **follows the tier** |
| `tier` | T3 (a refusal is always high-stakes) | unchanged — a T3 request redirected is still T3 |
| `references` | the matching `refused-domains/` file | the model files that design the honest version, plus `scan-protocol.md` when `full_scan` is true |

Crossing the rows is the failure to avoid: **a redirect answered in the refusal shape hands the
user nothing to ship**, and a refusal answered as a design ships the harm. If a safety-gate
trigger made you emit no stack, check which branch you were actually in — only a refusal
removes the stack.

A refusal is not a design. When the gate refuses, the output changes shape — do not emit a
mechanics stack for something you are declining to build.

```text
[Why this is out of bounds — name the pattern and the harm it does]

[What is safe to build instead — the legitimate goal, served honestly]

[What the regulation says, where one applies]
```

Rules for a refusal:

- `mode` stays whatever the request asked for. A refusal does **not** escalate to `/defend`
  on its own: `defend` means "add mitigation to a lever we are keeping", which is the
  opposite of declining to build it.
- `visible_stack` and `full_scan` are `false`. There is no stack to show.
- Do not produce the manipulative artifact "for illustration". A worked example of a fake
  countdown is still a fake countdown.
- If a `references/refused-domains/` file covers the pattern, cite it. The refusal should
  send the user to the mechanism analysis, not to a search.
- Always offer the honest alternative. A bare refusal leaves the user to find a worse vendor.

### Redirect Output Contract

When the gate redirects, the user has a legitimate goal and an unsafe tactic — so **build the
thing**. The output keeps the full tier-appropriate shape:

- `visible_stack` and `full_scan` follow the tier as normal, including `true` at T3. The
  stack is where the honest replacement gets designed; dropping it turns a redirect into a
  refusal and hands the user nothing to ship.
- Name the substitution explicitly: which unsafe tactic was replaced, and by what.
- The tier does not drop because the tactic changed. A T3 request redirected to a safe tactic
  is still T3 work with a T3 stack, T3 scan, and a safe rollout note.

Refusal is the **only** case where the stack disappears. If you are redirecting and you
produced no stack, you produced a refusal — redo it.

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
⟐ [ID] [Model] · Evidence [A|B|C] · Dose [弱|中|强] · Stop: [failure signal] · Falsified by: [the record's **可证伪条件**]
    -> [how it helps here]
⟐ [ID] [Model] · Evidence [A|B|C] · Dose [弱|中|强] · Stop: [failure signal] · Falsified by: [the record's **可证伪条件**]
    -> [how it helps here]
⚡ [COMBO-xx] [Model A] x [Model B] -> [interaction]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### T3 Default Output

Use this structure:

```text
[Behavioral Opportunity Scan]

[Design / Critique / Plan]

[Risks, Boundary Conditions, Safe Rollout Notes]

━━ BEHAVIORAL MECHANICS STACK ━━━━━━━━━━━━━━━━━━━━━━━━
⟐ [ID] [Model] · Evidence [A|B|C] · Dose [弱|中|强] · Stop: [failure signal] · Falsified by: [the record's **可证伪条件**]
    -> [how it helps here]
⟐ [ID] [Model] · Evidence [A|B|C] · Dose [弱|中|强] · Stop: [failure signal] · Falsified by: [the record's **可证伪条件**]
    -> [how it helps here]
⚡ [COMBO-xx] [Model A] x [Model B] -> [interaction]
✕ [ID] [Model] ruled out by: [the record's 边界 condition]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**One mechanism is one line.** Some records describe the same lever at two levels of
abstraction (`HB-13` hyperbolic discounting and `CA-05` temporal discounting), or with one
file owning the applied depth (`HB-09` and `PE-04`). Listing both does not give the stack two
supports — it counts one lever twice and borrows the higher evidence grade. The same-mechanism
groups are declared in `references/_schema.md`; when you cite a record that appears in one,
cite it once and keep the grade of the member that actually carries the depth.

**If any mechanism drives the design, the stack is not empty.** `visible_stack` and the
stack itself are one decision: an answer that emits no stack must be one where no mechanism
was used, which is only true at T0 or for a refusal. "Behavioural reasoning informed the
answer" always leaves at least one line to write — if you reasoned from a mechanism, it
belongs in the stack. Never set `visible_stack: true` and then emit no stack.

**The stack is part of the answer, not a plan for later.** Write it in the same response
that gives the design. "The stack will be populated once the scan runs" is never correct: you
have already chosen which levers the recommendation rests on, and that choice is what the
stack reports. If the answer recommends specific mechanisms, they are in the stack now.

**Every field in the stack is copied from the mechanism record, never invented.**
`Evidence` is the record's own grade and its named source; `Dose` is the band you are
recommending; `Stop` is the record's observable failure signal, made specific to this flow.
If you cannot fill a field, you have not read the record — read it, or drop the mechanism.

Evidence grades mean:

- `A` — replicated meta-analysis or large preregistration. Safe to build on.
- `B` — multiple independent studies agreeing, or one strong study with partial replication.
  Recommend it, and say what would falsify it here.
- `C` — single study, field observation, or practitioner consensus. Usable, but say so
  plainly and prefer a cheap test over a committed build.

Do not invent leverage scores, confidence decimals, or star ratings. Evidence grade plus
dose band plus stop signal is the honest version of the same information.

**Only real mechanism IDs may go in the stack.** Every `[ID]` must be a record that exists in
`references/model-index.md`, or a `COMBO-nn` from `references/combo-patterns.md`. Nothing else
has an ID: playbooks have no IDs, `references/anti-patterns.md` has no IDs, and a file
abbreviation is not an ID (`TA-` is not trust-architecture, `DP-` is not dark-patterns, `LT-`
is not linguistic-triggers). If you want to name something from a playbook, name the playbook
in `references` and describe the tactic in words in `notes` — do not mint an ID for it. An
invented ID is worse than no ID: it carries an evidence grade and a stop signal, so it reads
like a grounded citation while pointing at nothing.

## Reference Routing

Use `references/model-index.md` only as a lookup index — do **not** cite it as a reference in your output. Always navigate to and cite the specific model or playbook file.
Read only the files needed for the active tier.

**Cite the whole path, exactly as written above.** Every entry in this section shows the
complete repo-relative path; a path with the `models/` or `domain-playbooks/` segment dropped
resolves to nothing. A citation that cannot be opened is worse than no citation, because the
reader trusts it. Copy the path from this section rather than retyping it from memory.

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
- `references/refused-domains/` — four files, cite the exact one:
  - `manufactured-urgency.md` — fake scarcity, countdowns, queues, fabricated social proof
  - `compulsion-loops.md` — variable reward, streak loss, sunk-cost lock-in
  - `narrative-control.md` — narrative hijacking, manufactured controversy, source attacks
  - `stakeholder-pressure.md` — fabricated crises, threat amplification, information asymmetry
  Read when a request edges toward any of these, and for every `/defend` task. These records
  are framed for **recognition and defence**: mechanism, harm profile, detection signals,
  defences, and the regulation that already covers the pattern. Use them to name why a tactic
  is out of bounds and to redirect, never as a build guide.
- `references/domain-playbooks/dark-patterns.md`
  Read when auditing manipulative UX, replacing deceptive conversion tactics, or handling requests involving consent traps, cancellation traps, fake urgency, or other dark-pattern risk.
- `references/scan-protocol.md`
  Read for `/scan`, `/deep`, and all T3 work.
- `references/combo-patterns.md`
  Read when combinations are central, but treat high-leverage combos as optional tools, not default recommendations. Each mechanism record's **交互** field lists the combos it actually participates in — cite from there.

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

- `references/_schema.md`
  The v2 record contract: field definitions, the migration recipe, the alias registry, and the
  declared-but-unwritten registry. Read before editing any mechanism record or adding a family.
- `references/_build-status.md`
  Read only when extending the knowledge base or planning missing coverage.
- `references/dialogues/neuroscience-x-growth-debate.md`
  Read only when you want cross-disciplinary synthesis, not for normal task execution.
- `references/dialogues/sales-x-narrative-debate.md`
  Read only when you want deeper synthesis about trust, storytelling, objections, and meaning framing, not for normal task execution.

## Quality Bar

For every recommendation:

1. Map it to a concrete mechanism by ID, from a file that exists.
2. Carry forward the record's **dose band**, its **failure signal**, and its
   **可证伪条件** (the test that would refute the mechanism here) — a recommendation with no
   ceiling, no stop condition, and no stated way to be proven wrong is not finished.
3. State at least one boundary condition when the lever is strong or risky, taken from the
   record's **边界**.
4. Report the **evidence grade honestly** (A/B/C with its source). Do not upgrade a `C`
   into confident prose, and do not invent precision the record does not have.
5. Prefer implementable guidance over abstract theory.
6. Prefer transparent influence over covert manipulation.
