# Cognitive Architecture — Model Details

> **Domain**: core cognitive processing, load limits, prediction, time horizon, embodied cues
> **Use when**: the task depends on how people process information, switch between intuitive and reflective thinking, or abandon flows under cognitive strain
> **Scope**: concise reference for the few cognitive models most useful in product, UX, and content decisions

---

## CA-01 · Dual Process
**Tier**: 核心
**Evidence**: B — 行为层面的现象（摩擦、新颖、模糊会把判断推向更慢更费力的加工）有多项独立研究与元分析支持，来源为 Evans & Stanovich 2013 的 type-1/type-2 定义性特征综述与 Kahneman 2011 的普及综述。**但"系统1/系统2"是隐喻而非解剖实体**：Melnikoff & Bargh 2018（TiCS《The Mythical Number Two》）系统检视后指出，没有任何证据支持大脑中存在两个可分离的加工系统——所谓两系统的属性（快/慢、自动/受控、并行/串行、情绪/逻辑）彼此低相关，且同一任务可同时表现两类属性；Keren & Schul 2009 与 Kruglanski & Gigerenzer 2011 提出同样的"统一性假设不成立"批评。可复现的是"加工深度随线索与后果变化"这一连续维度，不是两个实体
**Effect**: 中等偏大，但只在连续维度意义上成立：线索与既有图式不匹配、或后果被判定为高时，核对行为与决策延迟可靠上升；效应大小取决于工作记忆余量，而非"切换到某个系统"。把它写成"人有两个系统"会导出错误预测（例如预期同一用户在同一任务上稳定处于某一"系统"），实测中个体内变异大于个体间差异

**机制链**: 线索与既有图式不匹配或后果被判定为高 → 慢速、串行、依赖工作记忆的受控加工被招募 → 决策延迟、核对与回改行为增加，或在该加工不可用时直接放弃
**剂量**: 弱 保留默认路径，只在一个字段旁给出可选说明 ；中 要求用户比较两个以上属性或核对一条外部信息（引入真实但有限的加工需求） ；强 显式呈现不可逆后果、要求用户用自己的话复述或二次确认，并提供可查证的外部依据 ；过载 摩擦超过用户对该决策的意愿投入 → 结果不是"更审慎"而是**反思性加工被完全绕过**：用户放弃、接受默认值、或把决策交给他人/客服，行为退化为最省力选项，且事后归因为"我没真正选过"
**时间动态**: 起效 秒级（单次界面即可改变加工深度） · 衰减 同一流程重复 3–5 次后受控加工被技能化压缩为组块，摩擦不再触发反思，只增加时间成本 · 饱和 长期高频使用后用户形成"这个流程要动脑"的入口级预判，在第一步之前就放弃
**调节变量**: 个体 工作记忆容量与认知需求（need for cognition）高者能维持受控加工更久，低者更快退回直觉路径；文化 高不确定性规避文化中模糊线索更易触发核对，低语境文化中冗长解释反而抬高负荷并加速放弃；情境 时间压力、疲劳、睡眠剥夺与饥饿状态下可用资源下降，反思被系统性跳过（方向确定，幅度随状态而异）
**失效信号**: 表单中途停留时长骤增而完成率下降；客服与帮助文档询问高度集中在同一字段；"返回上一步"点击率在同一步骤异常升高；简化版转化上升但理解度抽测分数不降（说明原摩擦未产生任何理解收益）；用户在事后访谈中说不出自己确认过什么
**可测代理**: 分步漏斗完成率与单步停留时长；首次提交前的字段回改次数；简化版与完整版的 7 日留存和退款率差；可选的 3 题理解度抽测（最小实验：同流程两版本随机分流）
**交互**: × CA-02 认知负荷 → 负荷占满工作记忆时受控加工实际不可用，摩擦不再引发审慎而只引发放弃，两机制叠加时放弃率呈超线性上升；× CA-05 时间折扣 → 反思成本落在当下、收益落在未来，受控加工被系统性跳过，这正是 COMBO-05 的近失与沉没成本能够生效的缝隙
**边界**: 不得把需要审慎的决策（知情同意、定价与续费条款、医疗与金融风险披露）刻意做成直觉判断——在同意场景中"降低摩擦"等于削弱同意的有效性，可能构成同意瑕疵与合规风险；不得把"用户选了直觉路径"当作免责理由；本记录不得用于论证"用户只有两个模式"从而为粗粒度人群分层背书

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.91；Effect Size: Large

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
**Tier**: 核心
**Evidence**: A — 工作记忆容量有限这一前提证据很强（Cowan 2001 的四±一容量估计取代了 Miller 的七±二；Sweller, van Merriënboer & Paas 2019 的认知负荷理论综述汇总了大量实验）。**但构念本身有争议**：de Jong 2010（《Cognitive load theory, educational research, and instructional design: some food for thought》）指出"认知负荷"缺乏独立于结果的操作定义，多数测量（双任务、瞳孔、NASA-TLX）是负荷的代理而非负荷本身，设计原则常与"先验知识不足"混淆，存在循环解释风险；"降低负荷提升学习/完成"的效应在专家被试上系统性反转（expertise reversal effect, Kalyuga 等）。因此容量限制按 A 级采用，具体设计处方按 B 级采用
**Effect**: 中等偏大，且**只对"可避免负荷"成立**：同屏未组块化元素数与放弃率、错误率正相关；对已把结构组块化的专家几乎无效应，对新手效应最大。效应量随专长度与情境稳定性剧烈变化，不能外推为"所有界面越简单越好"

**机制链**: 界面同时要求保持多个未组块化的元素 → 工作记忆容量被占满、元素间关联无法建立 → 犹豫与错误率上升，任务放弃或退回默认选项
**剂量**: 弱 合并同类字段、删掉重复说明与装饰性文案 ；中 把长流程切成 3–5 步并显示位置，把选项按语义分块到不超过四组 ；强 引入外部记忆支架：预填已知信息、自动保存草稿、并排对比表、可回看的摘要，使用户不必在脑内保持状态 ；过载 把负荷削到"零"（全默认、全自动填充、无任何解释与选择） → 用户失去对决策的掌控与可解释性，产生"这不是我选的"归因，事后反悔、退款与投诉上升，即负荷削减反转为信任损失
**时间动态**: 起效 单次任务内即时（秒级到分钟级） · 衰减 不衰减而是**转移**：同一流程重复 3–5 次后用户把结构组块化，原有负荷消失，继续简化不再产生收益 · 饱和 过度简化后用户未建立可迁移的心理模型，遇到第一个未覆盖的例外情形即崩溃
**调节变量**: 个体 领域专长度越高，外在负荷的负面影响越小（专家把元素组块化），工作记忆容量高者对同屏元素数更宽容；文化 高语境文化用户更依赖解释性文字，删文字反而抬高不确定性，低语境文化用户更接受结构化分块与图标化；情境 移动端、单手操作、弱网与分心环境下有效容量更低，疲劳与时间压力下同屏元素容忍阈值显著下降（方向确定，幅度未定）
**失效信号**: 用户在第三步之后反复回看第一步的答案；同一屏出现两处以上"这是什么意思"的客服提问；简化版完成率上升但 30 日留存不升（说明负荷不是瓶颈）；用户在例外情形下反复提交同一错误输入；专家用户抱怨"被当成新手"
**可测代理**: 每步停留时长与回退率；字段级错误率热图；完成时间分布的双峰性（双峰=部分用户已组块化，简化对其中一半无效）；可选的单题主观负荷自评或 NASA-TLX
**交互**: × CA-01 双系统 → 负荷占满工作记忆时慢通道不可用，摩擦不再引发审慎而引发放弃；× CA-04 注意极限 → 元素数与注意竞争同时逼近各自上限，放弃率呈超线性上升，COMBO-11 的预填与进度前置之所以稳，正因它同时降低两者；× MR-06 伪进度 → 起点降低"从零开始"的启动负荷，是本族中净效应最稳的一环
**边界**: 不得以"降低负荷"为名移除风险披露、条款要点、撤销与退出入口；教育、技能与安全培训产品中刻意保留的"合意困难"（desirable difficulty）是学习收益来源，按负荷最小化设计会摧毁学习效果；不得用负荷话术为信息隐藏背书

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.93；Effect Size: Large

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
**Tier**: 常用
**Evidence**: C — **神经层面与行为层面必须分开评级**。神经层面接近 B：预测误差信号在电生理与成像中有大量一致证据（失匹配负波、预测误差相关的 fMRI 反应、以及 Friston 自由能框架下的计算模型），但这些是**机制层证据**，不能直接推出"某种界面写法会提升转化"。行为层面为 C：产品语境下"预期违背提升注意"的结论绝大多数是从神经机制反推的设计假设，缺少对照实验；"预测编码是大脑的统一原理"这一强主张本身也被批评为难以证伪（可拟合任何数据），且与自适应共振等替代框架并存。本记录只作为排序假设使用，任何具体阈值都必须由 A/B 验证
**Effect**: 行为效应量不确定。可复现的部分是"中等偏离预期会提升注意与记忆"（violation of expectation 范式），但阈值高度依赖先验强度：先验越强，同一偏离的惊讶值越大、也越快被归因为错误。偏离过大时效应明确反转。**不得用神经机制反推行为设计**

**机制链**: 输入流与自上而下的预测模型之间产生可检测的偏差 → 偏差被作为精度加权的误差信号放大并重新分配注意 → 注意转向偏差源，模型被更新；偏差超出可归因范围时模型被整体放弃
**剂量**: 弱 在熟悉版式内只改一个措辞或一个数字，保持结构不变 ；中 保留约八成结构，只推翻一个核心主张或一个预期结果（"你以为的 X 其实是 Y"），并在内容内给出解释 ；强 连续两次预期违背（钩子一次、内容内二次反转），且每次都在同一屏内被解释兑现 ；过载 偏差超出用户可归因的范围（无解释、无参照系、或与用户的强先验直接冲突） → 误差信号不再被当作"值得更新"，而被归因为不可信或故障，注意撤离且信任下降，即惊讶反转为怀疑
**时间动态**: 起效 毫秒到秒级（失匹配与朝向反应） · 衰减 同一类型的预期违背重复 2–4 次后先验被更新，惊讶值归零（"又是这一套"） · 饱和 长期使用后用户把"惊讶"本身纳入元预期，钩子被识别为套路，此后连真实的新信息也被折价
**调节变量**: 个体 领域专长提高先验精度——同一偏差对专家是"错误"、对新手是"新奇"；认知需求高者愿意为解释付出加工成本，低者直接判为噪音；文化 高语境与高权威文化中偏离共识或权威的线索更易被归因为不可信而非有趣；情境 高认知负荷与时间压力下偏差被当作噪音过滤（没有余量更新模型），低风险娱乐情境中容忍度最高
**失效信号**: 钩子点击率上升而内容完成率下降（偏差未被兑现）；评论区集中出现"标题党""说的不是这个"；第二次触达中惊讶型开头打开率低于平铺直叙型；用户开始预测你的反转（"下一句肯定要转折"）；同一素材第 n 次曝光的 CTR 衰减快于普通素材
**可测代理**: 首屏 3 秒与首句留存；预期违背型与平铺型开头的完成率差；同一用户第 n 次触达的惊讶型素材 CTR 衰减曲线；"解释到位"与"解释缺失"两组的完成率差
**交互**: × CA-04 注意极限 → 多个预期违背同时出现会互相稀释误差信号，只有最先到达者获得注意，COMBO-09 要求一次只开一个缺口正源于此；× CA-02 认知负荷 → 偏差需要工作记忆余量才能被解析为"有趣的意外"，负荷高时同一偏差被解析为"错误"；× MR-12 奖励变异 → 变动奖励本质是可控的预测误差供给，误差可解析时提升参与，不可解析时转为不可信
**边界**: 不得把神经层面的预测误差证据当作行为效果的证明来支撑设计决策（这是本族最常见的越界）；在安全、医疗、金融告警场景中刻意制造预期违背会降低对真实告警的响应（狼来了效应），禁用；对已处于焦虑状态的用户，不可预测性本身就是伤害源

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.87；Effect Size: Large

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
**Tier**: 核心
**Evidence**: A — 知觉层面的选择性注意与容量限制是复现良好的现象：非注意盲与变化盲（Simons & Chabris 1999 的大猩猩实验被多次独立复制）、Lavie 的知觉负荷理论、以及注意瞬脱。**但"多线索稀释转化"是产品层外推，不是知觉结论**：其效应量取决于线索的相关性与任务阶段，同域多入口有时反而提升可达性；"注意力是有限资源池、会被耗尽"的强版本（与 ego depletion 同构）未被复现，不应作为设计前提。故知觉容量按 A 级采用，转化层结论按 B 级采用
**Effect**: 知觉层效应大（未获注意的刺激检测率可接近零）；转化层中等且条件性强——同屏等权竞争线索数上升时主行动点击率下降，但线索若服务于同一任务的不同阶段则无此效应

**机制链**: 多个线索在同一时间窗争夺有限的选择性注意与知觉容量 → 注意按显著性与任务相关性分配，其余被抑制（非注意盲） → 单一目标动作的检出与执行概率下降，未获注意的入口在行为上等于不存在
**剂量**: 弱 每屏一个主行动加一个视觉次级的文字链 ；中 按任务阶段分配主行动，每阶段只留一个，其余动作降级或折叠 ；强 主动删除或延后非当前阶段的一切提示：通知合并、入口折叠、序列化引导，一次只呈现一个决策点 ；过载 把所有线索压到零（页面无任何突出动作、通知全关、界面完全中性） → 用户找不到入口，任务启动率下降，注意不再被引导而是被清空，即"减少干扰"反转为"无路径"
**时间动态**: 起效 100–300 毫秒级（朝向反应与早期选择） · 衰减 同一位置的重复线索在数次曝光后产生习惯化（banner blindness），显著性收益衰减到接近零 · 饱和 长期高密度提示训练用户形成整块忽略策略，此后连真实重要提示也被跳过
**调节变量**: 个体 注意控制能力与工作记忆容量高者能在多线索下维持目标，ADHD 特质与高冲动性者对竞争线索更敏感；文化 集体主义与高语境文化对情境性、关系性线索分配更多注意，个人主义与低语境文化更聚焦中心目标；情境 小屏、移动中、驾驶与分心场景下有效视野与容量进一步收窄，高情绪唤醒状态下注意窄化
**失效信号**: 首屏主 CTA 点击率随同屏入口数增加而下降；热图显示视线在多个等权元素间来回而无点击；同一位置提示曝光高但点击趋零（习惯化）；用户反馈"不知道下一步点哪里"；通知关闭率随单次推送条数上升
**可测代理**: 同屏入口数与主 CTA 点击率的相关曲线；首次有效点击时间；前三个注视点覆盖的屏占比（注意集中度）；通知的曝光-点击-关闭三段率
**交互**: × CA-02 认知负荷 → 元素数与注意竞争同时上升时放弃率呈超线性；× CA-03 预测编码 → 显著性来自预期违背，因此"更醒目"的边际收益随先验更新而衰减，COMBO-09 的模式中断只在单点有效；× MR-11 近失效应 → 近失提示是最强的注意捕获物之一，在高竞争界面中它会吞掉主行动的全部注意预算
**边界**: 不得用注意捕获掩盖信息缺失（把关键条款做成不显著以降低注意，属欺骗性设计）；对低视力、认知障碍与前庭敏感用户，"减少线索"会直接变成不可用，显著性必须与无障碍标准并存；安全告警场景中压缩线索数量会降低召回，禁用

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Medium-Large

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
**Tier**: 核心
**Evidence**: B — 方向性结论（近期结果获得更高决策权重）复现良好，但**贴现率的数值不可移植**。Frederick, Loewenstein & O'Donoghue 2002（JEL《Time Discounting and Time Preference: A Critical Review》）综述指出：贴现率估计在不同诱导方法（真实选择、假设选择、拍卖、田野数据）之间相差可达数量级，且与真实行为的相关性弱；量级效应（magnitude effect）与延迟效应（delay effect）说明并不存在单一稳定的贴现率。**模型之争未决**：β-δ 准双曲线模型（Laibson 1997）能解释偏好反转与承诺需求，但被批评为对异质性与测量误差过度灵活、可拟合几乎任何数据；单一参数的双曲线模型（Mazur）在多数选择数据上拟合不劣，且更简约。因此"人有稳定贴现率"的强版本不被支持，可依赖的只有方向与框架依赖
**Effect**: 方向稳定、幅度不可移植：贴现率随金额量级、延迟长度、获得与损失、以及目标是否被具体化而变。设计上只能依赖"把未来拉近"的方向，不能依赖任何具体贴现率数值；对已具体化、可分解、有近期反馈的目标，有效贴现显著下降

**机制链**: 未来结果在心理上被表征为抽象且不确定 → 近端成本与收益获得更高的决策权重 → 选择当下省力或即时回报，推迟有长期收益的行动
**剂量**: 弱 把长期收益翻译成一个具体的近期里程碑（"第 3 天就能看到 X"） ；中 把收益切成可见的近期分段，并给出第一段的时间点、形式与判定标准 ；强 在近期窗口内制造一次真实、可验证、与长期目标同向的小收益（首周见效的样例、试算、演示数据） ；过载 把一切长期价值都压缩成即时刺激（处处即时反馈、天天有奖励） → 用户对延迟的容忍度进一步下降，任何必须等待的真实收益（技能、健康、复利）都被判定为"没有回报"而放弃，即"拉近未来"反转为"消灭未来"
**时间动态**: 起效 单次选择内即时（秒级） · 衰减 即时奖励的吸引力在重复 5–10 次后因参照点上移而衰减，需要不断加码 · 饱和 长期即时化会**内生地抬高**用户的贴现率，产品越做越难留住需要耐心的用户，且该变化在离开产品后仍残留
**调节变量**: 个体 年龄（青少年贴现率更高，随年龄下降）、资源稀缺与压力状态（稀缺心态提高贴现）、未来取向与自我控制特质；文化 长期取向文化对延迟收益耐心更高，短期取向与高不确定性文化中即时性诉求更强；情境 具体化、可视化、可分解的呈现降低有效贴现，抽象、遥远、无反馈的目标提高贴现
**失效信号**: 长期收益页面停留极短而"立即获得"入口点击集中；试用期结束前活跃度断崖；同一用户对"3 天后"与"30 天后"的反应无差异（时间描述已失去区分度）；留存曲线在首个"没有即时反馈"的阶段塌陷；用户主动询问"这到底什么时候有用"
**可测代理**: 同一承诺的"具体近期版本"与"抽象长期版本"转化差；从注册到第一次真实收益的时间（time-to-first-value）与 7/30 日留存的相关；折扣选择任务（今天 100 与 30 天后 X）作为个体差异的廉价代理
**交互**: × CA-01 双系统 → 即时选项走直觉通道、延迟选项需受控加工，时间压力下两者差距被放大；× MR-11 近失效应 → 近失把"下一次机会"拉到近端，等于人为降低有效延迟，COMBO-05 的锁定效应由此产生，其伦理门槛也由此产生；× MR-05 自主性 → 自主性收益在远期（能力成长）、控制式奖励收益在近期，短期指标会系统性偏向控制式设计
**边界**: 不得用于把高风险长期承诺（贷款、保险、自动续费订阅）包装成"每天不到一杯咖啡"以掩盖总成本；对资源稀缺人群，即时化诉求会加剧而非缓解短视，属加重既有脆弱性；贴现率不得作为个体能力或品格的度量，也不得用于信贷、雇佣、保险的差别定价

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.86；Effect Size: Medium-Large

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
**Tier**: 情境
**Evidence**: C — 这一族是本文件里证据最弱的一条，必须如实标注。高层次"具身隐喻"效应（重量对应重要性、温度对应人际温暖、洁净对应道德）在 2010 年代的大样本重复中系统性失败：Rabelo, Keller & Pilger 2015 未能复现重量-重要性效应，Lynott et al. 2014 的重复实验未复现温度-人际温暖效应，相关元分析给出的效应量接近零并提示发表偏倚。可复现的只剩低层次感知-运动一致性（运动线索影响时间估计、触觉反馈影响主观流畅度与错误率感知）。因此本记录**只能作为辅助一致性线索**，不得作为转化杠杆；v1 的 Confidence 0.74 已属高估
**Effect**: 小到中等且不稳定：材质、动效与品牌定位一致时可小幅提升主观流畅与可信评分；在缺少实质价值主张时效应趋零；单独使用几乎不改变高利害决策

**机制链**: 物理或感官属性（重量、温度、粗糙度、运动速度）被自动编码 → 与之关联的概念隐喻被部分激活（重要、温暖、费力、果断） → 对抽象判断产生小幅偏移，并提高或降低主观流畅度
**剂量**: 弱 材质与动效方向与定位一致（轻快对应活泼，稳重对应可信） ；中 在多个触点上统一同一感官隐喻（开箱、包装、动效曲线、声音） ；强 让物理交互承担信息功能：重量或阻力传达不可逆操作，触觉反馈确认状态，使用户通过身体而非文字理解后果 ；过载 感官线索与内容主张冲突或过度堆叠（处处动效、处处材质戏） → 感官处理占用认知资源，主观流畅度下降，用户报告"花哨""不专业""卡"，即隐喻反转为噪音
**时间动态**: 起效 百毫秒级（感知编码先于语义判断） · 衰减 单一线索的隐喻联想在重复曝光后语义化（用户学会"这个动效=加载中"），隐喻让位于约定俗成 · 饱和 长期使用后线索成为品类通用语，不再携带区分度，只剩加工成本
**调节变量**: 个体 感官敏感度与身体觉察（bodily awareness）高者效应更强，以参数而非感受判断的专业买家效应近零；文化 隐喻映射高度文化特定（重量对应重要性在多数语言中成立，但颜色、方位、温度的联想差异极大），跨文化复用同一感官隐喻风险很高；情境 高认知负荷与高利害决策中感官线索被忽略，低风险、体验型、需要"感觉对"的品类中效应最大
**失效信号**: 评价中出现"包装好看但东西一般"（感官承诺未被内容兑现）；动效丰富版本完成率不升反降；可用性测试中用户说不出动效含义；同一感官线索在两个市场的偏好方向相反；前庭敏感用户报告眩晕
**可测代理**: 同一功能"有感官反馈"与"无感官反馈"两版的完成率与单题主观流畅评分；动效时长与任务完成时间的比值；跨市场对同一材质与动效的偏好差；评价与客服中"花哨/卡顿/不专业"的词频
**交互**: × CA-02 认知负荷 → 感官线索本身占用加工资源，负荷已高时净效应为负；× CA-07 自我叙事 → 感官线索只有在与用户自我形象一致时才被读成"这就是我的风格"，COMBO-07 的线索层若只用物理线索而不接身份，习惯回路会脆弱；× CA-03 预测编码 → 动效的"惊喜感"来自预期违背，同一动效重复后惊讶值归零，只剩延迟成本
**边界**: 不得用感官线索替代实质信息（以高级材质感包装低质服务属误导）；不得把关键状态只编码为触觉或动效——听障、视障与前庭功能障碍用户不可用；对光敏性癫痫用户，闪烁与快速运动线索是医学风险而非设计选择，必须遵守 WCAG 闪烁阈值

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.74；Effect Size: Medium

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
**Tier**: 常用
**Evidence**: C — **神经层与叙事层之间存在一步未被证实的跳跃**。神经层证据较强（Raichle 等 2001 的默认网络、自我参照加工与内侧前额叶/后扣带的关联），但默认网络功能高度异质，与情景记忆、心理理论、未来情景模拟共享同一套区域，"任务一停就启动自我叙事"的二分不成立，把网络静息活动直接映射为"自我故事"是理论推断而非实证结论。行为层可复现的是自我参照效应（self-reference effect：与自我相关的材料记忆与说服优势，证据较好），以及未来自我连续性对延迟决策的初步影响（Hershfield 2011 的 future-self continuity，样本小、复现有限）。故整体按 C 级采用
**Effect**: 自我参照加工对记忆与说服的效应稳定（中等）；"身份框架改变长期行为"的效应小，且依赖一致性压力与公开性；未来自我连续性对储蓄类行为的效应有初步证据但复现有限

**机制链**: 信息被判定为与"我是谁/我将成为谁"相关 → 进入自我参照加工并接入自传体记忆与未来模拟 → 编码更深、意义感上升，行为被重新解释为"符合或违背我这个人"
**剂量**: 弱 用第二人称与用户自己的数据或原话复述结果 ；中 把行为与用户已声明的价值或目标显式对齐（"你说过 X 重要"），并在真实里程碑处给出身份标签 ；强 让身份在他人可见处成立（公开承诺、社群身份、可回看的自我历史），使违背身份同时产生社会与自我双重不一致 ；过载 身份标签被高频、无门槛地发放（人人都是"专家/大使/创始成员"） → 标签失去区分度与证据基础，用户识别为廉价激励，身份从"我是"退回"我被贴了标签"，一致性压力反转为反感与去认同
**时间动态**: 起效 单次触达内（分钟级，自我参照加工即时提升编码） · 衰减 缺少持续行为证据的身份标签在 2–6 周内贬值，同一叙事重复 3–5 次后用户开始反驳（"你老说我是 X"） · 饱和 深度身份融合的用户在遭遇一次身份违背（产品事故、社群冲突、被公开打脸）时经历去认同冲击，退出更彻底且伴随更强负面口碑
**调节变量**: 个体 自我概念清晰度高者受身份框架影响更大也更抗拒被定义，低自尊与高自我监控者对标签更敏感；文化 独立自我文化中身份指向个人特质与成就，互依自我文化中指关系角色与责任（"作为团队的一员"优于"你是个赢家"）；情境 生命转折点（入学、换工作、搬家）与公开场景下效应最强，私密、低风险、一次性任务中最弱
**失效信号**: 收到身份标签后次周行为无增量或下降；社群中出现对标签的玩梗与嘲讽；"你曾说 X 重要"类召回信息的打开率与退订率同时上升；身份声明与实际行为的公开不一致被他人指出后活跃度骤降；标签覆盖率与人均贡献呈负相关（通胀信号）
**可测代理**: 身份框架与结果框架文案的 7/30 日行为差；身份标签发放后的次周行为增量与 90 日留存；产品内 UGC 中自述身份词（"我是…"）的出现频率；召回信息的打开-退订比
**交互**: × CA-05 时间折扣 → 把未来自我变得连续（同一人而非陌生人）可降低有效贴现；× MR-04 身份承诺 → 叙事提供"我是谁"的素材、承诺提供"我做过什么"的证据，合流后退出成本从行为层升到自我层，COMBO-12 的四层锁定即此路径，其不可逆性也源于此；× CA-02 认知负荷 → 自我参照加工需要余量，负荷高时身份框架被当作无关信息跳过
**边界**: 不得把身份框架用于制造退出羞耻（"退出=你不是那种人"属胁迫性一致，禁用）；心理治疗、丧亲、身份危机与青少年用户对身份叙事操纵极度脆弱，禁用；不得基于推断的敏感身份（健康、宗教、性取向、政治立场）做身份框架，属高风险个人数据加工，多数辖区需单独同意

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.78；Effect Size: Medium

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
