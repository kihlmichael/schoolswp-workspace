"""Build an INDEX.md for a directory of scraped YouTube videos.

Reads all *.info.json files in the target directory, sorts by playlist
index (filename prefix), and writes INDEX.md with one row per video.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def fmt_duration(seconds: int) -> str:
    if not seconds:
        return "—"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h{m:02d}m"
    return f"{m}m{s:02d}s"


def build_index(directory: Path) -> str:
    rows = []
    for info_path in sorted(directory.glob("*.info.json")):
        stem = info_path.name[: -len(".info.json")]
        if stem.startswith("00-"):
            continue
        try:
            info = json.loads(info_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        video_id = info.get("id", "")
        title = info.get("title", "").strip()
        duration = fmt_duration(info.get("duration", 0))
        upload_date = info.get("upload_date", "")
        if upload_date and len(upload_date) == 8:
            upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
        rows.append(
            {
                "stem": stem,
                "video_id": video_id,
                "title": title,
                "duration": duration,
                "upload_date": upload_date,
            }
        )

    total_seconds = 0
    for info_path in directory.glob("*.info.json"):
        if info_path.name.startswith("00-"):
            continue
        try:
            info = json.loads(info_path.read_text(encoding="utf-8"))
            total_seconds += info.get("duration", 0) or 0
        except json.JSONDecodeError:
            continue

    total_h, rem = divmod(total_seconds, 3600)
    total_m, _ = divmod(rem, 60)

    lines = [
        "# FluentBoards — playlist YouTube officielle",
        "",
        "Source : chaîne **WPManageNinja** — playlist `PLXpD0vT4thWGD5hRcRN2MdLrRZ7mjZC24`",
        "",
        f"**{len(rows)} vidéos** | durée totale **{total_h}h{total_m:02d}m** | transcripts EN (auto-générés)",
        "",
        "Matériel brut pour la formation FluentBoards schoolsWP (démos officielles par l'éditeur, à condenser/remonter en version FR).",
        "",
        "| # | Titre | Durée | Date | Transcript |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        idx = row["stem"].split("-", 1)[0]
        yt_url = f"https://www.youtube.com/watch?v={row['video_id']}"
        md_link = f"[{row['stem']}.md]({row['stem']}.md)"
        lines.append(f"| {idx} | [{row['title']}]({yt_url}) | {row['duration']} | {row['upload_date']} | {md_link} |")

    return "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python build-youtube-index.py <directory>", file=sys.stderr)
        return 2
    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"not a directory: {directory}", file=sys.stderr)
        return 2
    index = build_index(directory)
    (directory / "INDEX.md").write_text(index, encoding="utf-8")
    print(f"wrote {directory / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
