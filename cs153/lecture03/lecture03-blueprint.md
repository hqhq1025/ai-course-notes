# CS153 Lecture 03 Blueprint

Status: complete and visually accepted on 2026-08-11.

## Goal

把 Shyam Sankar 访谈重写成一份关于“异构任务环境如何迫使软件交付、Kubernetes substrate、决策链和制造软件一起重构”的系统讲义。历史公开视频已转 private，因此以本地时间戳字幕为课堂主线，以 Palantir 官方 Apollo/Rubix 材料验证技术机制，并严格区分技术事实、讲者经验判断和政治/战略立场。

## Source Priority

1. 本地历史字幕 `lecture03.srt`。
2. Palantir Apollo 官方 Demo Day PDF 与产品截图。
3. Palantir 当前 Rubix 官方架构文档与图。
4. Stanford Winter 2025 课程页与本地官方封面。
5. 旧讲义仅作为主题索引，不直接沿用叙述。

## Section Plan

1. 个人使命、国防科技与观点来源审计。
2. On-prem / air-gapped / edge / cloud 异构部署问题。
3. Apollo：desired-state、catalog、release channel、health 与 rollback。
4. Rubix：统一 substrate、compliance-as-code、ephemeral nodes 与安全。
5. 从一个极端客户归纳通用产品能力。
6. Project Maven：从 computer vision 到完整 OODA decision chain。
7. 政府 kill chain 与商业 value chain 的共同软件骨架。
8. AI supply/demand、制造反向规划与 Warp Speed。
9. Privacy-security frontier 与制度 feedback loop。
10. 总结：高风险软件如何同时获得速度、控制和责任。

## Required Treatment

- 13 张 transcript-grounded diagrams 与 8 张官方 Apollo/Rubix 图全部进入正文。
- 首次解释 air gap、SRE、microservice、desired state、release channel、canary、rollback、Kubernetes、immutable image、ephemeral node、multi-tenancy、OODA、ontology、decision chain、efficient frontier。
- 明确版本差异：课堂口述 Rubix 节点随机在 40--72 小时替换；2026-08-11 当前官方文档写“不超过 48 小时”。二者均保留来源，不强行统一。
- Project Maven 与国防案例聚焦决策延迟、验证、权限、审计与反馈，不提供攻击操作细节。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

## Final Verification

- Output: 24 pages, 21 figures, 33 teaching boxes, 11 section summaries.
- `check_note_coverage.py --strict`: zero warnings.
- `check_quality.sh`: `⭐⭐⭐` with 612 prose characters per figure.
- XeLaTeX: two clean final passes; no overflow or undefined-reference warning.
- Canonical PDF QA: contact sheet plus full-size Apollo, Rubix, privacy-frontier,
  and final-page inspection completed and signed on 2026-08-11.
