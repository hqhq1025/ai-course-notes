# Lecture 37 Teacher-Voice Ledger

| Time | Spoken point | Why it matters | Planned note location |
|---|---|---|---|
| 00:00:52--00:02:30 | Zhou declines the abstract debate over whether LLMs “really reason” and fixes an operational definition: intermediate tokens between input and output. | Prevents the note from turning a mechanism lecture into an anthropomorphic philosophy claim. | Operational definition |
| 00:03:18--00:05:10 | The last-letter task was chosen after first-letter concatenation proved too easy because web acronyms leaked the pattern into pretraining. | Preserves the research-design lesson that synthetic tasks must avoid accidental shortcuts. | Last-letter example |
| 00:05:18--00:06:20 | The Boolean-circuit result explains why output tokens can substitute for depth on inherently serial computation. | Connects CoT to computational expressivity rather than “thinking like a human.” | Intermediate-token theory |
| 00:06:20--00:08:30 | The provocative claim is that pretrained LLMs may already contain reasoning trajectories; decoding can expose them without prompting or finetuning. | Separates latent capability from the procedure used to select a trajectory. | Pretrained reasoning |
| 00:08:30--00:12:10 | More candidates are not enough; Zhou rejects length as a selector and uses confidence on the final answer token. | Turns CoT decoding into a concrete ranking rule and exposes its calibration assumptions. | CoT decoding |
| 00:12:40--00:16:20 | Few-shot CoT works but needs task-specific exemplars; “let's think step by step” is generic but weaker. Zhou calls both interfaces unnatural. | Explains why a successful prompt is not yet a satisfying training solution. | Prompting tradeoffs |
| 00:16:20--00:19:55 | SFT is generic but generalizes poorly; the classroom warning is “don't scale blindly” when the learning paradigm is wrong. | Preserves the negative result and stops data volume from being presented as a universal cure. | SFT limits |
| 00:20:00--00:24:50 | Replacing human traces with model-generated candidate traces plus answer-based rejection enables iterative self-improvement; the model's own distribution matters. | Motivates rejection sampling and the transition from imitation to outcome-guided learning. | RL finetuning origin |
| 00:24:50--00:27:30 | The first ML principle is to optimize what is wanted: generation quality. Gradient machinery is secondary to defining the target. | Keeps objective design ahead of optimizer details. | Direct objective |
| 00:27:30--00:30:20 | A reliable verifier matters more than the exact RL algorithm; automatically checkable tasks are currently the favorable regime. | Establishes the core bottleneck and evidence boundary for RL reasoning. | Verification |
| 00:30:20--00:31:20 | Scaling reasoning can mean scaling output length, not only model depth; Zhou explicitly separates CoT reasoning from CoT prompting. | Prevents terminology collapse and connects training scale to the earlier theorem. | Scaling reasoning |
| 00:31:20--00:39:59 | The 2025 arithmetic puzzle illustrates long emergent traces. Zhou views human-like trajectories as useful but reiterates that LLMs are probabilistic models, and he distinguishes learned reasoning from exhaustive search. | Preserves both the intuition and the anti-anthropomorphic caveat. | Emergent traces and search |
| 00:40:17--00:45:10 | Token-level maximum likelihood does not align with answer-level probability; marginalizing over many reasoning paths motivates self-consistency. | Provides the probabilistic derivation behind majority aggregation. | Marginalization |
| 00:45:10--00:50:58 | Consistency rises with accuracy and can support confidence estimates, but the result is benchmark- and setup-dependent. | Adds calibration intuition without turning correlation into a guarantee. | Self-consistency evidence |
| 00:50:58--00:56:31 | Universal self-consistency handles free-form outputs; retrieval and abstraction supply missing knowledge or analogies. Zhou rejects the retrieval-versus-reasoning debate in favor of combining them. | Connects aggregation, retrieval, and deep research into one inference stack. | USC and retrieval |
| 00:56:31--00:57:30 | The final agenda is to move beyond unique verifiable answers and build real applications rather than saturating benchmarks. | Carries the lecture's actual research frontier into the final synthesis. | Open problems |
| 00:57:30--01:01:00 | In Q\&A, answer-token confidence is described as empirically useful for hallucination signals, while symbolic search remains a tool a model may invoke rather than the definition of reasoning itself. | Preserves the scope of the confidence claim and the search distinction. | Q\&A: confidence and search |
| 01:01:00--01:06:04 | Zhou admits that training-time distribution reshaping is poorly understood, answer extraction needs careful parsers, self-consistency is imperfect, AGI timelines are uncertain, and useful applications remain a harder test than demos. | Captures uncertainty and prevents the note from overstating a compact set of heuristics. | Q\&A: unresolved limits |

## In-note obligations

- Use at least 18 explicit teacher-voice markers such as `课堂提示`、`老师强调`、`讲义提醒`、`实践经验`.
- Define reasoning operationally before using anthropomorphic language.
- Preserve the first-letter shortcut story, the “don't scale blindly” warning, verifier primacy, and the distinction between learned reasoning and external search.
- Treat confidence, self-consistency, Gemini examples, and deep-research products as dated empirical evidence rather than universal guarantees.
- Keep the final skepticism about AGI timelines and the demand for real applications.
