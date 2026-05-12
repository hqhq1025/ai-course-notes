# Lecture 10 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source: `lecture10-slides.py`, official executable lecture source. The rewritten note follows source clusters rather than a PDF slide deck.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture10-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture10/lecture10-notes.tex` reports `21p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture10/lecture10-notes.tex --manifest cs336-2026/lecture10/lecture10-manifest.md` reports `figs=29 readfig=23 boxes=34 term_digest=4 formulas=3 code=0 summaries=4` with no hard errors or warnings.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture10-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| main overview | source cluster | yes | Lecture 10: inference 的总图 | schema figure, workload/lossy/lossless/dynamic structure | complete |
| landscape and metrics | source cluster | yes | Understanding the inference workload | TTFT/latency/throughput terminology digestion | complete |
| Transformer and arithmetic intensity | source cluster | yes | Understanding the inference workload | diagram, formulas, HBM/memory-bound explanation | complete |
| naive/cached inference and KV cache | source cluster | yes | Understanding the inference workload | both inference diagrams, KV formula, prefill/generation distinction | complete |
| GQA/MLA/CLA/local/DeepSeek attention | source cluster | yes | Taking shortcuts (lossy) | all local figures, quality caveats, terminology boxes | complete |
| quantization/AWQ/pruning/distillation | source cluster | yes | Taking shortcuts (lossy) | precision figure, AWQ, pruning/KD loop and results | complete |
| speculative sampling | source cluster | yes | Use shortcuts but double check | algorithm/results/stats/Medusa-EAGLE figures, exactness derivation | complete |
| continuous batching | source cluster | yes | Handling dynamic workloads | static batching figure, iteration-level/selective batching explanation | complete |
| PagedAttention | source cluster | yes | PagedAttention | fragmentation, blocks, logical sharing, copy-on-write, parallel block reads | complete |
| PDF visual QA | QA | yes | `qa/lecture10-notes/` | rendered pages + contact sheet + checked report | complete |
