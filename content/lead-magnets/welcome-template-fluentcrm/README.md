# Lead Magnet — Template Séquence Welcome FluentCRM

Système de capture complet produit via skill `lead-magnet-schoolswp` le 2026-04-16.

## Fichiers

- [01-pdf-content.md](01-pdf-content.md) — Contenu du PDF 1 page A4 (prêt à mettre en page)
- [02-landing-page.md](02-landing-page.md) — Copywriting + specs Fluent Forms de la landing
- [03-welcome-sequence.md](03-welcome-sequence.md) — 4 emails accueil + planning FluentCRM + KPIs
- [04-affiliate-sequence.md](04-affiliate-sequence.md) — Séquence affiliation FluentCRM Pro (5 emails) prise de relais post-welcome
- [05-manual-setup-fluentcrm.md](05-manual-setup-fluentcrm.md) — Guide UI pas à pas (templates + formulaire + page merci + 2 funnels)
- [06-templates-clipboard.md](06-templates-clipboard.md) — 9 templates prêts à coller (HTML ready) pour l'étape 1 du guide

## Cadrage

- **Ressource** : Template séquence welcome FluentCRM prête à copier
- **Promesse** : Configurer ta première automation FluentCRM qui tourne sans toi, en moins d'1 heure
- **Persona** : Freelance WordPress qui revend FluentCRM à ses clients
- **Stade funnel** : TOFU
- **Destination post-inscription** : Séquence produit affiliation FluentCRM (liste `affiliate_fluentcrm_sequence`)

## Funnel de bout en bout

```text
Landing → Fluent Forms → Redirect "merci" + email 1
→ Email 1 (J+0, livraison PDF + tag template_welcome_delivered)
→ Email 2 (J+1, story)
→ Email 3 (J+3, astuce + lien affilié FluentCRM Pro)
→ Email 4 (J+7, transition)
→ Move to list affiliate_fluentcrm_sequence
→ (prise de relais par la séquence affiliation FluentCRM)
```

## À faire côté exécution

1. Mise en page PDF (Canva ou Figma) à partir de `01-pdf-content.md`
2. Création de la landing Kadence + Fluent Forms selon `02-landing-page.md`
3. Création du funnel FluentCRM selon `03-welcome-sequence.md`
4. Création des 6 tags FluentCRM et des 2 listes (`lead_magnet_welcome_template`, `affiliate_fluentcrm_sequence`)
5. Construction de la séquence affiliation FluentCRM (skill `plugin-email-sequence`)
