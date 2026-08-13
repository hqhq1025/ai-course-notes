#!/usr/bin/env python3
"""Generate non-sensitive teaching diagrams for CS153 Lecture 08."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1600, 900
BG, INK, MUTED, LINE = "#F7F3EA", "#1F2933", "#667085", "#93A0AD"
COLORS = [("#DCEAF7", "#3E6C91"), ("#F1E5BD", "#8B6B1F"), ("#E6DDF2", "#6E568E"), ("#DCEBDD", "#4F7A55"), ("#F4DCD7", "#A44D40")]
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "images"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size)


def base(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.text((80, 52), title, fill=INK, font=f(43))
    draw.text((82, 116), subtitle, fill=MUTED, font=f(21))
    draw.line((80, 164, WIDTH - 80, 164), fill=LINE, width=2)
    draw.text((80, HEIGHT - 48), source, fill=MUTED, font=f(18))
    return image, draw


def node(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, lines: list[str], color: tuple[str, str]) -> None:
    left, top, right, bottom = rect
    fill, border = color
    draw.rounded_rectangle(rect, radius=22, fill=fill, outline=border, width=4)
    draw.text((left + 22, top + 18), title, fill=border, font=f(24))
    y = top + 66
    for line in lines:
        draw.text((left + 22, y), line, fill=INK, font=f(18))
        y += 31


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = LINE) -> None:
    draw.line((*start, *end), fill=color, width=6)
    draw.polygon([(end[0], end[1]), (end[0] - 22, end[1] - 12), (end[0] - 22, end[1] + 12)], fill=color)


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
    draw.text((80, 745), footer, fill="#A44D40", font=f(21))
    save(image, name)


def grid(name: str, title: str, subtitle: str, source: str, items: list[tuple[str, list[str]]], footer: str) -> None:
    image, draw = base(title, subtitle, source)
    rects = [(90, 220, 750, 430), (850, 220, 1510, 430), (90, 500, 750, 710), (850, 500, 1510, 710)]
    for index, ((label, lines), rect) in enumerate(zip(items, rects)):
        node(draw, rect, label, lines, COLORS[index])
    draw.text((80, 770), footer, fill="#A44D40", font=f(21))
    save(image, name)


def main() -> None:
    chain("01-response-pipeline.png", "Child-Safety Technology Is an End-to-End Response Pipeline", "Detection is only the first stage; review, action and reporting need clear owners", "Transcript-grounded redraw · 00:00–05:50", [("Platform signal", ["Upload / message", "User report", "Behavior event"]), ("Detection + triage", ["Known match", "Predictive score", "Priority queue"]), ("Human action", ["Review", "Remove / restrict", "Preserve evidence"]), ("Reporting handoff", ["Reporting agency", "Victim identification", "Investigation"])], "A classifier does not itself determine illegality, identity or investigative outcome.")
    grid("02-scale-funnel.png", "Reporting Volume and File Volume Are Different Measures", "Duplicates, bundles and novel material change investigator workload", "Transcript + NCMEC dated reporting context · 03:20–05:50", [("Reports", ["Platform submissions", "May bundle files", "Different incidents"]), ("Files", ["Images / videos", "Repeated circulation", "Different counts"]), ("Novel candidates", ["No known hash", "Require prediction", "Need verification"]), ("Scarce review", ["Moderator time", "Investigator priority", "Victim identification"])], "Compare years only after checking definitions, bundling rules and duplicate handling.")
    chain("03-hash-matching.png", "Hash Matching Is the Minimum Scalable Defense for Known Material", "Cryptographic identity and perceptual similarity solve different matching cases", "Transcript 05:10–06:00 · Thorn Safer Match", [("Verified reference", ["Trusted hash set", "Known material", "Access controlled"]), ("File fingerprint", ["Cryptographic hash", "Perceptual hash", "Video scene hash"]), ("Match policy", ["Exact / similarity", "Threshold", "Versioned list"]), ("Platform action", ["Block / quarantine", "Review", "Report workflow"])], "Hashes reduce viewing and repeated circulation; they do not detect every new file.")
    chain("04-predictive-classifier.png", "Predictive AI Extends Coverage Beyond Known Hashes", "Scores prioritize suspected novel material for trained human review", "Transcript 10:10–13:40 · Thorn Safer Predict", [("Unseen content", ["No trusted match", "Image / video / text", "Platform context"]), ("Classifier", ["Risk score", "Model version", "Calibrated threshold"]), ("Review queue", ["Priority", "Context labels", "Minimum exposure"]), ("Verified outcome", ["Action / report", "Feedback", "Possible new hash"])], "A predictive score is a triage signal, not a legal finding or standalone enforcement decision.")
    chain("05-moderator-triage.png", "Triage Should Maximize Protection While Minimizing Human Exposure", "Priority and case packaging reduce unnecessary review of traumatic material", "Transcript-grounded redraw · 13:40–16:20", [("Signals", ["Hash / score", "Account history", "User report"]), ("Priority", ["Severity context", "Confidence", "Child-at-risk signal"]), ("Protected review", ["Blur / reveal control", "Limited access", "Wellbeing support"]), ("Case package", ["Decision log", "Required report", "Escalation"])], "Moderator safety, access control and decision quality are all first-class system metrics.")
    grid("06-trusted-data.png", "High-Risk Training Data Requires Exceptional Governance", "Trusted access, provenance, segregation and retention matter as much as model choice", "Transcript-grounded redraw · 16:20–20:30", [("Trusted source", ["Authorized partner", "Verified labels", "Purpose limitation"]), ("Provenance", ["Source / date", "Label history", "Chain of custody"]), ("Segregation", ["Restricted environment", "Least privilege", "No casual access"]), ("Retention + audit", ["Deletion schedule", "Access log", "Incident response"])], "Training quality cannot justify uncontrolled copying or broad internal access.")
    grid("07-genai-threat-surface.png", "Generative AI Creates Risk Across the Full Supply Chain", "Training, model access, application design and downstream sharing need different controls", "Transcript 05:45–10:20 · Thorn Safety by Design", [("Development", ["Training data", "Model behavior", "Red teaming"]), ("Model access", ["Open / closed", "Fine-tuning", "Abuse resistance"]), ("Application", ["Prompt / upload", "Output filters", "User identity"]), ("Distribution", ["Hosting", "Search / sharing", "Reporting / removal"])], "No single watermark, classifier or policy controls every layer and modality.")
    chain("08-safety-lifecycle.png", "Safety by Design Is a Development, Deployment and Maintenance Discipline", "Controls must survive model updates, new modalities and changing misuse patterns", "Thorn Safety by Design + NIST GAI profile", [("Develop", ["Data policy", "Threat model", "Red-team / eval"]), ("Deploy", ["Input / output controls", "Identity / rate limits", "Human escalation"]), ("Monitor", ["Abuse telemetry", "Incident reports", "External signals"]), ("Maintain", ["Patch models", "Retest", "Publish progress"])], "A launch checklist is insufficient; safety needs continuous evidence and accountable ownership.")
    chain("09-platform-integration.png", "Platform Integration Must Be Fast, Idempotent and Auditable", "Upload and messaging paths need deterministic action and safe reporting handoff", "Transcript-grounded redraw · 10:10–24:10", [("Ingress", ["Upload / batch", "Message stream", "Tenant policy"]), ("Detection service", ["Match / predict", "Timeout / retry", "Version"]), ("Decision service", ["Quarantine", "Review queue", "User action"]), ("Audit + report", ["Evidence reference", "Idempotent report", "Status tracking"])], "Retries must not duplicate reports or lose the link between model evidence and human decision.")
    grid("10-evaluation-queue.png", "Model Quality and Review Capacity Must Be Designed Together", "Precision, recall and calibration determine how many alerts humans can safely process", "Transcript + Thorn/NIST evaluation context", [("Recall", ["Find true cases", "Avoid missed risk", "Broader threshold"]), ("Precision", ["Reduce false alerts", "Protect review capacity", "Narrower threshold"]), ("Calibration", ["Score matches risk", "Stable by segment", "Monitor drift"]), ("Queue capacity", ["Reviewers / SLO", "Priority", "Backlog limits"] )], "A threshold is an operations decision, not only a model metric.")
    grid("11-privacy-layers.png", "Privacy and Child Safety Require Layered Controls", "Content confidentiality, metadata, endpoints and governance expose different signals and risks", "Transcript-grounded redraw · 28:40–31:10", [("Content", ["Encryption", "Access authorization", "Minimum viewing"]), ("Metadata", ["Account / device", "Traffic pattern", "Retention limits"]), ("Endpoint / platform", ["Upload policy", "User reports", "Client security"]), ("Governance", ["Legal process", "Audit", "Appeal / oversight"])], "Encryption is essential, but no single layer resolves every privacy, safety and accountability question.")
    chain("12-text-risk.png", "Text-Risk Detection Needs Conversation Context and Escalation", "Early-warning models should support intervention without treating probability as guilt", "Transcript 31:10–32:50 · Safer Predict text context", [("Conversation", ["Sequence / context", "Age / access signals", "Policy scope"]), ("Risk model", ["Labels", "Confidence", "Language / drift"]), ("Escalation", ["Safety prompt", "Limit contact", "Review queue"]), ("Human decision", ["Context review", "Proportionate action", "Report if required"])], "False positives can harm users; false negatives can miss urgent risk, so escalation must be tiered.")
    chain("13-network-analysis.png", "Coordinated Harm Is Easier to See as a Behavior Graph", "Accounts, devices, contact patterns and shared infrastructure reveal network structure", "Transcript-grounded redraw · 31:50–33:10", [("Entities", ["Accounts", "Devices", "Payment / network"]), ("Edges", ["Contact pattern", "Shared artifact", "Creation timing"]), ("Graph signal", ["Community", "Repeated playbook", "Central coordinator"]), ("Coordinated action", ["Investigate cluster", "Disrupt network", "Monitor recurrence"])], "Graph correlation supports prioritization; it still requires policy, evidence and human review.")
    chain("14-prevention-ladder.png", "Prevention Requires More Than Post-Upload Removal", "Product guardrails, disruption, education and support reduce risk at different stages", "Transcript-grounded redraw · 33:10–35:30", [("Detect", ["Match / predict", "User reporting", "Early warning"]), ("Disrupt", ["Limit contact", "Remove network", "Rate / identity controls"]), ("Protect", ["Age-aware defaults", "Safety prompts", "Recovery support"]), ("Educate", ["Family dialogue", "Digital literacy", "Trusted resources"])], "Software can reduce opportunity and speed response; it cannot replace education, care or justice systems.")
    chain("15-startup-maturity.png", "Startups Need a Minimum Viable Safety Path", "Safety maturity should grow with user-generated content, messaging and model capability", "Transcript-grounded redraw · 35:20–37:20", [("Risk inventory", ["Uploads / messages", "Minors / reach", "Model misuse"]), ("Minimum controls", ["Known-hash API", "User report", "Incident owner"]), ("Managed program", ["Predictive triage", "Moderator process", "Audit / metrics"]), ("Proactive prevention", ["Threat research", "Graph / text signals", "Safety by Design"])], "Early integration is cheaper and safer than cleaning a platform after harmful communities take root.")
    chain("16-ecosystem-roles.png", "Child-Safety Outcomes Depend on Clear Ecosystem Roles", "Platforms, safety technology, reporting agencies and investigators solve different problems", "Transcript-grounded redraw · 37:10–37:53", [("Platform", ["Detect / act", "Preserve evidence", "User safeguards"]), ("Safety technology", ["Hash / classifier", "Workflow tooling", "Threat expertise"]), ("Reporting agency", ["Receive / triage", "Route reports", "Data quality"]), ("Law enforcement", ["Identify victims", "Investigate", "Protect / prosecute"])], "The platform cannot outsource its safety controls, and technology providers do not replace investigators.")


if __name__ == "__main__":
    main()
