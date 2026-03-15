# T8 — Maillage Interne

## Objectif

Optimiser la distribution du PageRank interne vers les pages piliers.

## Inputs

- T1_INVENTAIRE
- T7_OPTIM (articles prioritaires)

## Output

- Onglet `T8_MAILLAGE`
- Plan de liens internes à ajouter

## Règles de maillage

1. Chaque article satellite pointe vers son pilier
2. Chaque pilier pointe vers ses satellites (top 5)
3. Texte d'ancre : keyword exact ou variante proche
4. Position : dans le corps du texte, pas footer
5. Max 5 nouveaux liens par article (pour éviter over-optimization)

## Output format

| Article source | Article cible | Texte ancre | Paragraphe | Priorité |
|----------------|--------------|-------------|-----------|----------|
| /fluentcrm-avis | /crm-wordpress | CRM WordPress | 2e section | Haute |

## KPIs

- >= 30 liens internes planés
- 100% des piliers avec >= 5 satellites pointants
