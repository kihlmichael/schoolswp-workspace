# Configuration nœud Google Sheets dans n8n

## Paramètres principaux

- **Operation** : `Append or Update Row` (ou `Append Row` si tu ne veux pas de déduplication)
- **Document** : sélectionne ton Google Sheet
- **Sheet** : sélectionne l'onglet cible
- **Mapping Column Mode** : `Map Each Column Manually`

## Mapping des colonnes

Dans la section **Values**, crée une entrée par colonne :

| Column               | Value                            |
| -------------------- | -------------------------------- |
| `Nom`                | `{{ $json.Nom }}`                |
| `Email`              | `{{ $json.Email }}`              |
| `Téléphone`          | `{{ $json.Téléphone }}`          |
| `Activité_souhaitée` | `{{ $json.Activité_souhaitée }}` |
| `Date_activité`      | `{{ $json.Date_activité }}`      |

## Si tu utilises "Append or Update Row"

Il faut définir **Matching Columns** (la colonne clé pour éviter les doublons). Exemple : `Email`.

## Si tu utilises "Append Row"

Pas de matching column nécessaire — chaque exécution ajoute une nouvelle ligne.

## Résumé configuration recommandée

```
Resource       : Sheet
Operation      : Append Row
Document       : [ton fichier]
Sheet          : [ton onglet]
Data Mode      : Map Each Column Manually
Values         :
  Nom                 → {{ $json.Nom }}
  Email               → {{ $json.Email }}
  Téléphone           → {{ $json.Téléphone }}
  Activité_souhaitée  → {{ $json.Activité_souhaitée }}
  Date_activité       → {{ $json.Date_activité }}
```

> Note : les noms de colonnes dans le mapping doivent correspondre exactement aux en-têtes de la ligne 1 du Sheet (y compris accents et underscores).
