# Lecture 05 Blueprint

## Goal
Regenerate Lecture 05 as a slide-complete GPU performance note. The note should teach how GPU architecture, memory hierarchy, arithmetic intensity, low precision, fusion, recomputation, coalescing, tiling, and FlashAttention connect.

## Section Plan

1. GPU scale and hardware model: slides 001-018.
2. Performance model and low precision: slides 019-028.
3. Operator fusion and recomputation: slides 029-035.
4. Memory coalescing, tiling, and matrix performance anomalies: slides 036-048.
5. FlashAttention as IO-aware attention: slides 049-054.
6. Summary: slide 055.

## Required Glossary
SM, SP/CUDA core, warp, thread block, register, shared memory/SRAM, global memory/DRAM/HBM, tensor core, roofline, arithmetic intensity, memory-bound, compute-bound, low precision, operator fusion, recomputation, memory coalescing, tiling, wave quantization, online softmax, FlashAttention.

## QA Requirements
- Every slide image 001-055 appears in the note.
- Important diagrams and plots have `读图` explanations.
- LaTeX log has no missing-character warnings.
- Visual PDF QA contact sheet generated and reviewed.
