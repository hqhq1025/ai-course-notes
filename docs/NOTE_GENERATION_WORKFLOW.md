# Note Generation Workflow

This workflow is the required process for new high-quality notes and for major rewrites of old notes. It exists to prevent thin summaries and patchwork fixes.

## Goal

Move quality checks to the beginning of the process. A note should not be written directly from raw slides/transcripts. It should be built from a manifest, a coverage matrix, a blueprint, and a QA report.

## Phase 1: Source Packet

Collect all source material into the lecture directory:

- official slides or executable lecture source
- subtitle/transcript, if available
- cover image
- local copies of every referenced image
- rendered slide pages under `slides-images/` when a PDF deck exists

Build a manifest:

```bash
python3 tools/scripts/build_lecture_manifest.py cs336-2026/lecture01
```

The manifest lists required source nodes: slides, figures, executable lecture sections, image calls, and optional text nodes.

## Phase 2: Coverage Matrix

Before writing TeX, create a coverage matrix from the manifest. It may live in `lectureXX-coverage.md`.

Required columns:

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| slide-012 | dense figure | yes | Scaling | figure + `读图` + warning | planned |
| py-034 | terminology cluster | yes | History | glossary table | planned |
| table-resource-ledger | systems terms | yes | Systems | first-use glossary for sharding/fused kernels/collectives | planned |

Rules:

- Required visual nodes must be covered or explicitly omitted with a reason.
- Dense figures require `读图`.
- Dense terminology clusters require a table or concept box.
- Any first use of systems/resource-accounting terms requires a local definition. This includes sharding, fused kernel, collectives, ZeRO, optimizer state, activation checkpointing, DRAM/SRAM/HBM, and perplexity.
- Foundational concepts require diagram/table/formula scaffolding.

## Phase 3: Blueprint

Write `lectureXX-blueprint.md` before TeX.

For each section, specify:

- learning objective
- source nodes covered
- required figures and their explanations
- required first-use glossary entries
- required formulas and symbol explanations
- required terminology table
- worked examples
- warning boxes
- section summary

Do not write the final TeX until the blueprint covers the manifest.

For executable lecture sources, the manifest may contain many optional `text(...)` nodes. Required nodes are section headings and figures by default. Optional nodes should still inform the blueprint, but they do not all need verbatim coverage.

## Phase 4: Section Writing

Write one section at a time. Each section should include the relevant source nodes and satisfy the local contract:

- prose explanation
- figure(s), if source material contains teaching visuals
- `读图` boxes for important figures
- terminology digestion for term clusters
- formula derivations and symbol explanations
- code listings with captions
- `本章小结`

This prevents the note from becoming a thin summary that needs patching later.

## Phase 5: Automated QA

Run:

```bash
tools/scripts/check_quality.sh <lecture-dir>
python3 tools/scripts/check_note_coverage.py <lecture-notes.tex> --manifest <lecture-manifest.md>
rg -n "LaTeX Error|Undefined control sequence|Rerun to get|Overfull" <lecture-notes.log>
git diff --check
```

For strict review:

```bash
python3 tools/scripts/check_note_coverage.py <lecture-notes.tex> --manifest <lecture-manifest.md> --strict
```

The coverage checker is heuristic. It catches missing figure explanations, missing terminology digestion, missing summaries, and obvious manifest coverage gaps. If it warns because a section title was rewritten or a remote image was localized, either improve the manifest/coverage matrix or record the acceptance reason in `qa-report.md`.

## Phase 6: Visual PDF QA

Render the compiled PDF:

```bash
python3 tools/scripts/render_pdf_qa.py <lecture-notes.pdf>
```

Open the generated contact sheet and inspect suspicious pages at full size.

Fix any issue in TeX, recompile, and rerun visual QA. Do not mark the note complete with known visual problems.

## Phase 7: Final Artifacts

Each high-quality regenerated lecture should have:

```text
lectureXX/
├── lectureXX-notes.tex
├── lectureXX-notes.pdf
├── lecture-manifest.md
├── lectureXX-coverage.md       # recommended
├── lectureXX-blueprint.md      # recommended
├── qa/
│   └── lectureXX-notes/
│       ├── page-*.png
│       ├── contact.png
│       └── qa-report.md
└── images/ or slides-images/
```

## Definition of Done

- Manifest exists.
- Coverage matrix or equivalent planning section covers required nodes.
- Blueprint exists for major rewrites.
- All required source visuals are included or intentionally omitted.
- Important figures have read-the-figure explanations.
- Dense terminology is digested.
- Formulas have symbol explanations.
- PDF compiles without LaTeX errors, rerun warnings, or overfull boxes.
- Visual PDF QA is complete.
- `tools/scripts/check_quality.sh` reports `⭐⭐⭐` for CS336-style course notes.
