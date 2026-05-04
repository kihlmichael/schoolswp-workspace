---
name: defuddle
description: Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, articles, blog posts, or any standard web page. Do NOT use for URLs ending in .md — those are already markdown, use WebFetch directly.
---

# Defuddle

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: run `npm install -g defuddle` (already installed globally on this workstation, version 0.18.1+).

## Usage

Always use `--md` for markdown output:

```
defuddle parse <url> --md
```

Save to file:

```
defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |

## Routing schoolsWP

Préférer defuddle (local, 0 $) à `firecrawl_scrape` (MCP distant) pour :

- Veille concurrentielle SEO (1 article propre rapidement)
- Sourcing pour cocons sémantiques (lecture article concurrent)
- Préparation de sources NotebookLM (markdown propre, sans HTML pollué)
- Audit `radar` / `seo-specialist` quand l'agent a besoin du contenu d'une URL

Garder `firecrawl_scrape` pour :

- Pages JS-rendered (defuddle ne gère pas le JS lourd)
- Crawl multi-pages d'un site complet
- Quand on a besoin de screenshots ou structured data
