# Scripts video — Module 4 : Tracking, analytics et QR codes

**Formation** : Maitriser ClickWhale
**Module** : M4 — Tracking, analytics et QR codes (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~45 min
**Date** : 2026-03-23

---

### Lecon 4.1 — Comprends le tracking ClickWhale : ce qui est suivi et comment

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast du dashboard Statistics

---

**[INTRO — face camera]**

Tu as cree tes liens, tes pages de liens. Maintenant la question : est-ce que quelqu'un clique dessus ? Et sur lesquels ? Dans cette lecon, je t'explique exactement ce que ClickWhale suit, comment il le fait, et ou tu retrouves ces donnees.

**[ECRAN — screencast WordPress admin]**

[Navigation vers ClickWhale > Statistics dans le menu lateral]

Premiere bonne nouvelle : le tracking est actif par defaut des l'installation de ClickWhale. Tu n'as rien a configurer, rien a activer manuellement. Des que tu crees un lien et que quelqu'un clique dessus, ClickWhale enregistre l'information.

**[ECRAN — slide "Ce qui est tracke"]**

Qu'est-ce qui est enregistre exactement a chaque clic ?

Trois choses. Le timestamp — la date et l'heure exacte du clic. Le referrer — d'ou vient le visiteur qui a clique (Google, un article de ton site, un reseau social). Et le user agent — le type de navigateur et d'appareil utilise.

Ces trois donnees te permettent de repondre a trois questions : quand est-ce que les gens cliquent, d'ou ils viennent, et sur quel type d'appareil.

**[ECRAN — screencast du dashboard Statistics]**

[Montre le menu ClickWhale > Statistics]

Pour acceder a tes statistiques, va dans le menu lateral de WordPress, clique sur ClickWhale, puis sur Statistics. C'est ton tableau de bord de tracking. On va le detailler dans la lecon 4.3.

**[ECRAN — slide "RGPD et respect de la vie privee"]**

Point important sur la vie privee. ClickWhale ne depose aucun cookie sur le navigateur du visiteur. Pas de fingerprinting, pas de suivi entre les sessions. Chaque clic est enregistre de maniere isolee, sans identification du visiteur.

Ca veut dire quoi concretement ? Pas besoin de bandeau cookies supplementaire pour le tracking ClickWhale. Pas besoin de consentement specifique. Le tracking est conforme au RGPD de base.

Attention — ca ne te dispense pas d'avoir une politique de confidentialite sur ton site. Mais le tracking ClickWhale en lui-meme ne pose pas de probleme de conformite.

**[TRANSITION — face camera]**

Tu sais maintenant ce que ClickWhale suit et comment. Dans la prochaine lecon, je te montre comment activer ou desactiver ce tracking — et surtout dans quels cas tu voudrais le desactiver.

---

**Points cles** :
- Tracking actif par defaut — aucune configuration necessaire
- Donnees collectees : timestamp, referrer, user agent
- Pas de cookies, pas de fingerprinting — conforme RGPD de base
- Dashboard accessible via ClickWhale > Statistics

**Mots cles SEO** : tracking ClickWhale, statistiques clics WordPress, tracking liens affilies, ClickWhale analytics RGPD

---

### Lecon 4.2 — Active ou desactive le tracking (et pourquoi tu voudrais desactiver)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des settings

---

**[INTRO — face camera]**

Le tracking est actif par defaut, et dans 90% des cas tu vas le laisser comme ca. Mais il y a des situations ou tu veux le couper. Dans cette lecon, je te montre ou se trouve le reglage, comment l'utiliser, et surtout quand c'est pertinent de desactiver.

**[ECRAN — screencast WordPress admin]**

[Navigation vers ClickWhale > Settings > onglet Tracking]

Etape 1 : dans le menu lateral, va dans ClickWhale, puis Settings.

Etape 2 : clique sur l'onglet Tracking. Tu vois une option "Disable Tracking" avec une case a cocher.

[Montre la case a cocher]

Etape 3 : coche la case pour desactiver le tracking. Decoche-la pour le reactiver. Sauvegarde.

C'est tout. Un seul reglage, une seule case.

**[ECRAN — slide "Quand desactiver ?"]**

Dans quels cas tu voudrais desactiver le tracking ?

Premier cas : tu es sur un site de staging. Un site de staging, c'est une copie de ton site que tu utilises pour tester des modifications avant de les mettre en production. Sur ce site, tes propres clics de test pollueraient les statistiques. Desactive le tracking sur le staging.

Deuxieme cas : tu es sur un site de developpement local. Meme logique — les clics que tu fais pendant le dev ne sont pas des vrais clics utilisateurs.

Troisieme cas : conformite RGPD stricte. Si tu operes dans un contexte tres reglemente — sante, education, secteur public — et que ton DPO exige zero collecte de donnees de navigation, desactive le tracking. C'est rare, mais ca existe.

**[ECRAN — slide "Attention : consequences"]**

Un point critique a comprendre. Quand le tracking est desactive, aucune donnee n'est collectee. Zero. Et il n'y a pas de retour en arriere.

Si tu desactives le tracking pendant trois mois et que tu le reactives ensuite, tu auras un trou de trois mois dans tes statistiques. Les clics qui ont eu lieu pendant cette periode sont perdus definitivement.

Le tracking ne fonctionne pas comme un enregistrement en pause. C'est plutot comme une camera de surveillance : quand elle est eteinte, ce qui se passe n'est pas enregistre. Point.

**[ECRAN — slide "Recommandation"]**

Ma recommandation est simple.

En production — le site que tes visiteurs voient — laisse le tracking actif. Toujours.

Sur staging ou en dev — desactive-le pour ne pas polluer tes donnees.

Si tu as plusieurs installations WordPress (prod, staging, dev), verifie le reglage sur chacune independamment.

**[TRANSITION — face camera]**

Le tracking est en place. Dans la prochaine lecon, on rentre dans le vif : je te montre comment lire tes statistiques, identifier tes liens les plus performants, et reperer les pics d'activite.

---

**Points cles** :
- Reglage dans ClickWhale > Settings > onglet Tracking
- Une seule case a cocher : "Disable Tracking"
- Desactivation recommandee sur staging et dev uniquement
- Donnees non collectees pendant la desactivation = perdues definitivement
- En production : toujours laisser actif

**Mots cles SEO** : desactiver tracking ClickWhale, ClickWhale settings tracking, RGPD tracking WordPress

---

### Lecon 4.3 — Lis les statistiques : total clics, activite, top liens

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast complet du dashboard Statistics

---

**[INTRO — face camera]**

Tu as des liens, le tracking tourne. Maintenant il faut lire les donnees. Dans cette lecon, je te guide ecran par ecran dans le dashboard Statistics de ClickWhale. Tu vas apprendre a reperer tes liens les plus cliques, identifier les pics d'activite, et filtrer par periode.

**[ECRAN — screencast WordPress admin]**

[Navigation vers ClickWhale > Statistics]

Va dans ClickWhale, puis Statistics. C'est ton tableau de bord principal.

**[ECRAN — screencast vue d'ensemble]**

[Montre le chiffre "Total Clicks"]

En haut, tu vois le total de clics sur la periode selectionnee. C'est le nombre brut : combien de fois des visiteurs ont clique sur l'ensemble de tes liens ClickWhale.

Ce chiffre seul ne dit pas grand-chose. Ce qui compte, c'est son evolution dans le temps et sa repartition par lien. C'est ce qu'on va voir maintenant.

**[ECRAN — screencast timeline]**

[Montre le graphique d'activite jour par jour]

En dessous, tu as la timeline. C'est un graphique qui affiche l'activite des clics jour par jour. Chaque barre represente le nombre de clics pour une journee donnee.

Ce graphique te permet de reperer trois choses.

Les pics d'activite. Si tu publies un article le mardi et que tu vois un pic de clics le mercredi, c'est que ton article genere du trafic et que les gens cliquent sur tes liens. Le pic est directement lie a ta publication.

Les creux. Si tu vois des jours a zero clic, ca peut signifier que tes articles avec des liens ne recoivent pas de trafic, ou que tes liens sont mal positionnes dans le contenu.

Les tendances. Est-ce que tes clics augmentent semaine apres semaine ? Stagnent ? Diminuent ? La tendance sur 30 jours est plus fiable qu'un chiffre quotidien.

**[ECRAN — screencast top liens]**

[Montre le classement des liens les plus cliques]

En dessous de la timeline, tu as le classement de tes liens les plus cliques. C'est la vue la plus utile au quotidien.

Ce classement te dit exactement quels liens attirent le plus de clics. Si ton lien affilie TutorLMS a 150 clics et ton lien WP Rocket en a 8, la conclusion est claire : TutorLMS interesse beaucoup plus ton audience.

**[ECRAN — screencast filtres de periode]**

[Montre les filtres : 7 jours, 30 jours, custom]

Tu peux filtrer les statistiques par periode. Trois options : les 7 derniers jours, les 30 derniers jours, ou une periode personnalisee.

Pour une lecture hebdomadaire, utilise les 7 derniers jours. Pour un bilan mensuel, les 30 derniers jours. Et pour comparer deux mois entre eux, utilise la periode custom.

**[ECRAN — slide "Comment lire ses stats"]**

Voici comment je te recommande de lire tes statistiques.

Une fois par semaine, ouvre le dashboard, regarde les 7 derniers jours. Identifie le lien le plus clique de la semaine. Note si un pic correspond a une publication ou un partage sur les reseaux sociaux.

Une fois par mois, passe sur les 30 derniers jours. Compare avec le mois precedent. Est-ce que le total de clics augmente ? Quels liens montent, quels liens stagnent ?

C'est cette routine qui transforme tes donnees en decisions. On va approfondir l'analyse dans la lecon suivante.

**[TRANSITION — face camera]**

Tu sais lire tes statistiques. Dans la prochaine lecon, on va plus loin : je te montre comment croiser tes clics ClickWhale avec tes conversions reelles pour savoir quels liens affilies rapportent vraiment.

---

**Points cles** :
- Dashboard accessible via ClickWhale > Statistics
- Total clics = volume brut sur la periode
- Timeline = activite jour par jour (pics, creux, tendances)
- Top liens = classement des liens les plus cliques
- Filtres : 7 jours, 30 jours, ou periode personnalisee
- Routine recommandee : lecture hebdo + bilan mensuel

**Mots cles SEO** : statistiques ClickWhale, dashboard analytics WordPress, suivi clics liens affilies, ClickWhale statistics

---

### Lecon 4.4 — Analyse tes liens affilies : lesquels convertissent

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast ClickWhale + slides methode

---

**[INTRO — face camera]**

Un lien qui recoit beaucoup de clics mais zero conversion, ca ne rapporte rien. Dans cette lecon — contenu original schoolsWP, pas dans la doc officielle — je te montre comment croiser tes clics ClickWhale avec tes conversions reelles pour savoir quels liens affilies fonctionnent et lesquels sont a revoir.

**[ECRAN — slide "Clics vs Conversions"]**

Premiere distinction fondamentale. Un clic, c'est quelqu'un qui clique sur ton lien. Une conversion, c'est quelqu'un qui achete, s'inscrit ou realise l'action souhaitee chez l'affilieur. Ce sont deux choses differentes.

ClickWhale te donne les clics. L'affilieur te donne les conversions. Pour avoir une vue complete, tu dois croiser les deux.

**[ECRAN — slide "Le taux de conversion"]**

Le taux de conversion, c'est le ratio entre les deux. La formule est simple :

Taux de conversion = nombre de conversions divise par nombre de clics, multiplie par 100.

Exemple concret. Ton lien TutorLMS a recu 200 clics ce mois-ci dans ClickWhale. Sur le dashboard de l'affilieur TutorLMS, tu vois 4 ventes. Ton taux de conversion est de 2%.

**[ECRAN — slide "Benchmarks affiliation WordPress"]**

Est-ce que 2%, c'est bien ? Voici les reperes pour l'affiliation dans la niche WordPress.

Entre 1 et 3%, c'est normal. C'est le taux standard pour la plupart des programmes d'affiliation WordPress. Si tu es dans cette fourchette, tes liens fonctionnent correctement.

Au-dessus de 3%, c'est bon. Ton contenu est bien cible, ton audience fait confiance a ta recommandation.

En dessous de 1%, il y a un probleme a investiguer. On va voir lesquels.

**[ECRAN — slide "Dashboard mensuel du createur"]**

Voici la methode que j'utilise pour mon propre suivi mensuel. C'est un tableau simple avec quatre colonnes.

Colonne 1 : le nom du lien affilie. Colonne 2 : le nombre de clics ClickWhale sur le mois. Colonne 3 : le nombre de conversions chez l'affilieur. Colonne 4 : le taux de conversion calcule.

Tu peux faire ca dans un tableur, dans Notion, ou meme sur papier. L'important c'est de le faire chaque mois.

**[ECRAN — slide "Diagnostic : beaucoup de clics, 0 conversion"]**

Premier scenario problematique : tu as beaucoup de clics sur un lien mais zero conversion.

Verification numero 1 : le lien est-il correct ? Clique dessus toi-meme. Est-ce qu'il arrive sur la bonne page chez l'affilieur ? Un lien casse ou qui redirige vers une mauvaise page, ca arrive plus souvent qu'on croit.

Verification numero 2 : la landing page de l'affilieur fonctionne-t-elle ? Parfois, l'affilieur modifie sa page, change ses offres, ou desactive un produit. Ton lien marche, mais la page de destination ne convertit plus.

Verification numero 3 : le tracking affiliation est-il actif ? Verifie que ton tag d'affilie est bien dans l'URL. Si le parametre d'affiliation a saute — par exemple apres une modification du lien — tes ventes ne te sont pas attribuees.

**[ECRAN — slide "Diagnostic : 0 clics"]**

Deuxieme scenario : un lien a zero clic ou presque.

Deux causes principales. Le lien est mal place dans l'article. S'il est tout en bas d'un article de 3000 mots, la majorite des lecteurs ne le verront jamais. Remonte-le dans le premier tiers de l'article, pres d'un argument concret en faveur du produit.

Ou bien l'article lui-meme n'a pas de trafic. Un lien dans un article que personne ne lit ne recevra aucun clic. Verifie le trafic de l'article dans Google Search Console ou ton outil analytics.

**[ECRAN — slide "Actions correctives"]**

Pour resumer, voici tes actions correctives en fonction du diagnostic.

Beaucoup de clics, zero conversion : verifie le lien, la landing page, et le tracking affiliation.

Zero clics : repositionne le lien dans l'article ou travaille le trafic SEO de l'article.

Taux de conversion faible mais pas zero : le systeme fonctionne, optimise le contexte autour du lien. Un meilleur call-to-action, un argument plus concret, un temoignage.

**[TRANSITION — face camera]**

Tu as maintenant une methode pour analyser tes liens affilies au-dela du simple comptage de clics. Dans la prochaine lecon, on change de sujet : je te montre comment generer un QR code pour n'importe lequel de tes liens ClickWhale.

---

**Points cles** :
- Clics (ClickWhale) et conversions (affilieur) sont deux metriques distinctes
- Taux de conversion = conversions / clics x 100
- Benchmark WordPress : 1-3% = normal, >3% = bon, <1% = a investiguer
- Beaucoup de clics + 0 conversion → verifier lien, landing page, tracking
- 0 clics → repositionner le lien ou travailler le trafic de l'article
- Faire un bilan mensuel avec un tableau simple

**Mots cles SEO** : taux conversion affiliation WordPress, analyse liens affilies, ClickWhale conversions, optimiser affiliation WordPress

---

### Lecon 4.5 — Genere un QR code pour n'importe quel lien

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast complet de la generation

---

**[INTRO — face camera]**

Tu veux mettre un de tes liens sur un support physique — carte de visite, flyer, slide de presentation ? Il te faut un QR code. ClickWhale en genere un pour chacun de tes liens, directement depuis l'interface. Et l'avantage, c'est que les scans passent par ton lien ClickWhale, donc les clics sont trackes.

**[ECRAN — screencast WordPress admin]**

[Navigation vers ClickWhale > Links]

Etape 1 : va dans ClickWhale, puis Links. Tu retrouves la liste de tous tes liens.

[Clique sur "Edit" d'un lien existant]

Etape 2 : clique sur "Edit" pour ouvrir un lien existant. N'importe lequel — chaque lien peut avoir son QR code.

**[ECRAN — screencast editeur de lien]**

[Montre l'onglet General du lien]

Etape 3 : tu es dans l'onglet General du lien. En haut a droite, tu vois un bouton "Generate QR Code". Clique dessus.

[Clique sur "Generate QR Code"]

**[ECRAN — screencast modal QR code]**

[Montre la modal avec le QR code genere]

Le QR code apparait dans une fenetre modale. C'est une image vectorielle que tu peux telecharger.

Etape 4 : pour telecharger le QR code, fais un clic droit sur l'image, puis "Enregistrer l'image sous". Choisis l'emplacement sur ton ordinateur et sauvegarde.

[Demonstration du clic droit > sauvegarder l'image]

Le fichier est au format PNG. Tu peux l'utiliser directement dans tes supports : Canva, PowerPoint, InDesign, ou n'importe quel outil de mise en page.

**[ECRAN — slide "Ce que pointe le QR code"]**

Detail important : le QR code pointe vers ton lien ClickWhale, pas vers l'URL de destination finale. Ca veut dire que quand quelqu'un scanne le QR code, le clic passe d'abord par ClickWhale avant d'etre redirige.

Consequence : chaque scan est comptabilise dans tes statistiques, exactement comme un clic classique. Tu sais combien de personnes ont scanne ton QR code.

Et si tu changes l'URL de destination du lien plus tard, le QR code continue de fonctionner. Pas besoin de regenerer un nouveau QR code. C'est l'un des avantages majeurs d'utiliser des liens ClickWhale plutot que des QR codes generiques.

**[TRANSITION — face camera]**

Tu sais generer un QR code. Mais un QR code mal imprime ou mal dimensionne, personne ne le scannera. Dans la prochaine lecon, je te donne les bonnes pratiques pour que tes QR codes fonctionnent a tous les coups.

---

**Points cles** :
- Generation depuis ClickWhale > Links > Edit > onglet General > "Generate QR Code"
- Le QR code pointe vers le lien ClickWhale (clics trackes)
- Telecharger via clic droit > sauvegarder l'image (format PNG)
- Changer l'URL de destination ne casse pas le QR code
- Chaque scan = un clic comptabilise dans les statistiques

**Mots cles SEO** : QR code ClickWhale, generer QR code WordPress, QR code lien affilie, ClickWhale QR code tracking

---

### Lecon 4.6 — Bonnes pratiques QR codes : taille, contraste, test multi-devices

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides illustrees avec exemples visuels

---

**[INTRO — face camera]**

Un QR code que personne n'arrive a scanner, c'est du gaspillage. Dans cette lecon, je te donne les regles concretes pour que tes QR codes fonctionnent systematiquement — que ce soit sur une carte de visite, un flyer ou un ecran de presentation.

**[ECRAN — slide "Regle 1 : la taille minimum"]**

Premiere regle : la taille. Un QR code imprime doit faire au minimum 2 centimetres par 2 centimetres. En dessous, les cameras de smartphones anciens ou de mauvaise qualite ne pourront pas le lire.

Pour un support vu de loin — un roll-up, une affiche, un ecran de conference — augmente la taille proportionnellement. Sur un roll-up, vise au moins 10 centimetres de cote. La regle simple : plus le support est grand et vu de loin, plus le QR code doit etre grand.

**[ECRAN — slide "Regle 2 : le contraste"]**

Deuxieme regle : le contraste. Le QR code doit etre sombre sur fond clair. Noir sur blanc, c'est le standard. Bleu fonce sur blanc, ca marche aussi.

Ce qui ne marche pas : blanc sur fond sombre, couleurs claires sur couleurs claires, ou QR code avec peu de contraste entre le motif et le fond. La camera du telephone a besoin de distinguer nettement les modules noirs des espaces blancs.

Si tu veux integrer les couleurs de ta marque, garde le motif du QR code dans une couleur foncee et le fond dans une couleur tres claire. Ne fais jamais l'inverse.

**[ECRAN — slide "Regle 3 : la zone de silence"]**

Troisieme regle : la zone de silence. C'est l'espace blanc autour du QR code. Il doit etre d'au moins 4 modules de large. Un module, c'est un petit carre noir du QR code.

Concretement, ne colle pas de texte, de logo ou de bord de page directement contre le QR code. Laisse respirer. Si tu rognes la zone de silence, certains lecteurs de QR code ne detecteront pas le code.

**[ECRAN — slide "Regle 4 : le support d'impression"]**

Quatrieme regle : le support. Evite les surfaces reflechissantes — papier glace, plastification brillante, supports metalliques. Le reflet de la lumiere peut empecher la camera de lire le QR code.

Prefere les surfaces mates ou satinees. Pour les cartes de visite, un papier mat ou legerement texture fonctionne parfaitement.

**[ECRAN — slide "Regle 5 : tester"]**

Cinquieme regle — et la plus importante : teste toujours avant de diffuser.

Teste sur au moins deux appareils differents. Un iPhone et un Android, idealement. Les cameras et les applications de scan varient entre les appareils.

Teste dans les conditions reelles. Si ton QR code sera sur un roll-up dans une salle de conference, ne le teste pas uniquement a 20 centimetres de ton ecran. Recule-toi, simule la distance reelle.

Teste apres impression. Un QR code parfait a l'ecran peut devenir illisible une fois imprime si la qualite d'impression est basse ou si le papier absorbe trop d'encre.

**[ECRAN — slide "Cas d'usage concrets"]**

Ou utiliser tes QR codes concretement ?

Carte de visite : un QR code vers ta bio link page. Le contact scanne et a acces a tous tes liens en une seconde.

Roll-up ou banner pour une conference : un QR code vers ta page d'inscription ou ta landing page.

Flyer de formation : un QR code vers la page de vente ou un formulaire d'inscription.

Slides de presentation : un QR code en derniere slide — ou meme pendant la presentation — pour que les participants accedent a une ressource complementaire.

Dans tous les cas, ajoute un texte a cote du QR code qui explique ce que la personne va trouver en scannant. "Scanne pour acceder a la formation gratuite" est plus efficace qu'un QR code seul sans contexte.

**[TRANSITION — face camera]**

Tu as les regles pour des QR codes qui marchent a chaque fois. Dans la prochaine lecon, c'est a toi de jouer : tu vas analyser tes 5 liens les plus cliques et en tirer 3 conclusions actionnables.

---

**Points cles** :
- Taille minimum : 2x2 cm (plus grand si vu de loin)
- Contraste : motif sombre sur fond clair (jamais l'inverse)
- Zone de silence : au moins 4 modules d'espace blanc autour
- Support : surfaces mates, pas de papier glace
- Toujours tester sur plusieurs appareils avant diffusion
- Ajouter un texte explicatif a cote du QR code

**Mots cles SEO** : bonnes pratiques QR code, taille QR code impression, QR code carte de visite, QR code WordPress

---

### Lecon 4.7 — Exercice : Analyse tes 5 liens les plus cliques et tire 3 conclusions

**Type** : Exercice pratique (consignes ecrites)
**Duree estimee** : 20-30 min

---

## Objectif

Analyser les statistiques de tes liens ClickWhale et prendre des decisions basees sur les donnees. Cet exercice te met en situation reelle de pilotage de tes liens affilies et de tes liens internes.

## Prerequis

- Avoir au moins 5 liens actifs dans ClickWhale avec du trafic (idealement plusieurs semaines de donnees)
- Avoir acces aux dashboards de tes programmes d'affiliation (si tu as des liens affilies)

> Si tu n'as pas encore assez de donnees, utilise les donnees fictives fournies en fin d'exercice pour t'entrainer.

## Etapes

### 1. Identifie tes 5 liens les plus cliques

- Va dans ClickWhale > Statistics
- Selectionne la periode "30 derniers jours"
- Note les 5 liens avec le plus de clics dans un tableau :

| Rang | Lien | Clics (30j) | Type (affilie / interne / externe) |
|------|------|-------------|-----------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### 2. Croise avec les conversions (liens affilies uniquement)

- Pour chaque lien affilie dans ton top 5, connecte-toi au dashboard de l'affilieur
- Note le nombre de conversions sur la meme periode (30 jours)
- Calcule le taux de conversion : conversions / clics x 100

| Lien affilie | Clics ClickWhale | Conversions affilieur | Taux de conversion |
|-------------|------------------|----------------------|-------------------|
| | | | |
| | | | |

### 3. Analyse et tire 3 conclusions actionnables

Reponds a ces questions pour formuler tes conclusions :

- Quel lien a le meilleur taux de conversion ? Pourquoi ? (contenu de l'article, position du lien, pertinence du produit pour ton audience)
- Y a-t-il un lien avec beaucoup de clics mais zero conversion ? Quel est le probleme probable ?
- Y a-t-il un lien que tu pensais performant mais qui n'est pas dans le top 5 ? Pourquoi ?

Formule 3 conclusions sous cette forme :
- **Conclusion 1** : [constat] → [action concrete]
- **Conclusion 2** : [constat] → [action concrete]
- **Conclusion 3** : [constat] → [action concrete]

### Exemple de conclusions

- "Le lien TutorLMS est mon meilleur convertisseur (3.2%) — je dois le mettre en avant dans au moins 3 articles supplementaires ce mois-ci"
- "Le lien WP Rocket a 85 clics mais 0 conversion — je verifie que mon tag affilie est toujours actif et que la landing page fonctionne"
- "Mon lien vers la page Contact est dans le top 5 — mes lecteurs veulent me contacter, je devrais ajouter un formulaire de capture email sur cette page"

## Donnees fictives (si pas assez de donnees reelles)

| Rang | Lien | Clics (30j) | Conversions |
|------|------|-------------|-------------|
| 1 | TutorLMS (affilie) | 245 | 6 |
| 2 | FluentCRM (affilie) | 180 | 0 |
| 3 | Guide WordPress LMS (interne) | 156 | — |
| 4 | RankMath Pro (affilie) | 98 | 3 |
| 5 | Page Contact (interne) | 72 | — |

## Criteres de validation

- [ ] Tu as identifie tes 5 liens les plus cliques sur 30 jours
- [ ] Tu as croise les clics avec les conversions pour les liens affilies
- [ ] Tu as calcule le taux de conversion pour chaque lien affilie
- [ ] Tu as formule 3 conclusions actionnables (constat + action concrete)
- [ ] Chaque conclusion est basee sur des donnees, pas sur une intuition
- [ ] Au moins une conclusion concerne un lien a optimiser ou corriger

---

### Lecon 4.8 — Quiz : Valide tes acquis M4

**Type** : Quiz TutorLMS (8 questions)
**Seuil de reussite** : 80%

---

**Question 1** : Quelles donnees ClickWhale enregistre-t-il a chaque clic ?

- A) Nom, prenom et adresse email du visiteur
- B) Timestamp, referrer et user agent *(bonne reponse)*
- C) Adresse IP, geolocalisation et historique de navigation
- D) Cookies de session et empreinte numerique du navigateur

---

**Question 2** : Pourquoi le tracking ClickWhale est-il conforme au RGPD de base ?

- A) Parce que ClickWhale a obtenu une certification RGPD officielle
- B) Parce qu'il ne depose pas de cookies et ne fait pas de fingerprinting *(bonne reponse)*
- C) Parce qu'il anonymise automatiquement les adresses IP
- D) Parce qu'il demande le consentement avant chaque clic

---

**Question 3** : Dans quel cas est-il recommande de desactiver le tracking ?

- A) Quand tu as trop de clics et que la base de donnees est pleine
- B) Quand tu veux accelerer la vitesse de ton site
- C) Sur un site de staging ou de developpement *(bonne reponse)*
- D) Quand tu n'as pas de liens affilies

---

**Question 4** : Que se passe-t-il si tu desactives le tracking pendant un mois puis le reactives ?

- A) ClickWhale reconstitue les donnees manquantes a partir du cache
- B) Les clics du mois desactive sont perdus definitivement *(bonne reponse)*
- C) Les donnees sont mises en file d'attente et importees au reactiver
- D) Le tracking reprend avec un compteur remis a zero

---

**Question 5** : Quel est le taux de conversion normal pour l'affiliation dans la niche WordPress ?

- A) 10 a 15%
- B) 5 a 8%
- C) 1 a 3% *(bonne reponse)*
- D) Moins de 0.5%

---

**Question 6** : Un lien affilie recoit 120 clics mais 0 conversion. Quelle est la premiere verification a faire ?

- A) Desactiver le lien et en creer un nouveau
- B) Verifier que le lien est correct et que le tag affilie est bien present *(bonne reponse)*
- C) Contacter l'affilieur pour signaler un bug
- D) Augmenter le nombre de clics en ajoutant le lien dans plus d'articles

---

**Question 7** : Vers quoi pointe le QR code genere par ClickWhale ?

- A) Directement vers l'URL de destination finale
- B) Vers une page intermediaire ClickWhale avec publicite
- C) Vers le lien ClickWhale, donc les scans sont trackes *(bonne reponse)*
- D) Vers le dashboard Statistics pour que le visiteur voie les stats

---

**Question 8** : Quelle est la taille minimum recommandee pour un QR code imprime ?

- A) 1x1 cm
- B) 2x2 cm *(bonne reponse)*
- C) 5x5 cm
- D) La taille n'a pas d'importance si le contraste est bon
