# Lecture 21 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V004 | Dartmouth ambition, 2009 MT pipeline, 2013 verticalized NLP, and 2016 general paradigms. | Historical diagrams illustrate fragmentation and consolidation; they do not prove one architecture solves intelligence. | Consolidation history |
| V005--V010 | Variable-length representations, LSTM expressivity, sequential bottleneck, convolutional parallelism, and encoder-decoder attention. | LSTMs remain expressive; the critique is parallelism/path length, not incapacity. | Before self-attention |
| V011--V018 | Cross-modal content addressing, self-attention, original motivation, attention families, encoder/decoder dot product, and complexity. | Parallel reading succeeded; fully parallel generation remained difficult. | Self-attention mechanism |
| V019--V026 | Full Transformer, residual structure, weighted-average/convolution/multi-head comparison, MT/parsing results, and interpretable patterns. | Early task gains support the architecture; qualitative attention maps are not complete causal explanations. | Architecture and evidence |
| V027--V030 | Absolute/relative position evolution and Music Transformer mechanism/demo. | Music examples are qualitative and position schemes have different extrapolation assumptions. | Position representations |
| V031--V036 | Quadratic attention, long-context patterns, memory/retrieval methods, FLOPs/bandwidth, GQA/MQA, and online softmax. | Theoretical complexity and wall-clock speed differ; hardware and kernels matter. | Attention systems |
| V037--V043 | Other modalities, intentionally omitted topics, LLM substrate, data-center Transformer, tools, build loop, and research directions. | The talk is selective; future directions are attributed rather than treated as solved capability. | Modern systems and agenda |
| T001--T006 | Preserve the historical thesis, pipeline consolidation, reusable representations, LSTM tradeoffs, content addressing, and failed parallel decoding. | Spoken claims are paraphrased and timestamp-bounded. | Sections 1--4 |
| T007--T011 | Preserve architectural synthesis, weighted-average intuition, evidence caution, position evolution, and Music Transformer interpretation. | Mechanism and results remain tied to the lecture and cited primary sources. | Sections 5--7 |
| T012--T016 | Preserve long-context memory movement, systems co-design, lecture omissions, tool allocation, and forward research agenda. | November 2023 boundary remains explicit. | Sections 8--9 |
| T017--T018 | Preserve Q&A on decoding order, world models, recombination/generalization, multi-agent coordination, modularity, gradient descent, distillation, speculative decoding, and product feedback loops. | Q&A judgments are presented as speaker reasoning, not settled consensus. | Final synthesis |

## Acceptance Evidence

- The final note is 48 pages and references all 43 required visual nodes exactly once. It contains 50 teaching boxes, 22 in-note teacher-voice markers, 15 displayed formula blocks, 3 captioned listings, and 25,143 prose characters, averaging 584 prose characters per figure.
- `check_note_coverage.py --strict` reports 43 figures, 33 local read-figure treatments, 13 section summaries, and zero warnings or missing required nodes.
- `check_quality.sh` reports `⭐⭐⭐`; the stabilized final two-pass XeLaTeX log has no overfull/underfull boxes, undefined references, rerun requests, or hyperref warnings beyond the repository-standard Fandol font notices.
- Canonical PDF visual QA is signed in `qa/lecture21-notes/qa-report.md` after reviewing the complete 48-page contact sheet and enlarged TOC, formula, table, code, Music Transformer, long-context, systems, synthesis, and reference pages.
