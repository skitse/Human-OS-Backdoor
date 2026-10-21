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
