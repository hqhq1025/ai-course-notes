# CS25 V6 Lecture 08 — Coverage Matrix

| Required source node / concept | Source | Planned treatment |
|---|---|---|
| Language-model capability stack | slide 005; captions 00:01:20--00:02:52 | Opening recap and scaling-baseline explanation |
| Language alone is insufficient | slide 006; captions 00:02:56--00:03:33 | Central pivot and motivation paragraph |
| Digital versus physical multimodality | slide 007; captions 00:03:00--00:04:18 | Read-figure guide and native-multimodality definition |
| Native multimodal system landscape | slide 008 | Product examples treated as context, not benchmark evidence |
| Mixed sequence and global autoregression | slide 010; captions 00:06:31--00:07:26 | Factorization formula and packing pseudocode |
| Multimodal tokenization overview | slide 011; captions 00:05:19--00:07:10 | Representation table across text, image, video, and audio |
| Continuous versus discrete representations | slide 012 | First-use glossary and task-dependent tradeoff |
| Text-only output objective | slide 013; captions 00:07:33--00:07:55 | Masked cross-entropy formula and listing |
| Deployed text-output examples | slide 014; captions 00:07:58--00:08:12 | Capability boundary and product-name caution |
| Omni all-modality objective | slide 015; captions 00:08:12--00:09:16 | Joint-loss formula and operational definition |
| Four-part scaling recipe | slide 019; captions 00:09:16--00:11:33 | Four-column reading guide and transfer caveat |
| Two omni-model research questions | slide 021; captions 00:11:37--00:12:18 | Lecture roadmap |
| Chameleon early fusion | slide 022; arXiv 2405.09818v2 | Architecture, historical importance, and source boundary |
| VQ-VAE tokenization | slide 023; captions 00:12:55--00:14:18; arXiv 1906.00446v1 | Nearest-code formula, information bottleneck, pseudocode |
| Arbitrary interleaved generation | slide 024; captions 00:14:23--00:14:50 | Capability explanation and causal-order caveat |
| Chameleon multitasking | slide 025; captions 00:14:50--00:15:26 | Task taxonomy rather than name list |
| Chameleon limitations | slide 026; captions 00:15:32--00:16:30 | Continuous semantics and diffusion-generation warning |
| Transfusion architecture | slide 027; arXiv 2408.11039v1 | Shared backbone and modality-specific objective setup |
| Joint AR and diffusion objective | slide 028; captions 00:17:25--00:18:35 | Diffusion equations and joint-loss listing |
| Transfusion generations | slide 029 | Qualitative-evidence reading guide and non-proof warning |
| Transfusion limitations | slide 030; captions 00:19:22--00:20:25 | Understanding-generation representation split |
| Shared transformer baseline | slide 031 | Baseline before sparsity |
| Modality gap | slide 032; arXiv 2203.02053v2 | Layer-wise representation geometry and causal caveat |
| MoT deterministic routing | slide 033; captions 00:21:48--00:24:30; arXiv 2411.04996v2 | Clean first-state diagram and routing definition |
| Complete MoT architecture | slide 039; arXiv 2411.04996v2 | Final architecture, training losses, and shared-sequence explanation |
| Experimental configuration | slide 040 | Parameter, hidden-size, GPU, token, and compute reading guide |
| Scaling results | slide 041; captions 00:24:30--00:26:58 | Matched-budget interpretation and active-parameter accounting |
| Generation samples | slide 042 | Qualitative comparison and evaluation limits |
| MoT plus MoE | slide 043; captions 00:26:58--00:28:20 | Deterministic routing versus learned expert routing table |
| MoT summary and LMFusion | slide 044; arXiv 2412.15188v4 | Efficiency, stability, controllability, freezing, asynchronous extension |
| BAGEL | slide 045; arXiv 2505.14683v3 | Separate generation path, multimodal base, planning-before-generation |
| π0.7 | slide 046; arXiv 2604.15483v2 | Multimodal steering, subgoal images, robotics evidence boundary |
| Transfer question | slide 047; captions 00:35:11--00:36:10 | Explicit open-question framing |
| Two transfer directions | slide 048 | Understanding-to-generation and generation-to-understanding mechanism map |
| Transfer asymmetry | slide 051; captions 00:36:10--00:39:11 | Language compression, loss geometry, redundancy, warning box |
| Broader multimodal intelligence | slide 052; captions 00:39:12--00:40:04 | Digital processing versus real-time physical intelligence |
| Final conclusion | slide 056; captions 00:40:06--00:41:36 | Compute, infrastructure, specialization, unification frontier |
| Public-material and employer-opinion boundary | captions 00:00:59--00:01:12 | Cover source note and opening warning |
| Shared attention still fuses modality routes | Q&A 00:42:42--00:44:08 | MoT architecture clarification |
| Objective and parameter sharing are separate axes | Q&A 00:44:08--00:46:10 | Design table |
| Video generation as predictive world model | Q&A 00:46:16--00:48:00 | Qualified embodiment extension |
| Bitmap-text scaling thought experiment | Q&A 00:48:14--00:53:31 | Untested hypothesis and efficiency caveat |
| Object-centric visual embeddings | Q&A 00:53:45--00:55:32 | Representation frontier |
| Spatial-reasoning expertise boundary | Q&A 00:58:20--00:59:18 | Epistemic-humility warning |
| Language as current reasoning skeleton | Q&A 01:01:10--01:04:21 | Present engineering advantage versus open theoretical question |
| Optional progressive builds | slides 002--004, 009, 016--018, 020, 034--038, 049--050 | Explicitly omitted because the final fully revealed state is retained |
| Recording-skipped deck appendix | slides 053--055 | Documented optional; no Interaction Models content invented |
| Full recording visual audit | 776 five-second samples; 13 reviewed contact sheets | Record no deck-external teaching visual and freeze 56-page deck treatment |
