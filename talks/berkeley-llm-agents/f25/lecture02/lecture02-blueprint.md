# Lecture 02 Blueprint

## Teaching Question

为什么 AI 应用与训练不能直接复用传统 cloud abstraction，系统设计又为何在更高算力、
更低供应链弹性和更强 locality 约束下“回到未来”？

## Narrative Spine

| Unit | Source nodes | Teaching goal |
|---|---|---|
| 1. 去神秘化 | 001--007 | 用中文打字机说明复杂智能可由检索、组合与工程机制构成。 |
| 2. 模型浪潮 | 009--012 | 区分算法持续进步、消费增长与 hype cycle。 |
| 3. 应用市场 | 014--019, 021 | 模型能力与产品体验相关但不等价；ToC/ToB 商业节奏不同。 |
| 4. 第三支柱 | 023--25 | 从 scientific compute、web cloud、data cloud 走向 AI cloud。 |
| 5. 云价值重写 | 026--032 | 软件多样性、供应链弹性、bare metal/K8s 二分法为何都不足。 |
| 6. 回到未来 | 034--036 | 硬件/软件共设计、加速器集中与 locality 回归。 |

## Required Teaching Moves

- 对中文打字机案例说明“机制可分解”，不把文化史类比当作 LLM 等价证明。
- 解释 model improvement、app experience 与 willingness to pay 的不同因果层。
- 首次出现 I/O、AI cloud、locality、elasticity 时就地定义。
- 对 cloud 对照表逐列解释 workload、software variety、supply-chain flexibility。
- 保留讲者的强判断“bare metal 不对，K8s 也不对”，同时解释其语境和边界。
- 把 developer efficiency 与 infra efficiency 放进同一成本函数。
- 对无文字的硬件历史图写明读图顺序与不能推出的结论。

## Acceptance Targets

- 29 required slide pages referenced; 8 transition/redundant build pages documented optional.
- 20+ pages, 10+ teaching boxes, 3+ terminology blocks, 8+ teacher-voice markers.
- At least 260 prose characters per figure.
- Strict coverage, two XeLaTeX passes, `⭐⭐⭐`, clean log, signed visual QA.
