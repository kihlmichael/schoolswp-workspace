# Mapping WooCommerce → Google Sheets (n8n)

> 3 agents lancés en parallèle : JSON Analyst · Columns Analyst · Mapper

---

## 1. Diagnostic rapide

**JSON Analyst :**

- Structure **plate** (0 niveau d'imbrication) — 7 champs directement accessibles
- Types : `order_id` (number / identifiant), `customer_name` (string), `customer_email` (string), `total` (number / décimal), `currency` (string), `status` (string), `items_count` (number)
- Risque identifié : `total` est un float (89.90) — Google Sheets peut l'arrondir ou supprimer le zéro final selon le format de cellule
- `order_id` est un number — pas de risque de troncature (valeur courte), mais à formater en "Nombre entier" côté Sheets

**Columns Analyst :**

| Colonne Sheet | Champ JSON correspondant | Correspondance                                            |
| ------------- | ------------------------ | --------------------------------------------------------- |
| ID commande   | `order_id`               | ⚠️ approx. (libellé différent, pas d'espace dans le JSON) |
| Client        | `customer_name`          | ⚠️ approx. (nom court vs nom complet)                     |
| Email         | `customer_email`         | ⚠️ approx. (nom court vs nom complet)                     |
| Montant       | `total`                  | ⚠️ approx. (libellé sémantique différent)                 |
| Devise        | `currency`               | ⚠️ approx. (libellé différent)                            |
| Statut        | `status`                 | ⚠️ approx. (libellé différent)                            |

- Champ JSON sans colonne : `items_count` → ignoré (pas de colonne correspondante dans le sheet)
- Aucune correspondance exacte entre les noms JSON et les en-têtes du sheet
- **Conclusion : Auto-Map inutilisable — mapping manuel obligatoire**

**Mapper :** mapping généré, voir sections 3 et 7.

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
ID commande  →  {{ $json["order_id"] }}
Client       →  {{ $json["customer_name"] }}
Email        →  {{ $json["customer_email"] }}
Montant      →  {{ $json["total"] }}
Devise       →  {{ $json["currency"] }}
Statut       →  {{ $json["status"] }}
```

---

## 4. Erreurs ou incohérences détectées

- **Aucune colonne manquante** : les 6 colonnes du sheet ont toutes un champ JSON valide.
- **`items_count` non mappé** : présent dans le JSON mais absent du sheet — ignoré volontairement. Si tu veux l'ajouter, crée une colonne "Nb articles" et mappe `{{ $json["items_count"] }}`.
- **Auto-Map impossible** : aucun nom de colonne ne correspond exactement à un champ JSON (casse, espaces, langue différents) — le nœud Google Sheets en mode Auto-Map ne trouvera rien.

---

## 5. Erreurs fréquentes à éviter

- **Ne pas utiliser Auto-Map** — les noms de colonnes ("ID commande", "Client"…) ne matchent aucun champ JSON ("order_id", "customer_name"…). Le nœud insèrerait des lignes vides.
- **`total` / format décimal** — 89.90 peut s'afficher "89.9" dans Sheets. Formate la colonne "Montant" en "Nombre" avec 2 décimales côté Google Sheets.
- **Doubles guillemets obligatoires** dans les expressions n8n : `$json["order_id"]` et non `$json['order_id']` ni `$json.order_id`.
- **Ordre des colonnes** : le mapping doit respecter l'ordre exact des colonnes dans la ligne 1 du sheet — vérifier avant de sauvegarder.
- **Ligne 1 = en-têtes** : si la ligne 1 du sheet est vide ou contient autre chose que les en-têtes, n8n insérera les données à la mauvaise position.

---

## 6. Checklist avant test

```
[ ] Credentials Google configurées dans n8n (compte Google connecté)
[ ] Spreadsheet ID sélectionné (ou URL du sheet collée)
[ ] Onglet cible sélectionné (ex : "Feuille 1" ou "Commandes")
[ ] Ligne 1 du sheet = en-têtes exacts : ID commande | Client | Email | Montant | Devise | Statut
[ ] Operation = Append Row
[ ] Mode = Map Each Column Manually
[ ] Data Mode = Define Below
[ ] Toutes les expressions en doubles guillemets
[ ] Workflow sauvegardé avant test
[ ] Tester avec "Execute Node" sur un seul item avant activation
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
ID commande  →  {{ $json["order_id"] }}
Client       →  {{ $json["customer_name"] }}
Email        →  {{ $json["customer_email"] }}
Montant      →  {{ $json["total"] }}
Devise       →  {{ $json["currency"] }}
Statut       →  {{ $json["status"] }}

CHAMP JSON IGNORÉ
-----------------
items_count  →  (pas de colonne dans le sheet — à ajouter si besoin)
```
