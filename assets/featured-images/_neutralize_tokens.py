"""Scrub Novamira upload tokens from _upload_*.sh scripts (replace 3rd field with a placeholder)."""

import glob
import re

# Matches a ROWS line "ID lang TOKEN" where TOKEN is a long token string.
ROW = re.compile(r"^(\d{2,}\s+[a-z]{2}\s+)(\S{40,})\s*$")
PLACEHOLDER = "TOKEN_NEUTRALIZED"

total_files = 0
total_tokens = 0
for path in sorted(glob.glob("_upload_*.sh")):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    changed = 0
    out = []
    for line in lines:
        m = ROW.match(line)
        if m:
            out.append(f"{m.group(1)}{PLACEHOLDER}\n")
            changed += 1
        else:
            out.append(line)
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(out)
        total_files += 1
        total_tokens += changed
        print(f"  {path}: {changed} tokens neutralized")
    else:
        print(f"  {path}: (no token rows matched)")

print(f"Done: {total_tokens} tokens scrubbed across {total_files} files")
