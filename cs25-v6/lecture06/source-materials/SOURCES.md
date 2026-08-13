# CS25 V6 Lecture 06 — Source Manifest

## Canonical course sources

- Stanford CS25 V6 course page: `https://web.stanford.edu/class/cs25/`
- Official Stanford Online recording: `https://www.youtube.com/watch?v=dJtHauhRasc`
- Classroom date: 2026-05-07
- Stanford Online upload date: 2026-05-20
- Speaker: Andrew Lampinen, Anthropic; previously Google DeepMind and Stanford cognitive psychology.
- Recording runtime: 01:12:30. The prepared talk ends at approximately 00:45:30; the rest is substantive Q&A.
- Official deck: Google Drive file `1-YIOa5Yal4RCjAsV-0tnW_NNDGbY1GTo`, downloaded as `lecture06-slides.pdf` with 50 pages.

## Lecture-snapshot primary papers

- Lampinen et al., `On the generalization of language models from in-context learning and finetuning: a controlled study`, arXiv `2505.00661v3`, revised 2025-11-10: `https://arxiv.org/abs/2505.00661v3`.
- Lampinen et al., `Latent learning: episodic memory complements parametric learning by enabling flexible reuse of experiences`, arXiv `2509.16189v3`, revised 2025-12-23: `https://arxiv.org/abs/2509.16189v3`.
- Chaudhry et al., `Improving Latent Generalization Using Test-time Compute`, arXiv `2604.01430v1`, submitted 2026-04-01: `https://arxiv.org/abs/2604.01430v1`.

All three versions above were publicly available before the 2026-05-07 lecture. Later revisions must not be read back into the lecture snapshot.

## Supporting primary papers

- Berglund et al., `The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"`, arXiv `2309.12288v4`: `https://arxiv.org/abs/2309.12288v4`.
- Akyürek et al., `What learning algorithm is in-context learning? Investigations with linear models`, arXiv `2211.15661v3`: `https://arxiv.org/abs/2211.15661v3`.
- Dai et al., `Why Can GPT Learn In-Context? Language Models Implicitly Perform Gradient Descent as Meta-Optimizers`, arXiv `2212.10559v3`: `https://arxiv.org/abs/2212.10559v3`.

The gradient-descent papers support only a qualified analogy in restricted settings. The lecture explicitly asks why similar-looking optimization behavior does not imply identical generalization after information is consolidated into parameters.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata, source hashes, lecture-snapshot paper versions, and visual-audit counts.
- `lecture06.en.srt` preserves the official English manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture06-selection.tsv` freezes all 50 official deck pages: 45 required teaching pages and five optional title/divider/closing pages.
- `lecture06-teacher-voice-ledger.md` maps spoken motivations, caveats, examples, and Q&A into the note.
- `slides-images/` contains all 50 official deck pages rendered as 1440×810 JPEG images.

## Visual audit

- The complete 01:12:30 recording was sampled every five seconds, producing 870 frames and 15 timeline contact sheets.
- All 15 contact sheets were reviewed against the official 50-page deck.
- No deck-external whiteboard, demo, question card, or teaching diagram appears. Camera-only intervals and the Q&A repeatedly return to the official summary slide.
- Five pages are optional: the title card, three pure numbered section dividers, and the closing contact slide. The remaining 45 pages are independent teaching states and are required exactly once.

## Evidence boundaries

- `ICL generalizes better` is not a universal theorem. It is the result of controlled comparisons on reversal, syllogism, codebook, and related latent-structure tasks under the reported model and context conditions.
- A nonzero parametric score does not by itself show systematic latent reasoning. Word co-occurrence and other statistical cues can provide shortcuts.
- In-context augmentation does not create Shannon information from nothing. It makes implications and relations already latent in the corpus more explicit and easier for parametric learning to access.
- The episodic-retrieval experiment uses an oracle with perfect recall and imperfect precision. It demonstrates the value of bringing a relevant experience into context, not a solved general retrieval system.
- RL-based test-time regeneration transfers to several held-out structures but remains weak on true reversal unless it effectively enumerates missing relations. It is not a universal substitute for retrieval.
- The hippocampus/neocortex comparison is a computational analogy, not evidence that brains implement the same algorithms or representations as transformers.
- Q&A estimates such as offline augmentation being `at least 10×` more expensive are speaker judgments, not benchmarked measurements from the presented studies.
