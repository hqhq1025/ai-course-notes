# Progress Log

## 2026-08-18 Agentic AI MOOC Fall 2025 全套笔记

- 用户创建长期目标：查找 Agentic AI Learning 最新课程；若没有更新版本，则采用 Fall 2025，并按仓库最高标准整理全套笔记。
- Lecture 06 已按官方 51 页 deck 完成 source-first 重写：48 个 required 教学页全部入文，成稿 45 页、48 图、41 个教学盒、每图 265 字；strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX、日志检查与 45 页视觉 QA 均通过并签署。
- Lecture 07 已按官方 42 页 deck 完成 source-first 重写：42/42 页全部入文，成稿 42 页、42 图、45 个教学盒、每图 289 字；strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX、日志检查与视觉 QA 均通过并签署。
- Lecture 08 已按 video-first 标准完成：官网无 deck，8 个独立录像教学状态全部写入 manifest 并入文，成稿 21 页、36 个教学盒、7 处读图说明；strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX、日志检查与视觉 QA 均通过并签署。
- Lecture 09 已按官方 40 页 deck 完成 source-first 重写：40/40 页全部入文，成稿 41 页、40 图、45 个教学盒、每图 316 字；strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX、日志检查与视觉 QA 均通过并签署。
- Lecture 10 已按 video-first 标准完成：5 张录像教学帧与 3 张明确标注的讲义机制图形成 8 节点视觉主线，成稿 23 页、48 个教学盒、7 处读图说明；strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX 与视觉 QA 通过。QA 首轮发现 16-bit RGBA 图在 PDF 中空白，转为 8-bit RGB 后复验通过。
- Lecture 11 已按 video-first 标准完成：4 张录像教学帧与 4 张明确标注的讲义机制图形成 8 节点视觉主线，成稿 23 页、48 个教学盒、8 处读图说明、3 个 teacher-voice 标记；strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX、日志检查与视觉 QA 均通过并签署。
- Lecture 12 已按官方 99 页 deck 完成 source-first 重写：28 个目录/严格渐进/行政页有据标记 optional，71 个独立教学状态全部入文；成稿 63 页、71 图、62 个教学盒、每图 260 字，strict coverage 零警告，质量 `⭐⭐⭐`，双遍 XeLaTeX、日志检查与 63 页视觉 QA 均通过并签署。
- Agentic AI MOOC Fall 2025 全套 12/12 已完成逐讲验收：合计 497 页、472 个教学视觉、589 个教学盒。README、TRACKING、NOTE_GENERATION_TODO 与课程 README 已按实际 370 份 TeX 讲义口径更新。
- 最终批量验收完成：12/12 `check_note_coverage.py --strict` 零 warning，课程级 `check_quality.sh` 全部 `⭐⭐⭐`，12 份 PDF/QA/artifact 与日志均通过；`uv run --with pytest pytest -q tests/test_generate_site.py` 为 16 passed，`git diff --check` 通过。
- 已确认当前 thread 存在 active goal，未重复创建。
- 已读取课程笔记 source-first delivery skill、仓库 `AGENTS.md`、`QUALITY.md` 与现有持久计划。
- 已检查工作树：存在 `.Codex/`、若干 talk/interview 素材等无关未跟踪文件；本任务将保留它们。
- 已通过官方根域、Fall 2025 页面、官方 GitHub 和公开搜索核验：截至 2026-08-18 未发现该项目公开的 2026 新课程，根域仍 canonical redirect 到 `/f25`。
- 已解析官方完整课表：12 场教学讲座，另有一周 Thanksgiving 停课。
- 已审计本地 `talks/berkeley-llm-agents/f25`：已有 11 个倒序 lecture 目录与完整字幕，缺少 Oct 6 的 Agent Evaluation 讲座；旧稿无 PDF、无 source-first artifacts、无 visual QA。
- 已将课程目录迁移为官方正序 `lecture01--12`，并新增课程 README 与 course manifest。
- 已补齐 L04 的 94 分钟录像字幕、封面和 104 页官方 deck。
- 已下载、校验并渲染 9 份正式课堂 deck，共 540 页；L12 仓库 deck 已通过录像抽帧身份核验。
- 已为 12 讲生成初始 `lecture-manifest.md`。
- 最新版本核验、本地映射审计和课程级工作台账阶段完成；开始 Lecture 01 source-first 重写。
- Lecture 01 已完成 source-first 重写：86 页 deck 中 69 个教学节点纳入正文，17 个行政/过渡/重复 build-up 节点有明确省略理由。
- Lecture 01 最终为 60 页、69 张官方 slide、64 个教学盒、19,124 个正文字符；strict coverage 零 warning，质量 `⭐⭐⭐`，双遍 XeLaTeX 通过。
- Lecture 01 canonical PDF QA 渲染 60/60 页且无 near-blank page；已检查完整 contact sheet 及第 14、33、42、54、60 页原图并签署报告。
- 下一步进入 Lecture 02：Yangqing Jia 的 37 页 `Evolution of System Designs from an AI Engineer Perspective`。
- Lecture 02 已完成 source-first 重写：37 页 deck 中 29 个独立教学节点纳入正文，8 个章节过渡/重复 build 节点有明确省略理由。
- Lecture 02 最终为 34 页、29 张官方 slide、47 个教学盒、12,386 个正文字符；strict coverage 零 warning，质量 `⭐⭐⭐`，双遍 XeLaTeX 日志无硬错误或版式溢出。
- Lecture 02 canonical PDF QA 渲染 34/34 页且无 near-blank page；已检查完整 contact sheet 及第 11、20、22、34 页原图并签署报告。
- 下一步进入 Lecture 03：Jiantao Jiao 的 44 页 `Post-Training Verifiable Agents`。
- Lecture 03 已完成 source-first 重写：44 页 deck 中 40 个独立教学节点纳入正文，4 个步骤过渡页有明确省略理由。
- Lecture 03 最终为 42 页、40 张官方 slide、41 个教学盒、11,758 个正文字符；strict coverage 零 warning，质量 `⭐⭐⭐`，双遍 XeLaTeX 日志无硬错误或版式溢出。
- Lecture 03 canonical PDF QA 渲染 42/42 页且无 near-blank page；已检查完整 contact sheet 及第 16、22、42 页原图并签署报告。
- 下一步进入 Lecture 04：补齐此前缺失的 104 页 `Agent Evaluation & Project Overview`。
- Lecture 04 已从零完成：104 页 deck 中 78 个独立教学节点纳入正文，26 个封面/过渡/重复 build/纯链接页有明确省略理由。
- Lecture 04 最终为 64 页、78 张官方 slide、55 个教学盒、20,709 个正文字符；strict coverage 零 warning，质量 `⭐⭐⭐`，双遍 XeLaTeX 日志无硬错误或版式溢出。
- Lecture 04 canonical PDF QA 渲染 64/64 页且无 near-blank page；已检查完整 contact sheet 及第 42、54、58、64 页原图并签署报告。
- 下一步进入 Lecture 05：Weizhu Chen 的 37 页 `Challenges and Lessons from Training Agentic Models`。
- Lecture 05 已完成 source-first 重写：37 页 deck 中 31 个独立教学节点纳入正文，6 个封面/章节/Q&A 页有明确省略理由。
- Lecture 05 最终为 39 页、31 张官方 slide、57 个教学盒、13,843 个正文字符；strict coverage 零 warning，质量 `⭐⭐⭐`，双遍 XeLaTeX 日志无硬错误或版式溢出。
- Lecture 05 canonical PDF QA 渲染 39/39 页且无 near-blank page；已检查完整 contact sheet 及第 15、18、39 页原图并签署报告。
- 下一步进入 Lecture 06：Noam Brown 的 51 页 `Multi-Agent AI`。

## 2026-08-11 CS25 + CS153 rewrite

- 用户要求继 CS336 2026 后，对 CS25 与 Frontier Systems 全部讲义做同标准重写。
- 初始本地范围为 CS25 40 讲、CS153 11 讲；后续官方播放列表核验确认 CS25 V1--V5 实际为 41 讲，本地缺 Lecture 37，V6 另有 9/9 场公开录像。
- 已核验 wdkns upstream commit，开始建立逐讲素材与质量基线。
- 完成第一轮基线：51/51 当前均为 `⭐`，没有本地生成 PDF、manifest 或 canonical QA；CS153 11 讲与 CS25 大多数讲次都只有字幕和封面。
- 下一步核验官方课程范围、视频/slide 可访问性，并抽样读取旧稿判断可复用内容比例。
- 已完成 CS153 Lecture 01 新标准样板：替换为 Stanford Online 官方视频 `O5PfU_uDhS0`、官方人工字幕和官方封面，新增 27 张完整教学 slide、manifest、blueprint、coverage matrix 与 teacher-voice ledger。
- Lecture 01 重写后为 31 页、27 图、38 个教学盒；strict coverage 零 warning，质量 `⭐⭐⭐`，最终双遍 XeLaTeX 无版式溢出。
- 已生成 canonical QA，检查 contact sheet 与第 24/27/31 页原图并签署 QA 报告。下一步进入 Lecture 02 官方源核验和 slide/frame 重建。
- 已完成 CS153 Lecture 02：确认历史视频 `yeA-opPcYxk` 已 private，保留本地时间戳字幕与官方封面，新增可复现 `lecture02-diagrams.py` 和 12 张 transcript-grounded 教学图。
- Lecture 02 重写后为 20 页、12 图、30 个教学盒；strict coverage 零 warning、质量 `⭐⭐⭐`、最终双遍 XeLaTeX 无版式 warning。
- 已修复二级目录造成的近空白页，改为一级目录并加入社区平台变更评审附录；canonical QA 无 near-blank page，检查 contact sheet 与第 16/20 页原图并签署报告。
- 已启动 CS153 Lecture 03：确认历史视频 `jB13kCmWT2k` 已 private，完成 5 分钟字幕时间窗与 Apollo/Rubix/Maven/Warp Speed/隐私等主题锚点抽取，并找到 Palantir 官方 Apollo 与 Rubix 一手架构资料。
- 已完成 CS153 Lecture 03：以本地时间戳字幕为课堂主线，结合 Palantir Apollo Demo Day 与当前 Rubix 官方架构材料，新增 13 张 transcript-grounded diagrams 和 8 张官方产品/架构图。
- Lecture 03 最终为 24 页、21 图、33 个教学盒；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无 overflow/undefined warning。
- 已人工检查 canonical QA contact sheet 及 Apollo、Rubix、privacy-security frontier、末页等全尺寸页面并签署报告。CS153 当前完成 3/11，下一步进入 Lecture 04。
- 已完成 CS153 Lecture 04：确认历史视频 `qzT8I-J8sQ8` 已 private，以本地 1208 条时间戳字幕为课堂主线，并补入无监督机器翻译、HTPS、Chinchilla、LLaMA、Mistral 7B 五篇一手论文与欧盟委员会现行 GPAI 指引。
- Lecture 04 新增 16 张可复现 transcript-grounded diagrams，正文重构为 research question → formal verifier → scaling objective → training debugging → checkpoint-to-solution → product feedback → post-training operating system。
- Lecture 04 最终为 24 页、16 图、31 个教学盒；strict coverage 零 warning、8 个 teacher-voice markers、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式 warning，canonical QA 已人工签署。CS153 当前完成 4/11。
- 同步修复质量工具：SRT 转换支持点号毫秒；coverage/quality 正确识别 figure 与 teacher-voice 宏；manifest 自动列出 `source-materials/`；相关测试 9/9 通过。
- 已完成 CS153 Lecture 05：历史视频 `9SqYFxp9yRM` 已 private，以本地 931 条时间戳字幕为课堂主线，并用 Vercel/Next.js 官方资料核验 Framework-Defined Infrastructure、Build Output API、ISR、Fluid Compute、Spend Management 与 Observability。
- Lecture 05 新增 16 张可复现 transcript-grounded diagrams，正文重构为 application intent → IR → infrastructure 与 traffic → telemetry/metering → developer decision 两个闭环。
- Lecture 05 最终为 22 页、16 图、29 个教学盒、7 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。CS153 当前完成 5/11。
- 修复术语检查器将 `scale-to-zero` 误判为 `ZeRO` 的大小写/边界问题；质量脚本测试现为 10/10 通过。
- 已完成 CS153 Lecture 06：确认历史视频 `LriOr64E8D8` 已 private，以本地 1266 条时间戳字幕为课堂主线，并用 Saudi DGA、KFSHRC、Groq/Aramco Digital、`AI and Memory Wall` 与 in-memory computing 一手资料校验关键机制。
- Lecture 06 新增 16 张可复现 transcript-grounded diagrams，正文按 hardware efficiency → application diffusion → governance/accountability 三层重构，并显式区分讲者估计、官方事实和工程判断。
- Lecture 06 最终为 27 页、16 图、43 个教学盒、7 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。CS153 当前完成 6/11。
- 已完成 CS153 Lecture 07：确认历史视频 `4jDQi9P9UIw` 已 private，以本地 1288 条时间戳字幕为课堂主线，并用 Cursor secure indexing/privacy/Fast Apply/CursorBench/Router、turbopuffer、PostgreSQL 与 S3 一手资料校验持久机制。
- Lecture 07 新增 16 张可复现 transcript-grounded diagrams，正文按 context loop、edit loop 与 reliability loop 重构，覆盖 Merkle sync、embedding cache、blast radius、retry cascade、MVCC/vacuum、object-storage search、global inference、provider routing、security 和 abuse。
- Lecture 07 最终为 24 页、16 图、37 个教学盒、8 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。CS153 当前完成 7/11。
- 已完成 CS153 Lecture 08：历史视频 `MBD0Ah9cpYU` 当前要求登录，以本地 833 条时间戳字幕为课堂主线，并用 Thorn、NCMEC 与 NIST 一手资料校验 Match/Predict、Safety by Design、报告口径和 AI risk management。
- Lecture 08 新增 16 张非敏感、可复现 transcript-grounded diagrams；正文按 response loop、trusted-data loop 与 governance loop 重构，覆盖 hash matching、predictive triage、moderator wellbeing、calibration/queue capacity、E2EE/privacy、conversation/graph signals、startup safety 和 ecosystem roles。
- Lecture 08 最终为 25 页、16 图、36 个教学盒、11 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。初版 26 页存在仅两条参考资料的空尾页，已压缩为 25 页。CS153 当前完成 8/11。
- 视觉抽查时 `magick montage` 不可用，按仓库兼容说明改用 ImageMagick 6 的 `montage` 成功完成关键页拼图。
- 已完成 CS153 Lecture 09：以本地 1033 条时间戳字幕为课堂主线，并用 Okta Universal Directory/Identity Engine、官方 incident RCA、Auth0 并购资料、NIST Zero Trust 与 OAuth/OIDC/SCIM/WebAuthn 标准校验关键机制。
- Lecture 09 新增 16 张可复现 transcript-grounded diagrams，正文按 access loop、trust/incident loop 与 technology-transition loop 重构，覆盖 identity lifecycle、front-door SLO、board information loop、security-first culture、agent delegation/token lifecycle 与 two-platform acquisition boundary。
- Lecture 09 最终为 24 页、16 图、31 个教学盒、8 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。CS153 当前完成 9/11。
- 已完成 CS153 Lecture 10：以本地 1025 条时间戳字幕为课堂主线，并用 scaling laws、GPT-3、InstructGPT、Constitutional AI/RLAIF、Anthropic evaluation/interpretability、RSP v3.0 与 API lifecycle 官方资料校验关键机制。
- Lecture 10 新增 16 张可复现 transcript-grounded diagrams；正文按 scaling loop、training recovery loop、safety loop 与 chat-to-API product loop 重构，并显式区分 2025 课堂 ASL framing 与 2026-02-24 发布的 RSP v3.0。
- Lecture 10 最终为 23 页、16 图、29 个教学盒、7 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。CS153 当前完成 10/11。
- 已完成 CS153 Lecture 11：以 Joe Sullivan 39:17 时间戳字幕为课堂主线，并用 CISA/DOJ VDP、NIST SP 800-61 Rev. 3、SEC disclosure rule、第九巡回法院与美国最高法院官方记录校验 VDP、事件响应、披露治理与案件状态。
- Lecture 11 最终为 26 页、16 图、45 个教学盒、7 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式或引用 warning，canonical QA 已人工签署。
- CS153 Winter 2025 全量重写完成 11/11，共 270 页。全课 strict coverage、`⭐⭐⭐`、QA 五项签署与 LaTeX artifact hygiene 均通过；focused regression tests 26/26 通过。下一阶段进入 CS25 V1--V5 共 40 讲重写。
- 已完成 CS25 Lecture 01 新标准样板：定位 Stanford Online 官方视频 `P127jhj-8-Y`，从视频恢复 17 张 distinct teaching slides，新增 `cs25-preamble.tex`、sanitized metadata、manifest、blueprint、coverage matrix、teacher-voice ledger 与 source index。
- Lecture 01 重写为 25 页、17 图、35 个教学盒、9 个公式块、1 个 attention 伪代码 listing 与 6 个 teacher-voice markers；strict coverage 零 warning、质量 `⭐⭐⭐`、双遍 XeLaTeX 无版式 warning，canonical QA 已人工签署。按修正后的官方 V1--V5 范围，CS25 当前完成 1/41。
- 官方 CS25 播放列表实时返回 50 个条目：V1--V5 41 讲、V6 9 讲。V1--V5 完成后需要补建本地缺失的 Lecture 37，并继续 V6 九讲，不再使用“V6 仅前三讲公开”的旧快照。

---

## 2026-05-04
- Started update batch after user approval.
- Loaded planning, YouTube PDF, Bilibili PDF, and verification skills.
- Verified local tooling availability.
- Counted current notes: 290 PDFs and 289 TeX files before this batch.
- Confirmed Bilibili new videos have public metadata but no platform subtitles.
- Marked Bilibili note generation blocked due to B站 412 plus missing Whisper.
- Updated README and TRACKING with current inventory and active-course backlog.
- Downloaded CS336 Spring 2026 official materials for lecture05-10 into `cs336-2026/`.
- Verified downloaded CS336 files by `file` and `wc -c`.
- Final verification: 290 `*-notes.pdf` files, no stale README/TRACKING strings found, `git diff --check` clean, and CS336 downloaded files have valid file types.
- Created `NOTE_GENERATION_TODO.md` to track pending note generation.
- Confirmed 4 A100 80GB GPUs are visible via `/proc/driver/nvidia/gpus`.
- Confirmed `faster-whisper` and cached large-v3 model exist, but YouTube and Bilibili downloads currently require cookies.
- Downloaded Modern Agent 17 via public Bilibili playurl API, extracted audio, transcribed on A100 with faster-whisper large-v3, generated key frames, wrote TeX, and compiled `lecture17-notes.pdf`.
- Attempted Agentic RL 16 via public Bilibili playurl API; only preview-length media was accessible, so no incomplete PDF was generated.
- Verification after Modern Agent 17: note count is 291, generated PDF/TeX/SRT exist, no stale README/TODO strings found, and `git diff --check` is clean.
- Switched focus to CS336 at user request.
- Generated `cs336-2026/lecture01/lecture01-notes.tex` from official Spring 2026 `lecture01-slides.py`.
- Compiled initial `cs336-2026/lecture01/lecture01-notes.pdf` draft with XeLaTeX; output was 9 pages and was later superseded by the quality rewrite.
- Updated README/TRACKING/TODO after CS336 lecture01; note count temporarily became 292 before lecture02 was added.
- User clarified that CS336 notes must meet the repository depth standard rather than a thin summary.
- Rewrote `cs336-2026/lecture01/lecture01-notes.tex` into a deeper 964-line course note, removed manual TikZ figures, and added official image assets under `cs336-2026/lecture01/images/`.
- Recompiled `cs336-2026/lecture01/lecture01-notes.pdf` twice with XeLaTeX; current PDF is 27 pages by `mutool`, with 11 images including cover, 22 teaching boxes, 13 section-level summaries, and 9 code listings.
- Patched `tools/scripts/check_quality.sh` to fall back to `mutool` when `pdfinfo` is unavailable and to count actual box environments.
- Final verification: `tools/scripts/check_quality.sh cs336-2026/lecture01/lecture01-notes.tex` later reports `28p ⭐⭐⭐`, and `git diff --check` passed.
- Continued CS336 Spring 2026 with lecture02 at the same depth standard.
- Downloaded lecture02 figure assets, wrote `cs336-2026/lecture02/lecture02-notes.tex`, and compiled `lecture02-notes.pdf` twice with XeLaTeX.
- Lecture02 verification: `tools/scripts/check_quality.sh cs336-2026/lecture02/lecture02-notes.tex` later reports `26p ⭐⭐⭐`; note count became 293 PDFs.
- Resumed CS336 Spring 2026 at user request with stricter quality bar: deep exposition, careful technical detail, and one verified lecture at a time.
- Started `cs336-2026/lecture03/`, using official lecture03 slides plus the existing CS336 lecture03 note as a cross-check, not as a replacement for fresh writing.
- Wrote `cs336-2026/lecture03/lecture03-notes.tex` as a fresh Spring 2026 architecture/hyperparameters note with conservative recipe tables, formulas, code snippets, official slide figures, and explicit engineering judgment sections.
- Compiled `cs336-2026/lecture03/lecture03-notes.pdf` with XeLaTeX; quality verification reports `35p 11s 24b 33f ⭐⭐⭐`, and repository note count is now 294 PDFs.
- Continued to `cs336-2026/lecture04/` at user request.
- Confirmed Spring 2026 lecture04 is broader than the old CS336 lecture04: it covers attention alternatives (linear attention, Mamba-2, Gated Delta Net, sparse adaptation/DSA) before mixture-of-experts.
- Wrote `cs336-2026/lecture04/lecture04-notes.tex` as a fresh Spring 2026 long-form note tying attention alternatives and MoE together through sparse/conditional computation.
- Compiled `cs336-2026/lecture04/lecture04-notes.pdf` with XeLaTeX; quality verification reports `38p 14s 21b 41f ⭐⭐⭐`, and repository note count is now 295 PDFs.
- Continued to `cs336-2026/lecture05/` at user request.
- Confirmed Spring 2026 lecture05 is a 55-slide GPU performance lecture: GPU/TPU architecture, memory hierarchy, low precision, fusion, recomputation, memory coalescing, tiling, matrix-performance anomalies, and FlashAttention.
- Generated 55 slide images under `cs336-2026/lecture05/slides-images/`.
- Wrote `cs336-2026/lecture05/lecture05-notes.tex` as a fresh Spring 2026 long-form GPU performance note with matmul arithmetic-intensity derivation, low-precision tradeoffs, attention IO accounting, and FlashAttention design checklist.
- Compiled `cs336-2026/lecture05/lecture05-notes.pdf` with XeLaTeX; quality verification reports `31p 9s 21b 36f ⭐⭐⭐`, and repository note count is now 296 PDFs.
- Continued to `cs336-2026/lecture06/` at user request.
- Confirmed Spring 2026 lecture06 is an executable-source lecture on benchmarking, profiling, kernel fusion, torch.compile, and Triton kernels for GeLU, softmax, row sum, and matmul+ReLU.
- Downloaded/copied lecture06 visual assets into `cs336-2026/lecture06/images/`, including official referenced images and selected L05 GPU/roofline/tiling recap figures.
- Wrote `cs336-2026/lecture06/lecture06-notes.tex` as a fresh Spring 2026 long-form Kernels/Triton note with detailed GPU programming-model review, benchmarking/profiling methodology, fusion memory accounting, and Triton kernel walkthroughs for GeLU, softmax, row sum, and matmul+ReLU.
- Compiled `cs336-2026/lecture06/lecture06-notes.pdf` twice with XeLaTeX; single-note quality verification reports `31p 13s 31b 12f ⭐⭐⭐`, and repository note count is now 297 PDFs.
- Final L06 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-06 all `⭐⭐⭐`, `find . -name '*-notes.pdf' | wc -l` reports `297`, `git diff --check` passed, and the L06 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Continued to `cs336-2026/lecture07/` at user request.
- Confirmed Spring 2026 lecture07 is an executable-source lecture on multi-GPU parallelism: collectives, interconnect hardware, NCCL/PyTorch distributed, communication benchmark methodology, and bare-bones data/tensor/pipeline parallel MLPs.
- Downloaded lecture07 visual assets into `cs336-2026/lecture07/images/`, including official CS336 diagrams for ranks/interconnect/data/tensor/pipeline parallelism and PyTorch/NCCL diagrams for broadcast, scatter, gather, reduce, all-gather, all-reduce, and reduce-scatter.
- Wrote `cs336-2026/lecture07/lecture07-notes.tex` as a fresh Spring 2026 long-form Parallelism note with detailed sections on collectives, hardware topology, NCCL/PyTorch distributed, communication benchmarking, and data/tensor/pipeline parallel MLP implementations.
- Compiled `cs336-2026/lecture07/lecture07-notes.pdf` twice with XeLaTeX; single-note quality verification reports `25p 12s 30b 14f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 298 PDFs.
- Final L07 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-07 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `298`, `git diff --check` passed, and the L07 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Continued to `cs336-2026/lecture08/` at user request.
- Confirmed Spring 2026 lecture08 is a 73-page official PDF deck titled "Parallelism Basics".
- Attempted to install missing `pdftotext` support via `sudo apt-get install poppler-utils`; host requires an interactive sudo password, so the install was blocked.
- Used existing `mutool` to extract lecture08 per-page text into `/tmp/lecture08-text-*.txt` and render 73 slide images under `cs336-2026/lecture08/slides-images/`.
- Wrote `cs336-2026/lecture08/lecture08-notes.tex` as a fresh Spring 2026 long-form Parallelism Basics note with detailed sections on networking, collective communication, ZeRO/FSDP, pipeline/tensor/sequence/expert/context parallelism, 3D/4D recipes, and recent model configurations.
- Compiled `cs336-2026/lecture08/lecture08-notes.pdf` twice with XeLaTeX; single-note quality verification reports `41p 14s 23b 51f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 299 PDFs.
- Final L08 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-08 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `299`, `git diff --check` passed, and the L08 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Installed `poppler-utils` after the user provided the sudo password for this session; `pdftotext`, `pdfinfo`, and `pdfimages` are now available.
- Continued to `cs336-2026/lecture09/` at user request.
- Confirmed Spring 2026 lecture09 is a 57-page official PDF deck titled "Scaling Laws - Basics".
- Used `pdfinfo`/`pdftotext` to inspect/extract L09 text and rendered 57 slide images under `cs336-2026/lecture09/slides-images/`.
- Wrote `cs336-2026/lecture09/lecture09-notes.tex` as a fresh Spring 2026 long-form Scaling Laws Basics note with detailed sections on data scaling, data mixture/repetition, model-engineering scaling laws, critical batch size, muP, joint data-model scaling, Kaplan vs Chinchilla, IsoFLOPS, and deployment-aware overtraining.
- Compiled `cs336-2026/lecture09/lecture09-notes.pdf` with XeLaTeX until cross-reference warnings cleared; single-note quality verification reports `36p 12s 23b 44f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 300 PDFs.
- Final L09 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-09 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `300`, `git diff --check` passed, and the L09 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Continued to `cs336-2026/lecture10/` at user request.
- Confirmed Spring 2026 lecture10 is an executable-source lecture titled "inference", covering inference metrics, arithmetic intensity, KV cache, prefill/generation, latency-throughput tradeoffs, KV compression, quantization, pruning/distillation, speculative sampling, continuous batching, and PagedAttention.
- Downloaded lecture10 visual assets into `cs336-2026/lecture10/images/`, including official CS336 figures, Scaling Book Transformer/inference/GQA diagrams, a continuous batching diagram, and a quantization diagram; converted WebP inference diagrams to PNG for local TeX compilation.
- Wrote `cs336-2026/lecture10/lecture10-notes.tex` as a fresh Spring 2026 long-form Inference note with detailed derivations, 29 figures, 41 teaching boxes, and code snippets for KV-cache decoding, latency-throughput modeling, speculative sampling, continuous batching, and PagedAttention block tables.
- Compiled `cs336-2026/lecture10/lecture10-notes.pdf` with XeLaTeX until cross-reference warnings cleared; single-note quality verification reports `30p 13s 41b 29f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 301 PDFs.
- Final L10 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-10 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `301`, `git diff --check` passed, and the L10 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- User reviewed lecture01 and tightened the writing standard: important figures need explicit read-the-figure interpretation, concept-dense passages need concentrated explanations, foundational background concepts should use diagrams/tables/formulas, and available slides should be covered comprehensively.
- Updated `AGENTS.md`, `QUALITY.md`, `CLAUDE.md`, and `tools/skills/video-render-common/writing-and-figures.md` to capture these new standards.
- Started regenerating CS336 Spring 2026 lecture01 and lecture02 from official executable sources under the new standards, rather than continuing to patch the existing notes.
- Downloaded additional local image assets for regenerated lecture01/02, including industrialization, DGX B200 topology, Marin scaling forecast/result, The Pile chart, FP8, and roofline images, so the PDFs do not depend on remote image URLs.
- Replaced `cs336-2026/lecture01/lecture01-notes.tex` and `cs336-2026/lecture02/lecture02-notes.tex` with fresh new-standard drafts, then compiled both PDFs with XeLaTeX until rerun warnings cleared.
- Final lecture01/02 regeneration verification: lecture01 reports `20p 7s 32b 15f ⭐⭐⭐`, lecture02 reports `20p 9s 38b 11f ⭐⭐⭐`, `tools/scripts/check_quality.sh cs336-2026` reports all ten CS336 2026 notes as `⭐⭐⭐`, `git diff --check` passed, and both lecture logs have no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Added mandatory PDF visual QA workflow to shared note-generation skills and project standards, including page rendering, contact sheet inspection, full-size suspicious-page review, and required TeX fixes before completion.
- Installed missing project tooling/dependencies: `latexmk`, system `ripgrep`, `fd-find`, current-venv Python packages `yt-dlp`, `openai-whisper`, `torch` CPU, `pypdf`, `pdfplumber`, `pymupdf`, `pandas`, `matplotlib`, `beautifulsoup4`, and `lxml`; verified imports and `tests/test_generate_site.py` pass.
- Added workflow tooling: `build_lecture_manifest.py`, `check_note_coverage.py`, and `render_pdf_qa.py`, plus `docs/NOTE_GENERATION_WORKFLOW.md`; smoke-tested manifest, coverage, visual QA, and source-only `check_quality.sh .` behavior on CS336 lecture01/02.
- Extended workflow standards and `check_note_coverage.py` to require first-use explanations for dense systems terms including ZeRO, sharding, fused kernels, collectives, optimizer state, activation checkpointing, DRAM/SRAM/HBM, and perplexity; smoke test flags old CS336 lecture01 for these exact gaps.
- Completed CS336 2026 lecture01 and lecture02 new-workflow artifacts: manifests, coverage matrices, blueprints, PDF visual QA contact sheets, and checked QA reports.
- Regenerated CS336 2026 lecture03 under the new workflow as a 44-page slide-complete note with all 67 source slides included and 68 figures total; quality script reports `44p 11s 27b 68f ⭐⭐⭐`.
- Improved `render_pdf_qa.py` after lecture03 visual QA found near-blank pages from `pdftoppm`; the script now detects near-blank rendered pages and falls back/checks rendered output.
- Regenerated CS336 2026 lecture04 under the new source-first workflow as a 41-page slide-complete note with all 60 source slides included, attention/MoE glossary coverage, and read-the-figure explanations; quality script reports `41p 12s 42b 61f ⭐⭐⭐`, LaTeX log scan is clean, and visual QA contact sheet was reviewed.
- Regenerated CS336 2026 lecture05 under the new source-first workflow as a 38-page slide-complete GPU note with all 55 source slides included, 56 figures, 44 teaching boxes, and read-the-figure explanations; quality script reports `38p 8s 44b 56f ⭐⭐⭐`, LaTeX log scan is clean, and visual QA contact sheet was reviewed.
- Regenerated CS336 2026 lecture06 under the new source-first workflow as a 20-page source-node-complete kernels/Triton note with 8 figures, 36 teaching boxes, and detailed code walkthroughs for benchmarking, profiling, GeLU fusion, Triton GeLU, softmax, row-sum, and tiled matmul+ReLU; quality script reports `20p 15s 36b 8f ⭐⭐⭐`, LaTeX log scan is clean, and visual QA contact sheet was reviewed.
- Re-verified CS336 2026 lecture04 at the user's request before continuing serially: two XeLaTeX passes produced a 41-page PDF, `check_quality.sh` reports `41p ⭐⭐⭐`, `check_note_coverage.py` reports `figs=61 readfig=105 boxes=42 term_digest=3 formulas=2 code=0 summaries=10` with no hard errors, all 60 slide images are referenced, log scan is clean for hard LaTeX issues, and the refreshed PDF QA contact sheet/report were reviewed and marked complete.
- Regenerated CS336 2026 lecture07 under the new source-first workflow from the official executable lecture source: the note is now 26 pages with 15 figures, 18 read-the-figure explanations, 42 teaching boxes, 8 terminology-digestion hits, 7 formulas, and 7 code listings. Final verification reports `26p ⭐⭐⭐`; coverage has no hard errors; all local images are referenced; LaTeX log scan is clean; visual PDF QA contact sheet was reviewed and checked.
- Regenerated CS336 2026 lecture08 under the new source-first workflow from the 73-page official slide deck: the note is now slide-complete with all 73 slide images included, 53 pages, 74 figure inclusions, 59 read-the-figure/table/formula explanations, 76 teaching boxes, and explicit terminology digestion for collectives, sharding, ZeRO/FSDP, TP/SP/EP/CP, and pipeline concepts. Final verification reports `53p ⭐⭐⭐`, coverage has no hard errors, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Regenerated CS336 2026 lecture09 under the new source-first workflow from the 57-page official slide deck: the note is now slide-complete with all 57 slide images included, 42 pages, 58 figure inclusions, 53 read-the-figure/formula/table explanations, 59 teaching boxes, 5 formulas, and 3 code listings. Final verification reports `42p ⭐⭐⭐`, coverage has no hard errors, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Regenerated CS336 2026 lecture10 under the new source-first workflow from the official executable lecture source: the note is now source-node-complete with all local teaching PNGs included, 21 pages, 29 figure inclusions, 23 read-the-figure explanations, 34 teaching boxes, 4 terminology-digestion hits, and formulas for arithmetic intensity/KV cache/speculative sampling. Final verification reports `21p ⭐⭐⭐`, coverage has no hard errors or warnings, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Downloaded newly available official CS336 2026 materials for lecture11-13 from the Stanford lectures repository: lecture11 PDF deck (58 pages), lecture12 executable source, and lecture13 executable source.
- Generated CS336 2026 lecture11 under the new source-first workflow from the 58-page official slide deck: the note is slide-complete with all 58 slide images included, 43 pages, 59 figure inclusions, 53 read-the-figure/formula explanations, 60 teaching boxes, and terminology digestion for WSD, muP, optimizer scaling, Muon, Chinchilla methods, and recent scaling recipes. Final verification reports `43p ⭐⭐⭐`, coverage has no hard errors, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Generated CS336 2026 lecture12 under the new source-first workflow from the official executable lecture source: localized all 42 referenced image assets, wrote a 29-page evaluation note with 44 figure inclusions, 25 read-the-figure explanations, 40 teaching boxes, and terminology digestion for evaluation design, perplexity, zero-shot, methods/models/agents, ELO/LLM judges, ecological validity, contamination, and benchmark quality. Final verification reports `29p ⭐⭐⭐`, coverage has no hard errors or warnings, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Generated CS336 2026 lecture13 under the new source-first workflow from the official executable lecture source: localized all 18 referenced image assets, wrote a 20-page Data I note with 19 figure inclusions, 13 read-the-figure explanations, 46 teaching boxes, and terminology digestion for crawlers, WARC/WET, robots.txt/ToS, copyright/fair use/licensing, Common Crawl, filtering, deduplication, model-based filtering, provenance, and data audit loops. Final verification reports `20p ⭐⭐⭐`, coverage has no hard errors or warnings, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.

## 2026-05-12 YouTube ttkd0t5qTD4
- Started user-requested YouTube note task for `ttkd0t5qTD4`.
- Loaded `youtube-render-pdf` and `planning-with-files` workflows.
- Verified local `yt-dlp`, `ffmpeg`, `xelatex`, and `pdfinfo` availability.
- Anonymous YouTube metadata/format extraction failed because YouTube requires sign-in/bot confirmation. Will try local browser-cookie based extraction next.

## 2026-05-12 YouTube auth work
- User asked to solve the repeated YouTube login challenge fundamentally before continuing note generation.
- Confirmed yt-dlp is current (`2026.03.17`) and configured only with `--js-runtimes node`.
- Confirmed no ordinary browser profiles exist for `--cookies-from-browser`; found cached Playwright Chromium, which can be used to create a reusable authenticated profile.

- Installed `bgutil-ytdlp-pot-provider==1.3.1`.
- Installed then corrected `curl_cffi` to `0.14.0`; `yt-dlp --list-impersonate-targets` now shows Chrome/Safari/Firefox targets via curl_cffi.
- Verified plugin loading: `yt-dlp` reports `PO Token Providers: bgutil:http-1.3.1`.
- Remaining auth issue at this point: local bgutil HTTP server is not yet running, so tokens cannot be generated.

- User completed Google device-code OAuth authorization. Token cache was saved successfully.
- Continuing diagnosis because extraction now fails at a post-auth YouTube API HTTP 400, not at the earlier sign-in challenge.

- Added `tools/scripts/youtube_auth_check.sh` and expanded `.gitignore` for YouTube cookie files.
- OAuth was authorized but proved insufficient for actual media formats on this host; cookie-based YouTube account auth is now the required next input.

- Authenticated YouTube format listing succeeded after adding `--remote-components ejs:github`; real audio/video formats became available.
- Downloaded and merged the original 4K video to `youtube/ttkd0t5qTD4/original.mkv`; downloaded subtitle SRT files, thumbnail, and info JSON.
- Moving to transcript cleaning, frame extraction, TeX writing, PDF compilation, and visual QA.

- Completed `ttkd0t5qTD4` note generation: wrote TeX, compiled PDF, ran quality, coverage, log scan, diff whitespace check, and visual PDF QA.

## 2026-05-12 Zhang Xiaojun YouTube batch
- Started batch request for all Zhang Xiaojun YouTube interviews.
- First action: enumerate channel videos and podcast playlists, then build a deduplicated generation queue.

- Created Zhang Xiaojun YouTube batch queue files under `youtube/zhangxiaojun/`. Next canonical interview target is episode 138 (`vG1RBqn1sG4`).

- Downloaded episode 138 work media (`vG1RBqn1sG4`) as 720p `source.mp4`; YouTube reported no subtitles for requested languages, so local transcription is required.

- Stopped CPU transcription path and began GPU root-cause validation for faster-whisper/CTranslate2.

- Fixed transcription workflow to use CTranslate2 CUDA via `tools/scripts/transcribe_faster_whisper.py`. Episode 138 large-v3 GPU transcription completed in about 756 seconds with 6416 segments.

- GPU transcription root fix verified: episode 138 transcript now exists as `transcript.zh.srt/txt/json` from faster-whisper large-v3 CUDA.

## 2026-05-13 Zhang Xiaojun serial generation
- User requested serial high-standard generation for the broad AI/internet queue, newest to oldest.
- Treat EP140 as completed via `youtube/ttkd0t5qTD4`. Starting EP139 `Xxz5uh0L1mE` next. EP138 source/transcript work is preserved but paused to respect newest-to-oldest ordering.

- Episode 139 media and GPU transcript completed: `source.mp4`, `transcript.zh.srt/txt/json`, and chapter transcript split are available under `youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/`.

- Completed EP139 Agent survey note: `youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/ep139-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage passes, visual QA checked).

- Applied feedback: fixed no-slides podcast visual policy. EP139 now uses cover + concept diagrams only; repeated speaker frames were removed. Updated podcast workflow and quality script so interview notes are not incentivized to add repeated speaker frames for figure quota.

- Continuing serial Zhang Xiaojun generation with EP138 Luo Fuli (`vG1RBqn1sG4`), using existing source media and faster-whisper large-v3 CUDA transcript.

- Completed EP138 Luo Fuli note: `youtube/zhangxiaojun/ep138-vG1RBqn1sG4/ep138-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage passes, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP137 Hong Letong (`bv8ghyTFF9w`).

## 2026-05-13 CS336 workflow audit after user quality feedback
- User reported that CS336 notes have many images but still lack enough detailed prose explanation and transitions between small sections.
- Audited the workflow and sample CS336 notes. New static metrics confirmed the issue: several figure-heavy notes have low prose-per-figure and weak subsection openers despite previously scoring `⭐⭐⭐`.
- Updated `check_note_coverage.py` to detect `figure-heavy-prose-thin`, `thin-local-figure-explanations`, and `weak-section-openers`.
- Updated `check_quality.sh` to display prose-per-figure and demote figure-heavy notes below the prose-density threshold.
- Updated `AGENTS.md`, `QUALITY.md`, `docs/NOTE_GENERATION_WORKFLOW.md`, and shared video-writing rules to require prose-led flow, section bridge paragraphs, pre-figure setup, post-figure synthesis, and narrative blueprint fields.
- Added `docs/CS336_WORKFLOW_AUDIT_2026-05-13.md` with root cause, evidence, and follow-up repair plan.
- Rewrote CS336 2026 lecture12 as the first prose-led/teacher-voice sample: expanded from 29p to 32p, improved prose-per-figure from 149 to 260, added 13 teacher-voice markers, strengthened transitions between evaluation families, and passed the stricter coverage checker with no warnings.

- EP137 Hong Letong source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready. Status set to paused-ready-transcript for next serial writing step.

- Completed EP137 Hong Letong note: `youtube/zhangxiaojun/ep137-bv8ghyTFF9w/ep137-notes.pdf` (21 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP136 Guangmi LLM quarterly report (`u1Lzp-7Ybn8`).

- EP136 Guangmi source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready for survey note writing.

- Completed EP136 Guangmi quarterly report note: `youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/ep136-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP135 Tristan/Natural Selection (`x8qdqWIVVTA`).

- EP135 Tristan/Natural Selection source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready.

- Completed EP135 Tristan/Natural Selection note: `youtube/zhangxiaojun/ep135-x8qdqWIVVTA/ep135-notes.pdf` (21 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP134 Xie Chen data survey (`owjTOT14bG0`).

- EP134 Xie Chen data survey source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready.

- Completed EP134 Xie Chen data survey note: `youtube/zhangxiaojun/ep134-owjTOT14bG0/ep134-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP133 Saining Xie marathon interview (`iiBY0fqpThI`).

- EP133 Saining Xie source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready. Status set to paused-ready-transcript for next serial writing step.

- Completed EP133 Saining Xie marathon interview note: `youtube/zhangxiaojun/ep133-iiBY0fqpThI/ep133-notes.pdf` (23 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=10 boxes=30 term_digest=4 summaries=15`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP132 Gao Jiyang / Xinghaitu (`n4_c_HsodPg`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is running.

- Completed EP132 Gao Jiyang / Xinghaitu note: `youtube/zhangxiaojun/ep132-n4_c_HsodPg/ep132-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=8 boxes=28 term_digest=5 summaries=14`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP130 Zhang Yueguang / Muyan Zhiyu (`ruVJ_5dObxs`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is running.

- Completed EP130 Zhang Yueguang / Muyan Zhiyu note: `youtube/zhangxiaojun/ep130-ruVJ_5dObxs/ep130-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=9 boxes=26 term_digest=3 summaries=15`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).

- Fixed Zhang Xiaojun concept-figure rendering style after user reported tofu-box glyphs in EP133: added `tools/scripts/render_zhangxiaojun_concept_figures.py`, switched generated diagrams to a Chinese+Latin-safe AR PL font, simplified diagrams to sparse teaching cards, regenerated 60 figures across EP130/132/133/134/135/136/137/138/139, recompiled those PDFs, re-rendered visual QA, and rechecked whitespace.

- Completed EP129 Zhang Peng / Zhipu note: `youtube/zhangxiaojun/ep129-9zSMTUUEfmU/ep129-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=10 boxes=27 term_digest=2 summaries=14`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP128 Manus / Ji Yichao Peak (`MW-ezf2RhVg`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is starting.

- Completed EP128 Manus / Ji Yichao Peak note: `youtube/zhangxiaojun/ep128-MW-ezf2RhVg/ep128-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=8 boxes=28 term_digest=3 summaries=13`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP127 LLM quarterly report cross-year conversation (`SG90aehV3vU`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is starting.

- Completed EP127 Guangmi cross-year LLM quarterly report note: `youtube/zhangxiaojun/ep127-SG90aehV3vU/ep127-notes.pdf` (26 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=11 boxes=30 term_digest=5 summaries=11`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP127 done; next AI/internet selected target is EP125 (`k82iFzvKFCQ`) because EP126 is excluded from the filtered queue.
- Fixed manifest workflow to scan `figures/` directories so generated podcast concept diagrams are recorded as local visual assets.

- Completed EP125 Freda / Altimeter note: `youtube/zhangxiaojun/ep125-k82iFzvKFCQ/ep125-notes.pdf` (28 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=12 boxes=33 term_digest=5 summaries=14`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP125 done; next AI/internet selected target is EP123 (`qZbzFZ2R_Nw`) because EP124 and EP126 are excluded from the filtered queue.

- Completed EP123 ONE2X / Wang Guan note: `youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/ep123-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=25 term_digest=4 summaries=12`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP123 done; next AI/internet selected target is EP121 (`2o281Zy5aZE`) because EP122 and EP124 are excluded from the filtered queue.

- Completed EP121 DeepMind Tan Jie robotics note: `youtube/zhangxiaojun/ep121-2o281Zy5aZE/ep121-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=27 term_digest=3 summaries=10`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP121 done; next AI/internet selected target is EP120 (`40qPt8R2uys`).

- Completed EP120 Xiaopeng / Liu Xianming Physical AI note: `youtube/zhangxiaojun/ep120-40qPt8R2uys/ep120-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=9 boxes=30 term_digest=2 summaries=11`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP120 done; next AI/internet selected target is EP119 (`858HR43pegk`).

- Completed EP119 Kimi Linear / MiniMax M2 architecture survey note: `youtube/zhangxiaojun/ep119-858HR43pegk/ep119-notes.pdf` (22 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=30 term_digest=2 summaries=12`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP119 done; next AI/internet selected target is EP118 (`RxXVq7-sJzM`).

- Continuing serial Zhang Xiaojun generation with EP118 Li Xiang second interview (`RxXVq7-sJzM`).

- Completed EP118 Li Xiang second interview note: `youtube/zhangxiaojun/ep118-RxXVq7-sJzM/ep118-notes.pdf` (22 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=11 boxes=36 term_digest=3 summaries=11`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP118 done; next AI/internet selected target is EP117 (`zrvnoYYPaWQ`).

- Continuing serial Zhang Xiaojun generation with EP117 open-source paper exploration survey (`zrvnoYYPaWQ`).

- Completed EP117 open-source paper exploration survey note: `youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/ep117-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=10 boxes=26 term_digest=3 summaries=7`, visual QA checked; YouTube static cover plus generated concept diagrams, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP117 done; next AI/internet selected target is EP116 (`khrOsS7YQn4`).

- Continuing serial Zhang Xiaojun generation with EP116 Wu Minghui 19-year history interview (`khrOsS7YQn4`).

- Completed EP116 Wu Minghui / Minglue enterprise AI note: `youtube/zhangxiaojun/ep116-khrOsS7YQn4/ep116-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=9 boxes=36 term_digest=3 summaries=7`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP116 done; next AI/internet selected target is EP115 (`gQgKkUsx5q0`).

- Continuing serial Zhang Xiaojun generation with EP115 OpenAI Yao Shunyu Agent interview (`gQgKkUsx5q0`).

- Completed EP115 OpenAI Yao Shunyu Agent research note: `youtube/zhangxiaojun/ep115-gQgKkUsx5q0/ep115-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=6 boxes=34 term_digest=4 summaries=8`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP115 done; next AI/internet selected target is EP113 (`ouG6jrkECrc`) because EP114 is excluded from the filtered AI/internet queue.

- Continuing serial Zhang Xiaojun generation with EP113 Yang Zhilin K2 / Agentic LLM interview (`ouG6jrkECrc`).

- Completed EP113 Yang Zhilin / Kimi K2 Agentic LLM note: `youtube/zhangxiaojun/ep113-ouG6jrkECrc/ep113-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=6 boxes=31 term_digest=4 summaries=7`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP113 done; next AI/internet selected target is EP112 (`6yExfoTuSWw`).

- Continuing serial Zhang Xiaojun generation with EP112 Guangmi LLM quarterly report (`6yExfoTuSWw`).

- Completed EP112 Guangmi LLM quarterly report note: `youtube/zhangxiaojun/ep112-6yExfoTuSWw/ep112-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=8 boxes=32 term_digest=1 summaries=10`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP112 done; next AI/internet selected target is EP111 (`JxEetUlV9RA`).

- Continuing serial Zhang Xiaojun generation with EP111 Li Yifan lidar entrepreneurship interview (`JxEetUlV9RA`).

- Completed EP111 Li Yifan / Hesai lidar entrepreneurship note: `youtube/zhangxiaojun/ep111-JxEetUlV9RA/ep111-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=11 boxes=33 term_digest=1 summaries=8`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP111 done; next AI/internet selected target is EP110 (`8dKBH4x0D9o`).

- Continuing serial Zhang Xiaojun generation with EP110 Kimi K2 report / ChatGPT Agent / Qwen3-Coder survey (`8dKBH4x0D9o`).

- Completed EP110 Kimi K2 / ChatGPT Agent / Qwen3-Coder technical report note: `youtube/zhangxiaojun/ep110-8dKBH4x0D9o/ep110-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=8 boxes=27 term_digest=3 summaries=9`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP110 done; next AI/internet selected target is Lovart video special (`biptonYq-ys`).

- Continuing serial Zhang Xiaojun generation with Lovart / Chen Mian video special (`biptonYq-ys`).

- Completed Lovart / Chen Mian video special note: `youtube/zhangxiaojun/special-biptonYq-ys/lovart-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=9 readfig=5 boxes=38 term_digest=2 summaries=10`, visual QA checked; cover/title-frame plus generated concept diagrams, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark `biptonYq-ys` done; next AI/internet selected target is EP109 (`pWY0HVUH8GA`).

- Completed EP109 Xie Chen / Guanglun embodied simulation and synthetic data note: `youtube/zhangxiaojun/ep109-pWY0HVUH8GA/ep109-notes.pdf` (24 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=13 boxes=33 term_digest=6 summaries=9`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP109 done; next AI/internet selected target is `Puptr04av5g` (Wang He embodied intelligence history/capital-chaos subtitle edition).

- EP106/Puptr04av5g transcription command correction: initial run used legacy --output-json/--output-srt flags; current tool requires --out-prefix. Re-running with --out-prefix.

- EP106/Puptr04av5g transcription issue: single full-video faster-whisper run stalled after writing partial output around 01:08 despite process remaining alive. Root cause likely one long/awkward decode chunk rather than CUDA failure. Switched plan to chapter-based audio chunks and merge outputs.

- EP106/Puptr04av5g transcription issue 2: per-chunk shell loop also stalled on 3-minute chunk01 during model initialization/decode. Next approach: load WhisperModel once in a custom batch script and transcribe all chapter WAV chunks in one process.

- EP106/Puptr04av5g GPU runtime anomaly: CUDA/CTranslate2 calls left unkillable processes even after SIGKILL, so switched to testing CPU int8 transcription for chapter chunks rather than continuing to use the broken CUDA path.

- EP106/Puptr04av5g CPU fallback: chunks 01--03 transcribed successfully; generated provisional chapter-transcripts.md with later chunks marked pending while CPU transcription continues.

- EP106/Puptr04av5g CPU fallback: chunks 01--04 transcribed successfully; chunk05 running. Updated chapter-transcripts.md with completed chunks and pending markers for the rest.

- EP106/Puptr04av5g CPU fallback: chunk05 completed; updated chapter-transcripts.md with chapters 01--05. Remaining chunks 06--11 still running/pending.

- EP106/Puptr04av5g CPU fallback transcription completed for all 11 chunks and merged into `transcript.zh.json/srt/txt`; preserved the earlier stalled GPU partial transcript as `.gpu-partial` files for diagnosis.

- Completed EP106/Puptr04av5g Wang He embodied intelligence subtitle edition note: `youtube/zhangxiaojun/ep106-Puptr04av5g/ep106-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=18 boxes=25 term_digest=3 summaries=9`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark `Puptr04av5g` done and original EP106 `9DnjiuN6Yg0` duplicate/covered by the subtitle edition.

- Continuing serial Zhang Xiaojun generation with nuclear-fusion interview `pVuE4J5cn98`; metadata and 360p work video downloaded. YouTube exposes no subtitles despite title marker `含字幕`; using fixed-duration CPU transcription chunks because CUDA cleanup was unreliable in the previous item.

- Completed nuclear-fusion interview note `pVuE4J5cn98`: `youtube/zhangxiaojun/special-pVuE4J5cn98/fusion-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check clean with `figs=10 readfig=12 boxes=33 term_digest=3 summaries=9`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark `pVuE4J5cn98` done; next AI/internet selected target will be discovered from queue.

- Continuing serial Zhang Xiaojun generation with EP104 Rokid / Zhu Mingming (`qW-kgogQwJc`); metadata and 360p work video downloaded. YouTube exposes no subtitles; chapter-based CPU transcription is starting.

- EP104 CPU fallback transcription completed for all 20 fixed-duration chunks and was merged into `transcript.zh.json/srt/txt` plus `chapter-transcripts.md`.
- Completed EP104 Rokid / Zhu Mingming note: `youtube/zhangxiaojun/ep104-qW-kgogQwJc/ep104-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=9 readfig=8 boxes=33 term_digest=5 teacher_voice=7 summaries=7`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP104 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Checked next AI/internet queue item EP103 (`Xo7TxXkNsoA`) and found it is a duplicate upload of the already completed Lovart / Chen Mian video special `biptonYq-ys`: same title family, same 1h45m interview, same opening transcript and main chapter content. EP103 was transcribed locally before the duplicate was confirmed; no second note was generated. Queues were updated to mark EP103 `duplicate`, covered by `youtube/zhangxiaojun/special-biptonYq-ys/lovart-notes.tex`.

- Completed EP102 Zhang Xiangyu multimodal research note: `youtube/zhangxiaojun/ep102-vWrYHvSRz0s/ep102-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=26 term_digest=6 teacher_voice=4 summaries=8`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP102 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Completed EP101 YouWare / Ming Chaoping Agent application entrepreneurship note: `youtube/zhangxiaojun/ep101-a04POJEknCY/ep101-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=14 boxes=33 term_digest=4 teacher_voice=4 summaries=9`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP101 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Completed EP100 Mercedes-Benz / Ola Källenius transformation note: `youtube/zhangxiaojun/ep100-9Yjws_rt378/ep100-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=9 readfig=8 boxes=27 term_digest=4 teacher_voice=4 summaries=6`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP100 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Checked next AI/internet queue item EP99 (`aoaSwGAJW6M`) and found it is covered by the already completed nuclear-fusion subtitle edition `pVuE4J5cn98`: same guest/topic/title family. No second note generated. Queues were updated to mark EP99 `duplicate`, covered by `youtube/zhangxiaojun/special-pVuE4J5cn98/fusion-notes.tex`.

- Started VLA paper-survey投屏版 `eiQFomOuCJs`: metadata, cover, 1080p work video, 34 chapter-aligned slide/frame candidates, and contact sheet were acquired under `youtube/zhangxiaojun/special-eiQFomOuCJs/`.
- VLA paper-survey CPU fallback transcription completed for all 22 fixed-duration chunks and was merged into `transcript.zh.json/srt/txt` plus `chapter-transcripts.md` (4215 segments). Next step is to write the slide/frame-backed VLA course note.
- Completed VLA paper-survey投屏版 `eiQFomOuCJs`: `youtube/zhangxiaojun/special-eiQFomOuCJs/vla-notes.pdf` (24 pages, quality `⭐⭐⭐`, coverage check clean with `figs=26 readfig=17 boxes=23 term_digest=1 teacher_voice=1 summaries=6`, visual QA checked; real投屏 frames used as visual spine).
- Updated Zhang Xiaojun queues to mark `eiQFomOuCJs` done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Checked next AI/internet queue item EP98 (`3jI6F3M2ocU`) and confirmed it is the same VLA paper-survey content as the completed投屏版 `eiQFomOuCJs`: same duration, upload date, 34 chapter titles/timestamps, and description storyline. Queues were updated to mark EP98 `duplicate`, covered by `youtube/zhangxiaojun/special-eiQFomOuCJs/vla-notes.tex`.
- Started EP97 `YshXmh_q_Q4` Q1 2025 large-model quarterly review: metadata, cover, description, and 360p work video downloaded; YouTube exposes no subtitles or auto captions. Audio was split into 16 fixed-duration chunks and CPU int8 transcription is in progress.
- Completed EP97 Q1 2025 large-model quarterly review note: `youtube/zhangxiaojun/ep97-YshXmh_q_Q4/ep97-notes.pdf` (26 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=43 term_digest=5 teacher_voice=8 summaries=12`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP97 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Started EP96 `qtugoE1xQZk` autonomous-driving interview: metadata, cover, and description downloaded. YouTube exposes no subtitles or auto captions; queue status set to `in_progress`.
- Completed EP96 Lang Xianpeng autonomous-driving technical interview note: `youtube/zhangxiaojun/ep96-qtugoE1xQZk/ep96-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=30 term_digest=7 teacher_voice=7 summaries=7`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP96 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Started EP95 `VdWEE6vOYRw` Manus founder Xiao Hong interview: metadata, cover, and description downloaded. It is distinct from EP128 Peak/Manus final interview; YouTube exposes no subtitles or auto captions; queue status set to `in_progress`.
- Completed EP95 Manus founder Xiao Hong interview note: `youtube/zhangxiaojun/ep95-VdWEE6vOYRw/ep95-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=10 boxes=33 term_digest=4 teacher_voice=6 summaries=8`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP95 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Completed and accepted CS25 Lecture 02: 46 pages, 45 recovered teaching slides, 56 teaching boxes, strict coverage clean, `⭐⭐⭐`, double-pass XeLaTeX with no layout warnings, and signed canonical PDF QA.
- Updated CS25 V1--V5 tracking to 2/41; Lecture 03 Vision Transformers is now the active rewrite target.
- Prepared CS25 Lecture 03 source-first rewrite: verified official Stanford video `BP5CM0YxbP8` and V1 playlist, recovered and persisted 36 distinct teaching slides, added sanitized metadata, source index, blueprint, coverage matrix, teacher-voice ledger, and a manifest with 36 required visual nodes plus 12 spoken-explanation nodes.
- The legacy Lecture 03 note currently fails strict coverage (`3` figures, `0` read-figure explanations, all `36` required visual nodes missing); it will be replaced wholesale rather than incrementally patched.
- Replaced and accepted CS25 Lecture 03 as a 40-page source-first Vision Transformers note with 36 original teaching slides, 48 boxes, VTAB/BiT/ViT/Scaling ViT/MLP-Mixer coverage, strict zero-warning coverage, `⭐⭐⭐`, clean two-pass XeLaTeX, and signed canonical PDF QA.
- Updated CS25 V1--V5 tracking to 3/41; Lecture 04 is now the next rewrite target.
- Audited CS25 Lecture 04 against official Stanford Online video `w4Bw8WYL8Ps`, the V1 course page, manual `en-US` captions, Decision Transformer/CQL/D4RL primary sources, and latest `wdkns/wdkns-skills` HEAD `39f1a04`. Recovered 24 final teaching-slide states from the local 1080p recording and documented the visible title-slide date conflict.
- Replaced the legacy Lecture 04 note with a 34-page source-first Decision Transformer note: 24 figures, 40 teaching boxes, 10 teacher-voice markers, 15 formula blocks, 2 captioned code listings and 18,579 prose characters. Strict coverage is clean, quality is `⭐⭐⭐`, cross-references stabilize after three XeLaTeX passes, and canonical PDF visual QA is signed.
- Updated CS25 V1--V5 tracking to 4/41; Lecture 05 Mixture of Experts / Switch Transformer is now the active rewrite target.
- Audited CS25 Lecture 05 against official Stanford Online video `U8J32Z3qV8s`, official manual `en-US` captions, the V1 course page, and primary Switch Transformer / GShard / T5 / mT5 / V-MoE sources. Recovered and reviewed 38 complete teaching-slide states from the local 1080p recording, with redundant builds and repeated Q\&A navigation documented as intentional omissions.
- Replaced and accepted CS25 Lecture 05 as a 43-page source-first Switch Transformer note with 38 original teaching slides, 42 teaching boxes, 15 teacher-voice markers, 9 formula blocks, 2 captioned listings, and 16,621 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐`, two-pass XeLaTeX is clean apart from existing Fandol/underfull warnings, and canonical visual QA is signed.
- Updated CS25 V1--V5 tracking to 5/41; Lecture 06 Perceiver and Perceiver IO (`GV8-6ZgJVRk`) is the next source-first rewrite target.
- Resolved CS25 Lecture 06 source drift: historical Stanford Online ID `GV8-6ZgJVRk` is unavailable, while the current official replacement is `wTZ3o36lXoQ` (58:58, published 2022-07-15). Replaced the old 3,553-cue repeated subtitle track with 1,399 parsed official manual `en-US` captions and downloaded the current 1080p work video/thumbnail.
- Recovered and reviewed 39 complete teaching slides from 92 scene-difference candidates, including two distinct optical-flow qualitative examples while omitting repeated Q\&A navigation and intermediate video frames.
- Replaced and accepted CS25 Lecture 06 as a 38-page source-first Perceiver / Perceiver IO note with 39 original teaching slides, 35 teaching boxes, 12 teacher-voice markers, 7 formula blocks, 2 captioned listings, and 13,835 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐`, two-pass XeLaTeX is clean apart from existing Fandol warnings, and canonical visual QA is signed.
- Updated CS25 V1--V5 tracking to 6/41; Lecture 07 is the next source-first rewrite target.
- Audited CS25 Lecture 07 against official Stanford Online video `zejXBg-2Vpk`, 1,476 parsed manual captions, the V1 course page, and the NPT / Transformer / BERT / set-modeling primary sources. A 2-second scene scan produced 73 candidates; manual review retained 28 final teaching states and documented duplicate builds, Q\&A revisits, blank transitions, and bumpers as intentional omissions.
- Replaced the legacy Lecture 07 note wholesale, removing unsupported AI-SRE, incident, governance, and drift-monitoring material. The accepted note teaches self-attention, multi-head attention, teacher forcing, causal masking, dataset-as-input, ABD/ABA, permutation equivariance, stochastic target/feature masking, tabular rank evidence, corruption, duplicate intervention, and scaling boundaries.
- Accepted CS25 Lecture 07 as a 37-page source-first Self-Attention / Non-Parametric Transformer note with 28 original teaching slides, 30 teaching boxes, 26 teacher-voice markers, 19 formula blocks, 2 captioned listings, and 17,406 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐`, stabilized two-pass XeLaTeX has no layout warnings, and canonical visual QA is signed after contact-sheet plus full-size page checks.
- Updated CS25 V1--V5 tracking to 7/41; Lecture 08 is now the next source-first rewrite target.
- Audited CS25 Lecture 08 against official Stanford Online video `pC4zRb_5noQ`, 1,557 parsed manual captions, the V1 course page, Transformer Circuits framework/induction-head primary sources, and the lecture/article/upload date boundary. Manual review retained 64 teaching states from 108 recovered candidates and omitted duplicate builds, blank transitions, bumpers, the end slate, and low-resolution intermediate Lexoscope states.
- Replaced and accepted Lecture 08 as a 55-page source-first Transformer Circuits / Induction Heads note with 64 original teaching slides, 24 teaching boxes, 21 teacher-voice markers, 19 formula blocks, 2 captioned listings, and 17,849 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 278 prose characters per figure, stabilized two-pass XeLaTeX has no layout/reference/hyperref warnings, and canonical visual QA is signed after contact-sheet plus full-size table, formula, composition, spectrum, ablation, and soft-induction checks.
- Updated CS25 V1--V5 tracking to 8/41; Lecture 09 is now the next source-first rewrite target.
- Audited CS25 Lecture 09 against official Stanford Online video `wvE2n8u3drA`, 981 official manual-caption cues, the V1 course schedule, and classroom-era primary papers for raw-audio generation, generative/contrastive representation learning, and Audio Transformers. Recovered 47 final teaching states and preserved the 2021 `2105.00335v1` result boundary instead of importing the later revision.
- Replaced and accepted Lecture 09 as a 46-page source-first audio Transformer note with 47 original teaching slides, 28 teaching boxes, 18 teacher-voice markers, 18 formula blocks, 2 captioned listings, and 16,960 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 360 prose characters per figure, stabilized two-pass XeLaTeX has no layout/reference/hyperref warnings, and canonical visual QA is signed after contact-sheet plus full-size formula, metric, hierarchy, result-table, filterbank, and summary checks.
- Updated CS25 V1--V5 tracking to 9/41; Lecture 10 is now the next source-first rewrite target.
- Began CS25 Lecture 10 source-first regeneration. Confirmed official Stanford Online video `CYaju6aCMoQ` (V2, 52:48, uploaded 2022-08-11), replaced the 15,755-line rolling subtitle dump with 1,122 parsed official manual captions, downloaded a local 1080p working video, and recovered 32 distinct teaching slides from 1,584 two-second samples after removing bumpers, duplicate builds, Q&A revisits, and the end slate.
- Verified the lecture against Hinton's 44-page GLOM paper (`arXiv:2102.12627`, one public 2021 version). The central boundary is that GLOM is an imaginary design system / research proposal, not an empirically validated trained architecture. Source index, teacher-voice ledger, blueprint, coverage matrix, and the full note rewrite remain in progress.
- Replaced and accepted CS25 Lecture 10 as a 41-page source-first GLOM note with 32 original teaching slides, 38 teaching boxes, 12 in-note teacher-voice markers synthesized from a 30-row ledger, 13 formula blocks, 2 captioned listings, and 20,710 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 647 prose characters per figure, stabilized two-pass XeLaTeX has no layout/reference/hyperref warnings, and canonical visual QA is signed after contact-sheet plus full-size mechanism, formula, code, table, and final-page checks.
- Updated CS25 V1--V5 tracking to 10/41; Lecture 11 is now the next source-first rewrite target.
- Audited CS25 Lecture 11 against Stanford Online `XfpMkf4rD6E`: taught 2023-01-10, uploaded 2023-05-19, 1:11:40, with 1,667 parsed official manual-caption intervals. The legacy note's 2023-02-23 upload date was incorrect.
- Recovered 61 distinct teaching slides from 2,150 two-second 1080p samples and 139 high-recall candidates. Added a primary-source index, 35-row teacher-voice ledger, 61-slide manifest, blueprint, and coverage matrix; removed unsupported RLHF governance, deployment, drift, prompt-review, and team-process material from the old draft.
- Replaced and accepted CS25 Lecture 11 as a 67-page source-first Karpathy introduction with 61 teaching slides, 34 teaching boxes, 11 in-note teacher-voice markers, 16 formula blocks, 4 captioned listings, and 21,389 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 350 prose characters per figure, two-pass XeLaTeX is clean, and canonical visual QA is signed after full contact-sheet and enlarged dense-page checks.
- Updated CS25 V1--V5 tracking to 11/41; Lecture 12 is now the next source-first rewrite target.
- Audited CS25 Lecture 12 against official Stanford Online replacement video `DJ1Yy6Aquug`, 1,264 manual-caption cues, the V2 course archive, and six pre-lecture primary papers. Recovered 17 distinct teaching slides and documented that the formal deck ends at 00:30:54 while the remaining half hour is an information-dense Q\&A.
- Replaced and accepted Lecture 12 as a 27-page source-first language-alignment note with all 17 teaching slides, 32 teaching boxes, a 35-row teacher-voice ledger, 10 formula blocks, 2 captioned listings, and 14,325 prose characters. The note removes post-lecture Superalignment/deployment material and restores the actual 2023 lecture chain from human intent and RLHF through scalable oversight, targeted perturbations, preference payload, tools, outer/inner alignment, and interpretability.
- Strict coverage is zero-warning, quality is `⭐⭐⭐` at 842 prose characters per figure, all slides are referenced exactly once, stabilized two-pass XeLaTeX is clean, and canonical visual QA is signed after fixing an orphaned definition line and a mostly empty final page.
- Updated CS25 V1--V5 tracking to 12/41; Lecture 13 is now the next source-first rewrite target.
- Audited CS25 Lecture 13 against official Stanford Online video `tVtOevLrt5U`, the V2 archive, 1,439 manual-caption cues, Jason Wei's 37-page official deck, and eight classroom-date-compatible primary papers. Extracted two clean Playground frames showing the no-CoT wrong answer 33 and CoT derivation of 9.
- Replaced and accepted Lecture 13 as a 42-page source-first emergence and chain-of-thought note with all 36 teaching slides, 2 live-demo figures, 43 teaching boxes, a 43-node teacher-voice manifest, 13 in-note teacher markers, 8 formula blocks, 2 captioned listings, and 20,281 prose characters.
- Strict coverage is zero-warning, quality is `⭐⭐⭐` at 533 prose characters per figure, two-pass XeLaTeX is clean apart from repository-wide Fandol glyph notices, and canonical PDF QA is signed after correcting the official slide 22/23 mapping and rerendering all 42 pages.
- Updated CS25 V1--V5 tracking to 13/41; Lecture 14 is now the next source-first rewrite target.
- Completed CS25 Lecture 14 source-first rewrite and acceptance: official manual subtitles, 42 manually recovered teaching slides, source index, manifest, blueprint, coverage matrix, and teacher-voice ledger are in place.
- Final Lecture 14 artifact is 44 pages with 42 figures, 31 teaching boxes, 13 teacher-voice markers, 6 formulas, 2 captioned listings, and 17,277 prose characters; strict coverage is warning-free and quality is `⭐⭐⭐` at 411 chars/figure.
- Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical PDF QA is signed after full contact-sheet and enlarged-page review.
- CS25 V1--V5 progress is 14/41; Lecture 15 is the next source-first rewrite target.
- Completed and accepted CS25 Lecture 15 against Stanford Online `ct4tdyyNDY4`, official manual captions, 45 recovered teaching states, and five classroom-date-compatible primary papers.
- Final Lecture 15 artifact is 48 pages with 45 full-width figures, 29 teaching boxes, 12 teacher-voice markers, 6 formula blocks, 2 captioned listings, and 18,626 prose characters; strict coverage is warning-free and quality is `⭐⭐⭐` at 413 chars/figure.
- Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical QA is signed after full contact-sheet review, enlarged critical-page inspection, TOC compaction, table-width repair, and replacement of all cropped slide assets with full `1920x1080` frames.
- CS25 V1--V5 progress is 15/41; Lecture 16 is the next source-first rewrite target.
- Completed and accepted CS25 Lecture 16 against Stanford Online `sTQaJyrI-zg`, the official manual captions, 56 recovered teaching states, the V2 course archive, and the five primary papers used by the lecture.
- Final Lecture 16 artifact is 50 pages with 56 full-width figures, 18 teaching boxes, 9 teacher-voice markers, 9 formula blocks, 3 captioned listings, and 20,134 prose characters; strict coverage is warning-free and quality is `⭐⭐⭐` at 359 chars/figure.
- Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical QA is signed after full contact-sheet review and enlarged critical-page inspection.
- CS25 V1--V5 progress is 16/41; Lecture 17 is the next source-first rewrite target.
- Completed and accepted CS25 Lecture 17 against Stanford Online `nz7_wg5iOlA`, official manual captions, 84 manually recovered full-width teaching states, the V2 course archive, and the Med-PaLM, Performer, ProtNLM, DeepConsensus, and Enformer primary sources.
- Replaced the unsupported legacy draft with a 68-page source-first Biomedical Transformers note covering the true 2023 lecture chain from biomedical sequence representations and MultiMedQA through clinical human evaluation, efficient protein attention, protein annotation, sequencing correction, regulatory genomics, and foundation biomedical AI.
- Final Lecture 17 artifact has 84 figures, 38 teaching boxes, 14 teacher-voice markers, 10 formula blocks, 3 captioned listings, and 21,962 prose characters; strict coverage is warning-free and quality is `⭐⭐⭐` at 261 chars/figure.
- Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical QA is signed after full contact-sheet review and enlarged critical-page inspection.
- Corrected CS25 Lecture 18 to the official Stanford Online recording `L4DC7e6g2iI` (classroom date 2023-03-07), replacing an unrelated 2025 PhD-defense link and removing unsupported production/MoE/governance material from the legacy draft.
- Completed the source-first two-speaker note for Trenton Bricken's Attention/SDM talk and Will Dorrell's cognitive-map/TEM talk: 61 pages, 66 recovered teaching states, 26 teaching boxes, 11 teacher-voice markers, 17 formula blocks, 3 captioned listings, and 17,886 prose characters.
- All 66 required visuals are referenced exactly once; strict coverage is warning-free, quality is `⭐⭐⭐` at 271 chars/figure, and stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices.
- Canonical 61-page PDF QA is signed after full contact-sheet review and enlarged inspection of formulas, tables, code, handwritten derivations, synthesis, and references. CS25 V1--V5 progress is now 18/41; Lecture 19 is next.
- Completed and accepted CS25 Lecture 19 against the official Stanford Online video `fz8wf9hN20c`, official manual captions, 55 manually selected teaching states, and the PaLM-E, RT-1, RT-2, RT-X, Language Table, and Language-to-Rewards primary sources.
- Replaced the one-figure legacy summary with a 48-page source-first note covering physical-world failure cases, simulation and Moravec's paradox, data/interface bottlenecks, PaLM-E model consolidation, RT-2 action tokens and co-fine-tuning, RT-X transfer, reward-program interfaces, MPC, sim-to-real, Q&A tradeoffs, and physical safety.
- Final Lecture 19 artifact has 55 figures, 28 teaching boxes, 11 teacher-voice markers, 8 formula blocks, 3 captioned listings, and 18,174 prose characters; strict coverage is warning-free and quality is `⭐⭐⭐` at 330 chars/figure.
- Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical QA is signed after full contact-sheet and enlarged critical-page inspection. CS25 V1--V5 progress is now 19/41; Lecture 20 is next.
- Completed and accepted CS25 Lecture 20 against Stanford Online `wwQ1LQA3RCU`, official manual captions, 61 manually selected teaching states, and the MineDojo, Voyager, Eureka, VIMA, VPT, RT-2, and RoboCat primary sources.
- Replaced the one-figure legacy summary with a 54-page source-first Generalist Agents note covering active versus passive experience, the generalist-agent recipe, MineDojo/MineCLIP, Voyager code/memory/curriculum, Eureka reward reflection, three internet-video learning routes, multimodal prompting, VIMA, RT-2, RoboCat, and the human-level Minecraft challenge.
- Final Lecture 20 artifact has 61 figures, 38 teaching boxes, 18 teacher-voice markers, 9 formula blocks, 3 captioned listings, and 23,915 prose characters; strict coverage is warning-free and quality is `⭐⭐⭐` at 392 chars/figure.
- Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical 54-page QA is signed after full contact-sheet and enlarged critical-page inspection, including TOC and references compaction. CS25 V1--V5 progress is now 20/41; Lecture 21 is next.

## CS25 Lecture 21 completion
- Verified the official Stanford CS25 V3 entry and Stanford Online video `1GbDTTK3aR4` for Ashish Vaswani's 2023-11-07 lecture, using the official manual `en-US` captions and a November 2023 evidence boundary. No public standalone deck was found, so 1,613 three-second samples were audited and deduplicated to 43 distinct full-width teaching states.
- Replaced the thin legacy summary and fabricated 2026 date/source URL with a source-first 48-page note covering consolidation history, RNN/convolution/attention tradeoffs, scaled dot-product and multi-head attention, position representations, Music Transformer, long context, FLOPs versus memory hierarchy, MQA/GQA, online softmax, tool use, product loops, research directions, and Q\&A.
- Accepted 43/43 required figures referenced exactly once, 50 teaching boxes, 22 teacher-voice markers, 15 displayed formula blocks, 3 captioned listings, and 25,143 prose characters. Strict coverage is warning-free and quality is `⭐⭐⭐` at 584 prose characters per figure.
- Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical 48-page QA is signed after complete contact-sheet and enlarged critical-page inspection. CS25 V1--V5 progress is now 21/41; Lecture 22 is next.

## CS25 Lecture 22 completion
- Verified the Stanford CS25 V3 October 31, 2023 entry and official Stanford Online video `mcep6W8oB1I` with 1,431 parsed manual-caption cues. The speaker site exposed two deck variants; video-frame comparison at 00:26:30--00:26:40 proved the 71-page `transformers_united.pdf` is the final classroom deck because it includes the shown Zephyr/distillation pages omitted from the 67-page variant.
- Replaced the thin legacy note and unsupported fixed-recipe framing with a 60-page source-first treatment of SFT and preference-data distributions, Surge collection, iterative vendor endpoints, Zephyr alignment distillation, training/evaluation graphs, human Elo/AlpacaEval/Arena/MT-Bench, RM/red-team gaps, metric reversals, and GPT-4 judge bias.
- Accepted all 66 required teaching slides exactly once, with five pure divider/closing pages intentionally optional, 72 teaching boxes, 23 teacher-voice markers, 6 displayed formula blocks, 3 captioned listings, and 22,805 prose characters. Strict coverage is warning-free and quality is `⭐⭐⭐` at 345 prose characters per figure.
- Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond standard Fandol notices. Canonical 60-page QA is signed after full contact-sheet and enlarged critical-page inspection; an orphan final reminder page was removed before acceptance. CS25 V1--V5 progress is now 22/41; Lecture 23 is next.

## CS25 Lecture 23 completion
- Verified the official Stanford CS25 V3 November 14, 2023 entry, Stanford Online `ckNMsUuLryM`, the 52:28 1080p recording, and 1,210 parsed manual-caption cues. The legacy note contained unsupported Padlet, dashboard, priority-formula, governance-cadence, and deployment claims that were removed rather than preserved.
- No public standalone classroom deck was found. Three-second sampling produced 1,049 frames and 133 high-recall change candidates; contact-sheet review retained 39 distinct teaching states after removing repeated progressive builds, dividers, speaker-only Q&A frames, open-source repeats, and closing bumpers. The retained classroom region was cropped to remove the conferencing strip without redrawing content.
- Accepted `cs25/lecture23/lecture23-notes.pdf` at 48 pages with all 39 required teaching figures referenced exactly once, 70 teaching boxes, 19 in-note teacher-voice markers, 16 displayed formula blocks, 3 captioned listings, and 20,411 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 523 prose characters per figure. Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing the full 48-page contact sheet and enlarged NLLB-Seed, model challenge, MoE terminology, curriculum, relative-BLEU, toxicity, Q&A, and final synthesis pages. CS25 V1--V5 rewrite progress is now 23/41; Lecture 24 is next.

## CS25 Lecture 24 completion
- Verified Stanford Online `ylEk1TE1uBo`, the CS25 V3 November 28, 2023 classroom boundary, the 1:00:13 1080p recording, and 1,297 parsed manual-caption cues. The legacy note's prompt-dashboard, SLI/SLO, drift-monitoring, rollback, production-pipeline, observability, and generic deployment-checklist claims were unsupported and removed.
- No public standalone classroom deck was found. Three-second sampling produced 1,204 frames and 174 high-recall change candidates; manual review retained 64 distinct teaching states across emergence, Chain-of-Thought/ToT/Socratic/PAL/PoT, BabyLM, MultiOn demos, autonomy, Action API, memory, multi-agent communication, plan divergence, LLM OS, permissions, and sandboxing.
- Accepted `cs25/lecture24/lecture24-notes.pdf` at 65 pages with all 64 required teaching figures referenced exactly once, 79 teaching boxes, 25 in-note teacher-voice markers, 13 displayed formula blocks, 4 captioned listings, and 24,715 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 386 prose characters per figure. Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing the full 65-page contact sheet and enlarged Agent-stack, checkout, autonomy, Action API code, multi-agent, reliability, generalized-system, safety, and synthesis pages. A sparse trailing summary page was removed before acceptance. CS25 V1--V5 rewrite progress is now 24/41; Lecture 25 is next.

## CS25 Lecture 25 source audit and acceptance
- Verified Stanford Online `mE7IDf2SmJg`, the CS25 V3 December 5, 2023 classroom boundary, the 1:19:26 1080p recording, and 1,795 parsed official manual-caption cues. No public standalone classroom deck was found, so the visual spine was recovered from the official recording.
- Three-second sampling produced 1,589 frames and 77 high-recall candidates; manual review retained 49 distinct cropped teaching states. Repeated speaker windows, revisits, bumpers, and non-teaching transitions were omitted intentionally.
- Accepted `cs25/lecture25/lecture25-notes.pdf` at 56 pages with all 49 teaching figures referenced exactly once, 68 teaching boxes, 25 in-note teacher-voice markers, 17 displayed formula blocks, 3 captioned listings, and 23,845 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 486 prose characters per figure. Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing the full 56-page contact sheet and enlarged title/TOC, RAG equations, Frankenstein/FiD, Atlas objectives and result tables, Lost-in-the-Middle, multimodal RAG, RAG 2.0, and synthesis pages. CS25 V1--V5 rewrite progress is now 25/41; Lecture 26 is next.

## CS25 Lecture 26 source audit and acceptance
- Verified Stanford Online `fKMB5UlVY1E`, the official April 4, 2024 classroom date, April 23 upload, 1:17:28 1080p recording, and 1,795-cue official `en-US` manual subtitle track. The normalized transcript contains 891 timed lines and supports a 29-entry teacher-voice ledger.
- The official Google Slides deck linked in the video description exports to 114 pages. A fresh export on 2026-08-11 is byte-for-byte identical to local `slides.pdf` at SHA-256 `b16b112aa5b4b35a8b1ca221205e3bce24650a761609dc68b25edf2cb086091c`.
- Page review retained 91 teaching-bearing slides. Twenty-three pages are intentionally omitted: instructor/logistics material, pure dividers, the closing card, and four redundant intermediate communication-diagram builds whose distinct baseline, verification, conflict, and final correction states remain covered.
- The legacy note cited only 9/114 slides and invented prompt-calibration, dataset-drift, clinician-override, compliance-dashboard, incident-ticket, rollback, synthetic-replay, and regulator-checklist material. The replacement removes those unsupported claims and restores the actual Transformer/LLM/agent lecture.
- Accepted `cs25/lecture26/lecture26-notes.pdf` at 83 pages with all 91 required teaching figures referenced exactly once, 90 teaching boxes, 22 in-note teacher-voice markers, 28 displayed formula blocks, 3 captioned listings, and 25,357 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 278 prose characters per figure. Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after compressing a sparse third TOC page, reviewing the full 83-page contact sheet, and enlarging attention, emergence, DPO, Phi, reasoning, agent, autonomy, multi-agent, plan-divergence, LLM-OS, synthesis, and reference pages. CS25 V1--V5 rewrite progress is now 26/41; Lecture 27 is next.

## 2026-08-12 CS25 Lecture 27 completion

- Replaced the source-inaccurate legacy note for `3gb-ZkVRemQ` with a source-first dual-speaker lecture using Jason Wei's 20-page official deck, Hyung Won Chung's 67-page official deck, and the 1,551-cue official `en-US` manual-caption track.
- Verified the canonical classroom date (2024-04-11), upload date (2024-05-06), 1:17:07 runtime, speaker boundary, two official Google Slides exports, and SHA-256 provenance for both local PDFs.
- Classified all 87 pages: 66 required teaching pages and 21 intentional omissions limited to a contact card, divider, empty scaffold, or redundant progressive builds. Every required image appears exactly once and no optional page leaks into the note.
- Rewrote the lecture around Jason's data inspection / latent-task / scaling / emergence / U-shaped analysis and Hyung Won's dominant-force / Bitter Lesson / architecture transformation / inductive-bias lifecycle analysis, including the learning-objective and compute-trajectory Q&A extensions.
- Final acceptance: 61 pages, 66 figures, 36 teaching boxes, 24 teacher-voice markers, 20 formula blocks, 4 captioned listings, and 19,201 prose characters (290 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, two-pass XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, stranded headings, malformed boxes, or URL defects.
- CS25 V1--V5 rewrite progress is now 27/41. Lecture 28 is next.

## 2026-08-12 CS25 Lecture 28 source audit and acceptance

- Verified Stanford Online `AdLgPmcrXwQ`, “Stanford CS25: V4 I Aligning Open Language Models,” taught by Nathan Lambert on 2024-04-18 and uploaded on 2024-05-10. The 1:16:21 1080p recording provides a 1,693-cue official `en-US` manual-caption track.
- Detected and removed a severe source-contamination defect: the legacy `slides.pdf` was byte-identical to Lecture 27's Hyung Won Chung deck at SHA-256 `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`. It is replaced by Nathan Lambert's correct 77-page official Google Slides export at SHA-256 `3c3470dea235227cc43134b87106b8a913716b72bf8324edb8d0a34f79502268`.
- Classified the official deck into 67 required teaching pages and 10 intentional omissions limited to pure dividers, empty or superseded builds, one QR-only atlas state, and the closing contact card. Every required image appears exactly once; no optional page leaks into the note.
- Rewrote the lecture around open-model alignment history, base/IFT/SFT/RLHF/DPO distinctions, Alpaca/self-instruct, Vicuna/ShareGPT, OpenAssistant, LoRA/QLoRA/Guanaco, safety backlash, Arena/AlpacaEval/MT-Bench/Leaderboard, RLHF and reward modeling, DPO, Zephyr/Tulu 2/SteerLM/Starling, Llama 3, preference-data scarcity, and synthetic-data limits.
- Final acceptance: 57 pages, 67 figures, 30 teaching boxes, 30 teacher-voice markers, 14 formula blocks, 3 captioned listings, and 17,716 prose characters (264 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, two-pass XeLaTeX has no overfull/reference/rerun/hyperref warnings, and signed visual QA found no blank/cropped figures, overflow, orphan captions, stranded headings, malformed boxes, mostly empty trailing pages, or URL defects.
- CS25 V1--V5 rewrite progress is now 28/41. Lecture 29 is next.

## 2026-08-12 CS25 Lecture 29 source audit and acceptance

- Verified Stanford Online `RcJ1YXHLv5o`, “Stanford CS25: V4 I Demystifying Mixtral of Experts,” taught by Albert Jiang on 2024-04-25 and uploaded on 2024-05-16. The 1:04:31 official 1920x1080 recording provides a 2,830-cue automatic `en-orig` subtitle track, normalized into 276 readable timed segments.
- Detected and removed another severe source-contamination defect: the legacy 77-page `slides.pdf` and its rendered images were Nathan Lambert's Lecture 28 deck, byte-identical at SHA-256 `3c3470dea235227cc43134b87106b8a913716b72bf8324edb8d0a34f79502268`. No independent Mixtral deck is publicly linked, so the visual spine was rebuilt from the official recording.
- Audited 3,871 one-second samples and 58 high-recall visual-change candidates, then retained 26 required high-resolution teaching states. Seventeen omitted states are limited to bumpers, pure dividers, the closing card, and superseded progressive builds; Q\&A revisits add teacher voice but no new visual state.
- Rewrote the lecture around the Mistral 7B dense baseline, top-two routing, total/active/system cost accounting, Mixtral performance evidence, four architecture myths, load balance, compression/offload, routing interpretation, domain and token persistence experiments, community ablation, and the edge/cloud, batch, topology, RAG, expert-swapping, and gradient-flow Q\&A.
- Final acceptance: 38 pages, 26 figures, 37 teaching boxes, 31 teacher-voice markers, 26 formula blocks, 4 captioned listings, and 21,898 prose characters (842 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, two-pass XeLaTeX has no overfull/reference/rerun/hyperref warnings, and signed visual QA found no rendering or layout defects.
- CS25 V1--V5 rewrite progress is now 29/41. Lecture 30 is next.

## 2026-08-12 CS25 Lecture 30 source audit and acceptance

- Verified Stanford Online `zL9B3eXq0gY`, “Stanford CS25: V4 I Transformers that Transform Well Enough to Support Near-Shallow Architectures,” taught by Jake Williams on 2024-05-02 and uploaded on 2024-05-23. The 1:19:56 official 1920x1080 recording provides 1,487 manual `en-US` caption cues, normalized into 634 readable timed segments.
- Removed the contaminated legacy framing, including the fictitious 2026 course date, nonexistent Stanford lecture URL, `SAFU` misspelling, and unsupported governance/rollback material. With no public standalone deck, audited 4,796 one-second samples and recovered 27 independent teaching states from 3,409 slide-like frames and 68 high-recall candidates.
- Rewrote the lecture around standard attention versus SAFFU, deterministic bit-cipher embeddings, generalized co-occurrence and explicit softmax initialization, warm/freeze/thaw evidence, near-shallow computation, dynamic context and packing, frozen-embedding caching, PLM/BabyLM training, and the Le Potato edge pipeline with explicit evidence boundaries.
- Final acceptance: 38 pages, 27 figures, 44 teaching boxes, 34 teacher-voice markers, 28 formula blocks, 4 captioned listings, and 20,846 prose characters (772 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering or layout defects after enlarged review of the final self-test and references pages.
- CS25 V1--V5 rewrite progress is now 30/41. Lecture 31 is next.

## 2026-08-12 CS25 Lecture 31 source audit and acceptance

- Verified Stanford Online `cYfKQ6YG9Qo`, “Stanford CS25: V4 I From Large Language Models to Large Multimodal Models,” taught by Ming Ding of Zhipu AI on 2024-05-09 and uploaded on 2024-05-30. The 1:20:03 official 1920x1080 recording provides a manual `en-US` caption track normalized into 983 timestamped segments.
- Removed the legacy fictitious 2026-04-04 course date and unsupported monitoring, drift-detection, rollback, governance, fairness, privacy, and deployment checklists. With no public standalone deck, audited all 4,803 one-second samples, recovered 76 high-recall candidates, and selected 31 independent teaching states after excluding bumpers, pure dividers, transitions, duplicate shares, and changing frames inside one video demo.
- Rewrote the lecture around the BERT/GPT-3/ChatGPT moments, modern decoder recipe, ZeRO/Megatron/context parallelism, SFT/RLHF/DPO, data-algorithm-architecture equivalence, BLIP-2/LLaVA, CogVLM/CogAgent/Vary/GLM-4V, autoregressive image tokens, DDPM/Relay Diffusion/CogView3/DiT/MM-DiT, video scaling, dated research predictions, and Q\&A evidence limits.
- Final acceptance: 40 pages, 31 figures, 36 teaching boxes, 26 teacher-voice markers, 26 formula blocks, 5 captioned listings, and 20,701 prose characters (667 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering/layout defects or sparse trailing page.
- CS25 V1--V5 rewrite progress is now 31/41. Lecture 32 is next.

## 2026-08-12 CS25 Lecture 32 source audit and acceptance

- Verified Stanford Online `jm2hyJLFfN8`, “Stanford CS25: V4 I Behind the Scenes of LLM Pre-training: StarCoder Use Case,” taught by Loubna Ben Allal of Hugging Face on 2024-05-23 and uploaded on 2024-06-07. The 1:01:36 official 1920x1080 recording provides 1,259 manual `en-US` caption cues normalized into 1,230 timestamped segments; the speaker's official site links the 71-page Google Slides deck.
- Replaced the thumbnail-only legacy note, which had no canonical video URL and omitted the entire official deck. The source audit rendered all 71 pages, retained 58 required teaching slides, and documented 13 intentional omissions limited to pure dividers, intermediate animation builds, completion marks, one duplicate FineWeb page, and the closing slide.
- Rewrote the lecture around open-model transparency, Kaplan/Chinchilla and lifecycle-optimal scaling, Common Crawl/FineWeb, The Stack v1/v2 and Software Heritage, synthetic data, filter ablations, MinHash/LSH near-deduplication, PII and decontamination, metadata/FIM/mixture design, BigCode governance, responsible release, pass@k and membership testing, HumanEval contamination, LiveCodeBench, and the domain/tokenizer/dataset-governance Q\&A.
- Final acceptance: 55 pages, 58 figures, 43 teaching boxes, 27 teacher-voice markers, 13 formula blocks, 5 captioned listings, and 22,475 prose characters (387 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no layout/reference/rerun warnings beyond standard Fandol notices, and signed visual QA found no rendering, readability, overflow, or sparse-page defects.
- CS25 V1--V5 rewrite progress is now 32/41. Lecture 33 is next.

## 2026-08-12 CS25 Lecture 33 source audit and acceptance

- Verified official playlist item 33, Stanford Online `orDKvo8h71o`, “Stanford CS25: V4 I Hyung Won Chung of OpenAI,” recorded on 2024-04-11 and uploaded on 2024-06-11. The standalone 36:30 1920x1080 edit provides 376 manual `en-US` captions and links Hyung Won Chung's 67-page `Shaping the Future of AI from the History of Transformer` deck.
- Established the exact relationship to Lecture 27: Lecture 33 is the official standalone edit of the Hyung Won Chung half of combined upload `3gb-ZkVRemQ`; its deck is byte-identical to `cs25/lecture27/hyung-slides.pdf` at SHA-256 `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`. The standalone ends before the combined video's joint Q\&A, so Q\&A-only MLE/RLHF and compute-limit claims were explicitly excluded.
- Replaced the 11 KB legacy summary with a source-complete lecture on dominant-force modeling, compute per dollar, the Bitter Lesson, inductive-bias lifecycle, three Transformer families, the four-step encoder-decoder-to-decoder-only transformation, translation and FLAN natural experiments, representation hierarchy, bidirectionality, and KV-cache reuse.
- Final acceptance: 41 pages, 47 required official figures, 23 teaching boxes, 16 teacher-voice markers, 11 formula blocks, 3 captioned listings, and 12,585 prose characters (267 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering, overflow, readability, or sparse-tail defects.
- CS25 V1--V5 rewrite progress is now 33/41. Lecture 34 is next.

## 2026-08-12 CS25 Lecture 34 source audit and acceptance

- Verified official playlist item 34, Stanford Online `JKbtWimlzAE`, “Stanford CS25: V5 I Overview of Transformers,” taught by Steven Feng, Karan Singh, Jenny Duan, and Chelsea Zou on April 1, 2025 and uploaded April 18. The 1:01:28 official 1920x1080 recording supplies 1,298 manual-caption cues normalized into 1,264 timed segments, and the official source provides a 123-page deck.
- Corrected the legacy note's missing canonical video URL, incorrect presenter names, zero-slide visual coverage, absent teacher voice, and major content gaps. The source audit retains 100 required teaching pages and classifies 23 biography, administration, divider, QR/contact, and closing pages as intentional omissions.
- Rewrote the lecture as a systems map spanning embeddings/QKV/attention, data quality and scheduling, TinyDialogues, two-phase pretraining, CoT/ToT/PoT and latent reasoning, RLHF/DPO/RLAIF/GRPO/KTO, agent refinement/ReAct/LATS, ViT/CLIP/VLM, fMRI tokenization and cross-attention, scaling limits, model editing, and continual learning.
- Final acceptance: 80 pages, all 100 required figures referenced exactly once, 42 teaching boxes, 25 teacher-voice markers, 22 formula blocks, 5 captioned listings, and 26,118 prose characters (261 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering, overflow, caption, box, URL, or sparse-tail defects.
- CS25 V1--V5 rewrite progress is now 34/41. Lecture 35 is next.

## 2026-08-12 CS25 Lecture 35 source audit and acceptance

- Verified official playlist item 35, Stanford Online `gLwiPrwUDJ8`, “RL as a Co-Design of Product and Research,” taught by Karina Nguyen on April 8, 2025 and uploaded April 29. The 1:12:10 official 1920x1080 recording provides 1,325 manual-caption cues normalized into 1,288 valid timed segments.
- No standalone deck is publicly linked. A full one-second audit of all 4,330 seconds produced 2,540 slide-like frames and 208 high-recall candidates; manual review retained 60 independent teaching states and classified 148 progressive, repeated, administrative, speaker-only, or superseded states as optional.
- Replaced the legacy zero-figure, zero-teacher-voice note and its duplicated 3,135-cue subtitle artifact. The new lecture connects product belief, interface evidence, behavior evals, refusal diagnosis, real-world RL environments, reward design, reward hacking, deployment evidence, and Q\&A into a seven-layer product/research co-design loop.
- Final acceptance: 56 pages, all 60 required figures referenced exactly once, 42 teaching boxes, 17 teacher-voice markers, 24 formula blocks, 6 captioned listings, and 20,268 prose characters (337 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering, readability, overflow, caption, box, URL, or sparse-page defects.
- CS25 V1--V5 rewrite progress is now 35/41. Lecture 36 is next.

## 2026-08-12 CS25 Lecture 36 source audit and acceptance

- Verified Stanford Online `nEHNwdrbfGA`, “The Advent of AGI, Div Garg,” taught on 2025-04-15 and uploaded on 2025-05-13. The 1:01:01 official 1920x1080 recording is the canonical visual source because no standalone public deck is linked; 1,365 manual-caption cues were normalized into 1,296 timed transcript segments.
- Replaced the legacy duplicated 3,161-cue subtitle track and thin visual treatment. The exhaustive no-brightness-gate audit scanned the slide-led portion through 00:46:09, classified 544 candidate states, retained 58 required teaching states, and preserves the remaining Q\&A through the teacher-voice ledger and prose.
- Rewrote the lecture around AGI product form factors, agent contracts, interface/action loops, autonomy levels, REAL Bench, AgentQ demos and failure recovery, MCTS/self-critique/process supervision, preference learning, neural compute and memory, personalization, multi-agent coordination, MCP/A2A, and deployment evidence boundaries.
- Final acceptance: 51 pages, 58 figures, 29 teaching boxes, 15 teacher-voice markers, 16 formula blocks, 5 captioned listings, and 15,174 prose characters (261 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering, crop, overflow, orphan, readability, or sparse-tail defects.
- CS25 V1--V5 rewrite progress is now 36/41. Missing Lecture 37 is next.

## 2026-08-12 CS25 Lecture 37 source audit and acceptance

- Added the previously missing official playlist lecture: Stanford Online `ebnX5Ur1hBk`, “Large Language Model Reasoning,” taught by Denny Zhou on 2025-04-29 and uploaded on 2025-05-21. The 1:06:07 official 1920x1080 recording supplies 1,089 manual-caption cues, and Zhou's official 49-page Stanford deck is the canonical visual source.
- Rendered and reviewed all 49 deck pages, retaining 48 independent teaching pages and omitting only the final closing card. A 132-frame full-recording audit sampled every 30 seconds and found no deck-external live demo, whiteboard, code screen, or other independent teaching visual.
- Wrote the missing lecture around the operational definition of reasoning, serial computation from intermediate tokens, CoT decoding, prompting/SFT limits, model-generated traces, RL finetuning, verifier design, output-length scaling, marginalization, self-consistency/USC, analogical and step-back reasoning, deep research, and the full Q\&A evidence boundary.
- Final acceptance: 45 pages, 48 figures, 21 teaching boxes, 19 teacher-voice markers, 16 formula blocks, 5 captioned listings, and 15,942 prose characters (332 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is clean beyond standard Fandol notices and one harmless table underfull, and signed visual QA found no rendering, crop, overflow, orphan, readability, or sparse-tail defects.
- CS25 V1--V5 rewrite progress is now 37/41. Lecture 38 is next; the local V1--V5 directory set is now complete at 41/41.

## 2026-08-12 CS25 Lecture 38 source audit and acceptance

- Verified Stanford Online `vRQs7qfIDaU`, “On the Biology of a Large Language Model,” taught by Joshua Batson of Anthropic on 2025-05-13 and uploaded on 2025-06-05. The official 1:12:32 1920x1080 recording supplies 1,581 manual `en-US` caption cues normalized into 1,527 valid timed segments; the CS25 schedule links Anthropic's interactive article rather than a standalone public deck.
- Replaced the six-page, one-figure legacy note and its 18,675-line rolling-caption dump. A complete one-second scan of all 4,352 seconds produced 357 high-recall candidates; manual review retained 62 independent teaching states and classified 295 bumper, speaker-only, repeated, progressive, transition, or live-browser micro-states as optional.
- Rewrote the lecture around the biology analogy, token-level forward passes, polysemantic neurons, sparse features, Cross-Layer Transcoders, reconstruction error, attribution graphs, original-model interventions, medical and multilingual representations, parallel addition, metacognitive unfaithfulness, IDK inhibition, hallucinations, jailbreak competition, rhyme planning, and motivated reasoning.
- Final acceptance: 48 pages, all 62 required figures referenced exactly once, 21 teaching boxes, 10 in-note teacher-voice markers synthesized from an 18-row ledger, 7 formula blocks, 4 captioned listings, and 16,178 prose characters (260 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is clean beyond standard Fandol notices, and signed visual QA found no rendering, overflow, readability, box, URL, or sparse-tail defects after eliminating an initial orphan page 49.
- CS25 V1--V5 rewrite progress is now 38/41. Lecture 39 is next.

## 2026-08-12 CS25 Lecture 39 source audit and acceptance

- Verified Stanford Online `8kXIaUM3h1E`, “Multimodal World Models for Drug Discovery,” taught by Eshed Margalit of Noetik.ai on 2025-05-20 and uploaded on 2025-06-13. The official recording is 4,262 seconds (1:11:02) at 1920x1080; the video description and CS25 schedule link no standalone public deck.
- Refreshed the manual `en-US` subtitle track: 1,643 raw SRT cues parse into 1,622 timed segments, replacing the legacy 3,771-cue / 18,855-line rolling-caption artifact. The official thumbnail and temporary 279 MB source video are retained outside the repository as audit inputs.
- Completed a no-brightness-gate one-second scan of all 4,262 seconds. It produced 441 high-recall candidates, all OCRed and arranged into 28 contact sheets plus a global overview; manual review retained 60 independent teaching states and classified 381 administrative, speaker-only, repeated, progressive, transition, or embedded-video micro-states as optional.
- Replaced the thin one-figure legacy note with a source-first lecture spanning operational world models, translation versus disambiguation, contrastive/direct/cross-attention/token/AdaLN fusion, tumor immunology, aligned H\&E/protein/spatial-transcriptomic/genetic data, masked gene modeling, spatial-neighborhood conditioning, virtual cells, model counterfactuals, H\&E imputation, multimodal Transformers, biological feature interpretation, hierarchical bottlenecks, and the full Q\&A evidence boundary.
- Final acceptance: 51 pages, all 60 required figures referenced exactly once, 25 teaching boxes, 13 in-note teacher-voice markers synthesized from a 24-row ledger, 13 formula blocks, 4 captioned listings, and 17,532 prose characters (292 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is clean beyond standard Fandol notices and harmless terminology-table underfulls, and signed visual QA found no rendering, crop, overflow, orphan, URL, box, or sparse-tail defects after fixing an initial page-52 orphan and split Q\&A box.
- CS25 V1--V5 rewrite progress is now 39/41. Lecture 40 is next.

## 2026-08-12 CS25 Lecture 40 source audit and acceptance

- Verified Stanford Online `Y0H8D5ZKb5A`, “Diffusion Transformers,” taught by Sayak Paul on 2025-05-27. The canonical visual source is the speaker's official 66-page deck; the full 1:14:32 recording supplies the architecture, evaluation, parameter-sharing, and deployment Q\&A teacher voice.
- Replaced the legacy thin treatment with a source-complete lecture covering diffusion and Flow Matching, UNet/UViT/DiT transitions, patching and adaLN-Zero, PixArt-α, quadratic-attention cost, SANA, MMDiT/SD3, modality-specific projections, parameter sharing, structural controls, video generation, in-context generation, MoE, and open directions.
- Final acceptance: 49 pages, all 62 required deck pages referenced exactly once, 20 teaching boxes, 12 teacher-voice markers, 12 formula blocks, 4 captioned listings, and 17,316 prose characters (279 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no overfull boxes, and signed visual QA inspected the complete contact sheet plus the final terminology and reading pages.
- CS25 V1--V5 rewrite progress is now 40/41. Lecture 41 is next.

## 2026-08-12 CS25 Lecture 41 source audit and acceptance

- Verified Stanford Online `YGHF8_tf--g`, “Transformers for Video Generation,” taught by Andrew Brown of Meta GenAI on 2025-06-03 and uploaded on 2025-07-03. The official 1:13:35 recording and 1,504-cue manual captions are canonical because no public standalone deck is linked; the Movie Gen primary paper supplies formula and system-detail verification.
- Audited all 4,415 seconds at one-second resolution, reviewed 780 high-recall candidates, and retained 32 independent teaching/evidence states. The complete 00:54:10--01:13:20 Q\&A contributes required teacher voice even though it adds no independent visual state.
- Rewrote the lecture around temporal autoencoding, 8×8×8 compression and token accounting, Flow Matching and ODE inference, the randomly initialized Llama-style bidirectional backbone, three text encoders, cross-attention/AdaLN/MHA, 73K-token context parallelism, data filtering, progressive curriculum, editing, personalization, audio, Net Win Rate, scaling evidence, and open failure boundaries.
- Final acceptance: 37 pages, all 32 required figures referenced exactly once, 27 teaching boxes, 15 teacher-voice markers, 17 formula blocks, 3 captioned listings, and 15,067 prose characters (470 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no overfull boxes, and signed visual QA passed after replacing two mis-captured video states with the actual penguin-editing and personalization evidence frames.
- CS25 V1--V5 is complete at 41/41. The next active batch is the official 9-lecture CS25 V6 series.

## 2026-08-12 CS25 V6 Lecture 01 source audit and acceptance

- Re-verified the live CS25 V6 schedule and the official Stanford Online playlist: V6 contains nine public lectures. Local numbering follows classroom chronology; Lecture 01 is Stanford Online `bHSDPgZYie0`, “Overview of Transformers,” taught by Steven Feng and Karan Singh on 2026-04-02 and uploaded on 2026-04-22.
- Downloaded and hashed the official 156-page deck, 1,558-cue manual `en-US` captions, cover, and temporary 1080p recording. All deck pages were reviewed through ten contact sheets; 116 independent teaching pages are required and 40 administrative, divider, paper-title/QR, repeated, progressive, or closing pages are optional.
- Audited the complete 4,606-second recording at five-second resolution. Of 921 samples, 882 were slide-like and 194 stable high-recall candidates were reviewed; no independent deck-external teaching visual was found, so the official deck is the visual spine and spoken material is preserved through a 32-row teacher-voice ledger.
- Final acceptance: 90 pages, all 116 required figures referenced exactly once, 42 teaching boxes, 32 teacher-voice markers, 30 formula blocks, 6 captioned listings, and 30,192 prose characters (260 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no overfull boxes, and signed visual QA inspected all 90 pages in six enlarged segments plus full-size dense table and closing pages.
- CS25 V6 progress is now 1/9. Lecture 02, `From Representation Learning to World Modeling through Joint Embedding Predictive Architectures`, is next.

## 2026-08-12 CS25 V6 Lecture 02 source audit and acceptance

- Verified Stanford Online `GBd7iuJkW08`, “From Representation Learning to World Modeling,” taught by Heejeong “Hazel” Nam and Lucas Maes on 2026-04-09 and uploaded on 2026-04-22. The official 55-page deck and 1,371-cue manual `en-US` captions are canonical; Causal-JEPA v1 and LeWorldModel v1 preserve the lecture-date paper snapshot.
- Rendered and reviewed all 55 deck pages, retaining 47 required teaching pages. The complete 4,263-second recording was sampled every five seconds; 853 samples and 198 high-recall candidates revealed one required deck-external question card at 00:31:25 on object-representation fidelity and causal-graph recovery.
- Rewrote the lecture around controlled state transition, latent prediction and energy, object-centric slots, permutation-aware identity anchoring, object-history masking, action-node conditioning, counterfactual reasoning, planning efficiency, physical plausibility, predictive-sufficiency assumptions, SIGReg anti-collapse, latent MPC, physical probes, surprise, open-loop error, limitations, reproducibility tooling, and substantive physical-AI/agent/hallucination Q\&A.
- Final acceptance: 51 pages, all 48 required figures referenced exactly once, 35 teaching boxes, 27 teacher-voice markers, 19 formula blocks, 4 captioned listings, and 22,603 prose characters (470 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX is free of overfull and underfull boxes, and signed visual QA inspected all 51 pages in five enlarged segments plus full-size dense table, Q\&A, corrected question-card, and closing pages.
- CS25 V6 progress is now 2/9. Lecture 03, `SSM vs Transformers`, is next.
## 2026-08-12 — CS25 V6 Lecture 03 started

- Closed Lecture 02 after strict coverage, `⭐⭐⭐`, stable double XeLaTeX, and signed 51-page visual QA.
- Confirmed the active goal and moved the execution plan to Lecture 03.
- Re-verified upstream `wdkns-skills` HEAD and the official Stanford/YouTube metadata for Albert Gu's 2026-04-16 SSM-versus-Transformer seminar.
- Confirmed that the official course page provides no deck link, so Lecture 03 will use recording-derived slide reconstruction with official article/paper supplementation.
- Downloaded the 1920x1080 official recording to a private `/tmp` workspace, preserved the public cover and LF-normalized English original automatic captions, and generated deterministic timed/clean/chunked transcript derivatives.
- Hashed the private recording and public caption/cover artifacts into sanitized `metadata.json`; no raw `yt-dlp` metadata or video was added to the repository.
- Sampled the full Albert Gu segment every two seconds and completed an initial high-recall direct/projector/camera classification. The remaining visual task is to resolve camera-only slide states before freezing the selection manifest.

## 2026-08-12 — CS25 V6 Lecture 03 accepted

- Froze 33 recording-derived slide states after reviewing 1,999 two-second samples: 32 independent teaching states are required and the title card is optional because its metadata is preserved on the cover.
- Completed the 50-row teacher-voice ledger and rewrote the lecture around memory interfaces, KV-cache versus compressed state, modern SSM ingredients, hybrid models, token resolution, raw-data modeling, H-Net dynamic chunking, scaling evidence, and the final SSM/attention tradeoff.
- Final acceptance: 40 pages, 32 required figures exactly once, 34 teaching boxes, 16 teacher-voice markers, 13 formula blocks, 5 captioned listings, and 21,059 prose characters (about 658 per figure).
- Strict coverage has zero hard errors or warnings, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull or underfull boxes, and the 40-page visual QA is signed after contact-sheet and full-size focused review.
- Recomputed the selection, slide-tree, and teacher-voice hashes; all already match sanitized `metadata.json`. README/tracking totals now reflect 362 source notes, 163 Stanford notes, and CS25 V6 progress 3/9.
- Lecture 04, `The Ultra-Scale Talk: Scaling Training to Thousands of GPUs`, is now the active target; `The Future of Pretraining` is Lecture 05 in classroom chronology.

## 2026-08-12 — CS25 V6 Lecture 04 accepted

- Verified the live course row, official video `I5BKi32IEa8`, manual captions, 106-page official deck, class/upload dates, runtime, resolution, and primary systems references.
- Rendered and reviewed all 106 deck pages, freezing 75 required teaching states and 31 intentional optional pages; the 742-frame five-second recording audit found no independent deck-external teaching visual.
- Rewrote the lecture around resource accounting, DP collectives and bucket overlap, ZeRO/FSDP state ownership, TP/SP algebra, PP schedules, CP/Ring Attention, EP all-to-all and hardware bottlenecks, five-dimensional composition, Q&A, and energy responsibility.
- Final acceptance: 56 pages, 75 required figures exactly once, 25 teaching boxes, 12 teacher-voice markers, 11 formula blocks, 4 captioned listings, and 19,514 prose characters (260 per figure).
- Strict coverage has zero warnings, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull or underfull boxes, and signed visual QA inspected the complete contact sheet plus full-size code, schedule, Ring Attention, EP, decision-table, infrastructure, energy, and closing pages.
- README/tracking totals now reflect 363 source notes, 164 Stanford notes, and CS25 V6 progress 4/9. Lecture 05 `The Future of Pretraining` is next; its duplicated course-page slide link must be resolved independently before use.

## 2026-08-12 — CS25 V6 Lecture 05 accepted

- Confirmed that the live course-page slide URL is erroneous: it repeats Lecture 04's 106-page Ultra-Scale deck. Lecture 05 therefore uses the official 1920x1080 recording and manual `en-US` captions as the canonical source.
- Completed the full 695-frame, 12-contact-sheet five-second visual audit and froze 44 recording-derived states: 41 required teaching visuals plus three optional title/divider cards.
- Verified the lecture-date paper snapshot for two-phase pretraining v1, front-loading reasoning v1, RLP v2, Quiet-STaR, RPT, and RLPT; built sanitized metadata, sources, transcript derivatives, selection, manifest, 49-row teacher-voice ledger, blueprint, and coverage matrix.
- Rewrote the lecture around data weighting and ordering, two-phase curriculum, durable early reasoning, RLP's thought/no-think counterfactual, dense information-gain rewards, EMA, fair compute comparison, early-reasoning literature, engineering reproduction, and Q&A limits.
- Final acceptance: 46 pages, 41 required figures exactly once, 35 teaching boxes, 10 teacher-voice markers, 11 formula blocks, 5 captioned listings, and 19,358 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐`, stable double XeLaTeX is free of overfull/underfull boxes, and visual QA is signed.
- README/tracking totals now reflect 364 source notes, 165 Stanford notes, and CS25 V6 progress 5/9. Lecture 06 `Distinct Modes of Generalization from Parameters and Context` is next.

## 2026-08-12 — CS25 V6 Lecture 06 accepted

- Verified the official Stanford Online recording `dJtHauhRasc`, manual `en-US` captions, 50-page official deck, class/upload dates, 1920×1080 source, and lecture-date versions of the controlled-generalization, latent-learning, test-time-compute, reversal-curse, and ICL-as-optimization primary papers.
- Completed a full 870-frame, 15-contact-sheet five-second recording audit. No independent deck-external teaching visual appears; 45 official teaching pages are required and five title/divider/closing pages are intentional optional nodes.
- Built sanitized metadata, deterministic transcript derivatives, source manifest, selection table, 33-row teacher-voice ledger, blueprint, coverage matrix, and a 47-page source-first lecture covering reversal, syllogism, codebooks, explicit versus latent information, in-context augmentation, oracle episodic retrieval, RL regeneration, compute tradeoffs, Q&A engineering constraints, and complementary memory systems.
- Final acceptance: 45 required figures exactly once, 32 teaching boxes, 14 teacher-voice markers, 12 formula blocks, 5 captioned listings, and 17,318 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull/underfull boxes, and visual QA is signed after complete contact-sheet and focused full-size review.
- README/tracking totals now reflect 365 source notes, 166 Stanford notes, and CS25 V6 progress 6/9. Lecture 07 `Advancing Science and Medicine with Collaborative AI Agents` is next.

## 2026-08-13 — CS25 V6 Lecture 07 accepted

- Verified Stanford Online recording `jFdH7n6BAl0`, manual `en-US` captions, 1920×1080 source, class/upload dates, and the absence of an independent official deck. The official description advertises both AI co-scientist and AMIE, but the actual recording covers only AI co-scientist before Q&A, so no AMIE material was reconstructed.
- Audited the full 01:06:32 recording at two-second resolution: 1,996 samples across 34 complete contact sheets. The frozen selection contains 23 required teaching states and three optional title/context cards; no independent whiteboard or live-demo visual was found.
- Built sanitized metadata, source manifest, selection table, 31-row teacher-voice ledger, blueprint, coverage matrix, and a 38-page source-first lecture covering scientific discovery as search, collaborative agents, tournament ranking, tool/memory architecture, verification bottlenecks, AMR, AML, liver fibrosis, plant assemblies, rejuvenation, Alzheimer mechanisms, inverse comorbidity, report triage, and layered safeguards.
- Froze evidence to the 2026-05-14 classroom boundary: AI co-scientist `2502.18864v1`, AMR bioRxiv `2025.02.19.639094v1`, liver fibrosis bioRxiv `2025.04.29.651320v1`, and plant assemblies bioRxiv `2026.05.03.722499v1`; later revisions and publications are explicitly excluded from lecture-time claims.
- Final acceptance: 23 required figures exactly once, 57 teaching boxes, 20 teacher-voice markers, 12 formula blocks, 6 captioned listings, and 19,991 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull/underfull boxes, and signed visual QA reviewed all 38 rendered pages.
- README/tracking totals now reflect 366 source notes, 167 Stanford notes, and CS25 V6 progress 7/9. Lecture 08 `From Language Models to Native Multimodal Intelligence` is next.

## 2026-08-13 — CS25 V6 Lecture 08 accepted

- Verified Stanford Online recording `NDdc39KYqDU`, manual `en-US` captions, the 56-page official Google Drive deck, 1920×1080 source, class/upload dates, and lecture-date versions of Chameleon, VQ-VAE-2, Transfusion, Mind the Gap, Mixture-of-Transformers, LMFusion, BAGEL, and π0.7.
- Completed a full 776-frame, 13-contact-sheet five-second recording audit. No deck-external whiteboard, demo, question card, or teaching diagram appears; the prepared talk ends at 00:41:39 and the remainder is camera-only Q&A over the conclusion slide.
- Froze 37 required teaching pages exactly once and 19 intentional optional pages. Progressive builds collapse to their complete states, while deck pages 53--55 on Interaction Models remain optional because the actual recording jumps from page 52 to page 56 without presenting them.
- Built sanitized metadata, source manifest, selection table, 38-row teacher-voice ledger, blueprint, coverage matrix, and a 45-page source-first lecture covering mixed-modal sequence interfaces, continuous versus discrete representations, text-only versus omni losses, Chameleon, Transfusion, modality-aware sparsity, MoT/MoE routing, BAGEL, π0.7, transfer asymmetry, physical-world intelligence, and Q&A engineering boundaries.
- Final acceptance: 37 required figures exactly once, 62 teaching boxes, 16 in-note teacher-voice markers, 17 formula blocks, 6 captioned listings, and 25,986 prose characters, or 702 prose characters per figure. Strict coverage is zero-warning, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull/underfull boxes, and signed visual QA reviewed all 45 pages plus dense full-size pages.
- README/tracking totals now reflect 367 source notes, 168 Stanford notes, and CS25 V6 progress 8/9. Lecture 09 `Serving Transformers: Lessons from the Trenches of Production Inference` is next.

## 2026-08-13 — CS25 V6 Lecture 09 accepted; course complete

- Acquired and hashed the official 73-page deck, 1920×1080/60 fps recording, `en-US` subtitles, and cover for Charles Frye's `Serving Transformers: Lessons from the Trenches of Production Inference`.
- Parsed 1,759 subtitle cues into 950 timed utterances and completed a full 990-frame, 17-contact-sheet five-second recording audit. One live token-timing demo is retained beyond the deck; no missing whiteboard or live-coding visual was found.
- Froze 57 required deck pages + 1 live frame and 16 optional title/divider/progressive/unpresented nodes. Deck pages 070, 072, and 073 remain explicitly optional rather than being invented as classroom content.
- Produced the complete source-first artifact set: sanitized metadata, source manifest, selection TSV, 38-row teacher-voice ledger, blueprint, coverage matrix, primary-source register, 73 rendered slide images, transcript derivatives, TeX, PDF, and signed QA report.
- Final note metrics: 59 pages, 71 teaching boxes, 12 formula blocks, 7 captioned listings, 23,900 checker prose characters, and 419 prose characters per deck figure. Strict coverage has zero warnings, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull/underfull/reference warnings, and full visual QA passes.
- CS25 V6 now stands at 9/9 and the complete batch totals 472 pages, 474 teaching figures, and 393 teaching boxes. Global tracking is updated to 368 source notes and 169 Stanford notes.
