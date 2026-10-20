# Source Manifest: `BV1sAT16WEYg`

## Files

- `.gitignore`
- `cover.jpg`

## Supplementary Source Materials

- `sources/autoresearch.md`
- `sources/frame-1800.jpg`
- `sources/frame-4000.jpg`
- `sources/frame-6000.jpg`
- `sources/frame-contact.jpg`
- `sources/media.mp4`
- `sources/opro.md`
- `sources/source-guide.md`
- `sources/source.info.json`
- `sources/transcript-reading.md`
- `sources/transcript.raw.json`
- `sources/transcript.raw.srt`
- `sources/transcript.raw.txt`
- `sources/video.mp4`

## Local Visual Assets

- `assets/` 中 7 幅机制图，路径与解释见 `assets/figures.json`。

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| voice-01 | spoken explanation | yes | 03:29–10:58；13:21–14:57 | 从会解题到会改进自己的模型 |
| voice-02 | spoken explanation | yes | 10:58–13:21；29:48–34:47 | 长程任务需要怎样的上下文和系统 |
| voice-03 | spoken explanation | yes | 14:57–20:02；28:48–29:48 | 验证怎样阻止错误成为下一轮教材 |
| voice-04 | spoken explanation | yes | 20:02–28:48；01:07:01–01:08:51 | 把自我诊断接到训练与脚手架 |
| voice-05 | spoken explanation | yes | 34:47–40:26；52:02–57:53 | 科学发现要同时解决新颖性与可验证性 |
| voice-06 | spoken explanation | yes | 40:26–52:02；01:05:04–01:06:47 | 科研品味怎样变成训练信号 |
| voice-07 | spoken explanation | yes | 57:53–01:05:04；01:06:47–01:11:07 | 半年预测之后仍需回答的问题 |

## Existing Note

- `BV1sAT16WEYg-notes.tex`，依据 `generation/blueprint.json` 的 7 章安排。

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
