# Lecon 5.8 - Cas pratique : funnel complet produit physique + upsell digital

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 5 - One-Click Upsells et Downsells
- **Duree cible** : 12 min (~1700 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Construire un funnel complet de A a Z en live : produit physique + bump + upsell digital + downsell digital. Calculer l'AOV potentiel. Tester le parcours.

---

## Script narration

**[INTRO - face camera]**

On a vu la theorie, les configurations, les segments, les Dynamic Offers. Dans cette lecon, on assemble tout dans un cas pratique concret. Un funnel complet, construit en live, du premier clic a la commande finale.

Le scenario : tu vends des produits physiques (t-shirts) et tu veux augmenter ta valeur par commande avec des produits digitaux (guides, wallpapers). C'est une combinaison classique e-commerce qui fonctionne extremement bien.

---

**[SECTION 1 - Le funnel qu'on va construire]**

**[ECRAN - schema du funnel complet avec prix]**

Voici la structure :

- **Produit principal** : t-shirt schoolsWP a 29 euros
- **Order bump** : lot de 3 stickers a 7 euros
- **Upsell** : guide de style PDF "Comment porter le look dev" a 17 euros
- **Downsell** : wallpaper digital HD a 5 euros
- **Thank You Page** : confirmation + acces aux produits digitaux

L'AOV de base est de 29 euros. Si le client accepte tout, il depense 58 euros. C'est un doublement de la valeur de commande, +100%, sur un meme visiteur.

Allons-y.

---

**[SECTION 2 - Creer les produits WooCommerce]**

**[ECRAN - WooCommerce → Products → Add New]**

Premiere etape : creer les 4 produits dans WooCommerce si ce n'est pas deja fait.

**Produit 1 : T-shirt schoolsWP.**
Type : Simple product. Prix : 29 euros. Categorie : Merch. Ajoute les images, les tailles, la description. Publie.

**Produit 2 : Lot de 3 stickers.**
Type : Simple product. Prix : 7 euros. Categorie : Merch. Ce sera l'order bump.

**Produit 3 : Guide de style PDF.**
Type : Simple product (ou Virtual + Downloadable). Prix catalogue : 27 euros (on le proposera a 17 euros en upsell). Upload le fichier PDF dans la section "Downloadable files". Categorie : Digital.

**Produit 4 : Wallpaper digital HD.**
Type : Simple product (Virtual + Downloadable). Prix catalogue : 9 euros (on le proposera a 5 euros en downsell). Upload les fichiers.

**[ECRAN - les 4 produits visibles dans la liste WooCommerce]**

Les 4 produits sont en place. Passons au funnel.

---

**[SECTION 3 - Creer le flow CartFlows]**

**[ECRAN - CartFlows → Flows → Add New]**

Va dans CartFlows, Flows, Add New. Nomme-le "Funnel T-shirt + Upsell Digital".

**Step 1 : Landing Page.**
Add Step → Landing. Choisis un template epure ou pars d'une page vierge. Cette page presente le t-shirt avec un design Kadence : hero image, benefices, CTA "Commander maintenant" qui mene au checkout.

**[ECRAN - page de vente t-shirt dans Gutenberg]**

**Step 2 : Checkout.**
Add Step → Checkout. Configure :
- Produit principal : T-shirt schoolsWP (29 euros)
- Order Bump : active, connecte le lot de stickers (7 euros)
- Design Gutenberg + Kadence : formulaire epure, recap commande visible, bump bien positionne

**[ECRAN - checkout avec bump visible]**

Rappel du module precedent : le bump s'affiche comme une case a cocher juste avant le bouton "Payer". Le texte du bump doit etre court et percutant : "Ajoute le lot de 3 stickers exclusifs pour seulement 7 euros".

**Step 3 : Upsell.**
Add Step → Upsell (Offer). Configure :
- Produit : Guide de style PDF
- Offer Price : 17 euros (au lieu de 27 euros catalogue)

**[ECRAN - parametres upsell avec prix d'offre]**

---

**[SECTION 4 - Designer la page upsell]**

**[ECRAN - editeur Gutenberg de la page upsell]**

La page upsell du guide de style. Construisons-la element par element :

**Titre** (Kadence Advanced Heading, H2, centre) :
"Tu as choisi le look. Maintenant, maitrise le style."

**Sous-titre** (Kadence Advanced Text) :
"Le guide complet pour combiner ton t-shirt dev avec n'importe quelle tenue. 47 pages de conseils, photos et inspirations."

**Image** (bloc Image) :
Mockup du guide PDF, ouvert, avec quelques pages visibles.

**Benefices** (Kadence Icon List, 4 items) :
- 47 pages de conseils style illustres
- 15 tenues completes photographiees
- Combinaisons selon les saisons
- Bonus : checklist des pieces intemporelles

**Prix** (Kadence Advanced Text) :
"Normalement 27 euros - aujourd'hui seulement 17 euros avec ta commande."

**Bouton Oui** : `[cartflows_offer_yes]Oui, j'ajoute le guide pour 17 euros[/cartflows_offer_yes]`
Style : bouton large, vert, centre.

**Bouton Non** : `[cartflows_offer_no]Non merci, passer cette offre[/cartflows_offer_no]`
Style : texte simple, gris, sous le bouton Oui.

**Reassurance** (Kadence Advanced Text, petit, centre) :
"Telechargement immediat. Garantie satisfait ou rembourse 30 jours."

**[ECRAN - apercu de la page upsell complete]**

---

**[SECTION 5 - Designer la page downsell]**

**[ECRAN - editeur Gutenberg de la page downsell]**

Step 4 : Downsell. Add Step → Downsell (Offer). Produit : Wallpaper digital HD. Offer Price : 5 euros.

La page downsell est plus courte. Le client a deja refuse une offre - ne le surcharge pas.

**Titre** : "Pas besoin du guide complet ? Emporte au moins le wallpaper exclusif."

**Image** : apercu du wallpaper sur un ecran de bureau.

**Prix** : "Seulement 5 euros - disponible nulle part ailleurs."

**Bouton Oui** : `[cartflows_offer_yes]Oui, j'ajoute le wallpaper pour 5 euros[/cartflows_offer_yes]`

**Bouton Non** : `[cartflows_offer_no]Non merci, finaliser ma commande[/cartflows_offer_no]`

Pas besoin de longue liste de benefices. A 5 euros, c'est une decision impulsive. L'image et le prix suffisent.

---

**[SECTION 6 - Step Thank You Page]**

**[ECRAN - editeur de la Thank You Page]**

Step 5 : Thank You. Designe une page de confirmation avec :

- **Message principal** : "Merci pour ta commande ! Ton t-shirt est en preparation."
- **Recap commande** : utilise le shortcode `[cartflows_order_details]` pour afficher le resume automatique
- **Acces digital** : si le client a achete le guide ou le wallpaper, affiche les liens de telechargement. WooCommerce gere ca automatiquement via les emails de confirmation, mais un lien direct sur la Thank You Page ameliore l'experience.
- **CTA secondaire** : "Rejoins notre communaute" ou lien vers les reseaux sociaux

---

**[SECTION 7 - Calculer l'AOV potentiel]**

**[ECRAN - tableau des 4 scenarios avec calcul AOV]**

Faisons les comptes pour 100 clients qui entrent dans le funnel :

| Scenario | Calcul | Total |
|---|---|---|
| T-shirt seul | 29 euros | 29 euros |
| T-shirt + bump | 29 + 7 | 36 euros |
| T-shirt + bump + upsell | 29 + 7 + 17 | 53 euros |
| T-shirt + bump + upsell + (downsell non applicable car upsell accepte) | 29 + 7 + 17 | 53 euros |
| T-shirt + bump + downsell (upsell refuse) | 29 + 7 + 5 | 41 euros |
| Tout accepte sauf bump | 29 + 17 | 46 euros |
| Maximum possible | 29 + 7 + 17 | 53 euros |

Avec des taux moyens : 40% prennent le bump, 15% acceptent l'upsell, 20% de ceux qui refusent acceptent le downsell.

Sur 100 clients :
- Revenu produit de base : 100 x 29 = 2900 euros
- Revenu bump : 40 x 7 = 280 euros
- Revenu upsell : 15 x 17 = 255 euros
- Revenu downsell : 17 x 5 = 85 euros (17 = 20% des 85 qui ont refuse l'upsell)
- **Total : 3520 euros** au lieu de 2900 euros. **+21% d'AOV** sans un euro de pub supplementaire.

Et ce sont des estimations conservatrices. Avec un bon copywriting et des offres pertinentes, ces taux peuvent monter.

---

**[SECTION 8 - Tester le parcours complet]**

**[ECRAN - CartFlows → Settings → Test Mode]**

Derniere etape : tester. Active le mode test. Parcours le funnel en entier :

1. Landing Page : clique sur "Commander"
2. Checkout : remplis le formulaire, ajoute le bump, paie
3. Upsell : clique sur "Oui" une fois, puis recommence et clique sur "Non"
4. Downsell (apres refus upsell) : teste les deux boutons
5. Thank You : verifie le recap commande

**[ECRAN - commande WooCommerce avec tous les produits]**

Verifie dans WooCommerce que la commande contient les bons produits et les bons montants. Verifie que les produits digitaux sont bien attaches en telechargement.

Desactive le mode test. Ton funnel est en production.

---

**[OUTRO - face camera]**

Tu viens de construire un funnel complet : produit physique, order bump, upsell digital et downsell digital. C'est la structure type d'un funnel e-commerce rentable.

Retiens les chiffres : +21% d'AOV minimum, sans augmenter ton budget publicitaire. Chaque composant (bump, upsell, downsell) ajoute une couche de revenu supplementaire.

C'est la fin du Module 5. Tu maitrises maintenant les upsells one-click, les downsells, les Dynamic Offers, les Segments et les specificites PayPal. Dans le prochain module, on va s'attaquer a un autre levier de conversion : les A/B tests pour optimiser chaque element de ton funnel.

---

## Notes de production

- **Visuels** : schema funnel complet avec prix, captures WooCommerce (creation produits), CartFlows (tous les steps), Gutenberg (pages upsell et downsell), tableau calcul AOV
- **Captures d'ecran** : creation produits, flow complet Canvas Mode, page upsell designee, commande WooCommerce finale
- **Rythme** : soutenu, enchainement rapide des etapes. Montage possible en accelere sur les parties repetitives (creation produits)
- **Ton** : concret et chiffre, synthese du module
- **Duree estimee** : ~12 min a debit normal
- **Transition** : fin du Module 5, teaser Module 6 (A/B tests)
