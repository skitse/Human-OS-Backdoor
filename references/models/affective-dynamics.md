# Affective Dynamics — Model Details

## AD-01 · Variable Ratio Reinforcement
**Confidence**: 0.97 | **Effect Size**: Extreme (highest of all behavioral mechanisms)

**Mechanism**: Rewards delivered on an unpredictable schedule create the strongest and most resistant-to-extinction behavior patterns. This is the slot machine effect — the uncertainty itself is the reward.

**Schedule comparison** (extinction resistance):
```
Fixed ratio (every Nth action):    Low resistance — stops immediately when reward stops
Fixed interval (every N minutes):   Low resistance — behavior spikes just before reward
Variable ratio (unpredictable):     MAXIMUM resistance — behavior persists indefinitely
Variable interval (unpredictable):  High resistance
```

**Why it works**: Dopamine fires not just on reward delivery but on REWARD ANTICIPATION. Variable schedules keep dopamine system in constant anticipatory state.

**Implementation**:
```
Pull-to-refresh: Will there be new content? (variable reward) -> frequent checking
Loot boxes: Unknown reward → open one more
Feed scroll: Each scroll might reveal something interesting → infinite scroll
Push notifications: Might be something important → always check
Game drops: Rare item might appear → keep grinding
Email check: Might be important news -> frequent checking
Dating apps: Swipe → might match → keep swiping
Flash sales: Might be a great deal → check daily
```

**Design principles**:
- Variable rewards can increase engagement, but they should be used carefully and transparently
- Make reward checks cheap only when repeated checking is genuinely aligned with user value
- Avoid uncertainty loops that mainly increase reflexive checking without improving outcomes
- Mitigation: Fixed schedules and transparent reward systems reduce compulsion risk

**Combos**: Variable Ratio × Goal Gradient -> "almost there" + uncertain timing increases re-engagement pressure
Variable Ratio × Zeigarnik → incompleteness + uncertainty = maximum mental occupation

---

## AD-02 · Zeigarnik Effect
**Confidence**: 0.88 | **Effect Size**: Medium-Large

**Mechanism**: People remember and think about incomplete tasks far more than completed ones. Incompleteness creates a persistent cognitive loop demanding resolution.

**The tension**: Starting something creates a "task tension" that doesn't resolve until completion. This tension is aversive — people feel compelled to complete what they've started.

**Implementation**:
```
Onboarding: "Your profile is 60% complete" → visible incomplete state
Progress bars: Explicitly show what's missing, not just what's done
Courses: "3 of 7 lessons complete" → the 4 missing ones nag
Series: Cliffhanger episode endings → must watch next
Email sequences: "Part 2 of 5" → implies 4 incomplete parts
Checkout: "You left items in your cart" → abandoned = incomplete
Reading: "5 min read" shown upfront → start = commit to finish
Games: Quest log with incomplete items → must return to finish
```

**The cliffhanger formula**:
> Start an arc → introduce tension → cut before resolution → re-engagement is automatic

**Design principles**:
- Make incompleteness visible and salient
- Make completing the action cheap (low effort)
- Time the incompleteness reminder at re-engagement moments
- Mitigation: Allow easy "dismiss" / "mark complete later" options

**Combos**: Zeigarnik × Information Gap → "you won't know the outcome until you return"
Zeigarnik × Loss Aversion → "your progress will expire if you don't complete"

---

## AD-03 · Peak-End Rule
**Confidence**: 0.84 | **Effect Size**: Medium-Large (Kahneman's most replicated finding)

**Mechanism**: People's memory of an experience is determined primarily by:
1. The peak emotional moment (most intense, positive or negative)
2. The ending moment

The duration of the experience barely matters ("duration neglect").

**Formula**: Memory(experience) ≈ (Peak + End) / 2

**Implications**:
- A good experience ending badly is remembered worse than a shorter good experience
- A mediocre experience with a great ending is remembered better than it was
- You can recover a bad experience with a strong ending

**Implementation**:
```
Onboarding: End with a "magic moment" (the aha moment) → first impression memory
Purchase confirmation: End with celebration / social share → positive last memory
Customer service: Resolve the issue AND add unexpected positive gesture at end
Product exits: "Are you sure you want to cancel?" + show achievement summary
Courses: Graduation ceremony / certificate at end → peak memory
Event: Save best speaker / moment for near-end
Email: Strong CTA or value at end, not just in middle
App session end: "You achieved X today" → positive ending memory
```

---

## AD-06 · Fear/Threat Response
**Confidence**: 0.90 | **Effect Size**: Large

**Mechanism**: Threat perception activates fight-or-flight response, which heightens loss aversion and drives immediate action. Fear is the most powerful short-term motivator.

**Three fear types**:
1. **Loss fear**: "You'll lose [specific thing]"
2. **Social fear**: "Others will judge/exclude you"
3. **Existential fear**: "Your future self will regret this"

**Implementation**:
```
Loss fear: "Your 30-day streak ends tonight if you don't complete today's lesson"
Social fear: "Your competitor just added this feature"
Regret fear: "By 2025, people who didn't learn [skill] will earn 40% less"
Security fear: "Your account shows suspicious login activity" (then upsell 2FA)
Health: "People with your habits have 3× higher risk of X"
Financial: "At your current rate, you'll run out of savings in 8 years"
```

**The threat-action-relief loop**:
> Introduce threat → create urgency → offer solution → relief from resolving fear

**Warning**: Fear appeals must be paired with a clear, achievable solution. Fear without path = paralysis, not action. High-fear + low-efficacy → denial and avoidance.

**Calibration**: Use fear for retention and urgency, not for first impressions (trust builds before fear).

---

## AD-08 · Flow State
**Confidence**: 0.87 | **Effect Size**: Large (Csikszentmihalyi)

**Mechanism**: Optimal experience occurs at the intersection of high skill and high challenge. In flow: time distorts, self-consciousness disappears, intrinsic motivation peaks.

**Flow conditions**:
- Clear goals with immediate feedback
- Challenge level slightly above current skill (optimal difficulty)
- No distractions or interruptions
- Sense of control over outcomes

**Flow curve**:
```
Challenge too low → Boredom → Disengagement
Challenge matches skill → Flow → Total absorption
Challenge too high → Anxiety → Abandonment
```

**Implementation**:
```
Games: Dynamic difficulty adjustment to maintain optimal challenge
Learning apps: Adaptive difficulty based on performance
UX: Remove all friction from primary task; minimize cognitive interruptions
Onboarding: Gradual complexity ramp — don't overwhelm early, don't bore later
Writing tools: Distraction-free modes, word count that provides clear goal
Fitness: Progressive overload + immediate feedback (reps, time, weight)
Music: Playlist curation for task type (beat syncs with cognitive load)
```

---

## AD-10 · Curiosity / Information Gap
**Confidence**: 0.89 | **Effect Size**: Large (Loewenstein's Information Gap Theory)

**Mechanism**: When people become aware of a gap between what they know and what they WANT to know, they experience curiosity as an aversive state they're motivated to resolve.

**The gap formula**: Curiosity = Awareness of gap × Desire to close gap

**Key insight**: You can't create curiosity about things people don't care about. But for relevant topics, even a tiny hint of "there's more to know" creates powerful drive.

**Implementation**:
```
Headlines: "The one mistake that kills most startups" → gap: what mistake?
Subject lines: "I shouldn't be sharing this, but..." → gap: what is it?
Thumbnails: Show reaction/result without showing cause
Cliffhangers: "Part 2 reveals why this didn't work"
Progress: "70% of users discover something that surprises them in section 3"
Numbers: "The 3 things that account for 80% of outcomes" → read to find out
Teasers: "Here's what happened after 90 days..." (with image showing surprising result)
UI: "You've unlocked something. Check your profile."
```

**Curiosity loop anatomy**:
> Establish known → hint at unknown → create gap → provide path to close gap

**Combos**: Information Gap × Zeigarnik -> incomplete + unknown creates strong return pressure
Information Gap × Variable Ratio -> repeated "maybe there's something new" checking pressure
