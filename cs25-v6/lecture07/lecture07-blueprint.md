# CS25 V6 Lecture 07 — Writing Blueprint

## Acceptance target

- 23 required recording-derived visual states, each inserted exactly once.
- At least 12,000 Chinese prose characters, targeting more than 260 prose characters per required figure.
- At least 20 high-signal teaching boxes, 14 teacher-voice markers, 8 displayed formula blocks, and 4 captioned listings.
- Strict coverage with zero hard errors or warnings; `⭐⭐⭐`; stable double XeLaTeX; complete signed visual QA.

## Teaching arc

### 1. Why discovery needs a faster clock

- Slides 002--003.
- Define `AI co-scientist`, `collaborative agent`, `scientist in the loop`, and `clock speed of discovery`.
- Reconstruct the Med-PaLM-to-hypothesis-generation origin story and explain why hallucination made a one-model solution inadequate.
- State the source boundary: the official description promises AMIE, but the recording teaches only AI co-scientist.

### 2. Task complexity, timescale, and scientific superintelligence

- Slides 004--006.
- Read the vertical complexity/impact axis and horizontal time axis.
- Use AlphaFold as a specialized compression of a long workflow, then place general LLMs in the short, lower-complexity region.
- Explain why scientific superintelligence is a system property involving long-horizon exploration, comparison, tools, memory, and human validation.

### 3. Multi-agent system design

- Slide 007.
- Present the scientist input, supervisor/resource allocation, generation, reflection, ranking, evolution, proximity, meta-review, tools, and memory.
- Add generate-debate-evolve pseudocode, a pairwise-tournament/Elo formula, and an asynchronous resource-allocation model.
- Explain first-use terms: test-time compute, self-play, pairwise ranking, Elo, tool use, memory, and asynchronous task execution.

### 4. What internal evaluation can and cannot prove

- No new visual node; use prose before the case-study visuals.
- Separate internal judge scores, expert curation, hidden-result recapitulation, prospective laboratory validation, replication, and clinical evidence.
- Preserve the audience challenge about model-as-judge circularity.
- Make the verification bottleneck and experiment-budget allocation explicit.

### 5. AMR as controlled recapitulation

- Slides 008--010.
- Explain cf-PICIs, capsids, helper-phage tails, host range, and why the answer was hidden at test time.
- Compare years of conventional experimentation with days of AI hypothesis generation without claiming the AI performed the wet lab.
- Treat press coverage as optional context, not scientific evidence.

### 6. A ladder of biomedical and biological evidence

- Slides 009 and 011--015.
- AML: KIRA6 cell-line dose response, selectivity, two failed suggestions, and why in vitro activity is not therapy.
- Liver fibrosis: human hepatic organoids, Vorinostat, anti-fibrotic effect, regeneration signal, and model limitations.
- Plant assemblies: Structural Novelty Index, AlphaFold 3 screening, NRC7 11-mer, purification, and electron microscopy.
- OCT4: AlphaFold as structural-plausibility feedback, not functional proof.
- Rejuvenation: include the slide only with the explicit unpublished/peer-review warning.

### 7. Alzheimer's: recapitulation plus one prospective node

- Slides 016--019.
- Build the ACE inhibitor -> bradykinin -> B2R -> inflammatory cascade carefully.
- Separate prior public literature, AI recapitulation, predicted intervention, experiment, and unpublished validation.
- Read the benchmark table as a mechanism-recovery comparison, not a clinical leaderboard.

### 8. Inverse comorbidity and cross-domain synthesis

- Slides 020--025.
- Define inverse comorbidity and formulate the SCLC-versus-neurodegeneration question.
- Explain the hypothesis portfolio: genomic chaos, DHX9/SRRM4, evading death, and neural hijack.
- Treat Dr. Bellegia's response as encouraging expert feedback, not peer review or experimental replication.
- Use the report pages to explain provenance, uncertainty, research contacts, and human handoff.

### 9. Q&A as systems engineering

- No repeated visual nodes.
- Cover knowledge-cutoff leakage, agent communication, peer-review scaling, report triage, preserving low-ranked clues, subproblem decomposition, undisclosed compute, and layered safety.
- Include a model-routing table for Pro versus Flash and a safety-monitoring pseudocode listing.

### 10. Final synthesis

- Compress the lecture into `generate -> debate -> rank -> evolve -> test -> update`.
- Contrast hypothesis throughput with validation throughput.
- End with a decision checklist for responsible co-scientist deployment.
- Mention the unrecorded AMIE transition only to delimit the lecture scope.

## Required concept scaffolds

1. Task-complexity/timescale reading guide.
2. Specialized model versus general scientific system table.
3. Agent-role glossary.
4. Generate-debate-evolve pseudocode.
5. Pairwise tournament and Elo formulas.
6. Evidence ladder from internal score to clinical evidence.
7. Verification-budget allocation equation.
8. AMR recapitulation timeline.
9. Case-by-case validation-status table.
10. Tool-loop pseudocode for AlphaFold feedback.
11. ACE--bradykinin--B2R mechanism chain.
12. Inverse-comorbidity hypothesis table.
13. Report-triage checklist.
14. Layered safety pseudocode and failure-mode table.

## Evidence boundaries to repeat in prose

- Do not equate AI co-scientist with one foundation model or one prompt.
- Do not treat Elo or model-as-judge scores as truth, novelty, or scientific validity.
- Do not call AMR recapitulation a prospective AI discovery.
- Do not infer clinical efficacy from AML cell lines or liver organoids.
- Do not infer protein function from AlphaFold structural plausibility alone.
- Do not present rejuvenation, Alzheimer's, or inverse-comorbidity classroom results as peer-reviewed.
- Do not treat an expert email as replication.
- Do not invent the undisclosed agent count, token budget, or AMIE content.
- Do not frame layered safeguards as complete prevention of misuse.
