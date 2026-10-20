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

正文不把每页课件重新介绍一遍。段落先提出问题，再说明输入和条件，展开机制与例子，最后接到下一步。只有定义、关键机制和具体易错点进入知识框。课堂猜想保留一次清楚的归属；影响推导的条件放在解释中。

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
- `*-receipt.json`：模型、耗时、结束原因、token 统计与哈希。
- `qa/`：覆盖、质量、代码核查和 PDF 视觉检查。

直连对照的诊断保存在 `diagnostics/argon-direct-probe.json`。调用记录不包含认证信息。逐页渲染、联系表和断流临时缓冲在本地生成，Git 保留最终正文、原始输出、回执和 QA 文字记录。
