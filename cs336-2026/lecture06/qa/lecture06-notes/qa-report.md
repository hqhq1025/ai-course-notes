# PDF Visual QA: `lecture06-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture06/lecture06-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture06/qa/lecture06-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture06/qa/lecture06-notes/contact.png`
- Page count rendered: 23
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture06/qa/lecture06-notes/pdftoppm.log`
- Near-blank rendered pages: none

## Manual Checklist

- [x] Figures render and are readable.
- [x] Tables/formulas/code do not spill outside margins.
- [x] Important figures have nearby explanations.
- [x] No orphan captions, stranded headings, or mostly blank pages.
- [x] Box titles and long URLs look sane.

## Manual Review Notes

- Reviewed the complete 23-page contact sheet and full-size final pages 22--23 on 2026-08-11.
- The first render exposed a sparse second TOC page; the final PDF uses a section-level TOC.
- The profiler case heading initially overflowed by 7.6pt; the heading was shortened while all exact source labels remain visible in the table.
- The original sparse summary page was rebuilt as annotated readings, a hold-out shape-sweep experiment, a kernel-delivery checklist, and a failure-diagnosis table.
- All GPU hierarchy, grid, occupancy, softmax, row-sum, and GEMM-tiling figures render without cropping or unreadable scaling.
