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
**可证伪条件**: 在可独立核验的场景（电商、自助选购）中随机呈现可归因的真实人数信号并控制价格与评价可得性，若社会证明组在 7 日转化上不显著高于无信号组，则本记录"三条件同时成立时可达实验室量级"的现场可用性不成立，应把 30–75% 顺从率明确限定为实验情境并删除其转化杠杆表述（实验室顺从率本身不受影响）。

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
**可证伪条件**: 在控制赠品价值与请求成本的现场试验中，把同一赠品分别标注为"无条件礼物"与"注册后领取"，若两组的顺从率无显著差异（附条件未被识别为交易前置），则本记录"一旦礼物被读作交易的前置步骤，顺从率回落到与直接请求无差异"不成立，须撤回该条件句并把互惠的适用边界改写为不受附条件披露影响。

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
**可证伪条件**: 在随机分配"自愿承诺"与"被诱导承诺（限时＋返现）"的现场试验中，若被诱导组后续的复购或升级率不显著低于自愿组（诱导不削弱一致性压力），则本记录"被迫或明显诱导的承诺不产生一致性压力，反而为事后反悔提供理由"不成立，应降级为"诱导承诺同样有效，只是不能作为合规同意的替代"并据此收紧边界中的冷静期表述。

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
**可证伪条件**: 在用户具备可查证渠道（比价、第三方评测、资质公开库）的条件下，若高权威标识仍显著提升遵从而不回落至噪声级，则本记录"一旦用户具备专业知识或可查证渠道，头衔与标识的说服力接近零"不成立，应把权威的作用域从"缺乏核验路径"改写为"核验成本可接受时仍部分有效"，并调整其与专业证据的替代关系表述。

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
**可证伪条件**: 在工具类与内容消费类产品中，若把"其他用户数／活跃度"随机披露给用户后其感知价值或留存显著上升，则本记录"用户数与个体价值几乎无关，宣称网络效应属归类错误"不成立，须把归类边界从品类改为"是否存在用户间直接的价值传递通道"，并撤回按品类一刀切的判断。

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
**可证伪条件**: 在分别操纵"同伴参与可见""体验价值""窗口关闭"三个成分的因子设计中，若三成分同时存在时的效应不显著高于各成分单独效应之和（无交互增量），则本记录"存在独立于成分的增量"一句不成立，FOMO 应降级为成分的别名、不得作为独立杠杆计入；若增量稳定出现，才应把 FOMO 从复合构造提升为可独立测量的机制。

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
**可证伪条件**: 在私密场景或观众不共享该评价维度的条件下，若公开可见的地位标记仍显著提升支付意愿与留存，则本记录"私密场景或观众不共享该评价维度时，地位信号退化为纯粹的收集行为"不成立，应撤回该条件句并把作用域改写为"地位可内生为自我信号、不依赖外部观众"。

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
**可证伪条件**: 分层随机呈现与用户基线的差距（5%／15%／30%／50%）并控制目标可达成性，若"提升投入"与"挫败退出"的转折不落在可缩小阈值附近（例如差距扩大时投入仍单调上升，或任何差距都导致退出），则本记录"约 10–20% 以内提升投入、被判定为不可缩小时转为挫败与退出"不成立，须删除该数值区间并把方向改写为完全由可达成性信念决定。

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

---

## SD-05 · Liking Principle
**Tier**: 常用
**Evidence**: B — 相似—吸引（similarity–attraction）是该族最稳的一环：Byrne 1971 的态度相似范式与 Montoya, Horton & Kirchner 2008 元分析（313 项研究）确认态度相似与喜欢的相关稳定在中等量级，且**感知相似**比**实际相似**预测力更强；互惠式喜欢（reciprocal liking，即知悉对方喜欢自己后好感上升）在多组独立实验中方向一致；Cialdini 把亲和、相似、恭维、熟悉与关联列为 liking 杠杆。争议：①**"喜欢这个人 → 喜欢他的产品"这一转移步证据明显更薄**：相似性操纵改的多是对人的评价，落到购买决策的实验少且效应量不稳定，现场研究（汽车销售、募捐）高度混淆了专业度与熟悉度；②恭维与模仿（mimicry）的效应在大型复制与元分析中被下调，且模仿只在未被察觉前有效，察觉后转为反感；③该机制与 SD-04 权威偏见共用"信源好感"通路，容易重复计量
**Effect**: 中等，仅在"先建立人际好感 + 好感可归因到具名的推荐者 + 无更硬的选择依据"时改变选择；一旦存在可核验的产品证据（规格、价格、独立评测）或可退换承诺，好感让位于证据，效应收缩到噪声级
**机制链**: 出现与自身态度或背景相似、或以互惠友好方式对待自己的信息源 → 相似性与互惠回报被读作"这人站在我这边"，从而抬高对该信源建议的接受阈值 → 在缺少硬证据时采纳其推荐，并把推荐错误归因于产品本身
**剂量**: 弱 展示推荐者与用户的共同点（同城、同行业、同工具栈），仅作背景信息 ；中 由真实可辨认的人给出个性化推荐，并在推荐中回应用户已表达的具体需求 ；强 先建立持续的、互惠的、可归因的关系（长期顾问、社群主理人）再推荐高不确定性商品 ；过载 批量伪造亲和（统一话术的"专属顾问"、无差别恭维、越界的模仿）→ 用户识别为套近乎脚本，好感反转为操纵感，并对该渠道此后所有推荐整体打折
**时间动态**: 起效 分钟级到会话级（一次互动即可抬高好感） · 衰减 单次恭维或相似性提示的好感在数天内消退，同一套话术在第 2–3 次后失效 · 饱和 长期把关系当杠杆用会耗竭关系本身，顾问与用户的关系转为纯交易性，推荐打开率与信任同步下降
**调节变量**: 个体 关系导向型（互依型自我建构、高亲和需求）用户反应最强；规避型依恋与高警觉用户对恭维和模仿出现反向反应 · 文化 集体主义与关系文化中"先关系后交易"是默认脚本，好感转移更强更持久；制度化、低信任市场里热情被读作销售压力 · 情境 高不确定性、高单价、难退换时好感权重上升；标准化可核验商品上好感几乎不起作用
**失效信号**: 推荐转化在"由真人推荐"与"由系统推荐"两组间的差异消失；用户公开复述"顾问话术一模一样"；顾问加好友率与回复率上升而成交率下降（关系在被动消耗）；退订理由中出现"感觉被套近乎""像在演"类表述
**可测代理**: 有/无真人推荐者分流的转化差，按单价分层；相似性提示（同城/同行业/同工具栈）三档的点击与转化；顾问加好友率与实际成单率的比值随生命周期变化；"话术雷同"类客诉提及率
**交互**: × SD-02 互惠规范 → 好感让回报义务看起来是自愿的而非交易条件，是 COMBO-06 信任级联的情感入口（COMBO-06）；× SD-04 权威偏见 → 亲和与专业度共享"信源可信"通路，叠加时信任上升最快、被揭穿时跌得也最快；× PA-01 加工流畅性 → 熟悉的脸与顺耳的话提高流畅感并被误读为"更可信"，但流畅性可被伪造，故该组合不可当作质量证据
**边界**: 不得伪造亲和（虚拟"专属顾问"、脚本化恭维、越界模仿）冒充真实关系，构成误导性商业宣传；心理治疗、医疗、法律咨询等受托关系中不得用相似性与恭维提升依从（削弱当事人的自主判断）；不得向已知孤单、丧亲或处于情绪危机的用户售卖"陪伴感"以促成高单价交易
**可证伪条件**: 在同时具备硬证据（规格、价格、独立评测、可退换承诺）的条件下，若具名推荐者的好感仍显著改变选择而不收缩到噪声级，则本记录"好感让位于证据、效应收缩到噪声级"不成立，应把亲和从"缺乏更硬依据时的替代品"改写为"独立于证据的偏好项"，并相应调整其与产品证据的计功顺序。

**Mechanism**: Liking is a shortcut for trust. When the source of a recommendation is liked — through similarity, familiarity, compliment, or cooperation toward a shared goal — the recommendation inherits credibility it never earned on its own merits.

**Design principles**:
- Build the relationship before the ask (rapport → recommendation, not recommendation → rapport)
- Prefer real, identifiable recommenders over a scripted persona
- Make similarity specific and true ("we both use X"); never fabricate it

**Anti-pattern**: Scaling rapport with templates. The moment the pattern is spotted, liking inverts into perceived manipulation and poisons every later recommendation from the same channel.

---

## SD-07 · Conformity Effect
**Tier**: 常用
**Evidence**: B — Asch 1951 线段判断实验（严格的无异议多数下约 37% 试次从众、75% 的被试至少从众一次）。**该数字有明确的年代与文化局限**：Bond & Smith 1996 元分析（133 项研究、17 国）确认效应跨文化可复制，但同时给出两个限定——顺从率自 1950 年代起在个人主义样本中随时间下降，且集体主义文化样本的顺从率显著高于个人主义样本。争议：①37% 出自"答案不可核验 + 多数即时在场 + 公开作答"的极端情境，把它当常量会高估数倍；②现代线上环境缺少"在场的多数"，匿名的日志式从众远弱于面对面；③多数派规模（1 对 2 对 3+ 票）的边际效应在 Asch 变体与后来复现中并不单调
**Effect**: 中等偏大，但仅在"答案不可核验 + 多数即时可见 + 公开表态有社会代价"三条件叠加时达到实验室量级；退出任一条件（私下作答、有客观标准、多数不在场）后效应降到个位数百分比
**机制链**: 处于不确定且需要公开表态的情境 → 感知到群体的一致规范，并预期偏离会付出社会代价 → 调整自己公开的判断或行为向多数靠拢，即使私人判断并未改变
**剂量**: 弱 展示匿名的聚合多数选择作为背景信息，并允许用户私下保留异议 ；中 显示多数选择，并让用户的表态对他人可见（点赞、署名评论） ；强 让偏离多数在社群内可被识别（实名反对、退出即失去席位），同时收窄异议通道 ；过载 把一致性强加到没有正确答案、且用户握有私人证据的判断上，或把异议者公开标记 → 触发 reactance 与自我一致需求，用户不但拒绝从众、还公开反对并把该群体读作胁迫源，少数派立场反而被强化
**时间动态**: 起效 秒级到分钟级（在场多数形成后一次表态内即可出现） · 衰减 同一规范提示在 2–4 次重复后钝化，用户学会在被抓到的可能成本低时不再跟从 · 饱和 长期强制一致会把合规变成表面行为（私下意见不变），规范失去内化，一旦监督消失行为立即回弹
**调节变量**: 个体 场依存型、高社会焦虑、低自信与高归属需求者从众更强；高认知需求与高自我效能者显著更弱 · 文化 Bond & Smith 1996：集体主义与高语境文化的顺从率显著高于个人主义样本，且后者自 1950 年代以来持续下降；更年轻、更城市化的样本更弱 · 情境 不确定 + 多数在场 + 公开表态 + 群体有归属价值时最强；有客观标准、匿名私下、或多数派被判定为利益相关方时效应大幅削弱
**失效信号**: 多数提示的点赞与转发上升，而反对与弃购集中出现在客服与匿名渠道（表面一致下的双轨行为）；一旦出现可见的少数派异议即被大量附议（被压制的规范一次性释放）；一致性提示模块的停留时长持续下降（被当作噪音略过）；隐私浏览或隐身模式使用率上升
**可测代理**: 公开表态组与匿名表态组的选项分布距离（总变差或 KS 统计量）；多数派规模 1/2/3+ 三档的从众率；出现"可见的少数派异议"之后的观点翻转率；隐身与匿名使用率对公开从众率的时间序列
**交互**: × SD-01 社会证明 → 社会证明提供"什么是正常的"这一信息，从众提供"偏离会不会被罚"这一压力，二者叠成 COMBO-04 社会证明级联（COMBO-04）；× SD-09 群体内外 → 当多数被界定为外群体时从众率下降甚至反转为对抗，这是多数压力最常见的反例来源；× SD-14 地位信号 → 从众的代价（放弃个人判断）与收益（保住地位）之比由地位系统决定，公开排名会放大收益端
**边界**: 不得伪造多数（虚构"87% 用户都…"，或反向筛选隐藏少数派意见），构成误导与信息操纵；政治、宗教、健康与财务决策中不得以群体一致性施压改变个人判断；未成年人产品中不得制造"只有你这样"的可识别偏离标记
**可证伪条件**: 在同时移除三个条件的对照条件中（私下作答＋有客观标准＋多数不在场），若顺从率仍维持在实验室量级而不降到个位数百分比，则本记录"退出任一条件后效应降到个位数百分比"不成立，应删除该量化断言并把条件依存改写为更弱的方向性表述。

**Mechanism**: Under uncertainty with no checkable answer, the group's answer becomes the answer — not because the individual is convinced, but because deviating is socially costly and the majority is treated as evidence.

**Design principles**:
- Show what peers actually do, not what they "should" do
- Keep a visible, safe channel for dissent
- Never manufacture the majority

**Anti-pattern**: Manufacturing consensus where the user holds private evidence to the contrary. Enforcement converts conformity into surface compliance, and surface compliance into open reactance.

---

## SD-08 · Bandwagon Effect
**Tier**: 常用
**Evidence**: B — 核心证据来自采纳动力学与羊群行为研究：Bikhchandani, Hirshleifer & Welch 1992 的信息级联模型与 Banerjee 1992 的羊群行为模型给出"从采纳量推断质量"的机制；技术采纳的 S 曲线与临界质量现象（Rogers 1962 扩散曲线、Bass 1969 模型）在现场数据中反复出现。争议：①**与 SD-07 从众常被混为一谈**，但两者不同层——从众是调整到感知规范，bandwagon 是从采纳量推断质量与预期收益；支持从众的实验室文献（Asch 系）并不支持后者，支持后者的多是市场聚合数据；②驱动 S 曲线的也可是降价、渠道铺设与真实网络效应，脱离这些因素单看采纳量会把供给端效应误读为心理效应；③"人气本身吸引人气"的经典实验（Milgram 街上仰望、舞厅实验）方法学薄弱且多完成于 1960–70 年代，现代受控复现有限
**Effect**: 中等，仅在"采纳量可见 + 用户无法独立判断质量 + 采纳量被读作预期收益的代理"时影响选择；当试错成本低（可免费试用、可退）或存在独立质量信号（第三方评测、开源）时，采纳量的边际影响很小
**机制链**: 观察到某选项的采纳量增长，或听到"多数人已加入"的声明 → 把采纳量当作质量的代理，据此抬高对预期收益的估计并预期他人会继续加入 → 选择该选项以对冲选错风险，使采纳量进一步自我实现
**剂量**: 弱 把累计采纳量作为静态事实展示（"已有 1 万团队使用"） ；中 展示增速与临界质量语义（"本周新增 2,000""正在接近多数"） ；强 把采纳量与竞争淘汰绑定（"行业标准""不用就落伍"）并在决策点实时显示 ；过载 让"人气"成为唯一证据来源，且采纳量可刷、可回购或无据可查 → 一旦被证伪（数据造假或体验与质量不匹配），信任以快于爬升的速度崩塌，并连带否定所有同类增长叙事
**时间动态**: 起效 天级到周级（采纳叙事需要一定的传播与可见度才成形） · 衰减 同一"增长"声明在数周后成为背景事实，不再改变判断，须不断刷新数字才能重新生效 · 饱和 采纳率接近上限或用户已全部加入时，bandwagon 失去信息价值，只剩维持规模的成本与"后来者发现来晚了"的落差
**调节变量**: 个体 不确定规避高、信息搜寻成本高、缺少先验知识的用户受影响最大；领域专家与有独立评测能力的用户几乎免疫 · 文化 高不确定性规避与集体主义文化中"别人都在用"的规范性权重更大；低信任市场中"涨得快"反而被读作炒作信号 · 情境 采纳量可见、试错成本高、切换成本高时最强；可免费试用或可一键退出的场景中显著减弱
**失效信号**: 被"快速增长"说服而来的用户其 7 日留存低于自然流量用户（买来的采纳不是真采纳）；增长数字不再被引用，数字文案的转化增益衰减到零；公开出现"数据是不是刷的"质疑帖；采纳量与实际使用量（活跃、续费）持续背离
**可测代理**: 展示"采纳量/增速"分流与对照组的试用→付费转化差；披露数字后第 1/7/30 日的留存差（区分真采纳与从众进入）；采纳量增速与实际活跃增速的比值（持续大于 1 即刷量信号）；三种"多数"表述（1 万用户 / 行业标准 / 即将淘汰）的转化阶梯
**交互**: × SD-01 社会证明 → 社会证明给的是"别人怎么选"，bandwagon 给的是"别人正在加入并会继续加入"，叠加是 COMBO-10 社区飞轮达到临界质量的推手（COMBO-10）；× HB-04 稀缺 → 人气与名额有限同屏时"怕错过"挤掉独立判断，是 COMBO-01 的核心组合（COMBO-01）；× SD-06 网络效应 → 真实网络效应会让采纳量自我实现，而虚假 bandwagon 只是模仿其曲线，两者在注册数据上难以区分，必须用留存而非注册量验证
**边界**: 不得编造或选择性披露采纳量（把未激活、免费、机器人算进"10 万用户"）以制造虚假人气，构成虚假宣传；金融、医疗、加密等高风险品类中"人人都在买"构成投资或治疗建议的实质误导，须禁止；不得把 bandwagon 与真实网络效应混同，作为定价或锁定的依据
**可证伪条件**: 在试错成本低（可免费试用、可退）或存在独立质量信号（第三方评测、开源）的条件下，若采纳量仍显著改变选择、其边际影响不小于高试错成本场景，则本记录"采纳量的边际影响很小"不成立，应把 bandwagon 的作用域改写为不依赖试错成本、只依赖采纳量是否被读作质量代理。

**Mechanism**: Adoption volume is read as a proxy for quality. "Everyone is joining" raises the expected payoff of joining, which raises adoption — a self-fulfilling loop that is genuine when driven by real network effects and hollow when only narrated.

**Design principles**:
- Disclose what the number counts (active, paying — not cumulative signups)
- Separate real adoption from narrated adoption in reporting
- Keep trial and exit cheap, so adoption keeps reflecting preference

**Anti-pattern**: Using the growth narrative as the only evidence. Once the number is falsified, trust falls faster than it climbed and takes every other growth claim with it.

---

## SD-09 · In-group/Out-group
**Tier**: 常用
**Evidence**: B — Tajfel et al. 1971 的最小群体范式（minimal group paradigm）显示仅凭任意分组（甚至掷硬币）就出现内群体偏爱，这一**内群体偏爱**部分在数百项复制中稳健（Balliet, Wu & De Dreu 2014 元分析确认资源分配中的内群体偏爱稳定存在、量级中等）；Brewer 1999 的综述论证"内群体爱"与"外群体恨"可分离。争议：①**外群体敌意与内群体偏爱并不对称**——元分析中内群体偏爱稳定为中等效应，而对外群体的主动伤害与贬低要弱得多，且高度依赖感知到的零和竞争或地位威胁（现实冲突理论所刻画的竞争条件），"分组即有仇恨"是过度外推；②最小群体范式本身的效应量近年被质疑受需求特征与分配任务形式影响；③实验室的掷硬币分组与真实的族群、政治身份差异极大，后者混淆了历史、资源与既得地位，二者不能互相外推
**Effect**: 中等且高度条件化：内群体偏爱在"资源分配 + 身份被激活"时稳定出现（中等效应量）；外群体贬低只在"感知到零和竞争或地位威胁"时出现，缺少该条件时通常只有冷淡与忽视而非敌意
**机制链**: 出现一个可被感知的身份边界（我们/他们） → 个体按该边界重新归类自己与他人，并把"我们"的成员纳入互惠与信任范围 → 在资源、信息与容忍度上向内群体倾斜，边界外同等需求被系统性低估
**剂量**: 弱 提供可选的社群标签与共享符号（队名、口号，由用户自选加入） ；中 在协作与资源分配中让内群体身份可见（同组优先互助、组内排行） ；强 让身份与稀缺资源或地位绑定，并引入组间竞争（对抗式榜单、晋级名额） ；过载 把身份边界做成对人不对事的道德分类，并奖励对外的贬低（"非我族类"的公开羞辱、举报奖励） → 内群体内部一致性上升但群体间协作瓦解，组织陷入派系对抗，人才与信息停止跨界流动，长期创新能力下降
**时间动态**: 起效 分钟级（一次分组或一次共享威胁即可激活） · 衰减 身份显著性在缺少持续激活（仪式、竞争、可见标记）时于数周内回落，日常跨界协作会稀释边界 · 饱和 身份被推到极致后出现反向疲劳：成员主动脱敏或以"反身份"姿态退出（去部落化），社群黏性下降
**调节变量**: 个体 社会支配倾向高、身份需要强（自我复杂性低）的用户内群体偏爱最强；自我复杂性高、跨群体友谊多者外群体偏见显著更低 · 文化 集体主义与关系本位文化中内群体义务更强、内外边界更清晰；个人主义市场中群体边界更松散，但会更快围绕兴趣重组 · 情境 存在零和资源竞争、地位威胁或外部威胁时外群体贬低出现；资源充裕、共同目标或交叉身份（cross-cutting identities）时效应转弱甚至消失
**失效信号**: 跨组协作请求的接受率相对组内请求骤降且差距随时间扩大；组内互助活跃而跨组信息共享停滞（网络上表现为内群体密度与模块度同步上升）；出现对外群体的去人化语言（"他们那种人"）并获大量赞同；跨界成员（同属两组者）流失或被迫公开选边
**可测代理**: 内/外群体的资源分配差（独裁者或信任博弈、或内部预算分配）；跨组与组内协作请求的接受率之比；社交网络模块度与内外边比随时间的变化；去人化语言在社区文本中的占比（固定词表或分类器）
**交互**: × SD-14 地位信号 → 身份把地位标记变成忠诚标记，离开的成本从"失去等级"升级为"背叛"，这是 COMBO-12 身份锁定栈的锁芯（COMBO-12）；× SD-15 社会比较 → 同一比较在身份边界内被读作正当竞争、跨边界被读作威胁，是内外反应分岔的放大器；× SD-02 互惠规范 → 互惠只覆盖边界内时，它从黏合剂变成排斥机制（对内慷慨、对外吝啬），须用交叉身份设计打断
**边界**: 不得以制造或强化群体对立作为参与度手段（对抗式设计在政治、族群、宗教维度上造成真实伤害与社会成本）；不得用伪造的内群体身份（"和你一样的用户群体"）进行定向说服；未成年人产品与心理健康场景中不得以群体归属威胁（"你将不再属于"）作为留存手段
**可证伪条件**: 在不存在感知零和竞争或地位威胁的对照条件下（如中立资源分配任务），若外群体贬低而非仅有冷淡仍稳定出现，则本记录"外群体贬低只在感知到零和竞争或地位威胁时出现"不成立，应把外群体敌意改写为不严格要求竞争条件，并重新评估内群体偏爱与外群体贬低的不对称性表述。

**Mechanism**: A nameable boundary between "us" and "them" reclassifies strangers into in-group and out-group, and generosity, trust and tolerance follow the boundary rather than the person's actual merit.

**Design principles**:
- Create cross-cutting identities so no single boundary aligns with every resource
- Reward collaboration across groups, not only within them
- Keep the boundary about shared practice, not about who people are

**Anti-pattern**: Engineering rivalry for engagement. In-group cohesion rises, cross-group cooperation collapses, and the organisation loses the information flow that made the groups useful.

---

## SD-12 · Betrayal Aversion
**Tier**: 情境
**Evidence**: B — 最强证据来自信任博弈与交换实验：Bohnet & Zeckhauser 2004 与 Bohnet et al. 2008（巴西、中国、阿曼、瑞士、土耳其、美国）显示，在"由人决定"的委托中人们比在期望值相同的"由随机决定"中显著更少信任，即对"被人背叛"这一事件本身存在额外负效用；Aimone & Houser 2012 的综述（Journal of Economic Surveys）确认该差值在多数实验中方向一致。（该文是对信任与背叛厌恶文献的综述性归纳，非新增元分析，故本记录不据此上调等级。）争议：①该效应在**决策层面**稳定，但"背叛厌恶是一种稳定可测的个体差异特质"这一更强说法证据薄弱——个体层面重测信度低，量表结果与博弈行为相关弱，多数研究只能测到情境层面的平均差；②跨文化设计差异很大（Bohnet et al. 2008 各国效应不同），说明它受制度与信任环境调节，而非个体常数；③现实中的"被背弃"反应难以与损失厌恶、地位受损和 SD-04 权威崩塌分离，单列为独立杠杆会重复计量
**Effect**: 中等，仅在"委托关系 + 收益取决于他人是否履约 + 背弃可被当事人识别"时压低信任与合作；一旦有合同、担保、第三方托管、可追偿机制或匿名随机化，效应大幅削弱
**机制链**: 面对一个收益取决于他人是否会履行承诺的委托 → 把"可能被背弃"与期望值相同的"可能运气不好"区分开，并对前者赋予额外负效用 → 减少委托、要求抵押或制度担保，宁可用较低期望值换取不被背弃
**剂量**: 弱 披露委托关系中的规则与追偿路径，让背弃有明确代价 ；中 加入第三方托管、分期交付或可验证的履约记录 ；强 让履约记录与身份、声誉长期绑定，并对背弃设置实际可执行的代价 ；过载 用高监控与重惩罚代替信任（每步留证、动辄追责） → 交易成本超过被背叛的预期损失，用户把关系读作敌对或"你预设我会骗你"，主动退出或只做最低限度披露，合作剩余被监控成本吃掉
**时间动态**: 起效 秒级到天级（面对委托条款时信任意愿在一次决策内改变） · 衰减 一次被背叛的记忆衰减很慢，远慢于一次被善待；同一方的重复守信可在数周至数月内逐步修复，修复速度取决于具体道歉与制度补偿而非曝光量 · 饱和 过量的保证条款与免责声明会让"信任"信号本身失去意义，反而提醒用户此事需要防备，转化与推荐意愿同时下降
**调节变量**: 个体 依恋焦虑与低一般信任者反应最强；信任倾向高、有成功委托经历者反应弱 · 文化 高信任社会与强合约执行环境下背叛厌恶的行为代价较小；低信任、以关系替代制度的社会中委托高度依赖人际保证，背叛厌恶更强更持久 · 情境 金额大、不可逆、对方匿名或一次性博弈时效应最大；有担保、可退、可追偿或重复博弈时显著削弱
**失效信号**: 用户在合同与托管功能上的停留和询价上升，但成交不涨（安全措施变成焦虑触发器）；客服与评论中"是不是要坑我""先看有没有人被骗"类预防性提问占比上升；老用户转介绍率下降而自购留存不变（信任只覆盖自己）；主动要求超额担保或以公司而非个人名义签署的比例上升
**可测代理**: 同一期望值下"由人决定"与"由随机或算法决定"分组的委托率差（信任博弈式 A/B）；有/无担保承诺分组的首单转化与客单价；被背弃后回访与复购的恢复曲线及其半衰期；同一用户两次测量的稳定性系数（检验它是否真是个体特质）
**交互**: × SD-04 权威偏见 → 背书型信任一旦被背弃，跌落的不是好感而是整套判断依据，这是 COMBO-06 信任级联的反向放大器（COMBO-06）；× HB-02 损失厌恶 → 背叛厌恶是损失厌恶在"因果归因于人"时的加权版本，两者叠加会把风险溢价推到超过客观期望差；× TR-06 信任修复 → 修复只能减少后续委托损耗，无法恢复到被背叛前对陌生人的基准信任，因此不能作为首次转化的杠杆
**边界**: 不得用"零风险""平台全额担保"等无法兑现的承诺降低背叛厌恶（虚假担保本身就是一次背叛，并触发合同欺诈与消费者保护的相应条款）；医疗、心理、法律等受托关系中不得以"信任我"替代知情同意与客观风险披露；不得在争议处理中利用用户的背叛厌恶逼其接受不利和解（结构上可能构成胁迫）
**可证伪条件**: 在加入合同、担保、第三方托管或匿名随机化之后，若用户的信任与合作水平仍显著低于无背叛风险的基线，则本记录"一旦有合同、担保、第三方托管、可追偿机制或匿名随机化，效应大幅削弱"不成立，应把背叛厌恶从"可被制度对冲"改写为"对制度承诺本身不敏感"，并据此修改争议处理设计的建议。

**Mechanism**: A payoff that depends on another person's word carries a disutility the same payoff under chance does not. People pay a premium — lower expected value, collateral, third-party escrow — specifically to avoid being betrayed, not merely to avoid a bad outcome.

**Design principles**:
- Make promises verifiable and breaches costly, instead of adding reassurance
- Use escrow, staged delivery, and reputation that outlives a single transaction
- Repair with institutional compensation and a specific admission, not with volume of apology

**Anti-pattern**: Replacing trust with surveillance. Every additional guarantee says "we expect you to cheat", and the cost of the monitoring exceeds the loss it prevents.

---

## SD-13 · Gossip / Signaling
**Tier**: 情境
**Evidence**: C — 理论根基扎实但受控证据薄，故按最低等级标注。代价信号理论（Zahavi 1975；Gintis, Smith & Bowles 2001）与间接互惠（Nowak & Sigmund 1998）给出"谈论他人即传递其声誉信息并为合作提供奖惩"的机制；Dunbar 1996 的社会性梳理假说与 Feinberg et al. 2012 的元分析支持 gossip 能改变第三方对目标者的评价与合作意愿。争议：①大部分传播与产品证据来自观察和访谈，"gossip 影响购买或推荐"的因果实验很少且样本小，效应容易被社会期许与实验者需求特征夸大；②gossip 的正负作用方向不一致——负面 gossip 提升规范遵从，但也降低整体信任与信息分享，Feinberg et al. 2012 与后续研究在"惩罚"还是"联结"上结论不一；③作为推荐机制它与 SD-01 社会证明、SD-14 地位信号高度重合，三者容易被当成三个独立杠杆重复计数。**可证伪条件**：在控制信息新鲜度与来源可信度后，若"推荐行为可被他人看到"对受荐者转化的提升不显著高于等价的匿名推荐，则 gossip/signaling 作为独立机制不成立
**Effect**: 小到中等，仅在"推荐行为对推荐者本人的声誉可见 + 受荐者能识别推荐者身份 + 推荐本身有成本"时成立；匿名或零成本推荐下效应退化为普通社会证明
**机制链**: 一个人公开谈论或推荐某个对象（产品、人、行为） → 该信息同时暴露被谈论者的声誉与谈论者自身的品味、立场和信息来源 → 双方及围观者据此调整对彼此的信任与地位判断，并倾向以能提升自己声誉的方式继续传播
**剂量**: 弱 提供可选的分享入口与"我推荐"标记，不显示任何传播效果 ；中 让推荐者身份与其推荐历史对受荐者可见（"来自你关注的人""他的推荐被 30 人采纳"） ；强 让推荐与推荐者的声誉账户挂钩（贡献榜、口碑等级）并提供可见的传播链路 ；过载 把一切互动都变成可被围观和排名的公共表态，并奖励对他人（含竞品或异见者）的负面谈论 → 社群从信息交换转为声誉博弈：人们只做安全表演、真实信息下沉，诽谤与拉踩成本极低而收益可见，信任与信息多样性同时崩塌
**时间动态**: 起效 小时级到天级（一次公开推荐即可被围观并影响他人判断） · 衰减 同一人的重复推荐在社群内边际可信度快速下降（"他什么都推"），半衰期以推荐次数计而非以时间计 · 饱和 当每个用户都在推荐、推荐本身失去筛选价值时，声誉信号变成噪音，社区回到只信熟人直接经验的状态
**调节变量**: 个体 高自我监控与高地位需求者更在意推荐对自己声誉的影响，因而更谨慎，也更愿意推荐能给脸上贴金的品类；低自我监控者更接近真实偏好 · 文化 关系与面子文化中"议论他人"的信息权重高、传播快，但也更易触发为维护和谐而沉默；低语境、弱关系社会里推荐更依赖平台化评分而非人际议论 · 情境 小群体、高重复互动、声誉可长期积累时效应最强；大而匿名、一次性互动的场景中接近于零
**失效信号**: 公开推荐量上升但受荐者留存不升（推荐变成社交货币而非质量信号）；社区文本中负面提及与拉踩占比上升而原创信息分享下降；高声誉用户的推荐频次骤降（爱惜羽毛而退出公共表态）；推荐采纳者对推荐者的后续关注转为审判（"你居然推这个"）
**可测代理**: 署名推荐与匿名推荐分组对受荐者转化的差；推荐者声誉分与其推荐被采纳率的秩相关；同一推荐者第 1/3/5 次推荐的可信度衰减曲线；社区文本中负面提及占比与原创分享占比的比值变化
**交互**: × SD-14 地位信号 → 推荐成为地位展示，传的是推荐者的品味而非产品信息，这是 COMBO-16 内容病毒化栈的传播层（COMBO-16）；× SD-02 互惠规范 → 议论与推荐同时是给予与索取，一旦与声誉绑定，互惠从义务变成可积累的资产，构成 COMBO-17 社区飞轮栈的规范执行机制（COMBO-17）；× SD-01 社会证明 → 署名推荐比匿名聚合更有信息量（可归因），但一旦被识别为营销，反噬也更强
**边界**: 不得设计或激励针对特定个人的负面谈论与公开羞辱（诽谤与人格权风险，涉及名誉权与个人信息保护的相应条款）；不得用"曝光"威胁推动用户评价或复购；推荐链路中的利益关系（佣金、返现）必须披露，否则构成隐性广告；心理脆弱人群与未成年人社群中不得用声誉排名驱动相互监视
**可证伪条件**: 在控制信息新鲜度与来源可信度后，若"推荐行为可被他人看到"对受荐者转化的提升不显著高于等价的匿名推荐，则 gossip／signaling 作为独立机制不成立，应删除其独立杠杆的计数并归入 SD-01 社会证明；反之若该提升在预注册复制中稳定出现，才可把本记录由 C 升为 B 并保留"声誉可见性"这一必要条件。

**Mechanism**: Talking about people and recommending things is a costly signal: it exposes the speaker's taste, judgement and loyalties to third parties. The content travels; the speaker's reputation travels with it.

**Design principles**:
- Make the recommender attributable, so the signal actually carries information
- Tie recommendation to a reputation that decays when the recommendation becomes indiscriminate
- Disclose commission and affiliation, or the signal is a lie

**Anti-pattern**: Engineering the community into a reputation game. Public performance crowds out honest information, and negative talk about others becomes the cheapest way to gain standing.
