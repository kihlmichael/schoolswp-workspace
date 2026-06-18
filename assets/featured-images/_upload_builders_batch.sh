#!/usr/bin/env bash
# Upload the 24 builder-batch hero PNGs to schoolswp.com via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# id lang token
ROWS="
2289921 fr TOKEN_NEUTRALIZED
57155 fr TOKEN_NEUTRALIZED
57235 en TOKEN_NEUTRALIZED
57236 de TOKEN_NEUTRALIZED
55007 fr TOKEN_NEUTRALIZED
55420 en TOKEN_NEUTRALIZED
55419 de TOKEN_NEUTRALIZED
53976 fr TOKEN_NEUTRALIZED
679464 en TOKEN_NEUTRALIZED
679476 de TOKEN_NEUTRALIZED
50952 fr TOKEN_NEUTRALIZED
97482 en TOKEN_NEUTRALIZED
46176 fr TOKEN_NEUTRALIZED
44121 fr TOKEN_NEUTRALIZED
58540 en TOKEN_NEUTRALIZED
58545 de TOKEN_NEUTRALIZED
7862 fr TOKEN_NEUTRALIZED
6184 fr TOKEN_NEUTRALIZED
2471 fr TOKEN_NEUTRALIZED
3087 fr TOKEN_NEUTRALIZED
898 fr TOKEN_NEUTRALIZED
53915 fr TOKEN_NEUTRALIZED
58089 en TOKEN_NEUTRALIZED
58095 de TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
