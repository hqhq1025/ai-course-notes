# Lecture 25 Coverage Matrix

| Node | Required source | Planned treatment | Note section | Status |
|---|---|---|---|---|
| slide-01-title | `slides-images/slide-01-title.jpg` | Official lecture title and scope | Why retrieval | covered |
| slide-02-age-of-language-models | `slides-images/slide-02-age-of-language-models.jpg` | Autoregressive language-model framing | Why retrieval | covered |
| slide-03-elman-1991-neural-lm | `slides-images/slide-03-elman-1991-neural-lm.jpg` | Early neural language model history | Why retrieval | covered |
| slide-04-next-word-prediction | `slides-images/slide-04-next-word-prediction.jpg` | Next-token model and broken interface | Why retrieval | covered |
| slide-05-eliciting-outputs | `slides-images/slide-05-eliciting-outputs.jpg` | Prompting, instruction tuning, RLHF, remaining failures | Why retrieval | covered |
| slide-06-contextualization-architecture | `slides-images/slide-06-contextualization-architecture.jpg` | External-memory RAG architecture | Why retrieval | covered |
| slide-07-two-paradigms | `slides-images/slide-07-two-paradigms.jpg` | Closed/open book and parametric/non-parametric | Why retrieval | covered |
| slide-08-why-retrieval-solves-issues | `slides-images/slide-08-why-retrieval-solves-issues.jpg` | Customization, staleness, revision, grounding | Why retrieval | covered |
| slide-09-many-questions | `slides-images/slide-09-many-questions.jpg` | System design question map | Why retrieval | covered |
| slide-10-train-test-time | `slides-images/slide-10-train-test-time.jpg` | Train-time versus inference-time choices | Train/test taxonomy | covered |
| slide-11-frozen-rag | `slides-images/slide-11-frozen-rag.jpg` | Frozen RAG and in-context learning | Train/test taxonomy | covered |
| slide-12-contextualization-via-retrieval | `slides-images/slide-12-contextualization-via-retrieval.jpg` | Retriever-side contextualization | Train/test taxonomy | covered |
| slide-13-sparse-retrieval | `slides-images/slide-13-sparse-retrieval.jpg` | TF-IDF, BM25, exact lexical matching | Retrieval stack | covered |
| slide-14-dense-retrieval | `slides-images/slide-14-dense-retrieval.jpg` | DPR and dense bi-encoder scoring | Retrieval stack | covered |
| slide-15-vector-database | `slides-images/slide-15-vector-database.jpg` | Similarity search and FAISS | Retrieval stack | covered |
| slide-16-colbert-late-interaction | `slides-images/slide-16-colbert-late-interaction.jpg` | ColBERT late interaction | Retrieval stack | covered |
| slide-17-retrieval-sota-splade-dragon | `slides-images/slide-17-retrieval-sota-splade-dragon.jpg` | SPLADE, DRAGON, hybrid search | Retrieval stack | covered |
| slide-18-contextualizing-retriever-for-generator | `slides-images/slide-18-contextualizing-retriever-for-generator.jpg` | Generator-aware retriever training | Frozen-generator contextualization | covered |
| slide-19-replug | `slides-images/slide-19-replug.jpg` | RePlug likelihood and KL objective | Frozen-generator contextualization | covered |
| slide-20-in-context-ralm | `slides-images/slide-20-in-context-ralm.jpg` | BM25 plus trained reranker | Frozen-generator contextualization | covered |
| slide-21-retrieve-rerank | `slides-images/slide-21-retrieve-rerank.jpg` | Retrieve--rerank--generate pipeline | Frozen-generator contextualization | covered |
| slide-22-contextualization-both | `slides-images/slide-22-contextualization-both.jpg` | Jointly contextualized retriever and generator | Whole-system contextualization | covered |
| slide-23-rag-architecture | `slides-images/slide-23-rag-architecture.jpg` | Original RAG architecture | Whole-system contextualization | covered |
| slide-24-rag-equations | `slides-images/slide-24-rag-equations.jpg` | RAG-Sequence and RAG-Token marginalization | Whole-system contextualization | covered |
| slide-25-freezing-suboptimal-results | `slides-images/slide-25-freezing-suboptimal-results.jpg` | Ablation evidence against freezing | Whole-system contextualization | covered |
| slide-26-frankenstein-rag | `slides-images/slide-26-frankenstein-rag.jpg` | Frankenstein metaphor for mismatched components | Whole-system contextualization | covered |
| slide-27-fid | `slides-images/slide-27-fid.jpg` | Fusion-in-Decoder | Whole-system contextualization | covered |
| slide-28-knn-lm | `slides-images/slide-28-knn-lm.jpg` | Nearest-neighbor language model | Whole-system contextualization | covered |
| slide-29-retro-architecture | `slides-images/slide-29-retro-architecture.jpg` | RETRO pretraining architecture | Whole-system contextualization | covered |
| slide-30-retro-plus-plus | `slides-images/slide-30-retro-plus-plus.jpg` | RETRO++ hybrid results | Whole-system contextualization | covered |
| slide-31-contextualization-all-the-way | `slides-images/slide-31-contextualization-all-the-way.jpg` | Transition to fully coupled systems | Whole-system contextualization | covered |
| slide-32-realm | `slides-images/slide-32-realm.jpg` | REALM asynchronous retrieval pretraining | REALM and Atlas | covered |
| slide-33-atlas-retriever-objectives | `slides-images/slide-33-atlas-retriever-objectives.jpg` | Atlas retriever loss options | REALM and Atlas | covered |
| slide-34-atlas-retriever-continued | `slides-images/slide-34-atlas-retriever-continued.jpg` | Atlas retriever update derivations | REALM and Atlas | covered |
| slide-35-atlas-loss-functions | `slides-images/slide-35-atlas-loss-functions.jpg` | Atlas loss-function comparison table | REALM and Atlas | covered |
| slide-36-atlas-pretraining | `slides-images/slide-36-atlas-pretraining.jpg` | Atlas pretraining tasks | REALM and Atlas | covered |
| slide-37-atlas-retriever-update-results | `slides-images/slide-37-atlas-retriever-update-results.jpg` | Atlas update-strategy results | REALM and Atlas | covered |
| slide-38-atlas-vs-closed-book | `slides-images/slide-38-atlas-vs-closed-book.jpg` | Atlas versus closed-book scaling | REALM and Atlas | covered |
| slide-39-when-to-retrieve | `slides-images/slide-39-when-to-retrieve.jpg` | FLARE and active retrieval timing | Open questions | covered |
| slide-40-training-at-scale | `slides-images/slide-40-training-at-scale.jpg` | Scalable retriever training | Open questions | covered |
| slide-41-silo-legal-risk | `slides-images/slide-41-silo-legal-risk.jpg` | SILO legal-risk motivation | Open questions | covered |
| slide-42-lost-in-middle | `slides-images/slide-42-lost-in-middle.jpg` | Evidence-position failure | Open questions | covered |
| slide-43-toolformer | `slides-images/slide-43-toolformer.jpg` | Retrieval as tool use | Open questions | covered |
| slide-44-self-rag | `slides-images/slide-44-self-rag.jpg` | Active retrieval and self-critique | Open questions | covered |
| slide-45-instruction-tuning | `slides-images/slide-45-instruction-tuning.jpg` | Instruction tuning the full RAG system | Open questions | covered |
| slide-46-advanced-frozen-rag | `slides-images/slide-46-advanced-frozen-rag.jpg` | Hierarchical retrieval, fusion, reranking, HyDE | Open questions | covered |
| slide-47-open-questions | `slides-images/slide-47-open-questions.jpg` | Evaluation, chunking, scaling, databases | Future and RAG 2.0 | covered |
| slide-48-multimodal-rag | `slides-images/slide-48-multimodal-rag.jpg` | Cross-modal and visual retrieval augmentation | Future and RAG 2.0 | covered |
| slide-49-rag-2-0 | `slides-images/slide-49-rag-2-0.jpg` | Systems-over-models synthesis | Future and RAG 2.0 | covered |
| teacher-voice-01 | `lecture25-teacher-voice-ledger.md` | Language-model history and interface framing | Why retrieval | covered |
| teacher-voice-02 | `lecture25-teacher-voice-ledger.md` | Hallucination, attribution, staleness, revision, customization | Why retrieval | covered |
| teacher-voice-03 | `lecture25-teacher-voice-ledger.md` | Train/test choices and frozen RAG | Train/test taxonomy | covered |
| teacher-voice-04 | `lecture25-teacher-voice-ledger.md` | Sparse/dense/hybrid tradeoffs and Apple example | Retrieval stack | covered |
| teacher-voice-05 | `lecture25-teacher-voice-ledger.md` | RePlug, reranking, and generator-aware retrieval | Frozen-generator contextualization | covered |
| teacher-voice-06 | `lecture25-teacher-voice-ledger.md` | Frankenstein critique and architecture survey | Whole-system contextualization | covered |
| teacher-voice-07 | `lecture25-teacher-voice-ledger.md` | REALM/Atlas training compromises and Q&A | REALM and Atlas | covered |
| teacher-voice-08 | `lecture25-teacher-voice-ledger.md` | Long context, active retrieval, scaling, SILO, evidence position | Open questions | covered |
| teacher-voice-09 | `lecture25-teacher-voice-ledger.md` | Tool use, Self-RAG, advanced frozen RAG, evaluation | Open questions | covered |
| teacher-voice-10 | `lecture25-teacher-voice-ledger.md` | Multimodality, RAG 2.0, fine-tuning, hallucination definition | Future and RAG 2.0 | covered |
