# CS336 Workflow Audit: Figure-Heavy But Prose-Thin Notes

Date: 2026-05-13

## Trigger

User review found that the regenerated CS336 notes contain many images, but many parts still lack detailed explanatory prose and transitions between small sections. This is a workflow failure, not just a local writing issue.

## Root Cause

The previous workflow over-optimized for:

- slide-complete visual coverage;
- presence of `读图` boxes;
- page count, figure count, and box count;
- visual PDF QA.

It under-checked:

- whether figures are embedded in a coherent prose argument;
- whether a section explains the problem before showing a figure;
- whether there is enough local explanation near each dense visual;
- whether subsections transition from one idea to the next;
- whether a figure cluster is synthesized into a teaching conclusion.

As a result, a note could receive `⭐⭐⭐` while reading too much like a screenshot album.

## Evidence From Static Audit

After adding prose-density checks, several CS336 notes that previously scored `⭐⭐⭐` are now correctly flagged as prose-thin:

| Lecture | Main symptom |
|---|---|
| lecture03 | 68 figures, low prose per figure, multiple thin local explanations |
| lecture04 | 61 figures, prose per figure below threshold |
| lecture05 | 56 figures, prose per figure below threshold |
| lecture08 | 74 figures, prose per figure below threshold, weak section openers |
| lecture09 | 58 figures, prose per figure below threshold |
| lecture10 | 29 figures, borderline prose density and several thin local explanations |
| lecture11 | 59 figures, prose per figure below threshold |
| lecture12 | 44 figures, prose per figure below threshold and multiple thin local explanations |

The new checks intentionally demote these from `⭐⭐⭐` until the prose and transitions are strengthened.

## Workflow Fixes Implemented

### 1. Prose-led generation is now mandatory

Updated `AGENTS.md`, `QUALITY.md`, `docs/NOTE_GENERATION_WORKFLOW.md`, and the shared video writing rules to require:

- a bridge paragraph before figures/tables/formulas/code in non-summary sections;
- a section-level narrative question;
- transition-in and transition-out in blueprints;
- post-figure synthesis paragraphs;
- grouping slide pages into teaching units, not treating slides as the section structure.

### 2. New prose-density gate

Added `prose/fig` checks:

- figure-heavy CS336-style notes should target at least about 260 prose characters per figure, excluding captions and LaTeX boilerplate;
- dense figures should have about 220+ prose characters nearby;
- failing this gate produces `figure-heavy-prose-thin` or `thin-local-figure-explanations`.

### 3. New transition checks

`check_note_coverage.py` now flags `weak-section-openers` when a section/subsection:

- starts directly with a figure/table/formula/code block;
- has too little opener prose;
- lacks bridge language connecting it to surrounding sections.

### 4. Quality score is stricter

`check_quality.sh` now includes prose-per-figure in its report and prevents figure-heavy notes with insufficient prose density from receiving `⭐⭐⭐`.

## New Acceptance Rule

A slide-complete note is not acceptable if it is only image-complete. It must be:

1. source-complete,
2. prose-complete,
3. transition-complete,
4. figure-explanation-complete,
5. visually readable after PDF QA.

## Follow-Up Repair Plan

The next repair pass should prioritize existing CS336 notes now flagged by the stricter checker:

1. lecture08, lecture09, lecture11, lecture12: highest figure density and weakest prose-per-figure.
2. lecture03, lecture04, lecture05: slide-complete but still too compressed around visuals.
3. lecture10: borderline; add bridge paragraphs and local explanations around inference figures.

For each lecture, fix by rewriting section narratives, not by adding decorative boxes. The desired pattern is:

```text
section question -> prose explanation -> figure -> read-the-figure -> synthesis -> next section bridge
```
