# Lecture 34 Teacher-Voice Ledger

| Time | Spoken point | Why it matters | Planned placement |
|---|---|---|---|
| 00:01:20--00:01:58 | The V5 overview is organized around pretraining/data, post-training, applications, and current weaknesses. | Establishes the lecture's real teaching spine. | Opening roadmap |
| 00:06:23--00:07:32 | Embeddings convert words into dense vectors; contextual embeddings fix the one-vector-per-word limitation. | Supplies first-use intuition before attention. | Embeddings |
| 00:07:37--00:08:19 | Q/K/V are explained with a library query, book summary, and book contents analogy. | Preserves the instructor's concrete attention explanation. | QKV section |
| 00:08:34--00:09:16 | Positional encodings restore order, while layers and heads expand the relations the model can capture. | Connects components into the final Transformer. | Transformer assembly |
| 00:09:20--00:10:10 | Modern LLMs are scaled Transformer systems trained on large web corpora, then adapted by post-training. | Prevents treating architecture alone as the product. | LLM systems |
| 00:12:38--00:14:46 | Human learning is continuous, goal-driven, multimodal, structured, and far more data-efficient; these are hypotheses, not solved mechanisms. | Frames the small-data study without overclaiming brain equivalence. | Human/LLM comparison |
| 00:14:49--00:16:20 | The child-directed-speech study tests whether children's input distribution can improve small language models. | States the study question and evidence boundary. | TinyDialogues study |
| 00:19:43--00:20:18 | Diverse data beat pure child-directed speech, while synthetic TinyDialogues beats natural conversation but not the strongest mixed corpus. | Preserves the negative and mixed result. | TinyDialogues findings |
| 00:21:03--00:22:30 | Two-phase pretraining moves from broad data to a high-quality blend and prototypes mixtures at smaller token budgets. | Connects data selection to staged optimization. | Two-phase method |
| 00:22:30--00:23:11 | All tested phase-two blends beat simple continuation; benefits persist when token count and model size increase. | Core empirical result. | Two-phase evidence |
| 00:23:11--00:24:00 | Too much phase-two upsampling causes diminishing returns; phase duration is a tunable variable. | Adds the non-monotonic caveat. | Data-mixture warning |
| 00:25:09--00:26:20 | Post-training includes task adaptation, prompting, retrieval, and feedback; CoT can expose intermediate behavior but does not guarantee faithful reasoning. | Frames post-training as several interfaces. | Post-training opening |
| 00:26:25--00:29:12 | CoT extensions search, decompose, execute code, or attach notes; each changes the inference procedure rather than the pretrained weights. | Prevents acronym-list teaching. | CoT taxonomy |
| 00:29:13--00:31:32 | Prompting methods are inference-time scaffolds; RLHF/DPO/RLAIF instead change the model using human or AI preference signals. | Separates compute-time and training-time interventions. | Feedback transition |
| 00:31:32--00:34:13 | GRPO, KTO, and variational preference learning encode group-relative rewards, loss aversion, or heterogeneous preference profiles. | Explains why preference optimization is not one universal objective. | Preference methods |
| 00:34:20--00:35:20 | An agent adds environment, goals, tools, memory, decisions, and actions around a foundation model. | Defines agents beyond a single call. | Agent stack |
| 00:35:20--00:39:10 | Refinement, reflection, ReAct, and LATS use feedback and search differently; LATS combines multiple paths with MCTS-like selection. | Gives a mechanism-level self-improvement taxonomy. | Agent mechanisms |
| 00:39:11--00:41:34 | ViTs tokenize image patches; CLIP and VLMs align image and language representations. | Carries Transformer abstractions into vision. | Vision applications |
| 00:41:34--00:45:16 | fMRI data can be modeled as ROI-by-time sequences with masked prediction and cross-attention. | Explains the neuroscience case from data interface to objective. | fMRI foundations |
| 00:45:16--00:48:02 | Cross-attention predicts held-out brain regions; learned representations improve downstream disease classification over correlation/linear baselines. | Connects architecture to evidence and limits. | fMRI results |
| 00:48:03--00:50:01 | Future applications are broad, but missing capabilities include controllability, memory, embodiment, autonomy, and social/ethical reasoning. | Separates opportunity lists from capability gaps. | Future and missing ingredients |
| 00:50:05--00:54:40 | Smaller on-device models, interpretability, data limits, saturation, catastrophic forgetting, and new architectures are presented as open research directions. | Prevents “just scale” from becoming the only roadmap. | Scaling limits |
| 00:54:43--00:57:10 | Continual learning means permanent post-deployment capability updates, not merely RAG, in-context memory, distillation, or periodic retraining. | Enforces a strict first-use definition. | Continual learning |
| 00:57:10--01:00:16 | ROME/MEMIT, mistake-driven updates, lifelong MoE, compressed prompt memory, and progressive prompts address different slices of continual learning. | Digests a dense terminology cluster and preserves the instructor's opinion that weight updates may be needed for “true” learning. | Continual-learning survey |

## In-note obligations

- Use at least 22 explicit teacher-voice markers.
- Preserve negative and mixed results in both data studies.
- Distinguish inference-time prompting, parameter-updating preference optimization, agent-loop search, retrieval/memory, and continual weight updates.
- Label broad future claims and human-learning analogies as instructor framing or open hypotheses.
