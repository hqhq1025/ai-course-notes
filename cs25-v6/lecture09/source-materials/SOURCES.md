# Lecture 09 Source Materials

## Canonical course sources

- Stanford CS25 course page: `https://web.stanford.edu/class/cs25/`
- Official Stanford Online recording: `https://www.youtube.com/watch?v=ZUdIsRZhWXI`
- Class date: 2026-05-28; upload date: 2026-06-04.
- Speaker: Charles Frye, Modal.
- Official deck: Google Drive file `1mwRSslwZUCph1Au-9tY3ZJPrjXTnbAxm`, 73 pages.
- Captions: YouTube `en-US` subtitle track retained as `lecture09.en.srt`.

## Lecture-date primary references

- vLLM / PagedAttention: Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention*, arXiv `2309.06180`, SOSP 2023.
- Orca / iteration-level scheduling: Yu et al., *Orca: A Distributed Serving System for Transformer-Based Generative Models*, OSDI 2022, `https://www.usenix.org/conference/osdi22/presentation/yu`.
- SGLang / RadixAttention: Zheng et al., *SGLang: Efficient Execution of Structured Language Model Programs*, arXiv `2312.07104`.
- FlashAttention-2: Dao, *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning*, arXiv `2307.08691`.
- FlashInfer: Ye et al., *FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving*, arXiv `2501.01005`, MLSys 2025.
- Lossless speculative decoding: Leviathan et al., *Fast Inference from Transformers via Speculative Decoding*, arXiv `2211.17192`.
- EAGLE: Li et al., *EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty*, arXiv `2401.15077`.
- DFlash: Chen, Liang, and Liu, *DFlash: Block Diffusion for Flash Speculative Decoding*, arXiv `2602.06036`. Only claims public by the class date are used.
- FP8 formats: Micikevicius et al., *FP8 Formats for Deep Learning*, arXiv `2209.05433`.
- VibeServe: Kamahori et al., *Can AI Agents Build Bespoke LLM Serving Systems?*, arXiv `2605.06068`, public before the class date.
- NVIDIA CUDA Graph documentation: `https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-graphs`.
- NVIDIA Nsight Systems documentation: `https://docs.nvidia.com/nsight-systems/`.
- NVIDIA Nsight Compute documentation: `https://docs.nvidia.com/nsight-compute/`.

## Speaker-linked engineering sources

- LLM Engineer's Almanac workload advisor: `https://modal.com/llm-almanac/advisor`.
- Token timing simulator: `https://modal.com/llm-almanac/token-timing-simulator`.
- Workload archetypes: `https://modal.com/llm-almanac/workloads`.
- GPU glossary and arithmetic intensity: `https://modal.com/gpu-glossary/readme` and `https://modal.com/gpu-glossary/perf/arithmetic-intensity`.
- GPU fleet health: `https://modal.com/blog/gpu-health`.
- Serverless GPU allocation and startup: `https://modal.com/blog/truly-serverless-gpus`.
- Host overhead: `https://modal.com/blog/host-overhead-inference-efficiency`.
- Python host-side optimization case study: `https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary`.
- FlashAttention-4 engineering article referenced by the deck: `https://www.together.ai/blog/flashattention-4`.

## Local artifacts

- `lecture09-slides.pdf` and `slides-images/` preserve all 73 official deck pages.
- `lecture09.en.srt` preserves the English subtitle track with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture09-selection.tsv` freezes 58 required visuals and 16 optional deck nodes.
- `lecture09-teacher-voice-ledger.md` maps 38 spoken engineering lessons into the note.
- `lecture09-blueprint.md` and `lecture09-coverage.md` freeze the teaching order before prose generation.
- `images/token-timing-demo-002207.jpg` is the only required deck-external frame.

## Full-recording visual audit

- The complete 01:22:31 recording was sampled every five seconds.
- 990 frames were reviewed across 17 complete contact sheets.
- The live token-timing simulator is the only independent teaching visual outside the deck.
- No independent whiteboard, question card, or unrepresented live coding/demo appears.
- Deck pages 070, 072, and 073 are not treated as classroom teaching content: page 070 is a transition joke, page 072 was not reached in the recording, and page 073 is recruiting material.

## Evidence boundaries

- Market price/capability charts are snapshots and depend on provider methodology, traffic mix, and utilization.
- The GPU failure-rate table reflects the cited production context, not a universal H100 annualized failure guarantee.
- Speedup claims for speculative decoding, quantization, host optimization, and kernels depend on model, hardware, batch, sequence lengths, scheduler, and baseline.
- Quantization and intentionally lossy optimization require application-level evals; no format or technique is universally quality-preserving.
- Future hardware, megakernel, and agent-built-engine claims are forecasts or research directions rather than deployment guarantees.
