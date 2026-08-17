# Self-Evolving Agents 2026 专题课程

本目录把 NICE 学术发布的 11P 专题研讨会《全球嘉宾共话 Self-Evolving Agents：从学术前沿到产业落地》整理为一门中文专题课程。原视频包含两个简短开场、七场主题报告和两场 Panel；课程讲义将两个开场并入课程导读，其余内容整理为九个教学单元。

## 课程来源

- 视频合集：<https://www.bilibili.com/video/BV1P4LX68EcS>
- 发布方：NICE 学术
- 发布日期：2026-06-17
- 视频总时长：约 5 小时 54 分钟
- 字幕状态：无公开 CC 字幕，使用 Whisper 转写并人工结合画面校正术语
- 画面状态：匿名访问可稳定取得 480P；若后续获得登录态 1080P，将优先替换密集课件截图

## 课程结构

| 讲次 | 原分 P | 主题 | 类型 |
|---:|---:|---|---|
| 1 | P2 | Open-Ended Worlds 中的 Causal World Understanding 与 Self-Improving Agents | 主题报告 |
| 2 | P3 | Towards Self-Evolving LLM Agents: LLM-as-Optimizer and Agentic RL | 主题报告 |
| 3 | P4 | From Failed Foresight to Self-Evolving Agents | 主题报告 |
| 4 | P5 | Agent-World：让智能体与环境协同进化 | 主题报告 |
| 5 | P6 | 上午场 Panel：世界模型、Agentic RL 与环境协同 | 讨论课 |
| 6 | P8 | 迈向经验智能：从 Context Engineering 到 Context Learning | 主题报告 |
| 7 | P9 | Agent Externalization and Self-Evolving | 主题报告 |
| 8 | P10 | Theory of Agent: Towards the Second Half of Machine Intelligence | 主题报告 |
| 9 | P11 | 下午场 Panel：经验、外化、个性化与产业落地 | 讨论课 |

## 生成流程

1. 运行 `./download_materials.sh` 获取公开视频、音频与封面；原始媒体由 `.gitignore` 排除。
2. 每讲建立 `lecture-manifest.md`、coverage matrix 与 teacher-voice ledger。
3. 无 CC 字幕时使用 `tools/scripts/transcribe_faster_whisper.py` 或 OpenAI Whisper 生成逐讲 SRT。
4. 对字幕时间段密集采样画面，制作 contact sheet 后选择完整、清晰的最终课件状态。
5. 逐讲编写中文 LaTeX，双遍 XeLaTeX 编译，运行 coverage、质量和视觉 PDF QA。
6. 九讲完成后生成课程总 PDF，并更新仓库索引与跟踪文件。

## 最终交付

- 课程总讲义：`self-evolving-agents-2026-notes.tex`
- 本地课程 PDF：`self-evolving-agents-2026-notes.pdf`（71 页）
- PDF 视觉 QA：`qa/self-evolving-agents-2026-notes/contact.png` 与 `qa-report.md`
- 九个单元的转写、manifest 与 teacher-voice ledger 均已完成

详细生成记录与审计结果见 `course-plan.md`。
