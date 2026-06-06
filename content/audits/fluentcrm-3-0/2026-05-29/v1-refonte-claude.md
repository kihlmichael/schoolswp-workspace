# Refonte article 2779 - FluentCRM (avis complet 2026, version 3.0/3.1)

> Brouillon de refonte, voix "je", brand-compliant. À convertir en blocs Kadence/Gutenberg avant push sur l'ID 2779.
> Cible : freelances / formateurs WordPress. Mot-clé principal : `fluentcrm`. ~3700 mots.

---

## Meta (à reporter dans Rank Math)

- **Title (proposition)** : FluentCRM : mon avis complet 2026 (3.0, SMS, Gutenberg)
- **Slug** : `fluentcrm-est-il-le-meilleur-crm-wordpress` (inchangé)
- **Meta description** : FluentCRM 3.0 ajoute le SMS, un éditeur Gutenberg et une refonte Vue 3. Mon avis complet pour savoir si ce CRM WordPress auto-hébergé est fait pour ton site.
- **Mot-clé focus** : fluentcrm · secondaires : fluentcrm avis, fluentcrm 3.0, fluentcrm sms, fluentcrm gratuit vs pro

---

# FluentCRM est-il le meilleur CRM WordPress ? (mon avis 2026)

FluentCRM s'est imposé comme l'un des outils d'email marketing et de CRM les plus populaires de l'écosystème WordPress. Auto-hébergé, intégré à ton tableau de bord, sans coût par contact : sur le papier, la promesse est solide.

Depuis le 14 mai 2026, le plugin a passé un cap avec la version 3.0, suivie très vite par la 3.1. Refonte complète de l'interface, marketing par SMS, éditeur d'e-mails basé sur Gutenberg : c'est la plus grosse mise à jour depuis le lancement de l'outil en 2020.

Dans cet avis, je reprends FluentCRM à zéro : ce qu'il fait, ce que change vraiment la 3.0, combien ça coûte, comment migrer, et surtout pour quel profil il est pertinent. Parce qu'un CRM auto-hébergé, c'est puissant, mais c'est aussi une infrastructure que tu dois savoir tenir. Si tu es freelance ou formateur et que tu gères ton propre WordPress, c'est exactement ce que tu dois comprendre avant de t'engager.

## Qu'est-ce que FluentCRM ?

FluentCRM est un plugin d'email marketing et de gestion de la relation client (CRM) qui tourne entièrement à l'intérieur de WordPress. Il est édité par WPManageNinja, l'équipe derrière Fluent Forms, FluentSMTP, FluentBooking ou Fluent Support. Autrement dit, un éditeur installé, avec une gamme d'outils qui se parlent entre eux.

La différence majeure avec un Mailchimp, un Brevo ou un ActiveCampaign : tes contacts, tes campagnes et tes statistiques vivent dans **ta** base de données WordPress. Tu n'envoies pas tes données chez un tiers, et tu ne paies pas de surcoût quand ta liste grossit.

Trois caractéristiques résument bien le positionnement :

- **100 % auto-hébergé** : tout reste sur ton serveur, ce qui simplifie le respect du RGPD et te donne le contrôle complet de tes données.
- **Pas de tarif au contact** : tu peux gérer 500 ou 50 000 abonnés, le prix de la licence ne bouge pas. Ce sont ton hébergement et ton service d'envoi qui encaissent la charge.
- **Intégré nativement** à WooCommerce, aux LMS (Tutor LMS, LearnDash, LifterLMS) et à l'écosystème Fluent.

Pour donner un ordre de grandeur : avec une solution SaaS, une liste de 10 000 contacts te coûte souvent plusieurs dizaines d'euros par mois, qui grimpent avec ta liste. Avec FluentCRM, cette même liste ne change rien à ta licence. Sur deux ou trois ans, l'écart devient significatif.

Ce modèle a une contrepartie que je détaille plus bas : la fiabilité repose sur ta configuration serveur (cron, SMTP, hébergement). C'est le cœur du sujet pour un freelance ou un formateur qui gère son propre site, et la raison pour laquelle je ne recommande pas FluentCRM à tout le monde sans nuance.

## Que peut faire FluentCRM ?

Avant de parler des nouveautés, voici les briques de base. Elles sont disponibles dès la version gratuite, ce qui rend FluentCRM utilisable sérieusement sans débourser un centime.

### Gestion des contacts

Chaque abonné dispose d'un profil complet : informations, historique d'e-mails ouverts et cliqués, achats WooCommerce, activité, notes internes. Tu peux relier un contact à un utilisateur WordPress et synchroniser les deux dans les deux sens.

Pour un formateur, ça veut dire voir d'un coup d'œil quels cours un élève a achetés, quels e-mails il a ouverts et à quel moment il a décroché d'une séquence. Tu arrêtes de piloter à l'aveugle. Tu sais qui est chaud, qui est froid, et qui mérite une relance personnalisée.

### Listes, balises et segments

FluentCRM sépare clairement trois notions, et c'est important de les comprendre dès le départ :

- les **listes** servent à organiser tes abonnés par newsletter ou par grande catégorie (par exemple "Prospects formation" et "Clients") ;
- les **balises** (tags) décrivent un comportement ou un centre d'intérêt ("a téléchargé le lead magnet", "intéressé par WooCommerce") ;
- les **segments dynamiques** regroupent automatiquement des contacts selon des conditions, sans que tu aies à les trier à la main.

Cette logique de tags est ce qui rapproche FluentCRM d'un vrai CRM plutôt que d'un simple outil d'envoi. C'est elle qui permet, par exemple, d'envoyer une offre uniquement aux contacts qui ont ouvert tes trois derniers e-mails mais n'ont jamais acheté.

### Envoi d'e-mails et de campagnes

Tu crées des campagnes ponctuelles (une newsletter, une annonce) ou des séquences automatisées (une suite d'e-mails programmée). L'éditeur a été entièrement repensé en 3.0, j'y reviens en détail plus bas.

Les e-mails ne partent pas "par magie" : ils sont confiés à ton service d'envoi, FluentSMTP relié à Amazon SES, Brevo, Mailgun, ou un autre. C'est un point que beaucoup de débutants découvrent trop tard, et qui explique la majorité des problèmes de délivrabilité.

### Formulaires d'inscription et intégrations

FluentCRM se branche sur Fluent Forms, mais aussi sur la plupart des plugins de formulaires et de page builders du marché. Tu peux capturer un lead depuis un formulaire, lui poser un tag automatiquement et le faire entrer dans un tunnel, le tout sans quitter WordPress.

Côté intégrations, l'outil couvre WooCommerce, Easy Digital Downloads, les principaux LMS, les plugins de membership, et bien sûr l'écosystème Fluent (FluentBooking, FluentCart, Fluent Support).

### Entonnoirs d'automatisation

C'est la fonctionnalité la plus puissante, et celle qui justifie à elle seule de choisir FluentCRM. Tu construis des tunnels visuels en glisser-déposer : un déclencheur (nouvel abonné, achat WooCommerce, fin d'un cours Tutor LMS), des conditions (a tel tag ou pas), et des actions (envoyer un e-mail, poser un tag, attendre X jours, créer une tâche).

Quelques exemples concrets que tu peux modéliser :

- une **séquence de bienvenue** de cinq e-mails qui démarre à l'inscription à ta newsletter ;
- une **relance après achat** d'une formation, avec un e-mail de prise en main puis une demande d'avis une semaine plus tard ;
- un **parcours de réengagement** déclenché quand un contact n'a rien ouvert depuis 60 jours.

Tout se construit visuellement, sans code, et tu vois en un coup d'œil combien de contacts se trouvent à chaque étape.

### Segmentation avancée, rapports et panier abandonné

La version Pro ajoute la segmentation avancée (croiser des dizaines de conditions), des rapports détaillés (revenus générés par campagne et par séquence), et la récupération de panier abandonné WooCommerce. Pour une boutique, ce dernier point se rentabilise souvent en quelques semaines : un seul panier récupéré peut couvrir le coût annuel de la licence.

## Les nouveautés de FluentCRM 3.0 et 3.1

La version 3.0 est sortie en stable le 14 mai 2026, et le plugin est déjà passé en 3.1 depuis. Ce n'est plus une bêta : c'est la version officielle, en production. Si tu lis encore des contenus qui parlent de "bêta FluentCRM 3.0", ils datent d'avant la sortie et ne sont plus à jour.

Voici ce qui change concrètement, et pourquoi c'est important pour toi.

### Une refonte technique sous Vue 3

L'interface a été reconstruite avec Vue 3 et Element Plus. En pratique : une navigation plus rapide, des écrans plus réactifs, et une meilleure tenue sur les grosses bases de contacts. Si tu as déjà ouvert l'ancien tableau de bord en traînant 30 000 abonnés, tu sais à quel point ça pouvait ramer. La 3.0 corrige largement ce point. Le mode sombre fait aussi son apparition, avec préférence mémorisée.

À noter, par honnêteté : comme toute refonte majeure, le déploiement a connu quelques accrocs les premiers jours. Un bug d'affichage (écran qui se vide après la mise à jour) a été signalé sur le forum officiel mi-mai. L'éditeur l'a reconnu très vite et corrigé dans les versions suivantes. C'est exactement la raison pour laquelle je recommande de ne jamais mettre à jour un site client le jour d'une sortie majeure. J'y reviens dans la checklist.

### Le marketing par SMS

C'est la nouveauté la plus visible, et celle qui fait passer FluentCRM d'un outil d'emailing à une vraie plateforme multicanale. Le plugin gère désormais le SMS nativement :

- des **campagnes SMS** et des **étapes SMS dans tes automatisations** ;
- des **conversations bidirectionnelles** : tu reçois et tu lis les réponses de tes contacts ;
- la connexion à des passerelles d'envoi comme Twilio.

Pour un formateur, les usages sont immédiats : un rappel de webinaire par SMS a un taux de lecture largement supérieur à un e-mail, et une relance SMS quelques heures avant une session limite les absents. Deux réserves à garder en tête : le SMS a un coût à l'envoi facturé par la passerelle, et le consentement doit être recueilli proprement (c'est un canal encadré).

### Un éditeur d'e-mails basé sur Gutenberg

L'ancien builder est remplacé par un éditeur natif Gutenberg, avec aperçu par appareil et un mode plein écran sans distraction. L'avantage est double : si tu connais déjà l'éditeur de WordPress, tu n'as rien de nouveau à apprendre, et tes e-mails héritent de la même logique de blocs que tes pages.

La 3.0 ajoute aussi des **patterns d'e-mails réutilisables** (tu sauvegardes une mise en page une fois et tu la réutilises) et des **blocs produits** pour WooCommerce et FluentCart, pratiques pour insérer une offre avec son prix et son visuel directement dans une campagne.

### Récupération de paniers et rapports repensés

La récupération de panier abandonné est étendue à FluentCart, la solution e-commerce maison, en plus de WooCommerce. La 3.0 ajoute surtout de nouveaux rapports de progression dans les automatisations : tu vois précisément à quelle étape tes contacts décrochent, ce qui te permet d'ajuster un e-mail ou un délai plutôt que de deviner.

Le tableau de bord a lui aussi été entièrement réécrit, avec des graphiques, des widgets et la visibilité des paramètres UTM. Et un suivi d'e-mail anonymisé a été ajouté pour mieux respecter la vie privée de tes contacts.

### IA et nouveautés annexes

La 3.0 introduit "Write with AI" pour générer du contenu d'e-mail et des résumés, des résumés IA dans les fiches contact, un serveur MCP pour piloter le CRM via des agents IA, une recherche globale dans tout le CRM, un portail front-end pour tes contacts, et un meilleur importateur. Ce sont des ajouts confortables qui modernisent l'outil sans bouleverser tes habitudes.

## FluentCRM face aux autres solutions

Pour situer FluentCRM honnêtement, trois comparaisons reviennent souvent.

**Face à MailPoet.** MailPoet reste le plugin d'emailing le plus cherché en France, et c'est un excellent choix si ton besoin se limite à la newsletter et à des automatisations simples, en particulier sur une boutique WooCommerce où il s'intègre très bien. FluentCRM va plus loin côté CRM : la logique tags, les segments dynamiques, les tunnels multi-conditions et la vision contact à 360°. Si tu veux un outil qui pense "relation client" et pas seulement "envoi d'e-mails", FluentCRM prend l'avantage. Pour un simple bulletin mensuel, MailPoet reste pertinent.

**Face à Groundhogg.** Groundhogg joue dans la même catégorie (CRM auto-hébergé pour WordPress) et reste un bon choix si tu veux une approche très orientée funnel dès la version gratuite. FluentCRM se distingue par une interface plus aboutie depuis la 3.0 et par l'écosystème Fluent intégré. Les deux sont des outils sérieux ; le choix se joue souvent sur l'écosystème de plugins que tu utilises déjà.

**Face aux solutions SaaS (Brevo, ActiveCampaign, Kit).** C'est l'arbitrage de fond. Le SaaS te décharge de toute la maintenance technique : serveur, délivrabilité, cron, mises à jour. En échange, tu paies au contact et tes données vivent ailleurs. FluentCRM inverse l'équation : il te rend le contrôle et supprime le coût au contact, mais te confie la responsabilité de l'infrastructure. Il n'y a pas de bon ou de mauvais choix dans l'absolu, il y a ton niveau d'aisance technique.

## Combien coûte FluentCRM ? Gratuit ou Pro

FluentCRM existe en deux versions, et la bonne nouvelle, c'est que la gratuite est loin d'être bridée.

**La version gratuite**, disponible sur le [dépôt officiel WordPress](https://fr.wordpress.org/plugins/fluent-crm/), couvre déjà beaucoup : contacts illimités, campagnes, séquences, automatisations de base, formulaires, tags et listes. Beaucoup de freelances peuvent démarrer sérieusement sans payer, et c'est une vraie force par rapport à la concurrence SaaS qui limite vite la version gratuite.

**La version Pro** ajoute les fonctionnalités avancées : automatisations plus riches, intégrations e-commerce et LMS poussées, récupération de panier abandonné, rapports détaillés, tests A/B, et désormais le SMS. La licence est annuelle et dépend du nombre de sites sur lesquels tu l'utilises. Des offres à vie (lifetime) ont existé à certaines périodes.

Comme les tarifs évoluent, je préfère te renvoyer à la grille à jour sur le site de l'éditeur plutôt que d'avancer un montant qui sera vite périmé. La vraie question n'est pas "combien" mais "à partir de quel usage je passe en Pro". Mon repère : tant que tu fais de la newsletter et des séquences simples, la version gratuite suffit. Dès que tu as besoin de relancer des paniers, de rapports de revenus précis ou du SMS, la Pro se justifie sans hésiter.

## Comment migrer vers FluentCRM

FluentCRM propose des importateurs pour récupérer tes contacts depuis les principales plateformes : Mailchimp, ActiveCampaign, MailerLite, Drip, ConvertKit/Kit, ainsi que des passerelles depuis d'autres CRM WordPress comme JetPack CRM ou Groundhogg.

Migrer un outil marketing n'est pas anodin. Trois conseils pour une bascule propre :

1. **Importe d'abord une petite liste de test.** Une centaine de contacts suffit pour valider que les champs personnalisés, les tags et les listes se mappent correctement avant de tout transférer.
2. **Ménage ta délivrabilité.** Une grosse bascule d'un coup, avec un envoi massif dans la foulée, peut faire chuter ta réputation d'expéditeur. Échauffe ton domaine en montant progressivement les volumes.
3. **Recrée tes automatisations avant de basculer le trafic, pas après.** Un contact qui s'inscrit et entre dans un tunnel qui n'existe pas encore, c'est une séquence de bienvenue ratée et un prospect perdu.

Prends aussi le temps de faire le ménage : une migration est l'occasion idéale de supprimer les contacts inactifs depuis des mois plutôt que de les traîner (et de les payer, si tu venais d'un SaaS).

## La checklist avant d'utiliser FluentCRM sur un site pro

C'est la partie que beaucoup d'avis oublient, et la plus importante pour un freelance ou un formateur. FluentCRM est puissant parce qu'il est auto-hébergé. Mais il est exigeant pour la même raison : si ton infrastructure est fragile, c'est ton CRM qui trinque, et c'est ton chiffre d'affaires qui suit.

Avant de t'appuyer dessus pour de vrai, vérifie ces points :

- **Configure un cron serveur, pas le WP-Cron par défaut.** Le WP-Cron ne se déclenche qu'aux visites de ton site. Sur un site à faible trafic, tes e-mails et tes automatisations partent en retard, parfois de plusieurs heures. La documentation de FluentCRM recommande elle-même un cron serveur déclenché toutes les minutes. C'est, de loin, la première cause des "mes automatisations ne tournent pas".
- **Mets en place un service SMTP fiable.** FluentSMTP (gratuit, du même éditeur) relié à Amazon SES, Brevo ou Mailgun fait parfaitement le travail. WordPress seul n'est pas conçu pour envoyer du volume et tes e-mails finiraient en spam.
- **Choisis un hébergement à la hauteur.** Une grosse base et des envois massifs demandent de la mémoire et un `max_execution_time` correct. Un hébergement mutualisé d'entrée de gamme montrera vite ses limites.
- **Teste les montées de version majeures sur un staging.** Ne mets jamais à jour un FluentCRM vers une nouvelle version majeure sur un site client le jour de la sortie. Attends une ou deux versions de stabilisation, comme l'a montré le passage en 3.0.
- **Surveille la taille de ta base et nettoie les logs.** FluentCRM journalise beaucoup d'activité. Un outil de nettoyage est intégré : programme-le plutôt que de laisser ta base gonfler.
- **Garde la tête froide sur le suivi des ouvertures.** Le taux d'ouverture est une donnée imparfaite partout, pas seulement dans FluentCRM. La protection de la vie privée d'Apple Mail et les images bloquées par certains clients faussent la mesure chez tous les outils du marché. Fie-toi davantage aux clics et aux conversions.

Coche ces cases, et FluentCRM devient une infrastructure marketing fiable et rentable. Saute-les, et tu passeras tes soirées dans les logs à chercher pourquoi un e-mail n'est pas parti.

## Le support et la communauté

Un point qui revient dans la quasi-totalité des retours : le support de FluentCRM est excellent. Sur le dépôt WordPress, le plugin affiche une note de 4,8 sur 5, et l'écrasante majorité des avis récents saluent la réactivité et la qualité de l'équipe. Pour un outil dont tu dépends au quotidien et qui touche directement ta relation client, c'est un critère que je ne sous-estime pas. La documentation est par ailleurs fournie et tenue à jour.

## Mon avis final : pour qui FluentCRM est fait

FluentCRM en 2026, avec sa version 3.0/3.1, est l'un des meilleurs CRM WordPress du marché. La refonte technique sous Vue 3, le marketing par SMS et l'éditeur Gutenberg en font un outil sérieux, moderne et complet, qui n'a plus grand-chose à envier aux solutions SaaS sur le plan fonctionnel.

**Il est excellent pour toi si :**

- tu veux garder le contrôle de tes données et éviter le coût au contact qui grimpe avec ta liste ;
- tu gères une boutique WooCommerce, une activité de formation ou une communauté sur WordPress ;
- tu es à l'aise (ou correctement accompagné) sur la configuration cron, SMTP et hébergement.

**Il est à encadrer, voire à éviter, si :**

- ton hébergement est fragile et que tu ne veux toucher à aucun réglage technique ;
- tu cherches une solution clé en main où quelqu'un d'autre gère la délivrabilité et la maintenance à ta place. Dans ce cas, une solution SaaS te conviendra mieux, quitte à payer davantage.

En une phrase : FluentCRM ne se choisit pas comme un simple plugin, il se choisit comme une infrastructure marketing. Si tu acceptes cette logique et que tu prépares ton terrain technique, c'est un investissement que tu ne regretteras pas.

## FAQ

**Pourquoi le passage à Vue 3 compte pour les performances ?**
Vue 3 rend l'interface plus rapide et plus fluide, en particulier sur les grosses bases de contacts. Les écrans se chargent plus vite et l'application tient mieux la charge qu'avant.

**Qu'apporte le marketing par SMS dans FluentCRM 3.0 ?**
Des campagnes et des automatisations SMS, des conversations bidirectionnelles et la connexion à des passerelles comme Twilio. Garde en tête le coût d'envoi et l'obligation de consentement.

**Comment l'éditeur Gutenberg améliore la création de campagnes ?**
Tu crées tes e-mails avec l'éditeur natif de WordPress, avec aperçu par appareil, mode plein écran, patterns réutilisables et blocs produits WooCommerce/FluentCart. Aucune nouvelle interface à apprendre si tu connais déjà Gutenberg.

**Comment fonctionne la récupération de panier abandonné ?**
FluentCRM détecte les paniers non finalisés sur WooCommerce et FluentCart, puis déclenche une séquence de relance automatique. Les nouveaux rapports de progression te montrent où tes contacts décrochent pour ajuster tes flux.

**FluentCRM est-il 100 % auto-hébergé et conforme au RGPD ?**
Oui. Tout reste sur ton serveur WordPress, ce qui simplifie le respect du RGPD. Par défaut, aucune donnée n'est envoyée chez un tiers.

**Comment les e-mails sont-ils envoyés et y a-t-il une limite ?**
Via ton service d'envoi (FluentSMTP relié à Amazon SES, Brevo, Mailgun...). FluentCRM n'impose pas de limite d'envoi ; c'est ton service d'envoi et ton hébergement qui définissent le volume soutenable.

**Faut-il attendre avant d'installer FluentCRM 3.0 ?**
La 3.0 est stable depuis le 14 mai 2026 et déjà en 3.1. Sur un site client, teste toujours une montée de version majeure sur un environnement de staging avant de basculer la production.
