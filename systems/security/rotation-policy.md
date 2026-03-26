# Politique de rotation des clés API — schoolsWP OS

**Date** : 2026-03-15
**Responsable** : Michael KIHL

---

## Calendrier de rotation

| Service | Fréquence | Prochaine rotation | Procédure |
|---------|----------|-------------------|----------|
| `ANTHROPIC_API_KEY` | 90 jours | 2026-06-15 | Dashboard Anthropic → API Keys |
| `OPENAI_API_KEY` | 90 jours | 2026-06-15 | Dashboard OpenAI → API Keys |
| Thruuu JWT | 30 jours | 2026-04-15 | app.thruuu.com → Profile → Token |
| `WEBHOOK_SECRET` (n8n) | 180 jours | 2026-09-15 | n8n Variables → WEBHOOK_SECRET |
| `N8N_ENCRYPTION_KEY` | Jamais (sauf compromission) | — | Procédure spéciale ci-dessous |
| Google OAuth tokens | Auto-refresh | — | Géré par n8n automatiquement |
| RapidAPI key | 180 jours | 2026-09-15 | rapidapi.com → Apps → Keys |
| Notion API key | 180 jours | 2026-09-15 | notion.so → Settings → Integrations |
| Airtable API key | 180 jours | 2026-09-15 | airtable.com → Account → API |

---

## Procédure standard (90/180 jours)

1. Générer nouvelle clé sur le dashboard du service
2. Mettre à jour `agents/.env` (variables locales)
3. Mettre à jour n8n Variables ou Credentials selon le service
4. Tester le workflow concerné
5. Révoquer l'ancienne clé
6. Mettre à jour la date dans ce fichier

---

## Procédure urgence (compromission détectée)

1. **Révoquer immédiatement** la clé compromise sur le dashboard
2. Générer nouvelle clé
3. Mettre à jour tous les endroits où la clé est utilisée (`.env`, n8n, scripts)
4. Auditer les logs n8n pour détecter un usage anormal
5. Si données personnelles exposées : notifier CNIL sous 72h (Art. 33 RGPD)
6. Documenter l'incident dans `systems/security/incidents/YYYY-MM-DD-nom.md`

---

## Scan anti-secrets (pré-commit)

Le hook pre-commit détecte 12 patterns :

```bash
# Vérification manuelle :
git diff --cached | grep -iE '(api[_-]?key|secret|token|password|bearer|jwt|oauth|credential)\s*[=:]\s*["\x27]?[A-Za-z0-9+/]{20,}'
```

---

## Procédure rotation N8N_ENCRYPTION_KEY

> ⚠️ **CRITIQUE** — Ne faire qu'en cas de compromission avérée.

1. Exporter tous les credentials n8n (Settings → Export)
2. Arrêter n8n
3. Générer nouvelle clé : `openssl rand -hex 32`
4. Mettre à jour `N8N_ENCRYPTION_KEY` dans `systems/n8n/.env`
5. Redémarrer n8n
6. Reconfigurer manuellement tous les credentials (ils sont chiffrés avec l'ancienne clé)
7. Tester tous les workflows
