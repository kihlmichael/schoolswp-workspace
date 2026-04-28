# -*- coding: utf-8 -*-
"""Extract Thruuu SERP export for flyingpress vs perfmatters."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
import openpyxl

XLSX = r"D:\TÉLÉCHARGEMENT\thruuu_export_flyingpress vs perfmatters_2026-4-24.xlsx"
wb = openpyxl.load_workbook(XLSX, data_only=True)
print(f"Sheets: {wb.sheetnames}\n")

# Info sheet
if 'Info' in wb.sheetnames:
    ws = wb['Info']
    print("=== Info ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            print(f"  {row[0]}: {row[1] if len(row)>1 else ''}")

# Search Volume
if 'Search Volume' in wb.sheetnames:
    ws = wb['Search Volume']
    print("\n=== Search Volume ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            print(f"  {row}")

# Monthly Search Volume
if 'Monthly Search Volume' in wb.sheetnames:
    ws = wb['Monthly Search Volume']
    print("\n=== Monthly Search Volume ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            print(f"  {row}")

# SERP Overview — top 20 positions
if 'SERP Overview' in wb.sheetnames:
    ws = wb['SERP Overview']
    print("\n=== SERP Overview ===")
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0] if rows else []
    # Find key columns
    idx_pos = header.index('Position') if 'Position' in header else 0
    idx_type = header.index('Type') if 'Type' in header else None
    idx_title = header.index('Title') if 'Title' in header else None
    idx_url = header.index('URL') if 'URL' in header else None
    idx_wc = header.index('Word Count') if 'Word Count' in header else None
    idx_ic = header.index('Image Count') if 'Image Count' in header else None
    idx_pr = header.index('Page Rank') if 'Page Rank' in header else None
    idx_host = header.index('Hostname') if 'Hostname' in header else None
    idx_modif = header.index('Modification Date') if 'Modification Date' in header else None
    idx_schema = header.index('Schema Type') if 'Schema Type' in header else None
    for row in rows[1:]:
        if row[idx_pos] is not None:
            title = (row[idx_title] or '')[:60] if idx_title else ''
            host = row[idx_host] if idx_host and row[idx_host] else '(none)'
            wc = row[idx_wc] if idx_wc else '?'
            pr = row[idx_pr] if idx_pr else '?'
            ic = row[idx_ic] if idx_ic else '?'
            modif = (str(row[idx_modif])[:10]) if idx_modif and row[idx_modif] else '?'
            print(f"  #{row[idx_pos]:<3} host={host:<30} wc={wc!s:<5} pr={pr!s:<6} images={ic!s:<3} modif={modif}  | {title}")

# H1 sheet
if 'Heading 1 (Organic page only)' in wb.sheetnames:
    ws = wb['Heading 1 (Organic page only)']
    print("\n=== H1 of organic pages ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            if row[0] == 'Page position':
                continue
            print(f"  #{row[0]}: {row[1][:100] if row[1] else '(empty)'}")

# H2 outline (top 30 rows only for brevity)
if 'Heading 2 (Organic page only)' in wb.sheetnames:
    ws = wb['Heading 2 (Organic page only)']
    print("\n=== H2 outline (up to 40 rows) ===")
    rows = list(ws.iter_rows(values_only=True))
    for i, row in enumerate(rows[1:41], 1):
        if any(c is not None for c in row):
            print(f"  #{row[0]}: {row[1][:100] if row[1] else '(empty)'}")

# FAQ
if 'FAQ' in wb.sheetnames:
    ws = wb['FAQ']
    print("\n=== FAQ schemas on SERP ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            if row[0] == 'Page position':
                continue
            q = row[2] if len(row) > 2 else ''
            print(f"  #{row[0]}  Q: {q[:140] if q else ''}")

# Frequent Questions
if 'Frequent Questions' in wb.sheetnames:
    ws = wb['Frequent Questions']
    print("\n=== Frequent Questions ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            if row[0] == 'Tag':
                continue
            print(f"  {row[0]:<4} (×{row[2]}) {row[1][:120] if row[1] else ''}")

# Related Search
if 'Related Search' in wb.sheetnames:
    ws = wb['Related Search']
    print("\n=== Related Search ===")
    for row in ws.iter_rows(values_only=True):
        if any(c is not None for c in row):
            print(f"  {row[0]}")

# Topic (top relevancy)
if 'Topic' in wb.sheetnames:
    ws = wb['Topic']
    print("\n=== Topic (top 40 by relevancy) ===")
    rows = list(ws.iter_rows(values_only=True))
    header = rows[0]
    data = [r for r in rows[1:] if r[0] and r[5] is not None]
    data.sort(key=lambda r: -float(r[5] or 0))
    print(f"  {'keyword':<40} found  total  rel")
    for r in data[:40]:
        print(f"  {str(r[0])[:40]:<40} {r[1]!s:>4}  {r[2]!s:>5}  {r[5]:>6.2f}")
