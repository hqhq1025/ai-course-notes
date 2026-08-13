# Lecture 20 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V006 | Explain the two-kitten experiment, define a generalist agent, and introduce open environment, internet knowledge, and foundation-model ingredients. | The kitten experiment motivates active perception; it is not a direct benchmark of modern LLM embodiment. | Active experience and generalist definition |
| V007--V013 | Present Minecraft as an open-ended world, the MineDojo component view, 3,000+ task taxonomy, creative tasks, and representative demos. | Minecraft is a rich but simulated block world; success does not imply physical-world competence. | MineDojo environment and tasks |
| V014--V021 | Explain YouTube/Wiki/Reddit knowledge, asset/recipe catalogs, human questions, and transition to agent learning. | Internet knowledge is noisy and observational; it requires grounding and cannot directly supply actions. | Internet knowledge base |
| V022--V025 | Explain MineCLIP contrastive reward, language-conditioned RL, task results, and robustness. | Learned visual-language reward can be exploited or misaligned and must be validated against task success. | MineCLIP |
| V026--V038 | Explain symbolic interfaces, Mineflayer, Voyager data flow, code-as-action, iterative prompting, critic, skill memory, retrieval, automatic curriculum, integrated loop, and exploration/map results. | Voyager's evidence is within Minecraft and depends on GPT-4, executable APIs, and environment feedback. | Voyager |
| V039--V042 | Explain Eureka's coding-LLM/reward loop, reflection, reward-code edits, and dexterity/simulation scaling. | Reward improvement relies on simulator feedback and does not guarantee safe real-world reward design. | Eureka |
| V043--V050 | Present the outlook, internet-video properties, representative behavior, representation/reward/action learning, and multimodal foundation-model thesis. | Videos are cheap observations but lack native action labels and causal intervention. | Learning from internet video |
| V051--V061 | Explain multimodal prompting, VIMA architecture and tasks, RT-2/RoboCat, project evidence, multimodal prompt vocabulary, and the human-level Minecraft challenge. | Multimodal prompting demonstrates task unification in defined settings; current agents remain far from human creativity. | VIMA and outlook |
| T001--T004 | Preserve active-kitten motivation, passive-pretraining complement, generalist definition, and environment-complexity argument. | Spoken claims are paraphrased and timestamp-bounded. | Sections 1--3 |
| T005--T008 | Preserve creative-task/reward difficulty, internet knowledge, MineCLIP mechanism, and reward-model limitations. | Learned rewards remain proxies for task success. | Sections 3--4 |
| T009--T013 | Preserve symbolic interface motivation, code-as-action feedback, critic/skill memory, curriculum, and scoped Voyager evidence. | Minecraft progress metrics are not universal intelligence metrics. | Section 5 |
| T014--T015 | Preserve Eureka reward reflection and simulator-scaling interpretation. | Real-world safety and reward hacking remain explicit caveats. | Section 6 |
| T016--T018 | Preserve the three video-learning routes, multimodal embodied API, RT-2/RoboCat continuation, and final community challenge. | Future-looking claims remain attributed and current capability remains bounded. | Sections 7--9 |

## Acceptance Evidence

- Full source-first rewrite completed on 2026-08-11 with 61/61 required visual nodes referenced exactly once and 18 teacher-voice markers woven into the prose.
- `check_note_coverage.py --strict`: zero errors and zero warnings; 61 figures, 38 read-figure explanations, 38 teaching boxes, 9 formula blocks, 3 captioned listings, 9 summaries, and 23,915 prose characters.
- Final two-pass XeLaTeX compilation completed successfully; the 54-page PDF has no overfull/underfull boxes, undefined references, rerun requests, or hyperref warnings. Only the repository-accepted Fandol font notices remain.
- `check_quality.sh`: `⭐⭐⭐` with 54 pages and 392 prose characters per figure.
- `render_pdf_qa.py`: rendered all 54 pages, detected no near-blank pages, and produced `qa/lecture20-notes/contact.png`; manual checklist signed after full contact-sheet review and targeted full-size inspection.
