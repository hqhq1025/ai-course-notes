# CS25 Lecture 07 Blueprint

## Teaching thesis

This lecture connects two ideas that are often taught separately. First, Transformer training scales because causal masking permits teacher-forced next-token prediction at every position in parallel. Second, the same attention primitive can be moved one level up: instead of relating tokens inside one example, NPT relates entire datapoints and learns when to retrieve information from neighboring rows. The note must make the change of axis, objective, evidence, and scaling cost explicit.

## Section sequence

1. Source audit and two-part lecture map.
2. Attention, self-attention, and multi-head attention.
3. Autoregressive decoding, teacher forcing, and causal masks.
4. From parametric prediction to explicit dataset dependence.
5. Dataset-and-mask notation and the NPT input contract.
6. Per-attribute embedding, ABD/ABA alternation, and permutation equivariance.
7. Feature/target stochastic masking and learned lookup.
8. Tabular benchmark design and rank-based evidence.
9. Corruption test on real datasets.
10. Duplicate/intervention experiment and mechanism evidence.
11. Scaling, GNN/meta-learning connections, and future work.
12. Final synthesis.

## Figure spine

- V001--V009: Transformer overview, self-attention, multi-head attention, decoding, teacher forcing, and causal mask.
- V010--V016: NPT overview, motivation, classical non-parametric context, dataset-as-input, and mask notation.
- V017--V021: embedding, ABD/ABA tensor transformations, three-stage overview, and stochastic masking objective.
- V022--V023: tabular domain and benchmark table.
- V024--V026: corruption goal, method, and results.
- V027: semi-synthetic duplicate/intervention experiment.
- V028: limitations, experiments, and future work.

## Required teaching scaffolds

- Display equations for scaled dot-product attention, multi-head attention, autoregressive factorization, teacher-forcing loss, causal mask, NPT input/mask sets, ABD/ABA tensor shapes, permutation equivariance, masking objective, and datapoint-attention complexity.
- At least two captioned listings: causal teacher-forcing pseudocode and conceptual NPT forward/masking pseudocode.
- Dense terminology tables for Transformer training terms, non-parametric families, and tabular baselines/metrics.
- At least 15 teacher-voice markers woven into normal teaching flow.
- Every slide has a setup paragraph, source time interval, and nearby interpretation; dense figures receive explicit `读图` guidance and causal/metric warnings.

## Acceptance targets

- Replace the legacy AI-SRE/incident/governance material completely.
- 30+ PDF pages, 28 reviewed teaching slides, 10+ high-signal boxes, 15+ teacher-voice markers, and prose-led flow.
- Strict coverage checker has no warnings or errors.
- Two successful XeLaTeX passes.
- `check_quality.sh` grade `⭐⭐⭐`.
- Canonical visual QA contact sheet and signed report with no unresolved defects.
