# Lecture 14 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V005 | Reconstruct poker progression from 2015 failure through Libratus and Pluribus, centered on the exploitability benefit of search. | The 100,000x comparison is a rough extrapolation from the shown scaling relation, not a universal constant. | Poker and search |
| V006--V008 | Use AlphaGo Zero, the Bitter Lesson, and generality slide to define broad inference-time search. | MCTS is a successful domain-specific method; the lecture explicitly says a general method was unknown. | Go and general inference compute |
| V009--V011 | Credit the interdisciplinary team, summarize strategic-game milestones, and place GPT-2 progress beside game AI. | Team slide is retained because system integration is a substantive thesis. | Why Diplomacy |
| V012--V015 | Explain Diplomacy rules, simultaneous action, dialogue, and support mechanics. | Rules and dialogue are connected causally: negotiated support changes the legal outcome of actions. | Diplomacy mechanics |
| V016--V018 | Preserve public reputation, expert trust framing, and RL/planning plus language intersection. | The game is not reduced to deception; credible cooperation is central. | Trust and task selection |
| V019--V020 | Contrast zero-sum self-play with mixed cooperation and contrast text imitation with intentional grounded dialogue. | Human conventions and suboptimality matter outside two-player zero-sum settings. | Multi-agent and NLP perspectives |
| V021--V023 | Present Cicero's goal, qualitative player reaction, ranking, and “strong human” result. | The speaker explicitly declines to call the result superhuman. | Cicero evaluation |
| V024 | Explain the complete recurrent architecture from state/dialogue inputs to planning, intents, generation, filtering, and message/action outputs. | The language model is one component; planning is separate. | Cicero architecture |
| V025--V030 | Cover contribution overview, intent model, automatic intent annotation, inference conditioning, behavior-controlled messages, and quality metrics. | Intent labels are near-term actions, and truthfulness is enforced by data/conditioning choices. | Controllable dialogue |
| V031--V035 | Explain pure self-play versus imitation, piKL, dialogue-conditioned response, and human-policy modeling. | piKL balances strength and human conventions; it does not solve general planning. | Planning and piKL |
| V036--V038 | Explain self-play RL, message-filtering contribution, and value-based rejection of strategically harmful messages. | Filters depend on learned behavioral/value models and can inherit their errors. | Self-play and filtering |
| V039--V040 | Analyze Austria and France dialogue examples as grounded negotiation over game state. | Fluent dialogue is evaluated by its strategic effects, not style alone. | Dialogue case studies |
| V041--V042 | Preserve limitations, future directions, final result summary, and public code/model note. | Later planning work is excluded from the reconstructed lecture. | Limitations and future directions |
| T001--T041 | Weave search motivation, research incentives, Q&A, caveats, modularity, truthfulness rationale, and general-planning agenda into prose and boxes. | Transcript claims are paraphrased and time-bounded. | Across all sections |

## Acceptance Evidence

- All 42 required visual nodes are referenced exactly once in `lecture14-notes.tex`.
- Strict coverage passes with zero warnings: 42 figures, 31 teaching boxes, 13 teacher-voice markers, 6 formula blocks, 2 captioned listings, 11 summaries, and 17,277 prose characters.
- `tools/scripts/check_quality.sh` reports 44 pages, 411 prose characters per figure, and `⭐⭐⭐`.
- Two final XeLaTeX passes are stable with no layout, reference, rerun, or hyperref warnings beyond repository-standard Fandol notices.
- Canonical visual QA is signed in `qa/lecture14-notes/qa-report.md` after contact-sheet and enlarged-page inspection.
