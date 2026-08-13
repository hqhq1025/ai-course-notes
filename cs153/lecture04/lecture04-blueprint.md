# CS153 Lecture 04 Blueprint

Status: complete and visually accepted on 2026-08-11.

## Goal

把 Guillaume Lample 的访谈重写成一份关于“研究问题如何塑造模型基础设施，以及 open-weight checkpoint 如何经过部署、定制、反馈与治理变成可运行产品”的系统讲义。历史视频已转 private，因此以本地时间戳字幕保存课堂叙事，以论文和官方资料校验算法、模型与监管事实。

## Source Priority

1. 本地历史字幕 `lecture04.srt` 与官方封面 `cover.jpg`。
2. Lample 的无监督机器翻译、HyperTree Proof Search、LLaMA、Chinchilla、Mistral 7B 一手论文。
3. Mistral 官方 Mistral 7B 发布页与部署文档。
4. 欧盟委员会现行 GPAI transparency / copyright / safety 指引，用于标注课堂时点与当前状态差异。
5. 旧讲义仅作为主题索引，不沿用其薄摘要结构或未经分层的数字结论。

## Teaching Thesis

这讲不是“Mistral 公司史”。主线是四次系统边界扩张：

1. 从单语语料到跨语言表示对齐；
2. 从普通搜索树到可验证的 formal proof hyper-tree；
3. 从 compute-optimal 预训练目标到 inference-aware 小模型；
4. 从 model weights 到可部署、可定制、可观测、可治理的完整产品。

## Section Plan

1. 来源审计、课堂时点和整讲问题意识。
2. 无监督翻译：表示空间、对齐假设与迭代训练。
3. 形式化数学：proof state、tactic、subgoal 与 HyperTree Proof Search。
4. Informal-to-formal 如何反向要求自有 LLM 与低延迟采样基础设施。
5. Chinchilla 问题、inference-aware over-training 与“目标函数错配”。
6. 大规模训练的隐蔽故障、混淆因素、实验成本与 R&D iceberg。
7. Mistral 7B 的 data-first 组织方式，以及 GQA/SWA 的部署含义。
8. Checkpoint-to-solution：serving、私有部署、合成数据、fine-tuning、评测与更新。
9. Le Chat：快推理的约束、tool layer 与产品反馈飞轮。
10. Reasoning / RL：verifier environment、DeepSeek R1 评价与早期直觉风险。
11. 欧洲监管、主权和 privacy/reliability 市场；区分课堂判断与 2025--2026 生效规则。
12. Post-training operating system：为什么创新速度、清晰 pipeline 和产品层可能比单次预训练规模更关键。
13. 总结、实践作业与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有前置问题、图注、读图解释和证据边界。
- 首次解释 open weights、checkpoint、formal prover、proof state、tactic、subgoal、hyper-tree、compute-optimal、inference-optimal、FP16、confounding factor、fine-tuning、synthetic data、on-prem、private cloud、serving endpoint、post-training、verifier 与 data flywheel。
- 明确 Lample 的关键提醒：data work 不显眼但关键；大训练故障只能在规模上暴露；final run cost 不能代表完整 R&D cost；模型不是产品；reasoning 时代仍处早期。
- 对课堂数字使用“讲者估计/课堂口述”措辞，不把 ASR 中的 `70B/7B`、`A100/H100` 混淆直接写成事实。
- EU AI Act 部分并列写出：课堂时点技术规范仍在讨论；GPAI provider obligations 自 2025-08-02 起适用，旧模型有过渡期限。法律信息只做课程背景，不给合规建议。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

## Final Verification

- Output: 24 pages, 16 figures, 31 teaching boxes, 12 section summaries.
- `check_note_coverage.py --strict`: zero warnings; 8 teacher-voice markers.
- `check_quality.sh`: `⭐⭐⭐` with 733 prose characters per figure.
- XeLaTeX: two clean final passes; no overflow, underfull, or undefined-reference warning.
- Canonical PDF QA: contact sheet plus full-size terminology-table, reasoning,
  product-stack, regulation, and final-page inspection completed and signed on
  2026-08-11.
