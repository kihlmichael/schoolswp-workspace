#!/usr/bin/env python3
"""Snapshot the LiveAvatar documentation (docs.liveavatar.com) to clean per-page Markdown.

LiveAvatar docs are served by Mintlify, which exposes:
  - /sitemap.xml          -> the page list
  - <page>.md             -> a byte-perfect Markdown variant of each page
  - /llms.txt             -> curated index
  - /llms-full.txt        -> the full docs in a single file
  - /openapi.json         -> the API spec

This pulls the per-page .md variants (cleaner than defuddle/firecrawl) and writes them
mirroring the URL structure, each with a source-brute frontmatter, plus a generated
_index-documentation.md and the three side artifacts.

Designed for a monthly cron (zero Anthropic quota). Default output: snapshots/<date>/.

Usage:
  python snapshot.py                      # -> snapshots/<today>/
  python snapshot.py --out path/to/dir    # custom output dir
  python snapshot.py --date 2026-07-01    # override the stamped date
"""

from __future__ import annotations

import argparse
import datetime
import mimetypes
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://docs.liveavatar.com"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# Pages referenced in llms.txt but possibly absent from sitemap.xml; probed, kept if 200.
EXTRA_CANDIDATES = [
    "/docs/faq/master-faq",
    "/docs/faq/migration-guide",
    "/docs/faq/heygen-comparison",
    "/docs/faq/migration-faqs",
    "/docs/lite-mode/integrations",
    "/docs/elevenlabs-agent-plugin",
    "/docs/socials/x",
]
# Pages whose .md is an external embed (Notion/X) -> stubbed instead of dumping HTML.
EXTERNAL_EMBED = {"docs/faq/master-faq", "docs/socials/x"}


def fetch(url: str, timeout: int = 40) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001
        print(f"  ! error {url}: {e}")
        return 0, b""


def url_to_path(loc: str) -> str:
    p = loc[len(BASE) :].strip("/")
    return p if p else "index"


def md_url(rel: str) -> str:
    return f"{BASE}/{rel}.md"


def section_of(rel: str) -> str:
    parts = rel.split("/")
    if len(parts) == 1:
        return "root"
    return parts[-2] if len(parts) >= 3 else parts[0]


def extract_title(md: str, fallback: str) -> str:
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return fallback.replace("-", " ").title()


def extract_desc(md: str) -> str:
    seen_h1 = False
    for ln in (line.strip() for line in md.splitlines()):
        if ln.startswith("# "):
            seen_h1 = True
            continue
        if seen_h1 and ln and not ln.startswith("Source:") and not ln.startswith("#"):
            return ln
    return ""


def build_frontmatter(rel: str, url: str, title: str, desc: str, date_scrape: str, embed: bool) -> str:
    section = section_of(rel)
    tags = ["liveavatar", "heygen", "doc", "source-liveavatar", section]
    if rel.startswith("api-reference"):
        tags.append("api-reference")
    fm = [
        "---",
        "project: liveavatar",
        "type: doc-page",
        "source: liveavatar-docs",
        f"url: {url}",
        f"section: {section}",
        f"slug: {rel.split('/')[-1]}",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f'description: "{desc.replace(chr(34), chr(39))}"',
        f"date_scrape: {date_scrape}",
        "language: en-orig",
        "status: source-brute",
        "michael_status: a-voir",
        "formation_use: false",
    ]
    if embed:
        fm.append("is_external_embed: true")
    fm.append("tags: [" + ", ".join(tags) + "]")
    fm.append("---")
    fm.append("")
    fm.append(
        f"> Source: <{url}> - scraped {date_scrape} from docs.liveavatar.com "
        "(Mintlify .md variant). English original preserved as-is."
    )
    fm.append("")
    return "\n".join(fm) + "\n"


def stub_body(rel: str, url: str, title: str, desc: str) -> str:
    return (
        f"# {title}\n\n{desc}\n\n"
        f"> Note (snapshot): cette page embarque du contenu externe (Notion/X) ; sa variante "
        f"`.md` renvoie un dump HTML non exploitable. Voir la page en ligne : <{url}>.\n"
    )


def mime_of(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in (".md", ".markdown"):
        return "text/markdown"
    if ext == ".txt":
        return "text/plain"
    if ext == ".json":
        return "application/json"
    return mimetypes.guess_type(str(path))[0] or "application/octet-stream"


def main() -> None:
    ap = argparse.ArgumentParser(description="Snapshot LiveAvatar docs to clean per-page Markdown.")
    ap.add_argument("--out", help="Output directory (default: snapshots/<date>/ next to this script)")
    ap.add_argument("--date", help="Stamp date YYYY-MM-DD (default: today)")
    args = ap.parse_args()

    date_scrape = args.date or datetime.date.today().isoformat()
    out_dir = Path(args.out) if args.out else (Path(__file__).resolve().parent / "snapshots" / date_scrape)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output: {out_dir}")

    # 1. sitemap (regex, no XML parser -> no XXE surface)
    code, body = fetch(f"{BASE}/sitemap.xml")
    locs: list[str] = []
    if code == 200 and body:
        locs = [m.strip() for m in re.findall(r"<loc>([^<]+)</loc>", body.decode("utf-8", "replace"))]
    print(f"sitemap: {len(locs)} urls")

    # 2. extras (probe)
    for c in EXTRA_CANDIDATES:
        full = f"{BASE}{c}"
        if full in locs:
            continue
        ccode, _ = fetch(md_url(url_to_path(full)))
        if ccode == 200:
            locs.append(full)
            print(f"  + extra kept: {c}")
        else:
            print(f"  - extra skipped ({ccode}): {c}")

    locs = sorted(set(locs))
    print(f"Total pages: {len(locs)}")

    results = []
    for i, loc in enumerate(locs, 1):
        rel = url_to_path(loc)
        out_file = out_dir / (rel + ".md")
        out_file.parent.mkdir(parents=True, exist_ok=True)
        title = rel.split("/")[-1].replace("-", " ").title()
        desc = ""
        if rel in EXTERNAL_EMBED:
            body_md = stub_body(rel, loc, title, desc)
            fm = build_frontmatter(rel, loc, title, desc, date_scrape, embed=True)
            out_file.write_text(fm + body_md, encoding="utf-8")
            results.append((rel, loc, 200, title, len(body_md)))
            print(f"  [{i}/{len(locs)}] STUB {rel}")
            continue
        scode, sbody = fetch(md_url(rel))
        if scode != 200 or not sbody:
            print(f"  [{i}/{len(locs)}] FAIL {scode}  {rel}")
            results.append((rel, loc, scode, "", 0))
            continue
        md = sbody.decode("utf-8", "replace")
        title = extract_title(md, rel.split("/")[-1])
        desc = extract_desc(md)
        fm = build_frontmatter(rel, loc, title, desc, date_scrape, embed=False)
        out_file.write_text(fm + md, encoding="utf-8")
        results.append((rel, loc, scode, title, len(md)))
        print(f"  [{i}/{len(locs)}] OK   {rel} ({len(md)} chars)")
        time.sleep(0.15)

    # 3. side artifacts
    for name in ("llms.txt", "llms-full.txt", "openapi.json"):
        c, b = fetch(f"{BASE}/{name}")
        if c == 200 and b:
            (out_dir / name).write_bytes(b)
            print(f"  saved {name} ({len(b)} bytes)")
        else:
            print(f"  ! could not save {name} ({c})")

    # 4. index
    ok = [r for r in results if r[2] == 200]
    fail = [r for r in results if r[2] != 200]
    by_section: dict[str, list] = {}
    for rel, loc, scode, title, n in ok:
        by_section.setdefault(section_of(rel), []).append((rel, title))

    idx = [
        "---",
        "project: liveavatar",
        "type: doc-index",
        "source: liveavatar-docs",
        f"url: {BASE}",
        f"date_scrape: {date_scrape}",
        "status: source-brute",
        "michael_status: a-voir",
        "tags: [liveavatar, heygen, doc, source-liveavatar, index]",
        "---",
        "",
        "# LiveAvatar - Documentation snapshot",
        "",
        f"Snapshot de la doc officielle LiveAvatar (docs.liveavatar.com) capture le {date_scrape} "
        "via les variantes Markdown natives Mintlify (`.md`).",
        "",
        "LiveAvatar = plateforme HeyGen d'avatars video IA temps reel (lip-sync), successeur de "
        "HeyGen Interactive Avatar. 3 modes : Embed (iframe), FULL (pipeline IA gere par "
        "LiveAvatar, 2 credits/min), LITE (ta stack IA, LiveAvatar rend la video, 1 credit/min).",
        "",
        f"- Pages capturees : {len(ok)}/{len(results)}",
    ]
    if fail:
        idx.append(f"- Echecs : {len(fail)} ({', '.join(r[0] for r in fail)})")
    idx.append("- Annexes : `llms.txt`, `llms-full.txt`, `openapi.json`.")
    idx.append("")
    idx.append("## Arborescence par section")
    idx.append("")
    for sec in sorted(by_section):
        idx.append(f"### {sec}")
        idx.append("")
        for rel, title in sorted(by_section[sec]):
            idx.append(f"- [{title}]({rel}.md) - `{rel}`")
        idx.append("")
    (out_dir / "_index-documentation.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    print(f"\n=== Done: {len(ok)} ok, {len(fail)} failed. Output: {out_dir} ===")


if __name__ == "__main__":
    main()
