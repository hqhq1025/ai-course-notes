#!/usr/bin/env python3
"""Generate teaching diagrams for CS153 Lecture 10."""

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
    chain("01-scaling-program.png", "Frontier Scaling Is a Coupled Program, Not One Training Run", "Demand, capability, compute and reliability create reinforcing constraints", "Transcript-grounded redraw · 00:00–01:00", [("Demand", ["Users / API", "Coding growth", "Latency SLO"]), ("Capability", ["Model quality", "Post-training", "Tool use"]), ("Compute", ["Training clusters", "Inference fleet", "Data pipeline"]), ("Reliability", ["Capacity", "Recovery", "Product contract"])], "Growth can fund scaling, but it also raises the cost of outages, regressions and unsafe releases.")
    chain("02-scaling-hypothesis.png", "Scaling Laws Turn an Observation Into a Testable Program", "Small models and internet data provide evidence before the largest commitment", "Transcript 01:00–05:40 + GPT-2/GPT-3", [("Field signal", ["ImageNet", "GPT-2", "Broad transfer"]), ("Hypothesis", ["More compute", "More data", "Larger model"]), ("Pilot runs", ["Multiple scales", "Controlled recipe", "Measure loss"]), ("Frontier run", ["Forecast", "Allocate compute", "Validate residuals"])], "A scaling law is useful because it predicts before the expensive run, not because every curve is eternal.")
    grid("03-scaling-law-fit.png", "A Scaling Law Is a Fit With Residuals and Boundaries", "Log-log linearity helps extrapolation, but data quality and regime changes can break it", "Kaplan et al. 2020 + transcript 06:20–11:50", [("Axes", ["Compute / data / params", "Cross-entropy loss", "Log scale"]), ("Fit", ["Power-law slope", "Irreducible term", "Confidence"]), ("Residuals", ["Recipe change", "Data shift", "Optimization issue"]), ("Decision", ["Budget", "Model/data mix", "Stop / redesign"])], "A clean line does not prove the same exponent survives a new architecture, modality or post-training regime.")
    grid("04-compute-allocation.png", "Compute Allocation Is a Portfolio of Multipliers", "Architecture, data, optimizer and systems improvements can change effective capability per FLOP", "Transcript-grounded redraw · 12:00–15:20", [("Model", ["Architecture", "Context", "Sparsity"]), ("Data", ["Quality", "Mixture", "Dedup / curriculum"]), ("Optimization", ["Optimizer", "Schedule", "Stability"]), ("Systems", ["Parallelism", "Kernels", "Utilization"])], "Secret multipliers matter competitively, but the program still needs reproducible internal evidence.")
    grid("05-training-failure-domains.png", "Frontier Training Couples Many Failure Domains", "Workers, accelerators, network, storage and orchestration can each halt useful progress", "Transcript-grounded redraw · 15:00–17:20", [("Workers", ["GPU / TPU", "Host", "Process"]), ("Network", ["Collectives", "Congestion", "Partition"]), ("Storage", ["Dataset", "Checkpoint", "Throughput"]), ("Scheduler", ["Membership", "Restart", "Capacity quota"])], "At large scale, rare component failures become normal operating events.")
    grid("06-training-observability.png", "Training Observability Needs Four Telemetry Planes", "Model, optimizer, data and system signals explain different anomalies", "Transcript-grounded redraw · 17:20–20:10", [("Model", ["Loss", "Gradient", "Activation"]), ("Optimizer", ["LR / moments", "Update norm", "Overflow"]), ("Data", ["Batch source", "Token mix", "Corruption"]), ("System", ["Utilization", "Network", "Storage / errors"])], "A loss spike is an alert; diagnosis requires synchronized evidence from all four planes.")
    chain("07-checkpoint-recovery.png", "Checkpoint Recovery Must Preserve Scientific Meaning", "Rollback, replay and diagnosis should distinguish transient faults from recipe defects", "Transcript-grounded redraw · 17:20–19:10", [("Detect", ["Spike / stall", "NaN", "Worker failure"]), ("Checkpoint", ["Parameters", "Optimizer state", "Data cursor"]), ("Replay", ["Same batch", "Same code", "Controlled seed"]), ("Resume / fix", ["Transient retry", "Patch recipe", "Document incident"])], "A run that resumes but changes data order or optimizer state may no longer test the same hypothesis.")
    chain("08-follow-the-sun.png", "Training Operations Need Explicit Global Handoffs", "Follow-the-sun coverage reduces idle time only when ownership and evidence transfer cleanly", "Transcript-grounded redraw · 19:00–21:20", [("Active owner", ["Run status", "Current hypothesis", "Risk"]), ("Handoff packet", ["Timeline", "Dashboards", "Pending action"]), ("Next region", ["Acknowledge", "Verify", "Operate"]), ("Escalation", ["Research owner", "Systems owner", "Stop criteria"])], "Coverage without a precise handoff can create duplicate actions and ambiguous accountability.")
    chain("09-rlhf-pipeline.png", "RLHF Converts Human Preferences Into a Training Signal", "Demonstrations, comparisons, reward modeling and policy optimization solve different steps", "InstructGPT + transcript 21:00–26:20", [("SFT", ["Human demos", "Instruction data", "Initial policy"]), ("Preferences", ["Response pairs", "Human ranking", "Guideline"]), ("Reward model", ["Predict ranking", "Calibration", "Bias"]), ("RL policy", ["Optimize reward", "KL constraint", "Evaluate"])], "RLHF optimizes a learned proxy; reward quality and evaluation remain separate problems.")
    chain("10-constitutional-ai.png", "Constitutional AI Scales Supervision With Principles and AI Feedback", "Self-critique and AI preferences reduce direct label demand but inherit model limitations", "Anthropic Constitutional AI · transcript 26:00–27:40", [("Principles", ["Constitution", "Behavior goals", "Trade-offs"]), ("Critique + revise", ["Sample response", "Self-critique", "Improved response"]), ("AI preferences", ["Compare outputs", "Preference data", "Evaluator model"]), ("RLAIF", ["Reward model", "RL policy", "Human evaluation"])], "AI feedback scales oversight; humans still choose principles, audits and deployment boundaries.")
    chain("11-evaluation-stack.png", "Model Evaluation Depends on Elicitation and Environment", "A score reflects the task, prompt, tools, effort, judge and statistical uncertainty", "Anthropic evaluation research + transcript 27:30–30:40", [("Task", ["Capability", "Safety", "Realism"]), ("Elicitation", ["Prompt / scaffold", "Tools", "Search effort"]), ("Environment", ["Permissions", "Time / budget", "Feedback"]), ("Judge + confidence", ["Human / model", "Rubric", "Uncertainty"])], "Low measured performance may mean low capability—or simply weak elicitation.")
    chain("12-capability-safeguards.png", "Capability Evidence Should Trigger Stronger Safeguards", "Threshold assessment, required controls and deployment gates form a governance loop", "Historical ASL framing + current RSP v3.0", [("Capability evidence", ["Evaluation", "Elicitation", "Forecast"]), ("Threshold review", ["Risk domain", "Confidence", "Governance"]), ("Required safeguards", ["Security", "Deployment", "Access"]), ("Gate + reassess", ["Train / deploy", "Risk report", "Re-evaluate"])], "The 2026 RSP uses capability thresholds and required safeguards; classroom ASL terminology was an earlier snapshot.")
    chain("13-defense-in-depth.png", "Frontier Model Safety Requires Defense in Depth", "No single training method or classifier is sufficient across the model lifecycle", "Transcript-grounded redraw · 37:00–39:10", [("Training", ["Data / objectives", "CAI / RLHF", "Robustness"]), ("Access", ["Identity", "Rate / tier", "Least privilege"]), ("Runtime", ["Classifier", "Tool policy", "Monitoring"]), ("Response", ["Red team", "Incident", "Patch / revoke"])], "Independent layers should fail differently and produce evidence for the next control.")
    chain("14-interpretability-loop.png", "Mechanistic Interpretability Builds Internal Model Evidence", "Features and circuits support hypotheses, but causal validation remains necessary", "Anthropic monosemanticity research + transcript 38:17–39:03", [("Activations", ["Model layer", "High dimension", "Context"]), ("Features", ["Dictionary learning", "Sparse activation", "Semantic pattern"]), ("Circuit hypothesis", ["Interaction", "Behavior link", "Risk signal"]), ("Intervention", ["Ablate / steer", "Re-evaluate", "Audit limits"])], "Readable features are not a complete proof of intent, safety or global model behavior.")
    chain("15-compute-lifecycle.png", "Pre-training, Post-training and Inference Compute Are Complementary", "Different compute stages create broad capability, behavior and task-time search", "Transcript-grounded redraw · 34:40–36:50", [("Pre-training", ["Broad data", "World knowledge", "Base capability"]), ("Post-training", ["Instructions", "Preferences", "Tools / safety"]), ("Inference", ["Context", "Reasoning / search", "Latency cost"]), ("Feedback", ["Product evidence", "Evaluation", "Next recipe"])], "More inference compute does not remove the need for a capable, well-trained base model.")
    chain("16-chat-to-api.png", "Chat Is a Proving Ground; APIs Are Compatibility Contracts", "Fast product experiments should mature into versioned, supportable developer primitives", "Transcript-grounded redraw · 39:00–41:56", [("Chat experiment", ["Controlled UX", "Fast rollback", "Observe behavior"]), ("Evidence", ["Usefulness", "Safety", "Failure modes"]), ("API release", ["Schema", "Version", "SLO / docs"]), ("Lifecycle", ["Migration", "Deprecation", "Retirement"])], "Once customers automate against an API, change cost includes their code, compliance and business continuity.")


if __name__ == "__main__":
    main()
