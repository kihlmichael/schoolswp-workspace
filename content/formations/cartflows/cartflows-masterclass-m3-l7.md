# Lecon 3.7 — Methodes de paiement : Stripe, PayPal, Apple Pay

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 3 — Checkout optimise
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir quelles methodes de paiement activer dans WooCommerce pour CartFlows, comment configurer Stripe et PayPal, et comprendre l'impact de chaque methode sur la conversion et les upsells one-click.

---

## Script narration

**[INTRO — face camera]**

La methode de paiement, c'est le dernier obstacle entre ton client et son achat. S'il ne trouve pas son moyen de paiement prefere, il abandonne. C'est aussi simple que ca.

CartFlows ne gere pas les paiements directement — il utilise les passerelles WooCommerce. Mais le choix de ces passerelles a un impact direct sur ta conversion et sur les fonctionnalites CartFlows que tu peux utiliser. Dans cette lecon, on passe en revue Stripe, PayPal, et les paiements mobiles — Apple Pay et Google Pay.

---

**[SECTION 1 — Les methodes de paiement supportees par CartFlows]**

**[ECRAN — WooCommerce → Reglages → Paiements → liste des passerelles actives]**

CartFlows fonctionne avec toutes les passerelles de paiement WooCommerce. Stripe, PayPal, virement bancaire, cheque — tout ce que WooCommerce supporte, CartFlows le supporte.

Mais dans la pratique, pour un funnel de vente optimise, tu as besoin de deux passerelles : Stripe et PayPal. C'est le duo qui couvre la grande majorite des clients en France et en Europe.

Stripe gere les cartes bancaires — Visa, Mastercard, CB — plus Apple Pay et Google Pay. PayPal offre une alternative pour les clients qui preferent payer sans entrer leur numero de carte. A eux deux, tu couvres plus de 95% des preferences de paiement de tes clients.

---

**[SECTION 2 — Stripe : la passerelle de reference]**

**[ECRAN — WooCommerce → Reglages → Paiements → Stripe → configuration]**

Stripe, c'est la passerelle que je recommande en premier. Voici pourquoi.

Cote configuration : installe le plugin "WooCommerce Stripe Payment Gateway" (le plugin officiel gratuit). Dans WooCommerce → Reglages → Paiements, active Stripe et connecte ton compte. Tu renseignes tes cles API — cle publique et cle secrete — que tu trouves dans ton dashboard Stripe.

Les avantages de Stripe pour CartFlows. Premier avantage : le paiement par carte bancaire directement dans le checkout, sans redirection vers un site externe. Le client reste sur ta page. Deuxieme avantage : Stripe supporte les upsells one-click de CartFlows. Quand le client a deja entre sa carte, les offres upsell suivantes peuvent etre acceptees en un seul clic — pas besoin de retaper les informations de paiement. C'est un avantage majeur pour la conversion des upsells.

Troisieme avantage : Apple Pay et Google Pay. Avec Stripe, tu peux activer ces deux methodes de paiement mobile. On en reparle dans la section 4.

Les frais Stripe en France : 1,5% + 0,25 euros par transaction pour les cartes europeennes. Pour une vente a 97 euros, ca te coute 1,71 euros de frais. C'est competitif et transparent.

---

**[SECTION 3 — PayPal : la confiance du client]**

**[ECRAN — WooCommerce → Reglages → Paiements → PayPal → configuration]**

PayPal a un avantage unique : la confiance. Beaucoup de clients, surtout ceux qui achevent en ligne pour la premiere fois ou qui ne connaissent pas ton site, preferent payer via PayPal. Ils ne donnent pas leur numero de carte a un site inconnu — ils passent par un intermediaire qu'ils connaissent.

Pour la configuration : installe "WooCommerce PayPal Payments" (le plugin officiel). Connecte ton compte PayPal Business. Active le paiement PayPal dans WooCommerce → Reglages → Paiements.

L'avantage principal : le client clique sur le bouton PayPal, se connecte a son compte, confirme le paiement, et revient sur ta page. Pas besoin de taper un numero de carte. Pour certains segments — les 40 ans et plus, les acheteurs prudents — c'est le facteur decisif.

La limitation importante pour CartFlows : PayPal ne supporte pas les upsells one-click aussi bien que Stripe. Avec PayPal, le client doit reconfirmer chaque paiement supplementaire. Ca ajoute une etape de friction pour les offres upsell. C'est la raison principale pour laquelle Stripe reste la passerelle prioritaire si tu utilises des upsells dans ton funnel.

Les frais PayPal en France : 2,9% + 0,35 euros par transaction. Pour une vente a 97 euros, ca te coute 3,16 euros de frais. C'est presque deux fois plus cher que Stripe. C'est le prix de la confiance que PayPal apporte a certains clients.

---

**[SECTION 4 — Apple Pay et Google Pay via Stripe]**

**[ECRAN — checkout mobile avec bouton Apple Pay visible en haut du formulaire]**

Apple Pay et Google Pay sont des methodes de paiement express. Le client paie avec son empreinte digitale ou Face ID sur son telephone — pas de numero de carte a taper, pas de formulaire a remplir.

Ces deux methodes fonctionnent via Stripe. Tu n'as pas besoin d'un plugin supplementaire. Dans les reglages Stripe de WooCommerce, active "Payment Request Buttons". Un bouton Apple Pay apparait automatiquement sur les appareils Apple (iPhone, iPad, Mac avec Safari), et un bouton Google Pay sur les appareils Android et Chrome.

Ou est-ce que ca s'affiche ? En haut du formulaire de paiement, avant les champs de carte bancaire. Le client voit le bouton Apple Pay en premier, clique, confirme avec Face ID, et c'est termine. Pas de formulaire, pas de frappe — le paiement se fait en 3 secondes.

L'impact sur mobile est significatif. Sur les sites e-commerce, 60 a 70% du trafic vient du mobile. Si la moitie de ces visiteurs ont un iPhone, Apple Pay leur evite de taper 16 chiffres de carte sur un petit ecran. Le taux de conversion mobile augmente mecaniquement.

Le prerequis technique : ton site doit etre en HTTPS (ce qui devrait deja etre le cas) et tu dois verifier ton domaine dans le dashboard Stripe. Stripe te guide dans cette verification — c'est un fichier a ajouter a la racine de ton site.

---

**[SECTION 5 — Strategie recommandee et comparaison des frais]**

**[ECRAN — tableau comparatif Stripe vs PayPal : frais, upsells, mobile]**

Ma recommandation : active Stripe et PayPal au minimum. Les deux ensemble couvrent tous les cas d'usage.

Si tu utilises les upsells one-click de CartFlows — et tu devrais — Stripe est ta passerelle prioritaire. Le client paie par carte via Stripe, et toutes les offres upsell suivantes se font en un clic. Pas de friction, pas de re-saisie.

PayPal reste en deuxieme option pour les clients qui preferent. Tu perds le one-click sur les upsells pour ces clients, mais tu gagnes la vente initiale qu'ils n'auraient peut-etre pas faite autrement.

Comparaison rapide des frais sur une vente a 97 euros. Stripe : 1,71 euros. PayPal : 3,16 euros. La difference est de 1,45 euros par transaction. Sur 100 ventes par mois, ca represente 145 euros. C'est un cout a prendre en compte, mais si PayPal te rapporte ne serait-ce que 5 ventes supplementaires par mois, le calcul est largement positif.

---

**[SECTION 6 — Mode test : verifier avant de lancer]**

**[ECRAN — Stripe dashboard → toggle "Test mode"]**

Avant de lancer ton funnel, teste chaque methode de paiement. Stripe et PayPal ont tous les deux un mode test.

Pour Stripe : active le mode test dans ton dashboard Stripe, copie les cles API de test dans WooCommerce, et utilise la carte de test 4242 4242 4242 4242 avec n'importe quelle date future et CVC. Passe une commande complete — checkout, upsell, thank you page — pour verifier que tout fonctionne.

Pour PayPal : cree un compte sandbox sur developer.paypal.com. Utilise les identifiants sandbox dans WooCommerce. Fais une commande test complete.

Teste sur desktop et sur mobile. Verifie que le bouton Apple Pay apparait bien sur iPhone (tu auras besoin d'un vrai appareil Apple pour ca — le mode test Stripe fonctionne avec Apple Pay sandbox).

---

**[CONCLUSION — face camera]**

Active Stripe plus PayPal au minimum. Stripe seul si tu veux les upsells one-click sans friction. Active Apple Pay et Google Pay dans Stripe pour le mobile. Et teste tout avant de lancer.

La methode de paiement, c'est le dernier metre du funnel. Simplifie-le au maximum.

Dans la prochaine lecon, on voit les coupon URLs — comment appliquer une remise automatiquement via un lien.

---

## Notes de production

- **Visuels requis** : tableau comparatif Stripe vs PayPal (frais, upsells, mobile), capture checkout mobile avec Apple Pay, schema flux paiement Stripe vs PayPal
- **Captures d'ecran** : WooCommerce Reglages Paiements, Stripe config page, PayPal config page, Stripe dashboard toggle test mode, checkout frontend avec boutons Apple Pay + Google Pay
- **Points d'insistance voix** : "Active Stripe plus PayPal au minimum" (conclusion), "1,5% + 0,25 euros" et "2,9% + 0,35 euros" (bien articuler les chiffres)
- **Transitions** : structure en entonnoir — vue d'ensemble → detail par passerelle → comparaison → test
