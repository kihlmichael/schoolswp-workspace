# T9 — E-E-A-T Signals

## Objectif

Renforcer les signaux E-E-A-T sur les 20 articles les plus importants.

## Inputs

- T7_OPTIM (articles prioritaires)
- Skill : `eeat-template-builder`

## Output

- Onglet `T9_EEAT`
- Blocs E-E-A-T générés + scores

## Process

1. Sélectionner top 20 articles (position + business value)
2. Pour chaque article : générer les 3 blocs via `eeat-template-builder`
3. Score E-E-A-T /6 avant et après
4. Insérer les blocs dans WordPress

## Blocs prioritaires

1. **Disclosure affiliation** : tous les articles avec liens affiliés
2. **Bio auteur** : Michael KIHL + crédentials WordPress
3. **Date de mise à jour** : visible en haut de l'article

## KPIs

- 20 articles avec score E-E-A-T >= 4/6
- 100% articles affiliation avec disclosure
