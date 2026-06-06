"""List thruuu docx exports by mtime, parse the most recent one."""
import glob
import os
import time

cands = []
for pat in ["D:/TÉLÉCHARGEMENT/*.docx", "D:/TÉLÉCHARGEMENT/**/*.docx"]:
    for f in glob.glob(pat, recursive=True):
        cands.append(f)
cands = sorted(set(cands), key=lambda f: os.path.getmtime(f), reverse=True)

print("=== .docx by modification time (newest first) ===")
for f in cands[:12]:
    mt = time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(f)))
    print(f"  {mt}  {os.path.basename(f)}  ({os.path.getsize(f)/1024:.0f} KB)")

newest = cands[0] if cands else None
print("\n=== Parsing newest:", os.path.basename(newest) if newest else None, "===")
if newest:
    try:
        import zipfile
        import re
        with zipfile.ZipFile(newest) as z:
            xml = z.read("word/document.xml").decode("utf-8", "ignore")
        # strip tags, keep paragraph breaks
        xml = re.sub(r"</w:p>", "\n", xml)
        text = re.sub(r"<[^>]+>", "", xml)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        print(text[:2500])
    except Exception as e:
        print("parse error:", e)
