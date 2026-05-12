---
name: article-render-pdf
description: "Use when the user provides a URL to a web article, blog post, or X Article and wants LaTeX notes rendered as PDF. Triggers: article/blog URL, '整理这篇文章', '文章笔记'. Handles translation detection (traces back to original)."
---

# Article Render PDF

Use this skill to turn a web article, blog post, or X/Twitter article into a complete, compileable `.tex` note and a rendered PDF.

This skill complements `youtube-render-pdf` and `bilibili-render-pdf` for text-based content sources.

## Supported Sources

| Source | Fetch Method | Notes |
|--------|-------------|-------|
| **X/Twitter Articles** | `api.fxtwitter.com/{user}/status/{id}` | Full article JSON, zero auth |
| **X/Twitter Threads** | Same API, recursive via `replying_to_status` | Chase reply chain |
| **Tech blogs** | `mcp__duckduckgo-search__fetch_content` | Anthropic, OpenAI, etc. |
| **Official docs** | Same as blogs | OpenAI Codex docs, etc. |
| **Medium / Substack** | `WebFetch` or `fetch_content` | May need pagination |

## Goal

Produce a professional Chinese article note from a URL.

The output must:

- be written in Chinese with technical terms preserved in English
- faithfully represent the original author's content and arguments
- be structurally organized with `\section{...}` and `\subsection{...}`
- be a complete `.tex` document from `\documentclass` to `\end{document}`
- be compiled successfully to PDF as part of the final delivery

## Translation Detection (Critical)

Before processing any article, check if it is a translation:

### Detection Signals

- Title contains `【译】`, `[译]`, `翻译`, `Translation`
- Body mentions `原文链接`, `原文作者`, `Original by`, `Source:`
- Author is a known translator (e.g., `@dotey` 宝玉, `@MinLiBuilds` 实践哥MinLi)

### When Translation Is Detected

1. **Extract the original source URL** from the article body or entity links
   - Check `entityMap` in fxtwitter response for LINK entities
   - Search the first few paragraphs for `原文链接` or `Original:`
2. **Fetch the original content** using the appropriate method
3. **Generate notes from the original**, not the translation
4. **On the front page**, credit:
   - Original author and link
   - Translator as reference
   - Note: "本笔记基于英文原文整理"
5. The translation may be used as **terminology reference** for Chinese technical terms

### Finding Original X Articles

When the translation links to another X post:
```
# Extract entity URLs from fxtwitter response
article.content.entityMap → look for type: "LINK" entries
# The URL often points to the original author's X article
```

When the original is a podcast/video:
- Search YouTube: `yt-dlp "ytsearch:SPEAKER PODCAST_NAME YEAR"`
- Get transcript: `youtube-transcript-api` or auto-captions

## Content Acquisition

### X/Twitter Articles

```bash
# Fetch full article JSON (zero auth, no API key needed)
curl -s "https://api.fxtwitter.com/{user}/status/{id}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
tweet = data['tweet']
article = tweet.get('article', {})
blocks = article.get('content', {}).get('blocks', [])
# Extract text with structure
for block in blocks:
    btype = block.get('type', '')
    text = block.get('text', '')
    if 'header' in btype:
        print(f'\n## {text}\n')
    elif btype == 'unordered-list-item':
        print(f'- {text}')
    elif btype == 'ordered-list-item':
        print(f'1. {text}')
    elif btype == 'blockquote':
        print(f'> {text}')
    elif btype == 'code-block':
        print(f\"\`\`\`\n{text}\n\`\`\`\")
    else:
        print(text)
"
```

Key fields in the fxtwitter response:
- `tweet.article.title` — article title
- `tweet.article.content.blocks` — structured content blocks
- `tweet.article.content.entityMap` — links, media, embedded tweets
- `tweet.author.name` — author display name
- `tweet.created_at` — publish date
- `tweet.views` — view count

### Blogs and Documentation

```bash
# Use fetch_content for full text (supports pagination)
mcp__duckduckgo-search__fetch_content(url, max_length=20000)
# If content exceeds 20K chars, use start_index for pagination
mcp__duckduckgo-search__fetch_content(url, start_index=20000, max_length=20000)
```

### Image Extraction

For articles with embedded images:
- X Articles: extract media URLs from `entityMap` entries with type `MEDIA`
- Blogs: extract `<img>` tags from fetched HTML
- Download images to the article directory for LaTeX inclusion

## Writing Rules

1. Write the notes in Chinese unless the user explicitly requests another language.

2. Organize the document with `\section{...}` and `\subsection{...}`.
   Reconstruct the teaching flow when needed; do not blindly mirror original article order.

3. Start from `assets/notes-template.tex`.
   Adapt the metadata block for articles:
   - Change `课程笔记` to `文章笔记` on the front page
   - `\noteauthors{...}` → "基于 [Author Name] 文章内容整理". Never use "XX \& Codex", "XX \& AI", or similar
   - `\notedate{...}` → the article's actual publish date (e.g., "2025-03-15"). Never use `\today`
   - `\videochannel` → article author / source platform
   - `\videopublishdate` → publish date
   - `\videoduration` → estimated reading time (e.g., "阅读时长：约 15 分钟")
   - `\videourl` → article URL (always fill this in — you have the URL the user provided)
   - `\videocoverpath` → leave empty (articles typically have no cover image)
   - `\repourl{https://github.com/hqhq1025/ai-course-notes}` → keep the default; do not change or delete

4. For translated articles, add a note below the metadata box:
   ```latex
   \vspace{0.3cm}
   {\small 本笔记基于英文原文整理。原文作者：XXX，译者参考：YYY。\par}
   ```

5. Use highlight boxes deliberately:
   - `importantbox` for core concepts, key arguments, design principles
   - `knowledgebox` for background context, related work, terminology
   - `warningbox` for common misconceptions, pitfalls, caveats the author raises
   - No images inside boxes
   - No quota per section; add as many as the content justifies

6. When a mathematical formula or data comparison appears:
   - Show formulas in display math using `$$...$$`
   - Use LaTeX tables (`tabular` / `booktabs`) for structured comparisons

7. When code examples appear:
   - Wrap in `lstlisting` with a descriptive `caption`

8. Preserve notable quotes from the original author using `\textit{...}` or the `quote` environment.

9. End every major section with `\subsection{本章小结}`.
   Add `\subsection{拓展阅读}` when there are worthwhile external links.

10. End the document with `\section{总结与延伸}` containing:
    - Structured distillation of core claims
    - Your own synthesis and cross-links between sections
    - Concrete takeaways or open questions

11. Do not emit `[cite]`-style placeholders anywhere in the LaTeX.

## Directory Structure

```
articles/
├── anthropic-harness-design/      # kebab-case topic name
│   ├── content.txt                # fetched article text
│   ├── metadata.json              # author, date, url, type
│   ├── harness-design-notes.tex   # LaTeX source
│   └── harness-design-notes.pdf   # compiled PDF
├── dotey-karpathy-translation/    # translation example
│   ├── content.txt                # translated text (reference)
│   ├── original_content.txt       # original English text
│   ├── original_metadata.json     # original source metadata
│   ├── metadata.json
│   ├── dotey-karpathy-translation-notes.tex
│   └── dotey-karpathy-translation-notes.pdf
└── ...
```

### File Naming Rule

The `.tex` and `.pdf` files MUST be named `<dirname>-notes.tex` and `<dirname>-notes.pdf`, where `<dirname>` is the article directory name. For example, if the directory is `anthropic-harness-design/`, the files must be `anthropic-harness-design-notes.tex` and `anthropic-harness-design-notes.pdf`. Never use bare `notes.tex` or other ad-hoc names.

## Delivery

Deliver all of the following:

- the fetched article content as `content.txt`
- article metadata as `metadata.json`
- for translations: `original_content.txt` and `original_metadata.json`
- the final `.tex` file
- the compiled PDF (two passes of `xelatex -interaction=nonstopmode`)
- evidence that the compiled PDF was visually inspected via rendered pages/contact sheet and corrected if needed

## Compilation

```bash
cd <article-dir>
xelatex -interaction=nonstopmode <file>.tex  # first pass (generate references)
xelatex -interaction=nonstopmode <file>.tex  # second pass (resolve references)
```

After compilation, follow `../video-render-common/writing-and-figures.md` PDF Visual QA: render PDF pages, inspect a contact sheet/full-size suspicious pages, fix layout/rendering problems, and recompile before delivery.

## Rules

- Follow the `ai-course-notes/CLAUDE.md` conventions for LaTeX structure, boxes, and figures
- Always compile PDF twice (`xelatex` two passes) to resolve references
- When source is a translation, trace back to the original and use that as primary source
- Technical terms keep English original even when notes are in Chinese
- Do NOT use TikZ for any visualization — it causes compilation timeouts. Use LaTeX tables or pre-generated images instead

## Asset

- `assets/notes-template.tex`: default LaTeX template to copy and fill
