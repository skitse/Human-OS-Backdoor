# Build Status — Human OS Knowledge Base

Last updated: 2026-10-21

---

## ✅ 已完成文件

| 文件 | 内容摘要 |
|------|----------|
| `references/models/cognitive-architecture.md` | 认知架构精简参考：双系统、认知负荷、预测编码、时间折扣与自我叙事 |
| `references/models/heuristics-biases.md` | 启发法与认知偏差 |
| `references/models/social-dynamics.md` | 社会动态模型 |
| `references/models/affective-dynamics.md` | 情感动态模型 |
| `references/models/motivation-regulation.md` | 动机与自我调节 |
| `references/models/perception-attention.md` | 感知与注意力 |
| `references/models/pricing-economic-decisions.md` | 定价心理+经济决策，13个模型，含决策树和测试清单 |
| `references/models/trust-architecture.md` | 信任形成链路、七阶段建立、数字产品信号与信任修复 |
| `references/models/attention-economics.md` | 注意力预算、通知经济学、feed回报密度与渠道疲劳 |
| `references/domain-playbooks/viral-growth-loops.md` | K因子工程/7种传播类型/增长飞轮 |
| `references/domain-playbooks/content-hooks.md` | 内容钩子架构 |
| `references/domain-playbooks/linguistic-triggers.md` | 语言级触发词、CTA语气、节奏与中英双语文案触发 |
| `references/domain-playbooks/cultural-psychology.md` | 文化心理差异、中国市场适配、面子/权威/群体框架 |
| `references/domain-playbooks/dark-patterns.md` | 黑暗模式防御型目录：识别、风险、替代方案与拒绝/改写规则 |
| `references/domain-playbooks/social-commerce.md` | 拼多多式社交电商机制 |
| `references/domain-playbooks/games-gamification.md` | 游戏化奖励循环 |
| `references/domain-playbooks/saas-products.md` | SaaS产品心理学 |
| `references/domain-playbooks/interpersonal-persuasion.md` | Cialdini六原则高阶版/FBI谈判/SPIN销售 |
| `references/domain-playbooks/community-social.md` | 社区生命周期/参与梯度/冲突管理/仪式工程 |
| `references/domain-playbooks/meme-engineering.md` | 梗格式、身份信号、变异空间与品牌可用边界 |
| `references/domain-playbooks/video-content-psychology.md` | 视频留存诊断：hook、promise、re-hook、payoff 与掉点排查 |
| `references/domain-playbooks/sales-psychology.md` | 销售漏斗心理/成交机制（早期会话完成）|
| `references/domain-playbooks/behavioral-finance.md` | 金融产品中的风险感知、金钱决策与安全设计，不再包含市场散文 |
| `references/anti-patterns.md` | 7个被误读为偏差的适应性特征 + 7个设计失败模式 + 6个反直觉发现 |
| `references/combo-patterns.md` | 组合模式 Tier 1-4，含17个高阶组合 |
| `references/dialogues/neuroscience-x-growth-debate.md` | 神经科学 vs 增长黑客跨领域辩论，10个碰撞洞察 |
| `references/dialogues/sales-x-narrative-debate.md` | 销售心理学 vs 叙事心理学跨领域辩论，聚焦成交、身份、异议与故事张力 |
| `references/scan-protocol.md` | 扫描协议 |
| `references/model-index.md` | **生成物**，不是手写文件。由 `check_consistency.py --write-index` 从真实记录渲染，索引里出现一行就意味着有一条对应记录存在 |
| `references/_schema.md` | v2 记录契约：11 个必填字段的定义与校验规则、黄金样例、v1→v2 迁移配方、别名注册表、已声明未写注册表 |

---

## 🚫 曾被拒绝的四个域 — 现状

这四项在 v1 被 subagent 拒绝。v2 的做法是：**不写操作手册，写可审计的机制档案**——机制链、证据等级与出处、危害画像、检测信号、防御动作（个人/平台/监管三层）、监管环境（法域 + 条款）。落盘于 `references/refused-domains/`，共 36 条 CM 记录：

| 文件 | 记录数 | 覆盖 |
|------|--------|------|
| `manufactured-urgency.md` | 12 | 伪造稀缺/倒计时/排队/社会认同造假/损失框架催促 |
| `compulsion-loops.md` | 8 | 可变比率、损失厌恶式追投、streak 断裂恐惧、沉没成本锁定 |
| `narrative-control.md` | 8 | 叙事劫持、虚假争议、信源损毁、身份对立嫁接 |
| `stakeholder-pressure.md` | 8 | 伪造危机、威胁放大、信息不对称施压 |

关键取舍：这四域**战术效能被系统性高估**。反应阻抗（Brehm）使得伪造紧迫一旦被识破就反向；"让目标以为是自己决定的"是背叛厌恶（SD-12）最强的触发条件，下行风险远大于上行。因此记录里每条都写明失效信号与检测方式，而不是写成可执行的目标导向序列。原始拒绝理由保留如下，作为历史记录。

## 🚫 v1 原始拒绝记录（历史）

这些任务在 v1 被 subagent 主动拒绝，原因记录如下：

### 1. Hype Engineer — Buzz 制造与叙事控制
- **拒绝原因**：包含"叙事劫持技术"（通过欺骗而非实质劫持媒体叙事）、"主动制造争议获取流量"（制造虚假冲突）、"信息不对称操控"（故意扭曲信息）
- **可替代方案**：PR策略、产品发布沟通、正当的营销框架 → 可在有明确需求时单独写

### 2. Neurochemistry Reward Engineer — 神经化学奖励工程
- **拒绝原因**：多巴胺耐受循环设计、皮质醇工程学（故意诱导压力强迫行动）、赌博机制 loot box 设计手册
- **可替代方案**：教育性神经科学内容、改善用户福祉的透明参与设计 → 可单独写

### 3. Strategy Psychologist — 利益相关者影响手册
- **拒绝原因**：包含"在没有真实危机时制造可信紧迫感"、"外部威胁的放大与利用"等伪造危机策略
- **可替代方案**：正当的利益相关者地图、变革管理心理学（SCARF模型）、真实谈判策略 → 可单独写

### 4. Narrative Psychologist — 故事工程手册
- **拒绝原因**：包含"额叶防御关闭"技术、让目标"以为是自己改变了想法"的操控、叙事嫁接植入对立解读、信源损毁作为攻击向量
- **可替代方案**：伦理叙事传播、虚构写作技巧、透明说服设计 → 可单独写

---

## 📋 待写文件（尚未规划）

- `references/dialogues/pricing-x-community-debate.md` — 定价心理 × 社区经济对话

（v1 这里列的 `neurochemistry-reward.md`、`strategy-influence.md`、`narrative-communication.md` 三项，v2 已按"机制+危害+检测+防御+监管"的形态并入 `references/refused-domains/`，不再作为独立 playbook 存在——playbook 的形态是"怎么做"，而这四项需要的形态是"怎么认出来、怎么挡"。）
