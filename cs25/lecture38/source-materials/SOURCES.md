# Lecture 38 Source Audit

## Canonical public sources

- Course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Official recording: `https://www.youtube.com/watch?v=vRQs7qfIDaU`
- Official title: `Stanford CS25: V5 I On the Biology of a Large Language Model, Josh Batson of Anthropic`
- Classroom date: May 13, 2025.
- Stanford Online upload date: June 5, 2025.
- Runtime and resolution: 1:12:32, 1920x1080.
- Speaker: Joshua (Josh) Batson, Anthropic.
- Official supplementary article: `https://transformer-circuits.pub/2025/attribution-graphs/biology.html`
- The course row links the interactive Anthropic article rather than a standalone public slide deck.

## Captions and transcript

- YouTube exposes a manual `en-US` subtitle track with 1,581 SRT cues.
- After removing empty and rolling-caption duplicates, 1,527 timed transcript segments remain.
- `lecture38.en.srt` preserves the fresh manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are derived from that track.
- The discussion from approximately 01:08:27 through 01:12:26 is required teacher voice: it adds the attention limitation, strategy-selection hypothesis, reflection-versus-forward-pass tradeoff, adaptive-compute speculation, and a warning that “hallucination” is not always a token-local category.

## Visual-source audit

- No standalone public slide deck was found on the CS25 page, in the recording description, or on the linked Anthropic article.
- The complete 4,352-second recording was scanned once per second with no brightness gate and a low visual-difference threshold.
- The high-recall scan produced 357 candidates, all reviewed through 23 contact sheets and OCR.
- `lecture38-selection.tsv` marks 62 independent teaching states as required and 295 bumper, speaker-only, transition, repeated, progressive, or live-browser micro-states as optional.
- The official recording is therefore the canonical visual spine. The interactive article is a supplementary source for method details and evidence boundaries, not a substitute slide deck.

## Reproducibility and retention

- The temporary 1080p source recording is stored outside the repository at `/tmp/cs25-lecture38-audit/lecture38-source.mp4` and must not be committed.
- The raw `yt-dlp` metadata dump is stored outside the repository at `/tmp/cs25-lecture38-audit/metadata.full.json` and must not be committed.
- The downloaded course-page and article snapshots are temporary audit inputs under `/tmp/cs25-lecture38-audit/` and must not be committed.
- Public `metadata.json` contains only stable fields and SHA-256 hashes.
- SHA-256 values:
  - source video: `6ee62b369a4029f16be15de7d144cafff7a601e9b215eb7fe8caee6b27ecf04c`
  - manual captions: `a66324d8a3080206400abd14dc125d4c175248b876a86789e4a98447bec27a08`
  - cover: `b1559d900b2309dbd12cceda89cb65717da7984edd288b9b3486a0bc20559f78`
  - supplementary article snapshot: `0a17caa271974ab39d618b7aa86a650984049bd8c4afd943607dd654314a4c73`
  - course-page snapshot: `8575dfbf1f78413de961fb1a0680e10148ab36af67b63aa3c1f28f70508ff9e7`

## Evidence boundary

- The attribution graph is computed through an interpretable replacement model. It is evidence about a reconstructed computation, not a complete dump of every causal mechanism in the base transformer.
- The lecture explicitly freezes and reuses base-model attention rather than explaining it. Claims about strategy selection must therefore distinguish MLP-feature execution from attention-mediated routing.
- Reconstruction error is represented as graph nodes; missing or mis-reconstructed computation can still matter, so graph sparsity is not proof that omitted mechanisms are irrelevant.
- The article emphasizes successful case studies. The speaker notes that the method yields useful results for only a subset of attempted prompts, so the examples cannot be generalized to every prompt, model, or behavior.
- Feature interventions in the original model strengthen causal claims, but they do not make the feature labels uniquely correct or the graph globally complete.
- Results concern Claude 3.5 Haiku and the 2025 circuit-tracing setup. They are not universal claims about all transformers or current Anthropic product behavior in 2026.
