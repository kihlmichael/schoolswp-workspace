"""Construit le classeur 3 marchés (FR / DE / EN) pour l'audit Booknetic.

Genere :
- volumes-fr.csv, volumes-de.csv, volumes-en.csv (sources colocalisees)
- booknetic-volumes-3-marches.xlsx (3 onglets, source du Google Sheet Drive)

Donnees : DataForSEO + Ubersuggest (France 2250 / Germany 2276 / US 2840), collectees 2026-06-03.
"""

import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

HERE = Path(__file__).parent
MONTHS = [
    "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10",
    "2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04",
]
BASE_COLS = [
    "keyword", "volume_dfs", "volume_uber", "kd_dfs", "sd_uber",
    "competition", "cpc", "cpc_currency", "intent", "trend_quarterly", "trend_yearly",
]
HEADER = BASE_COLS + MONTHS


def row(keyword, vdfs="", vuber="", kd="", sd="", comp="", cpc="", cur="",
        intent="", tq="", ty="", monthly=None):
    monthly = monthly or {}
    return [keyword, vdfs, vuber, kd, sd, comp, cpc, cur, intent, tq, ty] + \
        [monthly.get(m, "") for m in MONTHS]


FR = [
    row("avis booknetic", 0, 0, "", 17, "", "", "EUR", "informational"),
    row("booknetic", 90, 90, "", 13, "LOW", 1.38, "EUR", "navigational/informational", -44, -55,
        {"2025-05": 110, "2025-06": 70, "2025-07": 90, "2025-08": 90, "2025-09": 110, "2025-10": 110,
         "2025-11": 90, "2025-12": 70, "2026-01": 70, "2026-02": 90, "2026-03": 50, "2026-04": 50}),
    row("booknetic alternative", 10, "", "", "", "", "", "EUR", "informational"),
    row("plugin rendez-vous wordpress", 10, "", 49, "", "HIGH", 0.08, "EUR", "navigational"),
    row("plugin prise de rendez-vous wordpress", 10, "", "", "", "LOW", 0.26, "EUR", "navigational"),
    row("bookingpress", 110, "", 19, "", "LOW", 0.71, "EUR", "navigational", 56, -18,
        {"2025-05": 140, "2025-06": 140, "2025-07": 140, "2025-08": 110, "2025-09": 110, "2025-10": 140,
         "2025-11": 140, "2025-12": 70, "2026-01": 90, "2026-02": 90, "2026-03": 140, "2026-04": 140}),
]

DE = [
    row("booknetic", 110, 110, 10, 36, "LOW", 4.71, "EUR", "navigational", "", -18,
        {"2025-05": 110, "2025-06": 70, "2025-07": 110, "2025-08": 110, "2025-09": 140, "2025-10": 140,
         "2025-11": 110, "2025-12": 110, "2026-01": 110, "2026-02": 90, "2026-03": 90, "2026-04": 90}),
    row("booknetic erfahrungen", 0, 0, "", 17, "", "", "EUR", "review (0 volume)"),
    row("booknetic test", 0, "", "", "", "", "", "EUR", "review (0 volume)"),
    row("booknetic bewertung", 0, "", "", "", "", "", "EUR", "review (0 volume)"),
    row("booknetic erfahrung", 0, "", "", "", "", "", "EUR", "review (0 volume)"),
    row("booknetic alternative", 10, "", "", "", "", "", "EUR", "informational"),
    row("booknetic kosten", 0, "", "", "", "", "", "EUR", "informational"),
]

TEN = {m: 10 for m in MONTHS}
EN = [
    row("booknetic", 170, 170, 13, 36, "LOW", 4.59, "USD", "navigational", -21, -58,
        {"2025-05": 210, "2025-06": 210, "2025-07": 210, "2025-08": 170, "2025-09": 210, "2025-10": 170,
         "2025-11": 140, "2025-12": 170, "2026-01": 170, "2026-02": 140, "2026-03": 140, "2026-04": 110}),
    row("booknetic review", 10, 10, 58, 44, "HIGH", "", "USD", "informational", "", -50, TEN),
    row("booknetic reviews", 10, "", 58, "", "HIGH", "", "USD", "informational", "", "", TEN),
    row("booknetic wordpress", 10, "", "", "", "MEDIUM", "", "USD", "navigational"),
    row("booknetic wordpress plugin", 10, "", "", "", "MEDIUM", 11.77, "USD", "navigational", "", "", TEN),
    row("amelia vs booknetic", 10, "", "", "", "LOW", "", "USD", "informational"),
]

MARKETS = {"FR (France)": FR, "DE (Germany)": DE, "EN (US)": EN}
CSV_NAMES = {"FR (France)": "volumes-fr.csv", "DE (Germany)": "volumes-de.csv", "EN (US)": "volumes-en.csv"}

# --- CSV per market ---
for sheet_name, rows in MARKETS.items():
    with open(HERE / CSV_NAMES[sheet_name], "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)

# --- XLSX 3 onglets ---
wb = Workbook()
wb.remove(wb.active)
bold = Font(bold=True)
for sheet_name, rows in MARKETS.items():
    ws = wb.create_sheet(title=sheet_name)
    ws.append(HEADER)
    for c in range(1, len(HEADER) + 1):
        ws.cell(row=1, column=c).font = bold
    for r in rows:
        ws.append(r)
    ws.freeze_panes = "B2"
    ws.column_dimensions["A"].width = 34
    for i in range(2, len(BASE_COLS) + 1):
        ws.column_dimensions[get_column_letter(i)].width = 13

out = HERE / "booknetic-volumes-3-marches.xlsx"
wb.save(out)
print("OK ->", out)
print("CSV ->", ", ".join(CSV_NAMES.values()))
