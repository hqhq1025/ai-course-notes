# Lecture 14 Writing Blueprint

## Teaching Thesis

The lecture is about allocating computation and modular responsibility. Search/planning converts inference-time compute into better decisions; Cicero then shows that a cooperative language agent needs separate but coupled models for strategic state, human conventions, intended actions, dialogue generation, and message evaluation.

## Source Boundary

- Required visual spine: 42 manually reviewed teaching states recovered from the official 1080p recording.
- Teacher voice: all major ledger rows should be synthesized; at least eight explicit classroom markers.
- Historical cutoff: 2023-01-31.
- Exclude later OpenAI reasoning results, later “test-time compute” scaling laws, and generic agent-system advice unless explicitly labeled as modern extension after the reconstructed lecture.

## Section Plan

1. **来源审计与课程主问题**
   - Official video, manual captions, no public standalone deck, 70-to-42 slide recovery.
2. **Poker：为什么 inference-time search 能压过巨量 train-time scaling**
   - Slides 1--5.
   - Exploitability, Brains vs AI, Libratus, Pluribus, research incentives.
3. **Go、Bitter Lesson 与通用 inference compute**
   - Slides 6--8.
   - AlphaGo Zero ablation, rough Elo-doubling calculation, broad definition of search, generality and value-sensitive budgets.
4. **为什么选择 Diplomacy**
   - Slides 9--20.
   - Strategic-game history, language-model progress, rules, support mechanics, trust, multi-agent and NLP perspectives.
5. **Cicero 的结果与闭环架构**
   - Slides 21--24.
   - Online evaluation, qualitative/quantitative result boundary, state/action/dialogue loop.
6. **贡献一：Intent-conditioned controllable dialogue**
   - Slides 25--30.
   - Intent labels, truthful-turn annotation, conditional generation, quality and perplexity result.
7. **贡献二：Dialogue-aware search 与 piKL**
   - Slides 31--35.
   - Self-play versus imitation, KL-regularized objective, human-policy modeling, dialogue-dependent action changes.
8. **贡献三和四：Self-play RL 与 value-based filtering**
   - Slides 36--38.
   - Human-behavior modeling, strategic/nonsense filters, expected-value test.
9. **对话案例、局限与未来方向**
   - Slides 39--42.
   - Tunisia negotiation, intent representation, dialogue-blind value model, truthfulness, general planning.
10. **总结与延伸**
    - Separate source facts from modern systems interpretation.

## Planned Formal Elements

- Exploitability / distance from Nash equilibrium as a worst-case loss measure.
- Rough compute substitution using Elo doublings, clearly labeled as the speaker's rule of thumb.
- Action prediction: `p(a_1,\ldots,a_7 \mid s,h,d)`.
- Intent-conditioned dialogue: `p(m \mid s,h,d,z_{speaker},z_{recipient})`.
- piKL objective: expected utility minus `lambda * KL(policy || human_anchor)`.
- Value-based message selection through predicted behavioral response.

## Planned Code Listings

1. Generic inference-time search loop with budgeted candidate expansion/evaluation.
2. Cicero-style closed-loop pseudocode: predict anchor policies, plan with piKL, derive intents, generate candidates, filter, send, repeat.

## Figure Treatment Rules

- Each of the 42 semantic slide filenames must appear exactly once in the TeX.
- Every subsection begins with prose explaining the question before its first visual.
- Target at least 14,000 prose characters and 330+ prose characters per figure overall.
- Dense slides receive explicit axis/column/diagram reading instructions and limitations.

## Acceptance Targets

- 40+ PDF pages.
- 42 required figures, 12+ teaching boxes, 5+ formulas, 2 captioned listings.
- Strict coverage with zero warnings.
- `check_quality.sh` grade `⭐⭐⭐`.
- Two-pass XeLaTeX without layout/reference/hyperref warnings.
- Canonical visual QA contact sheet reviewed and report signed.
