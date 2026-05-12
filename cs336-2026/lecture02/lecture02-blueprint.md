# Lecture 02 Blueprint

## Goal
Regenerate Lecture 02 as a self-contained resource-accounting note under the new workflow. The note must make tensor memory, FLOPs, FLOP/s, arithmetic intensity, optimizer state, and memory tradeoffs operational.

## Section Plan

### 1. 本讲主线
- Covers: Marin run result, motivating resource questions, efficiency framing.
- Required visual: `marin-forecast-result.jpg` with read-the-figure explanation.
- Required worked examples: 70B on 15T tokens over 1024 H100s; 8 H100 AdamW memory upper bound.

### 2. Tensor 与 Memory
- Covers: tensors store data/parameters/gradients/optimizer state/activations, rank and shape, dtype memory.
- Required visuals: `fp32.png`, `fp16.png`, `bf16.png`, `fp8-formats.png`, `cpu-gpu.png`.
- Required tables: shape ledger, dtype comparison.
- Required warning: low precision is not free.

### 3. Einops 与 Shape
- Covers: PyTorch dimension ambiguity, einsum/reduce/rearrange.
- Required code: PyTorch transpose example, einsum named-dimension example.
- Required glossary: einsum/reduce/rearrange.

### 4. Compute Accounting
- Covers: FLOPs vs FLOP/s, matmul FLOPs, benchmarking, MFU.
- Required formulas: `2BDK`, actual FLOP/s, MFU.
- Required worked example: equal FLOPs can run differently due to kernel shape.

### 5. Arithmetic Intensity 与 Roofline
- Covers: compute-memory loop, arithmetic intensity, accelerator intensity, ReLU/GeLU/dot/matvec/matmul, roofline.
- Required visuals: `compute-memory.png`, `roofline-improved-1400.png`.
- Required tables: operation intensity mapping to LLM components.
- Required warnings: roofline limits, complexity vs actual speed.

### 6. Training Step Accounting
- Covers: deep network, forward/backward FLOPs, optimizer state, training loop.
- Required visual: `deep-network.png`.
- Required code: AdaGrad state, training loop.
- Required glossary: optimizer state, SGD/Momentum/AdaGrad/RMSProp/Adam.

### 7. Memory Optimization
- Covers: gradient accumulation, activation checkpointing, sharding as related strategy.
- Required visual: `deep-network.png` reused with different interpretation.
- Required tables: memory optimization strategy comparison; checkpointing strategy table.

### 8. End-to-end Resource Ledger
- Covers: preflight checklist before launching a training job.
- Required table: parameter/FLOPs/memory/intensity/MFU checks.

### 9. 总结与延伸
- Synthesize resource accounting as common foundation for kernels, parallelism, inference, and scaling laws.

## QA Requirements
- `tools/scripts/check_quality.sh cs336-2026/lecture02/lecture02-notes.tex` reports `⭐⭐⭐`.
- `check_note_coverage.py` warnings are reviewed against this coverage matrix.
- `render_pdf_qa.py` contact sheet is generated and manually inspected.
