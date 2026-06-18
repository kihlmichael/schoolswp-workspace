"""Split oversized markdown files (>200 KB) into part1/part2 (or more) preserving section structure."""
import re
from pathlib import Path

OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-dev')

# Files to split: (filename, max_size_bytes, parts_basename)
TARGETS = [
    ('02-api-rest-overview.md',         70 * 1024, '02', 'api-rest-overview'),
    ('03-hooks-actions.md',             70 * 1024, '03', 'hooks-actions'),
    ('04-hooks-filters.md',             70 * 1024, '04', 'hooks-filters'),
    ('05-database-models.md',           70 * 1024, '05', 'database-models'),
    ('06-database-schema-query.md',     70 * 1024, '06', 'database-schema-query'),
    ('08-payment-gateway-integration.md', 70 * 1024, '08', 'payment-gateway-integration'),
]

def split_file(filename, max_bytes, num_prefix, slug):
    src = OUT_DIR / filename
    # Clean up any old parts from a previous split run
    for old in OUT_DIR.glob(f"{num_prefix}?-{slug}-part*.md"):
        old.unlink()
    text = src.read_text(encoding='utf-8')

    # Page boundary in the rendered files is `\n\n---\n\n## ` (a separator + a new page header).
    # We use this to split into per-page chunks. Each page in render_page produces:
    #   "## {title}\n\n**URL** : {url}\n\n{markdown}\n"
    # joined with "\n---\n" by write_section. So the safe boundary is the '## ' that comes
    # directly after '\n---\n\n' (i.e. preceded by a horizontal rule).
    # Find these positions to chunk reliably.
    first_page_match = re.search(r'(?ms)^## (?!.*?\bURL\b)', text)  # unused, fallback
    # Locate every '## ' that begins a *page* (immediately after '---' separator block, or first one after header).
    # We do this by finding all '## ' offsets where the preceding non-empty line is '---'.
    page_boundary = re.compile(r'(?ms)(?:^|\n)---\n+(## )')
    # First boundary may be a leading '---' just under the intro; locate first '## ' that follows the file's first '---' line.
    first_dash = text.find('\n---\n')
    if first_dash == -1:
        print(f"WARNING no '---' separator in {filename}; skipping split")
        return [filename]
    # Header block = everything up to and including the first '---' (with its trailing newline).
    header_end = text.find('\n', first_dash + 1) + 1
    header_block = text[:header_end].rstrip() + "\n\n"

    # Find all page-start positions: lines '## ' that come right after a horizontal rule
    # ('\n---\n+') or at the very beginning. Pages internal '---' separators are NOT followed
    # by '## ', so we use that as the reliable per-page boundary.
    rest = text[header_end:]
    # First, locate every offset where a '## ' starts a new page: it must be preceded by
    # '\n---\n' followed by blank lines. Use a positive lookbehind via regex.
    page_starts = []
    # Find the first '## ' at column 0 (start-of-line or string).
    first_h2 = re.search(r'(?ms)^## ', rest)
    if first_h2:
        page_starts.append(first_h2.start())
    for mm in re.finditer(r'\n---\n\s*\n## ', rest):
        # offset of the '## ' marker
        page_starts.append(mm.end() - 3)  # back up to capture '## '
    # Dedupe & sort
    page_starts = sorted(set(page_starts))
    if not page_starts:
        # fallback: split on every '## '
        page_starts = [mm.start() for mm in re.finditer(r'(?ms)^## ', rest)]
    page_starts.sort()
    page_starts.append(len(rest))
    chunks = []
    for i in range(len(page_starts) - 1):
        chunk_text = rest[page_starts[i]:page_starts[i+1]].strip('\n')
        if chunk_text:
            chunks.append(chunk_text + "\n\n---\n\n")

    # Now greedily bucket chunks into parts so that each part stays under max_bytes
    parts = []
    current = []
    current_size = len(header_block.encode('utf-8'))
    for c in chunks:
        c_size = len(c.encode('utf-8'))
        if current and (current_size + c_size > max_bytes):
            parts.append(current)
            current = []
            current_size = len(header_block.encode('utf-8'))
        current.append(c)
        current_size += c_size
    if current:
        parts.append(current)

    # If only one part results, no need to split
    if len(parts) == 1:
        return [filename]

    written = []
    suffixes = list('abcdefghijklmnopqrstuvwxyz')
    base_header_match = re.search(r'^# (.+)$', header_block, flags=re.MULTILINE)
    base_title = base_header_match.group(1).strip() if base_header_match else filename

    for idx, part_chunks in enumerate(parts, start=1):
        suffix = suffixes[idx - 1]
        new_name = f"{num_prefix}{suffix}-{slug}-part{idx}.md"
        new_path = OUT_DIR / new_name
        # Adjust header to mention part number
        part_header = re.sub(
            r'^# (.+)$',
            lambda m: f"# {m.group(1)} (Part {idx}/{len(parts)})",
            header_block,
            count=1,
            flags=re.MULTILINE,
        )
        body = "".join(part_chunks)
        new_path.write_text(part_header + body, encoding='utf-8')
        written.append(new_name)
        size_kb = new_path.stat().st_size / 1024
        print(f"  -> {new_name} ({size_kb:.1f} KB, pages={len(part_chunks)})")

    # Remove the original (oversized) so it doesn't get uploaded
    src.unlink()
    print(f"  (removed original {filename})")
    return written

for fname, max_bytes, num_prefix, slug in TARGETS:
    src = OUT_DIR / fname
    if not src.exists():
        continue
    size_kb = src.stat().st_size / 1024
    if size_kb <= max_bytes / 1024:
        print(f"OK {fname} ({size_kb:.1f} KB) — no split needed")
        continue
    print(f"\nSplitting {fname} ({size_kb:.1f} KB)...")
    split_file(fname, max_bytes, num_prefix, slug)

print("\n=== Final files ===")
for p in sorted(OUT_DIR.iterdir()):
    if p.suffix == '.md':
        size_kb = p.stat().st_size / 1024
        print(f"  {p.name:55} {size_kb:7.1f} KB")
