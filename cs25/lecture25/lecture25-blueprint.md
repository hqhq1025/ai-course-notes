# Lecture 25 Rewrite Blueprint

## Teaching Thesis

The lecture is a progression from a frozen language model plus search toward a jointly optimized retrieval-augmented system. The central question is not merely whether to retrieve, but which representation to search, when retrieval happens, what is trained, where evidence is fused, whether the generator uses it, how the system scales, and what counts as ground truth. The legacy note obscured this progression with invented operations and governance material.

## Planned Sections

### 1. Why retrieval augmentation exists

- Slides 01--09.
- Recover the history of language models, the next-token objective, instruction tuning as interface repair, and the enterprise shortcomings motivating external memory.
- Define parametric versus non-parametric memory, closed-book versus open-book, customization, staleness, revision, attribution, and generator faithfulness.
- Teaching devices: probability-chain formula, problem/mechanism table, external-memory warning, teacher-voice history.

### 2. Train-time and test-time taxonomy

- Slides 10--12.
- Separate updates to language model, query encoder, document encoder, reranker, index, and prompt at training and inference.
- Explain frozen RAG and contextualization via retrieval before introducing more tightly coupled systems.
- Teaching devices: train/test matrix, stop-gradient diagram, first-use glossary for retriever, index, embedding, reranker, and context.

### 3. Retrieval stack: sparse, dense, late interaction, hybrid

- Slides 13--17.
- Derive TF-IDF/BM25 intuition, dense bi-encoder scoring, vector-database/MIPS role, ColBERT late interaction, SPLADE/DRAGON, and hybrid fusion.
- Preserve Apple-versus-pear Q&A and exact-entity warning.
- Teaching devices: BM25 formula, cosine/dot-product formula, sparse/dense/late-interaction comparison, reciprocal-rank-fusion pseudocode.

### 4. Contextualizing retrieval for a frozen generator

- Slides 18--21.
- Explain RePlug's document weighting and KL objective, in-context RALM, learned reranking, and the retrieve--rerank--generate pipeline.
- Distinguish black-box generator access, log-probability/perplexity access, and full gradient access.
- Teaching devices: probability mixture, KL objective, access-level table, teacher-voice caveats.

### 5. Contextualizing the whole system

- Slides 22--31.
- Cover RAG sequence/token marginalization, the cost of independently frozen components, FiD decoder fusion, kNN-LM, RETRO, Retro++, and the transition to joint contextualization.
- Use the Frankenstein overlay as a deliberate classroom metaphor rather than decorative repetition.
- Teaching devices: architecture axes, fusion-location table, memory/compute accounting, local explanations for equations and benchmark tables.

### 6. REALM and Atlas deep dive

- Slides 32--38.
- Explain non-differentiable retrieval, asynchronous index refresh, query/document encoder updates, Atlas retriever losses, pretraining tasks, and closed-book comparisons.
- Preserve Q&A nuance on when query-only updates suffice and when document-side adaptation matters.
- Teaching devices: asynchronous-update loop, loss-function glossary, results-reading boxes, retriever-update pseudocode.

### 7. Open questions and advanced RAG

- Slides 39--46.
- Cover when to retrieve, FLARE, scalable in-batch training, SILO's legal-risk motivation, Lost-in-the-Middle, Toolformer, Self-RAG, instruction tuning of the full system, and developer-side advanced frozen RAG.
- Separate retrieval success from evidence utilization and legal motivation from legal resolution.
- Teaching devices: retrieval-policy formula, evidence-position warning, risk/evidence boundary, tool-use state machine.

### 8. Future systems, multimodality, and RAG 2.0

- Slides 47--49 plus closing Q&A.
- Discuss evaluation, database convergence, multimodal RAG, systems-over-models, learnable chunking, cost/quality tradeoff, retrieval plus fine-tuning, and hallucination versus generic error.
- End with a source-of-truth model: index selection, grounding strength, creative versus factual tasks, and why temperature is insufficient.
- Teaching devices: evaluation matrix, cost-quality objective, ground-truth/grounding table, final actionable checklist.

## Acceptance Targets

- All 49 retained teaching states included exactly once.
- At least 50 pages, 40 teaching boxes, 20 teacher-voice markers, 10 displayed formulas, and 3 captioned listings.
- At least 260 prose characters per figure on average and substantive local explanations for dense paper/benchmark slides.
- Strict coverage with no warnings, `⭐⭐⭐`, two-pass XeLaTeX, clean layout logs beyond repository-standard Fandol notices, and signed PDF visual QA.

## Explicit Exclusions

- No invented dashboards, SLI/SLOs, incident runbooks, gate dropout, multimodal drift monitors, regional governance workflows, or deployment checklists.
- No claim that RAG automatically eliminates hallucination, legal risk, stale data, or attribution failures.
- No back-projection of current Contextual AI products or database-market outcomes into the December 2023 classroom snapshot.
