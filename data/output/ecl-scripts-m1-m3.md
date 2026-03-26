# Scripts video — Modules 1 a 3 : Decouverte, installation, configuration

**Formation** : Maitriser Easy Content Linker
**Modules** : M1 a M3
**Lecons** : 10 videos + 3 quiz
**Duree totale** : ~72 min de video
**Date** : 2026-03-23

---

## Module 1 — Le maillage interne et Easy Content Linker

---

### Lecon 1.1 — Pourquoi le maillage interne change ton SEO

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides pour la theorie, schema visuel du maillage

---

**[INTRO — face camera]**

Tu publies des articles regulierement, mais Google ne les classe pas comme tu voudrais ? Il y a un levier que la plupart des blogueurs WordPress negligent : le maillage interne. Dans cette lecon, je t'explique pourquoi c'est aussi important que le contenu lui-meme.

**[ECRAN — slide "C'est quoi le maillage interne ?"]**

Le maillage interne, c'est l'ensemble des liens qui relient tes pages entre elles a l'interieur de ton site. Pas les liens vers d'autres sites. Les liens internes, de toi a toi.

Chaque lien interne dit a Google : "cette page est liee a celle-la, va la voir aussi." C'est un signal de pertinence et de hierarchie.

**[ECRAN — schema visuel : 5 articles relies par des fleches]**

Regarde ce schema. A gauche, un site sans maillage. Cinq articles isoles. Google les crawle un par un, sans comprendre leur relation.

A droite, les memes cinq articles avec des liens internes. Google comprend immediatement que ces articles forment un cluster autour d'un meme sujet. Il donne plus de poids a l'article central.

**[ECRAN — slide "Les 4 benefices du maillage interne"]**

Premier benefice : la distribution du jus de lien. Quand une page recoit un backlink externe, elle accumule de l'autorite. Les liens internes distribuent cette autorite vers tes autres pages. Sans maillage, l'autorite reste bloquee sur une seule page.

Deuxieme benefice : le crawl budget. Google n'a pas un temps infini pour explorer ton site. Les liens internes guident ses robots vers tes pages importantes. Moins de pages orphelines, plus de pages indexees.

Troisieme benefice : l'experience utilisateur. Un visiteur qui lit un article sur les LMS WordPress veut peut-etre comparer TutorLMS et LearnDash. Un lien interne bien place l'emmene vers cet article sans qu'il doive chercher.

Quatrieme benefice : le temps passe sur le site. Plus un visiteur navigue de page en page, plus Google considere que ton site est utile. Le maillage interne augmente naturellement le nombre de pages vues par session.

**[ECRAN — slide "Le probleme : c'est long a faire"]**

Le souci, c'est que le maillage interne manuel est penible. Pour chaque article, tu dois trouver les articles lies, choisir une ancre naturelle dans le texte, inserer le lien, verifier que tu n'en mets pas trop.

Sur un site de 50 articles, ca prend facilement 1 a 2 heures par article. Sur 200 articles, c'est tout simplement irealiste a la main.

C'est exactement le probleme que resout Easy Content Linker.

**[TRANSITION — face camera]**

Tu comprends maintenant pourquoi le maillage interne est un levier SEO majeur. Dans la prochaine lecon, je te presente Easy Content Linker et comment il automatise tout ca.

---

**Points cles** :
- Le maillage interne distribue le jus de lien, guide le crawl, ameliore l'UX et augmente le temps sur le site
- Sans maillage, tes articles sont des iles isolees pour Google
- Le maillage manuel est trop lent pour les sites de 50+ articles
- Easy Content Linker automatise ce processus avec l'IA

**Mots cles SEO** : maillage interne WordPress, liens internes SEO, jus de lien, crawl budget

---

### Lecon 1.2 — Ce que fait Easy Content Linker (et ce qu'il ne fait pas)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides explicatives, screencast rapide du dashboard

---

**[INTRO — face camera]**

Easy Content Linker est un plugin WordPress qui automatise le maillage interne avec l'intelligence artificielle. Mais pour eviter les malentendus, je vais t'expliquer ce qu'il fait vraiment, et surtout ce qu'il ne fait pas.

**[ECRAN — slide "Comment ca marche — les 3 etapes"]**

ECL fonctionne en trois etapes.

Etape 1 : l'analyse semantique. Le plugin envoie le contenu de chaque article a OpenAI pour creer ce qu'on appelle un embedding. C'est une empreinte numerique qui represente le sens de ton article. Pas les mots-cles, le sens. Deux articles sur le meme sujet auront des embeddings proches, meme s'ils n'utilisent pas les memes mots.

Etape 2 : le matching. ECL compare les embeddings de tous tes articles et identifie les paires les plus similaires. Chaque paire recoit un score de similarite entre 0 et 1. Plus le score est proche de 1, plus les articles sont lies thematiquement.

Etape 3 : la selection d'ancre. Pour chaque lien a creer, GPT analyse le texte de l'article source et trouve une phrase existante qui peut servir d'ancre naturelle. Il ne genere pas de nouveau texte. Il repere une phrase deja presente dans ton article.

**[ECRAN — slide "Architecture reversible"]**

Le point le plus important a comprendre : ECL ne modifie jamais ta base de donnees.

Les liens sont injectes dynamiquement au moment ou la page s'affiche. C'est un filtre WordPress qui ajoute les liens a la volee. Ton contenu original reste intact.

Si tu desactives le plugin, tous les liens disparaissent instantanement. Si tu supprimes un lien depuis l'historique, il disparait au prochain chargement de page. Zero risque, 100% reversible.

**[ECRAN — screencast rapide du dashboard ECL]**

[Montre le menu Content Linker dans WordPress]

Voici l'interface. Tu as le Dashboard avec les statistiques, l'Historique de tous les liens crees, les Reglages pour la configuration, et les Pages strategiques pour booster tes pages importantes.

[Montre un lien dans l'historique]

Chaque lien affiche l'article source, l'article cible, l'ancre choisie par l'IA, le score de similarite et la date de creation.

**[ECRAN — slide "Ce que ECL ne fait PAS"]**

Soyons clairs sur les limites.

ECL ne cree pas de contenu. Il ne genere pas d'articles, pas de paragraphes, pas de phrases. Il utilise uniquement le texte qui existe deja.

ECL ne remplace pas ta strategie de contenu. Si tes articles ne sont pas lies thematiquement, le plugin ne pourra pas creer de liens pertinents. Il faut d'abord avoir du contenu de qualite sur des sujets complementaires.

ECL ne gere pas les liens externes. Il ne cree pas de liens vers d'autres sites. C'est un outil de maillage interne uniquement.

**[TRANSITION — face camera]**

Tu sais maintenant comment fonctionne Easy Content Linker. Dans la prochaine lecon, on compare la version Lite et la version Pro pour que tu choisisses celle qui te convient.

---

**Points cles** :
- ECL utilise les embeddings OpenAI pour l'analyse semantique et GPT pour la selection d'ancres
- Architecture 100% reversible : aucune modification en base de donnees
- Le plugin trouve des phrases existantes comme ancres, il ne genere pas de nouveau contenu
- Ce n'est pas un outil de creation de contenu ni de gestion de liens externes

**Mots cles SEO** : Easy Content Linker, plugin maillage interne automatique WordPress, liens internes IA

---

### Lecon 1.3 — Lite vs Pro : le comparatif honnete pour choisir

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides tableau comparatif, arbre de decision

---

**[INTRO — face camera]**

Easy Content Linker existe en version gratuite et en version payante. La question classique : est-ce que la version Lite suffit, ou faut-il passer au Pro ? Je te donne une reponse honnete avec un arbre de decision.

**[ECRAN — slide tableau comparatif]**

Voici ce que tu as dans chaque version.

Analyse semantique par embeddings : disponible dans les deux versions.

Detection des opportunites de maillage : disponible dans les deux versions.

Suggestions d'ancres par GPT : disponible dans les deux versions.

Export CSV des recommandations : disponible dans les deux versions.

Nombre d'articles : illimite en Lite et en Pro.

Maintenant, ce qui change.

Injection automatique des liens : uniquement en Pro. En Lite, tu recois des recommandations et tu ajoutes les liens manuellement.

Pages strategiques avec boost : uniquement en Pro.

Detection de doublons : uniquement en Pro.

Mode silo par categorie : uniquement en Pro.

Ancres personnalisees par page : uniquement en Pro.

Exclusions granulaires par article : uniquement en Pro.

Support prioritaire : uniquement en Pro.

**[ECRAN — slide "Combien ca coute ?"]**

La version Lite est gratuite, sans limite d'articles. Tu paies uniquement les appels API OpenAI.

La version Pro demarre a 50 euros par an pour un site. 99 euros par an pour 3 sites. 199 euros par an pour 10 sites. Plus les appels API OpenAI.

Important : dans les deux cas, tu dois avoir un compte OpenAI avec du credit. Le cout API est generalement de 3 a 8 euros pour 100 liens.

**[ECRAN — slide "Arbre de decision"]**

Tu as moins de 30 articles ? Commence par la Lite. Les recommandations manuelles sont gereables a cette taille. Tu testes le plugin, tu vois la qualite des suggestions, et tu decides ensuite.

Tu as entre 30 et 100 articles ? La Lite reste utilisable, mais l'injection automatique du Pro te fait gagner un temps enorme. C'est le moment ou le passage au Pro devient rentable.

Tu as plus de 100 articles ? Le Pro s'impose. Ajouter manuellement des liens sur 100 articles, c'est des heures de travail. L'automatisation du Pro te fait economiser ce temps.

Tu geres plusieurs sites ? Le plan Growth a 99 euros pour 3 sites ou Agency a 199 euros pour 10 sites devient tres rentable.

**[TRANSITION — face camera]**

Tu sais maintenant quelle version te convient. La bonne nouvelle, c'est que le passage de Lite a Pro est transparent. Tes embeddings et tes recommandations sont conservees. On passe a l'installation dans le module suivant.

---

**Points cles** :
- Lite : recommandations manuelles, gratuit, illimite en articles
- Pro : injection automatique, pages strategiques, detection doublons, silos
- Prix Pro : 50€/an (1 site), 99€/an (3 sites), 199€/an (10 sites)
- Plus API OpenAI (~3-8€ pour 100 liens) dans les deux versions
- Moins de 30 articles : Lite suffit. Plus de 100 articles : Pro s'impose

**Mots cles SEO** : Easy Content Linker gratuit, Easy Content Linker Pro prix, plugin maillage interne WordPress gratuit

---

### Lecon 1.4 — Quiz M1

**Duree** : 5 min
**Type** : Quiz TutorLMS (5 questions QCM)
**Voir plan de formation pour les questions**

---

## Module 2 — Installation et connexion API

---

### Lecon 2.1 — Installe Easy Content Linker sur ton site

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro, screencast complet pour la demo

---

**[INTRO — face camera]**

On passe a la pratique. Dans cette lecon, tu installes Easy Content Linker sur ton site WordPress. Que tu choisisses la version Lite ou Pro, je te montre les deux methodes.

**[ECRAN — screencast WordPress admin]**

**Methode 1 : installer la version Lite depuis WordPress.org.**

[Montre le menu Extensions > Ajouter]

Va dans Extensions, puis Ajouter une extension. Dans la barre de recherche, tape "Easy Content Linker".

[Montre le resultat de recherche]

Tu devrais voir "Easy Content Linker Lite" par Baptiste Guiraud. Clique sur Installer, puis sur Activer.

[Montre le nouveau menu "Content Linker" dans la barre laterale]

C'est fait. Tu as un nouveau menu "Content Linker" dans ta barre laterale WordPress. On y reviendra dans une minute.

**Methode 2 : installer la version Pro depuis le fichier zip.**

[Montre Extensions > Ajouter > Telecharger une extension]

Si tu as achete la version Pro sur easycontentlinker.com, tu as recu un fichier zip par email ou dans ton espace Freemius. Va dans Extensions, Ajouter, puis clique sur "Telecharger une extension".

[Montre le bouton "Parcourir" et la selection du fichier]

Selectionne le fichier zip. Clique sur Installer.

[Montre l'activation]

Une fois installe, clique sur Activer. Le menu "Content Linker" apparait dans la barre laterale.

Si tu avais deja la version Lite installee, le Pro la remplace automatiquement. Tes donnees sont conservees.

**[ECRAN — screencast du menu Content Linker]**

[Clique sur Content Linker]

Le menu contient quatre sections. Dashboard, c'est ta vue d'ensemble. Historique, c'est la liste de tous tes liens. Reglages, c'est la configuration du plugin. Et Pages strategiques, pour booster tes pages importantes.

Pour l'instant, tout est vide. C'est normal. On va configurer la connexion API dans la prochaine lecon.

**[TRANSITION — face camera]**

Le plugin est installe. Prochaine etape : connecter ta cle API OpenAI pour que l'IA puisse analyser tes articles.

---

**Points cles** :
- Lite : installation depuis WordPress.org en 1 clic
- Pro : upload du fichier zip depuis Freemius
- Le Pro remplace la Lite automatiquement, sans perte de donnees
- Quatre sections : Dashboard, Historique, Reglages, Pages strategiques

**Mots cles SEO** : installer Easy Content Linker, installation plugin WordPress

---

### Lecon 2.2 — Cree ta cle API OpenAI et configure ton budget

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast platform.openai.com

---

**[INTRO — face camera]**

Easy Content Linker a besoin d'une cle API OpenAI pour fonctionner. Si tu n'en as jamais cree une, pas de panique. Je te montre tout, etape par etape. Et surtout, je te montre comment configurer un budget pour eviter les mauvaises surprises.

**[ECRAN — screencast platform.openai.com]**

Premiere chose importante : on va sur platform.openai.com. Pas sur chatgpt.com. C'est une erreur frequente. La plateforme API et ChatGPT sont deux interfaces differentes.

[Montre la page de connexion]

Si tu n'as pas de compte, clique sur "Sign up" et suis les etapes. Si tu as deja un compte ChatGPT, tu peux utiliser les memes identifiants.

[Montre le dashboard API]

Une fois connecte, tu arrives sur le dashboard. C'est ici que tu geres tes cles API, ton credit et tes limites.

**[ECRAN — section API Keys]**

[Navigue vers API Keys dans le menu lateral]

Clique sur API Keys dans le menu a gauche. Puis sur "Create new secret key".

[Montre la creation de cle]

Donne un nom a ta cle. Par exemple "Easy Content Linker". Clique sur Create.

[Montre la cle generee]

Ta cle commence par "sk-". Copie-la immediatement et colle-la dans un endroit sur, parce qu'elle ne sera plus affichee apres. Un gestionnaire de mots de passe, c'est l'ideal.

Ne partage jamais cette cle. Ne la mets pas dans un fichier public. Elle donne acces a ton compte OpenAI.

**[ECRAN — section Billing]**

[Navigue vers Settings > Billing]

Avant de coller cette cle dans ECL, on va configurer le budget. C'est essentiel.

[Montre "Add payment method"]

Si tu n'as pas encore de moyen de paiement, ajoute une carte. Sans ca, la cle ne fonctionnera pas — tu auras une erreur "Insufficient quota".

[Montre "Set monthly budget limit"]

Maintenant, configure un plafond mensuel. Je recommande de commencer a 10 euros. C'est largement suffisant pour un premier maillage de 50 a 150 liens.

[Montre la section "Usage limits"]

Tu peux aussi configurer une alerte par email. Par exemple, recevoir un email quand tu atteins 80% de ton budget. Ca te laisse le temps de reagir avant d'atteindre la limite.

**[ECRAN — slide "Combien ca coute concretement ?"]**

Pour te donner des reperes concrets :

50 liens : entre 1,50 et 4 euros
100 liens : entre 3 et 8 euros
200 liens : entre 6 et 15 euros
500 liens : entre 15 et 35 euros

Ces fourchettes varient selon le modele GPT choisi et la longueur de tes articles. Avec gpt-4o, tu es dans le bas de la fourchette.

Les embeddings sont le cout le plus faible. Ils sont calcules une seule fois par article. Si tu relances le traitement plus tard, seuls les nouveaux articles seront analyses.

**[TRANSITION — face camera]**

Ta cle est creee, ton budget est configure. Dans la prochaine lecon, on connecte tout ca dans Easy Content Linker et on choisit les bons modeles.

---

**Points cles** :
- Aller sur platform.openai.com, pas chatgpt.com
- La cle API commence par "sk-" — la copier immediatement, elle n'est affichee qu'une fois
- Ajouter un moyen de paiement obligatoire
- Configurer un budget mensuel (10€ pour commencer) et une alerte a 80%
- Cout moyen : 3-8€ pour 100 liens

**Mots cles SEO** : cle API OpenAI WordPress, cout API OpenAI, budget OpenAI plugin

---

### Lecon 2.3 — Connecte la cle API et choisis le bon modele

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des reglages ECL

---

**[INTRO — face camera]**

Tu as ta cle API OpenAI et ton budget est configure. Maintenant, on va coller cette cle dans Easy Content Linker et choisir les modeles qui conviennent a ton site.

**[ECRAN — screencast Content Linker > Reglages]**

[Navigue vers Content Linker > Reglages]

Dans les reglages, la premiere section concerne l'API OpenAI.

[Montre le champ "Cle API"]

Colle ta cle ici. Celle qui commence par "sk-".

[Montre le bouton "Sauvegarder et tester la cle"]

Clique sur "Sauvegarder et tester la cle". Si tout est bon, tu vois un message de confirmation vert.

[Montre un message de succes]

Parfait, la connexion fonctionne.

**[ECRAN — slide "Que faire si le test echoue ?"]**

Si le test echoue, voici les causes les plus frequentes.

"Invalid API key" : ta cle est mal copiee. Verifie qu'il n'y a pas d'espace avant ou apres. Regenere-en une nouvelle si necessaire.

"Insufficient quota" : ton compte OpenAI n'a pas de credit. Verifie que tu as ajoute un moyen de paiement et que ton budget mensuel n'est pas epuise.

"Rate limit exceeded" : tu as trop de requetes en cours. Attends quelques secondes et reessaie.

"Connection error" : ton hebergeur bloque peut-etre les appels sortants vers l'API OpenAI. Contacte ton hebergeur pour verifier.

**[ECRAN — screencast section "Modeles"]**

[Montre les menus deroulants des modeles]

ECL utilise deux types de modeles differents.

Le modele d'embeddings sert a analyser le contenu semantique de chaque article. Tu as deux choix.

text-embedding-3-small : c'est le modele recommande. Il est rapide, peu couteux, et suffisant pour 90% des sites. C'est celui que je te conseille.

text-embedding-3-large : plus precis, mais plus cher. Utile si tu as un site de plus de 500 articles dans plusieurs langues.

Le modele GPT sert a choisir les ancres dans le texte. Tu as deux choix.

gpt-4o : c'est le modele recommande. Meilleur rapport qualite-prix. Il trouve des ancres naturelles et pertinentes dans la grande majorite des cas.

gpt-5.2 : plus precis, mais deux a trois fois plus cher. Reserve aux sites ou la qualite des ancres est critique — par exemple un site editorial professionnel.

[Selectionne text-embedding-3-small et gpt-4o]

Pour ton premier maillage, je recommande text-embedding-3-small et gpt-4o. Tu pourras toujours changer de modele plus tard si les resultats ne te satisfont pas.

**[ECRAN — screencast section "Langue"]**

[Montre le menu deroulant de la langue]

Selectionne la langue de ton site. ECL adapte ses prompts pour trouver des ancres naturelles dans ta langue. Si ton site est en francais, selectionne Francais. C'est important pour la qualite des ancres.

**[TRANSITION — face camera]**

La connexion est faite, les modeles sont choisis. Ton Easy Content Linker est pret a fonctionner. Dans le prochain module, on passe a la configuration strategique.

---

**Points cles** :
- Coller la cle API et tester la connexion
- Si le test echoue : verifier la cle, le credit, le rate limit, la connexion de l'hebergeur
- Modeles recommandes : text-embedding-3-small + gpt-4o (meilleur rapport qualite/prix)
- Bien selectionner la langue du site pour la qualite des ancres

**Mots cles SEO** : configurer Easy Content Linker, API OpenAI WordPress plugin, gpt-4o embeddings

---

### Lecon 2.4 — Quiz M2

**Duree** : 5 min
**Type** : Quiz TutorLMS (5 questions QCM)
**Voir plan de formation pour les questions**

---

## Module 3 — Configuration strategique

---

### Lecon 3.1 — Configure les types de contenu source et cible

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des reglages ECL

---

**[INTRO — face camera]**

Easy Content Linker est connecte. Avant de lancer le moindre traitement, on va configurer les reglages strategiques. Premier reglage : quels contenus generent des liens, et quels contenus en recoivent.

**[ECRAN — screencast Content Linker > Reglages > Types de contenu]**

[Montre la section "Contenu source"]

Le contenu source, c'est celui qui va contenir les liens. Par defaut, ce sont les articles — le type "post" de WordPress. C'est logique : tes articles sont le contenu principal de ton site.

Est-ce que tu dois ajouter d'autres types ? Ca depend.

Si tu as des custom post types — par exemple des "fiches produit", des "cours", des "temoignages" — et que ces contenus sont assez longs pour contenir des liens naturels, tu peux les ajouter comme source. Mais attention : un contenu de 200 mots n'a pas la place pour 5 liens internes.

[Montre la section "Contenu cible"]

Le contenu cible, c'est celui qui recoit les liens. Par defaut, ce sont les articles et les pages.

Les pages sont importantes. Tes pages piliers, tes landing pages, tes pages de service — elles meritent de recevoir des liens depuis tes articles.

Mais certaines pages ne doivent pas etre cibles. Ta page de contact, tes CGV, ta page panier WooCommerce, ta page "Mon compte". Ces pages n'ont pas besoin de jus de lien.

**[ECRAN — slide "Configuration recommandee"]**

Pour un blog WordPress classique, voici ma recommandation.

Contenu source : articles uniquement. C'est suffisant dans 90% des cas.

Contenu cible : articles plus pages. Tes pages piliers et tes pages de service meritent de recevoir des liens.

Si tu utilises WooCommerce : ajoute les produits en cible uniquement si tu veux que tes articles renvoient vers tes fiches produit. Ne les ajoute pas en source — les fiches produit sont trop courtes.

[Revient sur les reglages et configure]

Je configure comme ca. Articles en source. Articles et pages en cible.

**[ECRAN — slide "Taxonomies personnalisees"]**

ECL peut aussi cibler les pages de categories et de tags. Ca veut dire que tes liens internes peuvent pointer vers une page de categorie, pas seulement vers un article individuel.

C'est utile si tes pages de categories ont du contenu enrichi — une description detaillee, un texte d'introduction. Si tes pages de categories sont juste des listes d'articles sans texte, ne les ajoute pas en cible.

**[TRANSITION — face camera]**

Les types de contenu sont configures. Prochaine etape : les seuils de similarite. C'est le reglage qui influence le plus la qualite de ton maillage.

---

**Points cles** :
- Source : articles par defaut, ajouter les CPT longs si pertinent
- Cible : articles + pages (exclure les pages utilitaires)
- WooCommerce : produits en cible seulement, pas en source
- Taxonomies : ajouter en cible uniquement si les pages de categories ont du contenu enrichi

**Mots cles SEO** : configurer maillage interne WordPress, types de contenu WordPress, custom post types liens internes

---

### Lecon 3.2 — Regle les seuils de similarite pour ton site

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides echelle de scores, screencast des reglages

---

**[INTRO — face camera]**

Les seuils de similarite sont le coeur du moteur d'ECL. Ils determinent quels articles sont assez proches pour meriter un lien entre eux. Un mauvais reglage, et tu te retrouves avec des liens non pertinents — ou pas assez de liens. Je t'explique comment trouver le bon equilibre.

**[ECRAN — slide "Comment fonctionne le score de similarite"]**

Quand ECL analyse tes articles, chaque paire d'articles recoit un score entre 0 et 1.

0, ca veut dire que les deux articles n'ont rien en commun. 1, ca veut dire qu'ils sont identiques.

Le seuil minimum, c'est le score en dessous duquel ECL ne creera pas de lien. Par defaut, il est a 0.70.

Le seuil maximum, c'est le score au-dessus duquel ECL detecte un doublon potentiel. Par defaut, il est a 0.95.

**[ECRAN — slide "Echelle d'interpretation"]**

Voici comment interpreter les scores.

En dessous de 0.65 : les articles sont lies par theme general, mais pas assez pour justifier un lien direct. Par exemple, un article sur "les meilleurs themes WordPress" et un article sur "comment installer WordPress". Meme univers, mais sujets differents.

Entre 0.65 et 0.80 : les articles partagent un theme proche. C'est la zone ou les liens internes sont les plus naturels. Par exemple, un article sur "TutorLMS avis" et un article sur "creer une formation en ligne avec WordPress". Sujets complementaires, lien pertinent.

Entre 0.80 et 0.90 : les articles sont tres proches. Les liens sont pertinents, mais attention a ne pas creer trop de liens entre des articles presque identiques. C'est la zone ideale pour les liens vers les pages piliers.

Entre 0.90 et 0.95 : les articles sont quasi identiques. ECL cree encore des liens, mais tu devrais verifier si ces articles ne sont pas des doublons.

Au-dessus de 0.95 : doublon probable. ECL t'alerte. Tu dois verifier et potentiellement fusionner ces articles.

**[ECRAN — screencast Content Linker > Reglages > Seuils]**

[Montre les champs de seuils]

Le seuil minimum est a 0.70 par defaut. C'est un bon point de depart pour la plupart des sites.

Mais tu dois l'adapter a ton cas.

[Montre un slider ou un champ de saisie]

Si tu as un blog generaliste avec des sujets varies — WordPress, SEO, marketing, design — tes articles sont naturellement plus eloignes les uns des autres. Baisse le seuil a 0.65 pour trouver plus de connexions.

Si tu as un blog de niche tres specialise — par exemple, uniquement sur les LMS WordPress — tes articles sont naturellement tres proches. Monte le seuil a 0.75 pour eviter les liens generiques qui n'apportent rien.

Le seuil maximum, laisse-le a 0.95. Ne le change que si tu as des pages intentionnellement similaires — par exemple des pages de services par ville. Dans ce cas, tu pourras whitelister ces categories dans les reglages.

**[ECRAN — slide "Mon recommandation"]**

Blog generaliste : 0.65
Blog de niche : 0.75
Site mixte (blog + pages de service) : 0.70 — le defaut
E-commerce avec blog : 0.70

Tu peux toujours ajuster apres le premier traitement. Si tu vois trop de liens non pertinents, monte le seuil. Si tu n'as pas assez de liens, baisse-le.

**[TRANSITION — face camera]**

Les seuils sont regles. Prochaine lecon : les limites de liens et le mode silo. On continue a affiner la configuration.

---

**Points cles** :
- Score 0 = rien en commun, 1 = identique
- Seuil minimum : 0.65 (generaliste), 0.70 (defaut), 0.75 (niche)
- Seuil maximum : 0.95 (detection doublons) — ne pas toucher sauf cas particulier
- Zone ideale pour les liens : 0.65-0.90
- Ajuster apres le premier traitement selon les resultats

**Mots cles SEO** : seuil similarite maillage interne, score semantique SEO, embeddings WordPress

---

### Lecon 3.3 — Configure les limites de liens et le mode silo

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des reglages, slide mode silo

---

**[INTRO — face camera]**

Combien de liens internes par article, c'est trop ? Et est-ce que tu devrais cloisonner tes liens par categorie ? Dans cette lecon, on configure les limites de liens et le mode silo.

**[ECRAN — screencast Content Linker > Reglages > Limites]**

[Montre les champs de limites]

ECL a deux limites configurables.

Le nombre maximum de liens sortants par article. Par defaut, c'est 5. Ca veut dire qu'un article peut contenir au maximum 5 liens internes generes par ECL. Attention, ca ne compte pas les liens que tu as ajoutes manuellement.

Le nombre maximum de liens entrants par article. Par defaut, c'est 20. Ca veut dire qu'un article peut recevoir au maximum 20 liens provenant d'autres articles.

**[ECRAN — slide "Comment choisir les bonnes limites"]**

Les bonnes limites dependent de la taille de ton site.

Petit site, 30 a 50 articles : je recommande 3 liens sortants maximum. Avec peu d'articles, 5 liens sortants risque de forcer des liens non pertinents. 3 liens bien choisis valent mieux que 5 liens moyens.

Site moyen, 50 a 200 articles : le defaut de 5 sortants fonctionne bien. Il y a suffisamment d'articles pour que ECL trouve 5 cibles pertinentes.

Gros site, plus de 200 articles : tu peux monter a 7 ou 8 liens sortants. Le volume d'articles garantit que les liens resteront pertinents.

Pour les liens entrants, 20 est genereux. Si tu veux concentrer le jus de lien sur tes pages les plus importantes, baisse a 10 ou 15. Les pages strategiques avec boost recevront quand meme plus de liens que les autres.

**[ECRAN — slide "Le mode silo"]**

Le mode silo est un reglage qui limite les liens internes a l'interieur d'une meme categorie.

Concretement, si tu actives le silo, un article de la categorie "LMS" ne recevra des liens que depuis d'autres articles "LMS". Il ne recevra pas de liens depuis un article "CRM" ou "SEO".

**[ECRAN — schema visuel : silos par categorie]**

[Schema avec 3 categories cloisonnees, liens internes uniquement a l'interieur de chaque silo]

L'avantage, c'est que ca renforce la coherence thematique de chaque cluster. Google comprend mieux la structure de ton site.

L'inconvenient, c'est que ca empeche les connexions transversales. Si un article CRM est legitimement lie a un article LMS, le silo bloquera ce lien.

**[ECRAN — slide "Quand activer le silo ?"]**

Active le silo si tes categories correspondent a des cocons semantiques bien definis. Chaque categorie couvre un sujet distinct, avec 10 articles ou plus.

Desactive le silo si tes categories sont mal organisees. Si tu as 20 categories dont la moitie avec 2 articles, le silo ne fera que limiter les possibilites.

Desactive aussi le silo si tu veux des connexions transversales entre tes piliers. Par exemple, un article "Automatiser TutorLMS avec FluentCRM" merite des liens depuis les categories LMS et CRM.

Mon conseil : desactive le silo pour ton premier maillage. Analyse les resultats. Si tu vois trop de liens entre categories non liees, active-le dans un second temps.

**[TRANSITION — face camera]**

Les limites et le silo sont configures. Derniere etape avant de lancer le traitement : les exclusions de categories. C'est ce qu'on voit dans la prochaine lecon.

---

**Points cles** :
- Liens sortants : 3 (petit site), 5 (defaut/moyen), 7-8 (gros site)
- Liens entrants : 20 par defaut, baisser a 10-15 pour concentrer le jus
- Mode silo : cloisonne les liens par categorie
- Activer le silo si categories = cocons bien definis (10+ articles chacune)
- Recommandation : desactiver le silo pour le premier maillage, analyser, puis decider

**Mots cles SEO** : silo SEO WordPress, limites liens internes, cocon semantique WordPress

---

### Lecon 3.4 — Choisis les categories a exclure (et pourquoi)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des reglages

---

**[INTRO — face camera]**

Tous les contenus de ton site ne meritent pas de participer au maillage interne. Certaines categories doivent etre exclues. Je t'explique lesquelles et pourquoi.

**[ECRAN — screencast Content Linker > Reglages > Categories exclues]**

[Montre la section d'exclusion de categories]

ECL te permet d'exclure des categories entieres du maillage. Les articles de ces categories ne genereront pas de liens et n'en recevront pas.

**[ECRAN — slide "Quelles categories exclure"]**

Premiere categorie a exclure : "Non classe" ou "Uncategorized". C'est la categorie par defaut de WordPress. Si tu as des articles dedans, ils sont probablement mal classes. Pas de raison de les inclure dans le maillage.

Deuxieme type : les categories de contenu perissable. Les actus, les news, les evenements passes. Un article "Les nouveautes WordPress 2024" n'a pas besoin de liens internes en 2026. Ca dilue le jus sans apporter de valeur.

Troisieme type : les categories purement techniques ou internes. Si tu as une categorie "Brouillons publics", "Tests", ou "Changelog", exclue-la.

Quatrieme type : les categories hors strategie SEO. Si tu as une categorie "Coups de coeur" ou "Billets d'humeur" qui n'est pas alignee sur tes piliers de contenu, exclue-la.

**[ECRAN — screencast configuration]**

[Selectionne 2-3 categories a exclure]

Je coche "Non classe" et "Actus". Ces categories ne participent pas a ma strategie SEO.

Les categories importantes — celles qui correspondent a mes piliers de contenu — restent incluses. Ce sont elles qui vont beneficier du maillage.

**[ECRAN — slide "Ce qu'il ne faut PAS exclure"]**

Ne te precipite pas a exclure trop de categories. Chaque exclusion reduit le nombre de connexions possibles.

Garde tes categories principales. Garde les categories avec 5 articles ou plus. Garde les categories alignees sur tes mots-cles cibles.

En cas de doute, ne pas exclure. Tu pourras toujours ajuster apres le premier traitement en regardant les resultats.

**[TRANSITION — face camera]**

La configuration est terminee. Ton ECL est pret a lancer le premier traitement. C'est ce qu'on fait dans le module suivant. On entre dans le vif du sujet.

---

**Points cles** :
- Exclure : Non classe, contenu perissable, categories techniques, categories hors strategie
- Ne pas exclure : categories principales, categories alignees sur les piliers SEO
- En cas de doute, garder la categorie — ajuster apres le premier traitement
- Chaque exclusion reduit les connexions possibles

**Mots cles SEO** : categories WordPress SEO, exclure categories maillage interne

---

### Lecon 3.5 — Quiz M3

**Duree** : 5 min
**Type** : Quiz TutorLMS (5 questions QCM)
**Voir plan de formation pour les questions**
