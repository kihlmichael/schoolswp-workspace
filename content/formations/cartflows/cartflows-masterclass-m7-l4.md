# Lecon 7.4 - Pinterest et Snapchat Pixel

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 7 - Tracking et Pixels
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir quand configurer les pixels Pinterest et Snapchat, les installer dans CartFlows, et comprendre pourquoi il ne faut pas installer des pixels inutiles.

---

## Script narration

**[INTRO - face camera]**

Facebook et Google, c'est fait. Maintenant, on va voir deux pixels supplementaires que CartFlows supporte nativement : Pinterest Tag et Snapchat Pixel.

Mais avant de te montrer la configuration, un conseil direct : ne configure que les pixels des plateformes ou tu fais de la publicite. Les autres polluent ton site pour rien. Chaque pixel ajoute du code JavaScript, ralentit le chargement de tes pages, et cree des requetes reseau supplementaires. Si tu ne fais pas de pub Pinterest, le Pinterest Tag n'a rien a faire sur ton site.

Ceci etant dit, si tu fais de la pub sur ces plateformes, le tracking est indispensable. Voici comment le mettre en place.

---

**[SECTION 1 - Pinterest Tag : pour les niches visuelles]**

**[ECRAN - Pinterest Ads Manager > Conversions > Create Tag]**

Le Pinterest Tag est le pixel de conversion de Pinterest. Il fonctionne exactement comme le Facebook Pixel : tu le poses sur ton site, et il remonte les actions des visiteurs a Pinterest pour que la plateforme puisse optimiser la diffusion de tes epingles sponsorisees.

Pinterest est particulierement pertinent pour certaines niches. Si tu vends dans la decoration, la mode, la cuisine, le DIY, le mariage, le fitness, ou tout sujet visuel - Pinterest est un canal d'acquisition a prendre au serieux. Les utilisateurs Pinterest sont en mode decouverte et achat. L'intention commerciale y est naturellement plus elevee que sur d'autres reseaux.

Pour creer ton tag, va dans Pinterest Ads Manager > Conversions > Create Tag. Pinterest va te donner un Tag ID - un numero a 13 chiffres.

Dans CartFlows, va dans Settings > Integrations (ou Pinterest selon ta version). Colle ton Tag ID. Active. Sauvegarde. C'est la meme logique que pour Facebook : CartFlows injecte le code automatiquement sur les pages de tes funnels.

Les events remontes sont similaires : page view, checkout, purchase. Pinterest les utilise pour optimiser tes campagnes vers les conversions, pas juste les clics.

---

**[SECTION 2 - Snapchat Pixel : pour les audiences jeunes]**

**[ECRAN - Snapchat Ads Manager > Snap Pixel]**

Le Snapchat Pixel cible un segment specifique : les 18-35 ans. Si ton audience est majoritairement dans cette tranche d'age et que tu fais de la publicite sur Snapchat, ce pixel est pertinent.

La configuration est identique. Dans Snapchat Ads Manager, va dans Events Manager > Snap Pixel. Cree ton pixel et recupere le Pixel ID.

Dans CartFlows, colle l'ID dans le champ dedie, active, sauvegarde. Les events e-commerce sont remontes automatiquement : page view, initiate checkout, purchase.

Snapchat utilise ces donnees pour optimiser la diffusion de tes pubs et pour creer des audiences similaires (lookalike) basees sur tes acheteurs reels. Plus le pixel collecte de donnees de conversion, meilleure est l'optimisation.

---

**[SECTION 3 - Quand ca vaut le coup (et quand ca n'en vaut pas)]**

**[ECRAN - arbre de decision : installer le pixel ou non]**

Voici la regle simple pour decider si tu dois installer un pixel.

Tu fais de la publicite payante sur cette plateforme ? Oui → installe le pixel. Non → ne l'installe pas.

Tu prevois de faire de la pub sur cette plateforme dans les 30 prochains jours ? Oui → installe le pixel maintenant pour qu'il commence a collecter des donnees. Non → attends.

Il n'y a aucun benefice a installer un pixel si tu ne fais pas de pub sur la plateforme correspondante. Le pixel ne t'apporte rien en organique. Il ne booste pas ton referencement. Il ne te donne pas de donnees utiles si tu n'as pas de campagnes a optimiser.

En revanche, chaque pixel inutile a un cout : du JavaScript supplementaire qui ralentit tes pages, des requetes reseau vers des serveurs tiers, et potentiellement des problemes de consentement RGPD a gerer. Plus tu as de pixels, plus ton bandeau cookies est complexe.

---

**[SECTION 4 - Configuration propre : la checklist]**

**[ECRAN - checklist installation pixels]**

Avant de passer a la suite, voici la checklist pour une configuration propre de tes pixels.

Un seul point d'injection par pixel. Si CartFlows gere le pixel, desactive-le dans tout autre plugin (PixelYourSite, Insert Headers and Footers, etc.).

Teste chaque pixel apres installation. Pour Facebook, utilise le Pixel Helper. Pour Pinterest, utilise le Pinterest Tag Helper (extension Chrome). Pour Snapchat, utilise le mode test dans le Ads Manager.

Note quelque part les pixels installes sur ton site, avec le nom, l'ID, et la date d'installation. Quand tu arretes une campagne sur une plateforme, desactive le pixel correspondant.

Un site rapide avec 2 pixels utiles vaut mieux qu'un site lent avec 5 pixels dont 3 ne servent a rien.

---

**[OUTRO - face camera]**

Pinterest Tag et Snapchat Pixel sont en place - si tu en as besoin. Rappelle-toi : le tracking doit servir tes decisions, pas alourdir ton site.

Dans la prochaine lecon, on va aborder un sujet technique important : la difference entre le tracking client-side et server-side, et pourquoi ca impacte directement la precision de tes donnees.

---

## Notes de production

- **Visuels ECRAN** : Pinterest Ads Manager (Tag creation), Snapchat Ads Manager (Pixel creation), CartFlows Settings (champs Pinterest/Snapchat), arbre de decision oui/non, checklist installation
- **Ton** : Pragmatique, anti-bloat, insistance sur "seulement si tu en as besoin"
- **CTA fin** : Enchainer sur L7.5 (server-side vs client-side)
- **Point attention montage** : L'arbre de decision doit rester affiche pendant toute la section 3
- **Mots-cles formation** : Pinterest Tag CartFlows, Snapchat Pixel WordPress, tracking multi-plateforme, pixels e-commerce
