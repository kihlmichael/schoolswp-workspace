"""Generate vertical HERO image 800x1200 (ratio 2:3) for landing page hero column.

Distinct from OG image (1200x630) which is kept for social sharing.
This one fills the right column of the Kadence hero visually.

Composition : "PDF cover" mockup, dark bg with subtle green glow, drop shadow,
title + bullets + footer URL.

Output : assets/og-images/hero-template-welcome-fluentcrm.png
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og-images" / "hero-template-welcome-fluentcrm.png"

# Format 2:3 portrait
W, H = 800, 1200

# Brand
DARK = (15, 20, 25)
GREEN = (0, 212, 0)
WHITE = (255, 255, 255)
LIGHT = (244, 245, 247)
GREY = (91, 99, 112)
GREEN_SOFT = (0, 168, 0)
PDF_LINE = (224, 230, 235)

FONT_DIR = "C:/Windows/Fonts"


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def text_size(draw: ImageDraw.ImageDraw, txt: str, font: ImageFont.FreeTypeFont):
    bbox = draw.textbbox((0, 0), txt, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    # Canvas with dark bg
    img = Image.new("RGBA", (W, H), DARK + (255,))

    # Subtle green glow top-right
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse((W - 500, -200, W + 200, 400), fill=(0, 212, 0, 50))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=90))
    img.alpha_composite(glow)

    # Bottom-left subtle glow
    glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow2_draw = ImageDraw.Draw(glow2)
    glow2_draw.ellipse((-200, H - 400, 400, H + 200), fill=(0, 212, 0, 30))
    glow2 = glow2.filter(ImageFilter.GaussianBlur(radius=100))
    img.alpha_composite(glow2)

    # === PDF cover card (white, large drop shadow) ===
    pdf_w = 580
    pdf_h = 880
    pdf_x = (W - pdf_w) // 2
    pdf_y = (H - pdf_h) // 2

    # Drop shadow
    shadow_offset = 24
    sh = Image.new("RGBA", (pdf_w + shadow_offset * 4, pdf_h + shadow_offset * 4), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(sh)
    sh_draw.rounded_rectangle(
        (shadow_offset * 2, shadow_offset * 2,
         shadow_offset * 2 + pdf_w, shadow_offset * 2 + pdf_h),
        radius=14,
        fill=(0, 0, 0, 110),
    )
    sh = sh.filter(ImageFilter.GaussianBlur(radius=20))
    img.alpha_composite(sh, (pdf_x - shadow_offset * 2, pdf_y - shadow_offset * 2 + 16))

    draw = ImageDraw.Draw(img)
    # Card body
    draw.rounded_rectangle(
        (pdf_x, pdf_y, pdf_x + pdf_w, pdf_y + pdf_h),
        radius=14,
        fill=WHITE,
    )

    # Green left strip
    strip_w = 12
    draw.rounded_rectangle(
        (pdf_x, pdf_y, pdf_x + strip_w, pdf_y + pdf_h),
        radius=6,
        fill=GREEN,
    )

    pad = 50
    inner_x = pdf_x + pad
    cur_y = pdf_y + 50

    # Pill schoolsWP
    pill_w, pill_h = 140, 32
    draw.rounded_rectangle(
        (inner_x, cur_y, inner_x + pill_w, cur_y + pill_h),
        radius=16,
        fill=GREEN,
    )
    pill_font = load_font("arialbd.ttf", 16)
    pill_text = "schoolsWP"
    ptw, pth = text_size(draw, pill_text, pill_font)
    draw.text(
        (inner_x + (pill_w - ptw) // 2, cur_y + (pill_h - pth) // 2 - 2),
        pill_text,
        font=pill_font,
        fill=WHITE,
    )
    cur_y += pill_h + 36

    # Tag "TEMPLATE GRATUIT"
    tag_font = load_font("arialbd.ttf", 13)
    draw.text(
        (inner_x, cur_y),
        "TEMPLATE GRATUIT · PDF",
        font=tag_font,
        fill=GREEN_SOFT,
    )
    cur_y += 30

    # Title (2 lines)
    title_font = load_font("arialbd.ttf", 44)
    draw.text((inner_x, cur_y), "Sequence", font=title_font, fill=DARK)
    cur_y += 56
    draw.text((inner_x, cur_y), "welcome", font=title_font, fill=DARK)
    cur_y += 56
    draw.text((inner_x, cur_y), "FluentCRM", font=title_font, fill=GREEN)
    cur_y += 70

    # Subtitle
    sub_font = load_font("arial.ttf", 17)
    draw.text(
        (inner_x, cur_y),
        "Pour freelances WordPress",
        font=sub_font,
        fill=GREY,
    )
    cur_y += 50

    # Divider
    draw.rectangle(
        (inner_x, cur_y, inner_x + 80, cur_y + 3),
        fill=GREEN,
    )
    cur_y += 32

    # 3 promesses with green check
    bullet_font_bold = load_font("arialbd.ttf", 19)
    bullet_font = load_font("arial.ttf", 14)
    bullets = [
        ("4 emails", "complets, pretes a copier"),
        ("7 jours", "planning + tags FluentCRM"),
        ("45 min", "installation chez ton client"),
    ]
    for label, desc in bullets:
        # Green dot
        draw.ellipse((inner_x, cur_y + 6, inner_x + 14, cur_y + 20), fill=GREEN)
        draw.text((inner_x + 26, cur_y + 2), label, font=bullet_font_bold, fill=DARK)
        draw.text((inner_x + 26, cur_y + 28), desc, font=bullet_font, fill=GREY)
        cur_y += 60

    cur_y += 20

    # Mock content lines (subtle, low position)
    line_h = 6
    line_gap = 12
    for i, lw in enumerate([pdf_w - pad * 2, pdf_w - pad * 2 - 40, pdf_w - pad * 2 - 80,
                             pdf_w - pad * 2 - 20, pdf_w - pad * 2 - 100]):
        draw.rounded_rectangle(
            (inner_x, cur_y, inner_x + lw, cur_y + line_h),
            radius=3,
            fill=PDF_LINE,
        )
        cur_y += line_h + line_gap

    # Bottom CTA pill
    cta_y = pdf_y + pdf_h - 80
    cta_w = pdf_w - pad * 2
    draw.rounded_rectangle(
        (inner_x, cta_y, inner_x + cta_w, cta_y + 44),
        radius=8,
        fill=(240, 255, 240),
        outline=GREEN,
        width=2,
    )
    cta_font = load_font("arialbd.ttf", 15)
    cta_text = "Telecharger gratuitement"
    tw, th = text_size(draw, cta_text, cta_font)
    draw.text(
        (inner_x + (cta_w - tw) // 2, cta_y + (44 - th) // 2 - 2),
        cta_text,
        font=cta_font,
        fill=GREEN_SOFT,
    )

    # === Outside the card : footer URL on dark bg, bottom-center ===
    foot_url_font = load_font("arialbd.ttf", 17)
    foot_label_font = load_font("arial.ttf", 14)
    url_text = "schoolswp.com"
    sub_text = "/ template-welcome-fluentcrm"
    uw, uh = text_size(draw, url_text, foot_url_font)
    sw_, sh_ = text_size(draw, sub_text, foot_label_font)
    total_w = uw + 12 + sw_
    foot_x = (W - total_w) // 2
    foot_y = H - 56
    draw.text((foot_x, foot_y), url_text, font=foot_url_font, fill=GREEN)
    draw.text((foot_x + uw + 12, foot_y + 3), sub_text, font=foot_label_font, fill=GREY)

    # Save (RGB, no alpha)
    final = Image.new("RGB", (W, H), DARK)
    final.paste(img.convert("RGB"), (0, 0))
    final.save(OUT, format="PNG", optimize=True)

    print(f"Hero vertical image generated: {OUT}")
    print(f"Size: {OUT.stat().st_size} bytes ({OUT.stat().st_size / 1024:.1f} KB)")
    print(f"Dimensions: {W}x{H} (ratio 2:3 portrait)")


if __name__ == "__main__":
    build()
