# Lecture 03 Blueprint

## Goal

Regenerate Lecture 03 under the new workflow as a slide-complete, self-contained guide to modern LM architecture and hyperparameter defaults.

## Section Plan

### 1. 目标、baseline 与现代默认值
- Covers slides 001-008.
- Explain why architecture work is empirical and why the lecture studies many released dense models.
- Compare original Transformer vs simple modern variant.
- First-use glossary: pre-norm, RoPE, SwiGLU, bias-free linear layers.

### 2. Norm 与 residual stream
- Covers slides 009-019.
- Explain pre-norm vs post-norm, residual stream preservation, gradient attenuation/spikes, double norm/non-residual postnorm.
- Explain LayerNorm vs RMSNorm and why FLOPs are not runtime.
- Include every slide and add read-the-figure boxes for data/evidence slides.

### 3. Activations、FFN 与 parallel blocks
- Covers slides 020-029.
- Explain ReLU, GeLU, GLU, GeGLU, ReGLU, SwiGLU, LiGLU.
- Give formulas and explain why gated activations help.
- Explain serial vs parallel blocks and why parallelism is mainly a systems/latency choice.

### 4. Position embeddings 与 RoPE
- Covers slides 030-035.
- Explain absolute sinusoidal embeddings, relative-position desiderata, rotation geometry, actual RoPE math, and implementation placement.
- Include formula chain and first-use warning about extrapolation.

### 5. Hyperparameter defaults
- Covers slides 036-051.
- Explain ff ratio, GLU 2/3 scaling, T5 exception, head-dim/head-count ratio, aspect ratio, vocab size, dropout, weight decay.
- Add tables summarizing what is conservative default, what varies, and what evidence supports it.

### 6. Stability tricks
- Covers slides 052-056.
- Explain softmax instability, z-loss, QK norm, logit soft-capping.
- Add warnings about stability patches changing model behavior.

### 7. Attention variants and inference pressure
- Covers slides 057-066.
- Explain attention heads are mostly stable except for inference-driven changes.
- Explain MQA, GQA, KV cache cost, arithmetic intensity, local/sliding-window attention, and hybrid/interleaved full attention.
- First-use glossary: MHA/MQA/GQA, KV cache, sliding-window/local attention.

### 8. 总结与延伸
- Covers slide 067.
- Synthesize: modern defaults are conservative empirical equilibria, not universal laws.
- Connect to later lectures: GPUs/kernels, parallelism, inference, scaling laws.

## QA Requirements

- Every slide image 000-066 appears in the note or is explicitly discussed as title/outline/recap.
- Important evidence slides have `读图` boxes.
- `check_note_coverage.py` warnings are reviewed against `lecture03-coverage.md`.
- `render_pdf_qa.py` contact sheet is generated and reviewed.
