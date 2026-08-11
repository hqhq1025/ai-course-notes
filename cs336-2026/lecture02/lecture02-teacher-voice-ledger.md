# Lecture 02 Teacher-Voice Ledger

Status: executable-source narration mapped on 2026-08-11.

Lecture 02 has no standalone subtitle file, but `lecture02-slides.py` contains teaching narration in `text(...)` nodes. The ledger records only spoken-style points that are explicitly supported by those nodes; independent editorial explanations remain labeled as `讲义提醒` rather than attributed to the instructor.

| Source node | Spoken point | Why it matters | Where it appears in note |
|---|---|---|---|
| `main():29–38` | Maximize computational efficiency; take away mechanics, resource-accounting mindset, and intuitions rather than ML magic. | Establishes the lecture's teaching contract. | `本讲主线` box `课堂提示：本讲要带走 mechanics、mindset 与 intuitions` |
| `motivating_questions():72–86` | The 70B/15T and 8-H100 estimates are rough back-of-the-envelope calculations; activation omission makes the memory result an upper bound. | Preserves the instructor's reason for doing approximate arithmetic. | `两个 motivating questions` box `老师强调：先做 napkin math，再谈精确排期` |
| `tensors_memory():119–181` | Deep learning can tolerate lower precision, but fp16/bf16 may still be unstable; use bf16 selectively and keep optimizer states in fp32. | Connects dtype diagrams to an operational mixed-precision policy. | `数值格式` box `课堂提示：Mixed precision 是按操作分配精度` |
| `tensor_operations_flops():282–332` | FLOPs and FLOP/s sound the same but measure work and speed; MFU is actual divided by promised FLOP/s, and 0.5 is usually good. | Prevents the central resource-accounting terminology error. | `FLOPs 与 FLOP/s` boxes on the acronym distinction and MFU threshold |
| `gradients_flops():525–556` | Zoom in on one layer, count two backward matmuls, then consider all layers to obtain the 2BP/4BP/6BP rule. | Preserves the derivation path instead of presenting 6BP as a memorized fact. | `Deep network 账本` box `老师强调：先 zoom in，再 consider all layers` |
| `optimizer():633–654` | Optimizer averages are commonly stored in fp32; AdaGrad uses 4 bytes/parameter and Adam 8 bytes/parameter; Transformer accounting is more complicated but follows the same method. | Links numerical stability, memory, and per-step compute. | `Optimizer state 与 training loop` box on fp32 optimizer state and source index rows |
| `gradient_accumulation():719–728` | Large batches improve stability but increase activation memory; accumulate micro-batch gradients and step only after the target batch is reached. | Distinguishes global-batch semantics from peak-memory control. | `Gradient accumulation` box `老师强调：global batch 与 micro-batch 解决不同问题` |
| `activation_checkpointing():734–773` | Activation checkpointing is rematerialization: keep a subset during forward, recompute during backward, and choose frequency as a memory/compute tradeoff. | Makes checkpointing a complexity decision rather than a slogan. | `Activation checkpointing` box `课堂提示：checkpoint frequency 是复杂度选择` |

Editorial attribution rule used in the note:

- `课堂提示` / `老师强调` / `实践经验` is used only for rows above.
- `讲义提醒` is used for synthesis not stated directly by executable narration, such as device-debug order, Roofline limitations beyond the source's ideal model, and the distinction from persistent model checkpoints.
