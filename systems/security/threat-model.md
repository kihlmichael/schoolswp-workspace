# Threat Model — schoolsWP OS

**Méthode** : STRIDE
**Date** : 2026-03-15
**Scope** : Agents Python, n8n, services tiers, infrastructure
**Auteur** : Michael KIHL — contact@michaelkihl.fr

---

## 1. Architecture & Trust Boundaries

```
[Local Machine] ──HTTPS──► [Anthropic / OpenAI]
     │
     ├── .env (Tier 1 secrets)
     ├── .mcp.json (n8n MCP)
     └── CLI Python agents (brain.bat, brain-lite.bat)
              │
              └──HTTPS──► [n8n Hosted: schoolswp-n8n.wp1.host]
                               │
                               ├── Google Sheets (OAuth2)  ← IDEAS trigger
                               ├── Google Docs (OAuth2)    ← article output
                               ├── Google Search Console (OAuth2)
                               ├── Notion (API key)
                               ├── Airtable (API key)
                               ├── DataForSEO (Basic Auth)
                               ├── Thruuu (JWT Bearer)
                               ├── Firecrawl (API key)
                               ├── Discord / Slack (webhook URL)
                               ├── Telegram Bot (token)
                               └── HeyGen / ElevenLabs (API keys)
```

**Frontières de confiance :**

| Boundary | Trust Level | Notes |
|----------|-------------|-------|
| Local machine | FULL | Utilisateur unique (Michael), Windows NTFS |
| n8n hosted | HIGH | Instance propriétaire, TLS, Basic Auth |
| Anthropic/OpenAI | HIGH | Providers tier 1, SLA robuste |
| Google APIs (OAuth2) | MEDIUM | Scope limité par les tokens |
| Tiers (Notion, Airtable, Thruuu...) | MEDIUM | SLA variable, API key sans expiry |
| PostgreSQL (n8n DB) | HIGH | Accès interne n8n uniquement |

---

## 2. Assets Critiques

| Tier | Asset | Localisation | Impact si compromis |
|------|-------|-------------|---------------------|
| **1** | `ANTHROPIC_API_KEY` | `agents/.env` | Accès illimité aux modèles Claude |
| **1** | `N8N_ENCRYPTION_KEY` | `systems/n8n/.env` | Déchiffrement de TOUS les credentials n8n |
| **1** | `GOOGLE_OAUTH_TOKENS` | `.claude/skills/googledrive/` | Accès Sheets, Docs, GSC, Gmail |
| **1** | Secrets webhook | n8n Variables | Bypass auth webhooks |
| **2** | Articles & stratégie SEO | Google Docs / GSheets | Propriété intellectuelle |
| **2** | KPI & métriques | Notion / Airtable | Intelligence business |
| **2** | Token Thruuu (JWT) | n8n Variables / 09_CONFIG | Accès API monitoring contenu |
| **3** | Workflow JSON exports | `systems/workflows/` | Logique automation (sans secrets) |

---

## 3. Analyse STRIDE

### S — Spoofing (Usurpation d'identité)

| ID | Menace | Vecteur | Probabilité | Impact | Mitigation | Statut |
|----|--------|---------|------------|--------|-----------|--------|
| S1 | Webhook spoofing | POST sans header `x-webhook-secret` | FAIBLE | MOYEN | Validate Secret (Code node) sur 3 webhooks | ✅ MITIGÉ |
| S2 | Spoofing Google Sheets trigger | Faux OAuth token | TRÈS FAIBLE | FAIBLE | OAuth2 géré par n8n | ✅ OK |
| S3 | Usurpation API key Anthropic | Keylogger ou vol .env | TRÈS FAIBLE | CRITIQUE | .gitignore + pre-commit hook | ✅ MITIGÉ |

---

### T — Tampering (Altération)

| ID | Menace | Vecteur | Probabilité | Impact | Mitigation | Statut |
|----|--------|---------|------------|--------|-----------|--------|
| T1 | Injection via Google Sheets IDEAS | Cellule malveillante dans le sheet | FAIBLE | MOYEN | Validation input dans Code node du Content Machine | ⚠️ PARTIEL |
| T2 | Modification workflow JSON | Accès repo git ou n8n UI | TRÈS FAIBLE | ÉLEVÉ | Pas de secrets dans les JSON exportés | ✅ MITIGÉ |
| T3 | Tampering fichier article markdown | Path traversal CLI (avant fix) | TRÈS FAIBLE | FAIBLE | `safe_read_path()` / `safe_write_path()` ajoutés | ✅ MITIGÉ |
| T4 | Prompt injection LLM (keyword/content) | Input CLI malformé | TRÈS FAIBLE | FAIBLE | CLI local, utilisateur de confiance | ⚠️ RISQUE ACCEPTÉ |

---

### R — Repudiation (Répudiation)

| ID | Menace | Vecteur | Probabilité | Impact | Mitigation | Statut |
|----|--------|---------|------------|--------|-----------|--------|
| R1 | Pas de log d'audit centralisé | Actions non tracées | FAIBLE | FAIBLE | n8n execution history (PostgreSQL) | ⚠️ PARTIEL |
| R2 | Exécutions n8n purgées | Rétention courte | FAIBLE | TRÈS FAIBLE | Configurer rétention ≥ 30 jours | ⚠️ À VÉRIFIER |

---

### I — Information Disclosure (Divulgation d'informations)

| ID | Menace | Vecteur | Probabilité | Impact | Mitigation | Statut |
|----|--------|---------|------------|--------|-----------|--------|
| I1 | `N8N_ENCRYPTION_KEY` volé → tous les credentials déchiffrés | Accès au serveur n8n | TRÈS FAIBLE | CRITIQUE | Accès serveur restreint, TLS | ⚠️ RÉSIDUEL |
| I2 | Tokens OAuth dans les logs d'exécution n8n | Logs accessibles via UI n8n | FAIBLE | MOYEN | Limiter `saveDataSuccessExecution` dans les workflows sensibles | ⚠️ À FAIRE |
| I3 | Clés API dans les commentaires workflow | Review JSON exports | TRÈS FAIBLE | ÉLEVÉ | Pre-commit hook, review manuelle | ✅ MITIGÉ |
| I4 | `.env` lisible localement | Accès machine physique | TRÈS FAIBLE | CRITIQUE | Machine personnelle, chiffrement disque recommandé | ⚠️ RÉSIDUEL |
| I5 | Thruuu JWT expiré mais lisible dans les logs | Log output pipeline | TRÈS FAIBLE | FAIBLE | JWT supprimé du code — lu depuis 09_CONFIG sheet | ✅ MITIGÉ |

---

### D — Denial of Service

| ID | Menace | Vecteur | Probabilité | Impact | Mitigation | Statut |
|----|--------|---------|------------|--------|-----------|--------|
| D1 | Webhook flooding | Attaquant connaît l'URL webhook | FAIBLE | MOYEN | Rate limiting reverse proxy (Nginx/Cloudflare) | ⚠️ À FAIRE |
| D2 | Boucle agent infinie → burn quota Anthropic | Bug dans orchestration multi-agent | FAIBLE | ÉLEVÉ | `max_tokens` limité par agent ; pas de récursion infinie détectée | ⚠️ RÉSIDUEL |
| D3 | Google Sheets trigger — polling chaque minute | 100+ lignes IDEAS → n8n overload | TRÈS FAIBLE | MOYEN | Poll toutes les minutes, lot unique | ⚠️ RÉSIDUEL |
| D4 | Quota Anthropic épuisé | Usage légitime intense (brain.bat loop) | FAIBLE | MOYEN | Pas de retry infini détecté dans les agents | ✅ OK |

---

### E — Elevation of Privilege (Élévation de privilège)

| ID | Menace | Vecteur | Probabilité | Impact | Mitigation | Statut |
|----|--------|---------|------------|--------|-----------|--------|
| E1 | Accès direct PostgreSQL n8n → credentials déchiffrés | Fuite `N8N_ENCRYPTION_KEY` + accès DB | TRÈS FAIBLE | CRITIQUE | Accès DB interne uniquement | ✅ OK |
| E2 | Code node n8n lit `$env` non prévu | Node malveillant injecté | TRÈS FAIBLE | MOYEN | Pas d'exécuteurs tiers, UI accès restreint | ✅ OK |
| E3 | `sudo` ou droits élevés depuis CLI Python | `subprocess` (inexistant) | AUCUNE | — | Aucun `subprocess` / `os.system` dans les agents | ✅ OK |

---

## 4. Risques résiduels acceptés

| ID | Risque | Justification |
|----|--------|---------------|
| T4 | Prompt injection LLM via CLI | CLI local, utilisateur unique de confiance — sanitization casserait la flexibilité |
| I4 | `.env` lisible en local | Machine personnelle protégée ; chiffrement disque Windows BitLocker recommandé |
| D2 | Boucle agent → quota burn | Pas de récursion détectée ; risque faible opérationnellement |
| I1 | `N8N_ENCRYPTION_KEY` critique | Mitigation principale = sécurité serveur n8n hébergé (wp1.host) |

---

## 5. Plan d'actions (par priorité)

### Priorité HAUTE

| Action | ID(s) | Statut |
|--------|-------|--------|
| Rate limiting webhooks via Nginx/Cloudflare devant n8n | D1 | ⏳ Manuel — config serveur |
| Chiffrement disque BitLocker activé sur machine Windows | I4 | ⏳ Manuel — OS setting |

### Priorité MOYENNE

| Action | ID(s) | Statut |
|--------|-------|--------|
| Limiter `saveDataSuccessExecution: 'none'` dans workflows sensibles | I2 | ⏳ n8n Settings |
| Validation input Google Sheets IDEAS (Content Machine) | T1 | ⏳ Code node |
| Vérifier rétention logs n8n (≥ 30 jours recommandé) | R2 | ⏳ n8n Settings |

### Priorité BASSE

| Action | ID(s) | Statut |
|--------|-------|--------|
| Documenter procédure récupération `N8N_ENCRYPTION_KEY` | I1, E1 | ✅ rotation-policy.md |
| Activer alertes quota Anthropic (seuil 80%) | D4 | ⏳ Dashboard Anthropic |

---

## 6. Contrôles déjà en place

| Contrôle | Scope | Vérifié |
|----------|-------|---------|
| Pre-commit hook (12 patterns secrets) | Git commits | ✅ |
| `.gitignore` fortress (tous les `.env`, `.mcp.json`, tokens) | Versioning | ✅ |
| Webhook auth via `x-webhook-secret` (3 webhooks) | n8n | ✅ |
| `safe_read_path()` / `safe_write_path()` | CLI Python | ✅ |
| Validation `--context` max 500 chars | CLI Python | ✅ |
| `logging.warning()` sur exceptions silencieuses | Pipeline Python | ✅ |
| JWT Thruuu supprimé du code — lu depuis Google Sheets | n8n workflow | ✅ |
| Placeholders Bearer → `$env.*` dans workflows locaux | JSON exports | ✅ |
| Politique de rotation des clés (90j / 180j) | Tous services | ✅ |
| GPG encryption optionnelle pour backup n8n | backup-n8n.sh | ✅ |

---

## 7. Références

- `systems/security/rotation-policy.md` — Politique de rotation des clés
- `systems/n8n/CLAUDE.md` — Patterns auth webhooks + Variables n8n
- `.git/hooks/pre-commit` — Hook anti-secrets
- OWASP Top 10 2021 — A01 (Broken Access Control), A02 (Crypto Failures)
- STRIDE methodology — Microsoft SDL
