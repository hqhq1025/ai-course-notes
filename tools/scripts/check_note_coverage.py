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


def main() -> None:
    args = parse_args()
    tex = args.tex
    text = read(tex)
    errors: list[str] = []
    warnings: list[str] = []

    figs = len(re.findall(r"\\includegraphics", text))
    readfig = len(re.findall(r"读图|怎么看|图.*说明|图.*含义", text))
    boxes = len(re.findall(r"\\begin\{(?:importantbox|knowledgebox|warningbox)\}", text))
    term_digest = len(re.findall(r"术语消化|术语表|背景概念|什么是|概念.*解释", text))
    formulas = len(re.findall(r"\\\[|\\\]|\$\$", text)) // 2 + len(re.findall(r"\\begin\{(?:align|equation)\*?\}", text))
    symbol_words = len(re.findall(r"其中|符号|表示|定义为|记为", text))
    code_blocks = len(re.findall(r"\\begin\{lstlisting\}", text))
    summary = len(re.findall(r"本章小结|总结与延伸", text))

    if figs >= 3 and readfig == 0:
        errors.append("figures-present-but-no-readfig-explanation")
    if figs >= 8 and readfig < 3:
        warnings.append("many-figures-but-few-readfig-explanations")
    if boxes < 5:
        errors.append("too-few-teaching-boxes")
    if term_digest == 0:
        warnings.append("no-terminology-digestion-detected")
    if formulas >= 3 and symbol_words < 3:
        warnings.append("formulas-present-but-symbol-explanation-looks-thin")
    if summary < 2:
        errors.append("missing-section-or-final-summary")
    if code_blocks and "caption=" not in text:
        errors.append("code-blocks-without-captions")

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
    print(f"figs={figs} readfig={readfig} boxes={boxes} term_digest={term_digest} formulas={formulas} code={code_blocks} summaries={summary}")
    for item in errors:
        print(f"ERROR {item}")
    for item in warnings:
        print(f"WARN {item}")

    if errors or (args.strict and warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()
