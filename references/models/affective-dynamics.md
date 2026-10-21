# Affective Dynamics — Model Details

## AD-01 · Variable Ratio Reinforcement
**Tier**: 核心
**Evidence**: B — Ferster & Skinner 1957 的强化程式比较确立了变动比率在消退抵抗上的优势，该结论在动物实验中高度可复现。争议与修正：Skinner 之后，"多巴胺=快乐"的读法已被推翻——Berridge & Robinson 1998 起的一系列实验把多巴胺定位为"想要（wanting/salience）"而非"喜欢（liking/hedonic pleasure）"，伏隔核的多巴胺耗竭消除寻求行为却不消除享受反应；因此变动比率放大的不是愉悦，而是"寻求"本身，这解释了为何该机制能在体验并不愉快时仍维持行为。另一争议：人类行为成瘾的强证据主要来自赌博机与社媒的观察与准实验研究，随机对照的因果证据有限，"可变比率=成瘾"的强断言应降级为"可变比率显著提高消退抵抗与寻求频率"
**Effect**: 大（消退抵抗为各强化程式之最），但仅当奖励不可预测且与"下一次可能更好"的信念绑定；一旦奖励可被用户预测或可被完全跳过，消退抵抗回落至固定程式水平

**机制链**: 奖励时有时无且不可预测 → 中脑多巴胺系统被维持在"预期但不保证"的寻求状态 → 检查行为以高于奖励实际产出率的频率持续
**剂量**: 弱 内容或奖励质量有自然波动，但不刻意设计（算法按相关性排序，不按随机化） ；中 每次交互的奖励质量确实不可预测 + 明确的停止点（有限流、有结尾） ；强 无限流 + 随机化奖励 + 无自然停止点 + 每次检查都极低成本（下拉即刷新） ；过载 变动比率叠加强负性事件（连续多次空手）→ 消退爆发：用户在一次高期待落空后出现"厌恶式卸载"，且此后对该品类的任何随机奖励都主动回避，比从未接触过的用户留存更低
**时间动态**: 起效 分钟级（首次不可预测奖励即建立期待） · 衰减 奖励质量持续低于期待时，消退抵抗表现为"延长挣扎"而非立即停止——行为先升后断崖，中断往往由一次显著失望触发 · 饱和 长期暴露后寻求频率维持在高原但主观效用持续下降，形成"用而不乐"的稳定状态（这正是 wanting/liking 分离的行为表现）
**调节变量**: 个体 冲动性高、延迟满足能力低、基线多巴胺反应性强（新奇寻求特质）者效应最强，有明确外部目标与时间预算者显著减弱 · 文化 高不确定性规避文化中随机奖励的吸引力弱于确定性收益，集体主义市场对社会性奖励（他人可见）比对纯随机奖励更敏感 · 情境 空闲、疲劳、情绪低落、无替代活动时最强，有明确任务与时间约束时最弱
**失效信号**: 使用时长上升但自评满意度与净推荐值同步下降（用而不乐）；会话数以"短而多"替代"长而深"，单次会话时长下降而日均开启次数上升；用户主动开启"减少推荐""关闭推送"等抑制功能；卸载集中发生在一次高期待落空之后，而非渐进流失
**可测代理**: 奖励产出的实际分布与用户检查频率之比（寻求/获得比）；单次会话时长与日均开启次数的反向变动；"减少推荐/关闭推送"开关的开启率；卸载前最后一次交互的奖励质量（可用会话日志回溯）
**交互**: × AD-02 蔡格尼克效应 → 未完成项提供"必须回来"的理由，变动比率提供"回来可能有奖"的理由，二者叠加使停止点消失（COMBO-02）；× AD-10 信息缺口 → 缺口制造寻求动机、变动比率决定寻求频率，是 COMBO-02 的第三层；× MR-12 奖励变异性 → 二者属同一机制的不同表述，计功时不可叠加
**边界**: 不得用于未成年人、赌博类产品、情绪障碍与成瘾易感人群（此为该机制的绝对红线，非可调参数）；不得以"提升参与"为名把变动比率用于福祉敏感场景；一旦设计目标是延长使用时长而非改善结果，即应视为需要伦理审查的设计；产品须提供自然停止点与使用时长可见性
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.97；Effect Size: Extreme (highest of all behavioral mechanisms)

**Mechanism**: Rewards delivered on an unpredictable schedule create the strongest and most resistant-to-extinction behavior patterns. This is the slot machine effect — the uncertainty itself is the reward.

**Schedule comparison** (extinction resistance):
```
Fixed ratio (every Nth action):    Low resistance — stops immediately when reward stops
Fixed interval (every N minutes):   Low resistance — behavior spikes just before reward
Variable ratio (unpredictable):     MAXIMUM resistance — behavior persists indefinitely
Variable interval (unpredictable):  High resistance
```

**Why it works**: Dopamine fires not just on reward delivery but on REWARD ANTICIPATION. Variable schedules keep dopamine system in constant anticipatory state.

**Implementation**:
```
Pull-to-refresh: Will there be new content? (variable reward) -> frequent checking
Loot boxes: Unknown reward → open one more
Feed scroll: Each scroll might reveal something interesting → infinite scroll
Push notifications: Might be something important → always check
Game drops: Rare item might appear → keep grinding
Email check: Might be important news -> frequent checking
Dating apps: Swipe → might match → keep swiping
Flash sales: Might be a great deal → check daily
```

**Design principles**:
- Variable rewards can increase engagement, but they should be used carefully and transparently
- Make reward checks cheap only when repeated checking is genuinely aligned with user value
- Avoid uncertainty loops that mainly increase reflexive checking without improving outcomes
- Mitigation: Fixed schedules and transparent reward systems reduce compulsion risk

**Combos**: Variable Ratio × Goal Gradient -> "almost there" + uncertain timing increases re-engagement pressure
Variable Ratio × Zeigarnik → incompleteness + uncertainty = maximum mental occupation

---

## AD-02 · Zeigarnik Effect
**Tier**: 常用
**Evidence**: B — Zeigarnik 1927 的原始观察；后续对"未完成任务被更好回忆"的复现结果混杂，Van Bergen 1968 的综述与近期重复实验显示效应量远小于教科书叙述，且高度依赖任务被打断的方式与被试的完成动机。争议核心：现代解释多认为这是"未完成状态在目标层级中保持激活"（目标激活/注意残留）而非独立的记忆优势，因此当任务被明确放弃或用户不再持有完成意图时效应消失——把它当作"只要留下未完成状态就能钩住用户"是过度外推
**Effect**: 中等偏小；仅在用户已持有完成意图、且中断是外部造成时稳定；用户主动放弃或对任务无兴趣时效应为零

**机制链**: 任务被启动但未完成 → 未达成目标在记忆中保持激活并持续占用注意 → 用户产生返回并完成的驱动力
**剂量**: 弱 显示完成度（"资料完成 60%"），可随时关闭提示 ；中 明确的缺失项清单 + 一键继续入口 + 在用户自然回访时提示 ；强 多个并行未完成项 + 社交可见的未完成状态 + 每次回访都刷新未完成清单 ；过载 未完成项数量超过用户可管理的范围（十余个并行进度条、永不闭合的清单）→ 认知负荷与失败感超过驱动力，用户以"全部放弃"来解除张力，留存低于不显示进度的对照组
**时间动态**: 起效 分钟级（启动即产生张力） · 衰减 未完成状态在数天内保持激活，之后转为背景噪音；超过约一周未回访的未完成项不再产生驱动力 · 饱和 反复开启新任务而不闭合旧任务会耗尽该效应，用户对进度提示脱敏
**调节变量**: 个体 尽责性高、目标导向强、有完成习惯者效应最强，低尽责性与"收藏即完成"型用户几乎无效 · 文化 高不确定性规避与高成就导向文化中"未完成"更令人不适，效应更强 · 情境 用户已投入且中断由外部造成时最强，任务本身无意义或用户已明确放弃时最弱
**失效信号**: 进度提示的点击率随时间单调下降而提示数量不变；用户批量关闭/清除未完成项（而非逐个完成）；"继续"入口曝光→点击转化低于冷启动入口；未完成清单越长，整体回访率越低（过载的直接证据）
**可测代理**: 未完成清单长度与 7 日回访率的曲线关系（找拐点）；"继续"提示的第 n 次曝光点击率；用户清除/关闭未完成项的行为频次；完成率与清单长度的相关性
**交互**: × AD-10 信息缺口 → 未完成提供"欠着"的张力、缺口提供"不知道"的张力，两者同时闭合才解除（COMBO-02）；× AD-01 变动比率 → 蔡格尼克保证会回来，变动比率保证回来得频繁（COMBO-02）；× HB-02 损失厌恶 → "进度会过期"把未完成从张力升级为损失
**边界**: 不得制造无法完成的伪进度（虚假百分比、永远差一步的进度条）；不得对未成年人使用"未完成焦虑"型留存设计；用户明确表示不感兴趣后须停止提示（GDPR/《个人信息保护法》下的营销拒绝权）；未完成清单必须可一次性清除
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.88；Effect Size: Medium-Large

**Mechanism**: People remember and think about incomplete tasks far more than completed ones. Incompleteness creates a persistent cognitive loop demanding resolution.

**The tension**: Starting something creates a "task tension" that doesn't resolve until completion. This tension is aversive — people feel compelled to complete what they've started.

**Implementation**:
```
Onboarding: "Your profile is 60% complete" → visible incomplete state
Progress bars: Explicitly show what's missing, not just what's done
Courses: "3 of 7 lessons complete" → the 4 missing ones nag
Series: Cliffhanger episode endings → must watch next
Email sequences: "Part 2 of 5" → implies 4 incomplete parts
Checkout: "You left items in your cart" → abandoned = incomplete
Reading: "5 min read" shown upfront → start = commit to finish
Games: Quest log with incomplete items → must return to finish
```

**The cliffhanger formula**:
> Start an arc → introduce tension → cut before resolution → re-engagement is automatic

**Design principles**:
- Make incompleteness visible and salient
- Make completing the action cheap (low effort)
- Time the incompleteness reminder at re-engagement moments
- Mitigation: Allow easy "dismiss" / "mark complete later" options

**Combos**: Zeigarnik × Information Gap → "you won't know the outcome until you return"
Zeigarnik × Loss Aversion → "your progress will expire if you don't complete"

---

## AD-03 · Peak-End Rule
**Tier**: 常用
**Evidence**: B — Kahneman, Fredrickson, Schreiber & Redelmeier 1993 的冷压与结肠镜研究；"峰终"在回顾性疼痛评价中稳定复现。争议：该规则对"整体回顾性评价"有效，但对"是否再次选择"的预测力弱于叙述中的暗示——Ariely & Carmon 2000 及后续研究显示，选择行为更多由当下预期与记忆之外的动机驱动；此外"时长忽视"并非普遍：当体验被分段或被赋予意义时，时长重新进入评价。因此峰终不应被当作"体验可以随便拉长"的许可
**Effect**: 中等；对回顾性评分与口碑的影响稳定，对复购与推荐行为的预测力较弱；体验被分段、被赋予意义或用户有客观指标可比时效应缩小

**机制链**: 体验结束时记忆被重建 → 峰值与结尾两个时点的强度在重建中获得不成比例的权重，时长被忽略 → 后续评价、口碑与再选择依据该重建结果
**剂量**: 弱 在流程末尾给一次明确的完成反馈（"已完成，这是你的结果"），不改动过程 ；中 在过程中设置一个有意义的峰值（首个真实成果）+ 结尾的收束动作（总结、成就） ；强 峰值前置到体验前三分之一 + 结尾给情绪高点（庆祝、社会分享）+ 全程无负面尾巴（不在末尾要评价、不在末尾推升级） ；过载 过度加工峰值与结尾（夸张庆祝、强制分享、每个流程都放烟花）→ 峰值通胀，用户把结尾设计识别为操纵，回顾评价反降，且真实峰值被噪音淹没
**时间动态**: 起效 体验结束时立即形成（回顾性评价在结束瞬间定型） · 衰减 记忆在数天内由细节转向概括，峰值与结尾的权重进一步上升，但具体内容失真 · 饱和 反复的"庆祝式结尾"使情绪高点钝化，需要不断加码，最终失效
**调节变量**: 个体 情绪反应强度高、经验开放性高者受峰值影响更大，分析型用户更依赖客观指标而非感受 · 文化 高情绪表达文化对结尾仪式反应更强，高克制文化中夸张庆祝反而引发尴尬 · 情境 体验短、不可重复、无客观对比指标时最强，可重复、可比价、有量化结果时最弱
**失效信号**: 结尾情绪设计的曝光与回顾评分不相关；用户在评价中主动复述中间环节的负面细节（说明峰值未被结尾覆盖）；强制分享率上升但分享后回流率下降；同一流程加码庆祝后 NPS 不升反降
**可测代理**: 体验结束即时评分与 7 日/30 日回顾评分的差；结尾设计 A/B 对 NPS 与复购的影响；用户在开放题中提及的时刻分布（峰值/结尾 vs 中段）；强制分享的接受率与分享后回流量
**交互**: × PA-10 序列位置效应 → 结尾之所以权重高，部分是序列位置的近因效应，二者共用同一底层，计功时需注意重叠；× HB-02 损失厌恶 → 结尾若出现"你将失去"信息，会覆盖此前所有正向峰值；× SD-01 社会证明 → 结尾的社会分享把私人峰值转为公开承诺，记忆被外部固化
**边界**: 不得用强结尾掩盖过程中的实质问题（尤其是医疗、金融、客服纠纷等用户已受损的场景，掩盖构成二次伤害）；不得在结尾强制索取好评或分享（违反平台评价规范与 FTC 关于评价操纵的规则）；负面体验的结尾加工不得用于降低投诉意愿
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.84；Effect Size: Medium-Large (Kahneman's most replicated finding)

**Mechanism**: People's memory of an experience is determined primarily by:
1. The peak emotional moment (most intense, positive or negative)
2. The ending moment

The duration of the experience barely matters ("duration neglect").

**Formula**: Memory(experience) ≈ (Peak + End) / 2

**Implications**:
- A good experience ending badly is remembered worse than a shorter good experience
- A mediocre experience with a great ending is remembered better than it was
- You can recover a bad experience with a strong ending

**Implementation**:
```
Onboarding: End with a "magic moment" (the aha moment) → first impression memory
Purchase confirmation: End with celebration / social share → positive last memory
Customer service: Resolve the issue AND add unexpected positive gesture at end
Product exits: "Are you sure you want to cancel?" + show achievement summary
Courses: Graduation ceremony / certificate at end → peak memory
Event: Save best speaker / moment for near-end
Email: Strong CTA or value at end, not just in middle
App session end: "You achieved X today" → positive ending memory
```

---

## AD-06 · Fear/Threat Response
**Tier**: 常用
**Evidence**: B — Leventhal 1970 与 Rogers 1975 的保护动机理论确立了"威胁 + 效能"的双通道；Witte & Allen 2000 对 98 项研究的 meta 分析显示恐惧诉求对态度与行为有中等正向效应，但显著受"感知效能"调节。争议：Tannenbaum et al. 2015 的更大规模 meta 分析确认平均效应为正，同时明确指出高恐惧 + 低效能条件下效应转为防御性回避（否认、拖延、攻击信源）；此外恐惧诉求的现场研究多测量态度与意向，对真实行为的长期效应证据薄弱，且重复暴露会快速习惯化
**Effect**: 中等，且严格条件化：仅当威胁被感知为高严重性 + 高易感性、同时给出了具体可行且高效能的应对路径时为正；高效能缺失时效应反转为回避

**机制链**: 威胁线索被评估为高严重性且与自身相关 → 恐惧唤醒提升注意与唤醒水平，并激活应对评估 → 采取所提供的行为（高效能时）或转入防御性回避（低效能时）
**剂量**: 弱 中性陈述风险并附可执行的第一步（"这类情况每年影响 X% 的人，你可以用 Y 检查"） ；中 具体化到用户自身处境的风险 + 明确的应对路径 + 效能证据（"已有 N 人用这个方法解决"） ；强 高严重性 + 高易感性 + 时间压力 + 唯一可行路径，且该路径就是产品本身 ；过载 恐惧强度超过用户感知效能（"不处理会致命"却没有可信的解决办法）→ 防御性回避：用户否认风险、关闭页面、攻击信源，行为改变为零甚至反向（回避筛查、拒绝信息）
**时间动态**: 起效 秒级（威胁评估即时） · 衰减 单次恐惧诉求的驱动在数小时到数天内衰减；重复同一威胁在 2–3 次后习惯化 · 饱和 长期使用恐惧框架会使受众整体脱敏，并抬高其对同类信息的怀疑基线，损害该渠道后续所有真实风险沟通
**调节变量**: 个体 自我效能感高者把恐惧转为行动，低自我效能与高特质焦虑者转为回避；反应效能（"这办法真有用吗"）比威胁强度更能预测行为 · 文化 高集体主义文化中社会性威胁（他人评价、家庭影响）强于个人健康威胁，高不确定性规避文化对模糊威胁的回避更强 · 情境 有明确可执行的下一步、且用户处于可行动窗口时最强，无解法、无时间、或用户已无力应对时最弱
**失效信号**: 恐惧文案曝光组的页面跳出率与关闭率显著高于对照；行为意向上升但实际行为不变（经典的高恐惧低行动组合）；同一威胁的第二、三次触达打开率断崖下降；用户投诉中出现"制造焦虑""贩卖恐慌"表述；筛查/咨询的预约完成率不升反降
**可测代理**: 恐惧强度分层的转化与跳出率曲线（找反转点）；"效能提示"有无的分臂对比（效能缺失组应出现回避）；威胁触达第 n 次的打开率；从文案曝光到实际行为完成的漏斗（意向→行为的转化率是关键指标）
**交互**: × HB-02 损失厌恶 → 恐惧提供唤醒、损失厌恶提供具体的"将失去什么"，两者叠加时紧迫感最强但也最快触发逆反；× MR-05 自我决定理论 → 效能感是恐惧转行动的必要条件，自主支持型文案显著优于控制型；× SD-04 权威偏误 → 权威来源提高威胁可信度，但也提高被识破后的信任崩塌幅度
**边界**: 不得用于无真实解法或解法即产品自身的场景（制造疾病再卖药，属欺诈与重大伦理违规）；健康、金融、人身安全场景须由具备资质的专业人士审核，并同时提供绝对风险与基准率；不得针对未成年人、患者、丧亲者等脆弱群体；恐惧诉求一旦被判定为贩卖焦虑，其信任损失外溢到品牌全部沟通
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.90；Effect Size: Large

**Mechanism**: Threat perception activates fight-or-flight response, which heightens loss aversion and drives immediate action. Fear is the most powerful short-term motivator.

**Three fear types**:
1. **Loss fear**: "You'll lose [specific thing]"
2. **Social fear**: "Others will judge/exclude you"
3. **Existential fear**: "Your future self will regret this"

**Implementation**:
```
Loss fear: "Your 30-day streak ends tonight if you don't complete today's lesson"
Social fear: "Your competitor just added this feature"
Regret fear: "By 2025, people who didn't learn [skill] will earn 40% less"
Security fear: "Your account shows suspicious login activity" (then upsell 2FA)
Health: "People with your habits have 3× higher risk of X"
Financial: "At your current rate, you'll run out of savings in 8 years"
```

**The threat-action-relief loop**:
> Introduce threat → create urgency → offer solution → relief from resolving fear

**Warning**: Fear appeals must be paired with a clear, achievable solution. Fear without path = paralysis, not action. High-fear + low-efficacy → denial and avoidance.

**Calibration**: Use fear for retention and urgency, not for first impressions (trust builds before fear).

---

## AD-08 · Flow State
**Tier**: 常用
**Evidence**: B — Csikszentmihalyi 1975 起的经验采样研究确立了心流的现象学特征与"技能-挑战匹配"条件。争议：心流的核心命题"挑战略高于技能"多为相关证据——经验采样只能显示匹配与主观心流共变，难以排除"处于心流时更愿意报告高挑战"的反向因果；此外"心流=高绩效"的推论缺乏稳健的因果证据，部分研究发现心流状态下对意外刺激的觉察下降（隧道视觉），在高风险任务中反而是风险因素；心流构念本身的测量效度也长期受批评
**Effect**: 中等；对主观投入度与坚持意愿的影响稳定，对客观产出的提升证据薄弱；挑战-技能匹配的窗口窄，且个体差异大

**机制链**: 任务难度略高于当前技能且反馈即时 → 注意资源被任务全部占用，自我监控与时间感暂时关闭 → 深度投入并持续延长任务时间
**剂量**: 弱 移除主任务路径上的干扰与打断，难度不变 ；中 自适应难度（按表现微调）+ 即时反馈 + 明确目标 ；强 自适应难度 + 即时反馈 + 无打断的全屏环境 + 难度随技能实时爬升 ；过载 难度持续爬升超过技能增长（或反馈被移除、打断频繁）→ 从心流直接跌入焦虑或挫败，且因为此前投入高，跌落时的放弃概率高于从未进入心流的用户
**时间动态**: 起效 分钟级（通常需数分钟无打断的连续投入） · 衰减 一次打断后需数分钟重新进入；打断频率高于每 10 分钟一次则无法形成 · 饱和 单次心流时长有生理上限（数十分钟到数小时），之后疲劳使技能实际下降，同一难度转为过载
**调节变量**: 个体 该领域技能水平决定匹配点，注意控制力高、容忍模糊者更易进入；焦虑特质高者窗口更窄 · 文化 对"过程导向"评价更高的文化中心流本身即被当作收益，结果导向文化中用户更在意产出因而对心流不敏感 · 情境 无打断、目标清晰、反馈即时、有自主控制权时最强，多任务、被监控、被动接受节奏时最弱
**失效信号**: 会话中打断次数与单次会话时长的负相关；自适应难度开启后放弃率上升（说明难度爬升超过技能）；用户主动调低难度或关闭"挑战模式"；心流时段后的次日回访率不升反降（疲劳透支）
**可测代理**: 单次会话时长与打断次数的联合分布；难度调整后的即时放弃率；主动降低难度的比例；会话内操作间隔的方差（心流时趋于稳定，焦虑时抖动大）
**交互**: × CA-02 认知负荷 → 心流要求负荷处于带宽内的高位，超出即转为焦虑，二者共同决定难度窗口；× MR-01 目标梯度 → 清晰目标提供方向、目标梯度提供推力，缺一则心流无法维持；× MR-05 自我决定理论 → 自主与胜任是心流的前置条件，控制型设计会直接摧毁心流
**边界**: 不得用于高风险场景（驾驶、医疗操作、金融交易）——心流伴随的隧道视觉会降低对意外的觉察；不得以"心流"为名移除必要的安全提示与休息提醒；未成年人产品的时长设计须内置强制休息；心流不可被强制，只能被创造条件
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.87；Effect Size: Large (Csikszentmihalyi)

**Mechanism**: Optimal experience occurs at the intersection of high skill and high challenge. In flow: time distorts, self-consciousness disappears, intrinsic motivation peaks.

**Flow conditions**:
- Clear goals with immediate feedback
- Challenge level slightly above current skill (optimal difficulty)
- No distractions or interruptions
- Sense of control over outcomes

**Flow curve**:
```
Challenge too low → Boredom → Disengagement
Challenge matches skill → Flow → Total absorption
Challenge too high → Anxiety → Abandonment
```

**Implementation**:
```
Games: Dynamic difficulty adjustment to maintain optimal challenge
Learning apps: Adaptive difficulty based on performance
UX: Remove all friction from primary task; minimize cognitive interruptions
Onboarding: Gradual complexity ramp — don't overwhelm early, don't bore later
Writing tools: Distraction-free modes, word count that provides clear goal
Fitness: Progressive overload + immediate feedback (reps, time, weight)
Music: Playlist curation for task type (beat syncs with cognitive load)
```

---

## AD-10 · Curiosity / Information Gap
**Tier**: 常用
**Evidence**: B — Loewenstein 1994 的信息缺口理论；Kang et al. 2009 用 fMRI 显示好奇心激活与奖赏和冲突相关的脑区，为"缺口=厌恶性状态"提供了神经层面的支持。争议：信息缺口理论预测"已知越多、缺口越具体、好奇心越强"，但这一"信息递增"预测在多项研究中被反证——当用户对某领域几乎一无所知时，一个具体缺口无法被感知（不知道自己不知道什么），而当缺口过于具体时答案可被直接猜测，好奇心反而下降，因此实际关系是倒 U 型而非单调；此外"好奇心被满足即奖赏"在点击诱饵场景中常反转为失望，形成对信源的信任折损
**Effect**: 中等；倒 U 型：缺口必须在用户已有知识基座上"刚好够具体"，过泛或过具体都降低驱动力；且兑现质量决定该效应能否重复使用

**机制链**: 用户意识到自己知道的和想知道的之间存在具体缺口 → 缺口被体验为厌恶性状态并占用注意 → 用户采取行动以闭合缺口
**剂量**: 弱 标题给出一半信息、留一个可推断的缺口，正文完整兑现 ；中 明确的问题 + 不立即给答案 + 答案在正文前三分之一兑现 ；强 缺口 + 高相关性 + 兑现延迟 + 社会证据（"很多人都在问这个"），但仍在正文内兑现 ；过载 缺口被反复制造却从不兑现（标题党、无限"下一页"）→ 单次点击可获客，但用户对信源建立"承诺不可信"的先验，此后该信源所有标题的点击率崩塌，且负向外溢到同一平台
**时间动态**: 起效 秒级（读到标题即产生） · 衰减 缺口在数分钟内衰减，未被闭合则转为烦躁并放弃；同一信源的缺口兑现率决定其可重复性 · 饱和 反复不兑现使好奇心驱动转为"标题免疫"，用户开始跳过该信源全部内容
**调节变量**: 个体 该领域知识中等者好奇心最强（倒 U 型的顶点），专家与完全新手都较弱；认知需求高者更强 · 文化 高不确定性规避文化中未闭合缺口更令人不适因而驱动力更强，但也更快转为烦躁 · 情境 时间充裕、低风险、内容可随时关闭时最强，任务导向、时间紧张、需要确定性时最弱
**失效信号**: 点击率与正文读完率背离（点击高、读完低且持续恶化）；同一信源第 n 次发布的点击率单调下降；用户评论中出现"标题党"指认；跳出时间集中在正文开头数秒（说明缺口被识别为未兑现）
**可测代理**: 标题缺口强度与点击率的曲线（找倒 U 顶点）；点击→读完率的比值（兑现质量代理）；同一信源多次发布的点击率衰减斜率；"标题党"关键词在评论/客服中的频次
**交互**: × AD-02 蔡格尼克效应 → 缺口提供"不知道"，未完成提供"没做完"，两者构成 COMBO-02 的两层张力；× AD-01 变动比率 → 缺口决定是否点开，变动比率决定点开多频繁（COMBO-02）；× PA-02 模式中断 → 中断负责抓住注意，缺口负责把注意留住
**边界**: 缺口必须在内容内被兑现，未兑现即构成欺骗性设计（中国《互联网广告管理办法》与平台标题党规则、FTC 关于 deceptive content 的规则）；不得用于健康、金融与安全信息的传播——未兑现的缺口会延迟真实求助；未成年人内容不得使用未闭合缺口；信源的兑现率是其可重复使用该机制的唯一前提
**v1 标注（数值置信度无出处，属伪精度，已由上方 Evidence 等级取代）**: 原 v1 记 Confidence 0.89；Effect Size: Large (Loewenstein's Information Gap Theory)

**Mechanism**: When people become aware of a gap between what they know and what they WANT to know, they experience curiosity as an aversive state they're motivated to resolve.

**The gap formula**: Curiosity = Awareness of gap × Desire to close gap

**Key insight**: You can't create curiosity about things people don't care about. But for relevant topics, even a tiny hint of "there's more to know" creates powerful drive.

**Implementation**:
```
Headlines: "The one mistake that kills most startups" → gap: what mistake?
Subject lines: "I shouldn't be sharing this, but..." → gap: what is it?
Thumbnails: Show reaction/result without showing cause
Cliffhangers: "Part 2 reveals why this didn't work"
Progress: "70% of users discover something that surprises them in section 3"
Numbers: "The 3 things that account for 80% of outcomes" → read to find out
Teasers: "Here's what happened after 90 days..." (with image showing surprising result)
UI: "You've unlocked something. Check your profile."
```

**Curiosity loop anatomy**:
> Establish known → hint at unknown → create gap → provide path to close gap

**Combos**: Information Gap × Zeigarnik -> incomplete + unknown creates strong return pressure
Information Gap × Variable Ratio -> repeated "maybe there's something new" checking pressure
