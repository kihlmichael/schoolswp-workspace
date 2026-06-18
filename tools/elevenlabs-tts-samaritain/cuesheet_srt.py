"""Generate a montage cuesheet (Markdown) + SRT subtitles for the M1 audio batch.

Reads the 10 MP3 durations via ffprobe, the scene texts from generate.py
(BATCH_SCENES), and the static metadata table (target timecode + capture)
defined below. Writes:

  - cuesheet-m1.md : per-scene mapping (audio file, captures, target/actual
    timing, drift) for the video editor.
  - subtitles-m1.srt : burnable subtitles, one cue per sentence, timing
    proportional to char length within each scene's measured duration.

Usage:
  .venv/Scripts/python.exe tools/elevenlabs-tts-samaritain/cuesheet_srt.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = PROJECT_ROOT / "content" / "formations" / "samaritain-security" / "production" / "audio-m1"
OUT_DIR = AUDIO_DIR  # cuesheet + SRT sit next to the MP3s

sys.path.insert(0, str(Path(__file__).parent))
from generate import BATCH_SCENES  # noqa: E402

# Static metadata from the TTS script doc (Google Drive id 1XAQOMcz...).
# (target_start_s, target_end_s, capture_hint, on_camera)
SCENE_META = {
    "M1-S01-hook":           (0,   15,  "face cam (pas de capture)",                                    True),
    "M1-S02-desactiver":     (15,  40,  "screencast live : page Extensions WP",                         False),
    "M1-S03-televerser":     (40,  70,  "screencast live : Extensions > Ajouter > Téléverser ZIP",      False),
    "M1-S04-licence":        (70,  110, "Cap 19 (écran licence vide) puis Cap 3 (Licence Active)",      False),
    "M1-S05-nouvelle-url":   (110, 150, "Cap 4 zoom URL connexion - SLUG À FLOUTER",                    False),
    "M1-S06-preuve-404":     (150, 175, "Cap 17 (page 404 'Oups')",                                     False),
    "M1-S07-nouvelle-url-ok":(175, 195, "Cap 18 (login sur slug perso) - SLUG À FLOUTER",               False),
    "M1-S08-url-secours":    (195, 230, "Zoom Cap 3 (récap licence, 'Clé de récupération')",            False),
    "M1-S09-dashboard":      (230, 270, "Cap 2 (tableau de bord, score 96/100)",                        False),
    "M1-S10-outro":          (270, 285, "face cam (pas de capture)",                                    True),
}


def probe_duration(mp3: Path) -> float:
    """Return MP3 duration in seconds via ffprobe."""
    res = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "json",
            str(mp3),
        ],
        capture_output=True, text=True, check=True,
    )
    return float(json.loads(res.stdout)["format"]["duration"])


def fmt_hms(s: float) -> str:
    """Format seconds as M:SS.s (cuesheet) — short form for editor."""
    m, sec = divmod(s, 60)
    return f"{int(m)}:{sec:05.2f}"


def fmt_srt(s: float) -> str:
    """Format seconds as HH:MM:SS,mmm (SRT spec)."""
    ms = int(round(s * 1000))
    h, rem = divmod(ms, 3600000)
    m, rem = divmod(rem, 60000)
    sec, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"


def split_sentences(text: str) -> list[str]:
    """Split a paragraph into sentence-like cues for SRT.

    Splits on . ? ! followed by whitespace, but keeps the punctuation with
    the preceding sentence. Also collapses double spaces and trims.
    """
    parts = re.split(r"(?<=[.!?…])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def build_srt_cues(scenes_with_durations: list[tuple[str, str, float, float]]) -> str:
    """Return SRT body. scenes_with_durations = [(name, text, start_s, duration_s)]."""
    lines: list[str] = []
    cue_idx = 1
    for _name, text, scene_start, scene_dur in scenes_with_durations:
        sentences = split_sentences(text)
        total_chars = sum(len(s) for s in sentences) or 1
        offset = 0.0
        for sent in sentences:
            share = len(sent) / total_chars
            cue_dur = scene_dur * share
            start = scene_start + offset
            end = start + cue_dur
            lines.append(str(cue_idx))
            lines.append(f"{fmt_srt(start)} --> {fmt_srt(end)}")
            lines.append(sent)
            lines.append("")
            cue_idx += 1
            offset += cue_dur
    return "\n".join(lines)


def main() -> int:
    if not AUDIO_DIR.exists():
        print(f"Audio dir missing: {AUDIO_DIR}", file=sys.stderr)
        return 1

    rows = []
    cumulative = 0.0
    srt_input: list[tuple[str, str, float, float]] = []

    for name, text in BATCH_SCENES:
        mp3 = AUDIO_DIR / f"{name}.mp3"
        if not mp3.exists():
            print(f"MISSING: {mp3.name}", file=sys.stderr)
            continue
        dur = probe_duration(mp3)
        target_start, target_end, cap, on_cam = SCENE_META[name]
        target_dur = target_end - target_start
        drift = dur - target_dur
        rows.append({
            "name": name,
            "text_chars": len(text),
            "dur": dur,
            "target_start": target_start,
            "target_end": target_end,
            "target_dur": target_dur,
            "actual_start": cumulative,
            "actual_end": cumulative + dur,
            "drift": drift,
            "cap": cap,
            "on_cam": on_cam,
        })
        srt_input.append((name, text, cumulative, dur))
        cumulative += dur

    # Cuesheet Markdown
    md = [
        "# M1 — Samaritain Security : cuesheet montage",
        "",
        f"Source audio : 10 MP3 ElevenLabs (voix clone Michaël), dossier `audio-m1/`.",
        f"Durée totale mesurée : **{fmt_hms(cumulative)}** (cible script doc : 4:45.00, drift total : {cumulative - 285:+.2f}s).",
        "",
        "| # | Scène | Capture | Cible script | Durée MP3 réelle | Démarre à | Drift |",
        "|---|-------|---------|--------------|------------------|-----------|-------|",
    ]
    for i, r in enumerate(rows, 1):
        target_range = f"{fmt_hms(r['target_start'])}–{fmt_hms(r['target_end'])} ({r['target_dur']:.0f}s)"
        md.append(
            f"| S{i:02d} | `{r['name']}.mp3` | {r['cap']} | "
            f"{target_range} | {r['dur']:.2f}s | {fmt_hms(r['actual_start'])} | "
            f"{r['drift']:+.2f}s |"
        )
    md += [
        "",
        "## Lecture du drift",
        "",
        "- Drift positif (+) : la voix-off est plus lente que la cible script. Allonge le plan capture ou mets une pause naturelle.",
        "- Drift négatif (-) : la voix-off est plus rapide. Le plan capture peut être raccourci, ou ajoute un fondu enchaîné.",
        "- Drift cumulé global = écart entre la durée vidéo totale et les 4:45 cibles. À répartir sur les face cam (S01, S10) si tu veux retomber pile.",
        "",
        "## Slugs à flouter dans le montage",
        "",
        "- S05 (`M1-S05-nouvelle-url.mp3` + capture 4) — l'URL personnalisée affichée par Samaritain.",
        "- S07 (`M1-S07-nouvelle-url-ok.mp3` + capture 18) — la même URL dans la barre d'adresse Chrome.",
        "",
        "Mêmes coordonnées que l'IP floutée pour rester cohérent (Gaussian blur, padding 4px).",
        "",
    ]

    cuesheet_path = OUT_DIR / "cuesheet-m1.md"
    cuesheet_path.write_text("\n".join(md), encoding="utf-8")

    # SRT subtitles
    srt_body = build_srt_cues(srt_input)
    srt_path = OUT_DIR / "subtitles-m1.srt"
    srt_path.write_text(srt_body, encoding="utf-8")

    print(f"OK cuesheet : {cuesheet_path}")
    print(f"OK SRT      : {srt_path}")
    print(f"Total durée audio M1 : {cumulative:.2f}s ({fmt_hms(cumulative)})")
    print(f"Cible script doc     : 285.00s (4:45.00)")
    print(f"Drift                : {cumulative - 285:+.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
