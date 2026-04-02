# Lecon B.5 — Generer des coupons uniques automatiquement

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : B — Cart Abandonment Recovery
- **Duree cible** : 8 min (~1 100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer la generation automatique de coupons uniques dans l'email 3 de la sequence, comprendre les avantages par rapport a un code generique, et choisir le bon montant de reduction.

---

## Script narration

**[INTRO — face camera]**

L'email 3 de ta sequence de relance propose un coupon de reduction. Mais pas n'importe quel coupon. Un code unique, genere automatiquement pour chaque client, avec une date d'expiration. C'est ce qui fait la difference entre une offre credible et un code generique qu'on trouve sur Google en deux secondes.

---

**[SECTION 1 — Activer les coupons automatiques]**

**[ECRAN — Cart Abandonment → Follow-Up Emails → Email 3 → Coupon settings]**

Va dans WooCommerce → Cart Abandonment → Follow-Up Emails. Clique sur l'email 3 (celui a 3 jours).

Dans les parametres de l'email, tu vas trouver une section "Coupon". Active l'option "Enable Coupon".

Trois champs a configurer :

**Type de reduction** : pourcentage ou montant fixe. Pour la plupart des boutiques, le pourcentage est plus efficace parce qu'il s'adapte au montant du panier. Un client avec un panier a 200€ recoit une reduction de 20€, un client avec un panier a 50€ recoit 5€. C'est proportionnel et percu comme equitable.

**Montant** : 10%. C'est le sweet spot. Assez pour convaincre un client hesitant, pas assez pour ruiner ta marge. En dessous de 5%, la reduction n'est pas percue comme significative. Au-dessus de 15%, tu sacrifies trop de marge et tu habitues tes clients a attendre les coupons.

**Expiration** : 48 heures apres l'envoi de l'email. L'expiration cree de l'urgence reelle. Le client sait que le code ne sera plus valable dans deux jours. C'est pas une fausse rarete — le code expire vraiment.

Valide. Le plugin generera desormais un coupon unique pour chaque abandon.

---

**[SECTION 2 — Comment ca fonctionne en coulisses]**

**[ECRAN — schema generation coupon]**

Quand l'email 3 est declenche (3 jours apres l'abandon), le plugin cree automatiquement un coupon WooCommerce.

Ce coupon a des caracteristiques specifiques :

- **Code unique** : chaque client recoit un code different. Pas de "RELANCE10" partage sur tous les emails.
- **Usage unique** : le code ne peut etre utilise qu'une seule fois. Le client ne peut pas le reutiliser pour une autre commande.
- **Date d'expiration** : le coupon expire apres le delai que tu as configure (48 heures par defaut).
- **Lie au panier** : le coupon est associe au panier abandonne du client.

Tu peux voir tous les coupons generes dans WooCommerce → Coupons. Ils apparaissent avec un prefixe identifiable (en general "abandon-") pour les distinguer de tes coupons manuels.

---

**[SECTION 3 — Pourquoi les coupons uniques sont superieurs aux codes generiques]**

**[ECRAN — slide comparaison unique vs generique]**

Tu pourrais te dire : "Pourquoi ne pas mettre un code generique comme RELANCE10 dans tous les emails ?" Trois raisons.

**Raison 1 : les abus.** Un code generique finit toujours par se retrouver sur des sites de coupons (Dealabs, Ma Reduc, etc.). Des gens qui n'ont jamais abandonne de panier chez toi l'utilisent. Tu perds de l'argent sans recuperer de panier.

**Raison 2 : le tracking.** Avec un coupon unique, tu sais exactement quel panier abandonne a ete recupere grace au coupon. Tu peux calculer le ROI precis de ton email 3. Avec un code generique, impossible de distinguer un vrai abandon recupere d'un opportuniste.

**Raison 3 : la perception.** Un code unique donne l'impression d'une offre personnelle. "Voici ton code exclusif : ABCD-1234." Le client se sent privilegie. Un code generique donne l'impression d'une promotion de masse — beaucoup moins convaincant.

---

**[SECTION 4 — Choisir le bon montant : la strategie]**

**[ECRAN — slide strategy 3 paliers]**

Le 10% est un point de depart. En fonction de ta marge et de ton panier moyen, tu peux ajuster.

**Marge elevee (>50%)** — tu peux monter a 15%. La reduction est significative pour le client et tu absorbes facilement le cout.

**Marge standard (30-50%)** — reste a 10%. C'est le bon equilibre entre incitation et rentabilite.

**Marge faible (<30%)** — descends a 5% ou passe sur un montant fixe (5€ de reduction). Le pourcentage sur un gros panier pourrait grignoter trop de marge.

Alternative au pourcentage : la livraison gratuite. Si tu factures la livraison, offrir la livraison gratuite dans l'email 3 peut etre plus efficace qu'un pourcentage — surtout si les frais de livraison etaient la raison de l'abandon.

Un dernier conseil : ne change pas le montant toutes les semaines. Configure 10%, laisse tourner 30 jours, analyse les resultats, puis ajuste si necessaire. Les decisions basees sur les donnees battent toujours l'intuition.

---

**[CONCLUSION — face camera]**

Les coupons uniques sont configures. Chaque abandon qui atteint l'email 3 recevra un code personnalise, a usage unique, avec une deadline reelle. C'est le dernier levier de ta sequence de relance.

Dans la prochaine lecon, on va analyser le tableau de bord pour voir combien de paniers tu recuperes et quel email performe le mieux.

---

## Notes de production

- **Visuels** : capture parametres coupon dans l'editeur email, schema generation coupon, slide comparaison unique vs generique
- **Donnees** : sweet spot 10% (standard industrie), coupons WooCommerce generes automatiquement
- **Transition** : enchaine sur LB.6 (analyser le tableau de bord)
