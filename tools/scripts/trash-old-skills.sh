#!/usr/bin/env bash
# Trash les 55 dossiers skills sources (copies dans leurs sous-dossiers categorie)
# Lancer APRES avoir ferme VS Code : bash tools/scripts/trash-old-skills.sh

PJ="D:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/skills"

dirs=(
  agent-constitution
  ai-playbook-schoolswp
  audit
  brain-lite
  branding
  clairtexte
  claude-project-setup
  consolidation-ops
  content-factory-autonome
  conversational-query-mapper
  credo-engine
  dev-wordpress
  etude-marche-france
  fast-websearch
  finance-freedom-flow
  firecrawl
  formation-pipeline
  geo-gsc-pipeline
  landing-page-factory
  linkedin
  lms-cocon-roi-prioritization
  local-prospecting-pipeline
  marketing
  mcp-builder
  meta-prompt-creator
  money-articles-30-plan
  n8n-reverse-engineer
  n8n-workflow-architect
  niche-detector-reachable
  note-to-sop
  os-claude-system
  os-router
  pact-engine
  performance-loop
  pinterest-pipeline
  plugin-email-sequence
  publish-repo
  race-engine
  reddit
  rewrite-conversion
  schoolswp-article-workflow
  schoolswp-youtube-studio
  seo-audit
  seo-brief-generator
  thumbnail-strategist
  utm-convention
  vscode-agent-visual
  wordpress
  workflow-debug
  workspace-guardian
  workspace-hygiene
  wp-image-metadata-seo
  youtube
  youtube-extractor
  youtube-omnichannel-engine
)

ok=0
fail=0
for d in "${dirs[@]}"; do
  if [ -d "$PJ/$d" ]; then
    trash "$PJ/$d" 2>/dev/null && { echo "OK   $d"; ((ok++)); } || { echo "FAIL $d"; ((fail++)); }
  else
    echo "SKIP $d (deja supprime)"
  fi
done

echo ""
echo "Done: $ok trashed, $fail failed"
