# Lecon 7.2 — Facebook Pixel : configurer les events

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 7 — Tracking et Pixels
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir creer un Facebook Pixel, le connecter a CartFlows, comprendre les events automatiques et tester avec le Pixel Helper. Configurer les conversions custom dans Ads Manager.

---

## Script narration

**[INTRO — face camera]**

Si tu fais de la publicite sur Facebook ou Instagram — ou si tu prevois d'en faire — le Facebook Pixel est ton outil de tracking numero un. C'est lui qui dit a Meta exactement ce que font tes visiteurs sur ton site, et surtout, quand ils achetent.

Sans pixel, Facebook ne sait pas si ta pub a genere des ventes. Tu paies pour des clics, mais tu n'as aucune visibilite sur les conversions. Avec le pixel, chaque vente est attribuee a la campagne qui l'a generee. Et Facebook utilise ces donnees pour optimiser la diffusion de tes pubs vers les personnes les plus susceptibles d'acheter.

On va configurer tout ca ensemble, etape par etape.

---

**[SECTION 1 — Creer ton pixel dans Business Manager]**

**[ECRAN — capture Facebook Business Manager > Events Manager]**

Premiere etape : creer le pixel. Va dans business.facebook.com, puis Events Manager dans le menu de gauche. Clique sur "Connecter des sources de donnees", selectionne "Web", puis "Pixel Meta".

Donne-lui un nom clair — par exemple "Pixel schoolsWP Vente" ou "Pixel MonSite Shop". Pas besoin de completer l'URL tout de suite.

Facebook va te proposer plusieurs methodes d'installation : code manuel, integration partenaire, ou envoi a un developpeur. On ne va utiliser aucune de ces options directement, parce que CartFlows gere l'integration nativement.

Ce qu'il te faut, c'est ton Pixel ID. C'est un numero a 15 chiffres que tu trouves dans les parametres de ton pixel. Copie-le. C'est la seule chose dont CartFlows a besoin.

---

**[SECTION 2 — Connecter le pixel a CartFlows]**

**[ECRAN — CartFlows > Settings > Facebook Pixel]**

Dans ton tableau de bord WordPress, va dans CartFlows > Settings. Tu vas trouver un onglet "Facebook Pixel" ou "Integrations" selon ta version.

Colle ton Pixel ID dans le champ prevu. Active l'option. Sauvegarde.

C'est tout. CartFlows va injecter le code du pixel sur toutes les pages de tes funnels automatiquement. Pas besoin de toucher au code, pas besoin d'ajouter des snippets dans le header. CartFlows gere l'injection proprement.

Un point important : si tu utilises deja un autre plugin pour le pixel (PixelYourSite, CAPI, ou autre), assure-toi de ne pas doubler l'installation. Deux pixels identiques sur la meme page = des donnees en double = des rapports faux. Un seul pixel par page, toujours.

---

**[SECTION 3 — Les events automatiques CartFlows]**

**[ECRAN — schema des events par etape du funnel]**

Quand le pixel est active, CartFlows declenche automatiquement des events Facebook standards a chaque etape de ton funnel. Voici ce qui se passe.

**PageView** — Declenche sur chaque page du funnel. C'est l'event de base : "quelqu'un a vu cette page."

**ViewContent** — Declenche sur ta page de vente ou ta landing page. Indique qu'un visiteur a vu ton offre.

**InitiateCheckout** — Declenche quand le visiteur arrive sur la page de checkout. Il a commence le processus d'achat.

**AddToCart** — Declenche quand le visiteur ajoute un produit au panier (selon ta configuration WooCommerce).

**Purchase** — Le plus important. Declenche quand le paiement est confirme. Cet event remonte le montant de la transaction a Facebook. C'est lui qui permet de calculer ton ROAS (retour sur investissement publicitaire).

CartFlows envoie aussi la valeur de la transaction avec l'event Purchase. Ca veut dire que dans Ads Manager, tu verras non seulement le nombre de ventes, mais aussi le chiffre d'affaires genere par chaque campagne.

---

**[SECTION 4 — Tester avec Facebook Pixel Helper]**

**[ECRAN — Chrome Web Store > Facebook Pixel Helper]**

Avant de lancer la moindre pub, tu dois verifier que ton pixel fonctionne correctement. L'outil officiel pour ca : Facebook Pixel Helper. C'est une extension gratuite pour Chrome.

Installe-la depuis le Chrome Web Store. Une fois activee, tu verras une petite icone dans ta barre d'outils. Visite chaque page de ton funnel et verifie que les bons events se declenchent.

Sur ta page de vente, tu dois voir PageView et ViewContent. Sur ton checkout, PageView et InitiateCheckout. Apres un achat test, Purchase avec le montant correct.

Si un event manque, verifie que le Pixel ID est correct dans CartFlows et qu'il n'y a pas de conflit avec un autre plugin de tracking. Si l'event se declenche deux fois, tu as probablement un doublon — desactive l'un des deux points d'injection.

---

**[SECTION 5 — Configurer les conversions custom dans Ads Manager]**

**[ECRAN — Facebook Ads Manager > Custom Conversions]**

Derniere etape : dire a Facebook quelles conversions tu veux optimiser. Dans Ads Manager, va dans "Conversions personnalisees" (Custom Conversions).

Cree une nouvelle conversion basee sur l'event Purchase. Tu peux aussi creer des conversions pour InitiateCheckout si tu veux mesurer les abandons de panier.

Quand tu crées une campagne Facebook Ads, selectionne "Conversions" comme objectif, et choisis ton event Purchase. Facebook va alors optimiser la diffusion vers les personnes les plus susceptibles d'acheter — pas juste de cliquer.

C'est la difference entre une campagne qui genere des clics a 50 centimes sans vente, et une campagne qui genere des ventes a 25 euros de CPA.

---

**[OUTRO — face camera]**

Ton pixel est installe, tes events sont en place, et tu as verifie que tout fonctionne. A partir de maintenant, chaque visite sur ton funnel, chaque etape du parcours, chaque achat — tout remonte dans Facebook.

Dans la prochaine lecon, on va configurer Google Analytics 4 pour avoir une vision encore plus complete de ton funnel.

---

## Notes de production

- **Visuels ECRAN** : Captures Business Manager (Events Manager, Pixel ID), CartFlows Settings (champ Pixel ID), schema events par etape, Chrome Pixel Helper en action, Ads Manager Custom Conversions
- **Ton** : Technique mais accessible, pas-a-pas sans jargon inutile
- **CTA fin** : Enchainer sur L7.3 (Google Analytics 4)
- **Point attention montage** : Insister visuellement sur le Pixel ID (15 chiffres) et le danger du doublon pixel
- **Mots-cles formation** : Facebook Pixel CartFlows, events e-commerce Meta, pixel helper test, conversions custom
