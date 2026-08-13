# Lecture 19 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V008 | Establish the title, physical-world failure cases, ecological learning, simulation, realistic scenes, long-horizon tasks, embodied-task taxonomy, and transition to foundation models. | Demonstrations motivate the problem; they do not prove a general-purpose home robot. | Motivation and simulation |
| V009--V015 | Explain the high-level/low-level gap, robotics scaling timeline, scaling recipe, Moravec's paradox, data scarcity, interface mismatch, and two-part roadmap. | “Scale up” remains a research hypothesis constrained by data, embodiment, and safety. | Foundation-model opportunity and bottlenecks |
| V016--V023 | Explain model consolidation, PaLM-E title/architecture, mixed task training, main model, multimodal examples, positive transfer, and real-robot results. | Positive transfer is reported for the presented task mixture and does not imply universal embodiment transfer. | PaLM-E |
| V024--V029 | Introduce RT-2, VLM semantic priors, VLM-as-policy architecture, action tokenization, co-fine-tuning data, and inference. | Tokenized actions are an interface choice; discretization and training support limit precision and OOD behavior. | RT-2 mechanism |
| V030--V036 | Cover emergent skills, aggregate results, seen/unseen categories, ablations, Language Table, chain-of-thought, and VLA summary. | Qualitative examples, average success rates, and ablations answer different questions and are not interchangeable. | RT-2 evidence |
| V037--V039 | Explain Open X-Embodiment/RT-X data mixture, cross-embodiment transfer evidence, and the part-one summary. | The lecture describes early positive-transfer signals, not language-model-level scaling maturity. | Cross-embodiment scaling |
| V040--V046 | Introduce Language to Rewards, direct-interface failures, the interface question, reward pipeline, prompt structure, MPC controller, and generated skill set. | LLMs propose reward programs; optimization and safety layers still govern physical execution. | Language to Rewards mechanism |
| V047--V055 | Explain humanoid/manipulation examples, benchmark comparison, sim-to-real pipeline, real-robot result, general pattern-machine framing, iterative improvement, final summary, and takeaway. | Demos show breadth and interface utility, not guaranteed correctness or safe autonomous deployment. | Language to Rewards evidence and synthesis |
| T001--T005 | Preserve the world-model failures, Gibson motivation, research transition, high/low distinction, and scaling caveat. | Spoken examples are paraphrased and time-bounded. | Sections 1--3 |
| T006--T010 | Preserve Moravec's paradox, data/interface bottlenecks, roadmap, PaLM-E consolidation motivation, and positive-transfer interpretation. | Model-family claims remain tied to the lecture's task mixtures. | Sections 3--4 |
| T011--T015 | Preserve RT-2's research question, action-interface caveat, co-fine-tuning rationale, multi-part evidence reading, and cautious RT-X interpretation. | No result is upgraded into universal robot generalization. | Sections 5--7 |
| T016--T018 | Preserve reward-interface motivation, controller responsibility boundary, and sequence-pattern interpretation. | Generated reward code remains subject to optimizer, simulator, hardware, and safety constraints. | Sections 8--9 |
| T019--T020 | Preserve direct-action versus reward-program Q&A, hybrid data bootstrap, persistent data bottleneck, and physical safety layers. | Future recipes and unreleased safety work remain attributed and speculative. | Sections 10--11 |

## Acceptance Evidence

- Final artifact: 48 pages, 55 recovered teaching figures, 28 teaching boxes, 11 in-note teacher-voice markers, 8 displayed formula blocks, 3 captioned listings, and 18,174 prose characters (`330` prose characters per figure).
- Every required visual asset is referenced exactly once. `check_note_coverage.py --strict` passes with zero warnings, including section bridges, terminology digestion, teacher voice, formula explanations, and manifest coverage.
- `check_quality.sh` reports `⭐⭐⭐`.
- Two stabilized XeLaTeX passes complete without overfull/underfull boxes, unresolved references, rerun requests, or hyperref warnings; only repository-standard Fandol font notices remain.
- Canonical PDF QA renders all 48 pages with no near-blank pages. The signed report records full contact-sheet review plus enlarged inspection of source tables, formulas, all three code listings, quantitative results, sim-to-real evidence, final comparison, safety synthesis, and references.
