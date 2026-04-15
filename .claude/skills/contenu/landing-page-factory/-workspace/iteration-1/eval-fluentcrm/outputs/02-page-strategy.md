# Page Strategy — FluentCRM

## Analyse du probleme
- **Quel probleme resout FluentCRM ?** Les entrepreneurs WordPress paient des abonnements SaaS (Mailchimp, ActiveCampaign, Kit) qui augmentent avec leur liste de contacts. Ils n'ont pas le controle de leurs donnees, dependent d'un service tiers, et paient des "taxes de croissance" mensuelles.
- **Pour qui exactement ?**
  - Freelances WordPress qui gerent des sites clients
  - Createurs de cours en ligne (LMS) qui veulent automatiser le suivi apprenant
  - Proprietaires de boutiques WooCommerce qui veulent relancer les paniers abandonnes
  - Blogueurs/solopreneurs qui construisent leur liste email
- **Alternative actuelle** : Mailchimp (49 USD/mois pour 1000 contacts), ActiveCampaign (prix qui grimpe), Kit (ex-ConvertKit). Problemes : cout croissant, donnees chez un tiers, integrations WordPress limitees ou payantes.

## Cartographie des claims

| Claim | Prouvable ? | Source de preuve |
|-------|-------------|-----------------|
| "70 000+ entreprises" | Oui | Affiche sur la homepage |
| "180+ avis 5 etoiles" | Oui | WordPress.org verifiable |
| "Note 4.8/5" | Oui | WordPress.org verifiable |
| "85% d'economies" | Partiellement | Comparateur de prix sur le site, depend du volume |
| "45+ integrations gratuites" | Oui | Page integrations verifiable |
| "2x croissance contacts en 1 an" (WP Fusion) | Oui | Case study publiee |
| "90% economie annuelle" (WP Fusion) | Oui | Case study publiee |
| "$1.75 pour 15K envois" | Oui | Tarif Amazon SES public |
| "GDPR compliant / 100% self-hosted" | Oui | Architecture technique verifiable |
| "N'affecte pas les performances WP" | Partiellement | Claim technique, tables custom + VueJS SPA |

## Angles proposes

### Angle 1 : "Arrete de payer Mailchimp" (Economie)
- **Hook** : Tu paies combien par mois pour envoyer des emails ?
- **Cible** : Solopreneur/blogueur WordPress avec 1000-10000 contacts, qui paie 30-100 EUR/mois a Mailchimp ou Kit
- **Emotion dominante** : Frustration (facture mensuelle qui grossit)
- **CTA principal** : Telecharger FluentCRM gratuitement
- **Mecanisme de preuve** : Comparateur de prix reel (FluentCRM vs Mailchimp/ActiveCampaign), temoignage @patricia70 et @zephyrmike, chiffres WP Fusion

### Angle 2 : "Tes donnees, ton serveur" (Souverainete / GDPR)
- **Hook** : Tes contacts sont chez Mailchimp. Pas chez toi.
- **Cible** : Freelance WordPress soucieux de la conformite RGPD, gerant des sites clients EU
- **Emotion dominante** : Inquietude (dependance a un tiers, risque RGPD)
- **CTA principal** : Reprendre le controle de tes donnees
- **Mecanisme de preuve** : Architecture self-hosted verifiable, temoignages @patricia70 et @lissie45, zero donnees externalisees

### Angle 3 : "WooCommerce + Email = Revenue Machine" (Automatisation e-commerce)
- **Hook** : 60% de tes paniers abandonnes repartent avec ton argent.
- **Cible** : Proprietaire de boutique WooCommerce avec 500+ commandes/mois
- **Emotion dominante** : Perte (argent qui s'echappe a chaque panier abandonne)
- **CTA principal** : Activer la relance de paniers abandonnes
- **Mecanisme de preuve** : Feature abandon de panier, integration WooCommerce native, temoignage @martijnreintjes (30K abonnes, newsletters hebdo via SES), workflows d'upsell/cross-sell
