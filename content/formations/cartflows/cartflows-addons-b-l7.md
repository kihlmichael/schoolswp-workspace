# Lecon B.7 — Segmenter les abandons

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : B — Cart Abandonment Recovery
- **Duree cible** : 8 min (~1 100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre que tous les abandons ne se valent pas, segmenter par montant/produit/recurrence, et adapter la strategie de relance en consequence.

---

## Script narration

**[INTRO — face camera]**

Jusqu'ici, on a traite tous les abandons de la meme facon : meme sequence, memes emails, memes delais. Ca fonctionne. Mais pour aller plus loin, il faut comprendre que tous les abandons ne se valent pas.

Un client qui abandonne un panier a 25€ et un client qui abandonne un panier a 250€ ne meritent pas la meme attention. La segmentation, c'est ce qui transforme une bonne sequence de relance en une strategie de recuperation intelligente.

---

**[SECTION 1 — Segmenter par montant du panier]**

**[ECRAN — tableau de bord Cart Abandonment avec montants]**

Dans le tableau de bord Cart Abandonment (WooCommerce → Cart Abandonment), tu vois la liste de tous les paniers abandonnes avec leur montant. C'est la premiere grille de lecture.

**Petit panier (moins de 30€)** : l'abandon est souvent lie a un manque de motivation. Le produit n'etait pas assez cher pour creer un vrai engagement. La sequence standard avec un coupon de 10% dans l'email 3 fonctionne bien — les 3€ de reduction suffisent a debloquer la decision.

**Panier moyen (30€ a 100€)** : c'est la zone ou la sequence de relance performe le mieux. Le client etait engage, le montant est significatif, et un rappel + argument + coupon recupere une bonne proportion de ces abandons.

**Gros panier (plus de 100€)** : la, l'enjeu est different. Le client a besoin de plus de reassurance. Les raisons d'abandon sont souvent liees a la confiance (est-ce que le site est fiable ?) ou au besoin de valider l'achat avec quelqu'un d'autre. Pour ces paniers, une relance plus agressive est justifiee — et le ROI d'un panier recupere a 200€ merite un effort supplementaire.

Conseil pratique : si tu vois des gros paniers abandonnes regulierement, envisage de les contacter manuellement en plus de la sequence automatique. Un email personnel du type "J'ai vu que tu avais commence une commande, est-ce que je peux t'aider ?" peut debloquer la situation.

---

**[SECTION 2 — Segmenter par produit]**

**[ECRAN — liste abandons filtree par produit]**

Le tableau de bord te montre aussi quel produit etait dans le panier abandonne. C'est une mine d'or d'informations.

Si un produit apparait dans un nombre disproportionne d'abandons, le probleme n'est probablement pas l'email de relance — c'est le produit lui-meme ou sa presentation.

**Abandon eleve sur un produit specifique** : verifie le prix (trop cher par rapport a la concurrence ?), la description (pas assez de details ?), les avis clients (pas de preuve sociale ?), les frais de livraison (surprise au checkout ?).

**Abandon faible sur un produit** : ce produit convertit bien. Analyse pourquoi et applique les memes principes aux autres produits.

Cette analyse produit par produit te permet d'ameliorer ta boutique au-dela de la simple relance email. L'abandon de panier est un symptome — la segmentation par produit t'aide a identifier la cause.

---

**[SECTION 3 — Segmenter par recurrence]**

**[ECRAN — historique client avec multiple abandons]**

Certains clients abandonnent une fois. D'autres abandonnent cinq fois. Ce n'est pas le meme profil.

**Premier abandon** : le client decouvre ta boutique, il hesite, il compare. La sequence standard fonctionne. Il a besoin d'un rappel et eventuellement d'un incentive.

**Abandon recurrent** : le client connait ta boutique, il revient, il met des produits au panier, et il ne finalise jamais. Deux hypotheses : soit il utilise le panier comme liste de souhaits (il garde les produits pour plus tard), soit il attend systematiquement une promotion.

Pour les abandonneurs recurrents, la sequence standard avec coupon peut creer un mauvais reflexe : le client apprend qu'en abandonnant, il recoit 10%. Il abandonne volontairement pour avoir la reduction.

Solution : ne pas envoyer de coupon aux clients qui ont deja abandonne plus de 2 fois. Les deux premiers emails (rappel + valeur) suffisent. Le coupon est reserve aux premiers abandons.

---

**[SECTION 4 — Adapter la strategie par segment]**

**[ECRAN — slide matrice segment × strategie]**

Voici comment adapter ta strategie selon le segment :

| Segment | Email 1 | Email 2 | Email 3 |
|---|---|---|---|
| Petit panier (<30€) | Rappel simple | Rappel + benefice | Coupon 10-15% |
| Panier moyen (30-100€) | Rappel simple | Rappel + temoignage | Coupon 10% |
| Gros panier (>100€) | Rappel simple | Rappel + garantie + temoignage | Coupon 5% + email personnel |
| Abandon recurrent | Rappel simple | Rappel + benefice | Pas de coupon |

En version gratuite, tu ne peux pas creer plusieurs sequences automatiques. Tu utilises la sequence standard et tu ajustes manuellement pour les gros paniers et les abandonneurs recurrents.

---

**[SECTION 5 — Version Pro : regles de segmentation avancees]**

**[ECRAN — slide features Pro]**

La version Pro de Cart Abandonment Recovery (59€/an) ajoute des regles de segmentation automatisees. Tu peux creer des sequences differentes selon :

- Le montant du panier (seuil configurable)
- Le produit ou la categorie de produit
- Le statut du client (nouveau vs existant)
- Le nombre d'abandons precedents

Si ton volume d'abandons justifie l'investissement (plus de 50 abandons par mois), la version Pro se rentabilise rapidement. Pour les boutiques avec moins de volume, la segmentation manuelle et la sequence standard suffisent.

---

**[CONCLUSION — face camera]**

Segmenter tes abandons, c'est passer d'une approche "un email pour tout le monde" a une strategie ciblee. Le montant du panier te dit combien investir dans la relance. Le produit te dit si le probleme est la relance ou la boutique. La recurrence te dit si tu crees de mauvaises habitudes.

Dans la prochaine lecon, on connecte Cart Abandonment Recovery a FluentCRM pour aller encore plus loin dans la relance — le court terme automatise, le long terme personnalise.

---

## Notes de production

- **Visuels** : tableau abandons avec montants, matrice segment × strategie, slide features Pro
- **Donnees** : seuils segmentation 30€/100€ (adapte boutique WooCommerce FR), Pro a 59€/an
- **Transition** : enchaine sur LB.8 (Cart Abandonment + FluentCRM)
