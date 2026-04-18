# Perception & Attention — Model Details

## PA-01 · Processing Fluency
**Confidence**: 0.88 | **Effect Size**: Large

**Mechanism**: The ease with which information is processed is misattributed to the quality and truth of that information. Things that feel easy to understand feel more true, more beautiful, and more trustworthy.

**Fluency effects**:
- Fluent stock tickers (e.g., "KAR") outperform difficult ones in early trading
- Fluent names are judged more likable and trustworthy
- High-contrast, clear fonts are judged more truthful
- Simple sentences are rated as more accurate

**Implementation**:
```
Copy: Use short sentences. Eliminate jargon. Active voice over passive.
Typography: High contrast, familiar serif/sans-serif fonts
Layout: Familiar patterns (users don't read novel UIs — they scan known patterns)
Naming: Product/feature names that are easy to pronounce → more memorable + trusted
Onboarding: Reduce cognitive load at every step → feels "just right"
Pricing: $9 (vs $9.00 vs nine dollars) → simple = trustworthy
Rhyming: "If it doesn't fit, you must acquit" — rhymes perceived as more true (rhyme-as-reason effect)
```

**Counterintuitive application**: Slight disfluency can INCREASE learning and memory retention (must process harder → deeper encoding). Use disfluency for educational content you want retained; use fluency for decisions you want made quickly.

---

## PA-02 · Pattern Interruption
**Confidence**: 0.87 | **Effect Size**: Large

**Mechanism**: Human attention is managed by a pattern-matching system that filters predictable inputs. Breaking an established pattern spikes attention involuntarily. This is the #1 hook mechanism.

**Why it works**: The brain's prediction system generates expectations. When reality violates expectations, an error signal fires → attention snaps to the unexpected element.

**The hook architecture**:
```
1. ESTABLISH PATTERN: Set up familiar expectation
2. INTERRUPT PATTERN: Violate it in unexpected way
3. OPEN LOOP: Create question or tension
4. PAYOFF: Deliver reward for staying
```

**Implementation**:
```
Video hooks: Start mid-action, not at beginning ("so then she said...")
Thumbnails: Jarring visual juxtaposition (expectation + violation)
Subject lines: "I'm quitting [thing you'd expect me to love]"
Copy: Start with contradiction: "I was wrong about [consensus belief]"
UI: Unexpected delight animation where user didn't expect it
Conversation: "Can I ask you something weird?" before key question
Presentations: Open with surprising statistic that violates audience assumption
Content format: Use format your audience doesn't expect in your niche
```

**Pattern interrupt in 2-second video hook**:
> First frame must either: start mid-action / show unexpected image / make surprising claim / create immediate question

**Combos**: Pattern Interruption × Information Gap → unexpected element + unresolved question = must watch

---

## PA-04 · Information Gap / Curiosity Gap
**Confidence**: 0.89 | **Effect Size**: Large

See also AD-10 for the emotional dynamics perspective.

**Cognitive mechanics**: Information gaps activate the same neural circuits as physical itch — they're intrinsically aversive and demand resolution.

**Gap architecture for content**:
```
Step 1: Establish what reader/viewer KNOWS (common ground)
Step 2: Reveal the existence of something they DON'T know
Step 3: Make the unknown feel important / valuable
Step 4: Provide easy path to close the gap (keep watching, click, read on)
```

**Headline formulas**:
```
"[Number] things [desirable group] knows that [reader's group] doesn't"
"The [unexpected thing] that [surprising actor] does before [common activity]"
"Why [common belief] is wrong — and what actually works"
"[Famous person] just [unexpected action] — here's why it matters"
"I spent [large investment] to learn [result] — here it is for free"
```

**Anti-patterns (kill curiosity)**:
- Revealing the answer in the headline (no gap)
- Gap too large to feel closeable
- Reader doesn't care about the domain (gap requires pre-existing interest)
- Clickbait that doesn't deliver → trains people to ignore your gaps

---

## PA-05 · Priming Effect
**Confidence**: 0.82 | **Effect Size**: Medium-Large

**Mechanism**: Prior exposure to concepts or stimuli shapes how subsequent stimuli are perceived and processed — without conscious awareness.

**Types**:
- **Semantic priming**: Exposure to "doctor" → "nurse" recognized faster
- **Conceptual priming**: Think about warmth → rate strangers as more friendly
- **Behavioral priming**: Exposure to elderly concepts → walk slower (controversial, smaller effect than originally claimed)

**Reliable applications**:
```
Landing pages: Show happy customers before pricing → price feels more acceptable
Trust page: Security badges before form → form completion increases
Negotiation: Luxury items in meeting room → higher price expectations
Menu design: Expensive items first → everything else seems reasonable
Email: Subject line primes reading of email body
Push notification text: Primes next action in app
Onboarding: Show success stories before user starts → competence priming
```

---

## PA-08 · Contrast Effect
**Confidence**: 0.88 | **Effect Size**: Large

**Mechanism**: Items are judged relative to adjacent context. The same item looks better next to a worse alternative and worse next to a better alternative.

**Implementation**:
```
Pricing: Show "Enterprise: $999/month" before "Pro: $49/month" → $49 feels cheap
Real estate: Show overpriced bad option first → target property looks better
Recruitment: Interview weak candidate right before strong one → strong looks exceptional
Product pages: "Compare to competitors" section where you win on key features
Before/after: Show "before" state first → "after" is dramatically better
Salary: Anchor high initial offer → any concession feels like a win for them
UI: Show cramped competitor UI before your clean interface
Reviews: Show 1-star reviews in context of overwhelming 5-stars → reassuring
```

---

## PA-10 · Serial Position Effect
**Confidence**: 0.83 | **Effect Size**: Medium-Large

**Mechanism**: People remember items at the beginning (primacy effect) and end (recency effect) of a list far better than items in the middle.

**Memory distribution in a 10-item list**:
```
Items 1-2:   Strong primacy recall
Items 3-8:   Poor recall ("the muddy middle")
Items 9-10:  Strong recency recall
```

**Implementation**:
```
Pricing pages: Put your preferred tier first or last (not in middle)
Navigation: Critical actions at start or end of nav bar
Email: Key CTA at top OR at end (not buried in paragraph 3)
Presentations: Open strong, close strong — muddle-through the middle
Checkout: Most important trust signal at start and end of flow
Feature lists: Lead with and close on strongest features
Menu: Best-margin items first and last on menu
Content: Hook in first sentence, CTA in last sentence
```
