"""Extract a focused gap-analysis report from the 3 thruuu exports."""
import os
import sys
from statistics import median

import openpyxl

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SRC = r"D:\TÉLÉCHARGEMENT"
FILES = {
    "dropshipping shopify vs wordpress": "thruuu_export_dropshipping shopify vs wordpress_2026-5-29.xlsx",
    "shopify vs woocommerce": "thruuu_export_shopify vs woocommerce_2026-5-29.xlsx",
    "dropshipping woocommerce": "thruuu_export_dropshipping woocommerce_2026-5-29.xlsx",
}
NOISE = {"reddit","posts","top","of","the","and","to","a","is","in","for","you","your",
         "rereddit","comments","r","de","la","le","les","des","un","une","et","ou","est",
         "vs","du","en","que","qui","pour","sur","avec","ce","plus","au","aux","par"}

def s(v):
    return "" if v is None else str(v).replace("\n"," ").replace("\r"," ").strip()

for kw, fname in FILES.items():
    path = os.path.join(SRC, fname)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    print("\n" + "="*70)
    print(f"KEYWORD: {kw}")
    print("="*70)

    # --- SERP Overview: header + organic word counts ---
    ws = wb["SERP Overview"]
    rows = list(ws.iter_rows(values_only=True))
    header = [s(c) for c in rows[0]]
    print("\nSERP OVERVIEW COLUMNS:", " | ".join(f"{i}:{h}" for i,h in enumerate(header) if h))
    # find indices
    def idx(name):
        for i,h in enumerate(header):
            if name.lower() in h.lower():
                return i
        return None
    i_opos = idx("Organic Position")
    i_url = idx("URL")
    i_host = idx("Hostname") or idx("Host")
    i_words = idx("Word")
    i_score = idx("Score")
    wc = []
    print("\nORGANIC RESULTS (pos | words | score | host | url):")
    for r in rows[1:]:
        r = [s(c) for c in r]
        op = r[i_opos] if i_opos is not None and i_opos < len(r) else ""
        if not op:
            continue
        words = r[i_words] if i_words is not None and i_words < len(r) else ""
        score = r[i_score] if i_score is not None and i_score < len(r) else ""
        host = r[i_host] if i_host is not None and i_host < len(r) else ""
        url = r[i_url] if i_url is not None and i_url < len(r) else ""
        try:
            w = int(float(words))
            wc.append(w)
        except Exception:
            pass
        print(f"  {op:>3} | {words:>6} | {score:>5} | {host:<22} | {url[:70]}")
    if wc:
        print(f"\nWORD COUNT STATS (organic): min={min(wc)} median={int(median(wc))} max={max(wc)} n={len(wc)}")

    # --- Topic: top NLP terms (found in >=4 pages), excl noise ---
    ws = wb["Topic"]
    trows = list(ws.iter_rows(values_only=True))
    th = [s(c) for c in trows[0]]
    terms = []
    for r in trows[1:]:
        r = [s(c) for c in r]
        if len(r) < 6:
            continue
        term = r[0]
        try:
            found = int(float(r[1])); relev = float(r[5])
        except Exception:
            continue
        if term.lower() in NOISE or len(term) < 3:
            continue
        terms.append((found, relev, term))
    terms.sort(key=lambda x: (-x[0], -x[1]))
    print("\nTOP NLP TERMS (found_in_pages | relevancy | term):")
    for found, relev, term in terms[:45]:
        print(f"  {found:>2} | {relev:5.1f} | {term}")

    # --- Frequent Questions (Tag, Question, Count) count>=2 ---
    ws = wb["Frequent Questions"]
    qrows = list(ws.iter_rows(values_only=True))
    print("\nFREQUENT QUESTIONS (count>=2):")
    for r in qrows[1:]:
        r = [s(c) for c in r]
        if len(r) < 3:
            continue
        tag, q, cnt = r[0], r[1], r[2]
        try:
            if int(float(cnt)) >= 2:
                print(f"  [{tag}] ({cnt}) {q}")
        except Exception:
            pass
    wb.close()
print("\nDONE")
