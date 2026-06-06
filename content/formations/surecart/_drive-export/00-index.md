# Formation SureCart - Sources

> Matériel source brut pour la future formation schoolsWP sur **SureCart** (plugin e-commerce WordPress par Brainstorm Force / SureCrafted).
> Collecte : **2026-06-04**. Langue des sources : anglais (officiel SureCart). La formation sera produite en français.

## Ce qui a été collecté

| Dossier                         | Contenu                                                                              | Fichiers |
| ------------------------------- | ------------------------------------------------------------------------------------ | -------- |
| `_sources/youtube-transcripts/` | Transcripts des 29 tutos de la playlist officielle « SureCart Tutorials »            | 29       |
| `_sources/docs-kb/`             | Base de connaissances support complète (`surecart.com/docs/`)                        | 230      |
| `_sources/docs-developer/`      | Docs développeur conceptuelles (hooks/filters, PHP models, shop loops, API overview) | 36       |
| `_sources/features/`            | Page feature Affiliate Marketing                                                     | 1        |

**Total : 296 fichiers markdown.**

## Sources officielles

- **Playlist YouTube** : https://www.youtube.com/playlist?list=PLusgtFvcq_GR-G--Fs2mvSEeGJoKdNdkx (chaîne SureCart, 29 vidéos)
- **Base de connaissances** : https://surecart.com/docs/ (les 25 pages de la KB, soit ~230 articles)
- **Docs développeur** : https://developer.surecart.com/ (pages conceptuelles uniquement ; les ~300 endpoints API détaillés n'ont pas été inclus, à la demande)
- **Affiliation** (couverture renforcée) :
  - https://surecart.com/features/affiliate-marketing/
  - `docs/surecart-affiliate-platform`, `docs/affiliate-program`, `docs/managing-the-affiliates`, `docs/create-affiliate-coupon-codes`, `docs/override-commissions-for-specific-affiliates`, `docs/manually-assign-affiliates-past-orders`, `docs/partner-program-tiers`, `docs/agency-program`, `docs/integrate-affiliatewp-with-surecart`

## Notes de collecte

- Transcripts récupérés via DataForSEO (sous-titres YouTube anglais). 29/29 OK.
- Docs récupérées via Firecrawl (markdown, contenu principal). 230/230 + 37 OK.
- **6 fichiers** ont eu leurs blocs de code remplacés par un marqueur (faux positif du hook anti-injection sur du PHP/shell). Récupérer le code depuis le `source_url` du fichier si besoin :
  - `docs-developer/guides-variant-swatches.md`
  - `docs-kb/customer-dashboard-shortcodes.md`
  - `docs-kb/how-to-use-surecart-3-0-with-avada-builder.md`
  - `docs-kb/hide-invoice-button-on-customer-dashboard.md`
  - `docs-kb/licensing-setup-and-functionality.md`
  - `docs-kb/change-customer-dashboard-permalinks.md`
- Chaque fichier porte un frontmatter avec son `source_url`.

## Index des 29 vidéos (playlist « SureCart Tutorials »)

1. How To Sell A Subscription With Setup Fee (`iT5RDdeA9oY`)
2. How To Create Checkout Forms (`zNZ8J6T9oBI`)
3. How To Add Terms & Conditions To Checkout Forms (`FWAY35mn0sw`)
4. How To Add Custom Fields To Checkout Forms (`rr8jy9lnPdI`)
5. How To Setup Login Flows (`r7hfxQ3GW-U`)
6. How To Sell Free Products (`olnjNI_35Zc`)
7. How To Setup Traditional Ecommerce Stores (`7TtiuzNYcy4`)
8. Order Bumps For WordPress Ecommerce Stores (`9poLamtMtyA`)
9. Cart Abandonment Recovery (`JL1UxdwWXIM`)
10. How To Duplicate Checkout Forms (`5yA6_5BbBh4`)
11. Beautiful Single Product Checkout Pages (`vyzAhXOjGDI`)
12. How To Setup Instant Checkout (`v1y7nS-4iPM`)
13. Free Trials, Paid Trials, And Setup Fees (`5Y1FQq7sgOU`)
14. How To Customize Product Pages (`8niZ9cUhSEE`)
15. How To Customize The Customer Area (`oBg6cCCjcsE`)
16. How To Manage Subscriptions (`sLBCkqh-a-I`)
17. Setup & Customize Your Shopping Cart (`MS-u9yCzS4c`)
18. Setup & Customize Product Lists (`VU1TQmXWBJo`)
19. Guide To Order Fulfillment (`ereEmkrf90o`)
20. Guide To Shipping Methods & Rates (`Dq1vpjmR35k`)
21. How to Manage Notifications (`8L80mJxa4Uo`)
22. Product Variations & Inventory Management (`g_VvY164vXY`)
23. How To Setup An Affiliate Platform (`meBbIldcWNw`)
24. How To Make Upsell Funnels (`97gSH-KPFZU`)
25. How To Generate Invoices (`cQhtxcKztL4`)
26. Master Your Shop Page (`fZUz4O3oNk0`)
27. Ultimate Guide To Cart Abandonment Recovery (`M20cc26HkYg`)
28. Product Quick Add (`jo_XPCNH3Aw`)
29. Upgrade Product Pages With Images, Videos, Variations (`tBLj34o6D8U`)

## Prochaines étapes suggérées

- Construire le plan de formation (modules / leçons) à partir de ces sources : `formation-outline.md`.
- Stack de livraison probable : TutorLMS + FluentCart + FluentCRM (cf. template formation schoolsWP).
- Copie Drive : `06_Formations/SureCart` (bundles consolidés, prêts pour NotebookLM).
