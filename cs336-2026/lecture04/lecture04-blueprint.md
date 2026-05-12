# Lecture 04 Blueprint

## Goal
Regenerate Lecture 04 as a slide-complete, source-first note on attention alternatives and mixture-of-experts. The note should explain mechanisms, tradeoffs, evidence, and systems implications rather than just naming model families.

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
- Every slide image 000-059 appears in the note.
- Important mechanism/evidence slides have read-the-figure boxes.
- First-use glossary for DSA, MoE, top-k routing, expert parallelism, all-to-all, z-loss, upcycling, MLA, MTP.
- Visual PDF QA contact sheet generated and reviewed.
