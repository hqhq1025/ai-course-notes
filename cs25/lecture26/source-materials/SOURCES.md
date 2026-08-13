# Lecture 26 Source Audit

## Canonical classroom sources

- Official video: Stanford Online, `Stanford CS25: V4 I Overview of Transformers`.
  - Video ID: `fKMB5UlVY1E`
  - Classroom date stated in the official description: 2024-04-04
  - Upload date: 2024-04-23
  - Runtime: 1:17:28 (`4648` seconds)
  - Resolution: 1920x1080
- Official course page: `https://web.stanford.edu/class/cs25/`
- Official V4 slide deck linked by the video description: Google Slides document `1oXPs3LXtIVIsVbwTyGjAWj_aWvak9c1uNC4uhkS6glk`.
  - Local canonical export: `slides.pdf`
  - Pages: 114
  - SHA-256: `b16b112aa5b4b35a8b1ca221205e3bce24650a761609dc68b25edf2cb086091c`
  - A fresh official Google Slides PDF export on 2026-08-11 produced the identical SHA-256, so the local PDF is byte-for-byte canonical.
- Official manual subtitle track: YouTube `en-US`.
  - Parsed cues: 1,795
  - Normalized transcript lines: 891
  - Derivatives: `transcript_timed.txt`, `transcript_clean.txt`, and five-minute `transcript_chunks.md`.

## Visual policy

- `slides-images/slide-001.jpg` through `slide-114.jpg` are page renders of the official deck.
- The source deck is complete; no video-frame reconstruction is needed for ordinary teaching slides.
- Required teaching pages: 91.
- Intentional omissions: instructor/admin logistics pages 2--10; pure section dividers 12, 34, 44, 52, 77, 86, 89, 95, and 108; redundant progressive communication builds 101, 102, 105, and 106; closing card 114.
- The retained communication slides preserve the baseline, protocol, verification, conflict, and final correction states, so the omitted builds add no independent teaching claim.

## Legacy-note audit

The legacy note is not a compressed version of the lecture. It cites only nine of 114 slide pages and invents a different engineering/governance lecture. Unsupported material to remove includes:

- prompt-calibration and dataset-drift dashboards;
- clinician override ratios and healthcare review logs;
- compliance dashboards, regulator checklists, incident tickets, and rollback plans;
- prompt registries, evidence patches, alert cadences, and synthetic replay;
- observer-agent monitoring roles and micro-rollback protocols;
- fabricated source mappings such as “Slide 41 compliance dashboard” and “Slide 45 incident flow.”

The authoritative lecture instead covers Transformer history and mechanics, emergence and alignment, cross-domain applications, LLM limitations, reasoning methods, agent demos and autonomy, neural-compute and memory analogies, multi-agent communication, reliability, plan divergence, the LLM-OS analogy, permissions, and sandboxing.

## Historical-claim policy

- Product examples, model comparisons, autonomy claims, and demos are presented as April 2024 classroom material.
- The note must not silently upgrade those claims into current 2026 product facts.
- Demonstrations by MultiOn and statements about GPT-4, Gemini, Waymo, AutoGPT, or agent capabilities must be labeled as speaker examples or period-specific claims unless independently sourced.
