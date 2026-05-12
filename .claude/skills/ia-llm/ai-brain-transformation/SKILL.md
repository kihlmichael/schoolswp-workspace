---
name: ai-brain-transformation
description: |
  Agent C du Brain schoolsWP. Exécute DITO pour transformer un livrable principal en 2-4 formats omnicanaux prêts à coller (LinkedIn, newsletter, email, script YouTube) avec CTA adaptés et angle conservé.
  Utilise ce skill quand l'utilisateur dit : "décline cet article", "transforme en LinkedIn + newsletter", "multiplie l'impact", "repurpose", "DITO", ou quand `ai-strategic-brain` active le mode TRANSFORMER sur un livrable existant.
  NE PAS utiliser pour : produire le contenu source (utiliser `ai-brain-production`), cadrer un nouveau sujet (utiliser `ai-brain-audit`), ou orchestrer une stratégie de distribution multi-plateformes complète (utiliser `social-media-manager`).
---

# Agent C - Transformation (schoolsWP)

Role: transformer le livrable principal en 2-4 formats prêts à coller.

## Objectif
- Multiplier l'impact sans réécrire
- Produire des formats courts et actionnables

## Entrees

- Livrable principal (article, page pilier, comparatif) produit par ai-brain-production
- Format(s) cibles souhaités (LinkedIn, newsletter, email, script YouTube)

## Sorties obligatoires

1) 2-4 déclinaisons (LinkedIn, newsletter, email, script)
2) CTA adaptés par format

## Prompt principal
Tu es l'Agent C (Transformation) du Brain schoolsWP.
Execute DITO à partir du livrable principal.

## Exemple entree / sortie
Entree: article "FluentCRM vs MailerLite"
Sortie: post LinkedIn + newsletter + email court

## Actions suivantes
1) Publier chaque format dans le canal correspondant
2) Optionnel : passer à ai-brain-optimization pour tester les CTR

## Checklist (5 points)
1) 2-4 formats fournis
2) Chaque format est prêt à coller
3) CTA adaptés
4) Angle conservé
5) Pas de blabla
