# Lecture 12 Teacher-Voice Ledger

Status: executable-source narration mapped on 2026-08-11.

Lecture 12 has no separate subtitle file. Teacher voice comes from explanatory `text(...)` nodes in `lecture12-slides.py`; the ledger records source-backed motivations, warnings, distinctions, and transitions only.

| Source node | Spoken point | Why it matters | Where it appears in note |
|---|---|---|---|
| `main():6–27` + `how_to_think_about_evaluation():372–390` | Before choosing data or metrics, ask what behavior and decision the evaluation is meant to support; there is no one true evaluation. | Establishes purpose before metric selection. | Opening box `课堂提示：评价先问目的，再选指标` and final box `老师强调：没有 one true evaluation` |
| `perplexity():62–103` | LAMBADA and HellaSwag can be viewed as probability/perplexity-style evaluations over candidate continuations, despite benchmark packaging. | Connects classical likelihood to downstream tasks. | Perplexity box `课堂提示：为什么说它们是 perplexity in disguise` |
| `chat_benchmarks():146–181` | Arena uses real user prompts and pairwise preferences, but its distribution and ranking have biases; automated judges require correlation checks. | Preserves the realism-versus-control caveat. | Chat benchmark warning `老师强调：Arena 真实但不干净` |
| `agentic_benchmarks():183–254` | Scaffolds greatly expand capability; evaluating an agent means evaluating language model plus planning, tools, memory, and execution scaffold. | Prevents attributing system success to model weights alone. | Agent box `课堂提示：agent benchmark 的归因问题` |
| `pure_reasoning_benchmarks():258–283` | ARC aims to separate reasoning from knowledge, but this is difficult and remains constrained to human-style reasoning. | States the construct boundary of “pure reasoning.” | ARC box `老师强调：reasoning benchmark 也有边界` |
| `realism():315–335` | Ecological validity improves with real professional/user tasks, but realism and privacy can conflict. | Explains why the best evals may not be fully public. | Realism box `课堂提示：真实 eval 往往不可完全公开` |
| `validity():339–368` | Internet-scale training weakens clean train/test splits; use overlap inference, reporting norms, fresh/private evals, and benchmark repair. | Frames validity as an evidence and governance problem. | Validity discussion and benchmark-quality figures |
| `how_to_think_about_evaluation():379–390` | Older evaluations often compared methods under standardized splits; current evaluations often compare models/systems where many components vary. | Clarifies why method and system leaderboards answer different questions. | `What are we evaluating?` subsection and methods/models/agents table |

Editorial attribution rule:

- `课堂提示` / `老师强调` is reserved for the source-backed rows above.
- `讲义提醒` marks additional benchmark-audit checklists and rule-design synthesis added by the note author.
