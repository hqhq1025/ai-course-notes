# Podcast And Interview Workflow

This workflow is for long-form podcasts, technical interviews, roundtables, and
video-podcast series such as Zhang Xiaojun Podcast, Modern Agent, Agentic RL,
LLM Architect, and similar sources.

The goal is to prevent thin transcript summaries, duplicated bilingual uploads,
unbounded media storage, and unclear source provenance.

## Current Audit Findings

The repository already contains many podcast/interview-style notes, but most
were created before the stricter source-first standard.

Recent audit of `modern-agent/`, `agentic-rl/`, `llm-architect/`, and
`youtube/` found:

- 48 podcast/interview/video-derived notes.
- 37 notes under 8 pages.
- 45 notes with fewer than 3 figures.
- 47 notes with figures but no detectable `读图` explanation.
- 47 notes without a source manifest.
- 47 notes without rendered PDF visual QA.

The current high-quality reference example is:

- `youtube/ttkd0t5qTD4/ttkd0t5qTD4-notes.tex`

That note has local metadata, subtitles, selected frames, a manifest, visual QA,
read-the-figure explanations, and passes quality/coverage checks.

## Content-Type Policy

Podcast material should be classified before generation.

| Kind | Examples | Required treatment |
|---|---|---|
| `interview` | Founder/researcher/operator interviews | Structured teaching note; preserve guest's thesis, mechanisms, examples, and open questions. |
| `review/survey` | Quarterly model reports, paper walkthroughs, topic surveys | Treat like a lecture: source-node coverage, terminology tables, figures/diagrams, and explicit synthesis. |
| `roundtable` | Multi-guest discussion | Track speaker positions and disagreements; avoid flattening into one voice. |
| `audio-essay` | Audiobook/article/podcast narration | Treat like article-render notes; fewer frames, more source text structure. |
| `duplicate` | English reupload, video version of same Chinese episode, pure-view version | Link to canonical item; do not generate duplicate notes unless it contains materially different content. |

## Queue Design

Every large podcast series must have a queue file before batch generation.

Required files:

```text
youtube/<series>/
├── queue.json
└── QUEUE.md
```

Each queue item should contain:

| Field | Meaning |
|---|---|
| `order` | Playlist order, newest first when sourced from YouTube. |
| `episode` | Episode number if present. |
| `id` | Platform video ID. |
| `url` | Canonical source URL. |
| `title` | Original title. |
| `kind` | `interview`, `review/survey`, `roundtable`, `audio-essay`, `duplicate`, or `video-special`. |
| `canonical_id` | The item to use when this upload is a duplicate. |
| `status` | `pending`, `in_progress`, `done`, `blocked`, `duplicate`, or `skipped`. |
| `source_policy` | Whether to retain full video, work video only, audio only, or no media after note generation. |
| `transcript_source` | `manual-subs`, `auto-subs`, `faster-whisper-large-v3`, or another explicit source. |
| `notes_path` | Final TeX path after generation. |
| `qa_path` | Visual QA report path after generation. |

For Zhang Xiaojun Podcast:

- Chinese numbered playlist is the canonical source by default.
- English/video-podcast uploads are tracked as duplicates or supplements.
- Items with title markers such as `含字幕`, `投屏版`, `纯享版`, `英文`, `音频版`, or `串台` need manual canonical review.

## Storage Policy

Do not keep full-resolution videos for every episode in a large batch.

Default per episode:

```text
episode-dir/
├── source.info.json
├── cover.jpg
├── transcript.zh.srt / transcript.zh.txt / transcript.zh.json
├── chapter-transcripts.md
├── frames/
│   ├── candidates-contact.jpg
│   └── frame-*.jpg
├── <episode>-notes.tex
├── <episode>-notes.pdf
├── lecture-manifest.md
└── qa/<pdf-stem>/
```

Allowed transient files:

- `source.mp4` or `work.mp4`: low/medium-resolution work copy for frame extraction.
- `audio.wav`: transcription input.

Default cleanup after successful PDF:

- Remove LaTeX intermediates: `.aux`, `.log`, `.out`, `.toc`, `.xdv`,
  `.fls`, `.fdb_latexmk`.
- Remove or ignore large media unless the user explicitly asked to keep it.
- Never commit cookies, OAuth caches, or full-resolution video files.

The repository `.gitignore` should ignore:

- `youtube_cookies*.txt`
- `cookies*.txt`
- `.yt-dlp-auth/`
- `*.mkv`, `*.mp4`, `*.webm`, `*.mov`

## Acquisition Workflow

1. Read queue item and confirm canonical source.
2. Fetch metadata and thumbnail.
3. Prefer manual subtitles; then platform auto-subs; then GPU Whisper.
4. If no subtitles are available, transcribe with:

```bash
tools/scripts/transcribe_faster_whisper.py <audio-or-video> \
  --out-prefix <episode-dir>/transcript.zh \
  --model large-v3 \
  --device cuda \
  --compute-type float16 \
  --language zh
```

5. Split transcript by chapter timestamps into `chapter-transcripts.md`.
6. Extract candidate frames from each chapter and build a contact sheet.
7. Select only frames with teaching value or source-provenance value.

## GPU Transcription Standard

Use faster-whisper via CTranslate2 CUDA. Do not infer GPU availability from
`torch.cuda.is_available()` alone, because the current environment may have a
CPU-only Torch while CTranslate2 can still use CUDA.

Required checks:

```bash
python3 - <<'PY'
import ctranslate2
print(ctranslate2.get_cuda_device_count())
print(ctranslate2.get_supported_compute_types("cuda"))
PY
```

Expected for this host:

- NVIDIA A100 devices are visible under `/proc/driver/nvidia/gpus`.
- `ctranslate2` reports CUDA devices and supports `float16`.
- `faster-whisper large-v3` can run with `device=cuda`.

If CUDA transcription fails:

1. Record the exact error in `findings.md`.
2. Check CTranslate2 CUDA support before reinstalling Torch.
3. Do not silently fall back to CPU for long videos unless the user approves.

## Writing Standard For Interviews

Interview notes are not course notes, but they still need teaching structure.

Required structure:

- Cover page with source metadata and original cover image.
- Table of contents.
- A short `导读` explaining the interview's technical value.
- Sections organized by ideas, not by raw transcript order when the conversation loops.
- `本章小结` after major sections.
- `总结与延伸` with:
  - the guest's closing view or substantive final discussion,
  - the note author's synthesis,
  - open questions or next directions.

Minimum quality bar for deep interviews over one hour:

- `⭐⭐` target: at least 15 pages, 5 teaching boxes, 3 figures, summaries, compiled PDF, and visual QA.
- `⭐⭐⭐` target: at least 20 pages, 10 teaching boxes, 5+ high-value figures or diagrams, terminology digestion, source manifest, coverage check, and visual QA.
  If the video has no slides, whiteboard, product demo, charts, or meaningful
  visual changes, do not insert repeated speaker frames to reach a larger figure
  quota. Use the cover image plus concept diagrams, tables, timelines, and
  process maps.

Frames in interviews usually do not prove technical claims. Use them sparingly.

For videos with no slides, whiteboard, product demo, charts, or meaningful visual
content, use the cover image on the title page and avoid repeating speaker-head
frames in the body. Replace repeated speaker frames with concept diagrams,
tables, timelines, or process maps that carry the actual teaching content.

## Concept Figure Style

For no-slide interviews, generated concept figures should be clean teaching
diagrams, not text-heavy posters.

Requirements:

- Use `tools/scripts/render_zhangxiaojun_concept_figures.py` or the same style
  rules when generating Zhang Xiaojun concept diagrams.
- Use a font that covers Chinese, Latin text, digits, arrows, and punctuation.
  The current safe default is `AR PL SungtiL GB`:
  `/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf`.
- Do not use `DroidSansFallbackFull.ttf` alone for mixed Chinese/English
  diagrams; it can render Latin text and symbols as tofu boxes.
- Keep diagrams sparse: 3--5 nodes for flow diagrams, 4--6 nodes for radial
  diagrams, and short one-line or two-line labels.
- Put detailed explanation in the surrounding prose and `读图` boxes, not inside
  the image.
- Prefer light backgrounds, strong alignment, consistent card sizes, and at most
  5--6 semantic colors per figure.
- Before finalizing a PDF, inspect at least one rendered contact sheet and the
  most text-heavy generated figure at full size. If any glyph appears as a tofu
  box, regenerate the figure before compiling the final PDF.

Use body video frames only when they add information beyond the cover, such as:

- source-provenance anchors for a genuinely important turning point,
- visible slides, product demos, code, whiteboards, charts, or screen shares,
- a rare scene change that affects interpretation.

If a body figure is just a speaker frame, add a `读图` box explaining its limited
role and do not overclaim visual evidence. Repeating the same speaker frame
across sections is a quality issue.

## Writing Standard For Surveys And Paper Walkthroughs

Survey episodes should be treated like lectures.

Requirements:

- Extract all paper names, model names, benchmark names, and systems terms.
- Add glossary tables for dense term clusters.
- Use generated diagrams or tables when the video lacks slides.
- Include formulas only when the original discussion needs them, and explain every symbol.
- Prefer source papers/reports for formulas and architecture details if the episode is a paper walkthrough.

## Validation Workflow

Every finished podcast/interview note must run:

```bash
python3 tools/scripts/build_lecture_manifest.py <episode-dir>
tools/scripts/check_quality.sh <episode-dir>/<notes>.tex
python3 tools/scripts/check_note_coverage.py <episode-dir>/<notes>.tex --manifest <episode-dir>/lecture-manifest.md
python3 tools/scripts/render_pdf_qa.py <episode-dir>/<notes>.pdf
git diff --check
```

Then inspect `qa/<pdf-stem>/contact.png` and complete the checkboxes in
`qa/<pdf-stem>/qa-report.md`.

## Regeneration Policy For Old Podcast Notes

Do not patch very thin old notes one box at a time. Regenerate when any of these
are true:

- fewer than 8 pages for a 1h+ episode,
- fewer than 3 figures and no good reason,
- no manifest and no visual QA,
- transcript-only summary with no terminology digestion,
- figures exist but have no `读图` explanation,
- title or metadata does not clearly identify the source.

Regeneration order should prioritize:

1. User-requested series and newest episodes.
2. AI/LLM/agent episodes with high technical density.
3. Episodes that already have subtitles or clean transcripts.
4. Old series with systematic thin-note metrics (`agentic-rl`, `llm-architect`, `modern-agent`).
