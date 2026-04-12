# Google Search Console API — Intégration n8n schoolsWP

Pas de node natif GSC fiable dans n8n → HTTP Request + OAuth2 Google.

---

## Node — GSC Pages (28j)

```
Name              : GSC Search Analytics - Pages 28d
Method            : POST
URL               : https://www.googleapis.com/webmasters/v3/sites/sc-domain:schoolswp.com/searchAnalytics/query
Authentication    : OAuth2 (credential : Google OAuth2)
Send Body         : true
Body Content Type : JSON
Specify Body      : Using JSON
```

> Si ta propriété GSC est de type URL-prefix (pas sc-domain) :
> `https://www.googleapis.com/webmasters/v3/sites/https%3A%2F%2Fschoolswp.com%2F/searchAnalytics/query`

Body JSON :

```json
{
  "startDate": "={{$now.minus({ days: 28 }).toISODate()}}",
  "endDate": "={{$now.minus({ days: 1 }).toISODate()}}",
  "dimensions": ["page"],
  "rowLimit": 200,
  "startRow": 0,
  "dataState": "final"
}
```

---

## Node — GSC Pages période précédente (J-29 à J-56)

```
Name : GSC Search Analytics - Pages Prev 28d
```

Body JSON :

```json
{
  "startDate": "={{$now.minus({ days: 56 }).toISODate()}}",
  "endDate": "={{$now.minus({ days: 29 }).toISODate()}}",
  "dimensions": ["page"],
  "rowLimit": 200,
  "startRow": 0,
  "dataState": "final"
}
```

---

## Node — GSC Pages + Requêtes (Workflow 03 Topic Discovery)

Body JSON :

```json
{
  "startDate": "={{$now.minus({ days: 28 }).toISODate()}}",
  "endDate": "={{$now.minus({ days: 1 }).toISODate()}}",
  "dimensions": ["page", "query"],
  "rowLimit": 250,
  "startRow": 0,
  "dataState": "final"
}
```

---

## Code node — Normaliser les rows (après chaque GSC node)

### Pour dimensions: ["page"]

```javascript
const rows = $json.rows || [];

return rows.map((row) => ({
  json: {
    url: row.keys?.[0] || "",
    clicks_28d: Number(row.clicks || 0),
    impressions_28d: Number(row.impressions || 0),
    ctr_28d: Number(row.ctr || 0),
    position_28d: Number(row.position || 0),
  },
}));
```

### Pour dimensions: ["page", "query"]

```javascript
const rows = $json.rows || [];

return rows.map((row) => ({
  json: {
    source_url: row.keys?.[0] || "",
    detected_query: row.keys?.[1] || "",
    clicks_28d: Number(row.clicks || 0),
    impressions_28d: Number(row.impressions || 0),
    ctr_28d: Number(row.ctr || 0),
    position_28d: Number(row.position || 0),
  },
}));
```

---

## Réponse API attendue

```json
{
  "rows": [
    {
      "keys": ["https://schoolswp.com/fluent-forms-avis/"],
      "clicks": 182,
      "impressions": 6400,
      "ctr": 0.0284,
      "position": 6.3
    }
  ],
  "responseAggregationType": "byPage"
}
```

---

## Limites API à respecter

- `rowLimit` modéré (200-250 max pour V2)
- 1 exécution quotidienne + 1 hebdo → dans les limites confortables
- En cas d'erreur quota : réduire rowLimit ou espacer les exécutions

---

## Architecture complète du bloc GSC dans n8n

```
HTTP Request (GSC 28j)
HTTP Request (GSC 28j précédents)  ← en parallèle
  → Merge (Combine, match sur keys[0])
  → Code (Normalize rows)
  → Code (Clean + Delta)
```
