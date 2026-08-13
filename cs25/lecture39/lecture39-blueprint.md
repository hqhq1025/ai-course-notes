# Lecture 39 Writing Blueprint

## Teaching thesis

The note should teach multimodal world models as a sequence of design decisions: define the intervention-conditioned prediction problem, distinguish translation from disambiguation, choose fusion and bottleneck locations, align expensive biological modalities, and validate simulations against measurements rather than trusting plausible outputs. The reader should leave able to connect generic Transformer mechanisms to spatial tumor biology without confusing model prediction with causal or clinical evidence.

## Section plan

### 1. From multimodal perception to an operational world model

- Figures 038, 040, 056, 059, 063--064.
- Define observations, actions, state transition, sensor modalities, and intervention-conditioned prediction.
- Preserve the audience contract and the claim that cancer is both a socially important application and a rich ML research substrate.

### 2. Translation, disambiguation, and five fusion families

- Figures 065--070, 072--080, 082.
- Use translation and disambiguation as the organizing distinction.
- Derive self-attention and cross-attention notation, then compare contrastive alignment, direct concatenation, cross-attention, bonus/CLS tokens, and adaptive LayerNorm.
- Mandatory warning: the taxonomy is incomplete and mechanisms can be composed.

### 3. Cancer as a partially observed dynamical system

- Figures 092, 094--096.
- Scaffold cancer immunology for a non-specialist reader: tumor, immune cells, microenvironment, treatment, response.
- Recast the clinical question as patient-conditioned intervention simulation.
- Separate a research world model from a clinical decision system.

### 4. Building an aligned multimodal cancer dataset

- Figures 097, 104, 108, 119, 125, 129, 134--135, 153, 175, 177.
- Explain H\&E, multiplex immunofluorescence, spatial transcriptomics, and genetic sequencing at first use.
- Teach why spatial registration, multiple cores, cells, genes, and assay cost dominate data engineering.
- Use the zoom sequence to explain the hierarchy patient → core → cell → gene.

### 5. Masked modeling, spatial context, and virtual cells

- Figures 179, 182, 184, 186, 192, 194, 197, 199, 205.
- Formalize gene/count tokenization, partial masking, conditional likelihood, and neighborhood conditioning.
- Explain why nearby cells provide disambiguating context.
- Treat counterfactual knockout outputs as hypothesis generators, not causal proof.

### 6. Cross-modal imputation from H\&E

- Figures 213, 215, 218, 224--225, 234.
- Explain the translation from cheap ubiquitous pathology images to expensive molecular measurements.
- Define imputation and calibration on first use.
- Emphasize gene-dependent error and the need for held-out-patient evaluation.

### 7. From unimodal encoders to massive multimodal Transformers

- Figures 237--241, 247.
- Compare separate modality encoders with a shared multimodal model.
- Explain masking policy, fusion placement, output heads, and intervention inputs.
- Connect model architecture to the patient-representation and experiment-selection loop.

### 8. Work in progress, interpretability, and evidence boundaries

- Figures 251, 256--259 plus Q&A.
- Cover raw-RNA training, learned biological features, hierarchical bottlenecks, missing healthy controls, causal validation, and sample-size limits.
- Discuss why a simulator still needs scientists or evaluated agents to select experiments.
- End with a concrete closed-loop research architecture and a scoped list of open problems.

## Required teaching devices

- At least 18 high-signal boxes distributed across definitions, intuition, engineering tradeoffs, and evidence boundaries.
- At least 7 formulas: world-model transition, multimodal posterior, contrastive loss, self/cross-attention, masked-count objective, neighborhood conditioning, and counterfactual delta.
- At least 4 captioned listings or pseudocode blocks: modality fusion, masked gene modeling, virtual-cell inference, and experimental prioritization.
- A terminology table covering modality, world model, translation, disambiguation, fusion, cross-attention, adaptive LayerNorm, H\&E, spatial transcriptomics, imputation, counterfactual, and calibration.
- Every figure receives a prose setup and local reading explanation; dense figures also receive an evidence-boundary sentence.
- Target at least 16,000 prose characters so 60 figures remain above the 260-character-per-figure heuristic.
