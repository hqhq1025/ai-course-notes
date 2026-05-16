#!/usr/bin/env python3
"""Check new-standard teaching coverage heuristics for a note."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check note coverage and pedagogy heuristics.")
    parser.add_argument("tex", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on warnings as well as errors.")
    return parser.parse_args()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_manifest_required(manifest: Path) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    if not manifest or not manifest.exists():
        return rows
    for line in read(manifest).splitlines():
        if not line.startswith("| "):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5 or parts[0] in {"ID", "---"}:
            continue
        node_id, kind, required, _source, title = parts[:5]
        if required == "yes":
            rows.append((node_id, kind, title.replace("\\|", "|")))
    return rows


def extract_manifest_rows(manifest: Path | None) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    if not manifest or not manifest.exists():
        return rows
    for line in read(manifest).splitlines():
        if not line.startswith("| "):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5 or parts[0] in {"ID", "---"}:
            continue
        node_id, kind, required, _source, title = parts[:5]
        rows.append((node_id, kind, required, title.replace("\\|", "|")))
    return rows


def strip_latex(line: str) -> str:
    """Return a rough prose-only version of a LaTeX line for heuristic checks."""
    line = re.sub(r"%.*$", "", line)
    line = re.sub(r"\\(?:section|subsection|caption|figsource|label)\*?(?:\[[^\]]*\])?\{[^}]*\}", " ", line)
    line = re.sub(r"\\(?:begin|end)\{[^}]*\}", " ", line)
    line = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", line)
    line = re.sub(r"[{}$^_]", " ", line)
    return re.sub(r"\s+", " ", line).strip()


def prose_char_count(lines: list[str]) -> int:
    chars = 0
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("%"):
            continue
        if "\\includegraphics" in line or "\\caption" in line or "\\figsource" in line:
            continue
        if any(cmd in line for cmd in [r"\toprule", r"\midrule", r"\bottomrule", r"\endhead"]):
            continue
        # Wide tables can contain teaching information, but they are not
        # narrative prose. Count them elsewhere via boxes/term digestion.
        if "&" in line and r"\\" in line:
            continue
        cleaned = strip_latex(line)
        chars += len(re.findall(r"[\u4e00-\u9fffA-Za-z0-9]", cleaned))
    return chars


def figure_local_explanation_counts(lines: list[str]) -> list[tuple[int, int]]:
    counts: list[tuple[int, int]] = []
    for idx, line in enumerate(lines):
        if "\\includegraphics" not in line:
            continue
        window = lines[max(0, idx - 10) : min(len(lines), idx + 24)]
        counts.append((idx + 1, prose_char_count(window)))
    return counts


BRIDGE_WORDS = (
    "本节", "前面", "上一", "接下来", "现在", "因此", "所以", "换句话说", "这意味着",
    "为了", "问题", "核心", "直觉", "回到", "进一步", "从", "下面", "这里",
)


def weak_section_openers(lines: list[str]) -> list[tuple[int, str]]:
    weak: list[tuple[int, str]] = []
    heading_re = re.compile(r"\\(?:section|subsection)\{([^}]*)\}")
    for idx, line in enumerate(lines):
        match = heading_re.search(line)
        if not match:
            continue
        title = match.group(1)
        if any(skip in title for skip in ["本章小结", "拓展阅读", "总结与延伸"]):
            continue
        opener_lines: list[str] = []
        first_meaningful = ""
        for raw in lines[idx + 1 : min(len(lines), idx + 12)]:
            stripped = raw.strip()
            if not stripped or stripped.startswith("%"):
                continue
            if not first_meaningful:
                first_meaningful = stripped
            if stripped.startswith(r"\begin{figure}") or stripped.startswith(r"\includegraphics"):
                break
            opener_lines.append(stripped)
            if prose_char_count(opener_lines) >= 120:
                break
        opener_text = " ".join(strip_latex(x) for x in opener_lines)
        opener_chars = len(re.findall(r"[\u4e00-\u9fffA-Za-z0-9]", opener_text))
        starts_with_visual = first_meaningful.startswith(r"\begin{figure}") or first_meaningful.startswith(r"\includegraphics")
        has_bridge = any(word in opener_text for word in BRIDGE_WORDS)
        if starts_with_visual or opener_chars < 90 or not has_bridge:
            weak.append((idx + 1, title))
    return weak


def main() -> None:
    args = parse_args()
    tex = args.tex
    text = read(tex)
    errors: list[str] = []
    warnings: list[str] = []
    lines = text.splitlines()

    figs = len(re.findall(r"\\includegraphics", text))
    readfig = len(re.findall(r"读图|怎么看|图.*说明|图.*含义", text))
    boxes = len(re.findall(r"\\begin\{(?:importantbox|knowledgebox|warningbox)\}", text))
    term_digest = len(re.findall(r"术语消化|术语表|背景概念|什么是|概念.*解释", text))
    teacher_voice = len(
        re.findall(
            r"课堂提示|老师强调|讲者强调|讲义提醒|口头|课上|经验判断|实践经验|"
            r"这里的提醒|课程提醒|老师在这里|teacher voice|speaker note",
            text,
            flags=re.I,
        )
    )
    formulas = len(re.findall(r"\\\[|\\\]|\$\$", text)) // 2 + len(re.findall(r"\\begin\{(?:align|equation)\*?\}", text))
    symbol_words = len(re.findall(r"其中|符号|表示|定义为|记为", text))
    code_blocks = len(re.findall(r"\\begin\{lstlisting\}", text))
    summary = len(re.findall(r"本章小结|总结与延伸", text))
    prose_chars = prose_char_count(lines)
    fig_local_counts = figure_local_explanation_counts(lines)

    if figs >= 3 and readfig == 0:
        errors.append("figures-present-but-no-readfig-explanation")
    if figs >= 8 and readfig < 3:
        warnings.append("many-figures-but-few-readfig-explanations")
    if figs >= 12:
        prose_per_fig = prose_chars / max(1, figs)
        if prose_per_fig < 260:
            warnings.append(f"figure-heavy-prose-thin=chars_per_figure:{prose_per_fig:.0f}<260")
    if fig_local_counts:
        thin_figs = [(line_no, count) for line_no, count in fig_local_counts if count < 220]
        if figs >= 8 and len(thin_figs) >= max(3, int(figs * 0.15)):
            preview = ",".join(f"L{line}:{count}" for line, count in thin_figs[:8])
            warnings.append(f"thin-local-figure-explanations={len(thin_figs)}/{figs} ({preview})")
    if boxes < 5:
        errors.append("too-few-teaching-boxes")
    if term_digest == 0:
        warnings.append("no-terminology-digestion-detected")
    manifest_rows = extract_manifest_rows(args.manifest)
    optional_text_nodes = [row for row in manifest_rows if row[1] == "text" and row[2] == "optional"]
    if len(optional_text_nodes) >= 20 and teacher_voice < 3:
        warnings.append(
            f"teacher-voice-underrepresented=markers:{teacher_voice}<3 optional_text_nodes:{len(optional_text_nodes)}"
        )
    if formulas >= 3 and symbol_words < 3:
        warnings.append("formulas-present-but-symbol-explanation-looks-thin")
    if summary < 2:
        errors.append("missing-section-or-final-summary")
    if code_blocks and "caption=" not in text:
        errors.append("code-blocks-without-captions")
    weak_openers = weak_section_openers(lines)
    if weak_openers:
        preview = ",".join(f"L{line}:{title[:24]}" for line, title in weak_openers[:8])
        warnings.append(f"weak-section-openers={len(weak_openers)} ({preview})")

    first_use_terms = {
        "ZeRO": ["ZeRO-1", "Zero Redundancy", "优化器状态", "分片", "stage"],
        "sharding": ["分片", "切分", "每张 GPU", "每卡", "只存"],
        "state sharding": ["优化器状态", "梯度", "参数", "分片"],
        "fused kernel": ["融合", "合并", "减少", "显存读写", "HBM"],
        "fused kernels": ["融合", "合并", "减少", "显存读写", "HBM"],
        "collectives": ["all-reduce", "all-gather", "reduce-scatter", "集合通信", "多 GPU"],
        "DRAM": ["Dynamic", "HBM", "显存", "全称", "memory"],
        "SRAM": ["Static", "cache", "片上", "高速缓存", "全称"],
        "HBM": ["High Bandwidth", "显存", "DRAM", "带宽"],
        "optimizer state": ["Adam", "m", "v", "一阶", "二阶", "动量"],
        "Activation checkpointing": ["重算", "激活", "显存", "gradient checkpointing"],
        "activation checkpointing": ["重算", "激活", "显存", "gradient checkpointing"],
        "perplexity": ["PPL", "交叉熵", "惊讶", "选项", "exp"],
    }
    unexplained_terms: list[str] = []
    for term, clues in first_use_terms.items():
        match = re.search(re.escape(term), text, flags=re.I)
        if not match:
            continue
        window = text[max(0, match.start() - 450) : min(len(text), match.end() + 700)]
        if not any(clue in window for clue in clues):
            unexplained_terms.append(term)
    if unexplained_terms:
        warnings.append("terms-appear-without-obvious-first-use-explanation=" + ",".join(sorted(set(unexplained_terms))))

    required = extract_manifest_required(args.manifest) if args.manifest else []
    if required:
        missing = []
        for node_id, kind, title in required:
            probe = title.strip("` ")
            if kind in {"slide", "figure"}:
                candidates = [probe, Path(probe).name]
            else:
                candidates = [probe[:40]]
            if not any(c and c in text for c in candidates):
                missing.append((node_id, kind, title))
        if missing:
            warnings.append(f"manifest-required-nodes-not-obviously-covered={len(missing)}")
            for node_id, kind, title in missing[:20]:
                warnings.append(f"  missing? {node_id} {kind}: {title[:80]}")

    print(f"note={tex}")
    print(
        f"figs={figs} readfig={readfig} boxes={boxes} term_digest={term_digest} "
        f"teacher_voice={teacher_voice} formulas={formulas} code={code_blocks} "
        f"summaries={summary} prose_chars={prose_chars}"
    )
    for item in errors:
        print(f"ERROR {item}")
    for item in warnings:
        print(f"WARN {item}")

    if errors or (args.strict and warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()
