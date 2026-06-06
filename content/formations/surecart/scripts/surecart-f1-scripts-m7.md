# Scripts vidéo - F1 Module 7 : Après la vente

**Formation** : Vendre sans WooCommerce (SureCart) - méthode CAISSE (parcours F1)
**Module** : M7 - Après la vente, espace client, emails, intégrations, affiliation (payant)
**Leçons** : 7 vidéos + 1 quiz + 1 checklist "outils connectés + 1er affilié"
**Durée totale** : ~35 min
**Type** : Vidéo HeyGen + voix ElevenLabs
**Date** : 2026-06-04
**Sources** : `_sources/docs-kb/` (overview-customer-dashboard, customers-access-dashboard, customize-email-templates, customer-email-notifications, sync-users-with-surecart, track-events-with-ga, track-events-with-fbpixels, integrating-analytics, surecart-affiliate-platform, affiliate-program, create-affiliate-coupon-codes, managing-the-affiliates, surecart-abilities) + `_sources/youtube-transcripts/` (15 espace client, 21 notifications, 23 affiliation)

> Rôle de ce module : fidéliser, automatiser et amorcer la croissance. C'est le dernier gros module. À la fin, l'élève a un espace client soigné, des emails maîtrisés, ses outils connectés, et il sait monter une affiliation simple. Plusieurs sujets sont volontairement traités à l'essentiel (CRM, analytics, webhooks) : on donne le principe et la voie d'accès, sans transformer la formation en cours technique avancé.

---

### Leçon 7.1 : L'espace client, tableau de bord et self-service

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Comprendre l'espace client auto-créé, le rendre accessible, et le personnaliser (blocs, template, intégration LMS).
**Écran** : Screencast page Dashboard, accès via menu, édition des blocs, choix du template.

---

**[INTRO - face caméra]**

Après l'achat, ton client a besoin d'un endroit à lui : pour retrouver ses commandes, ses factures, ses abonnements, ses téléchargements. SureCart te le crée tout seul, et il est déjà élégant. Dans cette leçon, on apprend à le rendre accessible et à l'adapter à ta marque.

**[SECTION 1 - Un espace client offert dès le départ]**

**[ÉCRAN - screencast : Pages, Dashboard]**

Quand tu actives SureCart, une page est créée automatiquement. Tu la trouves dans Pages, sous le nom Dashboard. Elle contient trois blocs : les abonnements, les commandes et les téléchargements du client. C'est un espace en self-service : ton client y gère ses commandes, ses moyens de paiement, son mot de passe, ses informations, et télécharge ses reçus et factures, sans t'écrire.

**[SECTION 2 - Comment le client y accède]**

**[ÉCRAN - slide "Trois portes d'entrée"]**

Trois chemins mènent à cet espace. Après l'achat, un bouton sur la page de remerciement l'y emmène. L'email de commande contient aussi un bouton pour voir les détails. Et un nouveau client est invité à définir un mot de passe pour ses prochaines connexions, sauf si tu as déjà mis un champ mot de passe au checkout, comme on l'a vu au module 3.

**[ÉCRAN - screencast : Appearance, Menus, ajouter Dashboard]**

Pense aussi à mettre un lien dans ton menu. Va dans Apparence, Menus, affiche toutes les pages, sélectionne Dashboard et ajoute-le au menu. Tes clients accèdent alors à leur espace depuis ta navigation, et se connectent en cliquant.

**[SECTION 3 - Personnaliser l'espace]**

**[ÉCRAN - screencast : édition de la page, blocs]**

Tu peux adapter cet espace. En éditant la page, tu réorganises les blocs, tu en retires, tu en ajoutes. Tu peux mettre un titre, une vidéo de bienvenue, des liens utiles. Et comme les commandes, abonnements et téléchargements sont aussi accessibles dans le menu de gauche, tu peux retirer les blocs du centre sans rien perdre. Dans les options de template de la page, tu peux afficher ou masquer ton logo, régler la largeur, et désactiver une section comme les téléchargements si tu n'en vends pas.

**[SECTION 4 - Deux styles, et le LMS]**

**[ÉCRAN - screencast : choix du template]**

Une décision de présentation. Par défaut, l'espace utilise un template SureCart, autonome et élégant, sans l'en-tête de ton site. Si tu préfères qu'il s'intègre à ton thème, avec ton en-tête et ton pied de page, change le template de la page pour le template par défaut. À toi de voir ce qui colle le mieux à ton image.

Et si tu vends des cours, sache que tu peux ajouter ici les blocs de ton plugin de formation, comme LearnDash ou TutorLMS, pour offrir un espace unifié où le client retrouve ses achats et ses cours au même endroit.

**[OUTRO - face caméra]**

Ton client a son espace. Maintenant, parlons de ce qui lui arrive dans sa boîte mail : les emails et notifications. C'est ta prochaine leçon, et ton exercice du module.

---

**Points clés** :

- Page Dashboard créée automatiquement (Pages, Dashboard), 3 blocs : abonnements, commandes, téléchargements. Self-service complet.
- Accès : bouton sur la page de remerciement, bouton dans l'email de commande, définition de mot de passe au premier accès. Ajouter au menu via Apparence, Menus.
- Personnaliser : réorganiser/retirer les blocs (infos aussi dans le menu de gauche), ajouter titre/vidéo/liens, options de template (logo, largeur, sections).
- Deux styles : template SureCart autonome, ou template par défaut intégré à ton thème. Blocs LMS (LearnDash, TutorLMS) intégrables.

**Mots clés SEO** : espace client SureCart, customer dashboard SureCart, my account SureCart, tableau de bord client WordPress, self-service SureCart

---

### Leçon 7.2 : Personnaliser emails et notifications

**Durée** : ~5 min (~800 mots)
**Objectif pédagogique** : Choisir quels emails partent, modifier leur contenu avec les variables Liquid, et gérer ses propres alertes. Exercice : l'email de confirmation de commande.
**Écran** : Screencast Settings Notifications, édition sur la plateforme, variables Liquid, alertes propriétaire.

---

**[INTRO - face caméra]**

Les emails automatiques de ta boutique, c'est ta relation client sur pilote. Confirmation de commande, accès au produit, remboursement, rappel d'abonnement. Autant qu'ils soient à ton image et bien réglés. Dans cette leçon, tu apprends à choisir lesquels partent, à les personnaliser, et à gérer tes propres alertes. C'est aussi ton exercice du module.

**[SECTION 1 - Deux publics : tes clients, et toi]**

**[ÉCRAN - slide "Deux familles d'emails"]**

Distingue bien deux choses. Les emails envoyés à tes clients, comme la confirmation de commande ou l'accès au produit. Et les notifications qui t'arrivent à toi, le propriétaire, comme l'alerte de nouvelle commande. Ces deux familles se règlent à deux endroits différents.

**[SECTION 2 - Choisir les emails clients]**

**[ÉCRAN - screencast : SureCart, Settings, Notifications]**

Va dans SureCart, Settings, Notifications. Tu vois la liste des emails clients : accès au produit, confirmation de commande, commande gratuite, remboursement, renouvellement et annulation d'abonnement, rappels, récupération. Tu actives ou désactives chacun avec un bouton, pour que ton client ne reçoive que ce qui compte. Enregistre.

**[SECTION 3 - Personnaliser le contenu]**

**[ÉCRAN - screencast : bouton Edit, plateforme Email Customer Emails]**

Pour modifier un email, clique sur Edit à côté. Tu es redirigé vers la plateforme SureCart, dans Email, Customer Emails. Là, tu changes le sujet et le corps. Le corps peut sembler technique, mais ne te bloque pas dessus.

**[ÉCRAN - zoom : variables Liquid]**

Ce que tu vois entre doubles accolades, ce sont des variables Liquid : elles insèrent du contenu dynamique. Par exemple, le nom du produit, le nom de ta boutique, ton adresse. Tu peux même les filtrer, par exemple mettre une majuscule au prénom, ou n'afficher que le prénom plutôt que le nom complet. Tu modifies le texte autour de ces variables pour parler comme toi.

**[ÉCRAN - screencast : Preview, Send Test, Revert to Default]**

Trois boutons te sauvent la mise. Preview pour voir le rendu, Send Test pour t'envoyer un email d'essai, et Revert to Default pour revenir au modèle d'origine si tu t'es trompé. Enregistre quand c'est bon.

**[SECTION 4 - Ton exercice : la confirmation de commande]**

**[ÉCRAN - screencast : édition de l'Order Confirmation]**

Faisons ton exercice. Dans Settings, Notifications, trouve l'email de confirmation de commande et clique sur Edit. Personnalise le sujet pour qu'il sonne comme toi, par exemple Merci pour ta commande, garde les variables qui affichent le nom du produit, ajuste le corps avec un mot chaleureux, fais un Preview, envoie-toi un test, et enregistre. Tu viens de t'approprier le premier email que reçoivent tes acheteurs.

**[SECTION 5 - Tes propres alertes]**

**[ÉCRAN - screencast : plateforme, ton nom, Notifications]**

Et toi, le propriétaire ? Tes alertes, comme la notification de nouvelle commande, se règlent sur la plateforme. Connecte-toi à app point surecart point com, clique sur ton nom en bas, puis Notifications. Tu actives ou désactives ce que tu veux recevoir, et tu enregistres. Et rappelle-toi du module 1 : la langue des emails se règle via Store Language, pour que tout parte en français.

**[OUTRO - face caméra]**

Tes emails sont à ton image. Mais pour vraiment automatiser ta relation client, tu vas vouloir connecter SureCart à ton outil d'emailing et à tes automatisations. C'est la prochaine leçon, avec FluentCRM.

---

**Points clés** :

- Deux familles : emails clients (confirmation, accès, remboursement, abonnement) et alertes propriétaire (nouvelle commande).
- Emails clients : SureCart, Settings, Notifications, activer/désactiver, puis Edit pour modifier sur la plateforme (Email, Customer Emails).
- Personnalisation : variables Liquid (nom produit, boutique) et filtres (majuscule, prénom seul). Preview, Send Test, Revert to Default.
- Alertes propriétaire : plateforme, ton nom, Notifications. Langue via Store Language.
- Exercice : personnaliser l'email de confirmation de commande.

**Mots clés SEO** : personnaliser emails SureCart, notifications SureCart, email confirmation commande SureCart, variables Liquid SureCart, modèles email SureCart

---

### Leçon 7.3 : Connecter FluentCRM et tes automatisations

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Comprendre le modèle headless, synchroniser les clients en utilisateurs WordPress, et brancher une automatisation pour déclencher ses séquences.
**Écran** : Screencast sync (Settings Advanced), intégration sur un produit, schéma vente vers CRM.

---

**[INTRO - face caméra]**

Tes emails transactionnels, on les a vus. Mais ta vraie machine relationnelle, ce sont tes séquences : bienvenue, nurturing, relance. Pour ça, tu connectes SureCart à ton outil d'emailing, comme FluentCRM. Je te montre l'essentiel : comment relier les deux, et comment une vente déclenche tes automatisations.

**[SECTION 1 - SureCart est headless, comprends ça d'abord]**

**[ÉCRAN - slide "Données dans le cloud"]**

Rappel important. SureCart est headless : les données clients vivent dans le cloud SureCart, pas dans ta base WordPress. C'est ce qui garde ton site léger et rapide. Mais pour que tes intégrations fonctionnent, par exemple donner accès à un cours ou pousser un contact dans ton CRM, tes clients doivent exister comme utilisateurs WordPress avec un rôle.

**[SECTION 2 - Synchroniser tes clients en utilisateurs]**

**[ÉCRAN - screencast : Settings, Advanced, Syncing, Sync Customers]**

La plupart du temps, quand un client achète et qu'un compte se crée, l'utilisateur WordPress est généré automatiquement, comme vu au module 3. Mais si tu as importé des clients, par exemple en migrant depuis un autre outil, tu dois les synchroniser. Va dans SureCart, Settings, Advanced, section Syncing, et clique sur Sync Customers. Tu choisis de synchroniser les utilisateurs WordPress et de rejouer l'action d'achat, puis Start Sync. Le processus tourne en arrière-plan, et tes clients sont reliés à des utilisateurs WordPress.

**[SECTION 3 - Brancher une intégration sur un produit]**

**[ÉCRAN - screencast : produit, section Integrations]**

Le pont concret se fait sur le produit. Dans la fiche produit, la section des intégrations te permet de déclencher une action quand quelqu'un achète : inscrire à un cours, donner un accès, ou alimenter ton CRM. C'est ce déclencheur qui relie ta vente à la suite.

**[SECTION 4 - Le schéma qui compte]**

**[ÉCRAN - slide "Vente vers tag vers séquence"]**

Voilà le schéma à retenir, et il boucle avec le module 2. Une vente, ou même l'achat de ton produit gratuit, ajoute le contact dans FluentCRM et lui pose un tag. Ce tag déclenche ta séquence de bienvenue, puis le reste de ta relation. SureCart encaisse et enregistre, ton CRM prend le relais sur la relation.

La construction des séquences elles-mêmes se fait dans FluentCRM, c'est son métier et un sujet à part entière. Ici, l'essentiel à retenir, c'est le branchement : tes clients deviennent des utilisateurs, et une vente nourrit tes automatisations. Le reste, tu le bâtis dans ton CRM.

**[OUTRO - face caméra]**

Ta vente nourrit maintenant ta relation client. Pour piloter tout ça, il te faut des chiffres fiables. Dans la prochaine leçon, on connecte SureCart à Google Analytics et au Pixel, pour suivre tes ventes.

---

**Points clés** :

- SureCart est headless : données dans le cloud, donc tes clients doivent exister en utilisateurs WordPress pour les intégrations.
- À l'achat, l'utilisateur est créé automatiquement (M3) ; pour des clients importés, synchroniser via Settings, Advanced, Syncing, Sync Customers.
- Brancher une intégration sur le produit (section Integrations) : inscription cours, accès, alimentation CRM.
- Schéma : vente (ou produit gratuit) ajoute le contact + tag dans FluentCRM, qui déclenche la séquence de bienvenue.
- Les séquences se construisent dans le CRM (sujet à part) ; ici, l'essentiel est le branchement.

**Mots clés SEO** : SureCart FluentCRM, connecter SureCart CRM, automatisation SureCart, sync utilisateurs SureCart, intégration SureCart WordPress

---

### Leçon 7.4 : Suivre tes ventes, Google Analytics et Pixel

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Mettre en place le suivi des ventes simplement (Site Kit), connaître la voie avancée (Tag Manager), et savoir que SureCart émet des événements.
**Écran** : Screencast Site Kit, slide événements SureCart, mention GTM et Pixel.

---

**[INTRO - face caméra]**

Vendre sans mesurer, c'est avancer les yeux fermés. Combien de visites, combien d'ajouts au panier, combien d'achats ? SureCart sait envoyer ces informations à Google Analytics et au Pixel. Je te montre la voie simple, et je te dis où va la voie avancée, à l'essentiel.

**[SECTION 1 - SureCart suit déjà tes événements]**

**[ÉCRAN - slide "Les événements suivis"]**

Bonne nouvelle d'abord : SureCart déclenche automatiquement les événements clés. L'ajout au panier, le début de checkout, l'achat terminé, le démarrage d'abonnement, et d'autres comme la vue produit. Ces événements sont la matière première de ton suivi : il reste à les envoyer vers ton outil de mesure.

**[SECTION 2 - La voie simple : Google Site Kit]**

**[ÉCRAN - screencast : plugin Google Site Kit]**

Pour Google Analytics, le plus simple est l'extension officielle Google Site Kit. Tu l'installes et tu l'actives. Elle affiche tes statistiques Google Analytics dans ton administration WordPress, et suit automatiquement l'ajout au panier et l'achat. Pour la plupart des créateurs, ça suffit largement : tu vois tes ventes remonter dans Google Analytics, sans manipulation compliquée.

**[SECTION 3 - La voie avancée : Google Tag Manager]**

**[ÉCRAN - slide "Tag Manager pour aller plus loin"]**

Si tu veux suivre plus d'événements, comme la vue produit ou le début de checkout, tu passes par Google Tag Manager. Le principe : tu crées un déclencheur sur l'événement SureCart, par exemple celui de la vue produit, et tu l'associes à une balise Google Analytics. C'est plus puissant, mais plus technique. Pour ce parcours, retiens que c'est possible, et garde-le pour quand tu en auras vraiment besoin.

**[SECTION 4 - Le Pixel et les autres outils]**

**[ÉCRAN - slide "Pixel et au-delà"]**

Pour le Pixel Facebook, même logique : tu passes par Google Tag Manager, avec une balise dédiée, ou par un peu de code qui écoute l'événement d'achat de SureCart pour l'envoyer au Pixel. Et au-delà de Google et Facebook, SureCart peut alimenter à peu près n'importe quel outil de mesure, grâce à ses événements, aux webhooks et à l'API. On effleure ça dans la dernière leçon du module.

**[ÉCRAN - slide "Commence simple"]**

Mon conseil : commence avec Site Kit pour voir tes ventes, et n'ajoute Tag Manager et le Pixel que si tu fais de la publicité ou si tu as besoin d'un suivi fin. Ne te noie pas dans le tracking avant d'avoir des ventes à suivre.

**[OUTRO - face caméra]**

Tu mesures tes ventes. Passons à un levier de croissance souvent ignoré quand on débute, et pourtant intégré gratuitement à SureCart : l'affiliation. On voit à quoi ça sert et quand l'utiliser. Prochaine leçon.

---

**Points clés** :

- SureCart émet automatiquement des événements : ajout au panier, début de checkout, achat, démarrage d'abonnement, vue produit.
- Voie simple pour Google Analytics : extension Google Site Kit (suit ajout au panier et achat, stats dans l'admin).
- Voie avancée : Google Tag Manager (déclencheur sur événement SureCart vers balise GA4) pour plus d'événements.
- Pixel Facebook : via Tag Manager ou code écoutant l'événement d'achat. Autres outils via événements, webhooks, API.
- Commencer simple (Site Kit), ajouter le reste seulement si besoin réel (publicité, suivi fin).

**Mots clés SEO** : Google Analytics SureCart, suivi ventes SureCart, Pixel Facebook SureCart, Site Kit SureCart, tracking SureCart

---

### Leçon 7.5 : Affiliation, à quoi ça sert et quand l'utiliser

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Comprendre ce qu'est une plateforme d'affiliation, qu'elle est intégrée gratuitement, et les réglages de base (signups, suivi, commissions).
**Écran** : Slide principe, screencast Settings Affiliates (vue d'ensemble).

---

**[INTRO - face caméra]**

Et si d'autres vendaient pour toi, et n'étaient payés que sur les ventes qu'ils apportent ? C'est l'affiliation. Beaucoup de débutants l'ignorent, alors qu'elle est intégrée gratuitement à SureCart, là où des plateformes externes coûtent des centaines d'euros par an. Dans cette leçon, on voit à quoi ça sert et comment ça se règle.

**[SECTION 1 - Ce qu'est l'affiliation]**

**[ÉCRAN - slide "Le principe de l'affiliation"]**

Une plateforme d'affiliation, c'est un point de rencontre. D'un côté, toi, qui veux vendre plus. De l'autre, des personnes, les affiliés, qui acceptent de promouvoir tes produits. Chaque affilié reçoit un lien unique qui trace ses apports. Quand quelqu'un achète via ce lien, la vente lui est attribuée et il touche une commission. Tu ne paies que sur les ventes réelles : c'est un levier sans risque pour aller chercher une audience qui n'est pas la tienne.

Et c'est intégré dans SureCart, sans extension ni abonnement à un service tiers.

**[SECTION 2 - Où ça se règle]**

**[ÉCRAN - screencast : SureCart, Settings, Affiliates]**

Tout se configure dans SureCart, Settings, Affiliates. Trois grands blocs : les inscriptions des affiliés, le suivi des apports, et les commissions et paiements. Voyons l'essentiel de chacun.

**[SECTION 3 - Inscriptions et suivi]**

**[ÉCRAN - screencast : Affiliate Signups]**

Côté inscriptions, tu actives les nouvelles candidatures, tu décris ton programme, par exemple gagne 15 % sur chaque vente apportée, et tu choisis d'approuver automatiquement ou à la main. Tu obtiens une URL d'inscription à partager. Mon conseil : approuve à la main au début, pour garder le contrôle sur qui représente ta marque.

**[ÉCRAN - screencast : Referral Tracking]**

Côté suivi, deux réglages clés. Le type d'attribution : si une personne clique sur plusieurs liens d'affiliés, qui touche la commission, le premier ou le dernier ? Et la durée de suivi, le cookie : combien de temps après le clic une vente compte encore pour l'affilié. Trente jours est un standard courant. Depuis les versions récentes de SureCart, le script de suivi est géré automatiquement par un simple bouton.

**[SECTION 4 - Commissions]**

**[ÉCRAN - screencast : Commissions & Payouts]**

Côté commissions, tu fixes un pourcentage ou un montant fixe. Le taux dépend de ton secteur : pour un produit numérique ou un logiciel, on voit souvent 20 à 30 %. Tu peux aussi récompenser les renouvellements d'abonnement, avec ou sans limite de durée, et activer les commissions à vie, où l'affilié touche sur les futurs achats du client qu'il a amené. Tu écris enfin tes conditions de paiement.

**[ÉCRAN - slide "À l'envers aussi"]**

Une note pour la culture : l'affiliation marche aussi dans l'autre sens. Tu peux toi-même gagner en recommandant SureCart, via son programme partenaire, avec ses propres règles de commission et de paiement. C'est un sujet distinct de ta propre plateforme, mais bon à savoir.

**[OUTRO - face caméra]**

Tu sais à quoi sert l'affiliation et comment elle se règle. Dans la prochaine leçon, on passe à la pratique : activer une base simple, approuver un premier affilié, et créer un coupon d'apporteur d'affaires.

---

**Points clés** :

- Affiliation : des affiliés promeuvent tes produits via un lien unique, et touchent une commission sur les ventes apportées. Tu ne paies que sur du réel.
- Intégrée gratuitement à SureCart (Settings, Affiliates), là où les plateformes externes coûtent cher.
- Inscriptions : activer, décrire le programme, approuver auto ou à la main (à la main recommandé au début), URL d'inscription.
- Suivi : attribution premier ou dernier clic, durée de cookie (30 jours courant), script auto sur versions récentes.
- Commissions : pourcentage ou fixe (souvent 20 à 30 % en numérique), sur renouvellements et à vie en option.
- À l'envers : tu peux aussi gagner en recommandant SureCart (programme partenaire, sujet distinct).

**Mots clés SEO** : affiliation SureCart, plateforme affiliation WordPress, programme d'affiliation SureCart, commission affilié SureCart, affiliate platform SureCart

---

### Leçon 7.6 : Affiliation, activer une base simple et des coupons d'apporteurs

**Durée** : ~5 min (~800 mots)
**Objectif pédagogique** : Activer le programme, approuver un affilié, créer un coupon lié à un affilié, et comprendre le suivi et les paiements manuels. Lié au livrable 1er affilié.
**Écran** : Screencast activation, Requests, coupon Link to Affiliate, Payouts.

---

**[INTRO - face caméra]**

Passons à la pratique. On active une affiliation simple, on approuve un premier affilié, et on crée un coupon à son nom. C'est exactement ce que demande ton livrable du module : un premier affilié en place.

**[SECTION 1 - Activer et fixer ta commission]**

**[ÉCRAN - screencast : Settings, Affiliates, activation]**

Sur la plateforme, dans Settings, Affiliates, active les nouvelles candidatures. Renseigne ta description, par exemple gagne 15 % sur toutes les ventes que tu apportes. Choisis d'approuver à la main. Fixe ta commission, mettons 15 %. Récupère l'URL d'inscription : c'est le lien que tu donnes aux personnes qui veulent te promouvoir.

**[SECTION 2 - Approuver un affilié]**

**[ÉCRAN - screencast : candidature, soumission]**

Quand quelqu'un remplit ton formulaire d'inscription, tu reçois un email, et sa demande apparaît dans tes affiliés.

**[ÉCRAN - screencast : SureCart, Affiliates, Requests]**

Va dans SureCart, Affiliates, onglet Requests, demandes. Clique sur la demande pour voir les informations. Tu as trois options : approuver, refuser, ou supprimer. Approuve. L'affilié reçoit alors un email pour finaliser son inscription et vérifier son adresse, puis il accède à son portail. Là, il voit ses clics, ses ventes apportées, ses gains, et son lien unique.

**[SECTION 3 - Le coupon d'apporteur d'affaires]**

**[ÉCRAN - screencast : Coupons, Add New, Link to Affiliate]**

Certaines audiences préfèrent un code à un lien. Tu peux donc lier un coupon à un affilié. Va dans SureCart, Coupons, Add New, comme au module 4. Donne un nom, un code, une remise. Restreins à certains produits si tu veux. Et surtout, dans le menu Link to Affiliate, choisis ton affilié. Crée le coupon.

Désormais, quand un client utilise ce code, ton affilié touche sa commission sur la vente, et le coupon apparaît dans son profil. C'est pratique pour un partenaire qui anime une communauté avec un code de réduction à son nom.

**[SECTION 4 - Suivre et payer]**

**[ÉCRAN - screencast : Affiliates, Clicks, Referrals]**

Pour suivre, SureCart range tout dans la section Affiliates : les demandes, les clics, les ventes apportées et les paiements. Dans Referrals, tu vois les ventes attribuées, que tu peux approuver, refuser ou modifier. Les clics te disent qui amène du trafic et qui convertit.

**[ÉCRAN - screencast : Payouts, Add New]**

Pour payer, va dans Payouts, paiements, Add New. Tu choisis l'affilié et la période, et SureCart génère le paiement à régler.

**[ÉCRAN - slide "Deux limites honnêtes"]**

Deux points d'honnêteté. D'abord, les paiements ne sont pas automatiques : SureCart prépare la liste, mais tu règles tes affiliés toi-même, en dehors de la plateforme. Tu peux le faire un par un ou en lot, au-dessus d'un montant minimum. Ensuite, l'affiliation ne suit que les vraies ventes : tes achats de test ne sont pas comptés. Pense-y quand tu valides ton installation.

**[OUTRO - face caméra]**

Tu as un premier affilié et un coupon à son nom. Pour finir ce module, un coup d'oeil vers tout ce que tu peux encore connecter : automatisations, webhooks, et le pilotage par l'IA avec les Abilities. Dernière leçon.

---

**Points clés** :

- Activer : Settings, Affiliates, candidatures + description + approbation manuelle + commission (ex. 15 %) + URL d'inscription.
- Approuver : SureCart, Affiliates, Requests, approuver ; l'affilié vérifie son email et accède à son portail (clics, ventes, gains, lien).
- Coupon d'apporteur : Coupons, Add New, remise, puis Link to Affiliate pour lier le code à l'affilié (commission au code).
- Suivre : Affiliates (Requests, Clicks, Referrals). Payer : Payouts, Add New (individuel ou lot).
- Limites : paiements manuels hors plateforme ; seules les vraies ventes sont suivies (pas le mode test).

**Mots clés SEO** : créer affilié SureCart, coupon affilié SureCart, payer affilié SureCart, gérer affiliés SureCart, referral SureCart

---

### Leçon 7.7 : Connecter SureCart à (presque) tout, webhooks et IA

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Connaître les voies de connexion (intégrations, webhooks, API, événements) et découvrir le pilotage par l'IA avec les Abilities et leurs garde-fous.
**Écran** : Slide voies de connexion, screencast Settings MCP, exemples de requêtes Abilities.

---

**[INTRO - face caméra]**

Pour finir ce module, je te montre l'horizon : tout ce que tu peux connecter à SureCart. Des intégrations toutes faites aux webhooks pour les bricoleurs, jusqu'à une nouveauté qui change la donne, piloter ta boutique en langage naturel avec une IA. On reste à l'essentiel, c'est une leçon de culture et d'ouverture.

**[SECTION 1 - Les voies de connexion]**

**[ÉCRAN - slide "4 voies pour connecter"]**

SureCart se connecte de plusieurs façons. Les intégrations sur le produit, vues en leçon 3, pour inscrire à un cours ou alimenter ton CRM, sans code. Les événements : SureCart émet des signaux à chaque action, ajout au panier, achat, abonnement démarré, que d'autres outils peuvent écouter. Les webhooks, qui envoient les données d'un événement vers une adresse externe, pour relier un service tiers. Et l'API, pour les besoins sur-mesure. Les trois dernières voies sont du ressort d'un développeur : tu n'en as pas besoin pour démarrer, mais c'est bon de savoir que la porte est ouverte.

**[SECTION 2 - Piloter par l'IA : les Abilities]**

**[ÉCRAN - slide "SureCart Abilities"]**

Voici la partie qui change vraiment la façon de travailler. Les Abilities te permettent de gérer ta boutique en parlant à un assistant IA, comme Claude ou ChatGPT. Au lieu de naviguer dans dix écrans, tu décris ce que tu veux en une seule demande.

**[ÉCRAN - screencast : Settings, MCP]**

La mise en place se fait dans SureCart, Settings, MCP : tu installes l'adaptateur et tu connectes ton assistant IA. C'est ce pont qui donne à l'IA accès à ta boutique.

**[SECTION 3 - Ce que ça donne concrètement]**

**[ÉCRAN - slide "Exemples de demandes"]**

Quelques exemples réels. Trouve l'abonnement actif de tel client et repousse son renouvellement de sept jours. Crée une facture pour telle personne, pour tel produit, à échéance à telle date, et envoie-la. Montre-moi la performance de ma boutique sur les 30 derniers jours. Crée trois coupons Black Friday avec ces règles. Rembourse à 50 % la dernière commande de tel client. Ce sont des tâches qui demandaient plusieurs étapes, faites en une phrase.

**[ÉCRAN - slide "Conseils d'usage"]**

Pour de bons résultats, sois précis : email du client, nom exact du produit, dates au bon format. Décris le but, pas chaque étape. Et pour les actions sensibles comme un remboursement, demande à l'IA de confirmer avant d'agir.

**[SECTION 4 - Les garde-fous]**

**[ÉCRAN - screencast : trois boutons de permission]**

C'est puissant, donc c'est encadré. Trois permissions à régler dans les réglages MCP. L'interrupteur principal, qui autorise ou non l'accès de l'IA. L'autorisation de créer et modifier des données. Et l'autorisation de supprimer, la plus sensible. Mon conseil : n'active la suppression que si tu en as vraiment besoin, et garde la confirmation avant toute action destructive. Tu donnes à l'IA exactement le niveau d'accès que tu choisis, pas plus.

**[OUTRO - face caméra]**

Tu as fait le tour de l'après-vente : espace client, emails, CRM, analytics, affiliation, et toutes les connexions possibles. Récupère ta checklist outils connectés plus premier affilié. Il ne reste qu'une chose à faire, et c'est la plus excitante : lancer. C'est le module 8. On se retrouve là-bas.

---

**Points clés** :

- Quatre voies de connexion : intégrations produit (sans code), événements (signaux à écouter), webhooks (données vers une adresse externe), API (sur-mesure). Les trois dernières relèvent d'un développeur.
- Abilities : piloter la boutique en langage naturel via un assistant IA (Claude, ChatGPT). Mise en place dans Settings, MCP (adaptateur + connexion).
- Exemples : prolonger un abonnement, créer une facture, voir la performance, créer des coupons en lot, rembourser, en une demande.
- Bonnes pratiques : être précis (email, nom, dates), décrire le but, demander confirmation avant une action sensible.
- Garde-fous : trois permissions (accès, modification, suppression). N'activer la suppression que si nécessaire ; confirmer le destructif.

**Mots clés SEO** : SureCart webhooks, SureCart API, intégrations SureCart, SureCart Abilities, piloter SureCart avec IA

---

## Notes de production (module)

### Captures et écrans à préparer

- Screencast page Dashboard, accès via menu, édition des blocs, choix du template, blocs LMS (7.1)
- Screencast Settings, Notifications + édition d'un email sur la plateforme + variables Liquid + Preview/Send Test (7.2)
- Screencast édition de l'email de confirmation de commande (exercice) + plateforme, notifications propriétaire (7.2)
- Slide "données dans le cloud" + screencast Settings, Advanced, Sync Customers + section Integrations du produit + slide vente vers tag vers séquence (7.3)
- Screencast Google Site Kit + slide événements SureCart + mention GTM et Pixel (7.4)
- Slide principe affiliation + screencast Settings, Affiliates (signups, tracking, commissions) (7.5)
- Screencast activation + Requests (approbation) + Coupons Link to Affiliate + Payouts (7.6)
- Slide "4 voies de connexion" + screencast Settings, MCP + exemples de requêtes Abilities + 3 permissions (7.7)

### Ton et transitions

- Intro/outro face caméra, fond neutre schoolsWP.
- Module riche : alterner screencast et slides pédagogiques. Plusieurs leçons à l'essentiel (CRM, analytics, webhooks) : donner le principe et la porte d'accès, pas un cours technique.
- Leçon 7.3 : assumer que la construction des séquences est un sujet à part (le CRM), ici on relie.
- Leçon 7.4 : pousser "commence simple" (Site Kit), ne pas noyer dans GTM.
- Leçon 7.7 : présenter les Abilities avec enthousiasme mais insister sur les garde-fous de permission.

### Livrables du module

- Checklist "outils connectés + 1er affilié" : espace client en place et accessible, email de confirmation personnalisé, clients synchronisés et CRM relié, suivi analytics actif (au moins Site Kit), affiliation activée avec un premier affilié approuvé et un coupon d'apporteur, permissions MCP réglées si Abilities utilisées.
- Quiz 5 questions (rôle de l'espace client, deux familles d'emails, modèle headless et sync, voie simple analytics, attribution affilié premier vs dernier clic).

### Garde-fous voix schoolsWP

- Tutoiement, singulier solo, jamais d'em-dash ni d'en-dash.
- Honnêteté : paiements affiliés manuels, mode test non suivi en affiliation, webhooks/API du ressort d'un développeur.
- Sécurité : insister sur les permissions des Abilities (surtout la suppression) et la confirmation avant action destructive.
- Aucune promesse absolue ; sujets à l'essentiel clairement annoncés comme tels.
- Ne pas conflater la plateforme d'affiliation du marchand (les autres te promeuvent) avec le programme partenaire SureCart (tu promeus SureCart).

### Cohérence avec le plan et les modules précédents

- L'espace client prolonge le champ mot de passe et la création de compte du M3, et la gestion d'abonnement du M5 (le client gère lui-même).
- Les emails complètent les notifications transactionnelles déjà croisées (M1 langue, M5 rappels d'essai).
- Le branchement CRM (7.3) honore l'annonce faite au M2.5 (produit gratuit vers séquence welcome) et au M5.
- Les coupons d'affiliés réutilisent la création de coupons du M4.
- Les événements et webhooks (7.7) prolongent le tracking analytics (7.4).
- La transition prépare le M8 (lancer), dernier module avant le Bonus.
