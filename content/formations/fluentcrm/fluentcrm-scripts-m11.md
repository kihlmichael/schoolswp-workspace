# Scripts video — Module 11 : Recurring campaigns et newsletters

**Formation** : Maitriser FluentCRM
**Module** : M11 — Recurring campaigns et newsletters (Premium)
**Lecons** : 6 videos + 1 quiz
**Duree totale** : ~40 min
**Prerequis** : M10 (campagnes email classiques)
**Date** : 2026-03-23

---

### Lecon 11.1 — Comprends les recurring campaigns : newsletter en autopilote

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu publies des articles chaque semaine sur ton site WordPress. Tes abonnes les decouvrent par hasard — ou pas du tout. Tu pourrais creer une campagne email chaque vendredi, copier les liens, envoyer manuellement. Mais tu as mieux a faire. Les recurring campaigns de FluentCRM font exactement ca a ta place : elles envoient une newsletter automatique a la frequence que tu choisis, avec tes derniers contenus, sans que tu touches a quoi que ce soit. Dans cette lecon, tu comprends le principe et tu vois quand les utiliser.

**[ECRAN — screencast FluentCRM > Email Campaigns]**

[Montre la liste des campagnes, puis le bouton "Create Campaign"]

Etape 1 : dans FluentCRM, va dans Email Campaigns. Tu connais deja les campagnes classiques — tu en as cree dans les modules precedents. Ici, on s'interesse a un type specifique : la recurring campaign. Clique sur "Create Campaign" et observe les options disponibles.

[Montre l'option "Recurring Campaign" dans le selecteur de type]

Etape 2 : FluentCRM propose plusieurs types de campagnes. La recurring campaign est celle qui nous interesse. Contrairement a une campagne classique que tu envoies une fois, la recurring campaign se relance automatiquement selon un calendrier que tu definis.

**[ECRAN — slide "Campagne classique vs Recurring"]**

[Montre un tableau comparatif]

Voici la difference fondamentale.

Campagne classique : tu la crees, tu la configures, tu l'envoies. Terminee. Pour envoyer une nouvelle newsletter, tu recommences de zero.

Recurring campaign : tu la crees, tu la configures une fois. Elle s'envoie automatiquement — chaque semaine, chaque mois, ou a la frequence que tu veux. Le contenu se met a jour tout seul grace aux blocs dynamiques.

**[ECRAN — screencast FluentCRM]**

[Montre les blocs dynamiques disponibles dans l'editeur]

Etape 3 : la magie des recurring campaigns repose sur deux blocs dynamiques. Le bloc "Latest Post" — il tire automatiquement tes derniers articles WordPress. Et le bloc "RSS" — il tire du contenu depuis n'importe quel flux RSS, meme externe. On les verra en detail dans les prochaines lecons.

**[ECRAN — slide "3 cas d'usage schoolsWP"]**

[Montre 3 scenarios]

Quand utiliser une recurring campaign ? Trois scenarios concrets.

Scenario 1 : newsletter hebdo automatique. Chaque vendredi, tes abonnes recoivent les 3 derniers articles schoolsWP. Tu ne fais rien — la campagne tire les articles publies dans la semaine.

Scenario 2 : newsletter mensuelle etudiants premium. Chaque premier du mois, les etudiants premium recoivent un recap des nouveaux modules de formation ajoutes.

Scenario 3 : newsletter segmentee par pilier. Les abonnes interesses par le CRM recoivent uniquement les articles CRM. Ceux interesses par le SEO recoivent les articles SEO. Meme campagne, contenu different selon la categorie.

**[TRANSITION — face camera]**

La recurring campaign est la piece qui manque entre ton blog et ta liste email. Tu publies du contenu, FluentCRM le distribue. Pas de manipulation manuelle, pas d'oubli le vendredi soir. Dans la prochaine lecon, tu crees ta premiere recurring campaign de A a Z.

---

**Points cles** :
- Recurring campaign = campagne qui se relance automatiquement selon un calendrier
- Difference avec campagne classique : configuration unique, envois repetes
- Deux blocs dynamiques : Latest Post (articles WP) et RSS (flux externes)
- Cas d'usage : newsletter hebdo, recap mensuel, contenu segmente par categorie
- Zero intervention manuelle apres la configuration initiale

**Mots cles SEO** : FluentCRM recurring campaign, newsletter automatique WordPress, campagne recurrente FluentCRM, newsletter autopilote

---

### Lecon 11.2 — Cree ta premiere recurring campaign

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu sais ce qu'est une recurring campaign. Maintenant tu en crees une. L'objectif : une newsletter hebdomadaire qui part chaque vendredi a 9h a toute ta liste, avec tes derniers articles. Six etapes, et c'est en place.

**[ECRAN — screencast FluentCRM > Email Campaigns > Create Campaign]**

[Clique sur "Create Campaign", selectionne "Recurring Campaign"]

Etape 1 : va dans Email Campaigns, clique sur "Create Campaign". Selectionne le type "Recurring Campaign". Donne-lui un nom interne clair — par exemple "Newsletter Hebdo schoolsWP". Ce nom n'est pas visible par tes abonnes, il sert a t'y retrouver dans ta liste de campagnes.

[Montre le champ "Subject" et "Preview Text"]

Etape 2 : configure l'objet et le preview text. Pour une newsletter recurrente, tu peux utiliser des merge tags dynamiques. Par exemple : "Les nouveautes schoolsWP de cette semaine" ou "3 articles frais pour toi, {{contact.first_name}}". Le preview text apparait apres l'objet dans la boite de reception — utilise-le pour donner envie d'ouvrir.

**[ECRAN — screencast selection des destinataires]**

[Montre la selection des listes et segments]

Etape 3 : choisis tes destinataires. Selectionne la liste ou le segment qui doit recevoir cette newsletter. Pour une newsletter generale, c'est ta liste principale — par exemple "Abonnes Blog". Pour une newsletter segmentee, tu cibles un segment specifique.

[Montre les options d'exclusion]

Tu peux aussi exclure des segments. Par exemple, exclure les contacts qui ont le tag "desabonne-newsletter" ou ceux qui sont dans une automation de vente active — pour ne pas les bombarder.

**[ECRAN — screencast editeur de contenu]**

[Ouvre l'editeur visuel de la campagne]

Etape 4 : construis le template. C'est la structure de ta newsletter — elle sera reutilisee a chaque envoi. En haut, un header avec ton logo schoolsWP. En dessous, une intro courte — un ou deux paragraphes personnalises. Puis le bloc dynamique qui tire tes articles — on le configure en detail dans la lecon suivante. En bas, un footer avec le lien de desabonnement.

[Montre l'ajout d'un bloc texte pour l'intro]

L'intro peut etre statique — le meme texte chaque semaine — ou tu peux la personnaliser avec des merge tags. Pour commencer, un texte simple suffit : "Voici les derniers articles publies sur schoolsWP cette semaine."

**[ECRAN — screencast ajout du bloc Latest Post]**

[Montre l'insertion du bloc Latest Post]

Etape 5 : insere le bloc "Latest Post". C'est lui qui rend ta newsletter dynamique. A chaque envoi, il tire automatiquement les articles les plus recents. On verra tous ses parametres dans la lecon 11.3. Pour l'instant, insere-le avec les reglages par defaut.

**[ECRAN — screencast planification]**

[Montre les options de planification]

Etape 6 : planifie l'envoi. Selectionne la frequence — "Weekly". Choisis le jour — "Friday". Choisis l'heure — "09:00". Choisis le fuseau horaire — celui de ton audience principale. FluentCRM enverra automatiquement chaque vendredi a 9h.

[Active la campagne]

Valide et active la campagne. Elle est maintenant programmee. Chaque vendredi, FluentCRM va generer un nouvel email avec tes derniers articles et l'envoyer a ta liste.

**[TRANSITION — face camera]**

Ta premiere recurring campaign est en place. Elle va tourner chaque semaine sans intervention. Mais le bloc Latest Post a beaucoup de parametres qui changent tout — nombre d'articles, categorie, affichage. C'est ce qu'on voit dans la prochaine lecon.

---

**Points cles** :
- Creer une recurring campaign : type "Recurring" > sujet > destinataires > template > planification
- Nom interne clair pour s'y retrouver dans la liste des campagnes
- Merge tags dynamiques dans l'objet : {{contact.first_name}}
- Template reutilise a chaque envoi — structure fixe, contenu dynamique
- Possibilite d'exclure des segments pour eviter le sur-sollicitation

**Mots cles SEO** : creer recurring campaign FluentCRM, newsletter hebdomadaire WordPress, campagne recurrente email, FluentCRM newsletter setup

---

### Lecon 11.3 — Le bloc Latest Post : insere tes derniers articles automatiquement

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM editeur email

---

**[INTRO — face camera]**

Le bloc Latest Post est le moteur de ta newsletter automatique. C'est lui qui decide quels articles apparaissent, combien, et comment ils sont affiches. Bien configure, il transforme chaque envoi en une newsletter pertinente et a jour. Mal configure, il envoie du contenu en vrac sans logique. Dans cette lecon, tu maitrises chaque parametre.

**[ECRAN — screencast FluentCRM > editeur recurring campaign]**

[Ouvre la recurring campaign creee en 11.2, positionne sur le bloc Latest Post]

Etape 1 : ouvre ta recurring campaign et clique sur le bloc Latest Post pour acceder a ses parametres. Tu vas voir plusieurs options de configuration.

**[ECRAN — screencast parametres du bloc]**

[Montre le parametre "Number of posts"]

Etape 2 : nombre d'articles. C'est le premier parametre — combien d'articles afficher dans chaque newsletter. Pour une newsletter hebdomadaire, 3 est un bon chiffre. Assez pour offrir du choix, pas trop pour ne pas noyer le lecteur. Pour une newsletter mensuelle, tu peux monter a 5 ou 6.

[Montre le parametre "Post Type"]

Etape 3 : type de publication. Par defaut, le bloc tire les articles (post type "post"). Mais tu peux aussi tirer d'autres types de contenu — des pages, des produits WooCommerce, des cours TutorLMS. Pour une newsletter de contenu classique, reste sur "post".

[Montre le filtre par categorie]

Etape 4 : filtre par categorie. C'est le parametre le plus puissant. Tu peux limiter les articles a une ou plusieurs categories WordPress. Par exemple : uniquement les articles de la categorie "LMS". Ou uniquement "CRM" et "Automatisation".

Cas concret schoolsWP : tu as une recurring campaign pour chaque pilier thematique. La newsletter "LMS" tire uniquement les articles LMS. La newsletter "CRM" tire uniquement les articles CRM. Meme template, meme frequence, contenu different.

[Montre le filtre par tag WordPress]

Etape 5 : filtre par tag. En plus des categories, tu peux filtrer par tag WordPress. Par exemple, uniquement les articles tagges "tutoriel" ou "comparatif". Ca te permet de creer des newsletters thematiques tres ciblees.

**[ECRAN — screencast options d'affichage]**

[Montre les options d'affichage du bloc]

Etape 6 : options d'affichage. Tu controles ce qui apparait pour chaque article dans la newsletter. Image mise en avant — oui ou non. Extrait — le resume automatique ou les premiers mots de l'article. Auteur, date de publication. Bouton "Lire la suite" avec le lien vers l'article.

[Active l'image mise en avant et l'extrait]

Pour une newsletter visuellement engageante, active l'image mise en avant et l'extrait. Desactive la date et l'auteur — sauf si tu as plusieurs auteurs et que ca a du sens pour ton audience.

[Montre le rendu dans le preview]

Etape 7 : previsualise le resultat. FluentCRM affiche un apercu avec tes vrais articles. Verifie que le rendu correspond a ce que tu veux : les bonnes images, les bons titres, les extraits lisibles.

**[ECRAN — screencast cas specifique : aucun article nouveau]**

[Montre le comportement quand il n'y a pas de nouvel article]

Etape 8 : que se passe-t-il si tu n'as pas publie d'article cette semaine ? Le bloc Latest Post tire les articles les plus recents disponibles — meme si ce sont les memes que la semaine precedente. Pour eviter de renvoyer du contenu deja envoye, tu peux cocher l'option "Only posts published since last campaign" si elle est disponible dans ta version de FluentCRM. Sinon, maintiens un rythme de publication regulier.

**[TRANSITION — face camera]**

Le bloc Latest Post est ton meilleur allie pour une newsletter zero maintenance. Filtre par categorie pour segmenter, ajuste le nombre d'articles pour doser, et verifie le rendu dans le preview. Dans la prochaine lecon, on voit le bloc RSS — pour tirer du contenu depuis n'importe quel flux, y compris externe.

---

**Points cles** :
- Nombre d'articles : 3 pour une hebdo, 5-6 pour une mensuelle
- Filtre par categorie : une recurring campaign par pilier thematique
- Filtre par tag WordPress : newsletters thematiques ciblees
- Options d'affichage : image, extrait, lien "Lire la suite"
- Preview obligatoire avant activation pour verifier le rendu reel

**Mots cles SEO** : FluentCRM Latest Post bloc, newsletter articles automatique, recurring campaign WordPress contenu, FluentCRM filtre categorie

---

### Lecon 11.4 — Le bloc RSS : tire du contenu depuis n'importe quel flux

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM editeur email

---

**[INTRO — face camera]**

Le bloc Latest Post tire tes propres articles WordPress. Mais parfois, tu veux inclure du contenu externe dans ta newsletter — un article d'un partenaire, les dernieres actualites d'un outil que tu recommandes, ou ton propre contenu depuis un autre site. Le bloc RSS de FluentCRM fait exactement ca. Tu lui donnes un flux RSS, il tire les derniers elements et les affiche dans ta newsletter.

**[ECRAN — screencast FluentCRM > editeur recurring campaign]**

[Ouvre l'editeur, montre la barre de blocs]

Etape 1 : dans l'editeur de ta recurring campaign, cherche le bloc "RSS Content" ou "RSS Feed" dans les blocs disponibles. Insere-le a l'endroit ou tu veux afficher le contenu externe.

[Montre le champ URL du flux RSS]

Etape 2 : entre l'URL du flux RSS. Chaque site avec un blog a un flux RSS — generalement accessible a l'adresse `site.com/feed/`. Par exemple, pour inclure les dernieres actualites de WordPress.org : `https://wordpress.org/news/feed/`.

**[ECRAN — screencast configuration du bloc RSS]**

[Montre les parametres du bloc]

Etape 3 : configure le nombre d'elements a afficher. Comme pour le bloc Latest Post, 3 a 5 elements est un bon point de depart. Le bloc tire les elements les plus recents du flux.

[Montre les options d'affichage]

Etape 4 : configure l'affichage. Tu retrouves des options similaires au bloc Latest Post — titre, description, image si disponible dans le flux, lien vers l'article original. Le rendu depend de la qualite du flux RSS source. Certains flux incluent des images et des descriptions riches, d'autres uniquement le titre.

**[ECRAN — screencast cas d'usage concrets]**

[Montre une newsletter avec deux blocs : Latest Post + RSS]

Etape 5 : combine les blocs. Voici un cas concret schoolsWP. Ta newsletter hebdomadaire contient deux sections. Section 1 : "Nos derniers articles" — bloc Latest Post avec tes 3 derniers articles. Section 2 : "Veille WordPress" — bloc RSS avec les 2 dernieres actualites de WordPress.org ou d'un blog de reference dans ta niche.

[Montre un deuxieme exemple : flux RSS de ton propre podcast ou chaine YouTube]

Etape 6 : tu peux aussi utiliser le bloc RSS pour tirer ton propre contenu depuis une autre plateforme. Ton podcast a un flux RSS. Ta chaine YouTube a un flux RSS. Integre-les dans ta newsletter pour que tes abonnes decouvrent tous tes contenus, pas seulement tes articles.

**[ECRAN — screencast verification du flux]**

[Teste un flux RSS dans le navigateur]

Etape 7 : avant d'utiliser un flux RSS, verifie qu'il fonctionne. Colle l'URL dans ton navigateur — tu dois voir du contenu XML structure. Si la page affiche une erreur ou est vide, le flux ne fonctionne pas et le bloc RSS n'affichera rien dans ta newsletter.

**[TRANSITION — face camera]**

Le bloc RSS elargit les possibilites de ta newsletter au-dela de ton propre blog. Contenu partenaire, veille sectorielle, tes autres plateformes — tout peut etre integre automatiquement. Dans la prochaine lecon, on parle planification : comment choisir la bonne frequence et le bon timing pour tes recurring campaigns.

---

**Points cles** :
- Bloc RSS : tire du contenu depuis n'importe quel flux RSS valide
- URL type : site.com/feed/ pour les sites WordPress
- Combiner Latest Post + RSS dans une meme newsletter pour varier le contenu
- Verifier le flux dans le navigateur avant de l'integrer
- Cas d'usage : veille sectorielle, contenu partenaire, podcast, YouTube

**Mots cles SEO** : FluentCRM bloc RSS, newsletter flux RSS WordPress, recurring campaign contenu externe, RSS feed email marketing

---

### Lecon 11.5 — Planifie : hebdo, bimensuel, mensuel — choisis ta frequence

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Ta recurring campaign est configuree, le contenu est dynamique. Reste la question qui change tout : a quelle frequence envoyer ? Trop souvent, tu fatigues ta liste. Pas assez, on t'oublie. Et le jour et l'heure comptent autant que la frequence. Dans cette lecon, tu configures la planification optimale pour ta newsletter.

**[ECRAN — screencast FluentCRM > recurring campaign > onglet Schedule]**

[Ouvre les parametres de planification d'une recurring campaign]

Etape 1 : accede aux parametres de planification de ta recurring campaign. C'est ici que tu definis quand et a quelle frequence FluentCRM envoie ta newsletter.

[Montre les options de frequence]

Etape 2 : choisis ta frequence. FluentCRM propose plusieurs options.

Hebdomadaire — une fois par semaine. C'est le rythme le plus courant pour un blog actif. Tu publies au moins 2-3 articles par semaine, tes abonnes recoivent un recap chaque semaine.

Bimensuel — toutes les deux semaines. Bon compromis si tu publies moins souvent. Un article par semaine suffit pour alimenter une newsletter bimensuelle.

Mensuel — une fois par mois. Adapte aux recaps, aux newsletters premium, ou aux audiences qui ne veulent pas etre sollicitees souvent.

**[ECRAN — slide "Quelle frequence pour quel cas"]**

[Montre un tableau de decision]

Voici comment choisir.

Tu publies 2+ articles par semaine ? Newsletter hebdo. Tu as assez de contenu frais pour chaque envoi.

Tu publies 1 article par semaine ? Newsletter bimensuelle. Ca te donne 2-3 articles par envoi.

Tu publies 2-3 articles par mois ? Newsletter mensuelle. Un recap complet chaque mois.

Cas schoolsWP : la newsletter generale est hebdomadaire — 3 derniers articles chaque vendredi. La newsletter etudiants premium est mensuelle — recap des nouveaux modules le premier du mois.

**[ECRAN — screencast configuration du jour et de l'heure]**

[Montre la selection du jour de la semaine]

Etape 3 : choisis le jour d'envoi. Pour une newsletter hebdo, le mardi et le jeudi ont historiquement les meilleurs taux d'ouverture en B2B. Le vendredi fonctionne bien pour du contenu "a lire ce week-end". Evite le lundi — les boites de reception sont surchargees.

[Montre la selection de l'heure]

Etape 4 : choisis l'heure d'envoi. Deux creneaux fonctionnent bien : 9h-10h le matin (debut de journee, les gens checkent leurs emails) et 14h (retour de pause dejeuner). Teste les deux sur plusieurs semaines et compare les taux d'ouverture.

[Montre la selection du fuseau horaire]

Etape 5 : choisis le fuseau horaire. C'est un detail qui change les resultats. Si ton audience est francophone en France, selectionne Europe/Paris. Si tu as une audience internationale, choisis le fuseau de la majorite de tes abonnes. FluentCRM envoie selon ce fuseau — pas celui de ton serveur.

**[ECRAN — screencast modification d'une campagne active]**

[Montre comment modifier la planification d'une campagne deja active]

Etape 6 : tu peux modifier la planification d'une recurring campaign active a tout moment. Change le jour, l'heure ou la frequence — les prochains envois suivront la nouvelle planification. Les envois passes ne sont pas affectes.

**[TRANSITION — face camera]**

La frequence ideale depend de ton rythme de publication et de ton audience. Commence par une frequence, observe les metriques pendant un mois, ajuste si necessaire. Le taux de desabonnement est ton indicateur cle — s'il monte, tu envoies trop souvent. Dans la prochaine lecon, on organise tes campagnes avec les labels pour garder le controle quand tu en as plusieurs.

---

**Points cles** :
- Hebdomadaire : 2+ articles par semaine — adapte aux blogs actifs
- Bimensuel : 1 article par semaine — bon compromis
- Mensuel : 2-3 articles par mois — recaps et audiences selectionnees
- Jour d'envoi : mardi, jeudi ou vendredi selon le contexte
- Heure : 9h-10h ou 14h — tester et comparer
- Fuseau horaire : celui de la majorite de ton audience, pas celui du serveur

**Mots cles SEO** : frequence newsletter FluentCRM, planification recurring campaign, meilleur jour envoi newsletter, FluentCRM schedule email

---

### Lecon 11.6 — Organise tes campagnes avec les labels

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu as ta newsletter hebdo generale, ta newsletter mensuelle premium, ta campagne de veille sectorielle. Plus une campagne de bienvenue, une de reengagement, et trois campagnes de promotion. En quelques mois, ta liste de campagnes devient un mur de texte. Les campaign labels de FluentCRM resolvent ce probleme — ils te permettent de classer, filtrer et retrouver tes campagnes en quelques secondes.

**[ECRAN — screencast FluentCRM > Email Campaigns]**

[Montre une liste de campagnes sans labels — desordonnee]

Etape 1 : voici une liste de campagnes sans organisation. Newsletters, promotions, sequences de bienvenue — tout est melange. Pour retrouver ta recurring campaign mensuelle, tu scrolles, tu lis les noms un par un. Pas efficace.

[Montre le menu des labels]

Etape 2 : dans la page des campagnes, repere la section labels. FluentCRM te permet de creer des labels pour categoriser tes campagnes. Clique sur "Add Label" ou "Manage Labels".

**[ECRAN — screencast creation des labels]**

[Cree un premier label]

Etape 3 : cree tes labels. Voici une structure qui fonctionne pour schoolsWP.

Label "Newsletter" — pour toutes les recurring campaigns de type newsletter.
Label "Promotion" — pour les campagnes de vente et offres speciales.
Label "Onboarding" — pour les sequences de bienvenue.
Label "Reengagement" — pour les campagnes de win-back.

[Cree les 4 labels avec des couleurs distinctes]

Donne a chaque label une couleur distincte. Les couleurs rendent le tri visuel immediat — tu vois d'un coup d'oeil quelles campagnes sont des newsletters, des promotions ou de l'onboarding.

**[ECRAN — screencast application des labels]**

[Selectionne une recurring campaign et lui assigne un label]

Etape 4 : assigne les labels a tes campagnes. Ouvre une campagne, ou selectionne-la dans la liste, et attribue-lui le label correspondant. Ta "Newsletter Hebdo schoolsWP" recoit le label "Newsletter". Ta "Promo Black Friday" recoit le label "Promotion".

[Montre l'assignation de label sur plusieurs campagnes]

Tu peux assigner un label a plusieurs campagnes en une fois si FluentCRM le permet dans ta version. Sinon, fais-le campagne par campagne — ca prend 30 secondes chacune.

**[ECRAN — screencast filtrage par label]**

[Montre le filtre par label dans la liste des campagnes]

Etape 5 : filtre par label. C'est la ou les labels prennent tout leur sens. Clique sur le label "Newsletter" — tu ne vois que tes recurring campaigns. Clique sur "Promotion" — uniquement les campagnes de vente. Tu passes d'un mur de 30 campagnes a une liste filtree de 5.

[Montre le filtre en action avec differents labels]

Quand tu geres 10, 20, 50 campagnes, ce filtrage devient indispensable. Tu retrouves n'importe quelle campagne en deux clics.

**[ECRAN — slide "Convention de nommage"]**

[Montre un tableau avec la convention]

Etape 6 : combine les labels avec une convention de nommage claire. Voici la methode schoolsWP.

Format : [Type] Nom descriptif — Frequence
Exemples :
- "[NL] Articles Hebdo schoolsWP — Weekly"
- "[NL] Recap Premium — Monthly"
- "[PROMO] Black Friday 2026 — One-shot"
- "[OB] Bienvenue Nouveaux Abonnes — Triggered"

Labels + nommage coherent = tu retrouves n'importe quelle campagne en moins de 5 secondes, meme avec des dizaines de campagnes.

**[TRANSITION — face camera]**

Les labels sont un petit investissement de temps qui rapporte gros quand ta liste de campagnes grandit. Cree tes labels des maintenant, assigne-les a tes campagnes existantes, et adopte une convention de nommage. Tu gagneras du temps chaque semaine. Dernier arret de ce module : le quiz pour valider tes acquis.

---

**Points cles** :
- Campaign labels : classement visuel par couleur et categorie
- Structure recommandee : Newsletter, Promotion, Onboarding, Reengagement
- Filtrage par label : retrouver une campagne en 2 clics parmi des dizaines
- Convention de nommage : [Type] Nom — Frequence
- Combiner labels + nommage pour une organisation zero friction

**Mots cles SEO** : FluentCRM campaign labels, organiser campagnes email, labels email marketing, FluentCRM organisation campagnes

---

### Lecon 11.7 — Quiz : Valide tes acquis M11

**Duree** : 8 min
**Type** : Quiz TutorLMS (8 QCM)
**Format** : Questions affichees dans TutorLMS, pas de video

---

**Question 1** : Quelle est la difference fondamentale entre une campagne classique et une recurring campaign dans FluentCRM ?

- A) La campagne classique est gratuite, la recurring campaign est payante
- B) La campagne classique s'envoie une fois, la recurring campaign se relance automatiquement selon un calendrier ✅
- C) La recurring campaign ne peut envoyer que des articles de blog
- D) La campagne classique ne peut pas utiliser de merge tags

**Explication** : Une campagne classique est un envoi unique. Une recurring campaign se relance automatiquement a la frequence definie (hebdo, bimensuel, mensuel) avec du contenu mis a jour dynamiquement.

---

**Question 2** : Tu veux creer une newsletter qui envoie automatiquement tes 3 derniers articles WordPress chaque semaine. Quel bloc utilises-tu ?

- A) Le bloc "Dynamic Content"
- B) Le bloc "RSS Feed"
- C) Le bloc "Latest Post" ✅
- D) Le bloc "Post Notification"

**Explication** : Le bloc Latest Post tire automatiquement les derniers articles publies sur ton site WordPress. Le bloc RSS sert pour le contenu externe ou les flux d'autres plateformes.

---

**Question 3** : Quel est l'avantage principal du filtre par categorie dans le bloc Latest Post ?

- A) Il accelere le temps de chargement de l'email
- B) Il permet de creer des newsletters segmentees par thematique sans dupliquer le template ✅
- C) Il empeche les articles en brouillon d'apparaitre
- D) Il trie les articles par nombre de commentaires

**Explication** : Le filtre par categorie te permet d'avoir une recurring campaign par pilier thematique (LMS, CRM, SEO) avec le meme template mais du contenu different selon la categorie filtree.

---

**Question 4** : Tu veux inclure les dernieres actualites de WordPress.org dans ta newsletter. Quel bloc utilises-tu et quelle URL entres-tu ?

- A) Bloc Latest Post avec l'URL wordpress.org
- B) Bloc RSS avec l'URL https://wordpress.org/news/feed/ ✅
- C) Bloc HTML avec un iframe vers wordpress.org
- D) Bloc Latest Post avec le filtre "External Sources"

**Explication** : Le bloc RSS tire du contenu depuis n'importe quel flux RSS valide. L'URL du flux WordPress.org est https://wordpress.org/news/feed/. Le bloc Latest Post ne fonctionne qu'avec le contenu de ton propre site.

---

**Question 5** : Tu publies 1 article par semaine sur ton blog. Quelle frequence de recurring campaign est la plus adaptee ?

- A) Quotidienne — pour maximiser la visibilite
- B) Hebdomadaire — un article par envoi suffit
- C) Bimensuelle — ca te donne 2-3 articles par envoi ✅
- D) La frequence n'a aucun impact sur les resultats

**Explication** : Avec 1 article par semaine, une newsletter bimensuelle te donne 2-3 articles par envoi — assez pour offrir de la valeur a chaque email. Une hebdo avec un seul article peut paraitre legere.

---

**Question 6** : Quel indicateur te signale que tu envoies tes newsletters trop frequemment ?

- A) Le taux d'ouverture augmente
- B) Le taux de desabonnement augmente ✅
- C) Le taux de clic reste stable
- D) Le nombre de nouveaux abonnes diminue

**Explication** : Un taux de desabonnement en hausse est le signal le plus direct que ta frequence est trop elevee. Si tes abonnes partent, reduis la cadence.

---

**Question 7** : Quelle convention de nommage est recommandee pour organiser tes campagnes FluentCRM ?

- A) Utiliser uniquement des numeros : "Campaign 001", "Campaign 002"
- B) [Type] Nom descriptif — Frequence, avec des labels couleur par categorie ✅
- C) Le nom de l'auteur suivi de la date : "Michael_2026-03-23"
- D) Pas de convention — FluentCRM trie automatiquement par pertinence

**Explication** : La convention [Type] Nom — Frequence combinee aux labels couleur permet de retrouver n'importe quelle campagne en quelques secondes, meme avec des dizaines de campagnes.

---

**Question 8** : Tu as une recurring campaign active et tu veux changer le jour d'envoi du vendredi au mardi. Que se passe-t-il ?

- A) Tu dois desactiver la campagne, en creer une nouvelle, et supprimer l'ancienne
- B) Les prochains envois suivront la nouvelle planification, les envois passes ne sont pas affectes ✅
- C) FluentCRM envoie un email supplementaire le mardi suivant pour compenser
- D) La modification est impossible sur une campagne active

**Explication** : Tu peux modifier la planification d'une recurring campaign active a tout moment. Les prochains envois suivront la nouvelle planification. Aucun impact sur les emails deja envoyes.

---

**Seuil de reussite** : 6/8 (75%)

**Message de reussite** : Module 11 valide. Tu maitrises les recurring campaigns FluentCRM : configuration, blocs dynamiques (Latest Post et RSS), planification et organisation par labels. Le module 12 t'attend pour passer aux integrations FluentCRM avec les autres outils de ton stack WordPress.

**Message d'echec** : Tu n'as pas atteint le seuil de 75%. Revois les lecons 11.1 a 11.6, en particulier les differences entre les blocs Latest Post et RSS, et les criteres de choix de frequence. Tu peux retenter le quiz autant de fois que necessaire.
