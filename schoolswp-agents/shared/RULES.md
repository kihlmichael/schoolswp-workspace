# RULES.md — Règles transverses schoolsWP

Règles partagées par les 4 agents (`content-studio`, `crm-automation`, `seo-geo`, `social-community`).
Chaque agent charge ce fichier au démarrage **en plus** de son `CLAUDE.md` et `soul.md`.

Source de vérité. Si un fichier agent contredit ce document, ce document prime.

---

## 1. Data safety — suppressions

- **Interdit** : `rm`, `rm -rf`, `sudo`, toute commande destructrice.
- **Obligatoire** : `trash <chemin>` pour toute suppression (fichier ou dossier).
- Ne jamais vider la corbeille automatiquement.
- Ne jamais écraser un fichier existant sans confirmation explicite.

## 2. Périmètre des modifications

- **Interdit de modifier `../shared/`** sans demander. C'est la source de vérité partagée.
- **Interdit de modifier le projet parent** (`D:\VS Code\CLAUDE CODE\projects\schoolswp\`) sans demander — uniquement lecture pour contexte.
- Chaque agent écrit dans son propre dossier (`<agent>/output/`, `<agent>/memory/`).
- Les crons communs sont dans `shared/cron_registry.json` — lecture seule, modification collective uniquement.

## 3. Branding schoolsWP

- **Toujours** : `schoolsWP` (capitalisation exacte). Jamais `schoolswp`, `SchoolsWP`, `School'sWP`.
- **Tutoiement systématique**. Jamais vouvoyer.
- **Langue** : français par défaut. Anglais uniquement si explicitement demandé.
- Mots interdits : voir `shared/skills/schoolswp-voice.md` et `BRAND_RULES.md` du projet parent.

## 4. Communication

- Réponses concises. Telegram n'est pas un blog.
- Pour tout contenu > 500 mots : sauvegarder dans `output/` et envoyer le chemin.
- Emoji reactions pour les accusés de réception courts.
- Confirmer le brief avant de produire un livrable long (article, landing, séquence).

## 5. Sécurité

- **Jamais de credentials** (clés API, tokens, mots de passe) dans les logs, les commits, ou les messages Telegram.
- `.env` et `.mcp.json` sont dans `.gitignore` — ne jamais les versionner.
- Credentials n8n à sanitiser avant tout export.
- Vérifier `.gitignore` avant `git add`.
- Ne jamais exécuter d'action destructrice sur schoolswp.com en production (suppression de pages, désactivation de plugins, modification DB) sans validation humaine explicite.

## 6. Interaction avec schoolswp.com (MCP novamira)

- **Lecture** (discover abilities, list plugins, read posts, get options) : libre.
- **Écriture** (create/update/delete post, modifier option, activer plugin) : **confirmation humaine obligatoire** avant chaque action.
- Jamais de `delete` sans double confirmation (message + intent explicite).
- Logger toute action d'écriture dans `memory/daily-logs/YYYY-MM-DD.md`.

## 7. Mémoire et logs

- Daily log obligatoire : `memory/daily-logs/YYYY-MM-DD.md`.
- Format : `## YYYY-MM-DD\n- Fait\n- Décisions\n- À suivre`.
- Mettre à jour `memory/memory.md` si nouvelle info stratégique (décision, pivot, contrainte).
- Ne jamais réécrire l'historique d'un daily log — append uniquement.

## 8. Agents Python du projet parent

Lancés depuis `D:\VS Code\CLAUDE CODE\projects\schoolswp\` :

```bash
.venv/Scripts/python -m agents.<module>.cli [args]
```

- Ne pas activer le venv (Windows + Bash non persistant) — chemin complet.
- Lint obligatoire après modification de `.py` : `ruff check`.

## 9. Escalade

En cas de doute sur une action (réversibilité, impact, périmètre) :

1. Ne pas exécuter.
2. Décrire l'action envisagée à l'humain.
3. Attendre confirmation explicite.

---

**Dernière mise à jour** : 2026-04-17
