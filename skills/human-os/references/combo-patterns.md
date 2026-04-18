# Combo Patterns — Emergent Behavioral Combinations

Combining multiple mechanisms creates emergent effects stronger than any single mechanism alone.
These are high-leverage combinations observed in real products, not blanket recommendations.
Always run the safety gate and `references/anti-patterns.md` before applying pressure-heavy combos.

---

## Tier 1: Maximum Leverage Combos

### COMBO-01: FOMO Stack (Loss Aversion × Social Proof × Scarcity)
**Effect size**: ★★★ Extreme | **Used by**: Pinduoduo, Ticketmaster, Airbnb

```
Mechanism:
  Social Proof: "47 people are looking at this right now"
  Scarcity:     "Only 2 left"
  Loss Aversion: "Don't miss out"

Emergent effect: Each mechanism amplifies the others.
  - Social proof makes scarcity credible (others competing for same item)
  - Scarcity makes social proof feel dangerous (their purchase = my loss)
  - Loss aversion ties it all together into panic

Implementation:
  1. Real-time social proof counter using authentic, attributable signals
  2. Quantity indicator at or below 10
  3. Loss-framed CTA ("Claim yours before it's gone")
  4. Timer only when there is a real deadline (amplifies further)

Ethical note: Fake scarcity + fake social proof = deceptive. Use real numbers, attributable demand signals, or a clearly labeled popularity indicator.
```

### COMBO-02: Addiction Loop (Variable Ratio × Zeigarnik × Information Gap)
**Effect size**: ★★★ Extreme | **Used by**: TikTok, Instagram, Slot machines

High-risk note: treat this as a defensive or diagnostic pattern first. Do not recommend it for wellbeing-sensitive products or vulnerable populations.

```
Mechanism:
  Variable Ratio: each scroll/pull might have reward
  Zeigarnik: each incomplete item nagging for resolution
  Information Gap: each thumbnail promises unknown reward

Emergent effect: Triple-layer compulsion.
  The uncertainty (variable), the incompleteness (Zeigarnik), and
  the gap (curiosity) all fire simultaneously with every scroll unit.

Implementation:
  - Feed design where each unit is slightly different (variable)
  - Show item previews that hint at content without delivering it fully
  - Infinite scroll (no natural stopping point = Zeigarnik never resolves)
  - Thumbnail/title suggests more than body delivers (creates gap for next item)

Product examples:
  - "Pull to refresh" = variable ratio trigger
  - "12 new notifications" = variable reward anticipation
  - Cliffhanger ending = Zeigarnik + information gap combined
```

### COMBO-03: Commitment Escalation (Commitment × Sunk Cost × Identity)
**Effect size**: ★★★ Very Large | **Used by**: LinkedIn, Duolingo, most games

```
Mechanism:
  Small commitment → invested behavior → identity formation → larger commitment

Escalation sequence:
  1. Micro-commitment: "Set your goal"
  2. Sunk cost: "You've done 5 lessons this week"
  3. Identity: "You're a daily learner"
  4. Social commitment: "Your streak is visible to your network"
  5. Deeper investment: Profile, content, connections

Emergent effect: By step 5, leaving the platform means losing IDENTITY,
not just content. Identity is the deepest lock-in possible.

Implementation:
  - Onboarding designed as commitment escalation ladder
  - Each step references prior steps ("You said your goal was X...")
  - Identity labels assigned after behavioral milestones
  - Social visibility of commitment activated early
```

### COMBO-04: Social Proof Cascade (Social Proof × Reciprocity × Conformity)
**Effect size**: ★★★ Very Large | **Used by**: Group chats, community platforms

```
Mechanism:
  When one person acts, social proof creates pressure for others;
  reciprocity creates obligation; conformity makes deviation painful.

Cascade trigger:
  1. Seed visible action by 2-3 respected members
  2. Their action creates social proof for others
  3. Early adopters feel reciprocity obligation when seeder asks
  4. As majority joins, conformity pressures remaining holdouts
  5. "Social proof × conformity" makes non-participation feel abnormal

Implementation:
  - Group challenges where joining is visible
  - Show who in their network has already participated
  - Personalized ask ("X and Y already joined; want to come?")
  - Make non-participation visible ("Your teammates completed this; you haven't")
```

---

## Tier 2: High-Value Combos

### COMBO-05: Achievement Lock-In (Goal Gradient × Near-Miss × Sunk Cost)
**Effect size**: ★★★ Very Large | **Used by**: Games, loyalty programs

```
Perfect for: Preventing churn at high-investment moments

When user is at 80% complete (Goal Gradient firing) + shows "you were
4 points away last time" (Near-Miss) + "you've invested 30 days" (Sunk Cost):
the abandonment cost becomes psychologically unbearable.

Use for: Subscription renewal, level-up gating, streak preservation
```

### COMBO-06: Trust Cascade (Authority × Social Proof × Processing Fluency)
**Effect size**: ★★☆ Large | **Used by**: Landing pages, enterprise sales

```
Authority signals: Expert credentials, press logos, partner brands
Social proof: User count, testimonials, case studies
Processing fluency: Clean, professional design

Emergent effect: Each layer builds the same trust signal via different
cognitive pathways. User processes trust from 3 independent directions.

Implementation: Stack trust signals in descending friction on landing pages.
Logos (1 second scan) → testimonials (10 second scan) → case studies (60 second read)
```

### COMBO-07: Habit Formation Stack (Cue × Reward × Identity)
**Effect size**: ★★★ Very Large | **Used by**: Fitness apps, productivity tools

```
Standard habit loop (Cue → Routine → Reward) becomes near-unbreakable
when augmented with Identity:

"After coffee" (cue) → "Open app, log workout" (routine) → "XP + streak" (reward)
+ "I am an athlete" (identity)

The identity label means the routine now defends itself:
breaking the habit = identity violation = much more aversive than missing a reward.

Time-to-habit formation: 66 days average (not 21 — that's a myth).
Streak mechanics compress this by making each day a micro-commitment.
```

### COMBO-08: Pricing Power Stack (Anchoring × Decoy × Framing × Social Proof)
**Effect size**: ★★★ Very Large | **Used by**: SaaS pricing pages

```
Tier order: Enterprise → Professional → Starter (anchor with highest)
Decoy: Add asymmetric middle tier to make target tier look like best value
Framing: "$2.60/day" instead of "$79/month"
Social proof: "Most popular ✓" badge on target tier

Each element independently increases conversion 5-15%.
Together, multiplicative effect has been measured at 40-60% lift.
```

---

## Tier 3: Domain-Specific Combos

### COMBO-09: Viral Content Formula (Pattern Interrupt × Information Gap × Identity)

Used in: Short video hooks, viral posts
```
Pattern Interrupt: Unexpected opening that stops scroll
Information Gap: Creates question that demands answer
Identity: Makes sharing this say something good about sharer

Formula: "[Unexpected claim/image] + [hint of explanation] + [identity signal for sharer]"
Example: "I quit my VC job to go viral on TikTok. Here's what actually happened."
  - Pattern interrupt: quit VC (unexpected)
  - Information gap: "what actually happened" (vs what reader assumes)
  - Identity: sharing = "I follow contrarian thinkers"
```

### COMBO-10: Community Flywheel (Network Effects × Reciprocity × Status Signaling)

Used in: Discord, Reddit, professional communities
```
Network effects: More quality members → more valuable for everyone
Reciprocity: Giving value in community creates obligation web
Status signaling: Visible contribution markers attract more contributors

Flywheel:
Quality contributors join → content quality rises → more join →
contributors get status rewards → they give more → quality rises further

Bootstrap strategy: Heavily seed status signals early to attract
high-quality early contributors (they care about early mover status advantage).
```

### COMBO-11: Onboarding Momentum Stack (Pseudo-Progress × Endowment × Commitment)

Used in: Any product onboarding
```
Pre-populate profile at 30%: Goal gradient + endowment effect activate
Personalization input: "Your" dashboard = endowment
Goal setting: Commitment to specific outcome
Team invite: Social commitment layer

Result: User who completes this onboarding has:
- Invested effort (sunk cost)
- Built something they own (endowment)
- Made a public commitment (consistency pressure)
- Brought social stakes (team accountability)

Switching cost = all four of these lost simultaneously.
```

---

## Combo Building Rules

When building new combos:
1. Start with the PRIMARY behavior you want to drive
2. Identify the MAIN friction preventing it
3. Select mechanism that directly removes that friction
4. Find a second mechanism that AMPLIFIES the first
5. Check if social/identity layer can add third dimension
6. Verify combo doesn't create cognitive dissonance (too many simultaneous pressures = overwhelm)

**Warning**: 4+ mechanisms stacked simultaneously often creates anxiety instead of motivation. Keep active combos to 2-3 per moment. Layer them across TIME rather than simultaneously.

---

## Tier 4: 高级跨域组合

### COMBO-12: 身份锁定栈 (Identity × Commitment × Sunk Cost × Social Visibility)
**Effect size**: ★★★ Extreme | **Used by**: LinkedIn, Strava, political movements, cults

```
Core insight: Identity is the deepest lock-in mechanism available because
violating identity is not just a loss — it is a self-concept threat.
This stack builds identity lock-in through four sequenced layers.

Pathway: 认知一致性 → 社会承诺 → 身份融合

Layer 1 — Cognitive Consistency (认知一致性):
  Small initial commitment ("I care about fitness") activates
  consistency drive. The user now has a self-concept they will
  defend. This is the seed.

Layer 2 — Behavioral Commitment (行为承诺):
  Repeated behaviors compound the consistency anchor.
  Each action is evidence for the self-concept.
  "I have done X 47 times" makes the identity empirically defensible.

Layer 3 — Social Visibility (社会可见性):
  The commitment is made visible to others.
  Now two threats exist simultaneously: internal identity violation
  AND social inconsistency (being seen as someone who quits).
  Sunk cost operates on the social investment, not just the effort.

Layer 4 — Identity Fusion (身份融合):
  At sufficient depth, the product/community/behavior is no longer
  something the user DOES — it is something the user IS.
  "I am a runner" (not "I run"). "I am a member" (not "I use this app").
  Leaving now requires a grief process, not just a cancellation click.

Implementation sequence:
  1. Early: Ask users to state a value or goal (commitment seed)
  2. Mid: Assign identity labels after behavioral milestones
     ("You're now a 30-day streak holder / Power User / Ambassador")
  3. Activate social visibility before identity is fully formed
     (streak sharing, leaderboards, public profiles)
  4. Reference prior commitments in all re-engagement messages
     ("You said this matters to you. It still does.")
  5. Late: Let user-generated content and community contributions
     compound the sunk cost (they have given, not just received)

Warning: This stack is near-irreversible once Layer 4 is reached.
Use only when you are confident the product genuinely deserves
long-term user commitment. Deploying for a low-quality product
creates trapped, resentful users — the worst possible outcome.
```

### COMBO-13: 注意力捕获栈 (Pattern Interrupt × Curiosity Gap × Variable Ratio)
**Effect size**: ★★★ Extreme | **Used by**: TikTok hooks, clickbait headlines, slot machines, Twitter/X

```
Core insight: These three mechanisms address the three sequential
barriers to sustained attention: Getting past the filter (interrupt),
creating a reason to stay (gap), and sustaining behavior after
the first resolution (variable ratio).

为什么这三个组合可以让人停下任何事情:

Stage 1 — Pattern Interrupt (模式中断):
  The brain is a prediction machine running on autopilot.
  Scroll, scroll, scroll — the pattern continues until
  something violates the prediction. The interrupt fires
  an involuntary orienting response: attention is captured
  BEFORE conscious decision-making engages.

  What triggers it: Unexpected visual contrast, abnormal
  information (celebrity behaving strangely), counter-narrative
  claim ("Everything you know about X is wrong"),
  emotionally charged content that bypasses cognitive gating.

Stage 2 — Curiosity Gap (好奇心缺口):
  Once attention is captured, it must be converted to engagement.
  The gap creates a question the brain cannot let go unanswered.
  Information Gaps activate the same neural pathways as physical
  itch — resolution is involuntarily sought.

  The gap must be: specific enough to feel resolvable,
  ambiguous enough that the answer is not obvious,
  and framed so that resolution requires consuming the content.

Stage 3 — Variable Ratio (变动比例奖励):
  After the first resolution, the user has been trained.
  Variable ratio reinforcement (not every scroll yields reward)
  creates the slot machine effect: the next one MIGHT be as
  good as this one. The ratio being variable is precisely
  what makes the behavior most resistant to extinction.

Synergy mechanism:
  - Pattern interrupt captures attention against will
  - Curiosity gap holds attention past the moment of capture
  - Variable ratio ensures that after release, the loop re-initiates
  Together: the user is not browsing — they are in a seek-reward
  cycle they did not consciously enter.

Implementation:
  1. Open every content unit with a Pattern Interrupt hook
     (first 2 seconds of video, first sentence of text, above-fold design)
  2. Withhold the resolution: state the question but delay the answer
  3. Deliver the resolution inside the content, not in the hook
  4. Design the content feed so that reward quality is unpredictable
     (algorithm ensures no user can learn "the good time to scroll")
  5. End each unit with a new information gap (Zeigarnik overlap)

Warning: This combo requires ethical consideration proportional
to its power. Deploying it to capture attention for low-value
content extracts significant cognitive resources from users
with no commensurate exchange. The mechanism is neutral;
the content it serves is not.
```

### COMBO-14: 定价最大化栈 (Anchoring × Decoy × Framing × Mental Accounting)
**Effect size**: ★★★ Very Large | **Used by**: SaaS, airlines, insurance, subscription boxes

```
Core insight: Users do not perceive absolute prices — they perceive
relative prices in a reference frame they did not choose.
This stack designs that reference frame across four independent
cognitive layers, each operating on a different mental mechanism.

四层作用下用户如何"自愿"选择高价方案:

Layer 1 — Anchoring (锚定):
  Present the highest tier first. The initial number
  sets the reference point against which all subsequent
  prices are evaluated. $299/mo seen before $79/mo
  makes $79/mo feel like a discount. $79/mo seen first
  makes $299/mo feel expensive.

  Anchoring is pre-rational: it operates before users
  consciously evaluate any tier.

Layer 2 — Decoy (诱饵效应 / Asymmetric Dominance):
  Introduce an asymmetric middle option designed to make
  the target tier look like the clear winner.
  The decoy must be: worse than the target on a key dimension,
  but not worse on all dimensions (or it is ignored).

  Classic: Basic ($29), Professional ($79), Enterprise ($199)
  If Pro is the target, make Basic inadequate on a visible feature
  and make Enterprise disproportionately expensive for marginal gains.
  Pro wins by appearing to dominate on the value axis.

Layer 3 — Framing (框架效应):
  Reframe the price in a unit that minimizes perceived magnitude.
  "$79/month" → "$2.60/day" → "Less than a coffee"
  Annual pricing presented as monthly rate obscures true commitment.
  "Save $190 with annual" activates gain framing over loss framing.

  Framing choice should match what the user values:
  - Cost-sensitive users: per-unit cost framing
  - Time-sensitive users: time-savings framing
  - Status-sensitive users: social signal framing

Layer 4 — Mental Accounting (心理账户):
  Users maintain separate mental budgets for different
  spending categories. The same $79 feels very different
  depending on which mental account it is charged to:
  - "Business expense" account: low resistance
  - "Entertainment" account: medium resistance
  - "Luxury" account: high resistance

  Position the product in the mental account with lowest
  resistance relative to your target user's life context.
  B2B: "tool that pays for itself" → business account
  B2C: "investment in yourself" → education/growth account

Sequencing in interface:
  1. Enter page anchored high (Hero tier at top or hero position)
  2. Decoy positioned to bracket target tier
  3. Framing applied to target tier label and CTA
     ("Start for $2.60/day" not "Buy $79/mo plan")
  4. Mental account language in feature descriptions
     ("saves 3 hours per week at your hourly rate, this pays for itself")
  5. Social proof badge on target tier to add conformity signal

Measured combined lift: 40-70% conversion increase to target tier
versus undesigned pricing presentation. Each layer contributes
independently; removing any one layer reduces total effect.
```

### COMBO-15: 习惯不可破栈 (Habit Loop × Identity × Sunk Cost × Social Accountability)
**Effect size**: ★★★ Extreme | **Used by**: Duolingo, Peloton, AA/12-step programs, CrossFit

```
Core insight: Habits are breakable. Identity-protected habits are
far less breakable. Identity-protected habits with sunk cost and
social accountability are nearly unbreakable without significant
psychological cost.

让一个行为变得几乎不可能停止的完整机制:

Foundation — Habit Loop (习惯回路):
  Cue → Routine → Reward, repeated until automatic.
  The habit loop alone is fragile: remove the cue, change the context,
  or introduce sufficient friction and the loop breaks.
  What makes this stack different: it installs three failure-cost
  multipliers that make breaking the habit aversive beyond the
  loss of the reward itself.

Multiplier 1 — Identity (身份):
  The routine becomes definitional.
  "Doing yoga" → "I am a yogi"
  Breaking the habit now requires: not just stopping a behavior,
  but resolving the self-concept question "who am I without this?"
  Identity is more aversive to violate than any reward is pleasurable to gain.

Multiplier 2 — Sunk Cost (沉没成本):
  Every completed repetition increases the psychological investment
  in the identity. 300 workouts, 200 days of streaks, 3 years of
  membership — quitting now means all of that effort "didn't count."
  Sunk cost is irrational economically but extremely powerful
  psychologically, especially when it compounds with identity threat.

Multiplier 3 — Social Accountability (社会问责):
  Others now expect the behavior. The community knows you as someone
  who does this. Stopping is visible. Peers will notice. Explanations
  will be required. The social cost of quitting adds to the
  identity and sunk cost costs.

  Social accountability creates: external cue, external reward
  (recognition), external consequence for non-performance.
  The habit loop is now reinforced from outside the self.

Compounding failure cost:
  To stop the behavior, the user must simultaneously pay:
  - Identity cost (who am I now?)
  - Sunk cost (what was all that for?)
  - Social cost (what will others think?)
  - Opportunity cost (I will lose my position/status/streak)

  Together, these costs make quitting feel like a major life event,
  not a simple behavioral change. This is why Peloton users
  continue subscribing long after they stop riding: stopping
  the subscription is psychologically larger than the monthly fee.

Implementation:
  1. Design habit loop with minimum viable friction cue
     (same time, same place, same trigger)
  2. Assign identity label at 21-day mark minimum
  3. Activate social layer before day 30 (social commitment before
     identity fully forms, so they compound together)
  4. Make sunk cost visible at natural churn moments
     ("You've done 47 workouts. Don't lose your streak.")
  5. Social accountability: peer check-ins, team challenges,
     visible absence when inactive

Warning: This stack creates a product that users may continue
using even when it stops serving them. The ethical obligation
is to ensure the product genuinely deserves long-term use.
Exit paths should remain accessible and friction-appropriate.
```

### COMBO-16: 内容病毒化栈 (Emotional Contagion × Social Currency × Information Gap × Identity Signal)
**Effect size**: ★★★ Very Large | **Used by**: Viral Twitter threads, BuzzFeed-era content, meme ecosystems

```
Core insight: Content does not go viral because it is true, useful,
or interesting. It goes viral because sharing it does something
for the sharer. This stack identifies the four shareable-content
drivers and explains why their combination produces self-propagating spread.

什么样的内容组合会在社交网络中自发扩散:

Driver 1 — Emotional Contagion (情绪感染):
  High-arousal emotions spread: awe, anger, anxiety, amusement.
  Low-arousal emotions don't: contentment, sadness, boredom.
  Jonah Berger's research: arousal amplifies social transmission
  regardless of valence (positive OR negative emotions spread;
  neutral content does not).

  Mechanism: Aroused state creates physiological need for expression.
  The share is an emotional discharge that requires a recipient.

Driver 2 — Social Currency (社交货币):
  Sharing is a self-presentation act. People share what makes them
  look a certain way to their audience. Content that makes the
  sharer look: smart, informed, funny, compassionate, insider,
  contrarian, or sophisticated has sharing motivation built in.

  The question is never "Is this interesting?" but "Does sharing
  this serve my social identity?"

Driver 3 — Information Gap (信息缺口):
  Novel information — things the audience doesn't know but should —
  creates obligation to share. "I learned something; now I need
  to pass it on" is a social norm around information that goes
  beyond self-interest. Surprising statistics, counter-narrative
  findings, and hidden-knowledge reveals all activate this.

Driver 4 — Identity Signal (身份信号):
  The content must serve as a signal of group membership.
  Sharing it says "I am part of this tribe / I hold these values /
  I know about this scene." Identity signal content gets shared
  inside social clusters where it reinforces group identity,
  which generates shares within the group rather than from the group.

Viral anatomy of maximum-spread content:
  - Emotional hook (arousal threshold within first 3 seconds)
  - Social currency (sharer looks good/smart/informed by sharing)
  - Information novelty (the audience doesn't already know this)
  - Identity marker (clearly signals in-group to the right audience)

Why combination matters:
  Any single driver produces intermittent sharing.
  Two drivers: consistent sharing within a niche.
  Three drivers: cross-network sharing.
  Four drivers: self-sustaining spread — each share reaches
  new audiences who themselves have the motivation to share,
  producing exponential rather than linear distribution.

Content architecture:
  1. Open with emotional hook (arousal, not information)
  2. Embed social currency signal in the first paragraph
     ("Most people don't know this...")
  3. Build information gap: state the claim, withhold the mechanism
  4. Close with identity signal: position the reader/sharer as
     part of the group that "gets it"
  5. Make sharing the natural resolution action
     (the share is the emotional discharge and the identity performance)

Platform-specific notes:
  - Twitter/X: social currency + identity signal weight higher
  - TikTok: emotional contagion + pattern interrupt weight higher
  - LinkedIn: social currency + information gap weight higher
  - WeChat: identity signal + social currency within closed networks
```

### COMBO-17: 社区飞轮栈 (Network Effects × Reciprocity × Status × Fear of Missing)
**Effect size**: ★★★ Extreme | **Used by**: Reddit, Discord, Hacker News, early Facebook groups

```
Core insight: Most communities fail to reach critical mass because
they attempt to activate network effects before the status and
reciprocity systems that make network effects valuable are in place.
This stack describes the sequenced conditions that allow communities
to become self-reinforcing.

如何让社区达到自我增强的临界质量:

The Critical Mass Problem:
  Network effects are only valuable once the network exists.
  A community with 10 members has low network value;
  one with 10,000 has high network value.
  The challenge is surviving the low-value phase long enough
  to reach self-sustaining scale.
  The four mechanisms below each address a different phase.

Phase 1 — Early Status System (早期地位系统):
  Before the network is valuable, status is.
  High-quality early contributors join for the status opportunity
  available only to early movers (founders, early adopters, OG members).
  The status system must be visible, legible, and have high early mover
  advantage — it is explicitly more valuable to join now than later.

  Implementation: Founding member badges, contributor rankings,
  early access tiers, public acknowledgment of first contributors.

Phase 2 — Reciprocity Web (互惠网络):
  As contributors give, obligations are created.
  A reciprocity network forms where members feel embedded
  in a web of mutual obligation. Leaving the community means
  abandoning relationships and unresolved reciprocity debts.

  Reciprocity builds attachment independent of network value.
  Even small communities become sticky when reciprocity is dense.

  Implementation: Visible giving acts (upvotes, endorsements,
  referrals), direct acknowledgment of help given, norms
  around contributing before extracting.

Phase 3 — Network Effect Activation (网络效应激活):
  Once the community has sufficient quality members (status
  attracted them) and reciprocity (keeps them engaged), the
  network effect activates: each new quality member makes
  the network more valuable for existing members, which
  attracts more quality members.

  This is the flywheel phase. It is self-sustaining once started
  but requires genuine density of quality contributions to trigger.

Phase 4 — FOMO Mechanism (错失恐惧机制):
  As the network grows, Fear of Missing Out operates as
  a pull force on non-members and a retention force on members.
  Non-members see that "this is where the conversations are happening"
  and the cost of not being in the community becomes visible.
  Members fear that leaving means losing access to current
  conversations, emerging knowledge, and relationships.

  FOMO is not activated artificially — it emerges naturally
  from genuine community value. Artificial FOMO in low-value
  communities produces joiners who immediately discover
  the value gap and churn with negative word-of-mouth.

Flywheel in operation:
  Status attracts quality early → reciprocity makes them stay →
  quality density creates network value → network value activates
  FOMO for outsiders → new quality members join →
  status system recalibrates to maintain incentive for new contributors →
  reciprocity web expands → network value increases → cycle continues

Bootstrap sequence (critical):
  1. Do NOT open to all: curate first 50-100 members for quality
  2. Over-invest in early member status signals immediately
  3. Seed reciprocity artificially: staff/founders model giving behavior
  4. Identify the first organic high-quality contributor and make
     their status highly visible (social proof for the value of early contribution)
  5. Hold quality bar aggressively until network effects are self-sustaining
  6. FOMO messaging to waitlist/outside only valid after real value exists

Failure modes:
  - Opening too early: low quality density, FOMO has no content to support it
  - Status inflation: giving status to everyone devalues status
  - Reciprocity collapse: extractors without givers destroy the web
  - FOMO without substance: manufactured urgency for low-value community = churn spike

Measured tipping points:
  Communities generally reach self-sustaining growth when daily active
  contributors exceed ~150 (Dunbar's number boundary) AND cross-member
  interaction density reaches threshold where most members recognize
  other members. Below this threshold, community feels like a broadcast
  channel. Above it, it feels like a home.
```
