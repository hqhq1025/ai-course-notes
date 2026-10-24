# PDF Visual QA: `ep07-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep07-DyMgxq0sDFo/ep07-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep07-DyMgxq0sDFo/qa/ep07-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep07-DyMgxq0sDFo/qa/ep07-notes/contact.png`
- Page count rendered: 27
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/youtube/uncle-moon/ep07-DyMgxq0sDFo/qa/ep07-notes/pdftoppm.log`
- Near-blank rendered pages: none

## Manual Checklist

- [x] Figures render and are readable.
- [x] Tables/formulas/code do not spill outside margins.
- [x] Important figures have nearby explanations.
- [x] No orphan captions, stranded headings, or mostly blank pages.
- [x] Box titles and long URLs look sane.

## 最终验收

- 实际查看全部 27 页联系图，放大检查 PDF 第 11 页的风险与复利说明、第 22 页的 Amdahl 教学公式及表格、第 26 页的四列表格与末章机制图。
- 最终双遍 XeLaTeX 成功，无 Overfull 或 Missing character 提示。七张正文机制图、七张解释表、21 个教学框正常显示。
- `check_quality.sh` 为 ⭐⭐⭐。覆盖检查无硬错误；已在来源清单补齐七个必需机制图节点，全部匹配。
- 接受 `no-terminology-digestion-detected` 提示：已有七张解释表，以及首次出现处的 RSU、CFP、Token、模型服务层等术语定义。表格标题未采用该启发式的限定关键词。
- 在原有全篇编辑后，Argon 另返回 19 处定点修改。复利与杠铃改为不互斥的两类金融概念，家庭开支底线是本段重点；风险刻度还原为讲者主观对照；末章删除无来源动作与劳动史旁枝，按个人条件解释学生及在职者的行动空间。
- 定点请求含当前完整书稿、完整官网逐字稿、已有来源校正与末章实际 SVG。回执记录 gemini-4-argon、stop、完整 JSON。
