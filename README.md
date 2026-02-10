# schoolsWP — n8n Automation Framework

**Projet** : [schoolsWP](https://schoolswp.com) | **Version** : 1.0.0
**Owner** : Michael KIHL | **Licence** : Propriétaire

---

## Vue d'ensemble

Framework d'automatisation n8n pour schoolsWP avec support MCP (Model Context Protocol), workflows production-ready, scripts d'automatisation et monitoring intégré.

### Fonctionnalités clés

- ✅ **Documentation exhaustive** : 150+ pages de best practices
- ✅ **Gestion centralisée des erreurs** : Workflow Mission Control
- ✅ **Intégration MCP** : OttoKit, Firecrawl, Pabbly, DataForSEO
- ✅ **Scripts d'automatisation** : Backup, déploiement, monitoring
- ✅ **Stack monitoring** : Prometheus + Grafana
- ✅ **Templates prêts à l'emploi** : API, ETL, Scheduled, Event-driven, MCP
- ✅ **Version control** : Backup automatique Git

---

## Installation rapide

### Prérequis

- Node.js 18+ et npm
- PostgreSQL 15+ (recommandé pour production)
- Git
- OpenSSL
- jq (pour scripts de backup)

### Setup en 3 minutes

```bash
# 1. Exécuter le script de setup
bash scripts/setup-n8n-environment.sh prod

# 2. Configurer les MCP endpoints dans .env (optionnel)
nano .env

# 3. Démarrer n8n
n8n start
```

### Accès à n8n

- **URL** : http://localhost:5678
- **Username** : admin
- **Password** : _(affiché par le script de setup)_

---

## Structure du projet

```
.
├── Règles du jeu – automatisation n8n.md   # Document maître (150+ pages)
├── README.md                                # Ce fichier
├── .env.example                             # Template configuration
├── .gitignore                               # Exclusions Git
│
├── workflows/                               # Workflows n8n
│   ├── error-workflow-centralized.json     # ⭐ Workflow d'erreur centralisé
│   ├── template-api-integration.json       # Template API + MCP
│   ├── template-etl-data-transformation.json
│   ├── template-scheduled-task.json
│   ├── template-event-driven-webhook.json
│   ├── template-multi-agent-mcp.json
│   └── examples/                            # Exemples MCP
│       ├── ottokit-github-pr-automation.json
│       ├── firecrawl-web-scraping.json
│       ├── pabbly-workflow-sync.json
│       └── dataforseo-keyword-analysis.json
│
├── scripts/                                 # Scripts bash
│   ├── setup-n8n-environment.sh            # ⭐ Installation complète
│   ├── backup-n8n-workflows.sh             # ⭐ Backup automatique Git
│   ├── restore-n8n-workflows.sh            # Restauration workflows
│   ├── deploy-to-staging.sh                # Déploiement staging
│   ├── deploy-to-production.sh             # Déploiement production
│   └── health-check.sh                     # Health check n8n
│
├── config/                                  # Configurations
│   ├── docker-compose.yml                  # ⭐ Stack Docker complète
│   ├── prometheus.yml                      # Config Prometheus
│   └── grafana-dashboards/                 # Dashboards Grafana
│
└── docs/                                    # Documentation
    ├── quick-reference-naming.md
    ├── quick-reference-error-handling.md
    ├── quick-reference-mcp.md
    └── troubleshooting-guide.md
```

---

## Démarrage rapide

### 1. Import du workflow d'erreur centralisé

```bash
# Via n8n UI
1. Aller dans Workflows → Import
2. Sélectionner workflows/error-workflow-centralized.json
3. Configurer les credentials (Slack, PostgreSQL)
4. Activer le workflow
```

### 2. Configurer les autres workflows

```bash
# Restaurer tous les workflows
bash scripts/restore-n8n-workflows.sh
```

### 3. Configuration MCP (optionnel)

Éditer `.env` et ajouter vos endpoints MCP :

```bash
MCP_OTTOKIT_ENDPOINT=https://mcp.ottokit.com/mcp/YOUR_KEY
MCP_FIRECRAWL_API_KEY=fc-YOUR_KEY
MCP_PABBLY_ENDPOINT=https://connect.pabbly.com/mcp/YOUR_KEY
MCP_DATAFORSEO_LOGIN=your-email@example.com
MCP_DATAFORSEO_PASSWORD=your-password
```

### 4. Backup automatique

```bash
# Configurer cron pour backup quotidien à 2h
crontab -e

# Ajouter cette ligne :
0 2 * * * /chemin/vers/scripts/backup-n8n-workflows.sh
```

---

## Stack Docker (Recommandé)

### Démarrer la stack complète

```bash
cd config
docker-compose up -d
```

**Services inclus** :
- n8n (port 5678)
- PostgreSQL (port 5432)
- Prometheus (port 9090)
- Grafana (port 3000)

### Accès Grafana

- **URL** : http://localhost:3000
- **Username** : admin
- **Password** : _(voir GRAFANA_ADMIN_PASSWORD dans .env)_

---

## Commandes utiles

### n8n

```bash
# Démarrer n8n
n8n start

# Démarrer en mode verbose
n8n start --tunnel

# Exécuter un workflow
n8n execute --id=WORKFLOW_ID
```

### Backup & Restore

```bash
# Backup manuel
bash scripts/backup-n8n-workflows.sh

# Restaurer workflows
bash scripts/restore-n8n-workflows.sh

# Restaurer un workflow spécifique
bash scripts/restore-n8n-workflows.sh workflows/my-workflow.json
```

### Déploiement

```bash
# Déployer en staging
bash scripts/deploy-to-staging.sh

# Déployer en production (avec confirmation)
bash scripts/deploy-to-production.sh
```

### Health Check

```bash
# Vérifier si n8n est opérationnel
bash scripts/health-check.sh
```

---

## Conventions de nommage

### Workflows

**Format** : `[Status] Source > Destination: Description (ID)`

**Exemples** :
- `[Prod] Salesforce > PostgreSQL: Daily Sync (PROJ-123)`
- `[Staging] Gmail > Slack: Lead Notification`
- `[InDev] API > Transform > Database: Customer ETL`

**Status** :
- `[InDev]` : En développement
- `[InTesting]` : En test
- `[Staging]` : Pré-production
- `[Prod]` : Production
- `[Offline]` : Hors ligne
- `[ForDeletion]` : À supprimer

### Credentials

**Format** : `Service_Environment_Type`

**Exemples** :
- `Salesforce_Production_OAuth`
- `PostgreSQL_Staging_Password`
- `Stripe_Dev_APIKey`

---

## MCP Integration

### Workflows disponibles

1. **OttoKit** : Automatisation GitHub
   - Création PR automatique
   - Review assignment
   - Label management

2. **Firecrawl** : Web Scraping
   - Scraping planifié
   - Extraction de données
   - Monitoring concurrence

3. **Pabbly** : Synchronisation workflows
   - Sync bidirectionnelle
   - Conflict resolution

4. **DataForSEO** : Analyse SEO
   - Keyword research
   - Competitor analysis
   - Reporting automatisé

---

## Monitoring

### Métriques Prometheus

Accès : http://localhost:9090

**Requêtes utiles** :

```promql
# Taux d'erreur
sum(rate(n8n_workflow_executions_failed[5m])) / sum(rate(n8n_workflow_executions_total[5m]))

# Temps d'exécution moyen
rate(n8n_workflow_execution_duration_seconds_sum[5m]) / rate(n8n_workflow_execution_duration_seconds_count[5m])

# Workflows actifs
n8n_workflows_active
```

### Dashboards Grafana

3 dashboards pré-configurés :
- **Workflow Execution Overview** : Métriques d'exécution
- **Resource Utilization** : CPU, RAM, DB
- **Business Metrics** : Records processed, API calls

---

## Sécurité

### Checklist de sécurité

- [ ] `N8N_ENCRYPTION_KEY` généré et stocké sécurisement
- [ ] Authentification basique activée (`N8N_BASIC_AUTH_ACTIVE=true`)
- [ ] Mot de passe fort pour basic auth
- [ ] Fichier `.env` jamais committé (dans `.gitignore`)
- [ ] Credentials sanitizées avant backup Git
- [ ] PostgreSQL avec mot de passe fort
- [ ] Accès réseau restreint (firewall)
- [ ] HTTPS configuré pour production
- [ ] Rotation régulière des secrets (quarterly)

### Génération de secrets

```bash
# Encryption key
openssl rand -base64 32

# API key
openssl rand -hex 32

# JWT secret
openssl rand -base64 64
```

---

## Troubleshooting

### n8n ne démarre pas

```bash
# Vérifier les logs
n8n start --log-level=debug

# Vérifier la base de données
psql -U n8n_user -d n8n_prod -c "SELECT 1"

# Vérifier le port
lsof -i :5678
```

### Workflows ne s'exécutent pas

1. Vérifier que le workflow est actif
2. Vérifier les credentials
3. Consulter les logs d'exécution dans n8n UI
4. Vérifier le workflow d'erreur centralisé

### Backup échoue

```bash
# Vérifier que jq est installé
which jq

# Vérifier l'API key
echo $N8N_API_KEY

# Tester l'API manuellement
curl -H "X-N8N-API-KEY: $N8N_API_KEY" http://localhost:5678/api/v1/workflows
```

---

## Documentation complète

Pour la documentation exhaustive, voir :

📖 **[Règles du jeu – automatisation n8n.md](./Règles%20du%20jeu%20%E2%80%93%20automatisation%20n8n.md)**

**Sections disponibles** :
1. Introduction & Philosophy
2. Architecture Foundations
3. Naming Conventions
4. Error Handling & Resilience
5. MCP Integration Architecture
6. Security Best Practices
7. Development Workflow
8. Testing Strategies
9. Deployment Guidelines
10. Logging & Monitoring
11. Performance Optimization
12. Quality Standards
13. Workflow Templates & Patterns
14. Troubleshooting Guide
15. Maintenance & Lifecycle
16. Appendices

---

## Contribution

Voir [CONTRIBUTING.md](./CONTRIBUTING.md) pour le guide complet.

---

## Support

**Issues** : Utiliser le système de tickets Git
**Documentation** : Voir [Règles du jeu – automatisation n8n.md](./Règles%20du%20jeu%20%E2%80%93%20automatisation%20n8n.md)
**Logs** : `logs/` directory

---

## Licence

Propriétaire - Usage interne uniquement

---

**schoolsWP** — Michael KIHL | [schoolswp.com](https://schoolswp.com)
