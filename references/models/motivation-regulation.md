# Motivation & Self-Regulation — Model Details

## MR-01 · Goal Gradient Effect
**Tier**: 核心
**Evidence**: B — 田野证据主要来自忠诚度计划的两项研究：Nunes & Drèze 2006 的洗车卡实验（12 格已赠 2 格 vs 10 格空卡，完成率 34% vs 19%）与 Kivetz, Urminsky & Zheng 2006 的咖啡卡实验（加速兑现缩短了实际达到免费饮品的时间）。**争议**：两项研究出自同一研究团队、样本为单一门店顾客，独立大样本复现在数字产品中很少且结果混合；动物学习中的 Hull 目标梯度（反应强度随接近奖赏上升）与人类"接近目标时努力增加"并非同一构念，v1 把它写成"Hull 的驱力理论已被数字证实"属于跨层误引。此外"最后 20% 付出 2–3 倍努力"没有可引用的实证支撑，属实践者估计。可依赖的是方向与条件，不是倍率
**Effect**: 中等偏大但条件性强：剩余距离小且可读、奖励对用户真实有价值、路径单一时，接近段的单位时间投入可靠上升；预置起点可带来约 1.5–2× 完成率（原研究），当起点被判定为任意、奖励价值不明、或目标可随时替换时效应趋零甚至为负

**机制链**: 目标被表征为可及且剩余距离可读 → 随距离缩小，单位努力的主观边际价值上升 → 单位时间投入增加、放弃阈值升高
**剂量**: 弱 只显示剩余距离（"还差 3 步"），不改变实际路径与奖励结构 ；中 预置一段有事实依据的起点（迁移的旧数据、已完成的前置动作），并在接近处提高反馈密度 ；强 临近完成处叠加一次性加速（双倍计入、临门奖励、临期加成），把剩余距离压缩成单一可见数字并给出完成后的具体兑现 ；过载 起点被抬得过高且无法解释（一进来就 80%）→ 用户中途发现"我根本没做这些"，进度从激励变成欺骗证据，完成率与信任同时下降
**时间动态**: 起效 首次看到进度状态即生效（分钟级） · 衰减 同一进度条的加速度收益在 3–5 个周期后习惯化，需不断加大预置量才能维持 · 饱和 预置量长期通胀后用户学会对起点打折（"人人都有 20%"），机制退化为无信息的装饰，且已消耗的可信度不可回收
**调节变量**: 个体 目标承诺度高、对奖励有真实需求者效应强，对奖励无兴趣者进度条只增加负荷；文化 个人成就取向文化中"接近目标"本身是激励，关系取向文化中同伴进度的权重高于绝对距离；情境 目标明确、路径单一、周期短时最强，目标模糊、周期长、可随时替换时最弱
**失效信号**: 进度超过 50% 后日活跃不升反降；用户在产品评价或社区指出起点是虚构的；预置比例与完成率的相关性转负；进度条中段的单日流失率高于起点；完成奖励领取率显著低于完成率（说明到终点才发现奖励不值得）
**可测代理**: 按进度条位置分桶的日活跃与完成率曲线（看拐点是否落在预期位置）；预置组与零起点组的完成率差；进度条上"最后一次交互"的位置分布；完成奖励领取率
**交互**: × MR-06 伪进度 → 两者在起点处叠加，但过载阈值也相同，一起越过时崩塌更快；× MR-11 近失效应 → 临近完成时近失把"下一次机会"拉到近端，COMBO-05 的锁定由此产生，其伦理门槛也由此产生；× CA-05 时间折扣 → 进度把远期奖励转成近端可见距离，等价于降低有效贴现
**边界**: 不得虚构进度——预置量必须有可核查来源（数据迁移、已完成前置动作、试用期计入），无来源的预置属欺骗性设计；对已处于债务、健康危机等高压状态的用户，人为制造"只差一点"会诱发非理性加码，禁用；不得把进度与不可退的付费绑定

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Large (Hull's drive theory, confirmed digitally)

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
**Tier**: 核心
**Evidence**: B — 习惯的自动性与情境线索依赖有较好证据：Neal, Wood & Quinn 2006 的爆米花实验显示习惯性进食由情境线索而非口味偏好驱动；Wood & Neal 2007 综述了情境-反应关联的强化路径。**但"线索→惯例→奖赏"三环模型是教学抽象，不是实证结构**：Duhigg 的叙述源自 MIT 基底核（Graybiel 实验室）的小鼠研究，被广泛批评为过度简化——奖赏主要在形成期起作用，在维持期作用很小，这与 v1"奖赏维持习惯"的表述相反；"21 天养成"是神话，Lally et al. 2010 的日记研究报告自动性达到平台的中位时间为 66 天（区间 18–254 天）；"keystone habits"（关键习惯级联）缺乏对照证据，属实践者主张
**Effect**: 中等偏大且高度依赖情境稳定性：在固定线索与低摩擦条件下自动性可靠上升、启动决策成本下降；复杂多步、需现场决策的行为很少完全自动化，因此本机制的效应主要体现在"启动"而非"执行质量"

**机制链**: 稳定情境线索（时间/地点/前置动作）反复与同一行为共现 → 情境-反应关联被强化，启动所需的决策成本下降 → 线索单独即可引发行为，且该行为对奖赏变化越来越不敏感
**剂量**: 弱 把新行为挂到一个已有的稳定线索之后（"通勤时""刷完牙后"），不改动其他结构 ；中 固定时间与地点、把首个动作压到 2 分钟内、并把奖赏做成即时可见的感官或数字反馈 ；强 线索绑定 + 摩擦最小化 + 连续追踪，使线索到行为完成的路径无分支、无选择、无等待 ；过载 线索过多过密（同一行为挂五个触发、每天多次提醒）→ 线索之间互相竞争并与情境解绑，自动性无法形成，提醒本身变成需要主动抵抗的噪音，行为反被抑制
**时间动态**: 起效 首个稳定重复周期（数天）内启动成本即可观察下降 · 衰减 线索中断（旅行、换工作、换设备）后自动性在 1–3 周内显著削弱，且往往不自动恢复 · 饱和 形成期 18–254 天、中位约 66 天（Lally et al. 2010），此后边际重复的收益递减到零，行为不再需要奖赏维持
**调节变量**: 个体 自我报告习惯强度（SRHI）高者对新线索更敏感，执行功能较弱者更依赖外部线索而非意图；文化 家庭与集体情境中社会线索（他人在场、共同仪式）可替代时间线索，个人主义情境更依赖个人日程与设备提示；情境 情境稳定（固定工位、固定通勤）时形成快，情境频繁变化时几乎不形成，压力期已有习惯最先崩解
**失效信号**: 第 3–6 周出现"为打卡而打卡"（行为时长下降但完成标记上升）；提醒关闭率上升而行为未下降（线索已内化或已失效，无法区分则说明追踪失效）；情境变化（假期、搬家、换设备）后行为归零且不恢复；同一行为的启动延迟不再缩短（自动性停滞）
**可测代理**: 线索到首次动作的延迟（启动延迟）周序列；完成时的情境一致性（同时间同地点占比）；SRHI 短表月度测量；提醒关闭率与完成率的背离幅度
**交互**: × MR-12 奖励变异 → 变动奖赏强化的是寻求而非自动性，混用会让习惯持续依赖奖赏、失去对奖赏的不敏感性，COMBO-07 的稳定收益因此被侵蚀；× MR-04 身份承诺 → 身份让习惯在奖赏消失后仍维持，这正是 COMBO-15 比 COMBO-07 更难破的原因；× CA-02 认知负荷 → 高负荷时习惯回路是唯一还能运行的行为通道，因此摩擦应放在形成期而非维持期
**边界**: 不得为成瘾性行为（赌博式奖励、无限滚动、短视频自动播放）设计习惯回路——在易感人群中这构成伤害而非产品价值；用药、康复、心理干预类习惯必须与专业方案一致，不得用习惯机制替代依从性评估；不得以情绪状态线索（焦虑、孤独、无聊）作为触发，那等于把痛苦商品化

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.91；Effect Size: Very Large (Duhigg / MIT research)

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
**Tier**: 常用
**Evidence**: C — 身份与自我概念影响行为有理论支持（Bem 自我知觉理论、Festinger 认知失调、self-concept–behavior 一致性），但"身份框架优于结果框架"缺少直接对照实验，v1 引的 Clear / Fogg 属实践者来源而非实证证据，必须如实标为 C。**可复现的部分**：公开承诺与一致性压力有小样本实验支持（Cialdini 系列），元分析效应为中等偏小且高度依赖公开性与自愿性；**未复现/被质疑的部分**：身份标签本身改变行为的独立效应缺乏大样本实验；Swann 的 identity fusion 在极端群体行为上有证据，外推到消费产品属越界；身份标签通胀（人人都是专家）导致的去认同是实践观察，无系统测量
**Effect**: 小到中等，且几乎完全由一致性压力与公开性驱动：在有社会见证、用户自愿、行为可回指的场景中效应可靠；私密、无见证、一次性任务中效应接近零；标签覆盖率上升时效应递减到负

**机制链**: 用户做出一个自愿、可被自己回忆的行为或声明 → 该行为被纳入自我概念，产生"我是做这件事的人"的推断 → 后续行为被选择为与自我概念一致，违背时产生自我与社会双重不适
**剂量**: 弱 在真实里程碑处给描述性标签（"你已经连续 12 天"），不做身份断言 ；中 让用户自己说出价值或目标，并在后续真实节点回指（"你说过 X 对你重要"） ；强 身份标签 + 他人可见 + 可回看的自我历史，使退出同时触发自我不一致与社会不一致，并把身份写入用户对外的自我描述 ；过载 标签通胀（人人都是专家/大使/创始成员）叠加高频身份断言 → 标签失去证据基础，用户识别为廉价激励并主动去认同，"你老说我是 X"引发反感，一致性压力反转为退出动机
**时间动态**: 起效 单次承诺后即时（分钟级，一致性压力启动） · 衰减 无新行为证据支撑的标签在 2–6 周内贬值，同一断言重复 3–5 次后引发反驳 · 饱和 深度身份融合后遭遇一次身份违背（产品事故、社群冲突、被公开打脸）即触发去认同冲击，退出更彻底且负面口碑强于普通流失
**调节变量**: 个体 自我概念清晰度高者受身份框架影响更大但也更抗拒被外部定义，高自我监控者对公开标签更敏感；文化 独立自我文化中身份指向个人特质与成就，互依自我文化中指向关系角色与责任（"作为团队的一员"优于"你是个赢家"）；情境 生命转折点（入学、换工作、搬家）与公开场景效应最强，私密、低风险、一次性任务中最弱
**失效信号**: 身份标签发放后次周行为无增量或下降；社群中出现对标签的玩梗与嘲讽；"你曾说 X 重要"类召回信息的打开率与退订率同时上升；标签覆盖率与人均贡献负相关；用户在产品之外公开否认该身份
**可测代理**: 身份框架与结果框架文案的 7/30 日行为差；标签发放后的次周行为增量与 90 日留存；产品内 UGC 中自述身份词（"我是…"）的词频；召回信息的打开-退订比；标签覆盖率与人均贡献的相关
**交互**: × MR-01 目标梯度 → 进度提供"我做到了"的证据，身份把证据转成自我定义，COMBO-03 的承诺阶梯即此路径；× CA-07 默认模式与自我叙事 → 叙事提供"我是谁"的素材、承诺提供"我做过什么"的证据，合流后退出成本从行为层升到自我层，COMBO-12 的不可逆性正源于此；× MR-06 伪进度 → 无事实依据的起点无法生成真实身份证据，标签退化为空头支票；× CA-03 预测编码 → 身份反差（"你居然是这种人"）是高效注意钩子，COMBO-09 与 COMBO-16 的身份信号层依赖此
**边界**: 不得把身份框架用于制造退出羞耻（"退出=你不是那种人"属胁迫性一致，禁用）；心理治疗、丧亲、身份危机与青少年用户对身份操纵极度脆弱，禁用；不得基于推断的敏感身份（健康、宗教、性取向、政治立场）做身份框架，多数辖区需单独同意

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.87；Effect Size: Large (James Clear / Fogg research)

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
**Tier**: 常用
**Evidence**: B — 需要满足与福祉、坚持的相关性证据强（Howard, Gagné & Morin 2021 的元分析，样本逾十万，三种需要与福祉的相关为中等），但以横断设计为主，因果方向未被充分隔离。**过度辩护效应（overjustification）所在 CET 的"控制性"因子（controlling contingency，即所谓 C 因子）存在复制危机**：Deci, Koestner & Ryan 1999 的元分析报告预期性、偶然性有形奖励会削弱内在动机（约 d≈-0.40），但 Cameron & Pierce 1994 与 Cameron, Banko & Pierce 2001 的再分析指出该削弱效应只在很窄的条件下成立（任务本就有内在兴趣 + 奖励为预期且与任务参与绑定），在表扬、非预期奖励、低基线兴趣任务上效应为正或为零，并批评前一元分析纳入了程序不当的研究；Deci 等 2001 又反驳对方纳入了无关研究。这场元分析之争至今未收敛，因此"给奖励会摧毁内在动机"不能作为通则使用。职场/教育场景的效应量也有争议：Cerasoli, Nicklin & Ford 2014 的元分析显示内在动机对绩效**质量**有中等预测力，对绩效**数量**预测力很弱，且当外在激励与绩效直接挂钩时内在动机的增量预测力消失；自主支持型管理培训的实验效应为小到中等且高度依赖管理者行为是否真的改变
**Effect**: 小到中等：自主、胜任、关系三种体验的满足与坚持度、创造力、福祉正相关（相关中等），但作为**干预**的因果效应量远小于 SDT 通俗读物的表述；在计件、强考核、短期指标场景中效应被外在激励吸收；过度辩护效应仅在"预期 + 偶然 + 有形奖励 + 任务本有趣"四条件同时满足时可靠出现

**机制链**: 环境提供或剥夺自主、胜任与关系三种体验 → 动机被内化为自主动机或被外化为受控动机 → 行为的坚持度、创造力与福祉随之升降，撤除外在控制后行为是否延续取决于内化深度
**剂量**: 弱 提供选项并给出理由（"你可以选 A 或 B，因为……"），保留真实的选择权 ；中 在任务设计中同时安排自主（路径选择）、胜任（难度匹配 + 具体信息性反馈）与关系（真实的人与共同目标） ；强 系统性移除控制性要素：不用指令式语言、不用排名施压、把威胁性截止期与评价换成信息性反馈，并让用户在目标层面拥有否决权 ；过载 把自主推到无限（什么都要用户自己定、无结构、无边界、无推荐）→ 决策负荷与方向缺失，胜任感与关系感反而下降，自主从"被尊重"变成"被放任"，完成率与动机同时下降
**时间动态**: 起效 数天到数周（需要环境体验累积，单次触达几乎无效应） · 衰减 自主支持型管理行为在考核季与压力期迅速回退，内在动机随之回落，通常以周计 · 饱和 内在动机对重复同一任务的增益在技能见顶后饱和，此时需要新挑战而非更多自主
**调节变量**: 个体 自主倾向（autonomy orientation）高者受影响更大，控制倾向者对外在激励既不敏感也无损；基线内在兴趣高者更易被外在奖励削弱，基线兴趣低者外在奖励无损耗甚至有益（这是过度辩护效应的边界方向）；文化 个人主义文化中自主权重更高，东亚样本中关系与胜任权重相对上升，且须区分"独立选择"与"意志自愿"两种自主操作化；情境 任务本身有趣、有余量、非计件时效应最强，计件、强考核、短期 KPI 场景中外在激励主导
**失效信号**: 引入选择后完成率不升而降（选择过载）；自主支持培训后 6–8 周管理者行为回退且团队指标同步回落；外在奖励撤销后行为立即归零（未内化）；引入排名或奖金后内在动机量表分数下降；用户报告"知道有选择但还是得这么做"（形式自主）
**可测代理**: 内在动机短表（IMI）或自主动机量表的前后测；奖励撤销后的行为留存曲线；自主支持感知量表的管理者评分与团队留存的相关；每步选择数量与完成率的倒 U 曲线
**交互**: × CA-05 时间折扣 → 自主性的收益在远期（能力成长），控制式奖励的收益在近期，短期指标会系统性偏向控制式设计；× MR-12 奖励变异 → 变动奖赏是最强的控制性因子，与自主支持直接冲突，混用时 SDT 的收益被抵消；× MR-04 身份承诺 → 身份内化是自主内化最强的形式，但被外部指派时立刻转为受控动机
**边界**: 不得把"给了选择"当作免责（形式自主掩盖实质控制属操纵）；教育、医疗、心理干预中的 SDT 原则须由专业人员实施，不得用动机话术替代治疗；不得用内在动机论证压低报酬——"这工作本身有意义"不能替代公平薪酬，这是 SDT 最常被滥用的方式

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.85；Effect Size: Large (Deci & Ryan)

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
**Tier**: 常用
**Evidence**: B — 直接来源是 Nunes & Drèze 2006 的 endowed progress 田野实验（洗车卡 12 格已盖 2 格 vs 10 格空卡，完成率 34% vs 19%）与 Kivetz, Urminsky & Zheng 2006 的咖啡卡实验。**争议**：两项均为单一研究组的田野研究，独立大样本复现有限；后续工作显示效应依赖"预置被解释为已获得的赠予"，当预置被识别为任意或无成本时效应消失甚至反转（欺骗感）；"起点越高越好"不成立，起点过高会压低感知目标价值。v1 把伪进度与目标梯度混为一条，实际两者的过载阈值与适用条件不同
**Effect**: 中等：原研究约 1.5–2× 完成率提升，仅在预置有可解释来源、奖励真实有价值、路径单一时成立；在被反复使用过该手法的品类中效应趋零，在用户曾因此受骗的个体上为负

**机制链**: 任务被呈现为已有部分完成而非从零开始 → 已投入感使放弃被感知为损失，同时剩余距离变短 → 启动概率上升、早期放弃率下降，完成率提高
**剂量**: 弱 在进度条上标出已完成的前置动作（读完引导、填完基本信息），不虚构任何量 ；中 迁移或预置一段有事实依据的起点（历史数据导入、试用期计入），并显式说明来源 ；强 起点 + 分段可见 + 临近完成的加速，使早期每一步都产生可见位移，并让"已完成"可被用户自己核对 ；过载 预置量过大且无来源（一进来就 80%）→ 用户判定进度为装饰，感知目标价值下降，在发现"其实什么都没做"时产生欺骗感，完成率与信任同时下降
**时间动态**: 起效 首次看到进度状态即生效（分钟级） · 衰减 同一手法在同一用户身上重复 2–3 个周期后收益衰减到接近零 · 饱和 品类内普遍采用后用户对起点一律打折，机制退化为无信息装饰，且已消耗的可信度无法回收
**调节变量**: 个体 对奖励有真实需求、目标承诺高者效应强，怀疑倾向高或曾被同类手法欺骗者效应为零或负；文化 个人成就取向文化中"已投入"是激励，关系取向文化中同伴共同进度比个人进度更有效；情境 路径单一、周期短、奖励明确时最强，目标模糊、可随时替换、奖励价值不确定时最弱
**失效信号**: 预置比例与完成率的相关性转负；用户在评价或社区指出"一进来就 50%"；进度条中段的单日流失率高于起点；完成奖励领取率显著低于完成率；同一用户第二次遇到同类预置时完成率不高于零起点版本
**可测代理**: 预置组与零起点组的完成率与 7 日留存差；进度条上最后一次交互的位置分布；完成奖励领取率；评价与客服中"进度是假的"类文本的词频
**交互**: × MR-01 目标梯度 → 起点抬高同时缩短剩余距离，两机制在起点处叠加，过载阈值也相同，一起越过时崩塌更快；× CA-05 时间折扣 → 伪进度把"开始"的收益拉到当下，是降低有效贴现最廉价的手段；× MR-04 身份承诺 → 起点只有在被解释为"你已经做了 X"时才生成身份证据，否则只是装饰；× CA-02 认知负荷 → 进度条把"还剩多少"外化为单一数字，卸载了用户的心理记账，COMBO-11 的稳定性主要来自这一层
**边界**: 不得虚构进度——预置必须有可核查来源（数据迁移、已完成前置动作、试用期），无来源的预置属欺骗性设计；金融、健康、教育合规场景中进度不得暗示已完成实际未完成的法定或安全步骤；不得把进度与不可退付费绑定以制造沉没成本

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.87；Effect Size: Large

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
**Tier**: 常用
**Evidence**: B — 赌博研究提供最直接的证据：Clark et al. 2009 的 fMRI 研究显示近失结果激活与获胜重叠的奖赏相关区域并提升继续游戏的动机；Dixon 系列研究显示近失在老虎机上的排列方式可显著提高继续下注率。**争议且必须分开写**：近失的效应方向取决于任务类型与归因——在**技能型、可重试**任务中近失提升再参与（"我差一点就做到了"提供具体可达路径），在**运气型、不可控**任务中近失提升的是继续下注，这是对经营者有利、对用户有害的方向；Reid 1986 把近失读作"强化的近似"与后续把它读作"认知扭曲"的两种解释并存，未被裁决。当差距被感知为任意、或机会不在近端时，近失只产生挫败与退出，v1 的"within range"警告方向正确但没有给出机制
**Effect**: 中等偏大且方向依赖归因：差距小（约 10% 以内）、可归因于自身努力、下一次机会在近端时，再参与率显著上升；差距大、归因于运气或系统、机会遥远时效应反转为退出；在运气型结构中效应最强也最有害

**机制链**: 结果接近但未达目标 → 反事实思维被激活（"只差一点"），并生成一条具体可及的下次路径 → 再参与动机上升，投入或下注增加
**剂量**: 弱 在结果页给出剩余差距的客观数字（"还差 2 项达标"），不做情绪化措辞 ；中 同时给出可达路径与时间窗（"本周还差 2 次，周末前可完成"），使差距归因指向用户可控的行为 ；强 在临近处叠加一次性机会（"最后 3 小时双倍计入"），并把差距压缩成单一可比数字，让"下一次"确定在近端 ；过载 反复制造近失而机会不可控（每次都差一点、每次都由随机决定）→ 用户识别为设计而非运气，产生被戏弄感，退出率与投诉上升，近失反转为不信任
**时间动态**: 起效 单次结果反馈内即时（秒级到分钟级） · 衰减 同一用户的近失提示在第 3–5 次后不再提升动机，转而提升"被操纵"感 · 饱和 长期近失供给把用户训练成对差距脱敏，此后连真实可达的目标也被折价，且该脱敏会外溢到其他产品的进度提示
**调节变量**: 个体 成就动机高与内控型归因者被近失激励，外控型与高神经质者被近失放大挫败；文化 成就取向与低不确定性规避文化中近失被读作"再试一次"，高不确定性规避文化中读作"系统不公"；情境 技能型、可重试、机会近端时最强，运气型、不可控、机会遥远时最弱且有害
**失效信号**: 近失提示出现后次轮参与率不升而降；评论中出现"每次都差一点，明显是设计好的"；用户指出差距数字与实际行为无对应关系；近失组在第 3 次之后的投诉率高于对照组；近失型活动的付费转化上升而 30 日留存下降（典型有害信号）
**可测代理**: 近失组与普通失败组的次轮参与率差；近失提示次数与再参与率的相关曲线（找拐点）；差距归因抽测（用户认为差距由自己还是系统决定）；近失组的 30 日留存与投诉率
**交互**: × MR-01 目标梯度 → 近失把"下一次机会"拉到近端，与目标梯度在临近处叠加，COMBO-05 的锁定效应由此产生；× CA-04 注意极限 → 近失提示是最强的注意捕获物之一，在高竞争界面会吞掉主行动的全部注意预算；× MR-12 奖励变异 → 近失 × 变动奖励构成赌博机的核心结构，在运气型任务中叠加即为成瘾性设计
**边界**: 不得在运气型、不可控的奖励结构中使用近失提示——这是老虎机的核心机制，对问题赌博人群构成不成比例的伤害；不得虚构差距（把用户从未接近过的目标描述为"差一点"）；金融、健康、教育评价场景中近失不得用于诱导追加投入或复购

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.89；Effect Size: Large

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
**Tier**: 核心
**Evidence**: A — 强化程序的行为学结论复现良好：变动比率（variable ratio）程序产生更高的反应率与更强的抗消退性（Ferster & Skinner 1957 起的大量动物与人类研究，老虎机与游戏化中的田野观察一致）。**但机制归因必须修正**：流行说法"多巴胺=快乐，所以变动奖励让人上瘾"是错的。Berridge & Robinson 1998、Berridge & Kringelbach 2015 区分 wanting（激励显著性，多巴胺依赖）与 liking（享乐愉悦，阿片与内源性大麻素依赖）——多巴胺被耗竭的动物仍表现 liking 的享乐反应，而 wanting 被削弱；因此变动奖励强化的是**寻求**，不是**愉悦**。这解释了为什么参与度与主观满意度会分离。伦理侧的伤害证据也较强：Dixon 等对老虎机结构的研究与问题赌博流行病学显示该结构对易感人群伤害不成比例
**Effect**: 大（对行为频率与抗消退），但**不等于主观收益**：在剥夺状态与显著线索下反应率可达固定奖励的数倍；饱足、无线索、低卷入时迅速归零；抗消退性使已形成的寻求行为极难停止，这既是效力来源也是危害来源

**机制链**: 奖励在时间与概率上不可预测 → 奖赏预测误差驱动激励显著性上升（wanting 增强，liking 不随之增强） → 寻求行为的频率与持续性上升，且对消退更抗性
**剂量**: 弱 奖励内容或时机有变化但完全可解释（"每周不同主题"），不引入概率不确定 ；中 在明确可预期的总体结构内加入小比例不确定（保底 + 偶发加成），并公开概率与上限 ；强 概率与时机同时不可预测、配合显著线索（音效、动画、倒计时）并允许可重复投入的循环，使"下一次"始终可能更好 ；过载 概率压到极低且无保底（长时间无奖励）→ 多数用户转为外显挫败与流失，少数用户进入强迫性使用（追损、失控），机制从参与驱动反转为伤害驱动并带来监管暴露
**时间动态**: 起效 首次不可预测奖励后即建立（单次到数次） · 衰减 抗消退性使行为在移除奖励后仍持续很久（这正是危险所在），但主观满意度在数周内先下降 · 饱和 长期变动奖励抬高基线需求（"上次给的多"），固定奖励不再有效，需不断加码，形成奖赏通胀
**调节变量**: 个体 冲动性、感觉寻求与多巴胺相关特质高者更易被捕获，问题赌博筛查阳性者风险不成比例；文化 对赌博容忍度高的辖区监管宽松但伤害率不低，宗教与强集体主义语境中公开的运气型机制接受度低；情境 剥夺、无聊、孤独与深夜状态下效应最强，有明确外部目标与时间边界时最弱
**失效信号**: 参与度上升而主观满意度与 NPS 下降（wanting 与 liking 分离的典型指纹）；使用时长分布极端右偏（P99 远超中位）；评论与客服出现"停不下来""想把输的追回来"；奖励移除后使用量衰减极慢且伴随负面情绪；收入集中于少数重度用户
**可测代理**: 使用时长分布的基尼系数或 P99/中位比；奖励移除后的行为衰减曲线（半衰期）；主观满意度与使用时长的相关系数（为负即已分离）；问题赌博/强迫性使用筛查量表（PGSI 类）的分布
**交互**: × MR-03 习惯回路 → 变动奖赏强化的是寻求而非自动性，混用会让习惯持续依赖奖赏、失去对奖赏的不敏感性，COMBO-07 的稳定收益因此被侵蚀；× MR-11 近失效应 → 近失 × 变动奖励是赌博机核心结构，在运气型任务中叠加为成瘾性设计；× MR-05 SDT → 变动奖赏是最强的控制性因子，直接抵消自主支持带来的内化
**边界**: 不得用于运气型、可变现、可追损的奖励结构（赌博式设计）；未成年人、问题赌博筛查阳性者与情绪脆弱人群禁用；概率与上限必须公开——隐藏概率在多个辖区已构成违法（如抽卡概率披露要求）；不得把变动奖励用于健康行为、用药依从或金融决策

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.93；Effect Size: Extreme

See AD-01 (Variable Ratio Reinforcement) — this is the motivational perspective of the same mechanism.

**Key insight for design**: Don't make reward schedules predictable. The unpredictability IS the engagement mechanic.

**Spectrum**:
```
Fixed → Variable → Random
Low engagement → High engagement → Maximum compulsion (ethical threshold)
```

**Ethical design**: Variable schedules create the most engagement but also the most compulsive behavior. Design with explicit intention about where on this spectrum you want to sit.
