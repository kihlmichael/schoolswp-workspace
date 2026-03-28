# Workspace Hygiene Report — 2026-03-25

## Etat general

1 probleme detecte — categorie : dossiers dupliques.

## Patch files et scripts residuels

Aucun detecte (hors scope de cet audit cible).

## Dossiers dupliques

| Dossier A | Dossier B | Statut | Action proposee |
|-----------|-----------|--------|-----------------|
| `.agent/` (93 fichiers) | `.agents/` (93 fichiers) | **identiques** (`diff -rq` = 0 difference) | garder `.agents/`, trash `.agent/` |

### Analyse detaillee

**Comparaison :**

- `.agent/skills/` : 93 fichiers SKILL.md (gws-*, persona-*, recipe-*)
- `.agents/skills/` : 93 fichiers SKILL.md (gws-*, persona-*, recipe-*)
- `diff -rq` entre les deux : aucune difference

**Source canonique : `.agents/`** (pluriel) — raisons :

1. **Reference dans CLAUDE.md du projet** : `.agents/skills/` est explicitement documente comme "Source library — 42 skills, descriptions FR synchronisees" dans la table Skills Registry
2. **Reference dans CLAUDE.md du workspace** : `.agents/skills/` est cite comme "Source library — 42 skills EN d'origine, descriptions synchronisees en FR" avec instruction "editer dans `.claude/skills/`, puis repercuter la description dans `.agents/skills/` via le script de sync"
3. **`.agent/` (singulier) n'est reference nulle part** : aucune mention dans CLAUDE.md, aucun script, aucun workflow

**Conclusion :** `.agent/` est un doublon exact de `.agents/`. Il a probablement ete cree par erreur (copie accidentelle ou renommage incomplet).

## Fichiers orphelins

Aucun detecte (hors scope de cet audit cible).

## Composants inactifs

Aucun detecte (hors scope de cet audit cible).

## Plan d'action resume

1. Trash `.agent/` (93 fichiers, doublon exact de `.agents/`)
2. Conserver `.agents/` tel quel — source de verite documentee

Commande a executer apres validation :

```bash
trash "d:/VS Code/CLAUDE CODE/projects/schoolswp/.agent/"
```

**Attente validation avant execution.**
