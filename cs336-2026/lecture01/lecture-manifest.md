# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture01`

## Files

- `cover.jpg`
- `lecture01-blueprint.md`
- `lecture01-coverage.md`
- `lecture01-manifest.md`
- `lecture01-notes.pdf`
- `lecture01-notes.tex`
- `lecture01-slides.py`

## Local Visual Assets

- `images/chinchilla-isoflop.png`
- `images/compute-memory.png`
- `images/course-staff.png`
- `images/dgx-b200-system-topology.png`
- `images/divine-benevolence.png`
- `images/gpt4-no-details.png`
- `images/industrialisation.jpg`
- `images/marin-loss-forecast.jpg`
- `images/pile-chart.png`
- `images/prefill-decode.png`
- `images/roller-flops.png`
- `images/tokenized-example.png`
- `images/transformer-architecture.png`
- `images/wei-emergence-plot.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | text | optional | `lecture01-slides.py:main` | Next time: resource accounting |
| py-002 | section | yes | `lecture01-slides.py:welcome` | CS336: Language Models From Scratch (Spring 2026) |
| py-003 | figure | yes | `lecture01-slides.py:welcome` | images/course-staff.png |
| py-004 | text | optional | `lecture01-slides.py:welcome` | ...bringing you the 3rd offering of CS336. |
| py-005 | text | optional | `lecture01-slides.py:welcome` | Lectures from 2nd offering (Spring 2025) are on [YouTube](https://www.youtube.com/playlist?li... |
| py-006 | text | optional | `lecture01-slides.py:welcome` | What's new? |
| py-007 | text | optional | `lecture01-slides.py:welcome` | - Same 'from scratch' philosophy |
| py-008 | text | optional | `lecture01-slides.py:welcome` | - Prioritize high value-per-time concepts, don't lose the forest for the trees |
| py-009 | text | optional | `lecture01-slides.py:welcome` | - More coverage of modern LM ingredients (mixture of experts, long-context, agents) |
| py-010 | section | yes | `lecture01-slides.py:why_this_course_exists` | Why did we make this course? |
| py-011 | text | optional | `lecture01-slides.py:why_this_course_exists` | Problem: researchers are becoming **disconnected** from the underlying technology. |
| py-012 | text | optional | `lecture01-slides.py:why_this_course_exists` | - 2016: researchers implemented and trained their own models. |
| py-013 | text | optional | `lecture01-slides.py:why_this_course_exists` | - 2018: researchers downloaded models (e.g., BERT) and fine-tuned them. |
| py-014 | text | optional | `lecture01-slides.py:why_this_course_exists` | - Today: researchers prompt API models (e.g., GPT/Claude/Gemini). |
| py-015 | text | optional | `lecture01-slides.py:why_this_course_exists` | Moving up levels of abstraction boosts productivity, but |
| py-016 | text | optional | `lecture01-slides.py:why_this_course_exists` | - These abstractions are leaky (in contrast to programming languages or operating systems). |
| py-017 | text | optional | `lecture01-slides.py:why_this_course_exists` | - There is still fundamental research to be done that requires tearing up the stack. |
| py-018 | text | optional | `lecture01-slides.py:why_this_course_exists` | **Full understanding** of this technology is necessary for **fundamental research**. |
| py-019 | text | optional | `lecture01-slides.py:why_this_course_exists` | Philosophy of this course: **understanding via building**. |
| py-020 | text | optional | `lecture01-slides.py:why_this_course_exists` | But there's one small problem... |
| py-021 | section | yes | `lecture01-slides.py:why_this_course_exists` | The industrialization of language models |
| py-022 | figure | yes | `lecture01-slides.py:why_this_course_exists` | https://upload.wikimedia.org/wikipedia/commons/c/cc/Industrialisation.jpg |
| py-023 | text | optional | `lecture01-slides.py:why_this_course_exists` | Frontier models are really expensive: |
| py-024 | text | optional | `lecture01-slides.py:why_this_course_exists` | - 2023: GPT-4 supposedly cost $100M to train. |
| py-025 | text | optional | `lecture01-slides.py:why_this_course_exists` | - 2025: xAI builds cluster with 230K GPUs for training Grok. |
| py-026 | text | optional | `lecture01-slides.py:why_this_course_exists` | There are no public details on how frontier models are built. |
| py-027 | text | optional | `lecture01-slides.py:why_this_course_exists` | : |
| py-028 | text | optional | `lecture01-slides.py:why_this_course_exists` | From the GPT-4 technical report |
| py-029 | figure | yes | `lecture01-slides.py:why_this_course_exists` | images/gpt4-no-details.png |
| py-030 | text | optional | `lecture01-slides.py:why_this_course_exists` | Frontier models are out of reach for us. |
| py-031 | text | optional | `lecture01-slides.py:why_this_course_exists` | We could build small language models (<1B parameters), but this might not be representative o... |
| py-032 | text | optional | `lecture01-slides.py:why_this_course_exists` | Example 1: fraction of FLOPs spent in attention versus MLP changes with scale. |
| py-033 | figure | yes | `lecture01-slides.py:why_this_course_exists` | images/roller-flops.png |
| py-034 | text | optional | `lecture01-slides.py:why_this_course_exists` | Example 2: emergence of behavior with scale |
| py-035 | figure | yes | `lecture01-slides.py:why_this_course_exists` | images/wei-emergence-plot.png |
| py-036 | section | yes | `lecture01-slides.py:why_this_course_exists` | What can we learn in this class that transfers to frontier models? |
| py-037 | text | optional | `lecture01-slides.py:why_this_course_exists` | There are three types of knowledge: |
| py-038 | text | optional | `lecture01-slides.py:why_this_course_exists` | - **Mechanics**: how things work (what a Transformer is, how model parallelism works) |
| py-039 | text | optional | `lecture01-slides.py:why_this_course_exists` | - **Mindset**: squeezing the most out of the hardware, taking scaling seriously |
| py-040 | text | optional | `lecture01-slides.py:why_this_course_exists` | - **Intuitions**: which data and modeling decisions yield good accuracy |
| py-041 | text | optional | `lecture01-slides.py:why_this_course_exists` | We can teach mechanics and mindset (these do transfer). |
| py-042 | text | optional | `lecture01-slides.py:why_this_course_exists` | We can only partially teach intuitions (do not necessarily transfer across scales). |
| py-043 | section | yes | `lecture01-slides.py:why_this_course_exists` | Intuitions? 🤷 |
| py-044 | text | optional | `lecture01-slides.py:why_this_course_exists` | Some design decisions are simply not (yet) justifiable and just come from experimentation. |
| py-045 | text | optional | `lecture01-slides.py:why_this_course_exists` | Example: Noam Shazeer paper that introduced SwiGLU |
| py-046 | figure | yes | `lecture01-slides.py:why_this_course_exists` | images/divine-benevolence.png |
| py-047 | section | yes | `lecture01-slides.py:why_this_course_exists` | The bitter lesson |
| py-048 | text | optional | `lecture01-slides.py:why_this_course_exists` | Wrong interpretation: scale is all that matters, algorithms don't matter. |
| py-049 | text | optional | `lecture01-slides.py:why_this_course_exists` | Right interpretation: algorithms that scale are what matter. |
| py-050 | section | yes | `lecture01-slides.py:why_this_course_exists` | accuracy = efficiency x resources |
| py-051 | text | optional | `lecture01-slides.py:why_this_course_exists` | In fact, efficiency is way more important at larger scales (can't afford to be wasteful). |
| py-052 | text | optional | `lecture01-slides.py:why_this_course_exists` | showed 44x algorithmic efficiency on ImageNet between 2012 and 2019. |
| py-053 | text | optional | `lecture01-slides.py:why_this_course_exists` | Framing: what is the best model one can build given a certain compute and data budget? |
| py-054 | text | optional | `lecture01-slides.py:why_this_course_exists` | In other words, **maximize efficiency**! |
| py-055 | section | yes | `lecture01-slides.py:current_lm_landscape` | Pre-neural (before 2010s) |
| py-056 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Language model to measure the entropy of English |
| py-057 | text | optional | `lecture01-slides.py:current_lm_landscape` | - N-gram language models (used in machine translation and speech recognition systems) |
| py-058 | section | yes | `lecture01-slides.py:current_lm_landscape` | Neural ingredients (2010s) |
| py-059 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Long-Short Term Memory (LSTM) |
| py-060 | text | optional | `lecture01-slides.py:current_lm_landscape` | - First neural language model |
| py-061 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Sequence-to-sequence modeling (for machine translation) |
| py-062 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Adam optimizer |
| py-063 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Attention mechanism (for machine translation) |
| py-064 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Transformer architecture (for machine translation) |
| py-065 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Mixture of experts |
| py-066 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Model parallelism |
| py-067 | section | yes | `lecture01-slides.py:current_lm_landscape` | Early foundation models (late 2010s) |
| py-068 | text | optional | `lecture01-slides.py:current_lm_landscape` | - ELMo: pretraining with LSTMs, fine-tuning improves downstream tasks |
| py-069 | text | optional | `lecture01-slides.py:current_lm_landscape` | - BERT: pretraining with Transformer, fine-tuning improves downstream tasks |
| py-070 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Google's T5 (11B): cast everything as text-to-text |
| py-071 | section | yes | `lecture01-slides.py:current_lm_landscape` | Embracing scaling |
| py-072 | text | optional | `lecture01-slides.py:current_lm_landscape` | - OpenAI's GPT-2 (1.5B): fluent text, first signs of zero-shot |
| py-073 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Scaling laws: provide hope / predictability for scaling |
| py-074 | text | optional | `lecture01-slides.py:current_lm_landscape` | - OpenAI's GPT-3 (175B): in-context learning |
| py-075 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Google's PaLM (540B): massive scale, undertrained |
| py-076 | text | optional | `lecture01-slides.py:current_lm_landscape` | - DeepMind's Chinchilla (70B): compute-optimal scaling laws |
| py-077 | section | yes | `lecture01-slides.py:current_lm_landscape` | Open models |
| py-078 | text | optional | `lecture01-slides.py:current_lm_landscape` | Early attempts (attempts to replicate GPT-3): |
| py-079 | text | optional | `lecture01-slides.py:current_lm_landscape` | - EleutherAI's open datasets (The Pile) and models (GPT-J) |
| py-080 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Meta's OPT (175B): GPT-3 replication, lots of hardware issues |
| py-081 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Hugging Face / BigScience's BLOOM (176B): focused on data sourcing |
| py-082 | text | optional | `lecture01-slides.py:current_lm_landscape` | Credible open-weight models (weights + paper): |
| py-083 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Meta's Llama models |
| py-084 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Mistral's models |
| py-085 | text | optional | `lecture01-slides.py:current_lm_landscape` | - DeepSeek's models |
| py-086 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Alibaba's Qwen models |
| py-087 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Moonshot's Kimi models |
| py-088 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Z.ai's GLM models |
| py-089 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Minimax's models |
| py-090 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Xiaomi's MIMO models |
| py-091 | text | optional | `lecture01-slides.py:current_lm_landscape` | These models are approaching closed models (GPT, Claude, Gemini, etc.). |
| py-092 | text | optional | `lecture01-slides.py:current_lm_landscape` | Open-source models (weights + paper + code + data): |
| py-093 | text | optional | `lecture01-slides.py:current_lm_landscape` | - AI2's Olmo models |
| py-094 | text | optional | `lecture01-slides.py:current_lm_landscape` | - NVIDIA's Nemotron models |
| py-095 | text | optional | `lecture01-slides.py:current_lm_landscape` | - Marin's models (open development) |
| py-096 | text | optional | `lecture01-slides.py:current_lm_landscape` | Openness is important for trust and innovation |
| py-097 | text | optional | `lecture01-slides.py:current_lm_landscape` | Ideas from open models enable us to teach CS336. |
| py-098 | text | optional | `lecture01-slides.py:current_lm_landscape` | What is a language model? |
| py-099 | text | optional | `lecture01-slides.py:current_lm_landscape` | - 2018 (BERT): something you fine-tune |
| py-100 | text | optional | `lecture01-slides.py:current_lm_landscape` | - 2020 (GPT-3): something you prompt |
| py-101 | text | optional | `lecture01-slides.py:current_lm_landscape` | - 2022 (ChatGPT): something you talk to |
| py-102 | text | optional | `lecture01-slides.py:current_lm_landscape` | - 2026 (agents): something that acts autonomously |
| py-103 | text | optional | `lecture01-slides.py:current_lm_landscape` | The fundamentals are the same (attention, kernels, optimization). |
| py-104 | text | optional | `lecture01-slides.py:current_lm_landscape` | The specs are different (longer context, inference efficiency matters even more). |
| py-105 | text | optional | `lecture01-slides.py:what_is_this_program` | This is an *executable lecture*, a program whose execution delivers the content of a lecture. |
| py-106 | text | optional | `lecture01-slides.py:what_is_this_program` | Executable lectures make it possible to: |
| py-107 | text | optional | `lecture01-slides.py:what_is_this_program` | - view and run code (since everything is code!), |
| py-108 | text | optional | `lecture01-slides.py:what_is_this_program` | - see the hierarchical structure of the lecture |
| py-109 | text | optional | `lecture01-slides.py:course_logistics` | All information online: |
| py-110 | text | optional | `lecture01-slides.py:course_logistics` | This is a 5-unit class. |
| py-111 | text | optional | `lecture01-slides.py:course_logistics` | Comment from Spring 2024 course evaluation: |
| py-112 | text | optional | `lecture01-slides.py:course_logistics` | > *The entire assignment was approximately the same amount of work as all 5 assignments from ... |
| py-113 | section | yes | `lecture01-slides.py:course_logistics` | Why you should take this course |
| py-114 | text | optional | `lecture01-slides.py:course_logistics` | - You have an obsessive need to understand how things work. |
| py-115 | text | optional | `lecture01-slides.py:course_logistics` | - You want to build up your research engineering muscles. |
| py-116 | section | yes | `lecture01-slides.py:course_logistics` | Why you should not take this course |
| py-117 | text | optional | `lecture01-slides.py:course_logistics` | - You actually want to get research done this quarter. (Talk to your advisor.) |
| py-118 | text | optional | `lecture01-slides.py:course_logistics` | - You are interested in learning about the hottest new techniques in AI (e.g., multimodality,... |
| py-119 | text | optional | `lecture01-slides.py:course_logistics` | - You want to get good results on your own application domain. (You should just prompt or fin... |
| py-120 | section | yes | `lecture01-slides.py:course_logistics` | How you can follow along at home |
| py-121 | text | optional | `lecture01-slides.py:course_logistics` | - All lecture materials and assignments will be posted online, so feel free to follow on your... |
| py-122 | text | optional | `lecture01-slides.py:course_logistics` | - Lectures are recorded via [CGOE](https://cgoe.stanford.edu/). |
| py-123 | section | yes | `lecture01-slides.py:course_logistics` | Assignments |
| py-124 | text | optional | `lecture01-slides.py:course_logistics` | - 5 assignments (basics, systems, scaling laws, data, alignment). |
| py-125 | text | optional | `lecture01-slides.py:course_logistics` | - No scaffolding code, but we provide unit tests and adapter interfaces to help you check cor... |
| py-126 | text | optional | `lecture01-slides.py:course_logistics` | - Implement locally to test for correctness, then run on cluster for benchmarking (accuracy a... |
| py-127 | text | optional | `lecture01-slides.py:course_logistics` | - Leaderboard for some assignments (minimize perplexity given training budget). |
| py-128 | section | yes | `lecture01-slides.py:course_logistics` | AI policy |
| py-129 | text | optional | `lecture01-slides.py:course_logistics` | - Coding agents can solve all the assignments, but you won't learn anything. |
| py-130 | text | optional | `lecture01-slides.py:course_logistics` | - AI can be tremendously useful for answering questions and tutoring. |
| py-131 | text | optional | `lecture01-slides.py:course_logistics` | - You must use our provided AGENTS.md file, which asks the AI to be pedagogically-minded. |
| py-132 | text | optional | `lecture01-slides.py:course_logistics` | - Please read our [AI policy guide](https://docs.google.com/document/d/1SZAlExB1qAc9izHt54gwu... |
| py-133 | section | yes | `lecture01-slides.py:course_logistics` | Compute |
| py-134 | text | optional | `lecture01-slides.py:course_logistics` | - Thanks to [Modal](https://modal.com/) for providing compute. 🙏 |
| py-135 | text | optional | `lecture01-slides.py:course_logistics` | - Please read the [guide](https://docs.google.com/document/d/1cHE0iKVyXLJ3XpIs2XuXTmZ-HMmPk2h... |
| py-136 | text | optional | `lecture01-slides.py:course_syllabus` | Remember it's all about **efficiency**: |
| py-137 | text | optional | `lecture01-slides.py:course_syllabus` | - Resources: data + hardware (compute, memory, communication bandwidth) |
| py-138 | text | optional | `lecture01-slides.py:course_syllabus` | - How do you train the best model given a fixed set of resources? |
| py-139 | text | optional | `lecture01-slides.py:course_syllabus` | Today, we are compute-constrained, so design decisions will reflect squeezing the most out of... |
| py-140 | text | optional | `lecture01-slides.py:course_syllabus` | - Systems: clearly about efficiency |
| py-141 | text | optional | `lecture01-slides.py:course_syllabus` | - Tokenization: working with raw bytes is elegant, but compute-inefficient with today's model... |
| py-142 | text | optional | `lecture01-slides.py:course_syllabus` | - Model architecture: many changes motivated by reducing memory or FLOPs (e.g., sharing KV ca... |
| py-143 | text | optional | `lecture01-slides.py:course_syllabus` | - Data filtering: avoid wasting precious compute updating on bad / irrelevant data |
| py-144 | text | optional | `lecture01-slides.py:course_syllabus` | - Scaling laws: use less compute on smaller models to do hyperparameter tuning |
| py-145 | text | optional | `lecture01-slides.py:course_syllabus` | Tomorrow, we will become data-constrained... |
| py-146 | text | optional | `lecture01-slides.py:basics` | Goal: be able to train a basic language model |
| py-147 | text | optional | `lecture01-slides.py:basics` | Components: tokenization, model architecture, training |
| py-148 | section | yes | `lecture01-slides.py:basics` | Tokenization |
| py-149 | text | optional | `lecture01-slides.py:basics` | What are the atoms that the model operates on? |
| py-150 | text | optional | `lecture01-slides.py:basics` | Formally: a tokenizer converts between raw inputs (bytes) and sequences of integers (tokens) |
| py-151 | figure | yes | `lecture01-slides.py:basics` | images/tokenized-example.png |
| py-152 | text | optional | `lecture01-slides.py:basics` | Popular tokenizer: **Byte-Pair Encoding** (BPE) |
| py-153 | text | optional | `lecture01-slides.py:basics` | Intuition: break input into frequently-occuring chunks |
| py-154 | text | optional | `lecture01-slides.py:basics` | Efficiency lens |
| py-155 | text | optional | `lecture01-slides.py:basics` | - Reduce context length (1000 bytes → ~250 tokens) |
| py-156 | text | optional | `lecture01-slides.py:basics` | - Adaptive computation (more modeling capacity on interesting parts of input) |
| py-157 | text | optional | `lecture01-slides.py:basics` | The dream: tokenizer-free model architectures, which operate directly on bytes |
| py-158 | text | optional | `lecture01-slides.py:basics` | These are promising, but have not yet been scaled up to the frontier. |
| py-159 | section | yes | `lecture01-slides.py:basics` | Model architecture |
| py-160 | text | optional | `lecture01-slides.py:basics` | Starting point: original Transformer |
| py-161 | figure | yes | `lecture01-slides.py:basics` | images/transformer-architecture.png |
| py-162 | text | optional | `lecture01-slides.py:basics` | Refinements: |
| py-163 | text | optional | `lecture01-slides.py:basics` | - Activation functions: ReLU, SwiGLU |
| py-164 | text | optional | `lecture01-slides.py:basics` | - Positional encodings: sinusoidal, RoPE |
| py-165 | text | optional | `lecture01-slides.py:basics` | - Normalization: LayerNorm, RMSNorm, QK norm, pre-norm versus post-norm |
| py-166 | text | optional | `lecture01-slides.py:basics` | - Attention: full, sparse/local attention, group-query attention (GQA), multi-head latent att... |
| py-167 | text | optional | `lecture01-slides.py:basics` | - Recurrence/state-space models/linear attention: Mamba, Gated DeltaNet |
| py-168 | text | optional | `lecture01-slides.py:basics` | - MLP: dense, mixture of experts |
| py-169 | text | optional | `lecture01-slides.py:basics` | - Shape (hidden dimension, depth, number of heads, number of experts) |
| py-170 | section | yes | `lecture01-slides.py:basics` | Training |
| py-171 | text | optional | `lecture01-slides.py:basics` | How do you set the parameters of the model? |
| py-172 | text | optional | `lecture01-slides.py:basics` | - Loss function (e.g., multi-token prediction) |
| py-173 | text | optional | `lecture01-slides.py:basics` | - Optimizer (e.g., AdamW, SOAP, Muon) |
| py-174 | text | optional | `lecture01-slides.py:basics` | - Initialization scale (e.g., Xavier init, muP) |
| py-175 | text | optional | `lecture01-slides.py:basics` | - Learning rate schedule (e.g., cosine, WSD) |
| py-176 | text | optional | `lecture01-slides.py:basics` | - Regularization (e.g., dropout, weight decay) |
| py-177 | text | optional | `lecture01-slides.py:basics` | - Batch size (e.g., critical batch size) |
| py-178 | text | optional | `lecture01-slides.py:basics` | - MoE specific: load balancing (e.g., aux-free) |
| py-179 | section | yes | `lecture01-slides.py:basics` | Assignment 1 (basics) |
| py-180 | text | optional | `lecture01-slides.py:basics` | - Implement BPE tokenizer |
| py-181 | text | optional | `lecture01-slides.py:basics` | - Implement Transformer, cross-entropy loss, AdamW optimizer, training loop |
| py-182 | text | optional | `lecture01-slides.py:basics` | - Do resource accounting |
| py-183 | text | optional | `lecture01-slides.py:basics` | - Train on TinyStories and OpenWebText |
| py-184 | text | optional | `lecture01-slides.py:basics` | - Leaderboard: minimize OpenWebText perplexity given 45 minutes on a B200 |
| py-185 | text | optional | `lecture01-slides.py:basics` | High-level principle: everything is about balancing the following: |
| py-186 | text | optional | `lecture01-slides.py:basics` | - Expressivity (can represent complex dependencies in the data) |
| py-187 | text | optional | `lecture01-slides.py:basics` | - Stability (keep parameter and gradient norms in goldilocks zone) |
| py-188 | text | optional | `lecture01-slides.py:basics` | - Efficiency (runs fast on hardware, both training and inference) |
| py-189 | text | optional | `lecture01-slides.py:systems` | Goal: squeeze the most out of the hardware (GPU or TPU) |
| py-190 | text | optional | `lecture01-slides.py:systems` | Components: kernels, parallelism, inference |
| py-191 | section | yes | `lecture01-slides.py:systems` | Basics |
| py-192 | text | optional | `lecture01-slides.py:systems` | - Resource accounting: memory and compute characteristics of a model |
| py-193 | figure | yes | `lecture01-slides.py:systems` | images/compute-memory.png |
| py-194 | text | optional | `lecture01-slides.py:systems` | - Model parameters must be moved from memory (HBM) to the compute (SMs) |
| py-195 | text | optional | `lecture01-slides.py:systems` | - Example: B200 can perform 2.25 PFLOP/sec (bf16) with 8TB/sec memory bandwidth |
| py-196 | text | optional | `lecture01-slides.py:systems` | - Roofline analysis: understand whether we're compute-bound or memory-bound |
| py-197 | text | optional | `lecture01-slides.py:systems` | - Benchmarking and profiling (nsight): see what happens in practice |
| py-198 | text | optional | `lecture01-slides.py:systems` | [DGX B200](https://docs.nvidia.com/dgx/dgxb200-user-guide/introduction-to-dgxb200.html): |
| py-199 | figure | yes | `lecture01-slides.py:systems` | https://docs.nvidia.com/dgx/dgxb200-user-guide/_images/dgx-b200-system-topology.png |
| py-200 | section | yes | `lecture01-slides.py:systems` | Kernels |
| py-201 | text | optional | `lecture01-slides.py:systems` | - Kernel is a function that runs on GPU |
| py-202 | text | optional | `lecture01-slides.py:systems` | - When using PyTorch, each primitive operation launches a standard kernel |
| py-203 | text | optional | `lecture01-slides.py:systems` | - Can write custom kernels to make GPUs go brrr |
| py-204 | text | optional | `lecture01-slides.py:systems` | - Principle: organize computation to minimize data movement |
| py-205 | text | optional | `lecture01-slides.py:systems` | - Naive: read HBM; compute A; write HBM; read HBM; compute B; write HBM |
| py-206 | text | optional | `lecture01-slides.py:systems` | - Fused: read HBM; compute A and B; write HBM |
| py-207 | text | optional | `lecture01-slides.py:systems` | - Strategies: operator fusion (matmul + activation), tiling (FlashAttention) |
| py-208 | text | optional | `lecture01-slides.py:systems` | - Warp divergence, memory coalescing, bank conflicts, occupancy, bulk-async memory transfers |
| py-209 | text | optional | `lecture01-slides.py:systems` | - Write kernels in CUDA/**Triton**/CUTLASS/ThunderKittens |
| py-210 | section | yes | `lecture01-slides.py:systems` | Parallelism |
| py-211 | text | optional | `lecture01-slides.py:systems` | - What if we have 1024 GPUs? |
| py-212 | text | optional | `lecture01-slides.py:systems` | - Data movement between GPUs is even slower, but same 'minimize data movement' principle holds |
| py-213 | text | optional | `lecture01-slides.py:systems` | - Use classic collective operations (e.g., gather, reduce, all-reduce) |
| py-214 | text | optional | `lecture01-slides.py:systems` | - Shard memory (parameters, activations, gradients, optimizer states) across GPUs |
| py-215 | text | optional | `lecture01-slides.py:systems` | - How to split computation: {data,tensor,pipeline,sequence,expert} parallelism |
| py-216 | section | yes | `lecture01-slides.py:systems` | Inference |
| py-217 | text | optional | `lecture01-slides.py:systems` | Goal: generate tokens given a prompt (needed to actually use models!) |
| py-218 | text | optional | `lecture01-slides.py:systems` | Inference is also needed for reinforcement learning, test-time compute, evaluation |
| py-219 | text | optional | `lecture01-slides.py:systems` | Two phases: prefill and decode |
| py-220 | figure | yes | `lecture01-slides.py:systems` | images/prefill-decode.png |
| py-221 | text | optional | `lecture01-slides.py:systems` | - Prefill (similar to training): tokens are given, can process all at once (compute-bound) |
| py-222 | text | optional | `lecture01-slides.py:systems` | - Decode: need to generate one token at a time (memory-bound) |
| py-223 | text | optional | `lecture01-slides.py:systems` | Methods to speed up decoding: |
| py-224 | text | optional | `lecture01-slides.py:systems` | - Use cheaper model (via model pruning, quantization, distillation) |
| py-225 | text | optional | `lecture01-slides.py:systems` | - Speculative decoding: use a cheaper "draft" model to generate multiple tokens, then use the... |
| py-226 | text | optional | `lecture01-slides.py:systems` | - Systems optimizations: fused kernels, continuous batching |
| py-227 | section | yes | `lecture01-slides.py:systems` | Assignment 2 (systems) |
| py-228 | text | optional | `lecture01-slides.py:systems` | - Implement a fused RMSNorm kernel in Triton |
| py-229 | text | optional | `lecture01-slides.py:systems` | - Implement distributed data parallel training |
| py-230 | text | optional | `lecture01-slides.py:systems` | - Implement optimizer state sharding |
| py-231 | text | optional | `lecture01-slides.py:systems` | - Benchmark and profile the implementations |
| py-232 | text | optional | `lecture01-slides.py:systems` | Recommended book: [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) |
| py-233 | text | optional | `lecture01-slides.py:systems` | - Nicely lays out how to approach systems for LLMs conceptually |
| py-234 | text | optional | `lecture01-slides.py:systems` | - From Google, so it foregrounds TPUs, but high-level concepts are similar |
| py-235 | text | optional | `lecture01-slides.py:scaling_laws` | Setting: if you had 1e25 FLOPs of compute, what hyperparameters would you use to train a good... |
| py-236 | text | optional | `lecture01-slides.py:scaling_laws` | Too expensive to do hyperparameter tuning at full scale! |
| py-237 | text | optional | `lecture01-slides.py:scaling_laws` | Key conceptual shift: instead of a single scale, think of a **scaling recipe** (FLOPs → hyper... |
| py-238 | text | optional | `lecture01-slides.py:scaling_laws` | For a scaling recipe: |
| py-239 | text | optional | `lecture01-slides.py:scaling_laws` | - Run experiments to compute the loss at various smaller scales (e.g., up to 1e24 FLOPs) |
| py-240 | text | optional | `lecture01-slides.py:scaling_laws` | - Fit a scaling law to predict the loss of the scaling recipe at the target scale (e.g., 1e25... |
| py-241 | text | optional | `lecture01-slides.py:scaling_laws` | Now you can: |
| py-242 | text | optional | `lecture01-slides.py:scaling_laws` | 1. Optimize the scaling recipe targeting a larger scale using smaller scale experiments |
| py-243 | text | optional | `lecture01-slides.py:scaling_laws` | 2. Predict the loss at the target scale before actually running the experiment! |
| py-244 | text | optional | `lecture01-slides.py:scaling_laws` | Scaling laws don't happen automatically, they require careful construction of a scaling recipe. |
| py-245 | text | optional | `lecture01-slides.py:scaling_laws` | Parameterize the model in a way to get **hyperparameter transfer** |
| py-246 | text | optional | `lecture01-slides.py:scaling_laws` | Predictability is at least as important as optimality! |
| py-247 | text | optional | `lecture01-slides.py:scaling_laws` | Question: given a FLOPs budget (C = 6 N D), use a bigger model (N) or train on more tokens (D)? |
| py-248 | text | optional | `lecture01-slides.py:scaling_laws` | Classic compute-optimal scaling laws: |
| py-249 | text | optional | `lecture01-slides.py:scaling_laws` | - ISOFLOP curves: for multiple small FLOPs budgets, find optimal N |
| py-250 | text | optional | `lecture01-slides.py:scaling_laws` | - Then fit a scaling law to extrapolate to large FLOPs budgets |
| py-251 | figure | yes | `lecture01-slides.py:scaling_laws` | images/chinchilla-isoflop.png |
| py-252 | text | optional | `lecture01-slides.py:scaling_laws` | TL;DR: D = 20 N is roughly optimal (e.g., 70B parameter model should be trained on ~1.4T tokens) |
| py-253 | text | optional | `lecture01-slides.py:scaling_laws` | Caveat: this doesn't take into account inference costs (want a smaller model) |
| py-254 | text | optional | `lecture01-slides.py:scaling_laws` | Live example from Marin |
| py-255 | figure | yes | `lecture01-slides.py:scaling_laws` | https://pbs.twimg.com/media/HDuErvvbsAAQ5Yt?format=jpg&name=4096x4096 |
| py-256 | text | optional | `lecture01-slides.py:scaling_laws` | Should be done training this week, should see how well we match the preregistered loss! |
| py-257 | section | yes | `lecture01-slides.py:scaling_laws` | Assignment 3 (scaling laws) |
| py-258 | text | optional | `lecture01-slides.py:scaling_laws` | - We define a training API (hyperparameters → loss) based on previous runs |
| py-259 | text | optional | `lecture01-slides.py:scaling_laws` | - Submit "training jobs" (under a FLOPs budget) and gather data points |
| py-260 | text | optional | `lecture01-slides.py:scaling_laws` | - Fit scaling laws to the data points |
| py-261 | text | optional | `lecture01-slides.py:scaling_laws` | - Submit extrapolated hyperparameters and loss predictions |
| py-262 | text | optional | `lecture01-slides.py:scaling_laws` | - Leaderboard: minimize loss given FLOPs budget |
| py-263 | text | optional | `lecture01-slides.py:data` | Question: What capabilities do we want the model to have? |
| py-264 | text | optional | `lecture01-slides.py:data` | Multilingual? Good at conversation? Agentic coding capabilities? |
| py-265 | section | yes | `lecture01-slides.py:data` | Evaluation |
| py-266 | text | optional | `lecture01-slides.py:data` | What is the purpose of evaluation? |
| py-267 | text | optional | `lecture01-slides.py:data` | 1. Internal: guide model development (smoothness across scales, relative performance matters) |
| py-268 | text | optional | `lecture01-slides.py:data` | 2. External: measure absolute quality of a real use case (ecological validity matters) |
| py-269 | text | optional | `lecture01-slides.py:data` | Examples of evaluations: |
| py-270 | text | optional | `lecture01-slides.py:data` | 1. Perplexity: ideally run on private documents not on Internet (avoid contamination) |
| py-271 | text | optional | `lecture01-slides.py:data` | 2. Advanced use cases: GPQA, HLE, SWE-Bench, Terminal-Bench |
| py-272 | text | optional | `lecture01-slides.py:data` | LMs are general purpose, require a diverse set of evaluations! |
| py-273 | section | yes | `lecture01-slides.py:data` | Data curation |
| py-274 | text | optional | `lecture01-slides.py:data` | - Data does not just fall from the sky. |
| py-275 | text | optional | `lecture01-slides.py:data` | - Sources: webpages crawled from the Internet, books, arXiv papers, GitHub code, etc. |
| py-276 | figure | yes | `lecture01-slides.py:data` | https://ar5iv.labs.arxiv.org/html/2101.00027/assets/pile_chart2.png |
| py-277 | text | optional | `lecture01-slides.py:data` | - Appeal to fair use to train on copyright data? |
| py-278 | text | optional | `lecture01-slides.py:data` | - Might have to license data (e.g., Google with Reddit data) |
| py-279 | text | optional | `lecture01-slides.py:data` | - Raw data is HTML, PDF, directories (not text), requires processing |
| py-280 | section | yes | `lecture01-slides.py:data` | Data processing |
| py-281 | text | optional | `lecture01-slides.py:data` | - Transformation: convert HTML/PDF to text (extract main content) |
| py-282 | text | optional | `lecture01-slides.py:data` | - Filtering: keep high quality data, remove harmful content (via classifiers) |
| py-283 | text | optional | `lecture01-slides.py:data` | - Deduplication: save compute, avoid memorization; use Bloom filters or MinHash |
| py-284 | text | optional | `lecture01-slides.py:data` | - Data mixing: how much to upweight/downweight each source? |
| py-285 | text | optional | `lecture01-slides.py:data` | - Rewriting / synthetic data: use LM to augment real data, more similar to downstream tasks |
| py-286 | text | optional | `lecture01-slides.py:data` | Types of data: |
| py-287 | text | optional | `lecture01-slides.py:data` | - Pretraining data: large and diverse |
| py-288 | text | optional | `lecture01-slides.py:data` | - Mid-training data: high quality, including long-context |
| py-289 | text | optional | `lecture01-slides.py:data` | - Post-training data: supervised fine-tuning (conversations, agentic traces with tool calling) |
| py-290 | section | yes | `lecture01-slides.py:data` | Assignment 4 (data) |
| py-291 | text | optional | `lecture01-slides.py:data` | - Convert Common Crawl HTML to text |
| py-292 | text | optional | `lecture01-slides.py:data` | - Train classifiers to filter for quality and harmful content |
| py-293 | text | optional | `lecture01-slides.py:data` | - Deduplication using MinHash |
| py-294 | text | optional | `lecture01-slides.py:data` | - Leaderboard: minimize perplexity given token budget |
| py-295 | text | optional | `lecture01-slides.py:alignment` | So far, we have trained a model on full supervision (predict the next token). |
| py-296 | text | optional | `lecture01-slides.py:alignment` | Now that the model should be reasonable, we can improve it further from **weak supervision**. |
| py-297 | text | optional | `lecture01-slides.py:alignment` | Why weak supervision? When it is easier to critique than to generate. |
| py-298 | text | optional | `lecture01-slides.py:alignment` | Basic template: |
| py-299 | text | optional | `lecture01-slides.py:alignment` | 1. Generate responses from the model. |
| py-300 | text | optional | `lecture01-slides.py:alignment` | 2. Score responses with a {human, verifier, LM judge}. |
| py-301 | text | optional | `lecture01-slides.py:alignment` | 3. Update the model to prefer better responses. |
| py-302 | text | optional | `lecture01-slides.py:alignment` | Algorithms: |
| py-303 | text | optional | `lecture01-slides.py:alignment` | - Proximal Policy Optimization (PPO) from reinforcement learning |
| py-304 | text | optional | `lecture01-slides.py:alignment` | - Direct Policy Optimization (DPO): for preference data, simpler |
| py-305 | text | optional | `lecture01-slides.py:alignment` | - Group Relative Preference Optimization (GRPO): remove value function |
| py-306 | text | optional | `lecture01-slides.py:alignment` | Challenges: |
| py-307 | text | optional | `lecture01-slides.py:alignment` | - RL algorithms are unstable and hard to tune |
| py-308 | text | optional | `lecture01-slides.py:alignment` | - At scale, this requires a lot of new infrastructure (inference with async rollouts) |
| py-309 | text | optional | `lecture01-slides.py:alignment` | - Constantly trading off systems efficiency and on-policyness |
| py-310 | section | yes | `lecture01-slides.py:alignment` | Assignment 5 (alignment) |
| py-311 | text | optional | `lecture01-slides.py:alignment` | - Implement Direct Preference Optimization (DPO) |
| py-312 | text | optional | `lecture01-slides.py:alignment` | - Implement Group Relative Preference Optimization (GRPO) |
| py-313 | text | optional | `lecture01-slides.py:tokenization` | This unit was inspired by Andrej Karpathy's video on tokenization; check it out! |
| py-314 | text | optional | `lecture01-slides.py:tokenization` | Summary: |
| py-315 | text | optional | `lecture01-slides.py:tokenization` | - Tokenizer: strings ↔ tokens (indices) |
| py-316 | text | optional | `lecture01-slides.py:tokenization` | - Character-based, byte-based, word-based tokenization are highly suboptimal |
| py-317 | text | optional | `lecture01-slides.py:tokenization` | - BPE is an effective heuristic that is data-driven |
| py-318 | text | optional | `lecture01-slides.py:tokenization` | - Tokenization is a separate step, maybe one day do it end-to-end from bytes... |
| py-319 | text | optional | `lecture01-slides.py:tokenization` | But whatever solution needs to satisfy: |
| py-320 | text | optional | `lecture01-slides.py:tokenization` | 1. Model (e.g., Transformer) should operate on chunks (abstractions) of the sequence (text, v... |
| py-321 | text | optional | `lecture01-slides.py:tokenization` | 2. Chunks should be variable (allocate more model capacity to interesting chunks) |
| py-322 | text | optional | `lecture01-slides.py:intro_to_tokenization` | Raw text is generally represented as Unicode strings. |
| py-323 | text | optional | `lecture01-slides.py:intro_to_tokenization` | A language model places a probability distribution over sequences of tokens (usually represen... |
| py-324 | text | optional | `lecture01-slides.py:intro_to_tokenization` | So we need a procedure that *encodes* strings into tokens. |
| py-325 | text | optional | `lecture01-slides.py:intro_to_tokenization` | We also need a procedure that *decodes* tokens back into strings. |
| py-326 | text | optional | `lecture01-slides.py:intro_to_tokenization` | is a class that implements the encode and decode methods. |
| py-327 | text | optional | `lecture01-slides.py:intro_to_tokenization` | A |
| py-328 | text | optional | `lecture01-slides.py:tokenization_examples` | To get a feel for how tokenizers work, play with this |
| py-329 | section | yes | `lecture01-slides.py:tokenization_examples` | Observations |
| py-330 | text | optional | `lecture01-slides.py:tokenization_examples` | - A word and its preceding space are part of the same token (e.g., " world"). |
| py-331 | text | optional | `lecture01-slides.py:tokenization_examples` | - A word at the beginning and in the middle are represented differently (e.g., "hello hello"). |
| py-332 | text | optional | `lecture01-slides.py:tokenization_examples` | - Numbers are tokenized into every few digits. |
| py-333 | text | optional | `lecture01-slides.py:tokenization_examples` | Here's the GPT-5 tokenizer from OpenAI (tiktoken) in action. |
| py-334 | text | optional | `lecture01-slides.py:tokenization_examples` | Check that encode() and decode() roundtrip: |
| py-335 | text | optional | `lecture01-slides.py:tokenization_examples` | Compression ratio: number of bytes per token |
| py-336 | text | optional | `lecture01-slides.py:tokenization_examples` | The larger the compression ratio, the shorter the sequence (good since attention is quadratic... |
| py-337 | text | optional | `lecture01-slides.py:tokenization_examples` | One could increase compression ratio by increasing **vocabulary size** (number of possible to... |
| py-338 | text | optional | `lecture01-slides.py:tokenization_examples` | Let's take a look at the actual vocabulary: |
| py-339 | text | optional | `lecture01-slides.py:character_tokenizer` | A Unicode string is a sequence of Unicode characters. |
| py-340 | text | optional | `lecture01-slides.py:character_tokenizer` | Each character can be converted into a code point (integer) via `ord`. |
| py-341 | text | optional | `lecture01-slides.py:character_tokenizer` | It can be converted back via `chr`. |
| py-342 | text | optional | `lecture01-slides.py:character_tokenizer` | Now let's build a `Tokenizer` and make sure it round-trips: |
| py-343 | text | optional | `lecture01-slides.py:character_tokenizer` | There are approximately 150K Unicode characters. |
| py-344 | text | optional | `lecture01-slides.py:character_tokenizer` | Problem 1: this is a very large vocabulary. |
| py-345 | text | optional | `lecture01-slides.py:character_tokenizer` | Problem 2: many characters are quite rare (e.g., 🌍), which is inefficient use of the vocabulary. |
| py-346 | text | optional | `lecture01-slides.py:character_tokenizer` | This tokenizer is the worst of both worlds (large vocabulary, low compression ratio). |
| py-347 | text | optional | `lecture01-slides.py:byte_tokenizer` | Unicode strings can be represented as a sequence of bytes, which can be represented by intege... |
| py-348 | text | optional | `lecture01-slides.py:byte_tokenizer` | The most common Unicode encoding is |
| py-349 | text | optional | `lecture01-slides.py:byte_tokenizer` | Some Unicode characters are represented by one byte: |
| py-350 | text | optional | `lecture01-slides.py:byte_tokenizer` | Others take multiple bytes: |
| py-351 | text | optional | `lecture01-slides.py:byte_tokenizer` | Now let's build a `Tokenizer` and make sure it round-trips: |
| py-352 | text | optional | `lecture01-slides.py:byte_tokenizer` | The vocabulary is nice and small: a byte can represent 256 values. |
| py-353 | text | optional | `lecture01-slides.py:byte_tokenizer` | What about the compression rate? |
| py-354 | text | optional | `lecture01-slides.py:byte_tokenizer` | The compression ratio is terrible, which means the sequences will be too long. |
| py-355 | text | optional | `lecture01-slides.py:byte_tokenizer` | Given that the context length of a Transformer is limited (since attention is quadratic), thi... |
| py-356 | text | optional | `lecture01-slides.py:word_tokenizer` | Another approach (closer to what was done classically in NLP) is to split strings into words. |
| py-357 | text | optional | `lecture01-slides.py:word_tokenizer` | This regular expression keeps all alphanumeric characters together (words). |
| py-358 | text | optional | `lecture01-slides.py:word_tokenizer` | To turn this into a `Tokenizer`, we need to map these chunks into integers. |
| py-359 | text | optional | `lecture01-slides.py:word_tokenizer` | Then, we can build a mapping from each chunk into an integer. |
| py-360 | text | optional | `lecture01-slides.py:word_tokenizer` | What's good: each token is meaningful (since humans invented words). |
| py-361 | text | optional | `lecture01-slides.py:word_tokenizer` | Compression ratio is good, but vocabulary size can be huge. |
| py-362 | text | optional | `lecture01-slides.py:word_tokenizer` | Moreover: |
| py-363 | text | optional | `lecture01-slides.py:word_tokenizer` | - Many words are rare and the model won't learn much about them. |
| py-364 | text | optional | `lecture01-slides.py:word_tokenizer` | - This doesn't obviously provide a fixed vocabulary size. |
| py-365 | text | optional | `lecture01-slides.py:word_tokenizer` | - New words we haven't seen during training get a special UNK token, which is ugly and can me... |
| py-366 | section | yes | `lecture01-slides.py:bpe_tokenizer` | Byte Pair Encoding (BPE) |
| py-367 | text | optional | `lecture01-slides.py:bpe_tokenizer` | The BPE algorithm was introduced by Philip Gage in 1994 for data compression. |
| py-368 | text | optional | `lecture01-slides.py:bpe_tokenizer` | It was adapted to NLP for neural machine translation. |
| py-369 | text | optional | `lecture01-slides.py:bpe_tokenizer` | (Previously, papers had been using word-based tokenization.) |
| py-370 | text | optional | `lecture01-slides.py:bpe_tokenizer` | BPE was then used by GPT-2. |
| py-371 | text | optional | `lecture01-slides.py:bpe_tokenizer` | Basic idea: *train* the tokenizer on raw text to construct a vocabulary tailored to the data. |
| py-372 | text | optional | `lecture01-slides.py:bpe_tokenizer` | Intuition: common sequences of bytes are represented by a single token, rare sequences are re... |
| py-373 | text | optional | `lecture01-slides.py:bpe_tokenizer` | Sketch: start with each byte as a token, and successively merge the most common pair of adjac... |
| py-374 | section | yes | `lecture01-slides.py:bpe_tokenizer` | Training the tokenizer |
| py-375 | section | yes | `lecture01-slides.py:bpe_tokenizer` | Using the tokenizer |
| py-376 | text | optional | `lecture01-slides.py:bpe_tokenizer` | Now, given a new text, we can encode it. |
| py-377 | text | optional | `lecture01-slides.py:bpe_tokenizer` | In Assignment 1, you will go beyond this in the following ways: |
| py-378 | text | optional | `lecture01-slides.py:bpe_tokenizer` | - encode() currently loops over all merges. Only loop over merges that matter. |
| py-379 | text | optional | `lecture01-slides.py:bpe_tokenizer` | - Detect and preserve special tokens (e.g., <\|endoftext\|>). |
| py-380 | text | optional | `lecture01-slides.py:bpe_tokenizer` | - Use pre-tokenization (e.g., the GPT-2 tokenizer regex). |
| py-381 | text | optional | `lecture01-slides.py:bpe_tokenizer` | - Try to make the implementation as fast as possible. |
| py-382 | text | optional | `lecture01-slides.py:train_bpe` | Start with the list of bytes of `string`. |

## Existing Note

- `lecture01-notes.tex`

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
