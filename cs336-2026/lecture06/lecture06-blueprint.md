# Lecture 06 Blueprint

## Goal
Regenerate Lecture 06 as a source-complete note on benchmarking, profiling, and writing kernels with Triton.

## Sections
1. GPU recap: hardware, programming model, warps, occupancy, bank conflicts, coalescing, block occupancy.
2. Benchmarking and profiling: wall-clock vs attribution, CUDA synchronization, torch profiler, Nsight.
3. GeLU case study: naive vs builtin vs compiled.
4. Triton mental model: blocks, programs, masks, pointer arithmetic.
5. Triton kernels: GeLU, softmax, row sum, tiled matmul+ReLU.
6. Summary and connections to multi-GPU parallelism.

## Required Glossary
SM, warp, thread block/CTA, grid, shared memory, bank conflict, memory coalescing, occupancy, block occupancy, CUDA event/synchronize, profiler, kernel launch, Triton program, block size, mask, stride, tiling, fusion.
