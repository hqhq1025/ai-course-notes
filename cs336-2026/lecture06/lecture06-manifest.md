# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture06`

## Files

- `lecture06-notes.pdf`
- `lecture06-notes.tex`
- `lecture06-slides.py`

## Local Visual Assets

- `images/block-occupancy.png`
- `images/cuda-grid.png`
- `images/gemm_tiled.png`
- `images/gpu-execution-model.jpg`
- `images/gpu-hardware.png`
- `images/online-softmax.jpg`
- `images/roofline.jpg`
- `images/tiling-math.jpg`
- `images/triton-row-sum.png`
- `images/triton-softmax.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | text | optional | `lecture06-slides.py:main` | Last lecture: high-level overview of GPUs and performance |
| py-002 | text | optional | `lecture06-slides.py:main` | This lecture: benchmarking/profiling + writing kernels |
| py-003 | text | optional | `lecture06-slides.py:main` | Summary: |
| py-004 | text | optional | `lecture06-slides.py:main` | - Know the programming model (PyTorch, Triton, PTX) to give you correctness |
| py-005 | text | optional | `lecture06-slides.py:main` | - Understand the hardware (SMs, warps, occupancy, bank conflicts, etc.) to optimize performance |
| py-006 | text | optional | `lecture06-slides.py:main` | - Benchmark to understand scaling |
| py-007 | text | optional | `lecture06-slides.py:main` | - Profile to see what's being executed for how long |
| py-008 | text | optional | `lecture06-slides.py:main` | - Triton: think in terms of thread blocks (read to shared memory, do stuff (fusion), write ba... |
| py-009 | text | optional | `lecture06-slides.py:main` | - Examples: GeLU (elementwise), softmax (row-wise), row sum (baby tiling), matmul (tiling) |
| py-010 | text | optional | `lecture06-slides.py:main` | Next time: more than one GPU! |
| py-011 | section | yes | `lecture06-slides.py:review_of_gpus` | Hardware |
| py-012 | figure | yes | `lecture06-slides.py:review_of_gpus` | images/gpu-hardware.png |
| py-013 | text | optional | `lecture06-slides.py:review_of_gpus` | \| Accelerator \| A100 \| H100 \| B200 \| |
| py-014 | text | optional | `lecture06-slides.py:review_of_gpus` | +------------------------------------+-----------+-----------+-----------+ |
| py-015 | text | optional | `lecture06-slides.py:review_of_gpus` | \| # SMs \| 108 \| 132 \| 148 \| |
| py-016 | text | optional | `lecture06-slides.py:review_of_gpus` | +------------------------------------+-----------+-----------+-----------+ |
| py-017 | text | optional | `lecture06-slides.py:review_of_gpus` | \| Register size (per SM) \| 256 KB \| 256 KB \| 256 KB \| |
| py-018 | text | optional | `lecture06-slides.py:review_of_gpus` | \| L1 cache + shared memory (per SM) \| 192 KB \| 256 KB \| 256 KB \| |
| py-019 | text | optional | `lecture06-slides.py:review_of_gpus` | \| L2 cache size \| 40 MB \| 50 MB \| 96-126 MB \| |
| py-020 | text | optional | `lecture06-slides.py:review_of_gpus` | \| HBM size \| 80 GB \| 80 GB \| 192 GB \| |
| py-021 | text | optional | `lecture06-slides.py:review_of_gpus` | +------------------------------------+-----------+-----------+-----------+ |
| py-022 | text | optional | `lecture06-slides.py:review_of_gpus` | \| Register bandwidth \| ~116 TB/s \| ~401 TB/s \| ~447 TB/s \| |
| py-023 | text | optional | `lecture06-slides.py:review_of_gpus` | \| L1 cache + shared memory bandwidth \| ~19 TB/s \| ~33 TB/s \| ~19 TB/s \| |
| py-024 | text | optional | `lecture06-slides.py:review_of_gpus` | \| L2 cache bandwidth \| ~5-8 TB/s \| ~12 TB/s \| ~9 TB/s \| |
| py-025 | text | optional | `lecture06-slides.py:review_of_gpus` | \| HBM bandwidth \| 2 TB/s \| 3.35 TB/s \| 8 TB/s \| |
| py-026 | text | optional | `lecture06-slides.py:review_of_gpus` | (B200s also have tensor memory (TMEM) for tensor cores (between registers and shared memory) ... |
| py-027 | section | yes | `lecture06-slides.py:review_of_gpus` | Programming model |
| py-028 | figure | yes | `lecture06-slides.py:review_of_gpus` | https://docs.nvidia.com/cuda/parallel-thread-execution/_images/grid-with-CTAs.png |
| py-029 | text | optional | `lecture06-slides.py:review_of_gpus` | - *Thread*: executes code on a small part of the data |
| py-030 | text | optional | `lecture06-slides.py:review_of_gpus` | - *Thread block* or concurrent thread array (CTA): a group of threads |
| py-031 | text | optional | `lecture06-slides.py:review_of_gpus` | - *Grid*: collection of thread blocks |
| py-032 | text | optional | `lecture06-slides.py:review_of_gpus` | (H100s and B200s also have thread block clusters that enable distributed shared memory.) |
| py-033 | text | optional | `lecture06-slides.py:review_of_gpus` | Why thread blocks? |
| py-034 | text | optional | `lecture06-slides.py:review_of_gpus` | For elementwise operations (e.g., GeLU), threads are most natural: each thread processes one ... |
| py-035 | text | optional | `lecture06-slides.py:review_of_gpus` | - f(i) for i = 0, ..., N-1 |
| py-036 | text | optional | `lecture06-slides.py:review_of_gpus` | However, for non-elementwise operations like softmax or matrix multiplication, threads need t... |
| py-037 | text | optional | `lecture06-slides.py:review_of_gpus` | Reading/writing from HBM is slow, so use shared memory (local to SM). |
| py-038 | text | optional | `lecture06-slides.py:review_of_gpus` | Thread block: a collection of threads that access the same shared memory. |
| py-039 | text | optional | `lecture06-slides.py:review_of_gpus` | Consequently, a thread block is scheduled on one SM. |
| py-040 | text | optional | `lecture06-slides.py:review_of_gpus` | In Triton, think natively in terms of thread blocks (later). |
| py-041 | section | yes | `lecture06-slides.py:review_of_gpus` | Interaction between programming model and hardware |
| py-042 | text | optional | `lecture06-slides.py:review_of_gpus` | Programming model provides an abstraction of the hardware. |
| py-043 | text | optional | `lecture06-slides.py:review_of_gpus` | In principle, don't need to think about anything else (for correctness). |
| py-044 | text | optional | `lecture06-slides.py:review_of_gpus` | In practice, performance is very sensitive to the hardware, so need to understand it to obtai... |
| py-045 | text | optional | `lecture06-slides.py:review_of_gpus` | Let's go over some considerations. |
| py-046 | text | optional | `lecture06-slides.py:review_of_gpus` | **Warps**: |
| py-047 | text | optional | `lecture06-slides.py:review_of_gpus` | - Within a thread block, threads are grouped into warps (32 threads per warp). |
| py-048 | text | optional | `lecture06-slides.py:review_of_gpus` | - Example: thread block has 64 threads => it has 2 warps. |
| py-049 | text | optional | `lecture06-slides.py:review_of_gpus` | \| TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT \| TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT \| |
| py-050 | text | optional | `lecture06-slides.py:review_of_gpus` | - All threads within a warp must execute same instructions in lockstep on an SM. |
| py-051 | text | optional | `lecture06-slides.py:review_of_gpus` | - Control divergence: if different threads in a warp need to execute different instructions (... |
| py-052 | text | optional | `lecture06-slides.py:review_of_gpus` | \| AAAAAAAAA....................... \| |
| py-053 | text | optional | `lecture06-slides.py:review_of_gpus` | \| .........BBBBBBBBBBBBBBBBBBBBBBB \| |
| py-054 | text | optional | `lecture06-slides.py:review_of_gpus` | - SM runs multiple warps and switches between them (e.g., when one warp is blocked on HBM rea... |
| py-055 | text | optional | `lecture06-slides.py:review_of_gpus` | **(Warp) occupancy**: |
| py-056 | text | optional | `lecture06-slides.py:review_of_gpus` | - Each thread can use between 0 and 255 registers. |
| py-057 | text | optional | `lecture06-slides.py:review_of_gpus` | - The more registers threads use, the fewer threads can be scheduled on an SM (low occupancy). |
| py-058 | text | optional | `lecture06-slides.py:review_of_gpus` | - Low occupancy isn't necessarily bad if each thread is doing more work. |
| py-059 | text | optional | `lecture06-slides.py:review_of_gpus` | - Example: thread coarsening (each thread processes multiple elements). |
| py-060 | text | optional | `lecture06-slides.py:review_of_gpus` | - Example: thread block has 64 threads, each using 160 registers, SM has 65536 registers |
| py-061 | text | optional | `lecture06-slides.py:review_of_gpus` | **Bank conflicts** (shared memory): |
| py-062 | text | optional | `lecture06-slides.py:review_of_gpus` | - Shared memory is divided into 32 banks, each 4 bytes wide. |
| py-063 | text | optional | `lecture06-slides.py:review_of_gpus` | B00 B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14 B15 B16 B17 B18 B19 B20 B21 B22 B... |
| py-064 | text | optional | `lecture06-slides.py:review_of_gpus` | ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... .... |
| py-065 | text | optional | `lecture06-slides.py:review_of_gpus` | ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... .... |
| py-066 | text | optional | `lecture06-slides.py:review_of_gpus` | ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... .... |
| py-067 | text | optional | `lecture06-slides.py:review_of_gpus` | - Each cycle, each bank can only be accessed by one thread (if not the same exact location). |
| py-068 | text | optional | `lecture06-slides.py:review_of_gpus` | - If multiple threads access the same bank, accesses serialized (bank conflict). |
| py-069 | text | optional | `lecture06-slides.py:review_of_gpus` | - Worst case example: matrix where each row spans all banks; 32 threads accessing first colum... |
| py-070 | text | optional | `lecture06-slides.py:review_of_gpus` | - Unavoidable: when doing matmul A @ B, access rows of A and columns of B |
| py-071 | text | optional | `lecture06-slides.py:review_of_gpus` | - Solution: swizzling rearranges shared memory (e.g., row xor col) to avoid bank conflicts |
| py-072 | text | optional | `lecture06-slides.py:review_of_gpus` | **Memory coalescing** (HBM): |
| py-073 | text | optional | `lecture06-slides.py:review_of_gpus` | - When the 32 threads in a warp access HBM, memory accesses combined into transactions of 128... |
| py-074 | text | optional | `lecture06-slides.py:review_of_gpus` | M00 M01 M02 M03 M04 M05 M06 M07 M08 M09 M10 M11 M12 M13 M14 M15 M16 M17 M18 M19 M20 M21 M22 M... |
| py-075 | text | optional | `lecture06-slides.py:review_of_gpus` | M32 M33 M34 M35 M36 M37 M38 M39 M40 M41 M42 M43 M44 M45 M46 M47 M48 M49 M50 M51 M52 M53 M54 M... |
| py-076 | text | optional | `lecture06-slides.py:review_of_gpus` | - Best case: full coalescing, all threads access the same cache line (32 threads x 4 bytes = ... |
| py-077 | text | optional | `lecture06-slides.py:review_of_gpus` | **Block occupancy**: |
| py-078 | figure | yes | `lecture06-slides.py:review_of_gpus` | https://developer-blogs.nvidia.com/wp-content/uploads/2019/06/pasted-image-0.png |
| py-079 | text | optional | `lecture06-slides.py:review_of_gpus` | - Thread blocks scheduled onto SMs in waves. |
| py-080 | text | optional | `lecture06-slides.py:review_of_gpus` | - B200 has 148 SMs, if we launch 160 thread blocks, first wave has 148 blocks, second wave ha... |
| py-081 | text | optional | `lecture06-slides.py:review_of_gpus` | - Wave quantization problem: last wave has fewer thread blocks, leaving some SMs idle (low bl... |
| py-082 | text | optional | `lecture06-slides.py:review_of_gpus` | - Solution: make number of thread blocks divide # SMs. |
| py-083 | text | optional | `lecture06-slides.py:review_of_gpus` | Summary: |
| py-084 | text | optional | `lecture06-slides.py:review_of_gpus` | - Programming model: grid (HBM) -> thread block (shared memory) -> thread (registers) |
| py-085 | text | optional | `lecture06-slides.py:review_of_gpus` | - Details of hardware (warps, bank conflicts, memory coalescing, occupancy) determine perform... |
| py-086 | text | optional | `lecture06-slides.py:benchmarking_and_profiling` | Recipe for success: |
| py-087 | text | optional | `lecture06-slides.py:benchmarking_and_profiling` | 1. Benchmark and profile your code |
| py-088 | text | optional | `lecture06-slides.py:benchmarking_and_profiling` | 2. Make changes |
| py-089 | text | optional | `lecture06-slides.py:benchmarking_and_profiling` | 3. Benchmark and profile your code again |
| py-090 | text | optional | `lecture06-slides.py:benchmarking_and_profiling` | Benchmark and profile your code! |
| py-091 | text | optional | `lecture06-slides.py:benchmarking` | Benchmarking measures the wall-clock time of performing some operation. |
| py-092 | text | optional | `lecture06-slides.py:benchmarking` | It only gives you end-to-end time, not where time is spent (profiling). |
| py-093 | text | optional | `lecture06-slides.py:benchmarking` | It is still useful for: |
| py-094 | text | optional | `lecture06-slides.py:benchmarking` | - comparing different implementations (which is faster?), and |
| py-095 | text | optional | `lecture06-slides.py:benchmarking` | - understanding how performance scales (e.g., with dimension). |
| py-096 | text | optional | `lecture06-slides.py:benchmarking` | You can use [`torch.utils.benchmark`](https://pytorch.org/tutorials/recipes/recipes/benchmark... |
| py-097 | text | optional | `lecture06-slides.py:benchmarking` | We will roll our own to make benchmarking more transparent. |
| py-098 | text | optional | `lecture06-slides.py:benchmarking` | Note: time is roughly constant when dimension is small, then cubic scaling. |
| py-099 | text | optional | `lecture06-slides.py:profiling` | While benchmarking looks at end-to-end time, profiling looks at where time is spent. |
| py-100 | text | optional | `lecture06-slides.py:profiling` | Independent of time, profiling also helps you understand what's going under the hood. |
| py-101 | text | optional | `lecture06-slides.py:profiling` | PyTorch has a built-in [profiler](https://pytorch.org/tutorials/recipes/recipes/profiler_reci... |
| py-102 | text | optional | `lecture06-slides.py:profiling` | In your assignment, you will use nsight to get more details. |
| py-103 | section | yes | `lecture06-slides.py:profiling` | add(dim=2048) |
| py-104 | section | yes | `lecture06-slides.py:profiling` | matmul(dim=2048) |
| py-105 | section | yes | `lecture06-slides.py:profiling` | matmul(dim=128) |
| py-106 | text | optional | `lecture06-slides.py:profiling` | Observations: |
| py-107 | text | optional | `lecture06-slides.py:profiling` | - You can see which CUDA kernels are actually being called (the long names). |
| py-108 | text | optional | `lecture06-slides.py:profiling` | - Different CUDA kernels are invoked depending on the tensor dimensions. |
| py-109 | text | optional | `lecture06-slides.py:profiling` | Name of CUDA kernel tells us something about the implementation. |
| py-110 | text | optional | `lecture06-slides.py:profiling` | Example: cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_nnn_align1_bi... |
| py-111 | text | optional | `lecture06-slides.py:profiling` | - cutlass: NVIDIA's CUDA library for linear algebra |
| py-112 | text | optional | `lecture06-slides.py:profiling` | - sm100: corresponds to the NVIDIA Blackwell architecture (B200) |
| py-113 | text | optional | `lecture06-slides.py:profiling` | - f32: float32 |
| py-114 | text | optional | `lecture06-slides.py:profiling` | - 64x64x16: tile shape (more on this later) |
| py-115 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | Let's benchmark and profile the [GeLU activation function](https://pytorch.org/docs/stable/ge... |
| py-116 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | The builtin and compiled versions are significantly faster! |
| py-117 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | To understand why, let's look at the profiler to see where time is being spent. |
| py-118 | section | yes | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | naive_gelu |
| py-119 | section | yes | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | builtin_gelu |
| py-120 | section | yes | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | compiled_gelu |
| py-121 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | Notes: |
| py-122 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | - Naive implementation: multiple kernels, requires many reads/writes from/to HBM (**no fusion... |
| py-123 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | - Builtin and compiled versions: one kernel (**kernel fusion**), one read from HBM, one write... |
| py-124 | text | optional | `lecture06-slides.py:naive_vs_builtin_vs_compiled_gelu` | - The compiled kernel is a Triton kernel. |
| py-125 | figure | yes | `lecture06-slides.py:triton_introduction` | https://docs.nvidia.com/cuda/parallel-thread-execution/_images/grid-with-CTAs.png |
| py-126 | text | optional | `lecture06-slides.py:triton_introduction` | In CUDA (developed by NVIDIA), specify what each thread does. |
| py-127 | text | optional | `lecture06-slides.py:triton_introduction` | - Pros: fine-grained control |
| py-128 | text | optional | `lecture06-slides.py:triton_introduction` | - Cons: need to manage more things (e.g., shared memory) |
| py-129 | text | optional | `lecture06-slides.py:triton_introduction` | In Triton (developed by OpenAI), specify what each thread block does. |
| py-130 | text | optional | `lecture06-slides.py:triton_introduction` | - Generally powerful enough (especially when getting started) |
| py-131 | text | optional | `lecture06-slides.py:triton_introduction` | - Conceptual framework: load data into shared memory, operate on it, write back to global memory |
| py-132 | text | optional | `lecture06-slides.py:triton_gelu_example` | Let's write the Triton kernel for GeLU. |
| py-133 | text | optional | `lecture06-slides.py:triton_gelu_example` | Triton compiles down to PTX (parallel thread execution), an assembly language for GPUs. |
| py-134 | text | optional | `lecture06-slides.py:triton_gelu_example` | We can see the PTX code generated by Triton. |
| py-135 | text | optional | `lecture06-slides.py:triton_gelu_example` | Observations: |
| py-136 | text | optional | `lecture06-slides.py:triton_gelu_example` | - ld.global.* and st.global.* reads and writes from global memory |
| py-137 | text | optional | `lecture06-slides.py:triton_gelu_example` | - %ctaid.x is block index, %tid.x is thread index |
| py-138 | text | optional | `lecture06-slides.py:triton_gelu_example` | - %f* are floating point registers, %r* are integer registers |
| py-139 | text | optional | `lecture06-slides.py:triton_gelu_example` | - One thread processes 8 elements at the same time (thread coarsening) |
| py-140 | text | optional | `lecture06-slides.py:triton_softmax_example` | So far, we've looked at elementwise operations in Triton (e.g., GeLU). |
| py-141 | text | optional | `lecture06-slides.py:triton_softmax_example` | Now let us look at operations that aggregate over multiple values. |
| py-142 | text | optional | `lecture06-slides.py:triton_softmax_example` | We will roughly follow the Triton fused softmax tutorial: |
| py-143 | text | optional | `lecture06-slides.py:triton_softmax_example` | Recall the softmax operation is used in attention and generating probabilities. |
| py-144 | text | optional | `lecture06-slides.py:triton_softmax_example` | Exponentiate and normalize each row of a matrix: |
| py-145 | text | optional | `lecture06-slides.py:triton_softmax_example` | [0 0 0] => [1/3 1/3 1/3] |
| py-146 | text | optional | `lecture06-slides.py:triton_softmax_example` | [1 1 -inf] [1/2 1/2 0 ] |
| py-147 | text | optional | `lecture06-slides.py:triton_softmax_example` | Let's first start with the naive implementation and keep track of reads/writes. |
| py-148 | text | optional | `lecture06-slides.py:triton_softmax_example` | Now let us write the Triton kernel. |
| py-149 | figure | yes | `lecture06-slides.py:triton_softmax_example` | images/triton-softmax.png |
| py-150 | text | optional | `lecture06-slides.py:triton_row_sum_example` | In the softmax example, an entire row fits in a block, so the reduction happens within a bloc... |
| py-151 | text | optional | `lecture06-slides.py:triton_row_sum_example` | What if the row doesn't fit in a block? |
| py-152 | text | optional | `lecture06-slides.py:triton_row_sum_example` | Example: 4096 columns, but block size is 1024... |
| py-153 | text | optional | `lecture06-slides.py:triton_row_sum_example` | Strategy: |
| py-154 | text | optional | `lecture06-slides.py:triton_row_sum_example` | - Break up row into tiles (4 in the example above) |
| py-155 | text | optional | `lecture06-slides.py:triton_row_sum_example` | - Each thread iterates over tiles and accumulates a sum |
| py-156 | text | optional | `lecture06-slides.py:triton_row_sum_example` | - Do final reduction (sum) over accumulators of each thread (shared memory or warp shuffles) |
| py-157 | text | optional | `lecture06-slides.py:triton_row_sum_example` | Consider the simpler example (row sum instead of softmax): |
| py-158 | figure | yes | `lecture06-slides.py:triton_row_sum_example` | images/triton-row-sum.png |
| py-159 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Matrix multiplication is the bread and butter of deep learning. |
| py-160 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | How should we build a matmul kernel? |
| py-161 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | \| k n |
| py-162 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | \| [ A1 A2 A3 ] [ B1 B2 B3 ] [ C1 C2 C3 ] |
| py-163 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | \| m [ A4 A5 A6 ] * k [ B4 B5 B6 ] = [ C4 C5 C6 ] |
| py-164 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | \| [ A7 A8 A9 ] [ B7 B8 B9 ] [ C7 C8 C9 ] |
| py-165 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | **Naive approach:** |
| py-166 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Fix any (m, n). |
| py-167 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | For each k: |
| py-168 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Read A[m, k] and B[k, n] from HBM. |
| py-169 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Multiply and accumulate. |
| py-170 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Write result to C[m, n] in HBM. |
| py-171 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Bottleneck: M K N reads, M N writes |
| py-172 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Arithmetic intensity: O(1) |
| py-173 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Computing C4 and C5 both need A4, A5, A6. |
| py-174 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Can we read A4, A5, A6 from HBM once to compute both? |
| py-175 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Answer: yes, using shared memory! |
| py-176 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | **Idealized approach:** |
| py-177 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Load all of A and B into shared memory, then compute C. |
| py-178 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Now we get M K + K N reads and M N writes. |
| py-179 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - This yields the idealized O(N) arithmetic intensity from before. |
| py-180 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - However, A and B are usually too large to fit in shared memory. |
| py-181 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | **Tiling:** |
| py-182 | figure | yes | `lecture06-slides.py:triton_matmul_relu_example` | images/gemm_tiled.png |
| py-183 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Key idea: divide the matrix C into output tiles (thread blocks). |
| py-184 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Fix an output tile in C. |
| py-185 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | For each pair of (row tile of A, column tile of B): |
| py-186 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Load the corresponding A tile and B tile from HBM into shared memory. |
| py-187 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Perform matrix multiplication on the tiles. |
| py-188 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Accumulate into the partial sum (in shared memory). |
| py-189 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Write output tile to HBM. |
| py-190 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Arithmetic intensity: O(tile_size). |
| py-191 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Bonus: |
| py-192 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Often, you want to apply an elementwise activation function. |
| py-193 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Example: GeLU(A @ B) |
| py-194 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | - Solution: kernel fusion! |
| py-195 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | **Implementation.** |
| py-196 | text | optional | `lecture06-slides.py:triton_matmul_relu_example` | Review: each matrix is linearized in memory |

## Existing Note

- `lecture06-notes.tex`

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
