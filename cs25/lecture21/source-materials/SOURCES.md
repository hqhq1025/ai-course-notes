# Lecture 21 Source Materials

## Canonical Classroom Sources

- Stanford CS25 V3 course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v3/`
- Stanford Online recording: `https://www.youtube.com/watch?v=1GbDTTK3aR4`
- Official title: *How I Learned to Stop Worrying and Love the Transformer*
- Speaker: Ashish Vaswani
- Classroom date: 2023-11-07
- Upload date: 2024-01-17
- Runtime: 1:20:38, 1920×1080
- Local official manual English captions: `lecture21.en.srt`, 1,866 parsed cues.
- Transcript derivatives: `transcript_timed.txt`, `transcript_clean.txt`, and five-minute `transcript_chunks.md`.
- No public standalone deck was found from the official course page, recordings page, video description, or exact-title search. The official 1080p recording is therefore the visual source of record.

## Visual Audit

- Three-second high-recall sampling produced 1,613 frames and 87 low-threshold candidates.
- Manual review retained 43 distinct teaching states in `slides-images/`.
- Repeated speaker-window variants, repeated slide revisits, incremental frames without distinct teaching content, Stanford bumpers, and the repeated `Thanks` page are intentionally omitted.
- Full 1920×1080 frames are preserved because the default crop used by the generic extractor would remove slide edges. Black letterbox bars and the official speaker overlay remain part of the source frame.

## Primary Technical Sources

- McCarthy et al., *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence* (1955): `http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf`
- Sutskever, Vinyals, and Le, *Sequence to Sequence Learning with Neural Networks*: `https://arxiv.org/abs/1409.3215`
- Bahdanau, Cho, and Bengio, *Neural Machine Translation by Jointly Learning to Align and Translate*: `https://arxiv.org/abs/1409.0473`
- Kalchbrenner et al., *Neural Machine Translation in Linear Time* (ByteNet): `https://arxiv.org/abs/1610.10099`
- Gehring et al., *Convolutional Sequence to Sequence Learning*: `https://arxiv.org/abs/1705.03122`
- Vaswani et al., *Attention Is All You Need*: `https://arxiv.org/abs/1706.03762`
- Parmar et al., *Image Transformer*: `https://arxiv.org/abs/1802.05751`
- Shaw, Uszkoreit, and Vaswani, *Self-Attention with Relative Position Representations*: `https://arxiv.org/abs/1803.02155`
- Huang et al., *Music Transformer*: `https://arxiv.org/abs/1809.04281`
- Child et al., *Generating Long Sequences with Sparse Transformers*: `https://arxiv.org/abs/1904.10509`
- Kitaev, Kaiser, and Levskaya, *Reformer: The Efficient Transformer*: `https://arxiv.org/abs/2001.04451`
- Roy et al., *Efficient Content-Based Sparse Attention with Routing Transformers*: `https://arxiv.org/abs/2003.05997`
- Wu et al., *Memorizing Transformers*: `https://arxiv.org/abs/2203.08913`
- Shazeer, *Fast Transformer Decoding: One Write-Head is All You Need* (multi-query attention): `https://arxiv.org/abs/1911.02150`
- Ainslie et al., *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*: `https://arxiv.org/abs/2305.13245`
- Dao et al., *FlashAttention*: `https://arxiv.org/abs/2205.14135`
- Schick et al., *Toolformer*: `https://arxiv.org/abs/2302.04761`

## Evidence Boundary

- The lecture is reconstructed at the 2023-11-07 classroom boundary.
- Later Transformer variants and post-2023 reasoning systems are not retroactively presented as lecture facts.
- Paper links are used to verify mechanisms and terminology; the lecture order, motivation, caveats, and Q&A claims come from the official recording and manual captions.
