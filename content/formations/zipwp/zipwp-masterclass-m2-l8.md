# Lecon 2.8 - Performance : vitesse et Core Web Vitals

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 2 - Personnalisation avancee
- **Lecon** : 8/8
- **Duree cible** : 8 min
- **Objectif pedagogique** : Mesurer et ameliorer la vitesse d'un site genere par ZipWP - outils de mesure, optimisations concretes, Core Web Vitals expliques.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Un site rapide convertit mieux. C'est une realite mesuree - chaque seconde de chargement en plus, c'est des visiteurs qui partent. Google le sait, et c'est pour ca que la vitesse est un facteur de classement SEO depuis des annees. Les Core Web Vitals - les metriques de performance de Google - sont pris en compte dans le ranking.

La bonne nouvelle : la stack ZipWP (Astra + Spectra) est nativement legere. Tu pars d'une base saine. Mais quelques optimisations supplementaires peuvent faire la difference entre un score PageSpeed de 65 et un score de 90.

---

[SECTION 1 - Pourquoi la vitesse compte]

Trois raisons concretes.

Le SEO. Google utilise les Core Web Vitals comme signal de classement. Un site rapide a un avantage - modeste mais reel - sur un site lent. Sur des mots-cles concurrentiels, ca peut faire la difference entre la page 1 et la page 2.

La conversion. Amazon a mesure qu'une seconde de delai supplementaire leur couterait 1,6 milliard de dollars par an. Tu n'es pas Amazon, mais le principe s'applique a toutes les echelles. Un site qui charge en 2 secondes convertit mieux qu'un site qui charge en 5 secondes.

L'experience utilisateur. Un site lent est frustrant. Les gens sont habitues a la vitesse - Netflix, YouTube, Google chargent instantanement. Si ton site met 4 secondes a s'afficher, le visiteur est deja parti.

---

[SECTION 2 - L'avantage natif d'Astra et Spectra]

Astra est l'un des themes WordPress les plus legers du marche. Le theme de base pese moins de 50 Ko et n'ajoute quasiment aucune requete HTTP supplementaire. C'est un avantage considerable par rapport a des themes lourds comme Divi ou Avada.

Spectra, etant base sur Gutenberg, ne charge pas de framework JavaScript supplementaire. Pas de jQuery custom, pas de runtime lourd. Les blocs Spectra generent du HTML propre et du CSS minimal.

SureForms est aussi concu pour la performance - pas de scripts externes charges inutilement, le JavaScript ne se charge que sur les pages qui contiennent un formulaire.

En resume : tu pars d'une base optimisee. Le gros du travail de performance est deja fait par la stack. Ce qui reste, c'est d'eviter de degrader cette base avec de mauvaises pratiques.

---

[SECTION 3 - Mesurer la performance]

Avant d'optimiser, mesure. Deux outils gratuits suffisent.

PageSpeed Insights - pagespeed.web.dev. Tu entres l'URL de ton site et Google analyse la performance sur desktop et mobile. Tu obtiens un score de 0 a 100 et des recommandations detaillees. Vise 80+ sur mobile - c'est un bon objectif realiste.

GTmetrix - gtmetrix.com. Plus detaille que PageSpeed, avec un waterfall qui montre chaque requete HTTP, son poids et sa duree. Utile pour identifier les ressources qui ralentissent le chargement.

Teste la page d'accueil en priorite - c'est la page la plus visitee. Puis teste les pages cles : services, contact, les pages qui recoivent du trafic SEO.

Note ton score initial avant toute optimisation. Tu pourras mesurer l'impact de chaque changement.

---

[SECTION 4 - Les optimisations concretes]

Voici les optimisations qui ont le plus d'impact, classees par priorite.

Optimisation 1 : compression des images. On l'a vu dans la lecon 2.5 - c'est souvent le levier le plus puissant. Des images non compressees peuvent representer 80% du poids de la page. Imagify ou ShortPixel gerent ca automatiquement apres installation.

Optimisation 2 : le cache. Un plugin de cache stocke les pages generees en version statique - le serveur n'a pas besoin de reconstruire la page a chaque visite. Installe un plugin de cache : LiteSpeed Cache (si ton hebergeur est LiteSpeed), WP Super Cache, ou W3 Total Cache. Configure-le et tu verras une amelioration immediate.

Optimisation 3 : limiter les plugins. Chaque plugin ajoute du code - CSS, JavaScript, parfois des requetes externes. Le site genere par ZipWP inclut Astra, Spectra, SureForms, SureRank. C'est suffisant pour demarrer. N'ajoute un plugin que si tu en as vraiment besoin, et desactive ceux que tu n'utilises pas.

Optimisation 4 : le lazy loading. Deja actif par defaut dans WordPress pour les images. Verifie qu'il fonctionne - les images en bas de page ne doivent se charger que quand tu scrolles. Spectra ajoute aussi le lazy loading sur les videos embarquees.

Optimisation 5 : minification CSS et JS. Le plugin de cache que tu installes propose generalement la minification - fusionner et compresser les fichiers CSS et JavaScript. Active cette option. Attention : teste le site apres activation, car la minification peut parfois casser des scripts.

---

[SECTION 5 - Core Web Vitals : ce que ca veut dire]

Google mesure trois metriques principales pour evaluer l'experience utilisateur de ton site.

LCP - Largest Contentful Paint. C'est le temps que met le plus gros element visible (souvent l'image hero ou le titre principal) a s'afficher. Objectif : moins de 2,5 secondes. Pour ameliorer le LCP : optimise l'image hero (c'est souvent le coupable), utilise le preload pour les ressources critiques, et active le cache.

INP - Interaction to Next Paint. C'est le delai entre le moment ou un visiteur clique sur un element (bouton, lien, formulaire) et le moment ou le navigateur reagit visuellement. Objectif : moins de 200 millisecondes. La stack Astra + Spectra est legere, donc l'INP est rarement un probleme - sauf si tu ajoutes beaucoup de scripts tiers (analytics, chatbots, popups).

CLS - Cumulative Layout Shift. C'est le deplacement inattendu des elements pendant le chargement - quand tu commences a lire et que le texte saute parce qu'une image se charge au-dessus. Objectif : moins de 0,1. Pour ameliorer le CLS : definis des dimensions fixes pour les images et les iframes, et evite d'inserer du contenu dynamique au-dessus du contenu visible.

Tu peux voir les Core Web Vitals de ton site dans PageSpeed Insights et dans la Google Search Console (section "Experience").

---

[OUTRO]

Un site rapide, c'est un site qui convertit mieux et qui se classe mieux dans Google. La stack ZipWP te donne une base saine - Astra et Spectra sont parmi les outils les plus performants du marche WordPress.

Ton travail : compresser les images, installer un plugin de cache, limiter les plugins, et verifier les Core Web Vitals. Vise un score PageSpeed de 80+ sur mobile. C'est atteignable avec ces optimisations.

C'est la fin du module 2. Tu as maintenant un site genere, personnalise, responsive et performant. Dans le module 3, on passe a la couche business - le SEO, les funnels, l'email marketing - pour transformer ce site en un outil de generation de leads et de ventes.

---

## Notes de production

### Captures d'ecran suggerees

1. **PageSpeed Insights** - Score d'un site ZipWP (desktop et mobile)
2. **GTmetrix waterfall** - Vue detaillee des requetes HTTP
3. **Plugin de cache** - Interface de LiteSpeed Cache ou WP Super Cache
4. **Imagify** - Dashboard avec les images compressees
5. **Core Web Vitals** - Schema des 3 metriques (LCP, INP, CLS) avec les seuils
6. **Google Search Console** - Section Experience avec les Core Web Vitals

### Transitions

- Intro → Section 1 : statistiques de vitesse sur fond sombre
- Section 3 : ouverture de PageSpeed Insights et GTmetrix
- Section 4 : screencasts des optimisations (compression, cache, plugins)
- Section 5 : schema visuel des 3 Core Web Vitals
- Outro : retour avatar, ton de synthese, teaser module 3

### Notes HeyGen / ElevenLabs

- Ton technique mais accessible - pas de jargon sans explication
- "Un site rapide convertit mieux" : articuler, c'est le message cle
- Section 5 (Core Web Vitals) : ralentir, acronymes a bien prononcer
- LCP : "Largest Contentful Paint" - epeler clairement
- INP : "Interaction to Next Paint" - idem
- CLS : "Cumulative Layout Shift" - idem
- Outro : ton motivant et fier - "c'est la fin du module 2, bravo"
