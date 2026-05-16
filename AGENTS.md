# AI Course Notes — Agent Guide

`AGENTS.md` is the source of truth for all coding and writing agents working in this repository. `CLAUDE.md` is kept only as a compatibility entrypoint for Claude Code and should point back here.

## Project

This repository stores Chinese LaTeX/PDF notes for public CS/AI/LLM courses, talks, interviews, and technical articles. Notes are generated from subtitles, official slides, PDFs, video frames, and public reference material.

Each lecture directory usually contains:

```text
<course>/<lectureXX>/
├── lectureXX-notes.tex
├── lectureXX-notes.pdf
├── lectureXX-slides.pdf or lectureXX-slides.py
├── lectureXX.srt or subs.en.srt
├── cover.jpg
├── images/
└── slides-images/
```

Do not commit LaTeX intermediates such as `.aux`, `.log`, `.out`, `.toc`, `.xdv`, `.fls`, or `.fdb_latexmk`.

## Core Commands

Compile one note:

```bash
cd <lecture-dir>
xelatex -interaction=nonstopmode -halt-on-error <lecture>-notes.tex
xelatex -interaction=nonstopmode -halt-on-error <lecture>-notes.tex
```

Render pages for visual PDF QA:

```bash
mkdir -p /tmp/pdf-check
pdftoppm -png -r 120 <lecture>-notes.pdf /tmp/pdf-check/page
montage /tmp/pdf-check/page-*.png -thumbnail 240x340 -tile 4x -geometry +8+8 /tmp/pdf-check/contact.png
```

Use `magick montage ...` instead of `montage ...` on systems that only expose the ImageMagick 7 wrapper.

Check note quality:

```bash
tools/scripts/check_quality.sh cs336-2026
VERBOSE=1 tools/scripts/check_quality.sh cs336-2026/lecture01/lecture01-notes.tex
```

Count canonical source PDFs, excluding generated web copies:

```bash
find . -path './.web-build' -prune -o -name '*-notes.pdf' -print | wc -l
```

Check whitespace before committing:

```bash
git diff --check
```

## Generation Workflow

1. Discover official sources before writing: course site, GitHub lecture repo, slide PDFs, handouts, and video descriptions.
2. Build a source manifest with `tools/scripts/build_lecture_manifest.py <lecture-dir>`.
3. Create a coverage matrix and blueprint before writing TeX. Do not start prose until required source nodes have a planned treatment.
4. Prefer official slides and executable lecture sources over transcript-only summaries.
5. If slides are PDFs, render high-resolution page images into `slides-images/`.
6. If only video is available, use subtitle-aligned frame search and inspect multiple nearby frames before selecting images.
7. Write one lecture at a time, compile to PDF, run quality and coverage checks, perform visual PDF QA, and update tracking files.
8. Preserve unrelated dirty worktree changes; do not revert user edits.

Workflow commands:

```bash
python3 tools/scripts/build_lecture_manifest.py <lecture-dir>
python3 tools/scripts/check_note_coverage.py <lecture-dir>/<lecture>-notes.tex --manifest <lecture-dir>/lecture-manifest.md
python3 tools/scripts/render_pdf_qa.py <lecture-dir>/<lecture>-notes.pdf
```

Podcast/interview batches have extra workflow requirements in
`docs/PODCAST_INTERVIEW_WORKFLOW.md`. Before generating a large podcast series,
build a deduplicated `queue.json`/`QUEUE.md`, classify items, choose canonical
uploads, and set the media retention policy. Use
`tools/scripts/audit_podcast_notes.py` to detect thin legacy notes, missing
manifests, missing visual QA, and duplicate-prone queue entries.

## Writing Standard

Notes are written in Chinese, with technical terms preserved in English where useful. They should be self-contained teaching notes, not thin summaries or translated slide captions.

Required structure:

- Cover page with source metadata.
- Table of contents.
- `\section{}` / `\subsection{}` organized by teaching logic.
- `\subsection{本章小结}` after major sections.
- `\section{总结与延伸}` at the end.
- `\subsection{拓展阅读}` when useful references exist.

Use high-signal boxes:

- `importantbox`: definitions, central claims, key mechanisms, algorithms, formulas.
- `knowledgebox`: background, historical context, intuition, design tradeoffs, terminology.
- `warningbox`: common mistakes, hidden assumptions, misleading metrics, causal confusions.

Boxes must carry concrete teaching content. Do not use boxes as decoration, and do not put images inside boxes.

## Figures Must Be Explained

Important figures cannot be dropped into the note with only a caption. A figure is important if it is a dense table, plot, benchmark, scaling curve, architecture diagram, resource breakdown, multi-panel result, or visual evidence for a claim.

## Prose-Led Teaching Flow Is Required

Slide-complete coverage must not turn a note into a screenshot album. Figures are evidence and anchors; prose is the actual lecture. Before inserting a cluster of figures, write the narrative problem that the cluster answers, define the variables and stakes, and tell the reader what question to carry into the figure.

Every non-summary `\section{}` and `\subsection{}` should begin with a short bridge paragraph before the first figure, table, formula, or code block. That bridge should answer at least two of:

1. What question does this subsection answer?
2. How does it follow from the previous subsection?
3. What source slides or lecture nodes are being synthesized here?
4. What should the reader understand before looking at the figure?

Avoid section patterns like:

```tex
\subsection{Some topic}
\begin{figure}
...
\end{figure}
\begin{knowledgebox}{读图：...}
...
\end{knowledgebox}
```

Prefer:

```tex
\subsection{Some topic}
前一节已经说明了 A 的瓶颈；本节转向 B，因为 ...
读这组图时先看 ...
\begin{figure}
...
\end{figure}
```

For CS336-style notes, a figure-heavy note should target at least 260 prose characters per figure on average, excluding captions and LaTeX boilerplate. Dense slides need local explanations of roughly 220+ prose characters nearby. These are heuristics, not a substitute for judgment, but a note that fails them is usually too thin.

## Teacher Voice Must Be Captured

Slides are not the full lecture. The instructor's spoken explanations often contain the motivation, caveats, practical heuristics, jokes that reveal common mistakes, and "why this matters" links that do not appear on slides. A high-quality note must preserve this teacher voice.

When subtitles, transcript, executable lecture `text(...)` nodes, speaker notes, or video audio are available:

1. Build a teacher-voice digest before writing prose.
2. Extract the instructor's motivations, warnings, informal definitions, examples, caveats, and transitions.
3. Add these to the coverage matrix as `teacher voice` or `spoken explanation` nodes.
4. Weave them into normal paragraphs and boxes. Do not relegate them to quotes or appendices.
5. Mark at least several places with language such as `课堂提示`、`老师强调`、`讲义提醒`、`实践经验` when the note is preserving a spoken insight that is not obvious from the slide alone.

For executable lecture sources, optional `text(...)` nodes are not disposable filler. They are often the closest available proxy for the teacher's spoken narration. The blueprint must sample and synthesize them, especially when they explain why a slide appears, what to compare, or what can go wrong.

For video transcripts, use a "teacher voice ledger" with rows like:

| Time / source node | Spoken point | Why it matters | Where it appears in note |
|---|---|---|---|

If a note has many optional transcript/source text nodes but contains no teacher-voice markers or spoken explanations, treat that as a quality failure even if slide coverage is complete.

## Slide-Complete Coverage

When a lecture has official slides, a slide PDF, an executable slide source, or the video visibly uses slides, the note should include every slide page screenshot, not just a hand-picked subset. Treat the slide deck as the visual spine of the lecture.

Requirements:

1. Render or capture every slide page into `slides-images/` or `images/`.
2. Insert each slide screenshot at the point where its idea is discussed.
3. Give every slide a substantive explanation: what it says, why it appears here, and how it connects to the surrounding concepts.
4. For dense slides, add `读图` boxes or tables that unpack columns, curves, examples, notation, and hidden assumptions.
5. If multiple consecutive slides are incremental builds of the same diagram, include the final fully revealed slide at minimum; include intermediate slides only when they teach distinct steps.
6. If a slide is purely administrative, duplicated, blank, or non-teaching, it may be omitted, but the omission should be intentional.

This rule is stronger than a minimum figure quota. A note with 10 figures can still be incomplete if the source deck has 60 teaching slides and most are absent.

For every important figure, add nearby explanatory text or boxes that answer:

1. What are the axes, rows/columns, legend entries, colors, or baselines?
2. What should the reader compare first?
3. What is the key trend, turning point, anomaly, or visual pattern?
4. What claim does this figure support?
5. What does the figure not prove?
6. How does it connect to later chapters, systems bottlenecks, or engineering decisions?

The explanation should be a mini-lesson, not a label. A good figure treatment usually has:

- a pre-figure setup paragraph that says why the figure appears now;
- the figure and source caption;
- a `读图` block that explains how to read it;
- a follow-up paragraph that connects the visual evidence back to the section argument.

Recommended pattern:

```tex
\begin{knowledgebox}{读图：这张图应该怎么看}
解释坐标轴/列含义/图例/baseline，然后描述关键趋势，最后给出教学结论。
\end{knowledgebox}

\begin{warningbox}{读图时容易犯的错误}
指出不能从图中推出的结论，或容易混淆的因果关系。
\end{warningbox}
```

## PDF Visual QA Is Required

After LaTeX compilation, inspect the rendered PDF before declaring completion. Use rendered page images or a contact sheet, then inspect suspicious pages at full size.

Check for missing/blank/cropped figures, unreadable screenshots, tables or formulas spilling outside margins, code blocks running off page, orphan captions, lonely dense figures without explanations, malformed box titles, mostly empty pages, and ugly raw-URL overflows. Fix the `.tex`, recompile, and repeat visual QA until the PDF is readable.

The visual QA script writes `qa/<pdf-stem>/contact.png` and `qa/<pdf-stem>/qa-report.md`. The report is a checklist for the human/agent review; checkboxes should be completed or issues fixed before the note is called done.

## Dense Terminology Must Be Digested

If a paragraph or bullet list contains several terms, acronyms, model names, system names, or method names, add a concentrated explanation block. Do not leave readers with a name list.

Use a table with columns like:

| 术语 | 解决的问题 | 核心机制与课程关系 |
|---|---|---|

Each term should explain:

- Why it was introduced.
- What mechanism it contributes.
- How it relates to modern LLMs, later course units, or engineering practice.

This is mandatory for dense clusters such as LSTM/seq2seq/attention/Adam/Transformer/MoE/ZeRO/Megatron-LM, GQA/MQA/MLA/CLA, QAT/PTQ/GPTQ/AWQ, and data/tensor/pipeline/sequence/context/expert parallelism.

## First-Use Glossary Rule

When a technical term first appears, define it near the first use unless it is truly common in the surrounding section. This is mandatory for systems/resource-accounting terms because readers cannot infer them from names alone.

Terms that must be explained on first use include:

- `sharding`: 分片；what is split, across which devices, and what is no longer replicated.
- `fused kernel`: multiple GPU operations merged into one kernel to reduce HBM reads/writes and launch overhead.
- `collectives`: multi-GPU communication primitives such as all-reduce, reduce-scatter, all-gather, and broadcast.
- `ZeRO`: optimizer/gradient/parameter state sharding over data-parallel ranks; explain ZeRO-1/2/3 when relevant.
- `optimizer state`: Adam/AdamW first moment `m` and second moment `v`, why they cost memory, and how they update.
- `activation checkpointing`: storing fewer forward activations and recomputing them during backward; distinguish from model checkpointing.
- `DRAM`, `SRAM`, `HBM`: spell out names and explain chip/HBM/cache roles.
- `perplexity`: exponential of cross-entropy; give the “effective choices per token” intuition and its limits.

If several of these appear in one table, add a glossary box immediately before or after the table.

## Background Concepts Need Scaffolding

For foundational concepts that readers may not already know, prefer a compact diagram/table plus formulas over prose alone. Examples include Shannon entropy, n-gram, perplexity, roofline, KV cache, ZeRO, speculative sampling, continuous batching, and PagedAttention.

A good background explanation usually has:

1. A small flow diagram, comparison table, or formula chain.
2. A `knowledgebox` for intuition.
3. An `importantbox` for definition or central formula.
4. A `warningbox` for common misconceptions.

Use simple tables or pre-generated images when possible. Simple TikZ is acceptable for compact concept diagrams, but avoid complex TikZ/PGFPlots because compilation can be slow.

## Math, Code, And Sources

- Display important formulas and explain every symbol immediately after.
- Use `lstlisting` with a caption for code.
- Label figures with source provenance: slide deck page, official source path, or video time interval.
- Prefer slide screenshots over video frames when official slides exist.
- Never invent citations or use placeholder `[cite]` text.

## Quality Bar

For CS336-style long-form course notes, target at least:

- 20+ pages.
- 10+ teaching boxes.
- Slide-complete coverage when slides exist; otherwise 8+ high-value figures.
- Detailed derivations, examples, and engineering interpretation.
- `tools/scripts/check_quality.sh` grade `⭐⭐⭐`.
- `check_note_coverage.py` has no hard errors; any warnings are either fixed or explicitly accepted in the QA report.
- `render_pdf_qa.py` has produced a contact sheet and QA report.

The formal checklist lives in `QUALITY.md`; follow it for review and acceptance.

## Tracking Files

Keep these updated when generating or revising notes:

- `README.md`: total note counts and course table.
- `TRACKING.md`: active course progress and next available materials.
- `NOTE_GENERATION_TODO.md`: current queue status.
- `task_plan.md`, `findings.md`, `progress.md`: persistent working memory for long-running batches.

Use the canonical PDF count command above; raw `find . -name '*-notes.pdf'` can be inflated by `.web-build`.

## Environment Notes

- `xelatex` is the PDF compiler.
- `pdfinfo`, `pdftotext`, and `pdfimages` are available via `poppler-utils`.
- `ffmpeg` is available.
- `faster-whisper` large-v3 has been used for transcription on available GPUs.
- For faster-whisper, check CTranslate2 CUDA support directly; this host may
  have CPU-only Torch while `ctranslate2` can still see A100 GPUs. Use
  `tools/scripts/transcribe_faster_whisper.py` for long podcast transcription.
- `nvidia-smi` may hang on this host; prefer lightweight GPU visibility checks or known cached transcription tooling.
- Bilibili full downloads often require cookies. Never commit cookie files or credentials.

## Git Hygiene

- The worktree may contain unrelated local changes. Do not revert or stage unrelated files unless requested.
- Use `apply_patch` for manual edits.
- Before finalizing, run relevant quality checks and `git diff --check`.
- Before finalizing any PDF note, run visual PDF QA on rendered pages/contact sheet.
- If committing, summarize exactly what was staged and note any remaining unstaged changes.
