# PDF Visual QA: `BV1CAHV6PEPM-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/interviews/crossroads/BV1CAHV6PEPM/BV1CAHV6PEPM-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/interviews/crossroads/BV1CAHV6PEPM/qa/BV1CAHV6PEPM-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/interviews/crossroads/BV1CAHV6PEPM/qa/BV1CAHV6PEPM-notes/contact.png`
- Page count rendered: 49
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/interviews/crossroads/BV1CAHV6PEPM/qa/BV1CAHV6PEPM-notes/pdftoppm.log`
- Near-blank rendered pages: none

## 人工验收结论

2026-10-25 验收通过，可交付当前 49 页 PDF。以下页码均为 PDF 文件页码；封面不显示页码，因此正文印刷页码比文件页码少 1。

- [x] 图片完整显示，图内关键文字、时间标签和多帧分隔可读。
- [x] 六张表及正文符号没有越过页边；本文没有代码块。
- [x] 30 组节目图各有图前说明、同页读图框和图后讲解。
- [x] 30 个图注与 30 条来源脚注逐页对应，未发现重复脚注。
- [x] 已检查标题、图注、知识框续页与留白，接受的留白见下文。
- [x] 知识框标题、内容、长网址正常；未发现乱码、文字重叠、缺图或裁切。

## 查阅范围

完整检查了四张分组联系图：

| 联系图 | PDF 页码 | 检查结果 |
|---|---|---|
| `contact-final-01-12.jpg` | 1 到 12 | 封面、目录、章节开头、图 1 到图 6 及表 1 正常 |
| `contact-final-13-24.jpg` | 13 到 24 | 图 7 到图 13、表 2 与表 3 正常 |
| `contact-final-25-36.jpg` | 25 到 36 | 图 14 到图 22、表 4 正常 |
| `contact-final-37-49.jpg` | 37 到 49 | 图 23 到图 30、表 5 与表 6、总结及参考链接正常 |

最终版本另外放大查阅了第 7、17、20、30、31、32、34、37、40、41、44、49 页。

- 第 20、31、37、40、44 页：此前图与读图跨页的问题已修复；图、图注、来源脚注和完整读图框均在同页。
- 第 30 页：图 18 的读图框标题、背景和正文均正常；先前固定图块内的可分页知识框错位已修复。
- 第 34 页：三帧图的时间标签和文字可读，来源脚注只出现一次。
- 第 17、32、41 页：表格列宽与长单元格正常；其他表格在联系图中检查通过。表 1 在第 9 到第 10 页间正常续表，续页保留表头。
- 第 31 页：论文标题斜体正常，没有残留 Markdown 星号。
- 第 49 页：参考链接换行正常，没有越过页边。

第 7 页下半部保留较多空白，前半部为完整的三步研究方法及过渡段，后续双帧图与读图框整体放在第 8 页。该留白有明确原因，人工接受。封面、目录和文末的留白符合各自用途。没有仅剩标题、孤立图注或缺失正文形成的空白页。

## 排版修复与验证

`generation/build.py` 将每组图与读图说明放在同一个 `minipage` 中。本期 `knowledgebox` 增加可选参数，读图框使用 `breakable=false`；其他长知识框保留分页。图片保持纵横比，最大高度为正文高度的 0.50，图块内部的 `intextsep` 为 3 pt。

图注仅显示来源脚注标记，脚注内容在图注之后生成。这样多行图注测宽时不会重复写入脚注。最终复查未发现图片缩小后关键文字无法辨认的情况。

- 两遍 XeLaTeX 均成功，输出均为 49 页；最新记录为 `generation/compile-1.txt` 和 `generation/compile-2.txt`。
- 两份编译记录均没有 `Overfull`、`Underfull` 或 `Missing character`。
- 最终 PDF 文本交叉检查得到 30 个图注、30 条来源脚注和 30 个读图标题，同页对应检查无异常。
- 最终文本边界检查没有发现横向越界；渲染器未报告近空白页。
- `check_quality.sh` 为 ⭐⭐⭐：49 页、7 个主节、42 个知识框、30 组图。

## 覆盖告警的人工判定

接受 `no-terminology-digestion-detected`。检查器依赖“术语消化”“术语表”“背景概念”等固定关键词；本讲义的标题没有使用这些词。

正文在首次展开讨论 Harness、on-policy distillation、KV Cache、PagedAttention、PostTrainBench 和 PPL 时给出了定义或机制解释。讲义另有六张路径、机制与取舍对照表，以及 PagedAttention、PostTrainBench 与 PPL 等概念框。因此该告警不代表术语解释缺失，无需为匹配标题关键词改写正文。

本报告验收 PDF 的显示与排版。节目事实和引用核验由本次任务的内容复核完成。
