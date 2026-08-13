#!/usr/bin/env python3
"""Generate transcript-grounded teaching diagrams for CS153 Lecture 02."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1600
HEIGHT = 900
BACKGROUND = "#F7F3EA"
INK = "#1F2933"
MUTED = "#667085"
BLUE = "#DCEAF7"
BLUE_DARK = "#3E6C91"
GOLD = "#F1E5BD"
GOLD_DARK = "#8B6B1F"
RED = "#F4DCD7"
RED_DARK = "#A44D40"
GREEN = "#DCEBDD"
GREEN_DARK = "#4F7A55"
PURPLE = "#E6DDF2"
PURPLE_DARK = "#6E568E"
LINE = "#93A0AD"

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "images"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size)


TITLE_FONT = font(48)
SUBTITLE_FONT = font(24)
BODY_FONT = font(30)
SMALL_FONT = font(22)
LABEL_FONT = font(26)


def canvas(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((80, 55), title, fill=INK, font=TITLE_FONT)
    draw.text((82, 120), subtitle, fill=MUTED, font=SUBTITLE_FONT)
    draw.line((80, 165, WIDTH - 80, 165), fill=LINE, width=2)
    draw.text((80, HEIGHT - 52), source, fill=MUTED, font=SMALL_FONT)
    return image, draw


def rounded_box(
    draw: ImageDraw.ImageDraw,
    bounds: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    fill: str,
    outline: str,
    title_size: int = 30,
    body_size: int = 24,
) -> None:
    left, top, right, bottom = bounds
    draw.rounded_rectangle(bounds, radius=24, fill=fill, outline=outline, width=4)
    draw.text((left + 28, top + 24), title, fill=outline, font=font(title_size))
    cursor = top + 78
    body_font = font(body_size)
    for line in lines:
        draw.text((left + 28, cursor), line, fill=INK, font=body_font)
        cursor += body_size + 14


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = LINE,
    width: int = 6,
) -> None:
    draw.line((*start, *end), fill=color, width=width)
    end_x, end_y = end
    start_x, start_y = start
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    length = max((delta_x * delta_x + delta_y * delta_y) ** 0.5, 1)
    unit_x = delta_x / length
    unit_y = delta_y / length
    perpendicular_x = -unit_y
    perpendicular_y = unit_x
    arrow_length = 22
    arrow_width = 12
    first = (
        end_x - unit_x * arrow_length + perpendicular_x * arrow_width,
        end_y - unit_y * arrow_length + perpendicular_y * arrow_width,
    )
    second = (
        end_x - unit_x * arrow_length - perpendicular_x * arrow_width,
        end_y - unit_y * arrow_length - perpendicular_y * arrow_width,
    )
    draw.polygon([end, first, second], fill=color)


def save(image: Image.Image, filename: str) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT / filename, quality=92)


def origin_loop() -> None:
    image, draw = canvas(
        "Reddit's Original Product Loop",
        "Slashdot-style discussion + Delicious-style user ranking",
        "Transcript-grounded redraw · 00:00–05:00",
    )
    boxes = [
        ((100, 270, 410, 560), "Submit", ["Users add links", "or text posts"], BLUE, BLUE_DARK),
        ((500, 270, 810, 560), "Vote", ["Upvote / downvote", "changes visibility"], GOLD, GOLD_DARK),
        ((900, 270, 1210, 560), "Rank", ["Front page updates", "without editors"], GREEN, GREEN_DARK),
        ((590, 640, 1030, 790), "Discuss", ["Comments turn links into communities"], PURPLE, PURPLE_DARK),
    ]
    for bounds, title, lines, fill, outline in boxes:
        rounded_box(draw, bounds, title, lines, fill, outline)
    arrow(draw, (410, 415), (500, 415))
    arrow(draw, (810, 415), (900, 415))
    arrow(draw, (1055, 560), (980, 640))
    arrow(draw, (590, 715), (260, 560))
    save(image, "01-origin-product-loop.png")


def company_timeline() -> None:
    image, draw = canvas(
        "Twenty Years of Organizational Transitions",
        "The same product passed through startup, acquisition, spinout, crisis and public-company phases",
        "Transcript-grounded redraw · 05:00–10:00 and 37:30–39:30",
    )
    y_position = 440
    draw.line((130, y_position, 1470, y_position), fill=LINE, width=8)
    events = [
        (150, "2005", "YC S05", "Build + seed"),
        (410, "2006", "Acquired", "Advance / Condé Nast"),
        (670, "2009", "Founders leave", "Tiny operating team"),
        (930, "2012–14", "Spinout + funding", "External leadership"),
        (1190, "2015", "Huffman returns", "Policy + product rebuild"),
        (1450, "2024–25", "Public company", "Scale + accountability"),
    ]
    for x_position, year, label, detail in events:
        draw.ellipse((x_position - 16, y_position - 16, x_position + 16, y_position + 16), fill=BLUE_DARK)
        draw.text((x_position - 55, y_position - 105), year, fill=BLUE_DARK, font=LABEL_FONT)
        draw.text((x_position - 95, y_position + 38), label, fill=INK, font=SMALL_FONT)
        draw.text((x_position - 105, y_position + 75), detail, fill=MUTED, font=font(18))
    save(image, "02-company-timeline.png")


def governance_stack() -> None:
    image, draw = canvas(
        "Community Governance Is a Layered System",
        "Voting alone cannot handle every abuse mode at internet scale",
        "Transcript-grounded redraw · 08:30–15:00",
    )
    layers = [
        (220, "Site-wide policy", "Minimum safety and legality rules", RED, RED_DARK),
        (350, "Platform enforcement", "Warnings, restrictions, suspensions", GOLD, GOLD_DARK),
        (480, "Subreddit rules + moderators", "Local norms and context-sensitive decisions", BLUE, BLUE_DARK),
        (610, "Voting and participation", "Users rank, discuss and report content", GREEN, GREEN_DARK),
    ]
    for top, title, detail, fill, outline in layers:
        rounded_box(draw, (250, top, 1350, top + 105), title, [detail], fill, outline, body_size=22)
    draw.text((95, 390), "More global\nless contextual", fill=RED_DARK, font=SMALL_FONT)
    draw.text((85, 650), "More local\nmore contextual", fill=GREEN_DARK, font=SMALL_FONT)
    save(image, "03-governance-stack.png")


def policy_design() -> None:
    image, draw = canvas(
        "Policy Design: Specific Enough, Flexible Enough",
        "Steve Huffman's phrase: 'specifically vague'",
        "Transcript-grounded redraw · 13:40–16:00",
    )
    rounded_box(draw, (120, 260, 680, 650), "Too specific", ["Clear literal tests", "Easy to game at edges", "Rules grow without bound"], RED, RED_DARK)
    rounded_box(draw, (920, 260, 1480, 650), "Too vague", ["Hard to predict", "Inconsistent enforcement", "Weak legitimacy"], PURPLE, PURPLE_DARK)
    rounded_box(draw, (610, 330, 990, 590), "Working zone", ["Concrete harm", "Room for context", "Explain precedents"], GREEN, GREEN_DARK)
    arrow(draw, (680, 455), (610, 455), RED_DARK)
    arrow(draw, (920, 505), (990, 505), PURPLE_DARK)
    save(image, "04-policy-specificity.png")


def enforcement_ladder() -> None:
    image, draw = canvas(
        "Enforcement Should Be a Ladder, Not a Single Switch",
        "Match intervention strength to harm, repetition and cooperation",
        "Transcript-grounded redraw · 16:00–20:00",
    )
    steps = [
        (130, 650, "1", "Explain", "Rule + evidence"),
        (390, 550, "2", "Warn", "Record notice"),
        (650, 450, "3", "Timeout", "Temporary limits"),
        (910, 350, "4", "Suspend", "User/community"),
        (1170, 250, "5", "Remove", "Severe or repeated harm"),
    ]
    for left, top, number, label, detail in steps:
        rounded_box(draw, (left, top, left + 240, top + 150), f"{number}. {label}", [detail], BLUE if number in {"1", "2"} else GOLD if number == "3" else RED, BLUE_DARK if number in {"1", "2"} else GOLD_DARK if number == "3" else RED_DARK, title_size=26, body_size=20)
    draw.text((105, 210), "Escalate only when needed", fill=MUTED, font=BODY_FONT)
    arrow(draw, (260, 620), (1280, 235), LINE, width=5)
    save(image, "05-enforcement-ladder.png")


def data_access() -> None:
    image, draw = canvas(
        "Open Content Still Needs Access Boundaries",
        "Human reading, search indexing, research, product APIs and model training impose different costs",
        "Transcript-grounded redraw · 22:00–27:30",
    )
    categories = [
        ((80, 280, 370, 620), "Humans", ["Web / app", "See community context"], GREEN, GREEN_DARK),
        ((410, 280, 700, 620), "Search", ["Index + link back", "Traffic exchange"], BLUE, BLUE_DARK),
        ((740, 280, 1030, 620), "Developers", ["Bots / tools", "Rate limits + API"], GOLD, GOLD_DARK),
        ((1070, 280, 1360, 620), "AI training", ["Bulk extraction", "License + safeguards"], RED, RED_DARK),
    ]
    for bounds, title, lines, fill, outline in categories:
        rounded_box(draw, bounds, title, lines, fill, outline, title_size=28, body_size=22)
    draw.text((250, 700), "Same public corpus", fill=INK, font=BODY_FONT)
    arrow(draw, (520, 720), (1120, 720), LINE)
    draw.text((650, 750), "increasing scale, substitution and infrastructure cost", fill=MUTED, font=SMALL_FONT)
    save(image, "06-data-access-boundaries.png")


def paid_communities() -> None:
    image, draw = canvas(
        "Paid Communities Add a Second Value Loop",
        "Subscription can fund expertise, but it changes moderation and access incentives",
        "Transcript-grounded redraw · 27:50–32:30",
    )
    rounded_box(draw, (110, 270, 430, 590), "Members", ["Pay for access", "Expect trust + value"], BLUE, BLUE_DARK)
    rounded_box(draw, (640, 210, 960, 530), "Community", ["Knowledge", "Moderation", "Identity"], GREEN, GREEN_DARK)
    rounded_box(draw, (1170, 270, 1490, 590), "Moderators / creators", ["Invest labor", "Share revenue"], GOLD, GOLD_DARK)
    arrow(draw, (430, 390), (640, 350), BLUE_DARK)
    arrow(draw, (960, 350), (1170, 390), GREEN_DARK)
    arrow(draw, (1330, 590), (800, 700), GOLD_DARK)
    arrow(draw, (800, 700), (270, 590), GOLD_DARK)
    draw.text((650, 735), "Revenue must not buy rule immunity", fill=RED_DARK, font=LABEL_FONT)
    save(image, "07-paid-community-loop.png")


def api_economics() -> None:
    image, draw = canvas(
        "API Economics: Preserve the Ecosystem, Price Industrial Use",
        "The hard part is separating community tools from businesses that substitute for the platform",
        "Transcript-grounded redraw · 32:55–38:00",
    )
    rounded_box(draw, (90, 260, 420, 650), "Moderation bots", ["Community labor", "High public value", "Keep accessible"], GREEN, GREEN_DARK)
    rounded_box(draw, (475, 260, 805, 650), "Research / hobby", ["Bounded volume", "Non-substitutive", "Rate limited"], BLUE, BLUE_DARK)
    rounded_box(draw, (860, 260, 1190, 650), "Third-party clients", ["User experience", "May replace ads", "Needs contract"], GOLD, GOLD_DARK)
    rounded_box(draw, (1245, 260, 1570, 650), "Bulk commercial use", ["High volume", "Model/data value", "Paid access"], RED, RED_DARK)
    draw.text((150, 720), "Access policy", fill=INK, font=BODY_FONT)
    arrow(draw, (330, 735), (1380, 735), LINE)
    draw.text((600, 770), "free / protected → negotiated / paid", fill=MUTED, font=LABEL_FONT)
    save(image, "08-api-economics.png")


def traffic_resilience() -> None:
    image, draw = canvas(
        "Traffic Resilience: Absorb, Divert, Degrade",
        "A community platform must survive unpredictable events without preserving every feature",
        "Transcript-grounded redraw · 40:00–43:20",
    )
    rounded_box(draw, (90, 290, 390, 610), "1. Absorb", ["Elastic capacity", "Caches", "Queues"], GREEN, GREEN_DARK)
    rounded_box(draw, (500, 290, 800, 610), "2. Divert", ["Multi-region", "Multi-cloud", "Traffic steering"], BLUE, BLUE_DARK)
    rounded_box(draw, (910, 290, 1210, 610), "3. Degrade", ["Read-only mode", "Disable costly paths", "Protect core"], GOLD, GOLD_DARK)
    rounded_box(draw, (1320, 290, 1530, 610), "4. Recover", ["Replay", "Reconcile", "Learn"], PURPLE, PURPLE_DARK, title_size=26, body_size=20)
    arrow(draw, (390, 450), (500, 450))
    arrow(draw, (800, 450), (910, 450))
    arrow(draw, (1210, 450), (1320, 450))
    save(image, "09-traffic-resilience.png")


def user_modes() -> None:
    image, draw = canvas(
        "Two User Modes, Two Product Contracts",
        "AI changes information retrieval faster than it changes human-to-human participation",
        "Transcript-grounded redraw · 43:30–45:10",
    )
    rounded_box(draw, (130, 250, 720, 680), "Scrollers", ["Come for communities", "Talk with humans", "Identity + belonging", "Feed and conversation"], GREEN, GREEN_DARK)
    rounded_box(draw, (880, 250, 1470, 680), "Seekers", ["Arrive with a question", "Want recent lived experience", "Often enter through search", "Need evidence links"], BLUE, BLUE_DARK)
    draw.text((670, 730), "same corpus · different intent", fill=MUTED, font=LABEL_FONT)
    save(image, "10-scrollers-seekers.png")


def reddit_answers() -> None:
    image, draw = canvas(
        "Reddit Answers: Retrieval Before Summarization",
        "The answer is useful only if readers can return to the underlying comments",
        "Transcript-grounded redraw · 45:00–46:10",
    )
    labels = [
        ((80, 310, 350, 570), "Question", ["Subjective intent"], BLUE, BLUE_DARK),
        ((430, 310, 700, 570), "Retrieve", ["Posts + comments"], GREEN, GREEN_DARK),
        ((780, 310, 1050, 570), "Summarize", ["LLM synthesis"], GOLD, GOLD_DARK),
        ((1130, 310, 1500, 570), "Cite", ["Link claims back", "to comments"], PURPLE, PURPLE_DARK),
    ]
    for bounds, title, lines, fill, outline in labels:
        rounded_box(draw, bounds, title, lines, fill, outline, title_size=28, body_size=22)
    arrow(draw, (350, 440), (430, 440))
    arrow(draw, (700, 440), (780, 440))
    arrow(draw, (1050, 440), (1130, 440))
    draw.text((470, 670), "Grounding preserves disagreement and source context", fill=RED_DARK, font=LABEL_FONT)
    save(image, "11-reddit-answers-rag.png")


def agent_access() -> None:
    image, draw = canvas(
        "Agent Access Needs a New Contract",
        "Web scraping is an accidental interface; a durable agent API must align cost, attribution and value",
        "Transcript-grounded redraw · 46:10–48:22",
    )
    rounded_box(draw, (100, 250, 470, 650), "Platform", ["Community corpus", "Infra cost", "Safety rules", "Business model"], BLUE, BLUE_DARK)
    rounded_box(draw, (615, 250, 985, 650), "Agent API", ["Identity", "Rate + scope", "Attribution", "Settlement"], GOLD, GOLD_DARK)
    rounded_box(draw, (1130, 250, 1500, 650), "Agents", ["Browse + act", "Serve users", "Create demand", "May bypass ads"], PURPLE, PURPLE_DARK)
    arrow(draw, (470, 410), (615, 410), BLUE_DARK)
    arrow(draw, (985, 410), (1130, 410), PURPLE_DARK)
    arrow(draw, (1130, 535), (985, 535), GREEN_DARK)
    arrow(draw, (615, 535), (470, 535), GREEN_DARK)
    draw.text((555, 710), "Open by default, bounded by sustainability", fill=GREEN_DARK, font=LABEL_FONT)
    save(image, "12-agent-access-contract.png")


def main() -> None:
    origin_loop()
    company_timeline()
    governance_stack()
    policy_design()
    enforcement_ladder()
    data_access()
    paid_communities()
    api_economics()
    traffic_resilience()
    user_modes()
    reddit_answers()
    agent_access()


if __name__ == "__main__":
    main()
