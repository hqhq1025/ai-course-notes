# Findings

## Agentic AI MOOC Fall 2025 source audit

- 核验日期为 2026-08-18。`https://agenticai-learning.org/` 返回到 `/f25` 的 canonical redirect；官方当前页标题为 `Agentic AI MOOC, Fall 2025`，页面的 past-course 菜单只列 Fall 2024 与 Spring 2025。
- 官方 GitHub 仓库为 `rdi-berkeley/agentic-ai-mooc`，`main` 当前 HEAD 为 `75042c6c5bf59925abb91c83edbccc8475f93b2e`；GitHub 显示最近 push 为 2026-01-23，页面仓库最近更新时间为 2026-06-24。仓库中仍只有 `f24.md`、`sp25.md`、`f25.md`，没有 2026 课程页。
- Fall 2025 共有 12 场教学讲座：Sep 15, Sep 22, Sep 29, Oct 6, Oct 13, Oct 20, Oct 27, Nov 3, Nov 10, Nov 17, Dec 1, Dec 8。Nov 24 是 Thanksgiving 停课。
- 官方提供 slides 的讲座：Sep 15、Sep 22、Sep 29、Oct 6、Oct 13、Oct 20、Oct 27、Nov 10，共 8 讲。Nov 3、Nov 17、Dec 1、Dec 8 页面只列 recording，其中 Dec 8 的官方仓库另有 `slides/dawn-agentic-ai.pdf`，需核验是否与课堂录像一致后再决定是否纳入 required deck。
- 本地 `talks/berkeley-llm-agents/f25/lecture01--11` 是倒序映射：L01=Dec 8，L02=Dec 1，L03=Nov 17，L04=Nov 10，L05=Nov 3，L06=Oct 27，L07=Oct 20，L08=Oct 13，L09=Sep 29，L10=Sep 22，L11=Sep 15。
- 本地缺失 Oct 6 `Agent Evaluation & Project Overview`，官方录像 ID 为 `VfOA2a0dj4w`，官方 deck 为 `slides/LLM Agent Evaluations & Project Overview.pdf`。
- 11 份旧 TeX 每份约 31--44 KB，拥有 29--46 个 teaching box 和 5--11 张抽帧图，但没有生成 PDF，也没有 manifest、coverage、blueprint、teacher-voice ledger 或 canonical QA。它们可作为正文与字幕素材，不能按当前标准视为完成。
- 现有 11 份字幕体量充足，每讲约 1,739--5,743 cues；teacher voice 恢复具备良好基础。
- 已将本地目录迁移为官方课堂日期正序 `lecture01--12`；旧素材整体保留，未删除无关工作树内容。
- 9 份确认课堂 deck 已下载并渲染：L01 86 页、L02 37 页、L03 44 页、L04 104 页、L05 37 页、L06 51 页、L07 42 页、L09 40 页、L12 99 页。
- L12 的 `dawn-agentic-ai.pdf` 虽未在 F25 页面直接链接，但官方仓库中的标题、章节顺序、`LLM Safety vs. LLM Agent Safety` 页面和 Web Agent 注入案例均与课堂录像抽帧一致，故接受为 required classroom deck。
- deck SHA-256：L01 `f5dcc916c8391b14408ee67b60a65f8ebc8eceee7e2dca9622442899a1c84ad8`；L02 `69bee6c823d246fb97ffbd5b2dbc664bd170631a3349b94e7e7ecbe91d8c6a09`；L03 `a78034457c37c1b91cc65b87cb63a90962c33323b3a1409c534477cbb8713ff6`；L04 `c83ee248428929dde1f2d399cb6a2e3b4d85786d486b881fe901b3ea440802c9`；L05 `e1e7546cbd090b22791d35d7ca79740a402fe2544f6611d2143c144fd2751768`；L06 `0e61cde167cfdc4760a5e4b182f196ccd5b45da878d37fa149e84e53e9c3ddce`；L07 `470b7b0232f796bc2b5ba8c3bc2a28dcc58c1f05e7f11741321de971c1fc981c`；L09 `cf6149087c33529a85abacbcecbf285a86248516c6bd0ffbee6d9f4b5beb0c5c`；L12 `395a0add9ee6328bc4206a042b90dbc70063fc6a8aa0420ad4483ffe0d2cab6b`。

## CS25 Lecture 23 source audit

- Official classroom evidence is Stanford Online `ckNMsUuLryM` and its 1,210 timed English caption cues. No standalone final classroom deck was found; the 39 accepted visuals are deduplicated, cropped classroom frames with timestamp provenance.
- The 40-page NLLB team seminar deck is verification-only and must not be described as the Stanford classroom deck. The 192-page NLLB paper is used to verify EOM, curriculum, metric, and toxicity terminology while classroom claims remain bounded to November 14, 2023.
- The legacy note's Padlet poll, localization map, priority formula, BigQuery/dashboard/versioning process, internal staff dashboard, agentic deployment, steering cadence, and fixed governance thresholds are unsupported and were removed.
- The accepted note treats the project as a coupled human/evaluation/data/model/safety system: interviews and language standards, FLORES-200, NLLB-Seed, LASER3/Stopes mining, data provenance, MoE/EOM/curriculum, automatic versus human evaluation, toxicity, open release, and Q&A boundaries.

## CS153 Lecture 02 source constraint

- Historical Stanford upload `yeA-opPcYxk` is private as of 2026-08-11 and no public Stanford re-upload was found.
- The repository retains timestamped subtitles and the official thumbnail, but no local video or slide deck.
- Because the lecture is an interview rather than a slide lecture, the accepted visual strategy is reproducible transcript-grounded concept diagrams with explicit provenance, not fabricated slide screenshots or repeated speaker frames.

## CS153 Lecture 03 source audit

- Historical Stanford upload `jB13kCmWT2k` is also private as of 2026-08-11; the repository retains timestamped subtitles and the official thumbnail but no local video or slide deck.
- Transcript topic anchors are now extracted to `/tmp/cs153-l03-work/transcript-windows.txt`: Apollo begins near 07:52, Rubix/Kubernetes near 16:40, Project Maven near 21:27, government/commercial abstraction near 27:00, Warp Speed near 33:57, and privacy/efficiency trade-offs near 39:49.
- Primary-source supplementation is available from Palantir's official Apollo documentation/demo transcript and official Rubix architecture documentation. These should be used to verify deployment constraints, release channels, schema-safe rollback, heterogeneous environments, hardened Kubernetes, autoscaling, multi-tenant isolation, and write-once/ship-anywhere claims.
- Lecture 03 can therefore use transcript-grounded diagrams plus official Palantir architecture figures or carefully redrawn mechanisms, with source facts separated from Shyam Sankar's strategic and political judgments.
- Final Lecture 03 treatment preserves a source-version difference instead of flattening it: the historical classroom transcript says Rubix nodes rotate in roughly 40--72 hours, while the Palantir Rubix documentation retrieved on 2026-08-11 says nodes live no longer than 48 hours.

## CS153 Lecture 04 source audit

- Historical Stanford upload `qzT8I-J8sQ8` is private as of 2026-08-11; the repository retains the official cover and a complete 42:43 automatic subtitle file with 1208 cues.
- The transcript's proper nouns are noisy (`Giam Lumpl`, `Mrol`, `Lasha`) but its timeline is usable: unsupervised MT near 03:00, formal proof search near 05:00, Chinchilla/LLaMA near 09:00, scale-only FP16 failure near 12:00, Mistral data work near 17:00, deployment last mile near 20:30, Le Chat feedback near 24:45, reasoning/DeepSeek near 27:45, EU AI Act near 30:50, and post-training competition near 37:10.
- Primary-source supplementation is local and reproducible: Lample's unsupervised MT and HTPS papers, Chinchilla, LLaMA, and Mistral 7B, plus official Mistral and European Commission pages indexed in `cs153/lecture04/source-materials/SOURCES.md`.
- Regulatory wording is intentionally dated: the classroom says concrete transparency specifications were still debated; current European Commission sources say GPAI provider obligations entered application on 2025-08-02, with a transition deadline of 2027-08-02 for models already on the market before that date.

## CS153 Lecture 05 source audit

- Historical Stanford upload `9SqYFxp9yRM` is private as of 2026-08-11; the repository retains the official cover and 931 timestamped subtitle cues but no slide deck or local video.
- The interview has no recoverable slide spine, so the accepted visual treatment is 16 reproducible transcript-grounded system diagrams rather than fabricated screenshots or repeated speaker portraits.
- Vercel and Next.js official sources verify the current mechanisms for Framework-Defined Infrastructure, Build Output API, ISR, Fluid Compute, Spend Management, Observability, and v0; the note explicitly distinguishes current product behavior from the 2025 classroom preview.
- The main systems synthesis is two coupled loops: `application intent → framework semantics → IR → infrastructure` and `traffic → telemetry/metering → developer decision → new deployment`.
- `scale-to-zero` exposed a checker bug because case-insensitive substring matching treated it as the mixed-case acronym `ZeRO`; the checker now uses term boundaries and exact case for `ZeRO`, with a regression test.

## CS153 Lecture 06 source audit

- Historical Stanford upload `LriOr64E8D8` is private as of 2026-08-11; the repository retains the official cover and 1266 timestamped subtitle cues for the 52:17 interview.
- The transcript mixes technical mechanisms with unsourced market, cost, capacity and productivity estimates. The accepted note explicitly labels those figures as speaker estimates unless an official source confirms the same scope and date.
- Primary-source anchors are sufficient for the main mechanisms: Saudi DGA cloud governance, KFSHRC's fully robotic heart transplant, Groq/Aramco Digital inference infrastructure, Gholami et al.'s `AI and Memory Wall`, and Sebastian et al.'s in-memory computing review.
- The strongest lecture synthesis is three-layered: `device/memory/interconnect/facility → useful compute per watt`, `capacity → affordable inference → application diffusion`, and `data/workflow/human accountability → deployable government agents`.
- Fully robotic surgery is not rewritten as autonomous surgery, shorter formulation search is not rewritten as shorter regulatory approval, and later Groq expansion announcements are not back-projected into the March 2025 classroom snapshot.

## CS153 Lecture 07 source audit

- Historical Stanford upload `4jDQi9P9UIw` is private as of 2026-08-11; the repository retains the official cover and 1288 timestamped subtitle cues for the 48:37 Cursor CTO interview.
- Classroom scale, customer position and incident details remain speaker accounts. Current Cursor docs are later snapshots and are used only to verify durable mechanisms or document evolution.
- Primary-source support is strong for secure codebase indexing, privacy/security controls, Fast Apply, model evaluation/routing, turbopuffer object-storage search, PostgreSQL vacuum behavior and S3 object semantics.
- The lecture's durable architecture is three coupled loops: workspace change to incremental retrieval context, request to model/edit/validation, and failure telemetry to mitigation/migration/guardrail.
- The PostgreSQL story is not rewritten as a universal anti-Postgres claim; the note traces MVCC residue, autovacuum/disk headroom, retry amplification, re-embedding and migration capacity.

## CS153 Lecture 08 source audit

- The historical upload `MBD0Ah9cpYU` requires sign-in as of 2026-08-11; the repository retains the official cover and 833 timestamped subtitle cues for the 37:53 Thorn interview.
- The accepted visual treatment is 16 reproducible, non-sensitive, transcript-grounded diagrams. The note never reproduces illegal material or gives generation, distribution or evasion instructions.
- Durable primary-source anchors come from Thorn Safer Match/Predict and Safety by Design materials, NCMEC CyberTipline reporting guidance, and NIST AI 600-1/100-4.
- The systems synthesis separates classifier signals, platform policy decisions, lawful reporting and investigation outcomes; predictive scores remain triage signals rather than legal conclusions.
- Final Lecture 08 is 25 pages with 16 figures, 36 teaching boxes and 11 teacher-voice markers; strict coverage is zero-warning, quality is `⭐⭐⭐`, double-pass XeLaTeX has no layout warnings, and canonical QA is signed.

## CS153 Lecture 09 source audit

- The repository retains the official cover and 1033 timestamped subtitle cues for the 39:02 Todd McKinnon interview, `wu2BWTVQQ1Q`.
- Primary-source support is available from Okta Universal Directory and Identity Engine policy docs, Okta's 2023 support-system incident RCA, current agent-identity material, the 2021 Auth0 acquisition release, NIST SP 800-207 and OAuth/OIDC/SCIM/WebAuthn specifications.
- The note separates the February 2025 classroom snapshot from later Okta continuous-session and agent-lifecycle product evolution.
- The durable systems synthesis is identity access loop, incident-to-trust learning loop and technology-transition-to-organization loop; agent access uses actor/subject delegation and short-lived scoped tokens rather than shared user secrets.
- Final Lecture 09 is 24 pages with 16 figures, 31 teaching boxes and 8 teacher-voice markers; strict coverage is zero-warning, quality is `⭐⭐⭐`, double-pass XeLaTeX has no layout warnings, and canonical QA is signed.

## CS153 Lecture 10 source audit

- The repository retains the official cover and 1025 timestamped subtitle cues for the 41:56 Ben Mann interview, `UdxSCFmUk9o`.
- Primary-source support covers neural scaling laws, GPT-3, InstructGPT, Constitutional AI/RLAIF, Anthropic evaluation and interpretability research, current RSP v3.0 and Claude API model lifecycle docs.
- The note explicitly separates the February 2025 classroom ASL framing from Anthropic's RSP v3.0 published on 2026-02-24.
- The durable systems synthesis is scaling forecast and compute allocation, distributed-training observability/recovery, post-training and elicitation-aware evaluation, capability-triggered safeguards, and chat-to-API compatibility discipline.
- Final Lecture 10 is 23 pages with 16 figures, 29 teaching boxes and 7 teacher-voice markers; strict coverage is zero-warning, quality is `⭐⭐⭐`, double-pass XeLaTeX has no layout warnings, and canonical QA is signed.

## CS153 Lecture 11 and course-level completion

- Lecture 11 uses the 39:17 local timestamped transcript plus CISA, DOJ, NIST, SEC, Ninth Circuit and Supreme Court primary sources; it treats the classroom's January 2025 appeal discussion as historical rather than current.
- Current procedural record is explicit: the Ninth Circuit affirmed on 2025-03-13, issued an amended opinion and denied rehearing en banc on 2025-11-12, and the Supreme Court denied certiorari on 2026-06-29.
- The final note is 26 pages with 16 transcript-grounded diagrams, 45 teaching boxes and 7 teacher-voice markers. It distinguishes VDP from bug bounty, payment from authorization, severity from materiality, and speaker account from adjudicated outcome.
- CS153 Winter 2025 is complete at 11/11 and 270 PDF pages. Every lecture passes strict coverage and `⭐⭐⭐`; all canonical QA reports have five signed checks, and `tests/test_note_quality_scripts.py` plus `tests/test_generate_site.py` pass 26/26.

## CS25 + CS153 rewrite audit（2026-08-11）

- 本地范围为 `cs25` 40 讲，编号为 lecture01--36、38--41；官方 V1--V5 播放列表实际有 41 讲，缺失的 `lecture37` 对应 `ebnX5Ur1hBk`（Denny Zhou, *Large Language Model Reasoning*）。`cs153` Winter 2025 为 11 讲。
- 两门课本地均已有 1:1 的 TeX 讲义，当前任务是 source-first 全量重写与验收，不是从零创建目录。
- wdkns/wdkns-skills 最新 `main` 仍为 `39f1a04c46e1d0d70f6b71a8fcf079b305a632b9`。
- 工作树已有大量 CS336 修改；目标课程当前未见已跟踪修改，仅 `cs25/lecture28/slides.txt` 为既有未跟踪文件，必须保留并判断来源后再使用。
- 基线质量脚本显示 51/51 全部为 `⭐`。当前目录没有生成后的 `*-notes.pdf`，因此页数统一显示 0；但图像与内容密度缺口同样真实。
- `cs153` 11 讲全部只有字幕 + cover，0 份 slide PDF、0 manifest、0 canonical QA；每讲正文约 20--31 个盒子但只有 0--1 张图。
- `cs25` 本地 40 讲全部有字幕 + cover，只有 L26/L28/L29/L34 有 slide PDF；L26/L28/L29 已渲染大量 slide images，其余绝大多数只有 1--2 张图。现有 40 讲均无 manifest、无 canonical QA，且还需补建官方缺失课。
- 这不是局部润色任务。两门课都需要重建 source manifest、teacher-voice ledger、视觉证据和 PDF 验收链路；CS25 中仅 L26/L28/L29 可直接从本地 slide deck 开始，其余讲次要从官方视频/公开视频资料恢复视觉骨架。

## CS25 Lecture 01 source audit and rewrite

- Official source is Stanford Online video `P127jhj-8-Y`, uploaded 2022-07-08 for the Fall 2021 V1 course; duration is 22:43.
- No standalone slide PDF was found on the official V1 course page. The video visibly contains a deck, so 17 distinct teaching slides were recovered by timestamped crop; title-only dividers and repeated self-attention animation builds are documented omissions.
- The durable teaching structure is three interface shifts: fixed-vector seq2seq to query-conditioned attention, recurrent state to token-to-token self-attention, and task-specific models to reusable encoder-only/decoder-only/encoder-decoder pretraining interfaces.
- Final Lecture 01 is 25 pages with 17 figures, 35 teaching boxes, 9 formula blocks, one attention pseudocode listing and 6 teacher-voice markers. Strict coverage is clean, quality is `⭐⭐⭐`, double-pass XeLaTeX has no layout warnings, and canonical QA is signed.
- Live official-playlist audit on 2026-08-11 returns 50 entries: V1--V5 total 41 and V6 total 9. This supersedes the earlier three-video V6 snapshot.

---

## Initial Repository State
- Branch: `main`, aligned with `origin/main`.
- Untracked directory: `cs336-2026/`.
- Current `README.md` says 270 notes, but local count before this batch is 290 `*-notes.pdf` files.
- `TRACKING.md` last update date is 2026-04-12.

## Active Course Signals
- CS336 Spring 2026 is live at `https://cs336.stanford.edu/`; schedule lists 19 meetings through June 3.
- Stanford CS336 lecture material repository is `https://github.com/stanford-cs336/lectures`; public materials currently include lecture 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.
- CS153 Spring 2026 playlist has 5 public videos.
- CS25 V6 schedule has 9 talks; YouTube playlist currently has the first 3 V6 recordings.
- Bilibili page for 五道口纳什 shows newest relevant items: Modern Agent 17 and Agentic RL 16.

## CS336 2026 Local Materials
- `cs336-2026/lecture05/lecture05-slides.pdf`: official PDF, 55 pages.
- `cs336-2026/lecture06/lecture06-slides.py`: official Python trace/source.
- `cs336-2026/lecture07/lecture07-slides.py`: official Python trace/source.
- `cs336-2026/lecture08/lecture08-slides.pdf`: official PDF, 73 pages.
- `cs336-2026/lecture09/lecture09-slides.pdf`: official PDF, 57 pages.
- `cs336-2026/lecture10/lecture10-slides.py`: official Python trace/source.

## Local Tooling
- `xelatex` is available.
- `poppler-utils` is now installed after the user provided the sudo password for this session; `pdftotext`, `pdfinfo`, and `pdfimages` are available for PDF extraction.
- `ffmpeg` is available.
- `whisper` CLI is not available.
- Python `whisper` module is not available.
- ImageMagick legacy `convert` is available.
- 4 x NVIDIA A100 80GB PCIe are visible under `/proc/driver/nvidia/gpus`.
- `nvidia-smi` hangs on this host; a local skill note confirms this is expected.
- `faster-whisper` 1.2.1 is installed and cached models include `Systran/faster-whisper-large-v3`.
- `yt-dlp --list-subs` for current YouTube videos now requires cookies/sign-in.

## Bilibili Processing Check
- `BV1NdDtBjEg7`: title is `[Modern Agent] 17 Codex 中的 Plan Mode 与 update_plan，plan dynamics：创建、状态更新与replan`, duration 889s, public metadata accessible.
- `BV15JdEBmEh9`: title is `[Agentic RL] [Env] 16 Docker容器沙盒，Jupyter Kernel 创建有状态的 CI（代码解释器）环境，实现 SWE-Vision`, duration 1321s, public metadata accessible.
- Both videos have empty Bilibili subtitle lists from `x/player/v2`.
- `yt-dlp` currently fails with HTTP 412 for both direct video pages.
- Public Bilibili playurl API can download `BV1NdDtBjEg7` full low-resolution mp4.
- Public Bilibili playurl API only provides about 5 minutes of `BV15JdEBmEh9`; it is not enough for a complete note.

## Generated Notes
- `modern-agent/lecture17/lecture17-notes.pdf`: generated and compiled successfully, 8 pages.
- `cs336-2026/lecture01/lecture01-notes.pdf`: regenerated as a quality-upgraded Spring 2026 long-form note, 27 pages by `mutool`, 11 embedded images, 9 important boxes, 7 knowledge boxes, 6 warning boxes, and 9 code listings.
- `cs336-2026/lecture01/images/`: added 10 official images referenced by `lecture01-slides.py` from `stanford-cs336/lectures` for source-backed figures.
- `tools/scripts/check_quality.sh`: now falls back to `mutool` when `pdfinfo` is unavailable and counts only actual `importantbox`/`knowledgebox`/`warningbox` environments.
- `cs336-2026/lecture02/lecture02-notes.pdf`: generated from Spring 2026 official executable material, 25 pages by quality script, 11 embedded images, 8 important boxes, 6 knowledge boxes, 8 warning boxes, and 16 code listings.
- `cs336-2026/lecture02/images/`: added official/local visual assets for fp32/fp16/bf16, CPU-GPU, compute-memory, deep-network, plus lecture-referenced Marin forecast, NVIDIA FP8, and JAX roofline images.

## CS336 2026 Lecture 03 Working Notes
- User explicitly requested stricter quality for continuing CS336 2026: notes should have depth, detailed exposition, and original synthesis/insight rather than simple slide summaries.
- `cs336-2026/lecture03/` already contains official Spring 2026 `lecture03-slides.pdf`, `cover.jpg`, and 67 extracted slide images.
- Existing `cs336/lecture03/lecture03-notes.tex` is available as a topic cross-check for architectures and hyperparameters, but the Spring 2026 note should be freshly structured around the 2026 slide sequence.
- `cs336-2026/lecture03/lecture03-notes.pdf`: generated as a Spring 2026 long-form architecture/hyperparameters note, 35 pages by `mutool`, 33 embedded figures, 24 teaching boxes, and 5 code listings. It emphasizes evidence strength, conservative defaults, stability, and inference-driven attention choices rather than only summarizing slides.

## CS336 2026 Lecture 04 Working Notes
- `cs336-2026/lecture04/lecture04-slides.pdf` has 60 pages and 60 extracted slide images.
- Spring 2026 lecture04 title is "Attention alternatives and mixtures of experts".
- First half covers attention cost, linear attention, recurrent/dual forms, Mamba-2, Gated Delta Net, Qwen Next, hybrid attention, and DeepSeek Sparse Attention.
- Second half covers MoE motivation, routing variants, expert setup, training objectives, load balancing, systems parallelism, router stability, fine-tuning, upcycling, and DeepSeek MoE v1/v2/v3 plus MLA/MTP.
- Existing `cs336/lecture04/lecture04-notes.tex` is useful for MoE cross-checks but misses the new attention-alternatives front half.
- `cs336-2026/lecture04/lecture04-notes.pdf`: generated as a Spring 2026 long-form note, 38 pages by `mutool`, 41 embedded figures, 21 teaching boxes, and 3 code listings. It frames attention alternatives and MoE under sparse/conditional computation, with formulas for linear attention, Mamba-2/GDN, MoE routing, load balancing, router z-loss, and MLA.

## CS336 2026 Lecture 05 Working Notes
- `cs336-2026/lecture05/lecture05-slides.pdf` has 55 pages and no pre-existing extracted slide images.
- Spring 2026 lecture05 title is "GPUs".
- The slide sequence is: GPU scaling and architecture; CPU vs GPU; SM/SP/thread/block/warp; memory hierarchy; TPUs; matrix multiplication and tensor cores; memory wall; roofline and GPU performance tricks; low precision including MXFP8/MXFP4; operator fusion; recomputation; memory coalescing; tiling; matrix shape performance anomalies; FlashAttention via tiling and online softmax.
- Existing `cs336/lecture05/lecture05-notes.tex` is useful as a concept cross-check, but the Spring 2026 note should be generated from the current 55-slide official deck.
- `cs336-2026/lecture05/slides-images/`: generated 55 slide images from the official PDF using `mutool draw`.
- `cs336-2026/lecture05/lecture05-notes.pdf`: generated as a Spring 2026 long-form GPU performance note, 31 pages by `mutool`, 36 embedded figures, 21 teaching boxes, and 3 code listings. It emphasizes GPU execution/memory model, roofline reasoning, arithmetic intensity, precision/layout tradeoffs, tiling, matrix-shape anomalies, and FlashAttention as IO-aware design.

## CS336 2026 Lecture 06 Working Notes
- `cs336-2026/lecture06/lecture06-slides.py` is a 744-line executable Python source lecture, not a slide PDF.
- Active local environment lacks `edtrace`, `lecture_util`, `gpu_util`, `torch`, and `triton`, so the lecture cannot be executed directly here; content must be generated from source text and code.
- Lecture06 title/content: "Kernels, Triton". It covers GPU hardware recap, programming model vs hardware, warps, occupancy, bank conflicts, coalescing, block occupancy, benchmarking with CUDA events, profiling with `torch.profiler`, GeLU naive/builtin/compiled comparison, Triton introduction, Triton GeLU, fused softmax, row-sum tiling, and matmul+ReLU tiling/fusion.
- Assets downloaded/copied into `cs336-2026/lecture06/images/`: `gpu-hardware.png`, `cuda-grid.png`, `block-occupancy.png`, `triton-softmax.png`, `triton-row-sum.png`, `gemm_tiled.png`, plus L05 recap images `gpu-execution-model.jpg`, `roofline.jpg`, `tiling-math.jpg`, and `online-softmax.jpg`.
- `cs336-2026/lecture06/lecture06-notes.pdf`: generated as a Spring 2026 long-form Kernels/Triton note, 31 pages by quality script, 12 embedded figures, 31 teaching boxes, and 9 code listings. It emphasizes the benchmark/profile loop, kernel fusion memory accounting, Triton block-level programming, row-wise and tiled reductions, and matmul+activation fusion.

## CS336 2026 Lecture 07 Working Notes
- `cs336-2026/lecture07/lecture07-slides.py` is a 619-line executable Python source lecture, not a slide PDF.
- Lecture07 title/content: "parallelism". It moves from single-GPU parallelism to multi-GPU/multi-node parallelism and covers collective operations, rank/world size, broadcast/scatter/gather/reduce/all-gather/reduce-scatter/all-reduce/all-to-all, GPU interconnect hierarchy, RDMA, InfiniBand/RoCE, NCCL, PyTorch `torch.distributed`, collective bandwidth benchmarking, and minimal MLP implementations of data parallelism, tensor parallelism, and pipeline parallelism.
- Assets downloaded into `cs336-2026/lecture07/images/`: official CS336 figures `gpu-node-overview.png`, `ranks.png`, `data-parallelism.png`, `tensor-parallelism.png`, `pipeline-parallelism.png`; plus PyTorch/NCCL collective diagrams `broadcast.png`, `scatter.png`, `gather.png`, `reduce.png`, `all-gather.png`, `all-reduce.png`, and `reduce-scatter.png`.
- `cs336-2026/lecture07/lecture07-notes.pdf`: generated as a Spring 2026 long-form Parallelism note, 25 pages by quality script, 14 embedded figures, 30 teaching boxes, and 7 code listings. It emphasizes collective operations as the vocabulary of distributed training, topology-aware communication cost, NCCL/PyTorch distributed semantics, collective benchmarking, and data/tensor/pipeline parallelism as batch/width/depth sharding choices.
- 2026-05-12 new-workflow rewrite: local `lecture07-slides.py` matches official Stanford raw source except whitespace. The regenerated note fixes the old standard gaps by adding explicit `读图` explanations for every important communication/topology/parallelism figure, first-use explanations for HBM/sharding/ZeRO/collectives, a localized classic topology image, collective-operation glossary tables, benchmark bandwidth formulas, and code-level walkthroughs for all-reduce, reduce-scatter/all-gather, data parallelism, tensor parallelism, and pipeline parallelism. Final metrics: 26 pages, 15 figures, 42 teaching boxes, 7 code listings, quality `⭐⭐⭐`, clean log scan, checked visual QA.

## CS336 2026 Lecture 08 Working Notes
- `cs336-2026/lecture08/lecture08-slides.pdf` is an official 73-page slide deck titled "Parallelism Basics".
- `pdftotext` is unavailable and installing `poppler-utils` via `sudo apt-get` is blocked by an interactive password prompt; existing `mutool` successfully extracted per-page text to `/tmp/lecture08-text-*.txt` and rendered all 73 slide images under `cs336-2026/lecture08/slides-images/`.
- Lecture08 structure: Part 1 networking for LLMs; Part 2 standard LLM parallelization primitives; Part 3 scaling and training big LMs with parallelism.
- Main topics: single-GPU compute/memory limits; collective communication and all-reduce vs reduce-scatter + all-gather; TPU/GPU network topology tradeoffs; naïve data parallelism; ZeRO stages 1/2/3 and FSDP; pipeline parallelism, bubbles, microbatches, zero-bubble ideas; tensor parallelism along width with row/column splits; activation memory and sequence parallelism; expert parallelism and MoE routing; context/ring attention; 3D/4D parallelism recipes; recent model parallelism examples including DeepSeek, Yi, Llama 3 405B, Gemma 2, Mixtral, Nemotron, and Qwen 3.
- `cs336-2026/lecture08/lecture08-notes.pdf`: generated as a Spring 2026 long-form Parallelism Basics note, 41 pages by quality script, 51 embedded figures, 23 teaching boxes, and 0 code listings. It emphasizes memory/communication accounting, ZeRO/FSDP state sharding, pipeline bubbles, tensor/sequence/expert/context parallelism, 3D/4D placement rules, and recent large-model parallelism configurations.
- 2026-05-12 new-workflow rewrite: old Lecture08 draft failed the stricter checks because it omitted 22 slide pages and had figures without explicit `读图` explanations. The regenerated note now uses all 73 slide pages as the visual spine, with one explanation block per teaching slide or dense table/figure. Final metrics: 53 pages, 74 figure inclusions, 76 teaching boxes, 59 read-figure hits, quality `⭐⭐⭐`, no missing slide images, clean log scan, checked visual QA.

## CS336 2026 Lecture 09 Working Notes
- `cs336-2026/lecture09/lecture09-slides.pdf` is an official 57-page slide deck titled "Scaling Laws - Basics".
- With `poppler-utils` installed, `pdfinfo` confirms 57 pages and `pdftotext -layout` extracted page text to `/tmp/lecture09-all.txt` and `/tmp/lecture09-pages/page-*.txt`.
- `mutool draw` rendered all 57 slide images under `cs336-2026/lecture09/slides-images/`.
- Lecture09 structure: motivation for taking scaling seriously; history/background of data scaling laws; neural/LLM scaling behaviors; data scaling and its theory; data mixture, distribution shift, and repetition; model-engineering scaling laws; architecture/optimizer/depth-width/batch/LR hyperparameters; joint data-model scaling laws; Kaplan vs Chinchilla compute-optimal tradeoffs; Chinchilla fitting methods; train-optimal vs deployment-aware overtraining; IsoFLOPS beyond LMs; final scaling law recap.
- `cs336-2026/lecture09/lecture09-notes.pdf`: generated as a Spring 2026 long-form Scaling Laws Basics note, 36 pages by quality script, 44 embedded figures, 23 teaching boxes, and 3 code listings. It emphasizes scaling laws as engineering forecasting tools, data scaling theory and pitfalls, hyperparameter/architecture scaling, critical batch size, muP, joint data-model scaling, Kaplan vs Chinchilla fitting methodology, and train-optimal vs deployment-optimal tradeoffs.
- 2026-05-12 new-workflow rewrite: old Lecture09 draft failed the stricter checks because it omitted 13 slide pages and had figures without explicit `读图` explanations. The regenerated note now includes all 57 slides in order and expands every important plot/formula/table into a read-the-figure or read-the-formula block. Final metrics: 42 pages, 58 figure inclusions, 59 teaching boxes, 53 read-figure hits, 5 formulas, 3 code listings, quality `⭐⭐⭐`, clean log scan, checked visual QA.

## CS336 2026 Lecture 10 Working Notes
- `cs336-2026/lecture10/lecture10-slides.py` is an official 611-line executable Python source lecture titled "Lecture 10: inference"; local execution is not required because the source contains the teaching text, formulas, and asset references.
- Main lecture structure: inference use cases and metrics; Transformer notation and arithmetic intensity; naive autoregressive inference vs KV cache; prefill/generation memory and compute accounting; latency/throughput/KV-cache model; lossy shortcuts including GQA, MLA, CLA, local/hybrid attention, DeepSeek v4 attention, quantization, pruning and distillation; lossless speculative sampling; dynamic serving with continuous batching, selective batching, and PagedAttention.
- Downloaded 28 original lecture/image assets into `cs336-2026/lecture10/images/` from the official CS336 image repository and referenced remote sources, then converted the two WebP Scaling Book diagrams into PNG for XeLaTeX compatibility.
- Existing `cs336/lecture10/lecture10-notes.tex` is useful as a cross-check, but the 2026 note should be freshly structured around the official Spring 2026 source and should emphasize inference as a memory-traffic and serving-systems problem, not just an algorithm list.
- `cs336-2026/lecture10/lecture10-notes.pdf`: generated as a Spring 2026 long-form Inference note, 30 pages by quality script, 29 embedded figures, 41 teaching boxes, and 5 code listings. It emphasizes inference as a memory-bandwidth/KV-cache/serving-systems problem, with detailed derivations for arithmetic intensity, KV cache size, latency-throughput tradeoffs, lossy KV compression, exact speculative sampling, continuous batching, and PagedAttention.
- 2026-05-12 new-workflow rewrite: old Lecture10 draft failed the stricter checks because figures had no explicit `读图` treatment and terminology digestion was not detectable. The regenerated note follows the executable source clusters, includes all local teaching PNGs, explicitly explains HBM/KV cache/TTFT/latency/throughput/arithmetic intensity/GQA/MLA/CLA/AWQ/speculative sampling/continuous batching/PagedAttention, and maps localized remote figures in coverage markers. Final metrics: 21 pages, 29 figures, 34 teaching boxes, 23 read-figure hits, quality `⭐⭐⭐`, clean log scan, no coverage warnings, checked visual QA.

## CS336 2026 Lecture 11 Working Notes
- `cs336-2026/lecture11/lecture11-slides.pdf` is an official 58-page slide deck titled "Scaling - Case Study and Details".
- Main lecture structure: motivation for scaling in practice; MiniCPM case study with muP, LR/batch scaling, WSD, and Chinchilla analyses; DeepSeek scaling with LR/batch and IsoFLOP; recent model scaling recipes including Qwen, Kimi K2, Hunyuan, LLaMA 3, MiniMax; optimizer scaling and StepFun; Muon; maximum update parametrization in depth and modern LM caveats.
- 2026-05-12 new-workflow generation: rendered all 58 slide images, wrote a slide-complete note with detailed `读图`/`读公式` blocks. Final metrics: 43 pages, 59 figure inclusions, 60 teaching boxes, 53 read-figure hits, quality `⭐⭐⭐`, clean log scan, checked visual QA.

## CS336 2026 Lecture 12 Working Notes
- `cs336-2026/lecture12/lecture12-slides.py` is an official 394-line executable Python source lecture titled "Lecture 12: evaluation".
- Main lecture structure: what makes a model good; perplexity and probability-based evaluation; exam benchmarks; chat/preference benchmarks; agentic benchmarks; pure reasoning benchmarks; safety benchmarks; realism/ecological validity; validity, contamination, and benchmark quality; how to think about evaluation.
- 2026-05-12 new-workflow generation: localized all 42 referenced image assets, wrote a source-node-complete evaluation note with detailed `读图` blocks and terminology explanations. Final metrics: 29 pages, 44 figure inclusions, 40 teaching boxes, 25 read-figure hits, quality `⭐⭐⭐`, clean log scan, no coverage warnings, checked visual QA.

## CS336 2026 Lecture 13 Working Notes
- `cs336-2026/lecture13/lecture13-slides.py` is an official 622-line executable Python source lecture titled "Lecture 13: Data I".
- Main lecture structure: data motivation and training stages; raw web sources and crawling limits; copyright, licenses, fair use, lawsuits, ToS; Common Crawl; Wikipedia/GitHub/arXiv; BERT/BooksCorpus, WebText, CCNet, C4, GPT-3, The Pile, Gopher/MassiveText, LLaMA, RefinedWeb/FineWeb, Dolma, DCLM, Nemotron-CC, The Stack, CommonPile; plus data quality audit loops.
- 2026-05-12 new-workflow generation: localized all 18 referenced image assets, wrote a source-node-complete Data I note with detailed source diagrams, dataset lineage tables, legal/ethical terminology, filtering/dedup/provenance explanations, and data-quality checklist. Final metrics: 20 pages, 19 figure inclusions, 46 teaching boxes, 13 read-figure hits, quality `⭐⭐⭐`, clean log scan, no coverage warnings, checked visual QA.

## CS336 Workflow Audit: Figure-Heavy But Prose-Thin
- User review on 2026-05-13 identified a real workflow gap: the regenerated CS336 notes include many images but often lack enough detailed prose and transitions between small sections.
- Root cause: previous checks rewarded slide-complete image coverage, `读图` keyword presence, page count, box count, and visual QA, but did not measure prose density, local explanation depth, or section bridge paragraphs.
- Added stricter checks in `tools/scripts/check_note_coverage.py`: `figure-heavy-prose-thin`, `thin-local-figure-explanations`, and `weak-section-openers`.
- Updated `tools/scripts/check_quality.sh` so figure-heavy notes with prose-per-figure below about 260 are demoted from `⭐⭐⭐` and the report shows `c/f` prose characters per figure.
- Updated `AGENTS.md`, `QUALITY.md`, `docs/NOTE_GENERATION_WORKFLOW.md`, and `tools/skills/video-render-common/writing-and-figures.md` to require prose-led section writing, transition-in/out in blueprints, pre-figure setup, post-figure synthesis, and connected teaching units.
- Created `docs/CS336_WORKFLOW_AUDIT_2026-05-13.md` documenting the root cause, evidence, workflow fixes, and repair priority.
- Lecture12 was rewritten as a sample under the stricter standard. Before rewrite: `figs=44 readfig=25 boxes=40 teacher_voice=0 summaries=6 prose_chars=6570`, warnings for `figure-heavy-prose-thin`, `thin-local-figure-explanations`, `teacher-voice-underrepresented`, and `weak-section-openers`. After rewrite: `figs=44 readfig=27 boxes=45 teacher_voice=13 summaries=7 prose_chars=11474`, no coverage warnings, and quality reports `32p 11s 45b 44f 260c/f ⭐⭐⭐`.

## CS336 2026 Lecture 01-02 Regeneration Notes
- User requested redoing CS336 2026 lecture01 and lecture02 under the new standards rather than patching old drafts.
- New standards are now documented in `AGENTS.md`, `QUALITY.md`, `CLAUDE.md`, and `tools/skills/video-render-common/writing-and-figures.md`: slide-complete coverage, detailed read-the-figure explanation, concentrated terminology digestion, and diagram/table/formula scaffolding for foundational concepts.
- Lecture01 and lecture02 are executable Python lecture sources, not PDF decks. The source text and image calls define the teaching-slide/node sequence; if browser rendering of trace pages is not reliable, treat every function/text/image cluster in the official source as the slide-complete coverage target.
- `cs336-2026/lecture01/lecture01-notes.pdf`: regenerated from scratch under the new standards, 20 pages by quality script, 15 figures, 32 teaching boxes, and 4 code listings. It covers all official image assets and executable-source teaching clusters, with read-the-figure boxes for industrialization, GPT-4 opacity, FLOPs breakdown, emergence, Transformer architecture, compute/memory, DGX topology, prefill/decode, Chinchilla IsoFLOP, Marin scaling, Pile data mixture, and tokenization.
- `cs336-2026/lecture02/lecture02-notes.pdf`: regenerated from scratch under the new standards, 20 pages by quality script, 11 figures, 38 teaching boxes, and 6 code listings. It covers tensors, dtype memory, CPU/GPU movement, einops, FLOPs vs FLOP/s, MFU, arithmetic intensity, roofline, gradient FLOPs, optimizer state, training loop, gradient accumulation, activation checkpointing, and an end-to-end resource ledger.

## Workflow Audit Findings
- Full-repo static scan of 303 source `.tex` notes showed systemic issues: 65 notes under 8 pages, 188 notes with fewer than 3 figures, 100 notes with figures but no read-the-figure explanation, 213 notes without obvious terminology digestion, and 38 notes with substantial slide/frame assets but low figure coverage.
- Highest-risk series by static metrics: `agentic-rl`, `llm-architect`, `modern-agent`, and many `cs25` notes are thin and likely need regeneration rather than patching.
- A user-provided review of old `cs336/lecture01/lecture01-notes.tex` exposed a new workflow gap: first-use explanations are missing for systems/resource-accounting terms such as ZeRO, sharding, fused kernel, collectives, optimizer state, activation checkpointing, DRAM/SRAM/HBM, and perplexity.
- Added `check_note_coverage.py` first-use glossary heuristics; it correctly flags old `cs336/lecture01` for unexplained `SRAM`, `fused kernel(s)`, `perplexity`, `sharding`, and `state sharding`.

## CS336 2026 Lecture 03 New-Workflow Regeneration Notes
- Lecture03 is a 67-page official PDF deck on LM architecture and hyperparameters.
- Regenerated `cs336-2026/lecture03/lecture03-notes.tex` under the new workflow as a slide-complete note: all 67 source slides are included, title/outline/recap slides receive concise explanations, and dense evidence slides receive `读图` treatment.
- Final lecture03 metrics: 44 pages, 68 figures, 27 teaching boxes, and quality script `⭐⭐⭐`.
- `render_pdf_qa.py` initially exposed a real visual QA problem: `pdftoppm` rendered near-blank pages despite successful LaTeX compile. The tool was fixed to detect blank rendered pages and fallback/check render output; regenerated contact sheet now has no near-blank pages.

## CS336 2026 Lecture 04 New-Workflow Regeneration Notes
- Lecture04 is a 60-page official PDF deck on attention alternatives and mixture-of-experts.
- Regenerated `cs336-2026/lecture04/lecture04-notes.tex` under the new workflow as a slide-complete note: all 60 source slides are included, grouped into attention alternatives, MoE motivation, routing, training, systems, stability/fine-tuning/upcycling, and DeepSeek case study.
- Final lecture04 metrics: 41 pages, 61 figures, 42 teaching boxes, and quality script `⭐⭐⭐`; LaTeX log scan has no errors, undefined controls, rerun warnings, overfull boxes, or missing-character warnings.
- 2026-05-12 re-verification confirms the source-slide contract directly: every `slides-images/slide-000.jpg` through `slide-059.jpg` appears in the note, plus the cover image. The refreshed visual QA contact sheet has 41 rendered pages and no near-blank pages; manual inspection found no obvious missing/cropped figures, spillover, or unaccompanied dense figures.

## CS336 2026 Lecture 05 New-Workflow Regeneration Notes
- Lecture05 is a 55-page official PDF deck on GPUs.
- Regenerated `cs336-2026/lecture05/lecture05-notes.tex` under the new workflow as a slide-complete note: all 55 source slides are included, grouped into GPU architecture, roofline/low precision, fusion/recomputation, coalescing/tiling/matrix mystery, and FlashAttention.
- Final lecture05 metrics: 38 pages, 56 figures, 44 teaching boxes, and quality script `⭐⭐⭐`; LaTeX log scan has no errors, undefined controls, rerun warnings, overfull boxes, or missing-character warnings.

## CS336 2026 Lecture 06 New-Workflow Regeneration Notes
- Lecture06 is an executable Python source lecture on benchmarking, profiling, and Triton kernels.
- Regenerated `cs336-2026/lecture06/lecture06-notes.tex` under the new workflow as a source-node-complete note covering GPU hardware recap, programming model, benchmarking/profiling, GeLU fusion, Triton mental model, fused softmax, tiled row sum, and tiled matmul+ReLU.
- Final lecture06 metrics: 20 pages, 8 figures, 36 teaching boxes, and quality script `⭐⭐⭐`; LaTeX log scan has no errors, undefined controls, rerun warnings, overfull boxes, or missing-character warnings.

## YouTube video ttkd0t5qTD4 note task
- User requested downloading original YouTube video `https://www.youtube.com/watch?v=ttkd0t5qTD4` and generating Chinese notes/PDF.
- Initial anonymous `yt-dlp --dump-single-json` failed with YouTube anti-bot login requirement: `Sign in to confirm you’re not a bot`. Root cause is platform-side anonymous access challenge, not a missing local codec or format issue. Next path: try local browser cookies without committing/storing cookie files.

## YouTube authentication root-cause investigation
- `yt-dlp` version is 2026.03.17 from the active venv, so the recurring YouTube login challenge is not explained by stale yt-dlp.
- No system Chrome/Chromium/Firefox/Edge/Brave binary or browser profile is installed under the usual `~/.config`/`~/.mozilla` locations. Therefore `yt-dlp --cookies-from-browser` has no local browser cookies to import yet.
- Playwright Chromium exists under `~/.cache/ms-playwright/chromium-1117`, so a durable local browser profile can be created, logged into manually, then exported to a Netscape cookie file for yt-dlp.

## YouTube auth fixes attempted
- Installed `bgutil-ytdlp-pot-provider==1.3.1`, which `yt-dlp` now loads as a YouTube POT provider.
- Installed `curl_cffi`, but version `0.15.0` was rejected by `yt-dlp` as unsupported. Root cause: current yt-dlp only accepts curl_cffi `0.5.10` or `0.10.x` through `0.14.x`. Fixed by forcing `curl_cffi==0.14.0`; impersonation targets are now available.
- With plugin loaded but no provider server running, yt-dlp still hit `LOGIN_REQUIRED`; next fix is to run the bgutil HTTP provider on `127.0.0.1:4416`.

## OAuth status for YouTube ttkd0t5qTD4
- User completed Google device-code authorization. The patched `yt-dlp-youtube-oauth2` plugin saved `youtube-oauth2.token_data` in the local yt-dlp cache.
- New failure after authorization: YouTube initial data API returns HTTP 400 when called through the OAuth plugin. This is a separate post-auth API compatibility issue, not the previous anonymous `LOGIN_REQUIRED` bot challenge.

## YouTube authentication root-solve status
- Device-code OAuth was successfully completed and token cache was written, but the third-party OAuth plugin remains incompatible with current YouTube internal API extraction: `/youtubei/v1/next` returns HTTP 400, and skipping initial data yields only storyboard formats, no real audio/video streams.
- Practical root path for this host is account cookies plus PO-token provider. Added `tools/scripts/youtube_auth_check.sh` to validate the full chain: yt-dlp, compatible curl_cffi, bgutil provider, local `youtube_cookies.txt`, and format listing.
- `.gitignore` now excludes `youtube_cookies*.txt`, generic `cookies*.txt`, and `.yt-dlp-auth/` so credentials are not committed.

## YouTube ttkd0t5qTD4 acquisition complete
- Cookie-based authenticated yt-dlp now works with `--remote-components ejs:github`, `bgutil` GVS PO token generation, and `curl_cffi==0.14.0`.
- Downloaded `youtube/ttkd0t5qTD4/original.mkv`: 3:48:00, 3840x2160 AV1 video plus Opus audio, about 3.8 GiB.
- Downloaded metadata, cover thumbnail, and multiple English/Chinese subtitle tracks. The best working source transcript appears to be `original.en-US.srt`, which contains Chinese dialogue with embedded English technical terms.

## YouTube ttkd0t5qTD4 final note
- `youtube/ttkd0t5qTD4/ttkd0t5qTD4-notes.pdf`: 21 pages, quality script `⭐⭐⭐`, coverage check passes with `figs=12 readfig=7 boxes=32 term_digest=2 summaries=11`.
- Visual PDF QA rendered 21 pages with no near-blank pages; contact sheet inspected and checklist completed.

## Zhang Xiaojun YouTube interview batch
- User requested all Zhang Xiaojun YouTube interviews. Treating `tyb` as `ytb/YouTube` unless corrected.
- Channel `/videos` flat list has 164 entries and includes Chinese episodes, English duplicate uploads, quarterly reports, surveys, and other non-interview formats. Need a deduplicated queue before generation to avoid redoing bilingual duplicates.

## Zhang Xiaojun queue created
- Built `youtube/zhangxiaojun/QUEUE.md` and `queue.json` from the channel playlists. Chinese canonical playlist has 147 entries: 133 rough interviews, 13 review/survey/quarterly-report items, and 1 video-special. English video podcast playlist has 17 entries and is tracked separately to avoid duplicate notes.
- Batch policy: process Chinese interview episodes first, newest to oldest; skip English duplicate uploads unless no Chinese source exists; do not retain every full-resolution original video by default because 100+ long interviews would require hundreds of GB to TB-scale storage.

## GPU transcription root-cause check
- User interrupted CPU transcription and requested a root fix for GPU. Evidence: NVIDIA A100 devices and driver are visible; `torch` in the current venv is CPU-only (`2.11.0+cpu`), but `ctranslate2==4.7.1` detects CUDA devices and supports CUDA compute types. Root issue for faster-whisper was using CPU mode unnecessarily, not missing GPU hardware.

## GPU transcription fixed
- Validated that NVIDIA A100 devices and CTranslate2 CUDA support are present. `torch` remains CPU-only, but faster-whisper does not require torch CUDA for CTranslate2 inference.
- Added `tools/scripts/transcribe_faster_whisper.py`, defaulting to `large-v3`, `device=cuda`, `compute_type=float16`. Smoke test on 2-minute sample succeeded.
- Re-ran episode 138 transcription with GPU large-v3: 6416 segments, about 755.8 seconds, output `transcript.zh.srt/txt/json`. This replaces the aborted CPU partial transcript.

## Zhang Xiaojun EP139 complete
- `youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/ep139-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage passes with `figs=9 readfig=9 boxes=25 term_digest=5 formulas=1 summaries=11`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Visual QA contact sheet inspected and checklist completed.

## Podcast visual policy update
- User feedback: for fixed-camera podcast/interview videos without meaningful visual content, use one image as cover and do not repeat speaker frames throughout the note. Implemented this in EP139 by removing body speaker frames and retaining only cover plus generated concept diagrams. Updated `docs/PODCAST_INTERVIEW_WORKFLOW.md`, `QUALITY.md`, and `tools/scripts/check_quality.sh` so high-quality podcast notes can receive `⭐⭐⭐` with 5+ substantive figures/diagrams instead of repeated speaker frames.

## Zhang Xiaojun EP138 complete
- `youtube/zhangxiaojun/ep138-vG1RBqn1sG4/ep138-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage passes with `figs=7 readfig=9 boxes=30 term_digest=3 summaries=15`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.

## Zhang Xiaojun EP137 acquisition
- `bv8ghyTFF9w` downloaded as work video; YouTube had no usable subtitles. Generated faster-whisper large-v3 CUDA transcript: 7042 segments, about 888.4 seconds. `chapter-transcripts.md` is ready for note writing.

## Zhang Xiaojun EP137 complete
- `youtube/zhangxiaojun/ep137-bv8ghyTFF9w/ep137-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=7 readfig=6 boxes=31 term_digest=5 summaries=17`; warnings are weak-section-opener heuristics only.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.

## Zhang Xiaojun EP136 acquisition
- `u1Lzp-7Ybn8` downloaded as work video; YouTube had no usable subtitles. Generated faster-whisper large-v3 CUDA transcript: 2067 segments, about 264.5 seconds. `chapter-transcripts.md` is ready for review/survey note writing.

## Zhang Xiaojun EP136 complete
- `youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/ep136-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=6 readfig=5 boxes=25 term_digest=5 summaries=18`; warnings are weak-section-opener heuristics only.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.

## Zhang Xiaojun EP135 acquisition
- `x8qdqWIVVTA` downloaded as work video; YouTube had no usable subtitles. Generated faster-whisper large-v3 CUDA transcript: 4236 segments, about 450.5 seconds. `chapter-transcripts.md` is ready for note writing.

## Zhang Xiaojun EP135 complete
- `youtube/zhangxiaojun/ep135-x8qdqWIVVTA/ep135-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=7 readfig=6 boxes=30 term_digest=2 summaries=17`; warnings are weak-section-opener heuristics only.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.

## Zhang Xiaojun EP134 acquisition
- `owjTOT14bG0` downloaded as work video; YouTube had no usable subtitles. Generated faster-whisper large-v3 CUDA transcript: 4751 segments, about 561.7 seconds. `chapter-transcripts.md` is ready for data-survey note writing.

## Zhang Xiaojun EP134 complete
- `youtube/zhangxiaojun/ep134-owjTOT14bG0/ep134-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=7 readfig=6 boxes=26 term_digest=3 summaries=19`; warnings are weak-section-opener heuristics only.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.

## Zhang Xiaojun EP133 acquisition
- `iiBY0fqpThI` downloaded as 480p work video; YouTube had no usable subtitles. Generated faster-whisper large-v3 CUDA transcript: 12819 segments, about 1369.9 seconds. `chapter-transcripts.md` is ready for marathon interview note writing.

## Zhang Xiaojun EP133 complete
- `youtube/zhangxiaojun/ep133-iiBY0fqpThI/ep133-notes.pdf`: 23 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=9 readfig=10 boxes=30 term_digest=4 summaries=15`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure compresses the 6h45m interview into research trajectory, vision as perspective, world-model definition, LLM boundary, reverse OpenAI / AMI Labs, LLM-pilled critique, robotics/VLA, intelligence spectrum, and the closing `42` synthesis.

## Zhang Xiaojun EP132 complete
- `youtube/zhangxiaojun/ep132-n4_c_HsodPg/ep132-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=9 readfig=8 boxes=28 term_digest=5 summaries=14`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 6614 segments, about 663.3 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as physical-world AI industrial training: Waymo systems engineering, Momenta production delivery, autonomous-driving business models, Xinghaitu whole-machine/supply-chain strategy, Data Recipe, robot-brain VLM/VLA dual system, Xu Huazhe departure and moat analysis, demo-to-production evaluation, and `go to soil` synthesis.

## Zhang Xiaojun EP130 complete
- `youtube/zhangxiaojun/ep130-ruVJ_5dObxs/ep130-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=9 readfig=9 boxes=26 term_digest=3 summaries=15`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 7333 segments, about 799.9 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as AI product methodology: Miaoya as strong internet product but not AI Native, flow-to-context design, One Way Door, AI product organization and taste, AI population / Will-Skill, Xingmian and Dokie product bets, Agent short-loop feedback, platform/tool/user-mind positioning, CEO all-in decision, and cross-episode Agent/context/language synthesis.

## Zhang Xiaojun concept figure display fix
- User reported tofu-box glyphs in generated concept diagrams, especially EP133 `download-internet-to-world.png`.
- Root cause: earlier ad hoc PIL drawing used `DroidSansFallbackFull.ttf`, which covers Chinese but lacks many Latin letters, arrows, digits, and punctuation used in mixed Chinese/English diagrams.
- Fix: added `tools/scripts/render_zhangxiaojun_concept_figures.py`, using `/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf`, which covers Chinese, Latin, digits, arrows, and common punctuation. The script also simplifies figures into sparse teaching cards with more whitespace and less in-image prose.
- Regenerated 60 concept figures across Zhang Xiaojun EP130, EP132--EP139; recompiled PDFs and regenerated visual QA contact sheets. Future no-slide podcast figures should use the script or the same font/style rules.

## Zhang Xiaojun EP129 complete
- `youtube/zhangxiaojun/ep129-9zSMTUUEfmU/ep129-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=9 readfig=10 boxes=27 term_digest=2 summaries=14`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 5266 segments, about 568.9 seconds.
- Applied podcast visual policy: cover plus simplified generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as a Zhipu company route: Tsinghua P2P / technology transfer, cognitive intelligence, GPT-3 and ChatGPT shocks, Scaling Law evolution, model-company differentiation, DeepSeek/open-source effects, IPO and governance thresholds, post-IPO financial/research balance, CEO as bridge, and `AGI path opener` synthesis.

## Zhang Xiaojun EP128 complete
- `youtube/zhangxiaojun/ep128-MW-ezf2RhVg/ep128-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage hard checks pass with `figs=9 readfig=8 boxes=28 term_digest=3 summaries=13`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 10161 segments, about 1005.1 seconds.
- Applied podcast visual policy: cover plus simplified generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as the final Manus pre-acquisition conversation: Peak's App Store/NLP/Open IE path, why the recording matters as a final interview, complexity and organization mistakes, Manus ARR flywheel, AI-as-manufacturing, Agent infrastructure gaps, complexity risk, Agent market map, globalization/Singapore, and the keep-it-simple product principle.

## Zhang Xiaojun EP127 complete
- `youtube/zhangxiaojun/ep127-SG90aehV3vU/ep127-notes.pdf`: 26 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=11 boxes=30 term_digest=5 summaries=11`; visual QA contact sheet inspected and checklist completed.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 1824 segments, about 280.6 seconds.
- Fixed EP127 text font coverage by using `AR PL UMing CN` with fake bold, after Fandol dropped the character `珺` in `张小珺`.
- Added EP127 concept figures to `tools/scripts/render_zhangxiaojun_concept_figures.py` and regenerated Zhang Xiaojun figures with the simplified AR PL concept-figure style.
- Fixed `build_lecture_manifest.py` to include `figures/` directories so podcast concept diagrams appear in source manifests.
- Note structure frames the cross-year quarterly report as AI War, OpenAI revenue stack, Nvidia GPU vs Google TPU, GPT/Claude/Gemini alternating lead, Search/Agent entry disruption, Online Learning as third paradigm, data/product loop, Neo Labs/Robotics, and China/global founder strategy.

## Zhang Xiaojun EP125 complete
- `youtube/zhangxiaojun/ep125-k82iFzvKFCQ/ep125-notes.pdf`: 28 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=12 boxes=33 term_digest=5 summaries=14`; visual QA contact sheet inspected and checklist completed.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 2298 segments, about 327.5 seconds.
- Note structure frames the interview as capital-market AI accounting: US tech three-line thesis, OpenAI product-company thesis and negative flywheel, OpenAI/Anthropic contrast, Robinhood alpha loop, founder taste, AI sector map, electronic revenue vs labor pool, AI bubble dashboard, and 2026 market watchlist.

## Zhang Xiaojun EP123 complete
- `youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/ep123-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=25 term_digest=4 summaries=12`; visual QA contact sheet inspected and checklist completed.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 6435 segments, about 791.0 seconds.
- Note structure frames the interview as AI product/platform theory: product-manager trajectory, compression as intelligence, data three stages, video-generation bet, generation-system stack, app/model boundary blur, recommendation vs generation systems, consumer-side power shift, distribution-to-production platforms, and trust as post-attention currency.

## Zhang Xiaojun EP121 complete
- `youtube/zhangxiaojun/ep121-2o281Zy5aZE/ep121-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=27 term_digest=3 summaries=10`; visual QA contact sheet inspected and checklist completed.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 3619 segments, about 442.3 seconds.
- Note structure frames the interview as robotics systems theory: graphics-to-robotics, RL/Sim2Real as first paradigm shift, multimodal model as brain and RL as cerebellum, VLA action gap, data bottleneck, Gemini Robotics 1.5 motion transfer, synthetic data loop, V-L-V world model, tactile/dexterous hand, robot generalist stages, safety, and China/US robotics split.

## Zhang Xiaojun EP120 complete
- `youtube/zhangxiaojun/ep120-40qPt8R2uys/ep120-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=9 boxes=30 term_digest=2 summaries=11`; visual QA contact sheet inspected and checklist completed.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 3281 segments, about 391.0 seconds.
- Note structure frames the interview as Xiaopeng Physical AI transformation: Liu Xianming trajectory, autonomous stack evolution, language bottleneck removal, cloud model factory, host-OEM data/infra loop, Robotaxi as lifestyle service, technical/organizational simplification, route switching risk balance, leader mission stages, and Software 3.0 as data-path shortening.

## Zhang Xiaojun EP119 complete
- `youtube/zhangxiaojun/ep119-858HR43pegk/ep119-notes.pdf`: 22 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=30 term_digest=2 summaries=12`; visual QA contact sheet inspected and checklist completed.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the survey as attention-architecture archaeology: Full Attention bottlenecks, Linear Attention/KDA, Kimi Linear hybrid design, Kimi vs DeepSeek vs MiniMax M2, MoE-to-Attention architectural analogy, old mechanisms revived under new scale and hardware constraints, hardware-friendly algorithms, and advice for young researchers.

## Zhang Xiaojun EP118 complete
- `youtube/zhangxiaojun/ep118-RxXVq7-sJzM/ep118-notes.pdf`: 22 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=11 boxes=36 term_digest=3 summaries=11`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 6562 segments, about 9982.4 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as a CEO-MoE system: human-vs-AI context, DeepSeek best-practice learning, VLA/Driver OS, traffic world model, Agent OS and action alignment, AGI-era terminal strategy, organization as MoE, energy/relationship loop, wisdom as relation, and shell-vs-foundation capability.

## Zhang Xiaojun EP117 complete
- `youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/ep117-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=13 readfig=10 boxes=26 term_digest=3 summaries=7`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 7794 segments, about 15757.5 seconds.
- YouTube edition is static cover/fixed visual; description points to a Bilibili projection edition and 50-page Feishu PPT. Bilibili metadata fetch returned HTTP 412 on this host; Tavily/Exa extraction of Feishu returned no usable content/timeout. Current note uses reliable local sources: YouTube description, transcript, chapter structure, cover, and generated concept diagrams.
- Note structure frames the survey as four AI-history lines: paper-reading loop, model paradigm changes, Infra/data scaling, language-model lineage, multimodal lineage, open-source learning map, and reader advice.

## Zhang Xiaojun EP116 complete
- `youtube/zhangxiaojun/ep116-khrOsS7YQn4/ep116-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=9 boxes=36 term_digest=3 summaries=7`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 8093 segments, about 13665.0 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as a ToB enterprise AI case: Web2/recommendation/measurement roots, Palantir-to-China ToB path, conversational data acquisition, 2022 painful turnaround, private data vs public token economics, enterprise Agentic Model, DeepMiner loop, supply-side capability vs linking networks, boss/partner organization, and trusted agentic model.

## Zhang Xiaojun EP115 complete
- `youtube/zhangxiaojun/ep115-gQgKkUsx5q0/ep115-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=6 boxes=34 term_digest=4 summaries=8`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 4401 segments, about 9092.1 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Acquisition note: `yt-dlp` format 18 repeatedly failed with curl slow transfer / HTTP 503; direct `curl -L -C -` on the signed `--get-url` succeeded and produced a valid 360p work video.
- Note structure frames the interview as Agent second-half theory: language as generalization tool, Agent tasks/environments, method vs task line, code as affordance, reward and multi-agent, interface/Super App boundaries, Chatbot-to-Agent evolution, single-pole vs plural world, and different bet strategy.

## Zhang Xiaojun EP113 complete
- `youtube/zhangxiaojun/ep113-ouG6jrkECrc/ep113-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=13 readfig=6 boxes=31 term_digest=4 summaries=7`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 2866 segments, about 6073.8 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as Kimi K2 model-company strategy: infinite mountain, brain-in-vat to Agent, test-time scaling, L1-L5 non-serial path, token efficiency/Rephrase/Muon, Agentic generalization, open-source strategy, scaling/data wall, Linear Attention IQ risk, base-model vs Agent-product boundary, RL management and founder story.

## Zhang Xiaojun EP112 complete
- `youtube/zhangxiaojun/ep112-6yExfoTuSWw/ep112-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=8 boxes=32 term_digest=1 summaries=10`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 1671 segments, about 4151.3 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the quarterly report as AI product/market strategy: model-company divergence, horizontal suite vs vertical integration, intelligence/product balance, product mining window, L4 experiences (Deep Research/Claude Code), Google revaluation, AGI bubble dashboard, and Chinese AGI global narrative.

## Zhang Xiaojun EP111 complete
- `youtube/zhangxiaojun/ep111-JxEetUlV9RA/ep111-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=11 boxes=33 term_digest=1 summaries=8`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 5671 segments, about 11312.3 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Acquisition note: `yt-dlp` format 18 repeatedly failed around 9.7% with curl 56 connection closed; direct `curl -L -C -` on the signed `--get-url` succeeded and produced a valid 360p work video.
- Note structure frames the interview as hard-tech/autonomous-vehicle supply-chain case: lidar as active eye, 99.5% cost-down path, three-founder equity, financing/cashflow, first 20M order, pricing logic, customer defection, entry into automaker main camp, new money vs old money, and national/industrial opportunity.

## Zhang Xiaojun EP110 complete
- `youtube/zhangxiaojun/ep110-8dKBH4x0D9o/ep110-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=8 boxes=27 term_digest=3 summaries=9`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 3526 segments, about 8445.2 seconds.
- Applied podcast visual policy: cover plus generated concept diagrams, no repeated body speaker frames.
- Acquisition note: first faster-whisper run on GPU 0 exited early around 2800 segments and wrote only partial SRT/TXT without JSON; removed partial transcript and reran on GPU 1 successfully.
- Local official sources captured under `official-sources/`: Kimi K2 tech report PDF/text, Qwen3-Coder page text, Manus Context Engineering page text, and OpenAI ChatGPT Agent page shell plus prior Tavily extraction context.
- Note structure frames the episode as Agent technical-report synthesis: Agent definition/types, in-context vs end-to-end routes, training ingredients, Kimi K2/MuonClip/agentic data/joint RL, ChatGPT Agent unified system and safety, Qwen3-Coder/code RL/long-horizon RL, Manus context engineering, and environment+task-reward paradigm.

## Zhang Xiaojun Lovart special complete
- `youtube/zhangxiaojun/special-biptonYq-ys/lovart-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=9 readfig=5 boxes=38 term_digest=2 summaries=10`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA: 3910 segments, about 6296.7 seconds.
- Visual policy: video has dynamic title/audio waveform frames rather than slides; note uses cover/title-frame and generated concept diagrams, no repeated body speaker frames.
- Acquisition note: `yt-dlp` format 18 repeatedly failed around 5.4% with curl 56 connection closed; direct `curl -L -C -` on the signed `--get-url` succeeded after multiple resumptions and produced a valid 640x360 work video.
- Note structure frames the special as an AI application startup case: Lovart as vertical design Agent, design workflow, product-manager training, 2025 application window, subsidy/delist/cash crunch, fighting CEO, PMF emotion loop, business model/copyright risk, application moat layers, and general-vs-vertical Agent coexistence.

## Zhang Xiaojun EP109 complete
- `youtube/zhangxiaojun/ep109-pWY0HVUH8GA/ep109-notes.pdf`: 24 pages, `⭐⭐⭐`, coverage check clean with `figs=11 readfig=13 boxes=33 term_digest=6 summaries=9`.
- Video had no YouTube subtitles; transcript source is faster-whisper large-v3 CUDA.
- Visual policy: fixed podcast visual; note uses cover plus generated concept diagrams, no repeated body speaker frames.
- Note structure frames the interview as embodied AI data infrastructure: Sim2Real/Real2Sim loop, synthetic-data evaluation-first workflow, autonomous-driving vs embodied physical interaction, Physical Real2Sim, Meta/Scale data-company signal, data-quality as diversity × human guidance, PI's simulation dilemma, global embodied supply-chain map, China/US opportunity split, NVIDIA as simulation company, cross-universe/world/embodiment generalization, and GPT-1/scaling-law-stage synthesis.

## Zhang Xiaojun EP106/Puptr acquisition note
- YouTube metadata and format listing required the authenticated project path: cookies, Chrome impersonation, mweb client, bgutil PO token provider, and remote EJS challenge solver. Bare `yt-dlp` hit the YouTube bot-confirmation page.
- The video title says `含字幕`, but YouTube exposed no downloadable subtitles or auto captions. The note therefore used faster-whisper transcription.
- CUDA/CTranslate2 became unhealthy during this item: a full-video faster-whisper run stalled around 01:08, and subsequent CUDA capability probes hung. Chapter-by-chapter CPU int8 fallback completed successfully and produced the final transcript. The partial GPU transcript was preserved with `.gpu-partial` suffixes for diagnosis.

## Zhang Xiaojun EP106/Puptr complete
- `youtube/zhangxiaojun/ep106-Puptr04av5g/ep106-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=18 boxes=25 term_digest=3 summaries=9`.
- YouTube exposed no downloadable subtitle tracks despite title marker `含字幕`; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 11 chapter chunks after CUDA/CTranslate2 became unhealthy.
- Visual policy: fixed interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames.
- Note structure frames the interview as embodied AI academic lineage and industry ethics: language as intelligence jump, vision-to-action loop, embodied AI from computer vision, Wang He Stanford path, synthetic data and category-level pose estimation, software/hardware spiral, VLM/VLA data gap, two startup traps, productivity-as-product, teleoperation economics, synthetic-data recipe, capital chaos, true-demo principles, and ten-thousand-unit validation clock.

## Zhang Xiaojun Nuclear Fusion Special complete
- `youtube/zhangxiaojun/special-pVuE4J5cn98/fusion-notes.pdf`: 21 pages, `⭐⭐⭐`, coverage check clean with `figs=10 readfig=12 boxes=33 term_digest=3 summaries=9`.
- YouTube exposed no downloadable subtitle tracks despite title marker `含字幕`; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 16 fixed-duration chunks.
- Visual policy: fixed interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames.
- Note structure frames the interview as a nuclear-fusion technical and industrial primer: fission/fusion basics, controllability, tokamak and magnetic confinement, copper/low-temperature/high-temperature superconducting magnets, triple product and Q, inertial confinement limits, why high magnetic field lowers device cost, public big-science vs startup commercialization, Honghuang 70/170/380 roadmap, first plasma, high-field magnet validation, deuterium-tritium vs deuterium-deuterium fuel/regulatory tradeoffs, AI-energy coupling, and civilization-scale energy implications.

## Zhang Xiaojun EP104 complete
- `youtube/zhangxiaojun/ep104-qW-kgogQwJc/ep104-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=9 readfig=8 boxes=33 term_digest=5 teacher_voice=7 summaries=7`.
- YouTube exposed no downloadable subtitle tracks; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 20 fixed-duration chunks because CUDA/CTranslate2 health was unreliable after previous long items.
- Visual policy: fixed interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames. QA contact sheet was inspected after compressing the table of contents to remove a mostly empty directory continuation page.
- Note structure frames the interview as a随身智能入口 case: first startup/Alibaba/M Lab platform training, 2019 AI-speaker-to-AR pivot, speaker-as-product vs glasses-as-platform, always-on information directness, display/AUI/GUI differences, China/US product definitions, four opportunities against giants, ecosystem allies, OS know-how, hardware black-forest risks, playfulness culture, and founder-IP vs product-reputation governance.

## Zhang Xiaojun EP103 duplicate
- `youtube/zhangxiaojun/ep103-Xo7TxXkNsoA/` was acquired and transcribed, but comparison showed it is the same Lovart/Chen Mian interview as the already completed `youtube/zhangxiaojun/special-biptonYq-ys/`.
- Evidence: title family is identical, durations are 1:45:28 vs 1:44:57, opening transcript lines and the main Lovart/downlisting/4000 RMB/design-Agent storyline match, and the existing Lovart special note already covers the content at `youtube/zhangxiaojun/special-biptonYq-ys/lovart-notes.tex`.
- Queue action: mark EP103 `duplicate`, canonicalized to `biptonYq-ys`; do not generate a second PDF unless the user explicitly wants a separate episode-numbered duplicate copy.

## Zhang Xiaojun EP102 complete
- `youtube/zhangxiaojun/ep102-vWrYHvSRz0s/ep102-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=26 term_digest=6 teacher_voice=4 summaries=8`.
- YouTube exposed no downloadable subtitle tracks; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 22 fixed-duration chunks.
- Visual policy: fixed interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames.
- Note structure frames the interview as a multimodal technical-route lecture: CV-to-NLP learning history, static-image generation/understanding/alignment split, generation-understanding gap, next-token compression defect, feature collapse, RL/CoT and critical decision, Meta-CoT, visual-space Long CoT, two-leg roadmap of data plus action space, long-context multi-model collaboration, online/autonomous learning, and world-model/robotics implications.

## Zhang Xiaojun EP101 complete
- `youtube/zhangxiaojun/ep101-a04POJEknCY/ep101-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=13 readfig=14 boxes=33 term_digest=4 teacher_voice=4 summaries=9`.
- YouTube exposed no downloadable subtitle tracks; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 24 fixed-duration chunks.
- Visual policy: fixed interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames.
- Note structure frames the interview as an Agent application product-method case: product-manager training through debate/OnePlus/ByteDance/Moonshot, experience-vs-data, bitter lesson, token consumption speed and per-token valuation, container/environment thesis, Vibe Coder as new crowd, Agent ecosystem models, PageRank-to-AgentRank, Agent network effects and trust/identity, OS Agent as living system, business-model tradeoffs, Agent product evaluation framework, founder ego control, and comparison with Manus/Lovart.

## Zhang Xiaojun EP100 complete
- `youtube/zhangxiaojun/ep100-9Yjws_rt378/ep100-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=9 readfig=8 boxes=27 term_digest=4 teacher_voice=4 summaries=6`.
- YouTube exposed no downloadable subtitle tracks; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 9 fixed-duration chunks.
- Visual policy: fixed interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames.
- Note structure frames the interview as a legacy industrial transformation case: China speed and local R&D flywheel, EV penetration vs luxury-brand residual value, luxury strategy as cashflow for innovation, MBOS as architecture-control layer, build-vs-partner decision matrix, AI car stack, technology democratization vs luxury experience, transformation CEO 51/49 decision loop, brand guardian success criteria, and a four-layer framework for industrial companies entering the AI/electrification era.

## Zhang Xiaojun EP99 duplicate
- EP99 `aoaSwGAJW6M` is the same Yang Zhao / Energy Singularity nuclear-fusion interview family as the already completed subtitle edition `pVuE4J5cn98`.
- Queue action: mark EP99 `duplicate`, canonicalized to `pVuE4J5cn98`; existing complete note is `youtube/zhangxiaojun/special-pVuE4J5cn98/fusion-notes.tex`.

## Zhang Xiaojun VLA paper-survey acquisition
- `youtube/zhangxiaojun/special-eiQFomOuCJs/` contains the 1080p投屏版 work video, cover, metadata, transcript, and 34 chapter-aligned slide/frame candidates. This item is not a fixed-camera-only podcast; the final note should use the real投屏 frames as the visual spine, not just concept diagrams.
- Chapter/frame coverage includes: robot foundation model intro; SayCan; Inner Monologue; DoReMi; VoxPoser; VLA taxonomy; ALOHA/Mobile ALOHA; Gato; RT-1; Octo; CrossFormer; GR-1/GR-2; PaLM-E; RT-2; RT-X; OpenVLA; HiRT; Figure Helix; π0; GR00T N1; Diffusion Policy; RDT; Prediction with Action/VPP; iRe-VLA.
- Transcript source is faster-whisper large-v3 CPU int8 fallback in 22 fixed chunks because YouTube exposed no downloadable subtitles.

## Zhang Xiaojun VLA paper-survey complete
- `youtube/zhangxiaojun/special-eiQFomOuCJs/vla-notes.pdf`: 24 pages, `⭐⭐⭐`, coverage check clean with `figs=26 readfig=17 boxes=23 term_digest=1 teacher_voice=1 summaries=6`.
- The final note uses real投屏 frames as the visual spine rather than generated concept diagrams, because this item is a technical paper walkthrough with readable slides/screen content.
- Visual QA rendered all 24 pages to `qa/vla-notes/contact.png`; manual checklist was marked complete after checking for readable figures, margins, figure explanations, orphan captions/headings, blank pages, box titles, and URL overflow.
- Note structure frames the video as a robotics foundation-model/VLA paper route map: foundation model vs专用机器人模型, SayCan/Inner Monologue/DoReMi/VoxPoser, VLA definition, ALOHA/Mobile ALOHA, Gato/RT-1/Octo/CrossFormer/GR-1, RT-2/RT-X/OpenVLA/HiRT, Figure Helix/pi0/GR00T N1, Diffusion Policy/RDT, Prediction with Action/VPP, UP-VLA, online RL, and follow-up questions for scaling laws, cross-embodiment data, world models, and humanoid deployment.

## Zhang Xiaojun EP98 duplicate
- EP98 `3jI6F3M2ocU` is the same VLA paper-survey content as `eiQFomOuCJs`.
- Evidence: both metadata records have duration `2:29:41`, upload date `2025-04-07`, the same 34 chapter titles and timestamps, and the same paper list from SayCan/Inner Monologue/DoReMi/VoxPoser through RT-2/RT-X/OpenVLA/HiRT/pi0/GR00T/RDT/VPP/UP-VLA.
- Queue action: mark EP98 `duplicate`, canonicalized to `eiQFomOuCJs`; existing complete note is `youtube/zhangxiaojun/special-eiQFomOuCJs/vla-notes.tex`.

## Zhang Xiaojun EP97 complete
- `youtube/zhangxiaojun/ep97-YshXmh_q_Q4/ep97-notes.pdf`: 26 pages, `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=43 term_digest=5 teacher_voice=8 summaries=12`.
- YouTube exposed no downloadable subtitles or auto captions; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 16 fixed-duration chunks and merged into `transcript.zh.json/srt/txt`.
- Visual policy: fixed podcast/review visual; note uses cover plus generated concept diagrams, no repeated speaker frames. The concept figure script now includes EP97 diagrams for Pre-training/Post-training, Coding as cyber environment, OpenAI vs Anthropic, AGI roadmap, intelligence measurement, Agent capabilities, Online Learning, model/product moats, model-company landscape, and China/US geofence.
- Note structure frames the episode as a Q1 2025 large-model technical review: Pre-training as base-model ceiling, Post-training/RL as behavior shaping, Coding as the most general cyber environment and model hand, OpenAI/Anthropic strategy as organizational expression, AGI roadmap from ChatGPT to Coding/Agent/AI4Science/Robotics, long-term memory over raw long context, Agent as environment/tool/memory/action loop, Online Learning as potential new paradigm, model-vs-product moats, model thieves such as Perplexity/Cursor/Manus, global model-company landscape, and China/US AI constraints.

## Zhang Xiaojun EP96 complete
- `youtube/zhangxiaojun/ep96-qtugoE1xQZk/ep96-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=30 term_digest=7 teacher_voice=7 summaries=7`.
- YouTube exposed no downloadable subtitles or auto captions; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 16 fixed-duration chunks and merged into `transcript.zh.json/srt/txt`.
- Visual policy: fixed technical interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames. The concept figure script now includes EP96 diagrams for autonomous-driving ten-year route, Tesla up-dimension path, HD-map/LiDAR vs vision, sensor cost stack, camera/LiDAR tradeoff, end-to-end stack, L3/L4 boundary, E2E+VLM+world model+RL, Li Auto data loop, Weicheng project pressure field, AV organization loop, and AV terminology map.
- Note structure frames the episode as an autonomous-driving technical route lesson: early HD-map/LiDAR/rule “tram track” thinking, Tesla vision/BEV/Transformer/chip co-design, camera vs LiDAR information tradeoff, BEV feature-level fusion vs post-fusion, end-to-end as a shift from feature development to capability training, L2/L3/L4 responsibility boundaries, ODD and takeover design, Li Auto data/privacy loop, supplier and organization pressure in the Weicheng project, and follow-up questions around world models, RL, and fleet data moats.

## Zhang Xiaojun EP95 complete
- `youtube/zhangxiaojun/ep95-VdWEE6vOYRw/ep95-notes.pdf`: 20 pages, `⭐⭐⭐`, coverage check clean with `figs=12 readfig=10 boxes=33 term_digest=4 teacher_voice=6 summaries=8`.
- YouTube exposed no downloadable subtitles or auto captions; final transcript was produced by faster-whisper large-v3 CPU int8 fallback in 26 fixed-duration chunks and merged into `transcript.zh.json/srt/txt`.
- Visual policy: fixed founder/interview visual; note uses cover plus generated concept diagrams, no repeated speaker frames. The concept figure script now includes EP95 diagrams for the two-part relay interview, founder cycle, VC as expensive capital, predicting giants' predictions, Monica product evolution, AI app taxonomy, waiting for model capability, model company vs app company, DeepSeek product lesson, Manus Agent thesis, A-ha lifeform moment, and founder game thinking.
- Note structure frames the episode as an AI application entrepreneurship and Agent product-method lesson: first-startup lessons from WeChat tools/SCRM, early commercialization and SaaS unit economics, VC as an expensive tool rather than a boss, predicting platform moves, Monica as plugin/workflow container and overseas product, AI application opportunity categories, DeepSeek's product/communication lesson, Manus as domestic Agent first shot, Agent task/tool/environment/memory/deliverable loop, and founder non-linear game thinking.

## CS25 Lecture 02 source-first rewrite accepted
- Mark Chen's GPT/Codex lecture was rebuilt around 45 recovered teaching slides and 16 teacher-voice nodes, spanning language-model history, generative pretraining, GPT-1/2/3, iGPT, DALL-E, HumanEval, pass@k, sampling temperature, Codex-S, and deployment limitations.
- Final artifact: `cs25/lecture02/lecture02-notes.pdf`, 46 pages, 45 figures, 56 teaching boxes, 18,176 prose characters, strict coverage with zero warnings, `⭐⭐⭐`, two clean XeLaTeX passes, and signed canonical visual QA.
- CS25 V1--V5 rewrite progress is now 2/41; Lecture 03 is the next target and currently lacks a manifest, coverage matrix, teacher-voice ledger, slide spine, and canonical QA.

## CS25 Lecture 03 source audit
- Official source is Stanford Online `BP5CM0YxbP8`, 1:08:36, in V1 playlist `PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`; the official page and video description expose no standalone slide PDF.
- A 4-second transition scan produced 72 candidate states. Manual review retained 36 teaching slides and intentionally omitted Stanford bumpers, pure transition pages, redundant progressive builds, repeated Q&A navigation, and black transition artifacts.
- The teaching spine is VTAB and few-shot adaptation -> SSL/semi-supervision/BiT -> deduplication -> ViT architecture and data/compute scaling -> position embeddings/shape/speed/receptive field -> Scaling ViT recipes -> MLP-Mixer and closing capacity/Q&A caveats.

## CS25 Lecture 03 accepted
- `cs25/lecture03/lecture03-notes.pdf` is 40 pages with 36 recovered teaching slides, 48 teaching boxes, 10 teacher-voice markers, 5 formula blocks, one patchify listing, and 17,394 prose characters.
- Strict coverage is clean (`figs=36 readfig=34 boxes=48 term_digest=2 teacher_voice=10 formulas=5 code=1 summaries=11`); the quality audit is `⭐⭐⭐`, both XeLaTeX passes are clean, and canonical visual QA is signed.
- CS25 V1--V5 rewrite progress is now 3/41. Lecture 04 is the next source-first rewrite target.

## CS25 Lecture 04 source audit
- Official source is Stanford Online `w4Bw8WYL8Ps`, 1:20:42, with an official manual `en-US` caption track. Replacing the old auto-caption file reduced parsed cues from 4,459 duplicated entries to 1,516 clean cues.
- The V1 course page and video description expose no standalone slide PDF. A masked scene-difference scan of the 1080p recording found 121 candidate transitions; manual review retained 24 final teaching states and omitted bumpers, administrative pages, redundant builds and repeated Q&A navigation.
- Source dates conflict: the V1 schedule lists October 11, 2021; the recovered title slide says October 11, 2022; the Stanford Online upload metadata says July 13, 2022. The accepted note records the conflict and anchors technical history to the NeurIPS 2021 paper/course schedule.
- The teaching spine is stable sequence-model scaling -> MDP/offline-RL data support -> return/state/action tokenization -> non-Markov context -> supervised loss and rollout -> probabilistic inference -> return conditioning / percent BC / context / sparse reward / Key-to-Door / critic experiments -> online-RL, discounting and pessimism boundaries.

## CS25 Lecture 04 accepted
- `cs25/lecture04/lecture04-notes.pdf` is 34 pages with 24 recovered teaching slides, 40 teaching boxes, 10 teacher-voice markers, 15 formula blocks, 2 captioned listings and 18,579 prose characters.
- Strict coverage is clean (`figs=24 readfig=13 boxes=40 term_digest=2 teacher_voice=10 formulas=15 code=2 summaries=10`); the quality audit is `⭐⭐⭐`, XeLaTeX has no overflow/undefined warning after reference stabilization, and canonical visual QA is signed.
- CS25 V1--V5 rewrite progress is now 4/41. Lecture 05, Mixture of Experts / Switch Transformer (`U8J32Z3qV8s`), is the next source-first rewrite target.

## CS25 Lecture 05 source audit
- Official source is Stanford Online `U8J32Z3qV8s`, 1:05:44, with an official manual `en-US` caption track. The V1 course page and video description expose no standalone slide PDF.
- A masked scene-difference scan of the local 1080p recording produced 111 candidate transitions. Manual review retained 38 final teaching states and intentionally omitted bumpers, redundant progressive builds, and repeated Q\&A navigation while preserving their spoken content in a 20-row teacher-voice ledger.
- The teaching spine is dense scaling laws -> sparsity as a new axis -> MoE history and gating -> Switch top-1 routing -> selective precision / initialization / regularization / load balance -> static capacity and token dropping -> top-1 versus top-2 -> sparse scaling and parallelism -> upstream/downstream evidence -> multilingual training -> distillation -> V-MoE priority routing and deployment boundaries.
- Source-boundary rules distinguish total parameters, active parameters, FLOPs, communication, storage, and wall-clock time; preserve “parameters for knowledge, FLOPs for reasoning” as an explicitly unsubstantiated hypothesis; and treat negative-log-perplexity plots with the correct sign.

## CS25 Lecture 05 accepted
- `cs25/lecture05/lecture05-notes.pdf` is 43 pages with 38 recovered teaching slides, 42 teaching boxes, 15 teacher-voice markers, 9 formula blocks, 2 captioned listings, and 16,621 prose characters.
- Strict coverage is clean (`figs=38 readfig=13 boxes=42 term_digest=7 teacher_voice=15 formulas=9 code=2 summaries=11`); the quality audit is `⭐⭐⭐`, two XeLaTeX passes produce no overflow/undefined warning, and canonical visual QA is signed after contact-sheet plus full-size page checks.
- CS25 V1--V5 rewrite progress is now 5/41. Lecture 06, Perceiver and Perceiver IO (`GV8-6ZgJVRk`), is the next source-first rewrite target.

## CS25 Lecture 06 source audit
- The historical local URL `GV8-6ZgJVRk` now returns `Video unavailable`. The current canonical Stanford Online upload is `wTZ3o36lXoQ`, 58:58, published 2022-07-15; all time provenance in the rewrite uses this current upload.
- The current video exposes an official manual `en-US` caption track. Replacing the old repeated track reduced parsed captions from 3,553 to 1,399.
- A 2-second masked slide scan produced 92 candidates. Manual review retained 39 final teaching states, including two distinct optical-flow examples, and omitted bumpers, pure section dividers, redundant progressive builds, repeated Q\&A navigation, and intermediate animation frames.
- The teaching spine is general-purpose perception motivation -> Transformer generality and quadratic cost -> latent cross-attention bottleneck -> ViT/DETR/Slot Attention comparisons -> Fourier position and permuted ImageNet -> Perceiver IO output queries -> multimodal arrays -> byte-level language -> optical flow and very large outputs -> small-data and speed-versus-generality boundaries.

## CS25 Lecture 06 accepted
- `cs25/lecture06/lecture06-notes.pdf` is 38 pages with 39 recovered teaching slides, 35 teaching boxes, 12 teacher-voice markers, 7 formula blocks, 2 captioned listings, and 13,835 prose characters.
- Strict coverage is clean (`figs=39 readfig=8 boxes=35 term_digest=4 teacher_voice=12 formulas=7 code=2 summaries=9`); the quality audit is `⭐⭐⭐`, stabilized XeLaTeX has no overflow/undefined/hyperref warning, and canonical visual QA is signed after contact-sheet plus full-size page checks.
- CS25 V1--V5 rewrite progress is now 6/41. Lecture 07 is the next source-first rewrite target.

## CS25 Lecture 07 source audit
- Official source is Stanford Online `zejXBg-2Vpk`, 1:05:43, published 2022-07-16, with 1,476 parsed official manual English captions. The video description identifies Aidan Gomez for the Transformer origin/intuition recap and Jannik Kossen / Neil Band for Non-Parametric Transformers.
- The V1 course page and video description expose no standalone slide PDF. A 2-second masked scene-difference scan produced 73 candidates; manual review retained 28 final teaching states and omitted bumpers, redundant progressive builds, repeated Q\&A navigation, blank transitions, and the end slate.
- Primary-source verification used Kossen et al. `2106.02584` for the dataset-and-mask input contract, ABD/ABA tensor shapes, permutation equivariance, stochastic feature/target masking, UCI average ranks, corruption table, duplicate intervention, and quadratic scaling boundary.
- The legacy note was not salvageable: its 12 nominal slide placements repeatedly used `cover.jpg` and introduced unsupported AI-SRE, incident timeline, governance toolkit, and drift-monitoring material absent from the lecture.
- The teaching spine is token self-attention -> multi-head relations -> teacher forcing and causal masking -> explicit dataset dependence -> $(X,M)$ input contract -> per-attribute embedding -> ABD/ABA alternation -> stochastic masking -> tabular rank evidence -> real-data corruption -> duplicate/intervention mechanism -> GNN/meta-learning/retrieval connections and scaling limits.

## CS25 Lecture 07 accepted
- `cs25/lecture07/lecture07-notes.pdf` is 37 pages with 28 recovered teaching slides, 30 teaching boxes, 26 teacher-voice markers, 19 formula blocks, 2 captioned listings, and 17,406 prose characters.
- Strict coverage is clean (`figs=28 readfig=6 boxes=30 term_digest=1 teacher_voice=26 formulas=19 code=2 summaries=11`); the quality audit is `⭐⭐⭐` at 621 prose characters per figure, stabilized two-pass XeLaTeX has no layout warnings, and canonical visual QA is signed after contact-sheet plus full-size checks of the cover, dense benchmark/corruption tables, duplicate panel, scaling table, and final page.
- CS25 V1--V5 rewrite progress is now 7/41. Lecture 08 is the next source-first rewrite target.

## CS25 Lecture 08 source audit
- Official source is Stanford Online `pC4zRb_5noQ`, 59:34, published 2022-07-17, with 1,557 parsed official manual English captions. The V1 schedule dates the class to 2021-11-15, while the induction-head article appeared on 2022-03-08; the note preserves the classroom's unpublished/tentative framing instead of backdating later confidence.
- The course page and video description expose no standalone slide PDF. A 1,787-sample frame scan yielded 108 candidates; manual review retained 64 final teaching states and omitted repeated builds, blank transitions, bumpers, the end slate, and low-resolution intermediate Lexoscope states while retaining the spoken soft-induction examples.
- Primary-source verification used the Transformer Circuits mathematical framework, the induction-head article and archival paper, Kaplan scaling laws, GPT-3, the Transformer paper, and Distill circuits work. The evidence taxonomy separates representational plausibility, temporal co-occurrence, behavioral generality, causal intervention, and near-complete toy-model accounting.
- The teaching spine is mechanistic interpretability -> ICL score and phase change -> one-layer QK/OV algebra -> skip trigrams -> eigenvalue copying signatures and MLP failure boundary -> two-layer virtual heads -> induction pattern -> small-model ablation -> large-model timing correlation -> soft induction and scaling-law limits.

## CS25 Lecture 08 accepted
- `cs25/lecture08/lecture08-notes.pdf` is 55 pages with 64 recovered teaching slides, 24 teaching boxes, 21 teacher-voice markers, 19 formula blocks, 2 captioned listings, and 17,849 prose characters.
- Strict coverage is clean (`figs=64 readfig=6 boxes=24 term_digest=1 teacher_voice=21 formulas=19 code=2 summaries=11`); the quality audit is `⭐⭐⭐` at 278 prose characters per figure, stabilized two-pass XeLaTeX has no layout/reference/hyperref warnings, and canonical visual QA is signed after contact-sheet plus full-size checks of terminology tables, QK/OV formulas, eigenvalue plots, two-layer expansion, ablation evidence, and soft induction.
- CS25 V1--V5 rewrite progress is now 8/41. Lecture 09 is the next source-first rewrite target.

## CS25 Lecture 09 source audit
- Official source is Stanford Online `wvE2n8u3drA`, 48:18, published 2022-07-18, with 981 parsed official manual English captions and a classroom date of 2021-11-29. The course page and video description expose no standalone slide PDF.
- A 1,449-sample masked scene-difference scan produced 119 candidates; manual review retained 47 final teaching states and omitted bumpers, blank transitions, duplicate builds, repeated navigation, non-distinct demo thumbnails, the stop-recording frame, and the end slate.
- Primary-source verification used Raw Audio Transformer `2106.16036`, Generative/Contrastive Audio Representations `2010.11459`, and classroom-era Audio Transformers `2105.00335v1`, plus WaveNet, VQ-VAE, Jukebox, FSD50K, ViT, and wav2vec 2.0. The note does not backport the later 2025 Audio Transformers revision into the 2021 lecture.
- The teaching spine is signal representation and time scale -> Fourier/STFT intuition -> sample-level autoregression -> local attention plus compressed context -> VQ/codebook hierarchy -> generative versus contrastive representation learning -> linear probes -> raw-waveform FSD50K classification -> Haar/pooling hierarchy -> learned filterbank inspection.
- Evaluation boundaries remain explicit: raw-audio top-5 next-sample accuracy is not perceptual quality; linear-probe accuracy and multi-label mAP are not interchangeable; waveform, spectrogram, learned filterbank, embedding, and VQ code are distinct representation levels; “Adieu WaveNet/Convolutions” is treated as a controlled-experiment challenge rather than a universal architecture-elimination claim.

## CS25 Lecture 09 accepted
- `cs25/lecture09/lecture09-notes.pdf` is 46 pages with 47 recovered teaching slides, 28 teaching boxes, 18 teacher-voice markers, 18 formula blocks, 2 captioned listings, and 16,960 prose characters.
- Strict coverage is clean (`figs=47 readfig=9 boxes=28 term_digest=4 teacher_voice=18 formulas=18 code=2 summaries=10`); the quality audit is `⭐⭐⭐` at 360 prose characters per figure, stabilized two-pass XeLaTeX has no layout/reference/hyperref warnings, and canonical visual QA is signed after contact-sheet plus full-size checks of Fourier/STFT formulas, raw-audio evaluation, VQ/codebook hierarchy, linear-probe evidence, Haar wavelets, FSD50K results, learned filterbanks, and the final comparison table.
- CS25 V1--V5 rewrite progress is now 9/41. Lecture 10 is the next source-first rewrite target.

## CS25 Lecture 10 source audit (in progress)
- Official source is Stanford Online `CYaju6aCMoQ`, “Represent part-whole hierarchies in a neural network,” 52:48, uploaded 2022-08-11 and labeled CS25 V2. The currently reachable course archive does not provide reliable historical class-date evidence, so the note must not invent a lecture date.
- The official video exposes an `en-US` manual-caption track. It yields 1,122 parsed captions and replaces the legacy 15,755-line rolling/repeated subtitle dump. A local 1080p working video is retained under the repository's ignored media policy.
- No standalone slide PDF is exposed by the official video or current course page. A 2-second crop-aware scan produced 1,584 samples and 49 candidates; manual review retained 32 distinct teaching states and omitted the Stanford bumpers, exact duplicate builds, repeated Q&A navigation, the paper-link end slide, and the final bumper.
- The old 12 KB note has no teaching figures, no source manifest, no teacher-voice ledger, no coverage matrix, and no verified video URL. It also collapses the talk into generic GLOM commentary and adds hindsight claims that are not tied to the lecture, so it requires full replacement rather than incremental repair.
- The primary technical source is Hinton's 44-page `arXiv:2102.12627`, published 2021-02-25 with no later arXiv revision. The paper and talk both frame GLOM as an imaginary system/design document: the mechanism is a proposal, not a benchmarked model result.
- The teaching spine is dynamic parse-tree allocation -> universal capsules and islands of agreement -> coordinate-frame psychology -> contrastive learning and collapse -> columns/levels/time -> four-source embedding update -> similarity-gated local attention -> transformational ambiguity versus Hough-style part-to-whole voting -> multimodal identity-pose distributions -> masked reconstruction/BPTT plus consensus distillation -> replicated local embeddings, longer-range sparse high levels, and location-conditioned neural fields.

## CS25 Lecture 10 accepted
- `cs25/lecture10/lecture10-notes.pdf` is 41 pages with 32 recovered teaching slides, 38 teaching boxes, 12 in-note teacher-voice markers synthesized from a 30-row ledger, 13 formula blocks, 2 captioned listings, and 20,710 prose characters.
- Strict coverage is clean (`figs=32 readfig=15 boxes=38 term_digest=3 teacher_voice=12 formulas=13 code=2 summaries=11`); the quality audit is `⭐⭐⭐` at 647 prose characters per figure, and stabilized two-pass XeLaTeX has no layout, reference, rerun, or hyperref warnings.
- Canonical visual QA is signed after inspecting the 41-page contact sheet and full-size SimCLR, coordinate-frame, four-source update, attention, Hough, uncertainty, reconstruction, consensus, sparsity, neural-field, audit-table, and final-reading pages. A mostly empty final reference page found during QA was eliminated by compact two-column reflow.
- The accepted note keeps the strongest boundary visible throughout: GLOM is a design document / imaginary system, so islands, consensus, multimodal basis functions, sparse upper levels, and biological connections are taught as testable hypotheses rather than benchmarked facts.
- CS25 V1--V5 rewrite progress is now 10/41. Lecture 11 is the next source-first rewrite target.

## CS25 Lecture 11 source audit
- Official Stanford Online source is `XfpMkf4rD6E`, taught 2023-01-10 and uploaded 2023-05-19; the previous note's upload date was incorrect. The 1:11:40 recording exposes 1,667 parsed manual-caption intervals.
- The first 10:14 is course-staff context; Karpathy's lecture starts at 10:14. Historical claims about context lengths, ChatGPT, and open research questions are therefore preserved as January 2023 evidence rather than current facts.
- No independent slide PDF is public. A 2-second 1080p scan yielded 2,150 samples and 139 candidates; manual review retained 61 teaching states spanning course context, pre-2012 field fragmentation, language-model history, attention, nanoGPT, model families, ViT/Conformer/Decision Transformer/AlphaFold, GPT-3/scaling/in-context learning, and the general-purpose-computer synthesis.
- Primary-source boundaries matter: the cortex analogy is speculation; attention priority is personal recollection; “delete recurrence” is a teaching compression of a multi-component package; AlphaFold2 is specialized rather than “just GPT”; activation-space inner optimization and external scratchpads are hypotheses, not established mechanisms.

## CS25 Lecture 11 accepted
- Final artifact is 67 pages with all 61 teaching slides, 34 teaching boxes, 35 ledger rows, 11 teacher-voice markers, 16 formula blocks, 4 captioned code listings, and 21,389 prose characters.
- Static acceptance is clean: strict coverage has zero warnings, quality is `⭐⭐⭐` at 350 prose characters per figure, every manifest slide is referenced exactly once, and `git diff --check -- cs25/lecture11` passes.
- Two XeLaTeX passes produce no overfull/underfull, undefined-reference, rerun, or hyperref warnings. Visual QA accepted all 67 rendered pages after contact-sheet and enlarged dense-page review.
- The replacement removes unsupported governance/deployment/team-process prose and restores the actual lecture's problem chain: unification, attention history, communication/computation, nanoGPT implementation, architecture families, cross-modal interfaces, and runtime adaptation through context.
- CS25 V1--V5 rewrite progress is now 11/41. Lecture 12 is next.

## CS25 Lecture 12 source audit and acceptance
- The historical YouTube ID used by the legacy note is unavailable; the official Stanford Online replacement is `DJ1Yy6Aquug`, taught 2023-01-17, uploaded 2023-05-20, 1:06:21, with 1,264 parsed official manual-caption cues.
- The official description and course archive expose no standalone slide PDF. High-recall video review retained 17 distinct teaching states; the formal slide talk ends near 00:30:54 and the remaining half hour is teacher-voice-heavy Q\&A over the same final slide.
- The legacy note mixed in post-lecture Superalignment and generic deployment/governance material. The replacement preserves the actual boundary: alignment versus governance, explicit/implicit intent, SFT--RM--RL, InstructGPT costs/preferences, early ChatGPT limitations, evaluation asymmetry, scalable oversight, targeted perturbations, critique results, discriminator--critique gap, preference payload, tools, outer/inner alignment, and interpretability.
- Primary-source verification used Christiano et al. `1706.03741`, Leike et al. `1811.07871`, Ouyang et al. `2203.02155`, Stiennon et al. `2009.01325`, Saunders et al. `2206.05802`, and Irving et al. `1805.00899`; no post-2023 result is presented as classroom evidence.
- Final artifact is 27 pages with all 17 teaching slides referenced exactly once, 32 teaching boxes, a 35-row teacher-voice ledger, 10 formula blocks, 2 captioned listings, and 14,325 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 842 prose characters per figure, and stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings.
- Canonical visual QA is signed after inspecting the full contact sheet and enlarged formula, table, code, result, transition, reference, and final pages. The first QA pass exposed an orphaned “定义” line and a mostly empty final page; both were fixed before acceptance.
- CS25 V1--V5 rewrite progress is now 12/41. Lecture 13 is next.

## CS25 Lecture 13 source audit and acceptance
- Verified Stanford Online `tVtOevLrt5U`, the CS25 V2 archive, 1,439 official manual-caption cues, Jason Wei's 37-page official Google Slides deck, and the pre-lecture primary papers on emergence, CoT, BIG-Bench Hard, multilingual CoT, self-consistency, scaling laws, and instruction tuning.
- The historical boundary is 2023-01-24. The old thin draft's later emergence-metric debate and generic product claims were removed rather than presented as classroom content.
- Accepted `cs25/lecture13/lecture13-notes.pdf` at 42 pages with all 36 teaching slides, 2 video-derived Playground states, 43 teaching boxes, 13 in-note teacher-voice markers, 8 formula blocks, 2 captioned listings, and 20,281 prose characters.
- Static acceptance is clean: strict coverage has zero warnings, quality is `⭐⭐⭐` at 533 prose characters per figure, every required visual is referenced exactly once, and `git diff --check -- cs25/lecture13` passes.
- Two-pass XeLaTeX has no overfull/underfull boxes, unresolved references, rerun requests, or hyperref layout warnings. Canonical visual QA is signed after correcting the slide 22/23 mapping and reviewing the full contact sheet plus enlarged source-audit, CoT demo, code, table, and final pages.
- CS25 V1--V5 rewrite progress is now 13/41. Lecture 14 is next.

## CS25 Lecture 14 source audit and acceptance
- Verified Stanford Online `phWxl0nkgKk`, the CS25 V2 archive, 1,176 official manual-caption intervals, and the course-recommended Cicero, piKL, and No-Press Diplomacy primary papers. No public standalone deck was found, so the official 1080p recording was sampled and manually deduplicated from 70 candidates to 42 distinct teaching states.
- The historical boundary is 2023-01-31. Later reasoning-model results are excluded from reconstructed classroom evidence; a clearly labeled modern-agent interpretation is kept separate.
- Accepted `cs25/lecture14/lecture14-notes.pdf` at 44 pages with all 42 teaching slides referenced exactly once, 31 teaching boxes, 13 in-note teacher-voice markers, 6 formula blocks, 2 captioned listings, and 17,277 prose characters.
- Static acceptance is clean: strict coverage has zero warnings, quality is `⭐⭐⭐` at 411 prose characters per figure, and the note includes a terminology digest plus substantive section-opening bridges.
- Two final XeLaTeX passes have no overfull/underfull boxes, unresolved references, rerun requests, or hyperref warnings beyond repository-standard Fandol notices. Canonical visual QA is signed after reviewing the full contact sheet and enlarged terminology, value-filtering/code, and final pages.
- CS25 V1--V5 rewrite progress is now 14/41. Lecture 15 is next.

## CS25 Lecture 15 source audit and acceptance
- Verified Stanford Online `ct4tdyyNDY4`, the 2023-02-07 classroom date, 1,840 non-empty official manual-caption cues, and the course-recommended RT-1, SayCan, and Inner Monologue papers plus BC-Z and DIAL primary sources.
- No public standalone slide deck exists. The 1080p official recording produced 315 high-recall stable candidates and 45 distinct teaching states. Final assets were re-extracted from the full `1920x1080` frames after visual QA exposed that the earlier `1680`-pixel crop truncated slide content on the right.
- Accepted `cs25/lecture15/lecture15-notes.pdf` at 48 pages with all 45 teaching figures referenced exactly once, 29 teaching boxes, 12 in-note teacher-voice markers, 6 displayed formula blocks, 2 captioned listings, and 18,626 prose characters.
- Static acceptance is clean: strict coverage has zero warnings and quality is `⭐⭐⭐` at 413 prose characters per figure. Two stabilized XeLaTeX passes have no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after compressing a mostly empty third TOC page, repairing a table-width overflow, reviewing the complete contact sheet, and enlarging RT-1, SayCan, Inner Monologue, DIAL, summary-table, and final pages.
- CS25 V1--V5 rewrite progress is now 15/41. Lecture 16 is next.

## CS25 Lecture 16 source audit and acceptance
- Verified the 2023-02-14 CS25 V2 course entry, Stanford Online video `sTQaJyrI-zg`, official 1:15:05 runtime, 6,652-line `en-US` manual subtitle track, and the three recommended Maieutic Prompting, Symbolic Knowledge Distillation, and Delphi primary papers.
- The legacy subtitle was a 16,655-line rolling automatic-caption file. It was replaced by the manual track and normalized into timed, clean, and five-minute chunk transcripts for teacher-voice auditing.
- No public standalone deck exists. Two-second sampling of the 1080p recording produced 2,253 frames, 207 high-recall stable candidates, and 56 manually deduplicated teaching states. Every final asset was extracted from the full `1920x1080` frame.
- Accepted `cs25/lecture16/lecture16-notes.pdf` at 50 pages with all 56 teaching figures referenced exactly once, 18 teaching boxes, 9 in-note teacher-voice markers, 9 formula blocks, 3 captioned listings, and 20,134 prose characters.
- Static acceptance is clean: strict coverage has zero warnings and quality is `⭐⭐⭐` at 359 prose characters per figure. Two stabilized XeLaTeX passes have no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical PDF QA is signed after reviewing the complete contact sheet and enlarged Maieutic, Symbolic KD, Delphi evaluation/data, public-critique, hybrid-architecture, final-table, and self-check pages.
- CS25 V1--V5 rewrite progress is now 16/41. Lecture 17 is next.

## CS25 Lecture 17 source audit and acceptance
- Verified Stanford Online `nz7_wg5iOlA`, the 2023-02-21 CS25 V2 course entry, the official 1:08:09 runtime, 1,581-cue `en-US` manual subtitle track, and the primary Med-PaLM, Performer, ProtNLM, DeepConsensus, and Enformer sources used by the lecture.
- No standalone public slide deck was found. The 1920x1080 official recording was sampled into 2,045 frames; stability filtering produced 103 high-recall candidates, and manual review retained 84 distinct full-width teaching states.
- The legacy note had only two figures and mixed in unsupported RLHF, bilingual fairness prompts, crowd re-ranking, ontology pipelines, and deployment procedures. The replacement removes those inventions and restores the actual classroom sequence: biomedical data as sequences, MultiMedQA, PaLM/Flan-PaLM/Med-PaLM, multidimensional clinical evaluation, Performer, protein LMs, ProtNLM, DeepConsensus, Enformer, and foundation biomedical AI.
- Accepted `cs25/lecture17/lecture17-notes.pdf` at 68 pages with all 84 teaching figures referenced exactly once, 38 teaching boxes, 14 in-note teacher-voice markers, 10 formula blocks, 3 captioned listings, and 21,962 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 261 prose characters per figure. Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing all 68 pages plus enlarged source-audit, rubric, formula, code, result, application, future-synthesis, Nobel-question, and reference pages. No blank/cropped figures, overflow, orphan captions, stranded headings, malformed box titles, or raw-URL issues remain.
- CS25 Lecture 18 legacy source attribution was wrong: `dEFn6nnoC-8` is a 2025 Trenton Bricken PhD defense, while the official 2023 CS25 classroom recording is `L4DC7e6g2iI` and contains two talks by Trenton Bricken and Will Dorrell. Unsupported MoE-routing, production-monitoring, governance, deployment, and incident-response material was removed.
- Accepted `cs25/lecture18/lecture18-notes.pdf` at 61 pages with all 66 teaching figures referenced exactly once, 26 teaching boxes, 11 in-note teacher-voice markers, 17 displayed formula blocks, 3 captioned listings, and 17,886 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 271 prose characters per figure. Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing all 61 pages plus enlarged formula, table, code, hand-drawn derivation, synthesis, and reference pages. CS25 V1--V5 rewrite progress is now 18/41; Lecture 19 is next.
- Verified CS25 Lecture 19 against Stanford Online `fz8wf9hN20c`, official manual captions, the 2023-10-10 classroom boundary, and primary PaLM-E, RT-1, RT-2, RT-X, Language Table, and Language-to-Rewards sources. The legacy note had no video URL, one figure, no manifest/teacher-voice ledger, and only a thin product summary.
- Accepted `cs25/lecture19/lecture19-notes.pdf` at 48 pages with all 55 teaching figures referenced exactly once, 28 teaching boxes, 11 in-note teacher-voice markers, 8 displayed formula blocks, 3 captioned listings, and 18,174 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 330 prose characters per figure. Stabilized two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing all 48 pages plus enlarged source tables, PaLM-E/RT-2 results, action-token and MPC code, sim-to-real evidence, final comparison, safety synthesis, and references. CS25 V1--V5 rewrite progress is now 19/41; Lecture 20 is next.

## CS25 Lecture 20 source audit and acceptance
- Verified Stanford Online `wwQ1LQA3RCU`, the 2023-10-24 classroom boundary, 985 parsed official manual-caption cues, and the MineDojo, Voyager, Eureka, VIMA, Video PreTraining, RT-2, and RoboCat primary sources. The legacy note had one figure and reduced the lecture to a thin project-name summary.
- Recovered 61 distinct full-width teaching states from the official 1080p recording and registered every state as a required manifest node. The teacher-voice ledger preserves 18 spoken explanations spanning the active-kitten motivation, open-ended environments, learned reward, code-as-action, skill memory, automatic curriculum, reward reflection, internet-video supervision, multimodal prompting, and the closing capability boundary.
- Accepted `cs25/lecture20/lecture20-notes.pdf` at 54 pages with all 61 teaching figures referenced exactly once, 38 teaching boxes, 18 in-note teacher-voice markers, 9 displayed formula blocks, 3 captioned listings, and 23,915 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 392 prose characters per figure. Final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing the complete 54-page contact sheet and enlarged TOC, Mineflayer/Voyager, code, Eureka architecture/reward/dexterity, VIMA, final audit-table, and references pages. The QA pass compressed a sparse second TOC page and trailing references page before acceptance. CS25 V1--V5 rewrite progress is now 20/41; Lecture 21 is next.

## CS25 Lecture 21 source audit and acceptance
- Verified Stanford Online `1GbDTTK3aR4`, the CS25 V3 archive, the 2023-11-07 classroom boundary, 1,866 parsed official manual-caption cues, and the primary Transformer, Music Transformer, MQA/GQA, FlashAttention/online-softmax, tool-use, and long-context sources used for technical scaffolding. The legacy note fabricated a 2026 date and unsupported course URL and contained only a cover plus a thin summary.
- No public standalone slide deck was found. Three-second sampling of the official 1080p recording produced 1,613 samples; brightness filtering yielded 87 candidates, and manual review retained 43 distinct full-width teaching states while intentionally omitting repeated speaker windows, revisits, bumpers, and duplicate closing slides.
- Accepted `cs25/lecture21/lecture21-notes.pdf` at 48 pages with all 43 teaching figures referenced exactly once, 50 teaching boxes, 22 in-note teacher-voice markers, 15 displayed formula blocks, 3 captioned listings, and 25,143 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 584 prose characters per figure. Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing the full 48-page contact sheet and enlarged title/TOC, encoder--decoder attention, complexity, multi-head, position, Music Transformer, long-context, memory-hierarchy, MQA/GQA, online-softmax, research-direction, and reference pages. CS25 V1--V5 rewrite progress is now 21/41; Lecture 22 is next.

## CS25 Lecture 22 source audit and acceptance
- Verified the official CS25 V3 schedule entry for October 31, 2023, Stanford Online `mcep6W8oB1I`, the 1:08:49 1080p recording, and 1,431 parsed manual-caption cues. The legacy note had a blank video URL, no slide coverage, and presented unsupported universal hyperparameters instead of the lecture's distribution/evaluator experiments.
- Nazneen Rajani's site exposes `stanford_talk.pdf` (67 pages) and `transformers_united.pdf` (71 pages). The 67-page variant omits Zephyr/distillation and UN advisory slides that appear in the recording; frame comparison at 00:26:30--00:26:40 matches pages 30--31 of the 71-page deck exactly, making it the canonical classroom source.
- Accepted `cs25/lecture22/lecture22-notes.pdf` at 60 pages with all 66 required teaching slides referenced exactly once, five pure divider/closing pages intentionally optional, 72 teaching boxes, 23 in-note teacher-voice markers, 6 displayed formula blocks, 3 captioned listings, and 22,805 prose characters.
- Strict coverage is zero-warning and quality is `⭐⭐⭐` at 345 prose characters per figure. Stabilized final two-pass XeLaTeX has no layout/reference/rerun/hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed after reviewing the full 60-page contact sheet and enlarged source-audit, data-landscape, task/length table, preference pilot, code, formula, evaluation-stack, SFT/distillation result, GPT-4 judge, synthesis, and reference pages. The initial sparse tail page was removed before acceptance. CS25 V1--V5 rewrite progress is now 22/41; Lecture 23 is next.

## CS25 Lecture 24 source audit and acceptance
- Official classroom evidence is Stanford Online `ylEk1TE1uBo`, the CS25 V3 schedule, and 1,297 timed manual-caption cues for the November 28, 2023 instructors lecture. No standalone final classroom deck was found, so all 64 accepted visuals are deduplicated, cropped classroom frames with timestamp provenance.
- The legacy note was not merely thin; it replaced the actual lecture with unsupported prompt governance, SLI/SLO, drift monitoring, rollback, production data pipelines, observability, and deployment checklists. The rewrite removes those claims and restores the missing BabyLM, emergence-metric critique, structured reasoning, MultiOn demos, autonomy, memory, manager--worker correction, plan divergence, LLM OS, permissions, sandboxing, and irreversible-action safeguards.
- `Intermediate-Guided Reasoning` is preserved as the speaker's classroom umbrella term rather than presented as a standard field label. MultiOn flight, mobile, Action API, and driving-test material is explicitly separated into classroom footage, speaker capability claims, independently verified behavior, and deployment conclusions.
- The accepted systems synthesis treats a foundation model as a neural compute unit inside a larger feedback-controlled architecture. API interaction is safer and more controllable than direct keyboard/mouse operation; multi-agent parallelism requires structured communication and synchronization; coding agents benefit from compiler/IDE feedback; deployable agents require error correction, least privilege, confirmation gates, audit trails, recovery, and sandboxing.

## CS25 Lecture 25 source audit and acceptance
- The authoritative lecture is Stanford Online `mE7IDf2SmJg`, Douwe Kiela's “Retrieval Augmented Language Models” session from December 5, 2023. The 1:19:26 1080p recording and 1,795-cue official manual-caption track support a 959-line cleaned transcript and a 22-entry teacher-voice ledger.
- No public standalone classroom deck was found. Three-second video sampling produced 1,589 frames, 77 high-recall candidates, and 49 manually deduplicated teaching states using the stable `crop=1580:920:0:80` classroom-slide region.
- The legacy note contained unsupported dashboard, incident-runbook, observability, temperature-scheduling, gate-dropout, multimodal-drift, regional-governance, synthetic-query, and generic deployment material. The rewrite removes those inventions and restores the actual lecture sequence from retrieval motivation through RAG 2.0.
- The accepted note separates retrieval from evidence use: sparse, dense, late-interaction, and hybrid retrieval solve different matching problems; frozen retriever/generator combinations create a Frankenstein mismatch; joint systems such as RAG, REALM, Atlas, FiD, RETRO, Self-RAG, and active retrieval move optimization across different interfaces.
- Strict coverage has zero warnings and quality is `⭐⭐⭐`: 56 pages, 49 figures each referenced exactly once, 68 teaching boxes, 25 teacher-voice markers, 17 formula blocks, 3 captioned listings, and 23,845 prose characters. Two-pass XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, stranded headings, or malformed boxes.
- CS25 V1--V5 rewrite progress is now 25/41. Lecture 26 is next.

## CS25 Lecture 26 source audit and acceptance
- The canonical source is Stanford Online `fKMB5UlVY1E`, “Stanford CS25: V4 I Overview of Transformers,” taught on April 4, 2024 and uploaded April 23. The 1:17:28 recording has an official 1,795-cue `en-US` manual-caption track normalized into 891 transcript lines.
- The video description links the official 114-page Google Slides deck. The repository PDF and a fresh official export are byte-identical at SHA-256 `b16b112aa5b4b35a8b1ca221205e3bce24650a761609dc68b25edf2cb086091c`, closing the visual provenance chain without video-frame reconstruction.
- Ninety-one teaching pages are required. Administrative instructor/logistics pages, pure dividers, the closing card, and four redundant progressive communication builds are intentionally omitted with recorded reasons; all distinct teaching states remain represented.
- The legacy note was source-inaccurate, referencing only nine slides while fabricating dashboards, clinician override, compliance, incident response, rollback, synthetic replay, observer-agent monitoring, and regulator artifacts. The rewrite replaces it completely with the actual arc: NLP history, attention, emergence, RLHF/DPO, MoE, applications, BabyLM, memory/RAG, continual learning, model editing, reasoning, agent demos, autonomy, neural compute, multi-agent verification, plan divergence, LLM OS, permissions, and sandboxing.
- The accepted note is 83 pages with 91 figures each referenced exactly once, 90 teaching boxes, 22 teacher-voice markers, 28 formula blocks, 3 captioned listings, and 25,357 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐`, two-pass XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, stranded headings, malformed boxes, or raw-URL defects.
- CS25 V1--V5 rewrite progress is now 26/41. Lecture 27 is next.

## CS25 Lecture 27 source audit and acceptance

- The canonical source is the combined Stanford Online upload `3gb-ZkVRemQ`, “Stanford CS25: V4 I Jason Wei & Hyung Won Chung of OpenAI,” taught on April 11, 2024 and uploaded May 6. It supersedes the unavailable legacy video ID `5XkoZDxBSx0` and contains a 1,551-cue official manual-caption track.
- Jason Wei's official deck has 20 pages with SHA-256 `0eddcb8d5bf1a443777ac0a14afc658fa8477d20ef680f79c3bf30e5dbde10f9`; Hyung Won Chung's official deck has 67 pages with SHA-256 `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`.
- Sixty-six pages are required. The 21 omitted pages are limited to a closing contact card, pure divider, empty comparison scaffold, or redundant progressive builds whose final complete state is retained.
- The legacy note fabricated emergence dashboards, attention-entropy diagnostics, governance templates, prompt registries, rollback checklists, and other unsupported material. The rewrite restores the actual two-part lecture: next-token prediction as massive multi-task learning, scaling laws, emergence metrics, inverse/U-shaped scaling, dominant driving forces, the Bitter Lesson, three Transformer families, a four-step encoder-decoder to decoder-only transformation, FLAN length-distribution effects, representation granularity, bidirectionality, KV-cache reuse, and learning-objective caveats.
- The accepted note is 61 pages with 66 figures each referenced exactly once, 36 teaching boxes, 24 teacher-voice markers, 20 formula blocks, 4 captioned listings, and 19,201 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐`, two-pass XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, stranded headings, malformed boxes, or raw-URL defects.
- CS25 V1--V5 rewrite progress is now 27/41. Lecture 28 is next.

## CS25 Lecture 28 source audit and acceptance

- The canonical source is Stanford Online `AdLgPmcrXwQ`, “Stanford CS25: V4 I Aligning Open Language Models,” taught by Nathan Lambert on April 18, 2024 and uploaded May 10. The 1:16:21 recording includes a 1,693-cue official manual-caption track and links the official 77-page Google Slides deck plus Lambert's Hugging Face companion collection.
- The legacy lecture directory was materially contaminated: its `slides.pdf` was actually Lecture 27's 67-page Hyung Won Chung deck, byte-identical at SHA-256 `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`. The correct 77-page Nathan Lambert export is now installed and rendered at SHA-256 `3c3470dea235227cc43134b87106b8a913716b72bf8324edb8d0a34f79502268`.
- Sixty-seven official pages are required. Ten omissions are intentional and limited to pure chapter dividers, empty or superseded progressive builds, one QR-only atlas state, and the closing contact card.
- The replacement note teaches alignment as a data/evaluation/system history rather than a single algorithm: IFT/SFT/RLHF/DPO definitions, self-instruct and real-user prompt distributions, open human data, QLoRA accessibility, safety-value conflicts, four evaluation infrastructures, reward modeling and DPO mechanics, competing model releases, preference-data scarcity, and synthetic-data distribution risk.
- The accepted note is 57 pages with 67 figures each referenced exactly once, 30 teaching boxes, 30 teacher-voice markers, 14 formula blocks, 3 captioned listings, and 17,716 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐`, two-pass XeLaTeX has no overfull/reference/rerun/hyperref warnings, and signed visual QA found no rendering or layout defects.
- CS25 V1--V5 rewrite progress is now 28/41. Lecture 29 is next.

## CS25 Lecture 29 source audit and acceptance

- The canonical source is Stanford Online `RcJ1YXHLv5o`, “Stanford CS25: V4 I Demystifying Mixtral of Experts,” taught by Albert Jiang on April 25, 2024 and uploaded May 16. The 1:04:31 official 1920x1080 recording supplies automatic `en-orig` captions with 2,830 raw cues and 276 deduplicated timed segments.
- The legacy directory was materially contaminated: its 77-page `slides.pdf` was Nathan Lambert's Lecture 28 deck at SHA-256 `3c3470dea235227cc43134b87106b8a913716b72bf8324edb8d0a34f79502268`. Because neither the course page nor video description publishes a standalone Mixtral deck, the incorrect PDF and 77 rendered pages were removed and the visual spine was reconstructed from the verified official recording.
- One-second high-recall review covered 3,871 samples and 58 visual-change candidates. Manual contact-sheet inspection retained 26 independent teaching states; 17 omissions are intentional and limited to bumpers, pure dividers, the closing card, and superseded progressive builds. The Q\&A reuses existing slides, so its distinct value is preserved through teacher voice rather than duplicate figures.
- The replacement note separates total capacity, active compute, and system cost; explains GQA/SWA/RMSNorm/SwiGLU, top-two routing, parameter decomposition, performance evidence, four MoE myths, load balance, compression and offload, routing interpretability, domain/token experiments, community ablation, and the serving/training Q\&A.
- The accepted note is 38 pages with 26 figures each referenced exactly once, 37 teaching boxes, 31 teacher-voice markers, 26 formula blocks, 4 captioned listings, and 21,898 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 842 prose characters per figure, two-pass XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, stranded headings, malformed boxes, or raw-URL defects.
- CS25 V1--V5 rewrite progress is now 29/41. Lecture 30 is next.

## CS25 Lecture 30 source audit and acceptance

- The canonical source is Stanford Online `zL9B3eXq0gY`, “Stanford CS25: V4 I Transformers that Transform Well Enough to Support Near-Shallow Architectures,” taught by Jake Williams on May 2, 2024 and uploaded May 23. The 1:19:56 official 1920x1080 recording supplies 1,487 manual `en-US` caption cues and 634 deduplicated timed segments.
- The legacy note was materially contaminated: it used a fictitious 2026 date and nonexistent lecture URL, misspelled SAFFU, and invented drift gates, observability/fairness dashboards, governance teams, incident replay, newsletters, an RLHF governance roadmap, and rollback thresholds. None survived the source-first rewrite.
- No standalone slide deck was publicly linked, so the recording is the visual source of truth. A one-second audit over all 4,796 seconds produced 3,409 slide-like frames, 68 high-recall candidates, 29 unique visual states, and 27 required teaching states after excluding the Stanford bumper and closing contact card; Q\&A reused existing slides but added required spoken clarifications.
- The accepted note is 38 pages with all 27 required figures referenced exactly once, 44 teaching boxes, 34 teacher-voice markers, 28 formula blocks, 4 captioned listings, and 20,846 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 772 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, sparse tail pages, or reference defects.
- CS25 V1--V5 rewrite progress is now 30/41. Lecture 31 is next.

## CS25 Lecture 31 source audit and acceptance

- The canonical source is Stanford Online `cYfKQ6YG9Qo`, “Stanford CS25: V4 I From Large Language Models to Large Multimodal Models,” taught by Ming Ding on May 9, 2024 and uploaded May 30. The 4,803-second official 1920x1080 recording supplies manual `en-US` captions normalized into 983 readable timestamped segments.
- The legacy note used a fictitious 2026-04-04 date and replaced the actual visual spine with invented operations/governance material. The official course page and description link no standalone deck, so a full one-second recording audit produced 4,710 slide-like frames, 76 high-recall candidates, and 31 required teaching states after intentional deduplication.
- The replacement note treats the talk as a transfer of LLM lessons into multimodality: objective and scaling history; training-state/resource accounting; alignment and data; Q-Former/projection/vision-expert/high-resolution interfaces; benchmark evidence boundaries; autoregressive versus diffusion generation; video systems/data requirements; and dated research advice.
- The accepted note is 40 pages with all 31 required figures referenced exactly once, 36 teaching boxes, 26 teacher-voice markers, 26 formula blocks, 5 captioned listings, and 20,701 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 667 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 31/41. Lecture 32 is next.

## CS25 Lecture 32 source audit and acceptance

- The canonical source is Stanford Online `jm2hyJLFfN8`, “Stanford CS25: V4 I Behind the Scenes of LLM Pre-training: StarCoder Use Case,” taught by Loubna Ben Allal on May 23, 2024 and uploaded June 7. The 3,696-second official 1920x1080 recording supplies manual `en-US` captions; the speaker's official site publishes the canonical 71-page Google Slides deck.
- The legacy note was materially incomplete: it omitted the canonical recording URL, used only the video thumbnail, and missed the official deck plus the lecture's scaling, filter-ablation, data-governance, formatting, tooling, contamination, and negative-result evidence. The replacement source audit preserves 58 required teaching pages and explicitly classifies 13 non-teaching, duplicate, or superseded pages as optional.
- The replacement note separates compute-optimal training from lifecycle-optimal deployment, traces Common Crawl through FineWeb and The Stack, preserves the speaker's negative repository-star filtering result, derives MinHash/LSH near-deduplication and pass@k, and connects PII/decontamination, code metadata, FIM, mixtures, BigCode collaboration, responsible release, contamination-resistant evaluation, and Q\&A governance tradeoffs.
- The accepted note is 55 pages with all 58 required slides referenced exactly once, 43 teaching boxes, 27 teacher-voice markers, 13 formula blocks, 5 captioned listings, and 22,475 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 387 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, raw-URL defects, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 32/41. Lecture 33 is next.

## CS25 Lecture 33 source audit and acceptance

- The canonical source is official playlist item 33, Stanford Online `orDKvo8h71o`, “Stanford CS25: V4 I Hyung Won Chung of OpenAI,” a 36:30 standalone edit recorded April 11, 2024 and uploaded June 11. Its manual-caption track has 376 segments, and the official description links the 67-page `Shaping the Future of AI from the History of Transformer` deck.
- This item is a duplicate publication boundary, not a duplicate source error: the standalone edit contains the Hyung Won Chung talk from the second half of combined Lecture 27 upload `3gb-ZkVRemQ`. The deck exports are byte-identical, while video IDs, covers, captions, timestamps, runtime, playlist position, and audience entry points differ. The standalone excludes the later joint Q\&A, so the new note does too.
- The replacement note preserves 47 required pages and classifies 20 progressive/divider states as optional. It treats exponentially cheaper compute as a historical direction rather than a guaranteed law; separates current-regime efficiency from long-run scalability; derives the four architecture transformations one assumption at a time; and labels FLAN, layer-depth, and bidirectionality evidence at the speaker's actual confidence level.
- The accepted note is 41 pages with all 47 required figures referenced exactly once, 23 teaching boxes, 16 teacher-voice markers, 11 formula blocks, 3 captioned listings, and 12,585 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 267 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 33/41. Lecture 34 is next.

## CS25 Lecture 34 source audit and acceptance

- The canonical source is Stanford Online `JKbtWimlzAE`, “Stanford CS25: V5 I Overview of Transformers,” taught by Steven Feng, Karan Singh, Jenny Duan, and Chelsea Zou on April 1, 2025 and uploaded April 18. The 3,688-second official recording supplies manual captions, while the byte-verified official deck contains 123 pages.
- The legacy note was materially incomplete and partially incorrect: it omitted the canonical video, named presenters incorrectly, contained no slide figures or teacher voice, and skipped both data studies, reasoning taxonomy, modern preference methods, agents, fMRI, scaling limits, and continual learning. The replacement manifest preserves 100 teaching pages and explicitly marks 23 non-teaching or redundant pages optional.
- The accepted note explains each intervention by where it changes the system: representation/architecture, data distribution, inference-time computation, preference optimization, environment interaction, or deployment-time adaptation. It also separates slide evidence from stronger causal claims, especially for child-directed data, judge-based preference optimization, fMRI attention, scaling saturation, and purported continual learning.
- Final acceptance is 80 pages with all 100 required figures referenced exactly once, 42 teaching boxes, 25 teacher-voice markers, 22 formula blocks, 5 captioned listings, and 26,118 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 261 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, raw-URL defects, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 34/41. Lecture 35 is next.

## CS25 Lecture 35 source audit and acceptance

- The canonical source is Stanford Online `gLwiPrwUDJ8`, “RL as a Co-Design of Product and Research,” taught by Karina Nguyen on April 8, 2025 and uploaded April 29. No standalone public deck is linked, so the 1:12:10 official 1080p recording and its 1,325-cue manual-caption track define the source boundary.
- The legacy note had no visual teaching spine or preserved teacher voice, while its 3,135 subtitle cues were heavily duplicated. The replacement audit scanned all 4,330 seconds, retained 60 distinct teaching states from 208 candidates, and explicitly classified 148 progressive, repeated, administrative, speaker-only, or superseded states as optional.
- The rewritten lecture treats product research as a co-design problem across product belief, interface, eval, data, environment, reward, and deployment. It preserves the speaker's practical refusal taxonomy, product-vignette evidence, RL-environment contract, verifier blind spots, reward-hacking warnings, and Q\&A boundaries without promoting product demos into universal causal claims.
- Final acceptance is 56 pages with all 60 required figures referenced exactly once, 42 teaching boxes, 17 teacher-voice markers, 24 formula blocks, 6 captioned listings, and 20,268 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 337 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, raw-URL defects, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 35/41. Lecture 36 is next.

## CS25 Lecture 36 source audit and acceptance

- The canonical source is Stanford Online `nEHNwdrbfGA`, “The Advent of AGI, Div Garg,” taught on 2025-04-15 and uploaded on 2025-05-13. No standalone public deck is linked, so the full 1:01:01 official 1080p recording and its normalized 1,296-segment manual-caption transcript define the evidence boundary.
- The legacy lecture used a heavily duplicated 3,161-cue subtitle file and lacked exhaustive visual coverage. The replacement audit scanned every second of the slide-led portion without a brightness gate, classified 544 candidate states, retained 58 independent teaching states, and records 486 repeated, progressive, administrative, speaker-only, or superseded states as optional.
- The accepted note treats AGI as an engineering stack rather than a product prediction: goal, policy, environment, evaluation, learning, memory, coordination, and deployment. It separates REAL/AgentQ evidence from stronger autonomy claims, preserves Q\&A caveats and practical heuristics, and explicitly freezes product and benchmark claims at the April 2025 classroom boundary.
- Final acceptance is 51 pages with all 58 required figures referenced exactly once, 29 teaching boxes, 15 teacher-voice markers, 16 formula blocks, 5 captioned listings, and 15,174 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 261 prose characters per figure, double XeLaTeX is clean beyond Fandol notices, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, raw-URL defects, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 36/41. Missing Lecture 37 is next.

## CS25 Lecture 37 source audit and acceptance

- The canonical sources are Stanford Online `ebnX5Ur1hBk` and Denny Zhou's official `LLM-Reasoning-Stanford-CS-25.pdf`, both identifying the April 29, 2025 CS25 V5 lecture. The official deck has 49 pages; the recording is 1:06:07 at 1080p with 1,089 manual-caption segments.
- The missing local lecture was rebuilt source-first rather than inferred from neighboring numbering. Forty-eight deck pages contain independent teaching content; page 49 is only the closing card. A complete 30-second recording sample confirmed that no live demo or other visual source needs to supplement the deck.
- The accepted note treats reasoning as intermediate-token computation rather than human cognition. It distinguishes candidate existence from decoding, prompt context from parameter updates, model-generated rejection sampling from general RL, answer marginalization from path maximization, internal consistency from calibration, and retrieval quality from reasoning quality.
- Final acceptance is 45 pages with all 48 required figures referenced exactly once, 21 teaching boxes, 19 teacher-voice markers, 16 formula blocks, 5 captioned listings, and 15,942 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 332 prose characters per figure, double XeLaTeX is stable, and signed visual QA found no blank/cropped figures, overflow, orphan captions, malformed boxes, raw-URL defects, or sparse tail page.
- CS25 V1--V5 rewrite progress is now 37/41. Lecture 38 is next; local V1--V5 source coverage is now 41/41 directories.

## CS25 Lecture 38 source audit and acceptance

- The canonical sources are Stanford Online `vRQs7qfIDaU`, the CS25 V5 schedule row dated 2025-05-13, and Anthropic's interactive `On the Biology of a Large Language Model` article. The 1:12:32 official recording is the visual spine because the course links no standalone public deck; it exposes 1,581 manual-caption cues, normalized into 1,527 timed segments.
- The legacy lecture had only one figure, roughly six pages, no canonical video URL, no source manifest, no teacher-voice ledger, and an 18,675-line rolling-caption artifact. A full one-second audit classified 357 candidate states, retaining 62 independent teaching visuals and documenting 295 intentional omissions.
- The strongest methodological boundary is that the Cross-Layer Transcoder replacement model reconstructs MLP computation while reusing, not explaining, base-model attention. Attribution graphs are prompt-local approximations with reconstruction error and success-case bias; original-model interventions strengthen causal claims but do not make labels unique or graphs globally complete.
- The accepted note teaches three model findings—abstract representations, parallel computation, and planning—through Dallas-to-Austin tracing, medical reasoning, multilingual interventions, parallel addition, IDK inhibition, jailbreak competition, rhyme planning, and chain-of-thought unfaithfulness. It keeps the Q\&A caveats on attention-mediated strategy selection, reflection, adaptive compute, calibration, and the ambiguity of hallucination labels.
- Final acceptance is 48 pages with 62 figures, 21 teaching boxes, 10 in-note teacher-voice markers from an 18-row ledger, 7 formula blocks, 4 captioned listings, and 16,178 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 260 prose characters per figure, double XeLaTeX is stable, and signed visual QA inspected the full contact sheet plus pages 7, 16, 31, 43, and 48.
- CS25 V1--V5 rewrite progress is now 38/41. Lecture 39 is next.

## CS25 Lecture 39 source audit and acceptance

- Canonical source is Stanford Online `8kXIaUM3h1E`, the 2025-05-20 CS25 V5 talk “Multimodal World Models for Drug Discovery” by Eshed Margalit of Noetik.ai, uploaded 2025-06-13. Runtime is 1:11:02, not 1:20:36; the course page and video description provide no standalone public slide deck.
- Fresh manual captions contain 1,643 cues and normalize to 1,622 non-empty timed segments, replacing the legacy 3,771-cue rolling subtitle dump. The old note has no canonical video URL and only one figure, so it requires full replacement.
- The exhaustive one-second visual audit scanned all 4,262 seconds and produced 441 high-recall candidates. Review of all OCR rows and 28 contact sheets retained 60 independent microscopy, spatial-omics, tumor-architecture, multimodal-fusion, world-model, patient-cohort, and counterfactual states; 381 cursor, animation, speaker-only, repeated, progressive, or transition states are documented as optional.
- The central organizing distinction is translation versus disambiguation. H\&E-to-gene imputation is a translation problem with an identifiability ceiling, while spatial-neighborhood conditioning is disambiguation. Contrastive alignment, direct concatenation, cross-attention, bonus tokens, and adaptive LayerNorm are composable mechanisms rather than mutually exclusive architecture families.
- The strongest evidence boundary is that virtual-cell and gene-knockout outputs are model counterfactuals, not causal biological effects. Patient-level sample size, non-random absence of healthy tissue, calibration, held-out-patient evaluation, real perturbation data, and wet-lab closure are mandatory before clinical claims.
- Final acceptance is 51 pages with 60 figures, 25 teaching boxes, 13 in-note teacher-voice markers from a 24-row ledger, 13 formula blocks, 4 captioned listings, and 17,532 prose characters. Strict coverage has zero warnings, quality is `⭐⭐⭐` at 292 prose characters per figure, stabilized double XeLaTeX is clean beyond standard Fandol notices and harmless terminology-table underfulls, and signed visual QA inspected the full contact sheet plus pages 15, 26, 49, 50, and 51 after fixing the initial sparse tail and split Q\&A box.
- CS25 V1--V5 rewrite progress is now 39/41. Lecture 40 is next.

## CS25 Lecture 40 source audit and acceptance

- Canonical visuals come from Sayak Paul's official 66-page Diffusion Transformers deck; pages 04--65 are 62 independent teaching pages, while title, administration, and closing-contact pages are intentional optional nodes. The 1:14:32 official recording contributes required teacher voice, especially architecture/evaluation Q\&A absent from the slide text.
- The note is complete only when DiT is presented as a systems design sequence rather than a model-name list: transport objective, latent representation, tokenization/patching, conditioning, attention cost, modality interaction, parameter sharing, control interfaces, video extension, and evaluation evidence.
- Final acceptance is 49 pages with 62 figures, 20 teaching boxes, 12 teacher-voice markers, 12 formula blocks, 4 captioned listings, and 17,316 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 279 prose characters per figure, double XeLaTeX is stable, and visual QA is signed.

## CS25 Lecture 41 source audit and acceptance

- No standalone public deck is linked for Andrew Brown's Movie Gen lecture, so the complete official recording is the visual spine. A no-brightness-gate one-second scan yielded 780 candidates; 32 independent teaching/evidence states are required and 748 administrative, speaker-only, repeated, progressive, loading, transition, or embedded-video micro-states are documented as optional.
- The key systems dependency chain is representation → transport objective → backbone/conditioning → context parallelism → data/curriculum → task-specific post-training → evaluation. Treating Movie Gen as one undifferentiated model hides that editing, personalization, and synchronized audio use distinct conditioning and training paths.
- The strongest evidence boundary is that human Net Win Rate, short-video scaling, and polished demonstrations do not establish reliable long-horizon interaction or physical reasoning. The full Q\&A therefore remains required teacher voice even without new visual states.
- Final acceptance is 37 pages with 32 figures, 27 teaching boxes, 15 teacher-voice markers, 17 formula blocks, 3 captioned listings, and 15,067 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 470 prose characters per figure, double XeLaTeX is stable, and visual QA is signed after correcting two initially mis-captured demo frames.
- CS25 V1--V5 is complete at 41/41; the official 9-lecture V6 series is the next active scope.

## CS25 V6 Lecture 01 source audit and acceptance

- The live 2026 course schedule and the 50-item official playlist agree on a nine-lecture V6 scope, but playlist upload order is not classroom chronology. `cs25-v6/COURSE_SCOPE.md` records the canonical date/title/speaker/video/slide mapping and flags the course page's duplicate Lecture 04/05 Drive link for later independent verification.
- Lecture 01's official deck has 156 pages. The source-complete policy retains 116 independent teaching pages; the 40 optional pages are limited to biographies/logistics, pure dividers, paper-title/QR pages without mechanisms, repeated research-question cards, progressive states superseded by complete pages, and the closing card.
- The full-recording audit found no deck-external teaching visual. The lecture's real additional value is teacher voice: it distinguishes self-supervised objectives, small-data evidence boundaries, RAG compute allocation, curriculum/model co-scaling, preference methods, agent loops, fMRI evidence, hallucination as a world-model error, true continual learning, alignment channels, JEPA, and SSM tradeoffs.
- Final acceptance is 90 pages with 116 figures, 42 teaching boxes, 32 teacher-voice markers, 30 formula blocks, 6 captioned listings, and 30,192 prose characters. Strict coverage is zero-warning, quality is `⭐⭐⭐` at 260 prose characters per figure, double XeLaTeX is stable, and visual QA is signed with no crop, overflow, orphan, URL, or sparse-tail defect.
- CS25 V6 is 1/9 complete; Lecture 02 JEPA/world modeling is the next active target.

## CS25 V6 Lecture 02 source audit and acceptance

- Verified Stanford Online `GBd7iuJkW08`, the live 2026 course row, the 55-page official deck, and 1,371-cue manual `en-US` captions. The classroom introduction resolves the speaker-name ambiguity as Heejeong “Hazel” Nam and Lucas Maes; Lucas is identified with Mila and Université de Montréal rather than the course row's shorthand Brown affiliation.
- Preserved the 2026-04-09 lecture snapshot by using Causal-JEPA `2602.11389v1` and LeWorldModel `2603.19312v1`; post-lecture Causal-JEPA v2 and LeWorldModel v3 wording is not projected backward into the class.
- Reviewed all 55 deck pages, retaining 47 independent teaching pages and marking 8 cover, agenda, title/credit, divider, or closing pages optional. The five-second full-recording audit produced 853 samples and 198 high-recall candidates; one independent deck-external question card at 00:31:25 is required.
- The note reconstructs the world-model contract, JEPA energy view, Slot Attention, permutation and identity anchoring, Causal-JEPA masked-history/future objective, action-node conditioning, CLEVRER/Push-T/PHYRE evidence, influence-neighborhood assumptions, LeWorldModel's MSE + SIGReg objective, latent MPC, probes, surprise tests, limitations, tooling, and the complete substantive Q\&A.
- Final acceptance: 51 pages, all 48 required figures referenced exactly once, 35 teaching boxes, 27 teacher-voice markers synthesized from a 35-row ledger, 19 formula blocks, 4 captioned listings, and 22,603 prose characters (470 per figure). Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no overfull or underfull boxes, and signed visual QA passed after replacing an inaccurate fast-seek speaker frame with the exact classroom question card.
- CS25 V6 is now 2/9 complete; Lecture 03 `SSM vs Transformers` is the next active target.
## 2026-08-12 — CS25 V6 Lecture 03 source boundary

- The latest public `wdkns/wdkns-skills` HEAD remains `39f1a04c46e1d0d70f6b71a8fcf079b305a632b9`; Lecture 03 continues under the same reconciled upstream-plus-repository standard used for Lectures 01–02.
- Stanford's official CS25 V6 schedule identifies the 2026-04-16 talk as `On the Tradeoffs of State Space Models and Transformers`, speaker Albert Gu (CMU, Cartesia AI).
- The official YouTube recording is `OyimE74UMF8`, duration 01:17:07, published by Stanford Online on 2026-04-27.

## 2026-08-12 — CS25 V6 Lecture 03 acceptance findings

- Stanford publishes no public deck link for this lecture, so the complete visual spine is reconstructed from the official recording: 33 frozen slide states, 32 required teaching states, and one optional title card represented by the cover metadata.
- The Albert Gu teaching segment ends around 01:06:35; the MongoDB sponsor segment beginning around 01:06:30 is intentionally excluded from lecture coverage.
- The lecture-date paper snapshot is stable: Mamba-3 remains arXiv `2603.15569v1` from 2026-03-16, H-Net remains `2507.07955v2` from 2025-07-15, and dnaHNet remains `2602.10603v3` from 2026-04-09.
- Final note statistics are 40 pages, 32 required figures exactly once, 34 teaching boxes, 16 teacher-voice markers, 13 formula blocks, 5 captioned listings, and 21,059 prose characters, or roughly 658 prose characters per required figure.
- Full-size review confirmed that the model comparison table, projector-derived states, H-Net architecture/code, scaling curves, formulas, and final tradeoff table are readable and uncropped.

## 2026-08-12 — CS25 V6 Lecture 04 acceptance findings

- Verified Stanford Online `I5BKi32IEa8`, class date 2026-04-23, upload date 2026-05-11, 61:48 runtime, 1920x1080 recording, 1,101-cue manual `en-US` captions, and the official 106-page deck linked by the live course row.
- Classified all deck pages before prose: 75 independent teaching states are required and 31 title/divider/link/thank-you or superseded progressive-build pages are optional.
- Audited 742 five-second samples across the complete recording. No independent deck-external teaching visual appears; the video contributes a 34-row teacher-voice ledger and substantive Q&A on MoE load balance, mathematical equivalence, input pipelines, and topology-aware layout.
- Final note is 56 pages with all 75 required figures exactly once, 25 teaching boxes, 12 teacher-voice markers, 11 formula blocks, 4 captioned listings, and 19,514 prose characters (260 per figure).
- The note teaches DP/collectives/overlap, ZeRO-1/2/3 and FSDP2, TP/SP matrix decomposition, PP schedules, CP/Ring Attention, EP/all-to-all/hardware constraints, and five-axis device-mesh selection.
- Visual QA caught and removed a near-blank second TOC spill page; final 56-page rendering has no near-blank page, overfull/underfull box, cropped figure, or unreadable dense table/code page.

## 2026-08-12 — CS25 V6 Lecture 05 acceptance findings

- The live Stanford course row incorrectly reuses Lecture 04 Google Drive file `1dxdC76Rk_o6UEd5AqhHjp0rapsxYOR6j`; direct inspection confirmed it is the 106-page Ultra-Scale deck, so Lecture 05 uses no public deck and reconstructs its visual spine from Stanford Online `e_H_tkpCAK4`.
- The full 57:56 recording was sampled every five seconds into 695 frames and 12 timeline sheets. All sheets were reviewed; 69 bright slide runs were reconciled into 44 independent states: 41 required teaching visuals and three optional title/divider cards.
- Lecture-snapshot primary sources are two-phase pretraining `2412.15285v1`, front-loading reasoning `2510.03264v1`, and RLP `2510.01265v2` from 2026-03-01; Quiet-STaR, RPT, and RLPT provide the early-reasoning comparison boundary.
- The note covers blend weights versus curriculum, quality and epoch estimation, diversity-first/quality-later two-phase training, five front-loading lessons, thought policy, no-think counterfactual, information-gain reward, dense group-relative advantage, EMA stability, token/FLOP/checkpoint matching, RPT comparison, and implementation/Q&A boundaries.
- Final acceptance: 46 pages, all 41 required figures exactly once, 35 teaching boxes, 10 in-note teacher-voice markers from a 49-row ledger, 11 formula blocks, 5 captioned listings, and 19,358 prose characters (472 per figure).
- Strict coverage has zero warnings, quality is `⭐⭐⭐`, stable double XeLaTeX has no overfull or underfull boxes, and signed visual QA reviewed the complete contact sheet plus full-size opening, two-phase, front-loading, RLP mechanism/code, RPT comparison, synthesis, and final pages.

## 2026-08-12 — CS25 V6 Lecture 06 source and acceptance findings

- The official Lecture 06 deck is Google Drive file `1-YIOa5Yal4RCjAsV-0tnW_NNDGbY1GTo`, a valid 50-page PDF. The full 01:12:30 recording was sampled every five seconds into 870 frames and 15 contact sheets; no deck-external whiteboard, demo, question card, or teaching diagram appears.
- Forty-five pages are required. The five intentional omissions are the title card, three pure numbered section dividers, and the closing contact slide.
- The lecture-date paper snapshot is controlled generalization `2505.00661v3`, Latent Learning `2509.16189v3`, test-time compute `2604.01430v1`, Reversal Curse `2309.12288v4`, and the two cited ICL/gradient-descent papers at their pre-lecture latest versions.
- Final acceptance is 47 pages with 45 required figures exactly once, 32 teaching boxes, 14 in-note teacher-voice markers from a 33-row ledger, 12 formula blocks, 5 captioned listings, and 17,318 prose characters.
- Strict coverage has zero warnings, quality is `⭐⭐⭐` at 384 prose characters per figure, stabilized double XeLaTeX has no overfull or underfull boxes, and signed visual QA inspected the complete contact sheet plus pages 1, 3, 15, 28, 42, and 47 at full size.
- Unlike Lectures 01–02, the official course row exposes no slide-deck link. The source plan is therefore: recover the full teaching slide sequence from the recording, preserve spoken explanation through a teacher-voice ledger, and use Albert Gu's official Goomba Lab article plus primary papers only as supplementary conceptual/provenance sources.
- Because the video visibly uses slides, the slide-complete requirement still applies: every distinct teaching slide state must be captured, selected, inserted exactly once, and explained; progressive reveals may be collapsed only when the final state preserves the teaching content.

### Initial full-recording visual audit

- The Albert Gu segment runs from the opening through approximately 01:06:35; the MongoDB sponsor presentation and startup promotion after that boundary are non-course advertising and are excluded from the lecture note.
- Two-second sampling over the complete Albert segment produced 1,999 frames. A high-recall Pillow/NumPy/SciPy pass classified 1,053 clean direct-slide frames, 830 projector-region frames, and 116 camera/fallback frames.
- The first direct-feed pass retained 60 stable states. These include many progressive builds rather than 60 independent slides; examples are the repeated `Recap: Attention Inference`, `Key Ingredients of SSMs`, `H-Net`, and `Dynamic Chunking Scales Better` states.
- The clean-feed sequence already establishes the major teaching spine: resurgence of recurrent/linear models; autoregressive inference and KV-cache cost; SSM state size/update/efficiency; autoregressive states as a common language; compression/retrieval tradeoffs; attention's dependence on pre-compressed/tokenized inputs; tokenizer-free modeling; effective tokens; H-Net; dynamic chunking; and the final SSM tradeoff summary.
- The main unresolved visual gap is the camera-dominant interval around 00:30–00:37, plus shorter camera intervals elsewhere. These must be checked against normalized projector crops so no teaching slide is omitted merely because the broadcast did not switch to the clean feed.

## 2026-08-13 — CS25 V6 Lecture 07 source and acceptance findings

- The official source is Stanford Online `jFdH7n6BAl0`, taught by Vivek Natarajan on 2026-05-14 and uploaded on 2026-05-27. The course page links no independent deck, so the clean slide feed in the 01:06:32 recording is the visual source of record.
- The full recording was sampled every two seconds into 1,996 frames and 34 contact sheets. Twenty-three teaching states are required exactly once; the title card, a press-coverage slide, and an unrecorded AMIE transition card are optional. The architecture sequence is collapsed to its complete final state, while the two pedagogically distinct `Task vs Timescale` states are retained.
- The video description promises AI co-scientist and AMIE, but the recording moves from AI co-scientist directly into Q&A. This mismatch is recorded in metadata and coverage, and the note does not invent an AMIE section.
- Classroom-date evidence is frozen to AI co-scientist arXiv `2502.18864v1`, AMR bioRxiv `2025.02.19.639094v1`, liver fibrosis bioRxiv `2025.04.29.651320v1`, and plant assemblies bioRxiv `2026.05.03.722499v1`. AI co-scientist v2 from 2026-06-29 and later publication outcomes are excluded from lecture-time claims.
- Evidence levels remain separate: AML cell-line assays, liver organoids, AlphaFold plausibility screens, expert emails, and unpublished classroom results are not presented as equivalent validation. Rejuvenation, Alzheimer ACE--B2R, and SCLC inverse-comorbidity examples retain explicit unpublished or informal-validation boundaries.
- Final acceptance is 38 pages with 23 required figures exactly once, 57 teaching boxes, 20 teacher-voice markers, 12 formula blocks, 6 captioned listings, and 19,991 prose characters, or 869 prose characters per required figure.
- Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no overfull or underfull boxes, and the signed visual QA confirms no blank/cropped figures, margin spills, orphan captions, malformed boxes, or mostly empty pages.

## 2026-08-13 — CS25 V6 Lecture 08 source and acceptance findings

- The canonical sources are Stanford Online `NDdc39KYqDU`, Victoria Lin's official 56-page deck `10Doblrt3Le_FpbVQoMP0DbuCIO3rtWPW`, and 1,178 parsed manual-caption segments. The talk runs 01:04:39, with prepared material ending at 00:41:39 and substantive Q&A continuing to 01:04:31.
- A complete five-second visual audit produced 776 frames and 13 contact sheets. The recording uses clean full-screen deck pages during the talk and a camera view during Q&A; no independent whiteboard, live demo, question card, or external diagram appears.
- Thirty-seven pages are required exactly once and 19 are intentional optional nodes. Pages 2--4, 9, 16--18, 20, 34--38, and 49--50 are progressive builds; page 1 is the title card; pages 53--55 are Interaction Models appendix pages that the recording never presents.
- The lecture-date source snapshot uses Chameleon `2405.09818v2`, VQ-VAE-2 `1906.00446v1`, Transfusion `2408.11039v1`, Mind the Gap `2203.02053v2`, MoT `2411.04996v2`, LMFusion `2412.15188v4`, BAGEL `2505.14683v3`, and π0.7 `2604.15483v2`; every version predates the 2026-05-21 classroom date.
- The note separates multimodal input from multimodal output, discrete tokens from continuous token-like vectors, sequence-level autoregression from diffusion time, deterministic modality routing from learned MoE gating, and digital multimodal processing from physical-world intelligence.
- Evidence boundaries are explicit: modality-gap plots do not prove causality; lower diffusion loss does not establish understanding, safety, or physical competence; MoT's discussed specialization helps image generation but not image understanding; language is a current reasoning scaffold rather than a proven universal requirement.
- Final acceptance is 45 pages with 37 required figures exactly once, 62 teaching boxes, 16 teacher-voice markers from a 38-row ledger, 17 formula blocks, 6 captioned listings, and 25,986 prose characters, or 702 per figure.
- Strict coverage has zero warnings, quality is `⭐⭐⭐`, stabilized double XeLaTeX has no layout warnings, and signed visual QA confirms readable figures/tables/code, valid page breaks, no raw-URL overflow, and no blank tail page.

## 2026-08-13 — CS25 V6 Lecture 09 and full V6 batch accepted

- Verified Stanford Online recording `ZUdIsRZhWXI`, the 73-page official Google Drive deck, `en-US` subtitles, 1920×1080/60 fps media, class date 2026-05-28, and upload date 2026-06-04.
- Audited the complete 01:22:31 recording at five-second resolution: 990 samples across 17 contact sheets. The only deck-external teaching visual is the live token-timing simulator; no independent whiteboard or unrepresented live coding appears.
- Froze 57 required deck pages, one required live-demo frame, and 16 intentional optional pages. Pages 070, 072, and 073 are not reconstructed as taught content because they are respectively a transition joke, an unpresented CI/CL appendix, and recruiting material.
- Built sanitized metadata, source manifest, selection table, 38-row teacher-voice ledger, blueprint, coverage matrix, and a 59-page production-inference lecture covering workload/SLO design, replica benchmarking, model/engine choice, roofline and GPU hierarchy, serverless allocation, observability/evals, speculative decoding, quantization, host/kernel profiling, and agentic serving.
- Final acceptance: 58 required visual assets exactly once, 71 teaching boxes, 12 formula blocks, 7 captioned listings, and 23,900 prose characters under the repository checker. Strict coverage is zero-warning, quality is `⭐⭐⭐`, stable double XeLaTeX has no layout/reference warnings, and signed visual QA reviewed all 59 pages.
- CS25 V6 is complete at 9/9: 472 pages, 474 teaching figures, and 393 teaching boxes. README/tracking totals now reflect 368 source notes and 169 Stanford notes.
# Agentic AI MOOC Fall 2025 completion note

- As of 2026-08-18, the public course root and official repository expose Fall 2025 as the latest course edition; no public 2026 edition was found.
- The canonical scope is 12 teaching lectures; Thanksgiving week is not a lecture.
- The local legacy tree was reverse-ordered and missing the 2025-10-06 evaluation lecture. It is now organized as `lecture01` through `lecture12`.
- Final accepted batch: 497 pages, 472 teaching visuals, 589 teaching boxes; all 12 pass strict coverage, `⭐⭐⭐`, double XeLaTeX, signed visual QA, and artifact checks.
