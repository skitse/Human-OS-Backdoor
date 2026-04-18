# Heuristics & Biases — Model Details

## HB-01 · Anchoring Effect
**Confidence**: 0.92 | **Effect Size**: Large

**Mechanism**: First numerical value encountered sets a reference point. All subsequent judgments are adjusted from this anchor — but insufficiently (adjustment is sticky).

**Cognitive chain**: Anchor exposure → selective accessibility of anchor-consistent info → insufficient adjustment → biased estimate

**Implementation**:
```
Pricing: Show highest tier first. After $999/month, $99 feels cheap.
Negotiation: Open high. The midpoint people settle on is anchored by your opening.
Donation: Show $500 as suggested, then $50 feels small but acceptable.
Ratings: Show product at "Was $299, Now $89" — $299 is the anchor.
Progress: Show "300 people have already done X" before asking user to do X.
```

**Design principles**:
- Optimization: Always introduce your desired reference point before presenting the actual offer
- Anchor with social numbers: "10,000 users rated this 4.8 stars" before asking for their rating
- Mitigation: Show multiple reference frames; require users to estimate independently before seeing anchor

**Combos**: Anchoring × Decoy Effect → premium tier makes middle tier look "reasonable"
Anchoring × Social Proof → "most popular users pay $X" anchors AND provides social validation

**Boundary conditions**:
- Weakened when: user is an expert in the domain, or when the anchor is obviously absurd
- Strengthened when: domain is uncertain, user is under time pressure, first-time decision

---

## HB-02 · Loss Aversion
**Confidence**: 0.95 | **Effect Size**: Large (2.25× loss-to-gain ratio)

**Mechanism**: Losses feel approximately 2.25× more painful than equivalent gains feel pleasurable. People will take irrational risks to avoid losses.

**Mathematical model**: v(x) = x^0.88 for gains; -2.25(-x)^0.88 for losses (Prospect Theory)

**Cognitive chain**: Outcome framed as loss → heightened emotional response → risk-seeking to avoid loss → action

**Implementation**:
```
Copy: "Don't lose your progress" > "Save your progress"
SaaS: "Your trial expires in 3 days" > "3 more days of premium"
Streak: "You'll lose your 47-day streak" > "Keep your streak"
Trial: "You lose access to [feature] on Friday" > "Your trial ends Friday"
Pricing: "$50 worth of features you're leaving behind" > "Upgrade for $50"
Social: "Others in your group have already completed this" (loss of relative position)
```

**Framing formula**:
> [What they already have] + [specific loss amount/item] + [time pressure] = maximum loss aversion

**Design principles**:
- Always reframe gains as potential losses when possible
- Make "the thing they'll lose" concrete and personalized
- Mitigation: Provide gain-framed alternatives; allow cooling-off periods; show opportunity costs

**Combos**: Loss Aversion × Social Proof → "you're the only one in your group who hasn't..."
Loss Aversion × Goal Gradient → "you've come 80% — losing this progress hurts"
Loss Aversion × Scarcity → maximum FOMO

---

## HB-03 · Default Effect
**Confidence**: 0.94 | **Effect Size**: Very Large (70-90% stick with defaults)

**Mechanism**: People systematically accept defaults. Opt-out participation rates are 30-50% higher than opt-in for equivalent programs.

**Channels**: Cognitive laziness + implicit recommendation + loss aversion (changing = risking loss) + effort asymmetry

**Implementation**:
```
Settings: Pre-check email notifications; users keep them
Subscription: Default to annual plan (users don't downgrade)
Savings: Auto-enroll in retirement contributions; only 10% opt out
Organ donation: Opt-out countries have 90%+ donation rates vs opt-in 15%
Portion size: Default meal size anchors consumption
Privacy: Use explicit choice for sharing-sensitive settings; do not hide meaningful consent in a default
```

**Design principles**:
- Set defaults to the user's safest or highest-probability-success path
- Make changing the default easy for preference changes, but require explicit choice for consent-sensitive settings
- Segmented defaults: different defaults for different user types
- Mitigation: Require active selection for high-stakes or rights-affecting decisions; document why defaults exist

**Boundary conditions**: Weakened when: decision is high-stakes and involves identity/money; users expect to customize

---

## HB-04 · Scarcity Heuristic
**Confidence**: 0.91 | **Effect Size**: Large

**Mechanism**: Limited availability signals value. Works for time, quantity, access, and social exclusivity. Perceived scarcity can drive urgency, but misleading scarcity creates trust, legal, and reputational risk.

**Types**:
1. **Quantity scarcity**: "Only 3 left in stock"
2. **Time scarcity**: "Offer expires in 2:47:32"
3. **Access scarcity**: "Invite-only" / "Waitlist"
4. **Social scarcity**: "Trending in your area right now"
5. **Information scarcity**: "Exclusive early access"

**Implementation**:
```
E-commerce: "Only 2 left" + "[X] people viewing this now"
SaaS pricing: "Founding member pricing — 47 spots remaining"
Events: "Last 8 tickets" + live countdown timer
Community: Waitlist with real queue position or clearly labeled staged access
Content: "This post will be deleted in 24 hours"
Offers: Time-limited discount with countdown
```

**Design principles**:
- Combine quantity AND time scarcity for maximum effect
- Make scarcity real and credible (users detect fake scarcity and react negatively)
- Real-time social proof of demand amplifies scarcity perception
- Mitigation: Show scarcity is real; allow opt-out; don't manufacture false urgency

**Combos**: Scarcity × Social Proof → "3 left, 8 people watching" = maximum urgency
Scarcity × Loss Aversion → the scarce thing becomes a potential loss

---

## HB-05 · Framing Effect
**Confidence**: 0.93 | **Effect Size**: Large

**Mechanism**: Identical information presented differently leads to systematically different decisions. Positive vs negative frames, absolute vs relative numbers, gain vs loss frames.

**Frame types**:
- **Gain frame**: "90% fat free"
- **Loss frame**: "Contains 10% fat"
- **Relative**: "Save 50%" vs "Save $5"
- **Social frame**: "Most users choose..."
- **Temporal frame**: "In 1 year you'll wish you started today"

**Implementation**:
```
Health: "95% survival rate" > "5% mortality rate"
Finance: "You're only spending $3/day" > "$90/month"
Progress: "You've completed 30%" vs "70% remaining"
Risk: "1 in 10 chance of success" vs "1 in 10 chance of failure" — depends on goal
Social: "Join 10,000+ people who..." > "Be among those who..."
```

**Formulas**:
- Selling → Gain frame ("what you get")
- Retention/urgency → Loss frame ("what you lose")
- Price sensitivity → Small unit frame ("$0.10 per day")
- Quality perception → Relative superlative ("top 5% rated")

---

## HB-08 · Sunk Cost Fallacy
**Confidence**: 0.88 | **Effect Size**: Large

**Mechanism**: Past investment (time, money, effort) irrationally drives future commitment beyond the point of rationality. People continue losing propositions to avoid "wasting" prior investment.

**Implementation**:
```
Games: Character progression / purchased items / leveling = sunk cost trap
SaaS: Data migration effort + setup investment = switching cost
Learning platforms: Accumulated streaks / certificates / progress = sunk cost
Social: Years of followers/content history = switching barrier
Onboarding: Invest users in setup early → they won't abandon
Group commitments: "Your team has been waiting for you"
```

**Design principles**:
- Front-load effort investment during onboarding (personalization, setup, data import)
- Create visible progress artifacts (streaks, levels, score) that feel "losable"
- Remind users of past investment at churn risk moments
- Mitigation: Allow easy export/migration; transparency about switching costs

**Combos**: Sunk Cost × Loss Aversion → "you'd be throwing away everything you've built"
Sunk Cost × Goal Gradient → "you're too close to quit now"

---

## HB-09 · Endowment Effect
**Confidence**: 0.87 | **Effect Size**: Medium-Large

**Mechanism**: People value things more once they own them. Mere possession (even temporary/virtual) increases perceived value 1.5-2×. Trial periods can create a real sense of ownership, so they should be used transparently.

**Implementation**:
```
Free trial: Give full access first; removal feels like loss (not missing gain)
Personalization: "Your" dashboard, "your" profile = ownership feeling
Game items: Give powerful item on day 1; if lost = disproportionate pain
Test drives / samples: Physical possession increases purchase likelihood 40%
"Save your work": Implicit ownership of created content
Beta access: "Your" early access = endowment
```

---

## HB-11 · Decoy Effect (Asymmetric Dominance)
**Confidence**: 0.85 | **Effect Size**: Medium-Large

**Mechanism**: Adding an asymmetrically dominated option makes the target option look more attractive. This is the classic 3-option pricing pattern.

**Classic setup**:
```
Option A (basic): $9/month
Option B (pro): $19/month        ← target
Option C (enterprise): $18/month ← decoy (close to B but worse)

→ Option B now looks like "best value"
```

**Implementation**:
```
Subscription tiers: Annual plan that makes monthly look expensive
Size options: Medium positioned as "value"
Feature bundles: Include decoy bundle that makes target bundle look complete
Event tickets: VIP decoy makes "premium" look reasonable
```

---

## HB-13 · Hyperbolic Discounting
**Confidence**: 0.86 | **Effect Size**: Medium-Large

**Mechanism**: People heavily discount rewards that are slightly delayed, but relatively little for delays far in the future. "Now" is worth dramatically more than "later."

**The gap**: $10 now vs $11 in a week → take $10 (irrational). $10 in 52 weeks vs $11 in 53 weeks → prefer $11 (patient). Same delay, different temporal distance.

**Implementation**:
```
Freemium: "Use premium NOW free for 30 days" (now > later)
Instant delivery: Prime's power is pure hyperbolic discounting
Buy now pay later: Gratification now, pain later (requires strong transparency safeguards)
Immediate unlock: "Get access instantly" > "Get access tomorrow"
App permissions: "Grant access now to use feature" — now bias drives approval
Flash sales: The "now" price vs "later" price gap amplifies present bias
```

**Design principles**:
- Make reward immediate, even if small
- Delay costs/pain as much as possible
- "Start free, pay later" models are built entirely on this mechanism
