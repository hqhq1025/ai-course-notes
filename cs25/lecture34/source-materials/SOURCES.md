# Lecture 34 Source Audit

## Canonical classroom sources

- Official video: Stanford Online, `Stanford CS25: V5 I Overview of Transformers`.
  - Video ID: `JKbtWimlzAE`
  - Classroom date: 2025-04-01
  - Upload date: 2025-04-18
  - Runtime: 1:01:28 (`3688` seconds)
  - Resolution: 1920x1080
- Official speakers named in the video description: Steven Feng, Karan Singh, Jenny Duan, and Chelsea Zou.
- Div Garg appears in the course/instructor deck as the course founder on leave, but is not listed as a speaker for this recording.
- Official V5 archive: `https://web.stanford.edu/class/cs25/past/cs25-v5/`.
- Official Google Slides deck: document `16tMMBUjPnqw-PvxF8xzu2m1Epdo1fH7nXWlt3mt2q5w`.
  - Local canonical export: `slides.pdf`
  - Pages: 123
  - SHA-256: `f6dc2b3322059040daf7c16b104fc7bc039b14ef7f6a45dd27555bb40cc7740e`
  - The pre-existing local `slides.pdf` is byte-identical to a fresh official export.
- Official manual subtitle track: YouTube `en-US`.
  - Raw cues: 1,298, including empty terminal cues
  - Parsed non-empty caption segments: 1,264
  - Derivatives: `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md`
  - SHA-256: `0e5888d953a60fbf7814624249058efcaa4dbdc26af71c9db0df69b88f7ea49f`

## Teaching structure and speaker flow

- 00:00--00:06:22: course framing and instructor introductions.
- 00:06:23--00:25:08: Steven Feng on embeddings, attention, Transformer basics, data strategy, child-directed speech, and two-phase pretraining.
- 00:25:09--00:29:13: Chelsea Zou on inference-time reasoning and Chain-of-Thought extensions.
- 00:29:13--00:34:15: feedback and preference-optimization methods, including RLHF, DPO, RLAIF, GRPO, KTO, and variational preference learning.
- 00:34:20--00:39:10: Chelsea Zou on self-improving agents, refinement, reflection, ReAct, and LATS.
- 00:39:11--00:48:02: Karan Singh on ViTs, VLMs, and Transformer foundation models for fMRI.
- 00:48:03--01:01:23: future applications, missing capabilities, model efficiency, interpretability, scaling limits, and continual/lifelong learning.

## Visual policy

- All 123 official pages are rendered as `slides-images/slide-001.jpg` through `slide-123.jpg`.
- Required teaching pages: 100.
- Optional pages: 23, limited to instructor biographies/course logistics, pure section dividers, two QR/contact slides, and the closing card.
- The deck contains no large progressive-build sequence that requires deduplicating final states beyond those administrative/divider decisions.
- The official deck is the visual spine; ordinary teaching figures use slide renders rather than video frames.

## Legacy-note audit

The legacy note is an approximately 8 KB, 270-line summary with zero slide figures, zero teacher-voice markers, no canonical video URL, approximate duration only, and no source manifest or visual QA. It names `Stephen Feng` and `Curran`, while the official description names Steven Feng, Karan Singh, Jenny Duan, and Chelsea Zou.

The old prose also collapses the lecture into generic Transformer/pretraining/post-training/application headings and omits the deck's two concrete data studies, the full Chain-of-Thought taxonomy, six preference-optimization methods, five self-improvement mechanisms, the fMRI foundation-model case study, and the detailed continual-learning survey. Those source-specific teaching chains must be restored.

## Historical-claim policy

- Model names, research trends, and capability claims are presented as an April 2025 classroom snapshot.
- Instructor opinions about scaling saturation, AGI gaps, brain-inspired learning, and “true” continual learning remain labeled as opinions or open questions.
- Study results from TinyDialogues and two-phase pretraining are separated from broader claims about human learning or universal data recipes.
- Post-training methods are defined by their optimization signal and infrastructure requirements rather than presented as an undifferentiated acronym list.
