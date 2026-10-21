# Attention Economics — Capture, Budget, and Recovery

> **Domain**: attention allocation · notification systems · feed design · signal-to-noise management · interruption cost
> **Use when**: the problem is not just persuasion, but competition for limited user attention across feeds, notifications, tasks, or interfaces
> **Scope**: attention budget, interruption cost, novelty decay, notification value, feed reward density, channel fatigue, attention recovery

---

## Why Attention Needs Its Own Model

Many behavioral models explain why users click. Attention economics explains whether they notice, tolerate, and keep noticing your prompts over time.

Use this file when the design question sounds like:

- "How often should we notify?"
- "Why are users muting or ignoring us?"
- "How do we compete for attention without burning trust?"
- "Why did this hook stop working after repeated exposure?"
- "How do we manage feed novelty without becoming exhausting?"

This file is especially relevant for:

- notifications
- feeds
- reminders
- inboxes
- dashboards
- productivity tools
- content systems

---

## Core Principle

Attention is not a static asset. It behaves like a constrained budget with compounding penalties for waste.

The practical chain is:

```text
signal emitted
-> attention captured or ignored
-> value confirmed or rejected
-> source reputation updated
-> future signals become easier or harder to notice
```

Each low-value interruption taxes the next one.

---

## Main Concepts

## AE-01 · Attention Budget 注意力预算
**Tier**: 核心
**Evidence**: C — 概念框架来自 Davenport & Beck 2001《The Attention Economy》与 Simon 1971 "attention is the bottleneck resource" 的论断；"注意力是有限资源"这一层有实验室基础（Kahneman 1973 的容量模型、Wickens 1984/2002 的多资源理论），但"每人每天有一个可消耗的注意力预算、且跨渠道共享"是把实验事实外推成工程隐喻，**没有直接测量证据**；行业侧的"预算超量则总响应下降"几乎全部来自平台内部数据与厂商 benchmark 报告，未经同行评审
**Effect**: 中等偏大，但只在同一用户、同一时段、同一渠道内成立：单位时间可处理的高显著性信号数量有上限，超出后新增信号被稀释而非叠加；跨渠道（推送 vs 邮件 vs 站内）是否共享同一预算尚无定论，把它当成统一账户会高估抑制收益
**机制链**: 同一时段内高显著性信号数量上升 → 有限容量的注意选择机制按显著性竞争、单条信号分得的加工资源下降 → 单条响应率与该来源的注意倾向同时下降
**剂量**: 弱 默认静默，只在用户已建立的活跃窗口内发一条高相关信息 ；中 把触达按价值排序成组合、每日设硬上限，低价值条目降级到摘要或收件箱 ；强 只在用户自己设定的时机与阈值上触发（价格提醒、任务到期），并给出可核对的触发原因 ；过载 为"不浪费预算"而把一切自动化、连高价值事件也压进摘要 → 用户失去对时间敏感事件的感知，开始定期手动检查（预算反被浪费），并把产品归类为"会漏事"，净价值转负
**时间动态**: 起效 分钟级（单次超量即可观察到响应率下降） · 衰减 日级：当天被浪费的预算在次日以更低的基线响应率体现，通常 2–3 天内恢复 · 饱和 周级：长期超量后预算不是恢复而是被重新分配，用户把该渠道整体移出可用集合（关通知、退订、卸载）
**调节变量**: 个体 基线注意控制力强与工作负荷高者预算更小、对超量更敏感，低负荷期预算显著扩大；文化 高语境、强关系义务的市场里"必须回复"的社会成本会挤占预算，低语境市场里渠道分层更清晰；情境 通勤、会议、睡眠窗口内可用预算接近零，节假日与项目截止期预算被重新排序（方向确定，幅度随人群而异）
**失效信号**: 单条触达响应率随当日触达总数单调下降且超线性；同一内容的第二次发送打开率低于第一次的一半；用户关闭某一类而非全部通知（说明是预算问题不是价值问题）；"漏看了"类客诉集中在被合并进摘要的高价值事件
**可测代理**: 同一用户当日触达条数与其后单条响应率的分层曲线；每渠道"每日有效触达条数"的边际响应拐点；关闭通知与退订率对触达频次的斜率；摘要合并后高价值事件的打开延迟分布
**交互**: × AE-02 打断成本 → 预算消耗与打断成本同向叠加，用户专注时二者相乘而非相加，超量后的响应坍塌快于任一单独机制；× AE-04 信源声誉 → 预算耗尽时用户不是减少注意而是重排来源优先级，一次超量会永久降低该来源在预算中的默认权重；× AE-03 信号衰减 → 预算超量与重复暴露同时发生时会合流成"该渠道不重要"的单一结论，衰减速度远快于任一项单独预测
**边界**: 不得把"注意力预算"当成可精确计量并据此对用户限流的依据——预算大小无法直接测量，任何"每日 N 条"的硬上限都是工程约定而非生理常量；不得用预算论证对紧急与安全类信息（医疗告警、支付异常、安全事件）做降级或摘要合并，此类信息必须走独立的高优先级通道；在同意与合规通知（条款变更、扣费提醒）上压缩触达会构成告知瑕疵
**可证伪条件**: 本记录按 C 级双侧标注：若一项跨渠道饱和实验（在一渠道内变动触达量、其余渠道保持不变，测量是否出现可测的此消彼长）显示渠道间存在稳定替代关系，则“注意力预算跨渠道共享”可上调至 B；若既无跨渠道替代、又在同一渠道内找不到能预测响应衰减的容量参数，则本记录应降级为“预算是无法分离出任何可测参数的工程隐喻，不存在可用阈值”

### 1. Attention Budget

Users do not grant infinite attention to a product. They grant a moving budget:

- per day
- per context
- per channel
- per emotional state

Design implication:

- notification permission is not a permanent entitlement
- every interruption spends scarce future attention

## AE-02 · Interruption Cost 打断成本
**Tier**: 核心
**Evidence**: B — 打断的真实成本有实验与田野证据：Mark, Gudith & Klocke 2008 观察到被打断后回到原任务的间隔中位数约 23 分钟（n=48，观察法、非随机对照，且"23 分钟"常被误引为普适常数）；Iqbal & Horvitz 2007 显示任务切换后的恢复时间随任务复杂度上升；Leroy 2009 的 attention residue 表明切换后残留影响后续表现；Pielot et al. 2017 的 24 小时关闭通知实验（n=30）显示专注与情绪改善但部分人感到错过信息。**争议**：这些研究样本都小、场景为知识工作，"打断成本随专注度上升"的方向稳定而幅度不可外推，把 23 分钟当作产品决策常数没有依据
**Effect**: 中等偏大且高度依赖时机：在深度专注、社交场合、睡眠窗口内打断，成本可达低价值场景的数倍；在用户主动等待结果时打断，成本接近零甚至为负
**机制链**: 信号在用户处于高投入任务中途到达 → 注意被迫从当前任务的目标栈切换到信号，切换与切回都消耗工作记忆与目标维持 → 当前任务错误率与完成时间上升，且该来源被记为"会打断我"
**剂量**: 弱 把信号放进被动拉取的位置（收件箱、站内消息、下次打开时的摘要），不抢占前台 ；中 在用户已建立的活跃窗口内推送到前台，一次只带一个可执行动作 ；强 只在用户显式设定的事件上抢占（价格触发、安全告警、协作阻塞解除），并同时给出"为什么现在打扰你"的一句话 ；过载 以"提升触达"为名对每次状态变化都抢占前台 → 用户的应对不是逐条判断而是整体关闭或开免打扰，此后连高价值告警也收不到，触达能力被清零
**时间动态**: 起效 秒级（抢占前台即产生切换成本） · 衰减 单次打断的影响在 10–30 分钟内衰减，但"这个来源会打断我"的预期跨天累积 · 饱和 重复打断后用户进入前置防御状态（系统级免打扰、通知摘要、静音该来源），此时任何频率都不再有效
**调节变量**: 个体 执行功能与工作记忆容量高者切换成本较低但残留更久，ADHD 特质人群被打断后更难回到原任务；文化 高关系义务文化中"不及时回"的社会成本高，打断被容忍但怨恨累积，低语境文化中被打断更直接被判定为失礼；情境 会议、驾驶、睡眠、育儿窗口内成本极高，等待电梯与排队等碎片窗口内成本接近零
**失效信号**: 通知被点开后 5 秒内返回原应用（说明是打断而非价值）；系统级免打扰与专注模式的开启率上升；应用内停留时长不变但推送打开率下降；客服与商店评论出现"太吵""关掉了"类表述；关键告警的响应延迟与总触达量同向上升
**可测代理**: 推送点开后的首次有效操作率与返回原应用时间；被打断时段（由专注模式或前后台日志推断）的响应率分层；免打扰开启率对触达频次的斜率；高优先级告警的响应时间中位数
**交互**: × AE-01 注意力预算 → 专注时打断同时消耗预算与抬高单位成本，二者乘积决定渠道寿命，任一项单独看不出来；× AE-05 通知经济学 → 频次规则若只按总量而不按专注状态分层，会在最贵的时刻发送最便宜的消息；× AE-08 渠道疲劳 → 高频打断是渠道疲劳最快的成因，疲劳一旦形成，降频无法恢复原有触达
**边界**: 不得以"降低打断成本"为名，把安全告警、扣费提醒、条款变更、医疗结果等必须及时获知的信息降级为被动拉取——这既违反产品诚信也构成告知义务瑕疵；不得在驾驶、医疗设备操作、紧急作业等场景使用任何抢占式打断；不得用"用户自己可以关"为默认高频抢占辩护，默认值即设计选择
**可证伪条件**: 若在一项随机分配打断时点的实验中（而非 Mark, Gudith & Klocke 2008 的观察法），被打断组的原任务恢复时间不显著长于匹配的未打断对照组，则“打断有可测的恢复成本”的声称不成立，本记录应降级为“打断成本只在自我报告与深度任务中可观察，行为层面不显著，23 分钟不得作常数”

### 2. Interruption Cost

Not all interruptions cost the same.

Cost increases when:

- the user is focused
- the timing is socially wrong
- the message is low-value
- the next action is unclear
- the user has recently been interrupted already

High interruption cost with low value creates fast channel death.

## AE-03 · Signal Decay 信号衰减
**Tier**: 核心
**Evidence**: C — "重复暴露导致响应衰减"的方向有广泛支持：habituation 的跨物种实验室证据很强（Rankin et al. 2009 综述），广告 wear-out 与 banner blindness 的田野观察一致（Benway 1998；Resnick & Albert 2014 的眼动研究显示用户系统性跳过横幅区域）。**但**衰减速度、次数阈值与恢复条件没有稳定参数：经典 wear-out 曲线来自 1970 年代单一媒介数据，无法迁移到推送与信息流；"第 3 次失效"这类数字属行业经验，无同行评审来源
**Effect**: 中等，方向确定而幅度不确定：同一格式、同一措辞、同一紧迫标记的响应率随重复单调下降，但拐点位置取决于该信号原本的信息量与用户对该类别的先验；把衰减当固定半衰期会系统性误判
**机制链**: 同一格式的信号反复出现且未带来新信息 → 该格式被降级为可预测的背景，注意选择机制不再为它分配资源 → 响应率下降，且对同类格式的其他信号一并降权（泛化）
**剂量**: 弱 保留格式不变、只更换具体内容与数字，让信息量承担全部差异 ；中 在格式层引入轮换（不同版式、不同载体、不同入口），并确保每次真的有新信息 ；强 把重复换成事件驱动：只在状态真的变化时出现，并让用户能验证"变了什么" ；过载 为对抗衰减而不断加大刺激强度（更红的角标、更急的倒计时、更响的措辞） → 强度通胀使所有信号同时失去区分度，用户对整类提示进入系统性忽略，连真实紧急信号也被跳过
**时间动态**: 起效 首次重复即可观察到小幅下降，明显衰减通常在 3–5 次同类暴露内出现（方向稳定、次数因内容而异） · 衰减 单次衰减在数天内可部分恢复，格式层面的降权在数周内不可逆 · 饱和 长期使用后该格式在该用户处永久失去注意分配，只能换载体（渠道迁移），无法靠内容补救
**调节变量**: 个体 认知需求高、主动核对信息的用户衰减更快（他们更快学会该格式无信息量），低卷入用户衰减慢但一旦衰减更彻底；文化 高不确定性规避市场对重复的安全提示容忍更久，信息流密集的高刺激市场衰减更快；情境 信息密度高的界面（信息流、收件箱）衰减最快，低频高利害场景（医疗、金融账单）衰减最慢
**失效信号**: 同一格式的点击率逐次下降而曝光量不变；用户对同类元素的首次注视时间缩短（眼动或停留时间代理）；点击后立即返回的比例上升；真实紧急事件的响应率同步下降（泛化污染的确定性证据）；用户开始用"又是这个"类表述
**可测代理**: 同格式第 n 次暴露的响应率曲线与拐点；同一用户对不同格式的响应差异（格式轮换实验）；点击后 5 秒内返回率；真实紧急信号与常规信号的响应率比值
**交互**: × AE-01 注意力预算 → 衰减让同一预算下可用的有效信号变少，预算看似充足实则已无可调用资源；× AE-06 回报密度 → 若密度靠提高频率而非提高单条价值维持，衰减速度会快于密度收益；× PE-11 人为稀缺 → 稀缺标记的衰减最快且不可逆，一旦被识破，真实稀缺也不再被相信
**边界**: 不得用"对抗衰减"为名提高刺激强度或制造伪变化（假倒计时、假剩余量、假新版本）——在中国构成《反不正当竞争法》第 8 条虚假宣传与《明码标价和禁止价格欺诈规定》下的价格欺诈，在美国构成 FTC Act 第 5 条下的欺骗性行为，在欧盟落入《不公平商业行为指令》附件一的黑名单；安全、医疗、金融类提示不得为"保持新鲜"而改写措辞或降低显著性
**可证伪条件**: 本记录按 C 级双侧标注：若同一格式的重复暴露在控制内容质量后仍显示单调且跨渠道参数稳定的响应衰减曲线，则衰减速度可上调至 B；若响应下降在控制内容质量后消失，或半衰期在两个渠道间相差一个数量级以上，则本记录应降级为“衰减无法与内容质量分离，不存在可用的次数阈值”

### 3. Signal Decay

Any repeated cue loses force over time.

Examples:

- the same urgency badge
- the same promo wording
- the same notification format
- the same feed pacing

If the reward does not justify repeated exposure, the cue becomes background noise.

## AE-04 · Source Reputation 信源声誉
**Tier**: 核心
**Evidence**: C — 信源可信度影响说服与注意的方向有经典支持（Hovland & Weiss 1951 及 sleeper effect；Pornpitakpan 2004 元分析显示高可信源短期说服力更强、长期差异缩小），但"低价值推送会让整个应用的使用下降"这一具体主张来自平台内部指标与行业复盘，没有公开的对照实验；把信源声誉当成可精确折算的权重属于工程假设
**Effect**: 中等偏大且不对称：一次低价值触达对声誉的损害大于一次高价值触达的增益，恢复需要连续多次兑现；对已被归类为"可忽略"的来源，单次高质量内容通常无法把它拉回
**机制链**: 用户对同一来源的多次触达结果做归纳 → 该来源被归入有用、可选、可忽略或已屏蔽的某一档，并成为后续注意分配的默认先验 → 该来源的新信号在内容被评估之前就已被降权或跳过
**剂量**: 弱 保持渠道只承载与其定位一致的内容（促销渠道不发系统告警，告警渠道不发促销） ；中 建立可核对的价值承诺（只在这个渠道发什么），并接受用户按类别订阅与退订 ；强 让每一次触达都可被事后验证兑现（发过的提醒真的发生过、报过的变化真的存在），并公开触达频次与内容类型 ；过载 用同一来源反复承载低价值内容以摊薄成本 → 来源被整体重分类为噪音，此后该来源的所有内容（含高价值）在评估前即被跳过，声誉损失跨渠道扩散
**时间动态**: 起效 单次触达即可小幅更新，3–5 次一致的低价值触达后完成重分类（天级到周级） · 衰减 负面重分类衰减很慢（月级），正面声誉若无持续兑现则按周衰减 · 饱和 一旦进入"已屏蔽"，任何内容策略都不再产生触达，只能换渠道或等用户主动重新订阅
**调节变量**: 个体 高信任倾向者初始给高分但落差后的下调更陡，怀疑倾向者需要更多次兑现才建立声誉；文化 高权力距离市场更依赖机构身份而非逐次兑现，低语境市场更依赖逐条内容的相关性；情境 高利害场景（支付、健康、安全）中声誉权重最高，娱乐场景中内容本身权重高于来源
**失效信号**: 同一来源的高价值内容打开率与低价值内容趋同（说明已被整体跳过）；用户按类别退订而非全部退订（说明在做来源内分层）；应用总使用时长下降而推送打开率下降更快；商店评论与社媒出现"这个 app 只会发广告"类定性；重新订阅率长期低于退订率
**可测代理**: 按内容类型分层的打开率与点击后完成率；退订的类别分布；同一用户对高价值与低价值触达的响应比；卸载前 30 天的触达构成；重新订阅率
**交互**: × AE-03 信号衰减 → 声誉下降与格式衰减互相加速，用户会用一次判断同时封掉格式与来源；× AE-08 渠道疲劳 → 渠道疲劳本质是来源声誉在渠道维度的投影，二者在同一批用户上同时触顶；× TR-02 可读性 → 触达内容不可解析会先被记为"不专业"，声誉损失先于价值评估发生
**边界**: 不得用"维护信源声誉"为名，把用户已订阅或已同意的类别静默取消或降级（例如把交易类通知并入营销摘要）——这在中国违反《消费者权益保护法实施条例》关于真实全面告知的要求，在美国落入 FTC Act 第 5 条下的欺骗性省略；不得把声誉指标用于对用户差别定价或差别服务
**可证伪条件**: 本记录按 C 级双侧标注：若一项对照实验显示低价值触达不仅降低该次响应、还使后续整体使用时长显著下降，则“信源声誉是可消耗的共享资产”可上调至 B；若低价值触达只降低其自身的响应、对整体使用无溢出，则本记录应降级为“声誉预算不存在，每次触达独立结算”

### 4. Source Reputation

Users learn whether a source is worth checking.

After repeated low-value signals, the source is reclassified:

- from useful
- to optional
- to ignorable
- to actively blocked

This is why one bad notification strategy can reduce total app engagement, not just notification engagement.

---

## Attention Budget Model

Use this mental model:

```text
Net Attention Value
= relevance
+ timing fit
+ expected reward
- interruption cost
- repetition fatigue
- trust damage from weak signals
```

If net value is negative enough often enough, the channel collapses.

Do not optimize open rate only. Optimize lifetime willingness to notice.

---

## High-Value Attention Patterns

### Pattern 1: High Signal Density

Each interruption should feel more informative than the surrounding noise.

Examples:

- "Your draft is approved"
- "2 teammates replied to your blocker"
- "You are one step away from completion"

Bad examples:

- generic nudges
- vague promo reminders
- low-context activity noise

### Pattern 2: Context Matching

Match the signal to the likely task state.

Examples:

- planning prompt in the morning
- re-engagement reminder at a previously active time
- progress reminder near a meaningful deadline

Do not send the same prompt independent of context.

### Pattern 3: Variable but Coherent Reward

Feeds and notifications can benefit from unpredictability, but only when the reward remains relevant.

Good:

- occasionally surprising, relevant updates
- mixed feed novelty within a trusted topic boundary

Bad:

- random irrelevant novelty
- algorithmic surprise with no user value

### Pattern 4: Recovery Windows

Users need quiet periods.

Strong systems alternate:

- capture
- value delivery
- recovery

Without recovery, even good signals become exhausting.

---

## AE-05 · Notification Economics 通知经济学
**Tier**: 常用
**Evidence**: C — **这一族主要来自行业实践而非同行评审实验**：通知频次与内容分层的规则来自 Firebase、OneSignal、Airship 等厂商 benchmark 报告与增长团队复盘，样本与口径均不公开；学术侧只有少量小样本实验（Pielot et al. 2017 的 24 小时关闭通知，n=30；Iqbal & Horvitz 的 bounded deferral 研究），且都未检验"每日 N 条"这类具体上限。没有任何 RCT 证明某个频次阈值普适有效，因此本记录如实标 C：方向可用，数字不可搬
**Effect**: 小到中等且强条件依赖：在用户已建立使用习惯、通知内容与既有关切匹配时，适度触达提高回访；在习惯未建立或内容不匹配时，触达主要产生退订与免打扰，净效果为零或负
**机制链**: 触达被按用户关切排序并限制在可承受量内 → 单条触达被判定为"值得看"而非"系统在提醒自己存在" → 该渠道的长期可触达性（而非单次打开率）得以维持
**剂量**: 弱 只发事务性与用户自己设定的事件通知，营销触达默认关闭、由用户主动开启 ；中 建立内容分级（事务、协作、进度、营销）并给每级独立开关与独立频次上限，默认值偏低 ；强 触达时机与用户历史活跃窗口对齐，附带可核对的触发原因，并把频次与内容构成对用户可见可改 ；过载 用 A/B 把频次一路推到打开率曲线的最高点并据此定为默认 → 短期打开数上升、长期可触达人数下降，渠道在数月内整体失效，且用户已把"关通知"当作对该类应用的默认动作
**时间动态**: 起效 单次触达秒级见效，频次调整的留存效应需 1–2 周才可读 · 衰减 频次收益在 2–4 周内被习惯化抵消，超量后的退订在 4–8 周内累积显现 · 饱和 长期超量后渠道进入不可逆的关闭状态，重新开启率通常远低于首次开启率
**调节变量**: 个体 已有强使用习惯的用户对频次更宽容，新用户在第 1–2 周内对任何营销触达都极度敏感；文化 高关系义务文化中即时通讯类触达被期待而营销触达被强烈排斥，低语境市场对渠道分层（邮件归邮件、推送归推送）更严格；情境 通勤与午休窗口容忍度高，夜间与会议窗口容忍度接近零，节假日的营销触达容忍度显著下降
**失效信号**: 推送权限授予率与单条打开率同时下降；退订集中在第 2–3 次营销触达；免打扰与专注模式开启率上升；同一用户打开率与发送频次呈负相关；重新开启通知的用户占比长期低于 10%
**可测代理**: 分内容层级的打开率、退订率与权限授予率；每用户每周有效触达数的边际收益曲线；关闭通知后的 30 天回访率；重新开启率
**交互**: × AE-02 打断成本 → 频次规则若不按专注状态分层，会在最贵的时刻发最便宜的消息，退订集中出现在该时段；× AE-04 信源声誉 → 频次超量首先损害来源声誉而非单条内容效果，二者不可分开优化；× AE-07 自然停止点 → 缺少停止点的产品必须靠通知把人拉回，这会把通知变成对设计缺陷的补偿，频次永远降不下来
**边界**: 不得把"打开率最优频次"当作默认值上线——以短期打开率优化频次会系统性高估可发送量，因为退订与权限关闭的成本滞后且不在同一指标里；自动续费、价格变更、条款更新等法定告知不得并入营销摘要或受营销频次上限约束（中国《消费者权益保护法实施条例》第 10 条要求自动展期与自动续费在扣费前以显著方式提示；美国 ROSCA 与 FTC Act 第 5 条要求清晰披露；欧盟 DSA 第 25 条禁止用界面设计削弱消费者的自主选择）；不得在夜间与已知睡眠窗口发送非紧急触达
**可证伪条件**: 本记录按 C 级双侧标注：若一项预注册随机试验以退订率与权限关闭率为主要终点，显示某个具体频次上限在两个独立队列上稳定优于不设上限，则本记录可上调至 B；若任何上限的退订率都不显著优于不设上限（即行业 benchmark 的‘最优频次’不可复现），则本记录应降级为“频次上限只是任意工程约定，不存在可用阈值”

## Notification Economics

### Notification Budget Rules

Treat notifications as a ranked portfolio:

1. mission-critical
2. socially meaningful
3. progress-relevant
4. optional engagement
5. promotional

If categories 4 and 5 crowd out 1-3, the whole channel degrades.

### Timing Rules

Strong notification timing depends on:

- habit history
- current likely task mode
- urgency reality
- social appropriateness

Bad timing can destroy good content.

### Frequency Rules

More is only better up to the point where the source is reclassified as noise.

Use:

- lower defaults
- explicit preference controls
- opt-up rather than opt-down when possible

### Notification Quality Test

Before sending, ask:

1. Would I want this right now?
2. Is the next action obvious?
3. Does this create value beyond reminding the user we exist?
4. Would repeated exposure make the source feel annoying?

If the answer to 3 is no, do not send it.

---

## Feed Economics

### Novelty Gradient

Feeds need a novelty band:

- too predictable -> ignored
- too chaotic -> abandoned

The best feeds mix:

- familiar topic relevance
- occasional surprise
- visible reward
- manageable cognitive load

## AE-06 · Reward Density 回报密度
**Tier**: 常用
**Evidence**: C — 可变比率强化在实验室动物上有强证据（Ferster & Skinner 1957），但外推到信息流与推送的"回报密度"属于类比而非验证；"每 N 屏出现一个高价值单元决定留存"这类结论来自产品分析而非对照实验；可变奖赏与成瘾的因果关系在人类田野研究中混杂严重（屏幕时间与幸福感的效应量在 Orben & Przybylski 2019 等的重新分析中大幅缩小）。方向可用，参数不可信
**Effect**: 中等，仅在单条价值可被用户快速判断且密度稳定时可维持扫描行为；密度靠降低质量门槛维持时，短期会话时长上升而回访下降
**机制链**: 用户在连续低价值单元中持续扫描并偶尔命中高价值单元 → 不确定的回报维持扫描行为（间歇强化），单条成本被摊薄 → 会话时长与回访频率上升，但感知成本与事后后悔同步累积
**剂量**: 弱 保持单元质量下限，宁可少发也不凑数 ；中 在稳定的主题边界内混入少量意外但相关的高价值单元，并把高价值单元放在可预期的位置附近 ；强 让密度可被用户自己调节（主题、频率、信源权重），并给出"为什么给你看这条"的依据 ；过载 为拉高密度而降低价值门槛或加大抽取强度（更长下滑、更强钩子、更多"猜你喜欢"） → 命中率下降使扫描成本上升，用户从"再刷一条"转为"关掉"，事后后悔提高，回访与信任同时下降
**时间动态**: 起效 首次会话内即可观察到（分钟级） · 衰减 同一密度在 1–2 周内被适应，需持续提高单条价值而非提高数量 · 饱和 长期高抽取后用户形成"这里没什么可看"的入口级预判，会话时长与打开频次同时下降
**调节变量**: 个体 认知需求高者对低价值单元的容忍更低、对密度变化更敏感，冲动性高者对间歇强化更敏感；文化 集体主义市场对社交类高价值单元权重更高，个人主义市场对信息与娱乐类权重更高；情境 碎片时间容忍低价值单元，整块时间与高认知负荷后更要求密度
**失效信号**: 单次会话内滑动数上升而完读与收藏下降（命中率下降）；会话时长不变但次日回访下降；"没意思""都是重复的"类反馈上升；高价值单元的实际点击率下降（用户已不再相信标记）；退出后短时间内重新打开的比例上升但单次时长下降
**可测代理**: 每 N 个单元的收藏、完读与分享率；命中率（有效互动单元数除以曝光单元数）；会话后自评后悔或"浪费时间"选项的选择率；次日回访率与密度调整的时间对齐
**交互**: × AE-03 信号衰减 → 用提高频率补密度会加速格式衰减，二者叠加时留存下降快于任一单项；× AE-07 自然停止点 → 无停止点时密度下降直接转成事后后悔，用户把"停不下来"归因为产品而非自己；× PE-07 零价格效应 → 免费内容使单条成本感知为零，密度下降不会立刻反映在点击上，只在回访上滞后显现
**边界**: 不得用可变奖赏设计针对未成年人的抽取机制，也不得在健康、金融、赌博相邻品类使用间歇强化提高使用时长（欧盟 DSA 第 25 条与第 38 条对界面设计与未成年人保护有明确约束）；不得把"密度"作为掩盖内容质量不足的手段；抽奖式与赌博式奖励机制在中国受《广告法》与网络游戏、网络直播相关规定限制，不得以"福利"名义规避
**可证伪条件**: 本记录按 C 级双侧标注：若在内容完全相同的条件下，随机变动高价值单元的间隔能稳定改变会话时长与次日回访，则“回报密度是可独立操纵的杠杆”可上调至 B；若回访率不随密度变化、只随内容质量变化，则本记录应降级为“密度不可分离，唯一有效变量是内容质量”

### Reward Density

Users continue when high-value units appear often enough to justify scanning cost.

If the feed requires too much scrolling for too little value:

- users shorten sessions
- check less often
- become harder to re-engage

## AE-07 · Natural Stopping Points 自然停止点
**Tier**: 常用
**Evidence**: C — "无限流缺乏停止点导致事后后悔与疲劳"主要来自自陈量表与行业观察（binge-watching 研究如 Flayelle et al. 2019 报告了自陈后悔，但效应小、方向受测量方式影响），没有把"加入停止点"作为随机干预的对照实验；"会话后感知时间成本上升"在实验室难以测量。如实标 C
**Effect**: 小到中等，方向明确但幅度依赖内容强度：在高抽取内容上，加入明确停止点会降低单次会话时长、提高次日回访与自评满意度；在低强度内容上几乎无差异
**机制链**: 内容流在某个可识别的边界处给出结束信号 → 用户获得一个自然的退出决策点，不必依靠意志力中断连续刺激 → 会话以"完成"而非"被打断"结束，事后评价与回访意愿上升
**剂量**: 弱 在内容块之间保留清晰的分隔与进度（已看完 X 之 Y） ；中 提供显式的收尾单元（今日已更新完、本轮回顾、稍后继续），并把"下次从这里开始"固定下来 ；强 让停止点与真实价值边界对齐（一章结束、一批任务清空），并在停止点给出可带走的产出（摘要、进度、清单） ；过载 把停止点做成强制拦截（每 10 分钟弹窗、必须确认才能继续） → 用户把它体验为打断而非照顾，转向能绕过的替代品，停止点反成流失原因
**时间动态**: 起效 单次会话内即可改变结束方式（分钟级） · 衰减 同一停止点形式的引导力在 1–2 周内减弱，需与真实内容边界绑定才能维持 · 饱和 长期使用后停止点成为常态结构，收益转为"不再产生后悔"的防守性价值，不再提高时长
**调节变量**: 个体 自我控制资源低、夜间使用比例高者从停止点获益最大，高自我控制者几乎无差异；文化 长时段连续消费被社会规范接受的市场中强制停止点抵触更强，重视作息规范的市场中接受度更高；情境 睡前、通勤终点、工作间隙等天然边界处停止点最有效，无外部边界的整块时间最弱
**失效信号**: 停止点出现后的继续率极高（说明只是形式）；次日回访不变而单次时长下降（说明被体验为拦截）；关闭"提醒我休息"类开关的比例上升；用户用多设备或网页版绕过停止点；自评后悔率不降
**可测代理**: 会话结束方式的分布（自然结束与强制中断）；停止点后的继续点击率；次日与 7 日回访率；会话后自评满意度与"时间花得值"选项选择率
**交互**: × AE-06 回报密度 → 密度不足时停止点会被读成"没内容了"，密度充足时停止点才被读成"告一段落"；× AE-01 注意力预算 → 有停止点的产品把预算还给用户，长期可触达性上升；× AE-05 通知经济学 → 有停止点的产品不需要靠通知拉回，通知频次可整体下调
**边界**: 不得把"减少使用时长"包装成卖点却在暗处延长其他路径（加了停止点却加大推送补偿），这属于界面与宣称不一致；不得在安全、医疗、紧急协作场景设置任何强制停止或延时；对未成年人产品的停止点应默认开启且不可由营销侧关闭
**可证伪条件**: 本记录按 C 级双侧标注：若把“加入明确停止点”作为随机干预（而非 Flayelle et al. 2019 的自陈量表）能同时降低单次会话时长并提高次日回访，则本记录可上调至 B；若只有自评后悔下降而会话时长与回访行为不变，则本记录应降级为“停止点只改变事后叙述，不改变使用行为”

### Natural Stopping Points

Infinite scroll is powerful but expensive.

Without natural stopping points:

- attention recovery drops
- fatigue rises
- perceived time cost increases after the session

Add moments like:

- completion cards
- progress summaries
- digest stops
- meaningful pauses

---

## Attention in Productivity and Utility Products

Attention economics is not only for content products.

For utilities and productivity tools:

- every dashboard element competes for finite cognitive bandwidth
- too many highlights means nothing is highlighted
- too many reminders means the system becomes self-defeating

Use strong salience sparingly.

Priority signals should be:

- rare
- legible
- behaviorally actionable

---

## Failure Modes

### 1. Notification Inflation

Too many medium-value notifications collapse the whole channel.

### 2. Hook Burnout

The first hook works, the fifth exposure does not.

### 3. Feed Exhaustion

Attention capture is high, but post-session regret rises, reducing long-term trust.

### 4. Dashboard Saturation

Everything is flagged as important, so users ignore the interface hierarchy entirely.

## AE-08 · Channel Fatigue 渠道疲劳
**Tier**: 常用
**Evidence**: C — 渠道疲劳的直接证据几乎全部是行业数据（推送关闭率、邮件退订率、短信投诉率的逐年变化）与厂商报告；学术侧有通知负荷的现场研究（Pielot et al. 2014 的 in-situ 研究，n=40；Shirazi et al. 2014 关于通知管理的研究），样本小、无长期随访。**没有任何同行评审实验给出"渠道在 N 次低价值触达后失效"的参数**，本记录如实标 C
**Effect**: 中等偏大且不可逆：渠道疲劳一旦形成，降频与提质只能减缓而不能恢复原有触达能力；跨渠道可迁移性有限——用户对推送疲劳后往往不会转向邮件，而是整体降低对该产品的注意
**机制链**: 同一渠道被反复用于低价值目的 → 用户对该渠道形成"打开即成本"的预期并主动屏蔽或忽略 → 该渠道有效触达率下降，成本转嫁到其他渠道与新用户获取上
**剂量**: 弱 为每个渠道定义唯一用途，并在渠道之间不重复同一内容 ；中 建立渠道级频次上限与内容分级，把低价值内容降级到被动渠道，并给用户一键降级入口 ；强 主动收缩渠道组合：关闭低效渠道，把资源集中到用户主动打开的少数入口（应用内、订阅摘要），并公开这一取舍 ；过载 在渠道失效后加大投入（换模板、换标题、加短信兜底）以追回触达 → 疲劳扩散到剩余渠道，用户以卸载或系统级屏蔽作为最终响应，获取成本上升而留存不升
**时间动态**: 起效 单次超量即可观察到该渠道响应率下降（小时到天） · 衰减 渠道级疲劳在数周内累积，降频后需 4–8 周才见部分恢复 · 饱和 长期疲劳后渠道进入结构性失效：即使内容与频次都理想，响应率仍显著低于基线，只能换渠道或重建用户预期
**调节变量**: 个体 多渠道并用、主动管理通知设置的用户更早触发疲劳且更难挽回，低卷入用户疲劳慢但一旦卸载不再回访；文化 短信主导市场中短信渠道疲劳更快，邮件主导的 B2B 市场中邮件疲劳相对慢但退订更彻底；情境 高频竞争品类（电商、内容、外卖）中用户对同一渠道的容忍度最低，低频高价值品类（保险、医疗）中渠道疲劳较慢
**失效信号**: 渠道级打开率与投诉率同向恶化；短信与邮件退订率单月跳升；应用卸载前的 30 天内该渠道触达密度显著高于留存用户；同一内容在多渠道重复发送后总响应低于单渠道；用户开始使用系统级过滤（邮件规则、短信拦截、通知摘要）
**可测代理**: 分渠道的打开率、退订率、投诉率与频次的三维曲线；卸载前 30 天渠道构成；多渠道去重后的总响应率；重新订阅率与渠道恢复周期
**交互**: × AE-04 信源声誉 → 渠道疲劳是声誉在渠道维度的投影，声誉修复不能修复渠道疲劳，二者需分别处置；× AE-02 打断成本 → 高成本渠道（推送、短信、来电）疲劳最快，用它们承载低价值内容是加速失效的最短路径；× AE-05 通知经济学 → 频次策略若只优化单渠道打开率，会把疲劳成本推给尚未失效的渠道，形成逐渠道击穿的序列
**边界**: 不得用"渠道疲劳"为名对已订阅用户静默降低法定告知的送达（扣费、条款、安全通知必须走可验证送达的渠道）；不得在用户明确退订后通过换号、换渠道、换发送方继续触达——中国《广告法》第 43 条与《消费者权益保护法实施条例》对未经同意发送商业信息有明确禁止，美国 CAN-SPAM 与 TCPA 对退订与同意有强制要求，欧盟 ePrivacy 指令要求事前同意；不得把渠道疲劳当作提高短信与电话触达合理性的理由
**可证伪条件**: 本记录按 C 级双侧标注：若一项长期对照研究显示渠道在若干次低价值触达后失效、且降频与提质均不能恢复响应（不可逆性），则本记录可上调至 B；若降频后响应完全恢复，则本记录应降级为“渠道疲劳是可逆的拥挤效应，不是持久状态，不存在失效阈值”

### 5. Channel Mispricing

Using high-cost channels for low-value messages:

- push for weak promos
- SMS for mild reminders
- modal interruption for trivial updates

This spends too much attention for too little value.

---

## Safe Use Rules

- treat attention as borrowed, not owned
- optimize for long-term noticeability, not short-term intrusion
- preserve recovery windows
- do not use high-pressure interruption patterns for low-value prompts
- for trust-sensitive products, explanation and control beat volume and urgency

Read alongside:

- `references/anti-patterns.md` for notification fatigue and trust erosion
- `references/models/perception-attention.md` for capture mechanics
- `references/models/cognitive-architecture.md` for attention resources and prediction error
- `references/models/affective-dynamics.md` for variable reward dynamics
- `references/domain-playbooks/linguistic-triggers.md` when the intervention is at the wording level
