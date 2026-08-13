# Lecture 15 Writing Blueprint

## Teaching Thesis

The lecture proposes a 2023 robotics-foundation-model recipe rather than announcing a finished foundation model. The recipe combines high-capacity token-based architectures, external Internet-scale language/vision priors, and large diverse offline robot datasets, with language serving as the interface between skills, plans, feedback, and relabeling. RT-1, SayCan, Inner Monologue, and DIAL occupy different layers of one robot system.

## Source Boundary

- Required visual spine: 45 manually reviewed teaching states recovered from the official 1080p recording.
- Teacher voice: synthesize all major ledger rows and include at least ten explicit classroom markers.
- Historical cutoff: 2023-02-07.
- Exclude RT-2, Open X-Embodiment, PaLM-E, Gemini Robotics, and later VLA systems from reconstructed classroom evidence.
- The terms `foundation model`, `Internet-scale model`, and `LLM` are deliberately loose in the talk; the note must define and separate them where useful.

## Section Plan

1. **来源审计与课程主问题**
   - Official video, manual captions, no public standalone deck, 315-to-45 slide recovery.
   - Distinguish a recipe/hypothesis from an existence claim.
2. **为什么机器人也想要 Foundation Model**
   - Slides 1--6.
   - Emergence, homogenization, physical-data bottlenecks, and three ingredients.
3. **从 Online Robot Learning 到 Offline Recipe**
   - Slides 7--12.
   - ML scaling principles, Internet-scale models, offline datasets, BC-Z history, data generation versus consumption.
4. **RT-1：把多任务模仿学习写成实时 Transformer**
   - Slides 13--16.
   - Existing data and throughput constraints, architecture, tokenization, 3 Hz inference, six-frame history, 256 action bins.
5. **RT-1 的 Scaling 与 Generalization 证据**
   - Slides 17--22.
   - Seen/unseen, distractors/backgrounds, multi-factor variation, mixed distributions, task diversity versus size, ablations.
6. **SayCan：让 LLM 计划，但让 Affordance 决定能不能做**
   - Slides 23--29.
   - Fixed skill vocabulary, lack of grounding, score product, long-horizon results, PaLM scaling and prompting.
7. **Inner Monologue：从 Open Loop 到 Feedback-Conditioned Replanning**
   - Slides 30--35.
   - Failure case, passive/active feedback, success detector, results, common-sense import.
8. **DIAL：用 VLM 重写 Offline Dataset 的语言覆盖**
   - Slides 36--41.
   - Teleoperation economics, four-stage pipeline, semantic coverage, novel instructions, label noise and diversity caveats.
9. **系统地图、Q&A 限制与研究议程**
   - Slides 42--45 plus transcript Q&A.
   - Component map, historical timeline, low-level skill bottleneck, imitation as existence proof, context-length limit.
10. **总结与延伸**
   - Separate 2023 source facts from a labeled modern VLA interpretation.

## Planned Formal Elements

- Behavioral cloning objective over offline demonstrations.
- Autoregressive token likelihood for images, language, and discretized actions.
- Action discretization from continuous control to 256 bins.
- SayCan factorization: language usefulness times affordance probability, or addition in log space.
- Closed-loop belief/state update for Inner Monologue.
- DIAL mixed-dataset objective over human and VLM-generated language labels.
- Data scaling table distinguishing episode count, task diversity, embodiment diversity, and instruction diversity.

## Planned Code Listings

1. RT-1-style tokenized multi-task imitation training/inference loop.
2. SayCan plus Inner Monologue closed-loop planner with affordance scoring and feedback-triggered replanning.

## Figure Treatment Rules

- Each of the 45 semantic slide filenames must appear exactly once in the TeX.
- Every subsection begins with prose explaining the question before its first visual.
- Target at least 16,000 prose characters and 350+ prose characters per figure overall.
- Dense architecture, result, ablation, and pipeline slides receive explicit axis/column/diagram reading instructions and evidence limits.
- Recovered video-demo states are used only where the motion example teaches a distinct generalization or feedback mechanism.

## Acceptance Targets

- 45+ PDF pages.
- 45 required figures, 14+ teaching boxes, 6+ formulas, 2 captioned listings.
- At least ten teacher-voice markers and one terminology digestion table.
- Strict coverage with zero warnings.
- `check_quality.sh` grade `⭐⭐⭐`.
- Two-pass XeLaTeX without layout/reference/hyperref warnings.
- Canonical visual QA contact sheet reviewed and report signed.
