# Lecture 07 Blueprint

Status: implemented under the new source-first workflow on 2026-05-12.

The final note follows this blueprint and adds explicit `读图` blocks, first-use glossary explanations, collective-operation tables, bandwidth formulas, and code walkthroughs for the official PyTorch distributed examples.

## Goal
Regenerate Lecture 07 as a source-node-complete note on distributed communication and multi-GPU training. It should teach collectives, hardware topology, PyTorch distributed, communication benchmarking, and data/tensor/pipeline parallelism.

## Required Glossary
rank, world size, process group, collective, broadcast, scatter, gather, reduce, all-gather, reduce-scatter, all-reduce, all-to-all, bandwidth, latency, RDMA, InfiniBand, RoCE, NCCL, data parallelism, tensor parallelism, pipeline parallelism, microbatch, pipeline bubble.

## Sections
1. Distributed training mental model.
2. Collective operations and diagrams.
3. Hardware topology and NCCL.
4. PyTorch distributed and benchmarking.
5. Data parallelism.
6. Tensor parallelism.
7. Pipeline parallelism.
8. Summary and connection to FSDP/ZeRO in later lectures.
