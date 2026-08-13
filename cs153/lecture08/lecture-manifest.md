# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs153/lecture08`

## Files

- `cover.jpg`
- `lecture08-blueprint.md`
- `lecture08-coverage.md`
- `lecture08-diagrams.py`
- `lecture08-notes.tex`
- `lecture08-teacher-voice-ledger.md`
- `lecture08.srt`

## Supplementary Source Materials

- `source-materials/SOURCES.md`

## Local Visual Assets

- `images/01-response-pipeline.png`
- `images/02-scale-funnel.png`
- `images/03-hash-matching.png`
- `images/04-predictive-classifier.png`
- `images/05-moderator-triage.png`
- `images/06-trusted-data.png`
- `images/07-genai-threat-surface.png`
- `images/08-safety-lifecycle.png`
- `images/09-platform-integration.png`
- `images/10-evaluation-queue.png`
- `images/11-privacy-layers.png`
- `images/12-text-risk.png`
- `images/13-network-analysis.png`
- `images/14-prevention-ladder.png`
- `images/15-startup-maturity.png`
- `images/16-ecosystem-roles.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | `lecture08-diagrams.py` | images/01-response-pipeline.png |
| V002 | figure | yes | `lecture08-diagrams.py` | images/02-scale-funnel.png |
| V003 | figure | yes | `lecture08-diagrams.py` | images/03-hash-matching.png |
| V004 | figure | yes | `lecture08-diagrams.py` | images/04-predictive-classifier.png |
| V005 | figure | yes | `lecture08-diagrams.py` | images/05-moderator-triage.png |
| V006 | figure | yes | `lecture08-diagrams.py` | images/06-trusted-data.png |
| V007 | figure | yes | `lecture08-diagrams.py` | images/07-genai-threat-surface.png |
| V008 | figure | yes | `lecture08-diagrams.py` | images/08-safety-lifecycle.png |
| V009 | figure | yes | `lecture08-diagrams.py` | images/09-platform-integration.png |
| V010 | figure | yes | `lecture08-diagrams.py` | images/10-evaluation-queue.png |
| V011 | figure | yes | `lecture08-diagrams.py` | images/11-privacy-layers.png |
| V012 | figure | yes | `lecture08-diagrams.py` | images/12-text-risk.png |
| V013 | figure | yes | `lecture08-diagrams.py` | images/13-network-analysis.png |
| V014 | figure | yes | `lecture08-diagrams.py` | images/14-prevention-ladder.png |
| V015 | figure | yes | `lecture08-diagrams.py` | images/15-startup-maturity.png |
| V016 | figure | yes | `lecture08-diagrams.py` | images/16-ecosystem-roles.png |
| T001 | text | optional | `lecture08.srt 00:00--03:20` | Thorn frames growth as a systems and reporting-capacity problem. |
| T002 | text | optional | `lecture08.srt 03:20--05:50` | Platforms detect, remove and report while investigators need prioritization. |
| T003 | text | optional | `lecture08.srt 05:10--06:00` | Known-content hash matching is the first scalable intervention. |
| T004 | text | optional | `lecture08.srt 05:45--10:20` | Generative AI changes the threat surface and creates novel objects. |
| T005 | text | optional | `lecture08.srt 10:10--13:40` | Predictive detection extends coverage beyond known reference hashes. |
| T006 | text | optional | `lecture08.srt 13:40--16:20` | Review tooling should reduce unnecessary moderator exposure. |
| T007 | text | optional | `lecture08.srt 16:20--20:30` | Trusted institutional data access requires exceptional governance. |
| T008 | text | optional | `lecture08.srt 20:30--24:10` | Generative-AI companies need controls across the lifecycle. |
| T009 | text | optional | `lecture08.srt 24:10--26:20` | Standards and red teaming make safety practice repeatable. |
| T010 | text | optional | `lecture08.srt 26:20--28:40` | Product, legal and reputational incentives persist across policy changes. |
| T011 | text | optional | `lecture08.srt 28:40--31:10` | Encryption and privacy are real design constraints. |
| T012 | text | optional | `lecture08.srt 31:10--32:50` | Text signals can help earlier but remain probabilistic. |
| T013 | text | optional | `lecture08.srt 31:50--33:10` | Network patterns expose coordinated behavior beyond isolated accounts. |
| T014 | text | optional | `lecture08.srt 33:10--35:30` | Prevention also requires education and user awareness. |
| T015 | text | optional | `lecture08.srt 35:20--37:20` | Startups face safety risk before they have mature teams or budgets. |
| T016 | text | optional | `lecture08.srt 37:10--37:53` | Platforms own action; investigators identify victims and pursue cases. |

## Existing Note

- `lecture08-notes.tex`

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
