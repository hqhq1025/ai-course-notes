# Lecture 16 Writing Blueprint

## Teaching Thesis

The lecture is not a generic survey of commonsense or a claim that small models always beat large ones. Its through-line is that language fluency, knowledge quality, logical consistency, and moral judgment are different system properties. Yejin Choi presents three case studies in which structure, curated data, critics, and explicit constraints turn a large language model into a component of a more auditable knowledge or reasoning system.

## Chapter Plan

1. **Source audit and the David-versus-Goliath question**
   - V001--V004; T001--T006.
   - Establish the 2023 boundary, Winograd rephrasing failure, and evaluation discipline.
2. **Maieutic Prompting: from explanations to consistency**
   - V005--V008; T007--T010.
   - Build the recursive explanation graph, formalize logical constraints, explain weighted MaxSAT, and read the result bars without claiming universal reliability.
3. **Why leaderboard success is not commonsense**
   - V009--V012; T011--T013.
   - Separate dataset solving from task solving and give the operational definition of commonsense.
4. **ATOMIC and COMET: language model versus knowledge model**
   - V013--V017; T014--T016.
   - Explain symbolic relation types, neural generation, human evaluation, model-size caveats, and downstream reuse.
5. **Symbolic Knowledge Distillation**
   - V018--V023; T017--T023.
   - Derive the machine-to-corpus-to-machine pipeline, critic filtering, sequence-output approximation, loose versus critical teacher, and ATOMIC10x evidence boundary.
6. **Delphi: what exactly is being predicted?**
   - V024--V035; T024--T029.
   - Introduce machine ethics as a deployment problem, define descriptive ethical judgments, unpack COMMONSENSE NORM BANK and UNICORN, and distinguish declarative principles from applied judgments.
7. **Adversarial pressure, bias, and non-authority**
   - V036--V044; T030--T033.
   - Cover the Alexa socket example, launch backlash, wild adversarial prompts, explicit non-authority stance, Western / political bias, and status-quo reinforcement.
8. **Applications and the neuro-symbolic hybrid**
   - V045--V056; T034--T036.
   - Compare blocklists with contextual reasoning, digest follow-up applications, and explain bottom-up plus top-down constraints.
9. **Q&A: cost, objectives, abstention, and pluralism**
   - T037--T044; no duplicate slide images.
   - Preserve the teacher's complexity caveat, language-versus-knowledge-model distinction, component-role framing, and humanities-governance requirement.
10. **Summary and extension**
   - Reassemble the three systems by resource, mechanism, evidence, and failure mode.
   - Include primary-source reading order and self-check questions.

## Required Formal Treatments

- Maieutic explanation graph and consistency constraints.
- Weighted MaxSAT objective and confidence weights.
- Sequence-level knowledge-distillation cross entropy and sample approximation.
- Critic thresholding and corpus construction.
- COMET conditional knowledge generation.
- Delphi supervised ethical-judgment objective.
- Hybrid objective combining neural evidence with symbolic/top-down constraints.

## Required Code Treatments

- Maieutic recursive explanation and global-consistency pseudocode.
- Symbolic knowledge-distillation data pipeline pseudocode.
- Optional hybrid moral-reasoning loop if page flow permits.

## Evidence Guardrails

- Do not equate explanation generation with truthful reasoning.
- Do not treat MaxSAT consistency as factual correctness.
- Keep COMET / GPT-3 comparisons with their prompting, scale, and supervision differences.
- Restrict ATOMIC10x claims to the seven causal relation types evaluated.
- Describe Delphi as a descriptive model trained on sampled judgments, not an ethical oracle.
- Do not infer neutrality from dataset size or majority labels.
- Treat the Delphi hybrid as in-progress classroom research.
- Keep all post-2023 developments outside reconstructed classroom evidence.
