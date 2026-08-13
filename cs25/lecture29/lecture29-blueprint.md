# Lecture 29 Writing Blueprint

## Teaching thesis

Mixtral is best understood through three separate budgets: total capacity stored in all experts, active compute used by one token, and communication/memory cost required to move tokens and keep experts resident. Sparse activation improves the capacity-to-compute frontier, but it does not make total parameters, load balance, topology, or interpretability disappear. The lecture's second thesis is equally important: discrete routing creates new evidence about model behavior, yet expert specialization is less human-readable than the word “expert” suggests.

## Planned sections

1. Source repair, lecture scope, and the dense-to-sparse roadmap.
2. Mistral 7B dense baseline: GQA, sliding-window attention, tensor shapes, and the single-layer code path.
3. MoE lineage and top-two routing: router logits, gating weights, expert MLPs, and weighted aggregation.
4. Mixtral 8x7B accounting: shared attention, total parameters, active parameters, capacity, and release-time evidence.
5. Performance plots and the MLP-knowledge hypothesis; what the benchmarks do and do not show.
6. Four myths: eight global experts, 56B parameters, cost equals active parameters, and domain-specialist experts.
7. Open systems questions: MoE attention, inference load balance, expert parallelism, compression, quantization, and offload.
8. Routing interpretability: domain histograms, consecutive-token persistence, token maps, expert ablation, and latent feature subspaces.
9. Q&A engineering synthesis: edge versus cloud, batch-size effects, memory residency, domain adaptation, RAG orthogonality, expert swapping, gradient flow, and very large expert counts.
10. Final synthesis, deployment checklist, self-test, and primary readings.

## Formal scaffolding

- GQA/MQA/MHA head-count and KV-cache comparison.
- Dense Transformer residual block and SwiGLU MLP equations.
- Router logits, top-k mask, normalized gates, and weighted expert output.
- Total-versus-active parameter decomposition: shared parameters plus all or selected expert parameters.
- Resident-memory estimate in bytes and why it differs from per-token FLOPs.
- Expert-load vector, slowest-expert latency, imbalance ratio, and capacity-factor intuition.
- Consecutive-token routing probability compared with random baselines.
- Expert-ablation delta and why a single failure does not identify a semantic module.

## Terminology obligations

Define near first use: dense model, Mixture of Experts, Sparse Mixture of Experts, expert, router, gating weights, top-k routing, GQA, MQA, sliding-window attention, SwiGLU, total parameters, active parameters, expert parallelism, all-to-all communication, load balancing, capacity factor, sparsification, quantization, CPU offload, domain specialization, permutation symmetry, adaptive computation, and routing persistence.

## Figure treatment

- Insert every required recovered slide exactly once and label it with the official recording timestamp.
- Explain axes, baselines, categories, and April 2024 evidence boundaries for every benchmark plot.
- Explain router diagrams as a token-level algorithm, not only as a picture of boxes.
- Pair each myth slide with a concrete accounting example.
- Treat domain-routing plots, token maps, and the treasure-hunt ablation as evidence with uncertainty, not proof of named concepts.
- Integrate Q&A claims near the relevant architecture or systems section.

## Acceptance targets

- 26 recovered teaching figures, each exactly once.
- At least 24 teacher-voice markers.
- At least 28 teaching boxes and 14 displayed formulas.
- At least three captioned `lstlisting` blocks.
- At least 260 prose characters per figure on average.
- Strict coverage with zero warnings, double XeLaTeX, `⭐⭐⭐`, rendered PDF QA, and a signed QA report.
