# Configuration Google Sheets — Mapping des données

## Pourquoi `{{ $json.prenom }}` ne fonctionne pas

Le problème vient du **mode de mapping**. Quand tu utilises `mappingMode: "defineBelow"` avec des expressions manuelles, n8n attend que chaque colonne soit explicitement mappée. Si le nœud est mal configuré (champ `value` vide ou mapping mode incorrect), les expressions ne s'évaluent pas.

Vérifie aussi : dans le nœud Google Sheets, il faut parfois accéder aux données via `{{ $json["prenom"] }}` plutôt que `{{ $json.prenom }}` si la clé contient des caractères spéciaux — mais ici `prenom` est simple, donc les deux formes marchent.

La vraie cause est souvent le `mappingMode`.

---

## Configuration correcte du nœud Google Sheets

### Paramètres généraux

| Paramètre        | Valeur                                                    |
| ---------------- | --------------------------------------------------------- |
| **Operation**    | `Append or Update` (ou `Append` si tu veux juste ajouter) |
| **Document**     | Sélectionner ton Google Sheets                            |
| **Sheet**        | Sélectionner la bonne feuille                             |
| **Mapping Mode** | `Define Below` (pas `Auto-Map`)                           |

> Si tu utilises `autoMapInputData`, n8n essaie de faire correspondre les noms de champs JSON avec les en-têtes de colonnes automatiquement — ça ne marchera pas ici car `prenom` ≠ `Prénom` (accents, majuscules, espaces).

---

### Mapping colonne par colonne

En mode `Define Below`, configure chaque colonne comme suit :

| Colonne Google Sheets  | Valeur à saisir             |
| ---------------------- | --------------------------- |
| **Prénom**             | `{{ $json.prenom }}`        |
| **Email**              | `{{ $json.email }}`         |
| **Téléphone**          | `{{ $json.telephone }}`     |
| **Activité souhaitée** | `{{ $json.activite }}`      |
| **Date activité**      | `{{ $json.date }}`          |
| **Statut**             | Valeur fixe ou laisser vide |

---

## Checklist de débogage

1. **Vérifie que le nœud précédent a bien été exécuté** — clique sur le nœud source et confirme que les données apparaissent dans l'onglet "Output".

2. **Utilise l'onglet "Input" du nœud Google Sheets** — tu dois voir les 6 champs JSON listés. Si l'onglet est vide, le problème vient du nœud en amont, pas du mapping.

3. **Mode de mapping** — passe en `Define Below` et saisis manuellement chaque paire colonne/expression.

4. **`Append or Update` avec `matchingColumns`** — si tu utilises cette opération, le champ `matchingColumns` ne doit PAS être vide. Mets `Email` par exemple comme clé de correspondance, sinon le nœud bloque.

5. **Authentification** — vérifie que les credentials Google sont valides et ont accès au fichier.

---

## Configuration JSON recommandée (typeVersion 4.5)

Si tu édites le JSON du workflow directement :

```json
{
  "operation": "appendOrUpdate",
  "mappingMode": "defineBelow",
  "matchingColumns": ["Email"],
  "columns": {
    "value": {
      "Prénom": "={{ $json.prenom }}",
      "Email": "={{ $json.email }}",
      "Téléphone": "={{ $json.telephone }}",
      "Activité souhaitée": "={{ $json.activite }}",
      "Date activité": "={{ $json.date }}",
      "Statut": ""
    }
  }
}
```

> Note : dans le JSON brut, les expressions doivent commencer par `=` puis `{{ ... }}`.

---

## Résumé

Le problème le plus fréquent dans ce cas : le `mappingMode` n'est pas en `Define Below`, ou `matchingColumns` est vide sur une opération `appendOrUpdate`. Passe en mode `Define Below` et saisis manuellement chaque colonne — ça marchera.
