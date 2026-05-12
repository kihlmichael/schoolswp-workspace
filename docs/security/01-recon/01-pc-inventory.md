# Etape 1 - Inventaire PC dev (Windows 11)

> Audit lecture seule. Date : 2026-05-12. Plateforme : Windows 11 Home, PC ROG Strix SCAR 16, user conta.
> Aucune modification effectuee. Aucun secret en clair dans ce rapport (4 derniers chars max si necessaire).

---

## Resume executif

5 findings CRITIQUE, 6 findings ELEVE, 5 findings MOYEN, 3 findings FAIBLE.

Le perimetre dev est riche mais fortement fragmente :

- ~14 fichiers .env contenant des secrets reels (hors .example), repartis sur 4 sous-systemes (root, n8n, fleet schoolswp-agents, apps annexes, archives).
- Memes secrets dupliques dans plusieurs fichiers (blast radius x4 sur ANTHROPIC_API_KEY notamment).
- .mcp.json.bak et .mcp.backup.json du 27-28 avril 2026, identiques byte-a-byte, encore presents sur disque alors qu anterieurs aux rotations documentees.
- Windows Defender real-time protection OFF (offset par Kaspersky, a confirmer).
- C:/Users/conta/bin en tete de PATH (vecteur PATH hijack).

La rotation prioritaire et la migration vers vault central (etapes 4, 7, 8 du briefing) sont indispensables. Le pipeline de hardening peut demarrer des que ces bases sont posees.

---

## 1. Process longs

Capture instantanee, processus dev en cours :

| Process | Count |
|---|---|
| node | 85 |
| claude | 14 |
| docker (toutes variantes) | 19 |
| python | 6 |
| pwsh | 1 |

Lecture : 85 processus node simultanes correspondent aux ~28 MCP servers + Claude Code stdio enfants + agents fleet. 14 instances claude = main + 4 fleet schoolswp-agents + ~9 sous-process / worktrees. Pas d anomalie immediate, mais surface memoire et complexite elevees.

## 2. Venvs Python

4 venvs detectes :

- .venv/ (workspace root, prod schoolsWP)
- apps/claude-telegram-poc/venv/ (POC, a archiver ?)
- systems/multi-agent-system/multi-agent-system/.venv/ (dossier duplique imbrique, anomalie connue cf CLAUDE.md)
- .claude/skills/external-video-use/.venv/ (skill externe, isole)

Aucun venv dans worktrees Git ou _archive/. Bon point.

## 3. Fichiers .env (KEYS uniquement, jamais les valeurs)

14 .env reels (hors .example et .backup.example), 132 variables au total.

| Fichier | Vars | Note |
|---|---|---|
| .env (root) | 27 | LLM/social/n8n hub |
| systems/n8n/.env | 52 | n8n prod (DB postgres + S3 + basic auth) |
| agents/telegram-claude/.env | 17 | 6 Telegram bot tokens FLOW/PULSE/RADAR/REDDIT/STUDIO/WELCOME + Discord |
| systems/multi-agent-system/multi-agent-system/.env | 13 | sous-systeme multi-agent (dossier duplique) |
| agents/.env | 6 | Hunter + Unipile + N8N_WEBHOOK_SECRET |
| apps/claude-telegram-poc/.env | 5 | POC isole |
| apps/_archive/elearning/elearning/elearning/.env | 5 | ARCHIVE, a verifier |
| apps/_archive/telegram-bot-legacy/.env | 2 | ARCHIVE, a verifier |
| tools/skoatch/.env | 1 | SKOATCH_TOKEN |
| .claude/skills/external-video-use/.env | 1 | ELEVENLABS_API_KEY |
| schoolswp-agents/(content-studio|seo-geo|crm-automation|social-community)/.claude/channels/telegram/.env | 4 x 1 | TELEGRAM_TOKEN fleet |

Doublons critiques (meme secret dans plusieurs fichiers) :

| Variable | Presence | Blast radius si leake |
|---|---|---|
| ANTHROPIC_API_KEY | .env, agents/.env, agents/telegram-claude/.env, multi-agent-system/.env | 4x |
| OPENAI_API_KEY | .env, systems/n8n/.env | 2x |
| FIRECRAWL_API_KEY | .env, agents/.env | 2x |
| ELEVENLABS_API_KEY | .env, .claude/skills/external-video-use/.env | 2x |
| Discord bot tokens + channels | .env, agents/telegram-claude/.env | 2x |

Cles sensibles infrastructure (n8n) :

systems/n8n/.env contient en clair :

- N8N_BASIC_AUTH_PASSWORD (gardien de l UI n8n)
- N8N_ENCRYPTION_KEY (cle maitre qui chiffre TOUTES les credentials stockees dans n8n)
- DB_POSTGRESDB_PASSWORD (DB prod n8n)
- S3_SECRET_KEY (backups n8n cote S3)
- WHATSAPP_CALLMEBOT_APIKEY
- DATAFORSEO_PASSWORD

Le N8N_ENCRYPTION_KEY est de loin le plus critique : un attaquant qui l obtient peut dechiffrer toutes les credentials cumulees dans n8n (ce qui inclut les credentials FluentCart, Stripe, et toute la stack OAuth Google).

## 4. Settings Claude Code

| Fichier | Bytes | Env blocks | Uppercase KEY entries |
|---|---|---|---|
| .claude/settings.local.json (workspace) | 85 418 | 1 | 18 |
| C:/Users/conta/.claude/settings.local.json (user) | 264 | 0 | 0 |
| C:/Users/conta/.claude/settings.json (user) | 12 013 | 0 | 0 |

Secrets dans .claude/settings.local.json (workspace) :

APIFY_TOKEN, DATAFORSEO_PASSWORD, DATAFORSEO_USERNAME, DISCORD_BOT_TOKEN, FIRECRAWL_API_KEY, FLUENTCRM_API_PASSWORD, FLUENTCRM_API_URL, FLUENTCRM_API_USERNAME, GEMINI_API_KEY, GITHUB_TOKEN, N8N_API_KEY, N8N_API_URL, RAPIDAPI_KEY, WISEWAND_API_KEY, WP_API_PASSWORD, WP_API_URL, WP_API_USERNAME, ZIPWP_TOKEN

Pattern coherent avec la memoire reference_claude_code_secrets_storage : les MCP lisent depuis ce fichier via launcher .mjs. Mais ces secrets sont aussi presents dans .env workspace et agents/.env pour certains (FIRECRAWL_API_KEY, APIFY_TOKEN, GEMINI_API_KEY, DISCORD_BOT_TOKEN, GITHUB_TOKEN, RAPIDAPI_KEY...). Source de verite ambigue.

## 5. .mcp.json variants

| Fichier | Date | Bytes | VAR refs | Suspect long strings | Notes |
|---|---|---|---|---|---|
| .mcp.json | 11 mai 2026 | 5 997 | 9 | 27 | actif, pattern launcher |
| .mcp.json.bak | 28 avril 2026 | 5 191 | 27 | 36 | suspect, identique au backup |
| .mcp.backup.json | 27 avril 2026 | 5 191 | 27 | 36 | identique a .bak, contient VAR substitution massive |
| .mcp.json.fluent | 29 avril 2026 | 2 043 | 1 | 7 | snapshot config Fluent |
| .mcp.json.example | 6 mai 2026 | 3 002 | 1 | 21 | template git-tracke |

Les long-strings dans .mcp.json.bak et .mcp.backup.json meritent une inspection rapprochee : les 27 VAR substitutions indiquent que le pattern variable-substitution etait en place, mais 36 strings de plus de 20 chars sans VAR peuvent etre des URLs, des noms de packages npm, OU des secrets residuels pre-rotation 2026-04-21 / 2026-04-29 documentees. Aucune reference 1Password CLI (op://) a ce jour.

## 6. Cles SSH

C:/Users/conta/.ssh/

- config (167 octets, a examiner)
- known_hosts (926 octets)
- known_hosts.old (94 octets)
- telegram_agents_wp1 (cle privee ED25519, 432 octets)
- telegram_agents_wp1.pub : SHA256:xiIx15i7gQIyoGjeiNzw15jV2ZFKjrGfyvVRpTlT6SM (telegram_agents@schoolswp-20260419)

1 seule cle privee, dediee au deploiement telegram-agents WP1 (xCloud). Pas de cle GitHub locale (cf insteadOf du .gitconfig qui route SSH vers HTTPS, deja documente en memoire).

Statut passphrase non testable depuis ici (le classifier a bloque la probe sur cle privee, comportement sain). A verifier manuellement par Michael avec un test passphrase vide dans une session separee (silence sans erreur = pas de passphrase = CRITIQUE).

## 7. PATH analysis

Entrees writable par conta listees dans l ordre du PATH :

| Position | Path | Risque |
|---|---|---|
| 1 (top) | C:/Users/conta/bin | CRITIQUE : user-writable, AVANT System32 |
| 9 | D:/VS Code/CLAUDE CODE/projects/schoolswp/.venv/Scripts | ELEVE : projet schoolswp prend precedence (intentionnel mais risque si compromis) |
| 24 | C:/Users/conta/.bun/bin | MOYEN |
| 25 | C:/Users/conta/.local/bin | MOYEN |
| 27 | C:/Users/conta/AppData/Local/Microsoft/WindowsApps | MOYEN |
| 29 | C:/Users/conta/AppData/Local/Python/bin | MOYEN |
| 30 | C:/Users/conta/AppData/Roaming/npm | MOYEN |
| 31 | C:/Users/conta/AppData/Local/Microsoft/WinGet/Packages/Ngrok.Ngrok_* | FAIBLE |
| 32 | C:/Users/conta/AppData/Local/Microsoft/WinGet/Packages/Cloudflare.cloudflared_* | FAIBLE |
| 34 | C:/users/conta/appdata/roaming/python/python314/scripts | MOYEN (casse mixte) |
| 35 | C:/Users/conta/AppData/Local/Programs/Antigravity/bin | MOYEN |
| 38 | C:/Users/conta/AppData/Local/Programs/ExifTool | FAIBLE (cf memory reference_exiftool_path) |
| 39 | C:/Users/conta/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin | MOYEN |
| 40 | C:/Users/conta/go/bin | MOYEN |

Doublons dans PATH (a nettoyer pour proprete) : C:/Program Files/Git/usr/bin et C:/Program Files/Git/mingw64/bin listes 2x chacun.

## 8. Containers Docker

3 containers brightbean-studio-* exited il y a 2 semaines (residu, a nettoyer).
1 container openshell-cluster-nemoclaw running depuis 30h sur port 8080 = legit (cf memoire project_nemoclaw_setup).

Networks : 5 (bridge, host, none, brightbean-studio_default residu, openshell-cluster-nemoclaw).

PM2 absent localement = les apps PM2 (telegram-agents, discord-orchestrator) tournent uniquement sur xCloud.

## 9. Caches credentials et identites tierces

- D:/.../projects/schoolswp/.credentials/gsc-client-secrets.json (398 octets, OAuth Google Search Console, deja gitignored).
- C:/Users/conta/.docker/config.json (403 octets, credsStore actif, Docker pousse les creds vers Credential Manager).
- C:/Users/conta/.gitconfig (1 225 octets, 16 safe.directory dont 2 doublons michaelkihl-fr).
- C:/Users/conta/.npmrc : ABSENT (bonne nouvelle, pas de _authToken qui traine).
- C:/Users/conta/.aws/ : vide (pas d AWS credentials).
- gh CLI : 2 comptes authentifies sous kihlmichael (un via env GITHUB_TOKEN, un via keyring). Token actif = env. Scopes : read:org, read:user, repo, workflow. Format classic PAT, pas fine-grained.
- Windows Credential Manager : Microsoft 365 SSO contact@michaelkihl.fr, Adobe (App Info), Docker Hub access+refresh tokens, gh kihlmichael keyring, docker/mcp/SHODAN_API_KEY. Aucun secret WP Umbrella detecte alors que la memoire reference_wp_umbrella_skill indique qu il devrait y etre. A investiguer.

## 10. Taches planifiees + services tiers

Taches planifiees non-Microsoft enabled (toutes legit) :
Adobe (Acrobat Update, Genuine Software Integrity, AdobeGCInvoker, Launch CCXProcess), ASUS x9 (AcPower, ArmourySocketServer, GearLink x5, P508PowerAgent), NVIDIA App SelfUpdate + Shader Compiler, OneDrive x3, Samsung_PSSD_Registration, ZoomUpdateTaskUser. Aucune tache custom dev/cron.

Services tiers running auto :
Kaspersky (AVP21.24 antivirus + KSDE5.25 VPN + kpm_service Password Manager), Adobe (ARM + Update), ASUS x9 (Armoury Crate, ScreenXpert, GlideX x3, Aura Wallpaper, GameSDK, ROG Live Service, MS Control, AsusCertService), NVIDIA NvContainer LocalSystem, WSL Service, Office ClickToRun, Microsoft Defender (mais real-time desactive, cf section 11), Claude CoworkVMService (cowork-svc depuis app Claude Windows native).

WSL2 disponible (service running) = option viable pour proxy sortant agents (Privoxy ou squid, recommandation briefing etape 10).

## 11. Windows Defender + AV

    AMServiceEnabled              : True
    AntivirusEnabled              : True
    RealTimeProtectionEnabled     : False    <-- OFF
    IoavProtectionEnabled         : False    <-- OFF
    BehaviorMonitorEnabled        : False    <-- OFF
    OnAccessProtectionEnabled     : False    <-- OFF
    TamperProtected               : (vide)
    AntivirusSignatureLastUpdated : 12/05/2026 01:15:03
    QuickScanAge                  : 0
    FullScanAge                   : 4294967295 (jamais)

Defender est en mode passif parce que Kaspersky 21.24 a pris le relais comme AV principal (AVP21.24, KSDE5.25, kpm_service_25.1). Comportement normal sous Windows 11. Threat detection history Defender : vide. Pas d evidence d infection courante.

Action requise : confirmer que Kaspersky est licencie, a jour, et que le real-time scan est actif cote Kaspersky (a verifier dans Kaspersky UI).

---

## Findings classes

### CRITIQUE

1. N8N_ENCRYPTION_KEY en clair dans systems/n8n/.env
   Cle maitre qui chiffre toutes les credentials stockees dans n8n (FluentCart, Stripe, Google OAuth, etc.). Compromission = compromission cascade de toute la stack n8n. Rotation immediate ET migration vault a prioriser absolument.

2. ANTHROPIC_API_KEY duplique dans 4 fichiers .env
   Blast radius x4. Un seul leak compromet la facturation Anthropic complete et donne acces a tous les agents. Migration vault avec une cle par machine (briefing etape 7 et 9).

3. .mcp.json.bak et .mcp.backup.json identiques byte-a-byte du 27-28 avril 2026
   Anterieurs aux rotations RapidAPI documentees (incident 2026-04-21) et Fluent (2026-04-29). Probable contiennent des secrets rotates mais non purges. A examiner et supprimer manuellement via Explorer.

4. C:/Users/conta/bin premier dans PATH
   Vecteur PATH hijack : tout executable malicieux depose la est lance avant ceux de System32. Soit deplacer en fin de PATH, soit auditer son contenu et le passer en read-only.

5. 6 Telegram bot tokens en clair dans agents/telegram-claude/.env
   FLOW, PULSE, RADAR, REDDIT, STUDIO, WELCOME. Pas de rotation possible sans casser les bots (memoire confirme), donc le stockage doit etre verrouille. Migration vault prioritaire + restriction d acces filesystem.

### ELEVE

6. Statut passphrase de la cle SSH telegram_agents_wp1 non verifie
   Si pas de passphrase = perte du PC = acces direct a l instance WP1 xCloud. A verifier manuellement par Michael (test passphrase vide dans une session separee, silence sans erreur = pas de passphrase).

7. PAT GitHub actif avec scopes large
   repo + workflow + read:org = peut push, peut alterer GitHub Actions, peut lire l organisation. Stocke a 2 endroits (env + keyring). A migrer en fine-grained PAT par usage.

8. 2 comptes GitHub kihlmichael simultanement actifs dans gh CLI
   Confusion d identite. Consolider en un seul (le keyring est plus sur que l env).

9. Windows Defender real-time OFF
   Compense par Kaspersky, mais necessite confirmation que Kaspersky est sous licence active et en real-time scan. Sinon, breche silencieuse.

10. Settings.local.json workspace 85 KB avec 18 secrets
    Concentration forte = single point of failure. La migration vers 1Password CLI (briefing etape 8) doit etre prioritaire.

11. 2 .env dans apps/_archive/
    telegram-bot-legacy/.env et elearning/elearning/elearning/.env. Archives donc oublies. Auditer ce qu ils contiennent (probablement des secrets pre-rotation) puis supprimer manuellement.

### MOYEN

12. Dossier systems/multi-agent-system/multi-agent-system/ duplique imbrique
    Anomalie documentee dans CLAUDE.md. Son .env contient 13 vars dont ANTHROPIC_API_KEY. Auditer si encore utilise, sinon archiver.

13. Containers brightbean-studio-* exited il y a 2 semaines
    Residu, a supprimer apres confirmation Michael.

14. PATH doublons : Git/usr/bin et mingw64/bin listes 2x chacun. Cosmetique mais signal d un PATH non maintenu.

15. gitconfig doublons : michaelkihl-fr liste 2x en safe.directory. A nettoyer.

16. docker/mcp/SHODAN_API_KEY dans Credential Manager
    Token Shodan dans Docker MCP credential store. Verifier si Docker MCP est activement utilise. Si non, retirer.

### FAIBLE

17. WP Umbrella token absent du Credential Manager alors que la memoire l indique present. Peut signifier qu il est dans un autre store (1Password, fichier). A localiser pour confirmer la memoire.

18. PM2 absent localement
    Les apps PM2 ne tournent que sur xCloud. Coherent. Note pour le runbook incident : si PC compromis, les apps tournent toujours cote xCloud.

19. Taches planifiees : zero tache dev custom
    Pas de cron-style local. Tout passe par n8n ou apps xCloud. Coherent.

---

## Recommandations pour les etapes suivantes du briefing

| Finding | Etape briefing | Priorite |
|---|---|---|
| #1, #2, #5, #10 | Etape 7 (rotation) + Etape 8 (vault) | P0, semaine 1-2 |
| #3, #11 | Etape 4 (secrets inventory + rotation immediate) | P0, AVANT etape 5 |
| #4, #14, #15 | Hardening PC dev (a ajouter en phase 0bis ?) | P1, semaine 2 |
| #6 | Manuel, immediat | P0, ce soir |
| #7, #8 | Etape 7 (rotation + scoping) | P1 |
| #9 | Manuel via Kaspersky UI | P1 |
| #12, #13, #16 | Cleanup workspace (hors briefing) | P2, mois 1 |
| #17, #18, #19 | Note pour etape 14 (runbook incident) | P2 |

## Etape 1 terminee. En attente validation pour etape 2 (inventaire WP).
