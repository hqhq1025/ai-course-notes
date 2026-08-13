# CS153 Lecture 07 Source Index

Access date: 2026-08-11.

## Classroom source

- Historical Stanford CS153 upload:
  `https://www.youtube.com/watch?v=4jDQi9P9UIw`.
  `yt-dlp` reports the video as private on 2026-08-11. The repository retains
  the official cover and a complete 48:37 automatic subtitle file,
  `lecture07.srt`, with 1288 cues.
- The transcript is a March 2025 snapshot. Scale numbers, provider position,
  database choices, security details and incident chronology are treated as
  speaker accounts unless a primary source confirms the same scope and date.

## Cursor official sources

- Secure codebase indexing:
  `https://cursor.com/blog/secure-codebase-indexing`.
- Codebase search documentation:
  `https://cursor.com/docs/agent/tools/search`.
- Privacy and data governance:
  `https://cursor.com/docs/enterprise/privacy-and-data-governance`.
- Security and privacy hardening:
  `https://cursor.com/docs/enterprise/security-hardening`.
- Agent security and tool approvals:
  `https://cursor.com/docs/agent/security`.
- Fast Apply / specialized edit model:
  `https://cursor.com/blog/instant-apply`.
- CursorBench and online/offline model evaluation:
  `https://cursor.com/blog/cursorbench`.
- Cursor Router, published after the classroom snapshot:
  `https://cursor.com/blog/router`.
- Current agent architecture overview:
  `https://cursor.com/docs/agent/overview`.

## Database and storage primary sources

- turbopuffer object-storage-native search architecture:
  `https://turbopuffer.com/blog/turbopuffer`.
- turbopuffer continuous recall measurement:
  `https://turbopuffer.com/blog/continuous-recall`.
- turbopuffer native filtering:
  `https://turbopuffer.com/blog/native-filtering`.
- Amazon S3 consistency and object model:
  `https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html`.
- PostgreSQL routine vacuuming and table bloat:
  `https://www.postgresql.org/docs/current/routine-vacuuming.html`.
- PostgreSQL `VACUUM` command and `VACUUM FULL` trade-offs:
  `https://www.postgresql.org/docs/current/sql-vacuum.html`.

## Version-handling rule

Cursor's 2026 documentation reflects later product and architecture evolution.
The note uses those pages to explain durable mechanisms such as content-based
embedding reuse, index sharing, model evaluation, routing, data governance and
object-storage search. It does not rewrite later features, scale or guarantees
as if they were already present in the March 2025 lecture.
