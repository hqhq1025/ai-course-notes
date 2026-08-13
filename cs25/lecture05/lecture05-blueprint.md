# CS25 Lecture 05 Teaching Blueprint

## Central thesis

Switch Transformer is not “a trillion-parameter dense model made cheap.” It is a conditional-computation system that increases available parameters while holding per-token expert compute roughly fixed. Its value comes from the joint design of routing, load balance, static capacity, precision, initialization, regularization, parallel placement, and evidence-aware evaluation.

## Teaching sequence

1. **Source audit and scaling question** (`V001--V003`, `T001`): distinguish dense scale, sparse parameters, active compute, memory, communication, and wall-clock time.
2. **MoE lineage and equations** (`V004--V006`, `T002--T003`): define expert, router/gating, top-k routing, weighted output, and the historical engineering obstacles.
3. **Switch layer as a constrained simplification** (`V007--V008`, `T004--T005`): show where sparse FFNs enter a Transformer and why top-1 is a systems choice.
4. **Training stability stack** (`V009--V012`, `T006--T009`): selective precision, initialization scale, expert dropout, and differentiable load balancing.
5. **Static-shape dispatch and token dropping** (`V013--V016`, `T009--T012`): derive capacity factor, explain overflow, preserve the negative “no token left behind” result, and separate sparsity from adaptive computation.
6. **Top-1 versus top-2 and sparse scaling** (`V017--V023`, `T013--T014`): read per-step, per-time, fixed-FLOP, small-scale, and diminishing-return plots without mixing metrics.
7. **Distributed execution and model design** (`V024--V026`, `T015--T016`): digest data/model/expert parallelism, explain total versus active parameters, and label the knowledge/reasoning statement as a hypothesis.
8. **Upstream and downstream evidence** (`V027--V032`, `T016--T017`): compare SuperGLUE, TriviaQA, model sizes, trillion-parameter Switch-C, and 101-language mT5 experiments.
9. **Distillation as deployment conversion** (`V033--V035`, `T018`): compare distillation objectives and what quality/parameter tradeoffs remain.
10. **Wrap-up, vision MoE, and boundaries** (`V036--V038`, `T019--T020`): priority routing, capacity below one, attention/storage/throughput Q&A, and realistic deployment conditions.

## Required pedagogical scaffolding

- Formula chain for scaling law, router probabilities, top-1 output, load-balancing loss, and expert capacity.
- First-use terminology table for MoE, expert, router/gating, top-1/top-2, capacity factor, token dropping, selective precision, and data/model/expert parallelism.
- At least two captioned pseudocode listings: top-1 dispatch and capacity-aware routing.
- At least ten teacher-voice markers distributed across motivation, numerical stability, negative results, evidence boundaries, and deployment Q&A.
- Every one of the 38 teaching slides placed near its explanation with time provenance.
- Dense plots and tables receive local “读图” guidance plus a statement of what the evidence does not prove.
- Every major section ends with `本章小结`; the note ends with `总结与延伸` and `拓展阅读`.

## Acceptance targets

- 28+ PDF pages for a 65-minute figure-heavy lecture.
- 38 required figures, 10+ teaching boxes, 3+ teacher-voice markers, 3+ read-figure explanations, 3+ formulas, and captioned code.
- `check_note_coverage.py --strict` produces no warnings.
- `check_quality.sh` reports `⭐⭐⭐`.
- XeLaTeX passes twice with stable references.
- Canonical PDF QA contact sheet reviewed and checklist signed.
