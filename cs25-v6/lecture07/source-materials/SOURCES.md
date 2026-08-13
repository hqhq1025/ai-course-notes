# CS25 V6 Lecture 07 — Source Manifest

## Canonical course sources

- Stanford CS25 V6 course page: `https://web.stanford.edu/class/cs25/`
- Official Stanford Online recording: `https://www.youtube.com/watch?v=jFdH7n6BAl0`
- Classroom date: 2026-05-14
- Stanford Online upload date: 2026-05-27
- Speaker: Vivek Natarajan, Google DeepMind.
- Recording runtime: 01:06:32. The prepared AI co-scientist material ends at approximately 00:59:40; the remaining recording is substantive Q&A.
- The course page exposes no independent slide deck for this lecture. The recording's clean direct-feed slide states are therefore the canonical visual spine.

The official YouTube description announces two topics: AI co-scientist and the AI co-physician project AMIE. The actual 01:06:32 recording completes only the AI co-scientist portion and then moves to Q&A. The lecture note follows the recorded evidence and does not invent an AMIE lecture segment. The final `Make medical expertise universally accessible` card is retained only as an optional transition and source-boundary artifact.

## Lecture-snapshot primary sources

- Gottweis et al., `Towards an AI co-scientist`, arXiv `2502.18864v1`, submitted 2025-02-26: `https://arxiv.org/abs/2502.18864v1`.
- Google Research, `Accelerating scientific breakthroughs with an AI co-scientist`, published 2025-02-19: `https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/`.
- Penadés et al., `AI mirrors experimental science to uncover a novel mechanism of gene transfer crucial to bacterial evolution`, bioRxiv `2025.02.19.639094v1`, posted 2025-02-19: `https://www.biorxiv.org/content/10.1101/2025.02.19.639094v1`.
- Guan et al., `AI-assisted Drug Re-purposing for Human Liver Fibrosis`, bioRxiv `2025.04.29.651320v1`, posted 2025-05-04: `https://www.biorxiv.org/content/10.1101/2025.04.29.651320v1`.
- Toghani et al., `AI-guided discovery of atypical protein assemblies`, bioRxiv `2026.05.03.722499v1`, posted 2026-05-04: `https://www.biorxiv.org/content/10.64898/2026.05.03.722499v1`.

All versions above were publicly available before the 2026-05-14 lecture. The arXiv v1 title is `Towards an AI co-scientist`; the retitled arXiv v2 and Nature publication appeared after the lecture and are excluded from the lecture snapshot.

## Supporting primary literature

- Singh et al., `Increased plasma bradykinin level is associated with cognitive impairment in Alzheimer's patients`, *Neurobiology of Disease* 139 (2020), DOI `10.1016/j.nbd.2020.104833`. This supports only the prior biological plausibility of bradykinin dysregulation; it does not validate the lecture's unpublished ACE--B2R prospective experiment.
- Takahashi et al., `Induction of Pluripotent Stem Cells from Adult Human Fibroblasts by Defined Factors`, *Cell* 131 (2007), DOI `10.1016/j.cell.2007.11.019`. This supplies the Yamanaka-factor background; it is not evidence for the lecture's unpublished rejuvenation result.
- AlphaFold is used as a specialized structural plausibility tool in the arXiv v1 OCT4 demonstration and in the plant-assembly study. Structural prediction does not by itself establish binding, function, safety, or clinical efficacy.

## Lecture-only evidence

Three parts of the recording are explicitly presented as preliminary or unpublished:

1. Early rejuvenation-factor results from the AbuGoot Lab at Harvard.
2. The Alzheimer's ACE--B2R recapitulation and prospective validation case with MGH collaborators.
3. The SCLC--neurodegeneration inverse-comorbidity hypothesis and cold-email expert follow-up.

These are represented as classroom evidence, not peer-reviewed conclusions. The note must preserve the slide language `Unpublished and needs peer review`, separate hypothesis generation from experimental confirmation, and avoid medical recommendations.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata, source hashes, lecture-version boundaries, and visual-audit counts.
- `lecture07.en.srt` preserves the official English manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture07-selection.tsv` freezes 26 recording-derived slide states: 23 required teaching visuals and three optional boundary/title cards.
- `lecture07-teacher-voice-ledger.md` maps spoken motivations, caveats, examples, interruptions, and Q&A into the note.
- `slides-images/` contains 26 clean 1920x1080 frames extracted from the official recording.

## Visual audit

- The full 01:06:32 recording was sampled every two seconds, producing 1,996 frames and 34 complete timeline contact sheets.
- All 34 contact sheets were reviewed. The recording alternates between speaker camera and a clean slide feed; no independent whiteboard derivation or live software demo appears.
- Progressive builds for `Task vs Timescale` and the system-design diagram were inspected separately. Two task-timescale states carry distinct teaching content; the system-design builds collapse to one complete readable state.
- Final independent states: 23 required teaching visuals plus three optional title, press, and unrecorded-AMIE transition cards.

## Evidence boundaries

- A high self-rating, Elo score, or base-LLM comparison is not a scientific truth metric. It is an internal prioritization signal that still needs external review and experiment.
- Recapitulating a hidden result is stronger than ordinary literature retrieval but weaker than prospective discovery unless leakage controls and timing are established.
- Cell-line inhibition, organoid response, predicted structure, and one prospective mechanistic node are different levels of evidence. None alone proves clinical benefit.
- The lecture's AMR, AML, liver-fibrosis, plant-assembly, rejuvenation, Alzheimer's, and inverse-comorbidity examples do not all share the same publication or validation status.
- The system is a scientist-in-the-loop hypothesis engine, not an autonomous replacement for falsification, peer review, reproducibility, safety review, or clinical trials.
- The lecture mentions a 10% unsafe-idea stopping threshold as an implementation detail in Q&A. Treat it as speaker-reported system behavior, not a general safety theorem.
