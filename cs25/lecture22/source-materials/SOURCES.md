# Lecture 22 Source Audit

## Official Lecture Sources

- Stanford CS25 V3 course archive: `https://web.stanford.edu/class/cs25/past/cs25-v3/`
  - Schedule entry: October 31, 2023.
  - Speaker: Nazneen Rajani, Hugging Face.
  - Talk title: `Recipe for Training Helpful Chatbots`.
- Stanford Online recording: `https://www.youtube.com/watch?v=mcep6W8oB1I`
  - Upload date: December 14, 2023.
  - Runtime: 1:08:49.
  - Source resolution: 1920x1080.
  - Manual subtitle track: `en-US`; 1,431 captions parsed by the repository transcript tool.
- Speaker-hosted final classroom deck: `https://www.nazneenrajani.com/transformers_united.pdf`
  - PDF title: `Transformers United`.
  - 71 pages, 16:9, SHA-256 `b8fba49e69b2a531c5dcd86ae8a35356a2f5872f7ee0a66783d9a0a73591cf5b`.
  - The deck was verified against the recording at 00:26:30--00:26:40: the `Recipe 2` and `Zephyr-7B` pages match the projected classroom slides.

## Rejected Deck Variant

- `https://www.nazneenrajani.com/stanford_talk.pdf` is a 67-page variant that omits the Zephyr/distillation and UN advisory pages discussed in the recording. It is retained only as provenance evidence and is not the canonical lecture deck.

## Primary Technical References

- Ouyang et al., `Training language models to follow instructions with human feedback`, `https://arxiv.org/abs/2203.02155`.
- Wang et al., `Self-Instruct`, `https://arxiv.org/abs/2212.10560`.
- Li et al., `CAMEL`, `https://arxiv.org/abs/2303.17760`.
- Zhou et al., `LIMA`, `https://arxiv.org/abs/2305.11206`.
- Ding et al., `UltraChat`, `https://arxiv.org/abs/2305.14233`.
- Touvron et al., `Llama 2`, `https://arxiv.org/abs/2307.09288`.
- Tunstall et al., `Zephyr: Direct Distillation of LM Alignment`, `https://arxiv.org/abs/2310.16944`.
- Wang et al., `Large Language Models are not Fair Evaluators`, `https://arxiv.org/abs/2305.17926`.
- Zheng et al., `Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena`, `https://arxiv.org/abs/2306.05685`.
- Hugging Face H4 evaluation analysis cited by the slides: `https://huggingface.co/blog/llm-leaderboard`.
- Hugging Face red-teaming workflow cited by the slides: `https://huggingface.co/blog/red-teaming`.

## Evidence Boundary

- Classroom facts and leaderboard snapshots are bounded to October 31, 2023.
- The note may explain later-standard terminology such as SFT, reward models, DPO, Elo, and LLM-as-a-judge, but it must not back-propagate post-lecture benchmark results into the speaker's claims.
- Zephyr's reported leaderboard claims are lecture-time results on the displayed evaluation protocols, not proof of universally better helpfulness or safety.
- The Q&A statement comparing roughly 10K SFT examples with roughly 100K RLHF examples is preserved as the speaker's order-of-magnitude classroom judgment, not a general sample-complexity law.

## Slide Coverage Policy

- Required teaching pages: 66 of 71.
- Intentionally omitted: pages 6, 32, 48, and 59 are pure section dividers; page 71 is a closing `Thanks` slide.
- Progressive highlight pages are retained when they teach different evaluation stages, dataset variables, or metric conclusions.

## Legacy Note Repair

- The legacy note had no official video URL, no manifest, no teacher-voice ledger, and no slide coverage.
- It presented fixed hyperparameters and broad data-count claims without tying them to the shown experiments or Q&A boundary.
- The rewrite must separate human-curated SFT results, synthetic Zephyr distillation results, reward-model/red-team benchmark gaps, and GPT-4 evaluator biases rather than collapsing them into a generic alignment recipe.
