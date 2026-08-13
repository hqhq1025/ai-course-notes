# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs25/lecture01`

## Files

- `cover.jpg`
- `lecture01-blueprint.md`
- `lecture01-coverage.md`
- `lecture01-notes.tex`
- `lecture01-teacher-voice-ledger.md`
- `lecture01.en.srt`
- `metadata.json`

## Supplementary Source Materials

- `source-materials/SOURCES.md`

## Local Visual Assets

- `slides-images/slide-01-course-page.jpg`
- `slides-images/slide-02-title.jpg`
- `slides-images/slide-03-instructors.jpg`
- `slides-images/slide-04-learning-goals.jpg`
- `slides-images/slide-05-attention-timeline.jpg`
- `slides-images/slide-06-prehistory.jpg`
- `slides-images/slide-07-where-we-are.jpg`
- `slides-images/slide-08-future.jpg`
- `slides-images/slide-09-part-soft-attention.jpg`
- `slides-images/slide-10-local-global-attention.jpg`
- `slides-images/slide-11-self-attention-formulation.jpg`
- `slides-images/slide-12-self-attention-diagram.jpg`
- `slides-images/slide-13-ingredients.jpg`
- `slides-images/slide-14-encoder-decoder.jpg`
- `slides-images/slide-15-good-bad.jpg`
- `slides-images/slide-16-gpt3.jpg`
- `slides-images/slide-17-bert.jpg`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | official video 00:30 | slides-images/slide-01-course-page.jpg |
| V002 | figure | yes | official video 00:55 | slides-images/slide-02-title.jpg |
| V003 | figure | yes | official video 01:30 | slides-images/slide-03-instructors.jpg |
| V004 | figure | yes | official video 02:05 | slides-images/slide-04-learning-goals.jpg |
| V005 | figure | yes | official video 03:10 | slides-images/slide-05-attention-timeline.jpg |
| V006 | figure | yes | official video 03:45 | slides-images/slide-06-prehistory.jpg |
| V007 | figure | yes | official video 04:30 | slides-images/slide-07-where-we-are.jpg |
| V008 | figure | yes | official video 05:55 | slides-images/slide-08-future.jpg |
| V009 | figure | yes | official video 06:30 | slides-images/slide-09-part-soft-attention.jpg |
| V010 | figure | yes | official video 07:10 | slides-images/slide-10-local-global-attention.jpg |
| V011 | figure | yes | official video 08:00 | slides-images/slide-11-self-attention-formulation.jpg |
| V012 | figure | yes | official video 10:30 | slides-images/slide-12-self-attention-diagram.jpg |
| V013 | figure | yes | official video 12:30 | slides-images/slide-13-ingredients.jpg |
| V014 | figure | yes | official video 13:40 | slides-images/slide-14-encoder-decoder.jpg |
| V015 | figure | yes | official video 16:10 | slides-images/slide-15-good-bad.jpg |
| V016 | figure | yes | official video 18:30 | slides-images/slide-16-gpt3.jpg |
| V017 | figure | yes | official video 20:30 | slides-images/slide-17-bert.jpg |
| T001 | text | optional | `lecture01.en.srt 00:05--00:56` | Transformers moved from NLP into CV and RL; playful robot clarification. |
| T002 | text | optional | `lecture01.en.srt 00:42--01:03` | The course is a guest-speaker series built around real research applications. |
| T003 | text | optional | `lecture01.en.srt 01:03--01:59` | Instructors span software engineering, generative modeling, RL, robotics and NLP. |
| T004 | text | optional | `lecture01.en.srt 02:04--02:40` | Three goals: mechanism, beyond-NLP applications and new research ideas. |
| T005 | text | optional | `lecture01.en.srt 03:00--03:39` | The 2017 Transformer sits inside a longer attention timeline. |
| T006 | text | optional | `lecture01.en.srt 03:39--04:25` | RNN/LSTM/GRU memory and long-context limitations. |
| T007 | text | optional | `lecture01.en.srt 04:25--06:03` | Cross-field spread and 2021-era missing ingredients. |
| T008 | text | optional | `lecture01.en.srt 06:03--07:53` | Soft/hard and global/local attention predate self-attention. |
| T009 | text | optional | `lecture01.en.srt 07:53--10:30` | Self-attention updates tokens through pairwise relationships. |
| T010 | text | optional | `lecture01.en.srt 10:30--11:38` | Animation contrasts direct interaction with recurrent chains. |
| T011 | text | optional | `lecture01.en.srt 11:38--13:32` | Position, normalization, residual paths and masking are necessary ingredients. |
| T012 | text | optional | `lecture01.en.srt 13:32--16:02` | Encoder/decoder blocks differ in context access and masking. |
| T013 | text | optional | `lecture01.en.srt 16:02--18:04` | Parallelism and long-range modeling trade against quadratic cost and data needs. |
| T014 | text | optional | `lecture01.en.srt 18:04--20:25` | GPT-3 demonstrates decoder-only autoregressive pretraining and prompting. |
| T015 | text | optional | `lecture01.en.srt 20:25--22:18` | BERT demonstrates encoder-only bidirectional masked pretraining. |
| T016 | text | optional | `lecture01.en.srt 22:18--22:43` | Closing directs learners to the guest-speaker sequence. |

## Existing Note

- `lecture01-notes.tex`

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
