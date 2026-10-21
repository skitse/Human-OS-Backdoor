# Trust Architecture — Model Details

> **Domain**: Trust formation · credibility design · reassurance systems · trust repair
> **Scope**: neural basis, staged trust formation, digital trust signals, trust recovery patterns
> **Use when**: the task depends on credibility, reassurance, consent, commitment, or risk reduction more than pure motivation or urgency

---

## Why Trust Needs Its Own Model

Many behavioral levers increase action in the short term. Trust determines whether those gains compound or reverse.

Use this file when the core design problem sounds like any of these:

- "Users hesitate because they are not sure this is real"
- "People do not trust the claim / product / flow / seller"
- "This is a high-ticket, high-risk, health, finance, B2B, or consent-sensitive experience"
- "We need to repair trust after friction, mistakes, bad messaging, or overused pressure tactics"

Trust is not one thing. It is the combined perception that:

1. the actor is competent
2. the actor is honest
3. the actor is aligned with the user's interests
4. the system behaves predictably enough to be low-risk

---

## TR-01 · Trust Chain 信任链
**Tier**: 核心
**Evidence**: B — 信任的多成分结构有较强支持：Mayer, Davis & Schoorman 1995 的 ability/benevolence/integrity 三成分模型被广泛引用与部分验证，McKnight et al. 1998 区分了 dispositional、制度性与人际信任，Rousseau et al. 1998 的跨学科综述支持"信任随经验更新"。**但**本记录把成分串成"信号→评估→风险估计→意愿→验证"的顺序链，这是工程化重构：没有任何研究验证过该序列的因果顺序与单向性，实际加工是并行且迭代的；因此成分划分按 B 处理，链的顺序部分按 C 处理
**Effect**: 中等偏大且不对称：链上任一环节失败会使后续环节的评估一并作废（不可补偿），而任一环节成功不能替代其他环节；在高利害决策中链条更长、验证环节权重更高
**机制链**: 一个可被感知的信号（身份、能力证据、立场、一致性）进入评估 → 用户把它折算成"这人或系统会不会伤害我"的风险估计并更新既有先验 → 风险估计低于阈值时产生前进意愿，随后的实际体验决定信任是兑现还是撤销
**剂量**: 弱 在每个接触点提供可核对的身份与下一步（让人能判断这是什么、谁在做） ；中 按用户自然检查风险的顺序排列证据：先可读性、再低成本可信度、再具体能力证明、再立场与可逆性 ；强 让承诺可被事后验证（说过的变化真的发生、写下的条款真的执行），并在失败时给出具体归因与补救 ；过载 把信任信号堆到无法核查的密度（满屏徽章、奖项、用户数、认证） → 用户无法区分哪个信号与自己的风险相关，反而启动防御性怀疑，信任评估从"证据不足"转为"过度包装"，整体信任下降
**时间动态**: 起效 首屏秒级形成初步判断（可读性与身份） · 衰减 未兑现的承诺在数周内削弱信任，单次背信可在一次事件内清零 · 饱和 长期一致后信任进入"默认不检查"状态，此时一次背信造成的落差最大（因为已无人复核）
**调节变量**: 个体 信任倾向（propensity to trust）高者初始门槛低但落差后下调更陡，专业买家更依赖可验证证据而非信号；文化 高权力距离与集体主义市场更依赖机构身份与关系背书，低语境市场更依赖条款、SLA 与可核验记录；情境 高金额、不可逆、涉及隐私或健康时链条更长且验证权重最高，低金额可逆场景中启发式即足够
**失效信号**: 用户在关键页反复回看条款或对比第三方评价（说明链条未闭合）；客服咨询集中在"你们到底是谁""会不会扣钱"类基础问题；转化在加入更多信任徽章后下降；承诺兑现类投诉与退款理由中出现具体落差描述；老用户开始要求书面确认
**可测代理**: 关键页的条款展开率与停留时间；身份与资质类问题的客服占比；承诺兑现率（说过的时限、价格、功能变更的实际达成）；首购与复购的信任相关投诉率；NPS 中信任维度的分项
**交互**: × TR-02 可读性 → 不可读的界面让链条在第一步就断，后续所有证据都不被处理；× TR-03 能力信号 → 能力证据降低"能不能做到"的不确定性，但与立场信号不可互替，一方缺失会使另一方被怀疑；× PE-01 价格相对性 → 价格呈现方式本身是信任信号，虚构锚点会让整条链在立场环节失败
**边界**: 不得用信任设计降低用户对真实风险的核查（例如用徽章与好评掩盖不利条款、把关键条款折叠进"已阅读"）；高利害场景（医疗、金融、法律、同意与扣费）中信任设计必须服务于知情而非说服，把"降低疑虑"当作目标会构成误导；不得在未取得资质时使用机构与认证类信号，中国《广告法》第 28 条与美国 FTC Act 第 5 条均将虚假资质列为虚假广告或欺骗性行为

## Trust Chain

The practical chain is:

```text
Signal noticed
-> credibility assessed
-> risk estimate updated
-> willingness to proceed
-> trust confirmed or broken by lived experience
```

Short version:

- competence signals reduce "Can they do this?"
- integrity signals reduce "Are they hiding something?"
- alignment signals reduce "Will this hurt me while helping them?"
- consistency signals reduce "Will this suddenly change later?"

---

## Neural / Cognitive Basis

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.84；Effect Size: Medium-Large in trust-sensitive contexts

Trust decisions blend fast heuristics and slower verification:

- **Processing fluency**: easy-to-read, coherent, orderly interfaces feel safer and more truthful
- **authority transfer**: trusted institutions, credentials, and known brands lend borrowed credibility
- **prediction consistency**: repeated, expectation-matching experiences lower perceived risk
- **threat monitoring**: ambiguity, inconsistency, hidden terms, and suspicious pressure cues activate defensive scrutiny

Design implication:

- initial trust often starts with heuristic cues
- durable trust only survives if the lived experience confirms those cues

---

## The 7 Stages of Trust Formation

## TR-02 · Legibility 可读性
**Tier**: 核心
**Evidence**: B — 加工流畅性与真实性判断的关联有多项研究（Reber & Schwarz 1999；Alter & Oppenheimer 2009 综述），元分析（Dechêne et al. 2010）报告中等效应；**但**存在复制与效应量争议：Meyer et al. 2015 的多实验室复制只支持较小效应，且部分流畅性操作（字体、颜色对比）无法稳定复现"感觉更真"的结果；把"排版清晰等于更可信"当成设计定律会高估收益。可读性降低认知负荷这一层证据较强，可信度外溢这一层较弱
**Effect**: 中等且分两段：可读性对"能不能开始处理"的影响大且稳定；对"是否相信"的外溢效应小且依赖情境，在用户已有动机核查时基本消失
**机制链**: 界面与文案的结构、术语与视觉层级决定信息能否被快速解析 → 解析成功时产生加工流畅感，失败时触发额外负荷与不确定 → 流畅时继续评估并倾向给出更高可信度，不流畅时推迟、放弃或转向外部求证
**剂量**: 弱 用用户的语言重写标题与按钮，去掉内部术语与缩写 ；中 让"这是什么、谁在做、下一步是什么、代价是什么"在一屏内可见，并把关键限制放在同一视觉层级 ；强 把复杂承诺结构化：条件、时限、例外、退出方式各占一行，并附可核对的示例与真实截图 ；过载 为"更清楚"而无限披露（把所有条款、所有指标、所有免责声明平铺首屏） → 信息量超过可解析阈值，用户回到"太长不看"并直接依赖第一印象，可读性投入反转为信任损失
**时间动态**: 起效 首屏秒级（首次注视即可判断是否可解析） · 衰减 不随重复衰减，但一旦用户学会跳过该区域（banner blindness 式适应）即失效 · 饱和 长期清晰化后边际收益递减到零，此时继续简化不再提升信任，只会削减必要信息
**调节变量**: 个体 领域专长度高者容忍术语、低者依赖平实语言，读写能力与语言熟练度低者从结构化改写中获益最大；文化 高语境文化中含蓄表达被接受但对"说不清楚"更敏感，低语境文化中直白的条件与价格更被信任；情境 移动端小屏、弱网、单手操作下可读性权重最高，桌面端深度阅读场景中结构化与完整性更重要
**失效信号**: 用户在关键段落反复回看或放大（说明未解析）；客服问题集中在"这到底是什么意思"；条款展开率极低但退款与投诉中出现"我不知道会这样"；A/B 简化后停留时间下降但理解度抽测分数不变（说明原文本未被读）；跳出集中在首屏第一段
**可测代理**: 关键页的首次有效滚动深度与段落回看次数；客服问题中"含义类"占比；三题理解度抽测（原文与改写版随机分流）；条款展开率与后续争议率的相关
**交互**: × TR-03 能力信号 → 能力证据只有在可被解析时才被计入，不可读的证据等于不存在（COMBO-06 信任级联：权威 × 社会证明 × 加工流畅性三层叠加时，信任在三个独立通道上同时上升，首次转化提升最明显，但三层中任何一层被证伪会同时拉低另外两层）；× TR-06 信任修复 → 修复声明的可读性决定它被读成"解释"还是"公关话术"；× PE-08 选择过载 → 清晰化若只做视觉不做结构，会同时增加选项可见度与决策负荷
**边界**: 不得以"简化"为名删减法定披露、风险提示、扣费条件与退出方式——中国《消费者权益保护法实施条例》要求以显著方式提示与消费者有重大利害关系的内容，《电子商务法》第 18 条要求搜索结果与推荐可解释，欧盟 DSA 第 25 条禁止用界面设计实质性扭曲或损害消费者的自主决定；不得用低对比度、灰字、折叠等方式降低不利信息的可读性（这正是监管定义下的暗黑模式）；不得把可读性当作替代实质证据的手段

### 1. Legibility

**Question in the user's head**: What is this and what is happening?

If the product, page, or message is hard to parse, trust cannot even begin.

**Signals**:
- clear headline
- obvious actor identity
- obvious next step
- readable layout

**Failure mode**:
- users cannot tell if the offer is legitimate, promotional, scammy, or unfinished

### 2. Basic Credibility

**Question**: Is this real?

Users look for low-cost legitimacy checks.

**Signals**:
- company / person identity
- real contact paths
- real domain and brand consistency
- policy visibility
- external references

**Failure mode**:
- vague authorship, anonymous claims, broken pages, missing policies, thin copy

## TR-03 · Competence Signaling 能力信号
**Tier**: 核心
**Evidence**: B — 信号理论（Spence 1973）与来源可信度研究支持"可验证的能力线索降低不确定性"，专业度线索对说服的影响在元分析中有中等效应（Pornpitakpan 2004）。**但**具体信号（客户 logo、认证徽章、案例数）在真实转化上的效应多为单一 A/B 或行业报告，属 C；且存在反噬证据：能力信号与实际体验不一致时，落差造成的信任损失大于从未展示（期望确认理论的负面不对称）。因此机制层按 B、具体信号层按 C
**Effect**: 中等偏大，仅在信号与用户实际风险相关且可验证时成立：具体的执行细节（怎么做的、失败过什么、时限多久）比抽象的资质堆叠更有效；与风险无关的资质几乎无效
**机制链**: 用户面对"他们能不能做到"的不确定性 → 寻找能区分真能力与空承诺的线索（具体细节、可核验的既往结果、可追责的承诺） → 线索被判定为可信后风险估计下降、前进意愿上升；若线索无法核验则被当作营销噪音
**剂量**: 弱 展示可核验的基本事实（谁在做、做过什么、联系方式、真实域名） ；中 给出与用户任务同类的具体执行证据（同类案例的输入、动作与结果，时限，失败与修正） ；强 提供可追责的能力承诺：明确交付物、时限、验收标准、不达标时的补救，并允许用户抽查其中一项 ；过载 用无法核验的资质堆叠代替具体证据（满屏奖项、认证、客户 logo、模糊的"服务过 500 强"） → 用户无法判断哪一条与自己的风险相关，转而认为是在用包装替代能力，信任评估下降且更难挽回
**时间动态**: 起效 首次接触秒级到分钟级（logo 与案例的扫描速度快于文字） · 衰减 同类信号在重复接触 3–5 次后失去区分度（每个竞品都这么说） · 饱和 能力信号饱和后只能靠可验证的履约记录维持，此时任何新的资质展示都不再提升信任
**调节变量**: 个体 专业买家更看重可核验的执行细节、对资质堆叠免疫，非专业买家更依赖品牌与认证等启发式线索；文化 高不确定性规避市场对认证与资质权重更高，高语境市场更看重推荐关系与口碑背书；情境 高金额、高复杂度、首次合作时能力信号权重最高，低金额重复购买时几乎不再被检查
**失效信号**: 用户在案例页停留后仍去第三方搜索（说明未采信）；转化在增加资质展示后不变或下降；成交后出现"和你们说的不一样"类投诉；销售与客服被反复要求"给个具体例子"；退款理由中出现交付物与承诺不符
**可测代理**: 案例页与资质页的到达率与停留时间；"要求具体案例或样例"的咨询占比；履约指标（承诺时限达成率、验收一次通过率）；能力相关投诉率；资质展示增减的 A/B 转化差
**交互**: × TR-02 可读性 → 不可解析的能力证据不被计入，二者必须同时满足（COMBO-06 信任级联中的权威层即本记录，它与社会证明、加工流畅性叠加时首次转化提升最明显，但一次资质造假会让另外两层同时失效）；× TR-04 立场信号 → 只有能力没有立场会被读成"很能干但会宰我"，能力信号反而放大威胁感；× TR-05 可预测性 → 能力需要靠一致性兑现，单次惊艳不能替代稳定交付
**边界**: 不得展示未实际服务过的客户、未取得的认证、未发生的案例——中国《广告法》第 28 条、《反不正当竞争法》第 8 条与美国 FTC Act 第 5 条均将虚构业绩与资质列为虚假宣传或欺骗性行为，欧盟《不公平商业行为指令》附件一第 1、2 条为黑名单；不得用能力信号掩盖已知的能力缺口（例如把"做不到"包装成"定制化"）；医疗、法律、金融等有执业资质要求的领域不得使用暗示资质的能力信号

### 3. Competence

**Question**: Can they actually deliver?

Users want evidence of capability, not just existence.

**Signals**:
- case studies
- product detail
- expertise markers
- operational specifics
- truthful limitation disclosure

**Failure mode**:
- overclaiming, generic promises, no specifics, no proof of execution

## TR-04 · Alignment Signaling 立场信号
**Tier**: 常用
**Evidence**: B — "公平与立场影响接受度"有实验基础：Kahneman, Knetsch & Thaler 1986 的双重权利（dual entitlement）显示人们按意图与参照交易判断公平，并愿为惩罚不公平付出成本（Fehr & Gächter 2000 的利他惩罚实验）；**但**"透明定价、可退出、解释推荐会提高信任"这一组具体设计主张的证据多为单项研究或行业 A/B，且存在方向反转的观察：主动披露不利信息在低信任品类中有时降低转化而非提高信任。机制层按 B、具体设计层按 C
**Effect**: 中等且方向可逆：在用户已感知到"对方可能利用我"的场景中，立场信号显著降低防御性核查并提高转化；在用户尚未产生怀疑时，过度强调"我们站在你这边"会引发反向怀疑（你为什么需要说明这个）
**机制链**: 用户在评估"对方会不会为自身利益牺牲我" → 观察默认值、退出成本、定价透明度与解释性文案所透露的意图 → 判定为对齐时降低防御与核查，判定为榨取时提高警惕或直接退出
**剂量**: 弱 让退出与取消的路径和进入一样容易找到，不设挽留墙 ；中 把对自己不利的信息主动放在决策点上（真实价格构成、适用与不适用、可能产生的额外费用），并解释默认值的理由 ；强 在结构上绑定利益：可验证的退款与不达标补救、可携带的数据导出、用户可关闭的自动化决策，并公开这些机制的实测达成率 ；过载 把立场信号做成表演（过度自证、反复声明"我们透明"、把不利信息淹没在更多披露里） → 用户把"需要不断证明自己无辜"读成有罪推定，信任不升反降，真实的对齐举措一并被怀疑
**时间动态**: 起效 分钟级（看到退出路径与真实价格构成即更新判断） · 衰减 单次表态在数天内失去作用，只有结构性安排（默认值、退出成本）持续生效 · 饱和 长期一致后立场信号进入背景，此时新增表态不再提升信任，一次被感知的榨取即可清零
**调节变量**: 个体 高公平敏感度与高隐私关注者对立场信号反应最强，价格敏感型用户更看重可退出而非表态；文化 高不确定性规避与高集体主义市场更看重"是否会被占便宜"的公共证据，低语境市场更看重合同条款与可执行救济；情境 订阅与自动续费、数据采集、算法推荐等高感知风险场景中权重最高，一次性小额交易中权重很低
**失效信号**: 退出路径的点击量高但完成率低（说明存在摩擦）；用户在取消流程中反复截图或投诉；"隐藏费用""套路"类评论集中在具体环节；透明度声明增加后转化不变而条款展开率上升（用户开始核查）；留存靠退出摩擦而非价值维持（取消挽留接受率异常高）
**可测代理**: 进入与退出路径的步数与耗时比；取消流程完成率与中途放弃率；额外费用相关投诉率；数据导出使用率；条款与定价构成展开率；挽留优惠接受率
**交互**: × TR-03 能力信号 → 有能力无立场被读成"会宰我"，立场信号必须与能力同时在场；× PE-06 支付痛苦 → 降低支付摩擦若不同时保证可退出，会被读成"方便你扣我钱"，立场信号缺失使支付便利反成负资产；× TR-06 信任修复 → 立场在违背后才被检验，此时结构性的可退出比任何道歉都有效
**边界**: 不得用立场信号为高退出摩擦辩护（把"可随时取消"写在页面上，实际取消需要电话与挽留流程）——中国《消费者权益保护法实施条例》第 10 条要求自动续费在扣费前显著提示、第 17 条禁止以格式条款不合理限制消费者权利；美国 FTC Act 第 5 条下取消摩擦已被执法（FTC 诉 Amazon 案 2025 年 9 月 25 日以 25 亿美元和解即以此为核心指控，尽管第八巡回法院 2025 年 7 月 8 日撤销了 2024 年负选项规则，FTC 仍依 ROSCA 与 FTC Act 第 5 条继续执法）；欧盟 DSA 第 25 条与 UCPD 附件一第 22、23 条禁止虚假的"可随时退出"声明；不得在医疗、金融、法律场景用立场话术替代风险披露

### 4. Alignment

**Question**: Are they on my side?

This is where users decide whether the system feels extractive or fair.

**Signals**:
- honest tradeoffs
- transparent pricing and consent
- user-benefit framing
- reversible decisions
- non-coercive defaults

**Failure mode**:
- hidden fees, manipulative defaults, aggressive urgency, one-sided framing

## TR-05 · Predictability 可预测性
**Tier**: 常用
**Evidence**: B — 期望确认理论（Oliver 1980）与"一致性降低感知风险"的方向有多项支持，程序公平研究（Thibaut & Walker 1975；Colquitt et al. 2001 元分析）显示一致且可解释的程序显著提高接受度；**但**"稳定规则提高信任"在产品情境中的证据多为相关研究，且存在边界：过度可预测会降低注意与惊喜价值（与可变奖赏相冲突），而用户对"可预测的坏"（稳定地差）并不因此更信任。因此按 B 但需注明双向边界
**Effect**: 中等，主要在降低"未来风险"的估计上有效；对提升"当前好感"几乎无效。可预测性对留存的作用大于对转化的作用
**机制链**: 用户观察到规则、时限与行为在多次交互中保持一致 → 形成"下次也大致如此"的预期，未来状态的不确定性下降 → 风险折价降低、承诺意愿与容忍度上升；一旦发生未解释的偏离，预期被打破、容忍度骤降
**剂量**: 弱 把规则、时限、价格与变更流程写清楚并保持前后一致 ；中 在流程中给出可核对的状态与里程碑（现在在哪一步、下一步何时发生、失败会怎样） ；强 让变更本身可预测：提前通知、给出过渡期、提供旧条款的保留选项，并公开历史变更记录 ；过载 为"稳定"而冻结一切（永不更新、永不调价、拒绝任何个性化） → 产品与用户实际需求脱节，用户把稳定读成停滞，且当不得不变更时因缺乏预期管理而冲击更大
**时间动态**: 起效 首个完整周期（天到周）内形成初步预期 · 衰减 预期在 1–3 次未解释的偏离后瓦解，即使偏离对用户有利（例如突然送东西）也会降低可预测感 · 饱和 长期稳定后用户不再检查，此时偏离的冲击最大，需要更强的解释与补救
**调节变量**: 个体 高不确定性规避与高尽责性用户对一致性权重最高，偏好探索的用户对过度稳定反应负面；文化 高不确定性规避文化中规则稳定性权重极高，低不确定性规避文化中灵活调整被容忍甚至被期待；情境 涉及金钱、健康、法律与工作流程时权重最高，娱乐与内容消费中可预测性权重低甚至反向
**失效信号**: 用户在每次扣费或交付前反复确认（说明预期未建立）；"和上次不一样"类投诉集中在规则与时限；变更通知后的流失集中在老用户；状态页与进度查询的访问频率异常高；SLA 或时限的实际达成率波动大但无人解释
**可测代理**: 规则、时限、价格的实际一致性（承诺与实际达成率）；变更通知提前量与变更后 30 天流失率；进度与状态查询频率；"与预期不符"类工单占比；老用户与新用户在变更事件后的留存差
**交互**: × TR-06 信任修复 → 违背后若不能重建可预测性（具体预防机制与时限），道歉无法恢复信任；× AE-06 回报密度 → 过度可预测与可变奖赏直接冲突，二者需分层：规则与交付可预测、内容与奖励可变化；× PE-13 动态定价接受度 → 价格可预测性是动态定价被接受的前提，缺乏规则透明时浮动即被读成掠夺
**边界**: 不得把"可预测"做成不可更改的锁定（用稳定规则绑定用户、提高退出成本），这在中国构成不合理限制消费者权利的格式条款（《消费者权益保护法实施条例》第 17 条），在欧盟落入 UCPD 附件一第 24 条与 DSA 第 25 条；不得用"稳定"掩盖已知缺陷（例如维持一个已知有害的默认值以避免用户注意）；金融与订阅类产品的价格与费率变更须依约与依法提前通知，不得以"一贯如此"为由拒绝变更披露

### 5. Predictability

**Question**: Will this behave consistently if I proceed?

Predictability turns a risky unknown into a manageable system.

**Signals**:
- stable rules
- clear timelines
- explained process
- status updates
- no surprise changes

**Failure mode**:
- moving deadlines, inconsistent policies, changing offers, silent failures

### 6. Earned Confidence

**Question**: Has my experience validated the promise?

Trust compounds only after the promise survives contact with reality.

**Signals**:
- fast first success
- expectation-matching onboarding
- clear fulfillment
- support responsiveness
- delivered value without bait-and-switch

**Failure mode**:
- first-session disappointment, mismatch between promise and product, hidden work after commitment

## TR-06 · Trust Repair 信任修复
**Tier**: 核心
**Evidence**: B — 修复策略有实验支持但结论是条件性的：Kim, Ferrin, Cooper & Dirks 2004 显示，对**能力型**违规，道歉（含责任承担）比否认更有效；对**诚信型**违规，道歉无效、否认甚至略优，因为道歉等于确认了对方最担心的动机问题；后续研究（如 Frontiers in Psychology 2022 关于口头与书面道歉的实验）进一步显示修复效果还受渠道与违规类型交互影响。**修复是不对称的**：负面信息在信任判断中的权重远大于正面信息（Slovic 1993 的不对称原则；Rothbart & Park 1986），一次违规造成的下降远大于一次好行为的上升，且修复需要连续多次兑现才部分恢复。Lewicki & Brinsfield 2017 的综述指出多数修复策略的平均效应小且短暂；补偿（实质性补救）在多数研究中比纯口头道歉更有效，但不能替代对诚信问题的结构性改变。整体按 B，且必须标注"道歉不是通用解"
**Effect**: 小到中等且高度不对称：修复能把信任恢复到违规前的部分水平而非全部；诚信型违规的修复上限显著低于能力型违规；修复速度取决于违规是否可被归因为"一次性"而非"本性"
**机制链**: 违规被用户察觉并触发对动机或能力的重新推断 → 用户按违规类型（能力或诚信）选择性地采信解释、道歉或补偿，并检查是否有结构性改变 → 归因为一次性且看到具体预防措施时信任部分恢复，归因为本性或发现解释不实时信任继续下降
**剂量**: 弱 在用户发现之前主动说明发生了什么、影响了谁、正在做什么（不等待曝光） ；中 按违规类型匹配动作：能力型给具体原因、修正与时限；诚信型给结构性改变（改默认值、改条款、可核查的第三方审计），而不是更多表态 ；强 补偿、结构性改变与可验证的后续记录三件套，并允许用户复核（公开事件报告、接受抽查、给出个人化的补救路径） ；过载 用过度道歉与过量补偿替代结构性改变（连发致歉信、无条件退款但不改机制） → 用户把重复致歉读成"还会再犯"，补偿被视为封口，信任在短期回升后跌回更低位，且此后再无解释空间
**时间动态**: 起效 违规被发现后的最初 24–72 小时决定修复上限（沉默与拖延本身构成第二次违规） · 衰减 修复带来的信任回升在 2–4 周内回落，除非有可验证的兑现；未兑现的承诺衰减更快 · 饱和 同一类违规重复发生后，任何修复动作的边际效果趋近于零，用户转入"不再听解释、只看行为"的状态
**调节变量**: 个体 高信任倾向者更接受解释、恢复更快，怀疑倾向与高公平敏感者更看重补偿与结构性改变；文化 高关系取向与高权力距离文化中公开承担与面子修复更重要，低语境文化中书面事实、时限与可执行补救更有效；情境 高利害、不可逆、涉及隐私或金钱的违规修复上限最低；能力型违规（延误、故障）修复空间大，诚信型违规（隐瞒、虚标、偷偷扣费）修复空间小
**失效信号**: 道歉后的流失在 30 天内二次上升；用户反复要求"给个时间表"或"要书面承诺"；同一类投诉在修复公告后仍持续出现；退款与补偿接受率上升但复购率不回升；社媒出现"上次也这么说"类对比贴；客服被要求转接上级的比例上升
**可测代理**: 违规事件后的 7、30、90 天留存曲线与复购率；补偿接受率与复购率的相关；同类投诉的复发率；承诺兑现率（修复公告中承诺项的实际达成）；公开事件报告的复核请求量
**交互**: × TR-05 可预测性 → 修复的实质是重建可预测性，没有具体预防机制与时限的道歉不改变预期；× TR-04 立场信号 → 违背后立场信号失效，此时结构性可退出（易取消、可导出、可申诉）比任何表态都有效；× PE-06 支付痛苦 → 与扣费相关的违规（隐藏续费、静默涨价）同时触发金钱痛苦与诚信怀疑，修复上限最低
**边界**: 不得把道歉当作免责工具或用于换取用户放弃法定权利（要求签署保密或放弃索赔作为补偿条件，在中国可能构成不合理限制消费者权利，在美国部分辖区构成对消费者救济权的不当限制）；诚信型违规不得用能力型话术解释（把"故意隐瞒"说成"流程疏忽"），这会二次损害信任并可能构成欺骗；不得在监管调查进行中发布与事实不符的修复声明；涉及安全与数据泄露时，修复必须服从法定通报义务（中国《个人信息保护法》第 57 条，欧盟 GDPR 第 33、34 条），不得以"修复信任"为由延迟通报

### 7. Repair or Reinforcement

**Question**: What happens when something goes wrong?

Trust-sensitive systems are judged hard at failure points.

**Signals**:
- visible ownership
- plain-language apology
- explanation without evasion
- remedy and next-step clarity
- prevention commitment

**Failure mode**:
- defensive tone, blame-shifting, vague apologies, forced support loops

---

## TR-07 · Borrowed Trust 借来信任
**Tier**: 情境
**Evidence**: C — 借来信任的机制基础（来源可信度、权威转移）有经典研究（Hovland & Weiss 1951；Pornpitakpan 2004 元分析显示高可信源短期说服更强），但"用第三方 logo、联名、认证提高转化"的具体效应几乎全部来自行业 A/B 与案例，样本与口径不公开；反向的"背书反噬"（endorsement spillover）也只有案例研究。**没有任何对照实验给出可迁移的效应量**，如实标 C
**Effect**: 小到中等且高度依赖匹配度：借来的信任只在第三方与被借用领域高度相关、且第三方本身在该用户处有既有声誉时有效；不相关或过度使用的背书几乎不产生信任，甚至会因为"明显是买的"而降低信任
**机制链**: 用户把对第三方的既有信任作为捷径，替代对主体的独立核查 → 主体被归入第三方所属的可信类别，核查成本被绕过 → 在低卷入、时间紧、难以核查的场景中前进意愿上升；一旦第三方背书被证伪或与产品不相关，捷径失效并反向污染主体
**剂量**: 弱 只展示真实且可核验的合作关系（真实客户、真实认证、可查的编号） ；中 让第三方证据与用户的具体风险对齐（同类客户的同类问题、同类场景的实测结果），并给出可核查路径 ；强 把第三方变成可追责的约束（SLA 由第三方审计、认证机构可查、联合责任条款），使信任有外部执行机制 ；过载 用大量不相关或无法核验的背书填满页面（成排 logo、名人合影、模糊奖项） → 用户识别为"背书采购"，借来的信任被整体折价，主体自身的能力证据也一并被怀疑
**时间动态**: 起效 秒级（logo 与认证的扫描极快） · 衰减 同一背书在重复接触 3–5 次后失去区分度（竞品都有），背书方的声誉事件会即时传染 · 饱和 背书饱和后不再提升信任，只剩风险敞口：背书方一旦出事，主体承担溢出损失
**调节变量**: 个体 非专业买家更依赖背书捷径，专业买家更看重可核验的一手证据并可能把背书视为替代证据的迹象；文化 高权力距离与集体主义市场对机构背书与名人推荐权重更高，低语境市场更看重可查的认证编号与审计报告；情境 首次接触、低金额、难核查时背书最有效；高金额、专业采购、需承担后果的场景中背书权重下降
**失效信号**: 用户点击 logo 后去第三方站点核查（说明未被直接采信）；背书区域曝光高但停留极短；转化在增加背书后不变；"你们真的和 X 合作吗"类咨询上升；背书方负面事件后本产品的退订与投诉同步跳升
**可测代理**: 背书区域的曝光、点击与核查路径完成率；背书相关咨询占比；背书增减的 A/B 转化差；背书方声誉事件后的 7 与 30 天留存变化；第三方认证的可核验率（编号可查比例）
**交互**: × TR-03 能力信号 → 背书只能加速而不能替代自身能力证据，背书强而能力弱时落差更大；× TR-01 信任链 → 借来的信任跳过的是评估环节而不是验证环节，首次成交后仍要由体验兑现；× AE-04 信源声誉 → 借来的信任是来源声誉的外部注入，一旦被判定为"买来的"，来源声誉损失是双向的
**边界**: 不得使用未授权的第三方标识、虚构合作关系、购买奖项或伪造认证——中国《广告法》第 28 条与《反不正当竞争法》第 8 条、美国 FTC Act 第 5 条与 FTC《消费者评价与推荐规则》（16 CFR Part 465，2024 年 10 月 21 日生效）对虚假背书与虚假评价设有民事罚则，欧盟《不公平商业行为指令》附件一第 1、2、4、11 条为黑名单；医疗、金融、法律领域的背书不得暗示监管批准或执业资质；不得用背书替代对已知缺陷的披露

## Trust Signal Families

### Competence Signals

- product detail
- precise claims
- proof of work
- expert authorship
- implementation specifics

### Integrity Signals

- plain terms
- real limitations
- transparent pricing
- honest comparisons
- no fake scarcity or false personalization

### Alignment Signals

- user-first defaults
- easy exit
- easy cancellation
- privacy-respecting settings
- clear why-this-is-recommended explanations

### Consistency Signals

- stable copy across surfaces
- coherent brand and UI
- consistent support answers
- clear process milestones
- expectations set early and met later

### Borrowed Trust Signals

- known partner brands
- trusted communities
- third-party validation
- credible customer logos
- authority transfer from recognized institutions

Use borrowed trust to accelerate trust formation, not to substitute for real product quality.

---

## Design Patterns

### Pattern 1: Trust Stack on High-Risk Pages

Use descending-friction trust signals:

1. immediate legibility
2. low-cost credibility markers
3. concrete proof
4. honest limitation or tradeoff
5. clear action path

This works better than dumping all trust badges at once.

### Pattern 2: Honest Weakness Disclosure

In trust-sensitive categories, revealing one real limitation can increase trust in every other claim.

Use when:

- the limitation is genuine
- the weakness is bounded
- the system still clearly fits the target user

Do not fake humility. It only works when the limitation is real and coherent.

### Pattern 3: Explain the Why

Whenever the system recommends, defaults, or prioritizes something, explain why.

Example:

- "Recommended because teams like yours usually start here"
- "We ask for this field now because it unlocks setup later"

This converts suspicious nudging into transparent guidance.

### Pattern 4: Reversible Commitment

In fragile-trust contexts, make the first commitment small and reversible.

Examples:

- free preview before signup
- explicit trial terms
- no-card onboarding path
- visible cancel path

### Pattern 5: Repair Fast and Specifically

When trust is damaged:

1. name what happened
2. state the user impact
3. say what changed
4. make the remedy obvious

Avoid vague reassurance like "We take this seriously" without operational detail.

---

## High-Trust Category Guidance

Apply extra trust rigor for:

- health
- finance
- legal
- education
- B2B software with data or workflow lock-in
- marketplaces with fraud risk
- subscriptions and billing flows

For these categories:

- prefer explanation over pressure
- prefer proof over hype
- prefer reversible action over forced commitment
- prefer transparent defaults over conversion-maximizing defaults

---

## Boundary Conditions

Trust signals weaken when:

- they are generic and repeated everywhere
- the user detects even one deceptive cue
- the proof is impressive but irrelevant
- the promise and first experience do not match
- urgency is strong but explanation is weak

Trust signals strengthen when:

- they are specific
- they are relevant to the exact risk the user feels
- they are encountered in the order users naturally inspect risk
- the system behaves consistently after commitment

---

## Combinations

- **Trust Transfer × Processing Fluency**
  Strong for first impressions and form completion.

- **Authority × Honest Weakness Disclosure**
  Strong in B2B, health, and expert-led contexts where credibility and honesty both matter.

- **Predictability × Fast First Success**
  Strong for onboarding and activation in trust-sensitive products.

- **Alignment × Easy Exit**
  Strong for subscription, marketplace, and consent-sensitive flows.

Use combinations to reduce felt risk, not to overpower scrutiny.

---

## Routing Notes

Prefer this file over general social dynamics when the central problem is trust, reassurance, or credibility rather than virality or conformity.

Read alongside:

- `references/anti-patterns.md` for trust-breaking failure modes
- `references/models/perception-attention.md` for fluency-driven trust cues
- `references/models/social-dynamics.md` for authority and trust transfer
- `references/models/cognitive-architecture.md` when ambiguity, threat, or cognitive load is the hidden trust blocker
