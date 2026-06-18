#!/usr/bin/env bash
# Upload the 14 sandbox-batch hero PNGs via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

ROWS="
56148 fr TOKEN_NEUTRALIZED
58229 en TOKEN_NEUTRALIZED
56793 de TOKEN_NEUTRALIZED
54820 fr TOKEN_NEUTRALIZED
55955 en TOKEN_NEUTRALIZED
55956 de TOKEN_NEUTRALIZED
54821 fr TOKEN_NEUTRALIZED
58239 en TOKEN_NEUTRALIZED
58235 de TOKEN_NEUTRALIZED
53100 fr TOKEN_NEUTRALIZED
1295032 en TOKEN_NEUTRALIZED
52615 fr TOKEN_NEUTRALIZED
57053 en TOKEN_NEUTRALIZED
57052 de TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
