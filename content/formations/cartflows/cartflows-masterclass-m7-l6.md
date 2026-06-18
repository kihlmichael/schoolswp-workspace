# Lecon 7.6 - RGPD et consentement : gerer les cookies correctement

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 7 - Tracking et Pixels
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre les obligations RGPD liees au tracking, choisir et configurer un plugin de consentement WordPress, et configurer CartFlows pour ne charger les pixels qu'apres consentement.

---

## Script narration

**[INTRO - face camera]**

On a configure tous les pixels. Facebook, GA4, Pinterest, Snapchat, et meme le server-side. Mais il reste une etape que beaucoup d'entrepreneurs ignorent - ou font mal. Le consentement.

En Europe, la loi est claire : tu dois obtenir le consentement du visiteur avant de charger les scripts de tracking marketing. Pas apres. Pas en meme temps. Avant. Si tu charges le pixel Facebook des que la page se charge, sans demander l'avis du visiteur, tu es en infraction avec le RGPD.

Et les sanctions ne sont pas theoriques. La CNIL inflige regulierement des amendes - de quelques milliers d'euros pour les petites structures a des millions pour les plus grosses. Meme si tu es solo-preneur, tu n'es pas exempt.

---

**[SECTION 1 - Ce que dit la loi, concretement]**

**[ECRAN - resume reglementaire simplifie]**

Voici ce que le RGPD et la directive ePrivacy imposent, en version simple.

Les cookies strictement necessaires au fonctionnement du site - par exemple le cookie de session WooCommerce qui maintient le panier - n'ont pas besoin de consentement. Ils sont indispensables, le site ne fonctionne pas sans.

Les cookies analytiques - GA4, Matomo - necessitent un consentement, meme s'ils sont consideres comme "moins intrusifs". La CNIL accepte certaines exemptions pour les outils de mesure d'audience configures de maniere anonyme, mais dans le doute, demande le consentement.

Les cookies marketing - Facebook Pixel, Pinterest Tag, Snapchat Pixel, et tout pixel publicitaire - exigent un consentement explicite, prealable, et libre. Le visiteur doit pouvoir refuser aussi facilement qu'accepter. Pas de case pre-cochee. Pas de bandeau qui disparait apres 3 secondes. Pas de "en continuant a naviguer, vous acceptez".

En resume : tant que le visiteur n'a pas clique "Accepter" sur les cookies marketing, aucun pixel publicitaire ne doit se charger.

---

**[SECTION 2 - Les solutions WordPress pour le consentement]**

**[ECRAN - logos CookieYes, Complianz, GDPR Cookie Consent]**

Plusieurs plugins WordPress gerent ca proprement. Voici les trois plus fiables.

**CookieYes** - Interface claire, scan automatique des cookies de ton site, generation du bandeau conforme RGPD. Version gratuite suffisante pour demarrer. La version pro ajoute le consentement geolocalise (bandeau RGPD en Europe, CCPA aux US).

**Complianz** - Plugin neerlandais tres complet. Il detecte les scripts de tracking sur ton site et les bloque automatiquement jusqu'au consentement. Integration native avec les principaux plugins de tracking WordPress. C'est le plus "set and forget" des trois.

**GDPR Cookie Consent (CookieBot)** - Solution SaaS avec plugin WordPress. Scan automatique des cookies, categorisation, et blocage. L'interface est solide, mais la version gratuite est limitee a 100 pages.

Tous les trois fonctionnent sur le meme principe : le plugin detecte les scripts de tracking, les bloque au chargement de la page, affiche un bandeau de consentement, et ne debloque les scripts que si le visiteur accepte la categorie correspondante.

---

**[SECTION 3 - Configurer CartFlows pour le consentement]**

**[ECRAN - CartFlows Settings + plugin consentement]**

Voici comment ca fonctionne avec CartFlows.

Premiere approche : tu laisses le plugin de consentement gerer le blocage. Complianz et CookieYes detectent automatiquement les scripts injectes par CartFlows (Facebook Pixel, GA4, etc.) et les bloquent jusqu'au consentement. C'est la methode la plus simple - tu n'as rien a configurer dans CartFlows.

Deuxieme approche : tu utilises Google Tag Manager comme intermediaire. Au lieu de coller les Pixel ID directement dans CartFlows, tu configures GTM et tu geres le consentement via le Consent Mode de GTM. Le plugin de consentement communique avec GTM, et GTM decide quels tags charger. C'est plus technique, mais ca te donne un controle total.

Dans les deux cas, teste apres configuration. Ouvre ton site en navigation privee, refuse les cookies, et verifie avec le Pixel Helper que le pixel Facebook ne se charge pas. Ensuite, accepte les cookies et verifie qu'il se charge. Si le pixel se charge avant le consentement, il y a un probleme de configuration.

---

**[SECTION 4 - Les categories de cookies]**

**[ECRAN - tableau des 4 categories]**

Le bandeau de consentement doit proposer des categories, pas juste un bouton "tout accepter". Voici les quatre categories standards.

**Necessaires** - Cookies de session, panier WooCommerce, securite. Toujours actifs, pas de consentement requis.

**Analytiques** - GA4, Matomo. Mesure d'audience. Le visiteur peut les refuser sans impact sur son experience d'achat.

**Marketing** - Facebook Pixel, Pinterest Tag, Snapchat Pixel, tout pixel publicitaire. C'est la categorie la plus impactee par les refus.

**Preferences** - Cookies de personnalisation (langue, devise, preferences d'affichage). Rarement utilises dans un contexte CartFlows.

Le visiteur doit pouvoir accepter ou refuser chaque categorie independamment. Un bouton "Tout accepter" est autorise, mais le bouton "Tout refuser" doit etre aussi visible et accessible.

En pratique, sur un site e-commerce WordPress, 50 a 70% des visiteurs acceptent les cookies marketing. Les 30 a 50% restants ne seront pas trackes par les pixels publicitaires - mais ils seront comptes dans tes ventes WooCommerce. Tes rapports de vente restent complets, seul le tracking d'attribution est partiel.

---

**[SECTION 5 - Le consentement comme avantage concurrentiel]**

**[ECRAN - badge "Site respectueux de ta vie privee"]**

Dernier point, et c'est une conviction. Le RGPD n'est pas un obstacle a ton business. C'est un avantage concurrentiel.

Les visiteurs sont de plus en plus sensibles a la protection de leurs donnees. Un site qui affiche un bandeau clair, qui explique quels cookies sont utilises et pourquoi, qui permet de refuser facilement - ce site inspire confiance.

Et la confiance, en e-commerce, c'est le facteur de conversion numero un. Un visiteur qui fait confiance a ton site est un visiteur qui sort sa carte plus facilement. Un site transparent sur ses pratiques de tracking se demarque de la masse des sites qui empilent les dark patterns pour forcer le consentement.

Joue la carte de la transparence. Configure ton bandeau proprement, explique clairement a quoi servent les cookies, et respecte le choix de tes visiteurs. C'est la bonne pratique legale, ethique, et commerciale.

---

**[OUTRO - face camera]**

Le Module 7 est termine. Tu as maintenant un systeme de tracking complet : Facebook Pixel, GA4, les pixels secondaires si necessaire, la comprehension du server-side, et un consentement RGPD propre.

Chaque vente est tracee. Chaque canal est mesure. Chaque decision que tu prends est basee sur des donnees, pas sur des intuitions. Et tout ca, dans le respect de la loi et de tes visiteurs.

---

## Notes de production

- **Visuels ECRAN** : Resume reglementaire (3 niveaux cookies), logos plugins consentement, CartFlows + plugin consentement, tableau 4 categories, badge confiance
- **Ton** : Serieux sur la conformite, positif sur l'avantage concurrentiel, pas alarmiste
- **CTA fin** : Conclusion du module 7, transition vers le module suivant
- **Point attention montage** : Insister visuellement sur le test "pixel ne se charge pas avant consentement" - capture ecran Pixel Helper inactif puis actif
- **Mots-cles formation** : RGPD cookies WordPress, consentement tracking, CookieYes CartFlows, Complianz WooCommerce, bandeau cookies e-commerce
