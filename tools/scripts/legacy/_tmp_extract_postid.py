import os, re, glob, sys

target_dir = r"C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/b47fd03a-625a-4929-a8f4-4ebaddad5489/tool-results"
files = sorted(glob.glob(os.path.join(target_dir, "mcp-firecrawl-firecrawl_scrape-1779643*.txt")))

for f in files:
    try:
        with open(f, encoding="utf-8", errors="replace") as fp:
            content = fp.read()
    except Exception as e:
        print(f"FAIL {os.path.basename(f)}: {e}")
        continue

    pid_match = re.search(r"postid-(\d+)", content)
    pid = pid_match.group(1) if pid_match else "?"

    canon_match = re.search(r'<link[^>]*rel=["\']?canonical["\']?[^>]*href=["\']([^"\']+)', content)
    canon = canon_match.group(1) if canon_match else "?"

    title_match = re.search(r"<title>([^<]+)</title>", content)
    title = title_match.group(1).strip() if title_match else "?"

    print(f"post_id={pid:>10} | {canon}")
    print(f"    title={title[:80]}")
