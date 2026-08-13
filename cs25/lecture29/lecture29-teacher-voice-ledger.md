# Lecture 29 Teacher-Voice Ledger

| Time | Spoken point | Why it matters | Planned note location |
|---|---|---|---|
| 00:01:04--00:01:54 | Albert frames the talk as architecture plus interpretation and deliberately inserts open research questions for the open-source community. | The lecture is not only a Mixtral product description; unresolved questions are part of the syllabus. | Source framing |
| 00:02:18--00:03:36 | GQA and sliding-window attention are not new inventions; Mistral 7B combines known choices into a strong dense baseline. | Prevents novelty inflation and motivates the dense-to-sparse comparison. | Dense baseline |
| 00:03:36--00:06:49 | Transformer design contains many small choices, so the speaker writes a tensor-shape-annotated PyTorch layer rather than relying on a block diagram. | Preserves the implementation-oriented teaching style. | Dense layer code |
| 00:07:01--00:08:24 | MoE is an old idea; Switch Transformers and the 2017 sparsely-gated layer made the parallelism and gating tradeoffs concrete. | Places Mixtral in a lineage rather than presenting it as a new category. | MoE history |
| 00:08:24--00:09:18 | The router computes gates, selects top two experts, applies expert MLPs, and forms a weighted sum. | Gives the spoken algorithm behind the slide equation. | Routing mechanism |
| 00:09:38--00:10:17 | A token sees only active parameters; the speaker links this to the cost-performance frontier, multilingual capability, 32K context, and Apache 2.0 release. | Separates per-token computation from total model capacity while preserving the release-time claims. | Mixtral overview |
| 00:10:32--00:11:44 | The speaker calls “MLPs store knowledge, attention stores algorithms/reasoning” conventional wisdom and expects MoE-fying MLPs to help knowledge most. | Must be taught as a hypothesis, not a theorem. | Why MoE-fy MLPs |
| 00:11:44--00:12:38 | Albert explains the active-parameter x-axis and says the largest gain is on knowledge-heavy tasks; other categories improve less. | Supplies the correct reading order and limits the benchmark conclusion. | Performance plots |
| 00:12:38--00:14:03 | MoE-fying Q/K/V is an open question; prior attempts could diverge in bf16 even when fp32 worked. | Connects architectural ambition to numerical stability. | MoE attention question |
| 00:14:15--00:15:09 | There are eight experts in every Transformer layer, and expert labels are permutation-equivalent within a layer. | Corrects the misleading intuition that Mixtral has eight global experts. | Myth 1 |
| 00:15:09--00:15:41 | Shared attention and gating mean the model is not 56B; the lecture reports roughly 46.7B total and 12.9B active parameters. | Establishes total-versus-active accounting. | Myth 2 |
| 00:15:41--00:16:49 | Serving cost is not proportional to active parameters because dynamic routing introduces communication and scheduling overhead. | Prevents the most common systems error. | Myth 3 |
| 00:16:49--00:17:36 | Inference waits for the most loaded expert; the speaker suggests capacity-aware rerouting and mixture-of-depth-style ideas as open directions. | Makes load balance a latency problem, not merely a training regularizer. | Inference load balance |
| 00:17:36--00:19:15 | Compression may exploit structure inside expert MLPs, but extreme SMoE sparsification had not yet produced convincing results. | Preserves the speculative status of the compression slide. | Compression |
| 00:19:15--00:20:24 | Discrete gating exposes which experts receive which tokens and may offer a cleaner interpretability handle than dense activations or many attention heads. | Explains why the lecture switches from architecture to interpretation. | Interpretability motivation |
| 00:20:24--00:22:28 | Pile-domain routing is near-uniform at shallow/deep layers; a mid-layer math/code spike is interesting but explicitly speculative. | Prevents over-reading a colorful histogram as named domain experts. | Domain experiment |
| 00:22:46--00:25:18 | Consecutive tokens route to the same expert more often than chance, especially around layer 15, then the effect weakens near the final layer. | Adds the layer-wise interpretation the table alone does not convey. | Consecutive-token analysis |
| 00:25:18--00:27:22 | Token maps do not reveal clean human-readable domains; coding-only experts would also leave other experts idle during code generation. | Connects interpretability uncertainty to utilisation efficiency. | Myth 4 |
| 00:27:22--00:28:38 | Within roughly a day of release, the open community found a striking expert ablation and turned it into a meme. | Captures the “open weights enable rapid inspection” lesson without treating the ablation as a full explanation. | Treasure hunt |
| 00:28:38--00:29:30 | Experts may encode linear combinations or subspaces unlike human concepts; recovering those features remains open. | Gives the lecture's real interpretability conclusion. | Interpretation agenda |
| 00:31:45--00:33:10 | Sparse activation does not remove the need to load all experts; dense models can be better for memory-constrained edge devices, while MoE benefits centralized serving. | Adds the memory-residency caveat. | Edge versus cloud Q&A |
| 00:37:12--00:39:48 | MoE gains have two dimensions: more capacity for knowledge and more efficient adaptive computation; mixture of depths changes how many parameters activate, while Mixtral changes which experts activate. | Provides a useful taxonomy of sparsity. | Adaptive computation Q&A |
| 00:40:43--00:41:36 | Communication is more expensive across nodes than across GPUs, and routing cost grows with token movement and topology. | Grounds expert parallelism in hardware. | Communication accounting |
| 00:42:47--00:43:33 | MoE throughput benefits become clearer at high batch size and large serving scale; use case and scale determine whether sparsity helps. | Prevents universal deployment claims. | Throughput Q&A |
| 00:43:50--00:44:40 | Continued pretraining or fine-tuning on a domain can be hard to beat; Mixtral experts are not explicit medical or coding modules. | Separates MoE capacity from domain adaptation. | Domain adaptation Q&A |
| 00:50:42--00:51:47 | Naively resident memory scales with total parameters, not active parameters; CPU expert offload trades GPU memory for transfer overhead. | Completes the systems memory model. | Memory/offload Q&A |
| 00:52:12--00:52:42 | The geometric mean of active and total parameters may be a rough dense-equivalent heuristic only when training tokens and data quality are comparable. | Labels a rule of thumb as conditional. | Capability heuristics |
| 00:53:26--00:54:41 | Better math scores do not cleanly separate knowledge recall from reasoning; benchmark categories themselves are ambiguous. | Stops the note from claiming that MoE creates new reasoning algorithms. | Benchmark caveat |
| 00:54:56--00:56:17 | MoE consumes more resident memory and complicates serving, but high-volume batches can recover throughput benefits. | States the deployment tradeoff in the speaker's own terms. | Serving synthesis |
| 00:56:31--00:57:48 | Mixtral keeps the Mistral 7B attention block and replaces only the MLP with top-two-of-eight expert MLPs. | Resolves a common architecture misunderstanding. | Block-level architecture |
| 00:58:20--00:58:58 | Training needs balanced expert loads; the team did not encounter a major training failure on Mixtral. | Distinguishes necessary balancing from reported project experience. | Training Q&A |
| 00:59:02--00:59:43 | RAG and MoE are orthogonal: dense/MoE models can each be used with or without retrieval. | Prevents architecture and knowledge-access mechanisms from being conflated. | RAG Q&A |
| 00:59:43--01:00:54 | Swapping in a domain expert is possible in principle, but the router must be retrained to use it. | Shows why experts are not plug-and-play modules. | Modular experts Q&A |
| 01:01:10--01:02:08 | Routing remains end-to-end differentiable; training compute is roughly tied to active parameters plus extra communication. | Addresses gradient-flow and cost misconceptions. | Training mechanics |
| 01:02:26--01:04:14 | More experts may increase specialization choices but make multi-node serving and communication harder; quantized Mixtral 8x7B can still be practical on one GPU. | Closes with a scale-dependent engineering judgment. | Scaling experts Q&A |

## In-note obligations

- Use at least 24 explicit teacher-voice markers.
- Preserve the distinction among measured benchmark evidence, speaker intuition, open research questions, and Q&A engineering judgment.
- Treat automatic-caption spellings as noisy transcription, not canonical terminology.
- Keep the long Q&A integrated into the teaching flow rather than attaching it as an unstructured appendix.
