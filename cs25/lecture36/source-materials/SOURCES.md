# Lecture 36 Source Audit

## Canonical public sources

- Course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Official recording: `https://www.youtube.com/watch?v=nEHNwdrbfGA`
- Official title: `Stanford CS25: V5 I The Advent of AGI, Div Garg`
- Classroom date: April 15, 2025.
- Stanford Online upload date: May 13, 2025.
- Runtime and resolution: 1:01:01, 1920x1080.
- Speaker: Div Garg, AGI, Inc.; previously MultiOn and a Stanford CS PhD student focused on reinforcement learning.
- Neither the course row nor the video description links a standalone slide deck. The official recording is therefore the canonical visual source.

## Captions and transcript

- YouTube exposes a manual `en-US` subtitle track with 1,365 SRT cues.
- Empty or non-text cues were omitted from the readable transcript, leaving 1,296 timed text segments.
- The previous local subtitle file contained 3,161 rolling and repeated cues. It was replaced by the fresh manual track.
- `lecture36.en.srt` preserves the official manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are derived from that manual track.

## Visual recovery method

- The first 2,770 seconds, which contain the complete slide-led lecture before Q\&A, were sampled once per second at 1920x1080.
- An exhaustive no-brightness-gate visual-change scan produced 544 high-recall states, including speaker motion, progressive builds, demo micro-steps, and repeated states.
- Every state was reviewed through contact sheets and OCR-assisted indexing.
- Fifty-eight independent teaching states were retained. The remaining 486 states are the Stanford bumper, speaker-only frames, transitions, repeated states, or superseded builds and micro-steps.
- `lecture36-selection.tsv` records the required/optional decision for all 544 states.
- Required states are copied into `slides-images/` with semantic filenames. The downloaded source video remains a temporary audit artifact and is not committed.

## Primary technical references

- AgentQ paper: `https://arxiv.org/abs/2408.07199`, *Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents*.
- REAL benchmark repository: `https://github.com/agi-inc/real`.
- REAL public evaluation site: `https://www.realevals.xyz/`.
- Model Context Protocol documentation: `https://modelcontextprotocol.io/`.
- Lilian Weng, *LLM Powered Autonomous Agents*: `https://lilianweng.github.io/posts/2023-06-23-agent/`.

## Legacy-note defects

- The old note omitted the canonical video URL and exact classroom/upload dates.
- It contained one figure, five teaching boxes, no teacher-voice markers, no displayed derivations, and no captioned listings.
- It compressed the lecture into roughly 10 KB and omitted almost the entire visual evidence chain: REAL Bench, AgentQ failures, live web-agent demonstrations, MCTS, process supervision, preference learning, the seven-step OpenTable trajectory, the neural-compute analogy, memory/personalization, multi-agent systems, MCP/A2A, and the deployment-risk synthesis.
- It treated the talk as a generic agent overview rather than the speaker's actual argument: human-like agents require evaluation, training, memory, communication, and operational controls to be designed together.
- The replacement note preserves the Q\&A because it contains important caveats on reliability targets, zero-shot distribution shift, domain-specific regression suites, hallucination, small versus large models, manager/worker mixtures, and memory architecture.

## Integrity hashes

- Source video SHA-256: `42aff13f8c24eb5a7693ea602f7584c2149cd5e5c6f50e4d7b7dfb137a04d06a`
- Manual-caption SHA-256: `370df8710dc1eded8a08bf9a84cee9c026f38c79a29b243afa3ebb1677d7a0cc`
- Cover SHA-256: `012fa80d7bc8a20dad02ab73813b4acc2520755ad06fa47c4dc5c3fd2bcaa8a0`
