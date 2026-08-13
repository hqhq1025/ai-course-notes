# Lecture 19 Source Index

## Canonical Lecture Source

- Official Stanford Online video: `https://www.youtube.com/watch?v=fz8wf9hN20c`
- Official title: *Stanford CS25: V3 I Low-level Embodied Intelligence w/ Foundation Models*
- Classroom date: 2023-10-10
- Upload date: 2023-12-08
- Speaker: Fei Xia, Google DeepMind
- Duration: 01:18:13
- Captions: official human-authored `en-US` track
- Course archive: `https://web.stanford.edu/class/cs25/`

The official video description defines two teaching threads: **Language to Rewards** and **Robotics Transformer 2 (RT-2)**. The note keeps that 2023 classroom boundary and does not import later robotics models as if they appeared in the lecture.

## Primary Research Sources

- PaLM-E project: `https://palm-e.github.io/`
- PaLM-E paper: `https://arxiv.org/abs/2303.03378`
- RT-1 project: `https://robotics-transformer1.github.io/`
- RT-1 paper (*RT-1: Robotics Transformer for Real-World Control at Scale*): `https://arxiv.org/abs/2212.06817`
- RT-2 project: `https://robotics-transformer2.github.io/`
- RT-2 paper (*RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control*): `https://arxiv.org/abs/2307.15818`
- Open X-Embodiment / RT-X project: `https://robotics-transformer-x.github.io/`
- Open X-Embodiment paper: `https://arxiv.org/abs/2310.08864`
- Language to Rewards project: `https://language-to-reward.github.io/`
- Language to Rewards paper: `https://arxiv.org/abs/2306.08647`
- Language Table paper: `https://arxiv.org/abs/2206.04717`

## Local Evidence

- `lecture19.en.srt`: official manual captions, normalized to LF.
- `transcript_timed.txt`: timestamp-preserving transcript used for teacher voice.
- `transcript_chunks.md`: five-minute source digest.
- `lecture19-selection.tsv`: selected visual states with video timestamps.
- `slides-images/`: 55 full-resolution teaching states recovered from the official 1080p recording.
- `metadata.json`: sanitized stable video metadata; raw yt-dlp output stays outside the repository.

## Legacy Note Audit

The legacy note had no video URL, used only one body figure, and compressed the lecture into a short product summary. It mentioned several correct names but did not preserve the lecture's two-part teaching structure, the data/interface bottlenecks, PaLM-E model consolidation, RT-2 action-token mechanism, co-fine-tuning evidence, Language-to-Rewards controller boundary, Q&A tradeoffs, or safety discussion. The rewrite therefore replaces the old body rather than incrementally extending it.
