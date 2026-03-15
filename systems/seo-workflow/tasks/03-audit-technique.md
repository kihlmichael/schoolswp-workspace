# T3 — Audit Technique

## Objectif

Détecter les issues techniques bloquantes pour le crawl et l'indexation.

## Inputs

- T1_INVENTAIRE (liste URLs)
- Screaming Frog ou Firecrawl

## Output

- Onglet `T3_AUDIT_TECH`
- Issues classées par sévérité

## Issues à détecter

| Issue | Sévérité |
|-------|----------|
| Noindex involontaire | Critical |
| H1 manquant ou dupliqué | High |
| Title dupliqué | High |
| Page lente (> 3s LCP) | High |
| Lien brisé (404 interne) | Medium |
| Images sans alt | Low |
| Canonical manquant | Medium |

## KPIs

- 100% des URLs T1 auditées
- Issues critical : 0 restante après correction
