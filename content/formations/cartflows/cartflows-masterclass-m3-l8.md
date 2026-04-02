# Lecon 3.8 — Coupon URL : appliquer une remise automatiquement

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 3 — Checkout optimise
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir construire une URL de checkout CartFlows qui applique automatiquement un code coupon WooCommerce — et comprendre les cas d'usage concrets pour maximiser la conversion.

---

## Script narration

**[INTRO — face camera]**

Tu envoies un email promo a ta liste. Le client clique sur le lien. Il arrive sur le checkout. Et la remise est deja appliquee. Il n'a rien a faire — pas de code a taper, pas de champ coupon a chercher. Le prix reduit est la, affiche, pret a payer.

C'est ce que permettent les coupon URLs dans CartFlows. Une fonctionnalite simple, mais qui change radicalement le taux de conversion de tes offres promotionnelles.

---

**[SECTION 1 — Le concept : la remise dans l'URL]**

**[ECRAN — URL affichee en gros avec le parametre ?coupon=PROMO20 surligne]**

Le principe est simple. Tu prends l'URL de ton checkout CartFlows — par exemple `tonsite.com/checkout-formation/`. Tu ajoutes un parametre a la fin : `?coupon=PROMO20`. Quand le client ouvre ce lien, CartFlows detecte le parametre, cherche le coupon correspondant dans WooCommerce, et l'applique automatiquement.

Le client arrive sur le checkout et voit directement le prix barre et le prix reduit. Pas d'etape supplementaire, pas d'action de sa part. La friction est a zero.

C'est l'inverse du champ coupon classique, ou le client doit trouver le code, le copier, le coller dans le bon champ, et esperer qu'il fonctionne. Avec le coupon URL, tout est fait pour lui.

---

**[SECTION 2 — Creer le coupon dans WooCommerce]**

**[ECRAN — WooCommerce → Marketing → Coupons → Ajouter un coupon]**

La premiere etape, c'est de creer le coupon dans WooCommerce. Va dans Marketing → Coupons → Ajouter un coupon.

Donne-lui un code clair et memorable — `PROMO20`, `LANCEMENT`, `VIP30`. Evite les codes aleatoires type `X7K9P2` pour les coupon URLs — meme si le client ne tape pas le code, il le voit dans la barre d'adresse. Un code lisible renforce la confiance.

Configure les parametres. Type de remise : pourcentage ou montant fixe. Montant : par exemple 20 pour 20%. Date d'expiration : indispensable pour les offres flash. Limite d'utilisation : si tu veux limiter a 100 utilisations ou une seule par client.

Tu peux aussi restreindre le coupon a certains produits ou categories. Pour un funnel CartFlows, je recommande de lier le coupon au produit specifique du flow — ca evite qu'il soit utilise ailleurs.

Publie le coupon. Il est pret.

---

**[SECTION 3 — Construire l'URL du checkout avec coupon]**

**[ECRAN — construction de l'URL etape par etape]**

Maintenant, tu construis l'URL. C'est de la concatenation basique.

Prends l'URL de ton checkout step CartFlows. Par exemple : `https://tonsite.com/checkout-formation/`

Ajoute le parametre coupon : `https://tonsite.com/checkout-formation/?coupon=PROMO20`

C'est tout. Ce lien est pret a etre utilise. Quand quelqu'un le clique, CartFlows applique le coupon `PROMO20` automatiquement.

Attention a la casse : le code coupon dans l'URL doit correspondre exactement au code cree dans WooCommerce. Si tu as cree `PROMO20` en majuscules, utilise `PROMO20` dans l'URL. WooCommerce n'est pas toujours sensible a la casse, mais par securite, garde la meme ecriture.

---

**[SECTION 4 — Cas d'usage concrets]**

**[ECRAN — 3 exemples avec icones : email, affilie, flash sale]**

Les coupon URLs sont particulierement efficaces dans trois situations.

**Emails exclusifs.** Tu envoies une offre speciale a ta liste email — "moins 20% cette semaine". Le lien dans l'email contient le coupon. Tes abonnes cliquent et arrivent directement sur un checkout avec la remise appliquee. Zero friction.

**Liens pour les affilies.** Tu donnes un lien personnalise a chaque affilie — avec un coupon dedie. L'affilie partage son lien, le client beneficie de la remise, et tu peux traquer quel affilie a genere la vente grace au code coupon.

**Offres flash.** Tu publies un lien sur tes reseaux sociaux — "24h seulement, moins 30%". Le lien contient le coupon avec une date d'expiration. Passe le delai, le coupon ne fonctionne plus, meme si quelqu'un retrouve le lien.

---

**[SECTION 5 — Combiner coupon et pre-remplissage]**

**[ECRAN — URL complete avec coupon + first_name + email]**

Tu peux aller plus loin. CartFlows permet de pre-remplir les champs du checkout via l'URL. Combine ca avec le coupon pour une experience ultra-fluide.

L'URL complete ressemble a ca :

`https://tonsite.com/checkout-formation/?coupon=PROMO20&billing_first_name=Jean&billing_email=jean@mail.com`

Le client clique. Il arrive sur le checkout avec la remise appliquee, son prenom deja rempli, et son email deja rempli. Il ne lui reste qu'a entrer ses informations de paiement et a cliquer sur "Payer".

C'est particulierement puissant dans les emails, ou tu connais deja le prenom et l'email du destinataire. La plupart des outils d'emailing — FluentCRM, MailerLite, ConvertKit — te permettent d'inserer des variables dans les liens. Tu construis le lien dynamiquement avec les donnees du contact.

---

**[SECTION 6 — Pourquoi ca convertit mieux]**

**[ECRAN — stat "2x plus de conversions" avec schema comparatif]**

Les coupon URLs convertissent significativement mieux que les champs coupon manuels. Le client n'a rien a faire — la remise est deja appliquee.

Le champ coupon classique pose trois problemes. Le client ne sait pas ou il est sur la page. Le client a oublie le code ou l'a mal copie. Le client voit le champ vide et se dit "il doit y avoir un code quelque part" — et part le chercher sur Google au lieu de payer.

Avec le coupon URL, ces trois problemes disparaissent. Le client voit le prix reduit des son arrivee. Il n'a aucune raison de quitter la page. Le chemin entre le clic et le paiement est le plus court possible.

---

**[CONCLUSION — face camera]**

Les coupon URLs, c'est le parametre `?coupon=CODE` ajoute a l'URL de ton checkout CartFlows. Le coupon est cree dans WooCommerce, l'URL l'applique automatiquement. Combine-le avec le pre-remplissage des champs pour une experience encore plus fluide.

Utilise-les dans tes emails, tes liens affilies, et tes offres flash. C'est simple a mettre en place, et l'impact sur la conversion est immediat.

---

## Notes de production

- **Visuels requis** : URL decomposee avec parametre coupon surligne, WooCommerce coupon creation screen, 3 icones cas d'usage (email/affilie/flash), URL complete avec pre-remplissage, comparaison champ coupon manuel vs coupon URL
- **Captures d'ecran** : WooCommerce Marketing → Coupons, CartFlows checkout avec coupon applique (prix barre visible), barre d'adresse avec le parametre coupon
- **Points d'insistance voix** : "Le client n'a rien a faire" (intro + section 6), "Zero friction" (section 1)
- **Transitions** : progression concept → creation → construction URL → usage → impact
