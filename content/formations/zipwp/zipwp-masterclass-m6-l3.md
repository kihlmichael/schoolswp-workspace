# Lecon 6.3 — ZipWP + SureForms + SureRank

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 6 — Ecosysteme et business
- **Lecon** : 3/10
- **Duree cible** : 8 min
- **Objectif pedagogique** : Configurer SureForms pour les formulaires et SureRank pour le SEO sur un site ZipWP — et savoir quand SureRank suffit vs quand passer a Rank Math.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Quand ZipWP genere un site, deux outils sont installes silencieusement en arriere-plan : SureForms pour les formulaires et SureRank pour le SEO. Ils sont la, ils fonctionnent, mais tu ne les as peut-etre pas configures correctement. Et une mauvaise config ici, c'est des formulaires qui n'arrivent nulle part et un SEO qui ne decolle pas.

On reprend ces deux outils depuis le debut. Configuration optimale, cas d'usage, et la vraie question : faut-il garder SureRank ou passer a Rank Math ?

---

[SECTION 1 — SureForms : formulaires natifs et legers]

SureForms est le plugin de formulaires de Brainstorm Force. Et son avantage principal : il est construit sur Gutenberg. Les formulaires sont des blocs, comme tout le reste de ton site. Pas de shortcode, pas d'iframe, pas de framework CSS supplementaire.

Ouvre SureForms dans le dashboard WordPress. Tu vas trouver les formulaires generes par ZipWP — generalement un formulaire de contact basique. Edite-le.

Les champs disponibles : texte, email, telephone, textarea, select (liste deroulante), checkbox, radio buttons, date, fichier upload. Tu as tout ce qu'il faut pour un formulaire de contact, un formulaire de devis, ou un formulaire d'inscription.

Configuration cle — les notifications. Va dans les reglages du formulaire, onglet "Notifications". Configure au minimum deux notifications : une pour toi (tu recois un email a chaque soumission) et une pour le visiteur (un email de confirmation automatique). Teste toujours en soumettant le formulaire toi-meme — verifie que les deux emails arrivent.

Configuration cle — les integrations. SureForms peut envoyer les donnees vers FluentCRM (ajouter un contact avec un tag), vers un webhook (envoyer les donnees a n'importe quel service), ou vers un service email externe. Si tu utilises FluentCRM, configure l'integration directement dans les reglages du formulaire — chaque soumission cree ou met a jour un contact.

Le design : puisque SureForms utilise des blocs Gutenberg, tu peux styliser les formulaires avec les memes outils que le reste de ton site. Couleurs, espacements, typographie — tout est coherent avec ton design Astra + Spectra.

---

[SECTION 2 — SureRank : SEO integre]

SureRank est le plugin SEO de la stack BSF. Il est installe par defaut sur les sites ZipWP et configure les bases du referencement.

Ce que SureRank gere : les meta titles et meta descriptions de chaque page et article. Le sitemap XML — genere automatiquement et soumis aux moteurs de recherche. Les balises OpenGraph pour le partage social. Les redirections 301 basiques. Le schema markup de base.

Configuration post-generation : ouvre chaque page de ton site ZipWP et verifie les meta titles et descriptions dans le panneau SureRank. ZipWP genere des meta automatiques, mais ils sont souvent trop generiques. Reecris-les en incluant ton mot-cle principal et une accroche claire. Le meta title doit faire entre 50 et 60 caracteres. La meta description entre 140 et 160 caracteres.

Active le sitemap : va dans SureRank → Settings → Sitemap. Verifie qu'il est actif et qu'il inclut tes pages et articles. Soumets l'URL du sitemap (tonsite.fr/sitemap.xml) dans Google Search Console.

Les reglages sociaux : configure les images et descriptions par defaut pour le partage Facebook et Twitter. Ca prend 5 minutes et ca evite les partages avec une image manquante ou un titre generique.

---

[SECTION 3 — SureRank vs Rank Math : quand changer]

La question que tout le monde pose : est-ce que SureRank suffit ou faut-il passer a Rank Math ?

SureRank suffit si : tu as un site vitrine avec 5-10 pages. Tu n'as pas besoin d'analyse SEO avancee. Tu veux garder ta stack 100% BSF. Tu debutes en SEO et tu veux rester dans la zone de confort.

Passe a Rank Math si : tu publies regulierement du contenu (blog, articles). Tu as besoin d'analyse de contenu en temps reel (scoring SEO pendant la redaction). Tu veux des fonctionnalites avancees : redirections massives, rich snippets multiples, local SEO, WooCommerce SEO, analytics integres. Tu es serieux sur le referencement et tu veux un outil complet.

La migration est facile : Rank Math inclut un outil d'importation qui reprend tous les meta titles, descriptions, et reglages de SureRank. Tu ne perds rien. Installe Rank Math, lance l'importation, desactive SureRank.

Chez schoolsWP, on utilise Rank Math. C'est l'outil le plus complet pour le SEO WordPress, et l'analyse de contenu en temps reel est indispensable quand tu publies regulierement. Mais si tu as un site vitrine de 5 pages, SureRank fait le travail.

---

[OUTRO]

SureForms et SureRank sont les deux utilitaires discrets de la stack ZipWP. Formulaires legers et natifs d'un cote, SEO de base de l'autre. Configure-les correctement des la generation, et ils travaillent en silence pour toi.

Si tu publies du contenu regulierement, envisage Rank Math — la migration est indolore et les fonctionnalites avancees valent le detour.

Dans la prochaine lecon, on attaque un comparatif detaille : SureCart vs WooCommerce. On va plus loin que ce qu'on a vu dans le module 5, avec un tableau complet pour t'aider a choisir definitivement.

---

## Notes de production

### Captures d'ecran suggerees

1. **SureForms editor** — Formulaire en edition dans Gutenberg avec les champs
2. **Notifications SureForms** — Configuration des emails de notification
3. **SureRank panneau** — Meta title et description dans l'editeur de page
4. **Sitemap SureRank** — Page de reglages sitemap
5. **Rank Math import** — Ecran d'importation depuis SureRank

### Transitions

- Intro → Section 1 : ouverture SureForms dans le dashboard WP
- Section 1 → Section 2 : transition vers SureRank, panneau SEO
- Section 2 → Section 3 : split screen SureRank vs Rank Math
- Section 3 → Outro : retour avatar, conseil final

### Notes HeyGen / ElevenLabs

- Ton tutoriel et methodique — deux outils a configurer, pas de diversion
- Section 1 (SureForms) : montrer les manipulations a l'ecran
- Section 3 (comparaison) : ton honnete et tranche, donner un avis clair
- Ne pas denigrer SureRank — c'est un bon outil pour son perimetre
