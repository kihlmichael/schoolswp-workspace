"""
Script de generation d'images pour les 3 angles FluentCRM.
Execute : .venv/Scripts/python .claude/skills/landing-page-factory/-workspace/iteration-2/eval-fluentcrm/outputs/generate-images.py
Prerequis : pip install openai, variable OPENAI_API_KEY dans .env
"""

import os
import base64
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_DIR = Path(__file__).parent / "images"

PROMPTS = {
    "angle-1": {
        "dir": BASE_DIR / "angle-1",
        "prompt": (
            "Dark-themed dashboard mockup showing email marketing analytics. "
            "Background color #12111F, accent green #00D400 on graphs and metrics, "
            "secondary magenta accent #E668D4 on notification badges. "
            "Clean flat UI design with email campaign stats: open rate 45 percent, "
            "click rate 12 percent, subscriber count 10247. "
            "Modern sans-serif typography. Minimal isometric style. "
            "No text except numbers on the dashboard. Professional SaaS interface feel."
        ),
    },
    "angle-2": {
        "dir": BASE_DIR / "angle-2",
        "prompt": (
            "Dark-themed isometric illustration showing WordPress ecosystem integration. "
            "Background #12111F. Central WordPress logo connected by glowing green #00D400 lines "
            "to floating plugin icons: shopping cart (WooCommerce), graduation cap (LMS), "
            "envelope (email), form clipboard, and contact card. "
            "Magenta #E668D4 accent on connection nodes. "
            "Clean flat vector style, no photography, no people. "
            "Spacious composition with breathing room between elements."
        ),
    },
    "angle-3": {
        "dir": BASE_DIR / "angle-3",
        "prompt": (
            "Dark-themed illustration about data sovereignty and privacy. "
            "Background #12111F. A shield icon in green #00D400 protecting a database cylinder. "
            "EU flag subtly integrated. Lock symbols in magenta #E668D4. "
            "Contrast with a fading cloud icon in gray representing SaaS platforms. "
            "Clean flat vector style, isometric perspective. "
            "No text, no people. Minimal and professional."
        ),
    },
}


def generate_image(name: str, config: dict) -> None:
    out_dir = config["dir"]
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating {name}...")
    result = client.images.generate(
        model="gpt-image-1",
        prompt=config["prompt"],
        n=1,
        size="1536x1024",
        quality="high",
    )

    image_data = base64.b64decode(result.data[0].b64_json)
    out_path = out_dir / "hero.png"
    out_path.write_bytes(image_data)
    print(f"  Saved: {out_path}")


if __name__ == "__main__":
    for name, config in PROMPTS.items():
        generate_image(name, config)
    print("Done. 3 images generated.")
