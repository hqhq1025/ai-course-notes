# Lecture 18 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V003 | Establish the first talk's thesis, motivation, and visual-to-math roadmap. | Mathematical approximation and biological implementability are not proof of neural use. | Source audit and roadmap |
| V004--V012 | Explain SDM requirements, sparse/distributed addresses, write superposition, noisy-query readout, circle intersections, and formal read steps. | Diagrams are low-dimensional teaching projections of a high-dimensional binary space. | SDM operations |
| V013--V022 | Reconstruct attention through language example, Q/K/V, dot products, softmax, value aggregation, and full update. | This is the lecture's 2023 attention recap, not a survey of later variants. | Attention recap |
| V023--V030 | Derive the exponential hypersphere-intersection approximation, Hamming/cosine relation, regression fit, SDM notation, equivalence, parameter tests, and required conditions. | The mapping is approximate and depends on normalization and coefficients. | Attention approximates SDM |
| V031--V035 | Explain continuous SDM, MLP implementation, whether learned attention resembles optimal SDM, learned beta, Transformer component interpretations, and open questions. | FFN/LayerNorm interpretations are research hypotheses, not unique explanations. | Transformer implications |
| V036--V040 | Map abstract SDM circuitry to cerebellar anatomy and preserve first-talk references. | Circuit mapping is biologically plausible but not experimentally confirmed as attention. | Biological plausibility |
| V041--V049 | Introduce cognitive maps, sequential-structure problem, navigation/tree examples, spatial and non-spatial evidence, graph world models, and desired general algorithm. | Neural evidence motivates functional structure; it does not identify a Transformer module anatomically. | Cognitive maps |
| V050--V059 | Explain TEM architecture, LEC/MEC/hippocampal factorization, recurrent structure, Hebbian memory, graph inference, grid-like codes, and rapid learning. | Model/neural similarity is evaluated at representational and computational levels. | TEM |
| V060--V066 | Recast TEM using Transformer/modern-Hopfield equations, query retrieval, relational-memory steps, softmax memory, architecture comparison, analysis, and conclusions. | TEM has strong inductive biases and a narrow task; one-layer success does not generalize to arbitrary LLM tasks. | TEM and Transformers |
| T001--T010 | Preserve the SDM thesis, visual-first order, associative-memory design criteria, write/read mechanism, Q/K/V explanation, and scope caveat. | Spoken claims are paraphrased and timestamp-bounded. | Sections 1--3 |
| T011--T020 | Preserve approximation conditions, continuous SDM, learned coefficients, architecture hypotheses, cerebellar mapping, timescale questions, pattern/neuron views, experimental test, and analogy limits. | Biology is clearly separated into implementability, hypothesis, and evidence. | Sections 4--6 |
| T021--T026 | Preserve the last-minute second-speaker context, structural-generalization problem, spatial/non-spatial evidence, and content/structure factorization. | Handwritten lecture is reconstructed from the official video, not a polished slide deck. | Section 7 |
| T027--T030 | Preserve TEM's architecture, graph inference, grid-like codes, and rapid adaptation. | Functional similarity does not imply cell-by-cell identity. | Section 8 |
| T031--T034 | Preserve modern Hopfield attention mapping, scaling advantage, two-way neuroscience/AI conclusions, and closing grid-cell Q&A. | The final relation remains an interpretive bridge, not a complete theory. | Sections 9--10 |

## Acceptance Evidence

- Final artifact: 61 pages, 66 recovered teaching figures, 26 teaching boxes, 11 in-note teacher-voice markers, 17 displayed formula blocks, 3 captioned listings, and 17,886 prose characters (`271` prose characters per figure).
- Every required visual asset is referenced exactly once. `check_note_coverage.py --strict` passes with zero warnings, including section bridges, terminology digestion, teacher voice, formula explanations, and manifest coverage.
- `check_quality.sh` reports `⭐⭐⭐`.
- Two stabilized XeLaTeX passes complete without overfull/underfull boxes, unresolved references, rerun requests, or hyperref warnings; only repository-standard Fandol font notices remain.
- Canonical PDF QA renders all 61 pages with no near-blank pages. The signed report records full contact-sheet review plus enlarged inspection of formulas, tables, code, hand-drawn derivations, final synthesis, and references.
