# Lecture 15 Source Index

## Scope

- Course: Stanford CS25, Transformers United V2.
- Classroom date: 2023-02-07.
- Topic: Robotics and Imitation Learning.
- Speaker: Ted Xiao, Google Brain at the time of the lecture.
- Historical boundary: the note reconstructs the talk and public primary sources available by 2023-02-07. RT-2 and later vision-language-action systems are not substituted for this lecture.

## Official Course And Video Sources

1. Stanford CS25 V2 archive: <https://web.stanford.edu/class/cs25/past/cs25-v2/>
   - Confirms the date, speaker, title, and the three required readings: RT-1, SayCan, and Inner Monologue.
2. Stanford Online recording: <https://www.youtube.com/watch?v=ct4tdyyNDY4>
   - Official title: `Stanford CS25: V2 I Robotics and Imitation Learning`.
   - Classroom date in description: 2023-02-07.
   - Upload date: 2023-05-23.
   - Duration: 1:16:07.
3. Official manual English subtitles (`en-US`).
   - Downloaded as `lecture15.en.srt` and parsed into 1,840 non-empty caption intervals.
   - The previous local file contained 4,183 repeated rolling-window auto-caption cues and was replaced.

## Local Visual Evidence

- No standalone public deck was found on the course page, video description, speaker page, or official project pages.
- `lecture15.mp4` is the private local 1080p official recording used only for source recovery and must not be committed.
- The screen-share region was sampled every two seconds to build the high-recall candidate set.
- 2,284 sampled frames produced 315 high-recall stable candidates. Manual contact-sheet review retained 45 distinct teaching states, keeping final progressive builds and intermediate states only when they add a new experiment, feedback channel, or demo.
- After the teaching states were fixed, all 45 assets were re-extracted at their audited timestamps from the full `1920x1080` source frame. This preserves the right side of the projected slide; the small speaker tile remains part of the official recording rather than being removed with a lossy crop.
- Selected slide images are stored in `slides-images/` with semantic filenames.

## Course-Recommended Primary Sources

1. Brohan et al., **RT-1: Robotics Transformer for Real-World Control at Scale**: <https://arxiv.org/abs/2212.06817>
   - Main source for the RT-1 architecture, tokenized actions, 3 Hz inference budget, multi-task imitation dataset, generalization experiments, data scaling, and ablations.
2. Ahn et al., **Do As I Can, Not As I Say: Grounding Language in Robotic Affordances**: <https://arxiv.org/abs/2204.01691>
   - Main source for SayCan, the product of language-model usefulness and robotic affordance scores, and long-horizon planning evaluation.
3. Huang et al., **Inner Monologue: Embodied Reasoning through Planning with Language Models**: <https://arxiv.org/abs/2207.05608>
   - Main source for passive scene descriptions, active clarification, success detection, and closed-loop replanning.

## Additional Primary Sources Used In The Lecture

1. Jang et al., **BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning**: <https://arxiv.org/abs/2202.02005>
   - Historical bridge from language-conditioned multi-task imitation to RT-1.
2. Xiao et al., **Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models** (DIAL): <https://arxiv.org/abs/2211.11736>
   - Main source for VLM-generated relabeling, language-space coverage, novel-instruction evaluation, and the claim that moderate label noise can be tolerated at scale.
3. Official project pages shown on the closing slide:
   - SayCan: <https://say-can.github.io/>
   - Inner Monologue: <https://innermonologue.github.io/>
   - RT-1 historical project URL: <https://robotics-transformer.github.io/>
   - DIAL: <https://instructionaugmentation.github.io/>

## Source Hierarchy And Exclusions

1. Official video slides control the visual and chronological spine.
2. Official manual transcript controls motivation, Q&A, caveats, data-collection heuristics, and the speaker's uncertainty.
3. Primary papers control formulas, terminology, experiment definitions, and precise result boundaries.
4. The legacy `lecture15-notes.tex` is not a source. It is replaced because it contains no slide spine, no manifest, no teacher-voice ledger, and no canonical visual QA.
5. RT-2, Open X-Embodiment, PaLM-E, Gemini Robotics, and later VLA scaling results are outside the classroom boundary and may appear only in a clearly labeled modern extension.
