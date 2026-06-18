#!/usr/bin/env python
"""Construit le CSV fusionne (DataForSEO + Ubersuggest) et le xlsx multi-onglets
pour l'audit suredash-vs-fluent-community (snapshot 2026-06-09).

Reproductible : relance ce script pour regenerer volumes-fr.csv,
seo-volumes-google-sheet.csv, suggestions-semantiques-fr.csv et le .xlsx
a uploader sur le Drive.

Marche : France (locId 2250), langue fr.
Sources : DataForSEO (Google Ads volume + Labs keyword_overview + search_intent)
          + Ubersuggest (volume + SD).
"""

import csv
import pathlib

HERE = pathlib.Path(__file__).parent

# --- Cluster cible : fusion DataForSEO (DFS) + Ubersuggest (Uber) ---
# Colonnes : kw, vol_dfs, vol_uber, comp_dfs, cpc_eur_dfs, cpc_usd_uber,
#            kd_dfs, sd_uber, intent_dfs, tendance_an, tendance_trim
CLUSTER = [
    # mot-cle                              volDFS volUber compDFS  cpcDFS cpcUber  KD   SD   intent                        an    trim
    ["suredash vs fluent community", 0, None, None, None, None, None, None, "commercial (0.76)", None, None],
    ["fluent community", 110, 110, "LOW", 14.76, 5.29, 28, 23, "navigational/informational", -56, -64],
    ["suredash", 20, 20, "LOW", 46.21, None, None, 34, "navigational", -50, None],
    ["fluent community vs buddyboss", 10, None, None, None, None, None, None, "navigational", None, None],
    ["buddyboss", 320, 320, "MEDIUM", 1.05, 1.05, 18, 35, "informational", -83, None],
    ["buddyboss alternative", 10, None, None, None, None, None, None, "informational", -100, None],
    ["communaute wordpress", 70, 140, "LOW", None, None, 46, 35, "navigational", -97, None],
    ["espace membre wordpress", 50, 90, "LOW", 1.52, 4.05, None, 18, "navigational", -57, -25],
    ["plugin membre wordpress", 10, None, None, None, None, None, None, "navigational", -100, None],
    ["creer une communaute wordpress", 0, 0, None, None, None, None, 4, "transactional", None, None],
    ["plugin communaute wordpress", 0, None, None, None, None, None, None, "navigational", None, None],
    ["suredash avis", 0, None, None, None, None, None, None, "(sous seuil)", None, None],
    ["fluent community avis", 0, None, None, None, None, None, None, "(sous seuil)", None, None],
]

HEADERS = [
    "Mot-cle",
    "Volume FR (DataForSEO)",
    "Volume FR (Ubersuggest)",
    "Concurrence Ads (DFS)",
    "CPC EUR (DFS)",
    "CPC USD (Uber)",
    "KD (DFS)",
    "SD (Uber)",
    "Intention (DFS)",
    "Tendance an %",
    "Tendance trim %",
]

# --- Champ semantique 'fluent community' : top suggestions DataForSEO (FR) ---
# Constat : tout le champ est brand-navigational, micro-volumes, langue EN detectee.
SUGGESTIONS = [
    ["fluent community", 110, "navigational", "marque (cible)"],
    ["fluent community roadmap", 10, "navigational", "marque"],
    ["fluent community wordpress plugin", 10, "navigational", "marque"],
    ["fluent community pricing", 10, "commercial", "decision (prix)"],
    ["fluent community changelog", 10, "informational", "marque"],
    ["fluent community app", 10, "navigational", "marque"],
    ["fluent community demo", 10, "navigational", "marque"],
    ["fluent community review", 10, "informational", "decision (avis)"],
    ["fluent community pro", 10, "navigational", "marque"],
    ["fluent community plugin", 10, "navigational", "marque"],
    ["fluent community free vs pro", 10, "commercial", "decision (free/pro)"],
    ["fluent community chat", 10, "navigational", "marque"],
    ["fluent community wordpress", 10, "navigational", "marque"],
    ["fluent community vs buddyboss", 10, "navigational", "decision (comparatif)"],
]
SUG_HEADERS = ["Suggestion", "Volume FR (DFS)", "Intention", "Type d'intention reelle"]


def write_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in rows:
            w.writerow(["" if c is None else c for c in r])


def main():
    write_csv(HERE / "volumes-fr.csv", HEADERS, CLUSTER)
    write_csv(HERE / "seo-volumes-google-sheet.csv", HEADERS, CLUSTER)
    write_csv(HERE / "suggestions-semantiques-fr.csv", SUG_HEADERS, SUGGESTIONS)

    try:
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Font, PatternFill
    except ImportError:
        print("openpyxl absent : CSV ecrits, xlsx saute.")
        return

    wb = Workbook()
    green = PatternFill("solid", fgColor="00D400")
    bold_white = Font(bold=True, color="FFFFFF")

    ws = wb.active
    ws.title = "Cluster cible"
    ws.append(HEADERS)
    for r in CLUSTER:
        ws.append(["" if c is None else c for c in r])
    for cell in ws[1]:
        cell.fill = green
        cell.font = bold_white
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    widths = [34, 16, 16, 14, 12, 12, 9, 9, 26, 12, 12]
    for i, wdt in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + i)].width = wdt
    ws.freeze_panes = "A2"

    ws2 = wb.create_sheet("Champ semantique (suggestions)")
    ws2.append(SUG_HEADERS)
    for r in SUGGESTIONS:
        ws2.append(r)
    for cell in ws2[1]:
        cell.fill = green
        cell.font = bold_white
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for i, wdt in enumerate([34, 16, 16, 26], 1):
        ws2.column_dimensions[chr(64 + i)].width = wdt
    ws2.freeze_panes = "A2"

    out = HERE / "suredash-fluent-community-volumes-seo.xlsx"
    wb.save(out)
    print("xlsx ecrit:", out)


if __name__ == "__main__":
    main()
