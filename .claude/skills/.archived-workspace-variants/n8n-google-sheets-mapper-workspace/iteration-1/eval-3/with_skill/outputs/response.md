# Mapping Google Sheets — Formulaire de réservation

---

## 1. Diagnostic rapide

**Ce qui est compris :** Le nœud HTTP Request renvoie un JSON imbriqué sur deux niveaux (`data.contact` et `data.booking`). Les données sont disponibles et non nulles. Les 6 colonnes du Google Sheet correspondent bien aux 6 champs présents dans le JSON.

**Ce qui est correct :** Toutes les valeurs cibles existent dans le JSON. Le format de date (`2025-04-15`) est déjà en `YYYY-MM-DD`, compatible Google Sheets. Aucun champ manquant.

**Ce qui demande attention :** Les champs sont imbriqués sous `data.contact` et `data.booking` — un `Auto-Map` ne fonctionnera pas, il faut un mapping manuel. Le numéro de téléphone commence par `+`, ce qui est correct en texte mais peut poser problème si la colonne est formatée en "Nombre" dans Sheets.

---

## 2. Réglages du nœud à utiliser

| Paramètre               | Valeur                                           |
| ----------------------- | ------------------------------------------------ |
| **Resource**            | `Sheet Within Document`                          |
| **Operation**           | `Append Row`                                     |
| **Document**            | [ID ou nom de ton Google Sheet — à sélectionner] |
| **Sheet**               | [Nom de l'onglet — à sélectionner]               |
| **Mapping Column Mode** | `Map Each Column Manually`                       |
| **Data Mode**           | `Define Below`                                   |

> Ne pas utiliser `Auto-Map Input Data` : les noms de champs JSON (`full_name`, `email_address`, etc.) ne correspondent pas aux noms de colonnes du Sheet.

---

## 3. Mapping colonne par colonne

```
Nom complet        → {{ $json["data"]["contact"]["full_name"] }}
Email              → {{ $json["data"]["contact"]["email_address"] }}
Téléphone          → {{ $json["data"]["contact"]["phone"] }}
Activité           → {{ $json["data"]["booking"]["activity"] }}
Date               → {{ $json["data"]["booking"]["date"] }}
Nombre de places   → {{ $json["data"]["booking"]["slots"] }}
```

---

## 4. Erreurs ou incohérences détectées

- **Aucune incohérence détectée** sur le mapping lui-même — tous les champs JSON existent et correspondent à chaque colonne.

- **Téléphone — risque de formatage** : la valeur `"+33612345678"` est une chaîne de caractères. Si la colonne "Téléphone" est formatée en "Nombre" dans Google Sheets, le `+` sera rejeté ou la valeur tronquée. S'assurer que la colonne est en format **Texte** dans Sheets.

- **Nombre de places — type numérique** : `slots` vaut `2` (entier). Si la colonne est en format Texte, la valeur sera stockée comme texte `"2"` — sans impact fonctionnel majeur, mais à savoir si des calculs sont prévus dans le sheet.

---

## 5. Erreurs fréquentes à éviter

- **Laisser `Auto-Map`** avec ce JSON imbriqué → toutes les colonnes seront vides, aucune erreur explicite ne sera remontée par n8n.
- **Oublier les guillemets doubles** dans les expressions (`$json['data']` au lieu de `$json["data"]`) → erreur d'exécution silencieuse ou valeur `undefined`.
- **Colonne "Téléphone" en format Nombre** dans Sheets → le `+33` sera interprété comme un nombre positif, le préfixe sera perdu.
- **Sélectionner le mauvais onglet** si le Google Sheet a plusieurs onglets → les en-têtes ne seront pas reconnus, les lignes s'ajouteront au mauvais endroit.
- **En-têtes absents en ligne 1** du sheet → n8n ne trouvera pas les colonnes et ignorera silencieusement les valeurs.

---

## 6. Checklist avant test

```
[ ] Le Google Sheet est bien connecté (credentials Google configurées dans n8n)
[ ] L'onglet cible est bien sélectionné (pas le mauvais onglet)
[ ] La ligne 1 du sheet contient exactement : Nom complet | Email | Téléphone | Activité | Date | Nombre de places
[ ] Mapping Column Mode = "Map Each Column Manually"
[ ] Data Mode = "Define Below"
[ ] La colonne "Téléphone" est formatée en Texte dans Google Sheets
[ ] Les expressions ont été saisies avec des doubles guillemets
[ ] Le workflow est sauvegardé avant le test
[ ] Un test manuel a été déclenché avec des données réelles du nœud précédent
```

---

## 7. Mapping final prêt à appliquer

```
RÉGLAGES
--------
Resource  : Sheet Within Document
Operation : Append Row
Mode      : Map Each Column Manually
Data Mode : Define Below

MAPPING
-------
Nom complet      → {{ $json["data"]["contact"]["full_name"] }}
Email            → {{ $json["data"]["contact"]["email_address"] }}
Téléphone        → {{ $json["data"]["contact"]["phone"] }}
Activité         → {{ $json["data"]["booking"]["activity"] }}
Date             → {{ $json["data"]["booking"]["date"] }}
Nombre de places → {{ $json["data"]["booking"]["slots"] }}
```
