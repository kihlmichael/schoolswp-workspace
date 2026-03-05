# Template: Error Handler Mission Control Enhanced

**Nom complet** : `[Template] Error Handler: Mission Control Enhanced`

Production-ready centralized error handling workflow avec severity classification, multi-channel notifications (Slack/Email/PagerDuty), database logging, Prometheus metrics, et automatic cleanup.

---

## 📋 Description

Ce template fournit un error handler centralisé avec:
- ✅ Webhook trigger pour recevoir erreurs de tous workflows
- ✅ Extraction et enrichment du contexte d'erreur
- ✅ Severity classification automatique (CRITICAL/WARNING/INFO)
- ✅ Prometheus metrics integration (counters, gauges, histograms)
- ✅ Multi-channel notifications:
  - **CRITICAL**: Slack + Email + PagerDuty incident
  - **WARNING/INFO**: Slack uniquement
- ✅ Database logging PostgreSQL avec retention 90 jours
- ✅ Performance metrics tracking
- ✅ Automatic log cleanup (retention policy)
- ✅ Webhook response pour confirmation

---

## 🎯 Use Cases

- Centralisation de tous les errors n8n dans un seul workflow
- Alerting différencié par severity (CRITICAL → on-call, WARNING → Slack)
- Observabilité complète des erreurs (metrics, logs, dashboards)
- Audit trail pour post-mortems et RCA (Root Cause Analysis)
- SLA tracking et error rate monitoring

---

## 📦 Prérequis

### Infrastructure
- [ ] n8n 2.4.8+ installé et configuré
- [ ] PostgreSQL 12+ avec table `error_logs` créée
- [ ] Prometheus Pushgateway installé (optionnel mais recommandé)
- [ ] Slack workspace avec bot configuré
- [ ] SMTP server pour emails (ou SendGrid/Mailgun)
- [ ] PagerDuty account pour critical incidents (optionnel)

### Credentials requises

**1. Slack OAuth2**
```bash
# Dans n8n UI: Settings → Credentials → Add Credential → Slack OAuth2 API
OAuth2 flow standard
Scopes: chat:write, channels:read
```

**2. SMTP (Email)**
```bash
# Dans n8n UI: Settings → Credentials → Add Credential → SMTP
Host: smtp.gmail.com (ou autre)
Port: 587 (TLS) ou 465 (SSL)
User: your-email@company.com
Password: <app-specific-password>
Secure: true
```

**3. PostgreSQL**
```bash
# Dans n8n UI: Settings → Credentials → Add Credential → Postgres
Host: localhost
Database: n8n_monitoring
User: n8n_logger
Password: <secure-password>
Port: 5432
SSL: Enabled
```

### Database Schema

Créer la table PostgreSQL pour error logs:
```sql
CREATE TABLE error_logs (
  id SERIAL PRIMARY KEY,
  error_id VARCHAR(50) UNIQUE NOT NULL,
  timestamp TIMESTAMP NOT NULL,
  severity VARCHAR(20) NOT NULL,
  workflow_name VARCHAR(255) NOT NULL,
  workflow_id VARCHAR(50),
  execution_id VARCHAR(50),
  node_name VARCHAR(255),
  node_type VARCHAR(100),
  error_message TEXT NOT NULL,
  error_stack TEXT,
  error_type VARCHAR(100),
  environment VARCHAR(50),
  execution_time_ms INTEGER,
  retry_count INTEGER DEFAULT 0,
  user_id VARCHAR(50),
  tags JSONB,
  custom_data JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Index pour performance
CREATE INDEX idx_error_logs_timestamp ON error_logs(timestamp);
CREATE INDEX idx_error_logs_severity ON error_logs(severity);
CREATE INDEX idx_error_logs_workflow_name ON error_logs(workflow_name);
CREATE INDEX idx_error_logs_error_id ON error_logs(error_id);

-- Partitioning par mois (optionnel, pour très gros volumes)
-- CREATE TABLE error_logs_2026_01 PARTITION OF error_logs
-- FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');
```

### Environment Variables
```bash
# Slack channels
SLACK_CRITICAL_CHANNEL=alerts-critical
SLACK_ERRORS_CHANNEL=alerts-errors

# Email configuration
ALERT_EMAIL_FROM=alerts@n8n.company.com
CRITICAL_ALERT_EMAIL=oncall@company.com

# Prometheus
PROMETHEUS_PUSHGATEWAY_URL=http://localhost:9091

# PagerDuty (optionnel)
PAGERDUTY_API_URL=https://api.pagerduty.com/incidents
PAGERDUTY_API_KEY=<your-pagerduty-api-key>
PAGERDUTY_SERVICE_ID=<your-service-id>

# n8n instance
N8N_URL=https://n8n.company.com
NODE_ENV=production
```

---

## 🚀 Installation

### 1. Import Template

```bash
# Via n8n UI
Settings → Import Workflow → Select error-handler-mission-control.json

# Via CLI
n8n import:workflow --input=./workflows/templates/error-handler-mission-control.json
```

### 2. Configure Credentials

1. **Slack Node** → Credentials → Sélectionner "Slack OAuth2 API"
2. **Email Node** → Credentials → Sélectionner "SMTP"
3. **PostgreSQL Nodes** → Credentials → Sélectionner "Postgres"

### 3. Get Webhook URL

1. Ouvrir le workflow
2. Cliquer sur le node "Webhook Error Input"
3. Cliquer "Listen for Test Event"
4. Copier l'URL: `https://your-n8n.com/webhook/error-handler`

### 4. Configure Other Workflows

Dans TOUS vos workflows de production:

**Method 1: Workflow Settings (Recommandé)**
```
1. Ouvrir workflow
2. Settings (gear icon)
3. Error Workflow → Sélectionner "Error Handler: Mission Control Enhanced"
4. Save
```

**Method 2: Error Trigger Node**
```json
{
  "nodes": [
    {
      "name": "On Error",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [500, 500]
    },
    {
      "name": "Send to Error Handler",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "POST",
        "url": "https://your-n8n.com/webhook/error-handler",
        "sendBody": true,
        "jsonBody": "={{ JSON.stringify($json) }}"
      }
    }
  ]
}
```

### 5. Test Error Handler

**Test manuel**:
```bash
# Envoyer une erreur de test
curl -X POST "https://your-n8n.com/webhook/error-handler" \
  -H "Content-Type: application/json" \
  -d '{
    "body": {
      "workflow": {
        "name": "Test Workflow",
        "id": "123"
      },
      "execution": {
        "id": "exec-456",
        "startedAt": "2026-01-30T12:00:00Z",
        "stoppedAt": "2026-01-30T12:00:05Z"
      },
      "node": {
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest"
      },
      "error": {
        "message": "Connection timeout - database unreachable",
        "name": "TimeoutError",
        "stack": "Error: Connection timeout\n    at HttpRequest.execute..."
      }
    }
  }'

# Expected:
# - Slack message dans #alerts-critical (car "timeout" → CRITICAL)
# - Email envoyé à oncall@company.com
# - PagerDuty incident créé
# - Log dans PostgreSQL
# - Metrics dans Prometheus
```

---

## 🎛️ Configuration

### Severity Classification Rules

Modifier la logique dans Code node "Extract Error Context":
```javascript
// Current: Keywords-based classification
const criticalKeywords = [
  'timeout',
  'connection refused',
  'authentication failed',
  'database',
  'payment',
  'critical'
];

// Add more keywords
const criticalKeywords = [
  ...criticalKeywords,
  'outage',
  'security',
  'unauthorized',
  'quota exceeded'
];

// Add custom logic
if (errorLower.includes('payment') && workflowName.includes('checkout')) {
  severity = 'CRITICAL'; // Payment errors always critical in checkout
}
```

### Log Retention Period

Par défaut: **90 jours**

Modifier dans PostgreSQL node "Cleanup Old Logs":
```sql
-- Default: 90 days
DELETE FROM error_logs
WHERE timestamp < NOW() - INTERVAL '90 days';

-- Custom: 30 days (reduce storage)
DELETE FROM error_logs
WHERE timestamp < NOW() - INTERVAL '30 days';

-- Custom: 1 year (compliance)
DELETE FROM error_logs
WHERE timestamp < NOW() - INTERVAL '365 days';
```

### Notification Channels

**Ajouter Microsoft Teams**:
```json
{
  "name": "Teams: Critical Alert",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "={{ $env.TEAMS_WEBHOOK_URL }}",
    "sendBody": true,
    "jsonBody": "={{ JSON.stringify({ '@type': 'MessageCard', 'summary': 'Critical Error', 'sections': [{ 'activityTitle': $json.workflow.name, 'activitySubtitle': $json.error.message }] }) }}"
  }
}
```

**Ajouter Opsgenie**:
```json
{
  "name": "Opsgenie: Create Alert",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.opsgenie.com/v2/alerts",
    "authentication": "genericCredentialType",
    "genericAuthType": "httpHeaderAuth",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        {"name": "Authorization", "value": "GenieKey {{ $env.OPSGENIE_API_KEY }}"}
      ]
    },
    "sendBody": true,
    "jsonBody": "={{ JSON.stringify({ message: $json.error.message, priority: 'P1', tags: ['n8n', $json.workflow.name] }) }}"
  }
}
```

### Prometheus Metrics Customization

Modifier dans Code node "Record Prometheus Metrics":
```javascript
// Add custom metrics
const prometheusMetrics = [
  // Existing metrics...
  `# TYPE n8n_error_by_node_type counter`,
  `n8n_error_by_node_type{node_type="${error.type}"} 1`,
  ``,
  `# TYPE n8n_error_recovery_attempts counter`,
  `n8n_error_recovery_attempts{workflow="${workflow.name}"} ${context.retryCount}`
].join('\n');
```

---

## 📊 Metrics & Dashboards

### Prometheus Metrics Exposées

```prometheus
# Counters
n8n_workflow_errors_total{severity="critical",workflow="ETL Salesforce",error_type="TimeoutError",environment="production"}

# Gauges
n8n_workflow_execution_time_seconds{workflow="ETL Salesforce"}
n8n_workflow_retry_count{workflow="ETL Salesforce"}
```

### Grafana Dashboard

Queries utiles pour dashboard:
```promql
# Error rate (errors/min)
rate(n8n_workflow_errors_total[5m])

# Error rate by severity
sum(rate(n8n_workflow_errors_total[5m])) by (severity)

# Top 10 workflows with most errors
topk(10, sum(n8n_workflow_errors_total) by (workflow))

# Critical errors in last 24h
sum(increase(n8n_workflow_errors_total{severity="critical"}[24h]))

# Average execution time by workflow
avg(n8n_workflow_execution_time_seconds) by (workflow)
```

### PostgreSQL Analytics

Queries utiles pour analysis:
```sql
-- Error trend (daily)
SELECT
  DATE(timestamp) as error_date,
  severity,
  COUNT(*) as error_count
FROM error_logs
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY DATE(timestamp), severity
ORDER BY error_date DESC, severity;

-- Top failing workflows
SELECT
  workflow_name,
  COUNT(*) as total_errors,
  COUNT(CASE WHEN severity = 'CRITICAL' THEN 1 END) as critical_errors,
  AVG(execution_time_ms) as avg_execution_time_ms
FROM error_logs
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY workflow_name
ORDER BY total_errors DESC
LIMIT 20;

-- Error patterns (common error messages)
SELECT
  substring(error_message, 1, 100) as error_pattern,
  COUNT(*) as occurrences,
  array_agg(DISTINCT workflow_name) as affected_workflows
FROM error_logs
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY substring(error_message, 1, 100)
ORDER BY occurrences DESC
LIMIT 10;

-- Node types causing most errors
SELECT
  node_type,
  COUNT(*) as error_count,
  COUNT(DISTINCT workflow_name) as affected_workflows
FROM error_logs
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY node_type
ORDER BY error_count DESC;
```

---

## 🧪 Testing

### Test 1: CRITICAL Error

```bash
curl -X POST "http://localhost:5678/webhook/error-handler" \
  -H "Content-Type: application/json" \
  -d '{
    "body": {
      "workflow": {"name": "Payment Processing", "id": "123"},
      "execution": {"id": "exec-456", "startedAt": "2026-01-30T12:00:00Z", "stoppedAt": "2026-01-30T12:00:05Z"},
      "node": {"name": "Stripe API", "type": "n8n-nodes-base.stripe"},
      "error": {"message": "Payment gateway timeout - critical", "name": "TimeoutError"}
    }
  }'

# Expected:
# - Severity: CRITICAL
# - Slack: #alerts-critical
# - Email: oncall@company.com
# - PagerDuty: Incident créé
# - PostgreSQL: Row inserted
# - Prometheus: Metric pushed
```

### Test 2: WARNING Error

```bash
curl -X POST "http://localhost:5678/webhook/error-handler" \
  -H "Content-Type: application/json" \
  -d '{
    "body": {
      "workflow": {"name": "Email Campaign", "id": "789"},
      "node": {"name": "Send Email"},
      "error": {"message": "Retrying email send - warning"}
    }
  }'

# Expected:
# - Severity: WARNING
# - Slack: #alerts-errors (NOT critical channel)
# - No Email
# - No PagerDuty
# - PostgreSQL: Row inserted
```

### Test 3: Database Cleanup

```sql
-- Insert old error logs for testing
INSERT INTO error_logs (error_id, timestamp, severity, workflow_name, error_message)
VALUES
  ('TEST-1', NOW() - INTERVAL '100 days', 'INFO', 'Test Workflow', 'Old error 1'),
  ('TEST-2', NOW() - INTERVAL '95 days', 'WARNING', 'Test Workflow', 'Old error 2');

-- Trigger workflow
-- Expected: Both rows deleted (> 90 days old)

SELECT * FROM error_logs WHERE error_id LIKE 'TEST-%';
-- Should return 0 rows
```

---

## ✅ Checklist Production

### Infrastructure
- [ ] PostgreSQL accessible depuis n8n (network/firewall)
- [ ] PostgreSQL table `error_logs` créée avec indexes
- [ ] Prometheus Pushgateway accessible (port 9091)
- [ ] SMTP server configuré et testé (test email sent)
- [ ] Slack bot ajouté aux channels (#alerts-critical, #alerts-errors)
- [ ] PagerDuty service créé et API key obtenue (si applicable)

### Security
- [ ] Webhook path non-devinable (`/webhook/error-handler-a3f8d9e2`)
- [ ] HTTPS activé (pas de HTTP en prod)
- [ ] PostgreSQL credentials sécurisées (vault/secrets manager)
- [ ] SMTP credentials sécurisées (app-specific password)
- [ ] PagerDuty API key sécurisée (rotation 90 jours)

### Notifications
- [ ] Slack critical channel testé (message reçu)
- [ ] Slack errors channel testé (message reçu)
- [ ] Email critical testé (email reçu, pas spam)
- [ ] PagerDuty incident testé (incident créé, notification on-call)
- [ ] Notification templates revus (formatting, links, context)

### Database
- [ ] Log retention policy définie (90 jours default)
- [ ] Database backup configuré (daily)
- [ ] Cleanup query testée (pas de data loss)
- [ ] Index performance vérifiée (< 100ms queries)
- [ ] Partitioning configuré si > 1M rows/month

### Observability
- [ ] Prometheus metrics testées (data visible dans Grafana)
- [ ] Grafana dashboard créé (error rate, top workflows, severity distribution)
- [ ] Alerting configuré (> 10 errors/min → Slack)
- [ ] Logs PostgreSQL analysables (queries analytics testées)
- [ ] SLA défini (MTTR < 15 min pour CRITICAL)

### Reliability
- [ ] Error handler ne peut pas crash (continueOnFail sur tous nodes)
- [ ] Webhook response 200 OK même si notifications fail
- [ ] Cleanup ne bloque pas workflow (async)
- [ ] Timeout configuré sur tous HTTP requests (< 30s)
- [ ] Fallback notification si Slack down (email)

---

## 🐛 Troubleshooting

### Problème: Slack notifications ne s'envoient pas

**Symptôme**: Pas de messages dans Slack, workflow success

**Solutions**:
```bash
# 1. Vérifier bot permissions
# Slack API → Your App → OAuth & Permissions
# Scopes requis: chat:write, channels:read

# 2. Vérifier bot dans channel
# Ouvrir #alerts-critical → Invite @your-bot

# 3. Test manuel
curl -X POST "https://slack.com/api/chat.postMessage" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channel": "alerts-critical", "text": "Test"}'

# 4. Vérifier env variable
echo $SLACK_CRITICAL_CHANNEL  # Should return: alerts-critical
```

### Problème: PostgreSQL inserts failing

**Symptôme**: Error "duplicate key value violates unique constraint"

**Causes**:
- Même error_id généré 2x (race condition)
- Retry workflow avec même errorId

**Solution**:
```sql
-- Change UNIQUE constraint to allow duplicates
ALTER TABLE error_logs DROP CONSTRAINT IF EXISTS error_logs_error_id_key;

-- Or: Use UPSERT instead of INSERT
INSERT INTO error_logs (...) VALUES (...)
ON CONFLICT (error_id) DO UPDATE SET
  retry_count = error_logs.retry_count + 1;
```

### Problème: Prometheus metrics not showing in Grafana

**Symptôme**: Queries return "No data"

**Solutions**:
```bash
# 1. Vérifier Pushgateway accessible
curl http://localhost:9091/metrics

# 2. Vérifier metrics pushed
curl http://localhost:9091/metrics | grep n8n_workflow_errors_total

# 3. Vérifier Prometheus scraping Pushgateway
# prometheus.yml:
scrape_configs:
  - job_name: 'pushgateway'
    static_configs:
      - targets: ['localhost:9091']

# 4. Test manual push
curl -X POST "http://localhost:9091/metrics/job/test" \
  --data-binary "test_metric 123"
```

### Problème: Email marked as spam

**Symptôme**: Emails arrivent dans spam folder

**Solutions**:
1. Configurer SPF record:
```dns
v=spf1 include:_spf.google.com ~all
```

2. Configurer DKIM signing (via SendGrid/Mailgun)

3. Use template avec bon formatting (pas trop de liens)

4. Warm up email domain (envoyer 10-20 emails/jour initialement)

---

## 📚 Références

- [Prometheus Pushgateway](https://github.com/prometheus/pushgateway)
- [PagerDuty API](https://developer.pagerduty.com/api-reference/)
- [Slack API](https://api.slack.com/messaging/sending)
- [PostgreSQL Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)

---

## 📄 License

MIT License - Voir fichier LICENSE principal

---

## 👥 Support

- Issues: https://github.com/your-repo/n8n-workflows/issues
- Docs: Voir "Règles du jeu – automatisation n8n.md"
- Contact: sre-team@company.com
