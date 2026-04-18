# Model Index — Quick Reference

60+ cognitive/behavioral models indexed for fast lookup.
Format: `ID | Name | Category | Effect Size | Domain Fit | Conf`

## How to Use
When scanning for applicable models: scan this index first, then read the full model file for mechanisms and implementation details.

Domain Fit codes: `COM`=commerce `CON`=content `GAM`=games `SaaS`=digital products `SOC`=social/community `POL`=policy/irl `ALL`=universal

---

## Category 1: Heuristics & Biases (HB)

| ID | Name | Effect | Domains | Conf | One-line |
|----|------|--------|---------|------|---------|
| HB-01 | Anchoring Effect | ★★★ | COM POL ALL | 0.92 | First number sets reference point for all subsequent judgment |
| HB-02 | Loss Aversion | ★★★ | COM SaaS POL | 0.95 | Losses felt 2.25× more than equivalent gains |
| HB-03 | Default Effect | ★★★ | SaaS POL COM | 0.94 | 70-90% stick with default; opt-in vs opt-out changes everything |
| HB-04 | Scarcity Heuristic | ★★★ | COM CON SOC | 0.91 | Rare = valuable; use only real, legible scarcity |
| HB-05 | Framing Effect | ★★★ | ALL | 0.93 | Same facts, different presentation → opposite decisions |
| HB-06 | Availability Heuristic | ★★☆ | COM CON POL | 0.85 | Recent/vivid events overweight probability estimates |
| HB-07 | Representativeness | ★★☆ | COM CON | 0.82 | Pattern matching overrides base rates; similarity can mislead judgment |
| HB-08 | Sunk Cost Fallacy | ★★★ | GAM SaaS COM | 0.88 | Past investment drives future behavior beyond rational point |
| HB-09 | Endowment Effect | ★★☆ | COM SaaS | 0.87 | Ownership (even virtual) increases perceived value 1.5-2× |
| HB-10 | Status Quo Bias | ★★★ | SaaS POL COM | 0.90 | Inertia is the most powerful force in user behavior |
| HB-11 | Decoy Effect | ★★☆ | COM SaaS | 0.85 | Third asymmetric option makes target option look attractive |
| HB-12 | Mental Accounting | ★★☆ | COM GAM | 0.83 | Separate mental budgets for different money/resource categories |
| HB-13 | Hyperbolic Discounting | ★★☆ | SaaS GAM COM | 0.86 | Steep discount of future rewards; near-future valued disproportionately |
| HB-14 | Optimism Bias | ★★☆ | COM CON | 0.80 | People overestimate positive outcomes for themselves |
| HB-15 | Confirmation Bias | ★★☆ | CON SOC POL | 0.88 | People seek confirming evidence and discount disconfirming input |
| HB-16 | Dunning-Kruger | ★☆☆ | CON GAM | 0.72 | Early competence can create overconfidence; calibrate onboarding carefully |
| HB-17 | Gambler's Fallacy | ★★☆ | GAM COM | 0.79 | After losses, the next win feels "due" despite independent odds |
| HB-18 | Planning Fallacy | ★★☆ | SaaS POL | 0.81 | People underestimate time and effort, especially early in projects |

---

## Category 2: Social Dynamics (SD)

| ID | Name | Effect | Domains | Conf | One-line |
|----|------|--------|---------|------|---------|
| SD-01 | Social Proof | ★★★ | ALL | 0.90 | Others' behavior = correctness signal; 30-75% conformity rates |
| SD-02 | Reciprocity Norm | ★★★ | COM SOC | 0.92 | Gift creates obligation; even unsolicited gifts work |
| SD-03 | Commitment & Consistency | ★★★ | SaaS GAM SOC | 0.91 | Prior small commitment locks in future larger behavior |
| SD-04 | Authority Bias | ★★★ | COM CON POL | 0.88 | Expert credentials / signals override content judgment |
| SD-05 | Liking Principle | ★★☆ | COM SOC | 0.85 | Similarity + familiarity + attractiveness → compliance |
| SD-06 | Network Effects | ★★★ | SaaS SOC | 0.93 | Value grows superlinearly with users; critical mass tipping |
| SD-07 | Conformity Effect | ★★★ | SOC GAM | 0.87 | People adopt majority norm when uncertain; 30-75% compliance |
| SD-08 | Bandwagon Effect | ★★★ | COM CON SOC | 0.89 | Join the winning side; momentum signals attract more momentum |
| SD-09 | In-group/Out-group | ★★★ | SOC CON | 0.86 | Tribal identity drives behavior; "us vs them" amplifies everything |
| SD-10 | FOMO (Social Scarcity) | ★★★ | COM SOC CON | 0.92 | Fear of missing = loss aversion × social proof; most viral mechanic |
| SD-11 | Trust Transfer | ★★☆ | COM SaaS | 0.84 | Reputation/endorsement from trusted source transfers to unknown |
| SD-12 | Betrayal Aversion | ★★☆ | SOC SaaS | 0.82 | Betrayal hurts more than impersonal loss; trust breaks are costly |
| SD-13 | Gossip / Signaling | ★★☆ | SOC CON | 0.80 | Sharing exclusive info = social currency; drives referral |
| SD-14 | Status Signaling | ★★★ | COM GAM SOC | 0.88 | Visible status markers drive aspirational purchase and behavior |
| SD-15 | Social Comparison | ★★★ | GAM SOC SaaS | 0.89 | Benchmarking against peers drives motivation (leaderboards) |

---

## Category 3: Affective Dynamics (AD)

| ID | Name | Effect | Domains | Conf | One-line |
|----|------|--------|---------|------|---------|
| AD-01 | Variable Ratio Reinforcement | ★★★ | GAM SOC COM | 0.97 | Slot machine effect; unpredictable rewards = highest engagement |
| AD-02 | Zeigarnik Effect | ★★★ | GAM SaaS CON | 0.88 | Incomplete tasks create mental tension that demands resolution |
| AD-03 | Peak-End Rule | ★★☆ | SaaS COM | 0.84 | Memory = (peak moment + ending) / 2; design endings and peaks |
| AD-04 | Emotional Contagion | ★★★ | SOC CON | 0.86 | Emotions spread in networks; viral content is emotional at core |
| AD-05 | Affective Forecasting Error | ★★☆ | COM SaaS | 0.82 | People misjudge future emotional states and future preferences |
| AD-06 | Fear/Threat Response | ★★★ | COM CON | 0.90 | Threat activates heightened loss aversion + action drive |
| AD-07 | Mere Exposure Effect | ★★☆ | COM CON | 0.83 | Familiarity increases liking; repetition builds preference |
| AD-08 | Flow State | ★★★ | GAM SaaS | 0.87 | Optimal challenge-skill = total absorption; time disappears |
| AD-09 | Nostalgia Effect | ★★☆ | COM CON | 0.80 | Past associations increase current value perception 20-40% |
| AD-10 | Curiosity / Information Gap | ★★★ | CON GAM SaaS | 0.89 | Knowledge gap creates discomfort that demands closure |
| AD-11 | Anticipatory Anxiety | ★★☆ | COM GAM | 0.81 | Near-win / near-loss amplifies next engagement |
| AD-12 | Hot-Cold Empathy Gap | ★★☆ | COM POL | 0.79 | Can't predict behavior in different emotional state from current |
| AD-13 | Mood-Congruent Memory | ★☆☆ | COM CON | 0.72 | Current mood filters memory retrieval; use for context priming |

---

## Category 4: Motivation & Self-Regulation (MR)

| ID | Name | Effect | Domains | Conf | One-line |
|----|------|--------|---------|------|---------|
| MR-01 | Goal Gradient Effect | ★★★ | GAM SaaS COM | 0.88 | Motivation accelerates as goal nears; pseudo-progress works |
| MR-02 | Implementation Intentions | ★★★ | SaaS POL | 0.88 | If-then plans increase goal achievement 2-3× |
| MR-03 | Habit Loop (Cue→Routine→Reward) | ★★★ | SaaS GAM POL | 0.91 | Behavior becomes automatic after cue-routine binding |
| MR-04 | Identity-Based Commitment | ★★★ | SOC GAM SaaS | 0.87 | "I am X" drives behavior more powerfully than "I do X" |
| MR-05 | Self-Determination Theory | ★★☆ | SaaS GAM POL | 0.85 | Autonomy + competence + relatedness → intrinsic motivation |
| MR-06 | Progress Momentum | ★★★ | GAM SaaS COM | 0.87 | Pseudo-progress (2/10 already done) increases completion |
| MR-07 | Temptation Bundling | ★★☆ | SaaS POL | 0.80 | Pair aversive behavior with pleasurable one; habit formation |
| MR-08 | Precommitment Devices | ★★☆ | SaaS POL | 0.83 | Locking future choices increases follow-through |
| MR-09 | Ego Depletion | ★★☆ | COM SaaS | 0.77 | Willpower depletes; reduce friction at low-willpower moments |
| MR-10 | Loss Frame Progress | ★★★ | SaaS GAM | 0.86 | "You'll lose your streak" > "keep your streak"; loss > gain framing |
| MR-11 | Near-Miss Effect | ★★★ | GAM COM | 0.89 | Almost-winning increases motivation and re-engagement |
| MR-12 | Reward Variability | ★★★ | GAM SOC | 0.93 | Variable rewards can raise engagement but also raise compulsion risk |

---

## Category 5: Perception & Attention (PA)

| ID | Name | Effect | Domains | Conf | One-line |
|----|------|--------|---------|------|---------|
| PA-01 | Processing Fluency | ★★★ | COM CON SaaS | 0.88 | Easy-to-process = true/good/trustworthy; friction reduces compliance |
| PA-02 | Pattern Interruption | ★★★ | CON COM | 0.87 | Breaking expected pattern spikes attention; hook mechanism |
| PA-03 | Selective Attention (Cocktail Party) | ★★☆ | CON COM | 0.84 | Relevant stimuli break through regardless of noise level |
| PA-04 | Information Gap / Curiosity Gap | ★★★ | CON GAM | 0.89 | "What happens next" loop is automated by information asymmetry |
| PA-05 | Priming Effect | ★★☆ | COM CON | 0.82 | Prior exposure shapes interpretation of subsequent stimuli |
| PA-06 | Gestalt Principles | ★★☆ | SaaS COM | 0.85 | Grouping/proximity/similarity/closure drive perception |
| PA-07 | Visual Hierarchy Bias | ★★★ | COM SaaS CON | 0.87 | F-pattern, Z-pattern reading; attention allocation is predictable |
| PA-08 | Contrast Effect | ★★★ | COM SaaS | 0.88 | Items are judged relative to adjacent context, not absolute |
| PA-09 | Change Blindness | ★★☆ | SaaS CON | 0.79 | People miss gradual changes; useful for progressive disclosure |
| PA-10 | Serial Position Effect | ★★☆ | COM CON | 0.83 | First and last items best remembered (primacy + recency) |
| PA-11 | Color/Urgency Signaling | ★★☆ | COM SaaS | 0.81 | Red = urgency; color affects decision speed and confidence |
| PA-12 | Temporal Landmarks | ★★☆ | COM SaaS | 0.80 | "Fresh start" effect at time boundaries (Monday, New Year) |
