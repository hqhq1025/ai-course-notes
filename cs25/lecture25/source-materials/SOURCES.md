# Lecture 25 Source Audit

## Official Lecture Sources

- Stanford CS25 V3 archive: `https://web.stanford.edu/class/cs25/past/cs25-v3/`
  - Schedule date: December 5, 2023.
  - Speaker: Douwe Kiela, Contextual AI.
  - Official title: `Retrieval Augmented Language Models`.
- Stanford Online recording: `https://www.youtube.com/watch?v=mE7IDf2SmJg`
  - Upload date: January 25, 2024.
  - Runtime: 1:19:26.
  - Source resolution: 1920x1080 at 25 fps.
  - Manual `en-US` subtitle track parsed into 1,795 cues and normalized into 959 deduplicated transcript lines.

## Slide Recovery

- The CS25 archive and video description do not expose a standalone deck, and no speaker-hosted final classroom deck was found during the source audit.
- The recording uses a stable projected-slide region with a conferencing bar and speaker window. The accepted crop is `1580x920` from `(0,80)`, removing the top 80 pixels and rightmost 340 pixels without redrawing slide content.
- Three-second sampling produced 1,589 frames. Bright-slide filtering and grayscale change detection retained 77 high-recall candidates; manual contact-sheet review selected 49 distinct teaching states.
- Exact repeats, Q&A revisits, progressive duplicates, pure section dividers, recruitment material, and Stanford bumpers are intentionally omitted. Spoken explanations from duplicate-slide Q&A are preserved in the teacher-voice ledger.

## Primary Technical References

- Karpukhin et al., `Dense Passage Retrieval for Open-Domain Question Answering`, `https://arxiv.org/abs/2004.04906`.
- Khattab and Zaharia, `ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT`, `https://arxiv.org/abs/2004.12832`.
- Guu et al., `REALM: Retrieval-Augmented Language Model Pre-Training`, `https://arxiv.org/abs/2002.08909`.
- Lewis et al., `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks`, `https://arxiv.org/abs/2005.11401`.
- Izacard and Grave, `Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering`, `https://arxiv.org/abs/2007.01282`.
- Khandelwal et al., `Generalization through Memorization: Nearest Neighbor Language Models`, `https://arxiv.org/abs/1911.00172`.
- Borgeaud et al., `Improving Language Models by Retrieving from Trillions of Tokens`, `https://arxiv.org/abs/2112.04426`.
- Izacard et al., `Few-shot Learning with Retrieval Augmented Language Models`, `https://arxiv.org/abs/2208.03299`.
- Shi et al., `REPLUG: Retrieval-Augmented Black-Box Language Models`, `https://arxiv.org/abs/2301.12652`.
- Ram et al., `In-Context Retrieval-Augmented Language Models`, `https://arxiv.org/abs/2302.00083`.
- Jiang et al., `Active Retrieval Augmented Generation`, `https://arxiv.org/abs/2305.06983`.
- Min et al., `SILO Language Models: Isolating Legal Risk In a Nonparametric Datastore`, `https://arxiv.org/abs/2308.04430`.
- Liu et al., `Lost in the Middle: How Language Models Use Long Contexts`, `https://arxiv.org/abs/2307.03172`.
- Schick et al., `Toolformer: Language Models Can Teach Themselves to Use Tools`, `https://arxiv.org/abs/2302.04761`.
- Asai et al., `Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection`, `https://arxiv.org/abs/2310.11511`.
- Lin et al., `RA-DIT: Retrieval-Augmented Dual Instruction Tuning`, `https://arxiv.org/abs/2310.01352`.

## Evidence Boundary

- The lecture is a December 2023 research survey. Statements such as DRAGON being the preferred off-the-shelf dense retriever, skepticism about dedicated vector databases, comments about retrieval hardware, and predictions about what will happen next are speaker judgments at classroom time, not current product specifications or permanent industry conclusions.
- `RAG 2.0` is the speaker's systems-oriented framing for jointly optimizing retrieval, chunking, ranking, generation, cost, and domain adaptation. It is not presented as a standardized architecture with one canonical implementation.
- The lecture distinguishes hallucination from generic error in the closing Q&A and argues that grounding depends on an explicit source of truth. The note must preserve this as a stated definition and discuss its limits rather than silently treating every wrong answer as hallucination.
- Frozen RAG, in-context RALM, RePlug, RAG, FiD, kNN-LM, RETRO, REALM, and Atlas differ in what is trained, when retrieval occurs, how evidence is fused, and whether gradients reach the retriever. The rewrite must keep these axes separate.
- Legal-risk, compliance, and attribution discussions are research motivations. They do not establish that a non-parametric datastore automatically resolves copyright, licensing, privacy, or deployment obligations.

## Legacy Note Repair

- The legacy note used an incorrect April 3, 2026 date, an approximate 60-minute duration, no recovered teaching slides, and a bespoke preamble instead of the shared CS25 template.
- It replaced the actual literature survey with unsupported operations material: dashboards, incident runbooks, observability checklists, temperature scheduling, gate dropout, multimodal drift detection, regional knowledge-base governance, synthetic-query exercises, and deployment checklists.
- It omitted most of the lecture's progression from frozen RAG to contextualized retrieval and jointly trained systems, the sparse/dense/hybrid retrieval discussion, RePlug, in-context RALM, RAG/FiD/kNN-LM/RETRO, REALM/Atlas, FLARE, SILO, Lost in the Middle, Toolformer, Self-RAG, multimodal RAG, RAG 2.0, and the final hallucination Q&A.
