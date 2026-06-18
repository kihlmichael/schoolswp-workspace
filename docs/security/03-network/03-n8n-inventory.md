# Etape 3 - Inventaire n8n

> Audit lecture seule via MCP n8n-mcp v2.51.3. Date : 2026-05-12.
> Instance : https://schoolswp-n8n.wp1.host
> Methode : n8n_audit_instance (built-in + custom scan 50+ regex) + n8n_list_workflows + n8n_manage_credentials.
> Aucune valeur secrete dans ce rapport.

---

## Resume executif

**377 findings totaux sur 65 workflows scannes** :

- **3 CRITIQUE** : secrets hardcodes detectes
- **10 ELEVE** : webhooks publics sans authentification sur workflows actifs
- **56 MOYEN** : erreurs handling absent + retention donnees + 4 emails hardcodes
- **308 FAIBLE** : retention executions excessive + nodes risque officiels (executeCommand etc.)

Constat marquants :

- **Instance n8n outdated** : 2.19.5 actuelle, 2.20.6 disponible (manque 1 update, peut contenir des CVE).
- **46 credentials stockees**, dont 29 inutilisees dans les 90 derniers jours (surface morte = vecteur d attaque).
- **216 nodes officiels potentiellement risques** scanned (executeCommand, HTTP avec injection, etc.).
- **3 community nodes** installes, non vetes par n8n.
- **publicApiEnabled = true** + **communityPackagesEnabled = true** + **telemetry diagnosticsEnabled = true**.
- **Aucun workflow ne touche FluentCart, Stripe, ou wp_update_post directement** sur le scope actif (donnees PII et financieres restent dans le perimetre WP).
- Mais : **3 workflows actifs ont des secrets hardcodes** (jwt_token, google_api_key) et **10 workflows actifs exposent des webhooks publics sans auth**.

---

## 1. Etat global de l instance

| Metric | Valeur |
|---|---|
| URL | https://schoolswp-n8n.wp1.host |
| Version n8n | 2.19.5 (latest 2.20.6, **a mettre a jour**) |
| Version MCP wrapper | 2.51.3 (a jour) |
| Total workflows | 65 |
| Actifs | 27 |
| Inactifs (non archives) | 17 |
| Archives | 21 |
| Total credentials | 46 |
| Credentials inutilisees recemment (>90j) | 29 |
| Findings totaux | 377 |

**Security settings n8n :**

- `communityPackagesEnabled` = true (permet d installer des nodes non-vetes, surface d attaque)
- `publicApiEnabled` = true (API publique active, ce qui permet ce meme audit, double tranchant)
- `telemetry.diagnosticsEnabled` = true (envoie des stats a n8n.io, fuite potentielle de noms de workflows)
- `templatesEnabled` = true (catalogue de templates utilisable)
- `nodesExclude` actif sur 4 nodes : executeCommand, localFileTrigger, e2eTest, dynamicCredentialCheck (**bon point** : nodes destructifs deja interdits)

---

## 2. CRITIQUE - Secrets hardcodes (3)

| Workflow ID | Workflow | Node | Type secret | Status |
|---|---|---|---|---|
| `BStRQkYKRv6VcRsf` | [InDev] LinkedIn Post > Claude: Prospecting Pipeline V4 | `Code: Validate Inputs & Auth` | jwt_token | **ACTIF** |
| `iXR2tvSfd5L9zE2t` | [Prod] Schedule > n8n: Workflows Backup | `Get All Workflows` | jwt_token | **ACTIF** |
| `nmXNUqXgmKVcrjsJ` | [InDev] Google Drive > Gemini: Organisateur Photos Vacances | `Analyser avec Gemini` | google_api_key | Inactif |

**Risque** :

- `iXR2tvSfd5L9zE2t` **Workflows Backup** est actif et stocke un jwt_token n8n-API en clair dans le node. Si le workflow est exporte (cf [Prod] Schedule > n8n: Workflows Backup qui justement exporte tous les workflows en JSON), le secret est dans le dump.
- `BStRQkYKRv6VcRsf` **Prospecting Pipeline V4** est actif **ET** expose un webhook public sans auth (voir section suivante). Combo : webhook public + jwt hardcoded dans le code = chemin d exploitation direct.
- `nmXNUqXgmKVcrjsJ` est inactif mais le google_api_key reste sur disque.

**Fix** (auto-fixable par le MCP n8n) :

1. `n8n_get_workflow` pour extraire la valeur.
2. `n8n_manage_credentials({action: 'create'})` pour creer une credential typee.
3. `n8n_update_partial_workflow` pour remplacer le secret par la reference credential.
4. Rotater le secret cote provider (jwt n8n + google_api_key) car deja stocke en clair = compromis par precaution.

---

## 3. ELEVE - Webhooks publics sans authentification (10 actifs)

Tous les webhooks suivants sont **actifs en prod ou InDev** et acceptent des requetes anonymes. Un attaquant qui devine l URL peut declencher le workflow.

| Workflow ID | Workflow | Node webhook | Impact si exploite |
|---|---|---|---|
| `BStRQkYKRv6VcRsf` | LinkedIn Post > Claude: Prospecting Pipeline V4 | Webhook: Receive Post URL | Trigger pipeline Claude (cout LLM) + jwt hardcoded expose |
| `WocLwnUAZPaZFitG` | Agent Orchestrator: Callback > Process Result | Webhook: Agent Callback | Empoisonnement de l orchestrator (false callbacks) |
| `krF2AcxO9sXBimLI` | Claude Skills > Google Sheets: Audit & Inventory Sync | Skills Audit Webhook | Triggers Google Sheets writes + Claude calls |
| `np4OG9UGDCGWaK4H` | Webhook > Discord: Tutor LMS Docs Watcher | Webhook PS1 receiver | Injection de notifications Discord arbitraires |
| `3JE0YzrhoiusJZ6T` | Webhook > Google Sheets: GEO Architect Bulk Fill | Webhook | Trigger ecritures Sheets + Claude calls |
| `Im1Khan3gJwhJkuu` | Webhook > Google Sheets: Thruuu Monitoring Results | Webhook | Pollution donnees Thruuu monitoring |
| `sLsPkcU3faV727dM` | YouTube > Kie.ai: Thumbnail Generator | webhook_trigger | Cout Kie.ai burn (videos) |
| `6utQzJcmXQczrHag` | Claude > Google Sheets: Skills Registry Sync | Webhook | Pollution registry skills + cout Claude |
| `CDuKpLL7E6LuaWNT` | Hub Drive > Auto Sync README Index | Webhook: On Demand | Trigger sync Drive + writes README |
| `MveNwfDlvVYYZTwz` | [Staging] Webhook: MIGRATION schoolswp | Webhook | Creation arborescence Drive arbitraire |

**Comment ils sont decouverts en pratique** :

- URL n8n webhooks suit le pattern `https://schoolswp-n8n.wp1.host/webhook/<uuid>` ou `/webhook-test/<uuid>`.
- Si une URL fuite dans un repo public ou un transcript (Telegram, n8n exports, captures d ecran), elle est expoitable directement.
- Pas de protection IP. Pas de signature. Pas de rate limit n8n natif.

**Fix** (auto-fixable par le MCP) :

1. Pour chaque webhook : `n8n_manage_credentials({action: 'create', type: 'httpHeaderAuth'})` avec un secret random.
2. `n8n_update_partial_workflow` pour configurer `authentication: 'headerAuth'` sur le node Webhook.
3. Cote consumer (ce qui appelle le webhook) : mettre a jour avec l en-tete d auth.

**Cas particulier** : pour les webhooks qui recoivent des callbacks de SaaS tiers (Skoatch, HeyGen, etc.) qui n acceptent pas custom headers, mettre une signature HMAC dans la payload + verifier dans le node Code juste apres.

---

## 4. MOYEN - Emails hardcodes dans 4 workflows

| Workflow ID | Workflow | Node | Email |
|---|---|---|---|
| `PkFO7Of9BrMfl8Ed` | [InDev] Google Drive Auto-Rename on Move | Alert Email | (a verifier) |
| `RQZnUp6C1qC82Q7K` | [InDev] Schedule > Pinterest | Envoyer Notification | (a verifier) |
| `ls46UbBJJuZCobfI` | [InDev] YouTube schoolsWP Analyse | Gmail Notification | (a verifier) |
| `NZMJOfiaNPqyAajd` | [Prod] WP Articles Content Fill v5 | Send a message | (a verifier) |

Faible criticite mais polluant pour le RGPD si l email est celui d un tiers. A externaliser en credential ou variable d environnement n8n.

---

## 5. Credentials stockees (46)

### Inventaire par usage

**Top 5 les plus utilisees** :

| Credential | Type | Workflows | Notes |
|---|---|---|---|
| Google Sheets - schoolsWP v2 | googleSheetsOAuth2 | 28 | colonne vertebrale data des workflows |
| Anthropic account | anthropicApi | 12 | duplique avec Anthropic_Production_ApiKey (3) = **consolider** |
| Google Drive - schoolsWP v2 | googleDriveOAuth2 | 11 | |
| Gmail - schoolsWP | gmailOAuth2 | 8 | duplique avec Gmail - schoolsWP v2 (1) = a unifier |
| n8n - schoolsWP (OpenAI) | openAiApi | 8 | |

**Credentials orphelines (usageCount = 0) - 17 trouvees** :

- `DataForSEO_Production_BasicAuth` (cree 2026-05-07, jamais utilisee, **a supprimer**)
- `SerpApi`, `Exa.AI`, `Wisewand`, `Brevo`, `Perplexity`, `Slack account`
- `Gemini_Production_API`, `Google Gemini(PaLM) Api account` (doublon Gemini)
- `Google Analytics - schoolsWP v2`, `Google Calendar - schoolsWP v2`, `Google Contacts - schoolsWP v2`
- `Google Sheets Trigger - schoolsWP`, `Google BigQuery - schoolsWP`, `YouTube - schoolsWP`
- `Agent Orchestrator Callback`, `Thruuu Monitoring Results`, `GEO Architect Bulk Fill`
- `QdrantApi - schoolsWP`

Toutes ces credentials :

1. **Auraient pu etre utilisees par un workflow qui n est plus actif**. Si oui, la credential reste valide cote provider mais sans usage = surface morte. Recommandation : supprimer la credential cote n8n + rotater la cle cote provider si elle a > 90 jours.
2. **Doublons clairs a consolider** :
    - Anthropic_Production_ApiKey + Anthropic account = un seul
    - Gemini_Production_API + Google Gemini(PaLM) Api account = un seul
    - Gmail - schoolsWP + Gmail - schoolsWP v2 = un seul
    - Google Drive - schoolsWP + Google Drive - schoolsWP v2 = un seul
    - Google Docs - schoolsWP + Google Docs - schoolsWP v2 = un seul

Apres consolidation, ~10 credentials a supprimer (estimation).

---

## 6. Nodes risques

**216 nodes officiels risques** ont ete detectes (HTTP Request, Code/Function, jsonata, etc.) qui peuvent fetcher et executer du code arbitraire. Le `nodesExclude` actuel bloque 4 nodes (executeCommand, localFileTrigger, e2eTest, dynamicCredentialCheck) : bon point.

**3 community nodes** installes. Non identifies dans l audit, mais a verifier dans n8n UI > Settings > Community Nodes. Risque : code tiers non vete avec acces complet a l instance.

---

## 7. Findings classes

### CRITIQUE

1. **3 secrets hardcodes dans des workflows**
   2 jwt_token (workflows actifs) + 1 google_api_key (workflow inactif). Auto-fixable via n8n_manage_credentials.

2. **n8n outdated v2.19.5**
   Manque 1 update vers 2.20.6 qui peut contenir des CVE. Update via xCloud panel ou commande directe.

3. **N8N_ENCRYPTION_KEY en clair dans systems/n8n/.env**
   Deja note a l etape 1. Cle maitre qui chiffre toutes les 46 credentials stockees. Compromission = decryption complete.

### ELEVE

4. **10 webhooks publics sans authentification sur workflows actifs**
   Voir section 3. Auto-fixable via httpHeaderAuth + secret random.

5. **publicApiEnabled = true**
   L API publique n8n est ouverte. Indispensable pour ce MCP, mais expose une surface qui doit etre protegee derriere Cloudflare Access (etape 7 du briefing).

6. **communityPackagesEnabled = true + 3 community nodes installes**
   Verifier quels packages sont actifs et leur reputation.

7. **29 credentials non-utilisees > 90 jours**
   Tokens valides cote provider mais zero usage cote n8n. Supprimer + rotater (auto- ou semi-auto via n8n_manage_credentials).

8. **Aucune politique de retention executions configuree**
   10 workflows flagges. Les payloads des executions (qui peuvent contenir PII via Gmail/FluentCRM/etc.) sont retenus indefiniment. Configurer dans n8n Settings > Executions.

9. **n8n basic auth password en clair dans systems/n8n/.env**
   Deja note etape 1.

### MOYEN

10. **48 workflows sans error handling**
    Pas d Error Trigger node. Les erreurs partent en silence ou en email Owner par defaut. Ajouter au minimum une notification Telegram/Discord sur les workflows critiques.

11. **4 emails hardcodes dans des nodes**
    Section 4. Faible mais pollue le RGPD.

12. **Doublons de credentials (Anthropic x2, Gmail x2, Drive x2, Docs x2, Gemini x2)**
    Source de confusion + rotation manquee si on ne rote qu une des deux. Consolider.

13. **17 workflows inactifs non archives**
    Bruit cognitif. Soit reactiver, soit archiver (`isArchived=true`).

14. **telemetry.diagnosticsEnabled = true**
    Stats envoyees a n8n.io. Pas critique mais leak de meta-info (noms workflows). A desactiver si paranoid.

### FAIBLE

15. **Retention executions excessive sur 10 workflows**
    Lie a #8. Faible parce que pas de PII massive, mais a nettoyer.

16. **21 workflows archives**
    Hygiene normale. A purger periodiquement si tu n y reviens jamais.

---

## 8. Workflows actifs : analyse par criticite

**Workflows actifs qui touchent l infra schoolswp.com** (mutations potentielles) :

- `DcbnlLoedzX2lVIJ` [Staging] WordPress > Google Sheets: Sync & Classify Blog Posts (lecture seule WP -> ecriture Sheets)
- `NZMJOfiaNPqyAajd` [Prod] WP Articles > Google Docs: Content Fill v5 (lecture WP -> ecriture Docs)
- `RQZnUp6C1qC82Q7K` [InDev] Schedule > Pinterest: Auto-Generate Pins on New Article (lecture WP -> ecriture Pinterest)
- `ktrlXAI5szH3lr8F` [Prod] Sheets > AI Agents: Veille Plugins schoolsWP W206 (Firecrawl + Sheets)
- `iXR2tvSfd5L9zE2t` [Prod] Schedule > n8n: Workflows Backup (lit tous workflows + jwt_token hardcoded)

**Bon point** : aucun workflow ne fait wp_update_post / wp_insert_post / FluentCart mutations / Stripe ops. Les mutations WP critiques restent dans WP (mu-plugins + dashboard admin + Novamira MCP execute-php quand actif).

**Workflows agents tres lies a Claude API (cout LLM)** :

- 12 workflows actifs utilisent la credential `Anthropic account`. Un attaquant qui controle un webhook public peut burn ton credit Anthropic.
- Aucun spend limit n8n natif. Mitigation : limit cote Anthropic Console + monitoring usage quotidien.

---

## 9. Recommandations actionnables

### A faire en 1 session focus n8n (estimation 2-3 heures)

1. **Update n8n vers 2.20.6** (via xCloud panel) - 10 min
2. **Auto-fix 3 hardcoded secrets** via le MCP (creer credentials, remplacer dans nodes, rotater cote provider) - 30 min
3. **Auto-fix 10 webhooks publics** en ajoutant httpHeaderAuth a chacun - 1h
4. **Supprimer 17 credentials orphelines** (apres avoir verifie qu aucun workflow inactif ne les utilise) - 20 min
5. **Consolider 5 doublons de credentials** (Anthropic, Gmail, Drive, Docs, Gemini) - 20 min
6. **Archiver 17 workflows inactifs non archives** - 5 min

### A faire en suivi (semaine 2)

7. **Cloudflare Access devant l UI n8n** (etape 7 briefing) - retire l acces public au panel n8n.
8. **Configurer execution data pruning** dans n8n Settings (max 7-14 jours).
9. **Mettre n8n derriere un firewall qui restreint /webhook/* a Cloudflare IPs** + rate limit Cloudflare sur ces routes.
10. **Audit des 3 community nodes installes** (n8n UI > Settings).
11. **Spend limit Anthropic dedie au workflow `BStRQkYKRv6VcRsf`** + alerte si depasse seuil.

### Bloqueurs sans modification

- L upgrade n8n peut casser des workflows si breaking changes (rare entre patches mineurs). A faire un samedi avec un rollback xCloud snapshot prepret.
- Ajouter auth aux webhooks publics impose de mettre a jour les consumers (apps schoolswp-agents Mac, autres workflows, Skoatch, etc.). Mapping precis a faire avant.

## Etape 3 terminee. En attente validation pour etape 4 (secrets multi-niveaux).
