# Lecture 33 Teacher-Voice Ledger

The standalone edit starts roughly 30:24 later than the same talk inside the combined Lecture 27 upload. Times below use the standalone video `orDKvo8h71o`, not the combined recording.

| Time | Spoken point | Why it matters | Planned placement |
|---|---|---|---|
| 00:02:05--00:02:58 | When progress is too fast to follow, study the change itself by comparing old and current systems. | Frames the talk as a research method rather than Transformer trivia. | Opening |
| 00:03:03--00:04:07 | Identify the dominant force, understand it, then roll it forward; even imperfect forecasts can be valuable. | Defines the speaker's approximate forecasting framework. | Dominant-force method |
| 00:04:40--00:05:57 | A falling pen can ignore drag because gravity dominates and is well modeled. | Teaches when simplification is legitimate. | Pen thought experiment |
| 00:07:05--00:07:55 | AI may be simpler than it looks because a dominant force exists; the claim is deliberately opinionated. | Preserves epistemic status. | Compute opening |
| 00:08:00--00:09:03 | Compute per dollar has followed a strong long-run trend; researchers should exploit rather than fight it. | Connects the historical plot to strategy. | Compute-cost section |
| 00:09:17--00:11:19 | Modeling how humans think they think can impose shortcuts that later become bottlenecks; the Bitter Lesson favors general methods plus scale. | Central principle behind the architecture analysis. | Bitter Lesson |
| 00:12:04--00:13:27 | The least structured method may be unusable today; add useful bias for the current regime but remember to remove it later. | Prevents the false conclusion that all structure is bad. | Inductive-bias lifecycle |
| 00:13:27--00:14:23 | Research incentives reward adding structure more than removing it; long-run winners can look worse now. | Adds a social mechanism to the technical argument. | Research incentives warning |
| 00:16:11--00:17:26 | A Transformer is first a sequence model: tokenize, embed, and model interactions, often with attention. | Supplies first-principles scaffolding. | Architecture foundations |
| 00:23:39--00:27:08 | Encoder-decoder and decoder-only can be made nearly identical through four local parameter and attention changes. | Turns architecture labels into a derivation. | Four-step transformation |
| 00:27:08--00:28:45 | Separate input and target parameters made sense for translation but are less natural for general world knowledge. | Shows that inductive bias is task- and era-dependent. | Translation case study |
| 00:28:47--00:30:46 | FLAN-T5 gained more than PaLM in academic instruction tuning; long inputs and short targets matched encoder-decoder structure. | Preserves the surprising empirical result and the speaker's hypothesis. | FLAN case study |
| 00:30:47--00:31:35 | Long generation and multi-turn chat weaken the input/target separation assumption. | Connects historical architecture to modern interaction. | FLAN follow-up |
| 00:31:50--00:33:01 | Cross-attending only to the final encoder layer may become a granularity bottleneck at extreme depth. | Makes the layer-alignment change a scale question, not cosmetic diagram editing. | Representation hierarchy |
| 00:33:11--00:35:12 | Bidirectionality helped difficult 2018 tasks but may matter less at scale and forces re-encoding in multi-turn chat. | Links quality and serving cost. | Bidirectionality and cache |
| 00:35:42--00:36:18 | Repeating this historical analysis helps identify current assumptions that should be replaced by more general scalable methods. | States the transferable research habit. | Conclusion |

## In-note obligations

- Use at least 14 explicit teacher-voice markers.
- Preserve the difference between empirical observation, historical interpretation, anecdotal evidence, hypothesis, and extrapolation.
- Do not import the combined video's later joint Q\&A into the standalone note.
- Keep compute availability, inductive bias, architecture structure, and systems cost as distinct analytical layers.
