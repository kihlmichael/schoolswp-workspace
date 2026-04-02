# Lecon 7.3 — Google Analytics 4 : e-commerce avance

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 7 — Tracking et Pixels
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer GA4 avec CartFlows, comprendre les events e-commerce automatiques, lire les rapports E-commerce purchases et Checkout journey, et utiliser l'attribution pour identifier les canaux rentables.

---

## Script narration

**[INTRO — face camera]**

Google Analytics 4, c'est l'outil de tracking gratuit le plus puissant que tu as a disposition. Facebook Pixel te donne la vision Facebook. GA4 te donne la vision complete : tous les canaux, toutes les sources, tout le parcours client, de la premiere visite a l'achat.

Et la bonne nouvelle, c'est que CartFlows envoie automatiquement les events e-commerce a GA4. Tu n'as pas besoin de configurer du code custom ou de passer par Google Tag Manager — meme si c'est une option avancee qu'on verra plus tard.

---

**[SECTION 1 — Connecter GA4 a CartFlows]**

**[ECRAN — CartFlows > Settings > Google Analytics]**

Si tu n'as pas encore GA4 sur ton site, commence par creer un compte sur analytics.google.com. Cree une propriete, configure un flux de donnees Web, et recupere ton Measurement ID. C'est un code qui commence par "G-" suivi de caracteres alphanumeriques — par exemple G-ABC123DEF4.

Dans CartFlows, va dans Settings > Integrations (ou Google Analytics selon ta version). Colle ton Measurement ID dans le champ prevu. Active l'option e-commerce tracking. Sauvegarde.

A partir de ce moment, CartFlows va envoyer les events e-commerce standards a GA4 sur chaque page de tes funnels. Pas besoin de configuration supplementaire pour les events de base.

Si tu utilises deja un plugin GA4 sur ton site (MonsterInsights, Site Kit by Google, ou autre), verifie qu'il n'y a pas de doublon. Meme regle que pour le pixel Facebook : un seul point d'injection par page, sinon les donnees sont faussees.

---

**[SECTION 2 — Les events e-commerce automatiques]**

**[ECRAN — liste des events GA4 avec description]**

CartFlows declenche automatiquement les events e-commerce GA4 standards. Voici les principaux.

**begin_checkout** — Le visiteur arrive sur ta page de checkout. Il a lance le processus de paiement. C'est le debut de ton entonnoir transactionnel dans GA4.

**add_to_cart** — Le visiteur ajoute un produit a son panier. Selon ta configuration WooCommerce et CartFlows, cet event peut se declencher avant ou au moment du checkout.

**purchase** — Le paiement est confirme. Cet event remonte le montant de la transaction, l'identifiant de commande, et les produits achetes. C'est l'event le plus important pour mesurer ton chiffre d'affaires par canal.

**refund** — Si tu geres les remboursements dans WooCommerce, cet event permet a GA4 de soustraire les montants rembourses de tes rapports e-commerce. Tes chiffres refletent le CA reel, pas le brut.

Chaque event est associe a des parametres : le montant (value), la devise (currency), l'identifiant de transaction (transaction_id), et la liste des produits (items). GA4 utilise ces parametres pour construire ses rapports e-commerce.

---

**[SECTION 3 — Le rapport E-commerce purchases]**

**[ECRAN — GA4 > Reports > Monetization > Ecommerce purchases]**

Maintenant, on va lire les donnees. Dans GA4, va dans Reports > Monetization > Ecommerce purchases.

Ce rapport te montre, produit par produit : le nombre de fois ou le produit a ete vu, le nombre de fois ou il a ete ajoute au panier, le nombre d'achats, et le chiffre d'affaires genere.

C'est ici que tu identifies tes produits stars et tes produits qui ne convertissent pas. Si un produit est vu 500 fois mais achete 2 fois, tu as un probleme de conversion. Si un produit est peu vu mais converti a 15%, tu as une opportunite — envoie-lui plus de trafic.

Tu peux filtrer par periode, par segment d'audience, par source de trafic. Par exemple : quels produits les visiteurs Facebook achetent le plus ? Quels produits les visiteurs organiques preferent ? Ces informations guident tes decisions de contenu et de publicite.

---

**[SECTION 4 — Le rapport Checkout journey]**

**[ECRAN — GA4 > Reports > Monetization > Checkout journey]**

Le deuxieme rapport essentiel : Checkout journey. Il te montre le parcours du client a travers les etapes de ton checkout, sous forme d'entonnoir.

Tu vois combien de personnes arrivent sur le checkout, combien ajoutent leurs informations de livraison, combien passent au paiement, et combien finalisent l'achat. A chaque etape, tu vois le taux d'abandon.

C'est extremement precieux. Si 70% des visiteurs arrivent au checkout mais seulement 30% finalisent l'achat, tu perds 40% de tes acheteurs potentiels dans le processus. Le rapport te dit exactement ou ils decrochent.

Avec CartFlows, tu peux ensuite modifier la page ou le taux d'abandon est le plus eleve — simplifier un champ, ajouter un element de reassurance, reduire le temps de chargement — et mesurer l'impact de tes modifications.

---

**[SECTION 5 — Attribution : quel canal a genere la vente]**

**[ECRAN — GA4 > Advertising > Attribution paths]**

L'attribution, c'est la question la plus strategique : quel canal a reellement genere la vente ?

Un client peut voir ta pub Facebook le lundi, lire ton article de blog le mercredi, cliquer sur ta newsletter le vendredi, et acheter. Qui merite le credit ? Facebook pour la decouverte ? Le SEO pour la consideration ? L'email pour la conversion ?

GA4 propose plusieurs modeles d'attribution. Le modele par defaut, "data-driven", utilise le machine learning pour distribuer le credit entre les points de contact selon leur contribution reelle a la conversion.

Va dans Advertising > Attribution paths pour voir les chemins complets de conversion. Tu verras par exemple que 35% de tes clients passent par "Paid Social > Organic Search > Direct" — ce qui signifie que ta pub Facebook genere la notoriete, ton contenu SEO nourrit l'interet, et le client revient en direct pour acheter.

Sans cette vision, tu pourrais couper ta pub Facebook en pensant qu'elle ne convertit pas, alors qu'elle est le premier maillon de la chaine.

---

**[SECTION 6 — Conseil pratique]**

**[ECRAN — checklist "30 min GA4"]**

Un dernier conseil. GA4 est gratuit et bien plus puissant que ce que la plupart des gens imaginent. Mais il faut investir un minimum de temps pour le comprendre.

Prends 30 minutes cette semaine pour parcourir les rapports e-commerce de ton GA4. Regarde le rapport Ecommerce purchases, le Checkout journey, et les chemins d'attribution. Meme si les chiffres sont encore faibles, prends l'habitude de les consulter regulierement.

Les entrepreneurs qui reussissent ne sont pas ceux qui ont le meilleur produit. Ce sont ceux qui comprennent leurs chiffres et prennent des decisions basees sur les donnees.

---

**[OUTRO — face camera]**

GA4 est maintenant connecte a ton funnel CartFlows. Tu as les events e-commerce, les rapports de vente, le parcours checkout et l'attribution multi-canaux. Tout ca gratuitement.

Dans la prochaine lecon, on va voir les pixels Pinterest et Snapchat — pour ceux qui font de la pub sur ces plateformes.

---

## Notes de production

- **Visuels ECRAN** : CartFlows Settings (Measurement ID), liste events GA4 (tableau), rapport Ecommerce purchases (capture GA4), entonnoir Checkout journey, attribution paths, checklist 30 min
- **Ton** : Technique progressif, exemples concrets chiffres, insistance sur la gratuite de GA4
- **CTA fin** : Enchainer sur L7.4 (Pinterest et Snapchat Pixel)
- **Point attention montage** : Le rapport Checkout journey merite un zoom visuel detaille — c'est le rapport le plus actionnable
- **Mots-cles formation** : Google Analytics 4 CartFlows, events e-commerce GA4, checkout journey, attribution multi-canaux
