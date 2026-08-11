# Lecture 04 Blueprint

## Goal
Regenerate Lecture 04 as a slide-complete, source-first note on attention alternatives and mixture-of-experts. Retain every teaching-bearing source page in lecture order and explain mechanisms, tradeoffs, evidence, and systems implications; only the pure title page is omitted because the note cover duplicates it.

## Section Plan

### 1. 本讲主线
- Covers title and framing slides 001-003.
- Explain why long context and conditional compute force architecture alternatives.

### 2. Attention alternatives
- Covers slides 004-013.
- Explain linear attention, recurrent form, Mamba-2, Gated Delta Net, hybrid attention, DSA.
- Required formulas: softmax attention, linear attention reordering, recurrent state update, sparse top-k selection.
- Required glossary: linear attention, state-space/recurrent attention, hybrid attention, DSA.

### 3. Why MoE
- Covers slides 014-024.
- Explain MoE as sparse conditional computation and why same FLOPs with more parameters can help.
- Explain training speed, quality, parallelizability, infrastructure cost.

### 4. Routing
- Covers slides 025-035.
- Explain routing function, top-k routing, token-choice, expert-choice, shared experts, fine-grained experts.
- Required formulas: router logits, top-k dispatch, auxiliary balancing intuition.

### 5. Training MoEs
- Covers slides 036-043.
- Explain sparsity challenge, REINFORCE, stochastic routing perturbations, load balancing losses, DeepSeek per-expert bias.

### 6. Systems side
- Covers slides 044-047.
- Explain expert parallelism, all-to-all, communication overhead, activation down-projection, stochasticity.

### 7. Stability, fine-tuning, and upcycling
- Covers slides 048-053.
- Explain router z-loss, sparse MoE fine-tuning overfit risk, dense-to-MoE upcycling.

### 8. DeepSeek MoE case study
- Covers slides 054-059.
- Explain DeepSeek MoE v1/v2/v3, MLA, MTP, and how attention + MoE choices combine.

### 9. 总结与延伸
- Covers slide 060.
- Synthesize attention alternatives and MoE as two forms of selective computation.

## QA Requirements
- Slide images 001--059 all appear in the note; slide 000 is intentionally omitted as a pure title page duplicated by the note cover.
- Important mechanism/evidence slides have read-the-figure boxes.
- First-use glossary for DSA, MoE, top-k routing, expert parallelism, all-to-all, z-loss, upcycling, MLA, MTP.
- No teacher-voice source is available in the lecture directory; classroom voice must not be fabricated.
- Strict coverage, double-pass XeLaTeX and visual PDF QA must all pass.
