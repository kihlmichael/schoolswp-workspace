---
name: notion
description: API Notion pour créer et gérer des pages, bases de données et blocs.
homepage: https://developers.notion.com
metadata: {"openclaw":{"emoji":"📝","requires":{"env":["NOTION_API_KEY"]},"primaryEnv":"NOTION_API_KEY"}}
last_reviewed: 2026-04-23
review_interval_days: 90
---

# Notion

Utilisez l'API Notion pour créer/lire/mettre à jour des pages, sources de données (databases) et blocs.

## Configuration

1. Créer une intégration sur https://notion.so/my-integrations
2. Copier la clé API (commence par `ntn_` ou `secret_`)
3. La stocker :
```bash
mkdir -p ~/.config/notion
echo "ntn_votre_cle_ici" > ~/.config/notion/api_key
```
4. Partager les pages/databases cibles avec votre intégration (cliquer "..." → "Connecter à" → nom de votre intégration)

## Bases de l'API

Toutes les requêtes nécessitent :
```bash
NOTION_KEY=$(cat ~/.config/notion/api_key)
curl -X GET "https://api.notion.com/v1/..." \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json"
```

> **Note :** Le header `Notion-Version` est requis. Ce skill utilise `2025-09-03` (dernière version). Dans cette version, les databases sont appelées "data sources" dans l'API.

## Opérations courantes

**Rechercher des pages et sources de données :**
```bash
curl -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"query": "titre de la page"}'
```

**Récupérer une page :**
```bash
curl "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03"
```

**Récupérer le contenu d'une page (blocs) :**
```bash
curl "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03"
```

**Créer une page dans une source de données :**
```bash
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"database_id": "xxx"},
    "properties": {
      "Name": {"title": [{"text": {"content": "Nouvel Élément"}}]},
      "Status": {"select": {"name": "À faire"}}
    }
  }'
```

**Requêter une source de données (database) :**
```bash
curl -X POST "https://api.notion.com/v1/data_sources/{data_source_id}/query" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {"property": "Status", "select": {"equals": "Actif"}},
    "sorts": [{"property": "Date", "direction": "descending"}]
  }'
```

**Créer une source de données (database) :**
```bash
curl -X POST "https://api.notion.com/v1/data_sources" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"page_id": "xxx"},
    "title": [{"text": {"content": "Ma Base de Données"}}],
    "properties": {
      "Name": {"title": {}},
      "Status": {"select": {"options": [{"name": "À faire"}, {"name": "Terminé"}]}},
      "Date": {"date": {}}
    }
  }'
```

**Mettre à jour les propriétés d'une page :**
```bash
curl -X PATCH "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"properties": {"Status": {"select": {"name": "Terminé"}}}}'
```

**Ajouter des blocs à une page :**
```bash
curl -X PATCH "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "children": [
      {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Bonjour"}}]}}
    ]
  }'
```

## Types de propriétés

Formats de propriétés courants pour les éléments de database :
- **Titre :** `{"title": [{"text": {"content": "..."}}]}`
- **Texte riche :** `{"rich_text": [{"text": {"content": "..."}}]}`
- **Sélection :** `{"select": {"name": "Option"}}`
- **Multi-sélection :** `{"multi_select": [{"name": "A"}, {"name": "B"}]}`
- **Date :** `{"date": {"start": "2024-01-15", "end": "2024-01-16"}}`
- **Case à cocher :** `{"checkbox": true}`
- **Nombre :** `{"number": 42}`
- **URL :** `{"url": "https://..."}`
- **Email :** `{"email": "a@b.com"}`
- **Relation :** `{"relation": [{"id": "page_id"}]}`

## Différences clés dans 2025-09-03

- **Databases → Data Sources :** Utiliser les endpoints `/data_sources/` pour les requêtes et récupérations
- **Deux IDs :** Chaque database a maintenant un `database_id` et un `data_source_id`
  - Utiliser `database_id` lors de la création de pages (`parent: {"database_id": "..."}`)
  - Utiliser `data_source_id` lors des requêtes (`POST /v1/data_sources/{id}/query`)
- **Résultats de recherche :** Les databases sont retournées comme `"object": "data_source"` avec leur `data_source_id`
- **Parent dans les réponses :** Les pages montrent `parent.data_source_id` aux côtés de `parent.database_id`
- **Trouver le data_source_id :** Rechercher la database, ou appeler `GET /v1/data_sources/{data_source_id}`

## Notes

- Les IDs de page/database sont des UUIDs (avec ou sans tirets)
- L'API ne peut pas définir les filtres de vue de database — c'est UI-only
- Limite de débit : ~3 requêtes/seconde en moyenne
- Utiliser `is_inline: true` lors de la création de data sources pour les intégrer dans les pages
