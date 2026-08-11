# Lecture 02 Coverage Matrix

Status: second-round executable-source and teacher-voice verification completed on 2026-08-11.

Verification evidence:

- Strict coverage: `figs=11 readfig=12 boxes=51 term_digest=2 teacher_voice=12 formulas=19 code=6 summaries=8 prose_chars=14076`, with no warnings or hard errors.
- Quality check: 22 pages, 10 sections, 51 teaching boxes, 11 source figures, `⭐⭐⭐`.
- XeLaTeX: two successful final passes; no overfull boxes, LaTeX errors, undefined control sequences, missing characters, emergency stops, or fatal errors.
- Visual QA: all 22 rendered pages inspected; section-level TOC removed a sparse second contents page, and the final source-index continuation was completed with a resource-accounting self-test.

Teacher source: `lecture02-slides.py` contains executable `text(...)` narration. Its motivations, caveats, heuristics, and transitions are mapped in `lecture02-teacher-voice-ledger.md` and woven into the note. Editorial synthesis that is not directly spoken is labeled `讲义提醒` rather than attributed to the instructor.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| `main()` Marin forecast result | figure + motivation | yes | 本讲主线 | figure + read-the-figure + scaling/resource connection | covered |
| `motivating_questions()` | worked examples | yes | 本讲主线 | training-time calculation + max-model-memory calculation + warnings | covered |
| `tensors_basics()` | tensor concepts | yes | Tensor 与 Memory | tensor state list + shape ledger table | covered |
| `fp32.png` | dtype figure | yes | 数值格式 | figure + read-the-figure | covered |
| `fp16.png` | dtype figure | yes | 数值格式 | figure + read-the-figure with bf16 comparison | covered |
| `bf16.png` | dtype figure | yes | 数值格式 | figure + read-the-figure with fp16 comparison | covered |
| `fp8_formats.png` | dense dtype figure | yes | 数值格式 | figure + read-the-figure | covered |
| `fp4 / NVFP4` | text concept | yes | 数值格式 | prose explanation + dtype comparison table | covered |
| `cpu-gpu.png` | device figure | yes | CPU 与 GPU memory | figure + read-the-figure | covered |
| `tensor_einops()` | code/shape cluster | yes | Einops 与 Shape | code listings + terminology box + warning | covered |
| `tensor_operations_flops()` | compute concepts | yes | Compute Accounting | FLOPs/FLOP/s table + matmul formula + MFU explanation | covered |
| `arithmetic_intensity()` | foundational concept | yes | Arithmetic Intensity 与 Roofline | compute-memory figure + formulas + bottleneck rule | covered |
| ReLU/GeLU/dot/matvec/matmul nodes | worked examples | yes | 从 ReLU 到 matmul | operation table + LLM mapping + warning | covered |
| `roofline-improved-1400.png` | dense plot | yes | Roofline 图 | figure + read-the-figure + MFU relationship + boundary warning | covered |
| `deep-network.png` | figure | yes | Training Step Accounting | figure + read-the-figure | covered |
| `gradients_flops()` | formula derivation | yes | Why 6BP | forward/backward formulas + 6BP box | covered |
| `optimizer()` | terminology/implementation | yes | Optimizer state memory | memory table + AdaGrad code + optimizer terminology box | covered |
| `train_loop()` | code | yes | Training loop | listing + zero grad warning + time-line box | covered |
| `gradient_accumulation()` | memory optimization | yes | Memory Optimization | formula + trade-off box + comparison table | covered |
| `activation_checkpointing()` | memory optimization | yes | Memory Optimization | deep-network figure + read-the-figure + checkpointing code + warning | covered |
| First-use systems terms | glossary | yes | Throughout | optimizer state, sharding, activation checkpointing, roofline, MFU, FLOP/s explained locally | covered |
| ZeRO / sharding mentions | forward reference | accepted | Resource ledger / memory optimization | First-use glossary explains sharding and ZeRO-1/2/3; full algorithms remain a forward reference to parallelism/FSDP lectures. | covered |
| PDF visual QA | QA | yes | `qa/lecture02-notes/` | rendered pages + contact sheet + report | covered |
