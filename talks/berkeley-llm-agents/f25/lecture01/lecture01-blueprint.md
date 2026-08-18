# Lecture 01 Blueprint

## Teaching Question

如何把一个只会预测下一个 token 的基础模型，训练成能够遵循指令、推理、使用工具，
并在算力约束下稳定迭代的 Agent 模型？

## Narrative Spine

| Unit | Source nodes | Question answered | Required treatment |
|---|---|---|---|
| 1. 全局地图 | slides 001--005 | 训练流水线有哪些阶段，各自瓶颈是什么？ | 三阶段成本/数据/时间表；区分训练与 specializing。 |
| 2. 预训练机制 | slides 007--010 | next-token prediction 为什么能学习世界知识？ | tokenization、条件概率、n-gram 泛化失败、神经语言模型。 |
| 3. 数据工程 | slides 012--015 | “用整个互联网”实际包含哪些治理步骤？ | Common Crawl、WARC、抽取、过滤、去重、mixture、midtraining。 |
| 4. 规模与预算 | slides 017--023 | scaling law 如何改变模型研发和预算分配？ | IsoFLOP、Chinchilla、Bitter Lesson、LLaMA 3 成本 worked example。 |
| 5. 后训练目标 | slides 025--028 | language modeling 为什么不等于 assisting users？ | alignment、instruction following、reasoning、test-time scaling。 |
| 6. SFT 数据 | slides 030--036 | 少量高质量样本如何塑造行为？ | 人工数据、Alpaca、rejection sampling、Kimi K2、LIMA。 |
| 7. RL 与奖励 | slides 038--047 | 为什么从模仿转向优化，奖励从哪里来？ | SFT 局限、rule reward/RM/LLM judge、GRPO、RLHF、偏好数据偏差。 |
| 8. 评估闭环 | slides 049--056, 075--077 | 如何判断改进真实存在？ | close/open-ended、MMLU、污染、Arena、AlpacaEval、PPL、长度偏差。 |
| 9. 系统与基础设施 | slides 058--073 | 为什么训练最终会成为系统问题？ | GPU、memory hierarchy、MFU、mixed precision、fusion、tiling、parallelism、MoE。 |
| 10. 收束与补充 | slides 079, 086 | 课程没有覆盖什么，tokenizer 如何建立词表？ | 开放问题与 BPE worked example；只保留 progressive reveal 的最终页。 |

## Prose-Led Flow

每个单元先提出工程问题，再放 2--5 张相邻 slides。图后说明：

1. 首先比较什么；
2. slide 支持哪个判断；
3. 哪些数字只是 2025 年公开项目的数量级估计；
4. 不能从图中推出什么；
5. 与后续 Agent 训练的关系。

## Teacher Voice Priorities

- 开场说明这是补录版本，公开数字主要来自 Kimi、LLaMA、DeepSeek。
- 三阶段数据量、时间和成本只表达数量级，不是精确报价。
- 2023 年前研究注意力偏向 architecture/loss，实践瓶颈转向 data/eval/systems。
- Agent RL 的环境会被策略利用，reward hacking 必须视作环境设计缺陷。
- 数据收集不是“下载完就结束”，过滤、去重和 mixture 决定最终行为。
- scaling law 的价值是用小规模实验预测大规模选择，而不是宣称规模解释一切。
- SFT 学得很快，往往更多是在学习格式和用户类型。
- SFT 复制正确答案可能教会模型在不知道时伪造可信答案。
- 长 rollout 与慢环境反馈使 RL 基础设施成为关键瓶颈。
- 50% MFU 已是很好的工程状态，不应把理论峰值当作日常目标。

## Acceptance Targets

- 20+ pages; target 35+ because the deck has 86 pages.
- All required slide nodes referenced; slides 080--085 may be optional as redundant BPE builds.
- 10+ teaching boxes, all three box types.
- 3+ terminology-digestion blocks.
- 10+ teacher-voice markers grounded in timestamps.
- Prose density at least 260 characters per included figure.
- Strict coverage, two XeLaTeX passes, clean log, `⭐⭐⭐`, signed PDF QA.
