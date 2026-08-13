# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs153/lecture10`

## Files

- `cover.jpg`
- `lecture10-blueprint.md`
- `lecture10-coverage.md`
- `lecture10-diagrams.py`
- `lecture10-notes.tex`
- `lecture10-teacher-voice-ledger.md`
- `lecture10.srt`

## Supplementary Source Materials

- `source-materials/SOURCES.md`

## Local Visual Assets

- `images/01-scaling-program.png`
- `images/02-scaling-hypothesis.png`
- `images/03-scaling-law-fit.png`
- `images/04-compute-allocation.png`
- `images/05-training-failure-domains.png`
- `images/06-training-observability.png`
- `images/07-checkpoint-recovery.png`
- `images/08-follow-the-sun.png`
- `images/09-rlhf-pipeline.png`
- `images/10-constitutional-ai.png`
- `images/11-evaluation-stack.png`
- `images/12-capability-safeguards.png`
- `images/13-defense-in-depth.png`
- `images/14-interpretability-loop.png`
- `images/15-compute-lifecycle.png`
- `images/16-chat-to-api.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | `lecture10-diagrams.py` | images/01-scaling-program.png |
| V002 | figure | yes | `lecture10-diagrams.py` | images/02-scaling-hypothesis.png |
| V003 | figure | yes | `lecture10-diagrams.py` | images/03-scaling-law-fit.png |
| V004 | figure | yes | `lecture10-diagrams.py` | images/04-compute-allocation.png |
| V005 | figure | yes | `lecture10-diagrams.py` | images/05-training-failure-domains.png |
| V006 | figure | yes | `lecture10-diagrams.py` | images/06-training-observability.png |
| V007 | figure | yes | `lecture10-diagrams.py` | images/07-checkpoint-recovery.png |
| V008 | figure | yes | `lecture10-diagrams.py` | images/08-follow-the-sun.png |
| V009 | figure | yes | `lecture10-diagrams.py` | images/09-rlhf-pipeline.png |
| V010 | figure | yes | `lecture10-diagrams.py` | images/10-constitutional-ai.png |
| V011 | figure | yes | `lecture10-diagrams.py` | images/11-evaluation-stack.png |
| V012 | figure | yes | `lecture10-diagrams.py` | images/12-capability-safeguards.png |
| V013 | figure | yes | `lecture10-diagrams.py` | images/13-defense-in-depth.png |
| V014 | figure | yes | `lecture10-diagrams.py` | images/14-interpretability-loop.png |
| V015 | figure | yes | `lecture10-diagrams.py` | images/15-compute-lifecycle.png |
| V016 | figure | yes | `lecture10-diagrams.py` | images/16-chat-to-api.png |
| T001 | text | optional | `lecture10.srt 00:00--01:00` | Rapid demand growth creates scaling and reliability pressure. |
| T002 | text | optional | `lecture10.srt 01:00--03:20` | ImageNet changed AI from academic promise to practical signal. |
| T003 | text | optional | `lecture10.srt 03:00--05:40` | GPT-2 suggested the path and GPT-3 tested the scaling hypothesis. |
| T004 | text | optional | `lecture10.srt 05:20--08:30` | Anthropic aimed to make safety central while continuing frontier work. |
| T005 | text | optional | `lecture10.srt 06:20--11:50` | Scaling skepticism mixed prior sigmoids, under-scaled examples and economics. |
| T006 | text | optional | `lecture10.srt 12:00--15:20` | Researchers and engineers co-design experiments and compute multipliers. |
| T007 | text | optional | `lecture10.srt 15:00--17:20` | Distributed workers, network and storage make rare failures routine. |
| T008 | text | optional | `lecture10.srt 17:20--20:10` | Loss spikes require continuous monitoring, rollback and ownership. |
| T009 | text | optional | `lecture10.srt 19:00--21:20` | Follow-the-sun helps but handoffs remain difficult. |
| T010 | text | optional | `lecture10.srt 21:00--26:20` | Early Claude combined pre-training, RLHF and product feedback. |
| T011 | text | optional | `lecture10.srt 26:00--27:40` | Constitutional AI scales supervision through principles and AI feedback. |
| T012 | text | optional | `lecture10.srt 27:30--30:40` | Evaluation depends on task setup, elicitation and reproducibility. |
| T013 | text | optional | `lecture10.srt 29:00--33:20` | Historical AI Safety Levels linked capabilities to safeguards. |
| T014 | text | optional | `lecture10.srt 34:40--36:50` | Pre-training, post-training and inference scaling are complementary. |
| T015 | text | optional | `lecture10.srt 37:00--39:10` | Defense in depth and interpretability provide different safety evidence. |
| T016 | text | optional | `lecture10.srt 39:00--41:56` | Chat moves quickly while APIs become long-lived contracts. |

## Existing Note

- `lecture10-notes.tex`

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
