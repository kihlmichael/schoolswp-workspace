"""Emit base64 of each consolidated .md file as separate .b64.txt files."""
import base64
from pathlib import Path

OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-customer')
for f in sorted(OUT_DIR.glob('*.md')):
    data = f.read_bytes()
    b64 = base64.b64encode(data).decode('ascii')
    (OUT_DIR / (f.stem + '.b64.txt')).write_text(b64, encoding='ascii')
    print(f"{f.name:50s} {len(data):>8} bytes -> {f.stem}.b64.txt ({len(b64)} chars)")
