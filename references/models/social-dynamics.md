# Social Dynamics — Model Details

## SD-01 · Social Proof
**Confidence**: 0.90 | **Effect Size**: Large (30-75% conformity rates)

**Mechanism**: In uncertain situations, people use others' behavior as a signal of correct action. The more uncertain the decision, the more weight social proof carries.

**Types of social proof** (strongest to weakest for typical contexts):
1. **Similarity proof**: "People like you did X" (highest — peer group)
2. **Expert proof**: "Professionals recommend X"
3. **User proof**: "10,000 people use X"
4. **Wisdom of crowds**: "Most popular choice: X"
5. **Celebrity/Authority**: "Endorsed by X"

**Implementation**:
```
Dynamic display: "47 people bought this in the last 24 hours"
Peer-specific: "3 of your LinkedIn contacts use this"
Consensus: "87% of users chose the annual plan"
Real-time: "12 people are viewing this right now"
Near-peer: "People in [your city/industry] chose X"
Rating clusters: "★★★★★ 4.8 from 2,847 reviews"
Progress: "10,347 people have completed this course"
```

**Amplification factors**:
- Recency ("in the last hour" > "last month")
- Similarity ("in your industry" > "users")
- Specificity (exact numbers > round numbers, e.g., "847" > "hundreds")
- Proximity (people you know > strangers)

**Combos**: Social Proof × Loss Aversion → "you're the last one in your group without X"
Social Proof × Scarcity → "3 left and 12 people watching"

---

## SD-02 · Reciprocity Norm
**Confidence**: 0.92 | **Effect Size**: Large

**Mechanism**: Receiving a gift — even unsolicited — creates a psychological obligation to reciprocate. The rule of reciprocity is one of the most powerful compliance triggers in human society.

**Key findings**:
- Unsolicited gifts work as well as solicited ones
- Size of gift matters less than the fact of giving
- Personalized gifts create stronger obligation than generic ones
- The rule operates even when we're aware of it

**Implementation**:
```
Free value first: Free tool / template / report before asking for email
Samples: Free taste → purchase obligation (supermarkets, SaaS trials)
Content: Provide substantial free value; paid product feels like reciprocating
Service: Unexpected upgrade / gesture → review / referral obligation
Community: Personal message from founder → high open rate + loyalty
Gift economy: Invite-only access as "gift" to early users
Personalized note: Handwritten or clearly personalized message in shipment
```

**Reciprocity in virality**:
> Give users something worth sharing → they feel obligated to share

**Design principles**:
- Give before you ask; always establish value first
- Make the gift visible and attributed ("This is my gift to you personally")
- Personalization increases obligation 2-3×
- Mitigation: Make it clear gifts are freely given, no obligation required

---

## SD-03 · Commitment & Consistency
**Confidence**: 0.91 | **Effect Size**: Large

**Mechanism**: Once people make a commitment (especially public or written), they feel psychological pressure to be consistent with that position. Small commitments create the foundation for larger ones (foot-in-the-door).

**Commitment escalation ladder**:
```
Micro-commitment (cognitive) → Small behavioral commitment →
Public commitment → Social commitment → Identity commitment
```

**Implementation**:
```
Onboarding: "What's your #1 goal?" → answer → now they're committed to that goal
Public pledge: "Share your commitment to X with friends" → social accountability
Step 1 of onboarding → commits to completing → sunk cost builds
Waitlists: Signing up = micro-commitment → primes for purchase
Quiz: "Based on your answers, you're a [type]" → identity commitment
Goals: "You set a goal to do X by [date]" → reminder = consistency trigger
Community: Public statement of intent in group chat → peer accountability
```

**The foot-in-the-door technique**:
1. Ask for tiny favor (share email, answer 1 question, like post)
2. Follow up with larger request
3. Conversion rate 2-3× higher than direct ask

**Design principles**:
- Make early commitments easy and low-cost
- Make commitments public whenever possible
- Reference prior commitments when asking for next step
- Mitigation: Allow easy withdrawal; never lock users into commitments they regret

---

## SD-04 · Authority Bias
**Confidence**: 0.88 | **Effect Size**: Large

**Mechanism**: People defer to authority figures or credential signals, often without evaluating the actual content. Authority can be real or symbolic.

**Authority signals** (strongest to weakest):
- Official credentials (Dr., PhD, "Harvard")
- Social proof of expertise (# of followers, published work)
- Physical/design signals (professional photo, quality design)
- Association signals (endorsed by X brand)
- Linguistic signals (confident, specific language)

**Implementation**:
```
Testimonials: Use job titles and companies, not just names
Case studies: "Used by [Fortune 500 company]" adds authority transfer
Content: "Research shows..." / "According to studies..." increases compliance
Design: High-quality visuals signal authority before content is read
Trust signals: SSL badges, press logos, partner logos
Credentials: Display certifications, awards, press features prominently
Author bio: Show expertise before asking for behavior change
Language: Specific numbers ("83% of users") > vague claims ("most users")
```

---

## SD-06 · Network Effects
**Confidence**: 0.93 | **Effect Size**: Very Large

**Mechanism**: Product value increases super-linearly with user count. At critical mass, growth becomes self-sustaining. Below critical mass, products fail regardless of quality.

**Types**:
1. **Direct network effects**: Value = f(number of users) — messaging apps, social networks
2. **Indirect network effects**: Value from complementary goods — platforms, marketplaces
3. **Data network effects**: More users → better AI/recommendations → more users

**Critical mass tactics**:
```
Geographically constrain launch (Uber city by city)
Target a specific community first (Facebook → Harvard → colleges)
Create artificial density (show "local" users even if sparse)
Subsidize one side of marketplace (Uber subsidized drivers first)
Seed with known users (show friends who are on platform)
```

**Design principles**:
- Make the network visible ("X of your friends use this")
- Reward users for bringing others into the network
- Show the user what they're missing by not having their network on platform

---

## SD-10 · FOMO (Social Scarcity Composite)
**Confidence**: 0.92 | **Effect Size**: Large — this is a COMBO of SD-01 × HB-02 × HB-04

**Mechanism**: Fear of Missing Out = Loss Aversion applied to social exclusion. The pain of being left out of something your peers are experiencing. Most powerful viral mechanic.

**FOMO architecture**:
```
1. Show peers engaging in desirable activity
2. Make activity look effortless and rewarding
3. Create visible in-group / out-group boundary
4. Add time pressure (you can join NOW, but window closes)
5. Show what in-group members get that out-group doesn't
```

**Implementation**:
```
Streaks: "Your friends maintained their streaks. You broke yours."
Groups: "Your team completed the challenge. You're the only one who didn't."
Events: "17 people from your network attended [event] last week"
Products: "Your colleagues are using [feature] you haven't tried"
Content: "Everyone is talking about X — here's what you're missing"
Exclusive: "Members got early access to X. Non-members didn't."
```

**Virality formula**:
> FOMO = (Visibility of peer participation) × (Desirability of experience) × (Perception of exclusivity)

---

## SD-14 · Status Signaling
**Confidence**: 0.88 | **Effect Size**: Large

**Mechanism**: Humans are deeply wired for status within hierarchies. Visible status markers drive aspirational purchase and behavior independent of functional utility.

**Status mechanics in products**:
```
Levels/tiers: Gold/Platinum/Diamond member tiers
Badges/achievements: Visible to others in community
Leaderboards: Public ranking creates aspiration + competition
Exclusive access: "Pro member only" rooms/features
Customization: Profile items that signal investment/skill
Early adopter markers: "Member since 2019" = higher status
Top contributor: Community recognition programs
```

**Design principles**:
- Make status visible to others (meaningless if private)
- Create multiple status dimensions (not just top 1% — everyone can have some status)
- Allow users to display status in external contexts (badges, shareable achievements)

---

## SD-15 · Social Comparison
**Confidence**: 0.89 | **Effect Size**: Large

**Mechanism**: People evaluate themselves relative to nearby peers. Upward comparison (looking at better performers) drives motivation. Downward comparison (looking at worse performers) drives satisfaction.

**Design principle**: Show users slightly-above-average comparison targets to drive motivation without inducing helplessness.

**Implementation**:
```
Leaderboards: Show top 10 + user's rank + person just above them
Progress: "You're ahead of 73% of users who started the same week"
Benchmarks: "Average user completes this in 3 days. You're on day 2."
Cohort: "Your cohort's average score is X. Yours is Y."
Asymmetric: Show the gap to close, not the gap from below
```

**Warning**: Upward comparison where the gap is too large → helplessness and abandonment.
Show "nearby achievable" comparisons, not aspirational/impossible ones.
