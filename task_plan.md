# CS25 + CS153 全量重写计划（当前）

更新时间：2026-08-13

## 当前目标

按 wdkns/wdkns-skills `main` commit `39f1a04c46e1d0d70f6b71a8fcf079b305a632b9`、仓库 `AGENTS.md` 与 `QUALITY.md`，重写并验收：

- `cs25/`：V1--V5 官方共 41 讲，现已全部按统一标准重写并验收。
- `cs153/`：11 讲，覆盖本地现有 Stanford Infra @ Scale / Frontier Systems 讲义。
- CS25 V6 官方播放列表截至 2026-08-11 已有 9/9 场录像，现已全部完成本地生成与验收；CS153 Spring 2026 继续作为独立新学期队列核验。

## 当前阶段

| 阶段 | 状态 | 验收点 |
|---|---|---|
| 1. 双课程素材与质量审计 | 已完成 | 51 讲逐讲统计 source、页数、图、盒子、字幕、slides、manifest、QA 与当前质量。 |
| 2. 官方范围与源文件核验 | 已完成 | 已确认本地范围、CS153 公开视频约束与 CS25 V6 新范围分离原则。 |
| 3. CS153 全量重写 | 已完成 | Lecture 01--11 全部完成；strict coverage、`⭐⭐⭐`、双遍编译、canonical QA 与 26 项 focused tests 均通过。 |
| 4. CS25 V1--V5 全量重写 | 已完成 | Lecture 01--41 全部通过 strict coverage、`⭐⭐⭐`、双遍编译与 canonical QA。 |
| 5. CS25 V6 扩展 | 已完成 | Lecture 01--09 全部正式验收；共 472 页、474 张教学图、393 个教学盒。 |
| 6. 全课程统一验收 | 已完成 | CS153 11/11、CS25 V1--V5 41/41、CS25 V6 9/9 均通过 strict coverage、`⭐⭐⭐`、canonical QA、teacher voice 与 tracking 验收。 |

## 重写标准

- 讲义是中文教学材料，不是字幕翻译或截图相册。
- 官方 slides 存在时做 source-complete coverage；视频口头信息进入 teacher-voice ledger。
- 每个重要图都有问题设置、读图方法、证据边界和工程连接。
- 首次出现的术语就地解释；密集名词必须有术语消化表。
- 每讲双遍 XeLaTeX、strict coverage、质量 `⭐⭐⭐`、canonical PDF 视觉 QA。
- 保留现有无关脏改动，不提交、不推送，不把 `.aux/.log/.out/.toc` 纳入交付。

---

# AI Course Notes Update Plan（历史）

## Goal
Refresh the repository status and course update tracking, then add a first feasible batch of new notes without pretending the long-running course backlog is complete.

## Scope For This Batch
- Update project inventory counts and active-course status in `README.md` and `TRACKING.md`.
- Inspect whether the newest short Bilibili items can be processed locally.
- Preserve the existing untracked `cs336-2026/` material and document what remains for CS336/CS153/CS25.
- Maintain `NOTE_GENERATION_TODO.md` as the ongoing generation queue.
- After user feedback, upgrade CS336 Spring 2026 notes to repository quality standards before continuing beyond lecture01.

## Phases

| Phase | Status | Notes |
|---|---|---|
| 1. Working plan | complete | Created persistent plan/findings/progress files. |
| 2. Refresh inventory | complete | Counted notes, inspected git status, verified source availability. |
| 3. Documentation update | complete | Patched README/TRACKING with current status and prioritized backlog. |
| 4. First-batch note generation | complete | Modern Agent 17 generated; Agentic RL 16 remains blocked by preview-only media without Bilibili cookies/full access. |
| 5. Verification | complete | Counts, stale-text search, diff whitespace check, CS336 file checks, and Modern Agent 17 PDF compile were run. |
| 6. CS336 lecture01 quality uplift | complete | Rewrote lecture01 from a 9-page draft into a 27-page long-form note with official figures, examples, formulas, code listings, and full summaries. |
| 7. CS336 lecture02 generation | complete | Generated a 25-page long-form resource-accounting note with official/source-backed figures and quality-script verification. |
| 8. CS336 lecture03 generation | complete | Generated a 35-page strict long-form architecture/hyperparameters note from official slides, with depth, engineering judgment, code snippets, and quality-script verification. |
| 9. CS336 lecture04 generation | complete | Generated a 38-page Spring 2026 long-form note covering attention alternatives and mixture-of-experts, with quality-script verification. |
| 10. CS336 lecture05 generation | complete | Generated a 31-page Spring 2026 long-form GPUs note from official slides, including GPU architecture, roofline, low precision, fusion, recomputation, coalescing, tiling, matrix performance, and FlashAttention. |
| 11. CS336 lecture06 generation | complete | Generated a 31-page Spring 2026 long-form Kernels/Triton note from executable slide source, covering benchmarking, profiling, fusion, Triton GeLU/softmax/row-sum/matmul kernels, and quality-script verification. |
| 12. CS336 lecture07 generation | complete | Generated a 25-page Spring 2026 long-form Parallelism note from executable slide source, covering collectives, hardware interconnects, NCCL/PyTorch distributed, communication benchmarking, data parallelism, tensor parallelism, pipeline parallelism, and quality-script verification. |
| 13. CS336 lecture08 generation | complete | Generated a 41-page Spring 2026 long-form Parallelism Basics note from official slide PDF, covering networking, ZeRO/FSDP, pipeline/tensor/sequence/expert/context parallelism, 3D/4D scaling recipes, recent model examples, and quality-script verification. |
| 14. CS336 lecture09 generation | complete | Generated a 36-page Spring 2026 long-form Scaling Laws Basics note from official slide PDF, covering data scaling, model/data/compute scaling, hyperparameter scaling, critical batch size, muP, Chinchilla methods, deployment-aware overtraining, and quality-script verification. |
| 15. CS336 lecture10 generation | complete | Generated a 30-page Spring 2026 long-form Inference note from official executable slide source, covering KV cache, prefill/generation, latency-throughput models, KV compression, quantization, pruning/distillation, speculative sampling, continuous batching, and PagedAttention. |
| 16. CS336 lecture01-02 regeneration under new standards | complete | Regenerated lecture01 and lecture02 from official Spring 2026 executable sources under slide-complete/figure-interpretation/terminology-digestion standards; both compile and report `⭐⭐⭐`. |
| 17. CS336 lecture04 new-workflow verification | complete | Re-verified lecture04 after the new source-first rewrite: all 60 slide images are included, PDF visual QA is checked, coverage and quality scripts pass, and log/diff checks are clean. |
| 18. CS336 lecture07 regeneration under new standards | complete | Regenerated lecture07 from the official executable source with read-the-figure explanations, terminology digestion, formulas, code walkthroughs, quality/coverage checks, and visual PDF QA. |
| 19. CS336 lecture08 regeneration under new standards | complete | Regenerated lecture08 from the 73-page official slide deck with slide-complete coverage, detailed read-the-figure/table/formula explanations, quality/coverage checks, and visual PDF QA. |
| 20. CS336 lecture09 regeneration under new standards | complete | Regenerated lecture09 from the 57-page official slide deck with slide-complete coverage, detailed read-the-figure/formula/table explanations, quality/coverage checks, and visual PDF QA. |
| 21. CS336 lecture10 regeneration under new standards | complete | Regenerated lecture10 from the official executable source with source-node-complete coverage, detailed read-the-figure explanations, terminology digestion, quality/coverage checks, and visual PDF QA. |
| 22. Discover newer CS336 lectures | complete | Official lecture11-13 materials were found and downloaded from the Stanford lectures repository. |
| 23. CS336 lecture11 generation under new standards | complete | Generated lecture11 from the 58-page official slide deck with slide-complete coverage, read-the-figure/formula explanations, quality/coverage checks, and visual PDF QA. |
| 24. CS336 lecture12 generation under new standards | complete | Generated lecture12 from the official executable source with localized images, source-node-complete coverage, read-the-figure explanations, quality/coverage checks, and visual PDF QA. |
| 25. CS336 lecture13 generation under new standards | complete | Generated lecture13 from the official executable source with localized images, source-node-complete coverage, read-the-figure explanations, quality/coverage checks, and visual PDF QA. |
| 26. YouTube ttkd0t5qTD4 authentication | complete | Root-solved YouTube extraction with account cookies, bgutil PO-token provider, compatible curl_cffi, and EJS remote challenge solver; format listing succeeds. |
| 27. YouTube ttkd0t5qTD4 video note | complete | Downloaded original 4K video/subtitles/cover/metadata, extracted frames, wrote 21-page Chinese TeX note, compiled PDF, passed quality/coverage checks, and completed visual QA. |
| 28. Zhang Xiaojun YouTube interview batch | in_progress | Build deduplicated queue for all Zhang Xiaojun Podcast YouTube interviews, then generate notes one video at a time under the authenticated YouTube workflow. |
| 29. CS336 prose-density workflow audit | complete | User feedback showed figure-heavy notes lacked enough prose and transitions; added prose-density/weak-opener checks, updated standards, and documented repair plan. |
| 30. CS153 and CS25 full-course rewrite | complete | CS153 11/11, CS25 V1--V5 41/41, and CS25 V6 9/9 now pass the source-first, teacher-voice, strict-coverage, `⭐⭐⭐`, double-XeLaTeX, and signed visual-QA workflow. |

## Decisions
- Do not attempt a full CS336/CS153/CS25 generation batch in one pass; those are multi-lecture long-form courses.
- Treat Bilibili videos as conditional on subtitles or local speech-to-text availability.
- Download official CS336 2026 lecture materials when available because this is low-risk and does not require video transcription.
- Use A100/faster-whisper for videos with downloadable audio but no subtitles.
- For CS336 Spring 2026, generate one lecture at a time and hold each finished note to the long-form repository standard before moving on.
- New user-requested standard: important figures need detailed read-the-figure explanations; dense terminology requires concentrated glossary-style digestion; foundational background concepts should use diagrams/tables/formulas; when slides or executable slide sources exist, cover every teaching slide/node rather than sampling only representative figures.

## Errors Encountered

| Error | Attempt | Resolution |
|---|---|---|
| Bilibili `yt-dlp` HTTP 412 | Tried direct metadata extraction for Modern Agent 17 and Agentic RL 16 | Public Bilibili APIs still provide metadata, but video/subtitle download is blocked by platform anti-bot. |
| No Whisper available | Checked `whisper` CLI and Python module | Mark Bilibili note generation as blocked until transcription tooling or cookies are available. |
| Agentic RL 16 preview only | Downloaded via public Bilibili playurl API | Public unauthenticated media contains only about 5 minutes; full note requires Bilibili cookies/full access. |
| Wrong working directory for chmod | Ran a root-relative path while already inside `cs336-2026/lecture01` | Re-ran with paths relative to the lecture directory before compiling. |
| Quality script reports 0 pages | `tools/scripts/check_quality.sh` depended on `pdfinfo`, which is unavailable on this host | Added a `mutool` fallback and changed box counting to actual box environments; final CS336 lecture01 check reports `27p 13s 22b 11f ⭐⭐⭐`. |
| Malformed regex while scanning L05 style | An early `rg` expression had an unclosed group | Re-ran with a simpler escaped expression and used the results for style alignment. |
| Long links caused overfull hboxes in L06 | First L06 XeLaTeX pass compiled but showed overfull URL lines in the reading list | Replaced raw visible URLs with short `\href{...}{...}` labels and recompiled. |
| `pdftotext` unavailable | Tried to inspect the old lecture07 slide PDF text for cross-checking | Used executable source, old TeX notes, and local slide images/official downloaded assets instead. |
| L07 overfull boxes | First L07 XeLaTeX pass compiled but showed a few overfull lines from long English distributed-systems terms in narrow text/table cells | Rephrased long terms into shorter Chinese labels and recompiled. |
| Raw PDF count inflated | `find . -name '*-notes.pdf'` counted `.web-build` generated site copies | Use canonical source count with `.web-build` pruned for README/project inventory verification. |
| `sudo apt-get` blocked | Tried to install `poppler-utils` for `pdftotext` after user approved installing missing tools | Host requires an interactive sudo password; used existing `mutool` to extract L08 text and render slide images instead. |
| L08 overfull boxes | First L08 XeLaTeX pass compiled but showed overfull lines from a long memory formula and a wide parallelism summary table | Split the formula into an `align*` block, tightened the table, shortened long English labels, and recompiled. |
| L09 PDF bookmark warnings | First L09 XeLaTeX pass warned about math symbols in section titles for `muP` | Replaced math in section/subsection titles with text `muP`, shortened the paragraph, and recompiled until rerun warnings cleared. |
| L10 tcolorbox math title | First L10 XeLaTeX pass stopped with `Missing $ inserted` from math in a box title | Rephrased the box title as plain text and recompiled until rerun warnings cleared. |
| YouTube anti-bot login challenge | Anonymous `yt-dlp --dump-single-json` and `yt-dlp -F` for `ttkd0t5qTD4` | Root cause: YouTube requires sign-in/bot confirmation for this host; next attempt will use local browser cookies if available, without committing cookie data. |
## Current execution checkpoint — 2026-08-13

- CS153 / Frontier Systems: 11/11 rewritten and accepted.
- CS25 V1–V5: 41/41 rewritten and accepted.
- CS25 V6: 9/9 rewritten and accepted; the course is complete.
- Lecture 05 uses 41 required recording-derived teaching states because the live course-page slide link duplicates Lecture 04's 106-page Ultra-Scale deck.
- Lecture 06 uses 45 required pages from the official 50-page deck; the full 870-frame recording audit found no independent deck-external teaching visual.
- Lecture 07 uses 23 required recording-derived teaching states; its evidence ledger freezes the classroom-date source snapshot and records that AMIE appears only in the description, not in the actual lecture.
- Lecture 08 uses 37 required pages from the official 56-page deck; pages 53--55 are deck-only Interaction Models appendix pages skipped in the recording and remain optional.
- Lecture 09 uses 57 required official deck pages plus one live token-timing demo frame. Deck pages 070, 072, and 073 are intentionally optional because they are a transition joke, a CI/CL appendix not taught in the recording, and a recruiting page.

### Errors encountered

| Error | Attempt | Resolution |
|---|---:|---|
| `ModuleNotFoundError: cv2` while clustering 2-second video samples | 1 | Keep the already extracted samples; replace the temporary OpenCV selector with Pillow/NumPy/SciPy so the repository gains no new dependency. |
| Extracting each slide with output-side seek decoded from the start of the 77-minute video and was too slow | 1 | Interrupted the inefficient pass; use a five-second input-side preseek followed by exact output-side seek within that window, then visually verify the contact sheet. |
| Dynamically importing the SRT helper for ad-hoc transcript slicing triggered a dataclass module-registration error | 1 | Read the already generated `transcript_timed.txt` directly; no source transcript or repository dependency changed. |
