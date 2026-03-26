"""
Thruuu SERP Export Consolidator
================================
Consolide 1001 fichiers Excel Thruuu en un classeur unique structuré.

Pack SEO essentiel :
- SERP Overview, Search Volume, Monthly Search Volume, AIO Overview
- FAQ, PAA, Frequent Questions, Related Search

Sortie : 1 onglet par type de donnée + README + QUALITY_REPORT + MAPPING
"""

import glob
import os
import re
import sys
from datetime import datetime

import pandas as pd
from openpyxl import load_workbook

# ── Configuration ──────────────────────────────────────────────────────
INPUT_DIR = r"D:\thruuu"
OUTPUT_FILE = r"D:\thruuu\__CONSOLIDATED_THRUUU.xlsx"
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Sheets to extract (exact names)
TARGET_SHEETS = {
    "SERP Overview",
    "Search Volume",
    "Monthly Search Volume",
    "AIO Overview",
    "FAQ",
    "AIO FAQ",
    "Frequent Questions",
    "Related Search",
}
# PAA sheets matched by pattern: "PAA  - Pos N" or "PAA - Pos N"
PAA_PATTERN = re.compile(r"^PAA\s+-\s*Pos\s+\d+$", re.IGNORECASE)


def extract_keyword(wb):
    """Extract the keyword/query from the Info sheet."""
    if "Info" not in wb.sheetnames:
        return "UNKNOWN"
    ws = wb["Info"]
    for row in ws.iter_rows(max_row=10, max_col=2, values_only=True):
        if row and row[0] == "Query":
            return str(row[1]).strip() if row[1] else "UNKNOWN"
    return "UNKNOWN"


def read_sheet_as_df(wb, sheet_name, keyword, source_file):
    """Read a single sheet into a DataFrame with traceability columns."""
    ws = wb[sheet_name]
    rows = list(ws.iter_rows(values_only=True))
    if not rows or len(rows) < 2:
        return None

    headers = list(rows[0])
    # Clean None headers
    headers = [h if h is not None else f"_col_{i}" for i, h in enumerate(headers)]
    data = rows[1:]

    # Filter out completely empty rows
    data = [r for r in data if any(v is not None for v in r)]
    if not data:
        return None

    # Ensure all rows have the same number of columns as headers
    data = [list(r) + [None] * (len(headers) - len(r)) if len(r) < len(headers)
            else list(r)[:len(headers)] for r in data]

    df = pd.DataFrame(data, columns=headers)
    df.insert(0, "keyword", keyword)
    df["source_file"] = source_file
    df["source_sheet"] = sheet_name
    df["import_timestamp"] = TIMESTAMP
    return df


def read_related_search(wb, keyword, source_file):
    """Read Related Search sheet (special format: 2 cols, no standard header)."""
    if "Related Search" not in wb.sheetnames:
        return None
    ws = wb["Related Search"]
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return None

    # Related Search has pairs: [Search Term, Google URL]
    data = []
    for row in rows:
        if row and len(row) >= 2 and row[0] is not None:
            data.append({
                "keyword": keyword,
                "related_search": str(row[0]).strip(),
                "google_url": str(row[1]).strip() if row[1] else None,
                "source_file": source_file,
                "source_sheet": "Related Search",
                "import_timestamp": TIMESTAMP,
            })
    if not data:
        return None
    return pd.DataFrame(data)


def read_paa_sheets(wb, keyword, source_file):
    """Read all PAA sheets (PAA - Pos N) and combine them."""
    frames = []
    for sheet_name in wb.sheetnames:
        if PAA_PATTERN.match(sheet_name):
            # Extract position from sheet name
            pos_match = re.search(r"(\d+)$", sheet_name)
            serp_position = int(pos_match.group(1)) if pos_match else None

            ws = wb[sheet_name]
            rows = list(ws.iter_rows(values_only=True))
            if not rows or len(rows) < 2:
                continue

            headers = list(rows[0])
            data = [r for r in rows[1:] if any(v is not None for v in r)]
            if not data:
                continue

            data = [list(r) + [None] * (len(headers) - len(r)) if len(r) < len(headers)
                    else list(r)[:len(headers)] for r in data]

            df = pd.DataFrame(data, columns=headers)
            df.insert(0, "keyword", keyword)
            df["serp_position"] = serp_position
            df["source_file"] = source_file
            df["source_sheet"] = sheet_name
            df["import_timestamp"] = TIMESTAMP
            frames.append(df)

    if not frames:
        return None
    return pd.concat(frames, ignore_index=True)


def process_file(filepath):
    """Process a single Thruuu Excel file and return dict of DataFrames."""
    source_file = os.path.basename(filepath)
    results = {}

    try:
        wb = load_workbook(filepath, read_only=True, data_only=True)
    except Exception as e:
        return {"_error": str(e), "_file": source_file}

    keyword = extract_keyword(wb)

    # Standard sheets
    for sheet_name in TARGET_SHEETS:
        if sheet_name == "Related Search":
            continue  # handled separately
        if sheet_name in wb.sheetnames:
            df = read_sheet_as_df(wb, sheet_name, keyword, source_file)
            if df is not None:
                key = sheet_name.replace(" ", "_").upper()
                if key not in results:
                    results[key] = []
                results[key].append(df)

    # Related Search (special format)
    df_rs = read_related_search(wb, keyword, source_file)
    if df_rs is not None:
        results.setdefault("RELATED_SEARCH", []).append(df_rs)

    # PAA sheets
    df_paa = read_paa_sheets(wb, keyword, source_file)
    if df_paa is not None:
        results.setdefault("PAA", []).append(df_paa)

    wb.close()
    return results, keyword, source_file


def main():
    files = sorted(glob.glob(os.path.join(INPUT_DIR, "*.xlsx")))
    # Exclude our own output file
    files = [f for f in files if not os.path.basename(f).startswith("__")]

    total_files = len(files)
    print(f"Fichiers à traiter : {total_files}")

    # Accumulators
    all_data = {}
    errors = []
    keywords_seen = {}
    file_stats = []

    for i, filepath in enumerate(files):
        fname = os.path.basename(filepath)
        if (i + 1) % 50 == 0 or i == 0:
            print(f"  [{i + 1}/{total_files}] {fname}...")

        result = process_file(filepath)

        if isinstance(result, dict) and "_error" in result:
            errors.append({"file": result["_file"], "error": result["_error"]})
            continue

        file_results, keyword, source_file = result
        rows_in_file = 0

        for key, frames in file_results.items():
            if key not in all_data:
                all_data[key] = []
            all_data[key].extend(frames)
            rows_in_file += sum(len(f) for f in frames)

        # Track keywords for dedup analysis
        keywords_seen.setdefault(keyword, []).append(source_file)
        file_stats.append({
            "source_file": source_file,
            "keyword": keyword,
            "rows_extracted": rows_in_file,
        })

    # ── Consolidate DataFrames ─────────────────────────────────────────
    print("\nConsolidation des données...")
    consolidated = {}
    stats = {}

    for key, frames in all_data.items():
        if frames:
            df = pd.concat(frames, ignore_index=True)
            consolidated[key] = df
            stats[key] = len(df)
            print(f"  {key}: {len(df):,} lignes")

    # ── Deduplication analysis ─────────────────────────────────────────
    print("\nAnalyse des doublons par keyword...")
    dup_keywords = {k: v for k, v in keywords_seen.items() if len(v) > 1}
    print(f"  Keywords uniques : {len(keywords_seen)}")
    print(f"  Keywords en doublon (présents dans 2+ fichiers) : {len(dup_keywords)}")

    # ── Data cleaning ──────────────────────────────────────────────────
    print("\nNettoyage des données...")
    for key, df in consolidated.items():
        # Strip whitespace from string columns
        for col in df.select_dtypes(include=["object"]).columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace({"None": None, "nan": None, "": None})

        # Standardize common sentinel values
        for col in df.columns:
            if "date" in col.lower():
                df[col] = df[col].replace({
                    "No Publication Date Found": None,
                    "No Modification Date Found": None,
                })

        consolidated[key] = df

    # ── Dedup in SERP_OVERVIEW: keep all but flag duplicates ───────────
    if "SERP_OVERVIEW" in consolidated:
        df = consolidated["SERP_OVERVIEW"]
        df["is_keyword_duplicate"] = df["keyword"].duplicated(keep="first")

    if "SEARCH_VOLUME" in consolidated:
        df = consolidated["SEARCH_VOLUME"]
        df["is_keyword_duplicate"] = df["keyword"].duplicated(keep="first")

    # ── Write output ───────────────────────────────────────────────────
    print(f"\nÉcriture du fichier final : {OUTPUT_FILE}")

    # Tab name mapping (max 31 chars for Excel)
    tab_names = {
        "SERP_OVERVIEW": "SERP_OVERVIEW",
        "SEARCH_VOLUME": "SEARCH_VOLUME",
        "MONTHLY_SEARCH_VOLUME": "MONTHLY_SEARCH_VOL",
        "AIO_OVERVIEW": "AIO_OVERVIEW",
        "FAQ": "FAQ",
        "AIO_FAQ": "AIO_FAQ",
        "FREQUENT_QUESTIONS": "FREQUENT_QUESTIONS",
        "PAA": "PAA",
        "RELATED_SEARCH": "RELATED_SEARCH",
    }

    with pd.ExcelWriter(OUTPUT_FILE, engine="xlsxwriter") as writer:
        workbook = writer.book

        # Header format
        header_fmt = workbook.add_format({
            "bold": True,
            "bg_color": "#1F4E79",
            "font_color": "#FFFFFF",
            "border": 1,
            "text_wrap": True,
            "valign": "vcenter",
        })

        # Write data tabs
        for key in ["SERP_OVERVIEW", "SEARCH_VOLUME", "MONTHLY_SEARCH_VOLUME",
                     "AIO_OVERVIEW", "FAQ", "AIO_FAQ", "FREQUENT_QUESTIONS",
                     "PAA", "RELATED_SEARCH"]:
            if key not in consolidated:
                continue
            df = consolidated[key]
            tab = tab_names.get(key, key[:31])
            df.to_excel(writer, sheet_name=tab, index=False, startrow=1, header=False)

            ws = writer.sheets[tab]
            # Write formatted headers
            for col_idx, col_name in enumerate(df.columns):
                ws.write(0, col_idx, col_name, header_fmt)
            # Freeze top row
            ws.freeze_panes(1, 0)
            # Auto-fit columns (approximate)
            for col_idx, col_name in enumerate(df.columns):
                max_len = max(
                    df.iloc[:100][col_name].astype(str).str.len().max() if len(df) > 0 else 10,
                    len(str(col_name))
                )
                ws.set_column(col_idx, col_idx, min(max_len + 2, 60))
            # Add autofilter
            ws.autofilter(0, 0, len(df), len(df.columns) - 1)

        # ── MAPPING tab ────────────────────────────────────────────────
        mapping_data = []
        source_cols = {
            "SERP_OVERVIEW": ["Position", "Organic Position", "Page", "SERP Type", "Type",
                              "SERP Title", "Title", "URL", "Meta Description", "Hostname",
                              "TLD", "Page Rank", "Word Count", "Image Count",
                              "Publication date", "Modification Date", "AMP Version",
                              "Has On Page FAQ", "Schema Type"],
            "SEARCH_VOLUME": ["Keyword", "Competition", "Competition Index",
                              "Search Volume", "CPC"],
            "MONTHLY_SEARCH_VOLUME": ["Keyword", "Year", "Month", "Monthly Search Volume"],
            "AIO_OVERVIEW": ["Position", "Position in Organic Listing", "Type", "Title",
                             "URL", "Description", "Hostname", "TLD", "Page Rank",
                             "Word Count", "Image Count", "Publication date",
                             "Modification Date", "AMP Version", "Has On Page FAQ",
                             "Schema Type"],
            "FAQ": ["Page position", "URL", "Question", "Answer"],
            "AIO_FAQ": ["Page position", "URL", "Question", "Answer"],
            "FREQUENT_QUESTIONS": ["Tag", "Question", "Count"],
            "PAA": ["Question", "Answer", "AI Overview"],
            "RELATED_SEARCH": ["related_search", "google_url"],
        }
        for tab_key, cols in source_cols.items():
            for col in cols:
                mapping_data.append({
                    "onglet_cible": tab_names.get(tab_key, tab_key),
                    "colonne_source": col,
                    "colonne_cible": col,
                    "transformation": "Aucune (conservée telle quelle)",
                })
            # Add traceability columns
            for extra in ["keyword", "source_file", "source_sheet", "import_timestamp"]:
                mapping_data.append({
                    "onglet_cible": tab_names.get(tab_key, tab_key),
                    "colonne_source": "(ajoutée)",
                    "colonne_cible": extra,
                    "transformation": "Colonne de traçabilité ajoutée automatiquement",
                })

        df_mapping = pd.DataFrame(mapping_data)
        df_mapping.to_excel(writer, sheet_name="MAPPING", index=False, startrow=1,
                            header=False)
        ws = writer.sheets["MAPPING"]
        for col_idx, col_name in enumerate(df_mapping.columns):
            ws.write(0, col_idx, col_name, header_fmt)
        ws.freeze_panes(1, 0)
        ws.set_column(0, 0, 25)
        ws.set_column(1, 1, 35)
        ws.set_column(2, 2, 35)
        ws.set_column(3, 3, 50)

        # ── QUALITY_REPORT tab ─────────────────────────────────────────
        qr_data = []

        # Global stats
        qr_data.append({"categorie": "GLOBAL", "metrique": "Fichiers traités",
                         "valeur": str(total_files - len(errors)), "detail": ""})
        qr_data.append({"categorie": "GLOBAL", "metrique": "Fichiers en erreur",
                         "valeur": str(len(errors)),
                         "detail": "; ".join(e["file"] for e in errors[:10])})
        qr_data.append({"categorie": "GLOBAL", "metrique": "Keywords uniques",
                         "valeur": str(len(keywords_seen)), "detail": ""})
        qr_data.append({"categorie": "GLOBAL", "metrique": "Keywords en doublon",
                         "valeur": str(len(dup_keywords)),
                         "detail": "; ".join(list(dup_keywords.keys())[:20])})
        qr_data.append({"categorie": "GLOBAL", "metrique": "Timestamp import",
                         "valeur": TIMESTAMP, "detail": ""})

        # Per-tab stats
        total_rows = 0
        for key, count in stats.items():
            total_rows += count
            tab = tab_names.get(key, key)
            qr_data.append({
                "categorie": "ONGLET",
                "metrique": f"Lignes dans {tab}",
                "valeur": f"{count:,}",
                "detail": "",
            })

        qr_data.append({"categorie": "GLOBAL", "metrique": "Total lignes consolidées",
                         "valeur": f"{total_rows:,}", "detail": ""})

        # Duplicate keyword details
        for kw, file_list in sorted(dup_keywords.items(),
                                     key=lambda x: len(x[1]), reverse=True)[:30]:
            qr_data.append({
                "categorie": "DOUBLON_KEYWORD",
                "metrique": kw,
                "valeur": str(len(file_list)),
                "detail": "; ".join(file_list[:5]),
            })

        # Error details
        for err in errors:
            qr_data.append({
                "categorie": "ERREUR",
                "metrique": err["file"],
                "valeur": "Erreur lecture",
                "detail": err["error"][:200],
            })

        # Anomalies: search volume = 0 or None
        if "SEARCH_VOLUME" in consolidated:
            sv_df = consolidated["SEARCH_VOLUME"]
            no_volume = sv_df[
                (sv_df["Search Volume"].isna()) | (sv_df["Search Volume"] == 0) |
                (sv_df["Search Volume"] == "0") | (sv_df["Search Volume"] == "None")
            ]
            qr_data.append({
                "categorie": "ANOMALIE",
                "metrique": "Keywords sans volume de recherche",
                "valeur": str(len(no_volume)),
                "detail": "; ".join(no_volume["keyword"].head(10).tolist()),
            })

        df_qr = pd.DataFrame(qr_data)
        df_qr.to_excel(writer, sheet_name="QUALITY_REPORT", index=False, startrow=1,
                        header=False)
        ws = writer.sheets["QUALITY_REPORT"]
        for col_idx, col_name in enumerate(df_qr.columns):
            ws.write(0, col_idx, col_name, header_fmt)
        ws.freeze_panes(1, 0)
        ws.set_column(0, 0, 20)
        ws.set_column(1, 1, 40)
        ws.set_column(2, 2, 20)
        ws.set_column(3, 3, 80)

        # ── README tab ─────────────────────────────────────────────────
        readme_lines = [
            ["CONSOLIDATION THRUUU - README"],
            [""],
            ["Date de génération", TIMESTAMP],
            ["Outil source", "Thruuu (analyse SERP)"],
            ["Répertoire source", INPUT_DIR],
            ["Fichiers traités", f"{total_files - len(errors)} / {total_files}"],
            [""],
            ["ONGLETS DU CLASSEUR"],
            ["SERP_OVERVIEW", "Résultats SERP complets : position, URL, titre, hostname, PageRank, word count, etc."],
            ["SEARCH_VOLUME", "Volume de recherche, CPC, compétition pour chaque keyword"],
            ["MONTHLY_SEARCH_VOL", "Tendance mensuelle du volume de recherche"],
            ["AIO_OVERVIEW", "Résultats AI Overview (si disponibles)"],
            ["FAQ", "Questions/réponses FAQ trouvées dans les pages"],
            ["AIO_FAQ", "FAQ issues des AI Overviews"],
            ["FREQUENT_QUESTIONS", "Questions fréquentes détectées (H1-H3)"],
            ["PAA", "People Also Ask (questions associées Google)"],
            ["RELATED_SEARCH", "Recherches associées Google"],
            ["MAPPING", "Table de correspondance colonnes source → cible"],
            ["QUALITY_REPORT", "Statistiques, doublons, erreurs, anomalies"],
            [""],
            ["COLONNES DE TRAÇABILITÉ (ajoutées à chaque onglet)"],
            ["keyword", "Le mot-clé recherché (extrait de l'onglet Info de chaque fichier)"],
            ["source_file", "Nom du fichier .xlsx d'origine"],
            ["source_sheet", "Nom de l'onglet source dans le fichier d'origine"],
            ["import_timestamp", "Date/heure de l'import"],
            [""],
            ["RÈGLES DE NETTOYAGE"],
            ["1. Espaces", "Suppression des espaces avant/après (trim) sur toutes les colonnes texte"],
            ["2. Valeurs vides", "'None', 'nan', '' → remplacés par cellule vide"],
            ["3. Dates sentinelles", "'No Publication Date Found', 'No Modification Date Found' → vide"],
            ["4. Doublons", "Colonne is_keyword_duplicate dans SERP_OVERVIEW et SEARCH_VOLUME (True si le keyword apparaît dans plusieurs fichiers, seule la 1ère occurrence est False)"],
            [""],
            ["CLÉ DE DÉDOUBLONNAGE"],
            ["Clé primaire", "keyword (le mot-clé recherché)"],
            ["Stratégie", "Toutes les lignes sont conservées. Le flag is_keyword_duplicate permet de filtrer les doublons si besoin."],
        ]

        ws_readme = workbook.add_worksheet("README")
        title_fmt = workbook.add_format({
            "bold": True, "font_size": 14, "font_color": "#1F4E79",
        })
        bold_fmt = workbook.add_format({"bold": True})
        section_fmt = workbook.add_format({
            "bold": True, "font_size": 12, "bg_color": "#D6E4F0",
        })

        for row_idx, row in enumerate(readme_lines):
            if len(row) == 1 and row[0] and row[0].isupper():
                ws_readme.write(row_idx, 0, row[0],
                                title_fmt if row_idx == 0 else section_fmt)
            elif len(row) >= 2:
                ws_readme.write(row_idx, 0, row[0], bold_fmt)
                ws_readme.write(row_idx, 1, row[1])

        ws_readme.set_column(0, 0, 30)
        ws_readme.set_column(1, 1, 100)

    print(f"\nTerminé ! Fichier généré : {OUTPUT_FILE}")
    print(f"Taille : {os.path.getsize(OUTPUT_FILE) / 1024 / 1024:.1f} Mo")

    # Print summary
    print("\n" + "=" * 60)
    print("RÉSUMÉ")
    print("=" * 60)
    print(f"Fichiers traités : {total_files - len(errors)} / {total_files}")
    print(f"Fichiers en erreur : {len(errors)}")
    print(f"Keywords uniques : {len(keywords_seen)}")
    print(f"Keywords en doublon : {len(dup_keywords)}")
    print(f"Total lignes : {total_rows:,}")
    for key, count in stats.items():
        print(f"  {tab_names.get(key, key)}: {count:,}")


if __name__ == "__main__":
    main()
