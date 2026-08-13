# CS25 Lecture 08 Blueprint

## Teaching thesis

The lecture starts from a behavioral mystery: a language model suddenly becomes much better at predicting later tokens in its context. It then builds a deliberately simplified algebra for attention-only Transformers, decomposes heads into QK routing and OV writing circuits, and uses two-layer composition to derive induction heads. The note must preserve the evidence ladder: exact toy-model algebra, small-model causal ablations, large-model temporal correlation, and speculative extrapolation are different strengths of claim.

## Section sequence

1. Source audit, date/version boundary, and mechanistic-interpretability scope.
2. In-context learning as a two-axis loss measurement.
3. Nats, derivatives, loss bump, and phase-change hypothesis.
4. One-layer attention-only simplification and tensor-product notation.
5. Direct path, fixed-pattern linearity, QK and OV circuits.
6. Skip trigrams, positional circuits, and one-layer expressivity limits.
7. Eigenvalue summaries and their failure boundary.
8. Two-layer expansion, mixed-product identity, and virtual heads.
9. Induction pattern, previous-token composition, and head taxonomy.
10. Small-model ablation, large-model co-occurrence, and evidence grading.
11. Soft induction, translation, alternative mechanisms, LSTM comparison, and scaling-law speculation.
12. Final synthesis and open interpretability problems.

## Figure spine

- V001--V010: definition, motivation, ICL curves, loss map, nats, derivatives, phase change.
- V011--V025: one-layer assumptions, tensor-product head/layer algebra, QK/OV circuits, skip trigrams, positional circuits, summary.
- V026--V033: eigenvectors/eigenvalues, copying signatures, head distributions, multi-layer usefulness, MLP failure boundary.
- V034--V048: two-layer factorization, mixed-product identity, path expansion, loss contributions, prior-head dependence, empirical pattern inspection.
- V049--V057: induction pattern, workhorse circuit, multiple heads, QK/OV signatures, local heads, hypothesis.
- V058--V064: small-model ablation, large-model timing, chunk/translation behavior, soft induction, alternative mechanisms, LSTM and scaling-law questions.

## Required teaching scaffolds

- Display equations for the 2D loss surface, ICL score, nat/bit conversion, attention-head tensor product, one-layer expansion, fixed-pattern linearity, QK/OV matrices, eigenvalue interpretation, two-layer expansion, mixed-product identity, and induction circuit.
- At least two captioned listings: computing the ICL score/phase diagnostic and an induction-head algorithm/ablation sketch.
- Dense terminology tables for interpretability scopes, matrix/circuit notation, path types, evidence strengths, and head taxonomy.
- At least 20 teacher-voice markers, with explicit language such as `课堂提示` and `老师强调`.
- Every dense slide has setup prose, source time provenance, read-the-figure guidance, and an evidence/limitation follow-up.

## Acceptance targets

- Replace the legacy dashboard/alert/nightly-pipeline/repository-workflow material completely.
- 55+ PDF pages, all 64 reviewed teaching slides, 15+ high-signal boxes, 20+ teacher-voice markers, 10+ formula blocks, and 2+ captioned listings.
- Strict coverage checker has no warnings or errors.
- Two successful stabilized XeLaTeX passes with no layout warnings.
- `check_quality.sh` grade `⭐⭐⭐`.
- Canonical visual QA contact sheet and signed report with no unresolved defects.
