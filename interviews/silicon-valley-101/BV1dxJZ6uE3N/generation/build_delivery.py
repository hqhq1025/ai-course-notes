"""Check writing provenance and build a single-episode website preview.

This command only writes local artifacts. It never publishes or changes Git.
Run with the same Python environment that provides the website dependencies.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


EPISODE = Path(__file__).resolve().parent.parent
REPO = EPISODE.parents[2]
GENERATION = EPISODE / "generation"
PREVIEW = Path("/tmp/sv101-web-preview")
MODEL = "gemini-4-argon"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def check_request(prefix, transcript):
    """Check local evidence, then return only public receipt fields."""
    receipt = json.loads(Path(str(prefix) + "-receipt.json").read_text())
    prompt = Path(str(prefix) + "-prompt.txt").read_bytes()
    raw = Path(str(prefix) + "-raw.txt").read_bytes()
    structured = json.loads(prefix.with_suffix(".json").read_text())
    if receipt.get("error") or receipt.get("http_error"):
        raise ValueError(f"{prefix.name}: failed request")
    if (receipt.get("requested_model") != MODEL
            or receipt.get("returned_models") != [MODEL]):
        raise ValueError(f"{prefix.name}: unexpected model")
    finishes = receipt.get("finish_reasons")
    if not finishes or any(value != "stop" for value in finishes):
        raise ValueError(f"{prefix.name}: incomplete completion")
    if receipt.get("stream_done") is not True:
        raise ValueError(f"{prefix.name}: stream lacks DONE")
    if sha256(prompt) != receipt.get("prompt_sha256"):
        raise ValueError(f"{prefix.name}: prompt differs from receipt")
    if sha256(raw) != receipt.get("output_sha256"):
        raise ValueError(f"{prefix.name}: output differs from receipt")
    if not isinstance(structured, dict) or json.loads(raw) != structured:
        raise ValueError(f"{prefix.name}: structured output differs from raw JSON")

    snapshot = receipt["source_snapshot"]
    snapshot_hash = sha256(json.dumps(
        snapshot, ensure_ascii=False, sort_keys=True).encode())
    if snapshot_hash != receipt.get("source_snapshot_sha256"):
        raise ValueError(f"{prefix.name}: source snapshot differs from receipt")
    transcript_path = (EPISODE / "sources/transcript-reading.md").resolve()
    recorded = [entry for entry in snapshot
                if Path(entry["path"]).resolve() == transcript_path]
    if (len(recorded) != 1 or recorded[0]["sha256"] != sha256(transcript)
            or recorded[0]["bytes"] != len(transcript)):
        raise ValueError(f"{prefix.name}: transcript differs from source snapshot")
    if not transcript or transcript not in prompt:
        raise ValueError(f"{prefix.name}: full transcript absent from actual prompt")

    return {
        "request": prefix.name,
        "requested_model": receipt["requested_model"],
        "returned_models": receipt["returned_models"],
        "finish_reasons": finishes,
        "stream_done": receipt["stream_done"],
        "duration_seconds": receipt["duration_seconds"],
        "prompt_sha256": receipt["prompt_sha256"],
        "output_sha256": receipt["output_sha256"],
        "source_snapshot_sha256": snapshot_hash,
        "transcript_check": {
            "source": "sources/transcript-reading.md",
            "sha256": sha256(transcript),
            "bytes": len(transcript),
            "matches_recorded_source": True,
            "complete_text_in_actual_prompt": True,
            "method": "exact UTF-8 byte sequence in saved prompt; prompt SHA-256 matches receipt",
        },
    }


def write_provenance(attempt, edits):
    transcript = (EPISODE / "sources/transcript-reading.md").read_bytes()
    prefixes = [GENERATION / f"chapter-{number:02d}-{attempt}"
                for number in range(1, 8)]
    prefixes.extend(GENERATION / edit for edit in edits)
    records = [check_request(prefix, transcript) for prefix in prefixes]
    payload = {
        "schema_version": 1,
        "episode": EPISODE.name,
        "verification_scope": {
            "chapter_drafts": 7,
            "whole_document_editorial_requests": len(edits),
            "total_requests": len(records),
        },
        "requests": records,
    }
    output = EPISODE / "provenance.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"Verified {len(records)} requests; wrote {output.name}", flush=True)


def build_preview():
    # Importing from the repository reuses its converters, theme and asset rules.
    sys.path.insert(0, str(REPO))
    from tools.web import generate_site as site

    tex = EPISODE / f"{EPISODE.name}-notes.tex"
    if not tex.is_file():
        raise FileNotFoundError(f"Render the final note first: {tex.name}")
    original_discover = site.discover_notes
    site.discover_notes = lambda root: [site.parse_note(root, tex)]
    try:
        result = site.build_site(
            REPO, PREVIEW,
            strict=True,
            fail_on_tikz_warnings=True,
            fail_on_pdf_figure_warnings=True,
            fail_on_latex_leaks=True,
            render_tikz=True,
            verbose_warnings=True,
            compress_images=True,
            image_max_width=1600,
            jpeg_quality=82,
            cache_root=None,
        )
    finally:
        site.discover_notes = original_discover
    if result:
        raise RuntimeError(f"Website source generation failed with status {result}")
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "-f",
         str(PREVIEW / "mkdocs.yml"), "--strict"],
        cwd=REPO, check=True,
    )
    print(f"Website preview built in {PREVIEW / 'site'}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["provenance", "preview", "all"],
                        nargs="?", default="all")
    parser.add_argument("--attempt", default="resume1")
    parser.add_argument("--edit", nargs="+", default=["editorial-02a", "editorial-02b"],
                        help="Successful editorial request prefixes, in application order")
    args = parser.parse_args()
    for name in (args.attempt, *args.edit):
        if not name or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in name):
            parser.error("Attempt and edit names must contain only letters, digits, hyphens or underscores")
    if len(set(args.edit)) != len(args.edit):
        parser.error("Editorial request prefixes must be unique")
    if args.action in {"provenance", "all"}:
        write_provenance(args.attempt, args.edit)
    if args.action in {"preview", "all"}:
        build_preview()


if __name__ == "__main__":
    main()
