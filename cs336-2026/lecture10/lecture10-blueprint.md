# Lecture 10 Blueprint

Status: implemented under the new source-first workflow on 2026-05-12.

## Goal

Regenerate Lecture 10 as a source-node-complete note on inference, KV cache, lossy/lossless shortcuts, and LLM serving systems. The note should explain inference as a memory-bound dynamic workload rather than a simple deployment afterthought.

## Section Plan

1. Lecture 10: inference overview and schema.
2. Understanding the inference workload: metrics, Transformer notation, arithmetic intensity, KV cache, prefill/generation.
3. Taking shortcuts (lossy): GQA, MLA, CLA, local/hybrid attention, DeepSeek attention, quantization/AWQ, pruning/distillation.
4. Use shortcuts but double check (lossless): speculative sampling.
5. Handling dynamic workloads: continuous batching and selective batching.
6. PagedAttention and KV-cache memory management.
7. 总结与延伸.

## Required Treatment

- Include every local teaching PNG from `images/` that corresponds to source image nodes.
- Add nearby `读图` explanations for all important diagrams, tables, and result figures.
- Explain first-use terms: HBM, KV cache, TTFT, latency, throughput, arithmetic intensity, prefill, generation, GQA, MQA, MLA, CLA, AWQ, QAT, PTQ, GPTQ, speculative sampling, continuous batching, selective batching, PagedAttention.
- Explain formulas and symbols for arithmetic intensity and KV-cache memory.
- Perform visual PDF QA after compilation.
