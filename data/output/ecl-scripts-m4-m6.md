# Scripts video — Modules 4 a 6 : Premier maillage, pages strategiques, audit

**Formation** : Maitriser Easy Content Linker
**Modules** : M4 a M6
**Lecons** : 9 videos + 3 quiz (dont 1 quiz final de 10 questions)
**Duree totale** : ~75 min de video
**Date** : 2026-03-23

---

## Module 4 — Premier maillage complet

---

### Lecon 4.1 — Lance le traitement : embeddings puis liens

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast du Dashboard ECL pendant le traitement

---

**[INTRO — face camera]**

C'est le moment. Ton ECL est configure, tes reglages sont en place. On lance le premier traitement complet. Je te montre exactement ce qui se passe, combien de temps ca prend, et ce qu'il faut surveiller.

**[ECRAN — screencast Content Linker > Dashboard]**

[Montre le dashboard avec les boutons de traitement]

Le traitement se fait en deux phases, et c'est important de comprendre la difference.

**Phase 1 : la generation des embeddings.**

[Clique sur "Lancer l'analyse"]

Quand tu cliques sur "Lancer l'analyse", ECL envoie le contenu de chaque article a OpenAI pour creer son empreinte semantique. C'est comme prendre une photo de chaque article pour que l'IA puisse les comparer.

[Montre la barre de progression]

Tu vois la barre de progression. Chaque article est traite un par un. Pour 50 articles, ca prend entre 5 et 10 minutes. Pour 200 articles, compte 15 a 20 minutes.

Point important : les embeddings sont calcules une seule fois. Si tu relances le traitement plus tard, les articles deja analyses ne seront pas recalcules. Seuls les nouveaux articles ou ceux modifies seront traites. Ca veut dire que la premiere execution est la plus longue. Les suivantes seront beaucoup plus rapides.

**[ECRAN — slide "Attention : garde l'onglet ouvert"]**

Le traitement se fait cote navigateur. Si tu fermes l'onglet, le traitement s'arrete.

Ne ferme pas l'onglet. Ne mets pas ton ordinateur en veille. Tu peux ouvrir d'autres onglets, mais garde celui-ci actif.

Si le traitement s'interrompt — panne internet, fermeture accidentelle — pas de panique. Les embeddings deja calcules sont sauvegardes. Tu relances et il reprend la ou il s'est arrete.

**[ECRAN — screencast Phase 2]**

**Phase 2 : la creation des liens.**

[Montre le demarrage de la phase 2]

Une fois les embeddings calcules, ECL passe a la creation des liens. Il compare les scores de similarite entre tous tes articles, identifie les meilleures paires, et demande a GPT de trouver une ancre naturelle dans le texte.

Cette phase est plus longue car chaque lien necessite un appel GPT. Pour 50 articles, compte 10 a 15 minutes. Pour 200 articles, 30 a 45 minutes.

[Montre les liens qui apparaissent progressivement dans le dashboard]

Tu vois les liens apparaitre en temps reel dans le dashboard. Le compteur de liens crees augmente au fur et a mesure.

**[ECRAN — slide "Estimations de temps et de cout"]**

Pour que tu saches a quoi t'attendre :

50 articles : 15-25 minutes au total, 1,50-4 euros
100 articles : 25-40 minutes au total, 3-8 euros
200 articles : 40-65 minutes au total, 6-15 euros
500 articles : je recommande de decouper par categorie (on en parle dans une minute)

**[ECRAN — slide "Pour les gros sites : decoupe par categorie"]**

Si tu as plus de 200 articles, ne traite pas tout d'un coup. Le risque c'est un timeout navigateur ou une facture API plus elevee que prevu.

La strategie recommandee : traite categorie par categorie, en commencant par ton pilier principal. Comme ca, tu valides la qualite des liens sur un premier lot avant de lancer le reste.

Configure temporairement les categories en source/cible pour n'inclure que celles que tu traites. Lance le traitement. Verifie les resultats. Puis passe aux categories suivantes.

**[TRANSITION — face camera]**

Le traitement est en cours ou termine. Dans la prochaine lecon, on plonge dans l'historique pour juger la qualite des liens generes.

---

**Points cles** :
- Phase 1 (embeddings) : une seule fois par article, 5-20 min selon le volume
- Phase 2 (liens) : appel GPT par lien, 10-45 min selon le volume
- Garder l'onglet ouvert pendant le traitement
- Si interruption : les embeddings sont sauvegardes, relancer reprend la ou ca s'est arrete
- Gros sites (200+) : decouper par categorie

**Mots cles SEO** : lancer maillage interne automatique, traitement embeddings WordPress, cout maillage interne IA

---

### Lecon 4.2 — Explore l'historique et juge la qualite des liens

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast de l'Historique ECL

---

**[INTRO — face camera]**

Le traitement est termine, les liens sont crees. Mais avant de se rejouir, il faut verifier la qualite. Un maillage automatique n'est bon que si les liens sont pertinents. Je te montre comment lire l'historique et reperer les bons et les mauvais liens.

**[ECRAN — screencast Content Linker > Historique]**

[Montre la page Historique avec la liste des liens]

Voici l'historique de tous les liens generes. Chaque ligne contient cinq informations.

L'article source : celui qui contient le lien.
L'article cible : celui vers lequel le lien pointe.
L'ancre : la phrase du texte qui sert de lien cliquable.
Le score de similarite : entre 0 et 1.
La date de creation.

[Montre un lien avec un score de 0.82]

Prenons ce lien. L'article source parle de "comment choisir un LMS WordPress". L'article cible est "TutorLMS avis complet". L'ancre est "un LMS qui s'integre nativement a WordPress". Le score est 0.82.

C'est un bon lien. Le sujet est lie, l'ancre est naturelle — c'est une phrase qui existait deja dans le texte — et le score est dans la zone ideale.

**[ECRAN — slide "Les criteres d'un bon lien"]**

Un bon lien interne genere par ECL respecte trois criteres.

Premier critere : la pertinence thematique. L'article source et l'article cible traitent de sujets complementaires. Un lecteur qui lit l'un aurait naturellement envie de lire l'autre.

Deuxieme critere : la naturalite de l'ancre. L'ancre est une phrase qui coule dans le texte. Elle ne donne pas l'impression d'avoir ete forcee. Quand tu lis le paragraphe, le lien semble logique.

Troisieme critere : le score de similarite. Dans la zone 0.65-0.90, les liens sont generalement pertinents. En dessous de 0.65, la pertinence baisse. Au-dessus de 0.90, verifie que ce ne sont pas des doublons.

**[ECRAN — screencast d'un mauvais lien]**

[Montre un lien avec un score de 0.62 ou une ancre peu naturelle]

Maintenant, voici un lien moins bon. L'article source parle de "securiser WordPress" et l'article cible est "les meilleurs plugins SEO". Le score est a 0.63. L'ancre est "optimiser ton site WordPress".

Le probleme : le lien entre securite et SEO est tenu. L'ancre est vague. Un lecteur qui lit un article sur la securite ne s'attend pas a atterrir sur un comparatif de plugins SEO.

Ce type de lien, il vaut mieux le supprimer.

**[ECRAN — screencast utilisation des filtres]**

[Montre les options de recherche et filtres]

Tu peux filtrer les liens par categorie pour les examiner par cluster. Tu peux aussi rechercher par titre d'article ou par ancre.

Mon conseil : apres le premier traitement, prends 15 a 20 minutes pour parcourir les liens. Verifie les liens avec les scores les plus bas en premier — ce sont les plus susceptibles d'etre non pertinents.

[Trie par score croissant]

En triant par score croissant, tu vois immediatement les liens les plus fragiles.

**[TRANSITION — face camera]**

Tu sais maintenant lire l'historique et juger la qualite des liens. Dans la prochaine lecon, je te montre comment corriger les problemes : supprimer les liens faibles et comprendre les exclusions.

---

**Points cles** :
- Un bon lien : pertinence thematique + ancre naturelle + score 0.65-0.90
- Verifier les liens avec les scores les plus bas en priorite
- Prendre 15-20 minutes apres le premier traitement pour un audit rapide
- Utiliser les filtres par categorie pour examiner cluster par cluster
- Trier par score croissant pour trouver les liens les plus fragiles

**Mots cles SEO** : historique liens internes, qualite maillage interne, audit liens internes WordPress

---

### Lecon 4.3 — Corrige les problemes : ancres faibles, liens non pertinents, erreurs

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast de l'Historique et du rapport d'exclusions

---

**[INTRO — face camera]**

Tu as identifie des liens qui ne te conviennent pas. Maintenant, on corrige. Je te montre comment supprimer un lien, comprendre pourquoi certains articles n'ont pas recu de liens, et que faire si le traitement s'est interrompu.

**[ECRAN — screencast Content Linker > Historique]**

[Montre un lien a supprimer]

Pour supprimer un lien, c'est simple. Clique sur le bouton "Revert" a cote du lien.

[Clique sur Revert]

Le lien disparait immediatement de l'historique. Et comme ECL fonctionne par injection dynamique, le lien disparait aussi de l'article au prochain chargement de page. Aucune trace dans ta base de donnees. C'est propre.

[Supprime 2-3 liens]

Je supprime ces deux liens dont les scores etaient en dessous de 0.65. Et celui-ci dont l'ancre n'etait pas naturelle.

**[ECRAN — screencast onglet "URLs exclues"]**

[Navigue vers le rapport d'exclusions]

Si certains articles n'ont pas recu de liens, ECL t'explique pourquoi dans l'onglet "URLs exclues". Chaque URL exclue a une raison.

[Montre les differentes raisons]

"Similarite trop basse" : aucun article n'est suffisamment lie thematiquement. C'est normal pour un article sur un sujet isole. Solutions : baisser le seuil minimum, ou ecrire plus de contenu sur ce sujet.

"Similarite trop haute — doublon detecte" : deux articles sont quasi identiques. On traitera ca dans le module 5 avec la detection de doublons.

"Max liens entrants atteint" : l'article cible a deja recu son nombre maximum de liens. Si c'est une page importante, augmente la limite ou configure-la en page strategique.

"Noindex" : l'article a une balise noindex. ECL ne cree pas de liens vers des pages que tu as toi-meme exclues de Google. C'est logique.

"Canonical different" : l'URL canonique pointe ailleurs. Verifie ta configuration de balises canoniques dans RankMath ou ton plugin SEO.

"Bloque par robots.txt" : le fichier robots.txt empeche l'acces. Verifie ton robots.txt.

"Exclusion manuelle" : tu as exclu cet article dans les reglages ou via la metabox.

**[ECRAN — slide "Que faire si le traitement s'est interrompu"]**

Si le traitement s'est arrete — navigateur ferme, panne internet, timeout — voici ce qu'il faut faire.

Premiere chose : ne panique pas. Les embeddings calcules sont sauvegardes. Les liens deja crees sont en place. Rien n'est perdu.

Deuxieme chose : retourne sur le Dashboard et relance le traitement. ECL detecte automatiquement ce qui a deja ete fait et reprend la ou il s'est arrete.

Troisieme chose : si le probleme se reproduit, reduis le lot. Traite par categorie au lieu de tout traiter d'un coup.

**[TRANSITION — face camera]**

Ton premier maillage est en place et nettoye. Dans le prochain module, on passe au niveau superieur : les pages strategiques et les exclusions granulaires. C'est la que tu transformes un bon maillage en un maillage strategique.

---

**Points cles** :
- Revert supprime un lien immediatement, sans trace en base de donnees
- Le rapport d'exclusions explique pourquoi certains articles n'ont pas de liens
- Les raisons les plus courantes : similarite trop basse, max liens atteint, noindex
- Interruption du traitement : relancer reprend automatiquement, rien n'est perdu
- Pour les gros sites : traiter par categorie si timeout

**Mots cles SEO** : supprimer liens internes WordPress, rapport exclusions maillage, corriger maillage interne

---

### Lecon 4.4 — Quiz M4

**Duree** : 5 min
**Type** : Quiz TutorLMS (5 questions QCM)
**Voir plan de formation pour les questions**

---

## Module 5 — Pages strategiques et exclusions

---

### Lecon 5.1 — Identifie tes pages strategiques (pillar, money, landing)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides schema de hierarchie, screencast rapide

---

**[INTRO — face camera]**

Jusqu'ici, ECL traite tous tes articles de la meme maniere. Mais sur ton site, certaines pages sont plus importantes que d'autres. Tes pages piliers, tes pages de vente, tes landing pages — elles meritent plus de liens internes. ECL te permet de les booster. Encore faut-il savoir lesquelles choisir.

**[ECRAN — slide "3 types de pages strategiques"]**

Il y a trois types de pages qui meritent un boost dans ECL.

**Les pages piliers.** Ce sont tes contenus longs et complets qui couvrent un sujet en profondeur. Par exemple, "Le guide complet des LMS WordPress" ou "Tout savoir sur le maillage interne". Ces pages sont le coeur de ta strategie de contenu. Elles doivent recevoir un maximum de liens internes.

**Les money pages.** Ce sont tes pages qui generent du revenu — directement ou indirectement. Les comparatifs avec liens affiliation, les pages de service, les pages de vente de formation. Un lien interne vers ces pages, c'est un visiteur potentiel en plus dans ton entonnoir de conversion.

**Les landing pages.** Ce sont tes pages de capture — inscription newsletter, telechargement d'un lead magnet, inscription a un webinaire. Plus elles recoivent de trafic interne, plus elles convertissent.

**[ECRAN — slide "Comment les identifier sur ton site"]**

Ouvre un tableur et fais une liste. Parcours tes pages et tes articles les plus importants.

Pour chaque contenu, pose-toi trois questions. Est-ce que cette page est le pilier d'un cluster thematique ? Est-ce qu'elle genere du revenu ou des leads ? Est-ce qu'elle merite plus de visibilite que les autres ?

Si tu reponds oui a au moins une question, c'est une page strategique.

Attention : ne selectionne pas plus de 10 a 15 pages. Si tu boostes tout, tu ne boostes rien. La force du boost, c'est la concentration.

**[ECRAN — slide "Quel niveau de boost pour chaque type"]**

ECL propose trois niveaux de boost.

Plus 10% : un boost leger. Pour les pages secondaires qui meritent un peu plus d'attention. Par exemple, un guide pratique important mais pas central.

Plus 25% : un boost modere. Pour les money pages et les landing pages. Elles recoivent plus de liens sans ecraser le maillage naturel.

Plus 50% : le boost maximum. Reserve aux pages piliers. Tes 3 a 5 contenus les plus importants du site. Ceux qui doivent concentrer le maximum de jus de lien.

**[ECRAN — slide "Exemple concret"]**

Sur un site schoolsWP, ca donnerait :

Page pilier "Guide complet LMS WordPress" : +50%
Comparatif "TutorLMS vs LearnDash" : +25%
Landing page "Formation gratuite LMS" : +25%
Guide pratique "Installer TutorLMS" : +10%

4 pages strategiques sur 80 articles. C'est un ratio sain.

**[TRANSITION — face camera]**

Tu as identifie tes pages strategiques et leur niveau de boost. Dans la prochaine lecon, on les configure dans ECL avec les ancres personnalisees.

---

**Points cles** :
- 3 types de pages strategiques : piliers (+50%), money pages (+25%), landing pages (+25%)
- Ne pas booster plus de 10-15 pages (concentration = efficacite)
- Criteres : pilier de cluster, generation de revenu/leads, besoin de visibilite
- Le boost augmente la probabilite de recevoir des liens, pas la garantie

**Mots cles SEO** : pages piliers WordPress, money pages SEO, booster pages stratégiques maillage interne

---

### Lecon 5.2 — Configure les bonus et les ancres personnalisees

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast complet des Pages strategiques ECL

---

**[INTRO — face camera]**

Tu as ta liste de pages strategiques. Maintenant, on les configure dans ECL. Je te montre comment attribuer les bonus et surtout comment choisir les ancres personnalisees — c'est la partie la plus strategique.

**[ECRAN — screencast Content Linker > Pages strategiques]**

[Navigue vers la section Pages strategiques]

Voici la page de gestion des pages strategiques. Tu peux ajouter n'importe quelle page ou article de ton site.

[Clique sur "Ajouter une page strategique"]

Je vais ajouter ma page pilier "Guide complet LMS WordPress".

[Selectionne la page dans le menu deroulant]

La page est ajoutee. Maintenant, deux choses a configurer : le niveau de bonus et les ancres personnalisees.

[Montre le selecteur de bonus]

Je selectionne +50% — c'est ma page pilier numero un.

[Montre les champs d'ancres personnalisees]

Maintenant, les ancres. ECL te permet de definir jusqu'a 5 ancres personnalisees par page. Quand l'IA trouve une de ces phrases dans un article, elle l'utilisera comme ancre de lien sans meme appeler GPT. Ca reduit les couts API et ca garantit des ancres exactement comme tu les veux.

**[ECRAN — slide "Comment choisir les bonnes ancres"]**

Le choix des ancres est strategique. Voici ma methode.

Premiere ancre : ton mot-cle principal exact. Par exemple, "LMS WordPress". C'est l'ancre la plus puissante pour le SEO.

Deuxieme ancre : une variante naturelle. Par exemple, "choisir un LMS WordPress". C'est une phrase qui apparait naturellement dans les articles de ton cluster.

Troisieme ancre : une variante longue traîne. Par exemple, "plugin LMS pour WordPress". Ca couvre une intention de recherche differente.

Quatrieme et cinquieme ancres : des formulations contextuelles. Par exemple, "systeme de formation en ligne WordPress" ou "plateforme de cours WordPress". Des phrases que tes articles utilisent naturellement.

Evite les ancres generiques comme "cliquez ici", "en savoir plus" ou "cet article". Elles n'apportent aucune valeur SEO.

**[ECRAN — screencast configuration complete]**

[Saisit les 5 ancres pour la page pilier LMS]

Je rentre mes 5 ancres. "LMS WordPress". "Choisir un LMS WordPress". "Plugin LMS pour WordPress". "Systeme de formation en ligne WordPress". "Plateforme de cours WordPress".

[Montre le bouton sauvegarder]

Je sauvegarde. Ces ancres sont maintenant reservees pour cette page. Elles ne seront jamais utilisees pour pointer vers un autre article. C'est la reservation automatique d'ECL.

[Ajoute une deuxieme page strategique — comparatif]

J'ajoute maintenant mon comparatif "TutorLMS vs LearnDash". Bonus +25%. Ancres : "TutorLMS vs LearnDash", "comparatif LMS WordPress", "quel LMS choisir".

**[ECRAN — slide "Astuce RankMath"]**

Si tu utilises RankMath, va voir les mots-cles focus de chaque page strategique. Ce sont d'excellents candidats pour les ancres personnalisees. RankMath et ECL sont complementaires : RankMath optimise le on-page, ECL optimise le maillage.

**[TRANSITION — face camera]**

Tes pages strategiques sont configurees avec les bons bonus et les bonnes ancres. Prochaine lecon : les exclusions granulaires par article. On va exclure chirurgicalement les contenus qui ne doivent pas participer au maillage.

---

**Points cles** :
- 5 ancres max par page strategique, reservees exclusivement
- Methode : mot-cle exact + variante naturelle + longue traîne + 2 formulations contextuelles
- Eviter les ancres generiques ("cliquez ici", "en savoir plus")
- Les ancres personnalisees evitent un appel GPT — economie d'API
- Complementarite avec RankMath : utiliser les focus keywords comme base d'ancres

**Mots cles SEO** : ancres personnalisees maillage interne, pages strategiques SEO WordPress, Easy Content Linker pages boost

---

### Lecon 5.3 — Maitrise les exclusions granulaires par article

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast de la metabox ECL dans l'editeur WordPress

---

**[INTRO — face camera]**

Parfois, tu veux exclure un article precis du maillage — pas une categorie entiere, juste un article. ECL te donne trois options d'exclusion granulaire, chacune pour un cas different. Je te montre quand utiliser laquelle.

**[ECRAN — screencast d'un article dans l'editeur WordPress]**

[Ouvre un article dans l'editeur]

Quand tu edites un article avec la version Pro, une metabox "Content Linker" apparait dans la colonne laterale.

[Montre la metabox avec les 3 options]

Tu as trois cases a cocher, et chacune fait quelque chose de different.

**Option 1 : "Exclure completement."**

[Coche la premiere option]

L'article ne participe plus au maillage du tout. Il ne genere pas de liens et il n'en recoit pas. C'est l'exclusion totale.

Quand l'utiliser ? Pour un article en cours de redaction que tu as publie temporairement. Pour un article que tu vas supprimer prochainement. Pour un contenu de test.

**Option 2 : "Ne pas generer de liens depuis cet article."**

[Decoche la premiere, coche la deuxieme]

L'article peut recevoir des liens — d'autres articles peuvent pointer vers lui. Mais il ne contiendra aucun lien ECL. Le texte reste vierge de liens automatiques.

Quand l'utiliser ? Pour une landing page avec un seul CTA. Tu ne veux pas distraire le visiteur avec des liens internes qui l'eloignent de ton objectif de conversion.

Pour une page de vente. Meme logique — chaque lien interne est une sortie potentielle avant l'achat.

**Option 3 : "Ne pas recevoir de liens vers cet article."**

[Decoche la deuxieme, coche la troisieme]

L'article peut generer des liens vers d'autres articles, mais aucun autre article ne pointera vers lui. Il donne du jus, mais il n'en recoit pas.

Quand l'utiliser ? Pour un article sponsorise. Tu ne veux pas envoyer du jus de lien vers du contenu sponsorise.

Pour un article temporaire — un compte-rendu d'evenement, un article saisonnier — que tu ne veux pas renforcer dans les resultats de recherche.

**[ECRAN — slide "Resume des 3 options"]**

[Tableau recapitulatif]

Exclure completement : pas de liens sortants, pas de liens entrants. Usage : brouillons, tests, a supprimer.

Pas de liens depuis : recoit des liens, ne genere pas de liens. Usage : landing pages, pages de vente.

Pas de liens vers : genere des liens, ne recoit pas de liens. Usage : articles sponsorises, contenu temporaire.

**[ECRAN — screencast de la detection de doublons]**

[Montre l'alerte de doublons dans le Dashboard]

Avant de conclure ce module, un mot sur la detection de doublons. Si ECL detecte deux articles avec un score superieur a 0.95, tu verras une alerte dans le Dashboard.

[Montre les details du doublon]

L'alerte te donne les deux articles et leur score. A toi de decider :

Fusionner les deux articles en un seul — garder le meilleur, rediriger l'autre en 301.
Differencier — reecrire l'un des deux pour qu'il couvre un angle different.
Whitelister — si c'est intentionnel, comme des pages de service par ville.

Ne laisse pas les doublons trainer. Ils diluent ton autorite SEO.

**[TRANSITION — face camera]**

Les exclusions et les pages strategiques sont en place. Ton maillage est maintenant strategique, pas juste automatique. Dans le dernier module, on audite, on optimise et on met en place la routine de maintenance.

---

**Points cles** :
- 3 exclusions granulaires : totale, pas de liens depuis (landing pages), pas de liens vers (sponsorise)
- Detection doublons (>95%) : fusionner, differencier ou whitelister
- Ne pas laisser trainer les doublons — impact SEO negatif
- Chaque exclusion a un cas d'usage precis — ne pas exclure au hasard

**Mots cles SEO** : exclure article maillage interne, detection doublons WordPress, exclusion liens internes

---

### Lecon 5.4 — Quiz M5

**Duree** : 5 min
**Type** : Quiz TutorLMS (5 questions QCM)
**Voir plan de formation pour les questions**

---

## Module 6 — Audit, optimisation et maintenance

---

### Lecon 6.1 — Audite ton maillage avec l'export CSV

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast de l'export + Google Sheets

---

**[INTRO — face camera]**

Ton maillage est en place. Mais comment savoir s'il est bien distribue ? Est-ce que certains articles recoivent trop de liens et d'autres pas assez ? L'export CSV te donne une vision complete. Je te montre comment l'exploiter.

**[ECRAN — screencast Content Linker > Historique > Export]**

[Clique sur le bouton "Exporter en CSV"]

Dans l'onglet Historique, clique sur "Exporter en CSV". Le fichier se telecharge immediatement.

[Ouvre le fichier dans Google Sheets]

J'ouvre le CSV dans Google Sheets. Chaque ligne represente un lien : article source, URL source, article cible, URL cible, ancre, score de similarite, date.

**[ECRAN — screencast Google Sheets — analyse]**

Premiere analyse : les articles qui recoivent le plus de liens.

[Cree un tableau croise dynamique ou trie par URL cible]

Je trie par article cible. Certains articles recoivent 15 liens, d'autres seulement 1. Si une page non strategique recoit 15 liens alors que ta page pilier en recoit 3, il y a un desequilibre.

Solution : augmenter le boost de la page pilier, ou baisser la limite de liens entrants pour forcer une meilleure distribution.

Deuxieme analyse : les articles orphelins.

[Filtre les articles qui n'apparaissent ni en source ni en cible]

Si un article n'apparait nulle part dans le CSV — ni comme source, ni comme cible — c'est un orphelin. Il n'est connecte a rien. Verifie pourquoi dans le rapport d'exclusions.

Les orphelins sont un probleme SEO. Google les decouvre difficilement et ne comprend pas leur place dans ta structure.

Troisieme analyse : la variete des ancres.

[Filtre par ancre pour un article cible]

Si une page cible recoit 10 liens avec la meme ancre exacte, c'est de la sur-optimisation. Les ancres doivent etre variees. ECL fait generalement un bon travail, mais verifie quand meme.

**[ECRAN — slide "Les 5 signaux d'un bon maillage"]**

Resume. Un bon maillage, c'est :

1. Les pages strategiques recoivent plus de liens que les autres.
2. Pas d'article orphelin — tout le monde est connecte.
3. Les ancres sont variees, pas repetitives.
4. Les scores sont dans la zone 0.65-0.90 pour la majorite des liens.
5. Les liens restent dans le meme cluster thematique quand le silo est active.

**[TRANSITION — face camera]**

Tu sais maintenant auditer ton maillage. Prochaine lecon : ajuster les reglages apres ce premier audit.

---

**Points cles** :
- Exporter le CSV et ouvrir dans Google Sheets
- 3 analyses cles : distribution des liens entrants, articles orphelins, variete des ancres
- Les pages strategiques doivent recevoir plus de liens
- Les articles orphelins sont un probleme SEO a corriger
- Les ancres doivent etre variees pour eviter la sur-optimisation

**Mots cles SEO** : audit maillage interne WordPress, export CSV liens internes, articles orphelins SEO

---

### Lecon 6.2 — Optimise : ajuste les reglages apres le premier maillage

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des reglages ECL

---

**[INTRO — face camera]**

L'audit est fait, tu as identifie les desequilibres. Maintenant, on ajuste les reglages pour que le prochain traitement soit meilleur. ECL a un systeme intelligent de flush qui nettoie les liens obsoletes quand tu changes un reglage. Je te montre comment ca marche.

**[ECRAN — screencast Content Linker > Reglages]**

[Montre les reglages actuels]

Reprenons les resultats de ton audit et ajustons.

**Scenario 1 : pas assez de liens generes.**

[Montre le seuil minimum]

Si beaucoup d'articles n'ont pas recu de liens et que le rapport d'exclusions indique "similarite trop basse", baisse le seuil minimum. De 0.70 a 0.65 par exemple. Ca ouvre plus de connexions possibles.

Tu peux aussi augmenter la limite de liens sortants par article. De 5 a 7 par exemple.

**Scenario 2 : trop de liens non pertinents.**

[Montre le seuil minimum]

Si tu as supprime beaucoup de liens en Revert parce qu'ils n'etaient pas pertinents, monte le seuil minimum. De 0.70 a 0.75. Ca filtre les connexions trop laches.

Tu peux aussi baisser la limite de liens sortants. De 5 a 3. Moins de liens mais mieux cibles.

**Scenario 3 : certaines categories polluent.**

[Montre les categories exclues]

Si tu vois des liens entre des categories non liees — par exemple "Recettes de cuisine" qui se lie a "Plugins WordPress" — exclue la categorie problematique.

**[ECRAN — slide "Notification flush"]**

[Montre la notification qui apparait apres un changement de reglage]

Quand tu changes un reglage structurel — types de contenu, categories exclues, mode silo — ECL affiche une notification : "Vos reglages ont change. Voulez-vous nettoyer les liens qui ne correspondent plus aux nouveaux criteres ?"

Clique sur "Nettoyer". ECL supprime les liens devenus obsoletes. Par exemple, si tu viens d'exclure une categorie, tous les liens depuis ou vers cette categorie seront supprimes.

Le nettoyage preserve les embeddings. Aucun cout API supplementaire. Seuls les liens sont recalcules.

Ensuite, relance le traitement pour generer de nouveaux liens avec les reglages mis a jour.

**[TRANSITION — face camera]**

Tes reglages sont optimises. Derniere lecon : la routine de maintenance pour que ton maillage reste performant dans le temps.

---

**Points cles** :
- Pas assez de liens : baisser le seuil minimum, augmenter les liens sortants
- Trop de liens non pertinents : monter le seuil minimum, baisser les liens sortants
- Categories polluantes : les exclure
- Notification flush : nettoie les liens obsoletes sans recalculer les embeddings
- Toujours relancer le traitement apres un changement de reglages

**Mots cles SEO** : optimiser maillage interne, reglages Easy Content Linker, ajuster liens internes WordPress

---

### Lecon 6.3 — Maintenance : nouveaux articles, mises a jour, routine mensuelle

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides de routine, screencast rapide

---

**[INTRO — face camera]**

Ton maillage est en place et optimise. Mais un maillage n'est pas un truc qu'on configure une fois et qu'on oublie. Ton site evolue — tu publies de nouveaux articles, tu modifies des anciens, tu supprimes des contenus. Je te donne la routine de maintenance pour que ton maillage reste performant.

**[ECRAN — slide "Quand relancer le traitement"]**

Trois situations necessitent de relancer ECL.

**Situation 1 : tu publies un nouvel article.**

L'article n'a pas encore d'embedding. Il faut lancer le traitement pour l'analyser et creer des liens depuis et vers cet article. Bonne nouvelle : seul le nouvel article sera analyse pour les embeddings. Les autres articles conservent les leurs. C'est rapide et peu couteux.

Frequence recommandee : apres chaque publication, ou une fois par semaine si tu publies regulierement.

**Situation 2 : tu modifies un article en profondeur.**

Si tu reecris un article — pas juste une correction de faute, une vraie refonte — son embedding n'est plus a jour. ECL detecte automatiquement que le contenu a change et recalcule l'embedding.

Les liens existants depuis et vers cet article sont peut-etre devenus obsoletes. Verifie-les dans l'historique. Supprime ceux qui ne sont plus pertinents.

**Situation 3 : tu supprimes un article.**

Les liens vers un article supprime vont pointer dans le vide. ECL gere ca automatiquement — les liens sont injectes dynamiquement, donc si l'article cible n'existe plus, le lien n'est pas affiche. Mais nettoie quand meme l'historique pour garder ta vue propre.

**[ECRAN — slide "Routine mensuelle recommandee"]**

Voici la routine que je recommande. Ca prend 20 minutes par mois.

**Semaine 1 : relancer le traitement.**
Lance le traitement pour integrer les nouveaux articles et les modifications. Les embeddings existants ne sont pas recalcules. Cout quasi nul.

**Semaine 2 : audit rapide de l'historique.**
Parcours les 10-20 derniers liens crees. Supprime les non pertinents. Verifie les ancres.

**Semaine 3 : verifier le rapport d'exclusions.**
Des articles orphelins sont peut-etre apparus. Verifie pourquoi et ajuste si necessaire.

**Semaine 4 : export CSV et comparaison.**
Exporte le CSV et compare avec le mois precedent. Les pages strategiques recoivent-elles plus de liens ? Les orphelins ont-ils ete corriges ?

**[ECRAN — slide "Mesurer l'impact SEO"]**

Pour mesurer si ton maillage fonctionne, voici les indicateurs a suivre.

**Google Search Console** : suis les impressions et les clics de tes pages strategiques. Un bon maillage fait monter les impressions en 4 a 8 semaines.

**Pages indexees** : tape "site:tonsite.com" dans Google. Le nombre de pages indexees devrait augmenter si tu avais des orphelins.

**Screaming Frog ou Ahrefs** : verifie la profondeur de crawl. Tes pages importantes devraient etre a 2-3 clics de la homepage, pas a 5-6.

**Google Analytics** : le nombre de pages par session devrait augmenter si tes liens internes guident bien les visiteurs.

Ne t'attends pas a des resultats en 48 heures. Le maillage interne est un levier de moyen terme. 4 a 12 semaines pour voir l'impact sur le classement.

**[ECRAN — slide "Le cout de maintenance"]**

Le cout de maintenance est quasi nul. Les embeddings ne sont pas recalcules. Seuls les nouveaux articles et les nouveaux liens generent des appels API.

Pour un site qui publie 4 articles par mois, le cout de maintenance est inferieur a 1 euro par mois. C'est le levier SEO le moins cher que tu puisses mettre en place.

**[TRANSITION — face camera]**

Tu as une routine, des indicateurs, et un maillage strategique. On passe au quiz final pour valider l'ensemble de la formation.

---

**Points cles** :
- Relancer apres chaque publication ou 1x/semaine
- Articles modifies en profondeur : verifier les liens et embeddings
- Routine mensuelle : traitement → audit historique → rapport exclusions → export CSV
- Impact SEO visible en 4-12 semaines
- Cout maintenance : <1€/mois pour un site avec 4 publications mensuelles

**Mots cles SEO** : maintenance maillage interne WordPress, routine SEO mensuelle, mesurer impact maillage interne

---

### Lecon 6.4 — Quiz final : valide tes acquis sur l'ensemble de la formation

**Duree** : 5 min
**Type** : Quiz TutorLMS (10 questions QCM)
**Voir plan de formation pour les questions**

---

## Notes de production generales

### Format video
- Avatar HeyGen (profil schoolsWP)
- Voix ElevenLabs (francais, voix clonee)
- Ecran : alternance face camera / screencast / slides

### Captures d'ecran a preparer
- Dashboard ECL (vide puis avec des liens)
- Reglages ECL complets (toutes les sections)
- Historique avec liens (bons et mauvais exemples)
- Rapport d'exclusions
- Pages strategiques configurees
- Metabox exclusions dans l'editeur WordPress
- platform.openai.com (API Keys, Billing, Usage)
- Export CSV dans Google Sheets
- Google Search Console (avant/apres)

### Sites de demo
- Site schoolsWP reel (avec 80+ articles)
- Les demos doivent montrer des donnees reelles, pas des exemples inventes

### Duree totale videos (hors quiz)
- M1 : 15 min (3 videos)
- M2 : 17 min (3 videos)
- M3 : 25 min (4 videos)
- M4 : 20 min (3 videos)
- M5 : 20 min (3 videos)
- M6 : 20 min (3 videos)
- **Total : 117 min (~2h de video)**
- Avec les quiz : ~2h27
