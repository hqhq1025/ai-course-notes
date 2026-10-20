# Argon 调用与课程写作方式

本版把连续性保存在资料、章节蓝图和完整讲义中。每次调用都显式提交整讲来源和主线；生成后再通读整讲编辑。

## 本次调用诊断

2026-10-20 UTC，在当前执行主机上测试了以下调用方式。

| 请求 | 结果 | 观测 |
|---|---|---|
| coproxy，整讲输出，high reasoning，60,000 token 上限 | 两次断流 | 约 630.110 秒与 630.265 秒，`upstream stream error: unexpected EOF` |
| 绕过 coproxy，直连同一 Copilot 上游，重放第一讲输入 | 断流 | 537.852 秒，收到 47,925 字符后 `Response ended prematurely`，没有完成事件 |
| coproxy，按章节输出，medium reasoning，24,000 token 上限 | 正常完成 | 每次携带整讲来源和写作蓝图 |
| coproxy，整讲编辑，只返回修改片段 | 正常完成 | 完整初稿与来源同时作为输入，逐字段应用修改 |

直连也出现了断流，说明绕过 coproxy 并不足以解决问题。当前证据将问题范围缩小到上游请求链路；没有定位到具体服务节点。长请求的断点也并非固定一致。

另外核对了实际运行的 coproxy 二进制和超时计算。版本显示为 0.8.5，构建提交为 `4ab5bb8fe1d10ef589aa3119940dea55120a1d86`。其流式写超时按配置计算为 3,630 秒，与观测到的约 630 秒不符。本次没有改动或重启共享代理。

## 当前采用的流程

1. 先准备官方讲义、逐页课件文字、字幕补充和 GitHub 案例。
2. Argon 制定整讲主线，分配全部课件页，提取教师的动机、例子和推理。
3. 按教学章节请求正文。每章都带上整讲来源和主线，采用 `medium` 推理强度。
4. 保存完成的章节、模型回执和原始输出。中断后只重试缺失章节。
5. 事实审阅后，将完整初稿、全部来源和审阅结果交回 Argon。编辑请求只返回确切的文字替换。
6. 校核替换位置和课件页码，再生成 TeX、Markdown 与 PDF。检查公式、代码、来源覆盖和实际页面。

成稿仍以逐页课件为组织骨架，每页对应图前引导、读图和展开说明。字幕中的例子与转折主要放进展开说明。这保证了课件覆盖，但也容易把现场探索压进长段落，让读者先看到整理后的结论。

## 字幕输入与使用核对

已检查八讲的 63 个 `section-NN-prompt.txt`：每个请求都包含对应整讲 `sources/community-transcript.md` 的完整内容，每讲约 1.8 万到 2.7 万字符。前两讲另外传入本地校订 ASR 字幕。请求构造见 `tools/scripts/nju_gse_argon/argon_writer.py` 的 `sources()`。

逐讲抽样表明，采集卡抢修、网页填表、标签打印机试打、汉诺塔、教务系统与 Agent 循环等口述内容已进入正文。部分现场转折被压缩，例如老师如何纠正二维码任务的错误起点，以及 HTML 卡片演示怎样引出 Harness。输入包含字幕，并不等于成稿完整保留了老师的探索顺序。

阅读排版更新在八讲中增加了 186 处分段、分点、编号和短语强调。原始 `prose.json` 保留，排版差异记录在 `presentation.json`。这一轮改善呈现；若继续调整教学结构，应按“提出问题、尝试、观察、纠正、形成结论”组织案例，再把课件放到对应位置。

## 复用入口

本次脚本位于仓库内 `tools/scripts/nju_gse_argon/`。依赖和恢复说明见该目录 README。在仓库根目录运行：

```bash
python3 tools/scripts/nju_gse_argon/run_chapters.py 1 2 3 4 5 6 7 8 --workers 4
python3 tools/scripts/nju_gse_argon/edit_lectures.py 1 2 3 4 5 6 7 8 --workers 3
python3 tools/scripts/nju_gse_argon/refine_lectures.py 1 2 3 4 8
python3 tools/scripts/nju_gse_argon/render_notes.py 1 2 3 4 5 6 7 8
python3 tools/scripts/nju_gse_argon/build_notes.py 1 2 3 4 5 6 7 8
```

已经完成的模型调用从文件恢复。上述顺序先恢复编辑，再应用残留问题的定点修订。修改输入后，应使用新的阶段名称保存结果，避免将旧缓存当作新生成。

调用端点为本机 `http://127.0.0.1:8536/v1/chat/completions`，模型固定为 `gemini-4-argon`。客户端会检查返回模型、结束原因和流结束标记。断流仍保存收到的文本与错误回执；残缺 JSON 不进入排版。

## 记录位置

- 各讲 `generation/plan.json`：主线与覆盖蓝图。
- `section-NN.json`、`bookends.json`：完成的章节与导读总结。
- `prose-draft.json`：整讲编辑前的初稿。
- `editorial.json`、`editorial-applied.json`：Argon 的全讲修改及应用结果。
- `refinement.json`：对复核发现的定点修订，仅有关讲次有此文件。
- `prose.json`：排版使用的最终正文。
- `presentation.json`：保持原文的分点、编号和强调记录。
- `*-receipt.json`：模型、耗时、结束原因、token 统计与哈希。
- `qa/`：覆盖、质量、代码核查和 PDF 视觉检查。

直连对照的诊断保存在 `diagnostics/argon-direct-probe.json`。调用记录不包含认证信息。逐页渲染、联系表和断流临时缓冲在本地生成，Git 保留最终正文、原始输出、回执和 QA 文字记录。
