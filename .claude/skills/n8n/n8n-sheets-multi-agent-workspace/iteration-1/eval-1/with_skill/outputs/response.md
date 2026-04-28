# Configuration nœud Google Sheets — Webinar Tally

> 3 agents lancés en parallèle : JSON Analyst · Columns Analyst · Mapper

---

## Résultats Agent 1 — JSON Analyst

**Structure du JSON**

- JSON **plat** (1 seul niveau, aucun champ imbriqué)
- 6 champs au total

| Champ              | Valeur exemple               | Type détecté                | Risques                                                                             |
| ------------------ | ---------------------------- | --------------------------- | ----------------------------------------------------------------------------------- |
| `prenom`           | `"Sophie"`                   | string                      | aucun                                                                               |
| `nom`              | `"Bernard"`                  | string                      | aucun                                                                               |
| `email`            | `"sophie.bernard@agence.fr"` | string                      | aucun                                                                               |
| `telephone`        | `"0654321987"`               | **string** (commence par 0) | ⚠️ Risque numérique — si Google Sheets traite comme nombre, le 0 initial sera perdu |
| `entreprise`       | `"Agence Digital"`           | string                      | aucun                                                                               |
| `date_inscription` | `"2025-05-10"`               | string (format ISO 8601)    | ⚠️ Google Sheets peut interpréter comme date et reformater                          |

---

## Résultats Agent 2 — Columns Analyst

**Correspondances JSON ↔ Colonnes Sheet**

| Colonne Sheet      | Champ JSON         | Statut     | Différence                                              |
| ------------------ | ------------------ | ---------- | ------------------------------------------------------- |
| `Prénom`           | `prenom`           | ⚠️ Approx. | Accent manquant dans JSON (`é` → `e`), casse différente |
| `Nom`              | `nom`              | ⚠️ Approx. | Casse différente (majuscule vs minuscule)               |
| `Email`            | `email`            | ⚠️ Approx. | Casse différente                                        |
| `Téléphone`        | `telephone`        | ⚠️ Approx. | Accent manquant + casse (`é` → `e`)                     |
| `Entreprise`       | `entreprise`       | ⚠️ Approx. | Casse différente                                        |
| `Date inscription` | `date_inscription` | ⚠️ Approx. | Underscore vs espace, casse différente                  |

**Champs JSON sans colonne** : aucun (6/6 mappés)

**Colonnes sans champ JSON** : aucune

**Recommandation** : Auto-Map **inutilisable** — les noms ne correspondent jamais exactement (accents, casse, underscores). **Mapping manuel obligatoire.**

---

## Résultats Agent 3 — Mapper

**Réglages nœud Google Sheets**

```
Resource  : Sheet Within Document
Operation : Append Row
Mode      : Map Each Column Manually
Data Mode : Define Below
```

**Expressions par colonne**

```
Prénom           → {{ $json["prenom"] }}
Nom              → {{ $json["nom"] }}
Email            → {{ $json["email"] }}
Téléphone        → {{ $json["telephone"] }}
Entreprise       → {{ $json["entreprise"] }}
Date inscription → {{ $json["date_inscription"] }}
```

---

## 1. Diagnostic rapide

- JSON **plat**, 6 champs, aucune imbrication
- **6/6 correspondances trouvées** — toutes approximatives (accents/casse/underscore)
- Auto-Map ne fonctionnera pas : les noms de colonnes Sheet ne correspondent jamais exactement aux clés JSON
- Deux risques de format : `telephone` (zéro initial) et `date_inscription` (reformatage auto Sheets)

---

## 2. Réglages du nœud à utiliser

```
Resource  : Sheet Within Document
Operation : Append Row
Mode      : Map Each Column Manually
Data Mode : Define Below
```

---

## 3. Mapping colonne par colonne

```
Prénom           → {{ $json["prenom"] }}
Nom              → {{ $json["nom"] }}
Email            → {{ $json["email"] }}
Téléphone        → {{ $json["telephone"] }}
Entreprise       → {{ $json["entreprise"] }}
Date inscription → {{ $json["date_inscription"] }}
```

---

## 4. Erreurs ou incohérences détectées

**Aucune incohérence bloquante.** Les 6 colonnes ont une correspondance JSON.

Points d'attention :

1. **`telephone`** — valeur `"0654321987"` déjà en string dans le JSON, donc le 0 initial est préservé. Mais si Google Sheets est formaté en "Nombre" sur cette colonne, il supprimera le 0. **Forcer le format "Texte brut" sur la colonne Téléphone dans Sheets.**

2. **`date_inscription`** — format ISO `"2025-05-10"` reconnu automatiquement par Google Sheets et converti en date locale (ex: `10/05/2025`). Si tu veux conserver le format ISO exact, **forcer "Texte brut" sur la colonne Date inscription** avant d'envoyer des données.

---

## 5. Erreurs fréquentes à éviter

- **Ne pas utiliser Auto-Map** — aucun nom de clé JSON ne correspond exactement aux en-têtes (accents, casse, underscores). Le mode auto produira des colonnes vides sans erreur visible.
- **Guillemets** — toujours des **doubles guillemets** dans les expressions : `$json["prenom"]` et non `$json['prenom']`.
- **Casse des clés** — `$json["Prenom"]` ≠ `$json["prenom"]`. Les clés JSON sont en minuscules sans accent — respecter exactement.
- **Téléphone** — ne pas laisser la colonne Sheet en format "Nombre automatique", le 0 initial disparaîtra.
- **Date** — si le format ISO doit être préservé tel quel, formater la colonne en "Texte brut" **avant** le premier envoi.
- **Ligne 1 vide** — si la ligne 1 du Sheet ne contient pas les en-têtes exacts, n8n ne trouvera pas les colonnes. Toujours vérifier avec "Reload columns" dans le nœud.

---

## 6. Checklist avant test

```
[ ] Credentials Google Sheets configurées dans n8n (OAuth2 ou Service Account)
[ ] Spreadsheet ID et onglet cible sélectionnés dans le nœud
[ ] Ligne 1 du sheet = en-têtes exacts : Prénom | Nom | Email | Téléphone | Entreprise | Date inscription
[ ] Colonne "Téléphone" formatée en Texte brut dans Google Sheets
[ ] Colonne "Date inscription" formatée selon le format souhaité (Texte brut pour ISO)
[ ] Mode = Map Each Column Manually
[ ] Data Mode = Define Below
[ ] Toutes les expressions en doubles guillemets
[ ] Workflow sauvegardé avant test
[ ] Test avec "Execute node" sur un item réel du webhook Tally
```

---

## 7. Mapping final copy-paste

```
RÉGLAGES
--------
Resource  : Sheet Within Document
Operation : Append Row
Mode      : Map Each Column Manually
Data Mode : Define Below

MAPPING
-------
Prénom           → {{ $json["prenom"] }}
Nom              → {{ $json["nom"] }}
Email            → {{ $json["email"] }}
Téléphone        → {{ $json["telephone"] }}
Entreprise       → {{ $json["entreprise"] }}
Date inscription → {{ $json["date_inscription"] }}
```
