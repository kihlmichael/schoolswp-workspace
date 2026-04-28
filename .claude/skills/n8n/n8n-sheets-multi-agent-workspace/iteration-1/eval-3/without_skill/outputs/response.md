# Mapping WooCommerce → Google Sheets dans n8n

## Configuration du nœud Google Sheets

**Operation** : Append or Update (ou Append Row si pas de déduplication nécessaire)
**Mapping Mode** : Define Below (`defineBelow`)

## Mapping des colonnes

| Colonne Sheets | Expression n8n               |
| -------------- | ---------------------------- |
| ID commande    | `{{ $json.order_id }}`       |
| Client         | `{{ $json.customer_name }}`  |
| Email          | `{{ $json.customer_email }}` |
| Montant        | `{{ $json.total }}`          |
| Devise         | `{{ $json.currency }}`       |
| Statut         | `{{ $json.status }}`         |

> `items_count` n'a pas de colonne dédiée — à ignorer ou ajouter une colonne "Nb articles" si besoin.

## Paramètres du nœud

- **Authentication** : OAuth2 (compte Google connecté)
- **Resource** : Spreadsheet
- **Operation** : Append Row (si tu veux juste ajouter) ou Append or Update (si tu veux éviter les doublons sur l'ID)
- **Spreadsheet ID** : ton ID Google Sheet (dans l'URL)
- **Sheet** : nom de l'onglet (ex: `Commandes`)
- **Mapping Mode** : `defineBelow` — puis ajouter chaque champ manuellement

Si tu utilises **Append or Update**, configure aussi :

- **Column to Match On** : `ID commande` (pour déduplication sur l'order_id)

## Version du nœud

Utilise **googleSheets typeVersion 4.5** (version confirmée stable sur n8n 2.0.x).

## Structure du workflow

```
WooCommerce Trigger (ou Webhook)
        ↓
Google Sheets — Append Row
```

Si tu pars d'un webhook WooCommerce, le payload arrive directement dans `$json` et les expressions ci-dessus fonctionnent sans transformation supplémentaire.
