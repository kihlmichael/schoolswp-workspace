# Hreflang Multilang Auditor

## Rôle

Audit des balises hreflang pour les sites multilingues (fr/en/es).

## 4 étapes d'audit

### 1. Inventaire hreflang
- Lister toutes les URLs avec balises hreflang
- Vérifier présence dans `<head>` et/ou sitemap XML

### 2. Règles de réciprocité
- Page FR doit pointer vers EN et vice versa
- x-default obligatoire sur au moins une langue
- Pas de self-referencing manquant

### 3. Détection des erreurs
- URLs hreflang inexistantes (404)
- Hreflang non réciproque
- Langue incorrecte (fr-FR vs fr)
- Hreflang sur pages noindex

### 4. Table de décision

| Situation | Action |
|-----------|--------|
| Page FR sans hreflang EN | Ajouter ou marquer monolangue |
| Hreflang non réciproque | Corriger la page cible |
| URL hreflang = 404 | Mettre à jour ou supprimer |
| x-default manquant | Ajouter sur page principale |
| Hreflang sur noindex | Retirer hreflang ou retirer noindex |

## Note schoolsWP

schoolswp.com est actuellement monolingue (FR). Ce skill s'applique si expansion EN/ES est envisagée.
