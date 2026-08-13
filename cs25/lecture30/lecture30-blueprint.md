# Lecture 30 Writing Blueprint

## Core thesis

The lecture is not a general endorsement of `shallow Transformers`. It presents a specific research program: replace part of standard Q/K re-dimensionalization with a learned comparison-weight matrix, derive non-random warm starts from generalized co-occurrences, freeze/caches selected representations to make the lower computation near-shallow, and test whether this enables small application-trained precision language models on edge hardware.

## Evidence layers

1. **Standard background:** dot-product attention, softmax, embedding bottlenecks, perplexity, context padding, packing, and edge latency.
2. **Derived proposal:** single-layer explicit softmax optimization, SAFFU composition, hidden attention targets, bit-cipher embeddings, and dynamic context branches.
3. **Lecture experiments:** warm/cold perplexity curves, MNIST warm starts, configuration tables, medium-model training, and the switch-controller result.
4. **Speaker judgment:** Lottery Ticket motivation, context-faithfulness argument, PLM naming, and possible multimodal/large-scale extensions.
5. **Open limitations:** no matched packing benchmark, no public implementation at lecture time, unsupported layer types, no demonstrated trillion-token/RLHF scale, and multi-second Le Potato latency.

## Planned structure

### 1. 来源、问题与证据边界

- Correct official title, date, speaker, upload, manual subtitles, and video-only slide provenance.
- Explain legacy fabrication removal.
- Define the three questions: how to initialize, where computation can be cached, and what small application-trained models can do.
- Figure: state 002.

### 2. 从标准 attention 到 SAFFU

- Scaffold standard $QK^\top$ attention and distinguish representation projection from weight prediction.
- Define SAFFU and its same-basis/non-negative assumptions.
- Explain the general $W\rightarrow U\rightarrow O$ diagram and why `near-shallow` refers to reusable lower computation rather than a one-layer network.
- Figures: states 003--004.
- Teacher voice: compatibility with conventional projections and the deliberately isolated mechanism.

### 3. 为什么非随机初始化是主线

- Lottery Ticket motivation as intuition, not proof.
- Dimensionality reduction remains necessary.
- Bit-cipher construction, frequency ordering, uniqueness, and identity-versus-semantics distinction.
- Figures: states 005--007.
- Add terminology table for cold start, warm start, explicit solution, priming number, and label embedding.

### 4. 从 generalized co-occurrence 到显式 softmax warm start

- Define $F(H,Y)=H^\top Y$ and the approximate log-co-occurrence solution.
- Explain every symbol and the non-negativity/log assumptions.
- Show the executable bottom-up procedure for feed-forward $U$, attention $W$, and output $O$.
- Explain hidden attention targets and why composition is harder than local layer fitting.
- Figures: states 008--009.
- Include a captioned pseudocode listing.

### 5. Warm start 的实验读法

- Read perplexity trajectories: starting point, same learning rate, early stopping, and what is/not controlled.
- Explain that the single-layer plot has no attention.
- Read MNIST result as layer-level cross-domain evidence, not a complete vision model.
- Discuss average input norm as an estimated priming number.
- Figures: states 010--011.

### 6. Context、multi-context 与 near-shallow caching

- Separate fixed long windows, radial/linguistic contexts, packing, padding, and dynamic batching.
- Explain multi-context branches and parameter subsetting.
- Distinguish bit identity from correlation-rich embeddings.
- Derive cached first-layer comparisons and the frozen-embedding requirement.
- Figures: states 012--016.
- Include a comparison table and a cost formula.

### 7. Precision language models：配置与训练动态

- Define the speaker's PLM term and two reference systems.
- Digest micro/tiny/small/medium/big/large/mega rows rather than merely reproducing the table.
- Explain warm/freeze/thaw stages and BabyLM-scale data.
- Treat GPT-2/A100 timing as rough, unmatched context.
- Ask what small PLMs can and cannot generalize.
- Figures: states 017--021.

### 8. Application-only edge learning

- Explain the no-generic-pretraining hypothesis.
- Reconstruct listen/transcribe/operate/learn loop and label acquisition.
- Show dialogue representation and configuration tables.
- Read positive prediction emergence with data sufficiency and latency caveats.
- Figures: states 022--027.
- Include state-machine pseudocode and a terminology table for edge, air-gapped, ASR, controller, and online/local learning.

### 9. Q&A：适用范围与未完成工作

- No-attention evidence plot.
- Unsupported convolution/activation types.
- Mixed non-negative modalities as a conjectured extension.
- Non-negativity and logarithm.
- No matched packing comparison.
- No public implementation at lecture time.
- No new figure; integrate repeated-screen clarifications.

### 10. 总结与延伸

- Compress the lecture into initialization, reusable computation, and local data loops.
- Provide a release/replication checklist: architecture assumptions, source code, data scale, cache invalidation, baselines, latency, and generalization split.
- Add self-test questions and primary references.

## Quantitative targets

- 27 required figures, each exactly once.
- At least 26 teacher-voice markers.
- At least 30 teaching boxes.
- At least 18 displayed formula blocks and 3 captioned listings.
- At least 11,000 prose characters, with a target above 400 prose characters per figure.
- Warning-free strict coverage, `⭐⭐⭐`, clean two-pass XeLaTeX, and signed 20+ page visual QA.
