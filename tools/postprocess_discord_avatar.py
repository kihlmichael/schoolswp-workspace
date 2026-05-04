"""Post-process the Discord orchestrator avatar to force pure schoolsWP green.

Gemini outputs a slightly desaturated green; this script remasks it to #00D400.
Background pixels (near-black) are forced to pure black #12111F for brand match.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "discord-avatars" / "01-orchestrator-discord.png"
DST = SRC

BRAND_GREEN = (0, 212, 0)
BRAND_BLACK = (18, 17, 31)


def main() -> int:
    img = Image.open(SRC).convert("RGB")
    arr = np.array(img)

    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]

    is_green = (g.astype(int) > r.astype(int) + 10) & (g.astype(int) > b.astype(int) + 10) & (g > 60)
    is_black = (r < 40) & (g < 40) & (b < 40)

    out = arr.copy()
    out[is_green] = BRAND_GREEN
    out[is_black] = BRAND_BLACK

    Image.fromarray(out).save(DST, "PNG", optimize=True)
    print(f"OK ({DST.stat().st_size // 1024} KB) -> {DST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
