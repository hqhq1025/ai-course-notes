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
3. Look for BOTH slides AND official lecture notes/readings — lecture notes provide precise formulas, proofs, and context that subtitles often garble
4. If slides are a PDF, extract pages as images (`magick -density 200 slides.pdf slides-images/slide-%03d.jpg`) — prefer these over video frames
5. **Google Slides / Google Docs**: some courses host slides on Google Slides instead of PDF. Strategy:
   - Try appending `/export/pdf` to the Google Slides URL to download as PDF (e.g., `https://docs.google.com/presentation/d/XXXXX/export/pdf`)
   - If export fails, note the URL in the metadata and fall back to video frame extraction
6. When slides are available, use them as the primary figure source and make sure slide screenshots appear in the final PDF; still download video for supplementary frames
7. When official lecture notes are available, use them to verify formula accuracy and fill in details the speaker glossed over verbally
8. If no materials found, proceed with video-only mode

## Source Acquisition

1. Inspect video metadata first (title, chapters, duration, thumbnails, subtitles)
2. Probe formats and choose the best working format for the task.
   - For a one-off user request to download the original video, keep the highest usable original.
   - For large podcast/interview batches, default to a low/medium-resolution work copy for frames/transcription and do not retain full-resolution originals unless requested.
3. Download original cover image (highest-res thumbnail), save locally for front page
4. Prefer manual subtitles over auto-generated; preserve timestamps
5. If YouTube requires authentication, use the repository helper:
   ```bash
   tools/scripts/youtube_auth_check.sh "<URL>"
   ```
   This validates cookies, browser impersonation, bgutil PO-token support, and EJS challenge solving.
6. Keep all required artifacts local (metadata, cover, subtitles/transcript, selected frames, final TeX/PDF). Avoid committing large media.

## Delivery

- the final `.tex` file
- the downloaded cover image
- any extracted or generated figure assets
- the compiled PDF
- evidence that the compiled PDF was visually inspected via rendered pages/contact sheet and corrected if needed

## Rules

- Follow `ai-course-notes/CLAUDE.md` conventions for LaTeX structure, boxes, and figures
- Always compile PDF twice (`xelatex` two passes) to resolve references
- After the final compile, follow the PDF Visual QA workflow in `../video-render-common/writing-and-figures.md`; do not mark the note complete until rendered pages have been inspected and layout/rendering issues fixed
- Prefer manual subtitles; fall back to auto-generated or `youtube-transcript-api`
- For videos with no usable subtitles, use `tools/scripts/transcribe_faster_whisper.py` with CUDA as described in the shared rules
- For fixed-camera interviews with no slides/demos/whiteboard, use the cover only and do not repeat speaker-head frames in the body; generate concept diagrams/tables instead
- Skip non-teaching content (intros, sponsor segments, channel promos)
- Use `[H]` float placement for all figures
- Set `\noteauthors` to "基于公开课程资料整理" or "基于 [Speaker Name] 授课内容整理" — never "XX \& Codex" or similar
- Set `\notedate` to the video's publish date or course semester — never `\today`
- Always fill `\videourl` with the URL the user provided
- Keep `\repourl{https://github.com/hqhq1025/ai-course-notes}` unchanged from the template default
- Do NOT use TikZ for any visualization — it causes compilation timeouts. Use tables or pre-generated images instead

## Asset

- `assets/notes-template.tex`: default LaTeX template to copy and fill
