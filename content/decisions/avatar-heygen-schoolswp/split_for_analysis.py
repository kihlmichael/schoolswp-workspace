"""Decoupe heygen-youtube.json en lots analysables par les sous-agents Phase 2.

Tronque les descriptions (les descriptions YouTube HeyGen sont longues et repetitives)
pour garder des fichiers lisibles par l'outil Read. Sortie : data/chunks/chunk-NN.json.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "data" / "heygen-youtube.json"
CHUNK_DIR = ROOT / "data" / "chunks"
CHUNK_SIZE = 35
DESC_MAX = 600


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    videos = data["videos"]
    compact = []
    for v in videos:
        desc = (v.get("description") or "").strip()
        if len(desc) > DESC_MAX:
            desc = desc[:DESC_MAX] + " [...]"
        compact.append({
            "id": v.get("id"),
            "url": v.get("url"),
            "title": v.get("title"),
            "description": desc,
            "published_at": v.get("published_at"),
            "duration_iso": v.get("duration_iso"),
            "view_count": v.get("view_count"),
            "tags": (v.get("tags") or [])[:8],
        })

    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for i in range(0, len(compact), CHUNK_SIZE):
        chunk = compact[i:i + CHUNK_SIZE]
        path = CHUNK_DIR / f"chunk-{n:02d}.json"
        path.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding="utf-8")
        n += 1
    print(f"OK {n} chunks de <= {CHUNK_SIZE} videos ecrits dans {CHUNK_DIR}")

    # index des playlists pour reference
    (ROOT / "data" / "playlists.json").write_text(
        json.dumps(data["playlists"], ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"playlists : {len(data['playlists'])}")


if __name__ == "__main__":
    main()
