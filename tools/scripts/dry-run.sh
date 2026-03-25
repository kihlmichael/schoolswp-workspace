#!/usr/bin/env bash
# ══════════════════════════════════════════════════════
#  schoolsWP — Dry Run : déclenche le workflow d'audit
#  avec données mock, sans consommer les APIs externes
#
#  Usage : bash tools/scripts/dry-run.sh [--force]
#  Prérequis : n8n démarré (docker compose up -d)
# ══════════════════════════════════════════════════════

set -euo pipefail

N8N_HOST="${N8N_HOST:-http://localhost:5678}"
N8N_USER="${N8N_USER:-admin}"
N8N_PASS="${N8N_PASS:-changeme_strong_password}"

WORKFLOW_PATTERN="schoolsWP — Audit SEO Mensuel"
FORCE="${1:-}"

echo "═══════════════════════════════════════════════"
echo "  schoolsWP — Dry Run Audit Workflow"
echo "  Host : $N8N_HOST"
echo "═══════════════════════════════════════════════"

# ── Vérifier que n8n est accessible ──────────────────
echo ""
echo "→ Vérification de la connectivité n8n..."
if ! curl -sf -u "$N8N_USER:$N8N_PASS" "$N8N_HOST/healthz" > /dev/null 2>&1; then
  echo "✗ n8n inaccessible sur $N8N_HOST"
  echo "  Vérifier : docker compose -f systems/systems/n8n/docker-compose.yml ps"
  exit 1
fi
echo "✓ n8n opérationnel"

# ── Récupérer l'ID du workflow ────────────────────────
echo ""
echo "→ Recherche du workflow \"$WORKFLOW_PATTERN\"..."

WORKFLOW_JSON=$(curl -sf -u "$N8N_USER:$N8N_PASS" \
  "$N8N_HOST/api/v1/workflows?limit=50" 2>/dev/null || echo '{"data":[]}')

WORKFLOW_ID=$(echo "$WORKFLOW_JSON" | \
  node -e "
    const d = JSON.parse(require('fs').readFileSync('/dev/stdin','utf8'));
    const wf = (d.data || []).find(w => w.name.includes('Audit SEO Mensuel'));
    if (wf) console.log(wf.id); else process.exit(1);
  " 2>/dev/null || echo "")

if [ -z "$WORKFLOW_ID" ]; then
  echo "✗ Workflow introuvable."
  echo "  Importer d'abord : systems/systems/n8n/systems/workflows/workflows/audit-monthly.json"
  echo "  Via UI : Settings → Import from file"
  echo "  Via CLI : n8n import:workflow --input=systems/systems/n8n/systems/workflows/workflows/audit-monthly.json"
  exit 1
fi
echo "✓ Workflow ID : $WORKFLOW_ID"

# ── Activer le workflow si nécessaire ─────────────────
echo ""
echo "→ Activation du workflow..."
curl -sf -u "$N8N_USER:$N8N_PASS" \
  -X PATCH "$N8N_HOST/api/v1/systems/workflows/workflows/$WORKFLOW_ID" \
  -H "Content-Type: application/json" \
  -d '{"active": true}' > /dev/null 2>&1 && echo "✓ Workflow actif" || echo "⚠ Impossible d'activer (déjà actif?)"

# ── Préparer les variables ────────────────────────────
FORCE_RERUN="false"
if [ "$FORCE" = "--force" ]; then
  FORCE_RERUN="true"
  echo ""
  echo "⚡ Mode FORCE : rapport existant écrasé si présent"
fi

# ── Déclencher via le Manual Trigger ────────────────
echo ""
echo "→ Déclenchement du workflow (mode manual + dry-run)..."
echo "  DATAFORSEO_DRY_RUN = true"
echo "  FORCE_RERUN        = $FORCE_RERUN"

EXEC_RESPONSE=$(curl -sf -u "$N8N_USER:$N8N_PASS" \
  -X POST "$N8N_HOST/api/v1/systems/workflows/workflows/$WORKFLOW_ID/execute" \
  -H "Content-Type: application/json" \
  -d "{\"data\": {\"_forceRun\": true, \"_dryRun\": true}}" 2>/dev/null || echo '{}')

EXEC_ID=$(echo "$EXEC_RESPONSE" | \
  node -e "
    const d = JSON.parse(require('fs').readFileSync('/dev/stdin','utf8'));
    console.log(d.data?.executionId || d.executionId || '');
  " 2>/dev/null || echo "")

if [ -z "$EXEC_ID" ]; then
  echo "✗ Impossible de récupérer l'ID d'exécution."
  echo "  Réponse brute : $EXEC_RESPONSE"
  echo "  → Déclencher manuellement via l'UI : $N8N_HOST"
  exit 1
fi

echo "✓ Exécution démarrée : $EXEC_ID"
echo ""
echo "═══════════════════════════════════════════════"
echo "  Suivi : $N8N_HOST/executions/$EXEC_ID"
echo "  PDF   : ./data/artifacts/audit-YYYY-MM.pdf"
echo "  Logs  : docker logs schoolswp-n8n --tail 50"
echo "═══════════════════════════════════════════════"

# ── Attendre la fin et afficher le statut ─────────────
echo ""
echo "→ Attente de la fin d'exécution (max 120s)..."
for i in $(seq 1 24); do
  sleep 5
  STATUS=$(curl -sf -u "$N8N_USER:$N8N_PASS" \
    "$N8N_HOST/api/v1/executions/$EXEC_ID" 2>/dev/null | \
    node -e "
      const d = JSON.parse(require('fs').readFileSync('/dev/stdin','utf8'));
      console.log(d.data?.status || d.status || 'unknown');
    " 2>/dev/null || echo "unknown")

  echo "  [$((i*5))s] Status : $STATUS"
  if [ "$STATUS" = "success" ]; then
    echo ""
    echo "✅ Dry run réussi !"
    echo "   PDF généré dans : ./artifacts/"
    exit 0
  elif [ "$STATUS" = "error" ] || [ "$STATUS" = "crashed" ]; then
    echo ""
    echo "✗ Exécution échouée ($STATUS)"
    echo "  Voir les logs : $N8N_HOST/executions/$EXEC_ID"
    exit 1
  fi
done

echo ""
echo "⚠ Timeout — vérifier manuellement : $N8N_HOST/executions/$EXEC_ID"
