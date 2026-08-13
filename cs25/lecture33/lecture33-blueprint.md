# Lecture 33 Writing Blueprint

## Source boundary

- Canonical item: official standalone video `orDKvo8h71o`, 36:30, uploaded 2024-06-11.
- Teaching deck: 67-page official Hyung Won Chung Google Slides export.
- Visual treatment: 47 required pages and 20 optional progressive/divider pages.
- Spoken treatment: use only the standalone 376-caption track. Exclude Q\&A-only material from the combined Lecture 27 upload.

## Teaching thesis

The talk is not a claim that decoder-only is eternally optimal. It teaches a reusable method: identify the dominant force in a changing field, understand how existing structures interact with that force, and revisit inductive biases when the operating regime changes. Transformer history is the worked example.

## Section plan

1. **研究变化本身** — slides 1--4 and 6; define dominant-force simplification and its evidence limits.
2. **Compute 与 Bitter Lesson** — slides 7--10 and 13--16; separate short-run efficiency from long-run scalability.
3. **三类 Transformer 的共同底座** — slides 17--18, 21--23, 25, 27--28, 32, and 37; define tokenization, embeddings, attention roles, and architecture interfaces on first use.
4. **四步架构变换** — slides 40--42, 44--45, 47--48, and 50--51; derive one local change at a time and explain what assumption disappears.
5. **历史任务为何奖励额外结构** — slides 52--58; use translation and FLAN as natural experiments, preserving empirical versus hypothesized explanations.
6. **表示粒度、双向性与缓存** — slides 59--64 and 66; connect layer depth, causal invariance, KV cache reuse, and multi-turn serving cost.
7. **总结与迁移** — slide 67; compress the method into a research checklist, self-test, and primary-source reading list.

## Required derivations and scaffolding

- Falling-pen dominant-force model with every symbol explained.
- Compute-cost trend as a historical observation, not a guaranteed law.
- Inductive-bias lifecycle diagram/table distinguishing current-regime gain from scale ceiling.
- Encoder-decoder attention roles: bidirectional self-attention, causal self-attention, and cross-attention.
- Four-step encoder-decoder to decoder-only transformation table.
- KV-cache complexity comparison for bidirectional re-encoding versus causal incremental decoding.
- First-use definitions for tokenization, embedding, cross-attention, causal mask, inductive bias, and KV cache.

## Quality risks

- Do not repeat Lecture 27's Jason Wei content merely because the deck was previously paired with it.
- Do not retain the old note's unsupported claim that every modern architecture choice follows directly from the Bitter Lesson.
- Do not upgrade the FLAN and bidirectionality anecdotes into universal causal proof.
- Do not include optional progressive frames unless they add a distinct teaching state.
- Do not end with the combined video's Q\&A about MLE/RLHF; it is outside this official standalone edit.

## Acceptance targets

- 47 required figures, each exactly once.
- 14+ teacher-voice markers.
- 20+ pages, 10+ teaching boxes, formulas with symbol explanations, and captioned code/listing examples where useful.
- Strict coverage clean, `⭐⭐⭐`, double XeLaTeX, and signed visual QA.
