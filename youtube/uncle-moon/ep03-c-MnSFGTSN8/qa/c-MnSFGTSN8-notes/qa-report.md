# PDF Visual QA: `c-MnSFGTSN8-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep03-c-MnSFGTSN8/c-MnSFGTSN8-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep03-c-MnSFGTSN8/qa/c-MnSFGTSN8-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep03-c-MnSFGTSN8/qa/c-MnSFGTSN8-notes/contact.png`
- Page count rendered: 21
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep03-c-MnSFGTSN8/qa/c-MnSFGTSN8-notes/pdftoppm.log`
- Near-blank rendered pages: none

## Manual Checklist

- [x] Figures render and are readable.
- [x] Tables/formulas/code do not spill outside margins.
- [x] Important figures have nearby explanations.
- [x] No orphan captions, stranded headings, or mostly blank pages.
- [x] Box titles and long URLs look sane.

## 验收记录

- 查看了全部 21 页联系图，放大检查 PDF 第 5 页的表格和机制图、第 15 页的正文与微秒符号。六张图的独立图集也已检查。
- 双遍 XeLaTeX 成功，修正了 μ 字形后无 Missing character 或 Overfull 提示。Fandol 的字体脚本声明警告不影响当前页面字形。
- 共六章、六张机制图、六个对照表、18 个教学框。`check_quality.sh` 为 ⭐⭐⭐；覆盖检查无硬错误，六个必需图节点全部匹配。
- 接受 `no-terminology-digestion-detected` 启发式提示：表格标题未使用脚本限定的关键词，但正文首次解释术语，表格包含研究机制、教育功能及缓存/预测/调度对照，实际已有集中解释。
- 全部章节和全篇编辑请求包含完整官网逐字稿。86 处全篇修改由 Argon 返回，覆盖来源归属、案例细节、研发目标、术语与衔接。
- 本期为人物访谈。批次负责人抽查三个时间点的工作视频，未见实质屏幕演示；正文使用机制图，不重复人物画面。
