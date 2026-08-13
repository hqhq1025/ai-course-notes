# Source Manifest: `cs25/lecture30`

## Files

- `cover.jpg`
- `lecture30-notes.tex`
- `lecture30.en.srt`
- `lecture30-selection.tsv`
- `lecture30-blueprint.md`
- `lecture30-coverage.md`
- `lecture30-teacher-voice-ledger.md`
- `metadata.json`
- `transcript_chunks.md`
- `transcript_clean.txt`
- `transcript_timed.txt`

## Supplementary Source Materials

- `source-materials/SOURCES.md`

## Local Visual Assets

- `slides-images/slide-01-motivation.jpg`
- `slides-images/slide-02-saffu-definition.jpg`
- `slides-images/slide-03-general-saffu-design.jpg`
- `slides-images/slide-04-no-lottery-tickets.jpg`
- `slides-images/slide-05-dimensionality-reduction.jpg`
- `slides-images/slide-06-bit-cipher.jpg`
- `slides-images/slide-07-softmax-cooccurrences.jpg`
- `slides-images/slide-08-nonrandom-feedforward-init.jpg`
- `slides-images/slide-09-single-layer-warm-starts.jpg`
- `slides-images/slide-10-image-classification-warm-starts.jpg`
- `slides-images/slide-11-longer-contexts.jpg`
- `slides-images/slide-12-multicontext-design.jpg`
- `slides-images/slide-13-embedding-brittleness.jpg`
- `slides-images/slide-14-caching-vector-comparisons.jpg`
- `slides-images/slide-15-packing-contexts.jpg`
- `slides-images/slide-16-plm-configs.jpg`
- `slides-images/slide-17-saffu-size-table.jpg`
- `slides-images/slide-18-medium-plm-training.jpg`
- `slides-images/slide-19-plm-training-speed.jpg`
- `slides-images/slide-20-small-plm-capabilities.jpg`
- `slides-images/slide-21-application-only-training.jpg`
- `slides-images/slide-22-self-supervised-voice.jpg`
- `slides-images/slide-23-smart-data-collection.jpg`
- `slides-images/slide-24-dialogue-data.jpg`
- `slides-images/slide-25-potato-configs.jpg`
- `slides-images/slide-26-emergent-positive-performance.jpg`
- `slides-images/slide-27-where-next.jpg`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| state-002 | figure | yes | `Stanford recording 00:04:39` | slides-images/slide-01-motivation.jpg |
| state-003 | figure | yes | `Stanford recording 00:06:00` | slides-images/slide-02-saffu-definition.jpg |
| state-004 | figure | yes | `Stanford recording 00:07:38` | slides-images/slide-03-general-saffu-design.jpg |
| state-005 | figure | yes | `Stanford recording 00:11:04` | slides-images/slide-04-no-lottery-tickets.jpg |
| state-006 | figure | yes | `Stanford recording 00:11:21` | slides-images/slide-05-dimensionality-reduction.jpg |
| state-007 | figure | yes | `Stanford recording 00:15:01` | slides-images/slide-06-bit-cipher.jpg |
| state-008 | figure | yes | `Stanford recording 00:19:13` | slides-images/slide-07-softmax-cooccurrences.jpg |
| state-009 | figure | yes | `Stanford recording 00:21:16` | slides-images/slide-08-nonrandom-feedforward-init.jpg |
| state-010 | figure | yes | `Stanford recording 00:24:03` | slides-images/slide-09-single-layer-warm-starts.jpg |
| state-011 | figure | yes | `Stanford recording 00:30:45` | slides-images/slide-10-image-classification-warm-starts.jpg |
| state-012 | figure | yes | `Stanford recording 00:34:22` | slides-images/slide-11-longer-contexts.jpg |
| state-013 | figure | yes | `Stanford recording 00:36:29` | slides-images/slide-12-multicontext-design.jpg |
| state-014 | figure | yes | `Stanford recording 00:37:34` | slides-images/slide-13-embedding-brittleness.jpg |
| state-015 | figure | yes | `Stanford recording 00:39:41` | slides-images/slide-14-caching-vector-comparisons.jpg |
| state-016 | figure | yes | `Stanford recording 00:42:14` | slides-images/slide-15-packing-contexts.jpg |
| state-017 | figure | yes | `Stanford recording 00:46:08` | slides-images/slide-16-plm-configs.jpg |
| state-018 | figure | yes | `Stanford recording 00:48:22` | slides-images/slide-17-saffu-size-table.jpg |
| state-019 | figure | yes | `Stanford recording 00:49:09` | slides-images/slide-18-medium-plm-training.jpg |
| state-020 | figure | yes | `Stanford recording 00:53:21` | slides-images/slide-19-plm-training-speed.jpg |
| state-021 | figure | yes | `Stanford recording 00:54:16` | slides-images/slide-20-small-plm-capabilities.jpg |
| state-022 | figure | yes | `Stanford recording 00:55:21` | slides-images/slide-21-application-only-training.jpg |
| state-023 | figure | yes | `Stanford recording 00:56:53` | slides-images/slide-22-self-supervised-voice.jpg |
| state-024 | figure | yes | `Stanford recording 00:58:34` | slides-images/slide-23-smart-data-collection.jpg |
| state-025 | figure | yes | `Stanford recording 01:02:15` | slides-images/slide-24-dialogue-data.jpg |
| state-026 | figure | yes | `Stanford recording 01:02:38` | slides-images/slide-25-potato-configs.jpg |
| state-027 | figure | yes | `Stanford recording 01:02:48` | slides-images/slide-26-emergent-positive-performance.jpg |
| state-028 | figure | yes | `Stanford recording 01:04:12` | slides-images/slide-27-where-next.jpg |
| state-001 | figure | optional | `Stanford recording 00:00:02` | Stanford Engineering bumper |
| state-029 | figure | optional | `Stanford recording 01:06:51` | closing thanks and contact card |

## Existing Note

- `lecture30-notes.tex`

## Generation Contract

- Review every independent visual state; teaching-bearing states are required by default.
- Every required figure must be placed exactly once or explicitly marked optional with a concrete omission reason.
- Q&A teacher voice is required even though screen sharing repeats main-talk slides.
- The note must distinguish standard Transformer mechanisms from the speaker's SAFFU/PLM proposal.
- Paper and slide claims must be labeled as lecture-time evidence or research hypotheses rather than established general results.
- Every important figure needs nearby reading guidance and evidence limits.
- Final PDF must pass strict coverage, `⭐⭐⭐`, double XeLaTeX, and rendered visual QA.
