#!/usr/bin/env python3
"""Generate teaching diagrams for CS153 Lecture 11."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1600, 900
BG, INK, MUTED, LINE = "#F7F3EA", "#1F2933", "#667085", "#93A0AD"
COLORS = [("#DCEAF7", "#3E6C91"), ("#F1E5BD", "#8B6B1F"), ("#E6DDF2", "#6E568E"), ("#DCEBDD", "#4F7A55"), ("#F4DCD7", "#A44D40")]
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "images"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size)


def base(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.text((80, 52), title, fill=INK, font=font(43))
    draw.text((82, 116), subtitle, fill=MUTED, font=font(21))
    draw.line((80, 164, WIDTH - 80, 164), fill=LINE, width=2)
    draw.text((80, HEIGHT - 48), source, fill=MUTED, font=font(18))
    return image, draw


def node(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, lines: list[str], color: tuple[str, str]) -> None:
    left, top, right, bottom = rect
    fill, border = color
    draw.rounded_rectangle(rect, radius=22, fill=fill, outline=border, width=4)
    draw.text((left + 22, top + 18), title, fill=border, font=font(24))
    y = top + 66
    for line in lines:
        draw.text((left + 22, y), line, fill=INK, font=font(18))
        y += 31


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((*start, *end), fill=LINE, width=6)
    draw.polygon([(end[0], end[1]), (end[0] - 22, end[1] - 12), (end[0] - 22, end[1] + 12)], fill=LINE)


def save(image: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / name, quality=92)


def chain(name: str, title: str, subtitle: str, source: str, items: list[tuple[str, list[str]]], footer: str) -> None:
    image, draw = base(title, subtitle, source)
    gap, left, top, bottom = 40, 80, 255, 650
    width = (WIDTH - 160 - gap * (len(items) - 1)) // len(items)
    for index, (label, lines) in enumerate(items):
        x = left + index * (width + gap)
        node(draw, (x, top, x + width, bottom), label, lines, COLORS[index % len(COLORS)])
        if index < len(items) - 1:
            arrow(draw, (x + width + 6, 450), (x + width + gap - 6, 450))
    draw.text((80, 745), footer, fill="#A44D40", font=font(21))
    save(image, name)


def grid(name: str, title: str, subtitle: str, source: str, items: list[tuple[str, list[str]]], footer: str) -> None:
    image, draw = base(title, subtitle, source)
    rects = [(90, 220, 750, 430), (850, 220, 1510, 430), (90, 500, 750, 710), (850, 500, 1510, 710)]
    for index, ((label, lines), rect) in enumerate(zip(items, rects)):
        node(draw, rect, label, lines, COLORS[index])
    draw.text((80, 770), footer, fill="#A44D40", font=font(21))
    save(image, name)


def main() -> None:
    grid("01-security-program.png", "Security Scales Through People, Process, Platform and Governance", "A larger team is not mature unless authority, tooling and executive decisions scale too", "Transcript-grounded redraw · 00:00–03:20", [("People", ["Product security", "Detection / IR", "GRC / privacy"]), ("Process", ["Risk review", "Incident command", "Disclosure"]), ("Platform", ["Identity", "Telemetry", "Vulnerability mgmt"]), ("Governance", ["CEO / board", "Counsel", "Decision rights"])], "Security maturity is an operating system, not only headcount.")
    chain("02-public-private-loop.png", "Technology and Government Need a Continuous Feedback Loop", "Digital harms, technical capability and public rules evolve at different speeds", "Transcript-grounded redraw · 03:20–09:10", [("Technology", ["New products", "New data flows", "New risks"]), ("Observed harms", ["Incidents", "Market failure", "Rights impact"]), ("Rules", ["Law / regulation", "Standards", "Enforcement"]), ("Implementation", ["Controls", "Reporting", "Feedback"])], "No regulation creates ambiguity too; poor regulation creates friction without reducing harm.")
    chain("03-vdp-intake.png", "A VDP Turns External Research Into a Remediation Workflow", "Acknowledgment, validation, ownership and coordinated disclosure need explicit service levels", "CISA/DOJ VDP guidance + transcript 12:30–15:20", [("Report", ["Researcher", "Repro steps", "Affected asset"]), ("Triage", ["Scope", "Severity", "Duplicate"]), ("Remediate", ["Owner", "Fix / verify", "Timeline"]), ("Close / disclose", ["Researcher update", "Coordinated release", "Credit / reward"])], "A mailbox without ownership and status updates is not a vulnerability disclosure program.")
    grid("04-vdp-vs-bounty.png", "A VDP and a Bug Bounty Solve Different Problems", "Safe reporting can exist without payment; bounty programs add reward and eligibility rules", "CISA BOD 20-01 + transcript", [("VDP", ["Safe channel", "Good-faith terms", "Response process"]), ("Bug bounty", ["Optional payment", "Severity table", "Eligibility"]), ("Shared", ["Scope", "Research rules", "Coordination"]), ("Not covered", ["Extortion", "Data misuse", "Out-of-scope harm"])], "Payment does not retroactively authorize harmful conduct or erase incident obligations.")
    grid("05-safe-harbor.png", "Safe Harbor Requires Clear Scope and Good-Faith Boundaries", "Researchers and defenders both need predictable rules before testing begins", "CISA/DOJ VDP guidance", [("In scope", ["Listed assets", "Allowed methods", "Test accounts"]), ("Good faith", ["Minimize access", "Stop on sensitive data", "Report promptly"]), ("Prohibited", ["Persistence", "Disruption", "Data use / extortion"]), ("Escalation", ["Safety contact", "Law enforcement", "Dispute path"])], "Ambiguous scope increases risk for researchers, users and the organization.")
    grid("06-incident-command.png", "Security Incidents Need a Cross-Functional Command Structure", "Technical containment, legal analysis, communications and business continuity run in parallel", "NIST SP 800-61r3 + transcript", [("Incident command", ["Severity", "Priorities", "Decision log"]), ("Technical", ["Contain", "Forensics", "Recover"]), ("Legal + comms", ["Privilege", "Notification", "Regulators"]), ("Business", ["Customer impact", "Continuity", "Executive / board"])], "The CSO owns security operations, not every legal, disclosure or corporate decision alone.")
    chain("07-evidence-chain.png", "Evidence Preservation Protects Investigation and Decision Quality", "Collection, integrity, access and timeline records must survive technical and legal review", "NIST incident response + transcript", [("Preserve", ["Logs / systems", "Snapshot", "Legal hold"]), ("Integrity", ["Hash", "Timestamp", "Source"]), ("Custody", ["Authorized access", "Transfer log", "Purpose"]), ("Timeline", ["Fact / hypothesis", "Decision", "Notification"])], "A complete record supports both remediation and later review; it must not be rewritten to fit a narrative.")
    chain("08-disclosure-decision.png", "Disclosure Decisions Start With Facts and Materiality", "Different audiences, legal bases and timing rules require a coordinated decision process", "SEC 2023 rule + NIST + transcript", [("Facts", ["Scope", "Data / systems", "Operational impact"]), ("Materiality", ["Investor / customer", "Likelihood / magnitude", "Counsel analysis"]), ("Audience", ["Users", "Regulators", "Law enforcement"]), ("Timing", ["Contract / statute", "Form 8-K", "Approved delay"])], "For SEC registrants, the four-business-day clock generally starts after materiality is determined—not automatically at discovery.")
    chain("09-decision-log.png", "Technical Facts and Legal Decisions Need a Shared Record", "Role clarity prevents both silent gaps and retrospective responsibility shifting", "Transcript-grounded redraw · 21:00–25:40", [("Technical fact", ["Evidence", "Confidence", "Unknowns"]), ("Counsel analysis", ["Duties", "Privilege", "Options"]), ("Executive decision", ["Risk", "Audience", "Timing"]), ("Record + revisit", ["Owner", "Rationale", "New evidence"])], "Counsel advises; executives decide within assigned authority; the record preserves who knew and chose what.")
    chain("10-current-legal-timeline.png", "The Sullivan Case Is No Longer a Pending Appeal", "The January 2025 classroom expectation was superseded by later appellate and Supreme Court action", "DOJ, Ninth Circuit and Supreme Court records", [("2016–2023", ["Incident", "2022 conviction", "2023 probation"]), ("Mar 13, 2025", ["Ninth Circuit", "Conviction affirmed", "Panel opinion"]), ("Nov 12, 2025", ["Amended opinion", "En banc denied", "Judgment stands"]), ("Jun 29, 2026", ["Cert denied", "Supreme Court", "Case remains affirmed"])], "The lecture's nexus argument is historical advocacy, not the current procedural status.")
    grid("11-regulation-paths.png", "Cybersecurity Rules Arrive Through Multiple Channels", "Rulemaking, standards, supervision, enforcement and litigation create different kinds of guidance", "Transcript-grounded redraw · 03:20–09:10, 35:20–39:17", [("Legislation / rules", ["Prospective", "Public process", "Defined scope"]), ("Standards", ["NIST / CISA", "Practice guidance", "Flexible adoption"]), ("Supervision", ["Sector regulator", "Exams / orders", "Company-specific"]), ("Enforcement / courts", ["Past conduct", "Case facts", "Precedent / deterrence"])], "Organizations need a control map that links each obligation to owner, evidence and review date.")
    grid("12-executive-accountability.png", "Cybersecurity Accountability Is Shared but Not Diffuse", "CSO, general counsel, CEO and board need distinct authority and escalation duties", "Transcript-grounded redraw · 31:20–33:40", [("CSO", ["Technical risk", "Incident command", "Escalate facts"]), ("General counsel", ["Legal duties", "Privilege", "Regulatory advice"]), ("CEO", ["Enterprise risk", "Resources", "Disclosure decision"]), ("Board / committee", ["Oversight", "Material risk", "Challenge / record"])], "Shared responsibility must still name a final decision-maker for each class of action.")
    chain("13-security-maturity.png", "Security Teams Mature From Reactive Response to Embedded Governance", "People growth should unlock platforms, prevention and executive decision quality", "Transcript-grounded redraw · 00:00–03:20", [("Reactive", ["Small team", "Tickets", "Hero response"]), ("Program", ["IR / product security", "VDP", "Risk process"]), ("Platform", ["Identity / telemetry", "Automation", "Guardrails"]), ("Embedded", ["Product ownership", "Board metrics", "External coordination"])], "Headcount without platform and decision rights scales queues, not security outcomes.")
    chain("14-resilience-loop.png", "Resilience Includes Human Recovery and Renewed Service", "Support, reflection and purposeful work help leaders continue after prolonged incidents or litigation", "Transcript-grounded redraw · 25:20–31:20", [("Impact", ["Incident / case", "Reputation", "Role loss"]), ("Support", ["Family / peers", "Professional help", "Legal counsel"]), ("Recovery", ["Rest", "Perspective", "New routines"]), ("Service + learning", ["Community work", "Mentoring", "Better systems"])], "Resilience is not silent endurance; it is supported recovery that preserves judgment and health.")
    chain("15-government-talent.png", "Technical Talent Improves Policy Only When It Stays in the Loop", "Government needs implementation knowledge; industry needs legitimate public accountability", "Transcript-grounded redraw · 36:20–39:17", [("Technical expertise", ["Systems", "Threats", "Operational cost"]), ("Policy design", ["Rights", "Incentives", "Clear duties"]), ("Implementation", ["Agency capacity", "Metrics", "Enforcement"]), ("Industry feedback", ["Evidence", "Failure modes", "Revision"])], "Engagement does not mean avoiding regulation; it means making public rules more technically grounded and enforceable.")
    chain("16-tabletop.png", "A Tabletop Exercise Connects VDP, Incident and Disclosure Governance", "Teams should rehearse ambiguity before a real report arrives", "Repository exercise design", [("VDP report", ["Validate", "Sensitive data", "Researcher contact"]), ("Incident", ["Severity", "Contain", "Evidence"]), ("Governance", ["Materiality", "CEO / board", "Counsel"]), ("Notify + learn", ["Users / regulators", "Recovery", "Postmortem"])], "The exercise succeeds only if owners, evidence and clocks remain clear when facts change.")


if __name__ == "__main__":
    main()
