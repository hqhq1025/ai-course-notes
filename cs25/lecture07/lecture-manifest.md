# Source Manifest: CS25 Lecture 07

Access date: 2026-08-11.

## Files

- `cover.jpg`: current Stanford Online official thumbnail.
- `metadata.json`: sanitized stable metadata for official upload `zejXBg-2Vpk`.
- `lecture07.en.srt`: official manual English captions, 1,476 parsed captions.
- `transcript_timed.txt`: timestamp-preserving transcript.
- `transcript_clean.txt`: five-minute transcript digest for source review.
- `lecture07.mp4`: local ignored 1080p official recording used for slide recovery.
- `slides-images/`: 28 reviewed teaching slides or final progressive-build states.

## Supplementary Source Materials

- `source-materials/SOURCES.md`: official sources, primary papers, and source-boundary notes.
- `lecture07-teacher-voice-ledger.md`: motivations, historical detail, Q&A clarifications, experiment interpretation, and planned placement.
- `lecture07-blueprint.md`: teaching thesis, section sequence, figure spine, and acceptance targets.
- `lecture07-coverage.md`: source-node treatment matrix.

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | official video 00:00:46 | `slides-images/slide-01-transformers-title.jpg` |
| V002 | figure | yes | official video 00:01:08 | `slides-images/slide-02-transformer-overview.jpg` |
| V003 | figure | yes | official video 00:02:16 | `slides-images/slide-03-self-attention.jpg` |
| V004 | figure | yes | official video 00:03:14 | `slides-images/slide-04-multi-head-attention.jpg` |
| V005 | figure | yes | official video 00:03:28 | `slides-images/slide-05-decoder-transition.jpg` |
| V006 | figure | yes | official video 00:04:28 | `slides-images/slide-06-sequence-generation.jpg` |
| V007 | figure | yes | official video 00:05:28 | `slides-images/slide-07-autoregressive-decoding.jpg` |
| V008 | figure | yes | official video 00:06:04 | `slides-images/slide-08-teacher-forcing.jpg` |
| V009 | figure | yes | official video 00:12:36 | `slides-images/slide-09-causal-mask.jpg` |
| V010 | figure | yes | official video 00:17:00 | `slides-images/slide-10-npt-overview.jpg` |
| V011 | figure | yes | official video 00:18:12 | `slides-images/slide-11-npt-motivation.jpg` |
| V012 | figure | yes | official video 00:22:00 | `slides-images/slide-12-traditional-nonparametric.jpg` |
| V013 | figure | yes | official video 00:24:00 | `slides-images/slide-13-entire-dataset-input.jpg` |
| V014 | figure | yes | official video 00:24:14 | `slides-images/slide-14-datapoint-attention.jpg` |
| V015 | figure | yes | official video 00:24:28 | `slides-images/slide-15-masking-objective-overview.jpg` |
| V016 | figure | yes | official video 00:26:28 | `slides-images/slide-16-full-dataset-mask-notation.jpg` |
| V017 | figure | yes | official video 00:27:16 | `slides-images/slide-17-per-attribute-embedding.jpg` |
| V018 | figure | yes | official video 00:28:22 | `slides-images/slide-18-flatten-datapoint-attention.jpg` |
| V019 | figure | yes | official video 00:30:58 | `slides-images/slide-19-abd-aba-architecture.jpg` |
| V020 | figure | yes | official video 00:31:04 | `slides-images/slide-20-three-stage-overview.jpg` |
| V021 | figure | yes | official video 00:33:34 | `slides-images/slide-21-stochastic-masking-objective.jpg` |
| V022 | figure | yes | official video 00:37:16 | `slides-images/slide-22-tabular-domain.jpg` |
| V023 | figure | yes | official video 00:38:08 | `slides-images/slide-23-tabular-benchmarks.jpg` |
| V024 | figure | yes | official video 00:51:16 | `slides-images/slide-24-corruption-goal.jpg` |
| V025 | figure | yes | official video 00:51:50 | `slides-images/slide-25-corruption-method.jpg` |
| V026 | figure | yes | official video 00:53:02 | `slides-images/slide-26-corruption-results.jpg` |
| V027 | figure | yes | official video 01:00:32 | `slides-images/slide-27-duplicate-intervention.jpg` |
| V028 | figure | yes | official video 01:05:36 | `slides-images/slide-28-summary-future-work.jpg` |
| T001 | text | optional | transcript 00:00:47--00:01:15 | Transformer combines self-attention, multi-head attention, and fast autoregressive training. |
| T002 | text | optional | transcript 00:01:15--00:02:16 | “Blue ball” intuition for intra-sequence relations. |
| T003 | text | optional | transcript 00:02:25--00:03:20 | Heads can specialize in different relation types. |
| T004 | text | optional | transcript 00:03:28--00:06:08 | Teacher forcing enables parallel next-token training. |
| T005 | text | optional | transcript 00:06:08--00:06:34; 00:12:36--00:13:04 | Causal masking prevents access to future gold targets. |
| T006 | text | optional | transcript 00:07:56--00:10:05 | Tensor2Tensor defaults and ablations reveal crucial optimization details. |
| T007 | text | optional | transcript 00:10:05--00:12:01 | Transformer origin story and rapid pre-deadline synthesis. |
| T008 | text | optional | transcript 00:16:45--00:18:15 | Explicit dataset dependence and “k-NN 2.0” intuition. |
| T009 | text | optional | transcript 00:18:15--00:19:20 | Prior non-parametric families and NPT’s plug-and-play goal. |
| T010 | text | optional | transcript 00:20:16--00:23:25 | Fixed-dataset supervised setting versus meta-learning extensions. |
| T011 | text | optional | transcript 00:23:40--00:24:22 | Dataset input, datapoint attention, and masking are the three core components. |
| T012 | text | optional | transcript 00:26:28--00:31:00 | Typed embedding, ABD/ABA, and row permutation equivariance. |
| T013 | text | optional | transcript 00:31:01--00:33:33 | Feature masking regularizes; target masking enables relational lookup. |
| T014 | text | optional | transcript 00:33:53--00:35:25 | Mini-batching, roughly 8,000 full-batch points, and 11-million-point scale. |
| T015 | text | optional | transcript 00:36:03--00:36:14 | Surprising robustness and light tuning on small datasets. |
| T016 | text | optional | transcript 00:36:22--00:37:56 | Tabular motivation, diverse datasets, and strong tuned baselines. |
| T017 | text | optional | transcript 00:37:21--00:40:20 | Average-rank interpretation and four-of-ten dataset result. |
| T018 | text | optional | transcript 00:38:44--00:39:15 | ABA ablation benefit and attribute-dimension tradeoff. |
| T019 | text | optional | transcript 00:51:16--00:53:00 | Column-wise corruption isolates reliance on other datapoints. |
| T020 | text | optional | transcript 00:54:41--01:00:35 | Duplicate lookup, intervention correlation, and transformed-target task. |
| T021 | text | optional | transcript 01:00:54--01:01:33 | Closing results, limitations, and future applications. |
| T022 | text | optional | transcript 01:02:19--01:03:35 | Fully connected learned graph analogy. |
| T023 | text | optional | transcript 01:04:19--01:05:16 | Small/large-data tradeoff and parametric memory question. |
| P001 | text | optional | Kossen et al. 2021 | NPT architecture, objective, experiments, and limitations. |
| P002 | text | optional | Vaswani et al. 2017 | Transformer attention and autoregressive training context. |
| P003 | text | optional | Devlin et al. 2018 | Masked modeling analogy. |
| P004 | text | optional | Zaheer et al. 2017; Lee et al. 2018 | Set equivariance and attention over unordered inputs. |
| P005 | text | optional | Gaussian processes / kernels / k-NN | Classical non-parametric prediction context. |
| P006 | text | optional | Garnelo et al. 2018 | Neural-process connection. |
| P007 | text | optional | Kipf et al. 2018 | Learned relational graph connection. |
| P008 | text | optional | Chen and Guestrin 2016 | XGBoost baseline context. |
| P009 | text | optional | Prokhorenkova et al. 2018 | CatBoost baseline context. |
| P010 | text | optional | Ke et al. 2017 | LightGBM baseline context. |
| P011 | text | optional | Arik and Pfister 2019 | TabNet neural tabular baseline. |
| P012 | text | optional | Breiman 2001 and standard k-NN/MLP baselines | Non-attention benchmark context. |
| O001 | figure | no | official video 00:00:02 | Stanford Engineering bumper. |
| O002 | figure | no | official video 00:01:14--00:03:20 | Progressive self-attention and multi-head builds; final states retained. |
| O003 | figure | no | official video 00:04:08--00:12:36 | Progressive decoding equations and mask animation; distinct final states retained. |
| O004 | figure | no | official video 00:17:22--00:30:58 | Repeated motivation and ABD/ABA build states; final teaching states retained. |
| O005 | figure | no | official video 00:38:08--00:50:20 | Q&A revisits benchmark and architecture slides; spoken clarification retained as T017--T018. |
| O006 | figure | no | official video 00:54:44--01:00:32 | Duplicate/intervention progressive builds; final complete multi-panel state retained as V027. |
| O007 | figure | no | official video 01:00:42--01:05:40 | Blank transitions, repeated summary build, and Stanford end slate; final summary retained as V028. |

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/text node must be placed in the note or explicitly marked with a concrete omission reason in the coverage matrix.
- Progressive reveals retain the final complete state and intermediate states only when they teach a distinct step.
- Every important figure needs setup prose, source time provenance, and a nearby interpretation.
- Dense terminology clusters need a table or concept box; foundational concepts need formulas and worked intuition.
- Final PDF must pass strict coverage, two-pass XeLaTeX, quality grade `⭐⭐⭐`, and rendered visual QA.
