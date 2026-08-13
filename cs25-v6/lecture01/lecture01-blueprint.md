# Lecture 01 Writing Blueprint

## Source boundary

- Canonical item: Stanford Online `bHSDPgZYie0`, 1:16:46, presented by Steven Feng and Karan Singh.
- Visual source: official 156-page V6 overview deck.
- Required slides: 116; optional slides: 40 administrative, divider, QR/title, repeated, progressive, or closing pages.
- Teacher voice: 1,558 parsed segments from the official `en-US` manual-caption track.
- Full-recording audit: 194 stable high-recall candidates; no independent deck-external teaching visual.

## Teaching thesis

The lecture is not merely “how attention works.” It presents a dependency map for modern Transformer systems: representation and sequence modeling establish the architecture; pretraining data determines what is learnable; post-training and inference-time computation shape behavior; agents and multimodal systems wrap the model in loops and interfaces; hallucination, memory, interpretability, alignment, world models, and state-space models expose where the current paradigm is incomplete. The note must teach these interfaces and evidence boundaries rather than repeat a catalog of names.

## Section plan

1. **From hand-engineered features to self-supervision** — slides 11, 13--18, and 20--22.
2. **Embeddings, recurrence, and the Transformer mechanism** — slides 23--33.
3. **Why data strategy is part of the model** — slides 35--37.
4. **Baby Scale and bilingual BabyLM** — slides 39--50 and 52--66, excluding repeated question cards.
5. **Retrieval and curriculum as two scaling axes** — slides 68, 70--72, 75--81, and 84--86.
6. **Reasoning and preference optimization** — slides 88--100.
7. **Self-improving agents as closed loops** — slides 102--107.
8. **Vision and neuroscience applications** — slides 109, 111--112, 114--115, and 117--118.
9. **Future capabilities, scaling limits, and hallucination** — slides 121--125, 127--128, and 130--137.
10. **Memory, continual learning, interpretability, and alignment** — slides 139--143 and 145--149.
11. **Beyond Transformers: JEPA/world models and SSMs** — slides 151--155.

## Required scaffolding

- Compact comparison of hand-engineered, supervised, and self-supervised learning.
- Formula chain for self-attention, multi-head attention, positional information, and recurrent versus parallel computation.
- First-use explanations of tokenization, embedding, contextual representation, KV roles, retrieval augmentation, curriculum, and post-training.
- Data-strategy table distinguishing selection, ordering, retrieval, curriculum, and parameter growth.
- Baby Scale and bilingual BabyLM result tables with explicit sample-size and transfer limits.
- RAG compute-allocation model that separates parametric learning from external memory.
- Terminology digest for CoT, ToT, Program-of-Thought, Socratic decomposition, RLHF, DPO, RLAIF, GRPO, and process supervision.
- Agent-loop diagram and failure-mode table for refinement, reflection, ReAct, memory, tools, and feedback.
- ViT/CLIP/fMRI interface comparison.
- Formal hallucination framework with reference world `W`, visible world `V`, and conflict policy `P`.
- Memory taxonomy separating context, retrieval, summaries, external stores, model editing, and parameter-level continual learning.
- Alignment table distinguishing outcome supervision, process supervision, constitutional rules, scalable oversight, and interpretability.
- JEPA/world-model/SSM comparison with honest tradeoffs and dated April 2026 evidence boundaries.

## Quality risks

- Do not turn 116 figures into a screenshot album; every cluster needs a motivating question, local explanation, and synthesis.
- Do not generalize small-model or child-language studies into universal human-learning laws.
- Do not treat RAG as free context or a substitute for all pretraining; show the compute and retrieval-quality tradeoff.
- Do not collapse all preference methods into RLHF or all agent loops into autonomous intelligence.
- Do not call every factual error a hallucination; preserve the lecture's world-model definition and separate planning errors.
- Do not call prompt memory, retrieval, or occasional weight editing “true continual learning” without the instructors' caveat.
- Do not frame JEPA or SSMs as proven Transformer replacements; the lecture presents research directions and tradeoffs.

## Acceptance targets

- 116 required figures, each exactly once.
- 25+ teacher-voice markers, 35+ teaching boxes, 20+ formula blocks, and 5+ captioned listings.
- At least 260 prose characters per figure on average.
- Strict coverage clean, `⭐⭐⭐`, stabilized double XeLaTeX, and signed visual QA.
