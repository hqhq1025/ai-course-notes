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

## CS336 2026 Lecture 08 Working Notes
- `cs336-2026/lecture08/lecture08-slides.pdf` is an official 73-page slide deck titled "Parallelism Basics".
- `pdftotext` is unavailable and installing `poppler-utils` via `sudo apt-get` is blocked by an interactive password prompt; existing `mutool` successfully extracted per-page text to `/tmp/lecture08-text-*.txt` and rendered all 73 slide images under `cs336-2026/lecture08/slides-images/`.
- Lecture08 structure: Part 1 networking for LLMs; Part 2 standard LLM parallelization primitives; Part 3 scaling and training big LMs with parallelism.
- Main topics: single-GPU compute/memory limits; collective communication and all-reduce vs reduce-scatter + all-gather; TPU/GPU network topology tradeoffs; naïve data parallelism; ZeRO stages 1/2/3 and FSDP; pipeline parallelism, bubbles, microbatches, zero-bubble ideas; tensor parallelism along width with row/column splits; activation memory and sequence parallelism; expert parallelism and MoE routing; context/ring attention; 3D/4D parallelism recipes; recent model parallelism examples including DeepSeek, Yi, Llama 3 405B, Gemma 2, Mixtral, Nemotron, and Qwen 3.
- `cs336-2026/lecture08/lecture08-notes.pdf`: generated as a Spring 2026 long-form Parallelism Basics note, 41 pages by quality script, 51 embedded figures, 23 teaching boxes, and 0 code listings. It emphasizes memory/communication accounting, ZeRO/FSDP state sharding, pipeline bubbles, tensor/sequence/expert/context parallelism, 3D/4D placement rules, and recent large-model parallelism configurations.

## CS336 2026 Lecture 09 Working Notes
- `cs336-2026/lecture09/lecture09-slides.pdf` is an official 57-page slide deck titled "Scaling Laws - Basics".
- With `poppler-utils` installed, `pdfinfo` confirms 57 pages and `pdftotext -layout` extracted page text to `/tmp/lecture09-all.txt` and `/tmp/lecture09-pages/page-*.txt`.
- `mutool draw` rendered all 57 slide images under `cs336-2026/lecture09/slides-images/`.
- Lecture09 structure: motivation for taking scaling seriously; history/background of data scaling laws; neural/LLM scaling behaviors; data scaling and its theory; data mixture, distribution shift, and repetition; model-engineering scaling laws; architecture/optimizer/depth-width/batch/LR hyperparameters; joint data-model scaling laws; Kaplan vs Chinchilla compute-optimal tradeoffs; Chinchilla fitting methods; train-optimal vs deployment-aware overtraining; IsoFLOPS beyond LMs; final scaling law recap.
- `cs336-2026/lecture09/lecture09-notes.pdf`: generated as a Spring 2026 long-form Scaling Laws Basics note, 36 pages by quality script, 44 embedded figures, 23 teaching boxes, and 3 code listings. It emphasizes scaling laws as engineering forecasting tools, data scaling theory and pitfalls, hyperparameter/architecture scaling, critical batch size, muP, joint data-model scaling, Kaplan vs Chinchilla fitting methodology, and train-optimal vs deployment-optimal tradeoffs.

## CS336 2026 Lecture 10 Working Notes
- `cs336-2026/lecture10/lecture10-slides.py` is an official 611-line executable Python source lecture titled "Lecture 10: inference"; local execution is not required because the source contains the teaching text, formulas, and asset references.
- Main lecture structure: inference use cases and metrics; Transformer notation and arithmetic intensity; naive autoregressive inference vs KV cache; prefill/generation memory and compute accounting; latency/throughput/KV-cache model; lossy shortcuts including GQA, MLA, CLA, local/hybrid attention, DeepSeek v4 attention, quantization, pruning and distillation; lossless speculative sampling; dynamic serving with continuous batching, selective batching, and PagedAttention.
- Downloaded 28 original lecture/image assets into `cs336-2026/lecture10/images/` from the official CS336 image repository and referenced remote sources, then converted the two WebP Scaling Book diagrams into PNG for XeLaTeX compatibility.
- Existing `cs336/lecture10/lecture10-notes.tex` is useful as a cross-check, but the 2026 note should be freshly structured around the official Spring 2026 source and should emphasize inference as a memory-traffic and serving-systems problem, not just an algorithm list.
- `cs336-2026/lecture10/lecture10-notes.pdf`: generated as a Spring 2026 long-form Inference note, 30 pages by quality script, 29 embedded figures, 41 teaching boxes, and 5 code listings. It emphasizes inference as a memory-bandwidth/KV-cache/serving-systems problem, with detailed derivations for arithmetic intensity, KV cache size, latency-throughput tradeoffs, lossy KV compression, exact speculative sampling, continuous batching, and PagedAttention.
