# Progress Log

## 2026-05-04
- Started update batch after user approval.
- Loaded planning, YouTube PDF, Bilibili PDF, and verification skills.
- Verified local tooling availability.
- Counted current notes: 290 PDFs and 289 TeX files before this batch.
- Confirmed Bilibili new videos have public metadata but no platform subtitles.
- Marked Bilibili note generation blocked due to B站 412 plus missing Whisper.
- Updated README and TRACKING with current inventory and active-course backlog.
- Downloaded CS336 Spring 2026 official materials for lecture05-10 into `cs336-2026/`.
- Verified downloaded CS336 files by `file` and `wc -c`.
- Final verification: 290 `*-notes.pdf` files, no stale README/TRACKING strings found, `git diff --check` clean, and CS336 downloaded files have valid file types.
- Created `NOTE_GENERATION_TODO.md` to track pending note generation.
- Confirmed 4 A100 80GB GPUs are visible via `/proc/driver/nvidia/gpus`.
- Confirmed `faster-whisper` and cached large-v3 model exist, but YouTube and Bilibili downloads currently require cookies.
- Downloaded Modern Agent 17 via public Bilibili playurl API, extracted audio, transcribed on A100 with faster-whisper large-v3, generated key frames, wrote TeX, and compiled `lecture17-notes.pdf`.
- Attempted Agentic RL 16 via public Bilibili playurl API; only preview-length media was accessible, so no incomplete PDF was generated.
- Verification after Modern Agent 17: note count is 291, generated PDF/TeX/SRT exist, no stale README/TODO strings found, and `git diff --check` is clean.
- Switched focus to CS336 at user request.
- Generated `cs336-2026/lecture01/lecture01-notes.tex` from official Spring 2026 `lecture01-slides.py`.
- Compiled initial `cs336-2026/lecture01/lecture01-notes.pdf` draft with XeLaTeX; output was 9 pages and was later superseded by the quality rewrite.
- Updated README/TRACKING/TODO after CS336 lecture01; note count temporarily became 292 before lecture02 was added.
- User clarified that CS336 notes must meet the repository depth standard rather than a thin summary.
- Rewrote `cs336-2026/lecture01/lecture01-notes.tex` into a deeper 964-line course note, removed manual TikZ figures, and added official image assets under `cs336-2026/lecture01/images/`.
- Recompiled `cs336-2026/lecture01/lecture01-notes.pdf` twice with XeLaTeX; current PDF is 27 pages by `mutool`, with 11 images including cover, 22 teaching boxes, 13 section-level summaries, and 9 code listings.
- Patched `tools/scripts/check_quality.sh` to fall back to `mutool` when `pdfinfo` is unavailable and to count actual box environments.
- Final verification: `tools/scripts/check_quality.sh cs336-2026/lecture01/lecture01-notes.tex` later reports `28p ⭐⭐⭐`, and `git diff --check` passed.
- Continued CS336 Spring 2026 with lecture02 at the same depth standard.
- Downloaded lecture02 figure assets, wrote `cs336-2026/lecture02/lecture02-notes.tex`, and compiled `lecture02-notes.pdf` twice with XeLaTeX.
- Lecture02 verification: `tools/scripts/check_quality.sh cs336-2026/lecture02/lecture02-notes.tex` later reports `26p ⭐⭐⭐`; note count became 293 PDFs.
- Resumed CS336 Spring 2026 at user request with stricter quality bar: deep exposition, careful technical detail, and one verified lecture at a time.
- Started `cs336-2026/lecture03/`, using official lecture03 slides plus the existing CS336 lecture03 note as a cross-check, not as a replacement for fresh writing.
- Wrote `cs336-2026/lecture03/lecture03-notes.tex` as a fresh Spring 2026 architecture/hyperparameters note with conservative recipe tables, formulas, code snippets, official slide figures, and explicit engineering judgment sections.
- Compiled `cs336-2026/lecture03/lecture03-notes.pdf` with XeLaTeX; quality verification reports `35p 11s 24b 33f ⭐⭐⭐`, and repository note count is now 294 PDFs.
- Continued to `cs336-2026/lecture04/` at user request.
- Confirmed Spring 2026 lecture04 is broader than the old CS336 lecture04: it covers attention alternatives (linear attention, Mamba-2, Gated Delta Net, sparse adaptation/DSA) before mixture-of-experts.
- Wrote `cs336-2026/lecture04/lecture04-notes.tex` as a fresh Spring 2026 long-form note tying attention alternatives and MoE together through sparse/conditional computation.
- Compiled `cs336-2026/lecture04/lecture04-notes.pdf` with XeLaTeX; quality verification reports `38p 14s 21b 41f ⭐⭐⭐`, and repository note count is now 295 PDFs.
- Continued to `cs336-2026/lecture05/` at user request.
- Confirmed Spring 2026 lecture05 is a 55-slide GPU performance lecture: GPU/TPU architecture, memory hierarchy, low precision, fusion, recomputation, memory coalescing, tiling, matrix-performance anomalies, and FlashAttention.
- Generated 55 slide images under `cs336-2026/lecture05/slides-images/`.
- Wrote `cs336-2026/lecture05/lecture05-notes.tex` as a fresh Spring 2026 long-form GPU performance note with matmul arithmetic-intensity derivation, low-precision tradeoffs, attention IO accounting, and FlashAttention design checklist.
- Compiled `cs336-2026/lecture05/lecture05-notes.pdf` with XeLaTeX; quality verification reports `31p 9s 21b 36f ⭐⭐⭐`, and repository note count is now 296 PDFs.
- Continued to `cs336-2026/lecture06/` at user request.
- Confirmed Spring 2026 lecture06 is an executable-source lecture on benchmarking, profiling, kernel fusion, torch.compile, and Triton kernels for GeLU, softmax, row sum, and matmul+ReLU.
- Downloaded/copied lecture06 visual assets into `cs336-2026/lecture06/images/`, including official referenced images and selected L05 GPU/roofline/tiling recap figures.
- Wrote `cs336-2026/lecture06/lecture06-notes.tex` as a fresh Spring 2026 long-form Kernels/Triton note with detailed GPU programming-model review, benchmarking/profiling methodology, fusion memory accounting, and Triton kernel walkthroughs for GeLU, softmax, row sum, and matmul+ReLU.
- Compiled `cs336-2026/lecture06/lecture06-notes.pdf` twice with XeLaTeX; single-note quality verification reports `31p 13s 31b 12f ⭐⭐⭐`, and repository note count is now 297 PDFs.
- Final L06 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-06 all `⭐⭐⭐`, `find . -name '*-notes.pdf' | wc -l` reports `297`, `git diff --check` passed, and the L06 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Continued to `cs336-2026/lecture07/` at user request.
- Confirmed Spring 2026 lecture07 is an executable-source lecture on multi-GPU parallelism: collectives, interconnect hardware, NCCL/PyTorch distributed, communication benchmark methodology, and bare-bones data/tensor/pipeline parallel MLPs.
- Downloaded lecture07 visual assets into `cs336-2026/lecture07/images/`, including official CS336 diagrams for ranks/interconnect/data/tensor/pipeline parallelism and PyTorch/NCCL diagrams for broadcast, scatter, gather, reduce, all-gather, all-reduce, and reduce-scatter.
- Wrote `cs336-2026/lecture07/lecture07-notes.tex` as a fresh Spring 2026 long-form Parallelism note with detailed sections on collectives, hardware topology, NCCL/PyTorch distributed, communication benchmarking, and data/tensor/pipeline parallel MLP implementations.
- Compiled `cs336-2026/lecture07/lecture07-notes.pdf` twice with XeLaTeX; single-note quality verification reports `25p 12s 30b 14f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 298 PDFs.
- Final L07 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-07 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `298`, `git diff --check` passed, and the L07 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Continued to `cs336-2026/lecture08/` at user request.
- Confirmed Spring 2026 lecture08 is a 73-page official PDF deck titled "Parallelism Basics".
- Attempted to install missing `pdftotext` support via `sudo apt-get install poppler-utils`; host requires an interactive sudo password, so the install was blocked.
- Used existing `mutool` to extract lecture08 per-page text into `/tmp/lecture08-text-*.txt` and render 73 slide images under `cs336-2026/lecture08/slides-images/`.
- Wrote `cs336-2026/lecture08/lecture08-notes.tex` as a fresh Spring 2026 long-form Parallelism Basics note with detailed sections on networking, collective communication, ZeRO/FSDP, pipeline/tensor/sequence/expert/context parallelism, 3D/4D recipes, and recent model configurations.
- Compiled `cs336-2026/lecture08/lecture08-notes.pdf` twice with XeLaTeX; single-note quality verification reports `41p 14s 23b 51f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 299 PDFs.
- Final L08 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-08 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `299`, `git diff --check` passed, and the L08 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Installed `poppler-utils` after the user provided the sudo password for this session; `pdftotext`, `pdfinfo`, and `pdfimages` are now available.
- Continued to `cs336-2026/lecture09/` at user request.
- Confirmed Spring 2026 lecture09 is a 57-page official PDF deck titled "Scaling Laws - Basics".
- Used `pdfinfo`/`pdftotext` to inspect/extract L09 text and rendered 57 slide images under `cs336-2026/lecture09/slides-images/`.
- Wrote `cs336-2026/lecture09/lecture09-notes.tex` as a fresh Spring 2026 long-form Scaling Laws Basics note with detailed sections on data scaling, data mixture/repetition, model-engineering scaling laws, critical batch size, muP, joint data-model scaling, Kaplan vs Chinchilla, IsoFLOPS, and deployment-aware overtraining.
- Compiled `cs336-2026/lecture09/lecture09-notes.pdf` with XeLaTeX until cross-reference warnings cleared; single-note quality verification reports `36p 12s 23b 44f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 300 PDFs.
- Final L09 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-09 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `300`, `git diff --check` passed, and the L09 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Continued to `cs336-2026/lecture10/` at user request.
- Confirmed Spring 2026 lecture10 is an executable-source lecture titled "inference", covering inference metrics, arithmetic intensity, KV cache, prefill/generation, latency-throughput tradeoffs, KV compression, quantization, pruning/distillation, speculative sampling, continuous batching, and PagedAttention.
- Downloaded lecture10 visual assets into `cs336-2026/lecture10/images/`, including official CS336 figures, Scaling Book Transformer/inference/GQA diagrams, a continuous batching diagram, and a quantization diagram; converted WebP inference diagrams to PNG for local TeX compilation.
- Wrote `cs336-2026/lecture10/lecture10-notes.tex` as a fresh Spring 2026 long-form Inference note with detailed derivations, 29 figures, 41 teaching boxes, and code snippets for KV-cache decoding, latency-throughput modeling, speculative sampling, continuous batching, and PagedAttention block tables.
- Compiled `cs336-2026/lecture10/lecture10-notes.pdf` with XeLaTeX until cross-reference warnings cleared; single-note quality verification reports `30p 13s 41b 29f ⭐⭐⭐`, and canonical repository source-note count excluding `.web-build` is now 301 PDFs.
- Final L10 verification: `tools/scripts/check_quality.sh cs336-2026` reports lecture01-10 all `⭐⭐⭐`, canonical source-note count excluding `.web-build` reports `301`, `git diff --check` passed, and the L10 LaTeX log scan found no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- User reviewed lecture01 and tightened the writing standard: important figures need explicit read-the-figure interpretation, concept-dense passages need concentrated explanations, foundational background concepts should use diagrams/tables/formulas, and available slides should be covered comprehensively.
- Updated `AGENTS.md`, `QUALITY.md`, `CLAUDE.md`, and `tools/skills/video-render-common/writing-and-figures.md` to capture these new standards.
- Started regenerating CS336 Spring 2026 lecture01 and lecture02 from official executable sources under the new standards, rather than continuing to patch the existing notes.
- Downloaded additional local image assets for regenerated lecture01/02, including industrialization, DGX B200 topology, Marin scaling forecast/result, The Pile chart, FP8, and roofline images, so the PDFs do not depend on remote image URLs.
- Replaced `cs336-2026/lecture01/lecture01-notes.tex` and `cs336-2026/lecture02/lecture02-notes.tex` with fresh new-standard drafts, then compiled both PDFs with XeLaTeX until rerun warnings cleared.
- Final lecture01/02 regeneration verification: lecture01 reports `20p 7s 32b 15f ⭐⭐⭐`, lecture02 reports `20p 9s 38b 11f ⭐⭐⭐`, `tools/scripts/check_quality.sh cs336-2026` reports all ten CS336 2026 notes as `⭐⭐⭐`, `git diff --check` passed, and both lecture logs have no LaTeX errors, undefined control sequences, rerun requests, or overfull boxes.
- Added mandatory PDF visual QA workflow to shared note-generation skills and project standards, including page rendering, contact sheet inspection, full-size suspicious-page review, and required TeX fixes before completion.
- Installed missing project tooling/dependencies: `latexmk`, system `ripgrep`, `fd-find`, current-venv Python packages `yt-dlp`, `openai-whisper`, `torch` CPU, `pypdf`, `pdfplumber`, `pymupdf`, `pandas`, `matplotlib`, `beautifulsoup4`, and `lxml`; verified imports and `tests/test_generate_site.py` pass.
- Added workflow tooling: `build_lecture_manifest.py`, `check_note_coverage.py`, and `render_pdf_qa.py`, plus `docs/NOTE_GENERATION_WORKFLOW.md`; smoke-tested manifest, coverage, visual QA, and source-only `check_quality.sh .` behavior on CS336 lecture01/02.
- Extended workflow standards and `check_note_coverage.py` to require first-use explanations for dense systems terms including ZeRO, sharding, fused kernels, collectives, optimizer state, activation checkpointing, DRAM/SRAM/HBM, and perplexity; smoke test flags old CS336 lecture01 for these exact gaps.
- Completed CS336 2026 lecture01 and lecture02 new-workflow artifacts: manifests, coverage matrices, blueprints, PDF visual QA contact sheets, and checked QA reports.
- Regenerated CS336 2026 lecture03 under the new workflow as a 44-page slide-complete note with all 67 source slides included and 68 figures total; quality script reports `44p 11s 27b 68f ⭐⭐⭐`.
- Improved `render_pdf_qa.py` after lecture03 visual QA found near-blank pages from `pdftoppm`; the script now detects near-blank rendered pages and falls back/checks rendered output.
- Regenerated CS336 2026 lecture04 under the new source-first workflow as a 41-page slide-complete note with all 60 source slides included, attention/MoE glossary coverage, and read-the-figure explanations; quality script reports `41p 12s 42b 61f ⭐⭐⭐`, LaTeX log scan is clean, and visual QA contact sheet was reviewed.
- Regenerated CS336 2026 lecture05 under the new source-first workflow as a 38-page slide-complete GPU note with all 55 source slides included, 56 figures, 44 teaching boxes, and read-the-figure explanations; quality script reports `38p 8s 44b 56f ⭐⭐⭐`, LaTeX log scan is clean, and visual QA contact sheet was reviewed.
- Regenerated CS336 2026 lecture06 under the new source-first workflow as a 20-page source-node-complete kernels/Triton note with 8 figures, 36 teaching boxes, and detailed code walkthroughs for benchmarking, profiling, GeLU fusion, Triton GeLU, softmax, row-sum, and tiled matmul+ReLU; quality script reports `20p 15s 36b 8f ⭐⭐⭐`, LaTeX log scan is clean, and visual QA contact sheet was reviewed.
- Re-verified CS336 2026 lecture04 at the user's request before continuing serially: two XeLaTeX passes produced a 41-page PDF, `check_quality.sh` reports `41p ⭐⭐⭐`, `check_note_coverage.py` reports `figs=61 readfig=105 boxes=42 term_digest=3 formulas=2 code=0 summaries=10` with no hard errors, all 60 slide images are referenced, log scan is clean for hard LaTeX issues, and the refreshed PDF QA contact sheet/report were reviewed and marked complete.
- Regenerated CS336 2026 lecture07 under the new source-first workflow from the official executable lecture source: the note is now 26 pages with 15 figures, 18 read-the-figure explanations, 42 teaching boxes, 8 terminology-digestion hits, 7 formulas, and 7 code listings. Final verification reports `26p ⭐⭐⭐`; coverage has no hard errors; all local images are referenced; LaTeX log scan is clean; visual PDF QA contact sheet was reviewed and checked.
- Regenerated CS336 2026 lecture08 under the new source-first workflow from the 73-page official slide deck: the note is now slide-complete with all 73 slide images included, 53 pages, 74 figure inclusions, 59 read-the-figure/table/formula explanations, 76 teaching boxes, and explicit terminology digestion for collectives, sharding, ZeRO/FSDP, TP/SP/EP/CP, and pipeline concepts. Final verification reports `53p ⭐⭐⭐`, coverage has no hard errors, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Regenerated CS336 2026 lecture09 under the new source-first workflow from the 57-page official slide deck: the note is now slide-complete with all 57 slide images included, 42 pages, 58 figure inclusions, 53 read-the-figure/formula/table explanations, 59 teaching boxes, 5 formulas, and 3 code listings. Final verification reports `42p ⭐⭐⭐`, coverage has no hard errors, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Regenerated CS336 2026 lecture10 under the new source-first workflow from the official executable lecture source: the note is now source-node-complete with all local teaching PNGs included, 21 pages, 29 figure inclusions, 23 read-the-figure explanations, 34 teaching boxes, 4 terminology-digestion hits, and formulas for arithmetic intensity/KV cache/speculative sampling. Final verification reports `21p ⭐⭐⭐`, coverage has no hard errors or warnings, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Downloaded newly available official CS336 2026 materials for lecture11-13 from the Stanford lectures repository: lecture11 PDF deck (58 pages), lecture12 executable source, and lecture13 executable source.
- Generated CS336 2026 lecture11 under the new source-first workflow from the 58-page official slide deck: the note is slide-complete with all 58 slide images included, 43 pages, 59 figure inclusions, 53 read-the-figure/formula explanations, 60 teaching boxes, and terminology digestion for WSD, muP, optimizer scaling, Muon, Chinchilla methods, and recent scaling recipes. Final verification reports `43p ⭐⭐⭐`, coverage has no hard errors, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Generated CS336 2026 lecture12 under the new source-first workflow from the official executable lecture source: localized all 42 referenced image assets, wrote a 29-page evaluation note with 44 figure inclusions, 25 read-the-figure explanations, 40 teaching boxes, and terminology digestion for evaluation design, perplexity, zero-shot, methods/models/agents, ELO/LLM judges, ecological validity, contamination, and benchmark quality. Final verification reports `29p ⭐⭐⭐`, coverage has no hard errors or warnings, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.
- Generated CS336 2026 lecture13 under the new source-first workflow from the official executable lecture source: localized all 18 referenced image assets, wrote a 20-page Data I note with 19 figure inclusions, 13 read-the-figure explanations, 46 teaching boxes, and terminology digestion for crawlers, WARC/WET, robots.txt/ToS, copyright/fair use/licensing, Common Crawl, filtering, deduplication, model-based filtering, provenance, and data audit loops. Final verification reports `20p ⭐⭐⭐`, coverage has no hard errors or warnings, LaTeX log scan is clean, and visual PDF QA contact sheet was reviewed and checked.

## 2026-05-12 YouTube ttkd0t5qTD4
- Started user-requested YouTube note task for `ttkd0t5qTD4`.
- Loaded `youtube-render-pdf` and `planning-with-files` workflows.
- Verified local `yt-dlp`, `ffmpeg`, `xelatex`, and `pdfinfo` availability.
- Anonymous YouTube metadata/format extraction failed because YouTube requires sign-in/bot confirmation. Will try local browser-cookie based extraction next.

## 2026-05-12 YouTube auth work
- User asked to solve the repeated YouTube login challenge fundamentally before continuing note generation.
- Confirmed yt-dlp is current (`2026.03.17`) and configured only with `--js-runtimes node`.
- Confirmed no ordinary browser profiles exist for `--cookies-from-browser`; found cached Playwright Chromium, which can be used to create a reusable authenticated profile.

- Installed `bgutil-ytdlp-pot-provider==1.3.1`.
- Installed then corrected `curl_cffi` to `0.14.0`; `yt-dlp --list-impersonate-targets` now shows Chrome/Safari/Firefox targets via curl_cffi.
- Verified plugin loading: `yt-dlp` reports `PO Token Providers: bgutil:http-1.3.1`.
- Remaining auth issue at this point: local bgutil HTTP server is not yet running, so tokens cannot be generated.

- User completed Google device-code OAuth authorization. Token cache was saved successfully.
- Continuing diagnosis because extraction now fails at a post-auth YouTube API HTTP 400, not at the earlier sign-in challenge.

- Added `tools/scripts/youtube_auth_check.sh` and expanded `.gitignore` for YouTube cookie files.
- OAuth was authorized but proved insufficient for actual media formats on this host; cookie-based YouTube account auth is now the required next input.

- Authenticated YouTube format listing succeeded after adding `--remote-components ejs:github`; real audio/video formats became available.
- Downloaded and merged the original 4K video to `youtube/ttkd0t5qTD4/original.mkv`; downloaded subtitle SRT files, thumbnail, and info JSON.
- Moving to transcript cleaning, frame extraction, TeX writing, PDF compilation, and visual QA.

- Completed `ttkd0t5qTD4` note generation: wrote TeX, compiled PDF, ran quality, coverage, log scan, diff whitespace check, and visual PDF QA.

## 2026-05-12 Zhang Xiaojun YouTube batch
- Started batch request for all Zhang Xiaojun YouTube interviews.
- First action: enumerate channel videos and podcast playlists, then build a deduplicated generation queue.

- Created Zhang Xiaojun YouTube batch queue files under `youtube/zhangxiaojun/`. Next canonical interview target is episode 138 (`vG1RBqn1sG4`).

- Downloaded episode 138 work media (`vG1RBqn1sG4`) as 720p `source.mp4`; YouTube reported no subtitles for requested languages, so local transcription is required.

- Stopped CPU transcription path and began GPU root-cause validation for faster-whisper/CTranslate2.

- Fixed transcription workflow to use CTranslate2 CUDA via `tools/scripts/transcribe_faster_whisper.py`. Episode 138 large-v3 GPU transcription completed in about 756 seconds with 6416 segments.

- GPU transcription root fix verified: episode 138 transcript now exists as `transcript.zh.srt/txt/json` from faster-whisper large-v3 CUDA.

## 2026-05-13 Zhang Xiaojun serial generation
- User requested serial high-standard generation for the broad AI/internet queue, newest to oldest.
- Treat EP140 as completed via `youtube/ttkd0t5qTD4`. Starting EP139 `Xxz5uh0L1mE` next. EP138 source/transcript work is preserved but paused to respect newest-to-oldest ordering.

- Episode 139 media and GPU transcript completed: `source.mp4`, `transcript.zh.srt/txt/json`, and chapter transcript split are available under `youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/`.

- Completed EP139 Agent survey note: `youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/ep139-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage passes, visual QA checked).

- Applied feedback: fixed no-slides podcast visual policy. EP139 now uses cover + concept diagrams only; repeated speaker frames were removed. Updated podcast workflow and quality script so interview notes are not incentivized to add repeated speaker frames for figure quota.

- Continuing serial Zhang Xiaojun generation with EP138 Luo Fuli (`vG1RBqn1sG4`), using existing source media and faster-whisper large-v3 CUDA transcript.

- Completed EP138 Luo Fuli note: `youtube/zhangxiaojun/ep138-vG1RBqn1sG4/ep138-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage passes, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP137 Hong Letong (`bv8ghyTFF9w`).

## 2026-05-13 CS336 workflow audit after user quality feedback
- User reported that CS336 notes have many images but still lack enough detailed prose explanation and transitions between small sections.
- Audited the workflow and sample CS336 notes. New static metrics confirmed the issue: several figure-heavy notes have low prose-per-figure and weak subsection openers despite previously scoring `⭐⭐⭐`.
- Updated `check_note_coverage.py` to detect `figure-heavy-prose-thin`, `thin-local-figure-explanations`, and `weak-section-openers`.
- Updated `check_quality.sh` to display prose-per-figure and demote figure-heavy notes below the prose-density threshold.
- Updated `AGENTS.md`, `QUALITY.md`, `docs/NOTE_GENERATION_WORKFLOW.md`, and shared video-writing rules to require prose-led flow, section bridge paragraphs, pre-figure setup, post-figure synthesis, and narrative blueprint fields.
- Added `docs/CS336_WORKFLOW_AUDIT_2026-05-13.md` with root cause, evidence, and follow-up repair plan.
- Rewrote CS336 2026 lecture12 as the first prose-led/teacher-voice sample: expanded from 29p to 32p, improved prose-per-figure from 149 to 260, added 13 teacher-voice markers, strengthened transitions between evaluation families, and passed the stricter coverage checker with no warnings.

- EP137 Hong Letong source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready. Status set to paused-ready-transcript for next serial writing step.

- Completed EP137 Hong Letong note: `youtube/zhangxiaojun/ep137-bv8ghyTFF9w/ep137-notes.pdf` (21 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP136 Guangmi LLM quarterly report (`u1Lzp-7Ybn8`).

- EP136 Guangmi source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready for survey note writing.

- Completed EP136 Guangmi quarterly report note: `youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/ep136-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP135 Tristan/Natural Selection (`x8qdqWIVVTA`).

- EP135 Tristan/Natural Selection source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready.

- Completed EP135 Tristan/Natural Selection note: `youtube/zhangxiaojun/ep135-x8qdqWIVVTA/ep135-notes.pdf` (21 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP134 Xie Chen data survey (`owjTOT14bG0`).

- EP134 Xie Chen data survey source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready.

- Completed EP134 Xie Chen data survey note: `youtube/zhangxiaojun/ep134-owjTOT14bG0/ep134-notes.pdf` (20 pages, quality ⭐⭐⭐, coverage hard checks pass, visual QA checked; cover + concept diagrams only, no repeated speaker frames).

- Continuing serial Zhang Xiaojun generation with EP133 Saining Xie marathon interview (`iiBY0fqpThI`).

- EP133 Saining Xie source media and faster-whisper large-v3 CUDA transcript completed; chapter transcript split is ready. Status set to paused-ready-transcript for next serial writing step.

- Completed EP133 Saining Xie marathon interview note: `youtube/zhangxiaojun/ep133-iiBY0fqpThI/ep133-notes.pdf` (23 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=10 boxes=30 term_digest=4 summaries=15`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP132 Gao Jiyang / Xinghaitu (`n4_c_HsodPg`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is running.

- Completed EP132 Gao Jiyang / Xinghaitu note: `youtube/zhangxiaojun/ep132-n4_c_HsodPg/ep132-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=8 boxes=28 term_digest=5 summaries=14`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP130 Zhang Yueguang / Muyan Zhiyu (`ruVJ_5dObxs`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is running.

- Completed EP130 Zhang Yueguang / Muyan Zhiyu note: `youtube/zhangxiaojun/ep130-ruVJ_5dObxs/ep130-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=9 boxes=26 term_digest=3 summaries=15`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).

- Fixed Zhang Xiaojun concept-figure rendering style after user reported tofu-box glyphs in EP133: added `tools/scripts/render_zhangxiaojun_concept_figures.py`, switched generated diagrams to a Chinese+Latin-safe AR PL font, simplified diagrams to sparse teaching cards, regenerated 60 figures across EP130/132/133/134/135/136/137/138/139, recompiled those PDFs, re-rendered visual QA, and rechecked whitespace.

- Completed EP129 Zhang Peng / Zhipu note: `youtube/zhangxiaojun/ep129-9zSMTUUEfmU/ep129-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=10 boxes=27 term_digest=2 summaries=14`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP128 Manus / Ji Yichao Peak (`MW-ezf2RhVg`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is starting.

- Completed EP128 Manus / Ji Yichao Peak note: `youtube/zhangxiaojun/ep128-MW-ezf2RhVg/ep128-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check passes with `figs=9 readfig=8 boxes=28 term_digest=3 summaries=13`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).

- Continuing serial Zhang Xiaojun generation with EP127 LLM quarterly report cross-year conversation (`SG90aehV3vU`): downloaded 720p work video, cover, and metadata. YouTube has no subtitles; faster-whisper large-v3 CUDA transcription is starting.

- Completed EP127 Guangmi cross-year LLM quarterly report note: `youtube/zhangxiaojun/ep127-SG90aehV3vU/ep127-notes.pdf` (26 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=11 boxes=30 term_digest=5 summaries=11`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP127 done; next AI/internet selected target is EP125 (`k82iFzvKFCQ`) because EP126 is excluded from the filtered queue.
- Fixed manifest workflow to scan `figures/` directories so generated podcast concept diagrams are recorded as local visual assets.

- Completed EP125 Freda / Altimeter note: `youtube/zhangxiaojun/ep125-k82iFzvKFCQ/ep125-notes.pdf` (28 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=12 boxes=33 term_digest=5 summaries=14`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP125 done; next AI/internet selected target is EP123 (`qZbzFZ2R_Nw`) because EP124 and EP126 are excluded from the filtered queue.

- Completed EP123 ONE2X / Wang Guan note: `youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/ep123-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=25 term_digest=4 summaries=12`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP123 done; next AI/internet selected target is EP121 (`2o281Zy5aZE`) because EP122 and EP124 are excluded from the filtered queue.

- Completed EP121 DeepMind Tan Jie robotics note: `youtube/zhangxiaojun/ep121-2o281Zy5aZE/ep121-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=27 term_digest=3 summaries=10`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP121 done; next AI/internet selected target is EP120 (`40qPt8R2uys`).

- Completed EP120 Xiaopeng / Liu Xianming Physical AI note: `youtube/zhangxiaojun/ep120-40qPt8R2uys/ep120-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=9 boxes=30 term_digest=2 summaries=11`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP120 done; next AI/internet selected target is EP119 (`858HR43pegk`).

- Completed EP119 Kimi Linear / MiniMax M2 architecture survey note: `youtube/zhangxiaojun/ep119-858HR43pegk/ep119-notes.pdf` (22 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=10 boxes=30 term_digest=2 summaries=12`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP119 done; next AI/internet selected target is EP118 (`RxXVq7-sJzM`).

- Continuing serial Zhang Xiaojun generation with EP118 Li Xiang second interview (`RxXVq7-sJzM`).

- Completed EP118 Li Xiang second interview note: `youtube/zhangxiaojun/ep118-RxXVq7-sJzM/ep118-notes.pdf` (22 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=11 boxes=36 term_digest=3 summaries=11`, visual QA checked; cover + simplified generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP118 done; next AI/internet selected target is EP117 (`zrvnoYYPaWQ`).

- Continuing serial Zhang Xiaojun generation with EP117 open-source paper exploration survey (`zrvnoYYPaWQ`).

- Completed EP117 open-source paper exploration survey note: `youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/ep117-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=10 boxes=26 term_digest=3 summaries=7`, visual QA checked; YouTube static cover plus generated concept diagrams, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP117 done; next AI/internet selected target is EP116 (`khrOsS7YQn4`).

- Continuing serial Zhang Xiaojun generation with EP116 Wu Minghui 19-year history interview (`khrOsS7YQn4`).

- Completed EP116 Wu Minghui / Minglue enterprise AI note: `youtube/zhangxiaojun/ep116-khrOsS7YQn4/ep116-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=9 boxes=36 term_digest=3 summaries=7`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP116 done; next AI/internet selected target is EP115 (`gQgKkUsx5q0`).

- Continuing serial Zhang Xiaojun generation with EP115 OpenAI Yao Shunyu Agent interview (`gQgKkUsx5q0`).

- Completed EP115 OpenAI Yao Shunyu Agent research note: `youtube/zhangxiaojun/ep115-gQgKkUsx5q0/ep115-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=6 boxes=34 term_digest=4 summaries=8`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP115 done; next AI/internet selected target is EP113 (`ouG6jrkECrc`) because EP114 is excluded from the filtered AI/internet queue.

- Continuing serial Zhang Xiaojun generation with EP113 Yang Zhilin K2 / Agentic LLM interview (`ouG6jrkECrc`).

- Completed EP113 Yang Zhilin / Kimi K2 Agentic LLM note: `youtube/zhangxiaojun/ep113-ouG6jrkECrc/ep113-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=6 boxes=31 term_digest=4 summaries=7`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP113 done; next AI/internet selected target is EP112 (`6yExfoTuSWw`).

- Continuing serial Zhang Xiaojun generation with EP112 Guangmi LLM quarterly report (`6yExfoTuSWw`).

- Completed EP112 Guangmi LLM quarterly report note: `youtube/zhangxiaojun/ep112-6yExfoTuSWw/ep112-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=8 boxes=32 term_digest=1 summaries=10`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP112 done; next AI/internet selected target is EP111 (`JxEetUlV9RA`).

- Continuing serial Zhang Xiaojun generation with EP111 Li Yifan lidar entrepreneurship interview (`JxEetUlV9RA`).

- Completed EP111 Li Yifan / Hesai lidar entrepreneurship note: `youtube/zhangxiaojun/ep111-JxEetUlV9RA/ep111-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=11 boxes=33 term_digest=1 summaries=8`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP111 done; next AI/internet selected target is EP110 (`8dKBH4x0D9o`).

- Continuing serial Zhang Xiaojun generation with EP110 Kimi K2 report / ChatGPT Agent / Qwen3-Coder survey (`8dKBH4x0D9o`).

- Completed EP110 Kimi K2 / ChatGPT Agent / Qwen3-Coder technical report note: `youtube/zhangxiaojun/ep110-8dKBH4x0D9o/ep110-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=8 boxes=27 term_digest=3 summaries=9`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP110 done; next AI/internet selected target is Lovart video special (`biptonYq-ys`).

- Continuing serial Zhang Xiaojun generation with Lovart / Chen Mian video special (`biptonYq-ys`).

- Completed Lovart / Chen Mian video special note: `youtube/zhangxiaojun/special-biptonYq-ys/lovart-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=9 readfig=5 boxes=38 term_digest=2 summaries=10`, visual QA checked; cover/title-frame plus generated concept diagrams, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark `biptonYq-ys` done; next AI/internet selected target is EP109 (`pWY0HVUH8GA`).

- Completed EP109 Xie Chen / Guanglun embodied simulation and synthetic data note: `youtube/zhangxiaojun/ep109-pWY0HVUH8GA/ep109-notes.pdf` (24 pages, quality `⭐⭐⭐`, coverage check clean with `figs=11 readfig=13 boxes=33 term_digest=6 summaries=9`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP109 done; next AI/internet selected target is `Puptr04av5g` (Wang He embodied intelligence history/capital-chaos subtitle edition).

- EP106/Puptr04av5g transcription command correction: initial run used legacy --output-json/--output-srt flags; current tool requires --out-prefix. Re-running with --out-prefix.

- EP106/Puptr04av5g transcription issue: single full-video faster-whisper run stalled after writing partial output around 01:08 despite process remaining alive. Root cause likely one long/awkward decode chunk rather than CUDA failure. Switched plan to chapter-based audio chunks and merge outputs.

- EP106/Puptr04av5g transcription issue 2: per-chunk shell loop also stalled on 3-minute chunk01 during model initialization/decode. Next approach: load WhisperModel once in a custom batch script and transcribe all chapter WAV chunks in one process.

- EP106/Puptr04av5g GPU runtime anomaly: CUDA/CTranslate2 calls left unkillable processes even after SIGKILL, so switched to testing CPU int8 transcription for chapter chunks rather than continuing to use the broken CUDA path.

- EP106/Puptr04av5g CPU fallback: chunks 01--03 transcribed successfully; generated provisional chapter-transcripts.md with later chunks marked pending while CPU transcription continues.

- EP106/Puptr04av5g CPU fallback: chunks 01--04 transcribed successfully; chunk05 running. Updated chapter-transcripts.md with completed chunks and pending markers for the rest.

- EP106/Puptr04av5g CPU fallback: chunk05 completed; updated chapter-transcripts.md with chapters 01--05. Remaining chunks 06--11 still running/pending.

- EP106/Puptr04av5g CPU fallback transcription completed for all 11 chunks and merged into `transcript.zh.json/srt/txt`; preserved the earlier stalled GPU partial transcript as `.gpu-partial` files for diagnosis.

- Completed EP106/Puptr04av5g Wang He embodied intelligence subtitle edition note: `youtube/zhangxiaojun/ep106-Puptr04av5g/ep106-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=18 boxes=25 term_digest=3 summaries=9`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark `Puptr04av5g` done and original EP106 `9DnjiuN6Yg0` duplicate/covered by the subtitle edition.

- Continuing serial Zhang Xiaojun generation with nuclear-fusion interview `pVuE4J5cn98`; metadata and 360p work video downloaded. YouTube exposes no subtitles despite title marker `含字幕`; using fixed-duration CPU transcription chunks because CUDA cleanup was unreliable in the previous item.

- Completed nuclear-fusion interview note `pVuE4J5cn98`: `youtube/zhangxiaojun/special-pVuE4J5cn98/fusion-notes.pdf` (21 pages, quality `⭐⭐⭐`, coverage check clean with `figs=10 readfig=12 boxes=33 term_digest=3 summaries=9`, visual QA checked; cover + generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark `pVuE4J5cn98` done; next AI/internet selected target will be discovered from queue.

- Continuing serial Zhang Xiaojun generation with EP104 Rokid / Zhu Mingming (`qW-kgogQwJc`); metadata and 360p work video downloaded. YouTube exposes no subtitles; chapter-based CPU transcription is starting.

- EP104 CPU fallback transcription completed for all 20 fixed-duration chunks and was merged into `transcript.zh.json/srt/txt` plus `chapter-transcripts.md`.
- Completed EP104 Rokid / Zhu Mingming note: `youtube/zhangxiaojun/ep104-qW-kgogQwJc/ep104-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=9 readfig=8 boxes=33 term_digest=5 teacher_voice=7 summaries=7`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP104 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Checked next AI/internet queue item EP103 (`Xo7TxXkNsoA`) and found it is a duplicate upload of the already completed Lovart / Chen Mian video special `biptonYq-ys`: same title family, same 1h45m interview, same opening transcript and main chapter content. EP103 was transcribed locally before the duplicate was confirmed; no second note was generated. Queues were updated to mark EP103 `duplicate`, covered by `youtube/zhangxiaojun/special-biptonYq-ys/lovart-notes.tex`.

- Completed EP102 Zhang Xiangyu multimodal research note: `youtube/zhangxiaojun/ep102-vWrYHvSRz0s/ep102-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=26 term_digest=6 teacher_voice=4 summaries=8`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP102 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Completed EP101 YouWare / Ming Chaoping Agent application entrepreneurship note: `youtube/zhangxiaojun/ep101-a04POJEknCY/ep101-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=14 boxes=33 term_digest=4 teacher_voice=4 summaries=9`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP101 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Completed EP100 Mercedes-Benz / Ola Källenius transformation note: `youtube/zhangxiaojun/ep100-9Yjws_rt378/ep100-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=9 readfig=8 boxes=27 term_digest=4 teacher_voice=4 summaries=6`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP100 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.

- Checked next AI/internet queue item EP99 (`aoaSwGAJW6M`) and found it is covered by the already completed nuclear-fusion subtitle edition `pVuE4J5cn98`: same guest/topic/title family. No second note generated. Queues were updated to mark EP99 `duplicate`, covered by `youtube/zhangxiaojun/special-pVuE4J5cn98/fusion-notes.tex`.

- Started VLA paper-survey投屏版 `eiQFomOuCJs`: metadata, cover, 1080p work video, 34 chapter-aligned slide/frame candidates, and contact sheet were acquired under `youtube/zhangxiaojun/special-eiQFomOuCJs/`.
- VLA paper-survey CPU fallback transcription completed for all 22 fixed-duration chunks and was merged into `transcript.zh.json/srt/txt` plus `chapter-transcripts.md` (4215 segments). Next step is to write the slide/frame-backed VLA course note.
- Completed VLA paper-survey投屏版 `eiQFomOuCJs`: `youtube/zhangxiaojun/special-eiQFomOuCJs/vla-notes.pdf` (24 pages, quality `⭐⭐⭐`, coverage check clean with `figs=26 readfig=17 boxes=23 term_digest=1 teacher_voice=1 summaries=6`, visual QA checked; real投屏 frames used as visual spine).
- Updated Zhang Xiaojun queues to mark `eiQFomOuCJs` done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Checked next AI/internet queue item EP98 (`3jI6F3M2ocU`) and confirmed it is the same VLA paper-survey content as the completed投屏版 `eiQFomOuCJs`: same duration, upload date, 34 chapter titles/timestamps, and description storyline. Queues were updated to mark EP98 `duplicate`, covered by `youtube/zhangxiaojun/special-eiQFomOuCJs/vla-notes.tex`.
- Started EP97 `YshXmh_q_Q4` Q1 2025 large-model quarterly review: metadata, cover, description, and 360p work video downloaded; YouTube exposes no subtitles or auto captions. Audio was split into 16 fixed-duration chunks and CPU int8 transcription is in progress.
- Completed EP97 Q1 2025 large-model quarterly review note: `youtube/zhangxiaojun/ep97-YshXmh_q_Q4/ep97-notes.pdf` (26 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=43 term_digest=5 teacher_voice=8 summaries=12`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP97 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Started EP96 `qtugoE1xQZk` autonomous-driving interview: metadata, cover, and description downloaded. YouTube exposes no subtitles or auto captions; queue status set to `in_progress`.
- Completed EP96 Lang Xianpeng autonomous-driving technical interview note: `youtube/zhangxiaojun/ep96-qtugoE1xQZk/ep96-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=13 readfig=12 boxes=30 term_digest=7 teacher_voice=7 summaries=7`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP96 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
- Started EP95 `VdWEE6vOYRw` Manus founder Xiao Hong interview: metadata, cover, and description downloaded. It is distinct from EP128 Peak/Manus final interview; YouTube exposes no subtitles or auto captions; queue status set to `in_progress`.
- Completed EP95 Manus founder Xiao Hong interview note: `youtube/zhangxiaojun/ep95-VdWEE6vOYRw/ep95-notes.pdf` (20 pages, quality `⭐⭐⭐`, coverage check clean with `figs=12 readfig=10 boxes=33 term_digest=4 teacher_voice=6 summaries=8`, visual QA checked; cover plus generated concept diagrams only, no repeated body speaker frames).
- Updated Zhang Xiaojun queues to mark EP95 done; next AI/internet selected target should be discovered from `ai-internet-queue.json`.
