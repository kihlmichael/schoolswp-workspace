#!/usr/bin/env python3
"""Inject Kadence TOC + FAQ schema JSON-LD into post 2888497 (DE).

TOC : kadence/tableofcontents block (server-side computed, REST-safe).
FAQ : custom HTML block with <script type="application/ld+json"> FAQPage
      schema. Reads the 4 Kadence accordion panes already in the post
      to derive the questions/answers. Markup remains, only schema added.

Per memory reference_rank_math_toc_block_bug.md: Rank Math TOC block injected
via REST without populated `headings` attribute crashes Gutenberg. Kadence
TOC computes side-server and is REST-safe — confirmed in use on 5 posts.
"""

import base64
import html as html_lib
import json
import re
import secrets
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
WORKSPACE = ROOT / "content" / "articles" / "_workspace"
POST_ID = 2888497
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8"))["env"]
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http(method, url, auth, payload=None):
    headers = {
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-inject/1.0",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


def make_uid():
    return f"{POST_ID}_{secrets.token_hex(3)}-{secrets.token_hex(1)}"


# Kadence TOC block - structure cloned from existing DE article 739385
def build_toc_block():
    uid = make_uid()
    attrs = {
        "uniqueID": uid,
        "allowedHeaders": [{"h1": False, "h2": True, "h3": False, "h4": False, "h5": False, "h6": False}],
        "linkStyle": "underline_hover",
        "containerBackground": "palette9",
        "title": "Inhaltsverzeichnis",
        "titleColor": "palette3",
        "titleFontWeight": "bold",
        "titleBorderColor": "",
        "titleTextTransform": "uppercase",
        "enableToggle": True,
        "toggleIcon": "arrowcircle",
        "contentColor": "palette1",
        "contentHoverColor": "palette2",
        "listGap": [None, "", ""],
        "maxWidth": 500,
        "displayShadow": True,
        "shadow": [{"color": "#000000", "opacity": 0.5, "spread": -10, "blur": 25, "hOffset": 0, "vOffset": 14, "inset": False}],
        "enableSmoothScroll": True,
        "borderStyle": [
            {"top": ["palette3", "", 2], "right": ["palette3", "", 2],
             "bottom": ["palette3", "", 2], "left": ["palette3", "", 2], "unit": "px"}
        ],
        "titleBorderStyle": [
            {"top": [None, "", ""], "right": [None, "", ""],
             "bottom": [None, "", ""], "left": [None, "", ""], "unit": "px"}
        ],
        "enableTitleToggle": True,
    }
    return f"<!-- wp:kadence/tableofcontents {json.dumps(attrs, ensure_ascii=False)} /-->"


def extract_qa(content):
    """Extract title + answer text from each Kadence pane within the FAQ section."""
    # Find the H2 FAQ anchor
    faq_h2 = re.search(r"<h2[^>]*>Häufig gestellte Fragen</h2>", content)
    if not faq_h2:
        return []

    # All panes (the FAQ section is the only set of panes, per audit)
    panes = re.findall(
        r"<!-- wp:kadence/pane[\s\S]*?<!-- /wp:kadence/pane -->", content
    )

    qas = []
    for p in panes:
        title_m = re.search(
            r'class="kt-blocks-accordion-title">\s*([^<]+?)\s*</span>', p
        )
        # Collect all <p> texts
        paras = re.findall(r"<p[^>]*>([\s\S]*?)</p>", p)
        # Strip inline HTML
        clean_paras = []
        for para in paras:
            t = re.sub(r"<[^>]+>", " ", para)
            t = html_lib.unescape(t)
            t = re.sub(r"\s+", " ", t).strip()
            if t:
                clean_paras.append(t)
        if title_m and clean_paras:
            qas.append({"q": title_m.group(1).strip(), "a": " ".join(clean_paras)})
    return qas


def build_faq_schema_block(qas):
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": qa["q"],
                "acceptedAnswer": {"@type": "Answer", "text": qa["a"]},
            }
            for qa in qas
        ],
    }
    # Use compact JSON-LD; wrap in wp:html so Gutenberg keeps it byte-perfect
    json_ld = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
    return (
        "<!-- wp:html -->\n"
        f'<script type="application/ld+json">{json_ld}</script>\n'
        "<!-- /wp:html -->"
    )


def main():
    user, pw = load_creds()
    auth = auth_header(user, pw)

    st, post = http("GET", f"{BASE}/{POST_ID}?context=edit", auth)
    if st != 200:
        print(f"[error] GET {st}")
        sys.exit(1)
    content = post["content"]["raw"]
    (WORKSPACE / "post-2888497-backup-pre-toc-faq.json").write_text(
        json.dumps(post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    if "wp:kadence/tableofcontents" in content:
        print("[warn] Kadence TOC already present, will skip TOC injection")
        toc_present = True
    else:
        toc_present = False

    if "FAQPage" in content:
        print("[warn] FAQPage schema already present, will skip FAQ injection")
        faq_present = True
    else:
        faq_present = False

    # Extract Q&A from existing accordion
    qas = extract_qa(content)
    print(f"[scan] extracted {len(qas)} Q&A pairs from accordion")
    for i, qa in enumerate(qas, 1):
        print(f"  Q{i}: {qa['q'][:80]}")
        print(f"  A{i}: {qa['a'][:120]}...")

    if not qas and not faq_present:
        print("[error] could not extract Q&A from content", file=sys.stderr)
        sys.exit(2)

    new_content = content

    # ---- Insert TOC before first H2 ----
    if not toc_present:
        first_h2_anchor = "Warum die Ninja Tables DataTables-Engine den entscheidenden Unterschied macht"
        idx = new_content.find(first_h2_anchor)
        if idx < 0:
            print("[error] first H2 anchor not found")
            sys.exit(3)
        back = new_content.rfind("<!-- wp:", 0, idx)
        toc_block = build_toc_block() + "\n\n"
        new_content = new_content[:back] + toc_block + new_content[back:]
        print(f"[inject] TOC inserted at offset {back}")

    # ---- Insert FAQ schema before H2 "Häufig gestellte Fragen" ----
    if not faq_present and qas:
        faq_h2_anchor = "Häufig gestellte Fragen"
        idx = new_content.find(faq_h2_anchor)
        if idx < 0:
            print("[error] FAQ H2 anchor not found")
            sys.exit(4)
        back = new_content.rfind("<!-- wp:", 0, idx)
        faq_block = build_faq_schema_block(qas) + "\n\n"
        new_content = new_content[:back] + faq_block + new_content[back:]
        print(f"[inject] FAQ schema inserted at offset {back}")

    delta = len(new_content) - len(content)
    print(f"[size] {len(content)} -> {len(new_content)} chars (delta {delta:+d})")
    (WORKSPACE / "post-2888497-patched-toc-faq.html").write_text(new_content, encoding="utf-8")

    # Push
    st, resp = http("POST", f"{BASE}/{POST_ID}", auth, payload={"content": new_content})
    print(f"[push] HTTP {st}  modified={resp.get('modified')}")

    # Verify byte-perfect + presence
    st, after = http("GET", f"{BASE}/{POST_ID}?context=edit", auth)
    after_raw = after["content"]["raw"]
    print(f"  byte-perfect: {'YES ✓' if after_raw == new_content else 'NO'}")
    print(f"  TOC present : {'wp:kadence/tableofcontents' in after_raw}")
    print(f"  FAQPage     : {'FAQPage' in after_raw}")

    (WORKSPACE / "post-2888497-after-toc-faq.json").write_text(
        json.dumps(after, indent=2, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
