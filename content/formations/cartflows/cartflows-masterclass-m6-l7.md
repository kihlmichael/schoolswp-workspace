# Lecon 6.7 - Connecter Google Analytics 4 + Facebook Pixel

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 6 - A/B Testing et Analytics
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Connecter GA4 et le Facebook Pixel a CartFlows. Verifier que les events e-commerce remontent correctement. Configurer le consentement cookies pour la conformite RGPD.

---

## Script narration

**[INTRO - face camera]**

CartFlows a son propre tableau de bord Analytics. C'est utile, mais limite. Pour avoir une vision complete de ton funnel - source du trafic, comportement des visiteurs, attribution des ventes - tu as besoin de connecter des outils externes.

Dans cette lecon, on connecte Google Analytics 4 et le Facebook Pixel a CartFlows. Et on le fait proprement, en respectant le RGPD.

---

**[SECTION 1 - Acceder aux reglages integrations CartFlows]**

**[ECRAN - CartFlows > Settings > Integrations]**

Dans ton tableau de bord WordPress, va dans CartFlows, puis Settings, puis l'onglet Integrations. C'est ici que tu vas configurer les connexions avec GA4 et Facebook.

CartFlows offre une integration native avec ces deux outils. Pas besoin de plugin supplementaire. Pas besoin de code personnalise. Tu colles un identifiant et CartFlows gere le reste.

---

**[SECTION 2 - Connecter Google Analytics 4]**

**[ECRAN - champ GA4 Measurement ID dans CartFlows]**

Pour GA4, tu as besoin de ton Measurement ID. C'est un identifiant qui commence par "G-" suivi de caracteres alphanumeriques. Exemple : G-ABC123DEF4.

Ou le trouver : ouvre Google Analytics, va dans Admin, puis Data Streams. Clique sur ton flux de donnees web. Le Measurement ID est affiche en haut.

Copie cet identifiant. Retour dans CartFlows > Settings > Integrations. Colle le Measurement ID dans le champ prevu. Enregistre.

C'est fait. CartFlows va maintenant envoyer automatiquement les events e-commerce a GA4 :

- **begin_checkout** : quand un visiteur arrive sur la page checkout
- **add_payment_info** : quand il remplit les informations de paiement
- **purchase** : quand la commande est validee

Ces events suivent le standard e-commerce GA4. Tu les retrouveras dans GA4 sous Rapports > Monetisation > Vue d'ensemble. Tu verras le revenu, le nombre de transactions, et le parcours d'achat de tes visiteurs.

---

**[SECTION 3 - Connecter le Facebook Pixel]**

**[ECRAN - champ Facebook Pixel ID dans CartFlows]**

Pour le Facebook Pixel, tu as besoin de ton Pixel ID. C'est un numero a 15-16 chiffres.

Ou le trouver : ouvre le Meta Business Suite (business.facebook.com). Va dans Events Manager. Selectionne ton pixel. Le Pixel ID est affiche en haut de la page.

Copie ce numero. Dans CartFlows > Settings > Integrations, colle-le dans le champ Facebook Pixel. Enregistre.

CartFlows envoie automatiquement les events suivants au pixel :

- **ViewContent** : quand un visiteur voit une page du funnel
- **InitiateCheckout** : quand il arrive sur le checkout
- **AddToCart** : quand il ajoute un order bump
- **Purchase** : quand la commande est validee, avec le montant

Ces events alimentent directement tes audiences Facebook. Tu pourras creer des audiences de retargeting (les visiteurs qui ont initie un checkout sans acheter), des audiences similaires (lookalike des acheteurs), et mesurer le ROAS de tes campagnes publicitaires.

---

**[SECTION 4 - Verifier avec Tag Assistant et Pixel Helper]**

**[ECRAN - extension Tag Assistant dans Chrome]**

La configuration est en place. Maintenant, on verifie que ca fonctionne reellement.

Pour GA4, installe l'extension Chrome "Google Tag Assistant". Ouvre ta page checkout. Clique sur l'extension. Elle te montre les tags detectes sur la page. Tu dois voir ton Measurement ID et les events envoyes. Si le tag apparait en vert, tout fonctionne. En rouge, il y a un probleme - verifie que l'ID est correct et que la page est bien dans un flow CartFlows.

Pour le Facebook Pixel, installe l'extension Chrome "Meta Pixel Helper". Meme principe : ouvre ta page checkout, clique sur l'extension. Elle affiche les events detectes. Tu dois voir "PageView" et "InitiateCheckout". Navigue dans ton funnel jusqu'a la page de remerciement - tu dois voir "Purchase" avec le montant.

Fais un test complet : place une commande de test (avec un coupon 100% ou un produit a 0 euro) et verifie que tous les events remontent dans GA4 (temps reel > evenements) et dans le Meta Events Manager (onglet Test Events).

---

**[SECTION 5 - RGPD : le bandeau cookies est obligatoire]**

**[ECRAN - plugin bandeau cookies WordPress]**

Avant d'activer les pixels sur ton site en production, il y a une obligation legale a respecter. Le RGPD impose que tu obtiennes le consentement de tes visiteurs avant de poser des cookies de tracking.

Concretement : configure un bandeau de consentement cookies avant d'activer GA4 et le Facebook Pixel. C'est la loi en Europe. Si tu ne le fais pas, tu t'exposes a des sanctions.

Des plugins WordPress comme Complianz ou CookieYes gerent ca proprement. Ils affichent un bandeau au premier visit, enregistrent le choix du visiteur, et bloquent les scripts de tracking tant que le consentement n'est pas donne.

L'installation detaillee d'un bandeau cookies depasse le cadre de cette lecon, mais la regle est non negociable : pas de bandeau, pas de pixels. Configure le consentement d'abord, active les pixels ensuite.

Note : certains visiteurs refuseront les cookies. Tes donnees Analytics seront donc partielles - typiquement 60 a 80% des visiteurs acceptent le tracking. C'est normal. Tes donnees CartFlows internes ne sont pas affectees par le consentement cookies puisqu'elles ne passent pas par des cookies tiers.

---

**[SECTION 6 - Recapitulatif de la configuration]**

**[ECRAN - checklist de configuration]**

Pour resumer la configuration complete :

1. Installer un plugin de consentement cookies (Complianz ou CookieYes).
2. Configurer le bandeau et les categories de cookies.
3. Coller le GA4 Measurement ID dans CartFlows > Settings > Integrations.
4. Coller le Facebook Pixel ID au meme endroit.
5. Verifier avec Tag Assistant (GA4) et Pixel Helper (Facebook).
6. Faire une commande de test et confirmer que les events remontent.

Six etapes. En 30 minutes, c'est fait.

---

**[OUTRO - face camera]**

Tu as maintenant trois sources de donnees : le tableau de bord CartFlows pour le suivi quotidien, GA4 pour comprendre d'ou vient ton trafic et comment il se comporte, et le Facebook Pixel pour le retargeting et la mesure de tes campagnes publicitaires.

C'est la fin du module 6. Tu sais tester, mesurer, et analyser. Dans le prochain module, on va assembler tout ce que tu as appris pour construire un funnel complet de A a Z.

---

## Notes de production

- **Visuels** : captures CartFlows Settings > Integrations, GA4 Data Streams (Measurement ID), Meta Events Manager (Pixel ID), extensions Chrome (Tag Assistant, Pixel Helper), checklist configuration
- **Captures d'ecran** : CartFlows integrations, GA4 admin, Meta Business Suite, extensions Chrome (8 captures minimum)
- **Ton** : technique mais accessible, pas-a-pas oriente action
- **Duree estimee** : ~8 min a debit normal
- **Point juridique** : insister sur l'obligation RGPD sans dramatiser
- **Transition** : cloture du module 6, ouverture vers le module 7
