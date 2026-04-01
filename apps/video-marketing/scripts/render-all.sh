#!/bin/bash
# Render all Remotion compositions to out/
# Usage: bash scripts/render-all.sh

set -e

COMPOSITIONS=(
  "BrandIntro"
)

echo "=== Remotion Batch Render ==="
echo "Compositions: ${#COMPOSITIONS[@]}"
echo ""

for comp in "${COMPOSITIONS[@]}"; do
  slug=$(echo "$comp" | sed 's/\([A-Z]\)/-\L\1/g' | sed 's/^-//')
  echo "Rendering $comp -> out/$slug.mp4"
  npx remotion render "$comp" "out/$slug.mp4" --overwrite
  echo "Done: $comp"
  echo ""
done

echo "=== All renders complete ==="
ls -lh out/*.mp4
