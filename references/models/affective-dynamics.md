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
**可证伪条件**: 在至少两个使用时长与目标人群可比的真实产品上做随机或交错设计的去随机化测试（on/off 交错、同期对照），并把『是否猜得出下一次奖励』作为操纵检查，若奖励变成可预测后，奖励可预测组的会话时长与 30 日留存并不显著低于变动比率组（即消退抵抗优势消失或反转），则变动比率在消退抵抗上的优势不成立，本记录应降级为『只提高行为频率、不延长消退抵抗』。
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
**可证伪条件**: 在随机分配『外部打断』与『用户主动放弃』两种中断的现场试验中，让两组持有相同的完成意图并控制任务重要性，测量中断后 24 小时内的自发恢复率，若主动放弃组的自发恢复率与外部打断组无显著差异，则『效应来自未完成状态的目标激活而非记忆优势』这一解释不成立，本记录应降级为『仅在有明确外部提醒时有效』。
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
**可证伪条件**: 在随机分配『体验中段质量』与『结尾质量』的两因素真实服务试验中（例如客服通话或体检流程），并控制体验时长与客观结果，测量事后整体评分与实际复购、复荐行为，若结尾质量的权重在行为结果上不显著高于中段质量（行为结果主要由客观结果与当下预期解释），则『结尾对复购与推荐的预测力较弱、回顾性评分与行为结果会背离』中的行为侧不成立，本记录关于行为预测力的声称须撤回。
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
**可证伪条件**: 在随机分配『高威胁＋高效能』与『高威胁＋低效能』的现场试验中控制威胁真实性、绝对风险披露与行动成本，测量 30 日内的目标行为率而非自评态度，若低效能组的防御性回避未出现，或高效能未显著调节威胁与行为的关系，则『效能缺失时恐惧诉求反转为回避』的调节关系不成立，本记录应降级为『仅提升态度、不改变行为』。
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
**可证伪条件**: 在随机分配『挑战略高于技能』与『技能明显高于挑战』的真实任务中，并控制任务奖励与时间压力，测量客观产出质量与对突发的意外刺激（如插入的告警）的觉察率，若匹配组的客观产出不显著高于对照，或匹配组未在意外刺激觉察上出现下降，则『心流提升投入但对客观产出证据薄弱，且伴随隧道视觉、在高风险任务中构成风险』中的风险侧不成立，本记录的边界须放宽。
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
**可证伪条件**: 在把『缺口具体程度』分层随机（无缺口、泛化缺口、具体缺口、可被直接回答的过具体缺口）的现场试验中，控制标题长度与内容真实兑现，测量点击率与点击后的停留、完成率以及二次打开率，若好奇心不呈倒 U 型（过具体组的指向性行为未回落，或几乎无知识的受众对具体缺口仍有同等驱动力），则『缺口必须刚好够具体、过泛或过具体都降低驱动力』的倒 U 结论不成立，本记录应降级为『缺口只要存在就有用』。
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

---

## AD-04 · Emotional Contagion
**Tier**: 常用
**Evidence**: B — 面对面通道证据强：Dimberg 1982 用面部肌电证明对情绪面孔的自动模仿、Chartrand & Bargh 1999 的变色龙效应显示互动中姿态与表情会自动趋同，Hatfield, Cacioppo & Rapson 1994 给出情绪传染的理论框架，这些在实验室可重复。争议：①**传染强度随通道衰减**——本记录给面对面/实时音视频通道评 B，而**文本与信息流通道的传播主要是相关与观察证据**：社媒情绪与用户情绪的相关研究无法排除选择效应（情绪相近者互相选择）与共同外因；Kramer et al. 2014 的 Facebook 情绪操纵是少数因果设计，但效应量小且因缺乏知情同意成为研究伦理的反面案例；②"情绪传染"与"行为传染"（跟风点赞、转发）是两件事，后者更可能由算法放大而非心理传染；③群体情绪同质化也可能来自算法筛选（同质内容被优先展示）而非传染；④文本通道只能支持"情绪化措辞影响互动率"，不足以支持"读完即染成同款情绪"。故机制按 B 评级，文本通道强度见 Effect 与 边界。
**Effect**: 面对面中等（表情与唤醒度在数分钟内趋同，肌电与自评可测）；**文本/信息流通道为小效应且难以与选择效应分离**，仅能支撑"情绪化措辞影响互动率"，不足以支撑"改变用户情绪状态"。缺少共处或处于弱通道（单向广播、无互动）时效应接近于零。
**机制链**: 接触到他人的情绪表达（表情、语调、文字的情绪标记） → 自动模仿其表情与体态并经反馈形成相应情绪体验 → 在互动中把自己的情绪状态向对方收敛，并据此调整后续行为强度
**剂量**: 弱 内容中使用中性的情绪标记，不刻意放大唤醒度 ；中 在实时互动中保持一致的、可被感知的情绪表达（客服语调、直播主播状态） ；强 让用户进入可互动的、有同步节奏的共同情绪场景（直播、社群实时活动、共同观看），并让情绪表达可见 ；过载 刻意把高唤醒情绪（愤怒、恐惧、狂喜）注入信息流以换取转发，且情绪与事实无关 → 群体情绪被推到极端后出现传染疲劳与反噬：用户把该信源整体归类为"情绪操纵"，退订与屏蔽上升，社区讨论质量下降，且极端情绪帖的后续互动成本上升
**时间动态**: 起效 秒级到分钟级（接触情绪表达后一次互动内趋同） · 衰减 单次接触的情绪抬升在数十分钟内回落至基线，重复暴露于同强度情绪后反应钝化（情绪通胀） · 饱和 长期处于高唤醒情绪流中，用户对情绪标记脱敏并以"情绪劳动"回应，传染效果下降而屏蔽与静音上升
**调节变量**: 个体 情绪易感性高、共情与自动模仿倾向强者效应最强；高自我分化与情绪调节能力强者显著更弱 · 文化 关系与集体主义文化中情绪表达的可见度与对他人的影响更强，且在情绪压抑规范下表达与体验分离；个人主义市场对显性情绪表达的传染更弱 · 情境 实时、双向、可看到表情与语气的互动中效应最大；单向广播、匿名文本流、缺少共同注意时最弱
**失效信号**: 高强度情绪帖的互动率上升而评论质量与净推荐值下降；用户开启"减少此类内容/静音"功能的比例按接触到的情绪强度上升；情绪帖占比升高而社区回访时长下降（情绪疲劳）；同一情绪话术第 n 次使用的互动增益衰减到零
**可测代理**: 有/无情绪表达的同一信息分流的互动率与情绪词比例；情绪帖占比与次日回访时长的相关性；"减少此类内容/静音/退订"开关开启率按其接触到的情绪强度分层；客服或主播对话中双方情绪词的一阶自回归系数（趋同速度）
**交互**: × AD-13 情绪一致性记忆 → 情绪决定当下体验也被决定记住什么，使被记住的版本比实际更极端（COMBO-16）；× SD-01 社会证明 → 情绪表达若附带"很多人也这样想"，传染从个体趋同升级为群体共振，构成 COMBO-16 内容病毒化栈的传播层（COMBO-16）；× HB-02 损失厌恶 → 恐惧与愤怒天然与损失框架相容，叠加时分享率最高但反噬也最快
**边界**: 不得以情绪操纵为目的在信息流中系统性注入情绪（Kramer et al. 2014 的 Facebook 实验因缺乏知情同意成为研究伦理的反面案例，是本记录的第一红线）；未成年人、心理创伤与情绪障碍人群不得作为情绪传染的目标或实验对象；医疗、政治与选举场景中不得用情绪传染替代事实披露；文本通道的传染强度不足以支撑"能改变用户情绪"的产品承诺
**可证伪条件**: 在同一信息流内随机分配情绪化措辞与中性措辞的平行文案，让同一批用户被随机分配到两种版本，并追踪其发布后的自评情绪轨迹；同时用固定人群的前置情绪基线把『情绪相近者互相选择』（选择效应）从『看后情绪改变』（传染）中分离出来，若情绪化措辞组与中性组在发布后自评情绪上的差异不显著高于其曝光前基线差（即差异可完全由选择解释），则文本与信息流通道的传染声称不成立，本记录的适用范围须收缩为仅面对面与实时音视频通道，并删除信息流侧的『影响情绪状态』表述。

**Mechanism**: Emotions converge between people who can perceive each other. The channel matters more than the message: face-to-face interaction carries reliable contagion, a text feed carries mostly correlation.

**Design principles**:
- Treat face-to-face and feed as two different mechanisms with two different evidence grades
- Keep high-arousal emotion tied to facts; it is the pairing that makes it contagious
- Give users a visible mute/de-escalation control

**Anti-pattern**: Engineering arousal for shares. The source gets classified as emotional manipulation, and subsequent factual content from it is discounted too.

---

## AD-05 · Affective Forecasting Error
**Tier**: 常用
**Evidence**: B — **持续时间维度的证据强于强度维度**。Gilbert & Wilson 2007 的综述与 Gilbert et al. 1998 的实验确立了"免疫忽视"（immune neglect）：人们在预测情绪性事件时会系统性忽略自己的心理免疫系统（合理化、意义重建、注意转移），因而高估负面情绪的持续时间。持续时间维度的方向在多组研究一致。争议：①**强度维度（impact bias）小得多**——对日常事件的情绪强度预测误差通常不大甚至没有；早期"离婚/失业比人们想的恢复快得多"（Brickman, Coates & Janoff-Bulman 1978 的适应性研究）存在测量问题（自评量表与回忆偏差），后续修正把"享乐适应普遍且迅速"缩小为"部分适应、时间不定"；②预测误差也源于**回忆误差**（回忆上次事件情绪时本身有偏差），不只是预测机制；③不同情绪方向不同——焦虑与恐惧的持续时间被高估，而对狂喜的强度常被低估；④故"人们总能预测错情绪"作为普遍规律会被数据反驳，本记录只对"负面事件的持续时间被高估"给可用量级。
**Effect**: 持续时间维度为中等且方向稳定（预测的持续时间普遍长于实际，尤其负面事件）；**强度维度为小效应且依事件类型而异**（日常事件几乎无偏差，重大事件最大）。仅在"高唤起事件 + 需要预测未来情绪 + 缺少同类经历"时达到可用量级；有既往同类经历或明确时间坐标时误差显著缩小。
**机制链**: 面对一个尚未发生的情绪性结果并预测自己未来的情绪 → 把当下的强烈反应投射到未来，同时忽略心理免疫机制（合理化、意义重建、注意转移）的恢复作用 → 高估负面事件的持续时间并据此做出过度规避或为"现在就消除风险"支付溢价
**剂量**: 弱 在文案中呈现真实的、含时间坐标的用户经历（"第 3 天最难受，第 2 周基本恢复"） ；中 让用户在决策前回忆上次同类事件的真实恢复时间，并提供可对照的时间锚 ；强 在取消/退订或续费路径中展示双方（保留与取消）的真实后续情绪与行为数据，并把预测锚定在真实时间线上 ；过载 利用过度悲观的预测卖"安心"（把灾难后果反复预演以促成保险或高额套餐） → 用户事后发现真实痛苦远小于承诺中的恐惧，识别为恐惧营销，信任与续约率下降，且此后对该渠道的风险提示整体折价
**时间动态**: 起效 分钟级（一次预测任务内即出现偏差） · 衰减 具有同类经历后偏差快速缩小，一次真实经历即可校正大部分预测错误（这是少数"越用越弱"的杠杆） · 饱和 反复用灾难预演驱动决策会让防御性预测失去说服力，用户对风险提示脱敏
**调节变量**: 个体 高焦虑特质与低情绪调节自我效能者偏差最大；有同类经历、具备心理距离（第三人称视角）者偏差显著更小 · 文化 强调情绪表达与"情绪真实"的文化中，对负面情绪的灾难化预测更强；情绪压抑规范下人们更少报告预测但仍出现行为规避 · 情境 面对高唤起、低概率、高后果的事件偏差最大；日常、可反复经历、有明确时间线的事件偏差接近零
**失效信号**: 用户决策后主动反馈"没有你说的那么糟"或"比预想恢复得快"；以恐惧预演为核心的文案其后 30 天留存低于不做预演的对照组；同一风险提示第 2、3 次触达响应率断崖式下降；出现"越提醒越不改"的防御性回避（提示频次与行为改变负相关）
**可测代理**: 投保或退订前自报的预期情绪持续时间与实际 2/4/8 周后自评的差值；含真实时间锚（"第 3 天难受/第 2 周恢复"）与不含的对照组转化与留存差；同一风险提示第 1/2/3 次触达的响应率曲线；决策后悔分数的回访测量
**交互**: × HB-13 双曲贴现 → 高估未来的痛苦使人们更愿为"现在消除风险"付溢价，两者叠加把远期风险定价推到失真（COMBO-01）；× AD-11 预期焦虑 → 预期焦虑提供当下痛苦，预测误差放大对未来的估计，两者共同支撑 FOMO 的恐惧引擎（COMBO-01）；× SD-14 地位信号 → 对未来情绪的错误预测常与身份焦虑绑定（"不买会后悔、会被人比下去"），使预测误差直接转成溢价
**边界**: 不得利用过度悲观的预测卖"安心"——把真实恢复史替换为最坏剧本构成误导（恐惧营销）；医疗与保险场景中必须披露真实恢复分布而非极端尾部，且不得以情绪预测替代客观风险披露；不得对已知处于急性心理危机的用户使用灾难预演类内容
**可证伪条件**: 在让同一被试预测一件近期重大负面事件（失业、落榜、分手）的情绪强度与持续时间之后，追踪其 1、3、6、12 个月的实际自评，并按『有无同类经历』分层分析，若实际情绪强度的下降幅度与预测的下降幅度无显著差异（即影响偏差不存在或方向相反），则『强度维度的影响偏差虽小但方向稳定』的声称不成立，本记录只保留持续时间维度的免疫忽视效应。

**Mechanism**: People forecast the duration of their emotional reactions poorly, in a specific direction: they underestimate their own recovery. The immune system they fail to discount is their own sense-making, not the event.

**Design principles**:
- Anchor forecasts to real timelines ("day 3 is worst, week 2 is normal")
- Show both branches — keep and cancel — with real follow-up data
- Treat one real experience as the strongest correction you can offer

**Anti-pattern**: Selling reassurance with a worst-case rehearsal. The gap between rehearsed terror and lived recovery is exactly the trust you spend.

---

## AD-07 · Mere Exposure Effect
**Tier**: 常用
**Evidence**: B — 重复接触提高喜好是该族最稳定的实验室发现之一：Zajonc 1968 用无意义汉字、假字与照片证明曝光次数与喜好正相关；Bornstein 1989 的元分析（200 余项实验）确认平均效应中等且不限于特定刺激类型。争议：①**倒 U 才是真正的发现**——对**初始为负性**或**复杂**的刺激，重复曝光**降低**喜好而非提高；Bornstein 的元分析本身已包含这一边界，把"越多曝光越好"当作结论是对该元分析的反向误读；②机制解释仍有分歧（加工流畅性、知觉熟悉性、错误归因），且曝光必须在**无惩罚性后果**的语境下发生——重复与负性体验配对时就变成习得性厌恶；③广告重复与销量的现场证据高度混淆预算与品类成熟度，"高频曝光=更高偏好"在成熟品类上常呈负向（wear-out）。故本记录按"对新颖/中性/简单刺激有效、初始负性或过载时反转"评 B。
**Effect**: 中等且**方向依初始态度与刺激复杂度而定**：对新颖、中性、简单刺激，喜好随曝光次数上升；对初始负性、高复杂或被判定为打扰的刺激，喜好随曝光下降。仅在低干扰、无负性配对的语境下成立；一旦曝光伴随打断或负性体验，效应转负。
**机制链**: 反复接触到同一个中性或新颖的刺激 → 对该刺激的加工流畅性提高，这种更流畅的体验被错误归因为"更喜欢它" → 在缺少其他信息时把熟悉度当作品质与偏好的依据
**剂量**: 弱 在同一界面内一致地重复使用同一视觉与术语（不追求额外曝光） ；中 在低频、无干扰的位置重复品牌或标识，且每次接触都有独立价值 ；强 在用户已有兴趣的语境中形成稳定重复（固定栏目、持续系列），且每次接触附带新信息 ；过载 在用户未同意或无兴趣的通道上高频硬性曝光，或对已被明确拒绝的刺激反复推送 → wear-out 与反击：喜爱度下降、跳过率与屏蔽率上升、出现"看到就烦"的品牌厌恶，且负性态度比未曝光时更难逆转
**时间动态**: 起效 数秒到单次曝光即可看出轻微偏好提升（对新奇刺激） · 衰减 两周到一个月不接触后熟悉度回落、偏好向基线回归；若曝光期间累积的是负性体验则不再衰减而是巩固为厌恶 · 饱和 在最优曝光次数前为上升段，超过后进入 wear-out，广告的"有效频次上限"就是这条曲线的拐点，拐点高度依刺激复杂度与品类而变
**调节变量**: 个体 认知需求高与独特性需求高者更快进入 wear-out；熟悉度偏好强、低唤醒需求者上升段更长 · 文化 高语境与关系文化中熟悉度作为信任信号权重更大、重复收益更高；低语境市场对陌生品牌的重复容忍度更低 · 情境 低干扰、用户有意愿、刺激简单时效应为正；高干扰、被动插入、刺激复杂或被判定为打断时效应为负
**失效信号**: 曝光次数与喜好/点击率的关系越过峰值后转负（wear-out 曲线出现下降段）；同一素材第 n 次曝光的跳过率与屏蔽率同步上升；品牌提及在评论中出现负面偏转（"又是它"）；用户主动使用"不再显示"类功能的比率按曝光频次单调上升
**可测代理**: 同一素材第 1/3/7/15 次曝光的点击、跳过与喜欢率曲线及其拐点；有/无频次上限控制的广告组偏好度与屏蔽率差；品牌名称的隐性偏好测量（选择任务）随曝光次数的变化；**初始负性态度分组的曝光-喜好斜率（预期为负，这条斜率的符号就是倒 U 的直接检验）**
**交互**: × PA-01 加工流畅性 → 流畅性是被错误归因的中介，主动降低可读性会削弱重复曝光的效果，也是 COMBO-06 信任级联最廉价的一层（COMBO-06）；× PA-05 启动效应 → 二者常被混谈，但输入与输出都不同，PA-05 是先行相关刺激改变通达性（输出为反应时），本记录是同一刺激的重复改变喜好（输出为偏好），不能互相替代；× HB-04 稀缺 → 稀缺抵消重复曝光的疲劳，因为每次接触都携带新信息
**边界**: 不得对用户已明确拒绝或投诉过的刺激继续高频曝光（构成骚扰，且制造品牌厌恶，效果为负）；不得把重复曝光用于掩盖虚假或有害内容（熟悉度会错误地充当真实性与可信度信号，这是"虚假真相效应"的伦理红线）；未成年人产品中不得用被动高频曝光替代用户主动选择；不得以"提高熟悉度"为名购买未经同意的注意力
**可证伪条件**: 对初始态度为负性或高复杂的刺激（难听音乐、被判定为打扰的广告位）做多次曝光，并按『初始态度』分层估计每个亚组『曝光次数—喜好』斜率的符号（亚组斜率／符号检验），而非总体平均斜率，若初始负性亚组的曝光—喜好斜率为正而非为负，则『倒 U、重复曝光把初始负性刺激变得更讨嫌』的结论不成立，本记录应回退为『重复提高喜好，仅有磨损带』。

**Mechanism**: Repeated exposure to a neutral stimulus raises liking for it — but only from a neutral start. The inverted U is the finding: exposure past the optimum, or exposure on top of a negative first impression, runs the other way.

**Design principles**:
- Find the frequency ceiling empirically; do not assume monotonic gain
- Keep every repetition independently useful, so repetition never reads as filler
- Re-check the slope by initial-attitude segment, not just the average

**Anti-pattern**: Buying frequency against an audience that already declined. Familiarity converts to aversion, and aversion is slower to reverse than indifference.

---

## AD-09 · Nostalgia Effect
**Tier**: 情境
**Evidence**: C — **机制侧与商业声称分别评级，两者均记 C**。机制侧：Sedikides, Wildschut, Arndt & Routledge 2008 的综述与 Wildschut et al. 2006 的多国研究显示怀旧是常见、可触发的自我相关情绪，具备提升自尊、增强社会联结、抵抗孤独与提升意义感的功能，实验可重复（该部分证据本身较好，但按本记录的整体声称评级，仍不据此单独上调）。争议与分级：①**商业效果未被证实**——"怀旧营销提高购买"主要来自案例汇报、行业观察与少量小样本实验，缺少可比口径的现场对照；把怀旧情绪的功能性证据当作商业提升证据是分级错误，本记录不让机制的可复制性把商业侧一并抬高；②触发与内容强相关（具体年代符号、个人成长线索），对不共享该年代的受众无效甚至造成疏离；③存在负向变体（bittersweet 体验），强调失去会降低对当下产品的评价；④效果高度依赖个体怀旧倾向与当下情绪状态。**可证伪条件见本记录下方独立一行。**
**Effect**: 情绪效果（自尊、联结、意义感）为小到中等且可重复；**对购买行为的效果未知且证据薄弱**，现有材料不足以支持"怀旧营销能提升转化或溢价"的可用量级。仅在"受众与该年代符号真实共享 + 产品与记忆真实相关 + 不贬低当下"时可能小幅提升偏好与回忆。
**机制链**: 接触到承载个人或集体过去的符号（年代视觉、旧包装、熟悉的场景） → 回忆被激活并带来社会联结与自我连续性的情绪体验 → 在情绪被抬高的窗口内对与该记忆相关的主张更宽容，并更愿重复已熟悉的选择
**剂量**: 弱 在视觉与文案中使用与品牌历史一致的元素（旧标识、真实档案照片） ；中 把怀旧作为叙事线索与产品真实的历史连起来，说明"当年是什么样、现在保留了什么" ；强 围绕真实的集体记忆节点做限时的、可参与的回顾活动（周年、旧版回归），并提供与记忆对应的实体证据 ；过载 把怀旧当作万能滤镜，对无关品类套用旧年代符号、或把记忆商品化到失真（虚构历史、美化不存在的过去） → 受众识别为情感挪用，怀旧转为疏离与嘲讽，反而降低对品牌真实性的评价
**时间动态**: 起效 小时内（一次接触即可触发回忆与情绪提升） · 衰减 单次怀旧刺激的情绪提升在数十分钟到数小时内回落，重复暴露的边际效应递减很快（可触发的记忆资源有限） · 饱和 同一记忆符号被反复使用后失去稀缺性并转为陈词滥调，受众从感动转为厌倦，最终被动过滤
**调节变量**: 个体 怀旧倾向高、当下孤独感强、处于人生过渡期者效果最强；年轻且无该年代经历者几乎无效甚至出现疏离 · 文化 集体记忆强、代际叙事清晰的社会中集体怀旧更有效；移民与多元社会中个人怀旧强于集体怀旧 · 情境 与个人生活史真正相交的符号、以及过渡或纪念节点（毕业、迁居、周年）时最强；日常无关联场景中接近噪声
**失效信号**: 怀旧素材的互动（收藏、分享）高而转化与客单价不变（情绪被消费但购买未被推动）；受众年龄分布与素材年代不匹配（触达错位）；评论出现"消费情怀""贩卖回忆"类表述；同一符号第二次使用时互动断崖下降
**可测代理**: 怀旧素材与中性素材分组的回忆率、品牌态度与转化差；自评怀旧强度与购买意向的相关；素材年代与受众出生年代的匹配度分层响应；同一符号第 1/2 次使用的互动衰减曲线；含真实档案证据与不含的信任度差
**交互**: × AD-04 情绪传染 → 怀旧是一种低唤醒、高联结的情绪，在共同观看或社群场景中被互相放大，构成 COMBO-16 的身份信号层（COMBO-16）；× SD-15 社会比较 → 共同的过去提供"我们曾经怎样"的比较基准，这是把怀旧从个人情绪转成群体认同的一步；× SD-14 地位信号 → 怀旧符号一旦被当作圈层标记，就会排挤没有该记忆的受众，收益与排斥同时上升
**边界**: 不得虚构或美化不存在的历史（编造品牌年代、伪造档案）——这既是情感挪用也是对商品来源的虚假表示；不得对已失去相关记忆载体的人群（丧亲、失忆、创伤）使用纪念性怀旧内容；**本记录的商业侧证据为 C，不得作为投放预算的主要依据**；不得用怀旧包装掩盖产品实质变化（旧瓶新酒式的版本替换须明确披露）
**可证伪条件**: 在控制素材年代与受众匹配度、品类相关性、曝光后时间窗的前提下，若怀旧素材组与中性素材组在转化或支付意愿上的差异不显著高于后者，则"怀旧可提升商业转化"的声称不成立，本记录应被降级为"仅影响自评情绪与回忆，不改变购买"。

**Mechanism**: Cueing a shared past reliably produces a warm, self-continuing emotional state. Whether that warmth moves a purchase is a separate claim with separate, much weaker evidence.

**Design principles**:
- Use real archives and real product history; the artefact is the proof
- Pair the memory with something still true today
- Measure conversion, not just engagement — the two routinely diverge here

**Anti-pattern**: Using nostalgia as a universal filter on an unrelated category. Audiences read it as emotional appropriation, and authenticity scores fall.

---

## AD-11 · Anticipatory Anxiety
**Tier**: 情境
**Evidence**: B — 机制侧证据良好：对预期性疼痛的恐惧可超过疼痛本身，这一方向在预期电击/预期疼痛范式中反复验证（预期期的自评焦虑与生理唤醒——皮电、心率、皮质醇——显著高于基线），且恐惧成分与期待成分可分离。争议与分级：①**掉落机制（drop mechanics）的应用证据是行业观察级（C）**——限时发售前"等开抢"的转化提升主要来自从业者报告与单个平台的案例分析，缺少随机对照；观察到的等候人数与开抢峰值同时混淆了稀缺（HB-04）与并发社会证明（SD-01），无法单独归因于预期焦虑；②预期焦虑与期待/兴奋共享同一生理唤醒且可互相转化（"又怕又想"），把唤醒一律读作焦虑并加以放大是误判；③慢性预期焦虑有明确健康成本（睡眠、皮质醇、心血管），使该机制的伦理门槛低于多数机制；④预期期长度存在最优值，过长导致焦虑疲劳与放弃。故机制按 B、掉落机制应用按 C 标注。
**Effect**: 机制为中等（预期期的自评焦虑与生理唤醒显著高于基线，且可预测回避行为）；**"预期焦虑提升发售转化"的应用效果证据薄弱**，只能作为行业观察、不能作为可靠设计依据。仅在"结果不确定 + 时间明确 + 用户无法在中途获得信息"时焦虑升高；提供确定性或中途信息会显著降低焦虑与行为冲动。
**机制链**: 知道一个不确定但重要的结果将在未来发生 → 在等待期反复模拟可能的不良结果，唤醒与注意被持续占用 → 为中止这种不适而行动（提前决定、抢购、反复检查信息），或在等待中回避与退出
**剂量**: 弱 提前披露发售时间与规则，把不确定性压到最低 ；中 设定明确的等待窗口（数小时到数天）并在其中提供进度或内容，让等待有信息增量 ；强 把等待做成可参与的悬念（倒计时 + 可预告 + 名额与库存的确定性事实），并让用户在等待期内有事可做 ；过载 用长周期的高压倒计时反复提醒结果未知、并持续制造不确定威胁（"会不会抢不到""可能会涨价"） → 焦虑转为回避与愤怒：用户屏蔽通知、放弃参与，并在事后对该品牌的风险沟通整体失信；长期暴露还有睡眠与情绪健康的实际成本
**时间动态**: 起效 分钟级（结果一旦被标记为不确定且重要，唤醒即上升） · 衰减 预期焦虑随等待期延长先升后降，过长（超过数天）转为疲劳与放弃；结果揭晓后 10–30 分钟内快速回落 · 饱和 反复经历被制造的预期焦虑后，用户对倒计时类提示脱敏并以"不看了"作为默认应对，机制失效
**调节变量**: 个体 焦虑特质高、不确定容忍度低、控制需求强者反应最强；高不确定容忍与有明确计划者显著更弱 · 文化 高不确定性规避文化中预期焦虑更强、对确定性信息需求更高；集体主义市场中与他人共同等待会同时放大与缓解（社会支持的两面） · 情境 结果重要、时间明确、缺乏中途信息时最强；可中途获取进展、可退出、或结果不重要时显著减弱
**失效信号**: 倒计时开启后通知屏蔽率与退订率按等待期长度上升；到点参与率不升而投诉与客服问询上升（"到底什么时候""是不是骗人"）；用户在结果揭晓前主动退出（焦虑回避）；同一商品的第二次倒计时活动参与率显著低于第一次（脱敏）
**可测代理**: 等待期内的自评焦虑与皮电/心率变异性变化；不含中途信息的纯倒计时与含中途信息的倒计时两组的到点参与率与投诉率；等待期长度（小时/天/周）分层的放弃率；第二次同类活动的参与衰减比；焦虑强度与参与率的关系是否呈倒 U
**交互**: × HB-04 稀缺 → 稀缺把"不确定"升级为"可能失去"，预期焦虑从情绪成本变为行动驱动，是 COMBO-01 FOMO 栈的引擎（COMBO-01）；× AD-05 情绪预测误差 → 人们既高估焦虑的持续时间又低估自己 habituate 的能力，使预期焦虑常被过度定价（COMBO-01）；× SD-10 FOMO → 预期焦虑是可单独测量的情绪成分，FOMO 是不可直接测量的复合构造，叠加时最易越过过载档
**边界**: 不得用长周期、高强度的不确定威胁制造预期焦虑（对未成年人、焦虑障碍与睡眠问题人群构成实际伤害，是硬红线）；不得在健康、金融、住房等生活必需品上以"抢不到"的恐惧驱动决策；**不得把生理唤醒一律当作购买意愿的证据**（唤醒同样可转为焦虑与回避）；必须披露确定性信息与退出路径
**可证伪条件**: 在随机分配『只保留倒计时与库存』『只保留同伴参与可见』『两者同时呈现』三种条件的发售试验中，控制折扣力度与产品价值，测量开抢后 24 小时内的转化以及抢后 7 日留存，若稀缺线索（HB-04）与同伴线索（SD-01）被分别移除后，倒计时的转化优势消失（即预期焦虑的贡献可被这两种已知机制完全解释），则掉落机制作为独立机制不成立，本记录的应用声称须归还给 HB-04 与 SD-01，只保留机制侧的预期焦虑部分。

**Mechanism**: Waiting for an important, uncertain outcome is aversive in itself, and the anticipation can outweigh the outcome. The arousal is real; reading it as demand is the mistake.

**Design principles**:
- Cut uncertainty first: announce the time and the rules
- Give the wait an information payoff, not just a countdown
- Keep the window short; long waits convert anticipation into abandonment

**Anti-pattern**: Sustained high-pressure uncertainty as a launch tactic. Notifications get muted, and the brand's later risk communication is discounted.

---

## AD-12 · Hot-Cold Empathy Gap
**Tier**: 情境
**Evidence**: B — **机制侧与补救手段分别评级：机制 B，补救 C**。机制侧在实验室稳健：Loewenstein 1996 的理论与一系列实验显示，处于"冷"状态（不饿、不渴、不恐惧）的人系统性低估"热"状态下的欲望强度与自己的行为（饥饿者的食物偏好、恐惧下的风险选择），且**热状态下的人低估自己未来冷状态下的偏好**，双向都会错。争议与分级：①**用承诺装置填补缺口的现场证据是混合的（C）**——储蓄承诺账户（Ashraf, Karlan & Yin 2006 的 SEED 实验）证据较强，但推广到健康、消费与注意力品类时结果不一致：一部分研究显示承诺装置的选择被需求效应解释（用户知道被观察时更愿选约束性选项），另一部分显示高放弃率与事后违约，"承诺装置有效"的普遍结论不被支持；②实验室多依赖唤起操纵（饥饿、运动、情绪诱导），生态效度有限；③个体差异大，自我控制高与未来自我连续性强者缺口更小；④"冷状态替热状态的自我做决定"本身有伦理争议。故不让机制的稳健性替补救手段背书。
**Effect**: 机制为中等（冷状态下的预测与热状态下的实际选择系统性偏离，方向稳定）；**补救效果不确定**（承诺装置的现场证据混合，需求效应与高放弃率同时削弱其可用量级）。仅当决策发生在冷状态、且该决策约束的是未来热状态时缺口出现；在热状态当场决策、或有明确反馈循环时缺口缩小。
**机制链**: 在冷静状态下为未来的高热状态预先做决定或做承诺 → 以当前不具该欲望的状态去估计未来的欲望强度，系统性低估其强度 → 做出在冷静时看似合理、在热状态到来时难以执行或事后后悔的选择
**剂量**: 弱 在冷静时提供"未来可能想要什么"的信息披露（费用、可撤销性） ；中 提供可撤销的约束工具（预算上限、可选提醒、延迟结算），默认不替用户做不可逆决定 ；强 在用户明确要求时提供有退出路径的承诺装置，并披露真实放弃率与历史违约数据 ；过载 在用户处于热状态时逼其做出约束未来的不可逆决定（自动续费、一次性大额预付），或反向在冷静期设计不可撤销条款 → 用户在热状态下无法履行或事后强烈后悔，退款、争议与负面口碑集中爆发，且该品类整体信任下降（对同行的约束性选项一并回避）
**时间动态**: 起效 分钟级（状态一旦改变，偏好与预测立刻偏离） · 衰减 缺口随状态切换立刻出现或消失，不随时间自然衰减；但自我控制策略与未来自我连续性信念可在数周至数月内缩小缺口 · 饱和 反复经历"冷时承诺、热时违约"后，用户学会整体不信任承诺装置，放弃率上升，工具被彻底弃用
**调节变量**: 个体 自我控制低、未来自我连续性弱、冲动性高者缺口最大；有既往违约经验并已调整策略者缺口缩小 · 文化 高自我约束规范与长期取向文化中承诺装置的接受度高、但事后羞耻与隐瞒成本也高；短期取向与即时满足文化中接受度低 · 情境 决策在冷状态、结果在热状态且不可撤销时缺口最大；当场决策、可撤销、有明确反馈时显著缩小
**失效信号**: 承诺装置的放弃率或自动续费取消率显著高于设计预期；客服与评论出现"签的时候没想清楚""当时以为做得到"类表述；承诺类选项被选中的比例强烈受"是否被观察/是否被提示"影响（需求效应信号）；同一用户的违约率与承诺强度正相关
**可测代理**: 冷状态下自报的未来欲望强度与热状态下实际选择的差值；有/无提示（被观察）条件下承诺装置选择率之差（需求效应估计）；承诺装置的按时履约率、放弃率与后续退款率；未来自我连续性量表得分与实际违约率的相关
**交互**: × SD-03 承诺与一致 → 冷状态下做出的承诺在热状态下变成必须维护的身份，缺口被一致性压力放大（COMBO-03）；× MR-08 预先承诺装置 → 冷热缺口是该机制要解决的问题，但装置本身效果证据较弱，不可用机制的高等级替装置背书；× HB-13 双曲贴现 → 贴现解释"为什么现在更重要"，共情缺口解释"为什么冷状态低估热状态的自己"，两者叠加时约束设计的失败率最高
**边界**: 不得在用户处于热状态（冲动窗口、情绪危机、疲劳）时推动不可撤销的长期承诺（自动续费、大额预付、亏本取消条款），可能构成不公平条款与暗黑模式；不得以"帮助自律"为名把承诺装置做成退出困难的锁定；健康与金融品类中必须披露真实放弃率与违约后果；不得对已知处于成瘾或冲动控制困难的人群推销约束性订阅
**可证伪条件**: 在随机分配『承诺装置组』与『无承诺装置组』的现场试验中，控制目标人群与决策时点（冷热状态），并追踪 6 至 12 个月的实际持有与坚持率而非仅签约率，若承诺装置组在长期坚持率上不显著高于对照，或放弃率把初始提升抵消殆尽（净效应为零或为负），则『承诺装置能填补冷热缺口』的补救声称不成立，本记录应降级为『仅描述缺口、不给补救方案』。

**Mechanism**: The self that plans is not the self that acts. A cold-state decision that binds a future hot state is made with systematically underestimated desire, in both directions.

**Design principles**:
- Default to reversible constraints; reserve irreversible ones for explicit opt-in
- Publish the real abandonment and default rates of your own commitment features
- Keep the hot-state decision free of long-term lock-in

**Anti-pattern**: Pushing an irreversible commitment inside an impulse window. The remedy's own evidence is mixed, so the harm is not offset by a proven benefit.

---

## AD-13 · Mood-Congruent Memory
**Tier**: 情境
**Evidence**: B — **机制侧与投放应用分别评级：机制 B，应用 C**。机制侧有可复现的实验室证据：Bower 1981 的情绪与记忆网络理论及其实验显示，处于某种情绪时更容易编码与提取与该情绪一致的材料；提取侧的情绪一致性回忆与情绪依赖性记忆（同情绪下回忆更好）在多项研究中得到支持，量级小到中等。争议与分级：①**效应量偏小且不稳定**——情绪对记忆的影响受材料效价、自传体与非自传体记忆、是否个人相关调节，部分研究报告无效应；情绪一致性在抑郁人群中更强（负性偏向），在非临床人群中较弱；②**"广告投放位置改变记忆"是应用推断而非实验结论（C）**——媒体语境效应与广告回忆的研究多为相关性，且混淆了受众选择（情绪一致的人更看那类内容）与语境影响；③情绪操纵的持续性有限，短时诱导的情绪未必贯穿记忆编码窗口。故不让机制等级被应用继承。**可证伪条件见本记录下方独立一行。**
**Effect**: 机制为小到中等（情绪一致材料的回忆率高于不一致材料，在个人相关材料与强情绪状态下更大）；**投放应用的效果未被证明**，只能作为待验证假设。仅在"情绪被有效诱导 + 编码或提取窗口内情绪保持 + 材料与情绪相关"时出现可测差异；情绪未真正改变或材料不相关时接近于零。
**机制链**: 处于某种情绪状态时接触或回忆信息 → 与当前情绪一致的信息获得优先编码与更高的提取通达性 → 事后记住的内容偏向与该情绪一致的版本，使回忆呈现系统性的情绪倾斜
**剂量**: 弱 在已知的语境情绪中投放中性且明确的信息，避免与语境冲突 ；中 让内容与所在语境的真实情绪一致（轻松的语境放轻松的内容），不强行反情绪 ；强 在活动前后保持情绪的连续性（一次活动内的视觉、文案、音乐同调），并在提取窗口内做一次一致的提醒 ；过载 为追求"语境一致"把高情绪化内容与争议性语境绑定，或在不合宜的情绪语境（悲伤、危机报道旁）插入商业信息 → 出现内容与语境的情绪冲突，受众对该品牌形成"不合时宜/不尊重"的记忆，负面记忆因情绪显著性而被记得更牢（反效果比中性投放更差）
**时间动态**: 起效 分钟级（情绪诱导后立即影响编码与提取） · 衰减 诱导情绪的效应在数十分钟到数小时内消退，记忆偏好随之减弱；编码窗口过后无法补救 · 饱和 同一情绪语境反复使用后，受众对该语境中的商业内容形成预期并整体跳过，语境效应的边际收益耗尽
**调节变量**: 个体 情绪易感性与情绪调节能力低者效应强，抑郁倾向人群的负性一致偏向更强；高情绪稳定性者更弱 · 文化 情绪表达规范不同的社会中，被诱导情绪的强度与持续度不同，集体主义文化中社会性情绪线索更强 · 情境 个人相关材料、强情绪状态、编码与提取窗口内情绪保持一致时最强；中性材料、情绪已消退或语境冲突时最弱甚至反转
**失效信号**: 语境情绪匹配组与不匹配组在回忆率与品牌态度上无差异（效应不存在）；受众对"不合时宜内容"的负面提及集中出现（反效果）；同一语境中的商业内容跳过率随时间单调上升；广告回忆测量与行为（点击、购买）长期背离
**可测代理**: 情绪诱导前后对一致/不一致材料回忆率的差（实验室或线上记忆测试）；语境情绪评分与广告回忆、品牌态度的相关；匹配与不匹配语境分组的回忆率与负面提及率；情绪诱导强度的个体差异分层响应
**交互**: × AD-04 情绪传染 → 情绪传染决定当下情绪状态，情绪一致性记忆决定该状态下什么被记住，两者叠成"记住的版本比实际更极端"（COMBO-16）；× PA-01 加工流畅性 → 情绪一致的加工更流畅，流畅性又被误读为真实性，使情绪一致的错误信息更容易被当作事实记住；× AD-05 情绪预测误差 → 人们回忆上次情绪时的偏差正是其预测偏差的来源，两者互为因果，不可当作独立证据叠加
**边界**: 不得在悲剧、灾难、危机报道等敏感语境中插入商业内容以博取情绪一致性（对当事者与受众构成冒犯，且负面记忆更牢固）；不得利用负性情绪偏向对抑郁倾向或心理脆弱人群定向投放；不得以"语境匹配"为名把商业信息伪装成新闻或编辑内容（构成隐性广告与信任破坏）
**可证伪条件**: 在随机分配语境情绪（而非依赖受众自选）、并控制内容相关性与曝光次数的现场试验中，若语境情绪与内容一致组在回忆率或后续行为上不显著优于不一致组，则"投放位置通过情绪一致性记忆改变记忆"的应用声称不成立，本记录应只保留机制层面的编码/提取效应并删除投放建议。

**Mechanism**: Mood at encoding and at retrieval biases which material is remembered. The effect is real but modest; the advertising-context application built on top of it is inference, not demonstrated.

**Design principles**:
- Avoid emotional conflict between the context and the message; neutrality beats a bad match
- Keep the emotion continuous across encoding and recall if you want the effect at all
- Validate context effects with random assignment, not with audience self-selection

**Anti-pattern**: Buying adjacency to a charged context for "emotional congruence". Mismatched placement is remembered harder than neutral placement, in the wrong direction.
