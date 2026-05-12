# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture02`

## Files

- `cover.jpg`
- `lecture02-notes.pdf`
- `lecture02-notes.tex`
- `lecture02-slides.py`

## Local Visual Assets

- `images/bf16.png`
- `images/compute-memory.png`
- `images/cpu-gpu.png`
- `images/deep-network.png`
- `images/fp16.png`
- `images/fp32.png`
- `images/fp8-formats.png`
- `images/marin-1e23-forecast.jpg`
- `images/marin-forecast-result.jpg`
- `images/roofline-improved-1400.png`
- `images/roofline-improved-1400.webp`
- `images/roofline-improved.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | text | optional | `lecture02-slides.py:main` | Announcements: |
| py-002 | text | optional | `lecture02-slides.py:main` | - Join the CS336 slack |
| py-003 | text | optional | `lecture02-slides.py:main` | - Sign up on Modal with your **Stanford** email |
| py-004 | text | optional | `lecture02-slides.py:main` | - Read the [AI policy guide](https://docs.google.com/document/d/1SZAlExB1qAc9izHt54gwunNpjKE6... |
| py-005 | text | optional | `lecture02-slides.py:main` | - Read the [cluster guide](https://docs.google.com/document/d/1cHE0iKVyXLJ3XpIs2XuXTmZ-HMmPk2... |
| py-006 | text | optional | `lecture02-slides.py:main` | Marin 1e23 FLOPs run finished and [matched forecasts](https://x.com/WilliamBarrHeld/status/20... |
| py-007 | figure | yes | `lecture02-slides.py:main` | https://pbs.twimg.com/media/HE1P1HmaUAAjLXF?format=jpg&name=medium |
| py-008 | text | optional | `lecture02-slides.py:main` | Last lecture: overview, tokenization |
| py-009 | text | optional | `lecture02-slides.py:main` | Today: resource accounting (systems) |
| py-010 | text | optional | `lecture02-slides.py:main` | Recall: what's the best model one can train given fixed resources (compute, memory)? |
| py-011 | text | optional | `lecture02-slides.py:main` | In other words: maximize (computational) **efficiency**. |
| py-012 | text | optional | `lecture02-slides.py:main` | Prerequisite: understand the resources (compute, memory) for a given computation. |
| py-013 | text | optional | `lecture02-slides.py:main` | What knowledge to take away from this lecture: |
| py-014 | text | optional | `lecture02-slides.py:main` | - Mechanics: straightforward (PyTorch semantics) |
| py-015 | text | optional | `lecture02-slides.py:main` | - Mindset: resource accounting (remember to do it) |
| py-016 | text | optional | `lecture02-slides.py:main` | - Intuitions: get a sense of how resources are spent, no ML magic today |
| py-017 | text | optional | `lecture02-slides.py:main` | Summary: |
| py-018 | text | optional | `lecture02-slides.py:main` | - Everything is operations on tensors (parameters, gradients, activations, optimizer states, ... |
| py-019 | text | optional | `lecture02-slides.py:main` | - einops: better way to think about tensor operations |
| py-020 | text | optional | `lecture02-slides.py:main` | - 6 (# data points) (# parameters) FLOPs per training step |
| py-021 | text | optional | `lecture02-slides.py:main` | - Arithmetic intensity / roofline analysis: compute-bound or memory-bound? |
| py-022 | text | optional | `lecture02-slides.py:main` | - Matrix multiplications are compute-bound, elementwise operations are memory-bound |
| py-023 | text | optional | `lecture02-slides.py:main` | - Gradient accumulation, activation checkpointing: reduce memory to use bigger batch sizes |
| py-024 | text | optional | `lecture02-slides.py:motivating_questions` | **Question**: How long would it take to train a 70B parameter model on 15T tokens on 1024 H100s? |
| py-025 | text | optional | `lecture02-slides.py:motivating_questions` | **Question**: What's the largest model that can you can train on 8 H100s using AdamW? |
| py-026 | text | optional | `lecture02-slides.py:motivating_questions` | Caveat: activations are not accounted for (depends on batch size and sequence length), so thi... |
| py-027 | text | optional | `lecture02-slides.py:motivating_questions` | This is a rough back-of-the-envelope calculation. |
| py-028 | text | optional | `lecture02-slides.py:motivating_questions` | But it gives you the flavor of napkin math one can quickly do to get a sense of resources. |
| py-029 | text | optional | `lecture02-slides.py:tensors_basics` | Tensors are the basic building block for storing everything: |
| py-030 | text | optional | `lecture02-slides.py:tensors_basics` | - data |
| py-031 | text | optional | `lecture02-slides.py:tensors_basics` | - parameters |
| py-032 | text | optional | `lecture02-slides.py:tensors_basics` | - gradients |
| py-033 | text | optional | `lecture02-slides.py:tensors_basics` | - optimizer state |
| py-034 | text | optional | `lecture02-slides.py:tensors_basics` | - activations |
| py-035 | text | optional | `lecture02-slides.py:tensors_basics` | Example: parameters of the DeepSeek v3.2 model |
| py-036 | text | optional | `lecture02-slides.py:tensors_basics` | Each tensor has a rank, which is the number of dimensions. |
| py-037 | text | optional | `lecture02-slides.py:tensors_basics` | In Transformers, will see tensors of rank 4: |
| py-038 | text | optional | `lecture02-slides.py:tensors_memory` | Elements of tensors are generally floating point numbers. |
| py-039 | section | yes | `lecture02-slides.py:tensors_memory` | fp32 |
| py-040 | figure | yes | `lecture02-slides.py:tensors_memory` | images/fp32.png |
| py-041 | text | optional | `lecture02-slides.py:tensors_memory` | The fp32 data type (also known as float32 or single precision) is the default. |
| py-042 | text | optional | `lecture02-slides.py:tensors_memory` | Traditionally, in scientific computing, fp32 is the baseline; you could use double precision ... |
| py-043 | text | optional | `lecture02-slides.py:tensors_memory` | In deep learning, you can be a lot sloppier. |
| py-044 | text | optional | `lecture02-slides.py:tensors_memory` | Let's examine memory usage of these tensors. |
| py-045 | text | optional | `lecture02-slides.py:tensors_memory` | Memory is determined by the (i) number of values and (ii) data type of each value. |
| py-046 | text | optional | `lecture02-slides.py:tensors_memory` | One matrix in the feedforward layer of GPT-3: |
| py-047 | section | yes | `lecture02-slides.py:tensors_memory` | fp16 |
| py-048 | figure | yes | `lecture02-slides.py:tensors_memory` | images/fp16.png |
| py-049 | text | optional | `lecture02-slides.py:tensors_memory` | The fp16 data type (also known as float16 or half precision) cuts down the memory. |
| py-050 | text | optional | `lecture02-slides.py:tensors_memory` | However, the dynamic range (especially for small numbers) isn't great. |
| py-051 | text | optional | `lecture02-slides.py:tensors_memory` | If this happens when you train, you can get instability. |
| py-052 | section | yes | `lecture02-slides.py:tensors_memory` | bf16 |
| py-053 | figure | yes | `lecture02-slides.py:tensors_memory` | images/bf16.png |
| py-054 | text | optional | `lecture02-slides.py:tensors_memory` | Google Brain developed brain floating point (bf16) in 2018 to address this issue. |
| py-055 | text | optional | `lecture02-slides.py:tensors_memory` | bf16 uses the same memory as fp16 but has the same dynamic range as fp32! |
| py-056 | text | optional | `lecture02-slides.py:tensors_memory` | The only catch is that the resolution is worse, but this matters less for deep learning. |
| py-057 | section | yes | `lecture02-slides.py:tensors_memory` | Mixed precision |
| py-058 | text | optional | `lecture02-slides.py:tensors_memory` | Implications on training: |
| py-059 | text | optional | `lecture02-slides.py:tensors_memory` | - Training with fp32 works, but requires lots of memory. |
| py-060 | text | optional | `lecture02-slides.py:tensors_memory` | - Training with fp16 and even bf16 is risky, and you can get instability. |
| py-061 | text | optional | `lecture02-slides.py:tensors_memory` | Solution: mixed precision training |
| py-062 | text | optional | `lecture02-slides.py:tensors_memory` | - Use bf16 for parameters, activations, and gradients |
| py-063 | text | optional | `lecture02-slides.py:tensors_memory` | - Use fp32 for optimizer states |
| py-064 | text | optional | `lecture02-slides.py:tensors_memory` | Pytorch has an automatic mixed precision (AMP) library. |
| py-065 | text | optional | `lecture02-slides.py:tensors_memory` | Tries to cast things into bf16 when safe (matmuls, not exp). |
| py-066 | section | yes | `lecture02-slides.py:tensors_memory` | fp8 |
| py-067 | text | optional | `lecture02-slides.py:tensors_memory` | In 2022, fp8 was standardized, motivated by machine learning workloads [primer](https://docs.... |
| py-068 | figure | yes | `lecture02-slides.py:tensors_memory` | https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/_images/fp8_formats.png |
| py-069 | text | optional | `lecture02-slides.py:tensors_memory` | H100s support two variants of FP8: E4M3 (range [-448, 448]) and E5M2 ([-57344, 57344]). |
| py-070 | text | optional | `lecture02-slides.py:tensors_memory` | Reference: |
| py-071 | section | yes | `lecture02-slides.py:tensors_memory` | fp4 |
| py-072 | text | optional | `lecture02-slides.py:tensors_memory` | In 2025, NVIDIA developed [nvfp4](https://developer.nvidia.com/blog/introducing-nvfp4-for-eff... |
| py-073 | text | optional | `lecture02-slides.py:tensors_memory` | Only 4 bits per value! |
| py-074 | text | optional | `lecture02-slides.py:tensors_memory` | Values: -6, -4, -3, -2, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2, 3, 4, 6 |
| py-075 | text | optional | `lecture02-slides.py:tensors_memory` | Use a separate scale factor per block, so actually get more dynamic range (but just can't var... |
| py-076 | text | optional | `lecture02-slides.py:tensors_memory` | Nemotron 3 Super was trained in NVFP4 |
| py-077 | text | optional | `lecture02-slides.py:tensors_memory` | Some of this is done in NVIDIA libraries outside of user control. |
| py-078 | text | optional | `lecture02-slides.py:tensors_on_gpus` | By default, tensors are stored in CPU memory. |
| py-079 | text | optional | `lecture02-slides.py:tensors_on_gpus` | However, what about GPUs? |
| py-080 | figure | yes | `lecture02-slides.py:tensors_on_gpus` | images/cpu-gpu.png |
| py-081 | text | optional | `lecture02-slides.py:tensors_on_gpus` | In order to take advantage of the massive parallelism of GPUs, we need to move them to GPU me... |
| py-082 | text | optional | `lecture02-slides.py:tensors_on_gpus` | Or create the tensor directly on the GPU: |
| py-083 | text | optional | `lecture02-slides.py:tensor_einops` | Einops is a library for manipulating tensors where dimensions are named. |
| py-084 | text | optional | `lecture02-slides.py:tensor_einops` | It is inspired by Einstein summation notation (Einstein, 1916). |
| py-085 | text | optional | `lecture02-slides.py:einops_motivation` | Traditional PyTorch code: |
| py-086 | text | optional | `lecture02-slides.py:einops_motivation` | Easy to mess up the dimensions (what is -2, -1?)... |
| py-087 | text | optional | `lecture02-slides.py:einops_einsum` | Einsum is generalized matrix multiplication with good bookkeeping. |
| py-088 | text | optional | `lecture02-slides.py:einops_einsum` | Let's try a more complex example... |
| py-089 | text | optional | `lecture02-slides.py:einops_einsum` | Dimensions that are not named in the output are summed over. |
| py-090 | text | optional | `lecture02-slides.py:einops_reduce` | You can reduce a single tensor via some operation (e.g., sum, mean, max, min). |
| py-091 | text | optional | `lecture02-slides.py:einops_rearrange` | Sometimes, a dimension represents two dimensions |
| py-092 | text | optional | `lecture02-slides.py:einops_rearrange` | ...and you want to operate on one of them. |
| py-093 | text | optional | `lecture02-slides.py:einops_rearrange` | ...where `total_hidden` is a flattened representation of `heads * hidden1` |
| py-094 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Having gone through all the operations, let us examine their computational cost. |
| py-095 | text | optional | `lecture02-slides.py:tensor_operations_flops` | A floating-point operation (FLOP) is a basic operation like addition (x + y) or multiplicatio... |
| py-096 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Two terribly confusing acronyms (pronounced the same!): |
| py-097 | text | optional | `lecture02-slides.py:tensor_operations_flops` | - FLOPs: floating-point operations (measure of computation done) |
| py-098 | text | optional | `lecture02-slides.py:tensor_operations_flops` | - FLOP/s: floating-point operations per second (also written as FLOPS), which is used to meas... |
| py-099 | section | yes | `lecture02-slides.py:tensor_operations_flops` | Intuitions |
| py-100 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Training GPT-3 (2020) took 3.14e23 FLOPs. |
| py-101 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Training GPT-4 (2023) is speculated to take 2e25 FLOPs. |
| py-102 | text | optional | `lecture02-slides.py:tensor_operations_flops` | H100 has a peak performance of 1979 teraFLOP/s with sparsity, 50% without |
| py-103 | text | optional | `lecture02-slides.py:tensor_operations_flops` | 8 H100s for 2 weeks: |
| py-104 | section | yes | `lecture02-slides.py:tensor_operations_flops` | Linear model |
| py-105 | text | optional | `lecture02-slides.py:tensor_operations_flops` | How many FLOPs is this matmul? |
| py-106 | text | optional | `lecture02-slides.py:tensor_operations_flops` | We have one multiplication (x[i][j] * w[j][k]) and one addition per (i, j, k) triple. |
| py-107 | text | optional | `lecture02-slides.py:tensor_operations_flops` | We can also time this operation to see how long it takes. |
| py-108 | text | optional | `lecture02-slides.py:tensor_operations_flops` | The actual FLOP/s of this operation: |
| py-109 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Each GPU has a specification sheet that provides the peak performance. |
| py-110 | text | optional | `lecture02-slides.py:tensor_operations_flops` | - Example: |
| py-111 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Note that the FLOP/s depends heavily on the data type! |
| py-112 | section | yes | `lecture02-slides.py:tensor_operations_flops` | Model FLOPs utilization (MFU) |
| py-113 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Definition: MFU = (actual FLOP/s) / (promised FLOP/s) [ignore communication/overhead] |
| py-114 | text | optional | `lecture02-slides.py:tensor_operations_flops` | Usually, MFU of ≥ 0.5 is quite good! |
| py-115 | text | optional | `lecture02-slides.py:tensor_operations_flops` | But why is MFU not closer to 1? |
| py-116 | text | optional | `lecture02-slides.py:tensor_operations_flops` | To answer this question, we need to look more closely at how computations are done on GPUs... |
| py-117 | figure | yes | `lecture02-slides.py:arithmetic_intensity` | images/compute-memory.png |
| py-118 | text | optional | `lecture02-slides.py:arithmetic_intensity` | How to compute a thing: |
| py-119 | text | optional | `lecture02-slides.py:arithmetic_intensity` | 1. Send inputs from memory to accelerator |
| py-120 | text | optional | `lecture02-slides.py:arithmetic_intensity` | 2. Perform computation |
| py-121 | text | optional | `lecture02-slides.py:arithmetic_intensity` | 3. Send outputs from accelerator to memory |
| py-122 | text | optional | `lecture02-slides.py:arithmetic_intensity` | How long does this take? |
| py-123 | text | optional | `lecture02-slides.py:arithmetic_intensity` | Depends on two things: |
| py-124 | text | optional | `lecture02-slides.py:arithmetic_intensity` | 1. Accelerator speed (FLOP/s) |
| py-125 | text | optional | `lecture02-slides.py:arithmetic_intensity` | 2. Memory bandwidth (bytes/s) |
| py-126 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | Assume we can overlap communication and computation perfectly. |
| py-127 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | What is the bottleneck? |
| py-128 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | - Memory-bound: communication time > computation time |
| py-129 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | - Compute-bound: computation time > communication time |
| py-130 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | In this case, ReLU is memory-bound. |
| py-131 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | Alternative way to see this: |
| py-132 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | Accelerator intensity: how much work can the accelerator do per byte transferred? |
| py-133 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | Arithmetic intensity: how much actual work per byte for this workload? |
| py-134 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | What is the bottleneck? |
| py-135 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | - Memory-bound: arithmetic intensity < accelerator intensity |
| py-136 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | - Compute-bound: arithmetic intensity > accelerator intensity |
| py-137 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | In general, we'll find ourselves memory bound. |
| py-138 | text | optional | `lecture02-slides.py:arithmetic_intensity_relu` | Can we increase arithmetic intensity? |
| py-139 | text | optional | `lecture02-slides.py:arithmetic_intensity_gelu` | Note that GeLU does more work than ReLU per byte moved, so it has higher arithmetic intensity. |
| py-140 | text | optional | `lecture02-slides.py:arithmetic_intensity_gelu` | But still memory-bound! |
| py-141 | text | optional | `lecture02-slides.py:arithmetic_intensity_gelu` | In other words, ReLU is not faster than GeLU (when doing things in an isolated way). |
| py-142 | text | optional | `lecture02-slides.py:arithmetic_intensity_dot_product` | Memory-bound! |
| py-143 | text | optional | `lecture02-slides.py:arithmetic_intensity_matrix_vector_product` | Memory-bound! |
| py-144 | text | optional | `lecture02-slides.py:arithmetic_intensity_matmul` | Finally, compute-bound! |
| py-145 | text | optional | `lecture02-slides.py:arithmetic_intensity_matmul` | As long as we have large matrices, we're compute-bound (saturating the accelerator). |
| py-146 | text | optional | `lecture02-slides.py:arithmetic_intensity_matmul` | Training Transformers involves big matrix multiplications. |
| py-147 | text | optional | `lecture02-slides.py:arithmetic_intensity_matmul` | Matrix-vector product is what happens during inference, which is why inference is memory-bound. |
| py-148 | text | optional | `lecture02-slides.py:arithmetic_intensity_matmul` | Note: arithmetic/accelerator intensity also depends on the precision (bf16 versus fp32). |
| py-149 | text | optional | `lecture02-slides.py:roofline_plots` | We can visualize the relationship between arithmetic intensity and performance using roofline... |
| py-150 | figure | yes | `lecture02-slides.py:roofline_plots` | https://jax-ml.github.io/scaling-book/assets/img/roofline-improved-1400.webp |
| py-151 | text | optional | `lecture02-slides.py:roofline_plots` | - Each slice on the x-axis is a particular computation (with some arithmetic intensity) |
| py-152 | text | optional | `lecture02-slides.py:roofline_plots` | - Each piecewise linear function corresponds to a particular hardware |
| py-153 | text | optional | `lecture02-slides.py:roofline_plots` | - Kink is the accelerator intensity (transition from memory-bound to compute-bound) |
| py-154 | text | optional | `lecture02-slides.py:roofline_plots` | We can now relate this back to MFU: |
| py-155 | text | optional | `lecture02-slides.py:roofline_plots` | MFU = min(1, arithmetic-intensity / accelerator-intensity) |
| py-156 | text | optional | `lecture02-slides.py:gradients_basics` | So far, we've constructed tensors and passed them through operations (forward). |
| py-157 | text | optional | `lecture02-slides.py:gradients_basics` | Now, we're going to compute the gradient (backward). |
| py-158 | text | optional | `lecture02-slides.py:gradients_basics` | As a simple example, let's consider the simple linear model: |
| py-159 | text | optional | `lecture02-slides.py:gradients_basics` | y = 0.5 (x * w - 5)^2 |
| py-160 | text | optional | `lecture02-slides.py:gradients_basics` | Forward pass: compute loss |
| py-161 | text | optional | `lecture02-slides.py:gradients_basics` | Backward pass: compute gradients |
| py-162 | text | optional | `lecture02-slides.py:gradients_flops` | Let us count the FLOPs for computing gradients. |
| py-163 | figure | yes | `lecture02-slides.py:gradients_flops` | images/deep-network.png |
| py-164 | text | optional | `lecture02-slides.py:gradients_flops` | Define a simplified model (2-layer linear network): |
| py-165 | section | yes | `lecture02-slides.py:gradients_flops` | Zoom in on one layer |
| py-166 | text | optional | `lecture02-slides.py:gradients_flops` | Let's focus on the second layer (h2 = h1 @ w2) |
| py-167 | text | optional | `lecture02-slides.py:gradients_flops` | **Forward pass**: Recall the number of forward FLOPs: |
| py-168 | text | optional | `lecture02-slides.py:gradients_flops` | **Backward pass**: How many FLOPs is running the backward pass? |
| py-169 | text | optional | `lecture02-slides.py:gradients_flops` | We need to compute: |
| py-170 | text | optional | `lecture02-slides.py:gradients_flops` | - h1.grad = d loss / d h1 |
| py-171 | text | optional | `lecture02-slides.py:gradients_flops` | - w2.grad = d loss / d w2 |
| py-172 | text | optional | `lecture02-slides.py:gradients_flops` | Note that the backward pass is 2x more expensive than the forward pass. |
| py-173 | section | yes | `lecture02-slides.py:gradients_flops` | Consider all layers |
| py-174 | text | optional | `lecture02-slides.py:gradients_flops` | This was just for w2, need to apply it to all parameters in the network. |
| py-175 | text | optional | `lecture02-slides.py:gradients_flops` | Putting it together: |
| py-176 | text | optional | `lecture02-slides.py:gradients_flops` | - Forward pass: 2 (# data points) (# parameters) FLOPs |
| py-177 | text | optional | `lecture02-slides.py:gradients_flops` | - Backward pass: 4 (# data points) (# parameters) FLOPs |
| py-178 | text | optional | `lecture02-slides.py:gradients_flops` | - Total: 6 (# data points) (# parameters) FLOPs |
| py-179 | text | optional | `lecture02-slides.py:gradients_flops` | This is for multilayer perceptrons (MLPs) |
| py-180 | text | optional | `lecture02-slides.py:gradients_flops` | ...but it turns out to be a good approximation for Transformers for short context lengths as ... |
| py-181 | figure | yes | `lecture02-slides.py:deep_network` | images/deep-network.png |
| py-182 | text | optional | `lecture02-slides.py:deep_network` | Consider a deep network with L layers and D-dimensional inputs, activations, and outputs. |
| py-183 | text | optional | `lecture02-slides.py:optimizer` | Recall our deep network. |
| py-184 | text | optional | `lecture02-slides.py:optimizer` | Let's define the AdaGrad optimizer |
| py-185 | text | optional | `lecture02-slides.py:optimizer` | - momentum = SGD + exponential averaging of grad |
| py-186 | text | optional | `lecture02-slides.py:optimizer` | - AdaGrad = SGD + averaging by grad^2 |
| py-187 | text | optional | `lecture02-slides.py:optimizer` | - RMSProp = AdaGrad but with exponential averaging of grad^2 |
| py-188 | text | optional | `lecture02-slides.py:optimizer` | - Adam = RMSProp + momentum |
| py-189 | text | optional | `lecture02-slides.py:optimizer` | AdaGrad |
| py-190 | section | yes | `lecture02-slides.py:optimizer` | Memory |
| py-191 | text | optional | `lecture02-slides.py:optimizer` | It is customary to use fp32 for stability (accumulating averages over powers over many steps). |
| py-192 | text | optional | `lecture02-slides.py:optimizer` | Optimizer state memory: |
| py-193 | text | optional | `lecture02-slides.py:optimizer` | - AdaGrad: 4 bytes/parameter for storing second moments |
| py-194 | text | optional | `lecture02-slides.py:optimizer` | - Adam: 8 bytes/parameter for storing first and second moments |
| py-195 | section | yes | `lecture02-slides.py:optimizer` | Compute (for one training step) |
| py-196 | section | yes | `lecture02-slides.py:optimizer` | Transformers |
| py-197 | text | optional | `lecture02-slides.py:optimizer` | The accounting for a Transformer is more complicated, but the same idea. |
| py-198 | text | optional | `lecture02-slides.py:optimizer` | Assignment 1 will ask you to do that. |
| py-199 | text | optional | `lecture02-slides.py:optimizer` | Blog post describing memory usage for Transformer training |
| py-200 | text | optional | `lecture02-slides.py:optimizer` | Blog post describing FLOPs for a Transformer: |
| py-201 | text | optional | `lecture02-slides.py:gradient_accumulation` | Large batch sizes: improve training stability |
| py-202 | text | optional | `lecture02-slides.py:gradient_accumulation` | However, activation memory scales with batch size, so might run out. |
| py-203 | text | optional | `lecture02-slides.py:gradient_accumulation` | Gradient accumulation: |
| py-204 | text | optional | `lecture02-slides.py:gradient_accumulation` | - Compute gradient on micro batches |
| py-205 | text | optional | `lecture02-slides.py:gradient_accumulation` | - Accumulate the gradients (don't zero it out) |
| py-206 | text | optional | `lecture02-slides.py:gradient_accumulation` | - Every batch_size / micro_batch_size steps, update the parameters and zero out the gradients |
| py-207 | text | optional | `lecture02-slides.py:activation_checkpointing` | For training, we need to store the activations of all layers |
| py-208 | text | optional | `lecture02-slides.py:activation_checkpointing` | For inference, we don't compute gradients, so we only need to store the current layer's activ... |
| py-209 | figure | yes | `lecture02-slides.py:activation_checkpointing` | images/deep-network.png |
| py-210 | text | optional | `lecture02-slides.py:activation_checkpointing` | The memory usage is |
| py-211 | text | optional | `lecture02-slides.py:activation_checkpointing` | Can we reduce this? |
| py-212 | text | optional | `lecture02-slides.py:activation_checkpointing` | Activation checkpointing = gradient checkpointing = rematerialization |
| py-213 | text | optional | `lecture02-slides.py:activation_checkpointing` | Key idea: |
| py-214 | text | optional | `lecture02-slides.py:activation_checkpointing` | - Forward pass: keep only activations at subset of layers |
| py-215 | text | optional | `lecture02-slides.py:activation_checkpointing` | - Backward pass: recompute the missing activations from the last checkpoint |
| py-216 | text | optional | `lecture02-slides.py:activation_checkpointing` | Philosophy: tradeoff memory for compute |
| py-217 | text | optional | `lecture02-slides.py:activation_checkpointing` | Can we reduce this even more, especially for deep networks (large L)? |
| py-218 | text | optional | `lecture02-slides.py:activation_checkpointing` | How frequently to checkpoint? |
| py-219 | text | optional | `lecture02-slides.py:activation_checkpointing` | - If store each layer's activations, then activation memory is O(L) and no recomputation. |
| py-220 | text | optional | `lecture02-slides.py:activation_checkpointing` | - If store no activations, then activation memory is O(1) and compute is O(L^2) (recompute fr... |
| py-221 | text | optional | `lecture02-slides.py:activation_checkpointing` | - If store every sqrt(L) layers, then activation memory is O(sqrt(L)) and O(L) recomputation. |

## Existing Note

- `lecture02-notes.tex`

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
