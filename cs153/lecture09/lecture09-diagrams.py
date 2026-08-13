#!/usr/bin/env python3
"""Generate teaching diagrams for CS153 Lecture 09."""

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
    chain("01-transition-window.png", "Technology Transitions Create New Control Points", "Cloud adoption changed application boundaries and exposed identity fragmentation", "Transcript-grounded redraw · 00:00–05:20", [("Old model", ["On-prem apps", "Local directories", "Network perimeter"]), ("Transition", ["SaaS sprawl", "Remote access", "Many credentials"]), ("Focused wedge", ["Single sign-on", "Immediate buyer pain", "Measurable value"]), ("New platform", ["Identity control plane", "Policy + lifecycle", "Cross-app trust"])], "A transition creates opportunity only when a narrow use case can grow into durable infrastructure.")
    chain("02-identity-control-plane.png", "Identity Becomes a Shared Control Plane", "A centralized identity layer connects sources, policy, applications and evidence", "Transcript + Okta Universal Directory", [("Identity sources", ["HR / directory", "Partners", "Customer signup"]), ("Directory", ["Principal profile", "Groups / attributes", "Lifecycle state"]), ("Policy engine", ["Authentication", "Authorization", "Assurance"]), ("Apps + audit", ["Sessions", "Provisioning", "System log"])], "The login page is the surface; the durable product is a policy and state platform.")
    grid("03-identity-lifecycle.png", "Identity Infrastructure Covers More Than Login", "Authentication, authorization, provisioning and audit solve different lifecycle problems", "Okta/OIDC/SCIM concepts", [("Authentication", ["Who is the principal?", "Authenticator", "Assurance level"]), ("Authorization", ["What may it do?", "Resource / action", "Policy decision"]), ("Provisioning", ["Create / update", "Entitlements", "Deprovision"]), ("Session + audit", ["Continuity", "Revocation", "Evidence trail"])], "SSO improves entry; lifecycle correctness determines long-term access safety.")
    grid("04-front-door-reliability.png", "Identity Is a Front Door With a Large Blast Radius", "Availability, latency, consistency and safe change all matter at authentication scale", "Transcript 04:00–06:10, 14:40–16:40", [("Availability", ["Multi-zone", "Failover", "Dependency isolation"]), ("Latency", ["p95 / p99", "Redirect chain", "MFA step"]), ("Correctness", ["Policy version", "Directory freshness", "Session state"]), ("Change safety", ["Canary", "Rollback", "Audit / SLO"])], "A fast but incorrect allow is a security failure; a secure but unavailable login is a business outage.")
    chain("05-access-request-path.png", "Every Access Request Is a Policy Decision", "Identity, device, application and risk context determine assurance and session outcome", "Okta Identity Engine + NIST Zero Trust", [("Request", ["Principal", "Device / network", "Target app"]), ("Context", ["Profile / group", "Risk signal", "Session history"]), ("Policy", ["Allow / deny", "Step-up", "Authenticator"]), ("Outcome", ["Session / token", "App access", "Audit event"])], "Zero Trust is repeated verification and least privilege, not a product checkbox.")
    chain("06-founder-adaptation.png", "Founder Transition Resets Resources and Certainty", "Operating with no inherited staff or status requires a new progress loop", "Transcript-grounded redraw · 06:00–12:20", [("Resource reset", ["No team", "No brand", "No admin"]), ("Daily evidence", ["Customer calls", "Prototype", "Buyer signal"]), ("Low odds", ["Unknown market", "Limited runway", "Frequent rejection"]), ("Team belief", ["Honest uncertainty", "Clear direction", "Visible progress"])], "Belief is not denial of probability; it is the ability to act while uncertainty remains explicit.")
    chain("07-ceo-board-loop.png", "CEO and Board Need an Unfiltered Information Loop", "Bad news must become options, decisions and accountable follow-through", "Transcript-grounded redraw · 12:00–14:40", [("Operating truth", ["Metrics", "Customer risk", "Bad news"]), ("CEO synthesis", ["Root causes", "Trade-offs", "Options"]), ("Board decision", ["Challenge", "Capital / risk", "Decision rights"]), ("Follow-through", ["Owner", "Milestone", "Revisit"])], "Protecting the board from bad news isolates the CEO and delays corrective action.")
    chain("08-incident-response.png", "Security Incidents Must Close a Learning Loop", "Detection, containment, investigation, remediation and notification require different evidence", "Transcript 15:20–19:10 + Okta 2023 RCA", [("Detect", ["Customer signal", "Telemetry", "Anomaly"]), ("Contain", ["Disable account", "Revoke sessions", "Limit access"]), ("Investigate", ["Timeline", "Log gaps", "Affected scope"]), ("Remediate + notify", ["Control changes", "Customer actions", "Public RCA"])], "A single credential error matters, but durable remediation fixes the system that allowed and hid it.")
    grid("09-security-first-culture.png", "Security-First Culture Is an Operating System", "Leader behavior, incentives, resources and evidence make priorities real", "Transcript-grounded redraw · 18:00–21:30", [("Leader behavior", ["Ask first", "Model escalation", "Accept bad news"]), ("Incentives", ["Goals", "Promotion", "Launch criteria"]), ("Resources", ["Security staff", "Platform work", "Customer support"]), ("Evidence", ["Control tests", "Incidents", "Audit / review"])], "Culture is what leaders repeatedly reward, fund, delay and disclose—not a list of values.")
    grid("10-shared-defense.png", "Attackers Need One Gap; Defenders Coordinate Many Controls", "Identity defense improves when telemetry and lessons can cross organizational boundaries", "Transcript-grounded redraw · 21:20–24:10", [("Attacker", ["One credential", "One session", "One weak workflow"]), ("Defender", ["Endpoint", "Identity", "App / data"]), ("Shared signals", ["Indicators", "Session risk", "Customer reports"]), ("Constraints", ["Privacy", "Legal rules", "Interoperability"])], "Shared signals reduce repeated discovery, but access and purpose limits remain mandatory.")
    chain("11-zero-trust-policy.png", "Zero Trust Turns Context Into Continuous Policy", "Assurance can change before, during and after the first login", "NIST SP 800-207 + Okta policy model", [("Identify", ["Principal", "Authenticator", "Enrollment"]), ("Evaluate", ["Device", "Network", "Risk"]), ("Enforce", ["Least privilege", "Step-up", "Deny"]), ("Re-evaluate", ["Session risk", "Universal logout", "Audit"])], "The perimeter does not disappear; trust becomes explicit, contextual and revocable.")
    chain("12-agent-delegation.png", "AI Agents Need Delegated Identity, Not Shared User Secrets", "The system must preserve who authorized the agent, for what audience and scope", "Transcript 24:10–27:50 + OAuth token exchange", [("User / owner", ["Intent", "Consent", "Accountability"]), ("Agent principal", ["Own identity", "Workload attestation", "Task context"]), ("Authorization", ["Delegation", "Scope / audience", "Short expiry"]), ("Tool / audit", ["Policy check", "Action", "Trace / revoke"])], "An agent acting for a user should not inherit every credential the user or laptop can access.")
    chain("13-token-lifecycle.png", "Tokens Are Temporary Capabilities With a Lifecycle", "Issuance, binding, use, rotation, revocation and retirement must be observable", "OAuth/OIDC/WebAuthn concepts", [("Issue", ["Authenticated principal", "Audience", "Scope"]), ("Bind", ["Device / key", "Sender constraint", "Session"]), ("Use", ["Resource check", "Least privilege", "Trace ID"]), ("Revoke / retire", ["Risk event", "Job complete", "Owner removed"])], "Long-lived bearer tokens convert one machine compromise into broad, persistent access.")
    grid("14-two-platform-acquisition.png", "Acquisitions Must Respect Product and Infrastructure Boundaries", "Workforce identity and developer customer identity share primitives but differ in users and workflows", "Transcript 30:00–36:20 + Okta/Auth0 acquisition sources", [("Workforce identity", ["Employees", "IT administration", "Enterprise apps"]), ("Customer identity", ["Product users", "Developer integration", "Custom UX"]), ("Shared primitives", ["Directory", "Auth protocols", "Security / scale"]), ("Integration seams", ["Roadmap", "Sales / support", "Platform migration"])], "Combining companies is not the same as immediately merging every runtime, team and customer workflow.")
    chain("15-trust-flywheel.png", "Identity Adoption Compounds Through Evidence of Trust", "Reliability, security, transparency and customer outcomes reinforce each other", "Transcript-grounded redraw · 27:30–35:20", [("Reliable service", ["Front door works", "Predictable change", "Fast recovery"]), ("Security evidence", ["Controls", "RCA", "Customer guidance"]), ("Customer trust", ["Early reference", "Broader deployment", "Renewal"]), ("Platform depth", ["More integrations", "More context", "Better policy"])], "Trust is earned by repeatable evidence and honest recovery, not by claiming incidents never happen.")
    chain("16-ai-adoption-curve.png", "Novelty Apps Precede Category-Defining AI Workflows", "Technical potential becomes durable value only after workflow and organization redesign", "Transcript-grounded redraw · 36:00–39:02", [("Capability shock", ["New model", "Broad attention", "Unclear use"]), ("Mr. T phase", ["Novel demos", "Thin workflow", "Low switching cost"]), ("Killer workflow", ["New task shape", "Compounding data", "Clear outcome"]), ("Organization redesign", ["Roles", "Controls", "Operating model"])], "Incumbent inertia can delay value even when the underlying technology is genuinely important.")


if __name__ == "__main__":
    main()
