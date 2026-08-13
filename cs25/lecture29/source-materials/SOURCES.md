# Lecture 29 Source Audit

## Official lecture sources

- Stanford CS25 V4 archive: `https://web.stanford.edu/class/cs25/past/cs25-v4/`
  - Classroom date: April 25, 2024.
  - Official title: `Demystifying Mixtral of Experts`.
  - Speaker: Albert Jiang, Mistral AI / University of Cambridge.
  - The schedule describes Mixtral 8x7B as a Sparse Mixture of Experts model with eight feed-forward experts per layer and top-two routing per token.
- Stanford Online recording: `https://www.youtube.com/watch?v=RcJ1YXHLv5o`
  - Upload date: May 16, 2024.
  - Runtime: 1:04:31.
  - Source resolution: 1920x1080.
  - Video-only SHA-256 used for slide recovery: `e5a9eaa9d22881dae0392115bd56e6dee26a901dc9cf77f31e3da1fadbe57e3b`.
  - The available English source is YouTube's `en-orig` automatic-caption track, not a manual subtitle track.

## Slide provenance and contamination repair

- The official CS25 page does not publish a standalone deck for this lecture. The video description also contains no deck link.
- The legacy `cs25/lecture29/slides.pdf` was not a Mixtral deck. It was byte-identical to Lecture 28's 77-page Nathan Lambert deck at SHA-256 `3c3470dea235227cc43134b87106b8a913716b72bf8324edb8d0a34f79502268` and has been removed.
- The 77 legacy `slides-images/slide-000.jpg` through `slide-076.jpg` were derived from that wrong deck and have also been removed.
- Slide recovery therefore uses the official recording as the canonical visual source.

## Video slide recovery

- A one-second high-recall scan over the full 3,871-second recording produced 3,871 samples, 3,710 slide-like frames, and 58 visual-change candidates.
- Manual contact-sheet review separated 43 distinct main-talk slide states from repeated Q&A screen-sharing states.
- Twenty-six states carry independent teaching content and are required. Seventeen states are intentional omissions limited to the Stanford bumper, pure dividers, the closing card, and superseded progressive builds.
- Candidate detection used the stable slide crop `560:315:28:45` on a temporary 360p transport copy. Final figures were re-extracted from the verified 1920x1080 source using crop `1680:945:84:135`, producing 1680x944 JPEGs.
- The full video and ephemeral Googlevideo URLs remain outside the repository. Only the selected teaching images and sanitized metadata are retained.

## Transcript preparation

- `lecture29.en.srt` contains 2,830 raw automatic-caption cues.
- Rolling caption overlap was removed and adjacent fragments were merged into 276 readable timed segments in `transcript_timed.txt` and `transcript_clean.txt`.
- `transcript_chunks.md` groups the deduplicated transcript into five-minute reading windows.
- Automatic-caption spelling errors such as `mistal`, `mixure`, and `gting` are source noise. The note normalizes technical names to Mistral, Mixtral, mixture, and gating without treating the transcript spelling as evidence.

## Primary technical references

- Jiang et al., `Mixtral of Experts`, `https://arxiv.org/abs/2401.04088`.
- Jiang et al., `Mistral 7B`, `https://arxiv.org/abs/2310.06825`.
- Shazeer et al., `Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer`, `https://arxiv.org/abs/1701.06538`.
- Fedus et al., `Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity`, `https://arxiv.org/abs/2101.03961`.

## Evidence boundary

- Benchmark plots, model comparisons, license statements, and deployment claims are April 2024 lecture-time evidence. They are not current product specifications or a 2026 leaderboard.
- The slide claim that MLPs store knowledge while attention implements algorithms is presented by the speaker as conventional wisdom and a working hypothesis, not a proved decomposition theorem.
- Expert-domain interpretations are explicitly tentative. A routing histogram or ablation does not identify a human-readable concept by itself.
- Active parameter count is not a full cost model. Total resident weights, router computation, token dispatch, all-to-all communication, load imbalance, batch size, and hardware topology all matter.
- Q&A remarks about edge devices, geometric-mean dense equivalents, expert swapping, and very large expert counts are speaker engineering judgments and research directions, not guaranteed recipes.

## Legacy note repair

- The legacy note used only nine figures and referenced the wrong 77-page deck.
- It treated Mixtral as a generic architecture/deployment survey and added unsupported material about fixed production recipes, deployment cases, and future directions that are not present in the lecture.
- The replacement must restore the actual sequence: Mistral 7B baseline, top-two SMoE routing, performance evidence, four myths, load/compression questions, routing interpretability, and the long systems-focused Q&A.
