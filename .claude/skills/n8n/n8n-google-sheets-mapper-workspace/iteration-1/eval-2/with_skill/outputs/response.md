# Configuration du nœud Google Sheets — Mapping

---

## 1. Diagnostic rapide

**Ce que je comprends :**

- Le nœud précédent produit 6 champs JSON plats (pas de structure imbriquée)
- Le Google Sheet a 6 colonnes, dont une (`Statut`) absente du JSON
- L'expression `{{ $json.prenom }}` est syntaxiquement valide en n8n, mais le problème vient probablement du **Mapping Column Mode** mal configuré — si le mode est `Auto-Map Input Data`, n8n tente de faire correspondre les noms de champs JSON aux colonnes automatiquement, ce qui échoue ici car les noms sont différents (ex: `prenom` vs `Prénom`)

**Ce qui est correct :**

- La structure JSON est propre et plate — mapping simple, pas d'imbrication à gérer
- La date est déjà au format `YYYY-MM-DD` — compatible Google Sheets

**Ce qui pose problème :**

- Mode de mapping probablement sur `Auto-Map` alors qu'il faut `Map Each Column Manually`
- Colonne `Statut` absente du JSON → pas de valeur disponible, à traiter manuellement
- Le téléphone `"0698765432"` risque d'être interprété comme un nombre et perdre le zéro initial

---

## 2. Réglages du nœud à utiliser

| Paramètre               | Valeur                                                                            |
| ----------------------- | --------------------------------------------------------------------------------- |
| **Resource**            | `Sheet Within Document`                                                           |
| **Operation**           | `Append Row`                                                                      |
| **Document**            | [ton Google Sheet — à sélectionner dans la liste]                                 |
| **Sheet**               | [nom de l'onglet — à sélectionner]                                                |
| **Mapping Column Mode** | `Map Each Column Manually`                                                        |
| **Data Mode**           | `Define Below` (obligatoire ici, les noms JSON ne correspondent pas aux colonnes) |

---

## 3. Mapping colonne par colonne

```
Prénom              → {{ $json["prenom"] }}
Email               → {{ $json["email"] }}
Téléphone           → {{ $json["telephone"] }}
Activité souhaitée  → {{ $json["activite"] }}
Date activité       → {{ $json["date"] }}
Statut              → (valeur statique ou laisser vide — absent du JSON)
```

---

## 4. Erreurs ou incohérences détectées

- **Prénom** : le champ JSON est `prenom` (sans accent), la colonne est `Prénom` (avec accent majuscule). En mode `Auto-Map`, n8n ne fait pas la correspondance → la cellule reste vide. Correction : passer en `Map Each Column Manually` et utiliser `{{ $json["prenom"] }}`.

- **Activité souhaitée** : le champ JSON est `activite` (sans accent, sans espace), la colonne est `Activité souhaitée`. Même problème qu'au-dessus. Correction : `{{ $json["activite"] }}` dans la colonne `Activité souhaitée`.

- **Date activité** : le champ JSON est `date`, la colonne est `Date activité`. Noms différents → pas de correspondance automatique. Correction : `{{ $json["date"] }}` dans la colonne `Date activité`.

- **Statut** : cette colonne n'existe pas dans le JSON. Elle sera ignorée ou vide. Si tu veux une valeur par défaut (ex: `"Nouveau"`), saisis-la en statique directement dans le champ de mapping.

- **Téléphone** : la valeur `"0698765432"` commence par un zéro. Si Google Sheets interprète le champ comme un nombre, le zéro disparaît → `698765432`. Correction recommandée : forcer le formatage de la colonne en "Texte brut" dans Google Sheets, ou préfixer avec une apostrophe via une expression : `{{ "'" + $json["telephone"] }}`.

---

## 5. Erreurs fréquentes à éviter

- **Laisser le mode sur `Auto-Map Input Data`** alors que les noms JSON diffèrent des colonnes → toutes les cellules restent vides sans message d'erreur
- **Utiliser `$json.prenom` plutôt que `$json["prenom"]`** : les deux fonctionnent pour des noms simples, mais la notation avec crochets et guillemets est plus sûre (obligatoire si le nom contient des espaces, accents ou caractères spéciaux)
- **Ne pas vérifier la ligne 1 du sheet** : si les en-têtes ne sont pas exactement en ligne 1, le nœud ne détecte pas les colonnes
- **Ne pas tester sur un vrai output** : utiliser "Execute previous nodes" avant de tester le nœud Google Sheets pour avoir des données réelles

---

## 6. Checklist avant test

```
[ ] Le Google Sheet est bien connecté (credentials n8n configurées)
[ ] L'onglet cible est bien sélectionné (pas le mauvais onglet)
[ ] La ligne 1 du sheet contient les en-têtes exacts : Prénom | Email | Téléphone | Activité souhaitée | Date activité | Statut
[ ] Mapping Column Mode = "Map Each Column Manually"
[ ] Data Mode = "Define Below"
[ ] Chaque expression est testée sur un vrai nœud précédent (cliquer "Execute previous nodes" d'abord)
[ ] La colonne Téléphone est formatée en "Texte brut" dans Google Sheets
[ ] La colonne Statut a une valeur statique définie (ou est laissée vide intentionnellement)
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
Prénom             → {{ $json["prenom"] }}
Email              → {{ $json["email"] }}
Téléphone          → {{ $json["telephone"] }}
Activité souhaitée → {{ $json["activite"] }}
Date activité      → {{ $json["date"] }}
Statut             → Nouveau   (valeur statique — à adapter selon ton besoin)
```

> Point clé : le problème principal n'est pas l'expression `{{ $json.prenom }}` elle-même — elle est correcte. Le problème est le mode de mapping. Passe en `Map Each Column Manually` + `Define Below`, et renseigne chaque colonne manuellement comme indiqué ci-dessus.
