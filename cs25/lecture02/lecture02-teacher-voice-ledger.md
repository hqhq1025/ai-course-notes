# CS25 Lecture 02 Teacher-Voice Ledger

| Time / source node | Spoken point | Why it matters | Planned note location | Status |
|---|---|---|---|---|
| 00:05--01:51 / T001 | Early 3-gram/RNN/LSTM samples improve from related words to longer coherence, but still expose obvious failures. | Starts with qualitative outputs rather than architecture worship. | history | complete |
| 01:52--05:11 / T002 | Transformer scale produces increasingly coherent GPT-2/3 samples, motivating the question of human detectability. | Connects scale to evaluation rather than claiming intelligence directly. | GPT-2/3 | complete |
| 05:12--09:08 / T003 | Human detection accuracy depends on model size and sample setting; generated news can approach chance-level discrimination. | Requires careful interpretation of the detection curve. | human evaluation | complete |
| 09:09--11:10 / T004 | Supervised learning is constrained by labeled data while the internet offers much larger unlabeled corpora. | Motivates generative pretraining. | unsupervised | complete |
| 11:11--12:59 / T005 | Autoregressive generation can be understood as analysis by synthesis: model the data distribution to learn useful structure. | Explains why next-token prediction can support transfer. | objective | complete |
| 13:00--14:10 / T006 | A sentiment neuron emerged in character-level language modeling without explicit sentiment labels. | Provides an early representation-learning example and its caveats. | sentiment neuron | complete |
| 14:11--18:14 / T007 | GPT-1 used pretrain/fine-tune; GPT-2 pushed toward zero-shot reading, summarization and translation. | Establishes the progression of task interfaces. | GPT-1/2 | complete |
| 18:15--23:41 / T008 | GPT-3 reframes language modeling as meta-learning from prompt examples; performance scales unevenly by task. | Defines in-context learning through evidence curves. | GPT-3 | complete |
| 23:42--26:23 / T009 | Image GPT asks whether pixels can be treated as a sequence and evaluates both completion and features. | Carries autoregressive pretraining beyond text. | iGPT | complete |
| 26:24--32:19 / T010 | DALL-E demonstrates text-conditioned image generation and zero-shot transformations, but examples remain selective evidence. | Connects multimodal generation to evaluation caution. | DALL-E | complete |
| 32:20--35:59 / T011 | Code is another modality, yet string similarity is insufficient because programs must satisfy specifications. | Motivates HumanEval and unit tests. | code/HumanEval | complete |
| 36:00--38:02 / T012 | pass@k measures the chance that at least one of k sampled programs is correct; training details define the benchmark context. | Introduces sampling-aware evaluation. | pass@k | complete |
| 38:03--41:25 / T013 | Easy, medium and hard problems show that pass@1 can be tiny even when some correct samples exist. | Explains why a single greedy sample understates model capability. | problem examples | complete |
| 41:26--43:16 / T014 | Optimal sampling temperature changes with k; diversity can improve pass@k while hurting pass@1. | Connects decoding to the metric being optimized. | temperature | complete |
| 43:17--46:52 / T015 | Sampling approximates a stronger oracle, and supervised fine-tuning produces Codex-S gains. | Separates model distribution quality from selection strategy. | oracle/Codex-S | complete |
| 46:53--48:18 / T016 | Codex remains limited by prompt brittleness, composition and correctness; sampling is powerful but not deployment assurance. | Preserves the speaker's closing caveats. | limitations/conclusion | complete |
