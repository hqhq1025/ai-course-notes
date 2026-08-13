# CS25 Lecture 06 Teaching Blueprint

## Central thesis

Perceiver turns attention into a domain-general input/output interface by moving expensive self-attention from the large raw input into a small latent workspace. Perceiver IO then uses output queries to decode arbitrary structured predictions. The architecture trades some domain-specific efficiency and data efficiency for a reusable interface across images, bytes, multimodal streams, optical flow, sets, and other arrays.

## Teaching sequence

1. **Why general-purpose perception** (`V001--V002`, `T001`): sensor diversity, fragile modality-specific systems, and the practical value of one interface.
2. **What Transformers get right and where they fail** (`V003--V007`, `T002--T003`): non-locality, position as a feature, weight sharing, QKV attention, quadratic scaling, and generality-versus-speed.
3. **Perceiver's latent bottleneck** (`V008--V011`, `T004--T006`): derive self-attention and cross-attention complexity, define learned latent queries, and explain repeated latent processing.
4. **Contrasts, position, and ImageNet evidence** (`V012--V015`, `T007--T010`): ViT patch assumptions, DETR/Slot Attention precedents, Fourier encodings, permuted pixels, and data-efficiency caveats.
5. **Perceiver IO as an output-query interface** (`V016--V021`, `T011--T013`): multimodal feature standardization, encode/process/decode, image and multimodal query construction, and ImageNet refinements.
6. **Language directly from bytes** (`V022--V027`, `T014--T016`): tokenizer assumptions, masked language modeling, GLUE fine-tuning, FLOP-matched results, and attention diagnostics.
7. **Dense structured outputs via optical flow** (`V028--V036`, `T017--T019`): task definition, AutoFlow transfer, RAFT comparison, Perceiver IO decoding, EPE, qualitative vector fields, and large-output compression.
8. **Scope, related work, and research boundaries** (`V037--V039`, `T020`): generality-speed Pareto tradeoff, small data, joint multimodal training, tabular interpretation, and source reading path.

## Required pedagogical scaffolding

- Formula chain for QKV attention cost, cross-attention cost, latent self-attention, Fourier features, output-query decoding, masked-language loss, EPE, and PSNR.
- First-use terminology table for inductive bias, non-local, latent array, cross-attention, output query, Fourier feature, byte-level language, optical flow, EPE, and PSNR.
- Captioned pseudocode for Perceiver encode/process/decode and task-specific output-query construction.
- At least ten teacher-voice markers covering motivations, Q&A clarifications, surprising results, evidence boundaries, and final limitations.
- All 39 teaching slides included with concrete time provenance; final Fourier build may use the later 00:39:52 revisit while being discussed at its original 00:26:18 position.
- Dense figures receive local “读图” treatment and explicit statements of what they do not prove.
- Every major section ends with `本章小结`; the note ends with `总结与延伸` and `拓展阅读`.

## Acceptance targets

- 30+ PDF pages for a 59-minute, 39-slide technical lecture.
- 39 required figures, 10+ teaching boxes, 3+ teacher-voice markers, 3+ read-figure explanations, 3+ formulas, and captioned code.
- `check_note_coverage.py --strict` produces no warnings.
- `check_quality.sh` reports `⭐⭐⭐`.
- XeLaTeX passes twice with stable references.
- Canonical PDF QA contact sheet reviewed and checklist signed.
