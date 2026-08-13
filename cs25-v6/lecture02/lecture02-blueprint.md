# Lecture 02 Coverage Blueprint

## Teaching thesis

The lecture is a two-part argument for predictive latent world models. Causal-JEPA asks what structural bias makes object interactions unavoidable during training. LeWorldModel asks what minimal objective makes the same family trainable end-to-end from pixels. The note should keep these as complementary axes—structure and optimization simplicity—while preserving the speakers' explicit evidence boundaries.

## Source graph

- Canonical visual spine: 55-page official deck.
- Required deck nodes: 47 independent teaching pages.
- Required video node: one deck-external classroom question card at 00:31:25.
- Spoken spine: 1,371 manual-caption cues, distilled into 35 teacher-voice rows.
- Primary lecture-snapshot papers: Causal-JEPA v1 and LeWorldModel v1.
- Background verification: Slot Attention, V-JEPA, V-JEPA 2, and DINO-WM primary papers.

## Planned sections

1. **World-model contract and JEPA**
   - State/action/next-state mapping.
   - Representation, transition, and dynamics as three design obligations.
   - Generative prediction versus latent compatibility.
   - Energy-based interpretation and representation collapse.
2. **From patches to objects**
   - V-JEPA, V-JEPA 2, and DINO-WM background.
   - Push-T, CLEVRER, and PHYRE task interfaces.
   - Slot Attention, permutation equivariance, and object identity.
3. **Causal-JEPA mechanism**
   - Object-history masking.
   - Bidirectional predictor and identity-conditioned mask tokens.
   - Actions as separate nodes.
   - Full objective and implementation pseudocode.
4. **Causal-JEPA evidence and causal boundary**
   - CLEVRER counterfactual reasoning.
   - Push-T token efficiency and ablations.
   - PHYRE correlation shortcuts and attention evidence.
   - Influence neighborhood assumptions and the non-identifiability caveat.
5. **LeWorldModel and anti-collapse**
   - End-to-end JEPA failure modes.
   - Two-term MSE + SIGReg objective.
   - Random projections, normality tests, and Cramér--Wold intuition.
6. **Planning and physical-structure evaluation**
   - Latent model-predictive control.
   - Solver loop, horizon, costs, and action constraints.
   - Control performance, planning speed, probes, surprise, and rollout geometry.
7. **Limitations, tooling, and Q&A synthesis**
   - Short horizons, toy environments, and unrealistic goal interfaces.
   - `stable-worldmodel` reproducibility layer.
   - Physical AI, masking necessity, JEPA-native agents, hallucination, diffusion compatibility, and fast/slow policy composition.

## Formula and code scaffolding

- Controlled world-model mapping `f: S x A -> S` and stochastic variant.
- JEPA compatibility energy and prediction loss.
- Slot Attention normalization and iterative update.
- Causal-JEPA masked-history/future objective.
- Object-token versus patch-token planning cost.
- Predictive sufficiency / influence-neighborhood statement.
- LeWorldModel two-term loss.
- SIGReg projected normality objective and Cramér--Wold intuition.
- MPC latent rollout and goal cost.
- Surprise score and probe definitions.
- Captioned listings for Slot Attention, object masking, LeWM training, and latent MPC.

## Figure treatment

- Use paired or sequential figures only when the reader is told what changes between pages.
- Explain axes, table columns, baselines, token counts, mask multiplicity, and confidence/error bars locally.
- Treat the 00:31:25 question card as a required evidence-boundary figure, not as decoration.
- Keep `causal`, `world model`, `collapse`, `slot`, `MPC`, `probe`, and `surprise` definitions near first use.

## Quality risks

- Do not imply that latent prediction automatically yields causal or physical understanding.
- Do not hide that object-centric encoders may swap, split, merge, or omit objects.
- Do not attribute all Causal-JEPA gains to masking when architecture and action conditioning also change.
- Do not report post-lecture Causal-JEPA v2 wording as if it were stated on 2026-04-09.
- Do not frame JEPA as an alternative neural architecture to Transformers; it is a training framework.
- Do not interpret latent probes as proof of usable control or human-like concepts.
- Do not present the speakers' VLA, hallucination, or System 1/System 2 opinions as settled field consensus.

## Acceptance targets

- 48 required figures, each exactly once.
- 24+ teacher-voice markers, 28+ teaching boxes, 16+ formula blocks, and 4+ captioned listings.
- At least 260 prose characters per figure on average.
- Strict coverage clean, `⭐⭐⭐`, stabilized double XeLaTeX, and signed visual QA.
