# PDF Visual QA: `lecture07-notes.pdf`

- PDF: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture07/lecture07-notes.pdf`
- Rendered pages: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture07/qa/lecture07-notes`
- Contact sheet: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture07/qa/lecture07-notes/contact.png`
- Page count rendered: 59
- Renderer: pdftoppm
- Renderer log: `/home/v-haoqiwang/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture07/qa/lecture07-notes/pdftoppm.log`
- Near-blank rendered pages: none

## Manual Checklist

- [x] Figures render and are readable.
- [x] Tables/formulas/code do not spill outside margins.
- [x] Important figures have nearby explanations.
- [x] No orphan captions, stranded headings, or mostly blank pages.
- [x] Box titles and long URLs look sane.

## Presentation revision visual review

- Reviewed on 2026-10-20: full contact sheet and full-size PDF pages 43 and 57 in the first presentation build. After the final formula fix, visually rechecked PDF pages 39 and 58; checked page 57 text placement with pdftotext.
- First-use `View = render(Model, ViewState)` now renders correctly on page 39. The emphasis applies to the following prose term, with no Markdown markers inside math. The later display equation and code remain readable.
- The stranded exercise 3 acceptance label now starts page 58 together with its numbered requirements. Exercise headings no longer have duplicate numbering.
- The final compile-pass2 log has no Overfull or missing-character messages.
- Reviewed PDF SHA-256: `4e678b048a7aac46460524ecc00a85537cc8d6a951ee110a3ec83e2fa4291162`.
