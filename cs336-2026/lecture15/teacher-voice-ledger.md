# Lecture 15 Teacher Voice Ledger

| Time | Spoken point | Why it matters | Planned placement |
|---|---|---|---|
| `00:00:21--00:00:27` | Post-training is “artisanal”: real recipes depend on messy data and engineering choices. | Prevents readers from treating SFT/RLHF as a clean, standardized formula. | Opening motivation and warning on recipe uncertainty. |
| `00:03:27--00:04:10` | Frontier post-training disclosure is sparse; older papers often contain better annotation details than modern release notes. | Explains why the lecture relies on Stiennon, Anthropic HH and older public evidence. | Evidence-quality caveat near slides 4--5. |
| `00:24:59--00:25:11` | Tail-knowledge fine-tuning can actively induce hallucinated references or citations. | Converts a vague “fine-tuning adds facts” belief into a concrete failure mechanism. | Knowledge extraction section, slides 19--21. |
| `00:32:32--00:33:07` | Roughly 500 carefully chosen safety examples can cause a broad reduction in unsafe following. | Shows behavioral control can be data-efficient when the behavior already exists in the base model. | Safety section, slides 22--27. |
| `00:39:21--00:40:22` | Mid-training runs are much shorter than pretraining, so data-mixture search is more practical. | Connects two-phase training to the course's earlier data-mixing and scaling-law tools. | Mid-training section, slides 28--30. |
| `01:02:01--01:02:10` | Even well-resourced preference-data efforts often end up using AI feedback. | Frames AI feedback as an operational response to annotation cost, not a purely ideological choice. | AI-feedback section, slides 45--47. |
| `01:13:22--01:13:28` | The gradient form is the most intuitive way to understand DPO. | Motivates reading DPO as weighted positive/negative log-likelihood updates. | DPO update section, slides 56--58. |
| `01:17:59--01:18:10` | Entropy loss and mode collapse remain important even though the lecture is out of time. | Preserves a spoken warning that the slide deck only states tersely. | Failure-mode section, slides 62--64. |
