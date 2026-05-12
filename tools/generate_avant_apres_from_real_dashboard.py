"""Transform the real FluentCRM dashboard screenshot into AVANT and APRES versions.

Strategy : open the cropped real screenshot (2233x1331), mask the 6 KPI numbers + the
chart area with white rectangles, redraw the new numbers and a custom line/bars chart.
Add a colored top banner (red for AVANT, green for APRES).

Output :
- assets/og-images/avant-fluentcrm-real.png
- assets/og-images/apres-fluentcrm-real.png
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "screenshots" / "fluentcrm-dashboard-real.png"
OUT_DIR = ROOT / "assets" / "og-images"

# Brand
DARK = (15, 20, 25)
GREEN = (0, 212, 0)
GREEN_SOFT = (0, 168, 0)
GREEN_LIGHT = (220, 255, 220)
WHITE = (255, 255, 255)
GREY = (100, 110, 120)
GREY_LIGHT = (210, 215, 220)
RED_SOFT = (190, 70, 70)
RED_VERY_SOFT = (252, 232, 232)
GREEN_VERY_SOFT = (232, 252, 232)

# FluentCRM chart colors (extracted from screenshot)
CHART_LINE = (87, 145, 226)         # bleu cumul line
CHART_FILL = (228, 240, 252)        # very light blue area fill
CHART_BAR = (162, 148, 240)         # purple bars
GRID = (220, 220, 220)
AXIS_LABEL = (100, 110, 120)

FONT_DIR = "C:/Windows/Fonts"


def f(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def text_size(d, txt, font):
    bbox = d.textbbox((0, 0), txt, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


# Crop region of the original screenshot
CROP_BOX = (247, 49, 2480, 1380)
CROP_W = CROP_BOX[2] - CROP_BOX[0]  # 2233
CROP_H = CROP_BOX[3] - CROP_BOX[1]  # 1331

# KPI tile number positions (within the cropped image)
# Based on visual inspection of fluentcrm-dashboard-cropped.png
# (x_start, y_start) for each tile's number top-left, and (x_end, y_end) for clearing rect
KPI_TILES = [
    # clear rect must FULLY cover the original number; new number font 72 fits in 80px height
    {"clear": (75, 140, 460, 230), "x": 95, "y": 145, "label": "Active Contacts"},   # tile 1
    {"clear": (635, 140, 1020, 230), "x": 655, "y": 145, "label": "Campagne"},       # tile 2
    {"clear": (1180, 140, 1560, 230), "x": 1200, "y": 145, "label": "E-mails envoyes"}, # tile 3
    {"clear": (75, 360, 460, 450), "x": 95, "y": 365, "label": "Etiquettes"},        # tile 4
    {"clear": (635, 360, 1020, 450), "x": 655, "y": 365, "label": "Modeles d'e-mail"}, # tile 5
    {"clear": (1180, 360, 1560, 450), "x": 1200, "y": 365, "label": "Automatisations actives"}, # tile 6
]

# Chart area within cropped image
CHART_BOX = (35, 695, 1660, 1265)   # full chart drawing zone (incl axis labels)
PLOT_BOX = (110, 720, 1640, 1180)   # internal plot area (between Y axis labels and X axis)


def draw_kpi_value(img, value, x, y, color, font_big):
    """Draw the new KPI number at the given baseline position."""
    d = ImageDraw.Draw(img)
    d.text((x, y), value, font=font_big, fill=color)


def mask_rect(img, box, fill=WHITE):
    d = ImageDraw.Draw(img)
    d.rectangle(box, fill=fill)


def draw_chart(img, kind: str):
    """Redraw the chart inside CHART_BOX. kind = 'avant' or 'apres'."""
    d = ImageDraw.Draw(img)
    # 1. Mask the entire chart area with white
    d.rectangle(CHART_BOX, fill=WHITE)

    # 2. Redraw legend (top center)
    legend_y = CHART_BOX[1] + 12
    legend_x_start = (PLOT_BOX[0] + PLOT_BOX[2]) // 2 - 200
    legend_font = f("arial.ttf", 22)

    # Legend par date (bar)
    d.rectangle(
        (legend_x_start, legend_y, legend_x_start + 56, legend_y + 24),
        outline=CHART_BAR, fill=None, width=3,
    )
    d.text((legend_x_start + 70, legend_y - 2), "Par date", font=legend_font, fill=DARK)

    # Legend cumule (line+circle)
    leg2_x = legend_x_start + 220
    d.rectangle(
        (leg2_x, legend_y, leg2_x + 56, legend_y + 24),
        outline=CHART_LINE, fill=None, width=3,
    )
    d.text((leg2_x + 70, legend_y - 2), "Cumule", font=legend_font, fill=DARK)

    # 3. Y axis labels and grid
    plot_x0, plot_y0, plot_x1, plot_y1 = PLOT_BOX
    plot_w = plot_x1 - plot_x0
    plot_h = plot_y1 - plot_y0

    if kind == "avant":
        y_max = 5  # show 0 to 5 (flat line, modest scale)
        line_pts_norm = [0.0] * 13   # 13 points = 30 jours / 2.5j
        bar_indices = []
        bar_value = 0
        right_axis_max = 5
    else:
        y_max = 400
        line_pts_norm = [0.02, 0.05, 0.08, 0.13, 0.20, 0.30, 0.42, 0.55, 0.66, 0.76, 0.85, 0.92, 0.96]
        # Bars on every other point (representing daily new subscribers)
        bar_indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        bar_values = [4, 6, 8, 12, 16, 22, 28, 30, 26, 22, 18, 12]
        right_axis_max = 30

    axis_label_font = f("arial.ttf", 18)

    # Left Y axis labels (cumulative)
    n_labels_y = 5
    for i in range(n_labels_y + 1):
        y_val = y_max * i // n_labels_y
        py = plot_y1 - i * plot_h // n_labels_y
        # Grid line
        d.line((plot_x0, py, plot_x1, py), fill=GRID, width=1)
        # Label left
        label = str(y_val)
        tw, th = text_size(d, label, axis_label_font)
        d.text((plot_x0 - tw - 12, py - th // 2), label, font=axis_label_font, fill=AXIS_LABEL)
        # Label right (bars scale)
        right_val = right_axis_max * i // n_labels_y
        d.text((plot_x1 + 12, py - th // 2), str(right_val), font=axis_label_font, fill=AXIS_LABEL)

    # Bars (drawn first, behind line)
    n = len(line_pts_norm)
    bar_w = 22
    if kind == "apres":
        for idx, val in zip(bar_indices, bar_values):
            bx = plot_x0 + idx * plot_w // (n - 1)
            bar_norm = val / right_axis_max
            bar_h = int(bar_norm * plot_h)
            d.rectangle(
                (bx - bar_w // 2, plot_y1 - bar_h, bx + bar_w // 2, plot_y1),
                fill=CHART_BAR,
            )

    # Line + filled area
    coords = []
    for i, v in enumerate(line_pts_norm):
        px = plot_x0 + i * plot_w // (n - 1)
        py = plot_y1 - int(v * plot_h)
        coords.append((px, py))

    # Filled area below (light blue)
    poly = coords + [(plot_x1, plot_y1), (plot_x0, plot_y1)]
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.polygon(poly, fill=CHART_FILL + (200,))
    img.alpha_composite(overlay)

    # Line itself
    d = ImageDraw.Draw(img)
    for i in range(len(coords) - 1):
        d.line((coords[i], coords[i + 1]), fill=CHART_LINE, width=4)
    # Dots on line
    for cx, cy in coords:
        d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), outline=CHART_LINE, fill=WHITE, width=2)

    # X axis dates (every 3 days from 2026-04-10 to 2026-05-10)
    dates = [
        "2026-04-10", "2026-04-13", "2026-04-16", "2026-04-19", "2026-04-22",
        "2026-04-25", "2026-04-28", "2026-05-01", "2026-05-04", "2026-05-07",
        "2026-05-10",
    ]
    n_dates = len(dates)
    for i, dlabel in enumerate(dates):
        px = plot_x0 + i * plot_w // (n_dates - 1)
        # Mini tick
        d.line((px, plot_y1, px, plot_y1 + 6), fill=AXIS_LABEL, width=1)
        # Rotated label : skip rotation, just render below
        tw, th = text_size(d, dlabel, axis_label_font)
        # Render at angle ~45° using transposed image
        label_img = Image.new("RGBA", (tw + 20, th + 20), (0, 0, 0, 0))
        ld = ImageDraw.Draw(label_img)
        ld.text((10, 10), dlabel, font=axis_label_font, fill=AXIS_LABEL)
        rotated = label_img.rotate(35, expand=True, resample=Image.Resampling.BICUBIC)
        rw, rh = rotated.size
        img.alpha_composite(rotated, (px - rw // 2 + 20, plot_y1 + 12))


def build_version(kind: str):
    """kind = 'avant' or 'apres'."""
    src = Image.open(SRC).convert("RGBA")
    crop = src.crop(CROP_BOX)

    # Banner above
    banner_h = 90
    new_h = banner_h + crop.height
    img = Image.new("RGBA", (crop.width, new_h), WHITE + (255,))
    img.paste(crop, (0, banner_h))

    d = ImageDraw.Draw(img)

    # Banner color + text
    if kind == "avant":
        bg = RED_VERY_SOFT
        fg = RED_SOFT
        title = "AVANT INSTALLATION"
        sub = "Compte FluentCRM dormant - liste qui ne recoit aucun email"
    else:
        bg = GREEN_VERY_SOFT
        fg = GREEN_SOFT
        title = "APRES INSTALLATION"
        sub = "Compte FluentCRM actif - sequence welcome installee, liste qui chauffe"

    d.rectangle((0, 0, crop.width, banner_h), fill=bg + (255,))
    title_font = f("arialbd.ttf", 28)
    sub_font = f("arial.ttf", 22)
    d.text((40, 20), title, font=title_font, fill=fg)
    d.text((40, 56), sub, font=sub_font, fill=GREY)

    # KPI replacements
    if kind == "avant":
        new_values = [
            ("340", DARK),     # Active Contacts (kept high - the real client situation)
            ("0", RED_SOFT),   # Campagne
            ("0", RED_SOFT),   # E-mails envoyes
            ("5", DARK),       # Etiquettes (a few placeholder tags)
            ("0", RED_SOFT),   # Modeles d'e-mail
            ("0", RED_SOFT),   # Automatisations actives
        ]
    else:
        new_values = [
            ("340", DARK),         # Active Contacts (same base)
            ("5", GREEN_SOFT),     # Campagne (sequence emails)
            ("1 360", GREEN_SOFT), # E-mails envoyes
            ("12", GREEN_SOFT),    # Etiquettes
            ("9", GREEN_SOFT),     # Modeles d'e-mail
            ("2", GREEN_SOFT),     # Automatisations actives (Funnel 1 + 2)
        ]

    # Working coords need offset by banner_h since we pasted crop at y=banner_h
    big_font = f("arialbd.ttf", 72)
    for tile, (val, color) in zip(KPI_TILES, new_values):
        # clear rect (apply banner offset)
        cx0, cy0, cx1, cy1 = tile["clear"]
        d.rectangle((cx0, cy0 + banner_h, cx1, cy1 + banner_h), fill=WHITE)
        # draw value
        d.text((tile["x"], tile["y"] + banner_h), val, font=big_font, fill=color)

    # Chart
    chart_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    # Translate CHART_BOX and PLOT_BOX coords by banner_h on Y
    cb = (CHART_BOX[0], CHART_BOX[1] + banner_h, CHART_BOX[2], CHART_BOX[3] + banner_h)
    pb = (PLOT_BOX[0], PLOT_BOX[1] + banner_h, PLOT_BOX[2], PLOT_BOX[3] + banner_h)

    # Patch the global CHART_BOX / PLOT_BOX temporarily inside draw_chart
    # Simpler: redraw chart manually here using cb/pb
    draw_chart_inline(img, kind, cb, pb)

    # Save (RGB final)
    final = Image.new("RGB", img.size, WHITE)
    final.paste(img.convert("RGB"), (0, 0))
    out = OUT_DIR / f"{kind}-fluentcrm-real.png"
    final.save(out, format="PNG", optimize=True)
    print(f"{kind.upper()} saved: {out} ({out.stat().st_size // 1024} KB) - {img.size}")


def draw_chart_inline(img, kind, chart_box, plot_box):
    d = ImageDraw.Draw(img)
    d.rectangle(chart_box, fill=WHITE)

    # Legend
    legend_y = chart_box[1] + 12
    legend_x_start = (plot_box[0] + plot_box[2]) // 2 - 200
    legend_font = f("arial.ttf", 22)
    d.rectangle((legend_x_start, legend_y, legend_x_start + 56, legend_y + 24),
                outline=CHART_BAR, fill=None, width=3)
    d.text((legend_x_start + 70, legend_y - 2), "Par date", font=legend_font, fill=DARK)
    leg2_x = legend_x_start + 220
    d.rectangle((leg2_x, legend_y, leg2_x + 56, legend_y + 24),
                outline=CHART_LINE, fill=None, width=3)
    d.text((leg2_x + 70, legend_y - 2), "Cumule", font=legend_font, fill=DARK)

    plot_x0, plot_y0, plot_x1, plot_y1 = plot_box
    plot_w = plot_x1 - plot_x0
    plot_h = plot_y1 - plot_y0

    if kind == "avant":
        y_max = 5
        line_pts_norm = [0.0] * 13
        bar_indices = []
        bar_values = []
        right_axis_max = 5
    else:
        y_max = 400
        line_pts_norm = [0.02, 0.05, 0.08, 0.13, 0.20, 0.30, 0.42, 0.55, 0.66, 0.76, 0.85, 0.92, 0.96]
        bar_indices = list(range(1, 13))
        bar_values = [4, 6, 8, 12, 16, 22, 28, 30, 26, 22, 18, 12]
        right_axis_max = 30

    axis_label_font = f("arial.ttf", 18)
    n_labels_y = 5

    # Y axis + grid
    for i in range(n_labels_y + 1):
        y_val = y_max * i // n_labels_y
        py = plot_y1 - i * plot_h // n_labels_y
        d.line((plot_x0, py, plot_x1, py), fill=GRID, width=1)
        label = str(y_val)
        tw, th = text_size(d, label, axis_label_font)
        d.text((plot_x0 - tw - 12, py - th // 2), label, font=axis_label_font, fill=AXIS_LABEL)
        right_val = right_axis_max * i // n_labels_y
        d.text((plot_x1 + 12, py - th // 2), str(right_val), font=axis_label_font, fill=AXIS_LABEL)

    # Bars
    n = len(line_pts_norm)
    bar_w = 22
    if kind == "apres":
        for idx, val in zip(bar_indices, bar_values):
            bx = plot_x0 + idx * plot_w // (n - 1)
            bar_norm = val / right_axis_max
            bar_h = int(bar_norm * plot_h)
            d.rectangle(
                (bx - bar_w // 2, plot_y1 - bar_h, bx + bar_w // 2, plot_y1),
                fill=CHART_BAR,
            )

    # Line + area
    coords = []
    for i, v in enumerate(line_pts_norm):
        px = plot_x0 + i * plot_w // (n - 1)
        py = plot_y1 - int(v * plot_h)
        coords.append((px, py))

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.polygon(coords + [(plot_x1, plot_y1), (plot_x0, plot_y1)], fill=CHART_FILL + (200,))
    img.alpha_composite(overlay)

    d = ImageDraw.Draw(img)
    for i in range(len(coords) - 1):
        d.line((coords[i], coords[i + 1]), fill=CHART_LINE, width=4)
    for cx, cy in coords:
        d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), outline=CHART_LINE, fill=WHITE, width=2)

    # X axis dates
    dates = [
        "2026-04-10", "2026-04-13", "2026-04-16", "2026-04-19", "2026-04-22",
        "2026-04-25", "2026-04-28", "2026-05-01", "2026-05-04", "2026-05-07",
        "2026-05-10",
    ]
    n_dates = len(dates)
    for i, dlabel in enumerate(dates):
        px = plot_x0 + i * plot_w // (n_dates - 1)
        d.line((px, plot_y1, px, plot_y1 + 6), fill=AXIS_LABEL, width=1)
        tw, th = text_size(d, dlabel, axis_label_font)
        label_img = Image.new("RGBA", (tw + 20, th + 20), (0, 0, 0, 0))
        ld = ImageDraw.Draw(label_img)
        ld.text((10, 10), dlabel, font=axis_label_font, fill=AXIS_LABEL)
        rotated = label_img.rotate(35, expand=True, resample=Image.Resampling.BICUBIC)
        rw, rh = rotated.size
        img.alpha_composite(rotated, (px - rw // 2 + 20, plot_y1 + 12))


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_version("avant")
    build_version("apres")
