"""Génère les variants 1:1, 9:16, 2:3 de la vidéo FlyingPress vs WP Rocket
à partir du master 16:9. Ne modifie que canvas/viewport/CSS — JS GSAP inchangé.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent
MASTER = ROOT / "16x9" / "index.html"

# Override CSS injecté pour les formats sans hauteur "wide" (vertical/carré).
# Force la séparation domain/path de l'URL CTA sur 2 lignes pour éviter overflow.
URL_SPLIT_OVERRIDE = """
      .cta-url .domain,
      .cta-url .path {
        display: block;
        line-height: 1.3;
      }"""

# Override layout pour formats verticaux : empile .scores et .prices au lieu de
# côte-à-côte. Permet aussi gaps plus petits pour économiser la hauteur.
VERTICAL_COMPARE_OVERRIDE = """
      .scores,
      .prices {
        flex-direction: column;
      }"""


def transform_canvas(html: str, w: int, h: int) -> str:
    """Force body et #root aux dimensions canvas finales. Permissif sur les
    valeurs sources (peut être appelé après scale_property).
    """
    html = re.sub(
        r'content="width=\d+, height=\d+"',
        f'content="width={w}, height={h}"',
        html,
    )
    html = re.sub(
        r"(html,\s*body\s*\{[^}]*?width:\s*)\d+px;",
        rf"\g<1>{w}px;",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"(html,\s*body\s*\{[^}]*?height:\s*)\d+px;",
        rf"\g<1>{h}px;",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"(#root\s*\{[^}]*?width:\s*)\d+px;",
        rf"\g<1>{w}px;",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r"(#root\s*\{[^}]*?height:\s*)\d+px;",
        rf"\g<1>{h}px;",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(r'data-width="\d+"', f'data-width="{w}"', html)
    html = re.sub(r'data-height="\d+"', f'data-height="{h}"', html)
    return html


def scale_font_sizes(html: str, factor: float) -> str:
    def replace(match: re.Match[str]) -> str:
        size = int(match.group(1))
        return f"font-size: {round(size * factor)}px"

    return re.sub(r"font-size:\s*(\d+)px", replace, html)


def scale_property(html: str, prop: str, factor: float) -> str:
    def replace(match: re.Match[str]) -> str:
        size = int(match.group(1))
        scaled = max(1, round(size * factor))
        return f"{prop}: {scaled}px"

    return re.sub(rf"{prop}:\s*(\d+)px", replace, html)


def inject_overrides(html: str, *, vertical_compare: bool, split_url: bool) -> str:
    """Insère les overrides CSS juste avant </style>."""
    extra = ""
    if vertical_compare:
        extra += VERTICAL_COMPARE_OVERRIDE
    if split_url:
        extra += URL_SPLIT_OVERRIDE
    if not extra:
        return html
    return html.replace("</style>", f"{extra}\n    </style>", 1)


def build_variant(
    out_dir: Path,
    *,
    w: int,
    h: int,
    scale: float,
    vertical_compare: bool,
    split_url: bool,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    html = MASTER.read_text(encoding="utf-8")
    # ORDRE CRITIQUE: scale d'abord (sur les valeurs master 1920x1080), PUIS
    # transform_canvas pour forcer body/root aux bonnes dimensions finales
    # (sinon scale_property("width") rescale body 1080→594 et tout déborde).
    html = scale_font_sizes(html, scale)
    for prop in ("width", "height", "margin-bottom", "margin-top", "gap", "letter-spacing"):
        html = scale_property(html, prop, scale)
    html = transform_canvas(html, w, h)
    html = inject_overrides(html, vertical_compare=vertical_compare, split_url=split_url)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    config = (ROOT.parent.parent / "hyperframes.json").read_text(encoding="utf-8")
    (out_dir / "hyperframes.json").write_text(config, encoding="utf-8")
    print(f"OK {out_dir.relative_to(ROOT)} ({w}x{h}, scale={scale})")


if __name__ == "__main__":
    # Scales calibrés sur la largeur (= contrainte horizontale).
    # 16:9 master = 1920 px wide. Pour les autres formats :
    # - 1:1 (1080) : 1080/1920 = 0.5625 → on descend à 0.50 car layout
    #   reste côte-à-côte, donc 2 blocs + gap doivent tenir en 1080.
    # - 9:16 (1080) : layout vertical, on peut un peu plus grossir → 0.55.
    # - 2:3 (1000) : layout vertical mais largeur encore plus serrée → 0.50.
    build_variant(
        ROOT / "1x1",
        w=1080,
        h=1080,
        scale=0.50,
        vertical_compare=False,
        split_url=True,
    )
    build_variant(
        ROOT / "9x16",
        w=1080,
        h=1920,
        scale=0.55,
        vertical_compare=True,
        split_url=True,
    )
    build_variant(
        ROOT / "2x3",
        w=1000,
        h=1500,
        scale=0.50,
        vertical_compare=True,
        split_url=True,
    )
