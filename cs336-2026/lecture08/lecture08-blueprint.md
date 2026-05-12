# Lecture 08 Blueprint

Status: implemented under the new source-first workflow on 2026-05-12.

## Goal

Regenerate Lecture 08 as a slide-complete note on Parallelism Basics. The note should explain why large-scale LLM training needs datacenter-level networking, how ZeRO/FSDP and model-parallel primitives work, and how recent large models combine DP/TP/SP/EP/PP/CP.

## Section Plan

1. 本讲主线：state and communication ledger.
2. Part 1: networking basics for LLMs, slides 001-013.
3. Part 2: standard LLM parallelization primitives, slides 014-056.
4. Part 3: 3D/4D parallelism and recent model configurations, slides 057-073.
5. 总结与延伸.

## Required Treatment

- Include every slide image `slide-001.jpg` through `slide-073.jpg`.
- Add nearby `读图`/`读表`/`读公式` explanation for every important slide.
- Explain first-use terms: collectives, sharding, ZeRO, FSDP, HBM, sequence parallel, expert parallel, context parallel, pipeline bubble.
- Explain formulas and symbols for memory accounting, all-reduce decomposition, SGD, pipeline bubble, and activation memory.
- Perform visual PDF QA after compilation.
