# Lecture 14 Source Index

## Scope

- Course: Stanford CS25, Transformers United V2.
- Classroom date: 2023-01-31.
- Topic: Strategic Games.
- Speaker: Noam Brown, FAIR at the time of the lecture.
- Historical boundary: the note reconstructs the talk and primary sources available by the classroom date. Later OpenAI reasoning work or later versions of Noam Brown's planning talks are not substituted for this lecture.

## Official Course And Video Sources

1. Stanford CS25 V2 archive: <https://web.stanford.edu/class/cs25/past/cs25-v2/>
   - Confirms the date, speaker, title, and three recommended readings.
2. Stanford Online recording: <https://www.youtube.com/watch?v=phWxl0nkgKk>
   - Official title: `Stanford CS25: V2 I Strategic Games`.
   - Classroom date in description: 2023-01-31.
   - Upload date: 2023-05-22.
   - Duration: 53:20.
3. Official manual English subtitles (`en-US`).
   - Downloaded as `lecture14.en.srt`.
   - Parsed into 1,176 caption intervals.
   - The previous local SRT was an auto-caption file with repeated rolling-window cues and was replaced.

## Local Visual Evidence

- No standalone public deck was found on the course page, the video description, or source searches.
- `lecture14.mp4` is the local 1080p official recording used only as a private source artifact.
- The full recording was sampled every two seconds after cropping to the screen-share region (`1680x945`).
- 1,600 frames produced 70 high-recall candidates. Manual contact-sheet review retained 42 distinct teaching states and omitted duplicate incremental builds, repeated section markers, the Stanford holding screen, and duplicate closing frames.
- Selected slide images are stored in `slides-images/` with semantic filenames.

## Course-Recommended Primary Sources

1. Bakhtin et al., **Human-level play in the game of Diplomacy by combining language models with strategic reasoning** (Science, 2022): <https://www.science.org/doi/full/10.1126/science.ade9097>
   - Main source for Cicero's architecture, online-league evaluation, grounded dialogue, planning, filtering, and limitations.
2. Jacob et al., **Modeling Strong and Human-Like Gameplay with KL-Regularized Search** (ICML 2022): <https://proceedings.mlr.press/v162/jacob22a.html>
   - Main source for piKL, the tradeoff between human imitation and strategic strength, and modeling human policies.
3. Anthony et al., **Learning to Play Diplomacy with No Human Supervision** / **No-Press Diplomacy from Scratch** (NeurIPS 2021): <https://proceedings.neurips.cc/paper/2021/hash/95f2b84de5660ddf45c8a34933a2e66f-Abstract.html>
   - Source for no-press Diplomacy, combinatorial action spaces, self-play, and the multiple-equilibria warning.

## Additional Primary Sources Visible In Slides

1. Brown and Sandholm, **Superhuman AI for heads-up no-limit poker: Libratus beats top professionals** (Science, 2017): <https://www.science.org/doi/10.1126/science.aao1733>
2. Brown and Sandholm, **Superhuman AI for multiplayer poker** (Pluribus, Science, 2019): <https://www.science.org/doi/10.1126/science.aay2400>
3. Silver et al., **Mastering the game of Go without human knowledge** / AlphaGo Zero (Science, 2017): <https://www.science.org/doi/10.1126/science.aar6404>
4. Sutton, **The Bitter Lesson** (2019): <http://www.incompleteideas.net/IncIdeas/BitterLesson.html>
   - Used for the broader claim that search and learning are general methods that scale with computation.

## Source Hierarchy And Exclusions

1. Official video slides control the visual and chronological spine.
2. Official manual transcript controls spoken motivation, Q&A, caveats, and historical claims.
3. Primary papers supply formulas, exact experiment context, and terminology.
4. The legacy `lecture14-notes.tex` is not a source. It is replaced because it had no figure coverage, no manifest, and added later LLM-agent generalizations without reconstructing Cicero's actual mechanisms.
5. Later talks that reuse similar search slides may help locate paper provenance, but they are not cited as evidence for what was said on 2023-01-31.
