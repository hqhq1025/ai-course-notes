---
name: bilibili-render-pdf
description: "Use when the user provides a Bilibili URL (BV number) and wants LaTeX course notes rendered as PDF. Triggers: Bilibili link, BV号, 'B站视频笔记', '整理B站课'. Falls back to Whisper when no CC subtitles."
---

# Bilibili Render PDF

Turn a Bilibili video into a complete, compileable `.tex` note and a rendered PDF.

This skill extends the youtube-render-pdf workflow with Bilibili-specific adaptations.

## Shared Rules

**Read `../video-render-common/writing-and-figures.md` for all writing rules, teaching content rules, figure handling, figure time provenance, and visualization guidelines.** These rules are mandatory.

## Bilibili vs YouTube: Key Differences

| Aspect | Handling |
|--------|----------|
| **Subtitle scarcity** | CC subtitles → Whisper speech-to-text → visual-only mode |
| **Login-gated HD** | 1080P+ requires cookies; use `yt-dlp --cookies-from-browser chrome` |
| **Multi-part videos** | Detect 分P videos, ask user which parts to process |
| **URL formats** | `bilibili.com/video/BVxxxxxxx` and `b23.tv` short links |
| **Danmaku** | Do not use danmaku as teaching content (too noisy) |

## Goal

Same as youtube-render-pdf — produce a professional Chinese lecture note with cover image, key frames, and synthesis section.

## Source Acquisition

### Supplementary Material Discovery

Same as youtube-render-pdf — search for official slides AND official lecture notes before downloading video.

Additional Bilibili-specific notes:
- Many Chinese courses host slides on their own course websites or Gitee/GitHub repos
- Some courses have companion textbooks or reading lists — check the video description
- Google Slides/Docs strategy: try `/export/pdf` URL pattern; fall back to video frames if export fails
- If slides are found, use slide screenshots as the primary figure source and ensure they appear in the final PDF rather than relying on video frames alone
- Official lecture notes are especially valuable for Bilibili courses where subtitles may be auto-generated and formula accuracy is lower

### Metadata Inspection

1. Inspect video metadata first (title, chapters, duration, thumbnail, subtitle availability)
2. Detect multi-part (分P) videos — list all parts and ask user which to process

### Subtitle Acquisition (Three-Level Fallback)

**Priority 1: CC subtitles**
```
yt-dlp --write-subs --sub-langs "zh-Hans,zh-CN,zh,ai-zh" --convert-subs srt \
  --skip-download -o "%(title)s.%(ext)s" "<URL>"
```

**Priority 2: Whisper speech-to-text**
```
yt-dlp -x --audio-format wav -o "audio.%(ext)s" "<URL>"
tools/scripts/transcribe_faster_whisper.py audio.wav \
  --out-prefix transcript.zh \
  --model large-v3 \
  --device cuda \
  --compute-type float16 \
  --language zh
```

**Priority 3: Visual-only mode** — skip subtitles, rely on dense frame sampling.

### Video and Cover Download

1. Download original cover image (highest-res thumbnail)
2. Probe formats, choose highest downloadable resolution (1080P+ needs cookies)
3. Keep all artifacts local

## Delivery

- the final `.tex` file
- the downloaded cover image
- any extracted or generated figure assets
- the compiled PDF
- the Whisper-generated SRT subtitle file, if speech-to-text was used
- evidence that the compiled PDF was visually inspected via rendered pages/contact sheet and corrected if needed

## Rules

- Follow `ai-course-notes/CLAUDE.md` conventions for LaTeX structure, boxes, and figures
- Always compile PDF twice (`xelatex` two passes) to resolve references
- After the final compile, follow the PDF Visual QA workflow in `../video-render-common/writing-and-figures.md`; do not mark the note complete until rendered pages have been inspected and layout/rendering issues fixed
- Prefer CC subtitles; fall back to Whisper only when unavailable
- For long videos, use the faster-whisper CUDA helper from the shared rules; do not silently run multi-hour CPU transcription
- For fixed-camera interviews with no slides/demos/whiteboard, use the cover only and do not repeat speaker-head frames in the body; generate concept diagrams/tables instead
- Skip non-teaching content (intros, sponsor segments, 一键三连, 关注投币)
- Use `[H]` float placement for all figures
- Set `\noteauthors` to "基于公开课程资料整理" or "基于 [Speaker Name] 授课内容整理" — never "XX \& Codex" or similar
- Set `\notedate` to the video's publish date or course semester — never `\today`
- Always fill `\videourl` with the URL the user provided
- Keep `\repourl{https://github.com/hqhq1025/ai-course-notes}` unchanged from the template default
- Do NOT use TikZ for any visualization — it causes compilation timeouts. Use tables or pre-generated images instead

## Asset

- `assets/notes-template.tex`: default LaTeX template to copy and fill
