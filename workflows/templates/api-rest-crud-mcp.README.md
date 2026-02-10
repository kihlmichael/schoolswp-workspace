# Template: REST API CRUD with MCP

**Nom complet** : `[Template] API Integration: REST CRUD with Cache & Validation`

Production-ready REST API CRUD template avec cache management, rate limiting, validation complète et métriques Prometheus.

---

## 📋 Description

Ce template fournit un endpoint REST API complet avec:
- ✅ Webhook trigger avec validation d'entrée (Joi schema)
- ✅ Rate limiting (100 req/min par client IP)
- ✅ HTTP method routing (GET/POST/PUT/DELETE)
- ✅ Cache management (5 min TTL) avec invalidation automatique
- ✅ Validation input/output avec Joi schemas
- ✅ Prometheus metrics tracking
- ✅ Error handling centralisé
- ✅ Response formatting standardisé

---

## 🎯 Use Cases

- API REST CRUD pour ressources (users, products, orders, etc.)
- Gateway API avec cache et rate limiting
- Microservice API avec observabilité complète
- Prototype API avec validation et métriques

---

## 📦 Prérequis

### Infrastructure
- [ ] n8n 2.4.8+ installé et configuré
- [ ] PostgreSQL (optionnel - pour persistence cache)
- [ ] Prometheus Pushgateway (optionnel - pour métriques)

### Credentials requises
```bash
# Créer dans n8n UI: Settings → Credentials
- HTTP Request credential (si API externe nécessite auth)
- Slack OAuth2 (pour error notifications)
```

### Environment Variables
```bash
# Required
API_BASE_URL=https://api.example.com/v1
WEBHOOK_BASE_URL=https://your-n8n-instance.com

# Optional - Metrics
PROMETHEUS_PUSHGATEWAY_URL=http://localhost:9091

# Optional - Cache config
CACHE_TTL_SECONDS=300  # 5 minutes default
RATE_LIMIT_RPM=100     # 100 requests per minute

# Optional - Error handling
ERROR_WEBHOOK_URL=https://your-n8n-instance.com/webhook/error-handler
```

---

## 🚀 Installation

### 1. Import Template

```bash
# Via n8n UI
Settings → Import Workflow → Select api-rest-crud-mcp.json

# Via CLI
n8n import:workflow --input=./workflows/templates/api-rest-crud-mcp.json
```

### 2. Configure Variables

Ouvrir le workflow et configurer dans **Settings → Variables**:

| Variable | Description | Exemple |
|----------|-------------|---------|
| `API_BASE_URL` | URL de l'API backend | `https://api.example.com/v1` |
| `CACHE_TTL_SECONDS` | Durée cache (secondes) | `300` |
| `RATE_LIMIT_RPM` | Limite req/min | `100` |

### 3. Activer Webhook

1. Cliquer sur le node "Webhook Trigger"
2. Cliquer "Listen for Test Event"
3. Copier l'URL du webhook: `https://your-n8n.com/webhook/api-crud`
4. Tester avec cURL:

```bash
# GET request
curl -X GET "https://your-n8n.com/webhook/api-crud?resourceId=123"

# POST request
curl -X POST "https://your-n8n.com/webhook/api-crud" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### 4. Configurer Error Workflow (Recommandé)

1. Importer `error-handler-mission-control.json`
2. Dans ce workflow, aller à **Settings**
3. **Error Workflow** → Sélectionner "Error Handler: Mission Control Enhanced"

---

## 🎛️ Configuration

### Rate Limiting

Par défaut: **100 requests/minute par IP**

Modifier dans le Code node "Rate Limiting Check":
```javascript
const RATE_LIMIT = 200; // Augmenter à 200 req/min
const WINDOW = 60000;   // 1 minute
```

### Cache TTL

Par défaut: **5 minutes**

Modifier dans le Code node "Check Cache":
```javascript
const CACHE_TTL = 600000; // 10 minutes (600,000 ms)
```

### Validation Schema

Modifier le Joi schema dans "Validate Input":
```javascript
const schema = Joi.object({
  name: Joi.string().min(2).max(100).required(),
  email: Joi.string().email().required(),
  age: Joi.number().min(18).max(120).optional(),
  status: Joi.string().valid('active', 'inactive').default('active')
});
```

### Supported HTTP Methods

Par défaut: `GET`, `POST`, `PUT`, `DELETE`

Ajouter d'autres méthodes dans le Switch node "Route by HTTP Method":
- Ajouter une branche pour `PATCH`
- Configurer la condition: `{{$json.method}} = PATCH`

---

## 📊 Métriques Prometheus

Le template expose automatiquement:

```prometheus
# Counter - Total requests
n8n_api_requests_total{method="GET", status="200", resource="users"}

# Histogram - Response time
n8n_api_response_time_seconds{method="POST", resource="users"}

# Gauge - Cache hit rate
n8n_api_cache_hit_rate{resource="users"}

# Counter - Rate limit violations
n8n_api_rate_limit_exceeded_total{client_ip="192.168.1.1"}
```

**Visualiser avec Grafana**:
1. Connecter Prometheus datasource
2. Importer le dashboard n8n API (ID: 12345)

---

## 🧪 Testing

### Test Local

```bash
# 1. GET request - Should return cached data after first call
curl -X GET "http://localhost:5678/webhook/api-crud?resourceId=123"
curl -X GET "http://localhost:5678/webhook/api-crud?resourceId=123"  # Cached

# 2. POST request - Create resource
curl -X POST "http://localhost:5678/webhook/api-crud" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com"
  }'

# 3. PUT request - Update resource
curl -X PUT "http://localhost:5678/webhook/api-crud?resourceId=123" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Name",
    "email": "updated@example.com"
  }'

# 4. DELETE request - Delete resource
curl -X DELETE "http://localhost:5678/webhook/api-crud?resourceId=123"

# 5. Test rate limiting - Send 101 requests in 60s
for i in {1..101}; do
  curl -X GET "http://localhost:5678/webhook/api-crud?resourceId=$i"
done
# Request #101 should return 429 Too Many Requests

# 6. Test validation failure
curl -X POST "http://localhost:5678/webhook/api-crud" \
  -H "Content-Type: application/json" \
  -d '{"name": "x"}'  # Too short, should fail validation
```

### Test Production

```bash
# Load test with Apache Bench
ab -n 1000 -c 10 https://your-n8n.com/webhook/api-crud?resourceId=123

# Expected results:
# - First 100 requests/min: 200 OK
# - Requests 101+: 429 Too Many Requests
# - Cache hit rate > 80% for repeated GET
```

---

## ✅ Checklist Production

Avant de déployer en production:

### Security
- [ ] Webhook path unique et non-devinable (`/webhook/api-crud-f8d9a2b3`)
- [ ] HTTPS activé (pas de HTTP en prod)
- [ ] Rate limiting testé et ajusté selon charge attendue
- [ ] Credentials jamais hardcodées (utiliser n8n Credentials)
- [ ] Input validation complète avec Joi schemas
- [ ] Output sanitization (pas de données sensibles exposées)

### Performance
- [ ] Cache TTL optimisé selon fraîcheur données requise
- [ ] Batch size testé (si applicable)
- [ ] Timeout configuré (< 30s recommandé)
- [ ] HTTP Request retry configuré (3 tentatives avec backoff)

### Observability
- [ ] Error workflow configuré et testé
- [ ] Prometheus metrics activées
- [ ] Logs structurés (JSON format)
- [ ] Alertes configurées pour erreurs critiques
- [ ] Dashboard Grafana créé et testé

### Reliability
- [ ] Test de charge effectué (minimum 100 req/s)
- [ ] Cache invalidation testée (POST/PUT/DELETE)
- [ ] Error handling testé (API down, timeout, invalid response)
- [ ] Rollback plan documenté
- [ ] Monitoring actif (Grafana + alertes)

### Documentation
- [ ] API documentation complète (OpenAPI/Swagger)
- [ ] Environment variables documentées
- [ ] Runbook créé (troubleshooting, common issues)
- [ ] Changelog maintenu
- [ ] Contact on-call défini

---

## 🐛 Troubleshooting

### Problème: Rate Limit trop strict

**Symptôme**: 429 Too Many Requests fréquents

**Solution**:
```javascript
// Dans Code node "Rate Limiting Check"
const RATE_LIMIT = 500; // Augmenter limite
const WINDOW = 60000;
```

### Problème: Cache stale data

**Symptôme**: Données obsolètes retournées

**Solution**:
1. Vérifier invalidation cache sur POST/PUT/DELETE
2. Réduire CACHE_TTL si nécessaire
3. Vérifier que `cacheKey` est unique par ressource

### Problème: Validation rejette requêtes valides

**Symptôme**: 400 Bad Request sur requêtes correctes

**Solution**:
```javascript
// Dans Code node "Validate Input"
// Activer debug mode
const validationResult = schema.validate(data, {
  abortEarly: false,
  debug: true
});
console.log('Validation errors:', validationResult.error);
```

### Problème: Métriques Prometheus non disponibles

**Symptôme**: Pas de données dans Grafana

**Solution**:
1. Vérifier `PROMETHEUS_PUSHGATEWAY_URL` est accessible
2. Test manuel:
```bash
curl -X POST "http://localhost:9091/metrics/job/n8n_api/instance/test" \
  --data-binary "test_metric 1"
```
3. Vérifier logs n8n pour erreurs HTTP

---

## 📚 Références

- [n8n Webhook Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)
- [Joi Schema Validation](https://joi.dev/api/)
- [Prometheus Pushgateway](https://github.com/prometheus/pushgateway)
- [Rate Limiting Patterns](https://en.wikipedia.org/wiki/Rate_limiting)

---

## 📄 License

MIT License - Voir fichier LICENSE principal

---

## 👥 Support

- Issues: https://github.com/your-repo/n8n-workflows/issues
- Docs: Voir "Règles du jeu – automatisation n8n.md"
- Contact: automation-team@company.com
