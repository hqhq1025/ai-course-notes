# AI Course Notes Update Plan

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

## Decisions
- Do not attempt a full CS336/CS153/CS25 generation batch in one pass; those are multi-lecture long-form courses.
- Treat Bilibili videos as conditional on subtitles or local speech-to-text availability.
- Download official CS336 2026 lecture materials when available because this is low-risk and does not require video transcription.
- Use A100/faster-whisper for videos with downloadable audio but no subtitles.
- For CS336 Spring 2026, generate one lecture at a time and hold each finished note to the long-form repository standard before moving on.

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
