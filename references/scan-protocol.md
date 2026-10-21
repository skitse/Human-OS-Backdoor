# Behavioral Opportunity Scan Protocol

Used in Mode C (`/scan`) and Mode D (`/deep`) before generating any design.
This protocol systematically identifies ALL applicable behavioral leverage points.

**Hard rule:** every mechanism you name must correspond to a record in
`references/models/`. Those records carry a dose band, a decay clock, observable failure
signals, moderators, cross-mechanism interactions, and a boundary. The scan's job is to
select mechanisms and carry those fields forward — not to produce a list of impressive
names. If an ID is not in `references/model-index.md`, it has no body and must not be
recommended.

---

## The 9-Step Scan

### Step 1: Goal Mapping
Define the target behavior change in concrete terms.

```
TARGET BEHAVIOR: [specific action user should take]
CURRENT BEHAVIOR: [what they do now]
GAP: [the friction / barrier between current and target]
SUCCESS METRIC: [how we measure behavior change]
```

Examples:
- "User clicks 'invite friend'" (not "increase engagement")
- "User completes payment" (not "improve conversion")
- "User opens app every morning" (not "boost retention")

### Step 2: Actor Profiling
Map the psychological state of the target human at the moment of decision.

```
ACTOR PROFILE:
  Emotional state: [anxious / excited / bored / rushed / uncertain]
  Cognitive load:  [high / medium / low] — affects System 1 vs System 2 operation
  Social context:  [alone / observed / in-group / competitive]
  Time pressure:   [high / medium / low]
  Prior state:     [first time / habitual / returning after absence]
  Identity:        [how do they see themselves in this context]
```

**Key insight**: High cognitive load + time pressure → System 1 dominates → heuristics and biases are MORE exploitable.

### Step 3: Friction Map
List every point where the desired behavior can fail.

```
FRICTION POINTS:
  Awareness: [do they know this action exists?]
  Motivation: [do they want to take action?]
  Ability: [can they do it easily?]
  Timing: [is the prompt happening at the right moment?]
  Social: [does taking action feel socially risky?]
  Cognitive: [is the decision too complex?]
```

For each friction point, identify the PRIMARY behavioral model that addresses it.

### Step 4: Mechanism Match

For each goal and friction point, scan model categories:

**Quick decision tree:**
```
Is the user hesitating?
  → HB-02 Loss Aversion (reframe as loss)
  → HB-04 Scarcity (now or never)
  → HB-03 Default Effect (make the right choice the default)

Does the user need motivation to start?
  → MR-06 Progress Momentum (show pseudo-progress)
  → MR-01 Goal Gradient (show they're close to a goal)
  → SD-01 Social Proof (others already started)

Is the user going to abandon?
  → AD-02 Zeigarnik (leave incomplete task in mind)
  → HB-02 Loss Aversion (frame accumulated progress as a thing about to be lost)
  → MR-03 Habit Loop (tie action to existing cue)

Does the user need to invite others / share?
  → SD-02 Reciprocity (give them something to give)
  → SD-14 Status Signaling (make sharing = social currency)
  → HB-04 Scarcity (exclusive access for sharer)
  → SD-10 FOMO (show what non-sharers are missing)

Is the content / hook not working?
  → PA-02 Pattern Interruption (break expected format)
  → AD-10 Information Gap (create knowledge gap)
  → PA-01 Processing Fluency (reduce cognitive friction)
  → AD-06 Fear/Threat Response (lead with a concrete stake, not a vague claim)

Pricing / offer not converting?
  → HB-01 Anchoring (show high price first)
  → HB-11 Decoy Effect (add asymmetric middle option)
  → HB-02 Loss Aversion (what they lose by not buying)
  → HB-09 Endowment Effect (free trial with personalization)
```

### Step 5: Dose, Clock, and Failure Signal

**This step is mandatory and is where most v1 scans stopped short.** Naming a mechanism
is not a recommendation. For every candidate you carry forward, read its v2 record and
extract four things:

```
DOSE BAND:     弱 / 中 / 强 / 过载 — pick the band you are recommending, and say why
               the band above it is wrong here
DECAY CLOCK:   when does this stop working? (from the record's 时间动态)
SATURATION:    what does "too much" look like, concretely?
FAILURE SIGNAL: the observable that means stop (from the record's 失效信号)
```

A recommendation without a dose band and a stop signal is incomplete. "Use loss aversion"
is not actionable; "strong band, stop when unsubscribe rate lifts on the second send" is.

Read the record's **边界** field too. If the record's boundary rules out this context, the
mechanism is disqualified regardless of how well it fits on paper.

### Step 6: Leverage Point Ranking

Rank mechanisms qualitatively. Avoid fake numerical precision.

Evaluate each candidate on four factors:

```
Effect Size          High / Medium / Low
Evidence Grade       A / B / C  — copied from the record's **Evidence** field, not invented
Domain Fit           High / Medium / Low
Implementation Ease  Easy / Moderate / Hard
```

**The evidence grade is not a judgment call.** Copy it from the mechanism record and carry
the named source with it. If you cannot find the record, you are not ready to recommend the
mechanism.

Then assign one of these priorities:

| Priority | Action |
|----------|--------|
| High | Implement or test first |
| Medium | Strong candidate if scope allows |
| Low | Use only if especially cheap or strategic |
| Skip | Do not prioritize |

Present the top 3-5 ranked mechanisms. Be specific about WHERE in the design each applies,
and carry each one's dose band and failure signal forward from Step 5.

### Step 7: Combo Check

For each mechanism, check for powerful combinations. See `references/combo-patterns.md`.

**Always check these high-value combos:**
- Does any mechanism amplify Loss Aversion?
- Can Social Proof be layered on top of anything?
- Is there a Variable Ratio opportunity anywhere in the flow?
- Can we chain Commitment + Consistency across multiple steps?
- Does any content piece benefit from Zeigarnik + Information Gap?

Cite a combo only when the mechanism you selected is one of its members — each mechanism
record's **交互** field lists the combos it actually participates in. A combo is a
description of a real interaction, not a way to make a stack look sophisticated.

### Step 8: Domain Playbook Match

Check if a pre-built playbook applies:
- Viral/referral mechanic? → `domain-playbooks/social-commerce.md`
- Content / hook? → `domain-playbooks/content-hooks.md`
- Game or reward loop? → `domain-playbooks/games-gamification.md`
- Product feature or onboarding? → `domain-playbooks/saas-products.md`

If playbook matches, use it as the base and customize.

### Step 9: Covert-Mechanic Check (T3 and `/defend`)

Before finalizing any high-pressure design, check it against
`references/refused-domains/`. Those records document the mechanisms that are designed to
be undetectable by their target — manufactured urgency, compulsion loops, narrative
control, stakeholder pressure — with the harm they cause, how auditors detect them, the
defences that work, and the regulation that already covers them.

They exist so you can **recognise and refuse** these patterns, not produce them. If your
design is converging on one of them, that is the signal to redirect, per the Safety Gate
in SKILL.md. Cite the specific `CM-` record when you explain why a tactic is out of bounds.

---

## Scan Output Format

```text
═══════════════════════════════════════════════════
BEHAVIORAL OPPORTUNITY SCAN
═══════════════════════════════════════════════════

GOAL: [target behavior]
ACTOR: [emotional state, cognitive load, context]

FRICTION POINTS:
  [point 1] → [mechanism ID + name]
  [point 2] → [mechanism ID + name]

TOP LEVERAGE POINTS (ranked):
  1. [ID] [Model] — [where to apply] — Priority: [High/Medium/Low]
       Dose: [弱/中/强]  |  Evidence: [A/B/C — source]
       Stop when: [the record's failure signal, made specific to this flow]
  2. …
  3. …

DISQUALIFIED (why they are wrong here):
  [ID] [Model] — [the 边界 condition that rules it out]

COMBO OPPORTUNITIES:
  ⚡ [COMBO-xx] [Model A] × [Model B] → [emergent effect]

COVERT-MECHANIC CHECK:
  [nearest CM- record / none — and if close, what was redirected]

PLAYBOOK MATCH: [playbook name / none]
═══════════════════════════════════════════════════
```

The `DISQUALIFIED` block matters as much as the ranked list. A scan that only ever
produces candidates has not done the work; naming what the context rules out is what
separates a recommendation from a catalogue.

---

## Fast-Track Scan (For Mode B)

When running in Mode B (design first, annotate after), use this condensed version mentally:

1. What's the decision moment? → find the highest-leverage model
2. What's the friction? → find the barrier-removing model
3. Any social layer? → social proof / reciprocity / FOMO
4. Any reward opportunity? → variable ratio / goal gradient
5. Any content hook needed? → information gap / pattern interrupt
6. What dose, and what would tell you to stop? → the record's dose band and failure signal

Annotate the top 3-5 in the behavioral stack at the end of output. Even in fast-track, the
dose band and the stop signal travel with the recommendation.
