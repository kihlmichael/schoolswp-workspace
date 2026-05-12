"""A/B test GPT Image 2 (OpenAI) vs Nano Banana (Gemini 2.5 Flash Image)
on 3 schoolsWP use cases that match GPT Image 2's marketed strengths.

Reads OPENAI_API_KEY + GEMINI_API_KEY from projects/schoolswp/.env
Writes PNG outputs + meta.json to outputs/<case>/<engine>.png

Run: .venv/Scripts/python tools/test-gpt-image-2-vs-nano-banana/run.py
"""

from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / ".env"
OUT_DIR = Path(__file__).resolve().parent / "outputs"

OPENAI_MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
OPENAI_ENDPOINT = "https://api.openai.com/v1/images/generations"
GEMINI_MODEL = "gemini-2.5-flash-image"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

GREEN_DESCRIPTION = "vibrant pure grass green schoolsWP signature color, saturated and clean"

CASES: list[dict] = [
    {
        "id": "01-thumbnail-text",
        "label": "Miniature article schoolsWP avec texte integre",
        "prompt": (
            "Wide 16:9 thumbnail for a WordPress blog article review. "
            "Bold typography centered: large title text exactly 'FluentCRM : 1 an apres' "
            "in clean sans-serif white, and below it a smaller subtitle 'Le CRM qui rentabilise' "
            f"in {GREEN_DESCRIPTION}. "
            "Background is a deep dark navy gradient with subtle grain. "
            "On the right third, a stylized abstract illustration of email envelopes flowing "
            "into a glowing dashboard panel, in the same green accent color. "
            "Premium editorial SaaS aesthetic, sharp clean kerning, minimum 80px x-height, "
            "no other text, no watermarks. Aspect ratio strictly 16:9."
        ),
        "size_oai": "1536x1024",
    },
    {
        "id": "02a-carousel-slide1",
        "label": "Carrousel LinkedIn slide 1 (cross-image consistency test)",
        "prompt": (
            "LinkedIn carousel slide, square 1:1 format. "
            "Centered three-quarter portrait of a 35-year-old French male solo founder "
            "with short dark brown hair, neat trimmed beard, wearing a plain charcoal grey hoodie, "
            "sitting at a clean wooden desk with a laptop. Soft natural daylight from the left. "
            "Background: minimalist home office with a single shelf of WordPress books, slightly out of focus. "
            f"In the upper-right corner, a small {GREEN_DESCRIPTION} square logo badge. "
            "Bold sans-serif headline white text on the bottom 30 percent: 'Le Fondateur - Episode 1'. "
            "Premium editorial photography style, magazine-quality, calm professional vibe."
        ),
        "size_oai": "1024x1024",
    },
    {
        "id": "02b-carousel-slide2",
        "label": "Carrousel LinkedIn slide 2 (cross-image consistency test)",
        "prompt": (
            "LinkedIn carousel slide, square 1:1 format. "
            "Same 35-year-old French male solo founder as the previous slide: "
            "short dark brown hair, neat trimmed beard, charcoal grey hoodie. "
            "This time facing the camera straight-on, mid-laugh, hands gesturing in conversation. "
            "Same minimalist home office background with WordPress books shelf. Same lighting and aesthetic. "
            f"Same small {GREEN_DESCRIPTION} square logo badge in upper-right corner. "
            "Bold sans-serif headline white text on the bottom 30 percent: 'Episode 2 - La realite'. "
            "Premium editorial photography style, identical to the previous slide for visual consistency."
        ),
        "size_oai": "1024x1024",
    },
    {
        "id": "03-commercial-illustration",
        "label": "Illustration commerciale brand (workflow plugins WP)",
        "prompt": (
            "Premium SaaS editorial illustration, flat vector style with subtle 3D depth, "
            "16:9 horizontal composition. "
            "Center: a stylized horizontal workflow diagram showing 3 connected nodes flowing left to right. "
            "Node 1 (left): a CRM contact card icon. "
            "Node 2 (middle): a WordPress dashboard panel. "
            "Node 3 (right): a stack of online course modules with a play button. "
            f"Connection lines between nodes pulse with the {GREEN_DESCRIPTION}, "
            "as glowing energy flow. "
            "Background: pure off-white with very subtle isometric grid texture. "
            "Clean professional aesthetic, premium illustration, no text on the icons themselves, "
            "no logos, no other elements. Strictly 16:9."
        ),
        "size_oai": "1536x1024",
    },
]


def load_keys() -> tuple[str, str]:
    keys = {"OPENAI_API_KEY": None, "GEMINI_API_KEY": None}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            for k in keys:
                if line.startswith(f"{k}="):
                    keys[k] = line.split("=", 1)[1].strip()
    for k in keys:
        if not keys[k]:
            keys[k] = os.environ.get(k)
        if not keys[k]:
            raise RuntimeError(f"{k} not found in .env or env")
    return keys["OPENAI_API_KEY"], keys["GEMINI_API_KEY"]


def call_gpt_image_2(prompt: str, size: str, api_key: str) -> tuple[bytes, dict]:
    body = json.dumps(
        {
            "model": OPENAI_MODEL,
            "prompt": prompt,
            "size": size,
            "quality": "medium",
            "n": 1,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        OPENAI_ENDPOINT,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    elapsed = round(time.time() - t0, 2)

    img_b64 = data["data"][0]["b64_json"]
    img_bytes = base64.b64decode(img_b64)
    meta = {
        "engine": "gpt-image-2",
        "model": OPENAI_MODEL,
        "size": size,
        "quality": "medium",
        "elapsed_s": elapsed,
        "usage": data.get("usage", {}),
    }
    return img_bytes, meta


def call_nano_banana(prompt: str, api_key: str) -> tuple[bytes, dict]:
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        f"{GEMINI_ENDPOINT}?key={api_key}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    elapsed = round(time.time() - t0, 2)

    img_b64 = None
    candidates = data.get("candidates", [])
    if not candidates:
        raise RuntimeError(f"No candidates: {json.dumps(data)[:400]}")
    cand0 = candidates[0]
    if "content" not in cand0:
        finish = cand0.get("finishReason", "?")
        safety = cand0.get("safetyRatings", [])
        raise RuntimeError(f"No content (finishReason={finish}, safety={safety})")
    for part in cand0["content"].get("parts", []):
        if "inlineData" in part:
            img_b64 = part["inlineData"]["data"]
            break
    if not img_b64:
        raise RuntimeError(f"No inlineData in Gemini response: {json.dumps(data)[:400]}")
    img_bytes = base64.b64decode(img_b64)
    meta = {
        "engine": "nano-banana",
        "model": GEMINI_MODEL,
        "elapsed_s": elapsed,
    }
    return img_bytes, meta


def run_case(case: dict, oai_key: str, gem_key: str) -> dict:
    case_dir = OUT_DIR / case["id"]
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "prompt.txt").write_text(case["prompt"], encoding="utf-8")

    results = {"case": case["id"], "label": case["label"], "engines": {}}

    print(f"\n=== {case['id']}  {case['label']}")
    print(f"GPT Image 2 ({case['size_oai']}, medium)... ", end="", flush=True)
    try:
        img, meta = call_gpt_image_2(case["prompt"], case["size_oai"], oai_key)
        (case_dir / "gpt-image-2.png").write_bytes(img)
        (case_dir / "gpt-image-2.meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        print(f"OK {meta['elapsed_s']}s")
        results["engines"]["gpt-image-2"] = {"ok": True, **meta}
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:400]
        print(f"FAIL {e.code} {err}")
        results["engines"]["gpt-image-2"] = {"ok": False, "error": f"{e.code} {err}"}
    except Exception as e:
        print(f"FAIL {e}")
        results["engines"]["gpt-image-2"] = {"ok": False, "error": str(e)}

    time.sleep(2)

    print(f"Nano Banana... ", end="", flush=True)
    try:
        img, meta = call_nano_banana(case["prompt"], gem_key)
        (case_dir / "nano-banana.png").write_bytes(img)
        (case_dir / "nano-banana.meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        print(f"OK {meta['elapsed_s']}s")
        results["engines"]["nano-banana"] = {"ok": True, **meta}
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:400]
        print(f"FAIL {e.code} {err}")
        results["engines"]["nano-banana"] = {"ok": False, "error": f"{e.code} {err}"}
    except Exception as e:
        print(f"FAIL {e}")
        results["engines"]["nano-banana"] = {"ok": False, "error": str(e)}

    return results


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    oai_key, gem_key = load_keys()

    summary = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "results": []}
    for case in CASES:
        summary["results"].append(run_case(case, oai_key, gem_key))
        time.sleep(3)

    (OUT_DIR / "_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nSummary written to {OUT_DIR / '_summary.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
