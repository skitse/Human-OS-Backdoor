# Mechanism Record Schema v2 — 机制记录结构契约

> **Status**: normative. This file defines the record format every mechanism entry MUST follow.
> `harness/scripts/check_consistency.py` enforces it mechanically. A record that does not
> match this schema fails CI, not review.

---

## Why this schema exists

v1 records were flat implementation bullet lists. They answered *"what is this mechanism"*
and *"where have I seen it used"*. They did not answer the questions that decide whether a
mechanism actually works in a given situation:

- How strong is the evidence, really — and under what conditions does the effect survive replication?
- How much of it do I apply before it stops working?
- How fast does it decay, and how fast do users habituate?
- What does it look like **when it is failing**?
- Who does it work on, and who is immune?

v2 makes those questions mandatory fields. The point is not longer files; it is that a
record with no failure signal and no moderators is a record that will be misapplied.

---

## Record format

One mechanism = one `##` entry. The heading line is parsed by the index generator, so its
shape is load-bearing.

```markdown
## {ID} · {English Name} {中文名}
**Tier**: {核心|常用|情境} | **Evidence**: {A|B|C} — {依据} | **Effect**: {效应量 + 成立条件}

**机制链**: {刺激} → {认知/生理过程} → {行为输出}
**剂量**: 弱 {…}；中 {…}；强 {…}；过载 {…}
**时间动态**: 起效 {…} · 衰减 {…} · 饱和 {…}
**调节变量**: 个体 {…} · 文化 {…} · 情境 {…}
**失效信号**: {可观察的反向现象}；{第二条}
**可测代理**: {可落地的度量指标}
**交互**: {× 其他机制 → 非线性后果}，引用 COMBO-xx
**边界**: {伦理门槛 / 法律暴露 / 信任成本 / 不可用场景}
```

### Line discipline (mechanically enforced)

The consistency checker parses entries line by line. Two rules follow from that:

1. **One field = one line.** A field's value continues on the same line to the end of that
   line. No multi-line values, no wrapped bullets, no nested lists inside a field.
   Sub-clauses are separated by the field's own delimiter (`；`, `→`, `·`).
2. **The `Tier` line carries three fields** separated by ` | `, each as `**Key**: value`.
   It is the only line allowed to do this.

Write dense single lines. A field that needs three sentences is usually two mechanisms
that should be split into two records.

**The checker reads the first field token it finds on a line and stops.** Putting two field
tokens around a ` | ` on any line *other* than the `Tier` line does not produce two fields —
the second one is silently swallowed, and the file fails with a `missing field **Evidence**`
that looks like a content problem. This is the single most common way a correct record gets
rejected:

```markdown
<!-- WRONG: only Tier is captured; Evidence and Effect vanish -->
**Tier**: 常用 | **Evidence**: B — Kahneman & Tversky 1979 | **Effect**: 中等，仅在…

<!-- RIGHT -->
**Tier**: 常用
**Evidence**: B — Kahneman & Tversky 1979
**Effect**: 中等，仅在…
```

Before assuming a field is "missing", grep the record for the token — if it is there but on
the same line as an earlier field, that is the bug, not the content.

### Field rules

| Field | Required | Rule |
|-------|----------|------|
| Heading | yes | `## {PREFIX}-{NN} · {Name}`. Prefix must be registered in `_schema.md` prefixes table. |
| `**Tier**` | yes | `核心` = high effect + high generality; `常用` = solid but conditional; `情境` = narrow trigger window. |
| `**Evidence**` | yes | Grade + named source + replication note. **Do not invent numeric confidence.** v1 used `Confidence: 0.92` with no source — that is fabrication and is no longer permitted. |
| `**Effect**` | yes | Effect size *with the condition it holds under*. "Large" alone is rejected. |
| `**机制链**` | yes | Exactly three stages, `→` separated. No stage may be a restatement of another. |
| `**剂量**` | yes | Four bands. The `过载` band must describe a real reversal, not just "too much". |
| `**时间动态**` | yes | Three clocks: onset, decay, satiation. Use orders of magnitude when exact data is absent (`分钟级`, `周级`). |
| `**调节变量**` | yes | At least individual, cultural, and situational. Each must state the *direction* of the moderation. |
| `**失效信号**` | yes | ≥2 observable signals. **Any entry citing only "users might not like it" is rejected.** |
| `**可测代理**` | yes | Metrics obtainable without new instrumentation, or a named minimal experiment. |
| `**交互**` | yes | At least one combo with the emergent effect named. May cite `combo-patterns.md`. |
| `**边界**` | yes | Must state at least one condition where the mechanism must not be used, and why. |

### Evidence grading

| Grade | Meaning |
|-------|---------|
| `A` | Meta-analysis or multi-lab replication, OR a well-replicated behavioural-economic finding with consistent field evidence |
| `B` | Multiple independent studies, limited field replication, or robust lab effect with contested boundary |
| `C` | Single-study, theoretical, or practitioner-observed. Must be labelled as such. |

A record may not claim `A` without naming the source. Records whose effect has a documented
**failed replication** must say so in `Evidence` — this is the single most common way a
knowledge base misleads its reader.

---

## Worked example (gold standard)

Copy this shape. Every v2 record should be substitutable for it field-for-field.

```markdown
## HB-02 · Loss Aversion 损失厌恶
**Tier**: 核心 | **Evidence**: B — Kahneman & Tversky 1979 prospect theory; λ≈2.25 in Tversky & Kahneman 1992. Contested by Gal & Rucker 2018, who argue much of the evidence is a reference-point/reframing artifact rather than a general "losses loom larger" principle | **Effect**: Large (≈2× gain/loss asymmetry) but only when the reference point is already owned or expected; shrinks toward parity when the reference point is ambiguous or the loss is framed as a foregone gain

**机制链**: 结果被置于既有参照点之下 → 负向偏离触发更强唤醒与注意分配 → 为避免确认损失而承担额外风险或成本
**剂量**: 弱 一次性告知"将失去X" ；中 具体化已持有物+明确时限，配合可见的进度或资产 ；强 叠加社会比较（"同组只有你没完成"）并做成默认路径 ；过载 参照点被用户判定为虚构或每次触达都在喊损失 → 损失框架被重新归类为营销噪音，反向降低可信度并抬高后续真实损失的折扣率
**时间动态**: 起效 秒级（单次触达即可改变选择） · 衰减 同一损失的重复提醒在 3–5 次后钝化，用户开始主动规避文案 · 饱和 长期使用会把"损失"重新定价为常态成本，机制失效且信任余额下降
**调节变量**: 个体 损失厌恶强度随特质性风险厌恶与调节焦点上升，高专业度用户对人为参照点免疫 · 文化 集体主义市场对"损失相对位置"（排名、面子）比对"损失金钱"更敏感 · 情境 高不确定性+时间压力下效应放大，高利害且可复核的决策中效应被反思性加工削弱
**失效信号**: 用户开始截图或复述你的"损失"主张并质疑其真实性；同一触达的点击率在第二、三次后不降反升于关闭/退订入口；客诉与退款理由中出现"被胁迫感"表述；净推荐值下降但短期转化不变
**可测代理**: 同一价值主张的 gain-frame / loss-frame 分流转化差；触达第 n 次的打开率曲线拐点；退订率与文案损失强度的相关性
**交互**: × HB-03 默认效应 → 默认值把参照点变成"本来就有"，使损失框架无需虚构即可成立（COMBO-01）；× MR-10 损失框架进度 → 把进程资产化为可失去物，强度高于收益框架；× SD-01 社会证明 → 从"你会失去"升级为"你正在掉队"，但双重施压也最快触发 reactance
**边界**: 不得用于虚构参照点（用户从未持有或期待过的东西）；健康、金融、法律场景下损失框架会放大焦虑并诱发非理性决策，须替换为收益框架加不确定性披露；一旦被判定为胁迫，修复成本高于该机制的全部历史收益
```

Note how the `Evidence` field names a real critique of its own mechanism. That is the
standard: a record that only cites supporting work is incomplete.

---

## Alias registry

Some IDs in circulation are not separate mechanisms — they are a second name for a
record that already exists. Registering them here keeps the old ID resolvable without
forking the knowledge base into two near-identical entries.

Rules, mechanically enforced by `harness/scripts/check_consistency.py`:

- An alias must point at an ID that has a real body.
- An ID may be **either** a canonical body **or** an alias — never both.
- When you alias a pair, delete the duplicate body. Two records describing one mechanism
  is the failure this table exists to prevent.

| Alias | Canonical | Why |
|-------|-----------|-----|
| HB-12 | PE-02 | 心理账户 / Mental Accounting — same mechanism, pricing file owns the depth |

## Declared-but-unwritten registry

This table records mechanisms that are **named and intended but have no body yet**.
They are listed so that coverage stays visible instead of silently shrinking, and so
that no other file cites them as if they existed.

Rules, mechanically enforced:

- An ID here must **not** have a body — write the body and remove the row.
- The scan protocol and SKILL.md must not route to a declared-only ID.
- `references/model-index.md` renders these in a separate, clearly-labelled section.

| ID | Name | Family | Blocks |
|----|------|--------|--------|
| AD-04 | Emotional Contagion | AD | viral content, community tone |
| AD-05 | Affective Forecasting Error | AD | subscription cancellation, onboarding promises |
| AD-07 | Mere Exposure Effect | AD | brand repetition, ad frequency |
| AD-09 | Nostalgia Effect | AD | legacy branding, retro campaigns |
| AD-11 | Anticipatory Anxiety | AD | pre-launch, drop mechanics |
| AD-12 | Hot-Cold Empathy Gap | AD | consent design, self-commitment tools |
| AD-13 | Mood-Congruent Memory | AD | context priming, ad placement |
| HB-06 | Availability Heuristic | HB | risk communication, testimonials |
| HB-07 | Representativeness | HB | base-rate framing, market sizing |
| HB-10 | Status Quo Bias | HB | migration, churn, opt-out design |
| HB-14 | Optimism Bias | HB | trial promises, plan selection |
| HB-15 | Confirmation Bias | HB | filter bubbles, community moderation |
| HB-16 | Dunning-Kruger | HB | onboarding calibration, skill gating |
| HB-17 | Gambler's Fallacy | HB | streak mechanics, pity timers |
| HB-18 | Planning Fallacy | HB | project tools, deadline promises |
| MR-02 | Implementation Intentions | MR | if-then plans, commitment UX |
| MR-07 | Temptation Bundling | MR | habit pairing, wellness products |
| MR-08 | Precommitment Devices | MR | savings, focus tools |
| MR-09 | Ego Depletion | MR | friction placement, low-willpower windows |
| MR-10 | Loss Frame Progress | MR | streak copy, progress framing |
| PA-03 | Selective Attention | PA | salience, context matching |
| PA-06 | Gestalt Principles | PA | layout, grouping, form design |
| PA-07 | Visual Hierarchy Bias | PA | scan patterns, above-the-fold |
| PA-09 | Change Blindness | PA | progressive disclosure, silent updates |
| PA-11 | Color/Urgency Signaling | PA | urgency cues, accessibility limits |
| PA-12 | Temporal Landmarks | PA | fresh-start campaigns, renewal timing |
| SD-05 | Liking Principle | SD | affinity, similarity, rapport |
| SD-07 | Conformity Effect | SD | norm formation, moderation |
| SD-08 | Bandwagon Effect | SD | momentum claims, launch signals |
| SD-09 | In-group/Out-group | SD | tribal identity, polarization risk |
| SD-11 | Trust Transfer | SD | endorsement, marketplace sellers |
| SD-12 | Betrayal Aversion | SD | breach response, dispute design |
| SD-13 | Gossip / Signaling | SD | referral, social currency |

`CA-06`/`CA-07` and the whole `PE-*` family are **canonical** and are no longer absent
from the index; the same is true of `attention-economics` and `trust-architecture`,
whose content is indexed as records below rather than as untracked prose.

## Registered prefixes

The index generator discovers prefixes automatically, but each new prefix must be declared
here so the consistency checker can verify that a family has a home file or a home section.

| Prefix | Family | Home |
|--------|--------|------|
| `CA` | Cognitive Architecture 认知架构 | `models/cognitive-architecture.md` |
| `HB` | Heuristics & Biases 启发法与偏差 | `models/heuristics-biases.md` |
| `SD` | Social Dynamics 社会动力学 | `models/social-dynamics.md` |
| `AD` | Affective Dynamics 情感动力学 | `models/affective-dynamics.md` |
| `MR` | Motivation & Regulation 动机与自我调节 | `models/motivation-regulation.md` |
| `PA` | Perception & Attention 感知与注意 | `models/perception-attention.md` |
| `TR` | Trust Architecture 信任架构 | `models/trust-architecture.md` |
| `AE` | Attention Economics 注意力经济 | `models/attention-economics.md` |
| `PE` | Pricing & Economic Decisions 定价与经济决策 | `models/pricing-economic-decisions.md` |
| `CM` | Covert Mechanics 隐蔽机制解剖 | `refused-domains/` |
| `RD` | Refused Domains 被拒领域 | `refused-domains/` |

### The `CM` family

`CM` records document mechanisms that are designed to be **undetectable by their target** —
manufactured urgency, engineered compulsion loops, narrative control, narrative grafting.
They follow the same schema but carry two additional mandatory fields:

```markdown
**危害画像**: {谁受损、如何受损、证据}
**检测信号**: {被针对者/审计方观察到的可核查痕迹}
**防御动作**: {可执行的反制措施：个人、平台、监管三层各一}
**监管环境**: {已存在的法律/合规约束，指明辖区与条文}
```

`CM` records exist so that these mechanisms can be **recognised, audited, regulated, and
defended against**. They document mechanism and consequence; they do not provide
target-specific operational sequencing. A `CM` record that reads as an execution plan for
deceiving an identified target is out of contract.

---

## Migration recipe (v1 body → v2 record)

Every existing body already contains the raw material. Migration is **transformation, not
invention** — with one exception noted at step 5.

1. Keep the `## {ID} · {Name}` heading and everything the author already wrote.
2. Move the existing prose *under* the new field lines. Existing headings inside a record
   (`### 价格锚定的6种形式`) may stay — only the eleven `**Field**:` lines are parsed.
3. Derive `剂量` by asking what the body already implies: what is the mild version, what is
   the version the body actually recommends, and **what happens past that**. The `过载`
   band must describe a real reversal observed in the body or in the field — if you cannot
   name one, the mechanism is not ready.
4. Derive `时间动态` from the body's own timing claims. If the body says nothing about
   decay, that is a finding: write what is known and mark the unknown explicitly rather
   than inventing a number.
5. `Evidence` is the one field that requires looking outward. Grade honestly:
   - `A` — replicated meta-analysis or large preregistered replication
   - `B` — multiple independent studies agreeing, or one strong study with partial replication
   - `C` — single study, field observation, or practitioner consensus
   Name the source. If the mechanism is contested, **say so in the Evidence line** — a
   record that only cites supporting work is incomplete and will be sent back.
6. `失效信号` must be things someone could actually watch for. "Users get annoyed" is not
   a signal. "Unsubscribe rate rises on the second send" is.
7. `交互` cites `COMBO-xx` ids from `references/combo-patterns.md`. Only cite a combo the
   record genuinely participates in — coverage is checked, so do not sprinkle ids.
8. `边界` is per-record and must name a concrete limit, not a sentiment.

### What "深度不够" looked like in v1, and what fixes it

| v1 symptom | v2 requirement that forces the depth |
|---|---|
| Effect asserted flatly | `Effect` must state the boundary condition where it holds |
| Mechanism named, not traced | `机制链` must be exactly 3 stages, stimulus → process → output |
| No sense of "how much" | `剂量` with four bands including a real overload reversal |
| Treated as permanent | `起效 / 衰减 / 饱和` clocks |
| One-size-fits-all | `调节变量` split into 个体 / 文化 / 情境 |
| No failure detection | ≥2 observable `失效信号` |
| Mechanism isolated | `交互` with combo ids, grounded in `combo-patterns.md` |
| Ethics as afterthought | per-record `边界` |

---

## Anti-patterns this schema is designed to prevent

| v1 failure | v2 countermeasure |
|---|---|
| Fabricated precision (`Confidence: 0.92`, no source) | Named-source evidence grading; numeric confidence banned |
| Index/body drift (70 indexed, 36 present) | Index is generated from bodies; drift is impossible by construction |
| Routing to non-existent files | `check_consistency.py` resolves every `references/...` path cited in SKILL.md and scan-protocol |
| "More is more" — no dose ceiling | Mandatory `剂量` band with a real `过载` reversal |
| Mechanisms presented as permanent | Mandatory decay + satiation clocks |
| No way to tell a lever is failing | Mandatory `失效信号` |
| Universal treatment of culturally-bound effects | Mandatory `调节变量` |
| Ethics as a footnote | `边界` is required per record, not per file |
