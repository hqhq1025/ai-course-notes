# PDF Visual QA: `UI09mbzn8ac-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep04-UI09mbzn8ac/UI09mbzn8ac-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep04-UI09mbzn8ac/qa/UI09mbzn8ac-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep04-UI09mbzn8ac/qa/UI09mbzn8ac-notes/contact.png`
- Page count rendered: 21
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep04-UI09mbzn8ac/qa/UI09mbzn8ac-notes/pdftoppm.log`
- Near-blank rendered pages: none

## Manual Checklist

- [x] Figures render and are readable.
- [x] Tables/formulas/code do not spill outside margins.
- [x] Important figures have nearby explanations.
- [x] No orphan captions, stranded headings, or mostly blank pages.
- [x] Box titles and long URLs look sane.

## 验收记录

- 查看了全部 21 页联系图，放大检查 PDF 第 11 页的净收入留存算例、表格和机制图，以及第 19 页的福利列表和教学框。六张图的独立图集也已检查。
- 双遍 XeLaTeX 成功，最终无 Missing character 或 Overfull 提示。Fandol 的字体脚本声明警告不影响当前页面字形。
- 共六章、六张机制图、六个对照表、18 个教学框。`check_quality.sh` 为 ⭐⭐⭐；覆盖检查无硬错误，六个必需图节点全部匹配。
- 接受 `no-terminology-digestion-detected` 启发式提示：正文与表格已经解释 NDR、SMB、Enterprise、FDE、SOC 2 等术语，标题不符合该脚本的关键词规则。NDR 教学算例按同批期初客户计算，排除了新客户收入。
- 全部章节和全篇编辑请求包含完整官网逐字稿。103 处全篇修改及最后三处定点修订均由 Argon 返回，保留早期快速验证与后期长期交付的阶段区别。
- 本期为人物访谈。批次负责人抽查三个时间点的工作视频，未见实质屏幕演示；正文使用机制图，不重复人物画面。
