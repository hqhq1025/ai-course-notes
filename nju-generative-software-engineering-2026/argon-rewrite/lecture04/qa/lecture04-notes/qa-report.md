# PDF Visual QA: `lecture04-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture04/lecture04-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture04/qa/lecture04-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture04/qa/lecture04-notes/contact.png`
- Page count rendered: 43
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture04/qa/lecture04-notes/pdftoppm.log`
- Near-blank rendered pages: none

## Manual Checklist

- [x] Figures render and are readable.
- [x] Tables/formulas/code do not spill outside margins.
- [x] Important figures have nearby explanations.
- [x] No orphan captions, stranded headings, or mostly blank pages.
- [x] Box titles and long URLs look sane.

## 最终人工验收

已核对第二轮 Argon 修订后的 43 页 PDF，重新检查全部联系表及物理第 14 页原图。第 14 页两段中的 C′ 现在均正常显示撇号，新旧提交身份可明确区分。课件截图、机制图、术语表、代码与参考链接均在版心内；第二遍编译日志没有 Overfull 或 Missing character。

接受物理第 35 页的章末留白：该页约 500 字，包含完整代码解释及本章小结，内容连续，不是孤立 3 行小结页。此处“无大面积空白页”检查是在明确接受该自然章末留白的条件下通过。

关键事实修订已核对，记录在 `../../generation/residual-findings.md`。实际章节引导段有明确问题与前后关系，接受自动连接词检测的启发式警告。

验收结果：通过，保留上述已接受的自然留白。PDF SHA-256：`b3f770708d3eb136e0e9e74498ca70753d46a90a44387cd39b2daf30a4036c43`。
