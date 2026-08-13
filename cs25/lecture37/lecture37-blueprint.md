# Lecture 37 Writing Blueprint

## Central thesis

The lecture should not be rewritten as a generic chain-of-thought survey. Its core systems argument is that “reasoning” is an operational interface of intermediate tokens, and capability depends on four separable interventions: expose candidate trajectories through decoding, reshape their distribution through training, aggregate uncertainty across trajectories, and retrieve relevant knowledge before or during generation.

## Teaching sequence

1. Fix the operational definition of reasoning and explicitly separate it from claims about human cognition.
2. Use the last-letter task and Boolean-circuit result to explain why intermediate tokens add serial computation.
3. Show how pretrained models can contain useful trajectories that greedy decoding hides.
4. Derive CoT decoding as candidate generation plus answer-confidence reranking, including calibration limits.
5. Compare few-shot CoT, zero-shot “let's think step by step,” and SFT by what they change and where they fail.
6. Move from human imitation to model-generated traces, rejection sampling, iterative self-improvement, and RL finetuning.
7. Make verifier design the center of the RL section, not the choice of optimizer acronym.
8. Use the long arithmetic trace to discuss output-length scaling, emergent structure, search, and anthropomorphic traps.
9. Derive answer-level marginalization and self-consistency from the mismatch between token likelihood and answer probability.
10. Extend aggregation to free-form outputs through universal self-consistency.
11. Combine retrieval with reasoning through analogical examples, abstraction, and deep-research loops.
12. End with the verifier frontier, non-unique objectives, application evidence, and Q\&A uncertainty.

## Figure treatment

- Retain all 48 required official pages exactly once.
- Treat pages 8--10, 13--18, 19--25, 33--42, and 43--46 as visual sequences whose local prose explains what changes from one page to the next.
- Every theorem, benchmark, probability diagram, worked trace, calibration plot, or product architecture gets a setup paragraph, a reading guide, and an evidence boundary.
- Page 49 is intentionally omitted because it is only the closing card; its substantive quotation is not needed to preserve the teaching argument.

## Math scaffolding

- Autoregressive factorization of a reasoning trace and final answer.
- Computational-depth versus generated-token intuition for serial problems.
- Candidate ranking by answer-token log probability.
- SFT negative log-likelihood over human traces.
- Outcome-filtered model-generated data and an expected-reward RL objective.
- Verifier precision/recall and false-positive contamination of training data.
- Answer marginalization over multiple reasoning paths.
- Monte Carlo self-consistency estimator and consistency-based confidence.
- Universal self-consistency as judge-based clustering/selection for free-form outputs.
- Retrieval-plus-reasoning decomposition and cost/accuracy tradeoffs.

## Code scaffolding

- CoT candidate generation and answer-confidence reranking.
- Rejection-sampling data generation with an explicit answer parser and verifier.
- Self-consistency aggregation for exact answers.
- Universal self-consistency for semantic/free-form answers.
- Retrieval-plus-reasoning loop with provenance and stopping conditions.

## Evidence boundaries

- Intermediate tokens increase available sequential computation; they do not prove that the textual trace is faithful or human-like.
- High answer confidence is a ranking signal, not a complete hallucination detector.
- SFT failure and RL-finetuning gains depend on task distribution, data quality, model capacity, and verifier reliability.
- Self-consistency estimates answer mass only under the chosen sampling distribution and can amplify correlated errors.
- Universal self-consistency adds a model judge whose bias and prompt sensitivity must be audited.
- Retrieval can improve reasoning by supplying facts or analogies, but retrieval quality and source provenance remain separate failure modes.
- April 2025 model/product examples must not be rewritten as 2026 product guarantees.

## Acceptance contract

- At least 20 pages, 10 teaching boxes, 18 teacher-voice markers, 4 formula blocks, and 4 captioned listings.
- At least 260 prose characters per figure on average; dense slides need local explanation near the image.
- Strict coverage must show all 48 required figures exactly once and no reference to optional slide 49.
- Final artifact must pass `⭐⭐⭐`, stabilized two-pass XeLaTeX, canonical rendered-page QA, and `git diff --check`.
