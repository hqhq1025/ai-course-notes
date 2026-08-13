# CS153 Lecture 07 Blueprint

Status: complete and accepted on 2026-08-11.

## Goal

把 Cursor CTO Sualeh Asif 的访谈重写成一份“AI coding product 如何把 retrieval、model serving、edit application、database/storage、security 和 incident response 组合成低延迟交互系统”的课程讲义。重点不是复述增长数字或事故戏剧性，而是解释每个失败为什么发生、哪些状态应当进入数据库、哪些数据适合 object storage，以及如何把 blast radius、backpressure、migration 和 provider routing 设计成可验证机制。

## Teaching Thesis

Cursor 的用户体验由三个循环耦合而成：

1. `workspace change → incremental index → retrieval context`；
2. `request → model/provider routing → generated plan/edit → fast apply`；
3. `traffic/failure → telemetry → mitigation/migration → safer architecture`。

## Section Plan

1. 来源审计与规模数字的证据边界。
2. 三个 product-critical systems：indexing、model inference、product/apply layer。
3. 单体与 blast radius：部署边界比代码仓库边界更重要。
4. Incremental indexing：Merkle-style sync、chunking、embedding cache 与 retrieval。
5. 数据模型演进：metadata、vectors、documents、jobs 和 source of truth 分层。
6. 事故一：retry、cron、migration 和 index rebuild 构成 feedback cascade。
7. 事故二：PostgreSQL growth、dead tuples、vacuum、disk pressure 与 emergency offload。
8. Cold start：重建 embedding 和 global index 的隐藏成本。
9. Object-storage-native search：durability、cache hierarchy、stateless compute 与 recall。
10. Global inference：self-hosted model、GPU region、latency 与 capacity planning。
11. Frontier provider portfolio：rate limit、failover、quality/cost routing 与 versioning。
12. Fast Apply：planning model 与 specialized apply model 的 latency budget。
13. Security：path/content protection、key control、privacy mode 与 shared responsibility。
14. Pricing 与 abuse：free token arbitrage、identity、quota 和 unit economics。
15. AI 对软件工程：education、IDE、agent harness 与 incident response。
16. 总结、设计作业与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有问题设置、读图说明和证据边界。
- 首次解释 blast radius、backpressure、Merkle tree、content-addressed cache、embedding、vector search、recall、source of truth、dead tuple、VACUUM、cold start、object storage、stateless compute、rate limit、provider routing、envelope encryption 和 abuse prevention。
- 所有增长、调用量、文档量与供应商地位使用“讲者估计/课堂口径”。
- 事故叙述重构为 dependency graph、feedback loop 与 recovery decision，不渲染个人英雄主义。
- 当前 Cursor secure indexing、privacy、CursorBench 和 Router 资料只用于验证机制或说明后续演化。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

## Acceptance

- Final note: 24 pages, 16 figures, 37 teaching boxes, 8 teacher-voice markers.
- Strict coverage: zero errors and zero warnings.
- Quality: `⭐⭐⭐`, 900 prose characters per figure.
- XeLaTeX: two clean passes with no overfull, underfull, undefined-reference, or LaTeX warnings.
- Canonical PDF QA: contact sheet and representative full-size pages reviewed; report signed.
