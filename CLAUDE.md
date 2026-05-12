# AI Course Notes — Claude Compatibility Guide

This file is a thin compatibility entrypoint for Claude Code. The project-wide agent instructions live in `AGENTS.md`; follow `AGENTS.md` as the source of truth.

## Read First

Before generating, editing, reviewing, or committing notes:

1. Read `AGENTS.md`.
2. Follow `QUALITY.md` for acceptance criteria.
3. For video/PDF note generation, also follow `tools/skills/video-render-common/writing-and-figures.md`.

## Claude-Specific Notes

- Claude Code automatically discovers `CLAUDE.md`, so this file exists to route Claude to the shared `AGENTS.md` rules.
- Do not duplicate long project rules here; update `AGENTS.md` when a rule should apply to all agents.
- If a local-only Claude preference is needed, use `.claude.local.md` and keep it out of git.

## Most Important Current Writing Rules

- Important figures need detailed `读图` explanations, not just captions.
- If official slides or visible video slides exist, include every teaching slide screenshot and explain each one; do not only sample representative slides.
- Dense terminology lists need concentrated glossary-style tables or concept boxes.
- Foundational background concepts should be scaffolded with diagrams/tables/formulas plus concise explanatory boxes.
- Generated notes must compile with XeLaTeX and pass `tools/scripts/check_quality.sh`.
- After compiling, render and inspect the PDF pages/contact sheet; fix visual layout/rendering issues before reporting completion.
