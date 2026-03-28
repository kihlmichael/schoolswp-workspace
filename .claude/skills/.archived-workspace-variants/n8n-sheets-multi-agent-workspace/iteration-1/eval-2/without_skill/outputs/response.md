# Configuration du nœud Google Sheets dans n8n

## Paramètres principaux

- **Operation** : `Append or Update` (ou `Append` si tu n'as pas besoin de dédupliquer)
- **Document** : sélectionner ton Google Spreadsheet
- **Sheet** : sélectionner l'onglet cible
- **Mapping Mode** : `Define Below` (mappage manuel)

---

## Mapping des colonnes

| Colonne Sheet | Expression n8n                   |
| ------------- | -------------------------------- |
| Prénom        | `{{ $json.lead.first_name }}`    |
| Nom           | `{{ $json.lead.last_name }}`     |
| Email         | `{{ $json.lead.contact.email }}` |
| Téléphone     | `{{ $json.lead.contact.phone }}` |
| Source        | `{{ $json.source }}`             |
| Score         | `{{ $json.score }}`              |
| Date création | `{{ $json.created_at }}`         |

---

## Configuration détaillée étape par étape

### 1. Ajouter le nœud

Ajoute un nœud **Google Sheets** après ton nœud API CRM.

### 2. Authentification

Connecte ton compte Google via OAuth2 (ou Service Account si configuré).

### 3. Paramètres du nœud

```
Resource       : Sheet Within Document
Operation      : Append Row (ou Append or Update)
Document ID    : [ton spreadsheet]
Sheet Name     : [ton onglet]
Data Mode      : Define Below (mappage manuel)
```

### 4. Champs à mapper

Dans la section **Fields to Send**, ajoute une entrée par colonne :

| Field Name (= nom exact de la colonne dans le Sheet) | Value                             |
| ---------------------------------------------------- | --------------------------------- |
| `Prénom`                                             | `={{ $json.lead.first_name }}`    |
| `Nom`                                                | `={{ $json.lead.last_name }}`     |
| `Email`                                              | `={{ $json.lead.contact.email }}` |
| `Téléphone`                                          | `={{ $json.lead.contact.phone }}` |
| `Source`                                             | `={{ $json.source }}`             |
| `Score`                                              | `={{ $json.score }}`              |
| `Date création`                                      | `={{ $json.created_at }}`         |

> Les noms de champs doivent correspondre **exactement** aux en-têtes de ta première ligne dans le Sheet (accents inclus).

---

## Notes importantes

**typeVersion** : utilise la version `4.5` (version confirmée sur n8n 2.0.3).

**Si tu utilises `Append or Update`** : le champ `Matching Columns` est obligatoire et ne doit pas être vide. Utilise `Email` comme clé de déduplication — ça évite les doublons si le même lead arrive deux fois.

**Format de la date** : `created_at` arrive en ISO 8601 (`2025-03-15T14:30:00Z`). Google Sheets l'accepte tel quel, mais si tu veux un format lisible, transforme-le en amont avec :

```
={{ new Date($json.created_at).toLocaleDateString('fr-FR') }}
```

**Score** : c'est un nombre entier (`87`), il sera stocké comme valeur numérique sans configuration supplémentaire.

---

## Résultat attendu dans le Sheet

| Prénom | Nom   | Email           | Téléphone    | Source   | Score | Date création        |
| ------ | ----- | --------------- | ------------ | -------- | ----- | -------------------- |
| Marc   | Duval | marc@startup.io | +33612345678 | LinkedIn | 87    | 2025-03-15T14:30:00Z |
