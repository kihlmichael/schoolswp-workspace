#!/usr/bin/env python3
"""Verify that post 52944 rendered correctly on the public URL."""
import urllib.request, re, sys, json

URL = "https://schoolswp.com/creer-plateforme-formation-wordpress/"
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 schoolsWP-verify"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="replace")

def first_match(pat, flags=0):
    m = re.search(pat, html, flags)
    return m.group(1).strip() if m else None

title_tag = first_match(r"<title[^>]*>([^<]+)</title>")
meta_desc = first_match(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', re.IGNORECASE)
og_title = first_match(r'<meta[^>]*property="og:title"[^>]*content="([^"]+)"', re.IGNORECASE)
canonical = first_match(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"', re.IGNORECASE)

print(f"[title ] {title_tag}")
print(f"[meta  ] {meta_desc}")
print(f"[og    ] {og_title}")
print(f"[canon ] {canonical}")

kws = [
    "woocommerce", "EasyHoster", "FlyingPress", "Kadence",
    "certification", "sécurité", "référencement", "design",
    "Intégrer WooCommerce", "Sécuriser votre plateforme"
]
print("\n[body KW presence]")
for kw in kws:
    n = html.lower().count(kw.lower())
    flag = "OK" if n > 0 else "MISS"
    print(f"  [{flag}] {kw}: {n}")

# Schema FAQ check
faq_schemas = re.findall(r'"@type"\s*:\s*"FAQPage"', html)
print(f"\n[schema] FAQPage instances: {len(faq_schemas)}")
questions = re.findall(r'"@type"\s*:\s*"Question"[^{]*"name"\s*:\s*"([^"]+)"', html)
print(f"[schema] Question entries: {len(questions)}")
for q in questions[:10]:
    print(f"  - {q}")
