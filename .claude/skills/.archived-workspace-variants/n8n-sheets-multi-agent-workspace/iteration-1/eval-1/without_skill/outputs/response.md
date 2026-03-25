# Configuration nœud Google Sheets — Inscription webinar Tally

## Paramètres du nœud

**Operation** : `Append or Update Row`
**Document** : sélectionner ton Google Sheet
**Sheet** : sélectionner l'onglet concerné

---

## Mapping des colonnes

Dans la section **"Values to Send"**, passer en mode `Define Below` et ajouter une ligne par colonne :

| Colonne Google Sheets | Valeur n8n                     |
| --------------------- | ------------------------------ |
| Prénom                | `{{ $json.prenom }}`           |
| Nom                   | `{{ $json.nom }}`              |
| Email                 | `{{ $json.email }}`            |
| Téléphone             | `{{ $json.telephone }}`        |
| Entreprise            | `{{ $json.entreprise }}`       |
| Date inscription      | `{{ $json.date_inscription }}` |

---

## Points d'attention

**typeVersion** : utilise la version **4.5** (confirmée compatible n8n 2.0.3).

**Matching column** : si tu utilises `Append or Update`, tu dois définir une colonne de correspondance pour éviter les doublons. Recommandé : `Email`. Cela mettra à jour la ligne si l'email existe déjà, ou ajoutera une nouvelle ligne sinon.

Si tu veux uniquement **ajouter** sans vérification de doublon, utilise l'operation `Append Row` — dans ce cas le champ `matchingColumns` n'est pas requis.

**Mapping mode** : ne pas utiliser `autoMapInputData` ici car les noms de champs JSON (`prenom`, `email`…) ne correspondent pas exactement aux en-têtes du sheet (`Prénom`, `Email`…) — le mapping manuel est obligatoire.

---

## Configuration complète (résumé)

```
Resource        : Sheet
Operation       : Append or Update Row
Document ID     : [ton sheet]
Sheet Name      : [ton onglet]
Mapping Mode    : Define Below
Matching Columns: Email

Values:
  Prénom          → {{ $json.prenom }}
  Nom             → {{ $json.nom }}
  Email           → {{ $json.email }}
  Téléphone       → {{ $json.telephone }}
  Entreprise      → {{ $json.entreprise }}
  Date inscription→ {{ $json.date_inscription }}
```
