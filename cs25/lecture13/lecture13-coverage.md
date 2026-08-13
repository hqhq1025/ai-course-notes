# Lecture 13 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V002 | Establish title, speaker, outline, and the two linked stories: emergence and CoT. | Administrative framing is brief but retained because it defines the lecture map. | 来源审计与阅读地图 |
| V003--V006 | Contrast the paper title, smooth scaling laws, scientific emergence, and an operational definition. | Smooth loss does not by itself predict task thresholds. | 平滑 scaling laws 与 emergent abilities |
| V007--V010 | Define chance-level few-shot emergence and unpack MMLU/IPA-style examples. | Threshold location depends on metric, model family, prompt, and baseline. | Few-shot 阈值 |
| V011 | Explain inverse scaling and why a larger scale can reverse the trend into a U-shape. | A partial curve cannot prove permanent degradation. | Inverse scaling |
| V012 | Show RLHF or another prompting/post-training technique helping only after sufficient scale. | Do not conflate prompting, RLHF, and pretraining scale. | Emergent prompting techniques |
| V013 | Interpret the hand-drawn ability frontier and unresolved white region. | Parameter thresholds are empirical, not natural constants. | 阈值为什么会移动 |
| V014--V015 | Compare model families and a controlled verb-frequency ablation. | The PaLM causal story is a running hypothesis; the toy ablation is stronger controlled evidence. | Better data |
| V016 | Explain how targeted fine-tuning can induce known desired behavior in a smaller model. | Capability discovery and capability transfer are different problems. | Fine-tuning desired behaviors |
| V017 | Compare parameters, FLOPs, loss, and perplexity as scale/quality axes. | Perplexity is a held-out next-token metric, not a universal downstream score. | Measure of scale |
| V018 | Explain few-shot crossover beyond task-specific fine-tuned baselines. | Result does not imply fine-tuning is obsolete for latency-constrained known tasks. | Surprising fine-tuning |
| V019 | Synthesize emergence, data, post-training, and uncertainty. | Preserve the speaker's open questions and 2023 evidence boundary. | Emergence evidence boundary |
| V020--V021 | Introduce the CoT paper, motivation, standard prompt, and worked reasoning prompt. | CoT changes inference context without changing weights. | Chain-of-thought mechanism |
| F001--F002 | Pair the live Playground failure and success states. | Same arithmetic task; the visible intervention is intermediate reasoning exemplars. | Live CoT demo |
| V022 | Preserve the classroom transition into the live demo. | Slide is sparse; video evidence carries the content. | Live CoT demo |
| V023 | Explain GSM8K and StrategyQA curves and the scale-dependent CoT delta. | Gains emerge only for sufficiently capable models. | CoT scaling |
| V024 | Explain BBH construction and prompt format. | BBH is a selected difficult subset, so baseline comparisons are conditional on construction. | BIG-Bench Hard |
| V025 | Read average score, human threshold, and task-level red/blue map. | Mean score and fraction above human answer different questions. | BBH results |
| V026 | Show that CoT's positive delta appears only beyond a model-scale threshold. | Threshold is model-family and benchmark specific. | BBH scaling |
| V027 | Explain flat answer-only curves versus emergent CoT performance. | CoT can unlock a measured ability; it does not prove human-like internal reasoning. | BBH emergence |
| V028 | Explain MGSM construction and unexpectedly strong Bengali/low-frequency-language results. | Evidence supports compositional generalization, not complete language parity. | Multilingual CoT |
| V029 | Analyze which error classes improve when scaling PaLM 62B to 540B. | Error categories are empirical diagnostics, not a full causal mechanism. | Why scaling helps CoT |
| V030 | Place standard prompting and CoT on a task-complexity / model-scale spectrum. | The boundary shifts with data, post-training, tools, and evaluation. | Task spectrum |
| V031 | Derive diverse-path sampling and majority vote. | Voting assumes answer extraction and some diversity among paths. | Self-consistency mechanism |
| V032 | Read benchmark gains and relate them to inference-time cost. | More samples are not free; optimal budget depends on task and latency. | Self-consistency results |
| V033 | Explain why self-consistency itself appears scale-dependent. | Small models can generate many consistently wrong paths. | Self-consistency emergence |
| V034 | Synthesize class discussion about prompting durability and few-shot generalization. | Open questions remain open; avoid retroactive certainty. | Chain-of-thought discussion |
| V035 | State the lecture's core conclusions. | Conclusions are about observed model families and benchmarks as of 2023-01-24. | Conclusions |
| V036 | Preserve Jason Wei's personal research agenda. | Clearly label recommendations as the speaker's 2023 view. | Looking forward |
| V037 | Omitted intentionally as a pure thanks/contact slide. | No teaching content is lost. | Manifest only |
| T001--T043 | Weave motivation, caveats, live-demo interpretation, Q&A, negative controls, costs, and open problems into prose and boxes. | Transcript claims are paraphrased rather than fabricated as quotations. | Across all sections |
