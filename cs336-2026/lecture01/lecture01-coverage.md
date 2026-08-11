# Lecture 01 Coverage Matrix

Status: second-round executable-source verification completed on 2026-08-11.

Verification evidence:

- Strict coverage: `figs=15 readfig=23 boxes=44 term_digest=5 teacher_voice=7 formulas=3 code=3 summaries=7 prose_chars=12639`, with no warnings or hard errors.
- Quality check: 22 pages after compilation, 15 source figures, `⭐⭐⭐`.
- Double-pass XeLaTeX succeeds with no overfull box, LaTeX error, fatal error, or undefined control sequence.
- Visual QA: full contact sheet and representative full-size pages reviewed; checklist signed.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| `welcome()` / `course-staff.png` | figure + opening | yes | 本讲总览 | figure + read-the-figure + course positioning | covered |
| `why_this_course_exists()` | motivation cluster | yes | 为什么要从零构建语言模型 | abstraction leak explanation + warning box | covered |
| `industrialisation.jpg` | metaphor figure | yes | 工业化与尺度 | figure + read-the-figure | covered |
| `gpt4-no-details.png` | evidence figure | yes | 工业化与尺度 | figure + warning about opaque frontier details | covered |
| `roller-flops.png` | dense table figure | yes | 尺度改变系统瓶颈 | figure + read-the-figure + FLOPs vs wall-clock warning | covered |
| `wei-emergence-plot.png` | multi-panel plot | yes | 尺度改变能力表现 | figure + read-the-figure + over-interpretation warning | covered |
| `divine-benevolence.png` | quote figure | yes | 三类可迁移知识 | figure + methodology interpretation | covered |
| `current_lm_landscape()` | terminology/history cluster | yes | 语言模型发展版图 | Shannon/n-gram diagram + terminology table + open model table | covered |
| `what_is_this_program()` | executable lecture concept | yes | 课程机制 | code listing + explanation of trace-based lectures | covered |
| `course_logistics()` | logistics/admin | partial | 课程机制 | condensed to course load, assignments, AI policy; pure logistics omitted | accepted |
| `course_syllabus()` | course roadmap | yes | 课程版图 | table + compute-memory figure + systems/scaling/data visuals | covered |
| `transformer-architecture.png` | architecture figure | yes | 课程版图 | figure + read-the-figure as future object to decompose | covered |
| `compute-memory.png` | systems concept figure | yes | 课程版图 | figure + read-the-figure | covered |
| `dgx-b200-system-topology.png` | systems topology figure | yes | 课程版图 | figure + read-the-figure | covered |
| `prefill-decode.png` | inference figure | yes | 课程版图 | figure + read-the-figure | covered |
| `chinchilla-isoflop.png` | scaling figure | yes | Scaling laws and data examples | figure + read-the-figure | covered |
| `marin-loss-forecast.jpg` | scaling forecast figure | yes | Scaling laws and data examples | figure + read-the-figure | covered |
| `pile-chart.png` | data mixture figure | yes | Scaling laws and data examples | figure + read-the-figure | covered |
| `tokenized-example.png` | tokenizer figure | yes | Tokenization | figure + read-the-figure | covered |
| `CharacterTokenizer` / `ByteTokenizer` / `BPETokenizer` | code mechanisms | yes | Tokenization | interface code + BPE merge code + trade-off tables | covered |
| Executable-source section titles | source navigation | yes | `Executable source 索引` | former comment-only markers replaced by a rendered source-node-to-note teaching map | covered |
| `transcript_timed.txt` | teacher voice | yes | throughout | eight timestamped spoken motivations, caveats and engineering heuristics tracked in `teacher-voice-ledger.md` and woven into prose/boxes | covered |
| First-use glossary terms | systems/LM terms | yes | Throughout | Shannon entropy, n-gram, open-weight/source, tokenizer, BPE, prefill/decode explained locally | covered |
| PDF visual QA | QA | yes | `qa/lecture01-notes/` | 22 rendered pages, contact sheet and representative full-size pages inspected; checklist signed | complete |
