# Lecture 19 Rewrite Blueprint

## Source Boundary

- Canonical video: Stanford Online `fz8wf9hN20c`, classroom date 2023-10-10.
- Visual spine: 55 selected teaching states in `slides-images/`, each used exactly once.
- Spoken spine: 20 teacher-voice intervals in `lecture19-teacher-voice-ledger.md`.
- Research boundary: PaLM-E, RT-1, RT-2, Open X-Embodiment/RT-X, Language Table, and Language to Rewards as presented or referenced in the 2023 lecture.

## Teaching Sequence

1. **Source audit and lecture contract**
   - Correct metadata, two-part structure, evidence hierarchy, and legacy-note limitations.
2. **Why embodied intelligence is hard**
   - Consequence prediction, world models, Gibson's ecological framing, simulation, realistic scenes, long-horizon tasks.
3. **Foundation models meet robotics**
   - Internet AI versus embodied AI, high-level reasoning versus low-level control, scaling timeline, Moravec's paradox, data and interface bottlenecks.
4. **PaLM-E: model consolidation**
   - Sensor-token injection, multimodal task mixture, generalist examples, positive transfer, real-robot results.
5. **RT-2: from VLM to VLA**
   - VLM prior, robot-policy architecture, action discretization/tokenization, co-fine-tuning, inference.
6. **RT-2 evidence and limits**
   - Emergent skills, quantitative categories, ablations, Language Table, chain-of-thought, what each result does and does not establish.
7. **Cross-embodiment scaling**
   - Open X-Embodiment/RT-X data mixture, positive transfer, “signs of life” versus language-model-scale maturity.
8. **Language to Rewards**
   - Why direct action/code generation is brittle, reward as interface, reward translator, motion controller/MPC, user iteration.
9. **Language-to-Rewards evidence**
   - Simulated skills, baseline comparison, sim-to-real, real-robot manipulation, sequence transformation/completion/improvement.
10. **Two interfaces, one systems view**
    - Direct action tokens versus reward programs, hybrid data-bootstrap/distillation recipe, data bottleneck, safety layers.
11. **总结与延伸**
    - Consolidate the lecture into model, data, interface, controller, evaluation, and safety decisions.

## Required Scaffolding

- First-use glossary for embodied intelligence, world model, affordance, low-level control, policy, trajectory, action token, co-fine-tuning, positive transfer, MPC, reward function, sim-to-real, and VLA.
- Formula chain for autoregressive action tokens, mixed co-fine-tuning objective, reward-conditioned control, and receding-horizon MPC.
- Three captioned listings:
  1. action discretization and token decoding;
  2. mixed web/robot co-fine-tuning sampler;
  3. reward-code generation plus MPC execution loop.
- Dense-term tables for PaLM-E/RT-1/RT-2/RT-X and for direct-action/reward-program interfaces.
- At least 10 explicit `\teachervoice{}` blocks woven into normal sections.
- Every non-summary section/subsection opens with a prose bridge before figures, formulas, tables, or code.

## Visual Treatment

- Each of V001--V055 appears exactly once.
- Video-bearing slides use one representative complete state; repeated playback frames are intentionally omitted.
- Result slides receive local “读图” explanations covering axes/categories/baselines, first comparison, key trend, claim supported, and claim not supported.
- The final note targets at least 14,300 prose characters (`260` per figure), 20+ pages, 16+ teaching boxes, 8+ formula blocks, and `⭐⭐⭐` quality.
