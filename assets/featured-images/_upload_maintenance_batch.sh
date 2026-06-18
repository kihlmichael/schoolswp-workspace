#!/usr/bin/env bash
# Upload the 13 maintenance-batch hero PNGs via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

ROWS="
2969996 fr TOKEN_NEUTRALIZED
1380389 fr TOKEN_NEUTRALIZED
1638614 en TOKEN_NEUTRALIZED
1638632 de TOKEN_NEUTRALIZED
57383 fr TOKEN_NEUTRALIZED
57412 en TOKEN_NEUTRALIZED
57413 de TOKEN_NEUTRALIZED
53653 fr TOKEN_NEUTRALIZED
57351 en TOKEN_NEUTRALIZED
57295 de TOKEN_NEUTRALIZED
50687 fr TOKEN_NEUTRALIZED
54889 en TOKEN_NEUTRALIZED
54888 de TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
