# Lecture 10 Coverage Matrix

Status: second-round executable-source and teacher-voice verification completed on 2026-08-11.

Source: `lecture10-slides.py`, official executable lecture source. The note follows source clusters rather than a PDF slide deck, and maps spoken-style `text(...)` narration in `lecture10-teacher-voice-ledger.md`. Additional deployment guidance not stated by the source is labeled `讲义提醒`.

Verification evidence:

- Strict coverage reports `figs=29 readfig=24 boxes=47 term_digest=4 teacher_voice=11 formulas=4 code=0 summaries=4 prose_chars=12498`, with no warnings or hard errors.
- Quality check reports 26 pages, 7 sections, 47 teaching boxes, 29 source figures, `⭐⭐⭐`.
- Double-pass XeLaTeX succeeds; final logs have no overfull boxes, LaTeX errors, undefined control sequences, missing characters, emergency stops, or fatal errors.
- Visual QA inspected the complete 26-page contact sheet and full-size pages 25--26; the sparse summary continuation was expanded into a five-ledger serving acceptance matrix and Pareto-frontier warning.

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
