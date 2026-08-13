# Lecture 23 Source Audit

## Official Lecture Sources

- Stanford CS25 V3 course archive: `https://web.stanford.edu/class/cs25/past/cs25-v3/`
  - Schedule entry: November 14, 2023.
  - Speaker: Angela Fan, Meta AI.
  - Talk title: `No Language Left Behind: Scaling Human-Centered Machine Translation`.
- Stanford Online recording: `https://www.youtube.com/watch?v=ckNMsUuLryM`
  - Upload date: December 15, 2023.
  - Runtime: 52:28.
  - Source resolution: 1920x1080.
  - The repository copy contains an English manual subtitle track normalized into 1,210 timed cues.
  - The projected slide region is stable throughout the lecture; 39 teaching states were recovered from the recording after reviewing 1,049 three-second samples and 133 change candidates.

## Primary Technical Sources

- NLLB team, `No Language Left Behind: Scaling Human-Centered Machine Translation`, `https://arxiv.org/abs/2207.04672`.
- Meta AI publication page, `https://research.facebook.com/publications/no-language-left-behind/`.
- NLLB code and model release in fairseq, `https://github.com/facebookresearch/fairseq/tree/nllb`.
- FLORES benchmark repository, `https://github.com/facebookresearch/flores`.
- Stopes multilingual data-mining pipeline, `https://github.com/facebookresearch/stopes`.
- WikiMatrix paper and data, `https://arxiv.org/abs/1907.05791`.
- LASER multilingual sentence representation repository, `https://github.com/facebookresearch/LASER`.

## Supplementary Verification Material

- Local temporary copy `/tmp/cs25-l23-nllb-paper.pdf`: the 192-page NLLB paper, used to verify terminology, metric definitions, and the scope of model/data claims.
- Local temporary copy `/tmp/cs25-l23-team-seminar.pdf`: a 40-page NLLB team seminar deck. It is used only to check technical labels and is not treated as the classroom deck.
- The classroom visual source of truth is the Stanford recording. Every retained image under `slides-images/` is a cropped frame from that recording and carries a timestamp in `lecture23-selection.tsv`.

## Evidence Boundary

- Classroom claims are bounded to the November 14, 2023 talk and its Q&A. Product language counts on the slides are explicitly treated as lecture-time snapshots; Fan herself said they could already be outdated.
- The headline `44% BLEU` improvement is a relative improvement reported by the NLLB project against the previous state of the art under its evaluation setup. It is not an absolute BLEU score and not a guarantee for every language pair.
- FLORES-200, automatic metrics, human evaluation, and toxicity evaluation answer different questions. The note must not collapse them into one scalar notion of quality.
- The team seminar and NLLB paper may clarify mechanisms shown in class, but they cannot be used to invent classroom anecdotes, operational dashboards, staffing processes, or governance routines absent from the recording.
- Q&A comments about current LLM fine-tuning, foundation models, Common Crawl cadence, and future work are speaker judgments at lecture time, not timeless empirical laws.

## Visual Coverage Policy

- The recording yielded 133 high-recall slide-change candidates. After inspecting contact sheets and nearby states, 39 distinct teaching states were retained.
- Progressive builds are represented by their final complete state unless an earlier state introduces a different mechanism.
- Pure dividers, blank transitions, duplicated title cards, repeated open-source cards, thank-you pages, speaker-only Q&A frames, and ending bumpers are intentionally omitted.
- The right-side conferencing strip was removed from all retained frames; no image was regenerated or redrawn.

## Legacy Note Repair

- The legacy note contained unsupported classroom polls, localization maps, priority formulas, BigQuery/dashboard/versioning processes, internal staff dashboards, agentic deployment, fixed steering-meeting cadence, and governance thresholds.
- Those claims have no support in the Stanford recording, transcript, or official NLLB sources and must not survive the rewrite.
- Real NLLB topics from the old note are also rewritten from source evidence rather than copied, so that teacher voice, metric boundaries, and data/model mechanisms remain auditable.
