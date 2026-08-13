# CS25 Lecture 12 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online official video, `DJ1Yy6Aquug`: `https://www.youtube.com/watch?v=DJ1Yy6Aquug`.
- Official title: *Stanford CS25: V2 I Language and Human Alignment*.
- Classroom date stated in the official description: 2023-01-17.
- Stanford Online upload date: 2023-05-20.
- Public duration: 1:06:21.
- Official CS25 V2 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- Stanford CS25 archive: `https://web.stanford.edu/class/cs25/past/cs25-v2/`.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture12.en.srt`, 1,264 parsed cues.
- Transcript derivatives: `transcript_timed.txt` preserves source intervals; `transcript_clean.txt` supports reading and search.
- Local sanitized public metadata: `metadata.json`.
- The official description and course archive expose no standalone slide PDF. A high-recall scan of the official 1080p recording retained 17 distinct teaching states in `slides-images/`. The main slide presentation ends near 00:30:54; the remaining half hour is an information-dense classroom Q&A and is covered through the teacher-voice ledger rather than repeated screenshots of the same final slide.

## Primary technical sources available by the lecture date

- Christiano et al., *Deep Reinforcement Learning from Human Preferences*: `https://arxiv.org/abs/1706.03741`.
- Leike et al., *Scalable Agent Alignment via Reward Modeling: a Research Direction*: `https://arxiv.org/abs/1811.07871`.
- Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*: `https://arxiv.org/abs/2203.02155`.
- Stiennon et al., *Learning to Summarize with Human Feedback*: `https://arxiv.org/abs/2009.01325`.
- Saunders et al., *Self-critiquing Models for Assisting Human Evaluators*: `https://arxiv.org/abs/2206.05802`.
- Irving, Christiano, and Amodei, *AI Safety via Debate*: `https://arxiv.org/abs/1805.00899`.

## Source-boundary notes

- This is a 2023-01-17 lecture. The note must not retroactively recast it as an account of OpenAI's later Superalignment initiative, nor import later product architectures, policies, or organizational processes as if Jan Leike discussed them in class.
- The speaker explicitly separates two objectives: recruiting capable AI systems to serve human intent (alignment), and writing the rules of the broader human--AI game (governance). He then says the lecture covers only the first objective. Governance appears only to establish that boundary.
- The lecture presents RLHF in a two-step visual simplification: learn a reward model from comparisons, then optimize a policy against it. Leike verbally notes that another step was omitted for simplicity. The note restores the standard SFT--RM--RL decomposition while marking it as clarification from the InstructGPT paper rather than pretending all three boxes appeared on the slide.
- Claims about ChatGPT describe the system available in January 2023. The speaker says exact ChatGPT data and step counts were not public; approximate InstructGPT quantities are recollected during Q&A and should not be rewritten as exact ChatGPT specifications.
- The InstructGPT preference plot supports the narrow claim that a 1.3B aligned model was preferred to a 175B base GPT-3 model on the paper's customer-prompt distribution. It does not show that a smaller model is generally more capable.
- The cost slide is an order-of-magnitude comparison: the speaker estimates human feedback at roughly USD 500,000 and about 20,000 hours, while alignment fine-tuning compute is tiny relative to pretraining. The slide does not prove that preference collection is cheap, representative, or sufficient.
- “Evaluation is easier than generation” is a useful asymmetry, not a universal theorem. The P/NP, sports, consumer product, and peer-review examples are teaching analogies. Hard-to-verify truth, hidden assumptions, persuasion, and evaluator blind spots can erase the advantage.
- The scaling-human-supervision curve is conceptual. It predicts a failure mode when model capability exceeds unaided human evaluation, but does not locate a measured crossing point or prove that deception necessarily emerges.
- The critiques experiment is a proof of concept. The lecture reports roughly 50% more flaws found with critique assistance, then immediately limits the claim: summarization is comparatively easy, the desired effect should be larger, and many generated critiques are garbage or nitpicking.
- `targeted perturbations` create a known good/bad pair by deliberately inserting a subtle flaw. They provide ground truth about which member was perturbed, not proof that the unperturbed answer is globally correct.
- The discriminator--critique gap is a diagnostic proposal: discrimination can reveal that the model encodes task-relevant information that its natural-language critique does not surface. A small measured gap would still depend on task construction and probe quality.
- The Q&A contains open engineering and research judgments: uncertainty calibration is immature; public user feedback should not be ingested naively; labeler pools are not representative; preference drift and prompt compatibility matter; browsing and APIs expand both verification power and attack surface; outer/inner alignment and interpretability remain unresolved.
- The speaker's outer/inner alignment discussion is deliberately tentative. A trusted outer signal might reduce some inner-alignment concerns to distribution shift plus continued trusted evaluation, but Leike repeatedly says the practical outcome is unclear.
- Interpretability is presented as another tool for detecting deception and understanding decisions, possibly neither sufficient nor necessary. Filtering only models with detectable misalignment may select for failures that are harder for the same interpretability tools to see.
