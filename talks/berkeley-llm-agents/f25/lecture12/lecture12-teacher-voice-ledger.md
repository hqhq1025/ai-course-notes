# Lecture 12 Teacher Voice Ledger

| Topic | Spoken point | Why it matters | Note location |
|---|---|---|---|
| Safety and security | Attackers follow useful technology, so agent safety must assume active adversaries. | Changes the threat model from accidental error to strategic exploitation. | Opening |
| Hybrid systems | LLMs are components inside hosts, tools, memories, data stores, and external environments. | Makes system boundaries and assets explicit. | System abstraction |
| Attack chains | Model output can become executable data, code, URLs, or instructions downstream. | Explains SQLi/RCE paths even when the model itself is not “hacked.” | Attack chain |
| Prompt injection | Indirect content can override instructions through retrieval, web pages, email, or memory. | Requires provenance and policy controls beyond prompt wording. | Injection section |
| Evaluation | Stand-alone LLM evaluation misses end-to-end agent behavior and tool consequences. | Motivates RedCode and AgentXploit. | Evaluation |
| Defense | No single defense is sufficient; use defense-in-depth, least privilege, privilege separation, and monitoring. | Provides the deployment architecture. | Defense |
| Privilege control | Policies should constrain actions at runtime and preserve utility where possible. | Connects security controls to usable agents. | Progent |
| Information flow | Track where information comes from and how it moves; provenance is a core defense primitive. | Addresses untrusted data and memory poisoning. | Final defenses |
