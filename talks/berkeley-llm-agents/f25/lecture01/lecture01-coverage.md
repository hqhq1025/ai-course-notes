# Lecture 01 Coverage Matrix

| Source nodes | Required | Teaching treatment | Note destination |
|---|---|---|---|
| 001--005 | yes | 课程定位、三阶段训练与 specializing 对照 | 训练全景 |
| 006 | no | 分节过渡页，无独立教学内容 | omitted: transition |
| 007--010 | yes | next-token prediction、n-gram 与神经语言模型 | 预训练机制 |
| 011 | no | 分节过渡页 | omitted: transition |
| 012--015 | yes | Web 数据处理与 midtraining | 数据工程 |
| 016 | no | 分节过渡页 | omitted: transition |
| 017--023 | yes | scaling laws、Chinchilla、成本 worked example | 规模与预算 |
| 024 | no | 分节过渡页 | omitted: transition |
| 025--028 | yes | LM 目标、alignment、reasoning 与 test-time scaling | 后训练目标 |
| 029 | no | 分节过渡页 | omitted: transition |
| 030--036 | yes | SFT、synthetic data、rejection sampling、Kimi K2、LIMA | SFT 数据 |
| 037 | no | 分节过渡页 | omitted: transition |
| 038--047 | yes | RL、GRPO、RL infra、RLHF 与偏好数据偏差 | RL 与奖励 |
| 048 | no | 分节过渡页 | omitted: transition |
| 049--052 | yes | 评估作用、close-ended 与污染/提示敏感性 | 评估闭环 |
| 053 | no | 分节过渡页 | omitted: transition |
| 054--056 | yes | 人评、Arena、LLM judge 与 spurious correlation | 开集评估 |
| 057 | no | 分节过渡页 | omitted: transition |
| 058--073 | yes | GPU、memory、MFU、precision、kernel、parallelism、MoE | 系统与基础设施 |
| 074 | no | Questions 过渡页 | omitted: administrative |
| 075--077 | yes | perplexity 与 length bias | 评估补充 |
| 078 | no | Wrap-up 过渡页 | omitted: transition |
| 079 | yes | 未覆盖主题与后续课程 | 总结与延伸 |
| 080--085 | no | BPE 同一动画的中间 build，无独立状态 | omitted: keep final build |
| 086 | yes | 完整 BPE 流程 | Tokenizer worked example |

## Spoken Explanation Coverage

| Time | Spoken node | Required treatment |
|---|---|---|
| 00:00--00:01 | 补录原因与公开资料边界 | 封面来源说明、课堂提示 |
| 00:01--00:09 | 三阶段训练和数量级瓶颈 | 总览表、数量级警告 |
| 00:09--00:10 | data/evaluation/systems 比 architecture/loss 更决定实践 | 主线 important box |
| 00:27--00:38 | Web 数据清洗与 mixture | 数据流水线、数据治理警告 |
| 00:44--00:52 | scaling law 与 Bitter Lesson | 研发预算 worked example、证据边界 |
| 01:03--01:08 | verifier rejection sampling 与 tool-use SFT | SFT/工具数据机制 |
| 01:09--01:12 | SFT 复制答案会教出 hallucination | warning box |
| 01:16--01:17 | 长 rollout 暂停与并发环境服务 | RL infra 工程提示 |
| 01:23--01:29 | evaluation is key、close/open-ended | 评估章节 |
| 01:32--01:37 | memory hierarchy 与 50% MFU | 系统术语表 |
