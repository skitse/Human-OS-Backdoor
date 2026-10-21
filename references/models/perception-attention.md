# Perception & Attention — Model Details

## PA-01 · Processing Fluency
**Tier**: 核心
**Evidence**: B — Reber & Schwarz 1999 及 Reber, Schwarz & Winkielman 2004 综述建立了"加工流畅性被误归因为真实性/喜好"的框架；Alter & Oppenheimer 2009 元分析（股票代码、字体、押韵）支持流畅性影响判断。争议：①"流畅性—真实性"联结的可复制性存在争论：Wänke & Hansen 的"真值错觉"综述认为效应依赖于流畅性被误归因于内容而非来源，当被试知道流畅性是被操纵的（字体、颜色）时效应显著减弱甚至反转；②元分析中多数研究的效应量为小到中等，且实验室的字体/对比度操纵与真实营销素材的差异巨大；③"元认知体验"解释（流畅性作为"我理解了"的线索）与"朴素理论"解释（"简单=真"的内隐信念）对同一数据给出不同机制，归属未定；④押韵—真理效应在控制韵律可预期性后缩小；⑤现场转化证据稀薄，多数"清晰文案提升转化"的案例混杂了信息量、长度与具体性
**Effect**: 小到中等，仅在流畅性可被归因于内容本身（而非明显的外观操纵）、且用户处于低动机浅加工时成立；用户被提示注意字体/格式、或高动机逐条核验时效应消失，甚至因"过于顺滑"而提高警惕
**机制链**: 信息以低阻力方式被解析（熟悉字体、短句、高对比、易发音命名） → 解析的轻松感被误读为"我理解并认同这条信息"，作为内容质量的替代线索 → 在未逐条核验的情况下提高可信度与偏好判断
**剂量**: 弱 统一字体与对比度、去掉术语与被动句（不改变信息结构） ；中 把关键结论改写为短句 + 具体数字 + 熟悉的版式，并让论证顺序符合读者的既有预期 ；强 在浅加工位置上集中投放高流畅度主张（首屏、标题、CTA），把复杂条件移到二级页面 ；过载 把排版做到过度平滑（模板化、无来源、无细节、通篇四字口号） → 流畅性失去诊断价值，用户改以"太像广告"为启发式反向折价，同时真实性判断转向来源核验
**时间动态**: 起效 秒级（单次呈现即改变可信度初值） · 衰减 同一版式在重复曝光后不再产生流畅性增量，用户对该站点的"顺滑"脱敏 · 饱和 全站模板化后流畅性成为基线，不再提供区分度，反而抬高"看起来都一样"的同质化折价
**调节变量**: 个体 认知需求低、时间压力大、领域知识少的用户更依赖流畅性线索；高认知需求与高怀疑特质用户会主动检查来源，效应显著减弱 · 文化 高语境文化中格式与措辞的得体性本身承载可信度，流畅性经由"得体"起作用；低语境文化更依赖具体证据，流畅性权重较低 · 情境 低风险、低金额、快速决策时效应最大；高利害、可复核、需向他人解释的决策中反思性加工压过流畅性
**失效信号**: 同一主张换成难读字体后可信度评分不再变化（效应已脱敏）；用户评论开始提到"排版很漂亮但没说什么"；高流畅度页面的转化提升在高动机人群（比价、专业用户）中消失；投诉中出现"看着很专业，实际没有依据"的表述
**可测代理**: 同内容两版（流畅/不流畅字体或句式）的可信度评分差与转化差；文案可读性指标（句长、术语密度）与转化率的相关，控制信息量后；高/低动机分组的效应差；"来源核验"行为（点击引用、搜索品牌）在流畅版与对照版的差异
**交互**: × SD-04 权威偏误 → 权威线索让用户停止加工内容，流畅性让内容不必被加工，二者叠加构成 COMBO-06 的信任瀑布，三层独立路径使错误主张极难被单点证据推翻（COMBO-06）；× HB-05 框架效应 → 流畅表述本身就是一种框架，同一事实的顺滑版本被当作默认解释；× CA-02 认知负荷 → 负荷越高越依赖流畅性替代核验，这是效应在移动端与首屏最强的机制原因
**边界**: 不得用流畅化排版掩盖实质缺失（关键条件、风险、费用、限制必须同等显眼，否则构成误导性商业表述）；金融、医疗、法律披露文件不得以提升流畅性为由删除风险与条件表述；对低识字水平与认知障碍人群，流畅性会被误读为"已理解"，须配合理解校验而非仅优化观感

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Large

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
**Tier**: 核心
**Evidence**: B — 机制基础为预测编码与注意的朝向反应（Sokolov 1963；Friston 预测误差框架），"预期违反捕获注意"在注意研究中较为稳固。争议：①"模式中断"作为营销钩子的现场效应缺少受控实验，证据以平台 A/B 数据与从业者观察为主；②新奇性效应快速习惯化，第 2–3 次同型中断即失效，因此横断面 A/B 会系统性高估其长期价值；③"中断即有效"忽略方向：违反预期既可能引发好奇，也可能引发困惑与反感（信任违背类中断的反弹最强）；④与信息缺口的边界模糊，很多"中断有效"的案例实际由缺口或情绪唤起驱动
**Effect**: 大但极短半衰期：中断带来的注意提升集中在最初 1–3 秒，且对"可解释的新奇"最强、对"莫名其妙"为零甚至为负；同一受众重复暴露后效应快速衰减
**机制链**: 出现违反当前预期的刺激（画面、开场、措辞、格式） → 预测误差触发朝向反应与注意重置，加工资源被强制转向该刺激 → 在意识评估之前争取到一次停留，为后续信息争取被加工的机会
**剂量**: 弱 在熟悉版式中做一处可见的偏离（非标准配图、反常标题句式） ；中 首帧/首句直接进入动作中段或反常识主张，并在 3 秒内给出可解释的线索 ；强 视觉与语义双重违反预期，且与后续内容形成因果闭环（中断本身是内容的入口而非噪音） ；过载 每个单元都以更夸张的违反开场、且与内容无因果关联 → 用户把中断读作标题党，产生"预期违反免疫"，之后连真实的新信息也被跳过
**时间动态**: 起效 亚秒级（首帧出现即触发朝向反应） · 衰减 同型中断在同一受众第 2–3 次出现后基本失效，平台层面按周计衰减 · 饱和 品类整体采用同类钩子后，中断成为新基线，需要更强的违反才能获得同等注意，进入噪音螺旋
**调节变量**: 个体 新奇寻求（novelty seeking）高、注意控制弱的用户反应最强；高执行功能与明确目标的用户会跳过中断继续原任务 · 文化 高不确定性规避文化中过度违反预期引起不安而非好奇，中断需保留可解释性；低语境、快节奏内容市场中断容忍度更高 · 情境 注意力竞争激烈、单次成本低的场景（信息流、短视频）效应最大；用户处于目标导向任务、或中断与信任相关（支付、医疗）时效应反转为警觉
**失效信号**: 首帧钩子的 3 秒留存在第 2–3 次曝光后下降而完播率不变（用户学会跳过）；用户评论出现"标题党/被骗进来"集中出现；中断强度提升而停留时长不再增加（免疫已形成）；品牌搜索量在中断加码后下降
**可测代理**: 首 3 秒留存与首帧类型的分组差；同一钩子在第 1/2/3 次曝光的留存衰减曲线；"中断后 3 秒内跳出率"与后续完播的相关；标题—内容一致度评分与复访率的关系
**交互**: × PA-04 信息缺口 → 中断负责争取停留、缺口负责把停留转成消费，二者构成 COMBO-09 的前两级，缺一环则中断只制造跳出（COMBO-09）；× AD-01 变动比率强化 → 中断+缺口+不可预测的奖励质量构成 COMBO-13 的注意力捕获栈，三级串联使停止变成主动行为（COMBO-13）；× CA-03 预测编码 → 中断的强度本质是预测误差量级，误差过大转为困惑，这是"过载"反转的机制根源
**边界**: 不得以与内容无因果关联的中断骗取点击（标题党构成误导性表述，且平台侧通常有明确处罚）；新闻、健康、金融信息中的中断不得歪曲事实基线（违反预期的表述若暗示不实结论即为虚假信息）；不得对儿童内容使用惊吓式中断

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.87；Effect Size: Large

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
**Tier**: 常用
**Evidence**: B — Loewenstein 1994 的信息缺口理论为核心框架，好奇心作为" deprivation 状态"有实验支持（Kang et al. 2009 显示被激发的 curiosity 伴随奖赏回路激活与更好的记忆）；Zeigarnik 1927 的未完成效应提供相邻证据。争议：①Zeigarnik 效应本身复制不稳（原始研究小样本，后续元分析效应接近零，且受任务中断方式调节），把它当作"开放环必然被记住"是过度外推；②"缺口越大越好奇"与"缺口过大即放弃"之间存在倒 U 关系，拐点依赖先备知识与可解性，缺少可迁移数值；③现场"好奇心缺口提升点击"的多数证据来自平台 A/B，无法区分缺口与标题情绪唤起；④缺口被反复证明为可解但不兑现时，效应转为对该来源的普遍忽略
**Effect**: 中等偏大，仅在"用户对该领域已有兴趣 + 缺口具体可解 + 解路径明确"三者同时成立时有效；缺口过大（不可解）或过小（答案显然）时效应都趋零，且不兑现会累积为来源级失信
**机制链**: 揭示"存在某个你不知道但应当知道的信息"并留出空位 → 空位被体验为一种不适的 deprivation 状态，占用工作记忆并要求闭合 → 沿最省力的路径（继续观看、点击、读完）闭合缺口
**剂量**: 弱 在完整信息之后提出一个自然的延伸问题（不阻断信息交付） ；中 标题/开场明确"存在答案"并限定范围（"3 个原因，第 2 个最反直觉"），正文兑现 ；强 把缺口与用户自身处境绑定（"你的账号属于哪一类，决定了你能不能用这个功能"），并把答案放在需要一次主动动作之后 ；过载 连续堆叠不兑现的缺口（每段结尾都抛新问题且从不回答） → 缺口从驱动变为噪音，用户以"这类账号从来不告诉我答案"整体屏蔽该来源，反弹强于从未使用
**时间动态**: 起效 秒级（缺口被指认的瞬间即产生闭合需求） · 衰减 未闭合缺口在数分钟至数小时内自然消退，重复暴露同型缺口后反应强度下降 · 饱和 长期不兑现导致来源级免疫，此后该来源的任何缺口都不再产生点击
**调节变量**: 个体 好奇心特质（curiosity trait）与认知需求高的用户反应最强；低认知需求用户需要更强的相关性绑定才被拉动 · 文化 高不确定性规避文化中过大的缺口引起焦虑与回避，需更强的"可解"承诺；高语境文化更接受含蓄留白 · 情境 有先备知识、缺口语义具体、单次成本低时效应最大；用户已明确目标（找具体答案）时缺口只增加摩擦
**失效信号**: 点击率上升但落地页跳出率同步上升（缺口与内容不匹配）；同一来源后续内容的打开率持续下滑；评论中出现"又是标题党/到底说不说"；用户开始跳过该来源的固定开场结构
**可测代理**: 有缺口/无缺口标题的点击率差与落地页完成率差；缺口兑现时点（第几秒给出答案）与完读率的关系；同一账号连续 N 条的打开率衰减曲线；"缺口—答案一致度"人工评分与复访率的相关
**交互**: × PA-02 模式中断 → 中断争取到的停留只有靠缺口才能转成消费，构成 COMBO-09 的核心两级，中断强而缺口弱时停留立刻流失（COMBO-09）；× AD-10 好奇的情绪侧 → 缺口提供认知空位、情绪唤起提供驱动力，两者分离时可诊断问题出在哪一环；× COMBO-16 的分享动机 → 缺口让"我知道而你还不知道"具备社交货币价值，是把私密好奇转成传播的那一步（COMBO-16）；× AD-02 蔡加尼克 → 未完成结构被记住，但把它当作可靠记忆杠杆是过度外推
**边界**: 不得构造不兑现的缺口（clickbait 在多数平台属违规，且在广告法下可能构成误导）；健康、金融、安全信息中不得用缺口延迟关键风险信息（"看到最后才知道"式结构对风险披露不可接受）；不得对儿童使用无限缺口结构（与问题性使用相关）

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.89；Effect Size: Large

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
**Tier**: 情境
**Evidence**: C — **该机制存在明确的复制危机，本记录按最低等级标注。** 社会启动（behavioral priming）的旗舰研究未能复制：Doyen et al. 2012 在 PLOS ONE 报告对 Bargh et al. 1996 "老年人词汇→走得更慢" 的直接复制失败，并指出原效应可由实验者期望解释；Harris, Coburn, Rohrer & Pashler 2013 在 PLOS ONE 的多实验复制同样未获得该效应；Shanks et al. 2013 对"金钱启动"的元分析发现校正发表偏倚后效应接近零；Camerer et al. 2018 的多实验室预注册复制（RPP）使多个社会启动效应量大幅下调。相对稳健的只有**语义/词汇启动**（启动词加快相关词识别，短 SOA 下可复制，但量级小、持续数百毫秒），以及部分**评价性启动**。争议结论：v1 把"看温暖概念→觉得别人更友好""看奢侈品→出更高价"写成可靠应用，属于把失败复制的研究当作确证，本记录不延续该写法；可用的只有"词汇层面的短时通达性提升"，不是"改变判断与行为"
**Effect**: 语义启动为小效应（反应时缩短约 10–30 毫秒级，仅在同模态、短间隔内成立）；行为/概念启动的效应在多实验室复制后接近零，不应作为设计依据。可迁移到产品的只有"用词一致性影响下一词的解析速度"，而非"氛围改变决策"
**机制链**: 先呈现一个语义相关的词或概念（"医生""安全""限时"） → 相关概念在记忆中短时激活，通达性提高（语义网络预激活） → 随后出现的相关词被更快解析，或更易被选为对当前刺激的解释
**剂量**: 弱 在同一屏内保持术语与措辞一致（按钮"继续"与标题"下一步"用同一动词族） ；中 在需要快速解析的位置使用与用户既有词汇一致的表述（用用户自己的行业词而非内部黑话） ；强 把关键动作的用词与紧邻的上下文语义对齐（表单旁放"安全/加密"措辞，动作按钮用"确认保存"而非"提交"），并保持短间隔、同模态 ；过载 堆叠多层"氛围式"启动（先放成功故事、再放奢侈品图、再放权威照）期望改变判断 → 启动链本身没有可复制的行为效应，用户只感到版面杂乱、认知负荷上升，转化不升反降，同时把预算消耗在无效设计上
**时间动态**: 起效 毫秒级至秒级（语义启动的窗口以百毫秒计，跨屏基本消失） · 衰减 启动效应在数秒内衰减，跨会话不残留；任何要求"上次看到的画面影响这次决策"的设计都没有证据支持 · 饱和 由于效应本身接近噪声，不存在可累积的饱和路径；反复暴露只增加视觉疲劳
**调节变量**: 个体 语义启动的个体差异极大且不稳定，无法据此分层；阅读速度与词汇量影响解析加速的幅度 · 文化 词汇联想网络本身是文化依赖的（同一词在不同语言中激活的语义邻域不同），跨语言迁移无证据 · 情境 仅在短间隔、同模态、低负荷的解析任务中可测得；跨屏、跨会话、高动机决策中效应不可测，任何现场"启动式"氛围设计都属未经验证的推断
**失效信号**: 更换"启动"素材后目标指标无变化（最常见的实情）；只有把素材与文案语义对齐时才见微小提升，说明起作用的是用词一致性而非氛围；同一启动设计的效应在第二次 A/B 中消失；团队用"氛围感"解释结果而无法给出机制检验
**可测代理**: 同内容两版措辞一致性（术语统一/混用）的解析时间与完成率差；按钮动词与上下文语义一致/不一致的分组转化差；若要做启动检验，须做预注册的多实验室式复制（同设计至少 3 个独立样本）并报告效应量与置信区间，单次 A/B 不足以支持启动结论
**交互**: × PA-01 加工流畅性 → 用词一致通过降低解析成本提升流畅性，这是启动类设计唯一可靠的落地路径，起作用的是流畅性而非启动本身；× CA-02 认知负荷 → 负荷越高，词汇一致性的收益越大，因为解析资源更稀缺；× HB-01 锚定 → 常被与启动混为一谈，锚定有多实验室支持而启动没有，二者不可互换论证
**边界**: 不得以"潜意识影响"为卖点作宣传（既无证据支撑，也可能构成虚假宣传）；不得把启动话术用于影响医疗、金融、法律决策中的实质判断；本记录明确不提供"如何用潜意识线索操纵选择"的操作序列——该序列建立在未被复制的效应上，实施它既无效又可能带来合规与声誉风险

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.82；Effect Size: Medium-Large

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
**Tier**: 核心
**Evidence**: B — 对比效应在知觉与判断中有稳固基础（Sherif 与 Helson 的适应水平理论；Simonson & Tversky 1992 的吸引力/折中效应为相邻证据）；价格情境中"先高后低"改变支付意愿的现场证据较充分（锚定与对比在定价页的 A/B 中稳定可测）。争议：①对比效应与锚定效应在文献与实践中常被混用，二者机制不同（知觉参照 vs 数值锚定），归因错误会导致设计错误；②对比方向不稳：同一低价比"更差选项"时显得贵还是便宜，取决于用户是否把两者归为同一比较集；③"先展示糟糕选项"若被识别为刻意安排的诱饵，会产生反感的反弹（诱饵效应在可辨识时减弱）；④效果依赖比较集的可信度，虚假对照物一旦被识破，全部价格信息的可信度受损
**Effect**: 大，仅在两个选项被用户归入同一比较集、且比较维度单一可辨时成立；跨类别、多维差异或比较集被判定为人为构造时，效应显著减弱甚至反转
**机制链**: 目标项被置于一个参照项之旁（更差或更好的相邻刺激） → 知觉与判断以相邻刺激为适应水平，目标项在关键维度上的相对位置被放大 → 在未重新建立独立参照的情况下接受被放大的相对价值判断
**剂量**: 弱 在同类目内按维度排序展示，让目标项自然处于可辨位置（不插入人为诱饵） ；中 提供真实的高价对照项与真实的低配对照项，目标项位于其间且优势维度明确 ；强 三段式比较结构（明显更差/明显更贵的真实选项夹住目标项），并在同一维度上把优势写成可核验的差异 ；过载 插入明显不合理的诱饵或虚构高价对照 → 用户识别出比较集是人造的，对整页价格信息重新定价为不可信，转化下降且退款/议价行为上升
**时间动态**: 起效 秒级（同一屏内的相邻呈现立即改变判断） · 衰减 离开该比较集后效应在数分钟内消退；重复访问同一页面对比效果递减 · 饱和 用户把该页的比较结构记住后，对照项不再起作用（"那个贵的选项是摆给我看的"）
**调节变量**: 个体 领域知识少、无外部参照的用户受对比影响最大；有独立比价习惯或已持有心理价格的用户几乎不受影响 · 文化 集体主义与关系文化中比较更多以"他人所处位置"为参照，价格对比效应被社会比较稀释；个人主义市场对绝对价格对比更敏感 · 情境 比较维度单一、金额中等、决策快速时效应最大；高金额、多维权衡、需向他人解释时用户会重建独立参照
**失效信号**: 移除诱饵项后目标项转化率无变化（诱饵本就没起作用）；用户在评论中指出"那个贵的选项没必要存在"；同一页面的价格异议与议价请求上升；对照项的点击率长期接近零（用户已识别为摆设）
**可测代理**: 有/无对照项的目标项转化差与选择份额变化；三段式结构中各段的点击分布（诱饵点击率过低即为可辨识信号）；同一目标项在不同比较集下的支付意愿差；价格类客服工单中"对比不实"的提及率
**交互**: × HB-01 锚定 → 对比改变知觉参照、锚定改变数值参照，两者在定价页叠加时提升幅度最大，但混淆归因会导致错误优化；× PE-01 价格相对性 → 对比是相对性的知觉侧实现，二者在定价结构中同源；× SD-15 社会比较 → 价格对比之外再叠他人选择对比，会让"贵/便宜"与"该不该"同时被改写
**边界**: 不得虚构对照项或伪造"原价/划线价"（《价格法》《禁止价格欺诈行为的规定》对虚构原价有明确禁止）；医疗、保险、信贷产品的对比结构不得通过不对称呈现隐藏真实成本（年化、总还款额须同维度可比）；不得对认知负荷高的用户（老年人、非母语者）使用高密度对比结构

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Large

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
**Tier**: 常用
**Evidence**: B — 首因与近因效应在自由回忆任务中高度可复现（Murdock 1962 的系列位置曲线；Glanzer & Cunitz 1966 显示近因依赖短时存储、首因依赖复述）；"中间项目被记住得更差"是记忆研究中最稳固的现象之一。争议：①在**再认**（有线索）而非自由回忆时曲线显著变平，多数真实界面任务是再认而非回忆，因此界面设计的可迁移性被高估；②"放第一或最后就能被选中"缺少现场实验，位置效应与视觉显著性、默认值、文案强度高度混淆；③列表长度调节巨大：短列表（≤5 项）几乎无中段劣势，长列表的中段损失才明显；④近因效应在信息持续可回看（可滚动、可搜索）时大幅削弱
**Effect**: 中等偏大，仅在自由回忆或强序列呈现（无法回看、无搜索、无外部记录）时成立；可回看、可搜索、可对照的界面上效应显著减弱，此时位置带来的收益多来自视觉显著性而非记忆
**机制链**: 信息以序列方式呈现 → 序列首端获得更多复述进入长时记忆、末端仍留在短时存储，中段两项优势皆无 → 回忆与选择集中于首末，中段信息被系统性遗漏
**剂量**: 弱 把最重要的单项放在序列首端（不改变其余结构） ；中 首末各放一个关键项，并把中段长度压缩到 5–7 项以内 ；强 首末双点设计 + 中段分组分块 + 末尾紧接行动按钮（首因给理由、近因给动作） ；过载 把全部关键信息都塞到首末两端（开场堆三个卖点、结尾堆五个 CTA） → 首末内部相互竞争，位置优势被摊薄，用户实际记住的仍是零，且认知负荷上升导致整体放弃
**时间动态**: 起效 即时（单次呈现后立即测量即出现曲线） · 衰减 近因部分在数十秒至数分钟内衰减（离开短时存储），首因部分随复述衰减较慢但也在小时级消退 · 饱和 反复暴露同一序列后用户形成结构记忆，位置效应转为"我知道第几项是什么"，收益消失
**调节变量**: 个体 工作记忆容量小、无外部记录习惯的用户中段损失最大；有笔记或搜索习惯的用户几乎不受位置影响 · 文化 受教育年限与读写习惯影响序列加工策略（首末优先 vs 全序列扫描），差异存在但方向不稳 · 情境 强序列、不可回看、单次曝光（视频、电话、口播、一次性邮件）时效应最大；可滚动、可搜索、可对照的界面中效应被显著削弱
**失效信号**: 用户在后续任务中选择了中段项目（说明存在外部检索而非记忆）；同一内容改为可搜索列表后首末位置优势消失；首末堆叠多个 CTA 后总点击率不升反降；召回测试中中段项目的再认率与首末无差异（任务本就是再认）
**可测代理**: 同一列表的首/中/末位置的点击份额与再认正确率（区分再认与自由回忆两种测法）；列表长度 5/10/20 项时中段点击份额的变化；可回看 vs 不可回看两种呈现的首末优势差；首末 CTA 数量与总点击率的关系曲线
**交互**: × CA-04 注意力上限 → 序列位置效应与注意资源共同决定实际被加工的项数，中段既是记忆盲区也是注意盲区；× PE-08 选择过载 → 长列表同时放大中段损失与过载，缩短列表对两者的改善同向；× HB-01 锚定 → 首项既是记忆优势位也是锚定位置，把锚与首因叠加时首项的影响远超单纯位置效应
**边界**: 不得利用位置效应隐藏不利信息（费用、风险、退订入口放在中段构成界面操纵，受 DSA 第 25 条与各地暗黑模式监管关注）；法律与金融披露不得依赖位置优势传达关键条款，须显式重复与单独确认；不得以位置设计替代信息本身的重要性排序

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.83；Effect Size: Medium-Large

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
