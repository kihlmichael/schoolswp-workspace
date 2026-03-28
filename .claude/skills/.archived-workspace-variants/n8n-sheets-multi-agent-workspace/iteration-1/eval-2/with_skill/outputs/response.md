# Mapping n8n → Google Sheets — CRM Lead

> 3 agents lancés en parallèle : JSON Analyst, Columns Analyst, Mapper.
> Résultats agrégés ci-dessous.

---

## 1. Diagnostic rapide

- **JSON** : imbriqué sur 3 niveaux (`lead` → `contact` → champs terminaux)
- **Champs disponibles** : 7 valeurs mappables (`first_name`, `last_name`, `email`, `phone`, `source`, `score`, `created_at`)
- **Colonnes du sheet** : 7 colonnes — correspondance complète trouvée pour chaque
- **Auto-Map** : inutilisable — noms de colonnes en français, champs JSON en anglais avec structure imbriquée
- **Mapping manuel obligatoire** sur toutes les colonnes
- **Point d'attention** : `Téléphone` commence par `+33` (string, pas de risque de troncature si la colonne est en format Texte dans Sheets) ; `Date création` est en ISO 8601 — à formater si affichage humain attendu

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
Prénom         → {{ $json["lead"]["first_name"] }}
Nom            → {{ $json["lead"]["last_name"] }}
Email          → {{ $json["lead"]["contact"]["email"] }}
Téléphone      → {{ $json["lead"]["contact"]["phone"] }}
Source         → {{ $json["source"] }}
Score          → {{ $json["score"] }}
Date création  → {{ $json["created_at"] }}
```

---

## 4. Erreurs ou incohérences détectées

Aucune incohérence critique. Points à noter :

- **`Date création`** : la valeur `2025-03-15T14:30:00Z` est un string ISO 8601. Google Sheets peut ne pas la reconnaître automatiquement comme date. Si tu veux un format lisible, utilise l'expression suivante à la place :
  ```
  {{ new Date($json["created_at"]).toLocaleDateString("fr-FR") }}
  ```
- **`Téléphone`** : valeur `+33612345678` — si la colonne Sheets est en format "Nombre", le `+` sera supprimé. Formater la colonne en **Texte brut** dans Google Sheets avant d'écrire.
- **`Score`** : valeur numérique `87` — aucun risque, mappé directement.

---

## 5. Erreurs fréquentes à éviter

- **Ne pas utiliser Auto-Map** : les noms de colonnes (`Prénom`, `Nom`, etc.) ne correspondent pas aux clés JSON (`first_name`, `last_name`) — Auto-Map produira des colonnes vides.
- **Guillemets simples** : n8n exige des doubles guillemets dans les expressions (`$json["champ"]` et non `$json['champ']`).
- **Champs imbriqués** : `$json["lead"]["contact"]["email"]` — ne pas écrire `$json["lead.contact.email"]` (notation pointée invalide dans n8n).
- **Colonne Téléphone en format Nombre** : Google Sheets tronque le `+` et convertit en scientifique. Toujours formater en Texte brut.
- **Workflow non sauvegardé** : les expressions ne sont pas évaluées tant que le workflow n'est pas sauvegardé — toujours sauvegarder avant de tester.

---

## 6. Checklist avant test

```
[ ] Credentials Google configurées dans n8n
[ ] Spreadsheet ID et onglet cible sélectionnés dans le nœud
[ ] Ligne 1 du sheet = en-têtes exacts (Prénom, Nom, Email, Téléphone, Source, Score, Date création)
[ ] Colonne "Téléphone" formatée en Texte brut dans Google Sheets
[ ] Mode = Map Each Column Manually
[ ] Data Mode = Define Below
[ ] Toutes les expressions en doubles guillemets
[ ] Chemins imbriqués corrects (lead > contact > email/phone)
[ ] Workflow sauvegardé avant test
[ ] Tester avec "Test step" sur une seule ligne avant activation
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
Prénom         → {{ $json["lead"]["first_name"] }}
Nom            → {{ $json["lead"]["last_name"] }}
Email          → {{ $json["lead"]["contact"]["email"] }}
Téléphone      → {{ $json["lead"]["contact"]["phone"] }}
Source         → {{ $json["source"] }}
Score          → {{ $json["score"] }}
Date création  → {{ $json["created_at"] }}
```
