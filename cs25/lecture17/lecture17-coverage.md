# Lecture 17 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| V001--V009 | Establish the lecture contract and explain why clinical text, encounter histories, proteins, and genomes can all be modeled as sequences while retaining different semantics. | “Sequence” is a representational commonality, not proof that one tokenizer or objective fits every modality. | Opening and biomedical sequence view |
| V010--V018 | Motivate clinical knowledge evaluation; reconstruct the paper context, biomedical-LM timeline, missing capabilities, medical QA tasks, MultiMedQA composition, examples, and summary. | Dataset aggregation improves breadth but does not equal clinical deployment coverage. | Clinical motivation and MultiMedQA |
| V019--V022 | Explain the long-form evaluation framework and separate clinician rubrics from layperson usefulness rubrics before domain alignment. | Human evaluation is based on a limited set of questions and raters. | Evaluation framework |
| V023--V034 | Trace PaLM to Flan-PaLM to Med-PaLM; explain benchmark results, scaling, selective prediction, human-evaluation limits, domain data, prompt tuning, and the alignment pipeline. | Multiple-choice gains and abstention curves do not prove safe autonomous care. | Scaling and Med-PaLM |
| V035--V043 | Unpack scientific consensus, comprehension/retrieval/reasoning, missing content, harm, bias, helpfulness, qualitative examples, and clinical takeaways. | Axes are distinct and sometimes non-complementary; longer answers can introduce more errors. | Human evaluation and clinical role |
| V044--V049 | Introduce long protein sequences, Performer kernel attention, complexity results, protein-LM evidence, and amino-acid attention. | Attention maps and benchmark gains do not establish biological causality. | Performer and protein LMs |
| V050--V057 | Explain ProtNLM motivation, UniProt free text, sequence-to-language framing, captioning, T5 tasks, results, and CRISPR-Cas9 example. | Generated descriptions are annotation hypotheses, not experimental validation. | ProtNLM |
| V058--V068 | Explain the genomics transition, DeepConsensus task, PacBio CCS, correction labels, Transformer representation, alignment loss, quality scores, read accuracy, and real-world impact. | Token/base accuracy, read-level accuracy, and operational impact are reported separately. | DeepConsensus |
| V069--V078 | Motivate gene-expression prediction from GWAS and non-coding variants; scaffold transcription regulation, disrupted binding, Enformer architecture, genomic tracks, results, and application takeaways. | Predicted variant effects prioritize hypotheses; they do not prove disease causality. | Enformer |
| V079--V084 | Preserve the future section, “when and how” thesis, foundation biomedical AI, combined scientist/physician metaphor, Nobel question, and acknowledgements. | The closing vision is explicitly forward-looking. | Summary and outlook |
| T001--T006 | Preserve the lecture contract, sequence examples, multimodal/scale argument, and transitions across the biomedical stack. | Spoken points are paraphrased and time-bounded. | Sections 1--2 |
| T007--T019 | Preserve knowledge-versus-usefulness framing, benchmark fragmentation, dual-rater evaluation, scaling caveats, abstention, small human-evaluation set, prompt-tuning mechanism, multidimensional axes, Q&A corrections, harm interpretation, and clinical complementarity. | No claim is upgraded from research evaluation to deployment readiness. | Sections 3--4 |
| T020--T025 | Preserve long-sequence motivation, Performer tradeoff, attention-map limitation, protein annotation demand, T5-style tasks, and CRISPR application boundary. | Protein descriptions remain predictions requiring biological validation. | Sections 5--6 |
| T026--T030 | Preserve the two genomics problems, PacBio CCS geometry, gap-aware correction, quality scores, and deployment/system impact. | DeepConsensus evidence is kept at the levels reported in the lecture. | Section 7 |
| T031--T034 | Preserve non-coding variant motivation, distant regulation, Enformer tracks, and the feedback from biomedical challenges to general AI. | Variant predictions are not causal proofs. | Section 8 |
| T035--T036 | Preserve the foundation-model integration thesis and the closing scientific-discovery question. | Future-looking views remain attributed to the speaker. | Section 9 |

## Acceptance Evidence

- Final artifact: 68 pages, 84 full-width recovered teaching figures, 38 teaching boxes, 14 in-note teacher-voice markers, 10 displayed formula blocks, 3 captioned listings, and 21,962 prose characters (`261` prose characters per figure).
- Every required slide asset is referenced exactly once. `check_note_coverage.py --strict` passes with zero warnings, including section bridges, terminology digestion, teacher voice, formula explanations, and manifest coverage.
- `check_quality.sh` reports `⭐⭐⭐`.
- Two stabilized XeLaTeX passes complete without overfull/underfull boxes, unresolved references, rerun requests, or hyperref warnings; only repository-standard Fandol font notices remain.
- Canonical PDF QA renders all 68 pages with no near-blank pages. The signed report records full contact-sheet review plus enlarged inspection of tables, formulas, code, dense result slides, application pages, final synthesis, and references.
