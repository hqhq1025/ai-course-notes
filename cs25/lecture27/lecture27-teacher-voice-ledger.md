# Lecture 27 Teacher-Voice Ledger

| Time | Spoken point | Why it matters | Planned placement |
|---|---|---|---|
| 00:00:55--00:01:27 | The fundamental question is why language models work so well; manually inspect data to build intuition. | Establishes the research method rather than starting from an abstract theory. | Opening and data-inspection section |
| 00:01:31--00:02:32 | Jason learned the lung-cancer classification task himself and gained intuitions that led to research. | Shows that domain contact changes the questions a researcher can ask. | Data-inspection case study |
| 00:04:17--00:07:03 | Next-word prediction on a large corpus is massive multi-task learning. | Core interpretation of pretraining. | Latent-task section |
| 00:07:21--00:08:51 | Even punctuation and arbitrary continuations define hidden tasks. | Prevents reducing pretraining to a neat benchmark list. | Arbitrary-task example |
| 00:09:15--00:10:44 | Compute is treated as model size times data, and loss can be predicted over many orders of magnitude. | Gives the operational meaning of the scaling-law slide. | Scaling section |
| 00:11:13--00:12:55 | Why scaling works is not settled; memorizing tail facts and representing more complex functions are hand-wavy guesses. | Preserves uncertainty and separates evidence from mechanism. | Scaling caveat box |
| 00:13:08--00:15:32 | Smooth overall loss is a weighted mixture of task losses; easy tasks can saturate while hard tasks improve later. | Explains how smooth aggregate curves coexist with abrupt task scores. | Emergence derivation |
| 00:16:54--00:19:24 | BIG-Bench tasks show smooth, flat, inverse, noisy, and emergent-looking curves. | Replaces a single emergence story with a taxonomy. | BIG-Bench reading guide |
| 00:20:28--00:23:56 | U-shaped scaling can arise from three hidden subtasks: repeat, repair a quote, and follow the instruction. | Gives a compositional explanation instead of mystical capability language. | U-shaped worked example |
| 00:23:59--00:25:51 | Plot scaling curves for a research intervention; one point cannot show whether the intervention saturates or accelerates. | Converts the talk into a reusable experimental method. | Jason conclusion |
| 00:26:19--00:26:40 | Training data are not automatically separated into good and bad; source filtering still matters. | Adds a practical data-quality caveat. | Data-quality warning |
| 00:28:29--00:29:00 | Pre-emergence curves may give no obvious warning, and intermediate model sizes are often missing. | Limits claims of predictability. | Emergence warning |
| 00:29:53--00:30:21 | Changing the metric can change the appearance of emergence; the underlying abilities are still real in Jason's view. | Separates metric geometry from useful behavior. | Emergence metric caveat |
| 00:32:29--00:33:22 | When progress is too fast to follow, study the change itself by comparing old and current systems. | Frames the second talk as methodology rather than history trivia. | Hyung opening |
| 00:33:27--00:34:31 | Identify the dominant force, understand it, then roll it forward; even a low hit rate can be valuable if one prediction matters greatly. | Explains why approximate forecasting can be rational. | Dominant-force framework |
| 00:35:04--00:36:21 | The falling pen can ignore drag because gravity dominates and is well modeled. | Provides the simplification analogy used throughout the talk. | Pen thought experiment |
| 00:37:29--00:38:19 | AI may be simpler than it looks because a dominant force exists; the coming argument is deliberately opinionated. | Preserves the speaker's epistemic status. | Compute-scaling caveat |
| 00:38:24--00:39:27 | Compute per dollar has followed an exceptionally strong long trend; do not compete with it, leverage it. | Connects the historical plot to research strategy. | Compute-cost section |
| 00:39:41--00:41:43 | Modeling how humans think they think can impose shortcuts that later become bottlenecks; the Bitter Lesson favors general methods plus scale. | Core principle behind the architecture analysis. | Bitter Lesson section |
| 00:42:28--00:43:51 | The least structured method may be unusable today; add the optimal bias for the current regime, but remember to remove it later. | Avoids the simplistic conclusion that all structure is bad. | Inductive-bias lifecycle |
| 00:43:51--00:44:47 | Research incentives reward adding structure more than removing it; long-run winners can look worse now. | Adds a social mechanism and practical research warning. | Research incentives box |
| 00:46:35--00:47:50 | A Transformer is first a sequence model: tokenize, embed, and model interactions, often with attention. | Supplies first-principles scaffolding. | Architecture foundations |
| 00:54:03--00:57:32 | Encoder-decoder and decoder-only can be made nearly identical through four parameter and attention changes. | Turns architecture categories into an explicit derivation. | Four-step transformation |
| 00:57:32--00:59:09 | Separate input and target parameters made sense for translation but are less natural for general world knowledge. | Shows that an inductive bias is task- and era-dependent. | Translation case study |
| 00:59:11--01:01:10 | FLAN-T5 gained more than PaLM in academic instruction tuning; long inputs and short targets accidentally matched encoder-decoder structure. | Preserves a surprising empirical result and its hypothesis. | FLAN case study |
| 01:01:11--01:01:59 | Long generation and multi-turn chat weaken the input/target separation assumption. | Connects historical architecture to modern interaction patterns. | FLAN follow-up |
| 01:02:14--01:03:25 | Cross-attending only to the final encoder layer may become a granularity bottleneck at extreme depth. | Makes the layer-alignment change more than a cosmetic diagram edit. | Representation hierarchy |
| 01:03:35--01:05:36 | Bidirectionality helped difficult 2018 tasks but may matter less at scale and forces re-encoding in multi-turn chat. | Links model quality and systems efficiency. | Bidirectionality and cache |
| 01:06:06--01:06:42 | Repeated historical analyses help ask which current assumptions should be revisited and replaced by a more general scalable method. | States the transferable research habit. | Hyung conclusion |
| 01:12:39--01:14:34 | Architecture may not be today's bottleneck; maximum-likelihood training with one correct target may be a stronger structural limitation, while RLHF is one imperfect alternative. | Important Q&A extension beyond the deck. | Final extension on objectives |
| 01:15:17--01:16:54 | Moore's-law transistor counts are a red herring; available compute, accelerators, low precision, specialization, energy, and physics are the real trajectory variables. | Qualifies the compute trend without treating it as guaranteed. | Final caveats and open questions |

## In-note obligations

- Use at least 20 explicit markers such as `课堂提示`, `讲者强调`, `讲义提醒`, or `实践经验`.
- Preserve the difference between empirical observation, hand-wavy mechanism, anecdotal result, and historical interpretation.
- Include both Q&A extensions: metric dependence of emergence and the possibility that the learning objective, not architecture, is now the stronger bottleneck.
