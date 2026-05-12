# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture10`

## Files

- `lecture10-notes.pdf`
- `lecture10-notes.tex`
- `lecture10-slides.py`

## Local Visual Assets

- `images/awq-schema.png`
- `images/cached-inference-1400.png`
- `images/cached-inference-1400.webp`
- `images/cla-diagram.png`
- `images/cla-results.png`
- `images/continuous-batching-static.png`
- `images/deepseek-v4-attention.png`
- `images/fp8-quantization.png`
- `images/gmqa.png`
- `images/gqa-accuracy.png`
- `images/gqa-speed.png`
- `images/inference-schema.png`
- `images/longformer-attention.png`
- `images/medusa-eagle.png`
- `images/mla-accuracy.png`
- `images/mla-accuracy2.png`
- `images/mla-schema.png`
- `images/naive-inference-1400.png`
- `images/naive-inference-1400.webp`
- `images/paged-attention-blocks.png`
- `images/paged-attention-fragmentation.png`
- `images/paged-attention-logical.png`
- `images/paged-attention-parallel.png`
- `images/paged-attention-sharing.png`
- `images/pruning-kd-loop.png`
- `images/pruning-kd.png`
- `images/speculative-sampling-algorithm.png`
- `images/speculative-sampling-results.png`
- `images/speculative-sampling-stats.png`
- `images/transformer-diagram.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | section | yes | `lecture10-slides.py:main` | Lecture 10: inference |
| py-002 | figure | yes | `lecture10-slides.py:main` | images/inference-schema.png |
| py-003 | section | yes | `lecture10-slides.py:main` | Understanding the inference workload |
| py-004 | section | yes | `lecture10-slides.py:main` | Taking shortcuts (lossy) |
| py-005 | text | optional | `lecture10-slides.py:main` | Summary: reduce inference complexity without hurting accuracy |
| py-006 | text | optional | `lecture10-slides.py:main` | From scratch recipe: |
| py-007 | text | optional | `lecture10-slides.py:main` | 1. Define faster model architecture |
| py-008 | text | optional | `lecture10-slides.py:main` | 2. Train faster model |
| py-009 | text | optional | `lecture10-slides.py:main` | Distillation recipe: |
| py-010 | text | optional | `lecture10-slides.py:main` | 1. Define faster model architecture |
| py-011 | text | optional | `lecture10-slides.py:main` | 2. Initialize weights using original model (which has a different architecture) |
| py-012 | text | optional | `lecture10-slides.py:main` | 3. Repair faster model (distillation) |
| py-013 | section | yes | `lecture10-slides.py:main` | Use shortcuts but double check (lossless) |
| py-014 | section | yes | `lecture10-slides.py:main` | Handling dynamic workloads |
| py-015 | text | optional | `lecture10-slides.py:main` | Batching over sequences in live traffic is tricky because: |
| py-016 | text | optional | `lecture10-slides.py:main` | 1. Requests arrive at different times (waiting for batch is bad for early requests) |
| py-017 | text | optional | `lecture10-slides.py:main` | 2. Sequences have shared prefixes (e.g., system prompts, generating multiple samples) |
| py-018 | text | optional | `lecture10-slides.py:main` | 3. Sequences have different lengths (padding is inefficient) |
| py-019 | section | yes | `lecture10-slides.py:main` | Summary |
| py-020 | text | optional | `lecture10-slides.py:main` | - Inference is important (actual use, evaluation, reinforcement learning) |
| py-021 | text | optional | `lecture10-slides.py:main` | - Different characteristics compared to training (memory-bound, dynamic) |
| py-022 | text | optional | `lecture10-slides.py:main` | - Techniques: new architectures, quantization, pruning/distillation, speculative sampling |
| py-023 | text | optional | `lecture10-slides.py:main` | - Ideas from systems (speculative execution, paging) |
| py-024 | text | optional | `lecture10-slides.py:main` | - New architectures have huge potential for improvement |
| py-025 | text | optional | `lecture10-slides.py:landscape` | Inference shows up in many places: |
| py-026 | text | optional | `lecture10-slides.py:landscape` | - Actual use (chatbots, code completion, agents, batch data processing) |
| py-027 | text | optional | `lecture10-slides.py:landscape` | - Model evaluation (e.g., on instruction following) |
| py-028 | text | optional | `lecture10-slides.py:landscape` | - Reinforcement learning (sample many generations, then apply score) |
| py-029 | text | optional | `lecture10-slides.py:landscape` | Why **efficiency** matters: training is one-time cost, inference is repeated many times |
| py-030 | text | optional | `lecture10-slides.py:landscape` | - OpenAI processes ~8.6T tokens per day |
| py-031 | text | optional | `lecture10-slides.py:landscape` | - For reference, DeepSeek v4 was trained on 32T tokens |
| py-032 | text | optional | `lecture10-slides.py:landscape` | Moreover: |
| py-033 | text | optional | `lecture10-slides.py:landscape` | - Chatbots: most tokens are meant for human consumption (humans are bottleneck) |
| py-034 | text | optional | `lecture10-slides.py:landscape` | - Agents: query → internal trace → output for human (number of tokens generated can grow unbo... |
| py-035 | text | optional | `lecture10-slides.py:landscape` | - Tokens generated = compute spent |
| py-036 | text | optional | `lecture10-slides.py:landscape` | Companies doing inference (a big deal for anyone who has a product or platform): |
| py-037 | text | optional | `lecture10-slides.py:landscape` | - Providers serving closed models (OpenAI, Anthropic, Google, etc.) |
| py-038 | text | optional | `lecture10-slides.py:landscape` | - Providers serving open-weight models (Together, Fireworks, Baseten, DeepInfra, Groq, Cerebr... |
| py-039 | text | optional | `lecture10-slides.py:landscape` | Open-source packages: |
| py-040 | text | optional | `lecture10-slides.py:landscape` | - vLLM: from Berkeley, pioneered PagedAttention, popular and good default |
| py-041 | text | optional | `lecture10-slides.py:landscape` | - SGLang: from Berkeley, pioneered RadixAttention, good for agentic workloads |
| py-042 | text | optional | `lecture10-slides.py:landscape` | - TensorRT-LLM: from NVIDIA, highly optimized for GPUs |
| py-043 | text | optional | `lecture10-slides.py:landscape` | - llama.cpp: C++ only, supports CPU inference, runs locally |
| py-044 | text | optional | `lecture10-slides.py:landscape` | Inference is huge. Important to make it fast. |
| py-045 | text | optional | `lecture10-slides.py:landscape` | What does "fast" mean (metrics)? |
| py-046 | text | optional | `lecture10-slides.py:landscape` | - Time-to-first-token (TTFT): how long user waits before any generation happens (for interact... |
| py-047 | text | optional | `lecture10-slides.py:landscape` | - Latency (seconds/token): how fast tokens appear for *one* query (for interactive applications) |
| py-048 | text | optional | `lecture10-slides.py:landscape` | - Throughput (tokens/second): how fast tokens appear for *many* queries (for batch processing) |
| py-049 | text | optional | `lecture10-slides.py:landscape` | What governs efficiency? |
| py-050 | text | optional | `lecture10-slides.py:landscape` | - Training (supervised): you see all tokens, can parallelize over sequence (matmul in Transfo... |
| py-051 | text | optional | `lecture10-slides.py:landscape` | - Inference: you have to generate sequentially, can't parallelize over generation, so harder ... |
| py-052 | text | optional | `lecture10-slides.py:review_transformer` | Notation (similar to einops): |
| py-053 | text | optional | `lecture10-slides.py:review_transformer` | - Symbols denote dimensions (and their length): B (batch), T (sequence), D (model dim), H (he... |
| py-054 | text | optional | `lecture10-slides.py:review_transformer` | - Example: BT<font color="red">D</font> x <font color="red">D</font>H → BTH |
| py-055 | text | optional | `lecture10-slides.py:review_transformer` | - <font color="red">Contracting (red)</font> dimensions appear in both operands and disappear... |
| py-056 | text | optional | `lecture10-slides.py:review_transformer` | - Regular (black) dimensions appear in one operand and stay in result |
| py-057 | text | optional | `lecture10-slides.py:review_transformer` | - Example: <font color="blue">B</font><font color="red">D</font> x <font color="blue">B</font... |
| py-058 | text | optional | `lecture10-slides.py:review_transformer` | - <font color="blue">Batching (blue)</font> dimensions appear in both operands and stay in re... |
| py-059 | figure | yes | `lecture10-slides.py:review_transformer` | https://jax-ml.github.io/scaling-book/assets/img/transformer-diagram.png |
| py-060 | text | optional | `lecture10-slides.py:review_transformer` | Conventions: |
| py-061 | text | optional | `lecture10-slides.py:review_transformer` | - F = 4 D (MLP up-projects into 4x the model dimension) |
| py-062 | text | optional | `lecture10-slides.py:review_transformer` | - D = N H (model dimension split across N heads) |
| py-063 | text | optional | `lecture10-slides.py:review_transformer` | - N = K G (for GQA, number of heads split across K groups) |
| py-064 | text | optional | `lecture10-slides.py:review_transformer` | - S = T (during training, condition on S input tokens to predict T output tokens) |
| py-065 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Setup: multiply X <font color="gray">(B x D)</font> and W <font color="gray">(D x F)</font> m... |
| py-066 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Intuition: B is batch size, D is hidden dimension, F is up-projection dimension in MLP |
| py-067 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Let's do FLOPs and memory read/write accounting for the matrix multiplication (X * W). |
| py-068 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | 1. Read X <font color="gray">(B x D)</font> from HBM |
| py-069 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | 2. Read W <font color="gray">(D x F)</font> from HBM |
| py-070 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | 3. Compute Y = X <font color="gray">(B x D)</font> @ W <font color="gray">(D x F)</font> |
| py-071 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | 4. Write Y <font color="gray">(B x F)</font> to HBM |
| py-072 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Recall that **arithmetic intensity** is how much compute we do per byte transferred (want to ... |
| py-073 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Assuming B is much less than D and F, then we can simplify: |
| py-074 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Accelerator intensity of H100: |
| py-075 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | If computation intensity > accelerator intensity, **compute-bound** (good) |
| py-076 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | If computation intensity < accelerator intensity, **memory-bound** (bad) |
| py-077 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Conclusion: compute-bound iff B > 295 |
| py-078 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | Extreme case (B = 1, corresponding to matrix-vector product): |
| py-079 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | - Arithmetic intensity: 1 |
| py-080 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | - Memory-bound (read D x F matrix, perform only 2 D F FLOPs) |
| py-081 | text | optional | `lecture10-slides.py:review_of_arithmetic_intensity` | - This is basically what happens with inference... |
| py-082 | figure | yes | `lecture10-slides.py:arithmetic_intensity_of_inference` | https://jax-ml.github.io/scaling-book/assets/img/naive-inference-1400.webp |
| py-083 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Naive inference: to generate each token, feed history into Transformer |
| py-084 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Complexity: generating T tokens requires O(T^3) FLOPs (one feedforward pass is O(T^2)) |
| py-085 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Observation: a lot of the work can be shared across prefixes |
| py-086 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Solution: store **KV cache** in HBM |
| py-087 | figure | yes | `lecture10-slides.py:arithmetic_intensity_of_inference` | https://jax-ml.github.io/scaling-book/assets/img/cached-inference-1400.webp |
| py-088 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | KV cache: for every sequence (B), token (S), layer (L), head (K), store an H-dimensional vector |
| py-089 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Two stages of inference: |
| py-090 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 1. **Prefill**: given a prompt, encode into vectors (parallelizable like in training) |
| py-091 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 2. **Generation**: generate new response tokens (sequential) |
| py-092 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Let's compute the FLOPs and memory IO for both the MLP and attention layers. |
| py-093 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | S is the number of tokens we're conditioning on, T is the number of tokens we're generating. |
| py-094 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Later, we'll specialize to prefill (T = S) and generation (T = 1). |
| py-095 | section | yes | `lecture10-slides.py:arithmetic_intensity_of_inference` | MLP layers (only looking at the matrix multiplications) |
| py-096 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 1. Read X <font color="gray">(B x T x D)</font> from HBM |
| py-097 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 2. Read Wup <font color="gray">(D x F)</font>, Wgate <font color="gray">(D x F)</font>, Wdown... |
| py-098 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 3. Compute U = X <font color="gray">(B x T x D)</font> @ Wup <font color="gray">(D x F)</font> |
| py-099 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 4. Write U <font color="gray">(B x T x F)</font> to HBM |
| py-100 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 5. Compute G = X <font color="gray">(B x T x D)</font> @ Wgate <font color="gray">(D x F)</font> |
| py-101 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 6. Write G <font color="gray">(B x T x F)</font> to HBM |
| py-102 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 7. Compute Y = GeLU(G)*U <font color="gray">(B x T x F)</font> @ Wdown <font color="gray">(F ... |
| py-103 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 8. Write Y <font color="gray">(B x T x D)</font> to HBM |
| py-104 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Assume that B*T is much smaller than D and F. |
| py-105 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | For the two stages: |
| py-106 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 1. Prefill: easy to make compute-bound (good) by making `B*T` large enough (large batches, lo... |
| py-107 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 2. Generation: two problems |
| py-108 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - Generating one token at a time (T = 1) |
| py-109 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - B is number of concurrent requests, unpredictable for interactive applications |
| py-110 | section | yes | `lecture10-slides.py:arithmetic_intensity_of_inference` | Attention layers (focusing on the matrix multiplications with FlashAttention) |
| py-111 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - S is number of previous tokens (already generated) |
| py-112 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - T is number of next tokens (to generate logits for) |
| py-113 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 1. Read Q <font color="gray">(B x T x D)</font>, K <font color="gray">(B x S x D)</font>, V <... |
| py-114 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 2. Compute A = Q <font color="gray">(B x T x D)</font> @ K <font color="gray">(B x S x D)</font> |
| py-115 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 3. Compute Y = softmax(A) <font color="gray">(B x S x T x K x G)</font> @ V <font color="gray... |
| py-116 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 4. Write Y <font color="gray">(B x T x D)</font> to HBM |
| py-117 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | For the two stages: |
| py-118 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 1. Prefill: T = S |
| py-119 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | 2. Generation: T = 1 |
| py-120 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Unlike MLPs, no dependence on B, so batching doesn't help! |
| py-121 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Why? |
| py-122 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - In MLP layers, every sequence hits the same MLP weights (Wup, Wgate, Wdown don't depend on B) |
| py-123 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - In attention layers, every sequence has its own KV cache vectors (Q, K, V all depend on B) |
| py-124 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | Summary: |
| py-125 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - Prefill is compute-bound, generation is memory-bound |
| py-126 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - Prefill MLP intensity: `B*S` |
| py-127 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - Prefill attention intensity: `S/2` |
| py-128 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - Generation MLP intensity: `B` (requires concurrent requests) |
| py-129 | text | optional | `lecture10-slides.py:arithmetic_intensity_of_inference` | - Generation attention intensity: `<1` (impossible to improve) |
| py-130 | text | optional | `lecture10-slides.py:throughput_and_latency` | So we have shown that inference is memory-bound. |
| py-131 | text | optional | `lecture10-slides.py:throughput_and_latency` | Let us now compute the theoretical maximum latency and throughput of a single request. |
| py-132 | text | optional | `lecture10-slides.py:throughput_and_latency` | Assumption: can overlap compute and communication perfectly and ignore overhead. |
| py-133 | text | optional | `lecture10-slides.py:throughput_and_latency` | Instantiate latency and throughput for Llama 2 13B on an H100: |
| py-134 | text | optional | `lecture10-slides.py:throughput_and_latency` | Result: worse latency, better throughput |
| py-135 | text | optional | `lecture10-slides.py:throughput_and_latency` | Result: even worse latency, even better throughput |
| py-136 | text | optional | `lecture10-slides.py:throughput_and_latency` | Result: doesn't fit into memory and throughput gains are diminishing too... |
| py-137 | text | optional | `lecture10-slides.py:throughput_and_latency` | What increasing batch size does: |
| py-138 | text | optional | `lecture10-slides.py:throughput_and_latency` | - Worsens latency because larger KV cache (O(B) size) to read/write |
| py-139 | text | optional | `lecture10-slides.py:throughput_and_latency` | - Improves throughput because amortizes the cost of reading parameters |
| py-140 | text | optional | `lecture10-slides.py:throughput_and_latency` | **Tradeoff** between latency and throughput: |
| py-141 | text | optional | `lecture10-slides.py:throughput_and_latency` | 1. Smaller batch sizes yield better latency but worse throughput |
| py-142 | text | optional | `lecture10-slides.py:throughput_and_latency` | 2. Larger batch sizes yield better throughput but worse latency |
| py-143 | text | optional | `lecture10-slides.py:throughput_and_latency` | Easy parallelism: if you launch M copies of the model, latency is the same, throughput increa... |
| py-144 | text | optional | `lecture10-slides.py:throughput_and_latency` | Harder parallelism: shard the model and the KV cache |
| py-145 | text | optional | `lecture10-slides.py:throughput_and_latency` | Note: time-to-first-token (TTFT) is essentially a function of prefill time |
| py-146 | text | optional | `lecture10-slides.py:throughput_and_latency` | Use smaller batch sizes during prefill for faster TTFT |
| py-147 | text | optional | `lecture10-slides.py:throughput_and_latency` | Use larger batch sizes during generation to improve throughput |
| py-148 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Recall that memory is the bottleneck for inference. |
| py-149 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | So let's try to reduce the size of the KV cache |
| py-150 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | ...but make sure we don't lose too much accuracy. |
| py-151 | section | yes | `lecture10-slides.py:reduce_kv_cache_size` | Grouped-query attention (GQA) |
| py-152 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | https://jax-ml.github.io/scaling-book/assets/img/gmqa.png |
| py-153 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Idea: N query heads, but only K key and value heads, each interacting with N/K query heads |
| py-154 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Multi-headed attention (MHA): K=N |
| py-155 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Multi-query attention (MQA): K=1 |
| py-156 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Group-query attention (GQA): K is somewhere in between |
| py-157 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Latency/throughput improves: |
| py-158 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/gqa-speed.png |
| py-159 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Why does GQA improve latency and throughput? |
| py-160 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | GQA reduces the KV cache by a factor of N/K. |
| py-161 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Reminder: reducing memory usage leads to speedup (since we're memory-bound). |
| py-162 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Result: Worse latency, but better throughput (and it fits in memory now!) |
| py-163 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Result: Worse latency, but better throughput (and still fits in memory!) |
| py-164 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Check that accuracy doesn't drop: |
| py-165 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/gqa-accuracy.png |
| py-166 | section | yes | `lecture10-slides.py:reduce_kv_cache_size` | Multi-head latent attention (MLA) |
| py-167 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/mla-schema.png |
| py-168 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Normal attention: KV cache consists of K = W_K h, V = W_V h (N*H dimensions) |
| py-169 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | MLA: store compressed vector c = W_c h (C dimensions), project up to K = W_K c, V = W_V c whe... |
| py-170 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | DeepSeek v2: reduce N*H = 16384 to C = 512 |
| py-171 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Wrinkle: MLA is not compatible with RoPE, so need to add additional 64 dimensions for RoPE, s... |
| py-172 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Latency/throughput improvements follow similarly from the KV cache reduction as argued earlier |
| py-173 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Let's now check the accuracy. |
| py-174 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | First, MHA is better than GQA (though more expensive) [Table 8] |
| py-175 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/mla-accuracy.png |
| py-176 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Second, MLA is even a bit better than MHA (and much cheaper) [Table 9] |
| py-177 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/mla-accuracy2.png |
| py-178 | section | yes | `lecture10-slides.py:reduce_kv_cache_size` | Cross-layer attention (CLA) |
| py-179 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/cla-diagram.png |
| py-180 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Idea: share KVs across **layers** (just as GQA shares KVs across heads) |
| py-181 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Empirically improves the pareto frontier of accuracy and KV cache size (latency and throughput) |
| py-182 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/cla-results.png |
| py-183 | section | yes | `lecture10-slides.py:reduce_kv_cache_size` | Local (sliding window) attention |
| py-184 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/longformer-attention.png |
| py-185 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Idea: just look at the local context, which is most relevant for modeling |
| py-186 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Effective context scales linearly with the number of layers |
| py-187 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | KV cache is independent of sequence length! |
| py-188 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Problem: this can still hurt accuracy |
| py-189 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Solution: interleave local attention with global attention (hybrid layers) |
| py-190 | section | yes | `lecture10-slides.py:reduce_kv_cache_size` | DeepSeek v4 attention |
| py-191 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Supports 1M context length |
| py-192 | figure | yes | `lecture10-slides.py:reduce_kv_cache_size` | images/deepseek-v4-attention.png |
| py-193 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Compressed Sparse Attention (CSA): compresses every m tokens into 1 |
| py-194 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - DeepSeek Sparse Attention (DSA): selects the top k |
| py-195 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Heavily Compressed Attention (HCA): compresses even more |
| py-196 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | Summary: |
| py-197 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Goal: reduce the KV cache size (since inference is memory-bound) without hurting accuracy |
| py-198 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Lower-dimensional KV cache (GQA, MLA, CLA) |
| py-199 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Local attention (truncates the KV cache) on some of the layers |
| py-200 | text | optional | `lecture10-slides.py:reduce_kv_cache_size` | - Other ideas: linear attention / state-space-models (Mamba 2, GatedDeltaNet), diffusion models |
| py-201 | text | optional | `lecture10-slides.py:quantization` | Key idea: reduce the precision of numbers |
| py-202 | text | optional | `lecture10-slides.py:quantization` | Less memory means higher latency/throughput (since inference is memory-bound). |
| py-203 | text | optional | `lecture10-slides.py:quantization` | Of course we have to worry about accuracy... |
| py-204 | figure | yes | `lecture10-slides.py:quantization` | https://www.datocms-assets.com/104802/1709770809-twitter-post-20.png |
| py-205 | text | optional | `lecture10-slides.py:quantization` | - fp32 (4 bytes): needed for parameters and optimizer states during training |
| py-206 | text | optional | `lecture10-slides.py:quantization` | - bf16 (2 bytes): default for inference |
| py-207 | text | optional | `lecture10-slides.py:quantization` | - fp8 (1 byte) [-240, 240] for e4m3 on H100s: can train if you dare |
| py-208 | text | optional | `lecture10-slides.py:quantization` | - int8 (1 byte) [-128, 127]: less accurate but cheaper than fp8, but for inference only |
| py-209 | text | optional | `lecture10-slides.py:quantization` | - int4 (0.5 bytes) [-8, 7]: cheaper, even less accurate |
| py-210 | text | optional | `lecture10-slides.py:quantization` | Quantization-aware training (QAT) |
| py-211 | text | optional | `lecture10-slides.py:quantization` | - During training, quantize-and-dequantize during the forward pass to simulate quantization e... |
| py-212 | text | optional | `lecture10-slides.py:quantization` | - Pro: weights are trained to work with quantization |
| py-213 | text | optional | `lecture10-slides.py:quantization` | - Con: requires expensive large-scale training |
| py-214 | text | optional | `lecture10-slides.py:quantization` | Post-training quantization (PTQ): |
| py-215 | text | optional | `lecture10-slides.py:quantization` | - Done after training, so much cheaper |
| py-216 | text | optional | `lecture10-slides.py:quantization` | - Run on sample data to determine scale and zero point for each layer or tensor |
| py-217 | text | optional | `lecture10-slides.py:quantization` | - GPTQ: use Hessian information to update non-quantized weights to account for quantization e... |
| py-218 | section | yes | `lecture10-slides.py:quantization` | Activation-aware quantization (AWQ) |
| py-219 | text | optional | `lecture10-slides.py:quantization` | - Observation: some activation channels are large |
| py-220 | text | optional | `lecture10-slides.py:quantization` | - Weights that hit those matter more |
| py-221 | text | optional | `lecture10-slides.py:quantization` | - Allocate more precision to those weights |
| py-222 | text | optional | `lecture10-slides.py:quantization` | - Idea: select which weights (0.1-1%) to keep in high precision based on activations |
| py-223 | text | optional | `lecture10-slides.py:quantization` | - fp16 → int3 produces 4x lower memory, 3.2x speedup |
| py-224 | figure | yes | `lecture10-slides.py:quantization` | images/awq-schema.png |
| py-225 | text | optional | `lecture10-slides.py:model_pruning` | Key idea: just rip out parts of an expensive model to make it cheaper |
| py-226 | text | optional | `lecture10-slides.py:model_pruning` | ...and then fix it up. |
| py-227 | text | optional | `lecture10-slides.py:model_pruning` | Paper from NVIDIA |
| py-228 | figure | yes | `lecture10-slides.py:model_pruning` | images/pruning-kd-loop.png |
| py-229 | text | optional | `lecture10-slides.py:model_pruning` | Algorithm: |
| py-230 | text | optional | `lecture10-slides.py:model_pruning` | 1. Identify important {layer, head, hidden dimension} on a small calibration dataset (1024 sa... |
| py-231 | text | optional | `lecture10-slides.py:model_pruning` | 2. Remove unimportant layers to get a smaller model |
| py-232 | text | optional | `lecture10-slides.py:model_pruning` | 3. Distill the original model into pruned model |
| py-233 | text | optional | `lecture10-slides.py:model_pruning` | Results: |
| py-234 | figure | yes | `lecture10-slides.py:model_pruning` | images/pruning-kd.png |
| py-235 | text | optional | `lecture10-slides.py:speculative_sampling` | Recall the two stages of inference: |
| py-236 | text | optional | `lecture10-slides.py:speculative_sampling` | - Prefill: given a sequence, encode tokens in parallel (compute-bound) [note: also gives you ... |
| py-237 | text | optional | `lecture10-slides.py:speculative_sampling` | - Generation: generate one token at a time (memory-bound) |
| py-238 | text | optional | `lecture10-slides.py:speculative_sampling` | In other words, checking is faster than generation. |
| py-239 | text | optional | `lecture10-slides.py:speculative_sampling` | Speculative sampling |
| py-240 | text | optional | `lecture10-slides.py:speculative_sampling` | - Use a cheaper **draft model** p to guess a few tokens (e.g., 4) |
| py-241 | text | optional | `lecture10-slides.py:speculative_sampling` | - Evaluate with target model q (process tokens in parallel), and accept if it looks good |
| py-242 | figure | yes | `lecture10-slides.py:speculative_sampling` | images/speculative-sampling-algorithm.png |
| py-243 | text | optional | `lecture10-slides.py:speculative_sampling` | This is modified rejection sampling with proposal p and target q |
| py-244 | text | optional | `lecture10-slides.py:speculative_sampling` | Modification: always generate at least one candidate (rejection sampling will keep looping) |
| py-245 | text | optional | `lecture10-slides.py:speculative_sampling` | Key property: guaranteed to be an **exact sample** from the target model! |
| py-246 | text | optional | `lecture10-slides.py:speculative_sampling` | Proof by example: assume two vocabulary elements {A, B} |
| py-247 | text | optional | `lecture10-slides.py:speculative_sampling` | - Target model probabilities: [q(A), q(B)] |
| py-248 | text | optional | `lecture10-slides.py:speculative_sampling` | - Draft model probabilities: [p(A), p(B)] |
| py-249 | text | optional | `lecture10-slides.py:speculative_sampling` | - Assume p(A) > q(A) [draft model oversamples A]. |
| py-250 | text | optional | `lecture10-slides.py:speculative_sampling` | - Therefore p(B) < q(B) [draft model undersamples B]. |
| py-251 | text | optional | `lecture10-slides.py:speculative_sampling` | - Residual probabilities max(q-p, 0): [0, 1] |
| py-252 | text | optional | `lecture10-slides.py:speculative_sampling` | Compute the probabilities of speculatively sampling a token: |
| py-253 | text | optional | `lecture10-slides.py:speculative_sampling` | - P[sampling A] = p(A) * (q(A) / p(A)) + p(B) * 1 * 0 = q(A) |
| py-254 | text | optional | `lecture10-slides.py:speculative_sampling` | - P[sampling B] = p(B) * 1 + p(A) * (1 - q(A) / p(A)) * 1 = q(B) |
| py-255 | figure | yes | `lecture10-slides.py:speculative_sampling` | images/speculative-sampling-results.png |
| py-256 | figure | yes | `lecture10-slides.py:speculative_sampling` | images/speculative-sampling-stats.png |
| py-257 | text | optional | `lecture10-slides.py:speculative_sampling` | In practice: |
| py-258 | text | optional | `lecture10-slides.py:speculative_sampling` | - Target model has 70B parameters, draft model has 8B parameters |
| py-259 | text | optional | `lecture10-slides.py:speculative_sampling` | - Target model has 8B parameters, draft model has 1B parameters |
| py-260 | text | optional | `lecture10-slides.py:speculative_sampling` | - Try to make draft model as close to target (distillation) |
| py-261 | text | optional | `lecture10-slides.py:speculative_sampling` | Extensions to improve the draft model: |
| py-262 | text | optional | `lecture10-slides.py:speculative_sampling` | - Medusa: draft model generates multiple tokens in parallel |
| py-263 | text | optional | `lecture10-slides.py:speculative_sampling` | - EAGLE: draft model takes high-level features from target model |
| py-264 | figure | yes | `lecture10-slides.py:speculative_sampling` | images/medusa-eagle.png |
| py-265 | text | optional | `lecture10-slides.py:speculative_sampling` | Summary: |
| py-266 | text | optional | `lecture10-slides.py:speculative_sampling` | - Exact sampling from target model (thanks to math)! |
| py-267 | text | optional | `lecture10-slides.py:speculative_sampling` | - Exploits asymmetry between checking and generation |
| py-268 | text | optional | `lecture10-slides.py:speculative_sampling` | - Lots of room for innovation on the draft model (involves training) |
| py-269 | text | optional | `lecture10-slides.py:continuous_batching` | Problem: |
| py-270 | text | optional | `lecture10-slides.py:continuous_batching` | - Training: get a dense block of tokens (batch size x sequence length) |
| py-271 | text | optional | `lecture10-slides.py:continuous_batching` | - Inference: requests arrive and finish at different times, so you have a ragged array |
| py-272 | figure | yes | `lecture10-slides.py:continuous_batching` | https://images.ctfassets.net/xjan103pcp94/1LJioEsEdQQpDCxYNWirU6/82b9fbfc5b78b10c1d4508b60e72fdcf/cb_02_diagram-static-batching.png |
| py-273 | text | optional | `lecture10-slides.py:continuous_batching` | Solution: iteration-level scheduling |
| py-274 | text | optional | `lecture10-slides.py:continuous_batching` | - Decode step by step |
| py-275 | text | optional | `lecture10-slides.py:continuous_batching` | - Add new requests to the batch as they arrive (so don't have to wait until generation comple... |
| py-276 | text | optional | `lecture10-slides.py:continuous_batching` | Problem: |
| py-277 | text | optional | `lecture10-slides.py:continuous_batching` | - Batching only works when all sequences have the same dimensionality (right?) |
| py-278 | text | optional | `lecture10-slides.py:continuous_batching` | - But each request might have a different length |
| py-279 | text | optional | `lecture10-slides.py:continuous_batching` | Solution: selective batching |
| py-280 | text | optional | `lecture10-slides.py:continuous_batching` | - Training: when all sequences of the same length, operate on a B x S x H tensor |
| py-281 | text | optional | `lecture10-slides.py:continuous_batching` | - But we might have different lengths: [3, H], [9, H], [5, H], etc. |
| py-282 | text | optional | `lecture10-slides.py:continuous_batching` | - Attention computation: process each sequence separately |
| py-283 | text | optional | `lecture10-slides.py:continuous_batching` | - Non-attention computation: concatenate all the sequences together to [3 + 9 + 5, H] |
| py-284 | text | optional | `lecture10-slides.py:paged_attention` | Paper that introduced vLLM in addition to PagedAttention |
| py-285 | text | optional | `lecture10-slides.py:paged_attention` | Previous status quo: |
| py-286 | text | optional | `lecture10-slides.py:paged_attention` | - Request comes in |
| py-287 | text | optional | `lecture10-slides.py:paged_attention` | - Allocate section of KV cache for prompt and response (up to a max length) |
| py-288 | figure | yes | `lecture10-slides.py:paged_attention` | images/paged-attention-fragmentation.png |
| py-289 | text | optional | `lecture10-slides.py:paged_attention` | Problem: fragmentation (what happens to your hard drive) |
| py-290 | text | optional | `lecture10-slides.py:paged_attention` | - But this is wasteful since we might generate much fewer tokens (internal fragmentation)! |
| py-291 | text | optional | `lecture10-slides.py:paged_attention` | - Might be extra unused space between sections (external fragmentation)! |
| py-292 | text | optional | `lecture10-slides.py:paged_attention` | Solution: PagedAttention (remember operating systems) |
| py-293 | text | optional | `lecture10-slides.py:paged_attention` | - Divide the KV cache of a sequence into non-contiguous **blocks** |
| py-294 | figure | yes | `lecture10-slides.py:paged_attention` | images/paged-attention-blocks.png |
| py-295 | text | optional | `lecture10-slides.py:paged_attention` | Two requests share the KV caches: |
| py-296 | figure | yes | `lecture10-slides.py:paged_attention` | images/paged-attention-logical.png |
| py-297 | text | optional | `lecture10-slides.py:paged_attention` | In general, multiple types of sharing KV caches across sequences: |
| py-298 | figure | yes | `lecture10-slides.py:paged_attention` | images/paged-attention-sharing.png |
| py-299 | text | optional | `lecture10-slides.py:paged_attention` | - Sharing the system prompt |
| py-300 | text | optional | `lecture10-slides.py:paged_attention` | - Sampling multiple responses per prompt (e.g., for program synthesis) |
| py-301 | text | optional | `lecture10-slides.py:paged_attention` | Solution: share prefixes, copy-on-write at the block level |
| py-302 | figure | yes | `lecture10-slides.py:paged_attention` | images/paged-attention-parallel.png |
| py-303 | text | optional | `lecture10-slides.py:paged_attention` | Other vLLM optimizations: |
| py-304 | text | optional | `lecture10-slides.py:paged_attention` | - Kernel to fuse block read and attention (reduce kernel launch overhead) |
| py-305 | text | optional | `lecture10-slides.py:paged_attention` | - Use latest kernels (FlashAttention, FlashDecoding) |
| py-306 | text | optional | `lecture10-slides.py:paged_attention` | - Use CUDA graphs to avoid kernel launch overhead |
| py-307 | text | optional | `lecture10-slides.py:paged_attention` | Summary: use ideas from operating systems (paging) to make use of memory for dynamic workloads |

## Existing Note

- `lecture10-notes.tex`

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
