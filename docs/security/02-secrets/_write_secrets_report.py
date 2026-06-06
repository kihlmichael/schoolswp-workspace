"""Generate the secrets inventory report."""
import json
import os
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "04-secrets-inventory.md"

parts = []

parts.append("# Etape 4 - Inventaire secrets multi-niveaux\n\n")
parts.append("> Audit lecture seule. Date : 2026-05-12.\n")
parts.append("> Methode : scanner Python custom (equivalent gitleaks, 30 patterns) sur 8 repos Git + on-disk scan + croisement avec etape 1.\n")
parts.append("> Aucune valeur secrete dans ce rapport (4 derniers chars max si necessaire).\n\n")
parts.append("---\n\n")

parts.append("## Resume executif\n\n")
parts.append("**29 secrets reels detectes au total**, repartis sur 4 niveaux de stockage :\n\n")
parts.append("| Classification | Count | Action |\n|---|---|---|\n")
parts.append("| LEAKED PUBLIC | 0 | (les 3 repos kihlmichael sont prives, verifie via gh) |\n")
parts.append("| LEAKED PRIVATE (Git history) | 10 | Rotation par precaution (acces a l historique = compromission) |\n")
parts.append("| AT REST UNENCRYPTED (sur disque) | 18+ | Migration vault prioritaire (etape briefing 7-8) |\n")
parts.append("| PROPER (vault ou chiffre) | ~1Password (a confirmer) | Continuer |\n\n")

parts.append("**Bonne nouvelle** : aucun secret dans un repo public que tu controles. Les 3 repos kihlmichael (schoolswp, schoolswp-telegram-agents, michaelkihl-fr) sont tous prives.\n\n")
parts.append("**Mauvaise nouvelle** : 10 secrets sont dans l historique Git du repo principal schoolswp. Si quelqu un a un fork local (anciens claude-code clones, machines secondaires), il peut les voir. **Rotation par precaution recommandee.**\n\n")
parts.append("**Trois priorites immediates** :\n\n")
parts.append("1. Rotater les 2 cles Gemini (...yW1E et ...RUX0) presentes dans 4 fichiers de l historique schoolswp.\n")
parts.append("2. Rotater le jwt n8n (...rcGY) dans `multi-agent-system/workflows/geo-architect-bulk-fill.json` (egalement note etape 3).\n")
parts.append("3. Investiguer le `.mcp.json` actuel qui contient un jwt_token en clair (...fCmA) au lieu d une substitution ${VAR}.\n\n")

parts.append("---\n\n## 1. Surface scannee\n\n")
parts.append("### Repos Git\n\n")
parts.append("| Repo | Type | Remote | Commits | Findings |\n|---|---|---|---|---|\n")
parts.append("| `projects/schoolswp` | private | github.com/kihlmichael/schoolswp | 157 | **10** |\n")
parts.append("| `projects/schoolswp/agents/telegram-claude` | private | kihlmichael/schoolswp-telegram-agents | 16 | 0 (CLEAN) |\n")
parts.append("| `projects/michaelkihl-fr` | private | kihlmichael/michaelkihl-fr | 4 | 0 (CLEAN) |\n")
parts.append("| `tools/ultimate-scraper` | local-only | (no remote) | 0 | (init non commited) |\n")
parts.append("| `novamira` | fork | use-novamira/novamira | 80 | 0 (CLEAN) |\n")
parts.append("| `thruuu-claude-content-strategist` | fork | thruuu/... | 6 | 0 (CLEAN) |\n")
parts.append("| `projects/brightbean-studio` | fork | brightbeanxyz/... | 297 | 7 (URL postgres user:pass, fixture de fork) |\n")
parts.append("| `projects/claude-mem` | fork | thedotmack/... | 2957 | 2 (sanitizer test fixtures) |\n\n")
parts.append("Total commits scannes : 3525. Volume de lignes streame : ~4.2M.\n\n")

parts.append("### On-disk (hors Git)\n\n")
parts.append("- 5 variantes `.mcp.json` (actuel + 4 backups)\n")
parts.append("- 14 fichiers `.env` reels (cf etape 1)\n")
parts.append("- 1 fichier `.credentials/gsc-client-secrets.json`\n")
parts.append("- 1 fichier `.claude/settings.local.json` workspace (85 KB, 18 secrets)\n")
parts.append("- 1 cle SSH privee (telegram_agents_wp1)\n\n")

parts.append("---\n\n## 2. LEAKED PRIVATE - Git history schoolswp (10 findings)\n\n")
parts.append("Repo `projects/schoolswp` est PRIVE sur GitHub, mais les secrets sont dans l historique et peuvent etre vus par :\n\n")
parts.append("- Toute personne avec acces au repo (theoriquement Michael seul, mais a verifier les collaborators GitHub).\n")
parts.append("- Tout clone local existant (machines secondaires, anciens Claude Code workspaces, sauvegardes).\n")
parts.append("- Tout fichier `.pack` Git sauvegarde par WPvivid / WP Umbrella / Backblaze.\n\n")
parts.append("**Table des findings** :\n\n")
parts.append("| # | Type | Commit | Fichier | Last 4 | Verdict |\n|---|---|---|---|---|---|\n")
parts.append("| 1 | gemini_api_key | a4cbc571 | `.nano-banana-config.json` | ...yW1E | Cle Gemini #1, **ROTATER** |\n")
parts.append("| 2 | gemini_api_key | e61d4bcc | `data/setup_gemini_credential.py` | ...RUX0 | Cle Gemini #2, **ROTATER** |\n")
parts.append("| 3 | gemini_api_key | e61d4bcc | `tools/scripts/nas-photo-renamer.py` | ...RUX0 | Duplicate de #2 |\n")
parts.append("| 4 | gemini_api_key | e61d4bcc | `tools/scripts/photo-vacances-organizer.py` | ...RUX0 | Duplicate de #2 |\n")
parts.append("| 5 | password_in_url | e61d4bcc | `systems/multi-agent-system/workflows/content-machine-schoolswp-v2.json` | (URL) | URL avec basic auth user:pass embedded, a verifier |\n")
parts.append("| 6 | password_in_url | 080ef6a9 | `multi-agent-system/workflows/content-machine-schoolswp-v2.json` (ancien path) | (URL) | Duplicate de #5 sur path legacy |\n")
parts.append("| 7 | jwt_token | 080ef6a9 | `multi-agent-system/workflows/geo-architect-bulk-fill.json` | ...rcGY | jwt n8n hardcode, **ROTATER** (deja note etape 3) |\n")
parts.append("| 8 | generic_bearer | 080ef6a9 | `multi-agent-system/workflows/geo-architect-bulk-fill.json` | ...rcGY | Meme jwt formate en Bearer, duplicate de #7 |\n")
parts.append("| 9 | jwt_token | 080ef6a9 | `settings.json` (root) | ...91q4 | **INVESTIGUER** : settings.json a la racine du repo ? probable Claude Code ancien |\n")
parts.append("| 10 | telegram_bot_token | 2b8fe366 | `claude-telegram-poc/README.local.md` | ...xxxx | Probable masque ('xxxx' en hex), **VERIFIER** si reel |\n\n")

parts.append("**Cles Gemini uniques** : 2 distinctes (...yW1E et ...RUX0). Si tu en utilises encore une au moins, rotater les deux et nettoyer.\n\n")

parts.append("**Action immediate** : pour chaque finding :\n\n")
parts.append("1. Identifier le service provider (Gemini Console pour les API keys, n8n UI pour le jwt).\n")
parts.append("2. Generer une nouvelle valeur cote provider.\n")
parts.append("3. Revoke l ancienne valeur.\n")
parts.append("4. Mettre a jour les usages courants (vault + workflow n8n + .env).\n\n")
parts.append("**Nettoyer l historique Git** est theoriquement possible avec `git filter-repo` mais brise les hashes commits. Recommandation : ne PAS reecrire l historique. La rotation suffit (les anciennes valeurs deviennent invalides cote provider).\n\n")

parts.append("---\n\n## 3. AT REST UNENCRYPTED - Disque (hors Git)\n\n")
parts.append("### `.mcp.json` actuel : 1 jwt en clair\n\n")
parts.append("Le scan a trouve un jwt_token en clair (prefix `eyJhbGci...`, last4 ...fCmA) dans `.mcp.json` au lieu d une substitution ${VAR}. C est probablement reste comme \"fallback\" en attendant la migration vault.\n\n")
parts.append("Action : verifier de quel MCP server il s agit, migrer en op:// ou ${VAR}, rotater le secret cote provider.\n\n")

parts.append("### `.mcp.json` backups : tous CLEAN\n\n")
parts.append("Bonne nouvelle : `.mcp.json.bak`, `.mcp.json.fluent`, `.mcp.backup.json`, `.mcp.json.example` utilisent tous le pattern ${VAR} substitution. Pas de secret en clair residuel pre-rotation.\n\n")
parts.append("Note de l etape 1 invalidee : j avais classe `.mcp.json.bak` et `.mcp.backup.json` comme CRITIQUE par prudence. Le scan precis confirme qu ils sont propres. **Peut tout de meme les supprimer pour proprete** (fichiers de 27/28 avril 2026 obsoletes).\n\n")

parts.append("### `apps/_archive/telegram-bot-legacy/.env` : 1 telegram_bot_token\n\n")
parts.append("Fichier dans `_archive/`. Le scan a trouve un telegram_bot_token (last4 ...cfEY). 2 hypotheses :\n\n")
parts.append("- Le token est encore actif cote Telegram (oubli de rotation). **Verifier dans Telegram BotFather**.\n")
parts.append("- Le token a deja ete revoqué quand le bot a ete deprecated. Dans ce cas, le fichier peut etre supprime sans risque.\n\n")

parts.append("### `apps/_archive/elearning/elearning/elearning/.env` : CLEAN\n\n")
parts.append("5 variables mais aucun secret matche les patterns. Probable placeholders ou config de demo. Peut etre supprime apres confirmation.\n\n")

parts.append("### `.env` workspace + 13 autres : 132 variables\n\n")
parts.append("Inventaire detaille dans le rapport de l etape 1 (`01-recon/01-pc-inventory.md` section 3). Resume :\n\n")
parts.append("- **27 vars** dans `.env` racine\n")
parts.append("- **52 vars** dans `systems/n8n/.env` (dont N8N_ENCRYPTION_KEY, N8N_BASIC_AUTH_PASSWORD, DB_POSTGRESDB_PASSWORD, S3_SECRET_KEY)\n")
parts.append("- **17 vars** dans `agents/telegram-claude/.env` (6 Telegram bot tokens)\n")
parts.append("- **13 vars** dans `systems/multi-agent-system/multi-agent-system/.env`\n")
parts.append("- ~17 autres dans 9 .env satellites\n\n")
parts.append("Tous sont AT REST UNENCRYPTED en clair sur disque, lisibles par tout process qui tourne en tant que `conta` ou root. **Mitigations** : migration vault (etape 8 briefing) + NTFS perms restrictives via icacls.\n\n")

parts.append("### `.claude/settings.local.json` workspace : 18 secrets\n\n")
parts.append("85 KB, top-level `env` block. Pattern launcher .mjs valide (cf memory `reference_claude_code_secrets_storage`) mais ces 18 secrets sont AT REST UNENCRYPTED dans le fichier.\n\n")
parts.append("KEYS : APIFY_TOKEN, DATAFORSEO_PASSWORD/USERNAME, DISCORD_BOT_TOKEN, FIRECRAWL_API_KEY, FLUENTCRM_API_*, GEMINI_API_KEY, GITHUB_TOKEN, N8N_API_KEY/URL, RAPIDAPI_KEY, WISEWAND_API_KEY, WP_API_*, ZIPWP_TOKEN.\n\n")

parts.append("### `.credentials/gsc-client-secrets.json`\n\n")
parts.append("OAuth client secret Google Search Console. Gitignored, present sur disque. AT REST UNENCRYPTED mais protege par les credentials OAuth user-level Google.\n\n")

parts.append("### Cle SSH privee `telegram_agents_wp1`\n\n")
parts.append("ED25519 sur disque. Si pas de passphrase = AT REST UNENCRYPTED (a verifier manuellement, cf etape 1 finding #6).\n\n")

parts.append("---\n\n## 4. Runbook rotation prioritaire\n\n")
parts.append("Ordre d execution recommande (du plus critique au moins) :\n\n")
parts.append("### P0 - A faire dans les 48h\n\n")
parts.append("| Ordre | Secret | Localisation | Action | Estimation |\n|---|---|---|---|---|\n")
parts.append("| 1 | jwt_token `.mcp.json` actuel (...fCmA) | `.mcp.json` workspace | Identifier MCP server proprietaire, migrer en op:// ou ${VAR}, rotater | 15 min |\n")
parts.append("| 2 | Gemini API key #1 (...yW1E) | Git history schoolswp `.nano-banana-config.json` | Generate new key in Google AI Studio, revoke old | 5 min |\n")
parts.append("| 3 | Gemini API key #2 (...RUX0) | Git history schoolswp data/setup_gemini_credential.py + 2 autres | Generate new key, revoke old, mettre a jour les 3 fichiers en local (sans rewrite history) | 10 min |\n")
parts.append("| 4 | jwt n8n geo-architect-bulk-fill (...rcGY) | Git history + workflow n8n actif | n8n UI > export workflow > create credential > update node | 15 min |\n")
parts.append("| 5 | jwt settings.json (...91q4) | Git history schoolswp root | Identifier (cookie Claude Code ?), revoke | 10 min |\n")
parts.append("| 6 | Telegram bot token archive (...cfEY) | `apps/_archive/telegram-bot-legacy/.env` | BotFather > revoke ou confirmer deja-revoke | 5 min |\n")
parts.append("\n")
parts.append("### P1 - A faire en semaine 2 (avec la migration vault de l etape 8)\n\n")
parts.append("Tous les secrets AT REST UNENCRYPTED migres vers 1Password (un par un, avec drill de validation cote provider) :\n\n")
parts.append("- 18 secrets de `.claude/settings.local.json`\n")
parts.append("- 132 secrets repartis sur 14 fichiers `.env`\n")
parts.append("- credentials Google Workspace `.credentials/`\n\n")
parts.append("### P2 - Cleanup\n\n")
parts.append("- Supprimer `.mcp.json.bak` et `.mcp.backup.json` (apres confirmation, redondants avec `.mcp.json.example`)\n")
parts.append("- Supprimer `apps/_archive/telegram-bot-legacy/.env` apres rotation token\n")
parts.append("- Supprimer `apps/_archive/elearning/elearning/elearning/.env`\n")
parts.append("- Auditer les Application Passwords WP orphelins (SEOpital, ClaudeAPI - deja note etape 2)\n")
parts.append("- Reduire les scopes du PAT GitHub `ghp_...` (etape 1 finding #7)\n\n")

parts.append("### Note importante sur les rotations cote provider\n\n")
parts.append("Pour les services qui n offrent pas de UI de rotation (rare en 2026), seule la generation d une nouvelle key + revoke est possible. Si une vieille key reste valide cote provider mais que tu n y as plus acces, elle reste un risque.\n\n")
parts.append("Inventaire des UIs de rotation pour les 30+ providers schoolsWP : a documenter dans `docs/security/09-rotation-runbook.md` (etape 9 du briefing).\n\n")

parts.append("---\n\n## 5. Findings classes\n\n")
parts.append("### CRITIQUE\n\n")
parts.append("1. **`.mcp.json` actuel contient un jwt_token en clair** (last4 fCmA) au lieu d une substitution ${VAR}. Le pattern launcher .mjs n est pas applique partout. Investiguer + migrer.\n\n")
parts.append("2. **10 secrets dans l historique du repo private schoolswp** (2 cles Gemini distinctes + 2 jwt + 2 URL avec basic auth + 1 Telegram bot). Le repo est private (controle gh), mais l historique est lisible par tous les forks + clones existants.\n\n")
parts.append("3. **N8N_ENCRYPTION_KEY en clair** dans `systems/n8n/.env` (deja note etape 1 et 3). Cle maitre = decryption en cascade de 46 credentials n8n.\n\n")

parts.append("### ELEVE\n\n")
parts.append("4. **`.claude/settings.local.json` concentre 18 secrets** sans chiffrement. Single point of failure.\n\n")
parts.append("5. **2 fichiers `_archive/` contiennent des secrets** (telegram-bot-legacy + elearning). Surface oubliee.\n\n")
parts.append("6. **`telegram_agents_wp1` cle SSH** : statut passphrase non confirme (a tester manuellement).\n\n")
parts.append("7. **PAT GitHub `ghp_...` classic, scopes large** (deja note etape 1).\n\n")

parts.append("### MOYEN\n\n")
parts.append("8. **Doublons de secrets dans Git history** : la meme cle Gemini ...RUX0 apparait dans 3 fichiers. Augmente la surface si quelqu un grep les vieux commits.\n\n")
parts.append("9. **2 URLs avec basic auth dans `multi-agent-system/workflows/`** : revoir la nature (interne ou externe, encore valide ou pas).\n\n")
parts.append("10. **brightbean-studio (fork)** : 7 URLs postgres user:pass dans docker-compose/CI. Ce n est pas TON repo donc pas TON probleme strict, mais ton fork local le contient. Si tu push vers ton remote (verifier `git remote -v`), tu propages.\n\n")

parts.append("### FAIBLE\n\n")
parts.append("11. **claude-mem (fork)** : 2 findings dans `benchmark/tests/sanitizer.test.ts` = fixtures de test du sanitizer (intentionnel cote upstream).\n\n")

parts.append("---\n\n## 6. Recommandations pour la suite\n\n")
parts.append("**Avant l etape 5 (backup)** : terminer les P0 de la table de rotation ci-dessus. Sinon le backup capture des secrets actuellement valides qui restent exposes si le backup leaks.\n\n")
parts.append("**Apres l etape 5** : passer a l etape 7 (rotation complete) puis 8 (vault central).\n\n")
parts.append("**Long terme** : installer gitleaks ou trufflehog en pre-commit hook bloquant. Patterns sont deja dans `.gitleaks.toml` standard, ajouter quelques patterns custom (HeyGen `hgg_`, Skoatch token, etc.).\n\n")

parts.append("## Etape 4 terminee. En attente validation pour etape 5 (backup non-negociable).\n")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
print(f"WRITTEN: {OUT} ({OUT.stat().st_size} bytes)")
