# Lecture 02 Source Audit

## Canonical classroom sources

- Official Stanford recording: `https://www.youtube.com/watch?v=GBd7iuJkW08`
  - Title: `Stanford CS25: Transformers United V6 I From Representation Learning to World Modeling`
  - Classroom date: 2026-04-09
  - Upload date: 2026-04-22
  - Runtime: 1:11:03 (`4263` seconds)
  - Resolution: 1920x1080 at 30 fps
- Live V6 course page: `https://web.stanford.edu/class/cs25/`
- Official Google Drive deck: document `1bF5Yfzf-FG5iNIAgsXn2DwVD3l3ymvZW`
  - Deck title: `Joint Embedding Predictive World Models`
  - Local canonical export: `slides.pdf`
  - Pages: 55
  - SHA-256: `5259e63fab1e586cd232e61120562410c7672bf5eb51633041ffdae678a168d1`
- Official manual YouTube captions: `en-US`
  - Raw cues: 1,371
  - Parsed non-empty segments: 1,371
  - SHA-256: `37aaacb2a76f3383d90dd8b6ea9901cd0dba8a597c9caa328dcf216c21251fbd`

The deck identifies the presenters as Heejeong Nam and Lucas Maes. The classroom introduction resolves the public-name ambiguity explicitly: “Hazel or Heejeong Nam.” It also identifies Lucas Maes as a PhD student at Mila and Université de Montréal. The course-row label “Brown University” is therefore not used as Lucas's affiliation.

## Lecture-snapshot primary papers

- Nam et al., `Causal-JEPA: Learning World Models through Object-Level Latent Interventions`, `https://arxiv.org/abs/2602.11389v1`.
- Maes et al., `LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels`, `https://arxiv.org/abs/2603.19312v1`.
- Locatello et al., `Object-Centric Learning with Slot Attention`, `https://arxiv.org/abs/2006.15055`.
- Bardes et al., `Revisiting Feature Prediction for Learning Visual Representations from Video`, `https://arxiv.org/abs/2404.08471`.
- Assran et al., `V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning`, `https://arxiv.org/abs/2506.09985`.
- Zhou et al., `DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning`, `https://arxiv.org/abs/2411.04983`.

Version control matters here. On 2026-05-28, after the 2026-04-09 lecture, Causal-JEPA v2 changed the title to `Object-Level Latent Masking` and softened parts of the causal interpretation. On 2026-06-03, LeWorldModel also received a post-lecture revision. This note treats the classroom deck, spoken caveats, Causal-JEPA v1, and LeWorldModel v1 as the historical lecture snapshot; later revisions are mentioned only as provenance, not projected backward into the talk.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata, source counts, visual-audit results, and content hashes.
- `lecture02.en.srt` preserves the refreshed manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture02-selection.tsv` records all 55 required/optional slide decisions.
- `lecture02-teacher-voice-ledger.md` maps spoken motivation, caveats, examples, and Q&A into the note.
- `slides-images/` contains all 55 official deck renders, including optional pages for reproducibility.
- `images/frame-00-31-25.jpg` preserves the only independent deck-external teaching visual found in the recording audit.

## Visual audit

- All 55 deck pages were rendered at 200 DPI and reviewed through five contact sheets.
- Required teaching pages: 47.
- Optional pages: 8, limited to the cover, agenda, paper/speaker title pages, collaborator credits, pure section dividers, and closing card.
- The complete recording was sampled every five seconds, producing 853 samples. Transition and perceptual-change clustering retained 198 stable high-recall candidates across 13 contact sheets.
- One independent deck-external teaching visual was found at 00:31:25: a classroom question card asking what happens when the object-centric representation is unfaithful and whether the true causal graph can be recovered. It is required because the spoken answer supplies a central evidence boundary.
- All other candidates were official deck states, progressive reveals already represented by the deck, speaker-only views, conferencing UI, or Q&A camera views.

## Evidence boundaries

- `Causal` in the April lecture means temporally directed predictive dependencies under explicit assumptions; the method does not recover the true causal graph.
- Object masking creates an inductive bias toward interaction-dependent prediction. It does not guarantee correct object discovery, causal identification, or transfer to arbitrary real-world scenes.
- CLEVRER, Push-T, and PHYRE are controlled benchmarks. Their gains support the stated mechanism in those settings, not a universal claim that object tokens always dominate patch tokens.
- LeWorldModel's compact objective and speed results are method- and hardware-specific. They do not show that pretrained encoders, generative world models, or all alternative anti-collapse methods are unnecessary.
- Latent probes, surprise curves, and rollout visualizations indicate encoded physical structure; they do not establish human-like understanding or long-horizon reliability.
- Q&A opinions about VLA systems, physical AI, hallucination, and System 1/System 2 are speaker judgments and forward-looking engineering hypotheses, not settled empirical conclusions.

## Private temporary inputs

- `/tmp/cs25-v6-lecture02.3zZxA0/source.mp4`
- `/tmp/cs25-v6-lecture02.3zZxA0/source.info.json`
- `/tmp/cs25-v6-lecture02.3zZxA0/papers/`
- `/tmp/cs25-v6-lecture02.3zZxA0/video-audit/`
- `/tmp/cs25-v6-lecture02.3zZxA0/contact-sheets/`

The source video, downloaded paper copies, raw `yt-dlp` metadata, and audit scratch files remain outside the repository and must not be committed.
