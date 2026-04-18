# Motivation & Self-Regulation — Model Details

## MR-01 · Goal Gradient Effect
**Confidence**: 0.88 | **Effect Size**: Large (Hull's drive theory, confirmed digitally)

**Mechanism**: Effort and motivation increase as people approach a goal. Velocity accelerates in the final stretch. Critically: pseudo-progress (artificial head start) triggers the same acceleration.

**Pseudo-progress finding (Nunes & Drèze, 2006)**:
Car wash loyalty card study: "Collect 10 stamps, get free wash" vs "Collect 12 stamps, already have 2."
Both require 10 more stamps. BUT: pseudo-progress card had 2× completion rate.

**Implementation**:
```
Loyalty programs: "You've already earned 200 of 1000 points" (even from thin air)
Onboarding: Show profile at 30% complete before user does anything
Progress bars: Design so early steps move bar quickly
Gamification: Give starting XP bonus on day 1
Distance framing: "You're only 3 items away from your goal"
Countdowns: "Just 2 more to unlock [reward]"
Streaks: Early streak "bonus" to get them started
Learning: Pre-completed first lesson ("You've already started!")
```

**The acceleration principle**:
> Last 20% of progress → 2-3× more effort than first 20%

**Design principles**:
- Compress early progress (feel faster) to build momentum
- Show distance-to-goal prominently as completion nears
- Add extra incentives at the near-completion point ("you're so close — bonus reward for finishing")
- Mitigation: Don't inflate pseudo-progress so much it feels deceptive when users realize it

---

## MR-03 · Habit Loop
**Confidence**: 0.91 | **Effect Size**: Very Large (Duhigg / MIT research)

**Mechanism**: Behaviors become automatic through repeated association of: Cue → Routine → Reward. Once formed, habits run without conscious decision. Cue alone can trigger the full loop.

**The loop**:
```
CUE (trigger) → ROUTINE (behavior) → REWARD (positive reinforcement)
    ↑                                          |
    └──────────────────────────────────────────┘
```

**Cue types**:
1. Time: 7am, Monday morning, after lunch
2. Location: in bed, at desk, in car
3. Emotional state: anxious, bored, procrastinating
4. Preceding action: after coffee, after gym, after waking
5. Other people: seeing certain person, phone buzz

**Implementation**:
```
App: Design for existing cue (morning = news; bathroom = social; commute = podcasts)
Notifications: Trigger at existing habit cue time (not random)
Habit stacking: "After you [existing habit], do [new habit]"
Onboarding: Ask "When do you usually [existing behavior]?" → set reminder for that time
Reward design: Make reward immediate and obvious (animation, sound, number increase)
Streak mechanics: Make breaking streak emotionally painful (cue becomes checking streak)
Social habits: Friend activity as cue to re-engage
```

**Keystone habits**: Some habits create cascading changes (exercise → diet → sleep → mood). Find and target these.

---

## MR-04 · Identity-Based Commitment
**Confidence**: 0.87 | **Effect Size**: Large (James Clear / Fogg research)

**Mechanism**: "I am X" drives behavior more powerfully than "I do X" or "I want X." Identity is the most persistent motivation because abandoning behavior = abandoning identity.

**Hierarchy of behavior change drivers**:
```
Weakest: Outcomes ("I want to lose weight")
Medium:  Process ("I'll go to gym 3x/week")
Strongest: Identity ("I am an athlete")
```

**Identity shift formula**:
> Small win → evidence for new identity → stronger identity → more behavior in service of identity

**Implementation**:
```
Labels: "You're a top contributor" → they behave like one
Onboarding: "What kind of [user] are you?" + assign identity label
Streaks: "You're a daily learner" (after X days) → identity label
Levels: Level-up = identity change ("You're now a Pro member")
Community: Membership in named group ("Founding members", "Power users")
Badges: Visible identity markers that they wear in community
Personalization: "People like you (Data Scientists) typically do X"
Quizzes: "Your learning style is X" → now they act consistently with it
```

---

## MR-05 · Self-Determination Theory (SDT)
**Confidence**: 0.85 | **Effect Size**: Large (Deci & Ryan)

**Three core needs** for intrinsic motivation:
1. **Autonomy**: Sense of volition; doing things because YOU chose to
2. **Competence**: Feeling effective and capable; mastery progression
3. **Relatedness**: Connection to others; belonging; being cared for

**Why extrinsic rewards backfire (Overjustification Effect)**:
When you pay someone to do what they loved doing freely, they stop loving it. Extrinsic rewards can DECREASE intrinsic motivation.

**Design principles**:
```
Autonomy:
  - Offer choice in how to accomplish goal (path options)
  - Avoid controlling language ("you must" → "you can")
  - Rationale provision: explain WHY, not just what

Competence:
  - Match challenge to skill (flow curve)
  - Immediate, specific feedback
  - Progress visibility
  - Allow failure → recovery → mastery narrative

Relatedness:
  - Human connection in product (real faces, names)
  - Community features
  - Shared goals and celebrations
  - Acknowledgment of user contributions
```

---

## MR-06 · Progress Momentum (Pseudo-Progress Effect)
**Confidence**: 0.87 | **Effect Size**: Large

**Mechanism**: Just SHOWING a progress bar — even with artificial early progress — triggers goal gradient acceleration. People who feel they've started something are more likely to complete it.

**The endowed progress effect**: People given a head start (even fake) work harder and complete more than those starting at 0%.

**Implementation**:
```
Profile completion: Start new users at 20% (bio empty but "photo added" credited)
Onboarding: "Step 1 of 5 complete" shown after just viewing intro screen
Loyalty: Award points for account creation / first login
Gamification: Give 100XP starting bonus "for joining"
Courses: "Introduction complete (1/10)" after 2-minute welcome video
Progress bars: Design so first 3 actions fill bar to 50%
Challenges: "You've completed Day 0 — Day 1 starts tomorrow"
```

---

## MR-11 · Near-Miss Effect
**Confidence**: 0.89 | **Effect Size**: Large

**Mechanism**: Nearly achieving a goal or nearly winning a reward creates stronger motivation for re-engagement than completely missing. "So close!" feels motivating, not demoralizing (within range).

**Why it works**: Near-miss activates counterfactual thinking ("I almost had it") → creates specific, achievable path to next attempt.

**Implementation**:
```
Games: Slot machine shows "almost winning" symbols
Loot: Rare item drop at 1% — show "you were this close" meter
Progress: "You were 50 points away from Gold status this month"
Competitions: "You finished 4th out of 100" (podium miss = motivating)
Sales: "This deal expired 3 hours before you checked" → urgency for next
Challenges: "Your streak ended at 29 days — one day away from 30!"
Learning: "You scored 78% — 2 more correct and you'd have earned the badge"
```

**Warning**: Near-miss only motivates when:
- The goal felt achievable
- The gap is small and specific
- Another attempt is available soon

If the goal felt impossible or the loss is ambiguous, near-miss just feels like loss.

---

## MR-12 · Reward Variability
**Confidence**: 0.93 | **Effect Size**: Extreme

See AD-01 (Variable Ratio Reinforcement) — this is the motivational perspective of the same mechanism.

**Key insight for design**: Don't make reward schedules predictable. The unpredictability IS the engagement mechanic.

**Spectrum**:
```
Fixed → Variable → Random
Low engagement → High engagement → Maximum compulsion (ethical threshold)
```

**Ethical design**: Variable schedules create the most engagement but also the most compulsive behavior. Design with explicit intention about where on this spectrum you want to sit.
