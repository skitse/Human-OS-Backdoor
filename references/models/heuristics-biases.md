# Heuristics & Biases — Model Details

## HB-01 · Anchoring Effect
**Tier**: 核心
**Evidence**: B — Tversky & Kahneman 1974 的转盘实验为原始证据；Wegener, Petty, Blankenship & Detweiler-Bedell 2010 的综述给出中等效应。争议与边界：Critcher & Gilovich 2008 证明"附带锚"（与判断对象无关的数字）只在判断者没有理由折扣它时才移动估计——一旦锚的无关性被提示或判断者有动机核算，效应大幅衰减；且真实定价/薪酬谈判的现场实验效应远小于课堂演示，锚定被高估的部分主要来自实验室的低利害与不可核实设定
**Effect**: 中等；仅在锚值可信、决策者对该量级无内部先验、且无从外部核价时明显；领域专家或锚值明显荒谬时效应接近零

**机制链**: 先出现的数值被编码为该量的参照点 → 调整从锚点起步且过早停止（同时锚点启动与之一致的语义信息） → 估计值向锚点偏移
**剂量**: 弱 在用户形成价格预期前展示一个高位行业参照（"同类平均 $X"），不施加任何压力 ；中 价目表按降序排列 + 划线原价 + 用户首次接触该品类 ；强 高价锚 + 诱饵档 + 单位化框架同时出现，且决策时限紧、无可比价渠道 ；过载 锚值离合理区间太远（$9999/月）或与产品明显不符 → 被判定为钓鱼价，锚点被整体折价，用户转向外部比价，转化率低于无锚对照组
**时间动态**: 起效 秒级（单次暴露即改变估计） · 衰减 同一用户重复见到同类锚点后折扣，约 3–5 次触达后锚点被归类为"页面装饰" · 饱和 用户建立品类内部价格模型后，锚点不再移动估计，只影响对卖家的信任评价
**调节变量**: 个体 领域知识越高锚定越弱（专家有内部参考价），认知需求低与时间压力大者更强 · 文化 高不确定性规避市场更依赖外部锚，"原价"标签的可信度权重更高 · 情境 不确定 + 高时间压力 + 首次决策时最强，锚值可被第三方核实时最弱
**失效信号**: 用户在评论或客服里贴出第三方比价截图并质疑划线价；"原价"标签的点击热区异常高（用户在核验而非浏览）；加购后放弃率随锚点幅度上升而非下降；广告点击率上升但成交客单价下滑（吸引的是折扣猎手）
**可测代理**: 同页 A/B 锚值高低两组的选中档位分布与成交客单价；"原价"标签曝光到比价插件触发的比率；加购→支付转化率对锚点幅度的斜率（正斜率=有效，负=已过载）
**交互**: × HB-11 诱饵效应 → 高价锚提供量级坐标、诱饵提供支配关系，两者联合把目标档定义成"唯一理性解"（COMBO-08）；× HB-05 框架效应 → 锚定决定量级、框架决定单位，"$2.6/天"因此既小又相对便宜（COMBO-08）；× HB-02 损失厌恶 → 划线原价把"省下的钱"变成已持有资产，锚点被转写为损失框架
**边界**: 不得使用虚构原价（中国《价格法》与《禁止价格欺诈行为的规定》、欧盟 Omnibus 指令均要求"原价"为真实近期成交价）；医疗方案、贷款、保险等高利害决策中锚定会诱发系统性误配，须改为区间披露加独立估算工具；锚点一旦被用户公开证伪，修复成本高于该页全部历史收益
**可证伪条件**: 若在锚值可被第三方核实、判断者对该品类有内部价格模型的分组中，高价锚组的档位选择与成交客单价不显著高于无锚对照组，则“锚定可移动真实支付意愿”的声称不成立，本记录应降级为“锚定只移动无先验量级的估计值，不移动成交”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.92；Effect Size: Large

**Mechanism**: First numerical value encountered sets a reference point. All subsequent judgments are adjusted from this anchor — but insufficiently (adjustment is sticky).

**Cognitive chain**: Anchor exposure → selective accessibility of anchor-consistent info → insufficient adjustment → biased estimate

**Implementation**:
```
Pricing: Show highest tier first. After $999/month, $99 feels cheap.
Negotiation: Open high. The midpoint people settle on is anchored by your opening.
Donation: Show $500 as suggested, then $50 feels small but acceptable.
Ratings: Show product at "Was $299, Now $89" — $299 is the anchor.
Progress: Show "300 people have already done X" before asking user to do X.
```

**Design principles**:
- Optimization: Always introduce your desired reference point before presenting the actual offer
- Anchor with social numbers: "10,000 users rated this 4.8 stars" before asking for their rating
- Mitigation: Show multiple reference frames; require users to estimate independently before seeing anchor

**Combos**: Anchoring × Decoy Effect → premium tier makes middle tier look "reasonable"
Anchoring × Social Proof → "most popular users pay $X" anchors AND provides social validation

**Boundary conditions**:
- Weakened when: user is an expert in the domain, or when the anchor is obviously absurd
- Strengthened when: domain is uncertain, user is under time pressure, first-time decision

---

## HB-02 · Loss Aversion
**Tier**: 核心
**Evidence**: B — Kahneman & Tversky 1979 前景理论；λ≈2.25 出自 Tversky & Kahneman 1992 的累积前景理论参数估计。争议：Gal & Rucker 2018 系统质疑"损失厌恶是普遍原则"，认为大量证据其实是参照点设置与重述框架的产物，而非独立于情境的"损失更痛"倾向；λ 的取值也随情境、标的与测量方法大幅变动，不应作为固定常数使用
**Effect**: 大（约 2 倍得失不对称），但仅在参照点已被拥有或已被期待时成立；参照点模糊、或损失被重述为"未获得的收益"时，效应向对称收敛

**机制链**: 结果被置于既有参照点之下 → 负向偏离触发更强唤醒与注意分配 → 为避免确认损失而承担额外风险或成本
**剂量**: 弱 一次性告知"将失去 X" ；中 具体化已持有物 + 明确时限，配合可见的进度或资产 ；强 叠加社会比较（"同组只有你没完成"）并做成默认路径 ；过载 参照点被用户判定为虚构，或每次触达都在喊损失 → 损失框架被重新归类为营销噪音，反向降低可信度并抬高后续真实损失的折扣率
**时间动态**: 起效 秒级（单次触达即可改变选择） · 衰减 同一损失的重复提醒在 3–5 次后钝化，用户开始主动规避文案 · 饱和 长期使用会把"损失"重新定价为常态成本，机制失效且信任余额下降
**调节变量**: 个体 损失厌恶强度随特质性风险厌恶与调节焦点上升，高专业度用户对人为参照点免疫 · 文化 集体主义市场对"损失相对位置"（排名、面子）比对"损失金钱"更敏感 · 情境 高不确定性加时间压力下效应放大，高利害且可复核的决策中效应被反思性加工削弱
**失效信号**: 用户开始截图或复述你的"损失"主张并质疑其真实性；同一触达的点击率在第二、三次后不降反升于关闭/退订入口；客诉与退款理由中出现"被胁迫感"表述；净推荐值下降但短期转化不变
**可测代理**: 同一价值主张的 gain-frame / loss-frame 分流转化差；触达第 n 次的打开率曲线拐点；退订率与文案损失强度的相关性
**交互**: × HB-03 默认效应 → 默认值把参照点变成"本来就有"，使损失框架无需虚构即可成立（COMBO-01）；× HB-08 沉没成本 → 已投入的进度被重新定价为"可失去的资产"，损失框架因此不需要虚构参照点；× SD-01 社会证明 → 从"你会失去"升级为"你正在掉队"，但双重施压也最快触发 reactance
**边界**: 不得用于虚构参照点（用户从未持有或期待过的东西）；健康、金融、法律场景下损失框架会放大焦虑并诱发非理性决策，须替换为收益框架加不确定性披露；一旦被判定为胁迫，修复成本高于该机制的全部历史收益
**可证伪条件**: 若在参照点被明确界定为已持有资产的预注册实验中，损失组与等额收益组的选择差异不显著大于 1，或 λ 在不同情境下无法收敛到区间，则“约 2 倍得失不对称可作为设计常数”的声称被推翻，本记录应降级为“损失框架仅在参照点由产品方设定时改变选择，不构成稳定比例”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.95；Effect Size: Large (2.25× loss-to-gain ratio)

**Mechanism**: Losses feel approximately 2.25× more painful than equivalent gains feel pleasurable. People will take irrational risks to avoid losses.

**Mathematical model**: v(x) = x^0.88 for gains; -2.25(-x)^0.88 for losses (Prospect Theory)

**Cognitive chain**: Outcome framed as loss → heightened emotional response → risk-seeking to avoid loss → action

**Implementation**:
```
Copy: "Don't lose your progress" > "Save your progress"
SaaS: "Your trial expires in 3 days" > "3 more days of premium"
Streak: "You'll lose your 47-day streak" > "Keep your streak"
Trial: "You lose access to [feature] on Friday" > "Your trial ends Friday"
Pricing: "$50 worth of features you're leaving behind" > "Upgrade for $50"
Social: "Others in your group have already completed this" (loss of relative position)
```

**Framing formula**:
> [What they already have] + [specific loss amount/item] + [time pressure] = maximum loss aversion

**Design principles**:
- Always reframe gains as potential losses when possible
- Make "the thing they'll lose" concrete and personalized
- Mitigation: Provide gain-framed alternatives; allow cooling-off periods; show opportunity costs

**Combos**: Loss Aversion × Social Proof → "you're the only one in your group who hasn't..."
Loss Aversion × Goal Gradient → "you've come 80% — losing this progress hurts"
Loss Aversion × Scarcity → maximum FOMO

---

## HB-03 · Default Effect
**Tier**: 核心
**Evidence**: A — Johnson & Goldstein 2003 的器官捐献跨国比较；Jachimowicz, Duncan, Weber & Johnson 2019 对 58 项研究的 meta 分析给出中等偏大效应（d≈0.68）。争议：该 meta 分析同时指出默认效应把"隐含推荐""努力成本""现状偏好"三种通道混在一起，单一 d 值无法区分它们；更关键的是器官捐献的经典对比被批评为国家间制度差异的混淆——选择加入/退出制的登记率差异远大于实际移植率的差异，登记率并不等于行为
**Effect**: 中等偏大（meta d≈0.68），但只在默认被读作"平台的推荐"且改变默认需要可见成本时成立；默认一旦被识破为"为自己利益而设"，效应翻转而非衰减

**机制链**: 选项被预置为无需动作即生效 → 不做动作被解读为"这是被推荐的，且改变要付出成本" → 用户停留在预置状态
**剂量**: 弱 预置一个可逆、低风险的选项（如列表默认按相关性排序），入口就在同屏 ；中 预置与用户目标一致的选项 + 一次性说明"已为你设置，可随时更改" + 更改入口在同一屏 ；强 预置为高承诺档（年付/自动续费）+ 更改入口下移到设置第三层 + 预置发生在用户注意力被占用时（注册流程末尾） ；过载 预置与用户利益相反且被识别（默认勾选付费加购、默认公开隐私项）→ 一次曝光即触发"被套路"判定，投诉、退订与监管举报同时上升，且用户此后对所有默认值主动反选，净转化下降
**时间动态**: 起效 一次（生效即完成，无需重复触达） · 衰减 首次手动更改后失效，且"我改过一次"的经验会外溢到同类默认，后续遵从率明显下降 · 饱和 用户对产品越熟悉遵从率越低，且被动默认留存用户的价值系统性低于主动选择用户
**调节变量**: 个体 认知负荷高、决策疲劳、对该领域无明确偏好者遵从率最高，有领域知识且有偏好者几乎不受影响 · 文化 高权力距离与高不确定性规避市场更倾向接受"平台已设好"的默认（视为权威建议） · 情境 选项多、决策琐碎、默认位于流程末端时最强，涉及身份、金钱或权利且被明确提示时最弱
**失效信号**: 设置页"更改默认"的点击率异常高（>15% 说明默认与偏好系统性错配）；注册流程在默认勾选步骤的停留时间骤增；退订理由高频出现"我不知道我订阅了"；媒体或监管点名默认勾选
**可测代理**: 默认遵从率（未修改即继续的比率）；设置页各默认项更改率排行；30/90 天留存中"被动默认用户"与"主动选择用户"的价值差；客服工单中"我什么时候订阅的"类占比
**交互**: × HB-02 损失厌恶 → 更改默认被编码为"主动放弃已生效的东西"，使黏性高于单纯的努力成本（COMBO-01 的默认化前置）；× HB-09 禀赋效应 → 默认生成的数据与配置成为"我的东西"，退出即失去（COMBO-11）；× HB-08 沉没成本 → 默认档位使用越久，降级越像承认当初选错
**边界**: 知情同意、隐私授权、自动续费、器官捐献与受益人指定等高权利敏感项不得使用默认（GDPR Art.7 要求同意须为明确的肯定动作，中国《个人信息保护法》第 14 条要求单独同意，美国 FTC negative-option 规则要求续费前明确披露）；默认只能用于"用户目标的最省力路径"，不得指向与用户利益相反的方向
**可证伪条件**: 若在高权利敏感场景（自动续费、隐私授权）中明确提示“已为你预置、可更改”后，默认遵从率不显著高于强制主动选择组，则“默认是普适转化杠杆”的声称不成立，本记录应删除高承诺档位的默认化建议，只保留低风险、与用户目标一致的预置
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.94；Effect Size: Very Large (70-90% stick with defaults)

**Mechanism**: People systematically accept defaults. Opt-out participation rates are 30-50% higher than opt-in for equivalent programs.

**Channels**: Cognitive laziness + implicit recommendation + loss aversion (changing = risking loss) + effort asymmetry

**Implementation**:
```
Settings: Pre-check email notifications; users keep them
Subscription: Default to annual plan (users don't downgrade)
Savings: Auto-enroll in retirement contributions; only 10% opt out
Organ donation: Opt-out countries have 90%+ donation rates vs opt-in 15%
Portion size: Default meal size anchors consumption
Privacy: Use explicit choice for sharing-sensitive settings; do not hide meaningful consent in a default
```

**Design principles**:
- Set defaults to the user's safest or highest-probability-success path
- Make changing the default easy for preference changes, but require explicit choice for consent-sensitive settings
- Segmented defaults: different defaults for different user types
- Mitigation: Require active selection for high-stakes or rights-affecting decisions; document why defaults exist

**Boundary conditions**: Weakened when: decision is high-stakes and involves identity/money; users expect to customize

---

## HB-04 · Scarcity Heuristic
**Tier**: 常用
**Evidence**: B — Worchel, Lee & Adewole 1975 的饼干罐实验；Lynn 1991 对可得性与价值关系的 meta 分析给出中等效应。争议：van Herpen, Pieters & Zeelenberg 2009 证明稀缺的方向取决于归因——供给型稀缺（限量、停产）提升偏好，而需求型稀缺（"很多人在买"）对以独特性或身份为消费动机的品类反而降低偏好，因为他人购买稀释了区隔价值；此外虚假稀缺会触发 Brehm 1966 意义上的心理逆反，效果由正转负
**Effect**: 中等，且方向依归因而定：供给稀缺提升支付意愿，需求稀缺在独特性相关品类上降低偏好；品类高度同质、可随时补货时效应接近零

**机制链**: 可得性受限的信号被感知 → 可得性被推断为价值与竞争强度的证据，并触发逆反与损失预期 → 提前决策或提高支付意愿
**剂量**: 弱 真实库存或名额上限，静态展示（"本期限 200 席"），无倒计时 ；中 真实库存 + 可核验的需求信号（"当前 12 人在看"）+ 一个真实的截止时间 ；强 供给与需求双稀缺 + 倒计时 + 与损失框架合并的 CTA，且稀缺对象已在用户购物车内 ；过载 稀缺信号密度过高或反复重置（每次刷新都是"仅剩 2 件"）→ 被判定为伪造，触发逆反：用户不买并主动传播"这是假稀缺"，此后对该品牌所有稀缺信号永久免疫
**时间动态**: 起效 秒级到分钟级（限时类） · 衰减 同一稀缺主张在 2–3 次触达后钝化，倒计时归零而活动未结束会一次性摧毁全部稀缺可信度 · 饱和 长期使用会把品类整体重新定价为"总在打折"，正价销售能力永久受损
**调节变量**: 个体 独特性需求高者对"很多人在买"型稀缺反应为负，冲动性购买倾向高者对限时稀缺反应最强 · 文化 集体主义与高面子市场对"名额/资格稀缺"这类社会性稀缺的反应强于纯数量稀缺 · 情境 品类可替代性低、决策不可逆时最强，品类同质且随时可补货时几乎无效
**失效信号**: 倒计时归零后页面仍在售卖；同一 SKU 的"仅剩 N 件"在多次访问中不下降或回升；比价插件或用户帖出现"库存造假"指认；稀缺文案曝光组的退货率与差评率显著高于对照组
**可测代理**: 稀缺文案 A/B 的点击→支付转化与 30 天退货率之差；同一 SKU 库存显示跨会话的一致性（可用自检脚本每日采样）；倒计时结束后的页面行为日志；客服关键词中稀缺相关表述的占比
**交互**: × HB-02 损失厌恶 → 稀缺物被编码为即将失去的资产，紧迫感来自损失而非收益（COMBO-01）；× SD-01 社会证明 → 需求信号让稀缺变得可信，两者互为证据，但也最快被识破为编造（COMBO-01）；× HB-05 框架效应 → "仅剩 2 件"与"已售 98%"是同一事实的两种框架，后者把稀缺转写成社会证明，抗证伪性更强
**边界**: 不得虚构库存、名额或倒计时（中国《反不正当竞争法》第 8 条虚假宣传、《价格法》，欧盟 Omnibus 指令明确禁止虚假稀缺主张，美国 FTC 欺骗性定价指南）；医疗、住房、救灾物资与金融产品禁用稀缺框架（诱发恐慌性决策）；稀缺一旦被证伪，该品牌此后真实的稀缺也失去信号价值
**可证伪条件**: 若在独特性动机被单独测量的品类中，需求型稀缺信号（“很多人在买”）与无稀缺信号组的偏好差异不显著优于后者，则“稀缺方向由归因决定”的修正被推翻，本记录应降级为“稀缺仅提升支付意愿、不影响偏好方向”并删除独特性品类的反向预测
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.91；Effect Size: Large

**Mechanism**: Limited availability signals value. Works for time, quantity, access, and social exclusivity. Perceived scarcity can drive urgency, but misleading scarcity creates trust, legal, and reputational risk.

**Types**:
1. **Quantity scarcity**: "Only 3 left in stock"
2. **Time scarcity**: "Offer expires in 2:47:32"
3. **Access scarcity**: "Invite-only" / "Waitlist"
4. **Social scarcity**: "Trending in your area right now"
5. **Information scarcity**: "Exclusive early access"

**Implementation**:
```
E-commerce: "Only 2 left" + "[X] people viewing this now"
SaaS pricing: "Founding member pricing — 47 spots remaining"
Events: "Last 8 tickets" + live countdown timer
Community: Waitlist with real queue position or clearly labeled staged access
Content: "This post will be deleted in 24 hours"
Offers: Time-limited discount with countdown
```

**Design principles**:
- Combine quantity AND time scarcity for maximum effect
- Make scarcity real and credible (users detect fake scarcity and react negatively)
- Real-time social proof of demand amplifies scarcity perception
- Mitigation: Show scarcity is real; allow opt-out; don't manufacture false urgency

**Combos**: Scarcity × Social Proof → "3 left, 8 people watching" = maximum urgency
Scarcity × Loss Aversion → the scarce thing becomes a potential loss

---

## HB-05 · Framing Effect
**Tier**: 核心
**Evidence**: B — Tversky & Kahneman 1981 的亚洲疾病问题为原始证据；Kühberger 1998 的 meta 分析显示框架效应稳定但平均效应远小于经典演示。争议：大量现场"框架收益"其实是注意与显著性效应而非偏好反转，用户一旦自行换算等价形式效应即消失；Gal & Rucker 2018 进一步指出得失框架之所以有效，很大程度是因为它同时移动了参照点，与损失厌恶共用同一混淆，因此不宜把框架当作独立于参照点的机制来计功
**Effect**: 中等（meta 分析的平均效应小于课堂演示），机制上是"同一事实的不同侧面获得不成比例的权重"；用户能自行换算等价形式或利害很高时效应消失

**机制链**: 等价信息被以某一侧面呈现 → 该侧面在评估中获得不成比例的权重，其余侧面未被检索 → 判断与选择沿该侧面偏移
**剂量**: 弱 同屏并列两种等价表述（"90% 无脂 / 10% 含脂"），由用户自选 ；中 按决策目标选单一框架（获客用收益框架、留存用损失框架）并做单位化（"每天 $0.10"） ；强 框架 + 参照点转移 + 对比对象同时设置（"原价 $299 / 现价 $89 / 每天 $0.30"），且页面不提供换算工具 ；过载 框架与事实的落差被用户换算出来（"每天 $0.30 就是每月 $9"），或多种框架互相矛盾 → 触发"被操纵"归因，用户转入防御性核算，转化低于中性表述组
**时间动态**: 起效 单次呈现即时 · 衰减 同一框架重复曝光后用户学会换算，约 3–5 次后自动去框架化 · 饱和 长期使用单一框架会训练出"换算型"用户群，此后任何单位化表述都被自动还原为总额
**调节变量**: 个体 数值能力高者几乎不被单位化框架影响，认知需求低与时间压力大者效应最强 · 文化 高语境文化对"社会框架"（多数人选择）的反应强于"数字框架"，低语境文化相反 · 情境 单次、不可比、无换算工具时最强，并列呈现或用户自带计算器时最弱
**失效信号**: 用户在评论中自行换算总额并贴出（"其实就是 $108/年"）；同一 offer 的两种框架版本转化差趋近于零；客服出现"你们写每天多少钱、实际扣多少"类工单；按数值能力分层后高分组转化与框架无关
**可测代理**: 同一 offer 的 gain-frame / loss-frame / unit-frame 三臂 A/B 转化差；按数值能力分层后的效应衰减曲线；用户侧换算行为（打开费率页、比价插件）与转化的负相关；退款理由中"预期不符"的占比
**交互**: × HB-01 锚定 → 框架决定单位、锚定决定量级，二者叠加构成定价页的默认读法（COMBO-08）；× HB-02 损失厌恶 → 损失框架之所以强，部分是因为它把参照点从"未拥有"移到"已拥有"，这正是 Gal & Rucker 批评的混淆点；× PE-02 心理账户 → 同一金额记入不同账户时框架效应被放大数倍
**边界**: 不得用框架隐藏关键条款（总价、自动续费、退出成本必须与单位化表述同屏）；金融、医疗、法律场景中框架差异会导致实质不同的风险认知，须并列双框架并给绝对数值；用户换算后发现落差时，信任损失大于该文案的全部收益
**可证伪条件**: 若在同一事实的双框架并列呈现（绝对数值与单位化表述同屏）条件下，两组的风险认知与选择差异不显著高于并列无框架组，则“框架可独立于信息内容改变选择”的声称不成立，本记录应降级为“框架只在单一表述、无对照数值时才移动判断”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.93；Effect Size: Large

**Mechanism**: Identical information presented differently leads to systematically different decisions. Positive vs negative frames, absolute vs relative numbers, gain vs loss frames.

**Frame types**:
- **Gain frame**: "90% fat free"
- **Loss frame**: "Contains 10% fat"
- **Relative**: "Save 50%" vs "Save $5"
- **Social frame**: "Most users choose..."
- **Temporal frame**: "In 1 year you'll wish you started today"

**Implementation**:
```
Health: "95% survival rate" > "5% mortality rate"
Finance: "You're only spending $3/day" > "$90/month"
Progress: "You've completed 30%" vs "70% remaining"
Risk: "1 in 10 chance of success" vs "1 in 10 chance of failure" — depends on goal
Social: "Join 10,000+ people who..." > "Be among those who..."
```

**Formulas**:
- Selling → Gain frame ("what you get")
- Retention/urgency → Loss frame ("what you lose")
- Price sensitivity → Small unit frame ("$0.10 per day")
- Quality perception → Relative superlative ("top 5% rated")

---

## HB-08 · Sunk Cost Fallacy
**Tier**: 常用
**Evidence**: B — Arkes & Blumer 1985 的经典系列实验。争议：Friedman, Pommerenke, Lukose, Milam & Huberman 2007 用真实货币与更严格的激励设计系统搜寻沉没成本效应，未观察到可靠证据，据此认为实验室结果很大程度是"浪费规避"与自我形象维护的混合物，而非对不可回收成本的经济性误算；现场证据中沉没成本也与"继续投入可以获得信息"这一理性理由高度混淆，难以分离
**Effect**: 中等，且只在"投入与自我形象绑定"或"放弃需要向他人解释"时稳定；纯经济核算、匿名、投入可转移的情境下效应可消失

**机制链**: 已付出的时间、金钱或努力被记为不可回收资产 → 放弃被解读为"承认此前判断错误"的自我威胁，而非止损 → 追加投入以维持前后一致
**剂量**: 弱 在用户已完成部分流程时显示已投入量（"你已配置 6 项"），不施压 ；中 把已投入量做成可见资产（等级、连续天数、已导入数据）+ 在退出路径上提示其存在 ；强 已投入量 + 社会可见性（他人知道你的投入）+ 退出需主动解释（"确定要放弃你的 47 天记录吗"） ；过载 反复以沉没成本拦截挽留（每次退订都被"你已投入 X"拦一次）→ 用户把提示读作勒索，不仅完成退出还在公开评价里披露该手法，此后对该产品任何进度展示都反感
**时间动态**: 起效 在退出或降级决策点即时生效 · 衰减 单次挽留有效，同一用户被挽留 2 次以上后效应转负 · 饱和 沉没成本只能推迟退出、不能阻止退出：被挽留用户的 90 天留存显著低于自然留存，且口碑负向外溢
**调节变量**: 个体 自我一致性需求高、曾公开承诺目标者最强，把投入视为"学费"（学习框架）者最弱 · 文化 高面子与强关系文化中"向他人解释放弃"的成本更高，效应被放大 · 情境 退出可见、需向他人交代时最强，匿名、一次性、数据可导出时最弱
**失效信号**: 挽留弹窗后 7 日回访率回升但 30 日流失率不降（只是推迟）；退订流程完成时长与差评率正相关；"我投入了这么多"类表述出现在投诉而非好评中；被挽留用户的 LTV 低于未被挽留组
**可测代理**: 有/无沉没成本挽留的 30 日与 90 日留存差；退订流程各步骤的放弃率（哪一步劝退了谁）；被挽留用户的 NPS 与推荐行为；数据导出功能使用率（导出是退出前兆）
**交互**: × HB-02 损失厌恶 → 沉没成本把"过去的投入"变成"即将失去的资产"，两者共用同一套损失计算，强度叠加；× MR-01 目标梯度 → "已完成 80%"使止损被读成"浪费了 80%"而非"省下 20%"（COMBO-05）；× MR-04 身份承诺 → 投入一旦被公开标注为身份，退出就从经济决策变成身份否定（COMBO-12）
**边界**: 用户已明确表达退出意愿后不得重复以沉没成本拦截（暗黑模式清单明列，欧盟 DSA/DMA 与 FTC click-to-cancel 规则要求退出与订阅同等便利）；不得用于健康、赌博、投资加仓等会造成实质损失的场景——"再投一点就能回本"是亏损放大的标准路径；数据必须可导出，否则沉没成本实为扣押
**可证伪条件**: 若在匿名、投入不可转移、且明确告知“继续投入的期望回报为负”的现场对照中，有沉没成本提示组的继续率不显著高于无提示组，则“沉没成本独立驱动追加投入”的声称不成立，本记录应降级为“沉没成本只在投入与自我形象绑定或需向他人解释时起作用，属自我呈现现象而非成本误算”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Large

**Mechanism**: Past investment (time, money, effort) irrationally drives future commitment beyond the point of rationality. People continue losing propositions to avoid "wasting" prior investment.

**Implementation**:
```
Games: Character progression / purchased items / leveling = sunk cost trap
SaaS: Data migration effort + setup investment = switching cost
Learning platforms: Accumulated streaks / certificates / progress = sunk cost
Social: Years of followers/content history = switching barrier
Onboarding: Invest users in setup early → they won't abandon
Group commitments: "Your team has been waiting for you"
```

**Design principles**:
- Front-load effort investment during onboarding (personalization, setup, data import)
- Create visible progress artifacts (streaks, levels, score) that feel "losable"
- Remind users of past investment at churn risk moments
- Mitigation: Allow easy export/migration; transparency about switching costs

**Combos**: Sunk Cost × Loss Aversion → "you'd be throwing away everything you've built"
Sunk Cost × Goal Gradient → "you're too close to quit now"

---

## HB-09 · Endowment Effect
**Tier**: 常用
**Evidence**: B — Thaler 1980 提出，Knetsch 1989 的杯子实验为经典证据。争议：Sayman & Öncüler 2005 的 meta 分析发现真实的 WTA/WTP 比值远小于常被引用的约 2 倍；Plott & Zeiler 2005 更进一步论证该差距很大程度上是被试误解与实验程序的产物，在修正程序与充分激励后显著收缩；因此禀赋效应不宜作为固定倍数使用，其成立依赖真实所有权与不存在套利机会
**Effect**: 中等；经典约 2 倍的 WTA/WTP 比值在方法更严格的实验中明显缩水，但在"真实所有权 + 不可套利 + 对象由用户亲手定制"时稳定

**机制链**: 对象进入"我的"范畴 → 放弃它被编码为损失而非"未获得" → 要价高于出价，退出意愿低于进入意愿
**剂量**: 弱 让用户先做一次个性化设置（选主题、命名），再展示为"你的" ；中 免费期内给完整功能 + 沉淀用户生成内容（"你的仪表盘"）+ 到期前预览"你将失去的部分" ；强 用户已产出可积累资产（数据、作品、社交关系）+ 试用期长到形成习惯性所有权 + 到期瞬间一次性移除 ；过载 给予后强行收回且不给迁移路径（功能下线、数据锁定、突然降级）→ 所有权被读作诱饵，触发逆反与"被扣押"叙事，退款、差评与监管投诉集中爆发，此后用户拒绝任何试用邀请
**时间动态**: 起效 分钟级（心理所有权可在一次交互内形成） · 衰减 未使用即衰减：试用期内不活跃的用户不形成所有权，到期时无损失感 · 饱和 所有权一旦形成即稳定，但反复"给予-收回"会把所有权重定义为"租用"，此后不再有禀赋效应
**调节变量**: 个体 高自尊与高控制需求者所有权形成更快，把产品当纯工具而非"我的作品"者最弱 · 文化 高集体主义文化中"我的"边界依赖关系与共享，个人所有权效应弱于个体主义市场 · 情境 对象由用户亲手创建或定制、且不可轻易替代时最强，标准化、随时可再获取时最弱
**失效信号**: 试用到期转化率与试用期活跃度脱钩（说明起作用的不是所有权）；到期前 72 小时数据导出与截图行为量飙升；到期后 30 天回流率极低且伴随差评；用户明确表述"这是钓鱼试用"
**可测代理**: 试用期内个性化设置完成率与到期转化率的相关；到期前 72 小时导出/截图行为量；"失去"预览页曝光→转化；收回资产组的退款率与 NPS
**交互**: × HB-02 损失厌恶 → 禀赋效应是损失厌恶在所有权上的特例，二者叠加时最强；× HB-03 默认效应 → 默认生成的内容天然成为"我的"，退出成本被静默抬高（COMBO-11）；× HB-08 沉没成本 → 用户投入的定制劳动使对象同时具备"我的"与"我做的"两重锁定（COMBO-11）
**边界**: 不得用"给予-收回"制造虚假所有权（虚假试用、强制绑定）；用户生成内容必须可导出、可删除（GDPR Art.20 数据可携带权，中国《个人信息保护法》第 45 条）；医疗、住房与金融资产不得用所有权框架影响决策；一旦用户认定收回是设计而非意外，信任损失不可逆
**可证伪条件**: 若在真实所有权、无套利机会、且对象由被试亲手定制的实验中，WTA/WTP 比值不显著大于 1，则“禀赋效应可作为设计依据”的声称被推翻，本记录应降级为“禀赋效应是无法稳定复现的实验程序产物，仅保留用户生成内容带来的迁移成本这一工程事实”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.87；Effect Size: Medium-Large

**Mechanism**: People value things more once they own them. Mere possession (even temporary/virtual) increases perceived value 1.5-2×. Trial periods can create a real sense of ownership, so they should be used transparently.

**Implementation**:
```
Free trial: Give full access first; removal feels like loss (not missing gain)
Personalization: "Your" dashboard, "your" profile = ownership feeling
Game items: Give powerful item on day 1; if lost = disproportionate pain
Test drives / samples: Physical possession increases purchase likelihood 40%
"Save your work": Implicit ownership of created content
Beta access: "Your" early access = endowment
```

---

## HB-11 · Decoy Effect (Asymmetric Dominance)
**Tier**: 常用
**Evidence**: B — Huber, Payne & Puto 1982 提出不对称支配，为经典证据。争议：Frederick, Lee & Baskin 2014 的《The Limits of Attraction》系统检验发现吸引力效应在真实选择情境中远小于文献宣称，多项已发表演示无法复现，且效应高度依赖选项的呈现与描述方式；诱饵若被完全支配（在所有维度都更差）则被忽略而不产生拉动，这一边界在流行叙述里常被漏掉
**Effect**: 中等偏小；三选项、维度清晰可比时稳定，真实多属性、多档位情境中效应显著缩小，四档以上时被选择过载吞没

**机制链**: 出现一个被目标选项支配、但不被其他选项支配的选项 → 比较集被重构，目标选项获得"明确优于某物"的地位 → 选择向目标选项集中
**剂量**: 弱 三档并列，中间档在关键维度上略优，不加任何标记 ；中 中间档 + 不对称诱饵（更贵却只多一项） + "最受欢迎"标记 ；强 降序排列 + 诱饵 + 单位化框架 + 社会证明，使目标档成为"唯一理性解" ；过载 诱饵设计过度（诱饵被完全支配，或四档以上互相支配）→ 比较集失效，用户退回最便宜档或直接离开，吸引力效应被选择成本完全吞没
**时间动态**: 起效 单次呈现即时（比较是同步进行的） · 衰减 用户第二次访问同一价目表时效应约减半（已形成内部排序） · 饱和 长期暴露后用户按"中间档=被设计的目标"反向推理，主动选最低档
**调节变量**: 个体 领域知识低、无明确预算者效应最强，有硬性需求清单者几乎不受影响 · 文化 高不确定性规避市场更依赖"多数人选择"标记，而非纯支配关系 · 情境 三选项、单一维度清晰可比时最强，选项超过 4 个或维度超过 3 个时最弱
**失效信号**: 中间档被选率与"最受欢迎"标记是否显示无关（说明拉动来自诱饵或两者都无效）；最低档被选率异常升高（诱饵反噬）；用户在评论中直接指出"中间那档是故意设的"；四档价目表的整体转化低于三档
**可测代理**: 三臂 A/B（无诱饵 / 标准诱饵 / 完全支配诱饵）的档位分布；中间档被选率对诱饵价格的弹性；价目表停留时长与离开率的联合指标；选项数 3→4→5 的转化衰减曲线
**交互**: × HB-01 锚定 → 最高档提供量级锚、诱饵提供支配关系，两者共同把目标档定义成"理性"（COMBO-08）；× PE-08 选择过载 → 诱饵超过一个即开始反噬，吸引力效应被选择成本吞没；× SD-01 社会证明 → "最受欢迎"标记在诱饵失效时仍能单独起作用，是更稳的替代路径
**边界**: 不得构造用户无法识别的虚假支配（诱饵必须真实存在且可购买，否则构成虚假选项与欺诈）；金融、保险、医疗方案中诱饵会诱发系统性误配，须同时提供"按需求推荐"路径；档位必须控制在 3–4 档，超过即转为选择过载
**可证伪条件**: 若在诱饵真实可购买、档位数控制在 3–4 档的条件下，非对称中间档的存在对目标档份额的提升不显著高于无诱饵对照组，则“诱饵可稳定把选择推向目标档”的声称不成立，本记录应降级为“诱饵只在与框架、锚定同时出现时贡献边际增量，不能单独用于转化”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.85；Effect Size: Medium-Large

**Mechanism**: Adding an asymmetrically dominated option makes the target option look more attractive. This is the classic 3-option pricing pattern.

**Classic setup**:
```
Option A (basic): $9/month
Option B (pro): $19/month        ← target
Option C (enterprise): $18/month ← decoy (close to B but worse)

→ Option B now looks like "best value"
```

**Implementation**:
```
Subscription tiers: Annual plan that makes monthly look expensive
Size options: Medium positioned as "value"
Feature bundles: Include decoy bundle that makes target bundle look complete
Event tickets: VIP decoy makes "premium" look reasonable
```

---

## HB-13 · Hyperbolic Discounting
**Tier**: 核心
**Evidence**: B — Ainslie 1975 的双曲贴现模型；Frederick, Loewenstein & O'Donoghue 2002 的综述确认"偏好反转"（同一延迟在不同时点被不同定价）稳定复现。争议：同一综述记录了折现率估计从个位数到数千个百分点每月的跨度，说明测量方法（选择法 vs 匹配法、真实 vs 假设、金额大小）比"人的贴现率"更能解释方差；因此双曲形式宜作为定性预测使用，不宜当作个体参数或行业常数；准双曲（β-δ）与次可加模型在多数数据上拟合更好
**Effect**: 中等；"近端偏好反转"这一方向性预测稳健，但折现率的具体数值高度依赖测量方法，不能当作可迁移参数使用

**机制链**: 近端奖励被以具体生动的方式表征 → 远端奖励被抽象化并折价 → 选择在时间距离缩短时发生反转
**剂量**: 弱 把奖励到账时间从"7 天后"改为"完成即到账"，不改变奖励本身 ；中 即时小额奖励 + 明确的后续成本时间表（先给后用，且总成本可见） ；强 即时兑现 + 成本后置且被单位化（"今天 $0，30 天后每天 $0.5"）+ 无冷静期 ；过载 成本后置到用户在决策时无法想象（多期叠加的先享后付、隐藏的自动续费）→ 账单到期时支付痛苦回弹，形成"被套"叙事，退款、拒付与投诉集中出现，并招致监管关注
**时间动态**: 起效 秒级（奖励可见即刻） · 衰减 即时奖励的驱动在数小时到数天内衰减，重复的"现在免费"会训练出对后置成本的预期 · 饱和 用户学会"现在免费=以后更贵"后，即时框架不再有效，并主动寻找总成本
**调节变量**: 个体 冲动性与低延迟满足能力者效应最强，金融素养高者对单位化后置成本免疫 · 文化 高长期导向与高储蓄率文化中即时框架效应较弱 · 情境 决策疲劳、深夜、情绪唤醒、无计算工具时最强，有冷静期且总成本同屏时最弱
**失效信号**: 首期转化高但第二期扣款失败率与退订率同步抬升；拒付（chargeback）率与后置期数正相关；"为什么扣我钱"类工单集中在账单日；用户评论出现"总价算下来更贵"
**可测代理**: 首期转化与第 2/3 期留存及扣款成功率之差；总成本披露前后的转化差；账单日后 72 小时工单量与主题分布；按后置期数分层的退款与拒付率
**交互**: × CA-05 时间贴现 → 本记录是 CA-05 在行为层的表现，二者属同一机制的不同抽象层级，不要重复计数；× HB-05 框架效应 → 单位化把"未来的总痛"切成"现在的每天一点"，是后置成本能被接受的关键；× AD-01 变动比率 → 即时不确定性加上延迟成本，正是 COMBO-02 得以持续运转的经济学基础
**边界**: 不得用后置成本隐藏总价（消费信贷须披露年化利率，欧盟 CCD2、美国 TILA/Reg Z）；先享后付与订阅不得默认勾选自动续期；赌博、高频交易与成瘾性产品禁用即时奖励设计；用户发现总成本落差后，拒付率与监管投诉的代价高于该模式全部收益
**可证伪条件**: 若在真实货币、跨期限的激励实验中，被试的贴现率不随延迟期限延长而显著下降（即无法区分双曲与指数贴现），则“偏好反转是成瘾性产品设计的可靠基础”的声称被推翻，本记录应降级为“贴现率的期限结构在实验室外不稳定，不能作为订阅与信贷定价的依据”
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.86；Effect Size: Medium-Large

**Mechanism**: People heavily discount rewards that are slightly delayed, but relatively little for delays far in the future. "Now" is worth dramatically more than "later."

**The gap**: $10 now vs $11 in a week → take $10 (irrational). $10 in 52 weeks vs $11 in 53 weeks → prefer $11 (patient). Same delay, different temporal distance.

**Implementation**:
```
Freemium: "Use premium NOW free for 30 days" (now > later)
Instant delivery: Prime's power is pure hyperbolic discounting
Buy now pay later: Gratification now, pain later (requires strong transparency safeguards)
Immediate unlock: "Get access instantly" > "Get access tomorrow"
App permissions: "Grant access now to use feature" — now bias drives approval
Flash sales: The "now" price vs "later" price gap amplifies present bias
```

**Design principles**:
- Make reward immediate, even if small
- Delay costs/pain as much as possible
- "Start free, pay later" models are built entirely on this mechanism

---

## HB-06 · Availability Heuristic
**Tier**: 常用
**Evidence**: B — Tversky & Kahneman 1973 的可得性启发（实例的可提取性被当作频率证据）。争议：①Schwarz et al. 1991 证明驱动判断的是"提取的难易感"而非提取到的内容本身，二者可以分离——被要求举出 12 个例子（更难）的被试反而给出比举 6 个例子（更易）更低的发生频率估计，"可得性"因此不是单一机制；②"可得性解释风险误判"的因果主张弱于通俗表述：媒体覆盖率与风险感知的相关几乎都是观察数据，且难与情绪唤醒、政治立场分离；③生态理性论证指出可得性在真实环境中经常给出正确答案，把它一律称作偏差属过度归类。
**Effect**: 中等偏大（描述层面：频率与概率估计随实例可提取性上升），但仅在"该量无法直接计数、判断依赖记忆提取"时成立；有可查统计数据或计数成本低时效应消失

**机制链**: 一个问题要求估计频率或概率 → 判断者以"能想起多少例子、想起得多容易"替代实际计数 → 估计值向可提取的实例倾斜
**剂量**: 弱 在用户形成判断前提供一个具体案例（"李女士……"），不声称其代表性 ；中 具体案例 + 媒体化细节（画面、时间、地点）+ 与用户自身处境的可类比性 ；强 多个同向案例密集曝光 + 情绪化细节 + 案例与决策窗口重合（刚看到事故新闻就当页看到保险） ；过载 反复投放同类惨案或成功案例直到用户察觉叙事被操纵 → 可得性反转：用户把整个案例类别判为营销渲染，主动低估其真实频率并转向索要统计基率，机制由正转负
**时间动态**: 起效 单次暴露即可移动估计（分钟级） · 衰减 单个案例的记忆强度按天级衰减，未被复述者约一周后不再驱动判断 · 饱和 同向案例第 3–5 次后边际影响转负，用户以"又在讲这个故事"做折扣
**调节变量**: 个体 情绪反应性高、统计素养低者最强，有核数据习惯者几乎不受单个案例影响 · 文化 高不确定性规避与低机构信任的社会更依赖案例而非官方统计 · 情境 决策时限紧、无外部数据可查、案例与自身相似时最强，有可核实基率且用户主动核实时最弱
**失效信号**: 用户开始要求"具体概率/样本量"而非接受案例；案例类内容互动上升但转化不升（被当娱乐消费）；"又来了"类评论占比上升；客服被追问"能不能给我实际数据"
**可测代理**: 同一主张的"案例版"与"统计版"分流的估计差；案例第 n 次曝光的边际转化曲线；统计页/FAQ 访问率（用户在找基率）；案例类素材的投诉率
**交互**: × HB-02 损失厌恶 → 可得性负责"这件事好像很常见"，损失框架负责"我会失去"，两者把低概率事件估成迫近威胁（COMBO-01）；× SD-01 社会证明 → 同向案例同时是频率证据与从众证据，两通道难以分离（COMBO-04）；× PA-02 模式打断 → 情绪化案例只有打断注意才被记住，而可得性由记忆可得物决定，打断强度因此直接改变后续频率估计（COMBO-09）
**边界**: 不得用可得性伪造风险——把罕见事故说成常见、把个案说成规律属虚假宣传（中国《反不正当竞争法》第八条、美国 FTC Act §5 对误导性陈述的规制）；健康、安全、金融场景下案例框架会系统性扭曲风险认知，须同时披露基率与不确定性；保险与信贷场景中夸大恐惧可能构成不当销售
**可证伪条件**: 若在控制情绪唤醒、政治立场与呈现格式后，实例可提取性的实验操纵不再移动频率估计，或多个同向案例的边际效应不呈先升后降而是单调上升，则“可得性由记忆提取难易驱动、且会因过载反转”的声称不成立，本记录应降级为“可得性只是观察相关性，不作为风险沟通的设计依据”

**Mechanism**: Judgments of frequency and probability are made from how easily instances come to mind, not from counting. Vivid, recent, personally relevant instances are overweighted.

**Design principles**:
- Use concrete cases to make a risk feel real, but never present a case as a base rate
- Pair every case with the actual frequency, or the design is a lie of proportion
- Mitigation: show counts and confidence intervals alongside anecdotes; test which of the two the user actually acted on

---

## HB-07 · Representativeness
**Tier**: 常用
**Evidence**: B — Tversky & Kahneman 1974 的工程师/律师范式与合取谬误。争议：Koehler 1996 系统复核指出基率被忽视的程度被高估——当基率被表述为因果相关（说明该基率如何产生该案例）时，人们会正常使用它，故"基率忽视"很大程度上是实验范式把基率做成无关数字的产物；此外相似度判断在真实环境中常与贝叶斯推理一致，称其为偏差属规范性问题；合取谬误的复现则更稳健
**Effect**: 中等，且取决于基率的可及性与因果地位：基率被呈现为抽象统计时最易被忽视，被呈现为因果生成机制时几乎不被忽视；合取谬误方向稳定

**机制链**: 对象与某类别的典型形象相似 → 相似度被当作概率，基率与样本量被搁置 → 判断向相似度倾斜并忽略先验
**剂量**: 弱 在介绍个案时并列一行参考基率（"该类别占总体 3%"），不做因果解释 ；中 具体但非典型的个案描述 + 与用户目标相关的细节，基率降为脚注 ；强 生动个案 + 反典型基率缺席 + 决策被时限与情绪推动（"他就是那种典型用户"） ；过载 个案刻画典型到被用户识别为刻板印象 → 用户整体拒绝该分类框架并转向索要数据，代表性不再移动判断，同时对任何"典型用户画像"表述转为反感
**时间动态**: 起效 单次个案呈现即生效（秒级） · 衰减 用户获得自有经验样本后，代表性被真实经历覆盖，衰减以"亲自接触过几个案例"计而非以时间计 · 饱和 长期以画像驱动判断会使错误分类累积，用户一旦遭遇反例便整体放弃画像
**调节变量**: 个体 统计训练低者最强，有概率训练者会主动寻找基率 · 文化 高集体主义与高社会分类文化更依赖"典型形象"，基率更易被忽视 · 情境 给定生动描述、缺乏数据、判断对象陌生时最强，有历史数据或需向他人交代推理过程时最弱
**失效信号**: 用户追问"这类人到底有多少"；画像类文案点击高而匹配成功率低；推荐结果被投诉"不像我"；基率脚注阅读率异常高
**可测代理**: 有无基率提示的分类准确率差；"典型用户"文案匹配成功率对基率幅度的斜率；画像类内容投诉率；推荐后需人工纠正的比例
**交互**: × SD-01 社会证明 → 少量生动案例同时提供典型性与聚合证据，把少数样本读成常态（COMBO-04）；× HB-01 锚定 → 先给出的类别基准值成为概率起点，代表性决定"像不像"、锚定决定"从哪开始调"（COMBO-08）；× PA-01 处理流畅性 → 典型画像更易加工，流畅感被误读为真实性，加速分类固化（COMBO-06）
**边界**: 不得以群体画像做差别定价或资格筛选——基于用户画像的差别待遇受中国《消费者权益保护法实施条例》第九条与《个人信息保护法》第 24 条自动化决策条款约束，欧盟 GDPR 第 22 条限制纯自动化的重大决策；招聘、信贷、保险场景中代表性推断直接构成歧视风险；画像只能降低不确定性，不得替代可核验的个体数据
**可证伪条件**: 若把基率表述为因果生成机制后，被试对基率的使用与抽象百分比表述下的使用无显著差异，则“基率忽视主要是实验范式把基率做成无关数字所致”的修正被推翻，本记录应降级为“基率在呈现形式上被普遍忽视，因果表述无法挽救”，并删除因果化表述的建议

**Mechanism**: Probability is judged by resemblance to a category prototype. Base rates and sample size get set aside in favour of "how much does this look like the thing".

**Design principles**:
- State base rates causally, not as a bare percentage — causal framing is what makes people use them
- Never let a persona do the work of a segment's actual distribution
- Mitigation: give the user the reference class and the conjunctive-probability check

---

## HB-10 · Status Quo Bias
**Tier**: 核心
**Evidence**: B — Samuelson & Zeckhauser 1988 提出并命名；Kahneman, Knetsch & Thaler 1991 的损失厌恶解释曾被广泛接受。**本记录的判断：证据更支持"惰性与省略偏差是可分离的主通道，损失厌恶只是条件性放大器"**，理由是①现状偏好出现在从未被拥有的状态上（新员工保留旧计划、不选择即保留默认），无所有权即无损失可厌恶；②Gal 2006 论证损失厌恶解释与"避免任何行动"的惰性相混淆，同一组风险赌注数据既可读作现状偏好也可读作损失厌恶；③Gal & Rucker 2018 进一步指出损失厌恶证据本身与惰性混淆。反方：Novemsky & Kahneman 2005 主张在所有权与参照点明确时损失厌恶仍独立贡献。故两条通道并存，惰性更普遍、损失厌恶更条件性
**Effect**: 中等偏大（现状被识别为默认时被强偏好），但主作用通道是惰性与省略而非损失厌恶；存在明确所有权与参照点时可叠加损失厌恶而进一步上升，仅剩惰性时效应依然可观

**机制链**: 一个当前状态已经生效（无论是否被主动选择） → 改变被编码为主动作为并携带责任与不确定性，维持不动被编码为无作为 → 用户停留在现状，即使替代方案客观更优
**剂量**: 弱 保留现有设置并说明"随时可改"，改变入口可见 ；中 现状作为默认 + 迁移成本可见（"重新导入需要 10 分钟"）+ 一次性说明更改方法 ；强 现状 + 已积累的配置与数据 + 改变需向他人解释（团队已按此配置）+ 改变路径分步 ；过载 用现状偏好封死退出（订阅难取消、降级入口深埋、迁移被阻拦）→ 被判定为扣押：用户以合规投诉、公开差评与集体流失回应，监管关注度上升，且此后任何"保持现状"的默认都被主动反选
**时间动态**: 起效 一次性（不选择即生效，无需重复触达） · 衰减 用户每主动更改一次现状，下一次遵从率下降，且该经验外溢到同类默认 · 饱和 长期以惰性维持的用户价值系统性低于主动选择用户，被动留存先体现为低活跃而非流失
**调节变量**: 个体 决策疲劳、低领域知识、高不确定性规避者最强，有明确偏好与领域知识的专家几乎不受影响 · 文化 高不确定性规避与高权力距离市场更接受"保持现状即正确" · 情境 选项多、后果不明确、改变需多步时最强，涉及重大权益或被明确提醒有替代方案时最弱
**失效信号**: 更改入口点击率异常高但完成率低（用户想改而被阻）；退订/降级流程的放弃率随步骤数上升；"我不知道自己还在订阅"类工单占比上升；被动留存用户 30 日活跃显著低于主动选择用户
**可测代理**: 默认遵从率（未修改即继续的比例）；设置页更改完成率与点击率之比；被动留存与主动留存的价值差（活跃、LTV、NPS）；退订流程各步骤放弃率；迁移耗时中位数
**交互**: × HB-09 禀赋效应 → 现状中的配置与数据成为"我的东西"，退出即失去，惰性获得所有权支持（COMBO-11）；× HB-08 沉没成本 → 现状存续越久，改变的代价越像承认过去投入白费（COMBO-03）；× SD-01 社会证明 → 团队已按此方式配置使改变需要向他人解释，社会成本叠加惰性（COMBO-04）
**边界**: 退订、降级与数据迁移不得设置障碍——美国 FTC 的 negative-option（点击取消）规则虽于 2025 年被第八巡回法院撤销，但 FTC Act §5 与 ROSCA 下的执法与和解仍要求退出与订阅同等便利，欧盟 DSA 第 25 条、中国《消费者权益保护法实施条例》第十条与第十七条要求自动续费事先显著提示、格式条款不得限制解除合同；知情同意、隐私授权等高权利项不得以现状为默认；数据必须可导出，否则现状偏好实为扣押
**可证伪条件**: 若在所有权被单独操纵、且惰性被明确阻断的实验中，损失厌恶通道对现状保留的解释力显著高于惰性与省略通道，则“惰性为主通道、损失厌恶为条件性放大器”这一判断被推翻，本记录应降级为“两条通道无法分离”并删除可分离测量的建议

**Mechanism**: The current state is over-weighted simply because it is current. Doing nothing is coded as not acting, and not acting is coded as safe.

**Design principles**:
- Distinguish inertia from loss aversion when you measure it; they predict different things about whether ownership exists
- Keep the change path exactly as short as the acquisition path — asymmetric effort is the dark-pattern version of this mechanism
- Mitigation: make the change path a first-class flow, show what the current state costs, and let data leave

---

## HB-14 · Optimism Bias
**Tier**: 常用
**Evidence**: B — **个人风险侧与总体规划侧分别评级，机制侧 B、聚合规划侧 C**。个人风险侧：Weinstein 1980 的"不比平均更可能"效应在健康、事故、寿命等领域跨文化重复，是可靠的小到中等效应；聚合规划侧证据明显更弱：Harris & Hahn 2011（*Psychological Review* 118(1):135–154）指出该效应很大程度是非现实比较标准造成的统计假象——当参照点改为真实分布的中位数而非"平均人"，大量乐观差距消失或被反转。争议：把"我不太可能遭遇坏事"（个人）与"这个项目会按时完成"（聚合）当作同一机制是本族最常犯的错误，前者稳健、后者与会低估任务的规划谬误混在一起且证据薄。
**Effect**: 个人风险判断侧小到中等且方向稳定（自评风险低于真实同类中位数）；**聚合规划侧效应不稳健**，改用真实分布作参照后大幅收缩，不可作为排期与预算承诺的依据

**机制链**: 遇到关于自身未来的风险或工期判断 → 自我相关信息被优先提取、失败案例被当作"与我不同"，同时非现实平均人参照点被当作比较基准 → 判断向有利方向偏离并低估所需时间与代价
**剂量**: 弱 在用户做出承诺前提供同类用户的真实分布（"完成者中位数是 21 天"），不做评价 ；中 真实分布 + 用户已完成的少量成功经历 + 明确乐观期限（"你上次用了 14 天"） ；强 真实分布 + 用户自评的乐观估计被公开记录并在到期时回访 + 提前完成可获得的社会可见奖励 ；过载 反复用"你一定可以按时完成"抬高承诺、事后又以未完成追责 → 用户识别为设局，之后对所有工期与风险提示一律按反向打折，真实的延期预警也失去作用
**时间动态**: 起效 一次自我相关判断即生效（分钟级） · 衰减 用户经历过一次自估与实际的大落差后，个人侧的乐观偏差明显收缩，收缩以"亲身落空的次数"计而非以时间计 · 饱和 在高频交付场景中反复落空会转为悲观偏差（自评风险反高于真实中位数），乐观偏差不是稳定常量而是可被经历翻转的状态
**调节变量**: 个体 情绪状态好、控制感强、对该任务无历史记录者最强；有本人历史数据、曾多次落空者最弱甚至反转 · 文化 强调积极自我呈现与集体士气的文化中更强且表达更公开，强调风险披露与谦逊规范的文化中弱 · 情境 首次承诺、时间跨度远、反馈延迟长时最强，有即时反馈与同类基数可比时最弱
**失效信号**: 用户自报工期与同类真实中位数持续背离且从不修正；承诺类文案的到期完成率显著低于基线；用户开始主动索要"别人花了多久"；延期预警的打开率骤降（已被乐观表态透支）
**可测代理**: 自估完成时间与同类真实中位数的比值；承诺到期完成率；有没有真实分布提示两组的交付准时率差；风险自评与真实发生率的校准曲线（Brier 分数）；同一用户第 1/2/3 次预测的偏差收敛速度
**交互**: × HB-18 规划谬误 → 乐观偏差负责"我比平均更可能成功"，规划谬误负责"这个任务比看上去简单"，两者叠加产生系统性的工期坍塌（COMBO-11 的任务承诺层）；× HB-06 可得性 → 成功案例可提取而自身失败案例难以提取，可得性为乐观偏差供给证据（COMBO-09）；× SD-01 社会证明 → 公开可见的成功者样本只呈现存活者，把乐观偏差固化为"大家都做到了"
**边界**: 不得用乐观框架隐藏风险或推迟披露不确定性——金融、医疗、信贷场景中对收益与风险的乐观表述构成误导性陈述（美国 FTC Act §5，中国《消费者权益保护法》第八条知情权与第二十条虚假宣传）；不得以乐观期限作为契约承诺而不附概率区间；健康与安全场景中乐观偏差会直接降低防护行为，须改为个人风险反馈而非鼓励性话术；**本记录的聚合规划侧证据为 C，不得作为排期工具的默认假设写入产品**
**可证伪条件**: 若把参照点从虚构的“平均人”改为真实同类分布的中位数后，用户的自评风险与同类真实发生率的差不再显著大于零，则“乐观偏差会系统性压低个人风险判断”的声称不成立，本记录应降级为“个人风险侧的效果主要由非现实比较标准制造，属测量假象”

**Mechanism**: Personal risk is judged below the real base rate, because the comparison standard is a fictional "average person" rather than the actual distribution. The aggregate-planning version of this is a much weaker and partly artifactual claim.

**Design principles**:
- Separate the personal-risk claim from the project-planning claim; they have different evidence and different remedies
- Replace the "average person" standard with the real distribution, or the measured gap is partly manufactured by your own wording
- Mitigation: give the user their own historical calibration, not encouragement

---

## HB-15 · Confirmation Bias
**Tier**: 常用
**Evidence**: B — **选择性接触与歧义解释分别评级**。歧义解释侧（同化偏差）证据强：Lord, Ross & Lepper 1979 让对立双方阅读同一批混合证据，双方都向各自原立场移动、分歧加大，该效应在后续研究中稳定重复。选择性接触侧弱且常被夸大：Hart, Albarracín, Eagly, Brechan, Lindberg & Merrill 2009（*Psychological Bulletin* 135(4):555–588）对 67 篇报告、91 项研究、约 8000 名被试的元分析给出的亲己信息偏好只有 **d≈0.36（中等偏小）**，且当态度已被先行支持、或议题与价值无关、或信息质量低、或用户开放性高时进一步减弱；更有力的反向证据是——当不一致信息与当前目标相关时，反而出现"偏向不一致信息"的逆向效应。故"人们只愿看与自己一致的信息"这一通俗表述被证据削弱。
**Effect**: 歧义解释侧中等且稳定（同一材料对不同立场者产生相反解读）；选择性接触侧小（d≈0.36）且条件性强，在信息与目标相关、或议题不涉价值观时可消失甚至反转；仅凭算法推荐解释立场极化是过度归因

**机制链**: 接触一批立场混合或含义模糊的信息 → 既有立场决定了哪些内容被优先加工、被记为支持性，模糊之处被补全为一致解读 → 事后立场比事前更极端，且双方都认为自己是客观的
**剂量**: 弱 在同一页面并列呈现支持与反对的证据摘要，不做标注 ；中 并列呈现 + 让用户先写下自己的判断再展开证据 + 标明每条的来源与局限 ；强 要求用户对相反证据给出可被他人检验的反驳（"请说明什么数据会让你改变看法"）+ 把该标准事先记录 ；过载 反复把用户推入同质信息环境并同时展示其"客观"自我评价 → 用户在被隔离的同时确信自己见多识广，极化与敌意同时上升，一旦接触外部证据会整体否认信息源而非修正判断
**时间动态**: 起效 单次接触歧义材料即可产生同化偏差（分钟级） · 衰减 被迫为相反立场生成解释（"考虑对立面"）可短暂削弱，但效果在数小时到数天内回落 · 饱和 长期同质信息暴露使极化固化，此时追加更多一致证据不再改变立场，只提高对异见的敌意
**调节变量**: 个体 封闭性高、对该议题有公开承诺、自我认同与该立场绑定者最强；开放性高、有为其立场辩护经验者最弱 · 文化 强立场与强群体认同议题（政治、宗教、健康）上最强，工具性、低涉入议题上接近零 · 情境 信息含义模糊、证据混合、用户有动机维持立场时最强，证据清楚且需向持异见者当面交代时最弱
**失效信号**: 用户在读完相反证据后立场分布反而更分散（说明材料被同化而非被评估）；社区里"客观""事实是"类措辞与敌意表述同步上升；用户只引用被自己复述过的材料、从不引用原文；跨立场的共同事实基础持续收缩
**可测代理**: 同一歧义材料的立场前后测偏移（按初始立场分层）；亲己信息点击份额（对照 d≈0.36 基线）；用户接触相反证据后的反驳类型分布（针对证据 vs 针对来源）；跨立场用户对同一事实陈述的认同率差
**交互**: × SD-01 社会证明 → 用户只看到同立场者的判断，把群体共识当作事实核验，选择性接触与从众互相加固（COMBO-04）；× HB-06 可得性 → 一致案例更易提取、相反案例被忽略，两个通道共同压低证据的多样性（COMBO-09）；× PA-01 处理流畅性 → 一致论断加工更流畅，流畅感被误读为正确性，加速立场固化（COMBO-06）
**边界**: 不得以制造信息茧房作为留存手段（算法推荐的同质化投喂在未成年人保护与内容治理规则下受约束，欧盟 DSA 第 34–35 条要求系统性风险与推荐机制评估）；社区治理不得把"质疑官方叙事"等同于"传播错误信息"来压制异见；健康与安全场景中不得利用同化偏差推动未经证实的疗法；**本记录中"算法推荐是极化主因"这一常见推论证据不足，不得作为删改推荐系统的唯一依据**
**可证伪条件**: 若在把证据的含义写清楚（消除歧义）后，对立立场者的前后判断偏移不显著大于零，或亲己信息偏好份额在信息与目标相关时不降反升，则“歧义解释偏差是同化机制的一部分”这一声称被推翻，本记录应降级为“选择性接触仅为 d≈0.36 的弱效应，极化不能归因于信息选择”

**Mechanism**: Ambiguous evidence is assimilated toward the prior position, and people preferentially but only mildly seek congenial information. The interpretation effect is the strong one; the selective-exposure effect is real but modest and heavily conditional.

**Design principles**:
- Grade the two mechanisms separately — the strong one (assimilation) and the weak one (selective exposure) have different evidence and different remedies
- Ask the user for their own disconfirmation standard before showing evidence, and record it
- Mitigation: mixed evidence plus source quality beats "show both sides" alone

---

## HB-16 · Dunning-Kruger
**Tier**: 情境
**Evidence**: C — **机制侧与"无知者无法自知"的强声称分开评级，后者按单研究加统计批评记 C**。Kruger & Dunning 1999 报告低能力者高估自己的百分位、高能力者低估自己。争议是该图形被广泛误读：Gignac & Zajenkowski 2020（*Intelligence* 80:101449）论证经典的"低能力者高估、高能力者低估"交叉图案很大程度是回归到均值与测量误差的统计假象——用异方差检验与二次回归可分离出真实的元认知成分，而真实成分比通俗版本小得多且**领域特异**；把两个组的观察分数直接比较在方法论上无效。仍站得住的部分：在**同一领域内**、有客观评分且被试对自身百分位做出估计时，低分位者的自我评估偏差确实大于高分位者，但幅度远小于"越无知越自信"的传播版本，且不跨领域迁移。
**Effect**: 小；仅在同一领域、有客观评分、被试需自评相对位置时，低分位者高估与高分位者低估的差可观察到，且幅度随领域差异与经验上升而消失；"跨领域的自信与能力脱钩"无证据支持，不能作为通用规律

**机制链**: 用户在某领域缺少判断该领域表现所需的技能 → 判断标准本身不可靠，导致自我评估向均值附近收缩并偏向有利方向 → 自评相对位置与真实相对位置脱节，且不随自信程度改善
**剂量**: 弱 提供同龄段或同水平的真实分布作为参照（"多数用户在第 3 次练习后达到 X"），不评价个人 ；中 真实分布 + 一次低风险、可失败的诊断性任务 + 结果直接反馈给用户本人 ；强 真实分布 + 诊断任务 + 把结果与后续推荐内容难度绑定（自评过高者先给基础内容）+ 允许随时重测 ；过载 把能力评估结果公开排名或用作准入资格（"你不适合本课程"）→ 用户读作羞辱与精英筛选，低分位者退出而非提升、并公开指控该评估无依据，机制由纠偏转为排斥
**时间动态**: 起效 在首次拿到关于自身的客观评分时（分钟级） · 衰减 单次反馈的自评校正在一到两周内被日常经验稀释，缺少重复测评即回落 · 饱和 重复同一诊断任务后用户学会该任务的评价标准并据以作答，自评开始贴合分数而非能力，测量本身失效
**调节变量**: 个体 领域新手、缺少该领域反馈史、自我评价与他人评价长期脱节者偏差最大；有密集外部反馈（竞赛、专业评审、公开测试）者最弱 · 文化 高自我肯定与鼓励性评价文化中自评普遍上移，压缩了可观察的偏差；谦逊规范强的文化中高能力者的低估更明显 · 情境 任务难度中等、反馈延迟长、无外部基准时偏差最大，标准清晰、结果即时、有可比同伴时最小
**失效信号**: 自评排名与实测排名的相关系数在多个领域上都不显著（说明该效应不可泛化）；用户在被给出诊断结果后仍重复相同的过难选择；同一用户第 2/3 次测评的自评与实测差值收敛但实测分数不升（说明学会的是测题而非能力）；测评被用户当作侮辱并以投诉回应
**可测代理**: 自评百分位与实测百分位的差，按实测分位分层（检验是否呈交叉图案）；用二次回归与异方差检验分离出的真实元认知成分；同一用户跨领域自评偏差的相关（检验是否领域特异）；诊断任务的第 1/2/3 次重测中实测分数与自评差的走势
**交互**: × HB-14 乐观偏差 → 乐观偏差提供"我比平均好"的基线，DK 提供"我无法判断自己在这个领域的位置"，两者叠加使新手在陌生领域最敢下重注（COMBO-11 的难度校准层）；× HB-06 可得性 → 用户只能提取到自己的少数成功案例，无法提取同类的整体分布，自评因此缺少校正输入；× MR-06 进度动量 → 初期的虚假进度感为过高自评提供证据，把 DK 偏差与伪进度绑定
**边界**: 不得将能力评估结果用于公开排名、准入资格或人格评价——把统计上的分位差当作"人是否自知"的一般判断，既超出证据也构成歧视风险（招聘与教育场景尤其）；不得用该机制羞辱用户或推动其购买更高级别的内容；**本记录整体按 C 标注，且"低能力者不知道自己无能"这一通俗结论已被证明主要来自统计假象，任何以该结论为前提的产品设计（自评即分级、跨领域难度推荐）都不应上线**
**可证伪条件**: 若用异方差检验与二次回归分离出的真实元认知成分在多个领域上都不显著大于零，或跨领域的自评偏差相关显著（说明不自领域特异），则“元认知赤字真实存在但领域特异且幅度小”这一判断不成立，本记录应降级为“经典交叉图案完全由回归到均值造成，不保留任何能力自评的应用建议”

**Mechanism**: Within one domain and against objective scoring, the lowest performers over-estimate their own standing more than the highest performers under-estimate theirs. The famous crossing graph is largely a regression-to-the-mean artefact, and the surviving deficit is small and domain-specific.

**Design principles**:
- Test the two halves separately: over-estimation by low scorers and under-estimation by high scorers are not one fact
- Never generalise a domain-specific measurement into a claim about a person's self-knowledge in general
- Mitigation: give the user their own measurement history, not a label

---

## HB-17 · Gambler's Fallacy
**Tier**: 情境
**Evidence**: B — **"误解独立序列"侧与"热手存在"侧必须分开陈述，二者不能互相取消**。误解独立序列：Tversky & Kahneman 1971 的"小数定律"与 Gilovich, Vallone & Tversky 1985 的篮球研究支持人们把独立结果串读成有规律的趋势（认为该进了、或该反转了）。但该文献本身被纠正：Miller & Sanjurjo 2018（*Econometrica* 86(6):2019–2047）证明原始热手分析带有选择偏差——在有限序列上按条件频率估计会系统性地低估热手，纠偏后热手效应在部分领域（尤其是可由技能影响的连续任务）真实存在，且在职业篮球的后续重分析中可被检出。因此正确表述是：**人们会误读独立序列，但真实序列并非全部独立**；把两者混为一谈会同时犯下"到处看见趋势"与"否认任何趋势"的两种错误。
**Effect**: 小到中等且方向依任务可分性而定：在结果确实独立且用户可验证其独立性的场景（彩票、轮盘、独立抽卡）中，人们会高估"该反转了"，此为可用杠杆；在结果可由技能或隐藏机制影响的场景中，人们会高估连串的可延续性，此时利用"该反转了"的设计与真实分布相反，会同时降低体验与收益

**机制链**: 用户观察到一串同向结果 → 该序列被套用"小数定律"，被读作必须自我平衡的过程而非独立抽样 → 用户据"该反转了"或"该延续了"调整下一次的投入与选择
**剂量**: 弱 如实展示历史结果序列，不做任何提示（历史本身即可诱发误读，且无操纵） ；中 展示历史序列 + 一个真实且用户可核验的机制说明（"每次抽取独立重置"或"命中率随熟练度上升"），把可推断性交给用户 ；强 展示序列 + 与用户投入挂钩的补偿机制（连败后提高回报"保底"），该机制真实生效且规则公开 ；过载 在不独立、可由技能影响的场景中伪装"该反转了"（隐藏真实衰减/难度递增，诱导用户在应当提升时停手），或反过来在独立场景中暗示"连中会延续" → 用户以真实结果核算后认定机制造假，不仅停止投入还公开揭露算法，此后任何保底或概率披露都不被采信
**时间动态**: 起效 观察到 3–5 个同向结果即可出现（分钟级） · 衰减 用户获得机制的真实说明并亲自验证一次后，误读明显减弱，减弱以"亲自验证的次数"计 · 饱和 长期在同一序列上使用反转或延续框架，用户会自行估计出真实分布，机制失去作用并转为对平台的怀疑
**调节变量**: 个体 统计训练低、对该机制无内幕知识、投入情绪高涨（刚输或刚连胜）者最强；有概率训练或可自行模拟者最弱 · 文化 博彩与运气文化浓厚的社会中反转直觉的语汇更完备、表达更公开，但实际行为差异小于自我报告差异 · 情境 结果独立且不可验证时反转直觉最强，机制公开、可核验、样本量大时最弱；连续结果的可见数量越多，误读越强
**失效信号**: 用户在连败后集中加码而后续真实命中率不变（保底被当作概率补偿）；用户自述"该赢了"类归因占比上升；保底机制上线后人均投入上升但活跃留存不升；用户开始自行记录并公开真实分布，与平台展示的序列发生冲突
**可测代理**: 连败后下一次投入金额相对基线的变化；用户对"独立性"的认知测题得分与投入行为的相关；保底机制组的投入曲线与无保底组对照；用户自算分布与平台展示分布的一致率；同一用户在被明确告知机制前后的下注分布偏移
**交互**: × MR-11 近端失误 → 近失误提供"差一点就中"，赌徒谬误提供"该轮到我了"，两者把随机序列读成即将兑现的过程（COMBO-05 的再参与层）；× AD-01 可变比率强化 → 变量奖励本身制造"再试一次"的动力，赌徒谬误为其提供理由，构成 COMBO-02 的核心循环；× HB-08 沉没成本 → 已投入的金额使继续被解读为摊平损失而非独立决策（COMBO-03）
**边界**: 不得在真实独立场景中暗示连串必然延续，也不得在非独立场景中伪装反转——两者都是对结果分布的虚假表示（中国《反不正当竞争法》第八条虚假宣传，以及赌博类产品的特别法约束）；不得对未成年人、或已知问题赌博人群设计保底与近失误组合；保底机制必须真实生效且规则公开可核验，否则构成欺诈；**不得把本机制用于投资加仓、赌博与任何会造成实质损失的场景**
**可证伪条件**: 若在结果确实独立且机制公开可核验的场景中，用户对“该反转了”的倾向不显著高于按真实概率作答，或在可由技能影响的任务中纠偏后的热手效应不显著大于零，则“两种误读可分别利用”的声称不成立，本记录应降级为“序列误读在两类任务上无法区分，不能作为设计依据”

**Mechanism**: Independent sequences are misread as self-correcting, and skill-influenced sequences are misread as random. These are two opposite errors, and the original analysis that measured the second was itself biased.

**Design principles**:
- Determine whether the process is actually independent before choosing a streak design; the two cases need opposite mechanics
- Publish the real distribution and let the user verify it — a hidden generator cannot be audited and will be assumed fake
- Mitigation: real, rule-disclosed pity timers only where the underlying process is genuinely independent

---

## HB-18 · Planning Fallacy
**Tier**: 核心
**Evidence**: B — Kahneman & Tversky 1979 提出内部视角／外部视角之分；Buehler, Griffin & Ross 1994 的系列实验给出稳定的低估（自估完成时间普遍短于实际）。争议：①该效应与乐观偏差、策略性虚报（为获批而故意低报）高度混淆，现场估算同时受诚实偏差与激励偏差驱动，两者需分别测量；②**补救措施的证据比偏差本身的证据更关键**：Flyvbjerg 的参考类别预测（reference class forecasting）在交通与基建项目的实证中确实降低低估，说明有效修正是更换参照分布而非要求人"更努力思考"；③对参考类别预测本身也有批评（类别选择、样本可得性与外部效度），其效果依赖可比项目的真实数据是否可得。
**Effect**: 中等偏大且方向稳定（自估工期／成本系统性低于实际），但效应的一部分来自激励性虚报而非认知偏差；可用参考类别预测显著压缩低估，而"提醒要谨慎""要求更仔细估算"的干预几乎无效

**机制链**: 用户被要求估算一个未来任务的工期或成本 → 以内部视角聚焦该任务的具体细节与最佳路径，忽略同类任务的历史分布 → 估算落在最优情形附近并系统性低于实际
**剂量**: 弱 在输入框旁展示同类任务的真实中位数与四分位（"同类任务中位 21 天"），不做默认填充 ；中 真实分布 + 要求用户先写出步骤再给总估 + 到期自动记录实际值回填其个人历史 ；强 真实分布 + 个人历史校准 + 到期回访对比 + 把估算偏差作为可见的个人指标（不作考核） ；过载 把估算偏差用于绩效考核或惩罚，或反复以"你总是高估自己"羞辱用户 → 用户转为策略性高估以自保（缓冲估算），参照分布失去信息价值，管理决策被系统性污染
**时间动态**: 起效 首次估算即出现（分钟级） · 衰减 用户在获得 2–3 次本人估算与实际的对照后，个人侧低估明显收缩 · 饱和 若把偏差与考核挂钩，饱和方向反转：用户学会稳定高估并预留缓冲，此时记录到的不再是认知偏差而是策略行为
**调节变量**: 个体 首次做该任务、对该类任务无历史数据、控制感强者最强；有个人历史校准数据者最弱 · 文化 高不确定性规避文化中估算更保守（低估幅度小但预留缓冲多），强调积极进取与承诺的文化中低估更大 · 情境 任务新颖、步骤多、依赖外部方、反馈延迟长时最强；任务重复、步骤已知、有可比项目数据时最弱
**失效信号**: 估算与实际的中位比值长期超过 1.3 且不随经验改善；用户开始自行加固定缓冲（说明估算已不可信）；同一用户在被要求谨慎估算后偏差不变（说明干预无效）；到期回填率低（说明用户不愿面对对照）
**可测代理**: 估算值与实际完成时间／成本的中位比值；第 1/2/3 次估算的偏差收敛曲线；有／无参考类别提示两组的偏差差；个人历史回填率；缓冲系数（自报估算与内部真实预期的差）
**交互**: × HB-14 乐观偏差 → 乐观偏差使"我比平均快"成立，规划谬误使"这个任务比看上去简单"成立，两者共同产生工期坍塌（COMBO-11 的任务承诺层）；× HB-08 沉没成本 → 项目超期后继续投入被解释为"已经做到这一步"，规划错误因此不会被及时中止（COMBO-03）；× SD-01 社会证明 → 只展示按期完成的成功者样本，使用户的外部参照失真，加固内部视角
**边界**: 不得用乐观工期承诺作为对他人的契约而不附概率区间——面向客户的交付承诺适用合同法与消费者权益保护（虚假承诺、误导性商业宣传）；不得将工期估算偏差用于绩效考核或人格评价（会把认知偏差转成策略性虚报，污染数据）；金融、医疗、工程等高风险交付中必须使用参考类别预测而非个人估算；**参考类别预测需要真实可比项目数据，无此类数据时不得假装可量化**
**可证伪条件**: 若在给出同类项目真实分布的参考类别预测组，其估算与实际的偏差不显著小于仅提供“请仔细估算”提示的对照组，则“更换参照分布才能修正规划谬误”的声称被推翻，本记录应降级为“低估无法通过外部视角缓解，仅记录为观察现象”并删除参考类别预测的推荐

**Mechanism**: Tasks are estimated from the inside view — the specific plan and its best case — while the distribution of similar past tasks is ignored. The effective remedy is replacing the reference class, not asking for more effort.

**Design principles**:
- Give the outside view as a default, not as advice: a distribution beats "please estimate carefully"
- Separate honest underestimation from strategic low-balling by measuring who bears the cost of overrun
- Mitigation: reference class forecasting, personal calibration history, and never attaching the deviation to a performance penalty

---
