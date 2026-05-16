# Note Generation Workflow

This workflow is the required process for new high-quality notes and for major rewrites of old notes. It exists to prevent thin summaries and patchwork fixes.

For long-form podcasts, interviews, roundtables, and mixed YouTube playlist
batches, also follow `docs/PODCAST_INTERVIEW_WORKFLOW.md`. Those sources need
extra queueing, deduplication, transcription, and storage rules before normal
note generation begins.

## Goal

Move quality checks to the beginning of the process. A note should not be written directly from raw slides/transcripts. It should be built from a manifest, a coverage matrix, a blueprint, and a QA report.

## Phase 1: Source Packet

Collect all source material into the lecture directory:

- official slides or executable lecture source
- subtitle/transcript, if available
- cover image
- local copies of every referenced image
- rendered slide pages under `slides-images/` when a PDF deck exists

For podcast/interview batches, first build or update the series queue
(`queue.json` and `QUEUE.md`), classify each item, choose the canonical upload,
and decide whether to retain full video, work video, audio only, or no media
after generation.

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
- Optional transcript / executable-source `text(...)` nodes must be sampled and synthesized as teacher voice. They are not all required verbatim, but the instructor's motivations, caveats, examples, and transitions must appear in the note.
- Create a teacher-voice ledger for lectures with subtitles/transcripts/executable text nodes:

| Source / time | Spoken point | Teaching value | Note location |
|---|---|---|---|
| transcript 00:12:40 | why this metric is misleading | warning/caveat | Evaluation section |
| py-083 text | practical reason for GQA | engineering intuition | Inference section |

- Dense figures require `读图`.
- Dense terminology clusters require a table or concept box.
- Any first use of systems/resource-accounting terms requires a local definition. This includes sharding, fused kernel, collectives, ZeRO, optimizer state, activation checkpointing, DRAM/SRAM/HBM, and perplexity.
- Foundational concepts require diagram/table/formula scaffolding.

## Phase 3: Blueprint

Write `lectureXX-blueprint.md` before TeX.

For each section, specify:

- learning objective
- narrative question: what problem this section answers
- transition in: how this section follows from the previous section
- transition out: what question it leaves for the next section
- teacher voice points to preserve: motivation, caveat, verbal example, practical heuristic, or transition
- source nodes covered
- required figures and their explanations
- required first-use glossary entries
- required formulas and symbol explanations
- required terminology table
- worked examples
- warning boxes
- section summary

Do not write the final TeX until the blueprint covers the manifest.

The blueprint must be prose-led, not figure-led. Do not plan a section as a list
of slides. Group source slides into teaching units with a clear argument:

```text
Question -> mechanism -> visual evidence -> interpretation -> implication
```

For example, "slides 021-027" is not a section plan. A valid plan says:
"Explain why ZeRO-1/2 are nearly communication-free relative to DDP, then use
slides 021-027 as evidence for the state/communication ledger."

For executable lecture sources, the manifest may contain many optional `text(...)` nodes. Required nodes are section headings and figures by default. Optional nodes should still inform the blueprint, but they do not all need verbatim coverage.

Do not let slides override the instructor. Slides provide visual evidence; the transcript/source text provides the teaching voice. When the two differ in emphasis, the note should explain the slide through the instructor's spoken framing.

## Phase 4: Section Writing

Write one section at a time. Each section should include the relevant source nodes and satisfy the local contract:

- bridge paragraph before the first figure/table/formula/code
- narrative explanation that would still make sense if figures were hidden
- prose explanation
- figure(s), if source material contains teaching visuals
- `读图` boxes for important figures
- post-figure synthesis paragraph that connects the figure back to the section argument
- terminology digestion for term clusters
- formula derivations and symbol explanations
- code listings with captions
- `本章小结`

This prevents the note from becoming a thin summary that needs patching later.

Figure-heavy lectures must meet a prose-density gate. As a heuristic, CS336-style
notes should have roughly 260+ prose characters per figure on average and dense
figures should have 220+ prose characters nearby. If the note fails this gate,
do not add more figures; add explanation, merge figure clusters into teaching
units, or remove low-value screenshots.

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

The coverage checker also flags:

- `figure-heavy-prose-thin`: too little explanatory prose for the number of figures;
- `thin-local-figure-explanations`: too many figures without enough nearby explanation;
- `weak-section-openers`: sections or subsections that begin with a figure/table or lack a bridge paragraph.
- `teacher-voice-underrepresented`: many optional transcript/source text nodes exist, but the note contains too few markers or sections preserving spoken teaching points.

These warnings should usually trigger a rewrite of the section narrative, not
just insertion of source-marker comments.

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

For podcast/interview items, see `docs/PODCAST_INTERVIEW_WORKFLOW.md` for the
expected queue fields, transcript artifacts, and cleanup policy.

## Definition of Done

- Manifest exists.
- Coverage matrix or equivalent planning section covers required nodes.
- Blueprint exists for major rewrites.
- All required source visuals are included or intentionally omitted.
- Important figures have read-the-figure explanations.
- Figure-heavy notes pass prose-density and local-figure-explanation checks.
- Non-summary sections have bridge paragraphs before figures/tables/formulas.
- Sections read as connected teaching units, not isolated slide captions.
- Teacher voice from transcript/source text is represented in the note.
- Dense terminology is digested.
- Formulas have symbol explanations.
- PDF compiles without LaTeX errors, rerun warnings, or overfull boxes.
- Visual PDF QA is complete.
- `tools/scripts/check_quality.sh` reports `⭐⭐⭐` for CS336-style course notes.
