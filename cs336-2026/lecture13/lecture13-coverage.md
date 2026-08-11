# Lecture 13 Coverage Matrix

Status: complete after second-round source-first rewrite and verification on 2026-08-11.

Source: `lecture13-slides.py`, official executable lecture source. The rewritten note follows source clusters and localizes all image assets.

Verification evidence:

- `tools/scripts/check_quality.sh cs336-2026/lecture13/lecture13-notes.tex` reports `22p 15s 55b 19f 601c/f ⭐⭐⭐`.
- Strict coverage reports `figs=19 readfig=13 boxes=55 term_digest=6 teacher_voice=10 summaries=3 prose_chars=11433` with no errors or warnings.
- `lecture13-teacher-voice-ledger.md` records nine executable-source narration clusters and distinguishes source-backed `课堂提示` from note-authored `讲义提醒`.
- Double-pass XeLaTeX succeeds; the second-pass log has no layout overflow, missing-character, undefined-control-sequence, or rerun warnings.
- Visual PDF QA was rendered and manually checked in `qa/lecture13-notes/`, including the contact sheet and enlarged pages 6, 7, 21, and 22.

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
