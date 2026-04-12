# Garde-fou IA — schoolsWP

Ce projet compte ~164 skills, 72 skills workspace, 4 rules scopees, 12 docs strategiques, 6 commands et 4 subagents.

Nettoyage du 2026-04-03 : 301 → 164 skills (-137, -45%).
- Phase 1 : doublons directs + package imports (gws/recipe/persona) = -97
- Phase 2 : skills generiques dupliquees du workspace + securite/dev/AI/media = -40
- ~40 skills restent bloquees par des locks Windows — a relancer apres redemarrage

Il est deja complet. Le risque n'est plus le manque — c'est l'accumulation.

---

## Regle principale

**Ne rien ajouter sans justification d'usage reel.**

Avant de creer une nouvelle skill, verifier :

1. Est-ce que le besoin revient au moins 3 fois ?
2. Est-ce qu'une skill existante couvre deja 70%+ du besoin ?
3. Est-ce que la nouvelle skill simplifie vraiment le travail ?
4. Est-ce qu'elle reduit la repetition ou ameliore la qualite de sortie ?
5. Est-ce qu'elle sera utilisee dans les 2 prochaines semaines ?

Si la reponse a une seule question est "non" : ne pas creer.

---

## Regle de nommage

- kebab-case uniquement
- nom court et descriptif
- pas de prefixe `schoolswp-` sauf si la skill est specifique au projet et risque un conflit de nom

---

## Regle de maintenance

- Supprimer les skills inutilisees depuis plus de 30 jours
- Fusionner les skills qui se recoupent a plus de 70%
- Garder les descriptions courtes et specifiques
- Eviter les skills trop abstraites ("generic-helper", "smart-optimizer")
- Privilegier les skills liees a un vrai workflow metier mesurable

---

## Regle avant modification du CLAUDE.md

Le CLAUDE.md est la source de verite technique du projet.

Avant de le modifier :

1. Verifier que l'info n'existe pas deja dans une rule scopee (.claude/rules/)
2. Verifier que l'info n'existe pas deja dans un doc (.claude/docs/)
3. Ne pas dupliquer — renvoyer vers la source existante
4. Ne pas ajouter de principes "philosophiques" — le style est dans branding.md et schoolswp-style-guide.md

---

## Regle avant ajout de subagent

Les 4 agents actuels (content-studio, crm-automation, seo-geo, social-community) couvrent les besoins.

Avant d'en ajouter un :

1. Verifier qu'aucun agent existant ne peut absorber le role
2. Verifier que le besoin justifie un agent autonome (pas juste un skill ou un command)
3. Documenter le role, le model et les limites dans le CLAUDE.md

---

## Test de qualite d'une skill

Une bonne skill doit :

- Etre activable sur un cas reel sans re-prompting
- Produire une structure de sortie claire et previsible
- Reduire le temps de production par rapport a un prompt libre
- Etre comprehensible par quelqu'un qui ne l'a pas creee

---

## Audit periodique recommande

Frequence : 1 fois par mois (dernier audit : jamais — a planifier)

Methode :

1. Lister toutes les skills
2. Identifier celles utilisees dans le mois
3. Identifier les doublons (>70% de recouvrement)
4. Supprimer ou fusionner
5. Mettre a jour l'INDEX.md

---

## Seuils d'alerte

| Indicateur | Seuil | Action |
|---|---|---|
| Nombre total de skills projet | > 150 | Audit obligatoire |
| Skills non utilisees depuis 60j | > 30% | Nettoyage |
| Skills sans description claire | > 10 | Corriger ou supprimer |
| CLAUDE.md > 400 lignes | oui | Deplacer vers rules/docs |

Le setup est a 164 skills (2026-04-03). Objectif cible : 80-100 apres fusion des clusters et suppression des locks restants.

Prochaine action : apres redemarrage PC, relancer la suppression des ~40 skills generiques bloquees par les locks Windows, puis fusionner les clusters (authority 13→5, engines 8→2, affiliation 5→2, money pages 5→2).
