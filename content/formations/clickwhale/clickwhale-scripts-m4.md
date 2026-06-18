# Scripts vidéo - Module 4 : Tracking, analytics et QR codes

**Formation** : Maîtriser ClickWhale
**Module** : M4 - Tracking, analytics et QR codes (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~45 min
**Date** : 2026-03-23

---

### Leçon 4.1 : Comprends le tracking ClickWhale : ce qui est suivi et comment

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast du dashboard Statistics

---

**[INTRO - face caméra]**

Tu as créé tes liens, tes pages de liens. Maintenant la question : est-ce que quelqu'un clique dessus ? Et sur lesquels ? Dans cette leçon, je t'explique exactement ce que ClickWhale suit, comment il le fait, et où tu retrouves ces données.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers ClickWhale > Statistics dans le menu latéral]

Première bonne nouvelle : le tracking est actif par défaut dès l'installation de ClickWhale. Tu n'as rien à configurer, rien à activer manuellement. Dès que tu crées un lien et que quelqu'un clique dessus, ClickWhale enregistre l'information.

**[ÉCRAN - slide "Ce qui est tracké"]**

Qu'est-ce qui est enregistré exactement à chaque clic ?

Trois choses. Le timestamp - la date et l'heure exacte du clic. Le referrer - d'où vient le visiteur qui a cliqué (Google, un article de ton site, un réseau social). Et le user agent - le type de navigateur et d'appareil utilisé.

Ces trois données te permettent de répondre à trois questions : quand est-ce que les gens cliquent, d'où ils viennent, et sur quel type d'appareil.

**[ÉCRAN - screencast du dashboard Statistics]**

[Montre le menu ClickWhale > Statistics]

Pour accéder à tes statistiques, va dans le menu latéral de WordPress, clique sur ClickWhale, puis sur Statistics. C'est ton tableau de bord de tracking. On va le détailler dans la leçon 4.3.

**[ÉCRAN - slide "RGPD et respect de la vie privée"]**

Point important sur la vie privée. ClickWhale ne dépose aucun cookie sur le navigateur du visiteur. Pas de fingerprinting, pas de suivi entre les sessions. Chaque clic est enregistré de manière isolée, sans identification du visiteur.

Ça veut dire quoi concrètement ? Pas besoin de bandeau cookies supplémentaire pour le tracking ClickWhale. Pas besoin de consentement spécifique. Le tracking est conforme au RGPD de base.

Attention - ça ne te dispense pas d'avoir une politique de confidentialité sur ton site. Mais le tracking ClickWhale en lui-même ne pose pas de problème de conformité.

**[TRANSITION - face caméra]**

Tu sais maintenant ce que ClickWhale suit et comment. Dans la prochaine leçon, je te montre comment activer ou désactiver ce tracking - et surtout dans quels cas tu voudrais le désactiver.

---

**Points clés** :
- Tracking actif par défaut - aucune configuration nécessaire
- Données collectées : timestamp, referrer, user agent
- Pas de cookies, pas de fingerprinting - conforme RGPD de base
- Dashboard accessible via ClickWhale > Statistics

**Mots-clés SEO** : tracking ClickWhale, statistiques clics WordPress, tracking liens affiliés, ClickWhale analytics RGPD

---

### Leçon 4.2 : Active ou désactive le tracking (et pourquoi tu voudrais désactiver)

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast des settings

---

**[INTRO - face caméra]**

Le tracking est actif par défaut, et dans 90% des cas tu vas le laisser comme ça. Mais il y a des situations où tu veux le couper. Dans cette leçon, je te montre où se trouve le réglage, comment l'utiliser, et surtout quand c'est pertinent de désactiver.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers ClickWhale > Settings > onglet Tracking]

Étape 1 : dans le menu latéral, va dans ClickWhale, puis Settings.

Étape 2 : clique sur l'onglet Tracking. Tu vois une option "Disable Tracking" avec une case à cocher.

[Montre la case à cocher]

Étape 3 : coche la case pour désactiver le tracking. Décoche-la pour le réactiver. Sauvegarde.

C'est tout. Un seul réglage, une seule case.

**[ÉCRAN - slide "Quand désactiver ?"]**

Dans quels cas tu voudrais désactiver le tracking ?

Premier cas : tu es sur un site de staging. Un site de staging, c'est une copie de ton site que tu utilises pour tester des modifications avant de les mettre en production. Sur ce site, tes propres clics de test pollueraient les statistiques. Désactive le tracking sur le staging.

Deuxième cas : tu es sur un site de développement local. Même logique - les clics que tu fais pendant le dev ne sont pas des vrais clics utilisateurs.

Troisième cas : conformité RGPD stricte. Si tu opères dans un contexte très réglementé - santé, éducation, secteur public - et que ton DPO exige zéro collecte de données de navigation, désactive le tracking. C'est rare, mais ça existe.

**[ÉCRAN - slide "Attention : conséquences"]**

Un point critique à comprendre. Quand le tracking est désactivé, aucune donnée n'est collectée. Zéro. Et il n'y a pas de retour en arrière.

Si tu désactives le tracking pendant trois mois et que tu le réactives ensuite, tu auras un trou de trois mois dans tes statistiques. Les clics qui ont eu lieu pendant cette période sont perdus définitivement.

Le tracking ne fonctionne pas comme un enregistrement en pause. C'est plutôt comme une caméra de surveillance : quand elle est éteinte, ce qui se passe n'est pas enregistré. Point.

**[ÉCRAN - slide "Recommandation"]**

Ma recommandation est simple.

En production - le site que tes visiteurs voient - laisse le tracking actif. Toujours.

Sur staging ou en dev - désactive-le pour ne pas polluer tes données.

Si tu as plusieurs installations WordPress (prod, staging, dev), vérifie le réglage sur chacune indépendamment.

**[TRANSITION - face caméra]**

Le tracking est en place. Dans la prochaine leçon, on rentre dans le vif : je te montre comment lire tes statistiques, identifier tes liens les plus performants, et repérer les pics d'activité.

---

**Points clés** :
- Réglage dans ClickWhale > Settings > onglet Tracking
- Une seule case à cocher : "Disable Tracking"
- Désactivation recommandée sur staging et dev uniquement
- Données non collectées pendant la désactivation = perdues définitivement
- En production : toujours laisser actif

**Mots-clés SEO** : désactiver tracking ClickWhale, ClickWhale settings tracking, RGPD tracking WordPress

---

### Leçon 4.3 : Lis les statistiques : total clics, activité, top liens

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast complet du dashboard Statistics

---

**[INTRO - face caméra]**

Tu as des liens, le tracking tourne. Maintenant il faut lire les données. Dans cette leçon, je te guide écran par écran dans le dashboard Statistics de ClickWhale. Tu vas apprendre à repérer tes liens les plus cliqués, identifier les pics d'activité, et filtrer par période.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers ClickWhale > Statistics]

Va dans ClickWhale, puis Statistics. C'est ton tableau de bord principal.

**[ÉCRAN - screencast vue d'ensemble]**

[Montre le chiffre "Total Clicks"]

En haut, tu vois le total de clics sur la période sélectionnée. C'est le nombre brut : combien de fois des visiteurs ont cliqué sur l'ensemble de tes liens ClickWhale.

Ce chiffre seul ne dit pas grand-chose. Ce qui compte, c'est son évolution dans le temps et sa répartition par lien. C'est ce qu'on va voir maintenant.

**[ÉCRAN - screencast timeline]**

[Montre le graphique d'activité jour par jour]

En dessous, tu as la timeline. C'est un graphique qui affiche l'activité des clics jour par jour. Chaque barre représente le nombre de clics pour une journée donnée.

Ce graphique te permet de repérer trois choses.

Les pics d'activité. Si tu publies un article le mardi et que tu vois un pic de clics le mercredi, c'est que ton article génère du trafic et que les gens cliquent sur tes liens. Le pic est directement lié à ta publication.

Les creux. Si tu vois des jours à zéro clic, ça peut signifier que tes articles avec des liens ne reçoivent pas de trafic, ou que tes liens sont mal positionnés dans le contenu.

Les tendances. Est-ce que tes clics augmentent semaine après semaine ? Stagnent ? Diminuent ? La tendance sur 30 jours est plus fiable qu'un chiffre quotidien.

**[ÉCRAN - screencast top liens]**

[Montre le classement des liens les plus cliqués]

En dessous de la timeline, tu as le classement de tes liens les plus cliqués. C'est la vue la plus utile au quotidien.

Ce classement te dit exactement quels liens attirent le plus de clics. Si ton lien affilié TutorLMS a 150 clics et ton lien WP Rocket en a 8, la conclusion est claire : TutorLMS intéresse beaucoup plus ton audience.

**[ÉCRAN - screencast filtres de période]**

[Montre les filtres : 7 jours, 30 jours, custom]

Tu peux filtrer les statistiques par période. Trois options : les 7 derniers jours, les 30 derniers jours, ou une période personnalisée.

Pour une lecture hebdomadaire, utilise les 7 derniers jours. Pour un bilan mensuel, les 30 derniers jours. Et pour comparer deux mois entre eux, utilise la période custom.

**[ÉCRAN - slide "Comment lire ses stats"]**

Voici comment je te recommande de lire tes statistiques.

Une fois par semaine, ouvre le dashboard, regarde les 7 derniers jours. Identifie le lien le plus cliqué de la semaine. Note si un pic correspond à une publication ou un partage sur les réseaux sociaux.

Une fois par mois, passe sur les 30 derniers jours. Compare avec le mois précédent. Est-ce que le total de clics augmente ? Quels liens montent, quels liens stagnent ?

C'est cette routine qui transforme tes données en décisions. On va approfondir l'analyse dans la leçon suivante.

**[TRANSITION - face caméra]**

Tu sais lire tes statistiques. Dans la prochaine leçon, on va plus loin : je te montre comment croiser tes clics ClickWhale avec tes conversions réelles pour savoir quels liens affiliés rapportent vraiment.

---

**Points clés** :
- Dashboard accessible via ClickWhale > Statistics
- Total clics = volume brut sur la période
- Timeline = activité jour par jour (pics, creux, tendances)
- Top liens = classement des liens les plus cliqués
- Filtres : 7 jours, 30 jours, ou période personnalisée
- Routine recommandée : lecture hebdo + bilan mensuel

**Mots-clés SEO** : statistiques ClickWhale, dashboard analytics WordPress, suivi clics liens affiliés, ClickWhale statistics

---

### Leçon 4.4 : Analyse tes liens affiliés : lesquels convertissent

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast ClickWhale + slides méthode

---

**[INTRO - face caméra]**

Un lien qui reçoit beaucoup de clics mais zéro conversion, ça ne rapporte rien. Dans cette leçon - contenu original schoolsWP, pas dans la doc officielle - je te montre comment croiser tes clics ClickWhale avec tes conversions réelles pour savoir quels liens affiliés fonctionnent et lesquels sont à revoir.

**[ÉCRAN - slide "Clics vs Conversions"]**

Première distinction fondamentale. Un clic, c'est quelqu'un qui clique sur ton lien. Une conversion, c'est quelqu'un qui achète, s'inscrit ou réalise l'action souhaitée chez l'affilieur. Ce sont deux choses différentes.

ClickWhale te donne les clics. L'affilieur te donne les conversions. Pour avoir une vue complète, tu dois croiser les deux.

**[ÉCRAN - slide "Le taux de conversion"]**

Le taux de conversion, c'est le ratio entre les deux. La formule est simple :

Taux de conversion = nombre de conversions divisé par nombre de clics, multiplié par 100.

Exemple concret. Ton lien TutorLMS a reçu 200 clics ce mois-ci dans ClickWhale. Sur le dashboard de l'affilieur TutorLMS, tu vois 4 ventes. Ton taux de conversion est de 2%.

**[ÉCRAN - slide "Benchmarks affiliation WordPress"]**

Est-ce que 2%, c'est bien ? Voici les repères pour l'affiliation dans la niche WordPress.

Entre 1 et 3%, c'est normal. C'est le taux standard pour la plupart des programmes d'affiliation WordPress. Si tu es dans cette fourchette, tes liens fonctionnent correctement.

Au-dessus de 3%, c'est bon. Ton contenu est bien ciblé, ton audience fait confiance à ta recommandation.

En dessous de 1%, il y a un problème à investiguer. On va voir lesquels.

**[ÉCRAN - slide "Dashboard mensuel du créateur"]**

Voici la méthode que j'utilise pour mon propre suivi mensuel. C'est un tableau simple avec quatre colonnes.

Colonne 1 : le nom du lien affilié. Colonne 2 : le nombre de clics ClickWhale sur le mois. Colonne 3 : le nombre de conversions chez l'affilieur. Colonne 4 : le taux de conversion calculé.

Tu peux faire ça dans un tableur, dans Notion, ou même sur papier. L'important c'est de le faire chaque mois.

**[ÉCRAN - slide "Diagnostic : beaucoup de clics, 0 conversion"]**

Premier scénario problématique : tu as beaucoup de clics sur un lien mais zéro conversion.

Vérification numéro 1 : le lien est-il correct ? Clique dessus toi-même. Est-ce qu'il arrive sur la bonne page chez l'affilieur ? Un lien cassé ou qui redirige vers une mauvaise page, ça arrive plus souvent qu'on croit.

Vérification numéro 2 : la landing page de l'affilieur fonctionne-t-elle ? Parfois, l'affilieur modifie sa page, change ses offres, ou désactive un produit. Ton lien marche, mais la page de destination ne convertit plus.

Vérification numéro 3 : le tracking affiliation est-il actif ? Vérifie que ton tag d'affilié est bien dans l'URL. Si le paramètre d'affiliation a sauté - par exemple après une modification du lien - tes ventes ne te sont pas attribuées.

**[ÉCRAN - slide "Diagnostic : 0 clics"]**

Deuxième scénario : un lien à zéro clic ou presque.

Deux causes principales. Le lien est mal placé dans l'article. S'il est tout en bas d'un article de 3000 mots, la majorité des lecteurs ne le verront jamais. Remonte-le dans le premier tiers de l'article, près d'un argument concret en faveur du produit.

Ou bien l'article lui-même n'a pas de trafic. Un lien dans un article que personne ne lit ne recevra aucun clic. Vérifie le trafic de l'article dans Google Search Console ou ton outil analytics.

**[ÉCRAN - slide "Actions correctives"]**

Pour résumer, voici tes actions correctives en fonction du diagnostic.

Beaucoup de clics, zéro conversion : vérifie le lien, la landing page, et le tracking affiliation.

Zéro clics : repositionne le lien dans l'article ou travaille le trafic SEO de l'article.

Taux de conversion faible mais pas zéro : le système fonctionne, optimise le contexte autour du lien. Un meilleur call-to-action, un argument plus concret, un témoignage.

**[TRANSITION - face caméra]**

Tu as maintenant une méthode pour analyser tes liens affiliés au-delà du simple comptage de clics. Dans la prochaine leçon, on change de sujet : je te montre comment générer un QR code pour n'importe lequel de tes liens ClickWhale.

---

**Points clés** :
- Clics (ClickWhale) et conversions (affilieur) sont deux métriques distinctes
- Taux de conversion = conversions / clics x 100
- Benchmark WordPress : 1-3% = normal, >3% = bon, <1% = à investiguer
- Beaucoup de clics + 0 conversion → vérifier lien, landing page, tracking
- 0 clics → repositionner le lien ou travailler le trafic de l'article
- Faire un bilan mensuel avec un tableau simple

**Mots-clés SEO** : taux conversion affiliation WordPress, analyse liens affiliés, ClickWhale conversions, optimiser affiliation WordPress

---

### Leçon 4.5 : Génère un QR code pour n'importe quel lien

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast complet de la génération

---

**[INTRO - face caméra]**

Tu veux mettre un de tes liens sur un support physique - carte de visite, flyer, slide de présentation ? Il te faut un QR code. ClickWhale en génère un pour chacun de tes liens, directement depuis l'interface. Et l'avantage, c'est que les scans passent par ton lien ClickWhale, donc les clics sont trackés.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers ClickWhale > Links]

Étape 1 : va dans ClickWhale, puis Links. Tu retrouves la liste de tous tes liens.

[Clique sur "Edit" d'un lien existant]

Étape 2 : clique sur "Edit" pour ouvrir un lien existant. N'importe lequel - chaque lien peut avoir son QR code.

**[ÉCRAN - screencast éditeur de lien]**

[Montre l'onglet General du lien]

Étape 3 : tu es dans l'onglet General du lien. En haut à droite, tu vois un bouton "Generate QR Code". Clique dessus.

[Clique sur "Generate QR Code"]

**[ÉCRAN - screencast modal QR code]**

[Montre la modal avec le QR code généré]

Le QR code apparaît dans une fenêtre modale. C'est une image vectorielle que tu peux télécharger.

Étape 4 : pour télécharger le QR code, fais un clic droit sur l'image, puis "Enregistrer l'image sous". Choisis l'emplacement sur ton ordinateur et sauvegarde.

[Démonstration du clic droit > sauvegarder l'image]

Le fichier est au format PNG. Tu peux l'utiliser directement dans tes supports : Canva, PowerPoint, InDesign, ou n'importe quel outil de mise en page.

**[ÉCRAN - slide "Ce que pointe le QR code"]**

Détail important : le QR code pointe vers ton lien ClickWhale, pas vers l'URL de destination finale. Ça veut dire que quand quelqu'un scanne le QR code, le clic passe d'abord par ClickWhale avant d'être redirigé.

Conséquence : chaque scan est comptabilisé dans tes statistiques, exactement comme un clic classique. Tu sais combien de personnes ont scanné ton QR code.

Et si tu changes l'URL de destination du lien plus tard, le QR code continue de fonctionner. Pas besoin de régénérer un nouveau QR code. C'est l'un des avantages majeurs d'utiliser des liens ClickWhale plutôt que des QR codes génériques.

**[TRANSITION - face caméra]**

Tu sais générer un QR code. Mais un QR code mal imprimé ou mal dimensionné, personne ne le scannera. Dans la prochaine leçon, je te donne les bonnes pratiques pour que tes QR codes fonctionnent à tous les coups.

---

**Points clés** :
- Génération depuis ClickWhale > Links > Edit > onglet General > "Generate QR Code"
- Le QR code pointe vers le lien ClickWhale (clics trackés)
- Télécharger via clic droit > sauvegarder l'image (format PNG)
- Changer l'URL de destination ne casse pas le QR code
- Chaque scan = un clic comptabilisé dans les statistiques

**Mots-clés SEO** : QR code ClickWhale, générer QR code WordPress, QR code lien affilié, ClickWhale QR code tracking

---

### Leçon 4.6 : Bonnes pratiques QR codes : taille, contraste, test multi-devices

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides illustrées avec exemples visuels

---

**[INTRO - face caméra]**

Un QR code que personne n'arrive à scanner, c'est du gaspillage. Dans cette leçon, je te donne les règles concrètes pour que tes QR codes fonctionnent systématiquement - que ce soit sur une carte de visite, un flyer ou un écran de présentation.

**[ÉCRAN - slide "Règle 1 : la taille minimum"]**

Première règle : la taille. Un QR code imprimé doit faire au minimum 2 centimètres par 2 centimètres. En dessous, les caméras de smartphones anciens ou de mauvaise qualité ne pourront pas le lire.

Pour un support vu de loin - un roll-up, une affiche, un écran de conférence - augmente la taille proportionnellement. Sur un roll-up, vise au moins 10 centimètres de côté. La règle simple : plus le support est grand et vu de loin, plus le QR code doit être grand.

**[ÉCRAN - slide "Règle 2 : le contraste"]**

Deuxième règle : le contraste. Le QR code doit être sombre sur fond clair. Noir sur blanc, c'est le standard. Bleu foncé sur blanc, ça marche aussi.

Ce qui ne marche pas : blanc sur fond sombre, couleurs claires sur couleurs claires, ou QR code avec peu de contraste entre le motif et le fond. La caméra du téléphone a besoin de distinguer nettement les modules noirs des espaces blancs.

Si tu veux intégrer les couleurs de ta marque, garde le motif du QR code dans une couleur foncée et le fond dans une couleur très claire. Ne fais jamais l'inverse.

**[ÉCRAN - slide "Règle 3 : la zone de silence"]**

Troisième règle : la zone de silence. C'est l'espace blanc autour du QR code. Il doit être d'au moins 4 modules de large. Un module, c'est un petit carré noir du QR code.

Concrètement, ne colle pas de texte, de logo ou de bord de page directement contre le QR code. Laisse respirer. Si tu rognes la zone de silence, certains lecteurs de QR code ne détecteront pas le code.

**[ÉCRAN - slide "Règle 4 : le support d'impression"]**

Quatrième règle : le support. Évite les surfaces réfléchissantes - papier glacé, plastification brillante, supports métalliques. Le reflet de la lumière peut empêcher la caméra de lire le QR code.

Préfère les surfaces mates ou satinées. Pour les cartes de visite, un papier mat ou légèrement texturé fonctionne parfaitement.

**[ÉCRAN - slide "Règle 5 : tester"]**

Cinquième règle - et la plus importante : teste toujours avant de diffuser.

Teste sur au moins deux appareils différents. Un iPhone et un Android, idéalement. Les caméras et les applications de scan varient entre les appareils.

Teste dans les conditions réelles. Si ton QR code sera sur un roll-up dans une salle de conférence, ne le teste pas uniquement à 20 centimètres de ton écran. Recule-toi, simule la distance réelle.

Teste après impression. Un QR code parfait à l'écran peut devenir illisible une fois imprimé si la qualité d'impression est basse ou si le papier absorbe trop d'encre.

**[ÉCRAN - slide "Cas d'usage concrets"]**

Où utiliser tes QR codes concrètement ?

Carte de visite : un QR code vers ta bio link page. Le contact scanne et a accès à tous tes liens en une seconde.

Roll-up ou banner pour une conférence : un QR code vers ta page d'inscription ou ta landing page.

Flyer de formation : un QR code vers la page de vente ou un formulaire d'inscription.

Slides de présentation : un QR code en dernière slide - ou même pendant la présentation - pour que les participants accèdent à une ressource complémentaire.

Dans tous les cas, ajoute un texte à côté du QR code qui explique ce que la personne va trouver en scannant. "Scanne pour accéder à la formation gratuite" est plus efficace qu'un QR code seul sans contexte.

**[TRANSITION - face caméra]**

Tu as les règles pour des QR codes qui marchent à chaque fois. Dans la prochaine leçon, c'est à toi de jouer : tu vas analyser tes 5 liens les plus cliqués et en tirer 3 conclusions actionnables.

---

**Points clés** :
- Taille minimum : 2x2 cm (plus grand si vu de loin)
- Contraste : motif sombre sur fond clair (jamais l'inverse)
- Zone de silence : au moins 4 modules d'espace blanc autour
- Support : surfaces mates, pas de papier glacé
- Toujours tester sur plusieurs appareils avant diffusion
- Ajouter un texte explicatif à côté du QR code

**Mots-clés SEO** : bonnes pratiques QR code, taille QR code impression, QR code carte de visite, QR code WordPress

---

### Leçon 4.7 : Exercice : Analyse tes 5 liens les plus cliqués et tire 3 conclusions

**Type** : Exercice pratique (consignes écrites)
**Durée estimée** : 20-30 min

---

## Objectif

Analyser les statistiques de tes liens ClickWhale et prendre des décisions basées sur les données. Cet exercice te met en situation réelle de pilotage de tes liens affiliés et de tes liens internes.

## Prérequis

- Avoir au moins 5 liens actifs dans ClickWhale avec du trafic (idéalement plusieurs semaines de données)
- Avoir accès aux dashboards de tes programmes d'affiliation (si tu as des liens affiliés)

> Si tu n'as pas encore assez de données, utilise les données fictives fournies en fin d'exercice pour t'entraîner.

## Étapes

### 1. Identifie tes 5 liens les plus cliqués

- Va dans ClickWhale > Statistics
- Sélectionne la période "30 derniers jours"
- Note les 5 liens avec le plus de clics dans un tableau :

| Rang | Lien | Clics (30j) | Type (affilié / interne / externe) |
|------|------|-------------|-----------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### 2. Croise avec les conversions (liens affiliés uniquement)

- Pour chaque lien affilié dans ton top 5, connecte-toi au dashboard de l'affilieur
- Note le nombre de conversions sur la même période (30 jours)
- Calcule le taux de conversion : conversions / clics x 100

| Lien affilié | Clics ClickWhale | Conversions affilieur | Taux de conversion |
|-------------|------------------|----------------------|-------------------|
| | | | |
| | | | |

### 3. Analyse et tire 3 conclusions actionnables

Réponds à ces questions pour formuler tes conclusions :

- Quel lien a le meilleur taux de conversion ? Pourquoi ? (contenu de l'article, position du lien, pertinence du produit pour ton audience)
- Y a-t-il un lien avec beaucoup de clics mais zéro conversion ? Quel est le problème probable ?
- Y a-t-il un lien que tu pensais performant mais qui n'est pas dans le top 5 ? Pourquoi ?

Formule 3 conclusions sous cette forme :
- **Conclusion 1** : [constat] → [action concrète]
- **Conclusion 2** : [constat] → [action concrète]
- **Conclusion 3** : [constat] → [action concrète]

### Exemple de conclusions

- "Le lien TutorLMS est mon meilleur convertisseur (3.2%) - je dois le mettre en avant dans au moins 3 articles supplémentaires ce mois-ci"
- "Le lien WP Rocket a 85 clics mais 0 conversion - je vérifie que mon tag affilié est toujours actif et que la landing page fonctionne"
- "Mon lien vers la page Contact est dans le top 5 - mes lecteurs veulent me contacter, je devrais ajouter un formulaire de capture email sur cette page"

## Données fictives (si pas assez de données réelles)

| Rang | Lien | Clics (30j) | Conversions |
|------|------|-------------|-------------|
| 1 | TutorLMS (affilié) | 245 | 6 |
| 2 | FluentCRM (affilié) | 180 | 0 |
| 3 | Guide WordPress LMS (interne) | 156 | - |
| 4 | RankMath Pro (affilié) | 98 | 3 |
| 5 | Page Contact (interne) | 72 | - |

## Critères de validation

- [ ] Tu as identifié tes 5 liens les plus cliqués sur 30 jours
- [ ] Tu as croisé les clics avec les conversions pour les liens affiliés
- [ ] Tu as calculé le taux de conversion pour chaque lien affilié
- [ ] Tu as formulé 3 conclusions actionnables (constat + action concrète)
- [ ] Chaque conclusion est basée sur des données, pas sur une intuition
- [ ] Au moins une conclusion concerne un lien à optimiser ou corriger

---

### Leçon 4.8 : Quiz : Valide tes acquis M4

**Type** : Quiz TutorLMS (8 questions)
**Seuil de réussite** : 80%

---

**Question 1** : Quelles données ClickWhale enregistre-t-il à chaque clic ?

- A) Nom, prénom et adresse email du visiteur
- B) Timestamp, referrer et user agent *(bonne réponse)*
- C) Adresse IP, géolocalisation et historique de navigation
- D) Cookies de session et empreinte numérique du navigateur

---

**Question 2** : Pourquoi le tracking ClickWhale est-il conforme au RGPD de base ?

- A) Parce que ClickWhale a obtenu une certification RGPD officielle
- B) Parce qu'il ne dépose pas de cookies et ne fait pas de fingerprinting *(bonne réponse)*
- C) Parce qu'il anonymise automatiquement les adresses IP
- D) Parce qu'il demande le consentement avant chaque clic

---

**Question 3** : Dans quel cas est-il recommandé de désactiver le tracking ?

- A) Quand tu as trop de clics et que la base de données est pleine
- B) Quand tu veux accélérer la vitesse de ton site
- C) Sur un site de staging ou de développement *(bonne réponse)*
- D) Quand tu n'as pas de liens affiliés

---

**Question 4** : Que se passe-t-il si tu désactives le tracking pendant un mois puis le réactives ?

- A) ClickWhale reconstitue les données manquantes à partir du cache
- B) Les clics du mois désactivé sont perdus définitivement *(bonne réponse)*
- C) Les données sont mises en file d'attente et importées au réactiver
- D) Le tracking reprend avec un compteur remis à zéro

---

**Question 5** : Quel est le taux de conversion normal pour l'affiliation dans la niche WordPress ?

- A) 10 à 15%
- B) 5 à 8%
- C) 1 à 3% *(bonne réponse)*
- D) Moins de 0.5%

---

**Question 6** : Un lien affilié reçoit 120 clics mais 0 conversion. Quelle est la première vérification à faire ?

- A) Désactiver le lien et en créer un nouveau
- B) Vérifier que le lien est correct et que le tag affilié est bien présent *(bonne réponse)*
- C) Contacter l'affilieur pour signaler un bug
- D) Augmenter le nombre de clics en ajoutant le lien dans plus d'articles

---

**Question 7** : Vers quoi pointe le QR code généré par ClickWhale ?

- A) Directement vers l'URL de destination finale
- B) Vers une page intermédiaire ClickWhale avec publicité
- C) Vers le lien ClickWhale, donc les scans sont trackés *(bonne réponse)*
- D) Vers le dashboard Statistics pour que le visiteur voie les stats

---

**Question 8** : Quelle est la taille minimum recommandée pour un QR code imprimé ?

- A) 1x1 cm
- B) 2x2 cm *(bonne réponse)*
- C) 5x5 cm
- D) La taille n'a pas d'importance si le contraste est bon
