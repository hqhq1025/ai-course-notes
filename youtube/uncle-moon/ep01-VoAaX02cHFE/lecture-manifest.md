# Source Manifest: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep01-VoAaX02cHFE`

## Files

- `README.md`
- `cover.jpg`
- `coverage-matrix.md`
- `teacher-voice-ledger.md`

## Supplementary Source Materials

- `sources/deepseek-r1.md`
- `sources/official-page-metadata.json`
- `sources/references.json`
- `sources/sglang.md`
- `sources/source-notes.md`
- `sources/source.info.json`
- `sources/transcript.official.txt`
- `sources/transcript.txt`

## Local Visual Assets

- none found

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| speech-01 | section | yes | sources/transcript.txt 00:00:40–00:24:23 | 从模型能力到推理与训练的闭环 |
| voice-01 | text | optional | sources/transcript.txt 00:00:40–00:24:23 | RadixArk、SGLang、Miles 分工；预训练/后训练/推理；私有 Agent 数据的机会；从怀疑 SGLang 到重估；FlexGen、Vicuna、Arena 历史；实时语音等待与轮次；新架构首日支持的人工投入；中美差距半年一年仅为当时口述判断。 |
| speech-02 | section | yes | sources/transcript.txt 00:27:25–00:39:18 | 强化学习怎样把反馈变成模型更新 |
| voice-02 | text | optional | sources/transcript.txt 00:27:25–00:39:18 | 多回答比较数据与排序；reward model、policy、critic、advantage 定义；PPO/DPO/GRPO 不作绝对胜负；critic 初期估计差导致不良更新；warm-up 条件；推理直觉、实验反馈循环；DeepSeek-R1-Zero 与 V3 的名称纠正。 |
| speech-03 | section | yes | sources/transcript.txt 00:24:23–00:27:25；00:41:21–00:46:30；01:11:08–01:15:14 | 从可执行环境到千卡训练系统 |
| voice-03 | text | optional | sources/transcript.txt 00:24:23–00:27:25；00:41:21–00:46:30；01:11:08–01:15:14 | 函数调用时延与并发；沙箱执行层/任务奖励数据层；多轮模拟用户；Gym 口述已完成数据集合与远期调度愿景分开；故障恢复、正确性、MFU；几节点经验不能直接外推万卡；Miles 千卡口述验证，万卡尚需优化；商业项目支持规模验证。 |
| speech-04 | section | yes | sources/transcript.txt 00:47:24–01:07:02；01:25:00–01:28:52 | 研究判断来自怎样的学习和转向 |
| voice-04 | text | optional | sources/transcript.txt 00:47:24–01:07:02；01:25:00–01:28:52 | 清华电子、UGVR David Tse、伯克利焦剑涛/Jordan/Steinhardt；context 自嘲不是学习科学结论；研究多维差异；MMLU 最初被低估；Jordan 持续读经济学/优化；代表作而非篇数；defer 教职为当时状态；资源与训练机会，不把离校或烧token当统一建议。 |
| speech-05 | section | yes | sources/transcript.txt 01:07:02–01:11:08；01:14:12–01:24:58 | 预训练、持续学习与多模态的下一步 |
| voice-05 | text | optional | sources/transcript.txt 01:07:02–01:11:08；01:14:12–01:24:58 | 预训练质量影响后训练空间但非数学固定上界；on-policy蒸馏不是直接平均权重；研发反馈不能自动等同在线更新；算力能源约束；Omni/VLA/kernel/compiler/prefill解释；世界模型预测物理变化和模拟；Neo Labs 替代范式为探索；平台愿景保留多种可能。 |
| speech-06 | section | yes | sources/transcript.txt 00:00:40–00:07:52；00:39:18–00:47:24；01:12:32–01:14:12；01:15:14–01:22:50 | 开源社区怎样连接研究与创业 |
| voice-06 | text | optional | sources/transcript.txt 00:00:40–00:07:52；00:39:18–00:47:24；01:12:32–01:14:12；01:15:14–01:22:50 | 2023 agent 与RAG混淆导致市场教育；RAG检索/Agent行动；Nexusflow收购与资源差异；放弃归属收入具体数字未公开；融资1亿是节目披露不等于收入；开源极端优化取舍；AI平台和personal-agent交互是愿景；承接前章避免重复人物传记。 |
| speech-07 | section | yes | sources/transcript.txt 01:29:27–01:46:50 | Agent 时代的评测、技术品味与职业选择 |
| voice-07 | text | optional | sources/transcript.txt 01:29:27–01:46:50 | Arena偏好指标与任务完成评测；初级岗位与培养断层为嘉宾分析，非统计预测；复杂数据标注；跨专业门槛下降；批评代码要能定位问题和给方案；正直善良和合作；本科/博士/在职不同处境；勇于放弃非无条件退学辞职，保留判断与资源。 |

## Existing Note

- none

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
