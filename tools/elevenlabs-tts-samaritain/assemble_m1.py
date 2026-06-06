"""Assemble the M1 Samaritain Security teaching video end-to-end.

Pipeline:
  1. Download the 6 needed Drive captures via gws CLI (cached).
  2. Generate 4 schoolsWP-branded placeholder cards via PIL
     (S01 hook face cam, S02 screencast Extensions, S03 screencast téléverser,
      S10 outro face cam). Michael will swap with real footage later.
  3. Build 11 per-scene MP4 segments (S04 is split into S04a + S04b for the
     two-capture sequence licence-empty -> licence-active). Each segment
     loops one image for the duration of its scene's MP3.
  4. Concat the segments with ffmpeg, burn the SRT subtitles in the final pass.
     Output: content/formations/samaritain-security/production/m1-final.mp4
             1080p, H.264 yuv420p, AAC 192 kbps.

Idempotent: re-running only redoes what's missing. Pass --force to wipe
the work dir and start fresh.

Usage:
  .venv/Scripts/python.exe tools/elevenlabs-tts-samaritain/assemble_m1.py
  .venv/Scripts/python.exe tools/elevenlabs-tts-samaritain/assemble_m1.py --force
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
TOOL_DIR = Path(__file__).resolve().parent
AUDIO_DIR = PROJECT_ROOT / "content" / "formations" / "samaritain-security" / "production" / "audio-m1"
CACHE_DIR = TOOL_DIR / "captures-cache"
WORK_DIR = TOOL_DIR / "work-m1"
OUT_PATH = PROJECT_ROOT / "content" / "formations" / "samaritain-security" / "production" / "m1-final.mp4"
SRT_PATH = AUDIO_DIR / "subtitles-m1.srt"

GWS_CMD = r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"

VIDEO_W, VIDEO_H = 1920, 1080
FPS = 30

# schoolsWP brand colors
BRAND_DARK_BG = (15, 20, 25)       # #0F1419
BRAND_LIGHT_FG = (244, 245, 247)   # #F4F5F7
BRAND_GREEN = (0, 212, 0)          # #00D400 — "WP" accent

# Drive IDs of the captures referenced by the TTS script doc.
# Names: capN refers to the "Sans-titre-N.jpg" numbering in the Drive folder
# 1TV2_zkuHoeBAGoM4CnZ9o-8m1JRL9OMy. Numbers chosen per the TTS doc mapping.
CAPTURES_NEEDED = {
    "cap-2-dashboard":      "1h_nxPi2uVkwgQkr_9g0j65G-dvAFaNMz",  # Sans-titre-2.jpg, dashboard 96/100
    "cap-3-licence-active": "1t0xgffBye6kug5AU0MfPLrPCglWn3Tzx",  # Sans-titre-3.jpg, licence active
    "cap-4-nouvelle-url":   "1N99kyTAn29TVjvGXxh3BwpXou69NzCZB",  # Sans-titre-4.jpg, URL connexion
    "cap-17-page-404":      "1oIpWps5TG7FKPhIkWph4kCDjFcmcMURo",  # Sans-titre-17.jpg, 404
    "cap-18-login-slug":    "1N-0KFXAg_cKcF1FsIQ1HJvbrmJwlqnqX",  # Sans-titre-18.jpg, login slug perso
    "cap-19-licence-vide":  "1NKu5-wRVjiDRZic8y-QqjHuMQMUERgAF",  # Sans-titre-19.jpg, licence vide
}

# Scene timeline: (segment_id, image_source, audio_name, duration_share)
# duration_share: float in [0,1] — for scenes split across multiple images.
# image_source variants:
#   "cache:cap-name"                            -> normalize_image on cached capture
#   "placeholder:title|subtitle"                -> schoolsWP-branded card
#   "zoom:cap-name|x,y,w,h"                     -> crop the named cache image to
#                                                  (x,y,w,h) then scale-to-fit on
#                                                  1920x1080 brand-dark canvas
SCENE_PLAN = [
    ("S01",  "placeholder:Samaritain Security|Sécuriser ton WordPress en 1 clic",  "M1-S01-hook",              1.0),
    ("S02",  "placeholder:Module 1 - Étape 1|Désactive ton autre plugin sécu",     "M1-S02-desactiver",        1.0),
    ("S03",  "placeholder:Module 1 - Étape 2|Téléverse et active Samaritain",      "M1-S03-televerser",        1.0),
    ("S04a", "cache:cap-19-licence-vide",                                          "M1-S04-licence",           0.45),
    ("S04b", "cache:cap-3-licence-active",                                         "M1-S04-licence",           0.55),
    ("S05",  "cache:cap-4-nouvelle-url",                                           "M1-S05-nouvelle-url",      1.0),
    ("S06",  "cache:cap-17-page-404",                                              "M1-S06-preuve-404",        1.0),
    ("S07",  "cache:cap-18-login-slug",                                            "M1-S07-nouvelle-url-ok",   1.0),
    ("S08",  "cache:cap-3-licence-active",                                         "M1-S08-url-secours",       1.0),
    ("S09",  "cache:cap-2-dashboard",                                              "M1-S09-dashboard",         1.0),
    ("S10",  "placeholder:Rendez-vous au Module 2|Décode ton score, étape par étape", "M1-S10-outro",          1.0),
]


# ---------------------------------------------------------------------------
# Step 1: download captures
# ---------------------------------------------------------------------------
def download_captures() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    for name, file_id in CAPTURES_NEEDED.items():
        dest = CACHE_DIR / f"{name}.jpg"
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  cached: {name}.jpg ({dest.stat().st_size} B)")
            continue
        print(f"  fetching: {name}.jpg ...")
        res = subprocess.run(
            [GWS_CMD, "drive", "files", "get",
             "--params", json.dumps({"fileId": file_id, "alt": "media"}),
             "--output", str(dest)],
            capture_output=True, text=True, check=False,
        )
        if res.returncode != 0 or not dest.exists():
            raise RuntimeError(f"gws download failed for {name}: {res.stderr or res.stdout}")
        print(f"    -> {dest.stat().st_size} B")


# ---------------------------------------------------------------------------
# Step 2: build branded placeholder cards
# ---------------------------------------------------------------------------
def find_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Return a usable system font, falling back to PIL default if none found."""
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def build_placeholder(title: str, subtitle: str, dest: Path) -> None:
    """Render a 1920x1080 schoolsWP-branded card with wordmark + title + subtitle."""
    img = Image.new("RGB", (VIDEO_W, VIDEO_H), BRAND_DARK_BG)
    draw = ImageDraw.Draw(img)

    # Wordmark "schoolsWP" top-left, "WP" in green
    wm_font = find_font(56, bold=True)
    schools_w = draw.textlength("schools", font=wm_font)
    draw.text((80, 70), "schools", font=wm_font, fill=BRAND_LIGHT_FG)
    draw.text((80 + schools_w, 70), "WP", font=wm_font, fill=BRAND_GREEN)

    # Title centered
    title_font = find_font(96, bold=True)
    tw = draw.textlength(title, font=title_font)
    draw.text(((VIDEO_W - tw) / 2, 400), title, font=title_font, fill=BRAND_LIGHT_FG)

    # Subtitle centered, lighter weight
    sub_font = find_font(48, bold=False)
    sw = draw.textlength(subtitle, font=sub_font)
    draw.text(((VIDEO_W - sw) / 2, 560), subtitle, font=sub_font, fill=BRAND_LIGHT_FG)

    # Green accent bar bottom
    draw.rectangle([(0, VIDEO_H - 12), (VIDEO_W, VIDEO_H)], fill=BRAND_GREEN)

    img.save(dest, "JPEG", quality=92)


# ---------------------------------------------------------------------------
# Step 3: per-scene MP4 segments (image loop + audio)
# ---------------------------------------------------------------------------
def probe_duration(mp3: Path) -> float:
    res = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", str(mp3)],
        capture_output=True, text=True, check=True,
    )
    return float(json.loads(res.stdout)["format"]["duration"])


def build_zoom_image(src: Path, dest: Path, box: tuple[int, int, int, int]) -> None:
    """Crop a region of the source capture and scale-to-fit on a 1920x1080 brand canvas.

    The zoom region is given as (x, y, w, h) in the SOURCE image coordinates
    (i.e. the cap-N.jpg file at its native resolution). After cropping, the
    region is scaled (Lanczos) to fit within 1920x1080 while preserving its
    aspect ratio, then centered on a brand-dark canvas with letterbox padding.
    """
    x, y, w, h = box
    with Image.open(src) as im:
        im = im.convert("RGB")
        crop = im.crop((x, y, x + w, y + h))
        ratio = min(VIDEO_W / crop.width, VIDEO_H / crop.height)
        new_w = max(1, int(crop.width * ratio))
        new_h = max(1, int(crop.height * ratio))
        # Snap to even dimensions to keep libx264 yuv420p happy
        new_w -= new_w % 2
        new_h -= new_h % 2
        resized = crop.resize((new_w, new_h), Image.LANCZOS)
        canvas = Image.new("RGB", (VIDEO_W, VIDEO_H), BRAND_DARK_BG)
        offset = ((VIDEO_W - new_w) // 2, (VIDEO_H - new_h) // 2)
        canvas.paste(resized, offset)
        canvas.save(dest, "JPEG", quality=95, subsampling=0)


def normalize_image(src: Path, dest: Path) -> None:
    """Place the capture on a 1920x1080 brand-dark canvas WITHOUT upscaling.

    Captures are typically exported by Photoshop at 1024px wide ('save for web'),
    well below the 1080p target. Upscaling produces blur; keeping native pixels
    centered on the brand canvas is sharper, even if the effective image area
    is smaller. If the capture is larger than 1920x1080, downscale (Lanczos)
    to fit since downscaling preserves detail.
    """
    with Image.open(src) as im:
        im = im.convert("RGB")
        canvas = Image.new("RGB", (VIDEO_W, VIDEO_H), BRAND_DARK_BG)
        if im.width > VIDEO_W or im.height > VIDEO_H:
            ratio = min(VIDEO_W / im.width, VIDEO_H / im.height)
            new_w, new_h = int(im.width * ratio), int(im.height * ratio)
            im = im.resize((new_w, new_h), Image.LANCZOS)
        offset = ((VIDEO_W - im.width) // 2, (VIDEO_H - im.height) // 2)
        canvas.paste(im, offset)
        canvas.save(dest, "JPEG", quality=95, subsampling=0)


def build_segment(image_path: Path, audio_path: Path, duration: float, out: Path) -> None:
    """Encode a single scene as a silent-looped image with the matching MP3 audio."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", str(FPS), "-i", str(image_path),
        "-i", str(audio_path),
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", f"{duration:.3f}",
        "-shortest",
        str(out),
    ]
    subprocess.run(cmd, check=True)


def build_segment_image_only(image_path: Path, duration: float, out: Path) -> None:
    """Encode a silent image-only segment (used for the second half of S04)."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", str(FPS), "-i", str(image_path),
        "-f", "lavfi", "-i", f"anullsrc=channel_layout=stereo:sample_rate=48000",
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k",
        "-t", f"{duration:.3f}",
        "-shortest",
        str(out),
    ]
    subprocess.run(cmd, check=True)


def build_segment_with_audio_offset(
    image_path: Path, audio_path: Path, audio_start: float, duration: float, out: Path
) -> None:
    """Encode a segment that consumes part of an MP3 (start offset + duration)."""
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", str(FPS), "-i", str(image_path),
        "-ss", f"{audio_start:.3f}", "-t", f"{duration:.3f}", "-i", str(audio_path),
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", f"{duration:.3f}",
        "-shortest",
        str(out),
    ]
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------------------
# Step 4: concat + burn subtitles
# ---------------------------------------------------------------------------
def concat_and_burn(segment_paths: list[Path], srt: Path, out: Path) -> None:
    """Concat segments with the concat demuxer, then burn SRT subtitles."""
    list_file = WORK_DIR / "concat.txt"
    list_file.write_text(
        "\n".join(f"file '{p.as_posix()}'" for p in segment_paths) + "\n",
        encoding="utf-8",
    )

    intermediate = WORK_DIR / "concat-raw.mp4"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-f", "concat", "-safe", "0", "-i", str(list_file),
         "-c", "copy",
         str(intermediate)],
        check=True,
    )

    # Burn SRT. Windows quirks: ffmpeg subtitles filter wants forward slashes
    # and a backslash-escaped colon for the drive letter. Convert here.
    srt_for_filter = str(srt).replace("\\", "/").replace(":", "\\:")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-i", str(intermediate),
         "-vf", f"subtitles='{srt_for_filter}':force_style='Fontname=Segoe UI,Fontsize=18,PrimaryColour=&H00FFFFFF,OutlineColour=&HC0000000,BorderStyle=1,Outline=1.5,Shadow=0.5,MarginV=40'",
         "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "copy",
         str(out)],
        check=True,
    )


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------
def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--force", action="store_true", help="wipe work + cache and rebuild from scratch")
    args = p.parse_args()

    if args.force:
        if WORK_DIR.exists():
            shutil.rmtree(WORK_DIR)
        # Don't wipe cache — re-downloading captures is wasteful and Drive auth flaky.

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not SRT_PATH.exists():
        print(f"SRT missing: {SRT_PATH} - run cuesheet_srt.py first", file=sys.stderr)
        return 1

    print("[1/4] Downloading needed captures via gws...")
    download_captures()

    print("[2/4] Generating placeholder cards + normalizing capture frames...")
    images_dir = WORK_DIR / "images"
    images_dir.mkdir(exist_ok=True)
    for seg_id, source, _audio, _share in SCENE_PLAN:
        dest = images_dir / f"{seg_id}.jpg"
        if dest.exists():
            continue
        if source.startswith("placeholder:"):
            title, subtitle = source[len("placeholder:"):].split("|", 1)
            print(f"  placeholder {seg_id}: {title}")
            build_placeholder(title, subtitle, dest)
        elif source.startswith("cache:"):
            cap_name = source[len("cache:"):]
            print(f"  normalize  {seg_id}: {cap_name}")
            normalize_image(CACHE_DIR / f"{cap_name}.jpg", dest)
        elif source.startswith("zoom:"):
            cap_name, box_str = source[len("zoom:"):].split("|", 1)
            box = tuple(int(v) for v in box_str.split(","))
            if len(box) != 4:
                raise ValueError(f"zoom box must have 4 ints, got: {box_str}")
            print(f"  zoom       {seg_id}: {cap_name} crop={box}")
            build_zoom_image(CACHE_DIR / f"{cap_name}.jpg", dest, box)
        else:
            raise ValueError(f"Unknown image source: {source}")

    print("[3/4] Building per-scene MP4 segments...")
    segments_dir = WORK_DIR / "segments"
    segments_dir.mkdir(exist_ok=True)
    segment_paths: list[Path] = []

    # Pre-measure each audio file
    audio_durations: dict[str, float] = {}
    for _, _, audio_name, _ in SCENE_PLAN:
        if audio_name in audio_durations:
            continue
        mp3 = AUDIO_DIR / f"{audio_name}.mp3"
        audio_durations[audio_name] = probe_duration(mp3)

    # Track how much of each audio file has been consumed (for split scenes)
    audio_offsets: dict[str, float] = {name: 0.0 for name in audio_durations}

    for seg_id, _source, audio_name, share in SCENE_PLAN:
        seg_path = segments_dir / f"{seg_id}.mp4"
        segment_paths.append(seg_path)
        if seg_path.exists():
            print(f"  skip  {seg_id}.mp4 (already built)")
            continue

        img = images_dir / f"{seg_id}.jpg"
        mp3 = AUDIO_DIR / f"{audio_name}.mp3"
        full_dur = audio_durations[audio_name]
        seg_dur = full_dur * share

        if share >= 0.999:
            # Whole audio file -> straightforward segment
            print(f"  build {seg_id}.mp4 ({seg_dur:.2f}s, full {audio_name})")
            build_segment(img, mp3, seg_dur, seg_path)
        else:
            # Slice of audio starting where the last share left off
            start = audio_offsets[audio_name]
            print(f"  build {seg_id}.mp4 ({seg_dur:.2f}s, {audio_name} from {start:.2f}s)")
            build_segment_with_audio_offset(img, mp3, start, seg_dur, seg_path)
            audio_offsets[audio_name] = start + seg_dur

    print("[4/4] Concatenating + burning subtitles...")
    concat_and_burn(segment_paths, SRT_PATH, OUT_PATH)

    final_size = OUT_PATH.stat().st_size
    print()
    print(f"OK  : {OUT_PATH}")
    print(f"Size: {final_size / 1024 / 1024:.2f} MB")
    final_dur = probe_duration(OUT_PATH)
    print(f"Dur : {final_dur:.2f}s ({int(final_dur // 60)}:{final_dur % 60:05.2f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
