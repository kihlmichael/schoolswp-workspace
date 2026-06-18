"""Auto-blur IPv4 addresses in screenshots stored on Google Drive.

Pipeline:
  1. Download each capture from Drive (via gws CLI)
  2. Run Tesseract OCR with word-level bounding boxes
  3. Detect IPv4 patterns either inside a single OCR word or by concatenating
     adjacent words on the same line (Tesseract often splits "85.95.198.26"
     across multiple words)
  4. Apply a Gaussian blur over each detected bounding box
  5. Re-upload the blurred JPEG to Drive next to the original, suffixed
     "-blurred.jpg"

Why this exists:
  Screenshots contain Michael's personal IP that must be masked before any
  public use (videos, articles). Manual blurring is acceptable for one or two
  captures but does not scale to the dozen+ captures expected for modules M2
  through M5. Scripting it once buys back hours over the next two weeks.

Usage:
  .venv/Scripts/python.exe tools/blur-ip-in-captures/blur_ip.py <drive_folder_id>
  .venv/Scripts/python.exe tools/blur-ip-in-captures/blur_ip.py --file-ids ID1,ID2,ID3

Env:
  TESSERACT_CMD  (optional, default: C:/Program Files/Tesseract-OCR/tesseract.exe)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

import pytesseract
from PIL import Image, ImageFilter

TESSERACT_CMD = os.environ.get(
    "TESSERACT_CMD", r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

GWS_CMD = os.environ.get(
    "GWS_CMD", r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"
)

IP_REGEX = re.compile(r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b")

# Tesseract may split an IP across consecutive tokens. We glue together
# words sharing the same (block_num, par_num, line_num) before regex.


def gws(args: list[str]) -> dict | None:
    """Run a gws drive command and return parsed JSON output, or None."""
    cmd = [GWS_CMD, "drive", *args]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        sys.exit("gws CLI not found in PATH")
    if proc.returncode != 0:
        print(f"gws error: {proc.stderr}", file=sys.stderr)
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def list_folder_jpegs(folder_id: str) -> list[dict]:
    """List image/jpeg files in a Drive folder, excluding already-blurred ones."""
    q = (
        f"'{folder_id}' in parents "
        "and mimeType = 'image/jpeg' "
        "and trashed = false "
        "and not name contains 'blurred'"
    )
    res = gws(
        [
            "files",
            "list",
            "--params",
            json.dumps({"q": q, "fields": "files(id,name)", "pageSize": 200}),
        ]
    )
    return res.get("files", []) if res else []


def download_file(file_id: str, dest: Path) -> bool:
    """Download Drive file content to a local path via gws."""
    res = subprocess.run(
        [
            GWS_CMD,
            "drive",
            "files",
            "get",
            "--params",
            json.dumps({"fileId": file_id, "alt": "media"}),
            "--output",
            str(dest),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if res.returncode != 0:
        print(f"download failed for {file_id}: {res.stderr}", file=sys.stderr)
        return False
    return dest.exists() and dest.stat().st_size > 0


def upload_to_folder(local_path: Path, folder_id: str, name: str) -> str | None:
    """Upload a JPEG into a Drive folder. Returns the new file id."""
    res = subprocess.run(
        [
            GWS_CMD,
            "drive",
            "files",
            "create",
            "--json",
            json.dumps({"name": name, "parents": [folder_id], "mimeType": "image/jpeg"}),
            "--upload",
            str(local_path),
            "--upload-content-type",
            "image/jpeg",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if res.returncode != 0:
        print(f"upload failed: {res.stderr}", file=sys.stderr)
        return None
    try:
        payload = json.loads(res.stdout)
        return payload.get("id")
    except json.JSONDecodeError:
        return None


def get_file_parent(file_id: str) -> str | None:
    """Return the parent folder id of a Drive file."""
    res = gws(
        [
            "files",
            "get",
            "--params",
            json.dumps({"fileId": file_id, "fields": "parents,name"}),
        ]
    )
    if not res:
        return None
    parents = res.get("parents", [])
    return parents[0] if parents else None


def detect_ip_boxes(image: Image.Image) -> list[tuple[int, int, int, int]]:
    """Run OCR and return bounding boxes (left, top, right, bottom) around IPv4 strings.

    Tesseract often tokenises "85.95.198.26" into multiple words. We rebuild
    each text line by joining its words, run IP regex on the line, and map
    matches back to the original tokens via cumulative character offsets.
    """
    data = pytesseract.image_to_data(
        image, output_type=pytesseract.Output.DICT, lang="fra+eng"
    )
    n = len(data["text"])
    # Group token indices by (block, paragraph, line)
    lines: dict[tuple[int, int, int], list[int]] = {}
    for i in range(n):
        txt = data["text"][i]
        if not txt or not txt.strip():
            continue
        key = (data["block_num"][i], data["par_num"][i], data["line_num"][i])
        lines.setdefault(key, []).append(i)

    boxes: list[tuple[int, int, int, int]] = []
    for indices in lines.values():
        # Build the line text and remember the (start, end) char offset for each token
        spans: list[tuple[int, int, int]] = []  # (token_idx, start, end)
        line_chars: list[str] = []
        cursor = 0
        for j, i in enumerate(indices):
            tok = data["text"][i]
            if j > 0:
                line_chars.append(" ")
                cursor += 1
            start = cursor
            line_chars.append(tok)
            cursor += len(tok)
            spans.append((i, start, cursor))
        line_text = "".join(line_chars)

        for match in IP_REGEX.finditer(line_text):
            m_start, m_end = match.start(), match.end()
            # All tokens whose [start, end] intersect [m_start, m_end] are part of the IP
            ip_tokens = [
                idx for (idx, s, e) in spans if not (e <= m_start or s >= m_end)
            ]
            if not ip_tokens:
                continue
            lefts = [data["left"][i] for i in ip_tokens]
            tops = [data["top"][i] for i in ip_tokens]
            rights = [data["left"][i] + data["width"][i] for i in ip_tokens]
            bottoms = [data["top"][i] + data["height"][i] for i in ip_tokens]
            boxes.append((min(lefts), min(tops), max(rights), max(bottoms)))
    return boxes


def blur_boxes(image: Image.Image, boxes: list[tuple[int, int, int, int]], radius: int = 12, padding: int = 4) -> int:
    """Apply Gaussian blur over the given bounding boxes. Returns number of blurs applied."""
    applied = 0
    for left, top, right, bottom in boxes:
        box = (
            max(0, left - padding),
            max(0, top - padding),
            min(image.width, right + padding),
            min(image.height, bottom + padding),
        )
        region = image.crop(box)
        blurred = region.filter(ImageFilter.GaussianBlur(radius=radius))
        image.paste(blurred, box)
        applied += 1
    return applied


def process_file(file_id: str, file_name: str, parent_id: str, work_dir: Path, *, dry_run: bool = False) -> dict:
    src = work_dir / file_name
    if not download_file(file_id, src):
        return {"id": file_id, "name": file_name, "status": "download_failed"}

    with Image.open(src) as im:
        im.load()
        boxes = detect_ip_boxes(im)
        if not boxes:
            return {
                "id": file_id,
                "name": file_name,
                "status": "no_ip_found",
                "blurred": 0,
            }
        applied = blur_boxes(im, boxes)
        blurred_name = file_name.rsplit(".", 1)[0] + "-blurred.jpg"
        dst = work_dir / blurred_name
        im.convert("RGB").save(dst, "JPEG", quality=90)

    if dry_run:
        return {
            "id": file_id,
            "name": file_name,
            "status": "dry_run",
            "blurred": applied,
            "local": str(dst),
            "boxes": boxes,
        }

    new_id = upload_to_folder(dst, parent_id, blurred_name)
    return {
        "id": file_id,
        "name": file_name,
        "status": "uploaded" if new_id else "upload_failed",
        "blurred": applied,
        "new_id": new_id,
        "boxes": boxes,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("folder", nargs="?", help="Drive folder id to scan")
    g.add_argument("--file-ids", help="Comma-separated Drive file ids")
    p.add_argument("--dry-run", action="store_true", help="Do not upload back")
    p.add_argument(
        "--work-dir",
        default=str(Path(__file__).parent / "work"),
        help="Local temp folder for downloads",
    )
    args = p.parse_args(argv)

    work_dir = Path(args.work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)

    targets: list[tuple[str, str, str]] = []  # (id, name, parent_id)

    if args.file_ids:
        for fid in [x.strip() for x in args.file_ids.split(",") if x.strip()]:
            res = gws(
                [
                    "files",
                    "get",
                    "--params",
                    json.dumps({"fileId": fid, "fields": "id,name,parents,mimeType"}),
                ]
            )
            if not res:
                print(f"skip {fid}: cannot read metadata", file=sys.stderr)
                continue
            if not res.get("mimeType", "").startswith("image/"):
                print(f"skip {fid}: not an image ({res.get('mimeType')})", file=sys.stderr)
                continue
            parents = res.get("parents", [])
            if not parents:
                print(f"skip {fid}: no parent folder", file=sys.stderr)
                continue
            targets.append((res["id"], res["name"], parents[0]))
    else:
        files = list_folder_jpegs(args.folder)
        for f in files:
            targets.append((f["id"], f["name"], args.folder))

    if not targets:
        print("Nothing to process")
        return 0

    print(f"Processing {len(targets)} file(s)...")
    results = []
    for fid, fname, parent in targets:
        print(f"  - {fname} ({fid})")
        r = process_file(fid, fname, parent, work_dir, dry_run=args.dry_run)
        print(f"    -> {r['status']}, blurred={r.get('blurred', 0)}")
        results.append(r)

    print()
    print(json.dumps({"results": results}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
