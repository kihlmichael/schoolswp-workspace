# schoolsWP CTR Hunter — Workflow n8n

**Architecture finale : 2 workflows séparés.**

| Workflow           | Fichier JSON                     | Rôle                                                   |
| ------------------ | -------------------------------- | ------------------------------------------------------ |
| **A — CTR Hunter** | `n8n-ctr-hunter-workflow-a.json` | Détection + top queries + génération LLM + log Sheets  |
| **B — CTR Judge**  | `n8n-ctr-hunter-workflow-b.json` | Suivi J+21 + comparaison GSC + verdict + update Sheets |

**Importer dans n8n :** Settings → Import workflow → sélectionner le fichier JSON.

---

> Les sections V1 / V2 / V3 ci-dessous sont conservées comme référence historique.
> **Utiliser directement les JSON finaux ci-dessus** pour toute nouvelle installation.

---

## Versions historiques (référence)

| Version | Pipeline                                                    | Ce qu'elle apporte                                   |
| ------- | ----------------------------------------------------------- | ---------------------------------------------------- |
| V1      | Schedule → GSC pages → Scoring → IF → Sheets + Gmail        | Pages faibles CTR détectées + alertes                |
| V2      | V1 + boucle par URL → GSC queries → fusion → Sheets + Gmail | Pages + top requêtes par URL — alerte exploitable    |
| V3      | V2 + prompt IA → LLM → parse → Sheets + Gmail               | Génération auto de 10 titles + top 3 + hypothèse TDD |

---

## Configuration requise

**À remplacer dans le JSON avant import :**

| Placeholder                        | Valeur à renseigner                      |
| ---------------------------------- | ---------------------------------------- |
| `YOUR_GOOGLE_OAUTH_CREDENTIAL_ID`  | ID du credential Google OAuth2 dans n8n  |
| `YOUR_GOOGLE_SHEETS_CREDENTIAL_ID` | ID du credential Google Sheets OAuth2    |
| `YOUR_GMAIL_CREDENTIAL_ID`         | ID du credential Gmail OAuth2            |
| `YOUR_GOOGLE_SHEET_ID`             | ID du Google Sheet de suivi              |
| `you@example.com`                  | Adresse email de destination des alertes |

**Structure Google Sheet — onglet `Tests CTR` (colonnes exactes) :**

`date_scan` / `url` / `clicks` / `impressions` / `ctr_percent` / `position` / `target_ctr` / `opportunity_score` / `status` / `next_action`

---

## Logique du workflow

| Étape | Node             | Détail                                                        |
| ----- | ---------------- | ------------------------------------------------------------- |
| 1     | Schedule Trigger | Lundi 08:00, hebdomadaire                                     |
| 2     | HTTP Request     | POST Search Console API, dimensions=["page"], 90 jours        |
| 3     | Code             | Scoring quick wins — filtre pos 3-12 / imp >500 / CTR < cible |
| 4     | IF               | Si opportunités détectées → branches log + alerte             |
| 5a    | Google Sheets    | Append des lignes dans l'onglet Tests CTR                     |
| 5b    | Gmail            | Email récapitulatif top 5 opportunités                        |
| 6     | Code (else)      | Message "Aucune opportunité cette semaine"                    |

**Critères de sélection (Code node) :**

- Position : 3 → 12
- Impressions : > 500
- CTR actuel < CTR cible selon la position
- Tri par opportunity_score décroissant
- Top 20 maximum retenu

**CTR cibles par position :**

| Position | CTR cible |
| -------- | --------- |
| ≤ 3      | 15 %      |
| 4        | 12 %      |
| 5        | 10 %      |
| 6        | 8 %       |
| 7        | 6 %       |
| 8–10     | 5 %       |
| 11–12    | 4 %       |

**Formule score :** `Impressions × (CTR cible − CTR actuel)`

---

## V2 — Enrichissement par requête + génération IA

**Pipeline V2 :**

```text
V1 (détection) → HTTP Request dimensions=["page","query"] → Prompt IA → Sheets → Slack
```

**Étapes supplémentaires :**

1. Ajouter un second HTTP Request avec `dimensions: ["page", "query"]` pour récupérer les top queries par URL détectée
2. Pour chaque URL prioritaire, lancer le prompt IA ci-dessous
3. Pousser les titles générés dans le Google Sheet (onglet Variantes Titles)
4. Optionnel : remplacer Gmail par Slack pour l'alerte

**Prompt IA prêt à coller dans n8n (OpenAI / Claude node) :**

```text
Analyse cette URL détectée par CTR Hunter et génère 10 nouveaux titles SEO optimisés CTR.

Données :
- URL : {{ $json.url }}
- CTR actuel : {{ $json.ctr_percent }}%
- Position : {{ $json.position }}
- Impressions : {{ $json.impressions }}
- Mot-clé principal : [À compléter ou extraire de la query principale]
- Audience : freelances, créateurs, entrepreneurs WordPress

Objectif :
Proposer 10 titles crédibles, différenciants, optimisés CTR, sans clickbait trompeur.
```

**Points de vigilance pour l'adaptation :**

| Node                              | Niveau de risque      | Pourquoi                                 |
| --------------------------------- | --------------------- | ---------------------------------------- |
| Search Console API + Code scoring | Stable                | Cœur du workflow — ne pas modifier       |
| IF                                | Stable                | Logique simple                           |
| Google Sheets                     | Ajustements possibles | Mapping évolue selon version n8n         |
| Gmail                             | Ajustements possibles | TypeVersion et champs bougent parfois    |
| Slack (V2)                        | Simple à câbler       | Node natif n8n, credentials Slack OAuth2 |

---

## JSON n8n — V1 (prêt à importer)

```json
{
  "name": "schoolsWP - CTR Hunter V1",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "weeks",
              "triggerAtDay": [1],
              "triggerAtHour": 8,
              "triggerAtMinute": 0
            }
          ]
        }
      },
      "id": "1",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [260, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "=https://www.googleapis.com/webmasters/v3/sites/sc-domain:schoolswp.com/searchAnalytics/query",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "googleOAuth2Api",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"startDate\": \"{{$now.minus({days: 90}).toFormat('yyyy-MM-dd')}}\",\n  \"endDate\": \"{{$now.minus({days: 3}).toFormat('yyyy-MM-dd')}}\",\n  \"dimensions\": [\"page\"],\n  \"type\": \"web\",\n  \"rowLimit\": 25000\n}",
        "options": {
          "response": {
            "response": {
              "responseFormat": "json"
            }
          }
        }
      },
      "id": "2",
      "name": "Search Console API",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [500, 300],
      "credentials": {
        "googleOAuth2Api": {
          "id": "YOUR_GOOGLE_OAUTH_CREDENTIAL_ID",
          "name": "Google OAuth2"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const rows = $json.rows || [];\n\nfunction getTargetCtr(position) {\n  if (position <= 3) return 0.15;\n  if (position <= 4) return 0.12;\n  if (position <= 5) return 0.10;\n  if (position <= 6) return 0.08;\n  if (position <= 7) return 0.06;\n  if (position <= 10) return 0.05;\n  if (position <= 12) return 0.04;\n  return 0.03;\n}\n\nconst today = new Date().toISOString().slice(0, 10);\n\nconst results = rows\n  .map(row => {\n    const url = row.keys?.[0] || '';\n    const clicks = row.clicks || 0;\n    const impressions = row.impressions || 0;\n    const ctr = row.ctr || 0;\n    const position = row.position || 999;\n    const targetCtr = getTargetCtr(position);\n    const opportunityScore = impressions * Math.max(targetCtr - ctr, 0);\n\n    return {\n      scan_date: today,\n      url,\n      clicks: Number(clicks.toFixed ? clicks.toFixed(2) : clicks),\n      impressions: Number(impressions.toFixed ? impressions.toFixed(0) : impressions),\n      ctr_percent: Number((ctr * 100).toFixed(2)),\n      position: Number(position.toFixed(2)),\n      target_ctr_percent: Number((targetCtr * 100).toFixed(2)),\n      opportunity_score: Number(opportunityScore.toFixed(2)),\n      status: 'À tester',\n      next_action: 'Tester un nouveau title',\n      is_quick_win:\n        position >= 3 &&\n        position <= 12 &&\n        impressions > 500 &&\n        ctr < targetCtr\n    };\n  })\n  .filter(item => item.is_quick_win)\n  .sort((a, b) => b.opportunity_score - a.opportunity_score)\n  .slice(0, 20)\n  .map(item => ({ json: item }));\n\nreturn results;"
      },
      "id": "3",
      "name": "Score CTR Opportunities",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [760, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "has-items-check",
              "leftValue": "={{ $items().length }}",
              "rightValue": 0,
              "operator": {
                "type": "number",
                "operation": "larger"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "4",
      "name": "Has Opportunities?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [1020, 300]
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": "YOUR_GOOGLE_SHEET_ID",
        "sheetName": "Tests CTR",
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "date_scan": "={{ $json.scan_date }}",
            "url": "={{ $json.url }}",
            "clicks": "={{ $json.clicks }}",
            "impressions": "={{ $json.impressions }}",
            "ctr_percent": "={{ $json.ctr_percent }}",
            "position": "={{ $json.position }}",
            "target_ctr": "={{ $json.target_ctr_percent }}",
            "opportunity_score": "={{ $json.opportunity_score }}",
            "status": "={{ $json.status }}",
            "next_action": "={{ $json.next_action }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "date_scan",
              "displayName": "date_scan",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "url",
              "displayName": "url",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "clicks",
              "displayName": "clicks",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true
            },
            {
              "id": "impressions",
              "displayName": "impressions",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true
            },
            {
              "id": "ctr_percent",
              "displayName": "ctr_percent",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true
            },
            {
              "id": "position",
              "displayName": "position",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true
            },
            {
              "id": "target_ctr",
              "displayName": "target_ctr",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true
            },
            {
              "id": "opportunity_score",
              "displayName": "opportunity_score",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true
            },
            {
              "id": "status",
              "displayName": "status",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "next_action",
              "displayName": "next_action",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "id": "5",
      "name": "Log to Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [1280, 200],
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "YOUR_GOOGLE_SHEETS_CREDENTIAL_ID",
          "name": "Google Sheets OAuth2"
        }
      }
    },
    {
      "parameters": {
        "sendTo": "you@example.com",
        "subject": "=[CTR Hunter] {{$items().length}} pages à faible CTR détectées",
        "emailType": "text",
        "message": "=Le workflow CTR Hunter a détecté {{$items().length}} opportunités SEO.\n\nTop résultats :\n{{ $items().slice(0,5).map((item, index) => `${index + 1}. ${item.json.url}\\nCTR : ${item.json.ctr_percent}%\\nPosition : ${item.json.position}\\nImpressions : ${item.json.impressions}\\nScore : ${item.json.opportunity_score}`).join('\\n\\n') }}\n\nAction recommandée :\nTester un nouveau title sur les pages prioritaires."
      },
      "id": "6",
      "name": "Send Email Alert",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 2.1,
      "position": [1280, 400],
      "credentials": {
        "gmailOAuth2": {
          "id": "YOUR_GMAIL_CREDENTIAL_ID",
          "name": "Gmail OAuth2"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "return [{\n  json: {\n    message: 'Aucune opportunité CTR détectée cette semaine.'\n  }\n}];"
      },
      "id": "7",
      "name": "No Opportunities",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [1280, 560]
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [[{ "node": "Search Console API", "type": "main", "index": 0 }]]
    },
    "Search Console API": {
      "main": [
        [{ "node": "Score CTR Opportunities", "type": "main", "index": 0 }]
      ]
    },
    "Score CTR Opportunities": {
      "main": [[{ "node": "Has Opportunities?", "type": "main", "index": 0 }]]
    },
    "Has Opportunities?": {
      "main": [
        [
          { "node": "Log to Google Sheets", "type": "main", "index": 0 },
          { "node": "Send Email Alert", "type": "main", "index": 0 }
        ],
        [{ "node": "No Opportunities", "type": "main", "index": 0 }]
      ]
    }
  },
  "active": false,
  "settings": { "executionOrder": "v1" },
  "versionId": "1",
  "meta": { "templateCredsSetupCompleted": false },
  "id": "schoolswp-ctr-hunter-v1",
  "tags": []
}
```

---

## JSON n8n — V2 (pages + top queries par URL)

**Différence clé V1 → V2 :** après le scoring, une boucle `splitInBatches` relance l'API GSC pour chaque URL avec `dimensions: ["query"]` filtré par page. Le résultat est fusionné dans un champ `top_queries_text` prêt à logger et à envoyer en alerte.

**Colonnes Google Sheet V2 (ajouter à la V1) :** `top_queries_text`

```json
{
  "name": "schoolsWP - CTR Hunter V2",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "weeks",
              "triggerAtDay": [1],
              "triggerAtHour": 8,
              "triggerAtMinute": 0
            }
          ]
        }
      },
      "id": "1",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [240, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "=https://www.googleapis.com/webmasters/v3/sites/sc-domain:schoolswp.com/searchAnalytics/query",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "googleOAuth2Api",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"startDate\": \"{{$now.minus({days: 90}).toFormat('yyyy-MM-dd')}}\",\n  \"endDate\": \"{{$now.minus({days: 3}).toFormat('yyyy-MM-dd')}}\",\n  \"dimensions\": [\"page\"],\n  \"type\": \"web\",\n  \"rowLimit\": 25000\n}",
        "options": {
          "response": { "response": { "responseFormat": "json" } }
        }
      },
      "id": "2",
      "name": "Search Console Pages",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [480, 300],
      "credentials": {
        "googleOAuth2Api": {
          "id": "YOUR_GOOGLE_OAUTH_CREDENTIAL_ID",
          "name": "Google OAuth2"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const rows = $json.rows || [];\n\nfunction getTargetCtr(position) {\n  if (position <= 3) return 0.15;\n  if (position <= 4) return 0.12;\n  if (position <= 5) return 0.10;\n  if (position <= 6) return 0.08;\n  if (position <= 7) return 0.06;\n  if (position <= 10) return 0.05;\n  if (position <= 12) return 0.04;\n  return 0.03;\n}\n\nconst today = new Date().toISOString().slice(0, 10);\n\nreturn rows\n  .map(row => {\n    const url = row.keys?.[0] || '';\n    const clicks = row.clicks || 0;\n    const impressions = row.impressions || 0;\n    const ctr = row.ctr || 0;\n    const position = row.position || 999;\n    const targetCtr = getTargetCtr(position);\n    const opportunityScore = impressions * Math.max(targetCtr - ctr, 0);\n    return {\n      json: {\n        scan_date: today, url, clicks, impressions,\n        ctr_percent: +(ctr * 100).toFixed(2),\n        ctr_raw: ctr,\n        position: +position.toFixed(2),\n        target_ctr_percent: +(targetCtr * 100).toFixed(2),\n        opportunity_score: +opportunityScore.toFixed(2),\n        status: 'À analyser',\n        next_action: 'Récupérer les top queries',\n        is_quick_win: position >= 3 && position <= 12 && impressions > 500 && ctr < targetCtr\n      }\n    };\n  })\n  .filter(item => item.json.is_quick_win)\n  .sort((a, b) => b.json.opportunity_score - a.json.opportunity_score)\n  .slice(0, 20);"
      },
      "id": "3",
      "name": "Score CTR Opportunities",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [740, 300]
    },
    {
      "parameters": {
        "batchSize": 1,
        "options": {}
      },
      "id": "4",
      "name": "Loop Over Pages",
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 3,
      "position": [980, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "=https://www.googleapis.com/webmasters/v3/sites/sc-domain:schoolswp.com/searchAnalytics/query",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "googleOAuth2Api",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"startDate\": \"{{$now.minus({days: 90}).toFormat('yyyy-MM-dd')}}\",\n  \"endDate\": \"{{$now.minus({days: 3}).toFormat('yyyy-MM-dd')}}\",\n  \"dimensions\": [\"query\"],\n  \"type\": \"web\",\n  \"rowLimit\": 20,\n  \"dimensionFilterGroups\": [\n    {\n      \"filters\": [\n        {\n          \"dimension\": \"page\",\n          \"operator\": \"equals\",\n          \"expression\": \"{{$json.url}}\"\n        }\n      ]\n    }\n  ]\n}",
        "options": {
          "response": { "response": { "responseFormat": "json" } }
        }
      },
      "id": "5",
      "name": "Search Console Queries",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [1220, 300],
      "credentials": {
        "googleOAuth2Api": {
          "id": "YOUR_GOOGLE_OAUTH_CREDENTIAL_ID",
          "name": "Google OAuth2"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const pageData = $('Loop Over Pages').item.json;\nconst rows = $json.rows || [];\n\nconst topQueries = rows\n  .map(row => ({\n    query: row.keys?.[0] || '',\n    clicks: row.clicks || 0,\n    impressions: row.impressions || 0,\n    ctr_percent: +((row.ctr || 0) * 100).toFixed(2),\n    position: +(row.position || 999).toFixed(2)\n  }))\n  .sort((a, b) => b.impressions - a.impressions)\n  .slice(0, 10);\n\nreturn [{\n  json: {\n    ...pageData,\n    top_queries: topQueries,\n    top_queries_text: topQueries\n      .map((q, i) => `${i + 1}. ${q.query} | CTR ${q.ctr_percent}% | Pos ${q.position} | Imp ${q.impressions}`)\n      .join('\\n')\n  }\n}];"
      },
      "id": "6",
      "name": "Attach Top Queries",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [1460, 300]
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": "YOUR_GOOGLE_SHEET_ID",
        "sheetName": "Tests CTR",
        "columns": {
          "mappingMode": "autoMapInputData"
        },
        "options": {}
      },
      "id": "7",
      "name": "Log to Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [1700, 220],
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "YOUR_GOOGLE_SHEETS_CREDENTIAL_ID",
          "name": "Google Sheets OAuth2"
        }
      }
    },
    {
      "parameters": {
        "sendTo": "you@example.com",
        "subject": "=[CTR Hunter V2] {{$json.url}} à optimiser",
        "emailType": "text",
        "message": "=URL : {{$json.url}}\\nCTR : {{$json.ctr_percent}}%\\nPosition : {{$json.position}}\\nImpressions : {{$json.impressions}}\\nCTR cible : {{$json.target_ctr_percent}}%\\nScore : {{$json.opportunity_score}}\\n\\nTop queries :\\n{{$json.top_queries_text}}\\n\\nAction recommandée : tester un nouveau title."
      },
      "id": "8",
      "name": "Send Email Alert",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 2.1,
      "position": [1700, 380],
      "credentials": {
        "gmailOAuth2": {
          "id": "YOUR_GMAIL_CREDENTIAL_ID",
          "name": "Gmail OAuth2"
        }
      }
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [[{ "node": "Search Console Pages", "type": "main", "index": 0 }]]
    },
    "Search Console Pages": {
      "main": [
        [{ "node": "Score CTR Opportunities", "type": "main", "index": 0 }]
      ]
    },
    "Score CTR Opportunities": {
      "main": [[{ "node": "Loop Over Pages", "type": "main", "index": 0 }]]
    },
    "Loop Over Pages": {
      "main": [
        [{ "node": "Search Console Queries", "type": "main", "index": 0 }],
        []
      ]
    },
    "Search Console Queries": {
      "main": [[{ "node": "Attach Top Queries", "type": "main", "index": 0 }]]
    },
    "Attach Top Queries": {
      "main": [
        [
          { "node": "Log to Google Sheets", "type": "main", "index": 0 },
          { "node": "Send Email Alert", "type": "main", "index": 0 }
        ]
      ]
    }
  },
  "active": false,
  "settings": { "executionOrder": "v1" },
  "versionId": "2",
  "meta": { "templateCredsSetupCompleted": false },
  "id": "schoolswp-ctr-hunter-v2",
  "tags": []
}
```

---

## V3 — Génération automatique de titles via LLM

**Ce que fait V3 pour chaque page détectée :**

1. Récupère la page + ses top queries (= V2)
2. Construit un prompt IA avec les données
3. Génère 10 titles SEO optimisés CTR + top 3 + hypothèse de test
4. Parse la réponse JSON
5. Logge dans Google Sheets + alerte Gmail

**Architecture :**

```text
Schedule → GSC pages → Scoring → Loop Over Items
  → GSC queries filtrées → Code fusion
  → Code prompt → Basic LLM Chain + OpenAI Chat Model
  → Code parse → Google Sheets + Gmail
```

**Node IA recommandé :** `Basic LLM Chain` + `OpenAI Chat Model` (sous-node)

Pourquoi : le prompt est séparé du modèle — maintenable, remplaçable sans refaire la logique.

### Prompt IA (à coller dans Basic LLM Chain)

```text
Tu es un expert SEO spécialisé dans l'optimisation du CTR organique dans Google.

Ta mission : proposer 10 titles SEO optimisés pour améliorer le CTR d'une page déjà positionnée dans Google.

Contexte :
- URL : {{$json.url}}
- CTR actuel : {{$json.ctr_percent}}%
- Position moyenne : {{$json.position}}
- Impressions : {{$json.impressions}}
- CTR cible : {{$json.target_ctr_percent}}%
- Top queries :
{{$json.top_queries_text}}

Contraintes :
- rester crédible
- éviter le clickbait trompeur
- inclure naturellement le sujet principal
- varier les angles
- viser des titles clairs, concrets, différenciants
- privilégier des titles adaptés à une audience WordPress experte et pédagogique

Tu dois produire exactement :
1) 10 titles numérotés
2) 3 titles prioritaires à tester
3) 1 hypothèse de test CTR
4) 1 recommandation finale en une phrase

Format de sortie JSON strict :
{
  "titles": ["title 1", "title 2", "title 3", "title 4", "title 5", "title 6", "title 7", "title 8", "title 9", "title 10"],
  "top_3": ["title x", "title y", "title z"],
  "test_hypothesis": "…",
  "final_recommendation": "…"
}
```

### Code node — Parser la réponse IA

````javascript
let raw = $json.text || $json.response || $json.output || "";
raw = raw.trim();
raw = raw
  .replace(/^```json\s*/i, "")
  .replace(/^```\s*/i, "")
  .replace(/```$/i, "")
  .trim();

const parsed = JSON.parse(raw);

return [
  {
    json: {
      ...$("Attach Top Queries").item.json,
      generated_titles: (parsed.titles || []).join(" | "),
      top_3_titles: (parsed.top_3 || []).join(" | "),
      test_hypothesis: parsed.test_hypothesis || "",
      final_recommendation: parsed.final_recommendation || "",
    },
  },
];
````

### Colonnes Google Sheet V3 (ajouter aux colonnes V2)

`generated_titles` / `top_3_titles` / `test_hypothesis` / `final_recommendation`

Stockage : titles séparés par `|` pour rester dans une seule cellule.

### Alerte Gmail V3

```text
Sujet : [CTR Hunter V3] Titles générés pour {{$json.url}}

URL : {{$json.url}}
CTR : {{$json.ctr_percent}}% | Position : {{$json.position}} | Impressions : {{$json.impressions}}

Top queries :
{{$json.top_queries_text}}

Top 3 titles à tester :
{{$json.top_3_titles}}

Hypothèse : {{$json.test_hypothesis}}
Reco : {{$json.final_recommendation}}
```

---

## Roadmap V3.x

| Étape | Ce qu'elle ajoute                                                                                                            |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| V3.1  | Génération auto 10 titles + stockage Sheets + alerte email                                                                   |
| V3.2  | Colonnes `title_tested`, `test_start_date`, `test_result` dans le tracker                                                    |
| V3.3  | Second workflow qui relit les tests après 21 jours, compare avant/après, marque Concluant / Neutre / Négatif automatiquement |

V3.3 = boucle CTR autonome complète. Plus de suivi manuel.

---

## Architecture finale — 2 workflows séparés

**schoolsWP CTR Hunter** + **schoolsWP CTR Judge**

| Workflow       | Rôle                           | Déclenchement      |
| -------------- | ------------------------------ | ------------------ |
| **CTR Hunter** | Détecter + enrichir + proposer | Lundi 08:00, hebdo |
| **CTR Judge**  | Relire + comparer + classer    | Quotidien 07:30    |

**Règles fondamentales :**

- CTR Hunter ne décide pas du verdict
- CTR Judge ne génère pas de nouveaux titles
- 1 test = 1 variable (title OU meta, jamais les deux)
- Pas de verdict sans 21 jours minimum

---

### Workflow A — schoolsWP CTR Hunter (détection + génération)

**Déclenchement :** lundi 08:00, hebdomadaire

**Pipeline :**

```text
Schedule Trigger
→ Search Console API (dimensions=["page"], 90j)
→ Code (quick wins : pos 3-12 / imp >500 / CTR < cible)
→ Loop Over Items (batchSize=1)
  → Search Console API (dimensions=["query"], filtré par URL)
  → Code (fusion page + top queries)
  → Basic LLM Chain + OpenAI Chat Model (10 titles + top 3 + hypothèse)
  → Code (parse JSON réponse)
  → Google Sheets (append ligne)
  → Gmail / Slack (alerte)
```

**Ce qu'il écrit dans le sheet :**

`id` / `date_scan` / `url` / `top_queries_text` / `generated_titles` / `top_3_titles` / `recommended_title` / `test_hypothesis` / `final_recommendation` / `ctr_before` / `position_before` / `impressions_before` / `status` = `À lancer`

**Colonnes laissées vides :** `title_tested` / `test_start_date` / `review_date` / `ctr_after` / `verdict` / `notes`

---

### Workflow B — schoolsWP CTR Judge (suivi + verdict)

**Déclenchement :** quotidien à 07:30

**Condition d'entrée :** lignes où `status = En cours` ET `test_start_date ≤ aujourd'hui - 21j`

**Pipeline :**

```text
Schedule Trigger (quotidien 07:30)
→ Google Sheets (lire toutes les lignes)
→ Code (filtrer : status="En cours" ET test_start_date ≤ J-21)
→ Loop Over Items (1 ligne à la fois)
  → HTTP Request (GSC : CTR actuel de l'URL sur les 14 derniers jours)
  → Code (comparer CTR avant vs CTR après + détection signal trompeur)
  → Google Sheets (mettre à jour : verdict + position_after + ctr_after + ctr_delta + next_action + status)
  → Gmail (alerte résultat)
```

**Logique de verdict (Code node) :**

```javascript
const ctrBefore = $json.ctr_percent;
const ctrAfter = $json.ctr_current;
const posBefore = $json.position;
const posAfter = $json.position_current;

const deltaCtr = ctrAfter - ctrBefore;
const deltaPos = posAfter - posBefore; // négatif = amélioration position

// Signal trompeur : CTR monte PARCE QUE la position s'est améliorée fortement
const isMisleading = deltaCtr > 0.5 && deltaPos < -2;

let verdict;
if (isMisleading)
  verdict = "Neutre"; // gain de CTR attribuable à la position, pas au title
else if (deltaCtr > 0.5) verdict = "Concluant";
else if (deltaCtr < -0.5) verdict = "Négatif";
else verdict = "Neutre";

const nextAction =
  verdict === "Concluant"
    ? "Conserver + tester meta description"
    : verdict === "Négatif"
      ? "Revenir au title précédent"
      : isMisleading
        ? "Position améliorée — attendre stabilisation avant verdict"
        : "Tester un angle différent";

return [
  {
    json: {
      ...$json,
      ctr_after: +ctrAfter.toFixed(2),
      position_after: +posAfter.toFixed(1),
      ctr_delta: +deltaCtr.toFixed(2),
      verdict,
      next_action: nextAction,
      status: verdict, // Concluant / Neutre / Négatif
    },
  },
];
```

**Seuils de verdict :**

| Delta CTR              | Condition                | Verdict   | Action                     |
| ---------------------- | ------------------------ | --------- | -------------------------- |
| > +0.5 %               | Position stable (±2)     | Concluant | Conserver + tester meta    |
| > +0.5 %               | Position amélioration >2 | Neutre    | Attendre stabilisation     |
| Entre -0.5 % et +0.5 % | —                        | Neutre    | Tester un angle différent  |
| < -0.5 %               | —                        | Négatif   | Revenir au title précédent |

---

### Google Sheet partagé — 25 colonnes

| #   | Colonne              | Hunter (A) | Manuel (toi) | Judge (B)     |
| --- | -------------------- | ---------- | ------------ | ------------- |
| 1   | `id`                 | Écrit      | —            | —             |
| 2   | `owner`              | Écrit      | —            | —             |
| 3   | `site_property`      | Écrit      | —            | —             |
| 4   | `date_scan`          | Écrit      | —            | —             |
| 5   | `url`                | Écrit      | —            | Lu            |
| 6   | `keyword_main`       | Écrit      | —            | —             |
| 7   | `ctr_before`         | Écrit      | —            | Lu (baseline) |
| 8   | `position_before`    | Écrit      | —            | Lu            |
| 9   | `impressions_before` | Écrit      | —            | —             |
| 10  | `opportunity_score`  | Écrit      | —            | —             |
| 11  | `top_queries_text`   | Écrit      | —            | —             |
| 12  | `generated_titles`   | Écrit      | —            | —             |
| 13  | `top_3_titles`       | Écrit      | —            | —             |
| 14  | `recommended_title`  | Écrit      | —            | —             |
| 15  | `title_initial`      | Écrit      | —            | —             |
| 16  | `title_tested`       | Vide       | **Écrit**    | Lu            |
| 17  | `test_start_date`    | Vide       | **Écrit**    | Filtre (J+21) |
| 18  | `status`             | `À lancer` | `En cours`   | Verdict final |
| 19  | `ctr_after`          | —          | —            | Écrit         |
| 20  | `position_after`     | —          | —            | Écrit         |
| 21  | `ctr_delta`          | —          | —            | Écrit         |
| 22  | `verdict`            | —          | —            | Écrit         |
| 23  | `next_action`        | —          | —            | Écrit         |
| 24  | `review_date`        | —          | —            | Écrit         |
| 25  | `notes`              | —          | Optionnel    | —             |

**Statuts autorisés (liste fermée) :**

- `À lancer` — Hunter a détecté la page, aucun test démarré
- `En cours` — title modifié dans Rank Math, test actif
- `Concluant` — CTR amélioré, signal fiable
- `Neutre` — pas d'amélioration nette
- `Négatif` — CTR dégradé, revenir au title précédent
- `Archivé` — test clôturé manuellement (raison dans `notes`)

---

### Flux complet

```text
schoolsWP CTR Hunter (lundi 08:00, hebdomadaire)
  → détecte les pages quick wins dans GSC
  → génère les titles via LLM
  → logge dans Sheets (status = À lancer)

Toi (manuellement, 5 min par ligne)
  → choisis 1 title dans top_3_titles
  → modifies le title dans Rank Math
  → remplis title_tested + test_start_date dans Sheets (3 cellules)
  → passes status à "En cours"

schoolsWP CTR Judge (quotidien 07:30, dès J+21)
  → lit les lignes status="En cours" ET test_start_date ≤ J-21
  → récupère le CTR actuel dans GSC
  → calcule le delta + détecte signal trompeur
  → attribue le verdict (Concluant / Neutre / Négatif)
  → met à jour Sheets (status = verdict) + alerte Gmail
```

La seule action manuelle : modifier le title dans Rank Math et remplir 3 cellules dans Sheets.
