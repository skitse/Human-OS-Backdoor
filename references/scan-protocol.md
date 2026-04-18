# Behavioral Opportunity Scan Protocol

Used in Mode C (`/scan`) and Mode D (`/deep`) before generating any design.
This protocol systematically identifies ALL applicable behavioral leverage points.

---

## The 7-Step Scan

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
  → MR-10 Loss Frame (losing progress > gaining progress)
  → MR-03 Habit Loop (tie action to existing cue)

Does the user need to invite others / share?
  → SD-02 Reciprocity (give them something to give)
  → SD-13 Gossip/Signaling (make sharing = social currency)
  → HB-04 Scarcity (exclusive access for sharer)
  → SD-10 FOMO (show what non-sharers are missing)

Is the content / hook not working?
  → PA-02 Pattern Interruption (break expected format)
  → AD-10 Information Gap (create knowledge gap)
  → PA-01 Processing Fluency (reduce cognitive friction)
  → AD-04 Emotional Contagion (lead with peak emotion)

Pricing / offer not converting?
  → HB-01 Anchoring (show high price first)
  → HB-11 Decoy Effect (add asymmetric middle option)
  → HB-02 Loss Aversion (what they lose by not buying)
  → HB-09 Endowment Effect (free trial with personalization)
```

### Step 5: Leverage Point Ranking

Rank mechanisms qualitatively. Avoid fake numerical precision.

Evaluate each candidate on four factors:

```
Effect Size          High / Medium / Low
Confidence           High / Medium / Low
Domain Fit           High / Medium / Low
Implementation Ease  Easy / Moderate / Hard
```

Then assign one of these priorities:

| Priority | Action |
|----------|--------|
| High | Implement or test first |
| Medium | Strong candidate if scope allows |
| Low | Use only if especially cheap or strategic |
| Skip | Do not prioritize |

Present the top 3-5 ranked mechanisms. Be specific about WHERE in the design each applies.

### Step 6: Combo Check

For each mechanism, check for powerful combinations. See `references/combo-patterns.md`.

**Always check these high-value combos:**
- Does any mechanism amplify Loss Aversion?
- Can Social Proof be layered on top of anything?
- Is there a Variable Ratio opportunity anywhere in the flow?
- Can we chain Commitment + Consistency across multiple steps?
- Does any content piece benefit from Zeigarnik + Information Gap?

### Step 7: Domain Playbook Match

Check if a pre-built playbook applies:
- Viral/referral mechanic? → `domain-playbooks/social-commerce.md`
- Content / hook? → `domain-playbooks/content-hooks.md`
- Game or reward loop? → `domain-playbooks/games-gamification.md`
- Product feature or onboarding? → `domain-playbooks/saas-products.md`

If playbook matches, use it as the base and customize.

---

## Scan Output Format

```
═══════════════════════════════════════════════════
BEHAVIORAL OPPORTUNITY SCAN
═══════════════════════════════════════════════════

GOAL: [target behavior]
ACTOR: [emotional state, cognitive load, context]

FRICTION POINTS:
  [point 1] → [mechanism]
  [point 2] → [mechanism]

TOP LEVERAGE POINTS (ranked):
  1. [Model] — [where to apply] — Priority: [High/Medium/Low]
  2. [Model] — [where to apply] — Priority: [High/Medium/Low]
  3. [Model] — [where to apply] — Priority: [High/Medium/Low]

COMBO OPPORTUNITIES:
  ⚡ [Model A] × [Model B] → [emergent effect]

PLAYBOOK MATCH: [playbook name / none]
═══════════════════════════════════════════════════
```

---

## Fast-Track Scan (For Mode B)

When running in Mode B (design first, annotate after), use this condensed version mentally:

1. What's the decision moment? → find the highest-leverage model
2. What's the friction? → find the barrier-removing model
3. Any social layer? → social proof / reciprocity / FOMO
4. Any reward opportunity? → variable ratio / goal gradient
5. Any content hook needed? → information gap / pattern interrupt

Annotate the top 3-5 in the behavioral stack at the end of output.
