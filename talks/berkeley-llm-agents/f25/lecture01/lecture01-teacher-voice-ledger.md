# Lecture 01 Teacher Voice Ledger

| Time | Spoken point | Why it matters | Planned note location |
|---|---|---|---|
| 00:00:08--00:00:58 | 本视频因课堂技术故障与 fire alarm 补录；内容基于公开的 Kimi、LLaMA、DeepSeek 信息，除非明确说明，不代表 OpenAI。 | 界定课堂版本和证据边界。 | 封面来源说明 |
| 00:01:22--00:02:43 | 预训练的心智模型是“在互联网文本上预测下一个词”，规模超过 10T tokens，耗时数月，瓶颈是数据与计算。 | 把抽象目标与实际资源量级连接起来。 | 训练全景、预训练 |
| 00:03:04--00:04:59 | 经典 post-training/RLHF 让模型从“知道世界”变成“知道如何与人交互”，数据较少但瓶颈转为质量与评估。 | 解释为何后训练不是继续堆预训练数据。 | 后训练目标 |
| 00:05:08--00:07:12 | reasoning RL 使用可验证任务；环境和 verifier 可能被策略钻空子，例如修改测试使其永远通过。 | reward hacking 是环境设计问题。 | RL 与奖励 |
| 00:08:36--00:09:21 | 实践中真正关键的是 data、evaluation、systems；architecture/loss 是较早时期的主要注意力。 | 确立整讲工程主线。 | 训练全景 |
| 00:27:00--00:37:50 | Internet 数据要经过抽取、过滤、去重、分类和 domain reweighting；“干净互联网”不是天然存在。 | 防止把数据工程压缩成下载动作。 | 数据工程 |
| 00:44:10--00:49:20 | scaling laws 让团队在小模型上调 recipe 后外推到大规模；Bitter Lesson 主张长期要利用计算，但不是取消实验设计。 | 说明 scaling law 的研发用途和边界。 | 规模与预算 |
| 00:50:00--00:53:00 | LLaMA 3 405B 的 FLOPs、GPU hours、成本与碳排只是公开数据上的数量级估算。 | 避免把课堂估算当精确财务数字。 | 成本 worked example |
| 01:02:40--01:04:10 | 当有 verifier 时，可以生成多个答案并用 rejection sampling 留下正确或偏好更高的样本。 | 解释 synthetic SFT 的关键不是“让模型抄模型”，而是引入外部判据。 | SFT 数据 |
| 01:04:27--01:07:40 | SFT 可学习格式、风格、tool use 和初步 reasoning；复杂 tool use 需要模拟用户、工具和 rubric。 | 将 Kimi K2 的数据系统与 Agent 能力连接。 | SFT 数据 |
| 01:08:30--01:10:20 | SFT 是行为克隆；若模型不知道答案却被迫模仿正确答案，可能学会编造看似可信的引用。 | 解释 hallucination 的一种训练来源。 | RL 与奖励 warning |
| 01:15:30--01:17:20 | RL sampling 成本高，Agent rollout 更长；Kimi 对长尾 rollout 暂停，并并发执行环境服务。 | 说明算法改进依赖调度与环境基础设施。 | RL infra |
| 01:23:00--01:29:00 | 评估用于发现改进、选模型和判断能否上线；prompt 敏感性与 contamination 会扭曲 close-ended 分数。 | 评估是训练闭环而非发布前考试。 | 评估闭环 |
| 01:29:00--01:32:00 | open-ended 评估成本高，LLM judge 很快但会受输出长度等 spurious correlation 影响。 | 引出 Arena、AlpacaEval 与 length control。 | 开集评估 |
| 01:32:00--01:36:50 | GPU 的计算增长快于 memory/communication；memory hierarchy 决定供数速度，50% MFU 已很优秀。 | 校准系统指标直觉。 | 系统与基础设施 |
