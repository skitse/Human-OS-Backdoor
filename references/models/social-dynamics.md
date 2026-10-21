# Social Dynamics — Model Details

## SD-01 · Social Proof
**Tier**: 核心
**Evidence**: B — Asch 1951 线段判断实验（约 37% 试次从众、75% 至少从众一次）为实验室基准；Bond & Smith 1996 元分析（133 项研究、17 国）确认效应可复制，但同时发现顺从率随年代下降、且集体主义文化样本的顺从率显著高于个人主义样本。争议：①Asch 范式是"无客观答案可核验"的极端不确定情境，电商与评论场景中用户可自行比价、试用、看差评，效应量远小于实验室数字，真实"最受欢迎"标签的 A/B 提升通常只有个位数百分比；②Cialdini 系现场研究（Goldstein et al. 2008 酒店毛巾复用的描述性规范信息）在 Bohner & Schlüter 2014 的现场复制中效应大幅缩小甚至消失；③"数字越大越有效"缺剂量证据。只引支持性文献会把该机制高估 3–5 倍
**Effect**: 中等偏大，仅在"决策不确定 + 参照群体相似 + 信号可归因"三条件同时成立时达到实验室量级（顺从率 30–75%）；一旦用户能独立核验（比价、试用、读差评），效应降至接近噪声
**机制链**: 面对无客观答案或核验成本高的选择 → 他人行为被当作该情境下的正确性线索，不确定性越高其权重越大 → 复制多数人的选项以压低判断错误的预期代价
**剂量**: 弱 静态展示总用户量或累计评价数（"10,347 人学过"） ；中 展示与用户同类群体的具体行为并给出时间窗（"你所在行业 87% 选了年付"） ；强 实时、可归因、带竞争语义的同伴信号（"3 位你认识的人刚购买""12 人正在看这件"）叠加差评可见的评分分布 ；过载 社会证明变成不可核验的滚动数字，或与库存倒计时联动催单 → 用户识别为营销装置，反向把"高人气"读作"被推销的商品"，点击率与信任同步下降并外溢到真实评分
**时间动态**: 起效 秒级（首屏可见的同伴信号在一次停留内改变选择） · 衰减 同一用户在第 2–4 次遇到同类信号后开始忽略位置固定的社会证明模块（横幅盲视） · 饱和 当站内所有商品都标"最受欢迎/热销"时该信号失去区分度，只剩合规风险
**调节变量**: 个体 领域知识越少、自我效能越低，从众越强；高专业度与高认知需求用户几乎只信可核验证据 · 文化 Bond & Smith 1996：集体主义/高语境文化顺从率显著更高；个人主义市场对"多数人选了"反应弱，而对"像你的人选了"反应强 · 情境 高不确定、高社会可见、低可核验成本时效应最大；有明确客观标准（规格、价格、可退换）时可核验性把效应压到很小
**失效信号**: 社会证明模块的点击率第二周起持续下滑而页面其他模块不变；用户在评论或客服渠道复述你的数字并质疑口径（"12 人正在看"与真实并发数不符）；同一"热销"标签出现在互不相关的全部 SKU 上；转化率对社会证明文案的 A/B 不再敏感（两组差异落入置信区间）
**可测代理**: 同伴信号模块曝光→点击→转化的三段漏斗与无该模块对照分流的差；"最受欢迎"标签点击率随展示次数（第 1/2/3 次曝光）的衰减曲线；评论文本中质疑数字口径的提及率；同一 SKU 上标签与实际销量排名的秩相关
**交互**: × HB-02 损失厌恶 → 社会证明把"别人在做"翻译成"你正在掉队"，是 COMBO-01 的情绪引擎，但双重施压也最快触发抗拒（COMBO-01）；× SD-02 互惠规范 → 被点名的种子用户产生回礼义务，使早期可见行为形成级联，构成 COMBO-04 的启动条件（COMBO-04）；× HB-04 稀缺 → 社会证明为稀缺提供"为什么现在"的竞争理由，同时稀缺让社会证明显得危险
**边界**: 不得使用虚构或不可归因的人数（"XX 人正在浏览"若为常数即构成虚假宣传，《反不正当竞争法》第八条、《消费者权益保护法》第二十条）；医疗、金融、法律等高风险决策中社会证明会替代个体化证据，须改为披露样本量与选择偏差；未成年人产品中社会证明与同伴压力叠加，应限制可见的比较性数据

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.90；Effect Size: Large (30-75% conformity rates)

**Mechanism**: In uncertain situations, people use others' behavior as a signal of correct action. The more uncertain the decision, the more weight social proof carries.

**Types of social proof** (strongest to weakest for typical contexts):
1. **Similarity proof**: "People like you did X" (highest — peer group)
2. **Expert proof**: "Professionals recommend X"
3. **User proof**: "10,000 people use X"
4. **Wisdom of crowds**: "Most popular choice: X"
5. **Celebrity/Authority**: "Endorsed by X"

**Implementation**:
```
Dynamic display: "47 people bought this in the last 24 hours"
Peer-specific: "3 of your LinkedIn contacts use this"
Consensus: "87% of users chose the annual plan"
Real-time: "12 people are viewing this right now"
Near-peer: "People in [your city/industry] chose X"
Rating clusters: "★★★★★ 4.8 from 2,847 reviews"
Progress: "10,347 people have completed this course"
```

**Amplification factors**:
- Recency ("in the last hour" > "last month")
- Similarity ("in your industry" > "users")
- Specificity (exact numbers > round numbers, e.g., "847" > "hundreds")
- Proximity (people you know > strangers)

**Combos**: Social Proof × Loss Aversion → "you're the last one in your group without X"
Social Proof × Scarcity → "3 left and 12 people watching"

---

## SD-02 · Reciprocity Norm
**Tier**: 常用
**Evidence**: B — Regan 1971 可乐实验（收到免费饮料者购买抽奖券的数量约为未收到者的两倍）是核心实验室证据；Cialdini 的现场观察与"拒后撤"研究支持互惠规范跨情境存在。争议：①Regan 实验样本小（约 80 人）、单实验室，且"礼物→顺从"路径与"喜欢"混淆，后续难以把纯粹的互惠义务分离出来；②Gächter & Falk 2002 显示互惠异质性极大，约三成为无条件利他、约两成为完全自利，"规范"并非普遍常量；③商业场景中免费样品/免费内容的转化证据受选择偏差污染（领取者本就有需求），现场测得的增量远低于实验室；④礼物一旦被识别为战术，效应反转为抗拒
**Effect**: 中等，仅在礼物被判定为"自愿、非交换、有个人指向"时成立；一旦礼物被读作交易的前置步骤（附条件、夹带推销话术、明显模板化），顺从率回落到与直接请求无差异
**机制链**: 收到未索取的好处 → 产生未清偿的亏欠感与被识别为"受惠者"的自我形象压力 → 以超出礼物价值的回礼行为（购买、转发、评价、引荐）清偿
**剂量**: 弱 提供无附加条件的公开内容或工具，不索取任何回报 ；中 明确指向个人的小礼物（"这份模板是按你上次提的问题做的"），之后一次触达中提及但不明示回报 ；强 在关键请求之前给予不可忽视的定制化好处，并让"给予"被第三方看见（公开致谢、署名） ；过载 礼物与请求同时出现，或以"免费"换取邮箱/手机号/数据授权 → 被重新归类为交换甚至诱饵，用户以"我并没要"消解亏欠，反向产生被操纵感并抬高后续真实善意的折扣
**时间动态**: 起效 分钟级至小时级（收到礼物后的短窗口内顺从概率最高） · 衰减 亏欠感在数天至两周内衰减，并被"我已经谢过了"的自我叙事提前清偿 · 饱和 反复赠予后礼物被计为常规服务，互惠义务归零，成本变成纯支出
**调节变量**: 个体 互惠倾向的个体差异大于任何设计变量（Gächter & Falk 2002）；高警惕性与高马基雅维利倾向用户会把礼物直接定价为营销成本 · 文化 集体主义与人情社会（中国、日本、拉美）中互惠义务更强且期限更长，但"欠人情"同时带来回避，可能表现为不回应而非拒绝 · 情境 礼物与请求间隔越短、越个性化、越非金钱化，义务感越强；B2B 采购与合规审查情境中礼物触发利益冲突申报，效应被制度性阻断
**失效信号**: 领取免费资源的用户后续付费转化率与未领取组无差异；触达中出现"不用谢，我不需要"类明确解除义务的回复比例上升；礼物领取→退订的转化率高于领取→付费；客服工单中出现"你们送东西就是为了卖"的表述
**可测代理**: 礼物组/无礼物组的后续请求响应率差；从礼物到首次请求的时间间隔与响应率的关系曲线；领取者的退订率与投诉率；个性化三档（模板/按人名定制/按具体问题定制）的响应率梯度
**交互**: × SD-01 社会证明 → 种子用户的可见给予同时制造从众压力与回礼义务，是 COMBO-04 的两条腿，叠加后社区参与率非线性上升但退出成本同升（COMBO-04）；× SD-06 网络效应 → 互惠网络让低密度社区也变粘，是 COMBO-17 中"网络价值尚未出现时先靠义务留人"的那一段（COMBO-17）；× HB-08 沉没成本 → 用户已付出（而非已获得）时互惠方向反转，退出会被体验为背债
**边界**: 不得把附条件交换包装成礼物而不披露（"免费"须真免费，捆绑索取个人信息受《个人信息保护法》最小必要原则约束）；医疗、法律、政务、招投标场景中礼物构成利益冲突或贿赂风险，绝对不可用；不得利用互惠对脆弱人群（经济困难、情感依赖）施加索取

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.92；Effect Size: Large

**Mechanism**: Receiving a gift — even unsolicited — creates a psychological obligation to reciprocate. The rule of reciprocity is one of the most powerful compliance triggers in human society.

**Key findings**:
- Unsolicited gifts work as well as solicited ones
- Size of gift matters less than the fact of giving
- Personalized gifts create stronger obligation than generic ones
- The rule operates even when we're aware of it

**Implementation**:
```
Free value first: Free tool / template / report before asking for email
Samples: Free taste → purchase obligation (supermarkets, SaaS trials)
Content: Provide substantial free value; paid product feels like reciprocating
Service: Unexpected upgrade / gesture → review / referral obligation
Community: Personal message from founder → high open rate + loyalty
Gift economy: Invite-only access as "gift" to early users
Personalized note: Handwritten or clearly personalized message in shipment
```

**Reciprocity in virality**:
> Give users something worth sharing → they feel obligated to share

**Design principles**:
- Give before you ask; always establish value first
- Make the gift visible and attributed ("This is my gift to you personally")
- Personalization increases obligation 2-3×
- Mitigation: Make it clear gifts are freely given, no obligation required

---

## SD-03 · Commitment & Consistency
**Tier**: 核心
**Evidence**: B — Freedman & Fraser 1966 登门槛实验（先答应小请求者后续答应大请求约 52.8%，直接请求约 22.2%）为经典证据；Burger 1999 元分析认为登门槛效应可靠但量级中等。争议：①原始研究样本小、单情境，登门槛在后续复制中不稳定，Doliński 2016 综述指出它仅对亲社会请求稳健，对商业请求（尤其第二请求与原请求主题不同时）经常失败；②"一致性驱动"与"自我知觉理论"（Bem）对同一现象给出不同解释，机制归属未定；③低球技术与承诺升级的现场证据多来自小样本观察而非受控实验；④承诺一旦被用户识别为被设计出来的，可通过"我那时不了解情况"解除
**Effect**: 中等偏大，仅在承诺是自愿、公开、且被用户归因为自主选择时成立；被迫或明显诱导的承诺不产生一致性压力，反而为事后反悔提供理由
**机制链**: 做出一个低成本、可自主选择的表态或行为 → 该表态被纳入自我概念，与后续不一致会产生认知失调与形象风险 → 为维持自我一致而接受更大请求，或自行加码投入
**剂量**: 弱 让用户在无压力下做一个二选一的偏好表态（"你更在意速度还是完整度"） ；中 把表态公开化，并在下一次请求中显式引用（"你选的是完整度，这一步要多 5 分钟"） ；强 公开承诺 + 可见进度 + 同伴见证（"你在群里说过这周要完成"），使不一致具备社会成本 ；过载 在用户尚未形成真实偏好的阶段逼出公开承诺，或反复用"你说过…"追债 → 承诺被重估为被套话，用户以否认先前表态、注销或公开反悔恢复自主感，一致性压力反向成为离开的动力
**时间动态**: 起效 分钟级（单次表态即可改变随后的选择） · 衰减 约束力随未兑现次数递减，第 2–3 次未兑现后自我概念被改写为"我不是那种人"，机制彻底失效 · 饱和 长期靠引用旧承诺驱动的产品被重新归类为道德绑架，触达打开率与留存同时下滑
**调节变量**: 个体 自我监控高、自尊稳定性低的用户一致性压力更大；高自主需求（SDT 自主维度）用户对任何被设计的承诺最敏感 · 文化 集体主义与面子文化中公开承诺的社会成本更高、效应更强，但公开反悔的修复成本也更高，容易转为沉默退出 · 情境 承诺内容与用户真实目标一致时效应稳定；承诺在时间压力、信息不足或激励诱导下做出时，效应反转为合理化抵抗
**失效信号**: 用户在第二次请求时明确表示"我当时只是随便点的"；引用旧承诺的触达打开率低于常规触达；已承诺用户在下一步的转化率不高于未承诺用户；出现公开撤回（删帖、退群、发帖吐槽"被绑架"）
**可测代理**: 表态组 vs 无表态组的下一步完成率差；引用先前承诺 vs 不引用的响应率；承诺后 7/14/30 天的兑现率与流失率；"否认先前表态"类客服工单占比
**交互**: × HB-08 沉没成本 → 承诺叠加已投入量后退出成本指数上升，构成 COMBO-03 的升级阶梯，但阶梯越长越需要真实价值支撑（COMBO-03）；× MR-06 伪进度 → 预填进度让用户在尚未投入时先感到"已开始"，与承诺共同构成 COMBO-11 的启动动量（COMBO-11）；× MR-04 身份承诺 → 承诺被反复行为证据加固后升格为身份，进入 COMBO-12 的不可逆区（COMBO-12）
**边界**: 不得对未成年人、认知障碍者或在强诱导（限时、抽奖、返现）下取得的承诺作为后续索取依据；已撤回的同意不得继续当作承诺引用（《个人信息保护法》第十四条的撤回权）；信贷、保险、医疗等高利害决策中的承诺设计须留无条件冷静期

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.91；Effect Size: Large

**Mechanism**: Once people make a commitment (especially public or written), they feel psychological pressure to be consistent with that position. Small commitments create the foundation for larger ones (foot-in-the-door).

**Commitment escalation ladder**:
```
Micro-commitment (cognitive) → Small behavioral commitment →
Public commitment → Social commitment → Identity commitment
```

**Implementation**:
```
Onboarding: "What's your #1 goal?" → answer → now they're committed to that goal
Public pledge: "Share your commitment to X with friends" → social accountability
Step 1 of onboarding → commits to completing → sunk cost builds
Waitlists: Signing up = micro-commitment → primes for purchase
Quiz: "Based on your answers, you're a [type]" → identity commitment
Goals: "You set a goal to do X by [date]" → reminder = consistency trigger
Community: Public statement of intent in group chat → peer accountability
```

**The foot-in-the-door technique**:
1. Ask for tiny favor (share email, answer 1 question, like post)
2. Follow up with larger request
3. Conversion rate 2-3× higher than direct ask

**Design principles**:
- Make early commitments easy and low-cost
- Make commitments public whenever possible
- Reference prior commitments when asking for next step
- Mitigation: Allow easy withdrawal; never lock users into commitments they regret

---

## SD-04 · Authority Bias
**Tier**: 常用
**Evidence**: B — Milgram 1963 服从实验（基线条件下约 65% 被试施加到最高档电压）是该机制最强的实验室证据；Burger 2009 部分复制在 150V 处得到相近服从率。争议：①Milgram 的数据完整性与被试事后伤害长期存在方法学争议（Perry 的档案研究），且"盲目服从权威"被社会认同路径（Reicher & Haslam）重新解释为"认同实验者的科学目的"；②商业场景中权威线索（白大褂、机构 logo、头衔）的现场效应远小于实验室，在高动机审查下迅速失效；③权威信号与真实专业性可分离，用户越来越多地把头衔读作营销而非能力；④虚构权威属虚假宣传，法律暴露明确
**Effect**: 中等偏大，仅在用户缺乏领域知识且无核验路径时成立；一旦用户具备专业知识或可查证渠道，头衔与标识的说服力接近零，且虚假权威造成不对称的信任崩塌
**机制链**: 出现专业身份、机构标识或确定性语言等权威线索 → 用户以"谁在说"替代"说了什么"作为正确性捷径，降低对内容的独立评估 → 在未核验内容的情况下接受结论或执行指令
**剂量**: 弱 展示真实资质、执业编号或可点开的履历 ；中 在结论旁标注权威来源的具体依据（研究名、样本量、年份）并给出原文链接 ；强 权威线索与具体、可核验的专业判断绑定，并由第三方平台背书（同行评审、监管备案） ；过载 堆叠不可核验的头衔、机构 logo、白大褂形象与"专家一致认为"式表述 → 被识别为权威表演，用户转向反权威启发式，连真实资质也被折价，同时构成虚假宣传风险
**时间动态**: 起效 秒级（首屏权威线索在阅读内容之前改变可信度初值） · 衰减 同一权威线索在第 3–5 次曝光后进入盲视区，用户不再注意资质模块 · 饱和 当所有竞品都堆同一批 logo 与头衔时，权威信号失去区分度，只剩核验成本与合规风险
**调节变量**: 个体 领域知识越少、时间压力越大，权威依赖越强；高专业度与高怀疑特质用户先查来源，效应近乎消失 · 文化 高权力距离文化（东亚、拉美）中头衔与机构层级影响更强；低权力距离、高反权威文化中过度权威化引起反感 · 情境 高风险、不可验证、需快速决策时效应最大；可试用、可退换、结果可自证的场景中权威被体验证据取代
**失效信号**: 资质模块的点击/展开率持续下降而页面其他模块稳定；用户在评论或社交平台核对并指出头衔不实；"专家推荐"类文案的 A/B 差异不再显著；投诉与监管问询中出现"冒充专家/虚假背书"表述
**可测代理**: 带资质 vs 不带资质的转化差与停留差；资质模块展开率与展开后的转化提升；引用具体研究 vs 笼统"研究表明"的响应差；资质核验类客服工单数量
**交互**: × SD-01 社会证明 → 权威为同伴行为提供"专业人士也这么做"的合法性，二者与加工流畅性叠加构成 COMBO-06 的信任瀑布，三层独立路径使信任极难被单点证据推翻（COMBO-06）；× PA-01 加工流畅性 → 权威线索让用户停止加工内容，流畅性让内容不必被加工，两者共同压低核验意愿，是该组合最危险之处；× HB-05 框架效应 → 权威把"专家立场"变成默认解释框架，用户不再生成替代解释
**边界**: 不得虚构资质、机构隶属、研究成果或"专家共识"（《反不正当竞争法》第八条虚假宣传、《广告法》第二十八条虚假广告）；医疗、法律、金融建议须由持证主体出具并对个体情况负责，权威线索不得替代个体化评估；不得利用权威对处于依赖状态的人群（患者、债务人、求职者）施加服从压力

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Large

**Mechanism**: People defer to authority figures or credential signals, often without evaluating the actual content. Authority can be real or symbolic.

**Authority signals** (strongest to weakest):
- Official credentials (Dr., PhD, "Harvard")
- Social proof of expertise (# of followers, published work)
- Physical/design signals (professional photo, quality design)
- Association signals (endorsed by X brand)
- Linguistic signals (confident, specific language)

**Implementation**:
```
Testimonials: Use job titles and companies, not just names
Case studies: "Used by [Fortune 500 company]" adds authority transfer
Content: "Research shows..." / "According to studies..." increases compliance
Design: High-quality visuals signal authority before content is read
Trust signals: SSL badges, press logos, partner logos
Credentials: Display certifications, awards, press features prominently
Author bio: Show expertise before asking for behavior change
Language: Specific numbers ("83% of users") > vague claims ("most users")
```

---

## SD-06 · Network Effects
**Tier**: 常用
**Evidence**: B — 理论基础为 Katz & Shapiro 1985 的网络外部性与正反馈定价；直接网络效应在通信与协作类产品上有较强实证（同一网络内用户增长与留存正相关）。争议：①"价值随用户数超线性增长"（Metcalfe 定律）是启发式而非实测规律，Briscoe、Odlyzko & Tilly 2006 与 Odlyzko & Tilly 2005 指出实际价值增长慢于 n²，甚至接近 n log n；②大量被宣称为网络效应的增长其实来自病毒系数、规模经济或转换成本，三者常被混为一谈；③临界质量的阈值缺乏可迁移数值，品类间差异极大；④低质量增长会使单边网络效应反转为负（噪音、垃圾内容、供需失衡）
**Effect**: 大，但仅对"每新增一个用户都直接提升其他用户体验"的产品成立（通信、协作、双边市场）；工具类与内容消费类产品中用户数与个体价值几乎无关，此时宣称网络效应属归类错误
**机制链**: 用户数量或互补供给增加 → 每个用户可连接的对象与可获得的互补品变多，转换到更小网络的预期损失上升 → 增长自我强化，同时把用户锁定在既有网络
**剂量**: 弱 展示网络规模与同侪在场（"你的 12 位同事已加入"） ；中 在地理或人群上制造真实密度（先做透一个城市、一所学校、一个行业） ；强 补贴一侧以形成双边密度，并把跨边互动做成产品主路径（"在这里才找得到对方"） ；过载 用虚假密度（机器人、灌水内容、伪造"本地用户"）或强制导入通讯录填补临界质量 → 密度被识破后网络价值预期崩塌，用户把平台重新归类为空的，负口碑以同样速度传播
**时间动态**: 起效 周级至月级（密度需达到同侪可感知的阈值才起效，单次曝光无效） · 衰减 密度不增长时价值感按月衰减，用户开始把"没人"当作主要抱怨 · 饱和 达到临界质量后增长转为口碑与锁定驱动，新增用户的边际价值下降，机制从增长引擎变为防守壁垒
**调节变量**: 个体 社交需求强度与所在地理/行业集中度决定感知密度；独狼型用户与工具型需求者对网络规模不敏感 · 文化 关系密集型文化中"同侪已在"权重极高；弱关系文化更看重功能本身 · 情境 双边市场与协作工具效应强；单人可完成的任务、隐私敏感场景（医疗、金融）中网络效应被主动限制
**失效信号**: 新用户首周留存与"好友/同事数"的相关性消失；"这里没人/内容太少"成为流失原因的首位表述；补贴停止后跨边互动量断崖式下跌；DAU 增长而人均互动数下降（密度被稀释）
**可测代理**: 新用户 7 日留存对其连接数/同侪在场数的回归斜率；双边市场中供给侧密度与需求侧复购的相关；补贴退坡后的互动留存曲线；同城或同行业子网络密度与该子网络 NPS 的关系
**交互**: × SD-02 互惠规范 → 密度未达阈值时靠互惠义务先留人，密度达标后由网络价值接管，是 COMBO-10 与 COMBO-17 的接力机制（COMBO-10 / COMBO-17）；× SD-14 地位信号 → 网络价值转化为可显示的地位，早期贡献者获得早到者优势，是飞轮第一阶段的燃料（COMBO-17）；× SD-10 FOMO → 网络价值真实存在时 FOMO 是自然结果，价值不存在时 FOMO 只制造即刻流失
**边界**: 不得以虚假密度、机器人账号或伪造"本地用户"制造临界质量（构成虚假宣传与数据造假）；医疗、金融与未成年人社交产品中网络效应与同伴压力叠加，须限制可见的社交图谱；以网络效应构建的转换成本若被用于排除竞争，会触及滥用市场支配地位审查

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.93；Effect Size: Very Large

**Mechanism**: Product value increases super-linearly with user count. At critical mass, growth becomes self-sustaining. Below critical mass, products fail regardless of quality.

**Types**:
1. **Direct network effects**: Value = f(number of users) — messaging apps, social networks
2. **Indirect network effects**: Value from complementary goods — platforms, marketplaces
3. **Data network effects**: More users → better AI/recommendations → more users

**Critical mass tactics**:
```
Geographically constrain launch (Uber city by city)
Target a specific community first (Facebook → Harvard → colleges)
Create artificial density (show "local" users even if sparse)
Subsidize one side of marketplace (Uber subsidized drivers first)
Seed with known users (show friends who are on platform)
```

**Design principles**:
- Make the network visible ("X of your friends use this")
- Reward users for bringing others into the network
- Show the user what they're missing by not having their network on platform

---

## SD-10 · FOMO (Social Scarcity Composite)
**Tier**: 常用
**Evidence**: C — 这是复合构造而非单一机制。现有测量工具是 Przybylski et al. 2013 的 10 项 FoMO 量表，证据以自评量表与横断面相关为主（FoMO 与问题性社交媒体使用、错失焦虑相关），缺少能把它与损失厌恶、稀缺、社会比较分离的现场实验，"FOMO 驱动购买"的因果链基本未被实验证明。争议：①量表条目与神经质、归属需求高度重叠，构念效度受质疑；②营销文献把 FOMO 当作既有组合（社会证明 × 损失厌恶 × 稀缺）的别名而非独立机制，本记录沿用这一归类并明确标注；③现场"限时/限量"效果可被稀缺与时间折扣单独解释，无需引入 FOMO。标注为 C 类：理论构造 + 相关性证据
**Effect**: 中等，且几乎全部效应可归因于其组成成分；只有当"同伴参与可见 + 体验被判定有价值 + 窗口被判定关闭"三者同时成立时才出现独立于成分的增量，缺任一项即退化为其成分机制的普通强度
**机制链**: 看到同伴正在经历某种可欲体验 → 把"未参与"解读为社交位置与体验的双重损失，并伴随对窗口关闭的预期 → 在未评估自身需求的情况下加入、购买或持续刷新以消除落差
**剂量**: 弱 展示同伴的真实参与（"你的 3 位同事上周参加了"）而不施加时间压力 ；中 让参与可见且可比较，并披露真实窗口（"报名周三截止"） ；强 可见参与 + 真实稀缺 + 关闭后的可见后果（"未参加者的进度已落后一档"）三者同屏 ；过载 用不可核验的"人人都在"叙事叠加人造截止 → 用户识别为焦虑营销，反向以主动退出（关通知、退群、卸载）恢复控制感，且该反应在同侪间传染
**时间动态**: 起效 小时级（看到同伴动态后的一次会话内） · 衰减 单次错失叙事的焦虑在 1–3 天内消退，重复使用后用户主动关闭可见性（屏蔽动态、退出榜单） · 饱和 长期暴露导致错失疲劳，用户把平台内容整体降权，机制从拉新变为促退
**调节变量**: 个体 归属需求高、自尊不稳、社交焦虑高的用户反应最强，也最快出现回避行为；高自主动机用户对任何"人人都在"表述免疫 · 文化 集体主义与关系密集文化中"被落下"的社会成本更高、效应更强；个人主义市场对"错过体验"的敏感度高于"错过关系" · 情境 有真实窗口与真实同伴行为时成立；虚构窗口、无真实同伴参与、或用户已明确不关心该领域时效应为零甚至为负
**失效信号**: 通知关闭率与"屏蔽动态"使用率在 FOMO 触达后上升；同一错失叙事的打开率在第 2–3 次后快速衰减；用户公开发帖抱怨"制造焦虑"；参与率上升但 7 日留存下降（拉来的是被推着来的人）
**可测代理**: FOMO 触达组的参与率与 7/30 日留存对照；通知关闭率与触达强度的相关；错失叙事第 n 次曝光的打开率曲线；FoMO 量表高分/低分用户在同一触达下的响应差（用于检验异质性而非因果）
**交互**: × HB-02 损失厌恶 × HB-04 稀缺 → 三者互为担保构成 COMBO-01：社会证明让稀缺可信、稀缺让社会证明危险、损失框架把两者焊成紧迫（COMBO-01）；× SD-06 网络效应 → 真实网络价值使 FOMO 自然涌现，虚假密度使 FOMO 变成即刻流失的引信（COMBO-17）；× SD-15 社会比较 → 比较提供落差的度量、FOMO 提供落差的情绪，叠加时焦虑强度高于任一单独使用
**边界**: 不得制造虚假的同伴参与或虚假窗口（虚假宣传与误导性商业表述）；不得对未成年人及社交焦虑、抑郁倾向人群使用错失叙事（有证据关联问题性使用与情绪恶化）；健康、金融、教育场景中的 FOMO 会驱动非理性承诺，须替换为透明的可用性与真实截止

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.92；Effect Size: Large — this is a COMBO of SD-01 × HB-02 × HB-04

**Mechanism**: Fear of Missing Out = Loss Aversion applied to social exclusion. The pain of being left out of something your peers are experiencing. Most powerful viral mechanic.

**FOMO architecture**:
```
1. Show peers engaging in desirable activity
2. Make activity look effortless and rewarding
3. Create visible in-group / out-group boundary
4. Add time pressure (you can join NOW, but window closes)
5. Show what in-group members get that out-group doesn't
```

**Implementation**:
```
Streaks: "Your friends maintained their streaks. You broke yours."
Groups: "Your team completed the challenge. You're the only one who didn't."
Events: "17 people from your network attended [event] last week"
Products: "Your colleagues are using [feature] you haven't tried"
Content: "Everyone is talking about X — here's what you're missing"
Exclusive: "Members got early access to X. Non-members didn't."
```

**Virality formula**:
> FOMO = (Visibility of peer participation) × (Desirability of experience) × (Perception of exclusivity)

---

## SD-14 · Status Signaling
**Tier**: 常用
**Evidence**: B — 理论根基为 Veblen 1899 的炫耀性消费与 Zahavi 1975 的代价信号理论；实证上可见性商品的消费随相对收入上升（Charles, Hurst & Roussanov 2009），地位动机会改变产品偏好（Nelissen & Meijers 2011、Anderson et al. 2015 的地位商品实验）。争议：①解释力高度依赖"观众可识别信号"这一前提，私密场景中效应大幅缩小；②产品内的徽章与榜单有反向证据：Hanus & Fox 2015 的学期级研究发现徽章与排行榜降低了内在动机与满意度；③过度使用触发地位通胀，信号贬值速度快于获取速度；④排他性等级在未成年人产品中与社交排斥风险直接相关
**Effect**: 大，但仅在信号"公开可见 + 稀缺可辨 + 观众在意该维度"时成立；私密场景或观众不共享该评价维度时，地位信号退化为纯粹的收集行为
**机制链**: 出现一个公开可见、获取有代价的地位标记 → 该标记被观众读作能力、投入或归属的可信证据，持有者获得相对位置收益 → 为维持或提升相对位置而持续投入（付费、产出、拉新）
**剂量**: 弱 展示可选的、非排他的进度标记（完成度、年限） ；中 建立多维度、可达成的等级与可见的贡献记录，让多数人拥有某种地位 ；强 让地位与稀缺资源绑定（专属房间、优先权、可外显的成就）并把排名公开化 ；过载 把一切行为都徽章化、给所有人发同级标记、或让排名成为唯一可见维度 → 地位通胀使信号失去区分度，低排名用户以退出或降低投入回应，社区整体产出下降
**时间动态**: 起效 天级（获得标记后的展示行为在数日内出现） · 衰减 同一标记的展示价值在数周至数月内被新标记稀释，用户要求更高阶标记 · 饱和 等级体系扩张到人人有份时地位收益归零，只余维护成本与排名带来的负面情绪
**调节变量**: 个体 地位需求（社会支配倾向、自尊不稳）高的用户投入最强；内在动机主导的用户会被外部标记挤出（过度理由效应） · 文化 高权力距离与面子文化中可见地位的收益更大、失去地位的成本更高；平等主义文化中过度等级化引起反感 · 情境 有真实观众与共享评价维度时成立；私密工具、团队内部协作、结果不可外显的场景中效应接近于零
**失效信号**: 高阶标记获取率上升而低阶标记展示率下降（信号贬值）；排行榜中位以下用户的活跃度与留存显著低于无排行榜对照；社区出现"徽章没用/刷分"类公开讨论；为地位付费的用户续费率低于为功能付费的用户
**可测代理**: 有/无排行榜或徽章分组的留存与产出差（按分位段分层）；同一标记在第 1/4/12 周的展示率衰减曲线；地位型付费与功能型付费的续费率对比；低分位用户退出率
**交互**: × SD-02 互惠规范 → 可见的给予既产生义务又产生地位，是 COMBO-10 中"贡献→地位→更多贡献"的闭环（COMBO-10）；× SD-06 网络效应 → 早到者优势把网络密度转化为地位稀缺性，构成 COMBO-17 的启动燃料（COMBO-17）；× SD-15 社会比较 → 比较提供地位的度量尺，叠加时中位以下用户承受的负效用最大，须靠多维度设计分散
**边界**: 付费即得的地位标记若不披露，会摧毁信号的代价真实性并把地位变成明码标价的商品；未成年人产品中不得使用公开排名与排他性等级（社交排斥与自尊风险）；不得把地位与实质性权利（数据访问、服务优先级）捆绑到构成不公平待遇的程度

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Large

**Mechanism**: Humans are deeply wired for status within hierarchies. Visible status markers drive aspirational purchase and behavior independent of functional utility.

**Status mechanics in products**:
```
Levels/tiers: Gold/Platinum/Diamond member tiers
Badges/achievements: Visible to others in community
Leaderboards: Public ranking creates aspiration + competition
Exclusive access: "Pro member only" rooms/features
Customization: Profile items that signal investment/skill
Early adopter markers: "Member since 2019" = higher status
Top contributor: Community recognition programs
```

**Design principles**:
- Make status visible to others (meaningless if private)
- Create multiple status dimensions (not just top 1% — everyone can have some status)
- Allow users to display status in external contexts (badges, shareable achievements)

---

## SD-15 · Social Comparison
**Tier**: 常用
**Evidence**: B — Festinger 1954 的社会比较理论为核心框架，上行/下行比较的方向性效应由 Wills 1981 补充；社交媒体使用与主观幸福感的负相关在 Verduyn et al. 2017 综述与 Yoon et al. 2019 元分析中可复现，但量级小。争议：①相关研究难以分离选择效应（不幸福的人更多比较）与因果效应，纵向与实验证据远少于横断面证据；②"稍微高于平均的目标最有激励性"这一设计原则主要是实践推断，缺少剂量化的实验证据，个体差异极大；③上行比较既可激励也可引发挫败，方向取决于可达成性与领域重要性，未控制这两点时文献结论互相矛盾
**Effect**: 中等且方向依可达成性而定：差距被判定为可缩小（约 10–20% 以内、路径清晰）时提升投入，被判定为不可缩小时转为挫败与退出；无对照组的绝对反馈不产生比较效应
**机制链**: 出现与自身相近的他人的表现信息 → 用户以该信息为标尺评估自身能力与位置，产生上行（差距）或下行（优势）判断 → 依差距的可达成性调整投入：差距可缩小则加码，差距过大则降低目标或退出
**剂量**: 弱 提供不含他人的绝对进度（"你完成了 6/10"） ；中 提供同起点队列的分位信息（"同周开始的人里你在前 30%"）并给出下一步差距 ；强 显示紧邻上一位的具体差距与可执行路径（"再完成 2 项即可超过第 12 名"） ；过载 显示遥不可及的头部标杆并把排名作为唯一反馈 → 用户把差距判定为结构性不可缩小，出现无助、降低目标或直接退出，且该反应在同侪间传染
**时间动态**: 起效 分钟级（看到比较信息后的一次会话内改变努力或退出意图） · 衰减 同一分位信息的激励效果在 2–4 次重复后衰减，用户对"你超过了 X%"脱敏 · 饱和 长期暴露于固定排名导致中位以下用户把目标内化下调（"我就这样"），机制对留存转为负贡献
**调节变量**: 个体 社会比较倾向（INCOM 量表）高的用户反应最强；自尊稳定者上行比较偏激励，低自尊者偏威胁 · 文化 集体主义与关系文化中比较对象以熟人同侪为主，效应更强更持久；个人主义市场对陌生头部标杆的敏感度较低 · 情境 同起点、同任务、可比口径时效应成立；口径不可比（不同难度、不同资源）时比较信息被判定为不公平，产生反向抵触
**失效信号**: 中位以下用户收到分位信息后的次周活跃度低于未收到组；"排名/对比"模块展开率下降而绝对进度模块上升；出现"跟我比没意义/口径不一样"类公开质疑；比较触达后退出率上升而短期完成率也上升（榨取式激励）
**可测代理**: 分位信息组 vs 绝对进度组的次周留存与完成率差，按分位段分层；比较对象差距三档（5%/20%/200%）的投入变化；INCOM 高分与低分用户的分层响应；比较模块展开率随曝光次数的衰减
**交互**: × SD-14 地位信号 → 比较把静态地位变成动态竞赛，中位以下用户的负效用被放大，须与多维度地位设计配对；在地位驱动的飞轮里，比较正是把地位从标记变成竞赛的那一步；× SD-10 FOMO → 比较提供落差的度量、FOMO 提供落差的情绪，叠加后焦虑高于任一单独使用；× MR-01 目标梯度 → 当比较目标被折算成"还差 2 步"时，挫败被转成投入，这是唯一可安全放大的组合
**边界**: 不得用不可比口径（不同难度、不同资源投入）制造虚假差距（构成误导性对比）；不得向已知处于情绪困境的用户推送上行比较；未成年人产品中不得把公开分位排名作为主要反馈

**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.89；Effect Size: Large

**Mechanism**: People evaluate themselves relative to nearby peers. Upward comparison (looking at better performers) drives motivation. Downward comparison (looking at worse performers) drives satisfaction.

**Design principle**: Show users slightly-above-average comparison targets to drive motivation without inducing helplessness.

**Implementation**:
```
Leaderboards: Show top 10 + user's rank + person just above them
Progress: "You're ahead of 73% of users who started the same week"
Benchmarks: "Average user completes this in 3 days. You're on day 2."
Cohort: "Your cohort's average score is X. Yours is Y."
Asymmetric: Show the gap to close, not the gap from below
```

**Warning**: Upward comparison where the gap is too large → helplessness and abandonment.
Show "nearby achievable" comparisons, not aspirational/impossible ones.
