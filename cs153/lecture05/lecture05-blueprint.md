# CS153 Lecture 05 Blueprint

Status: complete and accepted on 2026-08-11.

## Goal

把 Guillermo Rauch 的访谈重写成一份关于“应用意图如何被编译成基础设施，以及使用量、成本和运行证据如何反馈给开发者”的系统讲义。历史视频已转 private，因此以本地时间戳字幕保存课堂主线，以 Vercel/Next.js 官方文档验证 FDI、Build Output API、ISR、Fluid Compute、Spend Management 和 Observability 的机制。

## Teaching Thesis

Vercel 不是“在 AWS 上再套一层 UI”。它把框架提供的应用结构当作高层语言，经 build-time compiler 生成 routing、cache、functions 和 immutable deployment；运行后再把 latency、resource usage、spend 和 failure evidence 反馈给开发者。整讲因此围绕两个闭环：

1. `application intent → intermediate representation → infrastructure`；
2. `traffic → metering/telemetry → developer decision → new deployment`。

## Section Plan

1. 来源审计与抽象层问题：为什么 hyperscaler 之上仍有平台价值。
2. Kubernetes 第一版失败：per-commit deployment 的弹性和单位经济学。
3. Framework-Defined Infrastructure：application-first inversion 与 cloud compiler。
4. Build Output / IR：框架意图如何映射为 routing、cache、functions 和 assets。
5. ISR 与多级缓存：把 backend load 转成 materialized edge output。
6. Build vs. Buy：只在差异化层自研，复用 hyperscaler commodity primitives。
7. 全球 metadata/control plane：immutable deployment、domain binding 与 gossip propagation。
8. Opinionated platform 与 Next.js：guard rails、vertical integration 和 ecosystem feedback。
9. Consumption economics：honest metering、noisy workload、telemetry 与 developer fitness function。
10. Soft cap / hard cap：预算控制、业务连续性和 delayed enforcement 风险。
11. AI workload shape：长 I/O wait、CPU-bound / I/O-bound、compute density 与 Fluid Compute。
12. v0 与 AI-native development：模型能力、custom function calling、idea-market fit 与产品研究。
13. Immutable MVP：一个 API/CLI、URL artifact、IPFS/gossip 启发与逐步替换过度配置。
14. Day 1 / Day 100 / Day 1000：体验、复杂度吸收和长期运营标准。
15. 职业与研究：在真实系统中制造 novel constraints，同时警惕 DIY 过度。
16. 总结、实践作业与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有问题设置、图注、读图解释和证据边界。
- 首次解释 hyperscaler、platform layer、Kubernetes、framework、guard rail、intermediate representation、ISR、materialization、control plane、data plane、immutable deployment、gossip protocol、consumption pricing、telemetry、noisy neighbor、CPU-bound、I/O-bound、compute density 和 TCO。
- 明确课堂时点与当前文档差异：课堂预告的新 compute 产品后来成为 Fluid Compute；当前 Vercel 文档强调并发复用、active CPU、预热实例和长执行支持，但这些后续细节不伪装成课堂原话。
- 对 Black Friday、收入、客户损失、uptime 和 compensation 等口述数字使用“讲者估计/现场案例”措辞，不做审计式结论。
- 删除旧稿中把 DynamoDB/PostgreSQL 简化成“好系统/坏系统”的绝对判断，改写为可归因性与资源隔离的 workload-level 比较。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

## Acceptance

- Final note: 22 pages, 16 figures, 29 teaching boxes, 7 teacher-voice markers.
- Strict coverage: zero errors and zero warnings.
- Quality: `⭐⭐⭐`, 736 prose characters per figure.
- XeLaTeX: two clean passes with no overfull, underfull, undefined-reference, or LaTeX warnings.
- Canonical PDF QA: contact sheet and representative full-size pages reviewed; report signed.
