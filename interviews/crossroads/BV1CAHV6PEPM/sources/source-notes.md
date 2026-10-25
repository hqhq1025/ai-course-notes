# 李磊访谈来源与校正

本期是《十字路口》对谈李磊，B 站视频 `BV1CAHV6PEPM`，时长 51 分 45 秒。B 站与小宇宙标记的发布时间换算到北京时间均为 2026-10-26 00:00。节目原声是讲义主线；以下资料用于校正专名、身份和技术定义。

## 同源材料

- [B 站原视频](https://www.bilibili.com/video/BV1CAHV6PEPM/)。讲义时间戳以这版为准。
- [同源 YouTube](https://www.youtube.com/watch?v=oDdQGehy7uQ)。频道是 Koji 杨远骋，标题相同，时长同为 3105 秒。
- [小宇宙正式节目页](https://www.xiaoyuzhoufm.com/episode/6add84e197726cd467573cf1)。官方章节说明保存在 `official-shownotes.txt`。音频版时长 3110 秒，不直接替换 B 站时间轴。
- 官方说明称文字版将发布于“十字路口 Crossing”公众号。小宇宙给出 App 文稿入口，公开网页中取得的是节目介绍和章节说明，尚未取得公开全文。正文应使用已取得的完整音频转写。

## 十条具体校正

1. 嘉宾是 HKU-NLP 在读博士 Lei Li，个人主页为 [lilei-nlp.github.io](https://lilei-nlp.github.io/)。本科就读西安电子科技大学，硕士就读北京大学，2023 年 9 月进入香港大学。节目称他是小米 MiMo 后训练研究员；不能写成已经博士毕业，也不能套用同名教授的履历。主页导师写为 Lingpeng Kong 和 Qi Liu；未核准中文姓名时保留英文。
2. 开场提到的获奖论文是 [Label Words are Anchors: An Information Flow Perspective for Understanding In-Context Learning](https://aclanthology.org/2023.emnlp-main.609/)。[EMNLP 2023 官方获奖名单](https://2023.emnlp.org/program/best_papers/)列出该论文和 Lei Li。李磊是合作者，不能写成独自完成或唯一第一作者。会议日期为 2023 年 12 月 6 日到 10 日；口述的“11 月、入学两个月”可整理成“2023 年入学后不久”。
3. 05:44、06:34 等处硬字幕确写 Astra。保留这个专名。讨论重点是前沿模型仍有能力短板，以及亲自搭建测试来找到研究问题。不需要自行补全未出现的产品版本、参数或排行榜。
4. 24:55 硬字幕确写 Eric Wallace。25:09 画面与字幕提到 OpenAI、Hugging Face 和 Swarm。[OpenAI 的正式事件页](https://openai.com/hugging-face-incident-and-misalignment/)确认 Eric Wallace 与 Michael Dalton 于 2026 年 8 月 5 日在 Black Hat 复盘事件。讲义只需保留嘉宾用此例说明选题与时机的作用。不要写成 Wallace 主动组织了一次攻击，也不要把这里的 swarm 自动等同于某个同名开源框架。
5. 00:49 与 39:58 所说 MiMo 直播是后训练中的强化学习训练。[官方训练指标页](https://mimo.xiaomi.com/rl/)标明 MiMo-V2.6 Pro 和 Flash 两个 run，指标来自 trainer logs。它不是从零预训练全过程的直播。网页可核准指标名称，不用补入节目未讨论的模型参数量、成本或当前性能排名。
6. 46:26 硬字幕把 ASR 的 `pulster trim bench` 校正为 PostTrainBench。[项目页](https://posttrainbench.com/)和[论文](https://arxiv.org/abs/2603.08640)说明，它让 LLM agent 在固定算力预算下改进给定的基础模型，实验预算为一张 H100、10 小时。评估重点是自动后训练能力，不能直接据此断言系统已经具备完整自主科研能力。
7. 46:45 的 `capacity` 应为 Karpathy；46:47 的“虚拟两国际 model”应为“训 Language Model 那个东西”；46:48 的 `pul` 应为 PPL。硬字幕均已检查。嘉宾没有在这里说清具体仓库，不要硬写成 nanochat 或 autoresearch。节目画面出现 90、38 等下降曲线数字，是示意画面，没有实验设定与数据出处，不当成实测结果。
8. RSI 在这段指递归自我改进（recursive self-improvement）。李磊区分生成训练数据、搜索训练参数或算法，与判断下一步什么问题值得研究。后者对应他所说的 research taste。结论应保持这一层次，不能把“信号越来越强”改写为“AI 已经能够独立定义并完成所有研究”。PPL 如进入正文，首次解释为困惑度，即交叉熵取指数；它衡量给定评测文本上的预测损失，不覆盖科研品味。
9. 47:46 的基准是 [Video-MME](https://video-mme.github.io/home_page.html)，官方仓库为 [MME-Benchmarks/Video-MME](https://github.com/MME-Benchmarks/Video-MME)。初版有 900 段视频、2700 道人工标注问答，覆盖不同视频时长，并区分有无字幕的评测设置。节目讲的是选择有价值的评测问题和让团队采用基准；不需要把整张当前榜单搬入讲义。不要将初版与后来的 Video-MME-v2 混用。
10. “大粉理论”是节目对小红书粉丝数超过论文引用数的调侃；它引出传播和研究被采用的话题，不是学术质量公式。42:03 的“数商”指向训练团队提供数据的数据供应商。不能解释成数字商或个人数商能力。导师、地区、快慢科研、专业选择等建议应保留嘉宾的条件与个人经验。避免改写成所有学校或公司的统一制度。

## 进一步核对

- [Hugging Face 下载统计文档](https://huggingface.co/docs/hub/models-download-stats)说明，计数基于特定文件的 GET 或 HEAD 请求；默认计数文件可以是 `config.json`。下载次数不要求下载完整权重，也不等于独立使用者或真实部署数。12:16 附近节目用“下载需硬盘”解释操纵成本，讲义应保留图的原意，同时纠正这一机制推论。
- 孙栩的[本人主页](https://xusun26.github.io/)明确给出中英文姓名。孔令鹏的[本人主页](https://ikekonglp.github.io/)与[高校中文简介](https://ceisd.shanghaitech.edu.cn/2026/0414/c17397a1125254/page.htm)相互对应。
- 16:22 硬字幕为“代季峰”，[清华主页](https://web.ee.tsinghua.edu.cn/daijifeng/zh_CN/index.htm)确认姓名；16:24 为“自然意志”。不要把这两处改成“戴季峰”或“深言科技（自然语义）”。

## 官方十个问题的时间线

| 时间 | 问题 |
|---|---|
| 03:28 | AI 时代，PhD 怎么拿到理想的结果？ |
| 08:07 | AI 论文大水漫灌，顶会怎么办？ |
| 12:16 | “大粉理论”：小红书粉丝多于论文引用 |
| 16:50 | PhD 从入学到毕业，要过哪几关？ |
| 20:08 | 没论文、没实习，PhD 怎么冷启动？ |
| 25:28 | 选学校还是选导师？ |
| 28:12 | 慢科研还是快科研？ |
| 31:08 | 内地、香港、美国，去哪读 PhD？ |
| 35:27 | 导师创业，PhD 得到了什么？ |
| 36:52 | 本科能进 AI Labs，还要读 PhD 吗？ |

后续讨论为 39:58 MiMo 后训练直播、42:03 数据公司、46:00 RSI、47:46 Video-MME、49:00 CS 专业、50:20 高三生选专业、51:24 饭要吃与觉要睡。
