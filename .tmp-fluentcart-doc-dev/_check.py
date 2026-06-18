"""Quick sanity check: count code fences per file."""
import pathlib
FENCE = chr(96) * 3
for f in sorted(pathlib.Path('.').glob('*.md')):
    text = f.read_text(encoding='utf-8')
    fences = text.count(FENCE)
    php = text.count(FENCE + 'php')
    json_ct = text.count(FENCE + 'json')
    ts = text.count(FENCE + 'typescript')
    print(f'{f.name:42}  fences={fences:4}  php={php}  json={json_ct}  ts={ts}')
