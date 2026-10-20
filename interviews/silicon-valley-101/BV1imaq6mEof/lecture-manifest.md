# Source Manifest: `/home/v-haoqiwang/ai-course-notes/interviews/silicon-valley-101/BV1imaq6mEof`

## Files

- `.gitignore`
- `audio.m4a`
- `cover.jpg`
- `video.mp4`

## Supplementary Source Materials

- `sources/hle.md`
- `sources/source-notes.md`
- `sources/source.info.json`
- `sources/terminal-bench.md`
- `sources/transcript.raw.json`
- `sources/transcript.raw.srt`
- `sources/transcript.raw.txt`

## Local Visual Assets

- `assets/data-supply.pdf`：数据供给的四种能力来源
- `assets/task-feedback.pdf`：任务环境与评分细则如何配合
- `assets/evaluation-distribution.pdf`：从多项评测到真实任务体验
- `assets/procurement-processing.pdf`：先采购原材料，再加工训练环境
- `assets/training-recipe.pdf`：把任务变成适合模型的学习信号
- `assets/expert-quality.pdf`：专家数据需要同时解决三类质量问题

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| voice-01 | section | yes | 04:08–09:22 | 数据公司究竟在交付什么 |
| voice-02 | section | yes | 09:22–20:20 | 把专家判断变成可学习的反馈 |
| voice-03 | section | yes | 20:20–33:35 | 榜单分数怎样连接真实能力 |
| voice-04 | section | yes | 33:35–44:18 | 先拿到原材料，再造训练环境 |
| voice-05 | section | yes | 44:18–48:45 | 一份好评测为何未必能直接训练 |
| voice-06 | section | yes | 48:45–58:01 | 专家数据的质量与激励 |

## Existing Note

- `BV1imaq6mEof-notes.tex`（生成后检查）；细节对应关系见 `sources/source-notes.md`。

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
