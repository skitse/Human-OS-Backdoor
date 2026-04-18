# Attention Economics — Capture, Budget, and Recovery

> **Domain**: attention allocation · notification systems · feed design · signal-to-noise management · interruption cost
> **Use when**: the problem is not just persuasion, but competition for limited user attention across feeds, notifications, tasks, or interfaces
> **Scope**: attention budget, interruption cost, novelty decay, notification value, feed reward density, channel fatigue, attention recovery

---

## Why Attention Needs Its Own Model

Many behavioral models explain why users click. Attention economics explains whether they notice, tolerate, and keep noticing your prompts over time.

Use this file when the design question sounds like:

- "How often should we notify?"
- "Why are users muting or ignoring us?"
- "How do we compete for attention without burning trust?"
- "Why did this hook stop working after repeated exposure?"
- "How do we manage feed novelty without becoming exhausting?"

This file is especially relevant for:

- notifications
- feeds
- reminders
- inboxes
- dashboards
- productivity tools
- content systems

---

## Core Principle

Attention is not a static asset. It behaves like a constrained budget with compounding penalties for waste.

The practical chain is:

```text
signal emitted
-> attention captured or ignored
-> value confirmed or rejected
-> source reputation updated
-> future signals become easier or harder to notice
```

Each low-value interruption taxes the next one.

---

## Main Concepts

### 1. Attention Budget

Users do not grant infinite attention to a product. They grant a moving budget:

- per day
- per context
- per channel
- per emotional state

Design implication:

- notification permission is not a permanent entitlement
- every interruption spends scarce future attention

### 2. Interruption Cost

Not all interruptions cost the same.

Cost increases when:

- the user is focused
- the timing is socially wrong
- the message is low-value
- the next action is unclear
- the user has recently been interrupted already

High interruption cost with low value creates fast channel death.

### 3. Signal Decay

Any repeated cue loses force over time.

Examples:

- the same urgency badge
- the same promo wording
- the same notification format
- the same feed pacing

If the reward does not justify repeated exposure, the cue becomes background noise.

### 4. Source Reputation

Users learn whether a source is worth checking.

After repeated low-value signals, the source is reclassified:

- from useful
- to optional
- to ignorable
- to actively blocked

This is why one bad notification strategy can reduce total app engagement, not just notification engagement.

---

## Attention Budget Model

Use this mental model:

```text
Net Attention Value
= relevance
+ timing fit
+ expected reward
- interruption cost
- repetition fatigue
- trust damage from weak signals
```

If net value is negative enough often enough, the channel collapses.

Do not optimize open rate only. Optimize lifetime willingness to notice.

---

## High-Value Attention Patterns

### Pattern 1: High Signal Density

Each interruption should feel more informative than the surrounding noise.

Examples:

- "Your draft is approved"
- "2 teammates replied to your blocker"
- "You are one step away from completion"

Bad examples:

- generic nudges
- vague promo reminders
- low-context activity noise

### Pattern 2: Context Matching

Match the signal to the likely task state.

Examples:

- planning prompt in the morning
- re-engagement reminder at a previously active time
- progress reminder near a meaningful deadline

Do not send the same prompt independent of context.

### Pattern 3: Variable but Coherent Reward

Feeds and notifications can benefit from unpredictability, but only when the reward remains relevant.

Good:

- occasionally surprising, relevant updates
- mixed feed novelty within a trusted topic boundary

Bad:

- random irrelevant novelty
- algorithmic surprise with no user value

### Pattern 4: Recovery Windows

Users need quiet periods.

Strong systems alternate:

- capture
- value delivery
- recovery

Without recovery, even good signals become exhausting.

---

## Notification Economics

### Notification Budget Rules

Treat notifications as a ranked portfolio:

1. mission-critical
2. socially meaningful
3. progress-relevant
4. optional engagement
5. promotional

If categories 4 and 5 crowd out 1-3, the whole channel degrades.

### Timing Rules

Strong notification timing depends on:

- habit history
- current likely task mode
- urgency reality
- social appropriateness

Bad timing can destroy good content.

### Frequency Rules

More is only better up to the point where the source is reclassified as noise.

Use:

- lower defaults
- explicit preference controls
- opt-up rather than opt-down when possible

### Notification Quality Test

Before sending, ask:

1. Would I want this right now?
2. Is the next action obvious?
3. Does this create value beyond reminding the user we exist?
4. Would repeated exposure make the source feel annoying?

If the answer to 3 is no, do not send it.

---

## Feed Economics

### Novelty Gradient

Feeds need a novelty band:

- too predictable -> ignored
- too chaotic -> abandoned

The best feeds mix:

- familiar topic relevance
- occasional surprise
- visible reward
- manageable cognitive load

### Reward Density

Users continue when high-value units appear often enough to justify scanning cost.

If the feed requires too much scrolling for too little value:

- users shorten sessions
- check less often
- become harder to re-engage

### Natural Stopping Points

Infinite scroll is powerful but expensive.

Without natural stopping points:

- attention recovery drops
- fatigue rises
- perceived time cost increases after the session

Add moments like:

- completion cards
- progress summaries
- digest stops
- meaningful pauses

---

## Attention in Productivity and Utility Products

Attention economics is not only for content products.

For utilities and productivity tools:

- every dashboard element competes for finite cognitive bandwidth
- too many highlights means nothing is highlighted
- too many reminders means the system becomes self-defeating

Use strong salience sparingly.

Priority signals should be:

- rare
- legible
- behaviorally actionable

---

## Failure Modes

### 1. Notification Inflation

Too many medium-value notifications collapse the whole channel.

### 2. Hook Burnout

The first hook works, the fifth exposure does not.

### 3. Feed Exhaustion

Attention capture is high, but post-session regret rises, reducing long-term trust.

### 4. Dashboard Saturation

Everything is flagged as important, so users ignore the interface hierarchy entirely.

### 5. Channel Mispricing

Using high-cost channels for low-value messages:

- push for weak promos
- SMS for mild reminders
- modal interruption for trivial updates

This spends too much attention for too little value.

---

## Safe Use Rules

- treat attention as borrowed, not owned
- optimize for long-term noticeability, not short-term intrusion
- preserve recovery windows
- do not use high-pressure interruption patterns for low-value prompts
- for trust-sensitive products, explanation and control beat volume and urgency

Read alongside:

- `references/anti-patterns.md` for notification fatigue and trust erosion
- `references/models/perception-attention.md` for capture mechanics
- `references/models/cognitive-architecture.md` for attention resources and prediction error
- `references/models/affective-dynamics.md` for variable reward dynamics
- `references/domain-playbooks/linguistic-triggers.md` when the intervention is at the wording level
