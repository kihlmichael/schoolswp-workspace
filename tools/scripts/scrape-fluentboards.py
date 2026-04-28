"""Scrape fluentboards.com (docs + pages + blog) en Markdown.

Sorties dans content/docs/fluentboards/{docs,pages,blog}/ + INDEX.md.

Usage :
    python tools/scripts/scrape-fluentboards.py --section docs        # 38 URLs
    python tools/scripts/scrape-fluentboards.py --section pages       # 19 URLs
    python tools/scripts/scrape-fluentboards.py --section blog        # 91 URLs
    python tools/scripts/scrape-fluentboards.py --section all

Le scraper lit le sitemap.xml pour lister les URLs, puis fetch chaque page,
extrait le <article> principal, convertit en Markdown via html2text.

Courtois : User-Agent identifiable, 1s entre requêtes, timeout 20s.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.request
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUT_ROOT = PROJECT_ROOT / "content" / "docs" / "fluentboards"

HEADERS = {"User-Agent": "schoolsWP-scraper/1.0 (+https://schoolswp.com)"}
SITEMAPS = {
    "docs": "https://fluentboards.com/docs-sitemap1.xml",
    "pages": "https://fluentboards.com/page-sitemap1.xml",
    "blog": "https://fluentboards.com/post-sitemap1.xml",
}


def urls_from_sitemap(sitemap_url: str) -> list[str]:
    r = requests.get(sitemap_url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return re.findall(r"<loc>([^<]+)</loc>", r.text)


def slug_from_url(url: str) -> str:
    path = url.rstrip("/").rsplit("/", 1)[-1]
    return re.sub(r"[^a-z0-9-]+", "-", path.lower()) or "index"


SELECTORS = [
    "div.betterdocs-entry-content",  # BetterDocs (plugin WP utilisé par fluentboards/docs)
    "div.entry-content",              # WP standard
    "article.post",                   # blog
    "main",                           # fallback large
]


def extract_main(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    # Supprime les éléments parasites (nav, scripts, footer)
    for tag in soup.select("nav, script, style, header, footer, .betterdocs-feelings, .betterdocs-modalwindow, .betterdocs-articles-list"):
        tag.decompose()
    for sel in SELECTORS:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 200:
            return str(el)
    return html


def html_to_md(html: str) -> str:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False
    h.single_line_break = True
    h.protect_links = True
    md = h.handle(html)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md


def build_frontmatter(url: str, title: str) -> str:
    return f"---\nsource_url: {url}\ntitle: {title!r}\nscraped_at: {time.strftime('%Y-%m-%d')}\n---\n\n"


def extract_title(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    m = re.search(r"<title>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
    if m:
        return re.sub(r"\s+\|\s+.*$", "", m.group(1)).strip()
    return "Untitled"


def scrape_one(url: str, out_dir: Path) -> tuple[str, str, int]:
    """Retourne (title, filename, content_length)."""
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as r:
        html = r.read().decode("utf-8", errors="replace")
    title = extract_title(html)
    main = extract_main(html)
    md = html_to_md(main)
    slug = slug_from_url(url)
    out_file = out_dir / f"{slug}.md"
    out_file.write_text(build_frontmatter(url, title) + f"# {title}\n\n{md}\n", encoding="utf-8")
    return title, out_file.name, len(md)


def scrape_section(section: str) -> list[dict]:
    urls = urls_from_sitemap(SITEMAPS[section])
    out_dir = OUT_ROOT / section
    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    for i, url in enumerate(urls, 1):
        try:
            title, filename, size = scrape_one(url, out_dir)
            print(f"[{i:3d}/{len(urls)}] {section}/{filename}  ({size} chars)  {title[:60]}")
            results.append({"url": url, "title": title, "file": filename, "size": size})
        except Exception as exc:
            print(f"[{i:3d}/{len(urls)}] [FAIL] {url}: {exc}", file=sys.stderr)
            results.append({"url": url, "title": "ERROR", "file": "", "size": 0, "error": str(exc)})
        time.sleep(1.0)
    return results


def write_index(_sections: dict[str, list[dict]] | None = None) -> None:
    """Régénère INDEX.md en scannant tous les .md déjà présents sur disque.

    Ne dépend pas du run courant — un run isolé (--section docs) régénère quand même
    l'index complet en lisant ce qui existe dans docs/ + pages/ + blog/.
    """
    lines = [
        "# FluentBoards — documentation scrapée",
        "",
        f"Dernier scrape : {time.strftime('%Y-%m-%d')} — source : fluentboards.com",
        "",
        "Matériel brut pour :",
        "- référence technique (incoming webhook → scénario card auto sur audit < 70)",
        "- base pédagogique d'une future formation FluentBoards",
        "",
    ]
    for section in ("docs", "pages", "blog"):
        section_dir = OUT_ROOT / section
        if not section_dir.exists():
            continue
        files = sorted(section_dir.glob("*.md"))
        if not files:
            continue
        lines.append(f"## {section.capitalize()} ({len(files)} pages)")
        lines.append("")
        for f in files:
            title = _read_title(f)
            lines.append(f"- [{title}]({section}/{f.name})")
        lines.append("")
    (OUT_ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def _read_title(md_path: Path) -> str:
    try:
        for line in md_path.read_text(encoding="utf-8").splitlines()[:20]:
            if line.startswith("title:"):
                return line.split(":", 1)[1].strip().strip("'\"")
    except Exception:
        pass
    return md_path.stem


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--section", default="docs", choices=["docs", "pages", "blog", "all"])
    args = parser.parse_args()

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    targets = list(SITEMAPS.keys()) if args.section == "all" else [args.section]
    for section in targets:
        print(f"\n=== Section: {section} ===")
        scrape_section(section)
    write_index()
    print(f"\n[OK] Index ecrit : {OUT_ROOT / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
