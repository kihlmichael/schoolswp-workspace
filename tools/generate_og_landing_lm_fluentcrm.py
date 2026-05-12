"""Generate OG image 1200x630 for landing page /template-welcome-fluentcrm/.

Pure PIL composition (no AI) for exact brand colors + perfect FR text rendering.

Output : assets/og-images/og-template-welcome-fluentcrm.png
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og-images" / "og-template-welcome-fluentcrm.png"

# Brand
W, H = 1200, 630
DARK = (15, 20, 25)        # #0F1419
GREEN = (0, 212, 0)         # #00D400
WHITE = (255, 255, 255)
LIGHT = (244, 245, 247)     # #F4F5F7
GREY = (91, 99, 112)        # #5b6370
GREEN_SOFT = (0, 168, 0)    # darker green for hover/accent
PDF_BG = (255, 255, 255)
PDF_LINE = (224, 230, 235)

FONT_DIR = "C:/Windows/Fonts"


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    p = f"{FONT_DIR}/{name}"
    return ImageFont.truetype(p, size)


def text_size(draw: ImageDraw.ImageDraw, txt: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), txt, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_pdf_mockup(img: Image.Image, x: int, y: int, w: int, h: int) -> None:
    """Draw a simplified PDF page mockup with title + content lines + green accent."""
    # Shadow
    shadow_offset = 14
    sh = Image.new("RGBA", (w + shadow_offset * 2, h + shadow_offset * 2), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(sh)
    sh_draw.rounded_rectangle(
        (shadow_offset, shadow_offset, shadow_offset + w, shadow_offset + h),
        radius=10,
        fill=(0, 0, 0, 70),
    )
    # blur the shadow
    from PIL import ImageFilter
    sh = sh.filter(ImageFilter.GaussianBlur(radius=12))
    img.alpha_composite(sh, (x - shadow_offset, y - shadow_offset))

    # Page (white) with green left strip
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=PDF_BG)
    # Green accent strip on left
    strip_w = 8
    draw.rounded_rectangle(
        (x, y, x + strip_w, y + h),
        radius=4,
        fill=GREEN,
    )

    # Top title bar (green pill)
    pad = 28
    title_y = y + pad
    pill_w, pill_h = 96, 22
    draw.rounded_rectangle(
        (x + pad, title_y, x + pad + pill_w, title_y + pill_h),
        radius=11,
        fill=GREEN,
    )
    pill_font = load_font("arialbd.ttf", 11)
    draw.text((x + pad + 12, title_y + 4), "schoolsWP", font=pill_font, fill=WHITE)

    # PDF heading
    head_font = load_font("arialbd.ttf", 22)
    draw.text(
        (x + pad, title_y + 40),
        "Sequence welcome",
        font=head_font,
        fill=DARK,
    )
    draw.text(
        (x + pad, title_y + 68),
        "FluentCRM",
        font=head_font,
        fill=GREEN,
    )

    # Sub label
    sub_font = load_font("arial.ttf", 12)
    draw.text(
        (x + pad, title_y + 102),
        "Template pret a copier . 4 emails . 7 jours",
        font=sub_font,
        fill=GREY,
    )

    # Content lines (mock paragraphs)
    line_y = title_y + 138
    line_h = 7
    line_gap = 12
    line_widths = [w - pad * 2, w - pad * 2 - 30, w - pad * 2 - 60, w - pad * 2,
                   w - pad * 2 - 80, w - pad * 2 - 20, w - pad * 2 - 100]
    for lw in line_widths:
        draw.rounded_rectangle(
            (x + pad, line_y, x + pad + lw, line_y + line_h),
            radius=3,
            fill=PDF_LINE,
        )
        line_y += line_h + line_gap

    # Green CTA mock at bottom
    cta_y = y + h - 60
    cta_w = w - pad * 2
    draw.rounded_rectangle(
        (x + pad, cta_y, x + pad + cta_w, cta_y + 30),
        radius=6,
        fill=(240, 255, 240),
        outline=GREEN,
        width=2,
    )
    cta_font = load_font("arialbd.ttf", 11)
    cta_text = "Telecharger le PDF"
    tw, th = text_size(draw, cta_text, cta_font)
    draw.text(
        (x + pad + (cta_w - tw) // 2, cta_y + (30 - th) // 2 - 2),
        cta_text,
        font=cta_font,
        fill=GREEN_SOFT,
    )


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGBA", (W, H), DARK + (255,))
    draw = ImageDraw.Draw(img)

    # Subtle radial-ish glow on right (green accent)
    from PIL import ImageFilter
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse((W - 600, H // 2 - 350, W + 200, H // 2 + 350), fill=(0, 212, 0, 35))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=80))
    img.alpha_composite(glow)

    # Brand strap (top-left)
    strap_font_bold = load_font("arialbd.ttf", 20)
    strap_font = load_font("arial.ttf", 14)
    draw.text((60, 50), "schoolsWP", font=strap_font_bold, fill=GREEN)
    draw.text((60, 78), "WordPress. Clair. Structure. Utile.", font=strap_font, fill=GREY)

    # Green accent bar under strap
    draw.rectangle((60, 102, 280, 104), fill=GREEN)

    # Main title (left half) - 2 lines
    title_font = load_font("arialbd.ttf", 56)
    draw.text((60, 160), "Sequence welcome", font=title_font, fill=WHITE)
    draw.text((60, 224), "FluentCRM", font=title_font, fill=GREEN)

    # Subtitle
    sub_font = load_font("arial.ttf", 22)
    draw.text(
        (60, 308),
        "Template gratuit pour freelances WordPress",
        font=sub_font,
        fill=WHITE,
    )

    # Bullet points
    bullet_font_bold = load_font("arialbd.ttf", 18)
    bullet_font = load_font("arial.ttf", 18)
    bullets = [
        ("4 emails", "complets pretes a copier"),
        ("7 jours", "planning, tags et conditions"),
        ("45 min", "installation chez ton client"),
    ]
    by = 372
    for label, desc in bullets:
        # Green dot
        draw.ellipse((60, by + 10, 72, by + 22), fill=GREEN)
        # Label (bold white) + desc (grey)
        draw.text((86, by + 5), label, font=bullet_font_bold, fill=WHITE)
        # Compute width of label to position desc inline
        lw, _ = text_size(draw, label, bullet_font_bold)
        draw.text((86 + lw + 12, by + 5), desc, font=bullet_font, fill=(180, 188, 200))
        by += 38

    # URL footer (bottom-left)
    url_font = load_font("arialbd.ttf", 16)
    draw.text((60, H - 56), "schoolswp.com", font=url_font, fill=GREEN)
    sep_font = load_font("arial.ttf", 14)
    draw.text(
        (60 + 130, H - 54),
        "/ template-welcome-fluentcrm",
        font=sep_font,
        fill=GREY,
    )

    # PDF mockup (right half)
    pdf_w, pdf_h = 380, 480
    pdf_x = W - pdf_w - 80
    pdf_y = (H - pdf_h) // 2
    draw_pdf_mockup(img, pdf_x, pdf_y, pdf_w, pdf_h)

    # Save as PNG (RGB, no alpha for OG safety)
    final = Image.new("RGB", (W, H), DARK)
    final.paste(img.convert("RGB"), (0, 0))
    final.save(OUT, format="PNG", optimize=True)

    print(f"OG image generated: {OUT}")
    print(f"Size: {OUT.stat().st_size} bytes ({OUT.stat().st_size / 1024:.1f} KB)")
    print(f"Dimensions: {W}x{H}")


if __name__ == "__main__":
    build()
