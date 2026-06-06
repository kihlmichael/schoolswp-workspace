import json
import urllib.request
import re
import os
import subprocess
import sys

# Config for multi-language synchronization
LANGS = {
    'fr': {
        'spreadsheet_id': '1AXUQlvhFbbCrCex_LZjyh8kVS7KX2jn_TJGaDgtoSwU',
        'wiki_path': os.path.join('content', 'docs', 'articles-blog.md'),
        'url_prefix': 'https://schoolswp.com/'
    },
    'de': {
        'spreadsheet_id': '1-kp7VkCs_e5u17mAWEOjXtgbADAStl3qdJ45Am4Mqy0',
        'wiki_path': os.path.join('content', 'docs', 'articles-blog-de.md'),
        'url_prefix': 'https://schoolswp.com/de/'
    },
    'en': {
        'spreadsheet_id': '1mFfPvThhJikma6KrN7edqs5A3ve2mqb1zqYCD54U_vc',
        'wiki_path': os.path.join('content', 'docs', 'articles-blog-en.md'),
        'url_prefix': 'https://schoolswp.com/en/'
    }
}

WP_API_URL = "https://schoolswp.com/wp-json/wp/v2/posts?per_page=30&status=publish"

# Detect GWS CLI execution arguments (Node direct vs CMD fallback)
GWS_EXEC_ARGS = ["gws"]
possible_js_paths = [
    r"C:\Users\conta\AppData\Roaming\npm\node_modules\@googleworkspace\cli\run.js",
    os.path.expandvars(r"%APPDATA%\npm\node_modules\@googleworkspace\cli\run.js")
]
for js_path in possible_js_paths:
    if os.path.exists(js_path):
        GWS_EXEC_ARGS = ["node", js_path]
        break

print("Checking for new blog articles in all languages on schoolsWP...")

# 1. Fetch latest posts from WordPress REST API (returns all languages)
try:
    req = urllib.request.Request(
        WP_API_URL, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        wp_posts = json.loads(response.read().decode('utf-8'))
except Exception as e:
    print(f"Error connecting to WordPress API: {e}")
    sys.exit(1)

if not wp_posts:
    print("No posts retrieved.")
    sys.exit(0)

def detect_language(post):
    link = post.get('link', '')
    if '/de/' in link:
        return 'de'
    elif '/en/' in link:
        return 'en'
    else:
        return 'fr'

def clean_title(title):
    # Unescape HTML entities
    title = title.replace("&amp;", "&").replace("&#8211;", "-").replace("&#8212;", "-").replace("&#8216;", "'").replace("&#8217;", "'")
    # Replace em-dashes (—) and en-dashes (–) to satisfy Rule 13 bis
    title = title.replace("—", " - ").replace("–", " - ")
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def update_wiki_table(wiki_content, year, title, date_only, url):
    year_header = f"## 📅 Année {year}"
    
    if year_header not in wiki_content:
        # Create a new year section at the top of the lists
        insert_marker = "---"
        pos = wiki_content.find(insert_marker)
        if pos != -1:
            insert_pos = pos + len(insert_marker)
            new_section = f"\n\n## 📅 Année {year}\n\n| # | Titre | Date de Publication | Lien Direct |\n|---|-------|---------------------|-------------|\n| 1 | {title} | {date_only} | [Voir l'article]({url}) |\n"
            return wiki_content[:insert_pos] + new_section + wiki_content[insert_pos:]
        else:
            # Append to the end
            new_section = f"\n\n## 📅 Année {year}\n\n| # | Titre | Date de Publication | Lien Direct |\n|---|-------|---------------------|-------------|\n| 1 | {title} | {date_only} | [Voir l'article]({url}) |\n"
            return wiki_content + new_section

    # If the year section exists, parse and update it
    start_pos = wiki_content.find(year_header)
    end_pos = wiki_content.find("## 📅 Année", start_pos + len(year_header))
    if end_pos == -1:
        end_pos = len(wiki_content)
        
    section_content = wiki_content[start_pos:end_pos]
    
    # Parse the table rows
    lines = section_content.split('\n')
    header_lines = []
    rows = []
    
    found_separator = False
    for line in lines:
        if line.strip().startswith('|'):
            if '---|' in line or '---|---' in line:
                found_separator = True
                header_lines.append(line)
            elif not found_separator:
                header_lines.append(line)
            else:
                # Data row - Extract columns
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 4:
                    rows.append(parts)
        else:
            if not found_separator:
                header_lines.append(line)
                
    # Add new row at the beginning (newest first)
    new_row = ["1", title, date_only, f"[Voir l'article]({url})"]
    rows.insert(0, new_row)
    
    # Re-index rows
    for idx, row in enumerate(rows, 1):
        row[0] = str(idx)
        
    # Rebuild section content
    new_section_lines = []
    for line in header_lines:
        if not line.strip().startswith('|'):
            new_section_lines.append(line)
            
    new_section_lines.append("| # | Titre | Date de Publication | Lien Direct |")
    new_section_lines.append("|---|-------|---------------------|-------------|")
    
    for row in rows:
        new_section_lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
        
    new_section_content = '\n'.join(new_section_lines) + '\n'
    return wiki_content[:start_pos] + new_section_content + wiki_content[end_pos:]

# Load current wiki files for all languages
wiki_contents = {}
for lang, config in LANGS.items():
    if not os.path.exists(config['wiki_path']):
        print(f"Error: Wiki file not found at {config['wiki_path']}")
        sys.exit(1)
    with open(config['wiki_path'], 'r', encoding='utf-8') as f:
        wiki_contents[lang] = f.read()

# Filter posts to find new ones for each language
new_posts = []
for post in wp_posts:
    lang = detect_language(post)
    slug = post['slug']
    config = LANGS[lang]
    expected_url = f"{config['url_prefix']}{slug}"
    
    # Check if this slug/URL already exists in the wiki
    if expected_url not in wiki_contents[lang]:
        new_posts.append((lang, post))

if not new_posts:
    print("All local Wikis and Google Sheets are up to date! No new articles found.")
    sys.exit(0)

print(f"Found {len(new_posts)} new article(s) to synchronize!")

# Process and add new posts (in chronological order, oldest first)
for lang, post in reversed(new_posts):
    config = LANGS[lang]
    post_id = str(post['id'])
    title = clean_title(post['title']['rendered'])
    slug = post['slug']
    date_only = post['date'].split('T')[0]
    url = f"{config['url_prefix']}{slug}"
    year = date_only.split('-')[0]
    
    print(f"\nProcessing [{lang.upper()}]: {title} ({date_only})")
    
    # A. Add to Google Sheet
    print(f"-> Appending to {lang.upper()} Google Sheet ({config['spreadsheet_id']})...")
    row_data = [[post_id, title, slug, date_only, url]]
    json_str = json.dumps(row_data)
    
    append_cmd = GWS_EXEC_ARGS + [
        "sheets", "+append",
        "--spreadsheet", config['spreadsheet_id'],
        "--json-values", json_str
    ]
    
    append_result = subprocess.run(append_cmd, capture_output=True, text=True)
    
    if append_result.returncode != 0:
        print(f"   [Error] Could not append to Google Sheet: {append_result.stderr}")
    else:
        print("   [Success] Added to Google Sheet!")
        
    # B. Add to local Wiki
    print(f"-> Prepending and re-indexing local {lang.upper()} Wiki...")
    wiki_contents[lang] = update_wiki_table(wiki_contents[lang], year, title, date_only, url)
    
    # Save updated Wiki content immediately to avoid race conditions
    with open(config['wiki_path'], 'w', encoding='utf-8') as f:
        f.write(wiki_contents[lang])
    print(f"   [Success] Updated {config['wiki_path']}!")

print("\nSynchronization complete! All Wikis and Google Sheets are 100% up to date.")
