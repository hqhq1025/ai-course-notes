# Lecture 27 Source Audit

## Canonical classroom sources

- Official video: Stanford Online, `Stanford CS25: V4 I Jason Wei & Hyung Won Chung of OpenAI`.
  - Video ID: `3gb-ZkVRemQ`
  - Classroom date: 2024-04-11
  - Upload date: 2024-05-06
  - Runtime: 1:17:07 (`4627` seconds)
  - Resolution: 1920x1080
  - This combined upload supersedes the unavailable legacy ID `5XkoZDxBSx0`.
- Official V4 archive: `https://web.stanford.edu/class/cs25/past/cs25-v4/`.
- Jason Wei official deck: Google Slides document `1JKpqsbkr5Fg-bj1iElPaC-ToTVpRmRLKZmN89krwl04` with resource key `0-VPgp_Yc4krPPW3Mxv6UjgQ`.
  - Local canonical export: `jason-slides.pdf`
  - Pages: 20
  - SHA-256: `0eddcb8d5bf1a443777ac0a14afc658fa8477d20ef680f79c3bf30e5dbde10f9`
- Hyung Won Chung official deck: Google Slides document `1u05yQQaw4QXLVYGLI6o3YoFHv6eC3YN8GvWD8JMumpE`.
  - Local canonical export: `hyung-slides.pdf`
  - Pages: 67
  - SHA-256: `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`
- Official manual subtitle track: YouTube `en-US`.
  - Parsed cues: 1,551
  - Normalized transcript lines: 729
  - Derivatives: `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md`.

## Speaker boundary

- Jason Wei: approximately 00:00--25:57, followed by Q&A through 00:30:25.
- Hyung Won Chung: approximately 00:30:28--01:17:03, including the joint Q&A.

## Visual policy

- `jason-slide-001.jpg` through `jason-slide-020.jpg` and `hyung-slide-001.jpg` through `hyung-slide-067.jpg` are renders of the two official decks.
- The two source decks are complete; ordinary teaching figures do not require video-frame reconstruction.
- Required teaching pages: 66.
- Intentional omissions: Jason's closing contact card; Hyung's duplicate progressive builds, pure divider, empty comparison scaffold, and the first half of the final chat-attention build.
- The retained pages preserve every independent teaching claim and every final complete progressive state.

## Legacy-note audit

The legacy note used an unavailable video ID, cited almost none of the 87 official slide pages, and invented a different governance/dashboard lecture. Unsupported material to remove includes multi-metric emergence dashboards, attention-entropy diagnostics, prompt registries, governance templates, rollback checklists, and claims that emergence must be validated by several unrelated telemetry signals.

The authoritative lecture instead contains two coherent talks: Jason Wei develops intuitions for next-word prediction, scaling, emergence, and inverse scaling; Hyung Won Chung uses the Bitter Lesson and Transformer history to reason about the lifecycle of inductive bias.

## Historical-claim policy

- Product, architecture, and scaling claims are presented as April 2024 classroom material.
- Speaker conjectures are labeled as conjecture, intuition, anecdotal evidence, or personal judgment rather than upgraded into settled fact.
- The note distinguishes smooth loss scaling from discontinuous benchmark metrics and does not treat a plotted threshold as proof of a new internal mechanism.
