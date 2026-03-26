"""
Fill empty Google Docs with article content from WordPress REST API.
Finds all empty docs in the articles folders and injects the WP content.
"""

import html
import json
import os
import re
import subprocess
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GWS = os.path.expandvars(r"%APPDATA%\npm\gws.cmd")
WP_API = "https://schoolswp.com/wp-json/wp/v2"

# Parent folders
FOLDERS = {
    "articles-fr": "1oFMl1i2no8uSyl9sHNjqPxmXj7W4uFCe",
    "articles-en": "1YsbmU5Dg8R1kEsRPe4McL8BRsyOsB4bn",
    "articles-de": "1ZvvmtgKZgb4QJ5ydKJ7Q3_lFCXRP_D1G",
}


def gws(service, resource, action, params=None, json_body=None):
    cmd = [GWS, service, resource, action]
    if params:
        cmd += ["--params", json.dumps(params)]
    if json_body:
        cmd += ["--json", json.dumps(json_body)]
    r = subprocess.run(
        cmd, capture_output=True, timeout=90, encoding="utf-8", errors="replace"
    )
    stdout = r.stdout or ""
    try:
        j = stdout.find("{")
        if j >= 0:
            return json.loads(stdout[j:])
    except Exception:
        pass
    return None


def html_to_plain(content):
    """Convert HTML content to plain text, preserving structure."""
    if not content:
        return ""
    # Replace headers with text + newlines
    text = re.sub(r"<h[1-6][^>]*>(.*?)</h[1-6]>", r"\n\n\1\n\n", content, flags=re.DOTALL)
    # Replace paragraphs
    text = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", text, flags=re.DOTALL)
    # Replace <br> with newlines
    text = re.sub(r"<br\s*/?>", "\n", text)
    # Replace <li> with bullet points
    text = re.sub(r"<li[^>]*>(.*?)</li>", r"  - \1\n", text, flags=re.DOTALL)
    # Replace <strong>/<b> (keep text)
    text = re.sub(r"</?(?:strong|b)>", "", text)
    # Replace <em>/<i> (keep text)
    text = re.sub(r"</?(?:em|i)>", "", text)
    # Replace <a> with text + URL
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"\2 (\1)", text, flags=re.DOTALL)
    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Decode HTML entities
    text = html.unescape(text)
    # Clean up excessive whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    return text


def get_all_wp_posts():
    """Fetch all published posts with content."""
    posts = []
    page = 1
    while True:
        r = requests.get(
            f"{WP_API}/posts",
            params={
                "per_page": 100,
                "page": page,
                "status": "publish",
                "_fields": "id,title,slug,content,date,link",
            },
            timeout=60,
        )
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        posts.extend(data)
        page += 1
    return posts


def get_all_drive_docs(folder_id):
    """Recursively get all Google Docs in subfolders."""
    docs = []
    # Get subfolders
    r = gws(
        "drive", "files", "list",
        params={
            "q": f"'{folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
            "fields": "files(id,name)",
            "pageSize": 50,
        },
    )
    for subfolder in r.get("files", []) if r else []:
        # Get docs in subfolder
        r2 = gws(
            "drive", "files", "list",
            params={
                "q": f"'{subfolder['id']}' in parents and mimeType = 'application/vnd.google-apps.document' and trashed = false",
                "fields": "files(id,name)",
                "pageSize": 200,
            },
        )
        for doc in r2.get("files", []) if r2 else []:
            docs.append(doc)
    return docs


def check_doc_empty(doc_id):
    """Check if a Google Doc is empty (only has newline)."""
    r = gws("docs", "documents", "get", params={"documentId": doc_id})
    if not r:
        return True
    body = r.get("body", {})
    content = body.get("content", [])
    # Empty doc has 2 elements: sectionBreak + empty paragraph
    if len(content) <= 2:
        return True
    return False


def insert_text(doc_id, text):
    """Insert text at the beginning of a Google Doc."""
    # Truncate if too long (Google Docs API has limits)
    if len(text) > 100000:
        text = text[:100000] + "\n\n[... contenu tronque ...]"
    r = gws(
        "docs", "documents", "batchUpdate",
        params={"documentId": doc_id},
        json_body={
            "requests": [
                {
                    "insertText": {
                        "location": {"index": 1},
                        "text": text,
                    }
                }
            ]
        },
    )
    return r is not None


def match_post_to_doc(doc_name, posts):
    """Match a Drive doc to a WP post by title/slug similarity."""
    doc_lower = doc_name.lower()
    best_match = None
    best_score = 0

    for post in posts:
        slug = post["slug"].lower()
        title = html.unescape(post["title"]["rendered"]).lower()

        # Score by slug match
        slug_words = slug.replace("-", " ")
        score = 0
        if slug in doc_lower:
            score = 100
        elif len(slug_words) > 10 and slug_words[:25] in doc_lower:
            score = 80
        else:
            # Score by title word overlap
            title_words = set(re.findall(r"\w{4,}", title))
            doc_words = set(re.findall(r"\w{4,}", doc_lower))
            if title_words and doc_words:
                overlap = len(title_words & doc_words)
                score = (overlap / max(len(title_words), 1)) * 60

        if score > best_score and score >= 40:
            best_score = score
            best_match = post

    return best_match


def main():
    print("=" * 60)
    print("FILL DRIVE DOCS WITH WORDPRESS CONTENT")
    print("=" * 60)

    # Step 1: Get all WP posts with content
    print("\n[1/3] Fetching all WordPress posts with content...")
    posts = get_all_wp_posts()
    print(f"  {len(posts)} posts loaded")

    # Step 2: Get all Drive docs
    print("\n[2/3] Scanning Drive docs...")
    all_docs = []
    for name, folder_id in FOLDERS.items():
        docs = get_all_drive_docs(folder_id)
        all_docs.extend(docs)
        print(f"  {name}: {len(docs)} docs")
    print(f"  Total: {len(all_docs)} docs")

    # Step 3: Fill empty docs
    print("\n[3/3] Filling empty docs with content...")
    filled = skipped = no_match = errors = 0

    for doc in all_docs:
        # Check if empty
        if not check_doc_empty(doc["id"]):
            skipped += 1
            continue

        # Match to WP post
        post = match_post_to_doc(doc["name"], posts)
        if not post:
            no_match += 1
            continue

        # Get content
        content_html = post.get("content", {}).get("rendered", "")
        if not content_html:
            no_match += 1
            continue

        # Convert to plain text
        plain = html_to_plain(content_html)
        if not plain or len(plain) < 50:
            no_match += 1
            continue

        # Add metadata header
        title = html.unescape(post["title"]["rendered"])
        header = f"Source: {post.get('link', '')}\nDate: {post['date'][:10]}\n\n{title}\n{'=' * len(title)}\n\n"
        full_text = header + plain

        # Insert into doc
        if insert_text(doc["id"], full_text):
            filled += 1
            print(f"  + {doc['name'][:65]}...")
        else:
            errors += 1
            print(f"  ! {doc['name'][:65]}...")

        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"DONE: {filled} filled, {skipped} already have content, {no_match} no WP match, {errors} errors")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
