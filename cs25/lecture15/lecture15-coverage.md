# Lecture 15 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V006 | Introduce the robotics foundation-model question, emergence/homogenization, the physical-data “last domino,” and the three-ingredient recipe. | The lecture does not claim a mature robotics foundation model already exists. | Motivation and ingredients |
| V007--V009 | Explain transferable ML-scaling design principles, external Internet-scale priors, and the move to offline robot data. | Architecture, external priors, and data regime are separate ingredients. | Three ingredients |
| V010--V012 | Reconstruct Google Brain robotics history, BC-Z/multi-task imitation, decoupled data consumption, and the combined recipe. | Multi-task imitation is an existence proof, not a final learning algorithm. | Online-to-offline history |
| V013--V016 | Present RT-1 constraints, architecture, TokenLearner compression, six-frame history, action discretization, model size, and real-time budget. | Real-time inference and dataset constraints drive the architecture. | RT-1 design |
| V017--V020 | Analyze seen/unseen robustness, multi-factor variation demos, and mixed data distributions. | Video-derived states are retained because they demonstrate distinct generalization axes. | RT-1 generalization |
| V021--V022 | Explain the data-scaling plot and architecture ablations. | Task diversity is more damaging to remove than an equal fraction of raw data; the result is specific to the reported setup. | RT-1 scaling evidence |
| V023--V026 | Introduce SayCan, the robotics timeline, fixed skill vocabulary, missing grounding, and the LLM-affordance score combination. | LLMs propose useful actions; learned affordances constrain executable actions. | SayCan mechanism |
| V027--V029 | Present long-horizon planning/execution results, grounding ablation, PaLM model scaling, CoT, and prompt improvements. | Better LLMs improve the planner without expanding the robot skill library. | SayCan results |
| V030--V035 | Show the open-loop failure, passive/active scene feedback, success detection, Inner Monologue results, and common-sense lesson. | Feedback closes planning loops but remains limited by perception and available skills. | Inner Monologue |
| V036--V041 | Explain RT-1 data cost, DIAL's four stages, semantic relabeling, novel-instruction evaluation, and takeaways on diversity/noise. | The lecture reports more than 60 novel instructions but not a complete compositional-generalization law. | DIAL |
| V042--V045 | Synthesize the component map, 2016--2023 progression, public projects, and closing demo. | Later VLA systems are excluded from classroom facts. | Synthesis and conclusion |
| T001--T047 | Weave exploratory framing, data economics, architecture constraints, uncertainty, Q&A bottlenecks, and context limits into prose and boxes. | Spoken claims are paraphrased and time-bounded; speculation is labeled. | Across all sections |

## Acceptance Evidence

- Final artifact: 48 pages, 45 full-width teaching figures, 29 teaching boxes, 12 in-note teacher-voice markers, 6 displayed formula blocks, 2 captioned listings, and 18,626 prose characters (`413` prose characters per figure).
- `check_note_coverage.py --strict` passes with zero warnings; all required visual and transcript nodes have a planned and implemented teaching treatment.
- `check_quality.sh` reports `⭐⭐⭐`.
- Two stabilized XeLaTeX passes complete without overfull/underfull boxes, unresolved references, rerun requests, or hyperref warnings; only repository-standard Fandol font notices remain.
- Canonical PDF QA renders all 48 pages with no near-blank pages. The signed report records contact-sheet review and enlarged inspection of RT-1, SayCan, Inner Monologue, DIAL, summary-table, and final self-check pages.
