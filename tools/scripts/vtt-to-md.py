"""Convert YouTube VTT subtitle files into clean Markdown transcripts.

Usage:
    python tools/scripts/vtt-to-md.py <directory>

Walks the directory, pairs each <prefix>.info.json with its best .vtt
subtitle file, and writes <prefix>.md with:

- YAML frontmatter (video_id, title, url, uploader, duration, upload_date)
- A clean transcript (no timestamps, no word-level tags, deduplicated)

Subtitle priority: .en.vtt > .en-US.vtt > .en-orig.vtt (whichever exists).
Skips files whose .md already exists unless --force is passed.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

VTT_TAG_RE = re.compile(r"<[^>]+>")
TIMESTAMP_LINE_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->")
METADATA_LINE_RE = re.compile(r"^(WEBVTT|Kind:|Language:|NOTE)")

SUB_PRIORITY = ("en.vtt", "en-US.vtt", "en-orig.vtt")


def clean_vtt(vtt_path: Path) -> str:
    """Extract deduplicated plain-text transcript from a VTT file."""
    text = vtt_path.read_text(encoding="utf-8", errors="replace")
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if METADATA_LINE_RE.match(line):
            continue
        if TIMESTAMP_LINE_RE.match(line):
            continue
        # Drop lines that still contain inline timing tags (word-level)
        if "<c>" in line or re.search(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", line):
            continue
        # Strip any remaining tags as a safety net
        line = VTT_TAG_RE.sub("", line).strip()
        if not line:
            continue
        lines.append(line)

    # Dedupe adjacent repeats (rolling captions create many duplicates)
    deduped: list[str] = []
    for line in lines:
        if not deduped or deduped[-1] != line:
            deduped.append(line)

    # Merge into paragraphs of ~80 words for readability
    words: list[str] = []
    for line in deduped:
        words.extend(line.split())

    paragraphs: list[str] = []
    buf: list[str] = []
    for word in words:
        buf.append(word)
        if len(buf) >= 80 and word.endswith((".", "?", "!")):
            paragraphs.append(" ".join(buf))
            buf = []
    if buf:
        paragraphs.append(" ".join(buf))

    return "\n\n".join(paragraphs)


def pick_subtitle(prefix: Path) -> Path | None:
    for suffix in SUB_PRIORITY:
        candidate = prefix.with_name(f"{prefix.name}.{suffix}")
        if candidate.exists():
            return candidate
    return None


def frontmatter(info: dict, video_id: str) -> str:
    title = (info.get("title") or "").replace('"', "'")
    uploader = (info.get("uploader") or "").replace('"', "'")
    duration = info.get("duration") or 0
    upload_date = info.get("upload_date") or ""
    url = f"https://www.youtube.com/watch?v={video_id}"
    return (
        "---\n"
        f"video_id: {video_id}\n"
        f'title: "{title}"\n'
        f"url: {url}\n"
        f'uploader: "{uploader}"\n'
        f"duration_seconds: {duration}\n"
        f'upload_date: "{upload_date}"\n'
        "source: youtube\n"
        "---\n\n"
    )


def convert_dir(directory: Path, force: bool = False) -> tuple[int, int, int]:
    """Return (converted, skipped, missing_subs)."""
    converted = skipped = missing = 0
    for info_path in sorted(directory.glob("*.info.json")):
        stem = info_path.name[: -len(".info.json")]  # e.g. "01-jDNdINFMZ5w"
        if stem.startswith("00-"):
            continue  # playlist-level metadata, not a video
        prefix = directory / stem
        md_path = directory / f"{stem}.md"

        if md_path.exists() and not force:
            skipped += 1
            continue

        sub_path = pick_subtitle(prefix)
        if sub_path is None:
            missing += 1
            continue

        try:
            info = json.loads(info_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            missing += 1
            continue

        video_id = info.get("id") or stem.split("-", 1)[-1]
        body = clean_vtt(sub_path)
        title = info.get("title") or video_id
        md = frontmatter(info, video_id) + f"# {title}\n\n{body}\n"
        md_path.write_text(md, encoding="utf-8")
        converted += 1

    return converted, skipped, missing


def main() -> int:
    args = sys.argv[1:]
    force = "--force" in args
    positional = [a for a in args if not a.startswith("--")]
    if not positional:
        print("usage: python vtt-to-md.py <directory> [--force]", file=sys.stderr)
        return 2

    directory = Path(positional[0])
    if not directory.is_dir():
        print(f"not a directory: {directory}", file=sys.stderr)
        return 2

    converted, skipped, missing = convert_dir(directory, force=force)
    print(f"converted: {converted}  skipped: {skipped}  missing subs: {missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
