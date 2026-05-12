"""Generate AVANT / APRES dashboard mockup images for the landing page section.

Both 1200x900 (4:3, matching the original placeholder size). Style : flat dashboard
mockup with FluentCRM-like KPI tiles and a tiny chart.

AVANT  : ternes colors, zeros everywhere, "Last email : 3 mois", flat line.
APRES  : brand green accent, real KPIs (47% open, 12% click, 4 tags), rising line.

Output :
- assets/og-images/avant-fluentcrm-dormant.png
- assets/og-images/apres-fluentcrm-actif.png
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "og-images"

W, H = 1200, 900

# Brand
DARK = (15, 20, 25)
GREEN = (0, 212, 0)
GREEN_SOFT = (0, 168, 0)
GREEN_LIGHT = (220, 255, 220)
WHITE = (255, 255, 255)
LIGHT = (244, 245, 247)
GREY = (91, 99, 112)
GREY_LIGHT = (200, 207, 215)
GREY_DARKER = (140, 148, 160)
RED_SOFT = (210, 90, 90)
RED_VERY_SOFT = (250, 220, 220)

FONT_DIR = "C:/Windows/Fonts"


def f(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def text_size(draw, txt, font):
    bbox = draw.textbbox((0, 0), txt, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_card(img: Image.Image, x, y, w, h, fill=WHITE, shadow=True, border=None):
    if shadow:
        sh = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
        sh_draw = ImageDraw.Draw(sh)
        sh_draw.rounded_rectangle((20, 20, 20 + w, 20 + h), radius=12, fill=(0, 0, 0, 60))
        sh = sh.filter(ImageFilter.GaussianBlur(radius=14))
        img.alpha_composite(sh, (x - 20, y - 16))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x, y, x + w, y + h), radius=12, fill=fill,
                        outline=border, width=1 if border else 0)


def kpi_tile(img, x, y, w, h, label, value, value_color, label_font, value_font,
             bg=WHITE, accent=None):
    draw_card(img, x, y, w, h, fill=bg)
    d = ImageDraw.Draw(img)
    pad = 18
    d.text((x + pad, y + pad), label, font=label_font, fill=GREY)
    d.text((x + pad, y + pad + 28), value, font=value_font, fill=value_color)
    if accent:
        # small green/red tag in top-right
        tag_text, tag_color = accent
        tag_font = f("arialbd.ttf", 11)
        tw, th = text_size(d, tag_text, tag_font)
        tag_pad = 6
        tag_w = tw + tag_pad * 2
        tag_h = th + tag_pad * 2
        d.rounded_rectangle(
            (x + w - tag_w - 12, y + 12, x + w - 12, y + 12 + tag_h),
            radius=tag_h // 2,
            fill=tag_color,
        )
        d.text((x + w - tag_w - 12 + tag_pad, y + 12 + tag_pad - 1),
               tag_text, font=tag_font, fill=WHITE)


def draw_line_chart(img, x, y, w, h, points, color, fill_color, label):
    """points = list of normalized values 0..1"""
    d = ImageDraw.Draw(img)
    draw_card(img, x, y, w, h, fill=WHITE, shadow=False, border=GREY_LIGHT)
    title_font = f("arialbd.ttf", 13)
    sub_font = f("arial.ttf", 11)
    d.text((x + 18, y + 14), label, font=title_font, fill=DARK)

    plot_x0 = x + 24
    plot_x1 = x + w - 24
    plot_y0 = y + 50
    plot_y1 = y + h - 30
    plot_w = plot_x1 - plot_x0
    plot_h = plot_y1 - plot_y0

    # Grid lines
    for i in range(4):
        gy = plot_y0 + i * plot_h // 4
        d.line((plot_x0, gy, plot_x1, gy), fill=GREY_LIGHT, width=1)

    if not points:
        return

    n = len(points)
    coords = []
    for i, v in enumerate(points):
        px = plot_x0 + i * plot_w // (n - 1) if n > 1 else plot_x0
        py = plot_y1 - int(v * plot_h)
        coords.append((px, py))

    # Filled area below
    poly = coords + [(plot_x1, plot_y1), (plot_x0, plot_y1)]
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.polygon(poly, fill=fill_color)
    img.alpha_composite(overlay)

    # Line
    for i in range(len(coords) - 1):
        d.line((coords[i], coords[i + 1]), fill=color, width=3)
    # Dots
    for cx, cy in coords:
        d.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), fill=color)


def build_avant():
    img = Image.new("RGBA", (W, H), LIGHT + (255,))
    d = ImageDraw.Draw(img)

    # Top dim banner (subtle red-orange tint)
    banner_h = 60
    d.rectangle((0, 0, W, banner_h), fill=(245, 235, 235, 255))
    label_font = f("arialbd.ttf", 16)
    d.text((40, 20), "AVANT", font=label_font, fill=RED_SOFT)
    sub_font = f("arial.ttf", 14)
    d.text((130, 22), "Compte FluentCRM dormant chez ton client",
           font=sub_font, fill=GREY)

    # Sidebar mock (gray)
    sb_w = 60
    d.rectangle((0, banner_h, sb_w, H), fill=(228, 232, 238, 255))
    for i in range(7):
        d.ellipse((20, banner_h + 30 + i * 50, 40, banner_h + 50 + i * 50),
                  fill=GREY_LIGHT)

    # Title area
    title_font = f("arialbd.ttf", 28)
    d.text((sb_w + 40, banner_h + 30), "Vue d'ensemble · FluentCRM",
           font=title_font, fill=DARK)
    d.text((sb_w + 40, banner_h + 70),
           "Derniere activite : il y a 3 mois",
           font=f("arial.ttf", 14), fill=GREY_DARKER)

    # KPI tiles row (4 tiles)
    tile_w = 240
    tile_h = 120
    tile_y = banner_h + 130
    gap = 20
    label_f = f("arialbd.ttf", 12)
    value_f = f("arialbd.ttf", 36)

    tiles = [
        ("Inscrits", "340", DARK, None),
        ("Emails envoyes", "0", RED_SOFT, ("INACTIF", RED_SOFT)),
        ("Automations actives", "0", RED_SOFT, None),
        ("Tags appliques", "0", GREY_DARKER, None),
    ]
    start_x = sb_w + 40
    for i, (label, value, vc, accent) in enumerate(tiles):
        x = start_x + i * (tile_w + gap)
        kpi_tile(img, x, tile_y, tile_w, tile_h, label, value, vc, label_f, value_f,
                 accent=accent)

    # Big chart card (flat zero line)
    chart_x = sb_w + 40
    chart_y = tile_y + tile_h + 30
    chart_w = (tile_w + gap) * 4 - gap
    chart_h = 280
    flat_points = [0.05] * 12
    draw_line_chart(img, chart_x, chart_y, chart_w, chart_h, flat_points,
                    color=GREY_DARKER, fill_color=(140, 148, 160, 30),
                    label="Emails envoyes - 90 derniers jours")

    # Bottom message card
    msg_y = chart_y + chart_h + 30
    msg_h = 90
    draw_card(img, chart_x, msg_y, chart_w, msg_h,
              fill=RED_VERY_SOFT, shadow=False)
    d.text((chart_x + 24, msg_y + 18),
           "Aucun email parti depuis 90 jours.",
           font=f("arialbd.ttf", 18), fill=DARK)
    d.text((chart_x + 24, msg_y + 50),
           "La liste de 340 contacts dort. Aucun retour visible pour ton client.",
           font=f("arial.ttf", 14), fill=GREY)

    # Final
    final = Image.new("RGB", (W, H), LIGHT)
    final.paste(img.convert("RGB"), (0, 0))
    out = OUT_DIR / "avant-fluentcrm-dormant.png"
    final.save(out, format="PNG", optimize=True)
    print(f"AVANT saved: {out} ({out.stat().st_size // 1024} KB)")


def build_apres():
    img = Image.new("RGBA", (W, H), LIGHT + (255,))
    d = ImageDraw.Draw(img)

    # Top brand banner (subtle green)
    banner_h = 60
    d.rectangle((0, 0, W, banner_h), fill=(232, 250, 232, 255))
    label_font = f("arialbd.ttf", 16)
    d.text((40, 20), "APRES", font=label_font, fill=GREEN_SOFT)
    sub_font = f("arial.ttf", 14)
    d.text((130, 22),
           "Compte FluentCRM actif - sequence welcome installee",
           font=sub_font, fill=GREY)

    # Sidebar (slight green tint)
    sb_w = 60
    d.rectangle((0, banner_h, sb_w, H), fill=(228, 240, 230, 255))
    for i in range(7):
        color = GREEN if i == 1 else GREY_LIGHT
        d.ellipse((20, banner_h + 30 + i * 50, 40, banner_h + 50 + i * 50),
                  fill=color)

    # Title
    title_font = f("arialbd.ttf", 28)
    d.text((sb_w + 40, banner_h + 30),
           "Vue d'ensemble · FluentCRM",
           font=title_font, fill=DARK)
    d.text((sb_w + 40, banner_h + 70),
           "Derniere activite : il y a 12 minutes",
           font=f("arial.ttf", 14), fill=GREEN_SOFT)

    # KPI tiles row
    tile_w = 240
    tile_h = 120
    tile_y = banner_h + 130
    gap = 20
    label_f = f("arialbd.ttf", 12)
    value_f = f("arialbd.ttf", 36)

    tiles = [
        ("Inscrits", "340", DARK, None),
        ("Taux d'ouverture", "47%", GREEN_SOFT, ("ACTIF", GREEN)),
        ("Taux de clic", "12%", GREEN_SOFT, None),
        ("Tags appliques", "4", GREEN_SOFT, None),
    ]
    start_x = sb_w + 40
    for i, (label, value, vc, accent) in enumerate(tiles):
        x = start_x + i * (tile_w + gap)
        kpi_tile(img, x, tile_y, tile_w, tile_h, label, value, vc, label_f, value_f,
                 accent=accent)

    # Big chart card (rising line)
    chart_x = sb_w + 40
    chart_y = tile_y + tile_h + 30
    chart_w = (tile_w + gap) * 4 - gap
    chart_h = 280
    rising_points = [0.05, 0.08, 0.12, 0.20, 0.32, 0.45, 0.58, 0.66, 0.74, 0.82, 0.88, 0.92]
    draw_line_chart(img, chart_x, chart_y, chart_w, chart_h, rising_points,
                    color=GREEN_SOFT, fill_color=(0, 212, 0, 50),
                    label="Emails envoyes - 90 derniers jours (sequence welcome active)")

    # Bottom success card
    msg_y = chart_y + chart_h + 30
    msg_h = 90
    draw_card(img, chart_x, msg_y, chart_w, msg_h,
              fill=GREEN_LIGHT, shadow=False)
    d.text((chart_x + 24, msg_y + 18),
           "1 360 emails partis sur les 30 derniers jours.",
           font=f("arialbd.ttf", 18), fill=DARK)
    d.text((chart_x + 24, msg_y + 50),
           "Bascule newsletter active. Le client voit son systeme d'emailing tourner.",
           font=f("arial.ttf", 14), fill=GREEN_SOFT)

    final = Image.new("RGB", (W, H), LIGHT)
    final.paste(img.convert("RGB"), (0, 0))
    out = OUT_DIR / "apres-fluentcrm-actif.png"
    final.save(out, format="PNG", optimize=True)
    print(f"APRES saved: {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_avant()
    build_apres()
