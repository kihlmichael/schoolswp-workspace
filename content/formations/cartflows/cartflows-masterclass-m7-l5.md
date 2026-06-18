# Lecon 7.5 - Tracking server-side vs client-side

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 7 - Tracking et Pixels
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre la difference entre tracking client-side et server-side, mesurer l'impact des adblockers sur les donnees, et savoir quand passer au server-side avec CartFlows et WordPress.

---

## Script narration

**[INTRO - face camera]**

Tout ce qu'on a configure jusqu'ici - Facebook Pixel, GA4, Pinterest Tag, Snapchat Pixel - fonctionne en mode client-side. Ca veut dire que le code de tracking s'execute dans le navigateur du visiteur.

Et ca pose un probleme de plus en plus important : les adblockers, les restrictions iOS, et les navigateurs qui bloquent les cookies tiers. Resultat : une partie de tes conversions est invisible. Tu fais des ventes, mais ton pixel ne les voit pas.

Dans cette lecon, on va comprendre pourquoi, mesurer l'impact, et voir les solutions.

---

**[SECTION 1 - Comment fonctionne le tracking client-side]**

**[ECRAN - schema client-side : navigateur → pixel → serveur plateforme]**

Le tracking client-side fonctionne comme ca. Quand un visiteur arrive sur ta page checkout, son navigateur charge le JavaScript du pixel. Ce script detecte l'action (page vue, achat, etc.) et envoie une requete au serveur de la plateforme - Facebook, Google, Pinterest.

C'est simple, ca marche depuis 15 ans, et c'est ce que 90% des sites utilisent. Le probleme, c'est que tout passe par le navigateur du visiteur. Et le navigateur, aujourd'hui, c'est un champ de bataille.

Les adblockers (uBlock Origin, Adblock Plus, et des dizaines d'autres) bloquent les requetes vers les domaines de tracking connus. Le script du pixel ne se charge meme pas, ou s'il se charge, la requete de conversion est bloquee.

iOS 14 et les versions suivantes ont introduit l'App Tracking Transparency. Sur Safari, l'Intelligent Tracking Prevention (ITP) supprime les cookies tiers et limite la duree des cookies first-party a 7 jours - voire 24 heures dans certains cas.

Firefox a son Enhanced Tracking Protection. Brave bloque tout par defaut.

---

**[SECTION 2 - L'impact chiffre : 20 a 30% de conversions invisibles]**

**[ECRAN - graphique : conversions reelles vs conversions reportees]**

Les etudes convergent : entre 20 et 30% des conversions ne sont pas reportees en tracking client-side. Sur certaines audiences tech-savvy, ca monte a 40%.

Concretement, si tu fais 100 ventes dans le mois, Facebook n'en voit que 70 a 80. Les 20 a 30 autres existent - l'argent est sur ton compte bancaire - mais elles ne sont pas attribuees a une campagne.

Les consequences sont serieuses. Facebook ne peut pas optimiser correctement tes campagnes si 25% des conversions lui sont cachees. Ton CPA affiche est artificiellement gongle - tu crois payer 40 euros par vente alors que le CPA reel est de 30. Tu risques de couper des campagnes rentables en pensant qu'elles ne le sont pas.

C'est un probleme qui s'aggrave chaque annee. Plus les navigateurs se durcissent, plus le tracking client-side perd en fiabilite.

---

**[SECTION 3 - Comment fonctionne le tracking server-side]**

**[ECRAN - schema server-side : navigateur → ton serveur → serveur plateforme]**

Le tracking server-side change l'architecture. Au lieu que le navigateur envoie les donnees directement a Facebook ou Google, c'est ton serveur qui le fait.

Le visiteur arrive sur ton checkout, la page se charge normalement. Mais au lieu de compter sur un script JavaScript dans le navigateur, ton serveur detecte l'action (achat confirme via WooCommerce, par exemple) et envoie la donnee directement a l'API de la plateforme.

Les adblockers ne peuvent pas bloquer ca. Ils bloquent les requetes du navigateur, pas les requetes de ton serveur. Le navigateur ne sait meme pas que le tracking a lieu. La conversion remonte a 100%.

Pour Facebook, ca s'appelle la Conversions API (CAPI). Pour Google, c'est le server-side tagging via Google Tag Manager server. Le principe est le meme : ton serveur envoie les donnees, pas le navigateur du visiteur.

---

**[SECTION 4 - Solutions server-side pour WordPress]**

**[ECRAN - logos PixelYourSite, WooCommerce, Google Tag Manager]**

Sur WordPress, tu as plusieurs options pour implementer le server-side.

**Facebook Conversions API** - Le plugin PixelYourSite Pro gere nativement la Conversions API. Tu connectes ton pixel, tu actives CAPI, et le plugin envoie les events de conversion directement depuis ton serveur WordPress. CartFlows est compatible - les events WooCommerce (commande confirmee, remboursement) sont remontes via l'API.

**Google server-side tagging** - Plus technique. Tu deploies un conteneur Google Tag Manager cote serveur (sur un sous-domaine ou un service cloud type Google Cloud Run). Les hits GA4 passent par ce serveur au lieu d'aller directement a Google. Ca necessite une configuration plus avancee, mais la precision de tracking est maximale.

**Plugins tout-en-un** - PixelYourSite est le plus populaire pour WordPress/WooCommerce. Il gere Facebook CAPI, Google server-side, Pinterest API, et TikTok API depuis un seul tableau de bord. L'integration avec CartFlows fonctionne via les hooks WooCommerce standards.

Un point important : le server-side ne remplace pas le client-side. Il le complete. La bonne pratique, c'est d'avoir les deux en parallele. Le client-side capture les visiteurs qui n'ont pas d'adblocker. Le server-side capture ceux qui en ont un. Les plateformes dedupliquent automatiquement pour eviter de compter une conversion deux fois.

---

**[SECTION 5 - Quand passer au server-side]**

**[ECRAN - seuil de decision : 500€/mois en pub]**

Mon conseil : configure d'abord le client-side. C'est ce qu'on a fait dans les lecons precedentes. Ca prend 5 minutes par pixel, c'est gratuit, et ca couvre 70 a 80% de tes conversions.

Passe au server-side quand tu depenses plus de 500 euros par mois en publicite. A ce niveau de budget, 20 a 30% de conversions invisibles represente un manque a gagner significatif en optimisation.

Si tu depenses 2000 euros par mois, le server-side n'est plus optionnel - c'est une necessite. La difference de precision entre 70% et 95% de conversions reportees impacte directement tes decisions d'allocation de budget.

L'investissement en temps : une demi-journee pour configurer PixelYourSite Pro avec CAPI. Une journee pour Google server-side tagging si tu n'es pas familier avec Google Cloud. C'est un investissement qui se rentabilise des le premier mois sur un budget pub serieux.

---

**[OUTRO - face camera]**

Le tracking client-side est ton point de depart. Le server-side est ton evolution naturelle quand tu montes en budget pub. Les deux ensemble te donnent la vision la plus precise possible de tes conversions.

Dans la prochaine lecon, on va aborder un sujet incontournable : le RGPD et le consentement cookies. Parce que tracker correctement, c'est aussi tracker legalement.

---

## Notes de production

- **Visuels ECRAN** : Schema client-side (3 etapes), graphique conversions reelles vs reportees, schema server-side (3 etapes), logos plugins, seuil decision 500€
- **Ton** : Technique accessible, chiffres concrets, progression logique (probleme → impact → solution → timing)
- **CTA fin** : Enchainer sur L7.6 (RGPD et consentement)
- **Point attention montage** : Les deux schemas (client-side vs server-side) doivent etre visuellement compares cote a cote
- **Mots-cles formation** : tracking server-side WordPress, Facebook Conversions API, adblockers impact, PixelYourSite CartFlows
