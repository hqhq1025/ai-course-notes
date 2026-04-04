# Shared Writing & Figure Rules for Video-to-PDF Skills

## Subtitle Preprocessing

YouTube auto-generated subtitles contain massive redundancy — each caption line repeats the tail of the previous line, causing the same sentence to appear 3-4 times. A raw 5-hour video can produce 80,000+ SRT lines, but only ~8,000 lines of unique content.

**Always clean subtitles before reading.** Use this Python snippet:

```python
import re
with open('subs.en.srt') as f:
    content = f.read()
blocks = re.split(r'\n\n+', content.strip())
texts, prev = [], ''
for block in blocks:
    lines = block.strip().split('\n')
    if len(lines) >= 3:
        timestamp = lines[1].split(' --> ')[0][:8]
        text = ' '.join(lines[2:]).strip()
        if text and text not in prev:
            texts.append(f'[{timestamp}] {text}')
            prev = text
# Second pass: merge lines where text is substring of previous
merged, prev = [], ''
for line in texts:
    text = line.split('] ', 1)[-1]
    if text and text not in prev:
        merged.append(line)
        prev = text
with open('subs_clean.txt', 'w') as f:
    f.write('\n'.join(merged))
```

This typically achieves **10x compression** (86k → 8k lines) with zero information loss. Save the result as `subs_clean.txt` next to the original SRT. For videos over 2 hours, this step is essential to avoid agent timeouts.

## Writing Rules

1. Write the notes in Chinese unless the user explicitly requests another language.

2. Organize the document with `\section{...}` and `\subsection{...}`.
   Reconstruct the teaching flow when needed; do not blindly mirror subtitle order.

3. Start from `assets/notes-template.tex`.
   Fill in the metadata block, including the local cover image path, and replace the body content block with the generated notes.
   Fill every metadata command with a concrete value:
   - `\noteauthors{...}` — use "基于公开课程资料整理" or "基于 [Speaker Name] 授课内容整理". Never use "某某 \& Codex", "某某 \& AI", or similar
   - `\notedate{...}` — use the video's publish date or course semester (e.g., "2025年春季" or "2025-03-15"). Never use `\today`
   - `\videourl{...}` — the full video URL. If truly unavailable, leave empty (`\videourl{}`) — but this should be rare
   - `\repourl{https://github.com/hqhq1025/ai-course-notes}` — keep the default; do not change or delete

4. The front page must include the video's original cover image when available.
   Place it on the first page rather than burying it later in the document.
   Keep it visually distinct from in-body teaching figures.

5. Use figures whenever they materially improve explanation.
   Include as many figures as are necessary for teaching clarity, even if that means many figures across the document.
   Do not optimize for a small figure count; optimize for explanatory coverage and readability.
   Good figures are key formulas, diagrams, tables, plots, visual comparisons, pipeline schedules, architecture views, and stage-by-stage visual progressions.

6. Do not place images inside custom message boxes.

7. When a mathematical formula appears:
   show it in display math using `$$...$$`
   then immediately follow with a flat list that explains every symbol

8. When code examples appear:
   wrap them in `lstlisting`
   include a descriptive `caption`

9. Highlight teaching signals deliberately and repeatedly when the content justifies it:
   use `importantbox` for core concepts the reader must walk away with, including formal definitions, central claims, key mechanism summaries, theorem-like statements, critical algorithm steps, and compact restatements of the main idea after a dense explanation
   use `knowledgebox` for background and side knowledge that improves understanding without being the main thread, including prerequisite reminders, historical lineage, engineering context, design tradeoffs, terminology comparisons, and intuition-building analogies
   use `warningbox` for common misunderstandings and failure points, including notation overload, hidden assumptions, misleading heuristics, easy-to-make implementation mistakes, causal confusions, off-by-one style reasoning errors, and places where the speaker contrasts a wrong intuition with the correct one
   there is no quota of one box per section; add multiple boxes in a section when the material contains multiple distinct teaching signals
   each box should carry a specific pedagogical payload rather than generic emphasis
   prefer placing a box immediately after the paragraph, derivation, or example that motivates it
   routine exposition should stay in normal prose; boxes are for high-signal takeaways, not decoration
   figures must stay outside `importantbox`, `knowledgebox`, and `warningbox`

10. End every major section with `\subsection{本章小结}`.
    Add `\subsection{拓展阅读}` when there are one or two worthwhile external links.

11. End the document with a final top-level section such as `\section{总结与延伸}`.
    That final section must include:
    - the speaker's substantive closing discussion, excluding routine sign-off language
    - your own structured distillation of the core claims, mechanisms, and practical implications
    - your expanded synthesis, including conceptual compression, cross-links between sections, and any careful generalization that stays faithful to the video
    - concrete takeaways, open questions, or next steps when the material supports them

12. Do not emit `[cite]`-style placeholders anywhere in the LaTeX.

## Teaching Content Rules

Build the notes from all of the following when available:

- video title and chapter structure
- the video's original cover image and key metadata
- on-screen diagrams, formulas, tables, plots, and architecture slides
- subtitle explanations, examples, and verbal emphasis
- code snippets shown or described in the talk

Skip content that does not contribute to the actual lesson:

- greetings
- small talk
- sponsorship
- channel logistics
- closing pleasantries

Keep the speaker's closing discussion when it carries actual teaching value, such as synthesis, limitations, future work, tradeoffs, advice, or open questions.

## Figure Handling

Select figures by necessity and teaching value, not by an arbitrary quota or a bias toward keeping the document visually sparse.

### Slides-First Rule

If official slides, lecture deck pages, or course handout pages are available, treat them as the **primary** visual source for the PDF.

- Prefer slide screenshots for definitions, taxonomies, architecture diagrams, benchmark tables, roadmap charts, and any content that was clearly authored as a teaching slide.
- Use video frames as the fallback when slides are unavailable.
- When both exist, mix them deliberately:
  - use slides for static explanatory content
  - use video frames for live demos, product UIs, code walkthroughs, whiteboard builds, and dynamic reveals
- If a lecture has slides and the note contains no slide screenshots, treat that as a quality gap unless there is a clear reason not to use them.
- If standalone slide files are unavailable but the video clearly shows slide pages, it is acceptable to capture slide screenshots from the video and use them as slide evidence.

### 幻灯片与关键帧实践

- 除了确保每个核心概念至少有一张幻灯片证据外，如果讲义本身没有 deck 就额外准备关键视频帧：任何讲述定义、公式、架构、对比、示意图的段落都应该配图，并在图题或正文中标明时间区间（例：`图3：00:26:03--00:27:40`）。
- 对于每个 section，展示幻灯片/画面时要说明其来源：如果是官方 PDF，将其导出成高分辨率 JPEG；如果是视频帧，生成 contact sheet 确保选中最终完整状态、用中性时间命名，随后在 LaTeX 中附 footnote 说明区间。
- 将 slide 与 frame 搭配使用：静态理论用 slides，动态演示、代码、一次性 whiteboard 依赖 video frames。若一个概念既有 slides 又有 frame，可先用 slides 讲基础，再用 frame 展示细节或者演示结果。
- 当假设某一节没有 slides 时，也要尽量挑图：通过 subtitles 定位，抓取多帧候选、再选最完整的一个，同样注明时间。缺失 slides 的情况需在简述中注明“视频帧来源：00:41:00--00:41:20”并且确保这一页已包含图像/表格。

When locating candidate frames, bias strongly toward recall before precision.
It is better to inspect too many nearby candidates first than to miss the one frame where the slide, formula, table, or diagram is finally fully revealed and readable.

### Frame Selection Checklist

Before inserting any video frame, first inspect several nearby candidates from the same subtitle-aligned interval and apply this checklist. If any item fails, reject the frame and keep searching nearby rather than forcing an approximate match.

- Relevance: the frame must directly support the exact concept discussed in the surrounding paragraph or subsection, not just the same broad topic.
- Required content visible: every visual element referenced in the text must already be visible in the frame.
- Fully revealed state: when slides, whiteboards, animations, or dashboards build progressively, use the final fully populated readable state rather than an intermediate state.
- Best nearby candidate: compare multiple nearby frames and prefer the one that is both most complete and most readable.
- Readability: text, formulas, labels, and diagram structure must be legible enough to justify inclusion.

### Frame Naming

- Use neutral timestamp-based names for raw candidate frames. Do not assign semantic names before inspecting the actual frame content.
- Rename a frame semantically only after visually confirming what is fully visible in the image.
- The semantic filename must describe the frame's actual visible content, not a guess based on subtitles, nearby narration, or the intended paragraph topic.
- If the frame is partially revealed, transitional, or ambiguous, keep searching and do not lock in a semantic name yet.

### Frame Locating Strategy

- Use the timestamped subtitle file as the primary locator for key-frame search.
- First identify the subtitle span that corresponds to the concept, example, formula, or visual explanation being discussed.
- Then search within that subtitle-aligned time interval, and slightly around its boundaries when needed, to find the best readable frame.
- Do not jump directly from one guessed timestamp to one extracted frame.
  First generate a dense candidate set across the relevant interval, then inspect and down-select.
- Prefer tools that help you inspect many nearby candidates at once, such as `magick montage`, contact sheets, tiled frame strips, or equivalent workflows.
  Use them to maximize recall and avoid missing the frame where the visual content is fully present.
- When the visual is a progressive PPT reveal, animation build, whiteboard accumulation, or dashboard state change, explicitly search for the final fully populated state.
  Do not stop at the first frame that seems approximately correct.
- If several nearby candidates differ only by progressive reveal state, keep checking until you find the frame with the most complete readable information.
- When in doubt between a sparse early frame and a denser later frame from the same explanation window, prefer the later frame if it is materially more complete and still readable.
- Include every figure that is necessary to explain the content well.
- It is acceptable, and often desirable, to include several figures within one section or subsection when the video builds an idea in stages.
- Omit repetitive or low-information frames.
- Extract frames near chapter boundaries and explanation peaks when chapters exist, but still validate them against subtitle timing.
- Search nearby timestamps when the first extracted frame catches an animation transition.
- Crop, enlarge, or isolate the relevant region when the full frame is too loose.
- When a slide reveals content progressively, capture the final readable state and add intermediate frames only when they teach a genuinely different step.
- For dense visual sections, it is acceptable to over-sample first and discard later.
  Do not optimize candidate count so early that key visual states are never inspected.
- Prefer a sequence of necessary figures over one overloaded figure with unreadable labels.
- Preserve readability of formulas and labels.

## Figure Time Provenance

Whenever the `.tex` or PDF references a specific video frame, or a crop derived from a video frame, record its source time interval on the same page as a bottom footnote.

- The footnote must show the concrete time interval, for example `00:12:31--00:12:46`.
- The interval should come from the subtitle-aligned segment used to locate the figure, not from a vague chapter-level estimate.
- If the figure is a crop, the footnote still refers to the original video time interval of the source frame or subtitle span.
- If several nearby frames in one figure all come from the same subtitle interval, one clear footnote is enough.
- Keep the figure and its time footnote anchored to the same page; prefer layouts such as `[H]`, a non-floating block, or another stable placement when ordinary floats would separate them.

## Visualization

For concepts that remain hard to explain with only screenshots and prose, add accurate visualizations.

**IMPORTANT: Do NOT use TikZ or PGFPlots.** TikZ compilation is extremely slow on this machine and can cause xelatex to hang or time out. This is a hard rule, not a suggestion.

Acceptable routes:

- generate figures ahead of time with Python scripts (matplotlib, PIL) and include them as images
- use LaTeX tables (`tabular` / `booktabs`) for structured comparisons
- use text-based diagrams or formatted lists for simple flows

Use visualizations for:

- process flows (use tables or text-based formatting)
- architecture layouts (use included images or tables)
- scaling-law plots (generate with matplotlib, include as image)
- summary diagrams (use tables)
- comparisons that are clearer as charts than prose (use booktabs tables)

Do not add decorative graphics that do not teach anything.
