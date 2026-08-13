# Lecture 16 Source Audit

## Official Course Sources

- CS25 V2 archive: `https://web.stanford.edu/class/cs25/past/cs25-v2/`
- Official Stanford Online video: `https://www.youtube.com/watch?v=sTQaJyrI-zg`
- Official playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`
- Classroom date: 2023-02-14.
- Video title: `Stanford CS25: V2 I Common Sense Reasoning`.
- Speaker: Yejin Choi, University of Washington / Allen Institute for AI.
- Runtime: `1:15:05`.
- Upload date: 2023-05-24.

The course archive lists three recommended papers and does not expose a standalone slide deck. The official 1080p recording is therefore the visual source of record.

## Recommended Primary Papers

1. Jung et al., *Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations*: `https://arxiv.org/abs/2205.11822`
   - Used to verify recursive explanation trees, logical consistency constraints, and weighted MaxSAT-style inference.
2. West et al., *Symbolic Knowledge Distillation: from General Language Models to Commonsense Models*: `https://arxiv.org/abs/2110.07178`
   - Used to verify the machine-to-corpus-to-machine pipeline, critic filtering, ATOMIC10x, and the smaller-student / stronger-than-teacher result.
3. Jiang et al., *Can Machines Learn Morality? The Delphi Experiment*: `https://arxiv.org/abs/2110.07574`
   - Used to verify Delphi's descriptive ethical-judgment objective, COMMONSENSE NORM BANK, UNICORN backbone, evaluation protocol, biases, and stated limitations.

## Additional Primary Background

- Bosselut et al., *COMET: Commonsense Transformers for Automatic Knowledge Graph Construction*: `https://aclanthology.org/P19-1470/`
- Hwang et al., *COMET-ATOMIC 2020: On Symbolic and Neural Commonsense Knowledge Graphs*: `https://arxiv.org/abs/2010.05953`

These sources support background claims about ATOMIC / COMET. They do not replace the lecture's own framing or its 2023 evidence boundary.

## Local Acquisition And Normalization

- `metadata.json` contains only stable public metadata fields. The raw `yt-dlp` dump remains under `/tmp` and is not committed.
- `lecture16.en.srt` is the official `en-US` manual subtitle track: 6,652 lines. It replaces the legacy 16,655-line rolling automatic-caption file.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` preserve teacher voice and timestamp provenance.
- `lecture16.mp4` is the private 1080p video-only source used for frame recovery. It is ignored and must not be committed.
- `cover.jpg` is the official YouTube thumbnail.

## Visual Recovery Audit

- The 1920x1080 source video was sampled every two seconds, producing 2,253 frames.
- The stable-frame extractor retained 1,999 bright slide frames and clustered them into 207 high-recall candidates.
- Manual contact-sheet review retained 56 distinct teaching states.
- Final assets were extracted from the full `1920x1080` frame. No right-side crop is applied; the small speaker tile remains part of the official recording.
- Progressive builds are represented by the final state unless an intermediate state introduces a distinct derivation, comparison, or failure example.
- From roughly 52:40 onward, the lecture is Q&A and repeatedly revisits earlier slides. Repeated visuals are omitted, but spoken explanations are retained in the teacher-voice ledger.

## Historical And Interpretive Boundary

- Classroom claims are bounded to 2023-02-14.
- Delphi is presented as an experiment in descriptive commonsense moral judgment, not as a moral authority or a deployment-ready adjudicator.
- Reported comparisons such as COMET versus GPT-3 are kept with the speaker's own non-apple-to-apple caveat.
- The in-progress neuro-symbolic Delphi hybrid is treated as a classroom research direction, not a validated production system.
- Later model releases and post-2023 machine-ethics results are excluded from reconstructed lecture evidence.
