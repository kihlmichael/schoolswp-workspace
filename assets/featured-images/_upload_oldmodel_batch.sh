#!/usr/bin/env bash
# Upload the 11 legacy-replacement hero PNGs via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

ROWS="
1946756 en TOKEN_NEUTRALIZED
50326 fr TOKEN_NEUTRALIZED
2865114 en TOKEN_NEUTRALIZED
2592793 fr TOKEN_NEUTRALIZED
2888497 de TOKEN_NEUTRALIZED
1136071 de TOKEN_NEUTRALIZED
1944479 en TOKEN_NEUTRALIZED
1944485 de TOKEN_NEUTRALIZED
1351611 de TOKEN_NEUTRALIZED
56041 en TOKEN_NEUTRALIZED
56040 de TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
