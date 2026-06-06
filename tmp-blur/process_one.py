"""Process one downloaded Drive tool-result JSON: decode base64 JPEG, blur IPs, save.

Usage:
  python process_one.py <tool_result_json> <output_basename>

Reads the JSON {content, id, mimeType, title}, decodes base64 content into
<basename>.jpg, runs detect_ip_boxes + blur_boxes, saves <basename>-blurred.jpg,
and prints a JSON summary on stdout (boxes + counts + paths).
"""
from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

# Make the blur_ip module importable
ROOT = Path(__file__).resolve().parents[1]  # projects/schoolswp/
sys.path.insert(0, str(ROOT / "tools" / "blur-ip-in-captures"))

from PIL import Image  # noqa: E402

import blur_ip  # noqa: E402


def main() -> int:
    tool_json_path = Path(sys.argv[1])
    basename = sys.argv[2]
    out_dir = Path(__file__).parent

    payload = json.loads(tool_json_path.read_text(encoding="utf-8"))
    b64 = payload["content"]
    raw = base64.b64decode(b64)

    src = out_dir / f"{basename}.jpg"
    src.write_bytes(raw)

    with Image.open(src) as im:
        im.load()
        # Convert to RGB to make sure paste works fine and re-encoding is consistent
        if im.mode != "RGB":
            im = im.convert("RGB")
        boxes = blur_ip.detect_ip_boxes(im)
        applied = blur_ip.blur_boxes(im, boxes) if boxes else 0
        dst = out_dir / f"{basename}-blurred.jpg"
        if boxes:
            im.save(dst, "JPEG", quality=92)

    out_b64 = ""
    if boxes:
        out_b64 = base64.b64encode(dst.read_bytes()).decode("ascii")

    summary = {
        "source_title": payload.get("title"),
        "source_id": payload.get("id"),
        "src_path": str(src),
        "dst_path": str(dst) if boxes else None,
        "src_size": src.stat().st_size,
        "dst_size": dst.stat().st_size if boxes else 0,
        "boxes": boxes,
        "blurred_count": applied,
        "image_size": im.size,
    }
    # Print summary on stdout; write base64 separately to keep stdout small
    if boxes:
        (out_dir / f"{basename}-blurred.b64").write_text(out_b64, encoding="ascii")
        summary["b64_path"] = str(out_dir / f"{basename}-blurred.b64")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
