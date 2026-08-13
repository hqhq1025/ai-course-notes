# Lecture 04 Blueprint

## Teaching thesis

The lecture should teach parallelism as a resource-accounting and scheduling problem. Every axis answers three questions: what tensor/state is sharded, which collective restores mathematical equivalence, and whether the resulting communication can overlap with useful compute on the available topology.

## Source mode

- Visual spine: official 106-page deck.
- Required visual nodes: 75 independent teaching states from `lecture04-selection.tsv`.
- Optional visual nodes: 31 title/divider/link/thank-you or superseded progressive-build pages.
- Teacher voice: complete 61:48 recording, including substantive Q&A after the slide talk.
- Video audit: 742 five-second samples; no deck-external teaching visual found.

## Section plan

1. Scaling pressure and resource accounting: slides 4--16.
2. Data parallelism, collectives, overlap, and ZeRO/FSDP: slides 19--46.
3. Tensor plus sequence parallelism: slides 49--69.
4. Pipeline parallelism and schedules: slides 71--77.
5. Context parallelism and Ring Attention: slides 79--86.
6. Expert parallelism, all-to-all, and hardware constraints: slides 88--97.
7. Five-dimensional composition, decision workflow, Q&A, and energy: slides 99--105.

## Required scaffolding

- First-use glossary for sharding, optimizer state, collectives, fused/overlapped communication, activation checkpointing, HBM, and device mesh.
- Formula chain for memory ownership in DP/ZeRO and communication decomposition of all-reduce.
- Matrix derivation for column/row tensor parallelism.
- Schedule interpretation for AFAB, 1F1B, DualPipe, and EP/PP overlap.
- Decision table comparing DP, TP/SP, PP, CP, and EP by sharded axis, critical collective, topology sensitivity, and use condition.
- Teacher-voice warnings that ZeRO-3, TP, CP, and EP should not be enabled merely because they exist.

## Acceptance targets

- All 75 required figures exactly once.
- At least 20 pages, 10 teaching boxes, multiple formula blocks, and captioned code.
- At least 260 prose characters per required figure on average.
- Strict coverage zero warnings, `⭐⭐⭐`, stable double XeLaTeX, and signed visual QA.
