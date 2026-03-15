# Politique de rotation des clés API — schoolsWP

Dernière révision : 2026-03-15

---

## Inventaire des services et fréquences de rotation

| Service | Fichier source | Fréquence | Prochain audit |
|---------|---------------|-----------|----------------|
| Anthropic API | `agents/.env` | 90 jours | 2026-06-13 |
| Firecrawl | `agents/.env` | 90 jours | 2026-06-13 |
| n8n API (JWT) | `.mcp.json` | 90 jours | 2026-06-13 |
| RapidAPI (LinkedIn/Twitter/Instagram/YouTube) | `.mcp.json` | 90 jours | 2026-06-13 |
| DataForSEO | `systems/n8n/.env` | 90 jours | 2026-06-13 |
| OpenAI | `systems/n8n/.env` | 90 jours | 2026-06-13 |
| HeyGen | `apps/elearning/elearning/.env` | 180 jours | 2026-09-11 |
| ElevenLabs | `apps/elearning/elearning/.env` | 180 jours | 2026-09-11 |
| Telegram Bot (prod) | `apps/telegram-bot/telegram-bot/.env` | 180 jours | 2026-09-11 |
| Telegram Bot (poc) | `apps/claude-telegram-poc/.env` | 180 jours | 2026-09-11 |
| Discord Webhook | `systems/n8n/.env` | 180 jours | 2026-09-11 |
| Google OAuth (refresh_token) | `.claude/skills/googledrive/scripts/token.json` | À la révocation | Sur incident |
| Thruuu API | `systems/multi-agent-system/multi-agent-system/.env` | 90 jours | 2026-06-13 |

---

## Procédure de rotation standard (pas d'incident)

1. Générer la nouvelle clé sur le dashboard du service
2. Mettre à jour la valeur dans le fichier `.env` correspondant (ou `.mcp.json`)
3. Tester que les agents/workflows fonctionnent avec la nouvelle clé
4. Révoquer l'ancienne clé sur le dashboard du service
5. Mettre à jour la date "Prochain audit" dans ce fichier

---

## Procédure en cas d'incident (leak suspecté)

1. **Révoquer immédiatement** la clé compromise sur le dashboard du service
2. Vérifier les logs d'utilisation du service pour détecter des accès non autorisés
3. Générer une nouvelle clé et la déployer
4. Si la clé était dans git : contacter GitHub Support pour purge (même si le repo est privé)
5. Documenter l'incident dans `systems/security/incidents/YYYY-MM-DD-nom-service.md`

---

## Règles clés RapidAPI (séparation des scopes)

Actuellement, une seule clé RapidAPI couvre 4 services (LinkedIn, Twitter, Instagram, YouTube).

**Risque** : si la clé leak, les 4 services sont compromis simultanément.

**Action recommandée** : à la prochaine rotation, créer une clé dédiée par service si l'offre RapidAPI le permet.

---

## Contrôles automatiques en place

- **Pre-commit hook** (`.git/hooks/pre-commit`) : bloque tout commit contenant des patterns de secrets connus
- **`.gitignore` fortress** : tous les fichiers `.env`, `.mcp.json`, `*token*.json`, `*credentials*.json` sont exclus du versioning
- **Scan ponctuel** : lancer `grep -rE "(sk-ant|sk-|fc-|eyJhbGci|AKIA|ya29\.)" . --include="*.json" --include="*.py" --include="*.js"` pour vérifier le repo

---

## Contacts et escalade

- Propriétaire : Michael KIHL — contact@michaelkihl.fr
- En cas de compromission grave : changer toutes les clés listées ci-dessus en priorité
