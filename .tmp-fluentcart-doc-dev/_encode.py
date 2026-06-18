"""Encode each markdown file to base64 in a sibling .b64 file."""
import base64
from pathlib import Path

D = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-dev')
for f in sorted(D.glob('*.md')):
    raw = f.read_bytes()
    b64 = base64.b64encode(raw).decode('ascii')
    (D / f"{f.stem}.b64").write_text(b64, encoding='ascii')
    print(f"{f.name:42}  raw={len(raw):7d} b={len(b64):7d}")
