#!/usr/bin/env bash
# Upload the 13 freelance/marketplace/misc/portraits hero PNGs via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

ROWS="
2506216 fr TOKEN_NEUTRALIZED
2888491 en TOKEN_NEUTRALIZED
1599511 fr TOKEN_NEUTRALIZED
1946752 en TOKEN_NEUTRALIZED
48485 fr TOKEN_NEUTRALIZED
48487 fr TOKEN_NEUTRALIZED
46119 fr TOKEN_NEUTRALIZED
45812 fr TOKEN_NEUTRALIZED
45640 fr TOKEN_NEUTRALIZED
4821 fr TOKEN_NEUTRALIZED
4530 fr TOKEN_NEUTRALIZED
3554 fr TOKEN_NEUTRALIZED
927 fr TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
