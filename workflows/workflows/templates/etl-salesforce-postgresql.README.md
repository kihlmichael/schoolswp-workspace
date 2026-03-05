# Template: ETL Salesforce to PostgreSQL

**Nom complet** : `[Template] ETL: Salesforce to PostgreSQL Daily Sync`

Production-ready ETL workflow pour synchronisation quotidienne de données Salesforce vers PostgreSQL avec idempotency, distributed lock, validation et batch processing.

---

## 📋 Description

Ce template fournit un ETL complet avec:
- ✅ Schedule trigger (cron daily)
- ✅ Idempotency check (évite doubles exécutions)
- ✅ Distributed lock mechanism (évite runs concurrents)
- ✅ Salesforce OAuth2 authentication
- ✅ Input schema validation (Joi)
- ✅ Batch processing (100 items/batch)
- ✅ PostgreSQL UPSERT (deduplication automatique)
- ✅ Output schema validation
- ✅ Slack success notifications
- ✅ Error handling centralisé

---

## 🎯 Use Cases

- Synchronisation quotidienne Salesforce → PostgreSQL
- Migration de données CRM vers Data Warehouse
- Backup automatique données Salesforce
- Intégration Salesforce avec outils BI (Metabase, Tableau)

---

## 📦 Prérequis

### Infrastructure
- [ ] n8n 2.4.8+ installé et configuré
- [ ] PostgreSQL 12+ avec table `contacts` créée
- [ ] Salesforce account avec API access
- [ ] Network access: n8n → Salesforce API
- [ ] Network access: n8n → PostgreSQL

### Credentials requises

**1. Salesforce OAuth2**
```bash
# Dans n8n UI: Settings → Credentials → Add Credential → Salesforce OAuth2 API
Client ID: <your_salesforce_connected_app_client_id>
Client Secret: <your_salesforce_connected_app_client_secret>
Access Token URL: https://login.salesforce.com/services/oauth2/token
Auth URL: https://login.salesforce.com/services/oauth2/authorize
Scope: api refresh_token offline_access
```

**2. PostgreSQL**
```bash
# Dans n8n UI: Settings → Credentials → Add Credential → Postgres
Host: localhost (ou IP/hostname)
Database: your_database
User: your_user
Password: your_password
Port: 5432
SSL: Enabled (recommandé en prod)
```

**3. Slack OAuth2** (optionnel - notifications)
```bash
# Dans n8n UI: Settings → Credentials → Add Credential → Slack OAuth2 API
OAuth2 flow standard
Scopes: chat:write, channels:read
```

### Database Schema

Créer la table PostgreSQL:
```sql
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY,
  salesforce_id VARCHAR(18) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  phone VARCHAR(50),
  account_name VARCHAR(255),
  created_date TIMESTAMP,
  last_modified_date TIMESTAMP,
  synced_at TIMESTAMP DEFAULT NOW(),
  CONSTRAINT contacts_salesforce_id_key UNIQUE (salesforce_id)
);

-- Index pour performance
CREATE INDEX idx_contacts_salesforce_id ON contacts(salesforce_id);
CREATE INDEX idx_contacts_email ON contacts(email);
CREATE INDEX idx_contacts_synced_at ON contacts(synced_at);
```

### Environment Variables
```bash
# Required
SALESFORCE_QUERY="SELECT Id, Name, Email, Phone, Account.Name, CreatedDate, LastModifiedDate FROM Contact WHERE LastModifiedDate >= LAST_N_DAYS:1"

# Optional
SLACK_SUCCESS_CHANNEL=data-sync-success
BATCH_SIZE=100
LOCK_TIMEOUT_MS=3600000  # 1 hour
ETL_SCHEDULE=0 2 * * *    # 2:00 AM daily

# Error handling
ERROR_WEBHOOK_URL=https://your-n8n-instance.com/webhook/error-handler
```

---

## 🚀 Installation

### 1. Import Template

```bash
# Via n8n UI
Settings → Import Workflow → Select etl-salesforce-postgresql.json

# Via CLI
n8n import:workflow --input=./workflows/templates/etl-salesforce-postgresql.json
```

### 2. Configure Credentials

1. Ouvrir le workflow
2. **Salesforce Node** → Credentials → Sélectionner "Salesforce OAuth2 API"
3. **PostgreSQL Nodes** → Credentials → Sélectionner "Postgres"
4. **Slack Node** → Credentials → Sélectionner "Slack OAuth2 API"

### 3. Configure Schedule

Modifier le **Schedule Trigger** node:
```
# Format cron: minute hour day month weekday
0 2 * * *    # 2:00 AM daily (default)
0 */6 * * *  # Every 6 hours
0 0 * * 0    # Every Sunday at midnight
```

### 4. Test Execution

**Test manuel** (avant activation schedule):
1. Cliquer sur "Execute Workflow" (bouton play)
2. Vérifier les logs:
   - ✅ Lock acquired
   - ✅ Data fetched from Salesforce
   - ✅ Validation passed
   - ✅ Batch processing completed
   - ✅ PostgreSQL insert successful
   - ✅ Lock released
   - ✅ Slack notification sent

**Vérifier PostgreSQL**:
```sql
SELECT COUNT(*) FROM contacts;
SELECT * FROM contacts ORDER BY synced_at DESC LIMIT 10;
```

### 5. Activate Workflow

1. Cliquer sur "Active" toggle (en haut à droite)
2. Le workflow s'exécutera automatiquement selon le schedule

---

## 🎛️ Configuration

### Batch Size

Par défaut: **100 items par batch**

Ajuster selon:
- Volume de données (plus de données = batches plus petits)
- Mémoire disponible n8n
- Timeout PostgreSQL

```javascript
// Dans Code node "Batch Processing"
const BATCH_SIZE = 200; // Augmenter à 200
```

### SOQL Query Salesforce

Modifier la requête dans **Salesforce Node**:
```sql
-- Default: Contacts modifiés dans les dernières 24h
SELECT Id, Name, Email, Phone, Account.Name, CreatedDate, LastModifiedDate
FROM Contact
WHERE LastModifiedDate >= LAST_N_DAYS:1

-- Custom: Tous les contacts actifs
SELECT Id, Name, Email, Phone, Account.Name, CreatedDate, LastModifiedDate
FROM Contact
WHERE IsActive = true

-- Custom: Contacts d'un compte spécifique
SELECT Id, Name, Email, Phone, Account.Name, CreatedDate, LastModifiedDate
FROM Contact
WHERE Account.Name = 'Enterprise Corp'
```

### Idempotency Period

Par défaut: **1 exécution par jour**

Modifier dans Code node "Check Idempotency":
```javascript
// Run only once per day (default)
const today = new Date().toISOString().split('T')[0];

// Run only once per hour
const currentHour = new Date().toISOString().slice(0, 13); // YYYY-MM-DDTHH
```

### PostgreSQL UPSERT Behavior

Par défaut: **ON CONFLICT DO UPDATE** (update existing)

```sql
-- Default: Update on conflict
INSERT INTO contacts (...)
VALUES (...)
ON CONFLICT (salesforce_id)
DO UPDATE SET
  name = EXCLUDED.name,
  email = EXCLUDED.email,
  ...

-- Alternative: Skip on conflict
INSERT INTO contacts (...)
VALUES (...)
ON CONFLICT (salesforce_id) DO NOTHING;
```

---

## 📊 Monitoring

### Métriques Clés

Le workflow tracked automatiquement:
- **Execution time** (durée totale)
- **Records fetched** from Salesforce
- **Records inserted** into PostgreSQL
- **Records updated** (via UPSERT)
- **Batches processed**
- **Errors encountered**

### Logs PostgreSQL

Requête pour analyser syncs:
```sql
-- Derniers syncs
SELECT
  DATE(synced_at) as sync_date,
  COUNT(*) as records_synced,
  MIN(synced_at) as first_sync,
  MAX(synced_at) as last_sync
FROM contacts
GROUP BY DATE(synced_at)
ORDER BY sync_date DESC
LIMIT 30;

-- Contacts jamais synchronisés (detection problèmes)
SELECT * FROM contacts
WHERE synced_at IS NULL OR synced_at < NOW() - INTERVAL '7 days';
```

### Slack Notifications

Le workflow envoie automatiquement:
- ✅ **Success**: Nombre de records synchronisés, durée, timestamp
- ❌ **Failure**: Erreur détaillée via error workflow centralisé

---

## 🧪 Testing

### Test 1: Idempotency

```bash
# Exécuter 2 fois de suite manuellement
# Expected: 2ème exécution skippée avec message "Already completed for today"
```

### Test 2: Distributed Lock

```bash
# Lancer 2 exécutions simultanées (API n8n)
curl -X POST "http://localhost:5678/api/v1/workflows/<workflow-id>/execute"
curl -X POST "http://localhost:5678/api/v1/workflows/<workflow-id>/execute"

# Expected: 2ème exécution fail avec "ETL already running"
```

### Test 3: Validation Failure

Modifier temporairement le Joi schema pour forcer une erreur:
```javascript
const schema = Joi.object({
  Id: Joi.string().length(18).required(),
  Email: Joi.string().email().required() // Force tous les contacts à avoir email
});

// Expected: Validation error, workflow stopped, error logged
```

### Test 4: Batch Processing

```bash
# Vérifier que batches sont créés correctement
# Dans les logs, chercher: "Processing batch 1/5", "Processing batch 2/5", etc.
```

### Test 5: PostgreSQL UPSERT

```sql
-- Insérer manuellement un contact avec salesforce_id existant
INSERT INTO contacts (salesforce_id, name, email)
VALUES ('003XXXXXXXXXXXXXX', 'Old Name', 'old@example.com');

-- Exécuter le workflow
-- Expected: Le contact est mis à jour (pas de duplicate)

SELECT * FROM contacts WHERE salesforce_id = '003XXXXXXXXXXXXXX';
-- Should show updated data from Salesforce
```

---

## ✅ Checklist Production

### Security
- [ ] Salesforce OAuth2 credentials stockées dans n8n Credentials (pas hardcodées)
- [ ] PostgreSQL credentials avec mot de passe fort (min 16 chars)
- [ ] PostgreSQL SSL activé pour connexions
- [ ] Firewall rules: n8n IP → PostgreSQL IP autorisé uniquement
- [ ] Salesforce IP restrictions configurées (Security → Network Access)

### Performance
- [ ] Batch size optimisé (tests avec 50, 100, 200, 500)
- [ ] Index PostgreSQL créés (salesforce_id, email, synced_at)
- [ ] VACUUM et ANALYZE PostgreSQL planifiés (weekly)
- [ ] Lock timeout ajusté selon durée moyenne exécution

### Reliability
- [ ] Idempotency testée (double run = no duplicates)
- [ ] Distributed lock testé (concurrent runs = 1 succeeds)
- [ ] Error workflow configuré et testé
- [ ] Rollback plan documenté (restore from PostgreSQL backup)
- [ ] Monitoring actif (Grafana alerts sur failures)

### Data Quality
- [ ] Input validation schema Joi complet
- [ ] Output validation schema Joi complet
- [ ] Data sanitization (trim whitespace, normalize phone)
- [ ] NULL handling défini (skip, default value, error?)
- [ ] Duplicate detection vérifié (UPSERT sur salesforce_id)

### Observability
- [ ] Slack notifications testées (success + failure)
- [ ] Logs structurés (JSON format)
- [ ] Execution time trackée (baseline établie)
- [ ] Data volume trackée (records/day graphed)
- [ ] Error rate < 1% (monitored)

### Documentation
- [ ] Runbook créé (troubleshooting, common issues)
- [ ] Data dictionary (mapping Salesforce → PostgreSQL fields)
- [ ] Schedule documenté (cron expression + timezone)
- [ ] Contact on-call défini (escalation path)

---

## 🐛 Troubleshooting

### Problème: "ETL already running" error

**Symptôme**: Workflow fail avec lock error

**Causes**:
1. Exécution précédente n'a pas terminé (> 1 hour)
2. Lock pas released (crash during execution)

**Solution**:
```javascript
// Dans Code node "Check Idempotency"
// Reset lock manually
const locks = $getWorkflowStaticData('global').locks || {};
delete locks['etl_salesforce_postgresql_lock'];
$setWorkflowStaticData('global', { locks });
```

### Problème: Salesforce API rate limit exceeded

**Symptôme**: Error "REQUEST_LIMIT_EXCEEDED"

**Causes**:
- Trop de requêtes Salesforce dans la journée
- Autre intégrations consomment le quota

**Solution**:
1. Vérifier quota Salesforce: Setup → System Overview → API Usage
2. Réduire fréquence: 1x/day → 1x/week
3. Optimiser SOQL query (limiter champs, filtrer par date)

### Problème: PostgreSQL connection timeout

**Symptôme**: Error "connect ETIMEDOUT"

**Causes**:
- Firewall bloque n8n → PostgreSQL
- PostgreSQL max_connections atteint
- PostgreSQL service down

**Solution**:
```bash
# Test network connectivity
ping <postgresql-host>
telnet <postgresql-host> 5432

# Check PostgreSQL logs
tail -f /var/log/postgresql/postgresql-12-main.log

# Check max_connections
psql -c "SHOW max_connections;"
psql -c "SELECT count(*) FROM pg_stat_activity;"
```

### Problème: Validation errors fréquents

**Symptôme**: Beaucoup de contacts skipped

**Causes**:
- Joi schema trop strict
- Données Salesforce incomplètes (NULL values)

**Solution**:
```javascript
// Rendre champs optionnels
const schema = Joi.object({
  Id: Joi.string().length(18).required(),
  Name: Joi.string().min(1).required(),
  Email: Joi.string().email().optional().allow(null, ''), // Allow NULL
  Phone: Joi.string().optional().allow(null, '')
});
```

### Problème: Duplicate records in PostgreSQL

**Symptôme**: Même salesforce_id apparaît plusieurs fois

**Causes**:
- UNIQUE constraint pas créée sur salesforce_id
- UPSERT pas configuré correctement

**Solution**:
```sql
-- Add UNIQUE constraint
ALTER TABLE contacts
ADD CONSTRAINT contacts_salesforce_id_unique UNIQUE (salesforce_id);

-- Cleanup duplicates (keep most recent)
DELETE FROM contacts a USING contacts b
WHERE a.id < b.id
AND a.salesforce_id = b.salesforce_id;
```

---

## 📚 Références

- [Salesforce SOQL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/)
- [n8n Salesforce Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce/)
- [PostgreSQL UPSERT](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT)
- [Joi Validation](https://joi.dev/api/)

---

## 📄 License

MIT License - Voir fichier LICENSE principal

---

## 👥 Support

- Issues: https://github.com/your-repo/n8n-workflows/issues
- Docs: Voir "Règles du jeu – automatisation n8n.md"
- Contact: data-team@company.com
