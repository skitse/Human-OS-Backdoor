# Cognitive Architecture — Model Details

> **Domain**: core cognitive processing, load limits, prediction, time horizon, embodied cues
> **Use when**: the task depends on how people process information, switch between intuitive and reflective thinking, or abandon flows under cognitive strain
> **Scope**: concise reference for the few cognitive models most useful in product, UX, and content decisions

---

## CA-01 · Dual Process
**Confidence**: 0.91 | **Effect Size**: Large

**Mechanism**: People alternate between fast, low-effort judgment and slower, effortful analysis. Friction, novelty, and ambiguity push work into slower processing.

**Cognitive chain**: Simple familiar cue -> fast judgment -> immediate action  
Complex or unclear cue -> reflective evaluation -> delay, scrutiny, or drop-off

**Implementation**:
```text
Onboarding: reduce fields and decisions before activation.
Checkout: remove ambiguity before asking for payment.
Content: put the main point before explanation when attention is fragile.
```

**Boundary conditions**:
- reflective processing is good when the decision is high-stakes
- fast processing is not the goal when consent, safety, or legal clarity matters

---

## CA-02 · Cognitive Load
**Confidence**: 0.93 | **Effect Size**: Large

**Mechanism**: Working memory is limited. Users abandon tasks when interfaces add avoidable load on top of the task itself.

**Cognitive chain**: Too many items or unclear structure -> working-memory overload -> hesitation, mistakes, abandonment

**Implementation**:
```text
Forms: remove nonessential fields.
Navigation: group options into a few meaningful chunks.
Onboarding: split complex setup into stages.
```

**Boundary conditions**:
- some effort is useful when it builds ownership or understanding
- the problem is avoidable load, not all effort

---

## CA-03 · Predictive Coding
**Confidence**: 0.87 | **Effect Size**: Large

**Mechanism**: People continuously predict what comes next. Attention spikes when reality differs from expectation by a manageable amount.

**Cognitive chain**: Expected pattern -> low attention  
Small meaningful surprise -> attention and curiosity  
Huge mismatch -> confusion or distrust

**Implementation**:
```text
Hooks: open with a specific expectation break.
Feeds: keep novelty inside a recognizable topic boundary.
Product updates: preserve most of the old pattern, change only what matters.
```

**Boundary conditions**:
- too little surprise creates boredom
- too much surprise creates comprehension cost or suspicion

---

## CA-04 · Attention Limits
**Confidence**: 0.88 | **Effect Size**: Medium-Large

**Mechanism**: Salient, relevant, or unexpected cues capture attention first. Competing prompts dilute one another.

**Cognitive chain**: Multiple competing cues -> attention fragmentation -> weaker noticing of the intended action

**Implementation**:
```text
Pages: one dominant action per section.
Notifications: send only when the message is likely to matter.
Content: foreground one question or one tension at a time.
```

**Boundary conditions**:
- salience without value becomes noise quickly
- repeated attention grabs degrade source reputation over time

---

## CA-05 · Temporal Discounting
**Confidence**: 0.86 | **Effect Size**: Medium-Large

**Mechanism**: Near-term outcomes feel more real than delayed ones. Immediate friction often outweighs distant benefit unless the future is made concrete.

**Cognitive chain**: Immediate effort vs abstract future value -> present bias -> delay or avoidance

**Implementation**:
```text
Savings: make the first concrete win visible early.
Habit products: reduce setup friction and specify the next step.
Pricing: translate long-term value into near-term outcomes users can picture.
```

**Boundary conditions**:
- users will tolerate present effort when the near-term payoff is legible
- abstract promises alone rarely overcome present bias

---

## CA-06 · Embodied Cues
**Confidence**: 0.74 | **Effect Size**: Medium

**Mechanism**: Sensory and physical cues can bias abstract judgment. Weight, warmth, smoothness, and motion can subtly influence seriousness, trust, or energy.

**Cognitive chain**: Physical cue -> associative meaning activation -> judgment shift

**Implementation**:
```text
Brand surface: material feel can reinforce premium or calm positioning.
UI motion: controlled motion can signal responsiveness or confidence.
Environment: physical context matters in demos, retail, and device setup.
```

**Boundary conditions**:
- these are supporting cues, not primary conversion levers
- effects weaken when stronger trust or value signals are missing

---

## CA-07 · Default Mode and Self-Narrative
**Confidence**: 0.78 | **Effect Size**: Medium

**Mechanism**: When not fully task-locked, people interpret information through self-story, identity, and future imagination.

**Cognitive chain**: Prompt touches identity or future self -> self-referential processing -> stronger memory and meaning

**Implementation**:
```text
Reports: frame outcomes in terms of the user's trajectory, not just raw metrics.
Onboarding: connect setup steps to who the user wants to become.
Content: use examples that help the audience place themselves in the story.
```

**Boundary conditions**:
- identity framing becomes manipulative when it pressures rather than clarifies
- not every task needs self-story; use only when motivation or meaning is central

---

## Selection Guide

Use:

- `Dual Process` when friction, clarity, or time pressure is the issue
- `Cognitive Load` when users stall or abandon complex flows
- `Predictive Coding` when hooks, novelty, or surprise matter
- `Attention Limits` when too many cues compete
- `Temporal Discounting` when long-term value loses to short-term effort
- `Embodied Cues` when physical or sensory experience matters
- `Default Mode and Self-Narrative` when identity and future self are central

---

## Output Guidance

Good outputs from this file sound like:

- "This flow fails because it pushes a simple decision into reflective mode."
- "The page asks users to hold too many choices in working memory."
- "The hook needs a clearer expectation break, not more explanation."

Bad outputs from this file sound like:

- giant neuroscience lectures
- ornate diagrams with no decision value
- mixed-language formatting that increases reading friction
