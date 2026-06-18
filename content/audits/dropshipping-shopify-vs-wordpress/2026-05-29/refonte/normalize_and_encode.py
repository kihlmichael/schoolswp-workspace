"""Re-collapse prettier-wrapped Gutenberg tags to single lines, then base64-encode."""
import base64
import re
from pathlib import Path

src = Path(__file__).parent / "content-gutenberg.html"
out_txt = Path(__file__).parent / "content-normalized.txt"
out_b64 = Path(__file__).parent / "content.b64"

html = src.read_text(encoding="utf-8")

# Collapse internal whitespace inside <p>, <li>, <h1-3> elements onto one line.
def collapse(m):
    inner = m.group(2)
    inner = re.sub(r"\s+", " ", inner).strip()
    return f"{m.group(1)}{inner}{m.group(3)}"

# <p ...> ... </p>
html = re.sub(r"(<p\b[^>]*>)(.*?)(</p>)", collapse, html, flags=re.S)
html = re.sub(r"(<li\b[^>]*>)(.*?)(</li>)", collapse, html, flags=re.S)
html = re.sub(r"(<h2\b[^>]*>)(.*?)(</h2>)", collapse, html, flags=re.S)
html = re.sub(r"(<h3\b[^>]*>)(.*?)(</h3>)", collapse, html, flags=re.S)

# Normalize blank lines (max 1 between blocks)
html = re.sub(r"\n{3,}", "\n\n", html).strip() + "\n"

out_txt.write_text(html, encoding="utf-8")
b64 = base64.b64encode(html.encode("utf-8")).decode("ascii")
out_b64.write_text(b64, encoding="ascii")

# sanity
print("bytes:", len(html.encode("utf-8")))
print("b64 len:", len(b64))
print("placeholders:",
      html.count("__TOC_BLOCK__"),
      html.count("__NINJA_TABLE__"),
      html.count("__CTA_BLOCK__"))
print("wp open/close:", html.count("<!-- wp:"), html.count("<!-- /wp:"))
print("em-dash:", html.count("—"), "en-dash:", html.count("–"))
# verify no multiline <p> remains
multiline_p = len(re.findall(r"<p\b[^>]*>[^<]*\n", html))
print("multiline <p> remaining:", multiline_p)
