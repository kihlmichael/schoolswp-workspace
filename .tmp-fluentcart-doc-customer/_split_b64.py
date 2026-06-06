"""Split each .b64.txt into chunks named <stem>.b64.p<N>.txt"""
from pathlib import Path

OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-customer')
CHUNK = 20000

# clear existing parts via overwrite-style: list and re-truncate
for old in OUT_DIR.glob('*.b64.p*.txt'):
    old.write_text('', encoding='ascii')  # truncate

for f in sorted(OUT_DIR.glob('*.b64.txt')):
    b64 = f.read_text(encoding='ascii')
    if len(b64) <= CHUNK:
        # single-piece - still write part1 for uniformity
        (OUT_DIR / (f.stem.replace('.b64', '') + '.b64.p1.txt')).write_text(b64, encoding='ascii')
        print(f"{f.name:50s} -> 1 part")
    else:
        parts = [b64[i:i+CHUNK] for i in range(0, len(b64), CHUNK)]
        stem = f.stem.replace('.b64', '')
        for i, p in enumerate(parts, 1):
            (OUT_DIR / f"{stem}.b64.p{i}.txt").write_text(p, encoding='ascii')
        print(f"{f.name:50s} -> {len(parts)} parts")
