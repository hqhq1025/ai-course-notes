# Lecture 13 Source Index

## Scope

- Course: Stanford CS25, Transformers United V2.
- Classroom date: 2023-01-24.
- Topic: Emergent Abilities and Scaling in LLMs.
- Speaker: Jason Wei, Google Brain at the time of the lecture.
- Historical boundary: the note explains claims and evidence available by the classroom date. Later debates about whether discontinuities are partly metric artifacts are not presented as lecture content.

## Official Course And Video Sources

1. Stanford CS25 V2 archive: <https://web.stanford.edu/class/cs25/past/cs25-v2/>
   - Confirms the date, speaker, title, and three recommended readings.
2. Stanford Online recording: <https://www.youtube.com/watch?v=tVtOevLrt5U>
   - Official upload title: `Stanford CS25: V2 I Emergent Abilities and Scaling in LLMs`.
   - Classroom date in description: 2023-01-24.
   - Upload date: 2023-05-21.
   - Duration: 1:07:48.
3. Official Google Slides deck: <https://docs.google.com/presentation/d/1yzbmYB5E7G8lY2-KzhmArmPYwwl7o7CUST1xRZDUu1Y/edit>
   - Exported locally as `lecture13-slides.pdf`.
   - 37 pages; pages 1--36 are teaching material, page 37 is a pure thanks slide.

## Local Evidence

- `lecture13.en.srt`: 1,439 cues from the official manual English subtitle track.
- `transcript_timed.txt`: timestamp-preserving cleaned transcript.
- `transcript_clean.txt`: continuous transcript for source reading.
- `transcript_chunks.md`: five-minute reading chunks.
- `slides-images/slide-01.jpg` through `slides-images/slide-37.jpg`: page-complete render of the official deck.
- `images/demo-no-cot-math-wrong.jpg`: official video at 00:39:54, no-CoT arithmetic demo ending in the wrong answer 33.
- `images/demo-cot-math-correct.jpg`: official video at 00:40:17, CoT arithmetic demo deriving the correct answer 9.

## Primary Papers Used In The Lecture

1. Kaplan et al., **Scaling Laws for Neural Language Models** (2020): <https://arxiv.org/abs/2001.08361>
   - Source for smooth power-law improvement of language-model loss with compute, data, and parameters.
2. Wei et al., **Emergent Abilities of Large Language Models** (TMLR 2022): <https://arxiv.org/abs/2206.07682>
   - Main framework, task catalog, few-shot emergence plots, data/fine-tuning discussion, and summary.
3. Wei, Tay, and Le, **Inverse Scaling Can Become U-Shaped** (2022): <https://arxiv.org/abs/2211.02011>
   - Source for the claim that an apparently worsening trend can reverse at a larger scale.
4. Wei et al., **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (NeurIPS 2022): <https://arxiv.org/abs/2201.11903>
   - Main CoT mechanism, GSM8K and StrategyQA results, and scale dependence.
5. Srivastava et al., **Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models** (BIG-Bench, 2022): <https://arxiv.org/abs/2206.04615>
   - Source benchmark for diverse task families and emergent few-shot examples.
6. Suzgun et al., **Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them** (2022): <https://arxiv.org/abs/2210.09261>
   - Source for BIG-Bench Hard, task examples, result summary, scaling, and emergence.
7. Shi et al., **Language Models are Multilingual Chain-of-Thought Reasoners** (ICLR 2023): <https://arxiv.org/abs/2210.03057>
   - Source for MGSM and the Bengali/underrepresented-language compositionality result.
8. Wang et al., **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (ICLR 2023): <https://arxiv.org/abs/2203.11171>
   - Source for sampling multiple reasoning paths and majority voting over final answers.
9. Chung et al., **Scaling Instruction-Finetuned Language Models** (2022): <https://arxiv.org/abs/2210.11416>
   - Recommended course reading and evidence that task, model, and CoT-data scaling can move capabilities into smaller or instruction-tuned models.

## Secondary Items Visible In Slides

- P. W. Anderson, **More Is Different** (Science, 1972), used only for the broader scientific intuition that quantitative changes can induce qualitative regime changes.
- Jacob Steinhardt, emergence discussion post (2022), quoted on slide 5 for the compact definition and physical examples.
- OpenAI InstructGPT / RLHF result visible in the emergent prompting and desired-behavior slides; it is used to distinguish prompting-time intervention from fine-tuning-time intervention.

## Source Hierarchy And Exclusions

1. Official deck controls visual order and required slide coverage.
2. Official transcript controls teacher voice, Q&A, caveats, and historical claims.
3. Primary papers supply definitions, formulas, benchmark details, and figure provenance.
4. The old `lecture13-notes.tex` is not a source. It is replaced because it had no visual coverage, no source manifest, and mixed later commentary into the 2023 lecture.
5. Schaeffer et al., **Are Emergent Abilities of Large Language Models a Mirage?** (2023) postdates the classroom lecture and is therefore excluded from the reconstructed lecture narrative. It may be mentioned only as explicitly later reading, not as something Jason Wei said in class.
