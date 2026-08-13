# Source Manifest: CS25 Lecture 05

Access date: 2026-08-11.

## Files

- `cover.jpg`: Stanford Online official thumbnail.
- `metadata.json`: sanitized stable video metadata.
- `lecture05.en.srt`: official manual English (`en-US`) captions.
- `transcript_timed.txt`: timestamp-preserving transcript.
- `transcript_clean.txt`: five-minute transcript digest for source review.
- `lecture05.mp4`: local ignored 1080p official recording used for slide recovery.
- `slides-images/`: 38 reviewed teaching slides or final progressive-build states.

## Supplementary Source Materials

- `source-materials/SOURCES.md`: official course/video sources, primary papers, code, and source-boundary notes.
- `lecture05-teacher-voice-ledger.md`: motivations, warnings, Q&A clarifications, and planned placement.
- `lecture05-blueprint.md`: teaching thesis, section sequence, and acceptance targets.
- `lecture05-coverage.md`: source-node treatment matrix.

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | official video 00:00:06 | `slides-images/slide-01-title.jpg` |
| V002 | figure | yes | official video 00:01:42 | `slides-images/slide-02-neural-scaling-laws.jpg` |
| V003 | figure | yes | official video 00:02:36 | `slides-images/slide-03-new-axis-sparsity.jpg` |
| V004 | figure | yes | official video 00:03:06 | `slides-images/slide-04-adaptive-mixtures-history.jpg` |
| V005 | figure | yes | official video 00:04:02 | `slides-images/slide-05-moe-gating-equations.jpg` |
| V006 | figure | yes | official video 00:04:26 | `slides-images/slide-06-moe-success-and-challenges.jpg` |
| V007 | figure | yes | official video 00:05:38 | `slides-images/slide-07-switch-transformer-layer.jpg` |
| V008 | figure | yes | official video 00:07:22 | `slides-images/slide-08-improved-training-methodology.jpg` |
| V009 | figure | yes | official video 00:08:50 | `slides-images/slide-09-selective-precision.jpg` |
| V010 | figure | yes | official video 00:10:22 | `slides-images/slide-10-reduced-initialization-scale.jpg` |
| V011 | figure | yes | official video 00:10:52 | `slides-images/slide-11-higher-regularization-fine-tuning.jpg` |
| V012 | figure | yes | official video 00:12:48 | `slides-images/slide-12-load-balance-loss.jpg` |
| V013 | figure | yes | official video 00:13:30 | `slides-images/slide-13-static-graph-dynamic-architecture.jpg` |
| V014 | figure | yes | official video 00:14:38 | `slides-images/slide-14-expert-capacity-factor.jpg` |
| V015 | figure | yes | official video 00:15:56 | `slides-images/slide-15-no-token-left-behind.jpg` |
| V016 | figure | yes | official video 00:25:32 | `slides-images/slide-16-putting-it-all-together.jpg` |
| V017 | figure | yes | official video 00:27:08 | `slides-images/slide-17-comparison-moe-switch.jpg` |
| V018 | figure | yes | official video 00:28:58 | `slides-images/slide-18-scaling-experts-per-training-step.jpg` |
| V019 | figure | yes | official video 00:29:44 | `slides-images/slide-19-scaling-experts-per-time.jpg` |
| V020 | figure | yes | official video 00:30:52 | `slides-images/slide-20-sparse-scaling-laws.jpg` |
| V021 | figure | yes | official video 00:31:30 | `slides-images/slide-21-expert-vs-model-parallelism.jpg` |
| V022 | figure | yes | official video 00:32:58 | `slides-images/slide-22-effective-at-small-scale.jpg` |
| V023 | figure | yes | official video 00:34:04 | `slides-images/slide-23-parameters-fixed-compute-diminishing-returns.jpg` |
| V024 | figure | yes | official video 00:36:26 | `slides-images/slide-24-contextualizing-parallelism.jpg` |
| V025 | figure | yes | official video 00:41:36 | `slides-images/slide-25-design-choices-switch-models.jpg` |
| V026 | figure | yes | official video 00:43:22 | `slides-images/slide-26-parameters-knowledge-compute-reasoning.jpg` |
| V027 | figure | yes | official video 00:43:58 | `slides-images/slide-27-upstream-quality-research-question.jpg` |
| V028 | figure | yes | official video 00:44:18 | `slides-images/slide-28-upstream-vs-superglue.jpg` |
| V029 | figure | yes | official video 00:45:20 | `slides-images/slide-29-switch-c-trillion-parameter.jpg` |
| V030 | figure | yes | official video 00:46:02 | `slides-images/slide-30-upstream-vs-triviaqa.jpg` |
| V031 | figure | yes | official video 00:46:28 | `slides-images/slide-31-fine-tuning-base-and-large.jpg` |
| V032 | figure | yes | official video 00:47:08 | `slides-images/slide-32-multilingual-training.jpg` |
| V033 | figure | yes | official video 00:47:42 | `slides-images/slide-33-distillation-techniques.jpg` |
| V034 | figure | yes | official video 00:48:24 | `slides-images/slide-34-distilling-pretrained-model.jpg` |
| V035 | figure | yes | official video 00:50:59--00:57:07 | `slides-images/slide-35-distilling-finetuned-superglue.jpg` |
| V036 | figure | yes | official video 00:57:08 | `slides-images/slide-36-wrapping-up.jpg` |
| V037 | figure | yes | official video 01:00:44 | `slides-images/slide-37-sparse-models-computer-vision.jpg` |
| V038 | figure | yes | official video 01:01:16 | `slides-images/slide-38-priority-routing-vision-moe.jpg` |
| O001 | figure | no | official video 00:00--00:06 | Stanford Engineering bumper and title transition. |
| O002 | figure | no | official video 00:06--00:01:42 | Repeated title state before the scaling-law slide. |
| O003 | figure | no | official video throughout | Progressive bullet and diagram builds; final complete teaching states retained as V001--V038. |
| O004 | figure | no | official video 00:17:16--00:25:32 | Q&A remains on V015; spoken explanations are retained as T012. |
| O005 | figure | no | official video 00:35:00--00:41:36 | Parallelism Q&A revisits related diagrams; final complete states retained as V024--V025. |
| O006 | figure | no | official video 00:49:00--00:57:04 | Distillation Q&A and repeated table navigation; final table states retained as V034--V035. |
| O007 | figure | no | official video 01:02:10--01:05:39 | Closing Q&A and end transition; teaching content retained as T020. |
| T001 | text | optional | transcript 00:00:25--00:02:35 | Scaling laws motivate sparsity as a new architectural axis. |
| T002 | text | optional | transcript 00:02:35--00:04:25 | Similar compute per input can select different weights through a router. |
| T003 | text | optional | transcript 00:04:25--00:05:05 | Translation successes did not remove complexity, communication, and instability barriers. |
| T004 | text | optional | transcript 00:05:05--00:07:20 | Sparse FFNs replace only selected Transformer feed-forward blocks. |
| T005 | text | optional | transcript 00:07:22--00:08:52 | Stable Switch training combines four engineering controls. |
| T006 | text | optional | transcript 00:08:53--00:10:21 | Router exponentiation is precision-sensitive while float32 router cost is negligible. |
| T007 | text | optional | transcript 00:10:24--00:11:20 | Smaller initialization scale is a simple stability fix. |
| T008 | text | optional | transcript 00:10:51--00:12:46 | Sparse experts need stronger fine-tuning regularization. |
| T009 | text | optional | transcript 00:12:48--00:14:36 | Load balance maps routing behavior to efficient dense hardware kernels. |
| T010 | text | optional | transcript 00:14:38--00:16:00 | Capacity factor trades token overflow against communication and memory. |
| T011 | text | optional | transcript 00:16:02--00:18:18 | No-token-left-behind is a surprising negative result. |
| T012 | text | optional | transcript 00:18:18--00:25:22 | Sparsity and adaptive computation are distinct under SPMD constraints. |
| T013 | text | optional | transcript 00:26:00--00:28:55 | Top-1 at low capacity can dominate top-2 in wall-clock Pareto efficiency. |
| T014 | text | optional | transcript 00:28:58--00:34:55 | Expert scaling shows gains, communication overhead, and diminishing returns. |
| T015 | text | optional | transcript 00:35:00--00:43:20 | Expert parallelism composes with data and model parallelism. |
| T016 | text | optional | transcript 00:43:22--00:46:26 | Knowledge-versus-reasoning statement is a hypothesis; upstream correlation has limits. |
| T017 | text | optional | transcript 00:46:28--00:48:20 | Sparse gains appear at Base/Large scale and across 101 languages. |
| T018 | text | optional | transcript 00:47:42--00:57:07 | Distillation converts a sparse teacher into a smaller deployment model with tradeoffs. |
| T019 | text | optional | transcript 00:57:08--01:02:10 | Vision MoE combines sparse weights with priority routing and capacity below one. |
| T020 | text | optional | transcript 01:02:10--01:05:39 | Q&A bounds the method by attention cost, storage, throughput, and per-weight efficiency. |
| P001 | text | optional | Jacobs et al. 1991 | Adaptive mixtures establish conditional local experts. |
| P002 | text | optional | Shazeer et al. 2017 | Sparsely-gated MoE scales conditional parameters in sequence models. |
| P003 | text | optional | Kaplan et al. 2020 | Dense neural language modeling exhibits empirical power-law scaling. |
| P004 | text | optional | Raffel et al. 2020 | T5 supplies the dense text-to-text baseline. |
| P005 | text | optional | Lepikhin et al. 2020 | GShard supplies conditional computation and automatic sharding context. |
| P006 | text | optional | Fedus et al. 2021 | Switch Transformer defines top-1 routing and the central experiments. |
| P007 | text | optional | Xue et al. 2021 | mT5 supplies the 101-language multilingual baseline. |
| P008 | text | optional | Sanh et al. 2019 | DistilBERT supplies a canonical distillation reference. |
| P009 | text | optional | Riquelme et al. 2021 | V-MoE extends sparse experts and priority routing to vision. |
| P010 | text | optional | TensorFlow Mesh repository | Mesh TensorFlow code documents the distributed MoE implementation lineage. |

## Generation Contract

- All 38 teaching slides are required visual nodes.
- Every required figure must be placed in the note with nearby explanation and concrete video-time provenance.
- Administrative frames, redundant progressive builds, and repeated Q&A navigation are intentionally omitted, but their spoken teaching content must be synthesized through T-nodes.
- Dense terminology clusters require a table or concept box.
- Foundational routing, load-balancing, capacity, and parallelism concepts require formulas or structured diagrams/tables.
- Final PDF must pass strict coverage, quality grading, two-pass XeLaTeX, and visual QA.
