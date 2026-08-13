# Lecture 36 Writing Blueprint

## Central thesis

The lecture should not be rewritten as an “AGI prediction” essay. Its teachable systems thesis is that useful autonomous agents require a co-designed stack: task contract, autonomy boundary, realistic evaluation, search and learning, persistent memory, personalization, agent communication, tool protocols, observability, and human override.

## Teaching sequence

1. Establish the AGI form-factor question and the four-part agent contract.
2. Separate an Everyday-AGI product vision from the evaluation/training/communication agenda needed to support it.
3. Define human-like computer interaction, API versus direct-control routes, and autonomy levels.
4. Use REAL Bench to teach deterministic environments, distributional evaluation, and slice-level reporting.
5. Treat AgentQ as a failure-recovery case study: MCTS, critique, process supervision, and preference learning.
6. Walk through the OpenTable trace as a trajectory-level debugging lesson.
7. Scaffold the neural-compute, looped-Transformer, memory, and personalization analogies with explicit limits.
8. Explain multi-agent parallelism/specialization, hierarchy, collectives-like synchronization, MCP, and A2A.
9. Turn reliability, loops, observability, audit, and override into an operational acceptance contract.
10. Preserve Q\&A caveats on distribution shift, benchmark saturation, domain-specific regression suites, model sizing, and memory.

## Figure treatment

- Retain all 58 required states exactly once.
- Group progressive demo states into mini-lessons, but keep distinct state transitions when they demonstrate search, recovery, concurrency, or an error boundary.
- Every dense benchmark, architecture, trajectory, protocol, or result figure gets nearby reading guidance and an evidence-limit paragraph.
- Product demos are dated classroom evidence, not current universal product specifications.

## Math and code scaffolding

- Agent policy and partial observability contract.
- End-to-end reliability multiplication and long-horizon compounding.
- Distributional evaluation over sites, tasks, and risk slices.
- MCTS selection and value backup.
- Process reward plus outcome reward.
- DPO-style preference objective.
- Persistent-memory retrieval and update equations.
- Personalization objective with privacy/safety constraints.
- Multi-agent decomposition and synchronization cost.
- Loop detection, budget, idempotency, and rollback pseudocode.
- Trace and regression-suite schemas as captioned listings.

## Evidence boundaries

- AgentQ benchmark results are paper/classroom results for a particular setup, not a guarantee for arbitrary websites.
- Direct computer control expands capability and risk simultaneously.
- The neural-compute and memory analogies are conceptual scaffolds, not literal equivalence to CPU/RAM/disk.
- MCP standardizes context/tool connections but does not automatically solve authorization, semantics, or safety.
- “99.9% reliability” is a deployment aspiration whose adequacy depends on task frequency and severity.
