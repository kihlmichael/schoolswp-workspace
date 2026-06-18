import sys
import json
import re

with open("d:/ANTIGRAVITY/drafts/schoolswp_home.html", "r", encoding="utf-8") as f:
    html = f.read()

# Title
title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
print(f"TITLE: {title_match.group(1) if title_match else 'None'}")

# Meta Description
desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
print(f"DESC: {desc_match.group(1) if desc_match else 'None'}")

# H1
h1_matches = re.findall(r'<h1.*?>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
print(f"H1 Count: {len(h1_matches)}")
for h1 in h1_matches:
    print(f" - {re.sub(r'<[^>]+>', '', h1).strip()}")

# H2
h2_matches = re.findall(r'<h2.*?>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
print(f"H2 Count: {len(h2_matches)}")
for h2 in h2_matches:
    print(f" - {re.sub(r'<[^>]+>', '', h2).strip()[:100]}...")

# Schema
schema_matches = re.findall(r'<script type="application/ld\+json".*?>(.*?)</script>', html, re.IGNORECASE | re.DOTALL)
print(f"SCHEMA COUNT: {len(schema_matches)}")
for i, schema_str in enumerate(schema_matches):
    try:
        data = json.loads(schema_str)
        if "@graph" in data:
            types = [item.get("@type", "Unknown") for item in data["@graph"]]
            print(f" Schema {i} Types: {', '.join(str(t) for t in types)}")
        else:
            print(f" Schema {i} Type: {data.get('@type')}")
    except Exception as e:
        print(f" Schema {i} invalid JSON: {e}")

# Check performance assets
print("Preload tags:", len(re.findall(r'<link rel=[\'"]preload[\'"]', html, re.IGNORECASE)))
print("Preconnect tags:", len(re.findall(r'<link rel=[\'"]preconnect[\'"]', html, re.IGNORECASE)))
print("Flying Press lazy CSS:", "flying-press" in html)
