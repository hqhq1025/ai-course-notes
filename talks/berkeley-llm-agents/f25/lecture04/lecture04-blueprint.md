# Lecture 04 Blueprint

## Teaching Question

如何设计一个可重复、有效、难以被投机的 Agent evaluation system，并把它实现为
可复用的 Green Agent benchmark 服务？

## Narrative Spine

| Unit | Slides | Required treatment |
|---|---|---|
| Evaluation foundations | 003--023 | Why/when eval, close/open, verifiable/non-verifiable, human/LLM judge, static/dynamic. |
| Agent eval taxonomy | 027--038 | Capability, application, general-set evaluation. |
| Eval validity | 040--046 | Outcome validity for text, code, state change, multi-step reasoning and failure modes. |
| Benchmark cases | 048, 050--063 | CyberGym, tau-bench/tau2, GDPval, CRMArena, LegalAgentBench. |
| Green Agent | 065, 067--071 | Roles, flow, architecture and prompt-based toolkit. |
| Project types | 072--080 | Existing benchmark integration versus new benchmark construction. |
| Build checklist | 082--088 | Task, environment, metrics, test cases and grading rubric. |
| Tau-bench implementation | 091--099, 102 | Interface, workflow, kickoff/green/white agents and integration. |

## Acceptance Targets

- 78 required pages and 26 documented optional title/build/admin pages.
- 40+ pages, 15+ boxes, 5+ terminology/reading blocks, 10+ teacher-voice markers.
- 260+ prose characters per figure, strict coverage, two-pass XeLaTeX, `⭐⭐⭐`,
  clean log and signed visual QA.
