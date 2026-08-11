# Lecture 08 Coverage Matrix

Status: second-round slide-complete rewrite completed on 2026-08-11.

Source deck: `lecture08-slides.pdf`, 73 pages. All 73 pages now appear in lecture order. Title, goals, section maps and recap pages are retained because they define the dependency structure, engineering objectives or configuration rules used by the surrounding prose.

Verification evidence:

- Verification evidence is regenerated after the second-round compilation and visual QA.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| slides 001--003 | title/goals/organization | yes | 本讲主线 | Every screenshot included; goals and dependency order explained before the terms map. | complete |
| slides 004--013 | networking basics | yes | Part 1 | Every screenshot included; compute/memory walls, intra/inter-node domains, collectives, topology and recap unpacked. | complete |
| slides 014--031 | data parallel and ZeRO/FSDP | yes | Part 2 | Every screenshot included; state ownership, lifecycle, communication and memory accounting explained stage by stage. | complete |
| slides 032--038 | pipeline parallel | yes | Part 2 | Every screenshot included; layer-wise idle time, microbatch bubbles, batch dependence and scheduling trade-offs explained. | complete |
| slides 039--049 | tensor and sequence parallel | yes | Part 2 | Every screenshot included; row/column TP, communication placement, activation lower bound and SP motivation explained. | complete |
| slides 050--056 | expert/context parallel and summary table | yes | Part 2 | Every screenshot included; EP routing, attention/expert decoupling, CP and batch coupling explained. | complete |
| slides 057--062 | 3D/4D composition and scaling evidence | yes | Part 3 | Every screenshot included; rules, Megatron recommendations, Narayanan scaling, TP=8 and recomputation interpreted. | complete |
| slides 063--073 | recent-model configurations and recap | yes | Part 3 | Every model page included; each configuration is read as a memory/network/topology consequence rather than a recipe to copy. | complete |
| teacher voice | not available | no | whole note | No subtitles, transcript, executable text nodes or speaker notes are present in the lecture directory. | not applicable |
| PDF visual QA | QA | yes | `qa/lecture08-notes/` | Regenerated 55-page contact sheet; full sheet plus pages 4/18/31/43/51/55 inspected; checklist signed. | complete |
