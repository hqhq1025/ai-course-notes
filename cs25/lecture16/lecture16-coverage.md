# Lecture 16 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V004 | Frame the David-versus-Goliath thesis, the Art-of-War evaluation discipline, strong-looking LM examples, and nearby inconsistency failures. | The lecture does not deny scaling gains; it challenges reliability and task validity. | Source audit and main question |
| V005--V008 | Reconstruct Maieutic tree generation, abductive explanations, logical inference, weighted MaxSAT, and benchmark results. | Logical consistency is not the same as truth or complete world knowledge. | Maieutic Prompting |
| V009--V012 | Explain adversarial leaderboard brittleness, the human/machine commonsense gap, and the lecture's operational definition. | “Commonsense” is scoped to practical, everyday, broadly shared knowledge and reasoning. | Benchmark critique and definitions |
| V013--V017 | Distinguish language models, symbolic knowledge graphs, and neural knowledge models; unpack ATOMIC relation types, COMET evaluation, and applications. | COMET, GPT-3, and GPT-2 comparisons are not apple-to-apple. | ATOMIC and COMET |
| V018--V023 | Explain the smaller-and-better question, symbolic-distillation funnel, sequence-level formula, loose/critical teachers, result bars, and ATOMIC10x comparison. | Scale/accuracy/diversity claims cover the seven evaluated causal relation types. | Symbolic Knowledge Distillation |
| V024--V030 | Introduce Delphi, machine ethics, Ask Delphi modes, compositional examples, everyday know-how, and benchmark results. | Delphi predicts descriptive judgments from training data; it is not a normative authority. | Delphi task and evaluation |
| V031--V035 | Trace COMMONSENSE NORM BANK sources, declarative-versus-applied morality failure, rules of thumb, UNICORN, and architecture motivation. | Aggregated data remains culturally and politically situated. | Delphi data and architecture |
| V036--V044 | Analyze exposed-socket judgment, adversarial launch pressure, public criticism, non-authority disclaimer, investment argument, status-quo risk, and bias acknowledgement. | Demo responses and public reactions do not establish universal moral competence. | Failure modes and governance |
| V045--V050 | Compare keyword blocking with contextual reasoning; cover identity judgments, controllable generation, social-norm narratives, and the hybrid agenda. | Follow-up applications inherit Delphi's data and bias limitations. | Applications and transition |
| V051--V056 | Explain original Delphi failures, theoretical bottom-up/top-down framework, common morality, detailed hybrid architecture, and adversarial results. | The hybrid is presented as work in progress and incurs substantial inference cost. | Neuro-symbolic hybrid |
| T001--T010 | Preserve the ChatGPT reliability challenge, David/Goliath nuance, Art-of-War methodology, lemons/cherries analogy, and Maieutic motivation/results. | Spoken examples are paraphrased and time-bounded. | Sections 1--2 |
| T011--T016 | Preserve the dataset/task distinction, commonsense definition, ATOMIC/COMET role, comparison caveat, and application motivation. | Human evaluation percentages do not imply deployment reliability. | Sections 3--4 |
| T017--T023 | Preserve crowdsourcing limits, critic imperfection, sampled sequence output, quality-versus-volume reasoning, and seven-relation scope. | The critic is not treated as an oracle. | Section 5 |
| T024--T036 | Preserve the machine-ethics motivation, research disclaimer, data provenance, launch backlash, non-authority position, bias acknowledgement, blocklist critique, and hybrid caveats. | Descriptive prediction is visibly separated from moral endorsement. | Sections 6--8 |
| T037--T044 | Preserve Q&A on description/prescription, cultural variation, component roles, computational cost, comparison limits, abstention, language-versus-knowledge objectives, and value pluralism. | Governance recommendations are attributed to the speaker and not converted into a universal rule. | Section 9 |

## Acceptance Evidence

- Final artifact: 50 pages, 56 full-width teaching figures, 18 teaching boxes, 9 in-note teacher-voice markers, 9 displayed formula blocks, 3 captioned listings, and 20,134 prose characters (`359` prose characters per figure).
- Every required slide asset is referenced exactly once. `check_note_coverage.py --strict` passes with zero warnings, including teacher voice and terminology digestion.
- `check_quality.sh` reports `⭐⭐⭐`.
- Two stabilized XeLaTeX passes complete without overfull/underfull boxes, unresolved references, rerun requests, or hyperref warnings; only repository-standard Fandol font notices remain.
- Canonical PDF QA renders all 50 pages with no near-blank pages. The signed report records full contact-sheet review plus enlarged inspection of mechanism, formula, code, result, architecture, comparison-table, and final pages.
