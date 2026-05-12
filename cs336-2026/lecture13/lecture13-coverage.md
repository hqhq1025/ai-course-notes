# Lecture 13 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source: `lecture13-slides.py`, official executable lecture source. The rewritten note follows source clusters and localizes all image assets.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture13-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture13/lecture13-notes.tex` reports `20p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture13/lecture13-notes.tex --manifest cs336-2026/lecture13/lecture13-manifest.md` reports `figs=19 readfig=13 boxes=46 term_digest=6 formulas=0 code=0 summaries=3` with no hard errors or warnings.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture13-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| main and motivation | source cluster | yes | Lecture 13 / 为什么数据最重要 | data secrecy, training stages, OLMo/Tulu examples | complete |
| raw sources | source cluster | yes | Raw sources | crawler, restrictions, decline of consent, shadow libraries | complete |
| copyright | source cluster | yes | Copyright | IP law, licenses, fair use, lawsuits, ToS | complete |
| Common Crawl | source cluster | yes | Common Crawl | crawler architecture, WARC/WET, HTML extraction | complete |
| specialized sources | source cluster | yes | Wikipedia/GitHub/arXiv | strengths, limitations, poisoning/license issues | complete |
| classic datasets | source cluster | yes | BERT/WebText/CCNet/C4 | source lineage, filtering, C4 domains | complete |
| modern datasets | source cluster | yes | GPT-3/The Pile/Gopher/LLaMA/RefinedWeb/Dolma/DCLM/Nemotron | data recipes, filtering strategies, result figures | complete |
| code and licensing | source cluster | yes | The Stack / CommonPile | code data, PR metadata, permissive-data caveats | complete |
| quality loop | synthesis | yes | 数据质量评估与反馈闭环 | audit metrics, eval-to-data feedback, checklist | complete |
| PDF visual QA | QA | yes | `qa/lecture13-notes/` | rendered pages + contact sheet + checked report | complete |
