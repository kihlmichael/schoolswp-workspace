#!/usr/bin/env bash
# Upload the 20 hosting-batch hero PNGs via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

ROWS="
2289949 fr TOKEN_NEUTRALIZED
2289791 fr TOKEN_NEUTRALIZED
59494 fr TOKEN_NEUTRALIZED
59551 en TOKEN_NEUTRALIZED
59570 de TOKEN_NEUTRALIZED
59256 fr TOKEN_NEUTRALIZED
59434 en TOKEN_NEUTRALIZED
59420 de TOKEN_NEUTRALIZED
57810 fr TOKEN_NEUTRALIZED
58610 en TOKEN_NEUTRALIZED
58598 de TOKEN_NEUTRALIZED
53666 fr TOKEN_NEUTRALIZED
53811 en TOKEN_NEUTRALIZED
53810 de TOKEN_NEUTRALIZED
4854 fr TOKEN_NEUTRALIZED
739366 en TOKEN_NEUTRALIZED
739385 de TOKEN_NEUTRALIZED
53488 fr TOKEN_NEUTRALIZED
722922 en TOKEN_NEUTRALIZED
739173 de TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
