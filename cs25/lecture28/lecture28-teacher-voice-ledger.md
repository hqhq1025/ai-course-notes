# Lecture 28 Teacher-Voice Ledger

| Time | Spoken point | Why it matters | Planned placement |
|---|---|---|---|
| 00:00:34--00:01:03 | This is not an Alignment 101 lecture; it retells the post-ChatGPT sequence so people know what still matters. | Sets the lecture as historical synthesis rather than a basic recipe. | Opening |
| 00:01:25--00:05:11 | Modern alignment rests on a much longer language-model history, from Shannon and autoregressive loss through Transformer, scaling, harms, and ChatGPT. | Prevents treating RLHF as an isolated invention. | Historical spine |
| 00:05:11--00:06:56 | RLHF appears necessary but not sufficient for ChatGPT-like behavior; company curves are not directly calibrated across organizations. | Preserves both the claim and its evidence limits. | RLHF motivation |
| 00:08:48--00:09:38 | The abbreviated story omits major academic/infrastructure contributions; base models are the bedrock of the ecosystem. | Separates base capability from alignment layers. | Atlas and definitions |
| 00:09:53--00:11:14 | Alignment is a broad notion of training toward user desires; IFT, SFT, RLHF, DPO, and “aligned” are overlapping but non-identical labels. | Avoids terminology collapse. | Definition table |
| 00:11:30--00:12:30 | The first months after ChatGPT were a land grab with basic unanswered questions about dialogue, red teaming, and user expectations. | Explains why early releases were messy. | Chapter 0 |
| 00:13:42--00:14:53 | IFT teaches chat templates, system prompts, multi-turn behavior, and response styles using autoregressive training on instruction-response pairs. | Gives the mechanism behind “instruction model.” | IFT section |
| 00:14:53--00:16:10 | Self-instruct made instruction data accessible by using a model to generate prompts and answers from a small seed set. | Explains the synthetic-data inflection point. | Self-instruct section |
| 00:16:55--00:18:55 | Vicuna changed prompt distribution through ShareGPT; realistic user prompts were scarce, valuable, and raised privacy/consent questions. | Shows why data source, not just algorithm, drove quality. | ShareGPT section |
| 00:19:00--00:21:05 | Weight-difference releases attempted to respect LLaMA's license but created awkward reconstruction workflows that later releases changed. | Connects open-model practice to licensing constraints. | Weight-diff section |
| 00:23:43--00:24:01 | OpenAssistant was an early successful open project; the field still needs more open human data. | Establishes the lecture's final data thesis early. | OpenAssistant section |
| 00:24:02--00:24:47 | StableVicuna got PPO working early and produced a good chat model, even though few groups could reproduce such pipelines then. | Corrects the idea that early open alignment was only IFT. | StableVicuna section |
| 00:24:56--00:27:09 | QLoRA reduced memory enough to bring more participants into fine-tuning and produced stronger Guanaco models using filtered OpenAssistant data. | Connects accessibility, memory, and ecosystem growth. | QLoRA section |
| 00:27:28--00:28:45 | LoRA/QLoRA made RL experiments exciting but did not reliably produce major RLHF model releases. | Separates lower training loss from validated model quality. | LoRA-with-RL caveat |
| 00:28:55--00:30:54 | Llama 2 safety backlash and “uncensored” fine-tunes exposed a real disagreement about refusal behavior and user control. | Frames safety as a distribution/design choice rather than a slogan. | Safety section |
| 00:32:14--00:32:48 | ChatBotArena, AlpacaEval, MT-Bench, and the Open LLM Leaderboard appeared within weeks because open builders lacked fast human feedback. | Explains why evaluation infrastructure became central. | Evaluation timeline |
| 00:33:14--00:33:56 | ChatBotArena is strategically important but too slow for day-to-day engineering feedback. | Distinguishes release signal from development signal. | Arena section |
| 00:33:56--00:36:16 | AlpacaEval gives fast preference-style feedback but is sensitive to judge choice, baseline choice, length, and what the score means. | Makes LLM-as-a-judge limitations concrete. | AlpacaEval section |
| 00:36:16--00:37:44 | MT-Bench covers multi-turn questions but has few prompts, nontrivial judge bias, and can be optimized against. | Prevents over-reading a popular score. | MT-Bench section |
| 00:37:44--00:39:08 | The Open LLM Leaderboard started as an engineering tool; benchmark contamination and gaming weakened its value for aligned-model development. | Explains metric lifecycle and Goodhart effects. | Leaderboard section |
| 00:39:03--00:39:45 | No evaluation dominates every use: Arena is the long-term public signal, while faster automated evals support iteration. | Supplies the evaluation portfolio conclusion. | Evaluation synthesis |
| 00:40:00--00:41:55 | The RLHF objective combines reward maximization with a KL penalty that keeps the policy near a reference model. | Supplies the intuition behind the formula. | RLHF objective |
| 00:42:00--00:43:44 | Pairwise preference modeling works better than naive scalar-score supervision; reward models learn relative judgments. | Grounds reward-model training. | Preference modeling |
| 00:43:44--00:46:20 | DPO emerges from directly optimizing the preference objective, but simplicity does not make it the same optimizer as PPO. | Prevents conflating DPO with generic RLHF. | DPO derivation |
| 00:46:33--00:49:35 | Zephyr and Tulu 2 showed DPO could make strong releases and scale, while SteerLM and Starling showed PPO/RL methods could still outperform it. | Preserves the mixed empirical record. | Model case studies |
| 00:50:00--01:00:00 | The modern ecosystem has more players and data recipes; the open/closed gap remains task-dependent and evolves quickly. | Frames April 2024 as a snapshot. | Ecosystem section |
| 01:00:00--01:03:48 | Preference data scarcity is a central bottleneck; synthetic data can help but repetitive, narrow distributions reduce generalization. | Provides the forward-looking data agenda. | Current directions |
| 01:04:49--01:05:30 | In a fast field, keep building skills and things that matter; nobody can track everything. | Preserves practical research advice. | Final extension |
| 01:05:44--01:06:20 | The speaker waits for a competitive model release before going deep on a method; LoRA plus preference optimization had not yet shown such a release. | Gives an evidence threshold for method hype. | Method-evidence warning |
| 01:06:24--01:06:57 | Evaluation contamination and judge bias are fundamentally hard to disentangle; human evaluation remains valuable. | Adds Q&A caveat. | Evaluation caveats |
| 01:09:02--01:09:40 | When PPO is set up correctly it can extract slightly more from data than DPO, but the advantage lives in fine margins and costs more iteration. | Gives the speaker's empirical judgment with caveats. | DPO versus PPO |
| 01:10:40--01:11:19 | Alignment changes the model distribution; RL-style objectives act over sequences and differ from token-wise MLE. | Gives a useful conceptual definition. | Final synthesis |
| 01:14:38--01:15:29 | Synthetic data is one route to more tokens, but it is early and models will remain in the loop of training other models. | Extends the data thesis beyond the deck. | Open questions |

## In-note obligations

- Use at least 22 explicit teacher-voice markers.
- Preserve distinctions among historical fact, model-release evidence, benchmark result, speaker experience, and forecast.
- Include evaluation failure modes and the mixed DPO/PPO evidence rather than presenting a single winning recipe.
