# Lead Magnet : Template Séquence Welcome FluentCRM

Système de capture complet produit via skill `lead-magnet-schoolswp` le 2026-04-16.

## Fichiers

- [01-pdf-content.md](01-pdf-content.md) - Contenu du PDF 1 page A4 (prêt à mettre en page)
- [02-landing-page.md](02-landing-page.md) - Copywriting + specs Fluent Forms de la landing
- [03-welcome-sequence.md](03-welcome-sequence.md) - 4 emails accueil + planning FluentCRM + KPIs
- [04-affiliate-sequence.md](04-affiliate-sequence.md) - Séquence affiliation FluentCRM Pro (5 emails) prise de relais post-welcome
- [05-manual-setup-fluentcrm.md](05-manual-setup-fluentcrm.md) - Guide UI pas à pas (templates + formulaire + page merci + 2 funnels)
- [06-templates-clipboard.md](06-templates-clipboard.md) - 9 templates prêts à coller (HTML ready) pour l'étape 1 du guide

## Cadrage

- **Ressource** : Template séquence welcome FluentCRM prête à copier
- **Promesse** : Configurer ta première automation FluentCRM qui tourne sans toi, en moins d'1 heure
- **Persona** : Freelance WordPress qui revend FluentCRM à ses clients
- **Stade funnel** : TOFU
- **Destination post-inscription** : Séquence produit affiliation FluentCRM (bascule par tag `sequence_fluentcrm_onboarding`, id 688)

## Funnel de bout en bout

```text
Landing → Fluent Forms (tag freebie_welcome_template_fluentcrm 746 + liste FREEBIES 26) → Redirect "merci" + email 1
→ Email 1 (J+0, livraison PDF + tag freebie_welcome_template_delivered 747)
→ Email 2 (J+1, story + tag 748)
→ Email 3 (J+3, astuce + lien affilié FluentCRM Pro + tag 749)
→ Email 4 (J+7, transition + tag freebie_welcome_template_completed 750)
→ Apply tag sequence_fluentcrm_onboarding (688)
→ (prise de relais par la séquence affiliation FluentCRM, Funnel 2)
```

## À faire côté exécution

1. PDF final prêt : `Template-Welcome-FluentCRM-schoolsWP.pdf` (à uploader dans la médiathèque WP)
2. Création de la landing Kadence + Fluent Forms selon `02-landing-page.md`
3. Création du funnel FluentCRM selon `03-welcome-sequence.md`
4. Tags : `freebie_welcome_template_*` (746-750) déjà créés en prod ; réutilisés `sequence_fluentcrm_onboarding` (688) + `plugin_fluentcrm` (606) ; liste `FREEBIES schoolsWP` (26)
5. Construction de la séquence affiliation FluentCRM (skill `plugin-email-sequence`)
