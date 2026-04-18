# Behavioral Finance — Money Decision Playbook

> **Domain**: fintech, investing, savings, budgeting, credit, insurance, payment-risk flows
> **Use when**: the task involves money anxiety, risk perception, loss framing, investment/saving behavior, or trust in a financial decision
> **Do not use for**: generic SaaS onboarding, ordinary checkout copy, or broad macro/market commentary

---

## Why This File Exists

This playbook is for **money decisions inside products and interfaces**, not for writing market essays.

Use it when the design problem sounds like:

- "Users are afraid to move money"
- "People freeze when investing or choosing a plan"
- "Customers overreact to short-term losses or volatility"
- "We need to explain financial risk without causing panic"
- "How do we design savings, budgeting, or portfolio nudges responsibly?"

If the task is ordinary pricing architecture, use `references/models/pricing-economic-decisions.md` first.

---

## Core Principle

Financial decisions feel different from ordinary product choices because they combine:

- loss aversion
- uncertainty
- delayed feedback
- trust sensitivity
- self-judgment and identity

Users are not just evaluating utility. They are also asking:

- "What if I regret this?"
- "What if I lose money?"
- "What does this say about whether I'm responsible?"
- "Can I trust this system with something important?"

---

## The 5 Main Money-Decision Patterns

### 1. Loss Salience Dominates Gain Salience

Small visible losses often outweigh larger abstract future gains.

Examples:

- a user notices a short-term drawdown more than long-term expected return
- a saver reacts more strongly to a fee than to future compounding
- a borrower focuses on monthly pain more than total cost

Design implication:

- make downside legible, but do not let short-term red numbers dominate the whole experience
- pair risk disclosure with time horizon, recovery context, and next-step clarity

### 2. Volatility Feels Like Danger

Users often treat fluctuation as failure.

Examples:

- first-time investors panic during normal market variance
- budgeting users feel shame when weekly spending spikes
- BNPL users misread low immediate payment as low total commitment

Design implication:

- separate normal variation from true risk events
- explain what changed, why it changed, and what action is appropriate

### 3. Trust Is a Precondition, Not a Layer

In finance, unclear wording or hidden tradeoffs destroy confidence quickly.

Design implication:

- disclose fees, timing, lockups, and risk in plain language
- show custody, regulation, security, and support paths clearly
- never use fake urgency, hidden consent, or ambiguous defaults in money flows

### 4. Present Bias Distorts Good Intentions

People want long-term financial outcomes but overvalue immediate comfort.

Examples:

- delaying savings setup
- avoiding account linking
- postponing debt repayment planning

Design implication:

- reduce activation friction
- use implementation prompts: "Set this up now in under 2 minutes"
- convert vague goals into concrete next actions

### 5. Self-Image Strongly Affects Action

Money decisions are tied to identity: competent, careful, successful, behind, irresponsible.

Design implication:

- avoid shame-heavy messaging
- frame progress as capability-building, not moral judgment
- show improvement paths users can realistically follow

---

## High-Value Design Moves

### Risk Communication

Use:

- plain-language risk labels
- downside ranges, not just abstract disclaimers
- time horizon context
- "what to do now" guidance after explaining risk

Avoid:

- giant warning blocks with no prioritization
- red-heavy interfaces that make ordinary fluctuation feel catastrophic
- overreliance on legal copy as the main education layer

### Savings and Investing Flows

Use:

- automatic contribution defaults with explicit user control
- milestone framing: first deposit, first month funded, first emergency buffer
- progress views tied to goals, not constant emotional whipsaw

Avoid:

- compulsive-checking loops around market movement
- gamified urgency around risky trading behavior
- social-comparison prompts that pressure users into unsuitable risk

### Lending and Credit

Use:

- total cost clarity
- repayment timing clarity
- scenario previews: on-time, late, early payoff
- plain-language consequences before commitment

Avoid:

- hiding total repayment behind low monthly framing alone
- confusing teaser rates
- softening obligation with playful UI that obscures seriousness

### Budgeting and Financial Habits

Use:

- gentle variance framing: "higher than usual" instead of "you failed"
- if-then plans: "If spending exceeds X, transfer Y tomorrow"
- recovery paths after slips

Avoid:

- all-or-nothing streak logic that punishes one bad day too hard
- moralizing tone
- fear blasts without practical next steps

---

## Pattern Library

### Pattern 1: Reassure Before Asking for Money Movement

Best for:

- bank linking
- first deposit
- large transfer
- autopay setup

Include:

- why the step matters
- what happens technically
- how the user stays in control
- what protections exist

### Pattern 2: Normalize Volatility Without Minimizing Risk

Best for:

- portfolio dashboards
- savings variance
- repayment projections

Include:

- what changed
- whether this is normal or exceptional
- what action, if any, is recommended

### Pattern 3: Make Long-Term Value Concrete

Best for:

- savings products
- insurance
- debt reduction
- subscription upgrades with clear financial return

Use:

- future-state translation into plain outcomes
- side-by-side cost of action vs cost of delay
- realistic scenario math rather than hype

### Pattern 4: Design Defaults for Safety, Not Extraction

Best for:

- contribution rates
- notification settings
- autopay
- privacy and consent in finance flows

Rule:

- defaults can simplify action, but they must remain easy to inspect and change

---

## Anti-Patterns

- using urgency or scarcity to rush a financial decision
- disguising risk with celebratory or game-like language
- encouraging compulsive checking of money movement
- using social proof to imply that higher risk is the normal smart choice
- burying fees, lockups, or repayment details

For any of the above, route through:

- `references/anti-patterns.md`
- `references/domain-playbooks/dark-patterns.md`
- `references/models/trust-architecture.md`

---

## Output Guidance

Good outputs from this file sound like:

- "Reduce panic by distinguishing normal volatility from action-worthy risk."
- "Explain the downside clearly, then give the user a reversible next step."
- "Use a safe default, but make inspection and change easy."
- "Replace shame framing with progress framing and recovery paths."

Bad outputs from this file sound like:

- trading tips
- macro market essays
- tactics for increasing risky speculation
- urgency tactics for finance decisions
