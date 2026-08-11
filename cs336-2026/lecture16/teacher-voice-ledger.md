# Lecture 16 Teacher Voice Ledger

| Time | Spoken point | Why it matters | Planned placement |
|---|---|---|---|
| `00:08:00--00:08:09` | PPO's value model can be as large as the policy model. | Makes the memory and tuning cost of PPO concrete. | PPO implementation section, slides 8--17. |
| `00:11:17--00:11:29` | Practical PPO can require stabilization hacks and environment-specific choices. | Prevents the clean objective from being mistaken for a complete implementation recipe. | PPO practice warning. |
| `00:12:54--00:13:07` | The “DPO is offline” distinction is overstated because DPO can be iterated online. | Clarifies that algorithm labels do not determine the whole data-collection loop. | Transition from PPO/DPO to GRPO. |
| `00:15:14--00:15:32` | GRPO replaces a learned value baseline with same-prompt group-normalized rewards. | Gives the core mental model before the formula. | GRPO introduction, slides 18--20. |
| `00:23:46--00:23:59` | Per-token length normalization systematically changes which responses receive larger updates. | Turns “length bias” into an optimization effect the reader can reason about. | GRPO objective audit, slides 22--24. |
| `00:30:22--00:31:11` | The celebrated “aha moment” is partly overstated: length growth can be objective bias and self-reflection already exists in the base model. | Separates causal evidence from a compelling training narrative. | DeepSeek R1-Zero evidence, slides 29--30. |
| `00:34:20--00:35:01` | Much of long-CoT capability can be transferred by distillation once a strong generator exists. | Explains why SFT and RL are complements rather than mutually exclusive routes. | R1 distillation section, slides 33--38. |
| `00:41:03--00:41:49` | Dataset construction and difficulty curriculum are central to RL, unlike ordinary SFT where data is often simply mixed together. | Elevates curriculum from implementation detail to part of the algorithm. | Kimi data curriculum, slides 40--44. |
| `01:06:26--01:08:08` | Verifiers can be hacked through repository history or even formal-tool edge cases. | Shows that “verifiable” does not mean adversarially robust. | Agentic RL section, slides 55--60. |
| `01:09:11--01:10:07` | RLHF and RLVR differ mainly in reward hackability; GRPO is now core knowledge but RL remains noisy and painful. | Supplies the lecture's real closing synthesis. | Final recap, slide 61. |
