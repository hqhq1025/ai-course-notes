# Findings

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
