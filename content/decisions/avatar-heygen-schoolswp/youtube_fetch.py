"""Phase 2 - collecte conforme des metadonnees publiques de la chaine YouTube HeyGen.

API YouTube Data v3 officielle, lecture publique (cle API, pas d'OAuth).
Recupere : infos chaine, playlists, et toutes les videos (titre, description,
date, duree, vues, tags). N'extrait AUCUNE transcription, ne telecharge AUCUNE video.

Sortie : data/heygen-youtube.json (snapshot date, source de verite Phase 2).
Lit YOUTUBE_API_KEY dans le .env racine.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
if not API_KEY:
    sys.exit("ERR: YOUTUBE_API_KEY manquant dans le .env racine")

BASE = "https://www.googleapis.com/youtube/v3"
CHANNEL_ID = "UCV0FmNF3iM-022BF1KbVtxA"  # @heygen_official (verifie Phase 1)


def get(endpoint: str, params: dict) -> dict:
    params = {**params, "key": API_KEY}
    r = requests.get(f"{BASE}/{endpoint}", params=params, timeout=60)
    if r.status_code != 200:
        sys.exit(f"ERR {endpoint} HTTP {r.status_code}: {r.text[:400]}")
    return r.json()


def fetch_channel() -> dict:
    data = get("channels", {
        "part": "snippet,statistics,contentDetails,brandingSettings",
        "id": CHANNEL_ID,
    })
    items = data.get("items", [])
    if not items:
        sys.exit("ERR: chaine introuvable")
    return items[0]


def fetch_all_playlist_items(playlist_id: str) -> list[str]:
    video_ids: list[str] = []
    page_token = None
    while True:
        params = {"part": "contentDetails", "playlistId": playlist_id, "maxResults": 50}
        if page_token:
            params["pageToken"] = page_token
        data = get("playlistItems", params)
        for it in data.get("items", []):
            vid = it.get("contentDetails", {}).get("videoId")
            if vid:
                video_ids.append(vid)
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return video_ids


def fetch_videos(video_ids: list[str]) -> list[dict]:
    videos: list[dict] = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        data = get("videos", {
            "part": "snippet,contentDetails,statistics",
            "id": ",".join(batch),
        })
        for v in data.get("items", []):
            sn = v.get("snippet", {})
            cd = v.get("contentDetails", {})
            st = v.get("statistics", {})
            videos.append({
                "id": v.get("id"),
                "url": f"https://www.youtube.com/watch?v={v.get('id')}",
                "title": sn.get("title"),
                "description": sn.get("description"),
                "published_at": sn.get("publishedAt"),
                "duration_iso": cd.get("duration"),
                "view_count": st.get("viewCount"),
                "like_count": st.get("likeCount"),
                "comment_count": st.get("commentCount"),
                "tags": sn.get("tags", []),
            })
    return videos


def fetch_playlists() -> list[dict]:
    playlists: list[dict] = []
    page_token = None
    while True:
        params = {"part": "snippet,contentDetails", "channelId": CHANNEL_ID, "maxResults": 50}
        if page_token:
            params["pageToken"] = page_token
        data = get("playlists", params)
        for p in data.get("items", []):
            sn = p.get("snippet", {})
            playlists.append({
                "id": p.get("id"),
                "title": sn.get("title"),
                "description": sn.get("description"),
                "item_count": p.get("contentDetails", {}).get("itemCount"),
            })
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return playlists


def main() -> None:
    channel = fetch_channel()
    uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    print(f"chaine : {channel['snippet']['title']}")
    print(f"stats : {channel.get('statistics')}")
    print(f"uploads playlist : {uploads}")

    video_ids = fetch_all_playlist_items(uploads)
    print(f"videos trouvees : {len(video_ids)}")
    videos = fetch_videos(video_ids)
    playlists = fetch_playlists()
    print(f"playlists : {len(playlists)}")

    out_dir = ROOT / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "heygen-youtube.json"
    payload = {
        "channel": {
            "id": channel.get("id"),
            "title": channel["snippet"].get("title"),
            "description": channel["snippet"].get("description"),
            "published_at": channel["snippet"].get("publishedAt"),
            "statistics": channel.get("statistics"),
        },
        "playlists": playlists,
        "videos": videos,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK ecrit {out} ({len(videos)} videos, {len(playlists)} playlists)")


if __name__ == "__main__":
    main()
