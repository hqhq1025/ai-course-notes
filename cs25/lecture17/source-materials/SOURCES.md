# Lecture 17 Source Audit

## Official Course Sources

- CS25 V2 archive: `https://web.stanford.edu/class/cs25/past/cs25-v2/`
- Official Stanford Online video: `https://www.youtube.com/watch?v=nz7_wg5iOlA`
- Official playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`
- Classroom date: 2023-02-21.
- Video title: `Stanford CS25: V2 I Biomedical Transformers`.
- Speaker: Vivek Natarajan, Google Health AI.
- Runtime: `1:08:09`.
- Upload date: 2023-05-25.

The course archive identifies three recommended works. No standalone public slide deck was found, so the official 1080p classroom recording is the visual source of record.

## Recommended Primary Works

1. Singhal et al., *Large Language Models Encode Clinical Knowledge*: `https://www.nature.com/articles/s41586-023-06291-2`
   - Used to verify MultiMedQA, Flan-PaLM, instruction prompt tuning, Med-PaLM, the clinician and layperson evaluation axes, and the paper's limitations.
2. *ProtNLM: Model-based Natural Language Protein Annotation*: `https://github.com/google-research/google-research/tree/master/protnlm`
   - Used to verify the sequence-to-text framing, T5-style tasks, UniProt free-text supervision, and protein-function annotation objective.
3. Avsec et al., *Effective Gene Expression Prediction from Sequence by Integrating Long-range Interactions*: `https://www.nature.com/articles/s41592-021-01252-x`
   - Used to verify the Enformer input/output task, long-range regulatory context, gene-expression tracks, and variant-effect interpretation.

## Additional Primary Background

- Choromanski et al., *Rethinking Attention with Performers*: `https://arxiv.org/abs/2009.14794`
  - Supports the FAVOR+ kernel-attention mechanism and linear-time/space attention discussion.
- Baid et al., *DeepConsensus Improves the Accuracy of Sequences with a Gap-Aware Sequence Transformer*: `https://research.google/pubs/deepconsensus-improves-the-accuracy-of-sequences-with-a-gap-aware-sequence-transformer/`
  - Supports the PacBio circular-consensus correction task, gap-aware alignment representation, base-quality prediction, and deployment claims discussed in class.
- Chowdhery et al., *PaLM: Scaling Language Modeling with Pathways*: `https://arxiv.org/abs/2204.02311`
- Chung et al., *Scaling Instruction-Finetuned Language Models*: `https://arxiv.org/abs/2210.11416`

These sources verify mechanisms and paper-level evidence. They do not authorize importing later biomedical models or post-lecture benchmark results into the reconstructed 2023 lecture.

## Local Acquisition And Normalization

- `metadata.json` contains only stable public metadata fields. Raw downloader metadata remains outside the repository.
- `lecture17.en.srt` is the official `en-US` manual subtitle track: 1,581 captions / 7,679 lines after normalization.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` preserve timestamped teacher voice.
- `lecture17.mp4` is a private 1920x1080 source used only for frame recovery. It is ignored and must not be committed or listed as a public source artifact.
- `cover.jpg` is the official YouTube thumbnail.

## Visual Recovery Audit

- The 1920x1080 recording was sampled every two seconds, producing 2,045 candidate frames.
- Stability and visual-difference filtering retained 103 high-recall candidates.
- Manual contact-sheet review retained 84 distinct teaching states.
- Every final image was extracted at the full 1920x1080 resolution; no right-side crop is used.
- Progressive builds are represented by the final informative state unless an intermediate state introduces a distinct mechanism, metric, or comparison.
- Classroom Q&A that revisits an earlier visual is retained in the teacher-voice ledger rather than duplicating the image.

## Historical And Interpretive Boundary

- Classroom claims are bounded to 2023-02-21.
- Med-PaLM is presented as a research model evaluated on MultiMedQA and a small long-form human-evaluation set, not as an autonomous clinician.
- Benchmark accuracy, scientific-consensus ratings, helpfulness, harm, and bias are distinct axes; none alone proves deployment readiness.
- Performer, ProtNLM, DeepConsensus, and Enformer are taught as examples of adapting sequence models to different biomedical representations, not as one unified production stack.
- The final “foundation biomedical AI” thesis is the speaker's forward-looking synthesis, not a claim that such a fully integrated system already existed.
- Later releases, later regulatory outcomes, and post-2023 biomedical foundation models are excluded from reconstructed classroom evidence.
