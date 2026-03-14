# n8n — Audit SEO Mensuel schoolsWP

Workflow d'automatisation qui génère un rapport PDF d'audit SEO chaque 20 du mois (Europe/Paris), avec archivage local, envoi email et notification Slack.

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│  Stack Docker (docker-compose.yml)                    │
│                                                       │
│  ┌─────────┐   ┌──────────────┐   ┌──────────────┐  │
│  │   n8n   │──▶│  pdf-service │   │  PostgreSQL  │  │
│  │ :5678   │   │    :3001     │   │    :5432     │  │
│  └─────────┘   └──────────────┘   └──────────────┘  │
│       │                                               │
│  volume: ./artifacts/ (PDFs de sortie)               │
│  volume: ../report/   (template + schema, read-only) │
└──────────────────────────────────────────────────────┘
```

---

## 1. Setup rapide

### Prérequis
- Docker + Docker Compose v2
- 2 Go RAM minimum

### Installation

```bash
# 1. Copier et remplir les variables d'environnement
cp n8n/.env.example n8n/.env
# Éditer n8n/.env (voir section Variables ci-dessous)

# 2. Créer le dossier d'artefacts
mkdir -p artifacts

# 3. Démarrer la stack
docker compose -f n8n/docker-compose.yml --env-file n8n/.env up -d

# 4. Vérifier que tout tourne
docker compose -f n8n/docker-compose.yml ps

# 5. Ouvrir n8n
open http://localhost:5678
```

### Importer le workflow

```bash
# Via CLI n8n (dans le container)
docker exec -it schoolswp-n8n n8n import:workflow \
  --input=/home/node/.n8n/workflows/audit-monthly.json

# OU via l'UI : Settings → Import from file → audit-monthly.json
```

---

## 2. Variables d'environnement (.env)

| Variable | Défaut | Description |
|---|---|---|
| `GENERIC_TIMEZONE` | `Europe/Paris` | **CRITIQUE** — timezone du scheduler |
| `TZ` | `Europe/Paris` | Timezone système du container |
| `TARGET_DOMAIN` | `schoolswp.com` | Domaine analysé |
| `DATAFORSEO_DRY_RUN` | `false` | `true` = données mock (tests) |
| `FORCE_RERUN` | `false` | `true` = ignore l'idempotence |
| `DATAFORSEO_LOGIN` | — | Login API DataForSEO |
| `DATAFORSEO_PASSWORD` | — | Password API DataForSEO |
| `DATAFORSEO_LOCATION` | `France` | Localisation (nom complet, ex: `France`) |
| `DATAFORSEO_LANGUAGE` | `French` | Langue (nom complet, ex: `French`, pas `fr`) |
| `OPENAI_API_KEY` | — | Clé API OpenAI |
| `OPENAI_MODEL` | `gpt-4o-mini` | Modèle OpenAI |
| `SMTP_HOST` | — | Serveur SMTP |
| `SMTP_FROM` | — | Adresse expéditeur |
| `REPORT_EMAIL_TO` | — | Destinataire du rapport |
| `SLACK_WEBHOOK_URL` | — | Webhook Slack (optionnel) |
| `ARTIFACTS_PATH` | `/artifacts` | Chemin de sortie des PDFs |
| `PDF_SERVICE_URL` | `http://pdf-service:3001` | URL du service PDF |

---

## 3. Scheduling & Timezone

### Expression cron
```
0 9 20-22 * *
```
Déclenche à **09h00** les jours **20, 21 et 22** de chaque mois.

### Règle week-end (implémentée dans le node "Build Config")
| Si le 20 tombe un... | Run effectif le... |
|---|---|
| Lundi–Vendredi | 20 (normal) |
| Samedi | 22 (lundi suivant) |
| Dimanche | 21 (lundi suivant) |

Le trigger déclenche 3 jours consécutifs, mais la logique interne ne laisse passer qu'**un seul jour valide par mois**, renforcé par le garde-fou idempotence.

### Configuration timezone
La timezone est contrôlée **uniquement** via les variables Docker :
```yaml
TZ=Europe/Paris
GENERIC_TIMEZONE=Europe/Paris
```
Pas de configuration supplémentaire nécessaire dans le workflow — `GENERIC_TIMEZONE` est reconnue nativement par n8n.

---

## 4. Idempotence

Le workflow utilise `$getWorkflowStaticData('global')` pour persister un registre des rapports générés.

```
Avant génération → vérifier si audit-YYYY-MM déjà dans staticData
  → Si oui et FORCE_RERUN=false → stop silencieux
  → Si oui et FORCE_RERUN=true  → relance complète
  → Si non → génération normale
Après succès → enregistrer { completedAt, pdfPath, pdfSizeKb }
```

**Résultat** : même si le trigger se déclenche 3 jours consécutifs (jours 20–22), le rapport n'est généré qu'une seule fois par mois.

---

## 5. Dry run (test sans APIs)

```bash
# Option A : script automatisé
bash scripts/dry-run.sh

# Option B : via n8n UI
# 1. Ouvrir le workflow dans l'éditeur
# 2. Cliquer "Test workflow" sur le Manual Trigger
# (DATAFORSEO_DRY_RUN=true dans .env requis)

# Option C : via CLI
docker exec -it schoolswp-n8n \
  n8n execute --id=<WORKFLOW_ID>
```

**Prérequis dry run :**
- `DATAFORSEO_DRY_RUN=true` dans `.env`
- `OPENAI_API_KEY` valide (l'analyse IA est réelle même en dry run)
- pdf-service démarré

---

## 6. Relance manuelle

### Via UI n8n
Ouvrir le workflow → cliquer le bouton **"Test workflow"** sur le nœud `Manual Trigger`.

### Via script
```bash
# Relance normale (respecte l'idempotence)
bash scripts/dry-run.sh

# Forcer même si rapport déjà généré ce mois
bash scripts/dry-run.sh --force
# OU : modifier FORCE_RERUN=true dans .env
```

### Via API n8n
```bash
curl -u admin:password \
  -X POST http://localhost:5678/api/v1/workflows/<ID>/execute \
  -H "Content-Type: application/json" \
  -d '{"data": {"_forceRun": true}}'
```

---

## 7. Données réelles (production)

La collecte DataForSEO est **entièrement câblée** dans le workflow. L'architecture de collecte est :

```text
IF: Dry Run? ──true──▶ Mock Data ──────────────────────────────────▶ Normalize Data
             └─false─▶ DFS: Domain Rank ▶ DFS: Ranked Keywords ──▶ Normalize Data
                                        ▶ DFS: Competitors     ↗
                                        ▶ DFS: Lighthouse      ↗
                                          Build Collected Data ↗
```

### Endpoints DataForSEO appelés (mode production)

| Node | Endpoint |
| --- | --- |
| `DFS: Domain Rank` | `POST /v3/dataforseo_labs/google/domain_rank_overview/live` |
| `DFS: Ranked Keywords` | `POST /v3/dataforseo_labs/google/ranked_keywords/live` (top 20, tri ETV desc) |
| `DFS: Competitors` | `POST /v3/dataforseo_labs/google/competitors_domain/live` (top 10) |
| `DFS: Lighthouse` | `POST /v3/on_page/lighthouse/live` |

Authentification : Basic Auth via `btoa(DATAFORSEO_LOGIN + ':' + DATAFORSEO_PASSWORD)` dans le header Authorization.

Pour activer la collecte réelle : `DATAFORSEO_DRY_RUN=false` dans `.env`.

---

## 8. Plan de tests

| Scénario | Test | Résultat attendu |
|---|---|---|
| Données manquantes | `Collect Data` retourne `{}` | Erreur claire dans `Normalize Data` |
| API DataForSEO down | Mock HTTP 503 | Retry x3 → alerte Slack/email |
| PDF Service down | Stopper le container | Retry x3 → workflow en erreur |
| OpenAI down / quota | Mock HTTP 429 | Retry x3 → ai_analysis vide (dégradé) |
| Email SMTP KO | SMTP credentials invalides | Workflow continue, alerte Slack |
| Règle week-end | Exécuter un 21 où le 20 était dimanche | `shouldRun=true`, rapport généré |
| Règle week-end (inverse) | Exécuter un 21 où le 20 était lundi | `shouldRun=false`, stop silencieux |
| Idempotence — 1er run | Run normal | PDF généré, staticData mis à jour |
| Idempotence — 2ème run | Run le même mois | Stop "Already Done", aucun doublon |
| FORCE_RERUN | 2ème run + `FORCE_RERUN=true` | Rapport regénéré, ancien écrasé |

---

## 9. Checklist mise en production

### Secrets & Credentials
- [ ] `.env` rempli et **non versionné** (`.gitignore` vérifié)
- [ ] Credentials SMTP créés dans n8n (Settings → Credentials)
- [ ] `N8N_ENCRYPTION_KEY` générée (ex: `openssl rand -hex 32`)
- [ ] `N8N_BASIC_AUTH_PASSWORD` fort (min 16 chars)

### Infrastructure
- [ ] Volume `./artifacts` créé et writable
- [ ] `pdf-service` healthcheck vert (`docker compose ps`)
- [ ] Firewall : port 5678 accessible uniquement en interne ou via proxy

### Workflow
- [ ] Workflow importé et **activé** (toggle en haut à droite)
- [ ] Dry run réussi (`bash scripts/dry-run.sh`)
- [ ] Email de test reçu
- [ ] Notification Slack testée

### Monitoring
- [ ] Logs n8n configurés (`N8N_LOG_LEVEL=info`)
- [ ] Rotation des logs Docker configurée (`--log-opt max-size=10m`)
- [ ] Alerte email/Slack sur échec workflow configurée dans n8n (Settings → Error Workflow)

### Backup
- [ ] Volume `n8n_data` sauvegardé (contient credentials + static data)
- [ ] Volume `postgres_data` sauvegardé
- [ ] `./artifacts/*.pdf` archivés (S3 ou autre)

---

## 10. Troubleshooting

### n8n ne démarre pas
```bash
docker compose -f n8n/docker-compose.yml logs n8n --tail 50
# Vérifier: DB_POSTGRESDB_PASSWORD renseigné dans .env
```

### PDF non généré
```bash
docker logs schoolswp-pdf-service --tail 30
curl -X POST http://localhost:3001/generate \
  -H "Content-Type: application/json" \
  -d '{"html": "<h1>Test</h1>"}'
```

### Workflow ne se déclenche pas le 20
```bash
# Vérifier la timezone dans le container
docker exec schoolswp-n8n date
# Doit afficher l'heure Paris, pas UTC
```

### Rapport déjà généré / impossible de relancer
```bash
# Option 1 : FORCE_RERUN=true dans .env + redémarrer
# Option 2 : effacer le staticData via l'API n8n
# Option 3 : dans l'éditeur n8n, Settings du workflow → Reset Static Data
```

### Réinitialiser le registre d'idempotence
Dans l'UI n8n → ouvrir le workflow → menu "..." → "Settings" → "Reset static data"

---

## Structure des fichiers

```
n8n/
├── docker-compose.yml        Stack Docker (n8n + pdf-service + postgres)
├── .env.example              Template des variables (copier en .env)
├── workflows/
│   └── audit-monthly.json    Workflow importable n8n
└── README.md                 Ce fichier

report/
├── template.html             Template HTML du rapport (placeholders {{...}})
└── schema.json               Schéma JSON normalisé des données d'audit

scripts/
├── pdf-service/
│   ├── Dockerfile            Image Playwright/Chromium
│   ├── server.js             API Express → génération PDF
│   └── package.json          Dépendances Node.js
└── dry-run.sh                Script de test end-to-end

artifacts/                    PDFs générés (gitignored)
└── audit-YYYY-MM.pdf
```
