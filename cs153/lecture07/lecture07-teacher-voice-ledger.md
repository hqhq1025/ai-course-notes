# CS153 Lecture 07 Teacher-Voice Ledger

| Time / source node | Spoken point | Why it matters | Planned note location | Status |
|---|---|---|---|---|
| 00:00--02:20 / T001 | Cursor grew roughly two orders of magnitude; custom-model calls and indexed documents reached frightening scale. | Establishes load shape while requiring estimates to remain estimates. | opening | integrated |
| 02:20--05:20 / T002 | The product rests on indexing, model inference and the product/apply layer rather than one monolithic AI endpoint. | Defines the three systems. | architecture | integrated |
| 05:20--07:50 / T003 | A monolith can remain productive if critical and experimental paths have different blast radii. | Separates code organization from deployment failure domains. | blast radius | integrated |
| 07:50--10:20 / T004 | Self-hosted inference and codebase indexing require different scaling and latency strategies. | Prevents one-size-fits-all infrastructure. | system comparison | integrated |
| 10:20--14:40 / T005 | Merkle-style synchronization and incremental work avoid repeatedly uploading or embedding unchanged code. | Preserves the indexing mechanism. | sync/index | integrated |
| 14:40--19:10 / T006 | Early database choices accumulated operational complexity as indexing scale changed. | Frames schema/storage evolution as workload-driven. | data model | integrated |
| 19:10--25:30 / T007 | An indexing incident became a cascade of retries, jobs and recovery actions rather than a single failed component. | Supplies a systems incident lesson. | incident one | integrated |
| 25:30--32:40 / T008 | PostgreSQL storage pressure became existential; emergency migration required reducing database workload and re-embedding codebases. | Connects MVCC/storage maintenance to migration cost. | incident two | integrated |
| 32:30--34:10 / T009 | The best way to scale a database is sometimes to remove it from the data path. | Motivates object storage without becoming an absolute rule. | object storage | integrated |
| 34:10--36:40 / T010 | Object storage is increasingly the durable layer while compute and caches become replaceable. | Captures the architectural trend. | object storage | integrated |
| 36:40--38:10 / T011 | Free-token abuse can target large model customers, making pricing and identity part of infrastructure. | Links abuse to unit economics. | abuse | integrated |
| 38:10--41:40 / T012 | Model providers face sudden inference demand; Cursor asks for more capacity and spreads traffic across providers. | Establishes provider routing and rate-limit pressure. | provider portfolio | integrated |
| 41:40--43:30 / T013 | Code security required substantial engineering; stored vectors were described as encrypted with client-held key material. | Preserves the security motivation while separating current guarantees. | security | integrated |
| 43:30--45:00 / T014 | Pricing must reflect model cost and prevent arbitrage without destroying product simplicity. | Connects product packaging to resource accounting. | pricing | integrated |
| 45:00--46:30 / T015 | AI does not make computer-science education obsolete; systems knowledge becomes more valuable as generated code expands. | Preserves the educational judgment. | software engineering | integrated |
| 46:30--47:50 / T016 | The IDE may become an agent workspace, but fast feedback and user control remain central. | Connects UX to infrastructure. | IDE future | integrated |
| 47:50--48:37 / T017 | AI can assist incident response, but the production loop still needs ownership and judgment. | Provides the closing synthesis. | incident learning | integrated |
