#!/usr/bin/env bash
# Upload the 17 draft hero PNGs via Novamira signed upload tokens.
set -u
URL="https://schoolswp.com/wp-json/novamira/v1/upload"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

ROWS="
2969994 fr TOKEN_NEUTRALIZED
2969990 fr TOKEN_NEUTRALIZED
2969989 fr TOKEN_NEUTRALIZED
2969501 fr TOKEN_NEUTRALIZED
2969375 fr TOKEN_NEUTRALIZED
2968090 en TOKEN_NEUTRALIZED
2967212 fr TOKEN_NEUTRALIZED
2967654 fr TOKEN_NEUTRALIZED
2967240 fr TOKEN_NEUTRALIZED
2592792 fr TOKEN_NEUTRALIZED
2592797 fr TOKEN_NEUTRALIZED
2592796 fr TOKEN_NEUTRALIZED
2289922 fr TOKEN_NEUTRALIZED
2538716 fr TOKEN_NEUTRALIZED
2289944 fr TOKEN_NEUTRALIZED
2289936 fr TOKEN_NEUTRALIZED
2289935 fr TOKEN_NEUTRALIZED
"

echo "$ROWS" | while read -r id lang token; do
  [ -z "$id" ] && continue
  f="post-${id}/slide-00-hero-${lang}.png"
  printf '=== %s-%s : ' "$id" "$lang"
  curl -s -A "$UA" -H "X-Novamira-Upload-Token: ${token}" -F "file=@${f}" "$URL"
  printf '\n'
done
