# Lecture 27 Writing Blueprint

## Teaching thesis

The two talks answer the same meta-question from different levels. Jason asks why one simple objective produces many abilities and recommends looking at data, decomposing latent tasks, and plotting scaling curves. Hyung asks how to reason about architectural change and recommends identifying the dominant driving force, understanding which inductive biases are temporary shortcuts, and removing them when scale changes the regime.

## Planned sections

1. Source framing and the shared research method.
2. Jason Part I: manual data inspection and next-token prediction as massive multi-task learning.
3. Smooth aggregate loss, task-mixture decomposition, emergence, and metric caveats.
4. Inverse/U-shaped scaling as hidden-task interference; scaling curves as an experimental tool.
5. Hyung Part II: study the change, dominant forces, compute per dollar, and the Bitter Lesson.
6. Structure versus scalability; the lifecycle of inductive bias and research incentives.
7. Sequence-model foundations and the three Transformer architecture families.
8. Four-step encoder-decoder to decoder-only transformation.
9. Why extra structure once helped: translation, FLAN, representation granularity, and bidirectionality.
10. Multi-turn caching, learning-objective Q&A, final synthesis, self-test, and reading.

## Formal scaffolding

- Next-token negative log-likelihood and perplexity.
- Compute proxy and power-law scaling curve.
- Aggregate loss as a weighted mixture of latent task losses.
- Thresholded task metric showing how smooth probability changes can look discontinuous.
- Three-subtask composition for the quote-repetition U shape.
- Falling-body equation for the dominant-force analogy.
- Attention masks for bidirectional and causal attention.
- Cross-attention and self-attention equations with symbol explanations.
- Cache-cost comparison for bidirectional versus causal multi-turn processing.

## Terminology obligations

Digest at first use: next-token prediction, cross-entropy, perplexity, scaling law, emergent ability, inverse scaling, U-shaped scaling, inductive bias, Bitter Lesson, encoder-decoder, encoder-only, decoder-only, self-attention, cross-attention, bidirectional attention, causal attention, tokenization, embedding, sequence model, KV cache, maximum-likelihood estimation, and RLHF.

## Figure treatment

- Insert every required official slide exactly once.
- Explain plots before they appear, then use `读图` boxes for axes, comparisons, and limits.
- Group progressive architecture slides into explicit derivations rather than screenshot sequences without prose.
- Treat all April 2024 product and architecture judgments as classroom-period claims.

## Acceptance targets

- 66 official teaching figures, each exactly once.
- At least 20 teacher-voice markers.
- At least 20 teaching boxes and 10 displayed formulas.
- At least three captioned `lstlisting` blocks.
- At least 260 prose characters per figure on average.
- Strict coverage with zero warnings, double XeLaTeX, `⭐⭐⭐`, rendered PDF QA, and a signed QA report.
