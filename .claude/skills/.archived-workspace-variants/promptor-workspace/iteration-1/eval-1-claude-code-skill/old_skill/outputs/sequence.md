# Eval 1 — Génération SKILL.md Claude Code (old_skill v2.0)

## Calibrage pour Claude Code

| Caractéristique | Application |
|-----------------|-------------|
| Format skill YAML + Markdown | En-tête YAML avec `name`, `description`, `allowed-tools` |
| `allowed-tools` explicite | `Read`, `Grep`, `Edit` — liste minimale suffisante |
| Instructions en étapes numérotées | 6 étapes décomposées — Claude Code est littéral |
| Format de sortie défini | Tableau + section insertions + Top 3 prioritaires |
| Convention d'appel | Chemins fournis dans le message utilisateur, extraits par le skill |
| Trigger keywords riches | Description YAML avec tous les déclencheurs naturels |

---

## Itération 1 — 22/25

Points faibles :
- Convention d'appel non définie (comment l'utilisateur fournit-il les chemins ?)
- Comportement post-rapport non précisé (modifier ou demander confirmation ?)
- Seuils "sous-représenté" non calibrés

Auto-réponses :
1. L'utilisateur fournit les chemins dans son message conversationnel — le skill les extrait
2. Le skill produit d'abord le rapport, puis demande confirmation avant toute modification via `Edit`

---

## Prompt final — 25/25

```markdown
## Objectif

Crée un skill Claude Code complet et fonctionnel. Ce skill analyse un article Markdown de blog
WordPress, compare son contenu à une liste de mots-clés fournie dans un fichier CSV, identifie
les mots-clés absents ou sous-représentés, et propose des insertions naturelles et contextuelles.

## Contexte technique

- Environnement : Claude Code (CLI Anthropic) — skill activé via fichier `.md` avec en-tête YAML
- Format des articles : fichiers `.md` (Markdown standard, articles WordPress)
- Format des mots-clés : fichier `.csv` avec colonne `keyword`, `Keyword`, `KEYWORD`, ou `kw`
- Convention d'appel : l'utilisateur mentionne les deux chemins dans son message. Ex :
  "analyse les mots-clés de `content/articles/mon-article.md` avec `data/keywords.csv`"

## Spécifications du skill (6 étapes)

1. **Extraire les chemins** : Identifier article Markdown + fichier CSV dans le message.
   Si l'un manque, demander avant de continuer.

2. **Lire le CSV** : Charger les mots-clés. Chercher la colonne dans l'ordre :
   `keyword`, `Keyword`, `KEYWORD`, `kw`. Ignorer doublons et lignes vides.

3. **Lire l'article** : Charger le contenu complet. Compter les mots pour calibrer les seuils.

4. **Analyse de présence** (insensible à la casse, gestion pluriels simples) :
   - **Absent** : aucune occurrence
   - **Sous-représenté** : 1 occurrence pour article > 800 mots, ou 2 pour > 2000 mots
   - **Présent** : seuils atteints

5. **Proposer des insertions** : Pour chaque absent/sous-représenté :
   1-3 suggestions avec : titre de section, phrase de localisation, formulation complète,
   niveau de priorité (Haute/Moyenne/Basse)

6. **Rapport et confirmation** : Résumé + tableau synthétique + insertions détaillées +
   Top 3 prioritaires + demande de confirmation avant toute modification du fichier.

## Format du skill à produire

En-tête YAML :
```yaml
---
name: keyword-gap-analyzer
description: |
  Analyse un article Markdown WordPress et détecte les mots-clés manquants
  par rapport à une liste CSV. Propose des insertions naturelles et contextuelles,
  puis applique les modifications après confirmation.
  Déclencher quand l'utilisateur dit : "analyse les mots-clés de [fichier] avec [csv]",
  "mots-clés manquants", "keyword gap", "optimise les mots-clés de cet article",
  "quels mots-clés manquent". Toujours demander les deux chemins si non fournis.
allowed-tools:
  - Read
  - Grep
  - Edit
---
```

Suivi des 6 étapes formulées comme instructions directes pour Claude Code.

## Tests de validation

- Article 1000 mots + CSV 20 mots-clés (7 absents) : identifie les 7 absents sans faux positifs
- Propose au moins une suggestion par mot-clé absent
- Ne modifie pas le fichier avant confirmation explicite
- Si chemins absents : demande les deux avant d'agir
```

---

## Grille d'évaluation finale

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 5/5 | 6 étapes atomiques, comportement post-rapport défini |
| Spécificité | 5/5 | Seuils calibrés, convention d'appel précise, colonnes CSV nommées |
| Structure | 5/5 | YAML frontmatter + instructions directes + tests validation |
| Contexte | 5/5 | Contexte WordPress Markdown, format CSV flexible |
| Actionnable | 5/5 | Tests de validation inclus, confirmation avant Edit |
| **TOTAL** | **25/25** | 2 itérations |
