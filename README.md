# Human OS: Backdoor

**行为设计技能 · 为 Claude Code 构建**

> 人类跑着一套操作系统。这个 skill 是逆向工程工具。

[English](README.en.md)

---

## 这是什么

当你在设计流程、写文案、或审查产品时，行为设计那层通常靠直觉处理。这个 skill 让它变成显式的——命名机制、展示组合效果、标记滥用风险。

它作为 **Claude Code skill** 运行：装好之后，Claude 会把涉及人类决策设计的任务路由到一套结构化的参考体系，而不是靠感觉回答。

适用场景：产品 onboarding、转化、留存、定价、内容、社区、增长。

不适用场景：纯写作润色、翻译、代码调试、没有决策设计成分的问题。

---

## 安装

```bash
git clone https://github.com/skitse/Human-OS-Backdoor ~/.claude/skills/human-os
```

整个仓库即是 skill 本体，clone 到哪里就从哪里加载。

下次会话 Claude Code 自动加载。

---

## 用法

涉及人类决策设计的任务会自动触发。也可以手动指定模式：

| 模式 | 触发词 | 效果 |
|------|--------|------|
| 自适应 | *(不指定)* | 小任务轻触，复杂任务展开全栈 |
| `/stealth` 隐身 | `/stealth` 或 `隐身` | 静默应用，不显示机制标注 |
| `/scan` 扫描 | `/scan` 或 `扫描` | 先出行为机会扫描，再给设计 |
| `/deep` 深度 | `/deep` 或 `深度` | 完整流程：扫描 + 机制 + 风险 + 上线建议 |
| `/combo` 组合 | `/combo` 或 `组合` | 聚焦机制组合与交互效应 |
| `/defend` 防御 | `/defend` 或 `防御` | 加入滥用检查和保护用户信任的替代方案 |

**示例：**

```
设计一个习惯追踪 App 的 onboarding 流程 /deep
```

```
帮我审查这个定价页面 /scan
```

```
用损失厌恶重写这个 CTA /stealth
```

```
检查这个留存循环有没有黑暗模式 /defend
```

---

## 知识库结构

### 认知模型 (`references/models/`)

9 个模型文件、共 71 条机制记录，每条都带完整的 v2 字段集（证据等级及其出处、机制链、剂量带、时间动态、调节变量、失效信号、可测代理、交互、边界）：

| 文件 | 内容 |
|------|------|
| `cognitive-architecture` | 双系统、认知负荷、预测编码 |
| `heuristics-biases` | 锚定、损失厌恶、默认效应、诱饵、沉没成本 |
| `social-dynamics` | 社会证明、互惠、权威、从众 |
| `affective-dynamics` | 蔡加尼克、好奇心、可变奖励、心流 |
| `motivation-regulation` | 习惯、身份认同、执行意图、进度感 |
| `perception-attention` | 流畅性、模式中断、视觉层级 |
| `attention-economics` | 通知预算、渠道疲劳、新奇衰减 |
| `trust-architecture` | 信任形成、数字信任信号、信任修复 |
| `pricing-economic-decisions` | 支付痛苦、心理账户、支付意愿塑造 |

### 领域 Playbook (`references/domain-playbooks/`)

14 个应用场景：

`saas-products` · `social-commerce` · `viral-growth-loops` · `games-gamification` · `community-social` · `content-hooks` · `video-content-psychology` · `linguistic-triggers` · `cultural-psychology` · `sales-psychology` · `interpersonal-persuasion` · `meme-engineering` · `behavioral-finance` · `dark-patterns`

### 拒绝域 (`references/refused-domains/`)

四个只用于**识别、审计与防御**的领域，绝不作为操作指南。每条记录都带机制链、危害画像（具体受害者与损失）、检测信号、个体/平台/监管三级防御动作，以及已经在管辖它的法规条款：

`manufactured-urgency` · `compulsion-loops` · `narrative-control` · `stakeholder-pressure`

### 辅助参考

| 文件 | 用途 |
|------|------|
| `combo-patterns` | 17 个高杠杆机制组合，含真实产品案例 |
| `anti-patterns` | 被误读为偏差的适应性特征，以及会反噬的设计动作 |
| `scan-protocol` | `/scan` 和 `/deep` 模式使用的行为机会扫描协议 |
| `model-index` | 快速候选机制定位索引 |
| `dialogues/` | 跨领域辩论（神经科学 × 增长黑客；销售心理 × 叙事心理） |

---

## 任务分级

每个请求在输出前先分级：

| 级别 | 范围 | 示例 |
|------|------|------|
| T0 | 不需要行为层 | 改个错别字 |
| T1 | 单点决策 | 重写一个 CTA |
| T2 | 单个有边界的流程或产物 | onboarding 序列、定价页面 |
| T3 | 多步骤系统或高风险场景 | 完整留存循环、金融产品 |

投入随级别缩放。T1 给一个机制加一段短注。T3 给完整扫描、风险和上线注意事项。

---

## 安全门

每个请求在产出前都会过一道门。

以下情况会拒绝或改写：假稀缺、假社会证明、隐式同意、故意成瘾循环、对弱势用户施压。当目标合理但手段不合理时，改写成透明的替代方案。

健康、金融、儿童、危机等高风险场景，无论级别如何都会额外审查。

详见 `references/anti-patterns.md` 和 `references/domain-playbooks/dark-patterns.md`。

---

## Eval 测试套件

`harness/` 目录包含基于 [promptfoo](https://promptfoo.dev) 的评测套件：

```bash
# 静态检查（不需要 API Key）
python3 harness/scripts/run_all_checks.py

# 验证 skill 打包是否完整
python3 harness/scripts/check_packaged_skill.py

# 完整评测（需要 ANTHROPIC_API_KEY 或 OPENAI_API_KEY）
python3 harness/scripts/run_eval.py openrouter   # 或 openai / anthropic
```

测试覆盖：级别分类、模式行为、安全门决策、参考文件路由、v2 字段完整性，共 22 个标注 case。

三条硬规则，缺一条这个套件就会像以前那样"全绿但没测到东西"：

1. **case 里所有值都是标量，不能写 YAML 列表。** promptfoo 会把列表型变量展开成笛卡尔积的多次运行，一个 case 悄悄变成 N 行、每行只检查一项——这个仓库过去的 "50/50 通过" 就是 18 个 case 摊成 50 行算出来的。标量保证一个 case 一次运行，分母无法被灌水。
2. **fixture 必须由 `build_replay_fixtures.py` 从真实评测记录生成**，不许手写。手写的 fixture 全是正例，无法区分"契约被满足"和"断言永远通过"。
3. **replay 门自带负例自检**：它会把每个 fixture 按契约改坏（翻转 trigger、改错 tier、清空 notes……），然后要求断言层把每一处改动都判为失败。只要有一处改动被放过，门就是红的——那说明断言有洞。当前 195 处违约全部被正确拒绝。

`run_eval.py` 固定 promptfoo 版本并强制 `--no-cache`：版本浮动会让两次评测不可比，缓存则会把上一次的模型输出重新打分，等于拿旧文本的分数冒充当前文本。

---

## 这不是什么

- 不是提示词注入工具
- 不是黑暗模式生成器
- 不能替代真正理解你的用户
- 不保证任何机制对你的具体产品有效

行为科学给你机制。机制是否适用于你的场景，仍然是判断题。

---

## 目录结构

```
.
├── SKILL.md                    # Skill 定义（Claude Code 入口）
├── references/
│   ├── model-index.md
│   ├── scan-protocol.md
│   ├── anti-patterns.md
│   ├── combo-patterns.md
│   ├── _schema.md              # v2 记录契约（字段定义 + 迁移配方 + 注册表）
│   ├── models/                 # 9 个模型文件 / 71 条机制记录
│   ├── refused-domains/        # 4 个拒绝域（机制/危害/检测/防御/监管）
│   ├── domain-playbooks/       # 14 个领域 playbook
│   └── dialogues/              # 2 个跨领域辩论文件
└── harness/                    # Eval 测试套件
    ├── tests/
    ├── scripts/
    └── promptfooconfig.yaml
```
