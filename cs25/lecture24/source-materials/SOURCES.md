# Lecture 24 Source Audit

## Official Lecture Sources

- Stanford CS25 V3 archive: `https://web.stanford.edu/class/cs25/past/cs25-v3/`
  - Schedule date: November 28, 2023.
  - Instructors: Steven Feng, Div Garg, and Karan Singh.
  - Official title: `Going Beyond LLMs: Agents, Emergent Abilities, Intermediate-Guided Reasoning, BabyLM`.
- Stanford Online recording: `https://www.youtube.com/watch?v=ylEk1TE1uBo`
  - Upload date: December 15, 2023.
  - Runtime: 1:00:13.
  - Source resolution: 1920x1080.
  - Manual `en-US` subtitle track parsed into 1,297 timed cues.

## Slide Recovery

- The Stanford archive does not expose a standalone deck for this lecture, and no instructor-hosted final deck was found during the source audit.
- The recording uses a stable full-screen slide layout with a small conferencing overlay. The recovered slide region is `1760x1000` after removing the top 80 pixels and rightmost 160 pixels.
- Three-second sampling produced 1,204 frames. Grayscale change detection retained 174 high-recall candidates; manual contact-sheet review selected 64 distinct teaching states.
- Progressive bullets use the final complete state unless an earlier slide introduces a different mechanism. Live demos retain milestones that change the task state, reveal a control boundary, or expose a failure.

## Primary Technical References

- Wei et al., `Emergent Abilities of Large Language Models`, `https://arxiv.org/abs/2206.07682`.
- Schaeffer et al., `Are Emergent Abilities of Large Language Models a Mirage?`, `https://arxiv.org/abs/2304.15004`.
- Wei et al., `Chain-of-Thought Prompting Elicits Reasoning in Large Language Models`, `https://arxiv.org/abs/2201.11903`.
- Wang et al., `Self-Consistency Improves Chain of Thought Reasoning in Language Models`, `https://arxiv.org/abs/2203.11171`.
- Zhou et al., `Least-to-Most Prompting Enables Complex Reasoning in Large Language Models`, `https://arxiv.org/abs/2205.10625`.
- Yao et al., `Tree of Thoughts`, `https://arxiv.org/abs/2305.10601`.
- Gao et al., `PAL: Program-Aided Language Models`, `https://arxiv.org/abs/2211.10435`.
- Chen et al., `Program of Thoughts Prompting`, `https://arxiv.org/abs/2211.12588`.
- Warstadt et al., `BabyLM Challenge`, `https://arxiv.org/abs/2301.11796`.
- Patil et al., `Gorilla: Large Language Model Connected with Massive APIs`, `https://arxiv.org/abs/2305.15334`.

## Evidence Boundary

- The lecture combines a source-reading survey with instructor prototypes. Claims about MultiOn booking a flight, passing a driving test, or providing a universal action API are classroom-time demonstrations and speaker claims from November 28, 2023, not current product specifications or independently reproduced benchmarks.
- `Intermediate-Guided Reasoning` is explicitly presented by the instructor as an umbrella phrase rather than an established canonical term.
- Emergence curves depend on task, prompting, model family, x-axis choice, and metric discretization. The note must preserve the classroom definition while also explaining the metric-artifact critique shown in class.
- BabyLM's child-scale data budget is a research constraint, not a claim that text-only next-token learning reproduces human development.
- The agent section is architectural and forward-looking. It must distinguish model capability, environment feedback, permissions, irreversible actions, and orchestration rather than translating 2023 prototype enthusiasm into guaranteed autonomy.

## Legacy Note Repair

- The legacy note had one cover figure, an incorrect 72-minute duration, and no recovered slide coverage.
- It invented prompt dashboards, version governance, deployment SLI/SLOs, drift rollback, data pipelines, and production checklists that are absent from the lecture.
- It omitted most of BabyLM, the emergence measurement caveat, the actual reasoning-method taxonomy, the MultiOn demos, autonomy levels, the neural-compute-unit analogy, manager-worker correction, plan divergence, and the final generalized-agent architecture.
