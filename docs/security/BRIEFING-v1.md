# Security Briefing schoolsWP v1.0

> Adapté du Security Briefing AFFISEO OS v1.1 pour le contexte schoolsWP (WordPress managé EasyHoster + n8n hébergé + apps xCloud + fleet agents Python locale sous Windows 11 + ~28 MCP servers + 9 bots Telegram + FluentCart paiements).
>
> Date de création : 2026-05-12
> Auteur : Michael KIHL
> Plateforme dev : Windows 11 Home (PC ROG Strix SCAR 16, voir mémoire hardware_pc_michael)
> Versioning : ce document est la référence unique. Toute itération crée une v1.X notée en haut.

---

## Carte mentale des cibles

```
schoolsWP OS
├── WP schoolswp.com (EasyHoster, prod, FluentCRM/Cart/Boards/Forms, TutorLMS, ~357 articles, PII clients)
├── WP michaelkihl.fr (xCloud, secondaire, Skoatch drafts)
├── n8n schoolswp-n8n.wp1.host (workflows + credentials hardcodées historiques)
├── xCloud apps : telegram-agents, discord-orchestrator, FluentBoards utils
├── PC Windows 11 dev (D:\VS Code\CLAUDE CODE\...) : agents Python, fleet schoolswp-agents,
│   MCP, .claude\settings.local.json
├── GitHub : projet schoolswp + novamira + thruuu + skoatch (historique potentiellement compromis)
├── Obsidian vault (D:\MES SITES\SCHOOLSWP.COM\12_Obsidian\schoolsWP, mémoire longue)
└── SaaS : Anthropic, OpenAI, RapidAPI, DataForSEO, Firecrawl, ElevenLabs, HeyGen, Higgsfield,
        Apify, Skoatch, Stripe via FluentCart, Cloudflare, Google Workspace, Discord, Telegram x9
```

---

## Phase 00 - Pré-requis hors-machine

### Étape 0.1 - MFA audit

Manuel, 45 min. Activer 2FA TOTP (pas SMS) + recovery codes imprimés sur :

- GitHub, Anthropic Console, OpenAI Platform
- RapidAPI, DataForSEO, Firecrawl, Apify
- HeyGen, Higgsfield, ElevenLabs, Skoatch
- Cloudflare, EasyHoster, xCloud, Hostinger (autres apps)
- Google Workspace (compte michaelkihlpro@gmail.com)
- 1Password
- Stripe (compte connecté à FluentCart)
- Compte Microsoft du PC Windows 11 (clé du royaume côté dev)
- Telegram (cloud password sur le compte perso, pas juste les bots)

Livrable : `docs/security/00-mfa-status.md` avec date de dernière vérif des recovery codes par service.

### Étape 0.2 - Canal d'alerte hors-bande

Healthchecks.io free tier. Ping cron toutes les 5 min depuis n8n (un workflow vide schedule + HTTP). Destinataires :

- Email perso non-Gmail (sinon Google panne = silence)
- Numéro Telegram secondaire non lié à @schoolsWP_bot ou à la fleet schoolswp-agents

Logique : si le PC dev brûle, si schoolswp.com tombe, si Telegram principal compromis, ce canal alerte.

---

## Phase 01 - Reconnaissance (lecture seule)

### Étape 1 - Inventaire du PC Windows 11 de dev

Prompt à coller dans Claude Code :

```
Mode AUDIT LECTURE SEULE. Aucune modif.

Produis projects\schoolswp\docs\security\01-pc-inventory.md :

1. Process longs : Get-Process | Where-Object { $_.ProcessName -match "python|node|claude|n8n|docker" }
2. Tous les venv Python listés (Get-ChildItem -Recurse -Filter pyvenv.cfg sous projects\, _archive\, etc.)
3. .env trouvés (Get-ChildItem -Path D:\ -Recurse -File -Filter ".env*" -Force 2>$null,
   exclure node_modules / .venv / _archive).
   Pour chaque : chemin, owner (Get-Acl), nb de variables, KEYS uniquement (jamais les valeurs).
4. .claude\settings.local.json présents (workspace + user-level %USERPROFILE%\.claude\),
   nb de blocs env.
5. .mcp.json + .mcp.json.bak + .mcp.json.fluent + .mcp.backup.json : flag chaque fichier
   qui contient une clé en clair (juste KEY, pas la valeur).
6. Clés SSH : %USERPROFILE%\.ssh\, fingerprint (ssh-keygen -lf) + passphrase yes/no.
7. PATH custom (sortie de $env:PATH), repérer les dossiers writable par user qui sont
   AVANT C:\Windows\System32 (vecteur PATH hijack).
8. Apps PM2 locales si présentes (pm2 list).
9. Docker containers locaux (docker ps -a).
10. Captures de credentials Apify / DataForSEO dans .credentials\, .config\, AppData\Roaming\, etc.
11. Specifique Windows : tâches planifiées (Get-ScheduledTask), services tiers
    (Get-Service | Where-Object { $_.StartType -eq 'Automatic' -and $_.Status -eq 'Running' }
    + filtrer par DisplayName ou Path non-Microsoft).
12. Defender + autres antivirus actifs (Get-MpComputerStatus, Get-MpThreat history).

Ne lis JAMAIS .env ni .claude\settings.local.json avec le tool Read
(cf memory feedback_never_read_env.md). Utilise Get-Content avec Select-String -Pattern
sur les NOMS de clés uniquement, ou Measure-Object pour compter sans afficher les valeurs.

Section "Findings immédiats" classés CRITIQUE / ELEVE / MOYEN / FAIBLE.
"En attente validation pour étape 2."
```

### Étape 2 - Inventaire WordPress (schoolswp.com + michaelkihl.fr)

```
Mode AUDIT LECTURE SEULE.

Pour CHAQUE site WP (schoolswp.com via Novamira MCP, michaelkihl.fr via xCloud) :

Produis docs\security\02-wp-inventory-<site>.md avec :

1. Users + rôles + dernière connexion (SELECT user_login, user_email, user_registered
   FROM wp_users JOIN wp_usermeta WHERE meta_key='wp_capabilities').
   Pour chaque admin : MFA actif ? mot de passe app password en cours ?
2. Plugins actifs + versions + dernière MAJ + vulnérabilités connues
   (croiser avec WP Umbrella, qui a déjà le scan vulns en place : skill umbrella:health).
3. Thèmes : actif + inactifs (les inactifs sont aussi vecteurs).
4. Capacités personnalisées : SELECT meta_value FROM wp_options WHERE option_name='wp_user_roles'.
5. Endpoints REST exposés : wp-json/?rest_debug=1 si dispo, sinon lister namespaces standards
   + ceux des plugins (fluentcrm/v2, fluentboards/v2, fluent-cart, novamira, rank-math, etc.).
6. wp-config.php : présence de DISALLOW_FILE_EDIT, AUTOMATIC_UPDATER_DISABLED, FORCE_SSL_ADMIN,
   constantes SECUPRESS_*, WP_DEBUG (doit être false en prod), DB_HOST (pas en clair dans repo).
7. .user.ini / .htaccess racine : déjà documenté pour schoolswp.com (cf project_user_ini_schoolswp).
8. SecuPress modules actifs (cf reference_secupress_submodule_slugs pour les slugs réels),
   et flag les bugs connus (DCTS JS, cf reference_secupress_dcts_js_bug).
9. Mu-plugins présents (schoolswp-person-schema.php, schoolswp-ai-summary-buttons, FluentCampaign
   tag_based_redirect, etc.). Pour chacun : version + dernière modif.

Findings classés. "En attente validation."
```

### Étape 3 - Inventaire n8n

```
Mode AUDIT LECTURE SEULE.

Via MCP n8n-mcp (jamais via REST direct curl, cf reference_n8n_cloudflare_ua_block) :

Produis docs\security\03-n8n-inventory.md :

1. n8n_list_workflows : tous les workflows, status (actif/inactif), dernière exécution.
2. Pour chaque workflow actif : noeuds Webhook (URLs publiques exposées),
   nodes HTTP Request avec auth=none + header Authorization manuel (le workaround connu),
   nodes Code qui font des appels externes.
3. Credentials stockés (n8n_manage_credentials avec list) : type, owner, dernière update.
4. Variables d'env n8n custom (si lisibles via n8n_audit_instance).
5. Users n8n + rôles + dernière connexion.
6. Webhook URLs publiques : lister chacune et noter si signature validée côté n8n.
7. Workflows mortels potentiels : ceux qui font wp_update_post, qui touchent FluentCart,
   qui appellent Stripe, qui suppriment de la DB.

Findings classés. Flag spécialement : credentials qui doivent être migrées en
1Password / vault, workflows actifs qui n'ont pas tourné depuis > 90 jours
(souvent du cassé silencieux qui leak des token expirés en logs).
```

### Étape 4 - Inventaire secrets multi-niveaux

```
Mode AUDIT LECTURE SEULE. Le rapport NE DOIT JAMAIS contenir une valeur en clair,
seulement les 4 derniers chars pour identification.

Produis docs\security\04-secrets-inventory.md :

1. Tous les blocs `env` de .claude\settings.local.json (workspace + user-level).
   Pour chaque KEY : 4 derniers chars + à quel MCP server elle correspond.
2. Tous les .env trouvés à l'étape 1, KEY par KEY, même règle.
3. Backups .mcp.json (.bak, .fluent, .backup.json) : flag tout secret encore présent.
4. Historique Git de TOUS les repos schoolsWP-related :
   - projects\schoolswp\ + sous-modules
   - novamira\ + thruuu\ + skoatch tools
   - schoolswp-agents\
   gitleaks detect --no-banner --redact pour chaque. Le rapport liste fichier:ligne + secret type.
5. Credentials Google Workspace (.credentials\gsc-client-secrets.json), Telegram bots tokens,
   tokens dans configs n8n, tokens dans tools\wp-media-upload\, tokens HeyGen / ElevenLabs.
6. PAT GitHub utilisés : un par usage ? un seul global ? scopes minimaux ?
7. Credential Manager Windows (cmdkey /list) : tokens stockés (WP Umbrella par exemple,
   cf project_wp_umbrella_account).

Classification : LEAKED PUBLIC / LEAKED PRIVATE / AT REST UNENCRYPTED / PROPER.

À la fin "Liste rotation prioritaire" : tout LEAKED PUBLIC + tout ce qui touche
paiement (Stripe via FluentCart) + tout ce qui touche prod schoolswp.com.

ROTATION IMMEDIATE avant l'étape 5 pour tout LEAKED PUBLIC.
```

---

## Phase 02 - Backup non négociable

### Étape 5 - Backup WP + vault + repos avec restore drill

```
Mode REMEDIATION (plan -> validation -> exécution).

Mission : avant TOUT hardening, garantir qu'on peut tout restaurer.

À sauvegarder :
- WP schoolswp.com : DB + wp-content\ (uploads + plugins + themes) + wp-config.php.
  Méthode : WP Umbrella backup natif + 2e copie restic vers Backblaze B2.
- WP michaelkihl.fr : idem si pas déjà couvert par xCloud snapshot.
- n8n : export complet de tous les workflows en JSON via MCP n8n_list_workflows
  + n8n_get_workflow boucle. Stocker en dehors du repo (vault Obsidian
  00_systeme\claude-code-bridge\ NON, c'est public au sens vault. Mieux : 1Password
  vault dédié ou Backblaze chiffré).
- Vault Obsidian : restic vers Backblaze (la lib privée + le journal log.md).
- Repo schoolswp : déjà sur GitHub, on ajoute un mirror Backblaze hebdo.

Plan dans docs\security\05-backup-plan.md.

DRILL OBLIGATOIRE avant de passer à l'étape suivante :
1. Restore le backup WP schoolswp.com le plus récent dans un site WordPress Studio local
   (MCP wordpress-studio:site_import).
2. Vérifier : login admin OK, frontend OK, 3 articles aléatoires OK, FluentCRM contacts list non vide.
3. Restore un workflow n8n exporté dans une instance n8n locale (Docker Desktop Windows).
4. Documenter le temps total restore dans RESTORE-RUNBOOK.md.

RESTORE-RUNBOOK.md stocké à 3 endroits : repo, 1Password, imprimé papier.

Note Windows : restic.exe disponible via scoop install restic ou winget install restic.restic.
Pour le scheduling, Task Scheduler Windows (schtasks /create) plutôt que cron.
```

---

## Phase 03 - Hardening WordPress + n8n + Cloudflare

### Étape 6 - WP users + admin access

```
Mode REMEDIATION.

Plan dans docs\security\06-wp-users-plan.md :

1. Pour schoolswp.com + michaelkihl.fr :
   - Lister tous les users avec capability administrator, editor, shop_manager (FluentCart),
     fluentcrm_admin, instructor (TutorLMS).
   - Désactiver (user_status=1 ou supprimer) tout admin inutilisé.
   - Forcer reset password sur tous les admins actifs (via Novamira execute-php).
   - Vérifier qu'aucun admin n'a "Michael KIHL" comme user_login (cf reference_wp_username_login_vs_displayname,
     toujours email michaelkihlpro@gmail.com en login).
2. Désactiver tous les Application Passwords inutilisés.
3. SecuPress Login Protection : activer Limit Login Attempts (slug limitloginattempts,
   cf reference_secupress_submodule_slugs), 5 tentatives, 1h ban.
4. Cacher /wp-login.php derrière SecuPress "Login URL" (move login).
5. wp-config.php : DISALLOW_FILE_EDIT, DISALLOW_FILE_MODS (à arbitrer car bloque MAJ depuis UI),
   FORCE_SSL_ADMIN.
6. Pour FluentCart / TutorLMS / FluentCRM : audit des permissions custom, retirer toute capability
   accordée à des rôles non-admin par accident.

Attend OK avant d'appliquer. Commence par michaelkihl.fr (moins critique).
```

### Étape 7 - n8n access + Cloudflare

```
Plan dans docs\security\07-n8n-cloudflare-plan.md :

1. n8n UI schoolswp-n8n.wp1.host : audit qui peut s'y connecter (users n8n + auth basic devant).
   Objectif : passer derrière Cloudflare Access (Zero Trust free tier, 50 users) avec ma seule
   identité Google Workspace autorisée. Pas d'accès public direct.
2. Webhooks publics n8n (entrants Stripe, Telegram, Gelato callbacks, etc.) restent publics
   mais avec signature obligatoire. Audit workflow par workflow.
3. Cloudflare schoolswp.com :
   - SSL/TLS mode = Full (strict)
   - Always Use HTTPS = on
   - Min TLS 1.2
   - WAF managed rules + OWASP core rules
   - Bot Fight Mode
   - Rate limit /wp-login.php (10 req/min/IP), /wp-json/ (60 req/min/IP), /xmlrpc.php déjà 127.0.0.1
   - Page Rules : cache disabled pour /wp-admin/ et /wp-json/
4. Cloudflare michaelkihl.fr : audit similaire.

OK avant d'appliquer.
```

---

## Phase 04 - Secrets centralisés + rotation

### Étape 8 - Vault central (1Password recommandé)

```
Mode REMEDIATION.

Compare sops+age vs 1Password CLI pour mon profil :
- solo entrepreneur
- déjà abonné 1Password
- ~30 services à gérer (MCP, agents Python, n8n, WP, Stripe, etc.)
- pas de CI complexe (juste GitHub Actions sur projects\schoolswp)
- environnement Windows 11 (op.exe disponible via winget install AgileBits.1Password.CLI)

Recommandation attendue : 1Password CLI + service accounts pour MCP et agents Python,
sops + age uniquement si gain net démontré sur la traçabilité Git.

Plan dans docs\security\08-vault-plan.md :
1. Créer vaults 1Password séparés : schoolsWP-prod, schoolsWP-dev, schoolsWP-apis, schoolsWP-bots.
2. Service account 1Password pour le PC dev (lecture seule sur dev), un autre pour xCloud apps
   (lecture seule sur prod).
3. Migration progressive : commencer par 1 MCP (au choix : un qui n'est pas critique pour la prod
   immédiate, type apify ou higgsfield).
4. Le launcher .mjs pattern (cf reference_claude_code_secrets_storage) est compatible avec
   `op read "op://schoolsWP-apis/anthropic/credential"` au lieu de lire settings.local.json.
5. .claude\settings.local.json devient progressivement vide de secrets.
6. gitleaks pre-commit confirmé bloquant.
7. Drill : rotater un secret de test (clé Apify par exemple), valider que le launcher pick
   la nouvelle valeur sans relancer Claude Code.

OK avant d'appliquer. Pilote sur 1 MCP non-critique.
```

### Étape 9 - Rotation prioritaire

```
Runbook manuel, pas d'exécution Claude Code (je le fais dans chaque UI provider).

Produis docs\security\09-rotation-runbook.md, tableau :
Service | Clé actuelle (4 derniers) | Status leak | Scopes possibles côté provider |
Action (ROTATE/SCOPE/OK) | URL gestion | Ordre | Process qui consomme

Pour chaque provider, suggère :
- Anthropic : clé par "machine" (agents Python content_factory, brain_lite, fleet content-studio,
  fleet crm-automation, fleet seo-geo, fleet social-community, MCP claude-code-guide,
  Skoatch via tools\skoatch\). Spend limit mensuel par clé.
- OpenAI : par usage (GPT pour fallback, embeddings, image fallback).
- RapidAPI : déjà rotaté incident 2026-04-21, vérifier toujours pas leaked.
- Stripe via FluentCart : restricted keys avec scopes minimaux (pas de live secret key
  dans le repo, jamais).
- WP Application Passwords : un par tool (wp-media-upload, n8n, novamira MCP, Skoatch publisher).
- Telegram bots : 9 tokens, rotation impossible sans casser les bots, donc plutôt
  protéger leur stockage et auditer leur usage.

Ordre = LEAKED PUBLIC d'abord, puis paiement, puis prod, puis dev.
```

---

## Phase 05 - Agents Python + MCP

### Étape 10 - Sandbox + cost limits agents

```
Mode REMEDIATION (plan -> validation -> exécution).

Audit dans docs\security\10-agents-audit.md :
- 28 agents Python core\agents-py\ : chacun a quels tools ? quels appels externes ?
- 4 instances fleet schoolswp-agents\ : autonomes, quels droits FS ?
- ~28 MCP servers : chacun a quels tools, quel scope ?

Plan de remédiation :
1. Whitelist sortante des agents Python : sur Windows, le plus simple est un proxy HTTP
   local (Privoxy ou squid via WSL2) + variables d'env HTTPS_PROXY pointant dessus,
   ACL host-based. Alternative : Windows Defender Firewall avec règles outbound par
   exécutable (NetFirewallRule -Program "...python.exe"), mais granularité limitée.
2. Filesystem : agents Python tournent comme user Windows mais peuvent être confinés
   en lecture seule sur tout sauf content\articles\ + content\audits\ + logs\.
   Le vault Obsidian D:\MES SITES\... = read-only strict via permissions NTFS (icacls).
3. Cost limits par agent :
   - Chaque module CLI lit une clé Anthropic dédiée (1Password service account).
   - Spend limit Anthropic à 20 $/mois par clé non-critique, 100 $ pour content_factory.
   - Circuit breaker via flag file logs\circuit-breaker.flag :
     si > N appels en 1h ou > X $/jour, l'agent skip et alerte Telegram.
4. Audit log immuable des tool calls MCP : append-only sur logs\mcp-audit.log
   (sur Windows, NTFS deny-write-after-append n'existe pas nativement. Alternative :
   log shipping immédiat vers Datadog / Loki / Logtail free tier, et le local devient
   juste un cache).
5. Prompt injection defense :
   - Tous les inputs venant de Firecrawl, Apify, DataForSEO, web scraping, emails Gmail
     reçus, Telegram DMs : marqués <untrusted_content>...</untrusted_content> dans les prompts.
   - Aucun tool call déclenché par untrusted (pas d'action destructive type wp_update_post
     suite à une consigne extraite d'un article scrapé).

OK avant d'appliquer. Pilote sur un agent : niche_scout (moins critique, lit du web).
```

### Étape 11 - Validation inputs + anti prompt injection sur endpoints

```
Mission : sécuriser les surfaces qui acceptent de l'externe.

Endpoints à durcir :
- Webhooks n8n entrants (Stripe, Telegram, Gelato, HeyGen) : signature vérifiée AVANT parsing,
  rejet 401 + log Discord en cas d'échec.
- API REST des Python agents s'il y en a d'exposées (cf inventaire étape 5).
- WP REST custom (mu-plugins schoolsWP) : audit nonces + capabilities checks.
- Discord bot + Telegram bots : qui peut envoyer une commande qui déclenche un agent ?
  Whitelist users Telegram (uniquement mon ID).
- Skoatch webhooks publish : signature + restriction site_id (jamais 742 schoolswp.com,
  cf project_skoatch_setup).

Plan dans docs\security\11-input-validation-plan.md.
Pilote sur 1 webhook n8n.
```

---

## Phase 06 - Staging + CI

### Étape 12 - Staging WordPress local

WordPress Studio MCP est déjà installé et tourne sous Windows. Procédure :

- `site_create` schoolsWP-staging avec import du backup étape 5
- Anonymiser PII (FluentCRM contacts, FluentCart customers) via WP-CLI :
  `wp db query "UPDATE wp_fc_subscribers SET email = CONCAT('test+', id, '@example.com')"` etc.
- Auth basique en plus de l'auth WP
- Robots noindex via header
- Bannière "STAGING DATA EFFAÇABLE"

Plan dans `docs\security\12-staging-plan.md`. Drill mensuel : refresh du staging à partir du dump prod anonymisé.

### Étape 13 - CI security sur projects\schoolswp

GitHub Actions déjà en place. Ajouts :

- gitleaks sur chaque PR (déjà via pre-commit, ajouter en CI obligatoire bloquante)
- pip-audit dans le workflow
- semgrep config p/python
- script custom : reject si `.env*` ou `.mcp.json` autre que `.example` est dans le diff
- trivy fs `--severity HIGH,CRITICAL --skip-dirs node_modules,.venv,_archive`

---

## Phase 07 - Ops

### Étape 14 - Monitoring + alerting dual-channel

Sources à shipper :

- WP Umbrella alerts (already on)
- n8n executions failures (workflow dédié `monitor-self`)
- agents Python logs (`logs\agents.log` rotation déjà en place)
- xCloud apps PM2 logs (telegram-agents, discord-orchestrator)
- Cloudflare security events (export S3 si Pro, sinon polling daily)
- Discord webhook schoolsWP-Routines déjà configuré (cf reference_discord_webhook_routines)
- Windows Event Log dev PC (Get-WinEvent filtered sur Security / Application) :
  shipping optionnel si tu veux corréler une compromission PC

Alertes routées sur DEUX canaux :

- Principal : Discord #alerts + Telegram @schoolsWP_bot
- OOB : Healthchecks.io + email perso non-Gmail

Triggers obligatoires :

- Nouvelle connexion admin WP réussie
- > 5 échecs login WP en 5 min
- Spend Anthropic journalier > 30 $
- Échec backup WP Umbrella ou Backblaze
- Workflow n8n actif qui n'a pas tourné depuis 7j (mort silencieux)
- Status 5xx > 1 % sur schoolswp.com

### Étape 15 - Runbook incident schoolsWP-specific

`docs\security\15-INCIDENT-RUNBOOK.md`, scénarios spécifiques :

- "Clé Anthropic leakée" : révocation Console + check usage 30 derniers jours + rotate sur tous les agents
- "Admin WP compromis" : reset all passwords via Novamira execute-php + révoque all Application Passwords + audit wp_options pour backdoors + audit wp_users pour comptes ajoutés
- "FluentCart paiement frauduleux" : Stripe Dashboard + FluentCart logs + check si site compromis ou juste card testing
- "Agent Python qui s'emballe" : kill circuit-breaker.flag manuel + révoque clé Anthropic spécifique + post-mortem
- "n8n workflow malveillant" : désactiver l'instance entière via Cloudflare Access deny all + audit workflows + rotate credentials n8n
- "GitHub repo compromis" : révoque PAT + force push reset to known good + audit Actions secrets + audit workflows malicieux ajoutés
- "Vault Obsidian compromis" : git history du vault, rollback, audit log.md pour entries non-Michael
- "PC Windows 11 compromis" : déconnecter du réseau, Windows Defender Offline Scan, snapshot disque via dd/wbadmin pour forensique, révoquer toutes les clés API stockées localement (au minimum : Anthropic, Stripe, WP Application Passwords)

Contacts d'urgence : Anthropic security, EasyHoster support, xCloud support, registrar AFNIC, Cloudflare, Stripe.

### Étape 16 - Dashboard + maintenance

`docs\security\16-DASHBOARD.md` avec score par catégorie :
WP (admin/plugins/users), n8n, MCP/secrets, agents Python, Cloudflare, backups, monitoring, CI.

Calendrier récurrent :

- Quotidien : check Discord #alerts + check facture Anthropic
- Hebdo : revue WP Umbrella vulns + n8n executions failures
- Mensuel : restore drill (étape 5) + refresh staging anonymisé (étape 12) + revue accès admins WP
- Trimestriel : rotation clés API non-critiques + gitleaks full scan + WP plugins audit complet
- Annuel : audit complet (rejouer étapes 1-5) + revue threat model + audit providers SaaS (les MCP encore utilisés ?)

---

## Différences clés vs Security Briefing AFFISEO v1.1

- Pas d'étape SSH hardening : EasyHoster + xCloud gèrent. Tu n'as pas root sur la prod WP.
- L'équivalent c'est WP admin + n8n UI + Cloudflare Access.
- Beaucoup plus de SaaS donc l'enjeu central c'est secrets + scoping clés, pas hardening kernel.
- Le restore drill se fait dans WordPress Studio (MCP déjà en place), gain énorme vs setup Docker.
- SecuPress est déjà partiellement actif mais a des bugs documentés en mémoire : ne pas le réactiver aveuglément, suivre les notes.
- FluentCart = paiement réel = surface qui n'existe pas dans AFFISEO. Stripe restricted keys obligatoire.
- Adaptations Windows 11 : icacls au lieu de chmod, NetFirewallRule au lieu d'iptables, Task Scheduler au lieu de cron, Get-WinEvent au lieu de journalctl, Windows Credential Manager (cmdkey) pour les tokens stockés hors 1Password.

## Estimation temps réaliste

3 à 5 semaines en mode 1-2h/jour. Bloque les étapes 0 + 1 + 4 + 5 sur un weekend complet (recon + secrets + backup), le reste s'étale.

---

## Avant de démarrer

1. Crée la racine de l'audit dans le repo (PowerShell) :

```
New-Item -ItemType Directory -Force -Path docs\security\00-prereq, docs\security\01-recon, docs\security\02-secrets, docs\security\03-network, docs\security\04-wp, docs\security\05-api, docs\security\06-agents, docs\security\07-staging, docs\security\08-monitoring, docs\security\09-backup, docs\security\10-incident
```

2. Garde une 2e instance Claude Code ouverte pendant les phases qui touchent à l'accès WP, à n8n ou à Cloudflare.

3. Aucune étape en parallèle : un blocker = un rollback identifiable.

4. À chaque nouvelle session Claude Code sur cet audit, démarre par :
   > "Tu reprends l'audit sécurité schoolsWP. Lis docs\security\BRIEFING-v1.md et le rapport de l'étape précédente AVANT toute action."
