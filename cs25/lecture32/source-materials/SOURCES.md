# Lecture 32 Source Materials

## Canonical lecture source

- Official CS25 V4 course page: `https://web.stanford.edu/class/cs25/past/cs25-v4/`.
- Official Stanford Online recording: `https://www.youtube.com/watch?v=jm2hyJLFfN8`.
- Speaker page and direct lecture entry: `https://loubnabnl.github.io/`.
- Official Google Slides deck: `https://docs.google.com/presentation/d/1DrO2hz87UFB9oSaQjZwoc3qRExI6mC-8I4hwCV6J7XM/edit?usp=sharing`.
- Official title: `Stanford CS25: V4 I Behind the Scenes of LLM Pre-training: StarCoder Use Case`.
- Speaker: Loubna Ben Allal, Hugging Face.
- Classroom date: 2024-05-23; upload date: 2024-06-07; duration: 3,696 seconds.
- Deck: 71 pages, SHA-256 `ce807c89c3a170e72a58f56220761c13dcdc0684b0de1b549f36f2736b67dbd3`.
- Manual `en-US` subtitles: 1,230 normalized segments, SHA-256 `ed4f1d9079f16f5c68225d94719179b6e41efa3a0399ec6626ccd69309cb9fc8`.

## Slide and transcript preparation

- The speaker-linked deck is the visual source of truth and is committed as `lecture32-slides.pdf`.
- All 71 pages are rendered at 160 DPI into `slides-images/`; 58 teaching pages are required in the note.
- Optional pages are limited to pure dividers, animation build-ups, completion markers, one duplicate FineWeb curve, and the closing card.
- The legacy 269,313-byte rolling-caption SRT with 2,911 timestamp lines has been replaced by the official 97,661-byte manual SRT and normalized to LF.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` provide the teacher-voice audit trail.

## Primary technical references

- Kaplan et al., `Scaling Laws for Neural Language Models`, `https://arxiv.org/abs/2001.08361`.
- Hoffmann et al., `Training Compute-Optimal Large Language Models` (Chinchilla), `https://arxiv.org/abs/2203.15556`.
- Muennighoff et al., `Scaling Data-Constrained Language Models`, `https://arxiv.org/abs/2305.16264`.
- DeepSeek-AI, `DeepSeek LLM`, `https://arxiv.org/abs/2401.02954`.
- Penedo et al., `The RefinedWeb Dataset for Falcon LLM`, `https://arxiv.org/abs/2306.01116`.
- Penedo et al., `FineWeb: decanting the web for the finest text data at scale`, `https://arxiv.org/abs/2406.17557` (post-lecture formal paper for the deck's preliminary results).
- Kocetkov et al., `The Stack`, `https://arxiv.org/abs/2211.15533`.
- Lozhkov et al., `StarCoder 2 and The Stack v2`, `https://arxiv.org/abs/2402.19173`.
- Li et al., `StarCoder: may the source be with you!`, `https://arxiv.org/abs/2305.06161`.
- Allal et al., `SantaCoder`, `https://arxiv.org/abs/2301.03988`.
- Gunasekar et al., `Textbooks Are All You Need`, `https://arxiv.org/abs/2306.11644`.
- Hugging Face, Cosmopedia dataset/blog: `https://huggingface.co/datasets/HuggingFaceTB/cosmopedia`.
- Lee et al., `Deduplicating Training Data Makes Language Models Better`, `https://arxiv.org/abs/2107.06499`.
- Brown et al., `Evaluating Large Language Models Trained on Code` (HumanEval), `https://arxiv.org/abs/2107.03374`.
- Cassano et al., `MultiPL-E`, `https://arxiv.org/abs/2208.08227`.
- Jain et al., `LiveCodeBench`, `https://arxiv.org/abs/2403.07974`.
- Zhou et al., `LIMA: Less Is More for Alignment`, `https://arxiv.org/abs/2305.11206`.
- Hu et al., `LoRA`, `https://arxiv.org/abs/2106.09685`.
- Stanford CRFM, Foundation Model Transparency Index: `https://crfm.stanford.edu/fmti/`.

## Evidence boundary

- This is a May 2024 lecture. Arena positions, model counts, benchmark scores, product capabilities, and transparency rankings are dated snapshots.
- “Open models nearly match GPT-4” refers to selected May 2024 evaluation views and does not imply universal parity across capability, safety, cost, or deployment.
- Scaling-law optima are empirical fits. The lecture explicitly distinguishes training-compute optimum from repeated-inference/lifecycle optimum and notes domain/data dependence.
- FineWeb and StarCoder filter conclusions come from specific ablation model sizes, token budgets, seeds, and benchmarks. No single heuristic is universally good; repository-star filtering is a demonstrated negative result.
- Near-deduplication improved the displayed StarCoder ablations, but gains depend on similarity thresholds, retained diversity, and evaluation protocol.
- PII detection reduces known classes of sensitive strings; it cannot certify that a dataset contains no private data or secrets.
- Opt-out and license metadata improve governance but do not settle all copyright, consent, jurisdiction, or downstream-use questions.
- Benchmark decontamination is approximate. HumanEval and public leaderboards remain vulnerable to semantic overlap and instruction-tuning overfit; time-split evaluation reduces but does not eliminate leakage.
- Membership tests are attribution aids, not definitive proof that a generated snippet was or was not memorized.
- Synthetic data quality depends on generator, seed sources, prompts, verification, diversity, and feedback loops. Quantity alone can amplify bias or collapse.

## Legacy note repair

- The legacy note had no canonical video URL, no official deck attribution, and only reused the thumbnail as a figure.
- It compressed the 71-page lecture into a short summary, omitted most scaling, filtering, governance, formatting, ecosystem, tooling, and contamination evidence, and did not preserve teacher-voice negative results.
- The replacement note follows the full source spine and clearly separates dated claims, mechanisms, ablation evidence, governance choices, and Q&A advice.
