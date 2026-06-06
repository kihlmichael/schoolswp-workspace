"""Locate Michael's FluentCart vs WooCommerce draft."""
import glob
import os

roots = ["D:/TÉLÉCHARGEMENT", "D:/TÉLÉCHARGEMENT/02_Comparatifs-thruuu"]
exts = (".docx", ".md", ".txt", ".gdoc", ".doc", ".rtf", ".odt")

for root in roots:
    if not os.path.isdir(root):
        print(f"(absent) {root}")
        continue
    print(f"\n=== {root} ===")
    for f in sorted(glob.glob(root + "/**/*", recursive=True)):
        if os.path.isfile(f):
            low = os.path.basename(f).lower()
            if low.endswith(exts) or "fluentcart" in low or "woo" in low:
                print(f"  {f}  ({os.path.getsize(f)/1024:.0f} KB)")
