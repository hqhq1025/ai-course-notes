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

Same as youtube-render-pdf — search for official slides before downloading video.

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
whisper audio.wav --model medium --language zh --output_format srt --output_dir .
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

## Rules

- Follow `ai-course-notes/CLAUDE.md` conventions for LaTeX structure, boxes, and figures
- Always compile PDF twice (`xelatex` two passes) to resolve references
- Prefer CC subtitles; fall back to Whisper only when unavailable
- Skip non-teaching content (intros, sponsor segments, 一键三连, 关注投币)
- Use `[H]` float placement for all figures

## Asset

- `assets/notes-template.tex`: default LaTeX template to copy and fill
