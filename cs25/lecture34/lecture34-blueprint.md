# Lecture 34 Writing Blueprint

## Source boundary

- Canonical item: Stanford Online `JKbtWimlzAE`, 1:01:28, four official presenters.
- Visual source: byte-verified 123-page official deck.
- Required slides: 100; optional slides: 23 administrative, divider, QR, or closing pages.
- Teacher voice: 1,264 parsed segments from the official `en-US` manual-caption track.

## Teaching thesis

The lecture is a systems map of modern Transformer work. Architecture is only the first layer; data selection, inference-time reasoning, preference optimization, agent loops, modality interfaces, and continual adaptation each change a different part of the pipeline. The note must teach those interfaces and evidence boundaries rather than present a catalog of model names.

## Section plan

1. **Course map and Transformer foundations** — slides 1, 12, 14--22.
2. **Why data strategy matters** — slides 24--30.
3. **Small-data natural experiment** — slides 31--43.
4. **Two-phase pretraining** — slides 46--58 and 60--61.
5. **Inference-time reasoning** — slides 63--76.
6. **Preference and feedback optimization** — slides 78--83.
7. **Self-improving agents** — slides 85--90.
8. **Vision and multimodal interfaces** — slides 93--95 and 97.
9. **Transformer foundation models for fMRI** — slides 99--110.
10. **Future, scaling limits, and continual learning** — slides 111--122.

## Required scaffolding

- Embedding and attention formula chain with Q/K/V symbol definitions.
- Positional encoding and multi-head attention intuition.
- Data-strategy table separating quality, diversity, structure, scale, and phase schedule.
- TinyDialogues coverage of datasets, metrics, results, and what the study does not prove.
- Two-phase pretraining algorithm, blend table, upsampling caveat, and scaling evidence.
- CoT taxonomy: linear chain, tree, program, graph, decomposition, and self-notes.
- Preference-method table: RLHF, DPO, RLAIF, GRPO, KTO, and variational preference learning.
- Agent loop diagram/table: environment, memory, tools, reasoning, action, feedback.
- ViT/VLM/fMRI token-interface comparison.
- Continual-learning glossary distinguishing RAG, in-context memory, distillation, model editing, MoE expansion, and weight updates.

## Quality risks

- Do not count instructor biography/logistics pages as teaching coverage.
- Do not turn 100 figures into a screenshot album; every cluster needs a problem statement and follow-up synthesis.
- Do not upgrade small-study evidence into a universal human-learning or data-mixture law.
- Do not describe all post-training methods as RLHF variants.
- Do not call prompt memory or retrieval “true continual learning” without noting the instructor's stricter definition.

## Acceptance targets

- 100 required figures, each exactly once.
- 22+ teacher-voice markers, 30+ teaching boxes, 15+ formula blocks, and 4+ captioned listings.
- 260+ prose characters per figure on average.
- Strict coverage clean, `⭐⭐⭐`, double XeLaTeX, and signed visual QA.
