# Lecture 03 Blueprint

## Teaching Question

如何用可验证环境、工具和 verifier 构造 Agent 后训练闭环，并在有限 rollout
预算下同时保持稳定性、难度和探索多样性？

## Narrative Spine

| Unit | Slides | Required treatment |
|---|---|---|
| Agentic shift | 001--006 | 从 human preference alignment 转向 environment feedback + verifiable reward。 |
| Training data | 008--011 | environment/tools/verifier 三元组、覆盖多样性、false positive/negative。 |
| Evaluation | 013--018 | benchmark、harness、unit eval、holistic intelligence、hardness/diversity/separability。 |
| SFT + RL | 020--023 | attempt 成本、先 imitate 后 explore、light/diverse SFT。 |
| Train longer | 024--030 | entropy-reward tradeoff、on-policy、clip、entropy loss。 |
| Train harder | 031--034 | 难度区间、confidence/reward 相关、hard prompt weighting。 |
| Sample better | 035--038 | parallel reasoning、beam search、GenSelect、DeepConf、总 recipe。 |
| Open ecosystem | 040--044 | 环境/eval/算法 collection、benchmark 定义、开放问题。 |

## Acceptance Targets

- 40 required slides; four step-transition pages documented optional.
- 20+ pages, 10+ boxes, 3+ terminology blocks, 8+ teacher-voice markers.
- Explain all formulas/symbols and distinguish slide evidence from lecture judgment.
- Strict coverage, two-pass XeLaTeX, `⭐⭐⭐`, clean log, signed PDF QA.
