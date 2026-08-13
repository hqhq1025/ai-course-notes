# CS153 Lecture 08 Blueprint

Status: complete on 2026-08-11; strict coverage, double-pass XeLaTeX, quality and signed PDF QA all passed.

## Goal

把 Julie Cordua 的访谈重写成一份关于“高风险内容安全系统如何从已知内容匹配，扩展到未知内容预测、文本风险识别、人工复核、法定报告与受害者识别”的工程讲义。全文避免刺激性细节，重点放在 detection pipeline、data governance、moderator safety、generative-AI lifecycle、privacy trade-off、network analysis、startup adoption 和 mission-driven operations。

## Teaching Thesis

儿童安全技术不是一个 classifier，而是三个互相约束的闭环：

1. `upload/message → detect → prioritize → human review → action/report`；
2. `verified outcome → trusted data/hash/model update → broader future detection`；
3. `emerging technology → threat research → Safety by Design → audit and transparency`。

## Section Plan

1. 来源审计、敏感内容处理与证据边界。
2. 问题规模：reports、files、duplicates、novel content 和 investigator scarcity。
3. 已知内容：cryptographic/perceptual hashing 与 match pipeline。
4. 未知内容：predictive classifier、score calibration 与 human review。
5. Triage 与 moderator safety：最小暴露、priority、case packaging 和 wellbeing。
6. Trusted data：legal access、provenance、label quality、segregation 与 retention。
7. Generative AI threat model：training data、input/output、model hosting 与 downstream sharing。
8. Safety by Design lifecycle：development、deployment、maintenance、testing 与 transparency。
9. Platform architecture：API/batch/stream integration、idempotency、audit 和 reporting handoff。
10. Privacy 与 encryption：content confidentiality、metadata、endpoint and network signals。
11. Text harms：conversation context、early warning、false positive 与 escalation。
12. Network pattern analysis：account graph、behavior signal 与 coordinated action。
13. Detection 到 prevention：intervention ladder、education 与 user controls。
14. Startup safety maturity：minimum viable safety、risk tier、build/buy 与 incident readiness。
15. Business model / ecosystem：commercial product、nonprofit mission、law enforcement boundary。
16. 总结、平台安全作业与拓展阅读。

## Required Treatment

- 16 张非敏感、transcript-grounded diagrams 全部进入正文，每张有问题设置、读图说明和证据边界。
- 首次解释 CSAM、hashing、cryptographic hash、perceptual hash、precision、recall、calibration、human review、triage、provenance、data segregation、red teaming、Safety by Design、end-to-end encryption、metadata、graph analysis、grooming-risk detection 与 revictimization。
- 不复述或可视化违法内容；不提供规避检测、生成或传播方法。
- 把报告数、文件数、研究比例与救援案例写成 dated source claims，不跨年份直接比较。
- 明确 predictive score 不是法律结论，人工复核、组织 policy、reporting agency 与执法调查承担不同职责。
- 对加密讨论保持技术和权利平衡，不把任一单一技术宣称为充分方案。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。
