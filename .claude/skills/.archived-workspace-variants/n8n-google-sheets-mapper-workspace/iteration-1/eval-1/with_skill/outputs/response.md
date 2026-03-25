# Configuration nœud Google Sheets — Mapping Eva Martin

---

## 1. Diagnostic rapide

- **JSON d'entrée** : 5 champs plats (pas d'imbrication), noms avec accents et underscores
- **Colonnes du sheet** : identiques aux clés JSON — correspondance exacte sur les 5 champs
- **Mode recommandé** : les noms JSON et colonnes étant identiques, `Auto-Map Input Data` peut fonctionner, mais `Map Each Column Manually` reste préférable pour garantir l'ordre et éviter les surprises
- **Point de vigilance** : `Téléphone` commence par `0` → risque de perte du zéro si interprété comme nombre par Google Sheets

---

## 2. Réglages du nœud à utiliser

| Paramètre               | Valeur                                            |
| ----------------------- | ------------------------------------------------- |
| **Resource**            | `Sheet Within Document`                           |
| **Operation**           | `Append Row`                                      |
| **Document**            | [ton Google Sheet — à sélectionner via le picker] |
| **Sheet**               | [nom de l'onglet — ex: `Feuille 1`]               |
| **Mapping Column Mode** | `Map Each Column Manually`                        |
| **Data Mode**           | `Define Below`                                    |

---

## 3. Mapping colonne par colonne

```
Nom                → {{ $json["Nom"] }}
Email              → {{ $json["Email"] }}
Téléphone          → {{ $json["Téléphone"] }}
Activité_souhaitée → {{ $json["Activité_souhaitée"] }}
Date_activité      → {{ $json["Date_activité"] }}
```

---

## 4. Erreurs ou incohérences détectées

- **Téléphone** : la valeur `"0612345678"` est une chaîne dans le JSON, mais Google Sheets peut la convertir en nombre et supprimer le `0` initial. Voir section 5 pour la correction.
- **Date_activité** : la valeur `"2025-01-25"` est au format ISO 8601 (YYYY-MM-DD) — format bien accepté par Google Sheets. Pas de conversion nécessaire.
- Aucune autre incohérence détectée : les 5 clés JSON correspondent exactement aux 5 en-têtes du sheet (casse, accents et underscores inclus).

---

## 5. Erreurs fréquentes à éviter

- **Téléphone stocké comme nombre** : Google Sheets peut interpréter `0612345678` comme un entier et supprimer le `0` initial. Pour forcer le format texte, deux options :
  - Préformater la colonne en "Texte brut" dans Google Sheets avant d'écrire
  - Ou préfixer avec une apostrophe dans l'expression : `{{ "'" + $json["Téléphone"] }}`
- **Mode Auto-Map avec des champs à accents ou underscores** : même si les noms semblent identiques, `Auto-Map` peut rater les correspondances sur des caractères spéciaux. Toujours préférer `Map Each Column Manually` dans ce cas.
- **Guillemets simples dans les expressions** : utiliser `$json["Nom"]` et non `$json['Nom']` — les guillemets simples provoquent une erreur d'exécution dans n8n.
- **Colonne absente en ligne 1** : si une colonne n'est pas en ligne 1, la valeur est ignorée silencieusement — vérifier que les en-têtes sont bien en ligne 1.

---

## 6. Checklist avant test

```
[ ] Le Google Sheet est bien connecté (credentials Google configurées dans n8n)
[ ] L'onglet cible est bien sélectionné (pas le mauvais onglet)
[ ] La ligne 1 du sheet contient exactement : Nom | Email | Téléphone | Activité_souhaitée | Date_activité
[ ] Mapping Column Mode = "Map Each Column Manually"
[ ] Chaque expression utilise des guillemets doubles
[ ] La colonne Téléphone est formatée en "Texte brut" dans le sheet (pour conserver le 0)
[ ] Le nœud précédent a bien été exécuté et ses données sont visibles dans l'onglet Output
[ ] Le workflow est sauvegardé avant le test
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
Nom                → {{ $json["Nom"] }}
Email              → {{ $json["Email"] }}
Téléphone          → {{ $json["Téléphone"] }}
Activité_souhaitée → {{ $json["Activité_souhaitée"] }}
Date_activité      → {{ $json["Date_activité"] }}
```
