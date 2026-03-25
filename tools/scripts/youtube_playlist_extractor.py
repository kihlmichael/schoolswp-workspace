#!/usr/bin/env python3
"""Extract transcripts and metadata from a YouTube playlist.

Usage:
    .venv/Scripts/python tools/scripts/youtube_playlist_extractor.py \
        --videos-json data/youtube-extracts/videos.json \
        --output-dir data/youtube-extracts/

The --videos-json file must contain a JSON array of objects with keys:
    videoId, title, description, views, likes, date, channel, duration
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Env
# ---------------------------------------------------------------------------

# Search .env in project root (same logic as agents)
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(_PROJECT_ROOT / ".env")

import os  # noqa: E402

APIFY_TOKEN: str = os.environ.get("APIFY_TOKEN", "")
APIFY_ACTOR = "starvibe~youtube-video-transcript"
APIFY_RUN_URL = f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/runs"
POLL_INTERVAL = 5  # seconds
POLL_TIMEOUT = 300  # 5 min max per video
BATCH_SIZE = 5

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def slugify(text: str, max_len: int = 60) -> str:
    """Convert text to kebab-case slug, truncated to *max_len* chars."""
    text = text.lower()
    text = re.sub(r"[''`]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if len(text) > max_len:
        text = text[:max_len].rstrip("-")
    return text


def format_duration(raw: str | int | None) -> str:
    """Best-effort duration formatting.

    Accepts ISO 8601 duration (PT1H2M3S), seconds as int, or passthrough string.
    """
    if raw is None:
        return "N/A"
    if isinstance(raw, (int, float)):
        total = int(raw)
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
    if isinstance(raw, str) and raw.startswith("PT"):
        parts = re.findall(r"(\d+)([HMS])", raw.upper())
        h = m = s = 0
        for val, unit in parts:
            if unit == "H":
                h = int(val)
            elif unit == "M":
                m = int(val)
            elif unit == "S":
                s = int(val)
        return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
    return str(raw)


def format_number(n: str | int | None) -> str:
    """Format a number with space-separated thousands."""
    if n is None:
        return "N/A"
    try:
        return f"{int(n):,}".replace(",", " ")
    except (ValueError, TypeError):
        return str(n)


# ---------------------------------------------------------------------------
# Apify transcript extraction
# ---------------------------------------------------------------------------


async def fetch_transcript(client: httpx.AsyncClient, video_id: str) -> str | None:
    """Run Apify actor for a single video and return the transcript text."""
    url = f"{APIFY_RUN_URL}?token={APIFY_TOKEN}"
    body = {
        "youtube_url": f"https://www.youtube.com/watch?v={video_id}",
        "language": "en",
        "include_transcript_text": True,
    }

    # Start the run
    resp = await client.post(url, json=body, timeout=30)
    resp.raise_for_status()
    run_data = resp.json()["data"]
    run_id = run_data["id"]
    dataset_id = run_data.get("defaultDatasetId")

    # Poll until finished
    status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={APIFY_TOKEN}"
    start = time.monotonic()
    while True:
        await asyncio.sleep(POLL_INTERVAL)
        r = await client.get(status_url, timeout=15)
        r.raise_for_status()
        status = r.json()["data"]["status"]
        if status == "SUCCEEDED":
            break
        if status in ("FAILED", "ABORTED", "TIMED-OUT"):
            return None
        if time.monotonic() - start > POLL_TIMEOUT:
            return None

    # Fetch dataset items
    if not dataset_id:
        dataset_id = run_data.get("defaultDatasetId")
    items_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={APIFY_TOKEN}"
    r = await client.get(items_url, timeout=30)
    r.raise_for_status()
    items = r.json()

    if not items:
        return None

    # The actor returns transcript_text in the first item
    item = items[0]
    transcript = item.get("transcript_text") or item.get("transcriptText") or item.get("text")
    return transcript if transcript else None


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------


def build_video_markdown(video: dict, transcript: str | None) -> str:
    """Build the Markdown content for a single video."""
    title = video.get("title", "Sans titre")
    video_id = video["videoId"]
    channel = video.get("channel", "N/A")
    views = format_number(video.get("views"))
    likes = format_number(video.get("likes"))
    date = video.get("date", "N/A")
    duration = format_duration(video.get("duration") or video.get("lengthSeconds"))
    description = video.get("description", "").strip() or "N/A"
    transcript_text = transcript.strip() if transcript else "Transcript non disponible"

    return f"""# {title}

## Metadonnees

| Champ | Valeur |
|-------|--------|
| URL | https://www.youtube.com/watch?v={video_id} |
| Chaine | {channel} |
| Vues | {views} |
| Likes | {likes} |
| Date | {date} |
| Duree | {duration} |

## Description

{description}

## Transcript

{transcript_text}
"""


def build_index_markdown(videos: list[dict], filenames: list[str]) -> str:
    """Build the _index.md summary file."""
    lines = ["# Playlist — Sommaire\n"]
    lines.append(f"Total : {len(videos)} videos\n")
    lines.append("| # | Titre | Chaine | Duree | Fichier |")
    lines.append("|---|-------|--------|-------|---------|")
    for i, (v, fname) in enumerate(zip(videos, filenames), 1):
        title = v.get("title", "Sans titre")
        channel = v.get("channel", "N/A")
        duration = format_duration(v.get("duration"))
        lines.append(f"| {i} | {title} | {channel} | {duration} | [{fname}]({fname}) |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


async def process_batch(
    client: httpx.AsyncClient,
    batch: list[tuple[int, dict]],
    total: int,
) -> list[tuple[int, dict, str | None]]:
    """Process a batch of videos in parallel. Returns (index, video, transcript)."""

    async def _one(idx: int, video: dict) -> tuple[int, dict, str | None]:
        title_short = video.get("title", "???")[:50]
        print(f"  [{idx}/{total}] Extracting: {title_short}...")
        try:
            transcript = await fetch_transcript(client, video["videoId"])
        except Exception as exc:
            print(f"  [{idx}/{total}] ERREUR: {exc}")
            transcript = None
        status = "OK" if transcript else "ECHEC"
        print(f"  [{idx}/{total}] {status}")
        return (idx, video, transcript)

    tasks = [_one(idx, v) for idx, v in batch]
    return await asyncio.gather(*tasks)


async def run(videos_json_path: Path, output_dir: Path) -> None:
    if not APIFY_TOKEN:
        print("ERREUR: APIFY_TOKEN manquant dans le .env")
        sys.exit(1)

    # Load videos
    raw = videos_json_path.read_text(encoding="utf-8")
    videos: list[dict] = json.loads(raw)
    total = len(videos)
    print(f"Playlist : {total} videos a traiter")
    print(f"Sortie   : {output_dir}\n")

    output_dir.mkdir(parents=True, exist_ok=True)

    results: list[tuple[int, dict, str | None]] = []

    async with httpx.AsyncClient() as client:
        # Build indexed list
        indexed = list(enumerate(videos, 1))

        # Process in batches of BATCH_SIZE
        for batch_start in range(0, total, BATCH_SIZE):
            batch = indexed[batch_start : batch_start + BATCH_SIZE]
            print(f"--- Batch {batch_start // BATCH_SIZE + 1} ({len(batch)} videos) ---")
            batch_results = await process_batch(client, batch, total)
            results.extend(batch_results)

    # Sort by original index
    results.sort(key=lambda x: x[0])

    # Generate files
    filenames: list[str] = []
    data_export: list[dict] = []

    for idx, video, transcript in results:
        slug = slugify(video.get("title", "video"))
        fname = f"{idx:02d}_{slug}.md"
        filenames.append(fname)

        # Write markdown
        md = build_video_markdown(video, transcript)
        (output_dir / fname).write_text(md, encoding="utf-8")

        # Collect structured data
        entry = {
            **video,
            "file": fname,
            "transcript_available": transcript is not None,
            "transcript_length": len(transcript) if transcript else 0,
        }
        data_export.append(entry)

    # Write _index.md
    ordered_videos = [v for _, v, _ in results]
    index_md = build_index_markdown(ordered_videos, filenames)
    (output_dir / "_index.md").write_text(index_md, encoding="utf-8")

    # Write _data.json
    (output_dir / "_data.json").write_text(
        json.dumps(data_export, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Summary
    ok_count = sum(1 for _, _, t in results if t)
    fail_count = total - ok_count
    print(f"\nTermine : {ok_count}/{total} transcripts OK, {fail_count} echecs")
    print(f"Fichiers generes dans {output_dir}/")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract YouTube playlist transcripts via Apify + merge metadata.",
    )
    parser.add_argument(
        "--videos-json",
        type=Path,
        required=True,
        help="JSON file with video metadata array",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/youtube-extracts/"),
        help="Output directory (default: data/youtube-extracts/)",
    )
    parser.add_argument(
        "--playlist-id",
        type=str,
        default=None,
        help="Playlist ID (informational, not used for extraction)",
    )
    args = parser.parse_args()

    if not args.videos_json.exists():
        print(f"ERREUR: fichier introuvable — {args.videos_json}")
        sys.exit(1)

    asyncio.run(run(args.videos_json, args.output_dir))


if __name__ == "__main__":
    main()
