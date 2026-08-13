# Lecture 28 Source Audit

## Canonical classroom sources

- Official video: Stanford Online, `Stanford CS25: V4 I Aligning Open Language Models`.
  - Video ID: `AdLgPmcrXwQ`
  - Classroom date: 2024-04-18
  - Upload date: 2024-05-10
  - Runtime: 1:16:21 (`4581` seconds)
  - Resolution: 1920x1080
- Speaker: Nathan Lambert, then a research scientist at the Allen Institute for AI (AI2) and author of Interconnects.
- Official course page: `https://web.stanford.edu/class/cs25/`.
- Official Google Slides deck linked in the video description: document `1quMyI4BAx4rvcDfk8jjv063bmHg4RxZd9mhQloXpMn0`.
  - Local canonical export: `slides.pdf`
  - Title: `[18 April 2024] Aligning open language models`
  - Pages: 77
  - SHA-256: `3c3470dea235227cc43134b87106b8a913716b72bf8324edb8d0a34f79502268`
- Official manual subtitle track: YouTube `en-US`.
  - Parsed cues: 1,693
  - Derivatives: `transcript_timed.txt`, `transcript_clean.txt`, and five-minute `transcript_chunks.md`.
- Official companion model collection: `https://huggingface.co/collections/natolambert/lecture-artifacts-aligning-open-language-models-66197653411171cc9ec8e425`.

## Source correction

The previous local `slides.pdf` was not a thin or stale copy of this lecture. It was byte-for-byte identical to Hyung Won Chung's Lecture 27 deck at SHA-256 `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`. The 67 wrong slide renders were replaced by 77 renders from Nathan Lambert's official deck. The local subtitle file was also replaced by the official manual track rather than the earlier repetitive auto-caption style file.

## Visual policy

- `slides-images/slide-001.jpg` through `slide-077.jpg` are page renders of the official deck.
- Required teaching pages: 67.
- Intentional omissions: history/chapter divider pages 2, 28, 44, 58, and 70; empty or superseded progressive builds 4, 13, 16, and 18; closing contact card 77.
- Timeline and atlas builds are retained when they add a distinct model, method, evaluation family, chapter focus, formula interpretation, or result.

## Legacy-note audit

The legacy note described Hyung Won Chung's architecture-history talk rather than Nathan Lambert's open-alignment lecture. It therefore had the wrong speaker, title, date, URL, slide deck, and teaching arc. It must be replaced completely rather than edited in place.

The authoritative lecture covers the history of open aligned models after ChatGPT; distinctions among instruction fine-tuning, supervised fine-tuning, RLHF, DPO, and alignment; Alpaca, Vicuna, ShareGPT, OpenAssistant, StableVicuna, QLoRA/Guanaco; safety and “uncensored” models; ChatBotArena, AlpacaEval, MT-Bench, and the Open LLM Leaderboard; RLHF objectives and reward modeling; DPO versus PPO; Zephyr, Tulu 2, SteerLM, and Starling; and the 2024 open-alignment ecosystem.

## Historical-claim policy

- Model rankings, release dates, ecosystem judgments, and Llama 3 comments are presented as April 2024 classroom evidence.
- The note distinguishes human preference evaluation, LLM-as-a-judge, and static benchmark evaluation rather than treating them as interchangeable.
- Speaker opinions about PPO, DPO, synthetic data, open versus closed gaps, and future algorithms remain labeled as experience, forecast, or personal judgment.
