# Lecture 12 Blueprint

Status: rewritten under the prose-led / teacher-voice workflow on 2026-05-13.

## Goal

Generate Lecture 12 as a source-node-complete note on evaluation: what it means for a model to be good, perplexity, exam/chat/agentic/reasoning/safety benchmarks, realism, validity, and how to reason about evaluation rules.

## Section Plan

1. Evaluation as construct-to-metric translation.
2. What is good: benchmarks, cost, preference, usage.
3. Perplexity and probability-based evaluation.
4. Exam benchmarks: MMLU, MMLU-Pro, GPQA, HLE.
5. Chat benchmarks: Arena, AlpacaEval, WildBench.
6. Agentic benchmarks: SWE-Bench, TerminalBench, CyBench, MLE-Bench, scaffolds.
7. Pure reasoning, safety, realism, validity.
8. How to think about evaluation.

## Required Treatment

- Localize and include every source image asset referenced by `lecture12-slides.py`.
- Add nearby `读图` explanations for important leaderboards, benchmark examples, result tables, pipelines, and diagrams.
- Explain first-use terms: perplexity, zero-shot, ELO, LLM judge, agent scaffold, ecological validity, train-test overlap, contamination, private/fresh evals.
- Preserve teacher voice: why there is no one true evaluation, why benchmark difficulty differs from realism, why Arena is real but biased, why agent benchmarks evaluate model + scaffold, and why validity is a trust problem.
- Add transition prose before every major benchmark family and synthesis prose after dense figure clusters.
- Perform visual PDF QA after compilation.
