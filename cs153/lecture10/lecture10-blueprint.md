# CS153 Lecture 10 Blueprint

Status: complete on 2026-08-11; strict coverage, double-pass XeLaTeX, quality and signed PDF QA all passed.

## Goal

把 Ben Mann 的访谈重写成一份关于 frontier model program 如何把 scaling hypothesis 转成可靠训练、post-training、安全评估和长期 API 产品的系统讲义。重点不是公司增长新闻，而是 compute/data/model scaling、research-engineering co-design、distributed failure recovery、training observability、RLHF/RLAIF、elicitation-aware evaluation、capability-triggered safeguards、interpretability 与 chat-to-API release discipline。

## Teaching Thesis

Frontier model scaling 由四个闭环组成：

1. `hypothesis → small-scale experiment → scaling fit → compute allocation`；
2. `training telemetry → anomaly → checkpoint/replay → root-cause fix`；
3. `pre-training → post-training → evaluation → safeguards → deployment`；
4. `chat experiment → behavior evidence → API contract → migration/deprecation`。

## Section Plan

1. 来源审计、课堂口径与 RSP 版本边界。
2. GPT-2/GPT-3 与 scaling hypothesis 的形成。
3. Scaling laws：log-log fit、irreducible loss、compute/data/model allocation 与 extrapolation risk。
4. Research-engineering co-design 与 compute multiplier secrecy。
5. Distributed training：failure domains、cloud dependencies、checkpoint 和 deterministic replay。
6. Training observability：loss spikes、data/optimizer/system telemetry 与 escalation。
7. Follow-the-sun operations 与 launch/train ownership。
8. Pre-training、RLHF、Constitutional AI/RLAIF 与 inference-time compute 的互补。
9. Evaluation：capability、safety、elicitation、judge reliability 与 real-world validity。
10. Historical ASL/RSP and current capability-threshold safeguards。
11. Defense in depth：training、classifier、access、monitoring 与 incident response。
12. Mechanistic interpretability：feature discovery、circuits、audit hypothesis 与 limits。
13. Training/inference architecture：centralized giant runs versus distributed serving。
14. Chat proving ground 与 API compatibility contract。
15. Engineers at the frontier：measurement, systems, data and evaluation as research multipliers。
16. 总结、frontier-model program 作业与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有问题设置、读图说明和证据边界。
- 首次解释 scaling law、power law、cross-entropy loss、compute-optimal、checkpoint、deterministic replay、loss spike、RLHF、reward model、RLAIF、Constitutional AI、elicitation、defense in depth、mechanistic interpretability、feature、API deprecation。
- 不把 speaker revenue claims、training incidents 或 secret multipliers 写成 independently audited facts。
- 高风险能力评估保持抽象：只讨论 capability threshold、evaluation design、access control 和 safeguards，不提供有害操作细节。
- 明确 RSP 2025 classroom terminology 与 2026 v3.0 current framework 的区别。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。
