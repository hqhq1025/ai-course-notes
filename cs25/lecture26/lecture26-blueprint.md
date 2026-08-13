# Lecture 26 Rewrite Blueprint

## Acceptance target

- Replace the legacy note completely; do not preserve its fabricated operations/governance storyline.
- Use the official 114-page deck as the visual spine and cover all 91 required teaching pages exactly once.
- Target 70+ pages, 30,000+ prose characters, 60+ teaching boxes, 20+ teacher-voice markers, 12+ displayed formulas, and at least three captioned listings.
- Keep prose above 300 characters per figure on average, with denser local explanations for benchmark tables, architecture diagrams, attention mechanics, autonomy levels, and multi-agent communication states.

## Teaching arc

| Section | Required slides | Core question | Required treatment |
|---|---:|---|---|
| 1. 课程定位与 NLP 历史 | 001, 011, 013--018 | Transformer 为什么会取代早期 NLP pipeline？ | Course scope; rule systems, embeddings, seq2seq; attention timeline; historical caveats. |
| 2. Attention 与 Transformer 机制 | 019--027 | Q/K/V、self-attention、multi-head 与 cross-attention 分别解决什么？ | QKV formulas and library analogy; scaled dot-product attention; causal/self/cross distinction; RNN comparison. |
| 3. Scale、Emergence 与 Alignment | 028--033, 035--043 | 大模型能力来自规模、训练过程还是度量方式？ | LLM objective/cost; emergence and metric artifact; beyond scaling; RLHF/DPO; ChatGPT/GPT-4/Gemini as 2024 examples; MoE. |
| 4. Transformer 的跨域应用 | 045--051 | 同一架构如何跨越文本、音频、视觉、机器人、游戏与生物？ | Modality table; why tokenization/representation differs; avoid name-list treatment. |
| 5. LLM 的限制与适应 | 053--069 | 数据、记忆、更新、解释与幻觉为何仍是系统瓶颈？ | Compute concentration; BabyLM; small/on-device models; memory/RAG; Phi/data quality; memorization; continual learning; interpretability; ROME; MoE; reflection; calibration. |
| 6. 推理脚手架 | 070--076 | 中间推理何时帮助，何时只是把错误写得更长？ | CoT mechanics and error taxonomy; small-model limits; generalized CoT; ToT; Socratic questioning; visible reasoning caveat. |
| 7. 从模型到 Agent | 078--085, 087--088 | 为什么一次模型调用不足以成为 agent？ | Agent stack; flight/driving demos as speaker claims; human-like interface rationale; autonomy levels; API versus direct interaction; Action API. |
| 8. Neural Compute Unit、记忆与个性化 | 090--094 | 把 LLM 看成 compute unit 后，系统还缺哪些部件？ | Token-in/token-out analogy; MIPS/CPU limits of analogy; looped Transformer; persistent memory; retrieval hierarchy; personalization and privacy. |
| 9. Multi-Agent 通信 | 096--100, 103--104, 107 | 并行 worker 如何避免自然语言协议失真？ | Parallelism benefit; manager/worker hierarchy; structured messages; verification; conflict and redo paths; state synchronization. |
| 10. 可靠性、LLM OS 与安全边界 | 109--113 | 长轨迹 agent 如何从错误中恢复并被安全部署？ | Stochastic compounding; observability; human fallback/2FA; plan divergence; AutoGPT critique; LLM OS mapping; generalized system; error correction, permissions, sandboxing. |

## Mandatory scaffolding

1. Attention background: Q/K/V table, scaled dot-product formula, multi-head formula, and self/cross-attention comparison.
2. Emergence: distinguish discontinuous task metrics from discontinuous underlying capability; explain what the slide does not prove.
3. RLHF/DPO: preference-data pipeline and the difference between reward-model training and direct preference optimization.
4. MoE: define expert routing, sparse activation, capacity/load balancing, and why “different brain regions” is only an intuition.
5. RAG/memory: define embeddings, vector search, persistent memory, personalization, and the difference between stored knowledge and skill learning.
6. Continual learning/model editing: contrast retraining, fine-tuning, retrieval, model editing, and online adaptation.
7. Reasoning methods: CoT, ToT, Socratic decomposition, failure visibility, and small-model limitations.
8. Agents: model call versus stateful feedback loop; action space; autonomy levels; API versus UI control; least privilege.
9. Multi-agent: manager/worker state machine, typed message schema, verification/redo loop, and synchronization hazards.
10. LLM OS: map model/context/memory/tools/peripherals/other models while warning that the analogy does not supply isolation, scheduling, or correctness automatically.

## Teacher-voice obligations

- Use at least 20 in-note markers such as `课堂提示`, `讲者强调`, `讲义提醒`, or `实践经验`.
- Preserve the instructors' uncertainty and questions: emergence may be a metric artifact; scaling is not the only lever; memorization versus learning is unresolved; continual learning is not ordinary retraining; CoT exposes but does not guarantee reasoning; single-call models are not agents; communication and correction are harder than parallelism.
- Label period-specific claims, startup demos, and product comparisons as April 2024 classroom evidence.
- Preserve the final deployment warning: error correction, security, user permissions, human fallback, and sandboxing remain unsolved system requirements.

## Visual QA watch list

- Dense attention/QKV diagrams and Transformer/RNN table.
- Emergence plots, DPO equation, model comparison slides, and MoE diagrams.
- Application mosaics and BabyLM/Phi result plots.
- ROME/model-editing and reasoning diagrams.
- Agent demo screenshots, autonomy chart, Action API, and memory hierarchy.
- Multi-agent progressive diagrams, plan-divergence plot, Karpathy LLM-OS diagram, and final generalized-system architecture.
