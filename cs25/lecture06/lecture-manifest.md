# Source Manifest: CS25 Lecture 06

Access date: 2026-08-11.

## Files

- `cover.jpg`: current Stanford Online official thumbnail.
- `metadata.json`: sanitized stable metadata for current official upload `wTZ3o36lXoQ`.
- `lecture06.en.srt`: official manual English (`en-US`) captions, 1,399 parsed captions.
- `transcript_timed.txt`: timestamp-preserving transcript.
- `transcript_clean.txt`: five-minute transcript digest for source review.
- `lecture06.mp4`: local ignored 1080p current official recording used for slide recovery.
- `slides-images/`: 39 reviewed teaching slides or final progressive-build states.

## Supplementary Source Materials

- `source-materials/SOURCES.md`: official sources, primary papers, and source-boundary notes.
- `lecture06-teacher-voice-ledger.md`: motivations, Q&A clarifications, surprising results, and planned placement.
- `lecture06-blueprint.md`: teaching thesis, section sequence, and acceptance targets.
- `lecture06-coverage.md`: source-node treatment matrix.

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | official video 00:00:58 | `slides-images/slide-01-why-understand-all-modalities.jpg` |
| V002 | figure | yes | official video 00:02:58 | `slides-images/slide-02-why-unified-systems.jpg` |
| V003 | figure | yes | official video 00:05:10 | `slides-images/slide-03-improving-transformers.jpg` |
| V004 | figure | yes | official video 00:06:02 | `slides-images/slide-04-standard-qkv-attention.jpg` |
| V005 | figure | yes | official video 00:08:02 | `slides-images/slide-05-why-non-locality.jpg` |
| V006 | figure | yes | official video 00:08:38 | `slides-images/slide-06-why-featurize-position.jpg` |
| V007 | figure | yes | official video 00:09:30 | `slides-images/slide-07-scalability-vs-generality.jpg` |
| V008 | figure | yes | official video 00:09:42 | `slides-images/slide-08-perceiver-title.jpg` |
| V009 | figure | yes | official video 00:10:40 | `slides-images/slide-09-self-attention-scales-poorly.jpg` |
| V010 | figure | yes | official video 00:16:16 | `slides-images/slide-10-cross-attention-linear-scaling.jpg` |
| V011 | figure | yes | official video 00:19:00 | `slides-images/slide-11-perceiver-architecture.jpg` |
| V012 | figure | yes | official video 00:21:42 | `slides-images/slide-12-contrast-vit.jpg` |
| V013 | figure | yes | official video 00:22:56 | `slides-images/slide-13-cross-attention-detr.jpg` |
| V014 | figure | yes | official video 00:26:18; final build revisited 00:39:52 | `slides-images/slide-14-fourier-position-encodings.jpg` |
| V015 | figure | yes | official video 00:29:34 | `slides-images/slide-15-imagenet-permuted-classification.jpg` |
| V016 | figure | yes | official video 00:33:50 | `slides-images/slide-16-featurizing-multimodality.jpg` |
| V017 | figure | yes | official video 00:40:32 | `slides-images/slide-17-basic-perceiver-architecture.jpg` |
| V018 | figure | yes | official video 00:41:34 | `slides-images/slide-18-perceiver-io-architecture.jpg` |
| V019 | figure | yes | official video 00:42:04 | `slides-images/slide-19-constructing-output-queries.jpg` |
| V020 | figure | yes | official video 00:43:00 | `slides-images/slide-20-multimodal-query-construction.jpg` |
| V021 | figure | yes | official video 00:43:06 | `slides-images/slide-21-imagenet-results.jpg` |
| V022 | figure | yes | official video 00:43:44 | `slides-images/slide-22-language-tokenization.jpg` |
| V023 | figure | yes | official video 00:45:14 | `slides-images/slide-23-why-remove-tokenizers.jpg` |
| V024 | figure | yes | official video 00:45:38 | `slides-images/slide-24-masked-language-modeling.jpg` |
| V025 | figure | yes | official video 00:45:54 | `slides-images/slide-25-glue-finetuning.jpg` |
| V026 | figure | yes | official video 00:47:18 | `slides-images/slide-26-language-from-bytes-results.jpg` |
| V027 | figure | yes | official video 00:48:00 | `slides-images/slide-27-language-attention-patterns.jpg` |
| V028 | figure | yes | official video 00:48:44 | `slides-images/slide-28-optical-flow-definition.jpg` |
| V029 | figure | yes | official video 00:49:16 | `slides-images/slide-29-optical-flow-transfer-task.jpg` |
| V030 | figure | yes | official video 00:50:06 | `slides-images/slide-30-raft-comparison.jpg` |
| V031 | figure | yes | official video 00:50:48 | `slides-images/slide-31-perceiver-io-optical-flow.jpg` |
| V032 | figure | yes | official video 00:51:14 | `slides-images/slide-32-optical-flow-results.jpg` |
| V033 | figure | yes | official video 00:51:38 | `slides-images/slide-33-qualitative-optical-flow-animals.jpg` |
| V034 | figure | yes | official video 00:51:50 | `slides-images/slide-34-qualitative-optical-flow-skater.jpg` |
| V035 | figure | yes | official video 00:52:20 | `slides-images/slide-35-decoding-very-large-outputs.jpg` |
| V036 | figure | yes | official video 00:53:06 | `slides-images/slide-36-quantitative-autoencoding.jpg` |
| V037 | figure | yes | official video 00:56:14 | `slides-images/slide-37-general-perception-summary.jpg` |
| V038 | figure | yes | official video 00:56:22 | `slides-images/slide-38-references.jpg` |
| V039 | figure | yes | official video 00:58:50 | `slides-images/slide-39-thank-you-and-papers.jpg` |
| O001 | figure | no | official video 00:00--00:02 | Stanford bumper and progressive motivation builds; V001 retains the complete teaching state. |
| O002 | figure | no | official video 00:01:54--00:02:58 | Progressive unified-system animation; V002 retains the complete state. |
| O003 | figure | no | official video 00:08:44 | Pure “Scalability vs. generality?” divider; V007 retains the completed comparison. |
| O004 | figure | no | official video 00:21:48--00:23:14 | Progressive DETR/Slot Attention builds and ImageNet divider; V013 retains the complete cross-attention examples. |
| O005 | figure | no | official video 00:23:16--00:40:32 | Q&A navigation repeatedly revisits Perceiver, ViT, DETR, Fourier, ImageNet and multimodality slides; final required states are retained once. |
| O006 | figure | no | official video 00:41:56--00:42:04 | Partial query construction build; V019 retains the complete state. |
| O007 | figure | no | official video 00:51:16--00:52:14 | Optical-flow videos produce many intermediate animation frames; V033--V034 retain two distinct complete examples. |
| O008 | figure | no | official video 00:53:20--00:56:14 | Summary/Q&A navigation revisits optical-flow results and decoder slides; V037 retains the final summary build. |
| O009 | figure | no | official video 00:58:56 | Stanford end bumper. |
| T001 | text | optional | transcript 00:00:17--00:02:58 | Hand-designed inductive biases cannot scale to every modality; unified systems reduce fragility. |
| T002 | text | optional | transcript 00:03:00--00:05:10 | Transformers are non-local, positional-feature based, weight-shared and hardware friendly, but scale poorly. |
| T003 | text | optional | transcript 00:05:10--00:09:30 | Generality and domain-specific speed form a Pareto tradeoff. |
| T004 | text | optional | transcript 00:10:40--00:16:16 | Self-attention makes large raw inputs prohibitively expensive. |
| T005 | text | optional | transcript 00:16:16--00:19:00 | Cross-attention gives linear input scaling when latent count is fixed. |
| T006 | text | optional | transcript 00:19:00--00:21:42 | Latents are learned; repeated processing and positional concatenation matter. |
| T007 | text | optional | transcript 00:21:42--00:23:12 | ViT uses image-specific patching, while DETR and Slot Attention already use cross-attention bottlenecks. |
| T008 | text | optional | transcript 00:23:12--00:30:01 | Q&A clarifies residuals, latent self-attention, hybrid architectures, and unsolved hierarchical variants. |
| T009 | text | optional | transcript 00:26:18--00:29:34 | Fourier positions and concatenation preserve weak structural assumptions. |
| T010 | text | optional | transcript 00:29:34--00:39:58 | Permuted ImageNet remains competitive, but learning structure from data is costly. |
| T011 | text | optional | transcript 00:33:48--00:40:32 | Modality and position tags standardize heterogeneous arrays. |
| T012 | text | optional | transcript 00:40:32--00:41:34 | Basic Perceiver predicts a compact output; Perceiver IO decodes structured outputs. |
| T013 | text | optional | transcript 00:41:34--00:43:06 | Output queries specify prediction identity, position, modality and task. |
| T014 | text | optional | transcript 00:43:44--00:45:38 | Tokenizers encode language-specific assumptions; bytes offer a common alphabet with longer sequences. |
| T015 | text | optional | transcript 00:45:38--00:48:00 | Byte-level masked language modeling and GLUE remain competitive at matched FLOPs. |
| T016 | text | optional | transcript 00:48:00--00:48:44 | Byte attention patterns are diagnostic, not proof of linguistic concepts. |
| T017 | text | optional | transcript 00:48:44--00:50:48 | Optical flow is a dense-output transfer problem with scarce realistic labels. |
| T018 | text | optional | transcript 00:50:32--00:51:14 | Weak-bias Perceiver IO was expected to overfit but worked without RAFT's hand-designed hierarchy. |
| T019 | text | optional | transcript 00:51:14--00:55:02 | EPE datasets, synthetic-to-real transfer and ground-truth construction require careful reading. |
| T020 | text | optional | transcript 00:55:02--00:58:53 | General fallback, speed tradeoff, small-data limit, joint multimodal future and tabular interpretation. |
| P001 | text | optional | Jaegle et al. 2021 | Perceiver defines the latent bottleneck and iterative attention. |
| P002 | text | optional | Jaegle et al. 2021 | Perceiver IO defines output-query decoding for structured outputs. |
| P003 | text | optional | Vaswani et al. 2017 | Standard Transformer QKV attention supplies the baseline. |
| P004 | text | optional | Dosovitskiy et al. 2020 | ViT supplies the image-patch Transformer comparison. |
| P005 | text | optional | Carion et al. 2020 | DETR demonstrates query-based cross-attention in object detection. |
| P006 | text | optional | Locatello et al. 2020 | Slot Attention demonstrates learned slots for object-centric grouping. |
| P007 | text | optional | Tancik et al. 2020 | Fourier features motivate high-frequency coordinate encodings. |
| P008 | text | optional | Devlin et al. 2018 | BERT supplies the masked-language and GLUE baseline. |
| P009 | text | optional | Clark et al. 2021 | CANINE supplies a tokenization-free language comparison. |
| P010 | text | optional | Xue et al. 2021 | ByT5 supplies a byte-level pretraining comparison. |
| P011 | text | optional | Teed and Deng 2020 | RAFT supplies the optical-flow state-of-the-art comparison. |
| P012 | text | optional | Sun et al. 2021 | AutoFlow supplies the synthetic training distribution. |
| P013 | text | optional | Wang et al. 2018 | GLUE supplies the language-understanding evaluation suite. |

## Generation Contract

- All 39 teaching slides are required visual nodes.
- Every required figure must appear with nearby prose-led explanation and concrete current-video time provenance.
- Administrative frames, duplicate progressive builds, repeated Q&A navigation, and intermediate optical-flow video frames are omitted intentionally; spoken teaching content remains required through T-nodes.
- Dense terminology clusters require a table or concept box; attention complexity, output queries, byte language, EPE, and PSNR require formulas or structured scaffolding.
- Final PDF must pass strict coverage, quality grading, two-pass XeLaTeX, and visual QA.
