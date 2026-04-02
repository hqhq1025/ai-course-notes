---
name: youtube-render-pdf
description: "Use when the user provides a YouTube URL and wants LaTeX course notes rendered as PDF. Triggers: YouTube link, '这个视频', '整理这节课', 'YouTube 笔记'."
---

# YouTube Render PDF

Turn a YouTube video into a complete, compileable `.tex` note and a rendered PDF.

## Goal

Produce a professional Chinese lecture note from a YouTube URL. The output must:
- use the video's actual teaching content rather than subtitle transcription alone
- place the video's original cover image on the front page
- include all necessary high-value key frames as figures
- end with a final synthesis section
- be a complete `.tex` document compiled successfully to PDF

## Shared Rules

**Read `../video-render-common/writing-and-figures.md` for all writing rules, teaching content rules, figure handling, figure time provenance, and visualization guidelines.** These rules are mandatory.

## Supplementary Material Discovery (Optional but Recommended)

Before downloading the video, search for official slides, lecture notes, or other supplementary materials:

1. Extract course code, speaker name, institution, year from video title/description
2. Search: video description links → course website → GitHub repos → speaker's website → web search
3. If slides are a PDF, extract pages as images (`magick -density 200 slides.pdf slides-images/slide-%03d.jpg`) — prefer these over video frames
4. When slides are available, use them as primary figure source; still download video for supplementary frames
5. If no materials found, proceed with video-only mode

## Source Acquisition

1. Inspect video metadata first (title, chapters, duration, thumbnails, subtitles)
2. Probe formats and choose highest downloadable resolution
3. Download original cover image (highest-res thumbnail), save locally for front page
4. Prefer manual subtitles over auto-generated; preserve timestamps
5. Keep all artifacts local (metadata, cover, subtitles, video, frames)

## Delivery

- the final `.tex` file
- the downloaded cover image
- any extracted or generated figure assets
- the compiled PDF

## Rules

- Follow `ai-course-notes/CLAUDE.md` conventions for LaTeX structure, boxes, and figures
- Always compile PDF twice (`xelatex` two passes) to resolve references
- Prefer manual subtitles; fall back to auto-generated or `youtube-transcript-api`
- Skip non-teaching content (intros, sponsor segments, channel promos)
- Use `[H]` float placement for all figures

## Asset

- `assets/notes-template.tex`: default LaTeX template to copy and fill
