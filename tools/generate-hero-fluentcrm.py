"""Genere hero + schema triggers/actions/benchmarks pour l'article
/fluentcrm-automations-indispensables/ via Gemini 2.5 Flash Image (API directe).

- Lit GEMINI_API_KEY depuis .claude/settings.local.json (pas .env, safety)
- Modele GA gemini-2.5-flash-image (pas -preview qui est cassee)
- Espacement 15s entre appels pour eviter rate-limit free tier
- Output : content/articles/fluentcrm-automatisations-indispensables/captures-brand/
"""
import base64
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SETTINGS = ROOT / ".claude" / "settings.local.json"
ENV_FILE = ROOT / ".env"
OUT_DIR = ROOT / "content" / "articles" / "fluentcrm-automatisations-indispensables" / "captures-brand"

MODEL = "gemini-2.5-flash-image"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def load_api_key() -> str:
    """Read GEMINI_API_KEY from .env first (priority per memory rule), fallback settings.local.json."""
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("GEMINI_API_KEY"):
                _, _, val = line.partition("=")
                val = val.strip().strip('"').strip("'")
                if val:
                    return val
    with open(SETTINGS, encoding="utf-8") as f:
        data = json.load(f)
    return data["env"]["GEMINI_API_KEY"]


def generate(prompt: str, output_path: Path, api_key: str) -> None:
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    req = urllib.request.Request(
        f"{ENDPOINT}?key={api_key}",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    print(f"  -> POST {MODEL} for {output_path.name}")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"  HTTP {e.code} BODY: {err_body[:600]}")
        raise
    parts = data["candidates"][0]["content"]["parts"]
    for part in parts:
        if "inlineData" in part:
            img = base64.b64decode(part["inlineData"]["data"])
            output_path.write_bytes(img)
            print(f"  OK saved {output_path.name} ({len(img)} bytes)")
            return
    raise RuntimeError(f"No inlineData in response: {json.dumps(data)[:400]}")


HERO_PROMPT = """Modern editorial hero image for a WordPress marketing automation tutorial, horizontal landscape 16:9.

Theme: FluentCRM email marketing automation on WordPress. The image should illustrate automated email workflows, lead nurturing, and customer journey.

Visual style: clean isometric flat illustration, professional editorial SaaS aesthetic, no real text or letters visible anywhere in the image (no logos, no readable words).

Composition: show an abstract email automation flow as a connected pipeline of 4 floating cards moving from left to right. The cards represent stages of a workflow without any text inside them, just abstract icons:
- First card: a tag-like shape (trigger)
- Second card: an envelope icon (first email)
- Third card: a clock icon (wait time)
- Fourth card: another envelope icon (follow-up email)
Thin curved arrows connect the cards in sequence.

Color palette: very light cool gray as main background, dark navy blue accents on shapes outlines, a single signature bright kelly green color used SPARINGLY only on arrows tips and small dot highlights for visual emphasis. No other colors.

Lighting: soft drop shadows below each card, gentle ambient occlusion. Breathing space, centered composition. No people, no text, no UI screenshots, no logos."""


SCHEMA_PROMPT = """Educational infographic diagram, horizontal 16:9 landscape format.

Show three vertical columns side by side with equal width and visual rhythm. Each column has a vertical accent bar on its left side in a bright kelly green color.

The columns represent three categories of automation building blocks. Each column has a category header at top (just an icon, no text), then 5 abstract icon tiles stacked vertically below it.

Column 1 icons: a tag shape, a list/rows icon, a form/input box, a shopping cart, a user silhouette.
Column 2 icons: an envelope, a tag plus a green plus sign, a clock, a webhook fork icon, a checkmark.
Column 3 icons: a target/bullseye, a shopping cart with a check, a flag, a chart bar, an arrow into a circle.

Connect the three columns with thin curved arrows flowing left to right between them, indicating data flow.

Color palette: very light cool gray background, dark navy blue for icon outlines and column headers area, bright kelly green only on accent vertical bars and arrow tips.

Style: minimal flat illustration, clean modern SaaS dashboard aesthetic, generous whitespace, subtle drop shadows on icon tiles. No real text, no letters, no logos, no UI screenshots. Just abstract pictograms."""


def main() -> int:
    api_key = load_api_key()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    targets = [
        ("hero-fluentcrm-automatisation.png", HERO_PROMPT),
        ("schema-triggers-actions-benchmarks.png", SCHEMA_PROMPT),
    ]
    for i, (filename, prompt) in enumerate(targets):
        out = OUT_DIR / filename
        try:
            generate(prompt, out, api_key)
        except Exception as e:
            print(f"  ERR {filename}: {e}")
        if i < len(targets) - 1:
            print("  ...waiting 15s to avoid rate-limit...")
            time.sleep(15)
    return 0


if __name__ == "__main__":
    sys.exit(main())
