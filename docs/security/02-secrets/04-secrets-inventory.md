# Etape 4 - Inventaire secrets multi-niveaux

> Audit lecture seule. Date : 2026-05-12.
> Methode : scanner Python custom (equivalent gitleaks, 30 patterns) sur 8 repos Git + on-disk scan + croisement avec etape 1.
> Aucune valeur secrete dans ce rapport (4 derniers chars max si necessaire).

---

## Resume executif

**29 secrets reels detectes au total**, repartis sur 4 niveaux de stockage :

| Classification | Count | Action |
|---|---|---|
| LEAKED PUBLIC | 0 | (les 3 repos kihlmichael sont prives, verifie via gh) |
| LEAKED PRIVATE (Git history) | 10 | Rotation par precaution (acces a l historique = compromission) |
| AT REST UNENCRYPTED (sur disque) | 18+ | Migration vault prioritaire (etape briefing 7-8) |
| PROPER (vault ou chiffre) | ~1Password (a confirmer) | Continuer |

**Bonne nouvelle** : aucun secret dans un repo public que tu controles. Les 3 repos kihlmichael (schoolswp, schoolswp-telegram-agents, michaelkihl-fr) sont tous prives.

**Mauvaise nouvelle** : 10 secrets sont dans l historique Git du repo principal schoolswp. Si quelqu un a un fork local (anciens claude-code clones, machines secondaires), il peut les voir. **Rotation par precaution recommandee.**

**Trois priorites immediates** :

1. Rotater les 2 cles Gemini (...yW1E et ...RUX0) presentes dans 4 fichiers de l historique schoolswp.
2. Rotater le jwt n8n (...rcGY) dans `multi-agent-system/workflows/geo-architect-bulk-fill.json` (egalement note etape 3).
3. Investiguer le `.mcp.json` actuel qui contient un jwt_token en clair (...fCmA) au lieu d une substitution ${VAR}.

---

## 1. Surface scannee

### Repos Git

| Repo | Type | Remote | Commits | Findings |
|---|---|---|---|---|
| `projects/schoolswp` | private | github.com/kihlmichael/schoolswp | 157 | **10** |
| `projects/schoolswp/agents/telegram-claude` | private | kihlmichael/schoolswp-telegram-agents | 16 | 0 (CLEAN) |
| `projects/michaelkihl-fr` | private | kihlmichael/michaelkihl-fr | 4 | 0 (CLEAN) |
| `tools/ultimate-scraper` | local-only | (no remote) | 0 | (init non commited) |
| `novamira` | fork | use-novamira/novamira | 80 | 0 (CLEAN) |
| `thruuu-claude-content-strategist` | fork | thruuu/... | 6 | 0 (CLEAN) |
| `projects/brightbean-studio` | fork | brightbeanxyz/... | 297 | 7 (URL postgres user:pass, fixture de fork) |
| `projects/claude-mem` | fork | thedotmack/... | 2957 | 2 (sanitizer test fixtures) |

Total commits scannes : 3525. Volume de lignes streame : ~4.2M.

### On-disk (hors Git)

- 5 variantes `.mcp.json` (actuel + 4 backups)
- 14 fichiers `.env` reels (cf etape 1)
- 1 fichier `.credentials/gsc-client-secrets.json`
- 1 fichier `.claude/settings.local.json` workspace (85 KB, 18 secrets)
- 1 cle SSH privee (telegram_agents_wp1)

---

## 2. LEAKED PRIVATE - Git history schoolswp (10 findings)

Repo `projects/schoolswp` est PRIVE sur GitHub, mais les secrets sont dans l historique et peuvent etre vus par :

- Toute personne avec acces au repo (theoriquement Michael seul, mais a verifier les collaborators GitHub).
- Tout clone local existant (machines secondaires, anciens Claude Code workspaces, sauvegardes).
- Tout fichier `.pack` Git sauvegarde par WPvivid / WP Umbrella / Backblaze.

**Table des findings** :

| # | Type | Commit | Fichier | Last 4 | Verdict |
|---|---|---|---|---|---|
| 1 | gemini_api_key | a4cbc571 | `.nano-banana-config.json` | ...yW1E | Cle Gemini #1, **ROTATER** |
| 2 | gemini_api_key | e61d4bcc | `data/setup_gemini_credential.py` | ...RUX0 | Cle Gemini #2, **ROTATER** |
| 3 | gemini_api_key | e61d4bcc | `tools/scripts/nas-photo-renamer.py` | ...RUX0 | Duplicate de #2 |
| 4 | gemini_api_key | e61d4bcc | `tools/scripts/photo-vacances-organizer.py` | ...RUX0 | Duplicate de #2 |
| 5 | password_in_url | e61d4bcc | `systems/multi-agent-system/workflows/content-machine-schoolswp-v2.json` | (URL) | URL avec basic auth user:pass embedded, a verifier |
| 6 | password_in_url | 080ef6a9 | `multi-agent-system/workflows/content-machine-schoolswp-v2.json` (ancien path) | (URL) | Duplicate de #5 sur path legacy |
| 7 | jwt_token | 080ef6a9 | `multi-agent-system/workflows/geo-architect-bulk-fill.json` | ...rcGY | jwt n8n hardcode, **ROTATER** (deja note etape 3) |
| 8 | generic_bearer | 080ef6a9 | `multi-agent-system/workflows/geo-architect-bulk-fill.json` | ...rcGY | Meme jwt formate en Bearer, duplicate de #7 |
| 9 | jwt_token | 080ef6a9 | `settings.json` (root) | ...91q4 | **INVESTIGUER** : settings.json a la racine du repo ? probable Claude Code ancien |
| 10 | telegram_bot_token | 2b8fe366 | `claude-telegram-poc/README.local.md` | ...xxxx | Probable masque ('xxxx' en hex), **VERIFIER** si reel |

**Cles Gemini uniques** : 2 distinctes (...yW1E et ...RUX0). Si tu en utilises encore une au moins, rotater les deux et nettoyer.

**Action immediate** : pour chaque finding :

1. Identifier le service provider (Gemini Console pour les API keys, n8n UI pour le jwt).
2. Generer une nouvelle valeur cote provider.
3. Revoke l ancienne valeur.
4. Mettre a jour les usages courants (vault + workflow n8n + .env).

**Nettoyer l historique Git** est theoriquement possible avec `git filter-repo` mais brise les hashes commits. Recommandation : ne PAS reecrire l historique. La rotation suffit (les anciennes valeurs deviennent invalides cote provider).

---

## 3. AT REST UNENCRYPTED - Disque (hors Git)

### `.mcp.json` actuel : 1 jwt en clair

Le scan a trouve un jwt_token en clair (prefix `eyJhbGci...`, last4 ...fCmA) dans `.mcp.json` au lieu d une substitution ${VAR}. C est probablement reste comme "fallback" en attendant la migration vault.

Action : verifier de quel MCP server il s agit, migrer en op:// ou ${VAR}, rotater le secret cote provider.

### `.mcp.json` backups : tous CLEAN

Bonne nouvelle : `.mcp.json.bak`, `.mcp.json.fluent`, `.mcp.backup.json`, `.mcp.json.example` utilisent tous le pattern ${VAR} substitution. Pas de secret en clair residuel pre-rotation.

Note de l etape 1 invalidee : j avais classe `.mcp.json.bak` et `.mcp.backup.json` comme CRITIQUE par prudence. Le scan precis confirme qu ils sont propres. **Peut tout de meme les supprimer pour proprete** (fichiers de 27/28 avril 2026 obsoletes).

### `apps/_archive/telegram-bot-legacy/.env` : 1 telegram_bot_token

Fichier dans `_archive/`. Le scan a trouve un telegram_bot_token (last4 ...cfEY). 2 hypotheses :

- Le token est encore actif cote Telegram (oubli de rotation). **Verifier dans Telegram BotFather**.
- Le token a deja ete revoqué quand le bot a ete deprecated. Dans ce cas, le fichier peut etre supprime sans risque.

### `apps/_archive/elearning/elearning/elearning/.env` : CLEAN

5 variables mais aucun secret matche les patterns. Probable placeholders ou config de demo. Peut etre supprime apres confirmation.

### `.env` workspace + 13 autres : 132 variables

Inventaire detaille dans le rapport de l etape 1 (`01-recon/01-pc-inventory.md` section 3). Resume :

- **27 vars** dans `.env` racine
- **52 vars** dans `systems/n8n/.env` (dont N8N_ENCRYPTION_KEY, N8N_BASIC_AUTH_PASSWORD, DB_POSTGRESDB_PASSWORD, S3_SECRET_KEY)
- **17 vars** dans `agents/telegram-claude/.env` (6 Telegram bot tokens)
- **13 vars** dans `systems/multi-agent-system/multi-agent-system/.env`
- ~17 autres dans 9 .env satellites

Tous sont AT REST UNENCRYPTED en clair sur disque, lisibles par tout process qui tourne en tant que `conta` ou root. **Mitigations** : migration vault (etape 8 briefing) + NTFS perms restrictives via icacls.

### `.claude/settings.local.json` workspace : 18 secrets

85 KB, top-level `env` block. Pattern launcher .mjs valide (cf memory `reference_claude_code_secrets_storage`) mais ces 18 secrets sont AT REST UNENCRYPTED dans le fichier.

KEYS : APIFY_TOKEN, DATAFORSEO_PASSWORD/USERNAME, DISCORD_BOT_TOKEN, FIRECRAWL_API_KEY, FLUENTCRM_API_*, GEMINI_API_KEY, GITHUB_TOKEN, N8N_API_KEY/URL, RAPIDAPI_KEY, WISEWAND_API_KEY, WP_API_*, ZIPWP_TOKEN.

### `.credentials/gsc-client-secrets.json`

OAuth client secret Google Search Console. Gitignored, present sur disque. AT REST UNENCRYPTED mais protege par les credentials OAuth user-level Google.

### Cle SSH privee `telegram_agents_wp1`

ED25519 sur disque. Si pas de passphrase = AT REST UNENCRYPTED (a verifier manuellement, cf etape 1 finding #6).

---

## 4. Runbook rotation prioritaire

Ordre d execution recommande (du plus critique au moins) :

### P0 - A faire dans les 48h

| Ordre | Secret | Localisation | Action | Estimation |
|---|---|---|---|---|
| 1 | jwt_token `.mcp.json` actuel (...fCmA) | `.mcp.json` workspace | Identifier MCP server proprietaire, migrer en op:// ou ${VAR}, rotater | 15 min |
| 2 | Gemini API key #1 (...yW1E) | Git history schoolswp `.nano-banana-config.json` | Generate new key in Google AI Studio, revoke old | 5 min |
| 3 | Gemini API key #2 (...RUX0) | Git history schoolswp data/setup_gemini_credential.py + 2 autres | Generate new key, revoke old, mettre a jour les 3 fichiers en local (sans rewrite history) | 10 min |
| 4 | jwt n8n geo-architect-bulk-fill (...rcGY) | Git history + workflow n8n actif | n8n UI > export workflow > create credential > update node | 15 min |
| 5 | jwt settings.json (...91q4) | Git history schoolswp root | Identifier (cookie Claude Code ?), revoke | 10 min |
| 6 | Telegram bot token archive (...cfEY) | `apps/_archive/telegram-bot-legacy/.env` | BotFather > revoke ou confirmer deja-revoke | 5 min |

### P1 - A faire en semaine 2 (avec la migration vault de l etape 8)

Tous les secrets AT REST UNENCRYPTED migres vers 1Password (un par un, avec drill de validation cote provider) :

- 18 secrets de `.claude/settings.local.json`
- 132 secrets repartis sur 14 fichiers `.env`
- credentials Google Workspace `.credentials/`

### P2 - Cleanup

- Supprimer `.mcp.json.bak` et `.mcp.backup.json` (apres confirmation, redondants avec `.mcp.json.example`)
- Supprimer `apps/_archive/telegram-bot-legacy/.env` apres rotation token
- Supprimer `apps/_archive/elearning/elearning/elearning/.env`
- Auditer les Application Passwords WP orphelins (SEOpital, ClaudeAPI - deja note etape 2)
- Reduire les scopes du PAT GitHub `ghp_...` (etape 1 finding #7)

### Note importante sur les rotations cote provider

Pour les services qui n offrent pas de UI de rotation (rare en 2026), seule la generation d une nouvelle key + revoke est possible. Si une vieille key reste valide cote provider mais que tu n y as plus acces, elle reste un risque.

Inventaire des UIs de rotation pour les 30+ providers schoolsWP : a documenter dans `docs/security/09-rotation-runbook.md` (etape 9 du briefing).

---

## 5. Findings classes

### CRITIQUE

1. **`.mcp.json` actuel contient un jwt_token en clair** (last4 fCmA) au lieu d une substitution ${VAR}. Le pattern launcher .mjs n est pas applique partout. Investiguer + migrer.

2. **10 secrets dans l historique du repo private schoolswp** (2 cles Gemini distinctes + 2 jwt + 2 URL avec basic auth + 1 Telegram bot). Le repo est private (controle gh), mais l historique est lisible par tous les forks + clones existants.

3. **N8N_ENCRYPTION_KEY en clair** dans `systems/n8n/.env` (deja note etape 1 et 3). Cle maitre = decryption en cascade de 46 credentials n8n.

### ELEVE

4. **`.claude/settings.local.json` concentre 18 secrets** sans chiffrement. Single point of failure.

5. **2 fichiers `_archive/` contiennent des secrets** (telegram-bot-legacy + elearning). Surface oubliee.

6. **`telegram_agents_wp1` cle SSH** : statut passphrase non confirme (a tester manuellement).

7. **PAT GitHub `ghp_...` classic, scopes large** (deja note etape 1).

### MOYEN

8. **Doublons de secrets dans Git history** : la meme cle Gemini ...RUX0 apparait dans 3 fichiers. Augmente la surface si quelqu un grep les vieux commits.

9. **2 URLs avec basic auth dans `multi-agent-system/workflows/`** : revoir la nature (interne ou externe, encore valide ou pas).

10. **brightbean-studio (fork)** : 7 URLs postgres user:pass dans docker-compose/CI. Ce n est pas TON repo donc pas TON probleme strict, mais ton fork local le contient. Si tu push vers ton remote (verifier `git remote -v`), tu propages.

### FAIBLE

11. **claude-mem (fork)** : 2 findings dans `benchmark/tests/sanitizer.test.ts` = fixtures de test du sanitizer (intentionnel cote upstream).

---

## 6. Recommandations pour la suite

**Avant l etape 5 (backup)** : terminer les P0 de la table de rotation ci-dessus. Sinon le backup capture des secrets actuellement valides qui restent exposes si le backup leaks.

**Apres l etape 5** : passer a l etape 7 (rotation complete) puis 8 (vault central).

**Long terme** : installer gitleaks ou trufflehog en pre-commit hook bloquant. Patterns sont deja dans `.gitleaks.toml` standard, ajouter quelques patterns custom (HeyGen `hgg_`, Skoatch token, etc.).

## Etape 4 terminee. En attente validation pour etape 5 (backup non-negociable).
