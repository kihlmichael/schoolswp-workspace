# Scripts vidéo - Module 9 : WooCommerce + FluentCRM

**Formation** : Maîtriser FluentCRM
**Module** : M9 - WooCommerce + FluentCRM (Premium)
**Leçons** : 7 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~55 min
**Prérequis** : M6 (automations de base), M7 (automation avancée)
**Date** : 2026-03-23

---

### Leçon 9.1 : Active l'intégration WooCommerce

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM settings

---

**[INTRO - face caméra]**

Tu utilises WooCommerce pour vendre tes formations ou tes produits. Tu utilises FluentCRM pour gérer tes contacts. Mais les deux ne se parlent pas encore. Résultat : tes clients WooCommerce n'existent pas dans FluentCRM, et tes emails marketing ignorent complètement l'historique d'achat. Dans cette leçon, tu actives l'intégration WooCommerce dans FluentCRM - et tu ouvres la porte à tout ce qu'on va construire dans ce module.

**[ÉCRAN - screencast FluentCRM > Settings > Integrations]**

[Ouvre FluentCRM > Settings dans le menu WordPress]

Étape 1 : dans ton tableau de bord WordPress, va dans FluentCRM > Settings > Integrations. Tu verras la liste des intégrations disponibles. WooCommerce apparaît si le plugin est actif sur ton site.

[Montre le toggle WooCommerce]

Étape 2 : active l'intégration WooCommerce. Un simple toggle. Dès que c'est fait, FluentCRM peut lire les données de commande WooCommerce : produits achetés, montants, statuts de commande.

**[ÉCRAN - screencast configuration de l'intégration]**

[Montre les options qui apparaissent après activation]

Étape 3 : configure les options de base. Trois paramètres importants.

Premier paramètre : "Auto-create contact on purchase". Active-le. Chaque nouveau client WooCommerce sera automatiquement créé comme contact dans FluentCRM. Sans ça, tu dois les importer manuellement - on verra comment dans la leçon suivante, mais l'auto-création est le mode recommandé.

[Montre le champ liste par défaut]

Deuxième paramètre : la liste par défaut. Choisis dans quelle liste FluentCRM les nouveaux clients seront ajoutés. Crée une liste "Clients WooCommerce" si elle n'existe pas encore. Ça te permet de segmenter immédiatement les acheteurs du reste de ta base.

[Montre le champ tag par défaut]

Troisième paramètre : le tag par défaut. Tu peux attribuer un tag automatique à chaque nouveau client. Par exemple "client" ou "acheteur". On affinera la segmentation par produit dans la leçon 9.4, mais ce tag de base est utile pour les filtres rapides.

**[ÉCRAN - screencast vérification]**

[Passe une commande test dans WooCommerce]

Étape 4 : vérifie que ça fonctionne. Passe une commande test - utilise un email que tu contrôles. Après la commande, va dans FluentCRM > Contacts. Tu dois retrouver le contact avec la liste et le tag que tu as configurés.

[Montre le contact créé dans FluentCRM avec les bonnes infos]

Si le contact apparaît avec la bonne liste et le bon tag, l'intégration est active. Si rien ne se passe, vérifie que WooCommerce est bien actif et que le toggle d'intégration est en position ON.

**[TRANSITION - face caméra]**

L'intégration est en place. À partir de maintenant, chaque achat sur ta boutique crée ou met à jour un contact dans FluentCRM. Mais qu'en est-il de tes clients existants - ceux qui ont acheté avant l'activation ? C'est le sujet de la prochaine leçon.

---

**Points clés** :
- FluentCRM > Settings > Integrations > WooCommerce toggle
- Trois paramètres : auto-création contact, liste par défaut, tag par défaut
- Chaque achat WooCommerce crée automatiquement un contact FluentCRM
- Toujours vérifier avec une commande test après activation

**Mots clés SEO** : FluentCRM WooCommerce intégration, connecter WooCommerce FluentCRM, FluentCRM e-commerce WordPress

---

### Leçon 9.2 : Synchronise tes clients existants

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM import + WooCommerce

---

**[INTRO - face caméra]**

Tu viens d'activer l'intégration WooCommerce. Les nouveaux clients seront automatiquement ajoutés à FluentCRM. Mais tu as probablement des dizaines, voire des centaines de clients qui ont acheté avant cette activation. Ils ne sont pas dans FluentCRM - ou ils y sont sans les données d'achat. Dans cette leçon, tu synchronises ta base existante. Et on clarifie une question importante : sync automatique ou import ponctuel - quand utiliser chaque méthode.

**[ÉCRAN - screencast FluentCRM > Import > WooCommerce Customers]**

[Ouvre FluentCRM > Contacts > Import]

Étape 1 : va dans FluentCRM > Contacts > Import. Tu verras plusieurs sources possibles. Choisis "WooCommerce Customers". Cette option lit directement la base de commandes WooCommerce et importe les clients comme contacts FluentCRM.

[Montre l'écran d'import WooCommerce]

Étape 2 : configure l'import. Tu peux filtrer par statut de commande. Sélectionne "Completed" pour n'importer que les clients dont la commande est finalisée. Pas les commandes en attente ou remboursées - ça polluerait ta base.

[Montre les champs de mapping]

Étape 3 : vérifie le mapping des champs. FluentCRM associe automatiquement prénom, nom, email. Les données d'achat - produits, montants, dates - sont stockées dans les propriétés WooCommerce du contact. Tu n'as pas besoin de créer des champs personnalisés pour ça.

**[ÉCRAN - screencast options d'import]**

[Montre les options liste et tag]

Étape 4 : attribue la même liste et le même tag que dans la leçon précédente - "Clients WooCommerce" et "client". Comme ça, les clients importés et les futurs clients automatiques ont la même segmentation de base.

[Montre le bouton d'import et le compteur]

Étape 5 : lance l'import. FluentCRM traite les contacts par lots. Sur une base de 500 clients, ça prend quelques minutes. Tu vois le compteur avancer en temps réel.

**[ÉCRAN - screencast vérification post-import]**

[Ouvre un contact importé, montre l'onglet WooCommerce]

Étape 6 : vérifie le résultat. Ouvre un contact importé. Dans sa fiche, tu dois voir un onglet ou une section "Purchase History" avec ses commandes WooCommerce : produits, montants, dates. Si cette section est vide, l'import n'a pas fonctionné correctement - recommence en vérifiant les filtres.

**[ÉCRAN - slide "Sync auto vs Import ponctuel"]**

[Montre un tableau comparatif]

Maintenant, la question : sync auto ou import ponctuel ?

Sync automatique - c'est ce qu'on a activé dans la leçon 9.1. Chaque nouvelle commande crée ou met à jour le contact en temps réel. C'est le mode principal, celui qui tourne en permanence.

Import ponctuel - c'est ce qu'on vient de faire. Tu l'utilises une seule fois, pour rattraper l'historique. Ou ponctuellement si tu migres depuis un autre CRM et que tu veux réimporter une base propre.

La règle : active la sync auto et fais un import ponctuel initial. Après, tu n'as plus besoin d'importer manuellement - sauf cas exceptionnel.

**[TRANSITION - face caméra]**

Ta base est synchronisée. Clients existants importés, futurs clients ajoutés automatiquement. Tu as une vue unifiée dans FluentCRM de tous tes acheteurs WooCommerce. Prochaine étape : capturer des leads directement à l'étape du paiement, avant même qu'ils aient acheté.

---

**Points clés** :
- Import WooCommerce : FluentCRM > Contacts > Import > WooCommerce Customers
- Filtrer par "Completed" pour n'importer que les vrais clients
- Sync auto = mode permanent pour les nouveaux achats
- Import ponctuel = rattrapage initial de l'historique
- Règle : activer la sync auto + faire un seul import initial

**Mots clés SEO** : synchroniser WooCommerce FluentCRM, importer clients WooCommerce CRM, FluentCRM import contacts

---

### Leçon 9.3 : Checkout subscription checkbox : capture des leads à l'achat

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WooCommerce checkout + FluentCRM settings

---

**[INTRO - face caméra]**

Un client passe commande sur ta boutique. Il remplit ses infos, son adresse, son moyen de paiement. Et juste avant de valider, il voit une case à cocher : "Recevoir nos conseils et offres par email". S'il coche, il est ajouté à ta liste marketing FluentCRM - avec son consentement explicite. C'est la checkout subscription checkbox. Dans cette leçon, tu la configures et tu comprends pourquoi c'est un des meilleurs endroits pour capturer des abonnés.

**[ÉCRAN - screencast FluentCRM > Settings > Integrations > WooCommerce]**

[Ouvre les settings de l'intégration WooCommerce dans FluentCRM]

Étape 1 : retourne dans FluentCRM > Settings > Integrations > WooCommerce. Cherche la section "Checkout Subscription" ou "Opt-in at Checkout".

[Montre le toggle d'activation]

Étape 2 : active la checkbox de checkout. Un toggle qui ajoute automatiquement une case à cocher sur la page de paiement WooCommerce.

**[ÉCRAN - screencast configuration de la checkbox]**

[Montre les options de personnalisation]

Étape 3 : personnalise le texte de la checkbox. Le texte par défaut est générique. Remplace-le par quelque chose de concret. Exemples adaptés à la vente de formations :

- "Recevoir les prochaines formations et tutoriels WordPress par email"
- "Être informé des nouveaux modules et mises à jour de la formation"

Évite les formulations vagues comme "Recevoir notre newsletter". Dis exactement ce que la personne va recevoir.

[Montre le champ liste et tag]

Étape 4 : choisis la liste et le tag pour les contacts qui cochent. Utilise une liste dédiée - par exemple "Opt-in Checkout" - pour les distinguer des contacts qui se sont inscrits via un formulaire classique. Tag suggéré : "lead-checkout".

[Montre l'option pré-cochée ou non]

Étape 5 : la case doit-elle être pré-cochée ? Non. Pour le RGPD et la confiance, laisse la case décochée par défaut. Le client doit faire l'action délibérément. Une case pré-cochée, c'est du consentement forcé - et c'est un problème légal en Europe.

**[ÉCRAN - screencast aperçu du checkout]**

[Montre la page de checkout WooCommerce avec la checkbox visible]

Étape 6 : visualise le résultat. Va sur ta page de paiement. Tu dois voir la checkbox sous les champs de commande, avant le bouton de validation. Teste avec une commande : si tu coches la case, le contact doit apparaître dans FluentCRM avec la liste "Opt-in Checkout" et le tag "lead-checkout".

[Montre le contact créé dans FluentCRM avec le bon tag]

Pourquoi c'est si efficace ? Parce que la personne est déjà en mode achat. Elle a sorti sa carte bancaire. Elle est engagée. Le taux d'opt-in à ce moment-là est bien plus élevé qu'un formulaire dans la sidebar ou un popup. Et tu récupères un contact qui a déjà prouvé un intérêt commercial fort.

**[TRANSITION - face caméra]**

La checkbox de checkout est en place. Chaque client qui coche est automatiquement ajouté à ta liste marketing - avec son consentement. Combine ça avec les tags par produit qu'on va configurer dans la prochaine leçon, et tu obtiens une segmentation précise dès que l'achat est finalisé.

---

**Points clés** :
- Checkout subscription = case à cocher opt-in sur la page de paiement WooCommerce
- Texte concret et spécifique - pas de "newsletter" générique
- Case décochée par défaut (RGPD)
- Liste et tag dédiés pour distinguer ces leads des autres
- Taux d'opt-in élevé car le client est déjà en mode achat

**Mots clés SEO** : FluentCRM checkout opt-in, WooCommerce subscription checkbox, capture leads checkout WordPress

---

### Leçon 9.4 : Segmente par produit et par montant d'achat

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automations + segments

---

**[INTRO - face caméra]**

Tous tes clients ne sont pas les mêmes. Celui qui a acheté un ebook à 19 euros n'a pas le même profil que celui qui a pris une formation complète à 497 euros. Et celui qui a acheté le module CRM n'a pas les mêmes besoins que celui qui a pris le module SEO. Dans cette leçon, tu mets en place un système de tags automatiques par produit acheté et par montant. Ça te donne une segmentation fine sans aucun travail manuel après la configuration initiale.

**[ÉCRAN - screencast FluentCRM > Automations > New Automation]**

[Crée une nouvelle automation]

Étape 1 : crée une nouvelle automation dédiée au tagging post-achat. Nomme-la "Auto-tag WooCommerce" - c'est une automation utilitaire qui tourne en arrière-plan en permanence.

[Montre le choix du trigger]

Étape 2 : choisis le trigger "New Order (WooCommerce)" ou "Order Completed". La différence : "New Order" se déclenche dès que la commande est créée, "Order Completed" attend que le paiement soit confirmé. Pour le tagging, utilise "Order Completed" - tu ne veux pas taguer quelqu'un qui n'a pas encore payé.

**[ÉCRAN - screencast configuration du tagging par produit]**

[Montre les conditions du trigger]

Étape 3 : le tagging par produit. Tu as deux approches.

Approche 1 - une automation par produit. Tu crées un trigger avec la condition "Specific Product" et tu choisis le produit. Puis tu ajoutes l'action "Apply Tag" avec un tag propre au produit. Par exemple : "a-achete-module-crm", "a-achete-module-seo", "a-achete-module-lms".

[Montre la configuration du trigger avec produit spécifique]

Approche 2 - une seule automation avec des conditions. Tu utilises un trigger générique "Order Completed", puis des blocs conditionnels "If product is X, apply tag Y". Plus compact, mais plus complexe à maintenir si tu as beaucoup de produits.

Ma recommandation pour la vente de formations : une automation par produit. C'est plus clair à lire, plus facile à débugger, et tu vois immédiatement quel produit déclenche quoi.

[Montre la création du tag et son application]

Étape 4 : crée tes tags produit avec une convention de nommage cohérente. Le format "a-achete-[nom-produit]" est clair. Exemples :
- a-achete-module-crm
- a-achete-module-seo
- a-achete-formation-complete
- a-achete-ebook-wordpress

**[ÉCRAN - screencast segmentation par montant d'achat]**

[Montre la création d'un segment dynamique]

Étape 5 : la segmentation par montant d'achat. Va dans FluentCRM > Contacts > Segments (ou Smart Segments si disponible). Crée des segments basés sur la valeur client.

[Montre la configuration des conditions de segment]

Trois segments utiles :
- "Petit acheteur" : total des achats inférieur à 50 euros
- "Acheteur confirmé" : total entre 50 et 200 euros
- "Client premium" : total supérieur à 200 euros

Pour les formations schoolsWP, adapte les seuils à tes prix. Si ta formation complète est à 497 euros, le seuil "premium" sera plus haut.

[Montre comment utiliser les propriétés WooCommerce dans les conditions]

FluentCRM donne accès aux données de commande dans les segments : nombre de commandes, montant total, dernière commande. Utilise "Total order value" ou "Lifetime value" selon ce qui est disponible dans ta version.

**[ÉCRAN - screencast cas concret schoolsWP]**

[Montre un exemple complet]

Étape 6 : cas concret pour la vente de formations. Un client achète le Module CRM à 97 euros. L'automation "Auto-tag WooCommerce" se déclenche. Le tag "a-achete-module-crm" est appliqué. Le contact tombe dans le segment "Acheteur confirmé" (entre 50 et 200 euros).

Plus tard, dans la leçon 9.6, on utilisera ces tags pour proposer un upsell ciblé : "Tu as le module CRM - voici le module Automation qui le complète."

**[TRANSITION - face caméra]**

Tes clients sont maintenant segmentés automatiquement par produit acheté et par montant. Chaque achat enrichit le profil du contact sans intervention manuelle. C'est la base de toute personnalisation email sérieuse. Dans la prochaine leçon, on s'attaque au panier abandonné - le levier le plus sous-utilisé dans la vente de formations en ligne.

---

**Points clés** :
- Trigger "Order Completed" (pas "New Order") pour tagger après paiement confirmé
- Convention de tag : "a-achete-[nom-produit]"
- Une automation par produit = plus clair et plus maintenable
- Segments par montant : petit acheteur, confirmé, premium - adapter les seuils à tes prix
- Ces tags sont la base des upsells et de la personnalisation post-achat

**Mots clés SEO** : FluentCRM segmentation WooCommerce, tag automatique produit FluentCRM, segmenter clients WordPress CRM

---

### Leçon 9.5 : Configure le panier abandonné

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + WooCommerce

---

**[INTRO - face caméra]**

Un visiteur ajoute ta formation au panier. Il va jusqu'à la page de paiement. Il remplit son email. Et il part. Pas de commande, pas de paiement. C'est le panier abandonné - et ça concerne en moyenne 70% des paniers en e-commerce. Pour la vente de formations, le taux est encore plus élevé parce que l'achat est rarement impulsif. La bonne nouvelle : avec FluentCRM, tu peux relancer ces contacts automatiquement. Et le message pour une formation n'a rien à voir avec celui d'un t-shirt - on va voir exactement quoi écrire.

**[ÉCRAN - screencast FluentCRM > Settings > WooCommerce > Abandoned Cart]**

[Ouvre les settings d'intégration WooCommerce]

Étape 1 : active le tracking des paniers abandonnés. Dans FluentCRM > Settings > Integrations > WooCommerce, cherche la section "Cart Tracking" ou "Abandoned Cart". Active le toggle.

[Montre les options de tracking]

Ce que FluentCRM fait concrètement : dès qu'un visiteur saisit son email sur la page de paiement, FluentCRM capture cet email et surveille si la commande aboutit. Si après un délai défini il n'y a pas de commande finalisée, le contact est marqué comme "panier abandonné".

**[ÉCRAN - screencast configuration du délai]**

[Montre le paramètre de délai]

Étape 2 : configure le délai avant de considérer un panier comme abandonné. Le délai par défaut est généralement 15 à 30 minutes. Pour la vente de formations, monte à 60 minutes. Pourquoi ? Parce que l'achat d'une formation est réfléchi. La personne compare, lit les avis, vérifie son budget. Si tu la relances après 15 minutes, c'est trop agressif. 60 minutes lui laissent le temps de revenir par elle-même.

**[ÉCRAN - screencast création de l'automation de relance]**

[Crée une nouvelle automation]

Étape 3 : crée l'automation de relance. Nouvelle automation, trigger "Abandoned Cart" (WooCommerce). Ce trigger se déclenche quand le délai est dépassé et que la commande n'a pas été finalisée.

[Montre le builder avec les blocs]

Étape 4 : construis la séquence de relance. Trois emails, espacés dans le temps. Voici le timing optimal pour la vente de formations :

[Montre le premier email avec délai]

Email 1 - 1 heure après l'abandon. Objet : "Ta formation t'attend". Pas de pression commerciale. Le ton est serviable. Contenu : rappel de ce qu'il y a dans le panier, lien direct pour finaliser, et une question simple - "Tu as une question sur la formation ? Réponds à cet email." Pour une formation, les objections sont souvent spécifiques : "Est-ce que ça couvre mon cas ?", "Est-ce que c'est adapté à mon niveau ?". En ouvrant le dialogue, tu traites l'objection.

[Montre le deuxième email avec délai de 24h]

Email 2 - 24 heures après l'abandon. Objet : "Ce que tu vas apprendre dans [nom de la formation]". Ici, tu développes la valeur. Pas un rappel du panier - un rappel de ce que la formation résout. Liste 3 à 5 bénéfices concrets. Si tu as des témoignages, c'est ici que tu les places. Un témoignage d'un apprenant qui avait la même hésitation est très efficace.

[Montre le troisième email avec délai de 72h]

Email 3 - 72 heures après l'abandon. Objet : "Dernière question avant de fermer ton dossier". Le dernier email est une clôture. Pas d'urgence artificielle, pas de fausse rareté. Une question directe : "J'ai vu que tu avais commencé l'inscription à [formation]. Est-ce que quelque chose t'a bloqué ? Si la formation ne correspond pas à ton besoin, dis-le moi - je peux t'orienter vers une meilleure option." Ce ton respectueux convertit mieux que n'importe quelle tactique de pression.

**[ÉCRAN - screencast ajout du goal de sortie]**

[Ajoute un Goal dans l'automation]

Étape 5 : ajoute un goal "Order Completed" dans l'automation. Si le contact finalise sa commande après le premier email, il ne doit pas recevoir les suivants. Le goal fait exactement ça - on l'a vu dans le module 7. Place-le en mode optionnel : s'il achète, il sort de la séquence. S'il ne répond à aucun des 3 emails, il sort naturellement à la fin.

**[ÉCRAN - screencast différence formation vs e-commerce]**

[Montre un slide comparatif]

Étape 6 : comprends la différence entre un panier abandonné e-commerce classique et un panier abandonné formation. En e-commerce classique, le message c'est "Tu as oublié quelque chose dans ton panier" - parce que souvent, c'est un oubli réel. Pour une formation, personne n'oublie. Le visiteur a hésité. Le message doit traiter l'hésitation, pas rappeler l'oubli. D'où le ton serviable et les questions ouvertes dans les emails qu'on a construits.

**[TRANSITION - face caméra]**

Ton système de relance de panier abandonné est en place. Trois emails, espacés intelligemment, avec un ton adapté à la vente de formations. Le goal protège les acheteurs des relances inutiles. Ce seul mécanisme peut récupérer 10 à 15% des paniers abandonnés - sur une formation à 200 euros, ça représente du chiffre d'affaires réel. Dans la prochaine leçon, on construit le funnel d'upsell post-achat.

---

**Points clés** :
- Activer le cart tracking dans FluentCRM > WooCommerce settings
- Délai recommandé pour les formations : 60 minutes (pas 15)
- 3 emails : serviable (1h), valeur (24h), clôture respectueuse (72h)
- Goal "Order Completed" pour sortir les acheteurs de la séquence
- Ton formation ≠ ton e-commerce : traiter l'hésitation, pas l'oubli

**Mots clés SEO** : FluentCRM panier abandonné, abandoned cart FluentCRM WooCommerce, relance panier WordPress, récupérer panier abandonné formation

---

### Leçon 9.6 : Crée un funnel d'upsell post-achat

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO - face caméra]**

Un client vient d'acheter une formation. Il est satisfait, il progresse. C'est le meilleur moment pour lui proposer la suite logique. Pas un email de vente générique - une recommandation personnalisée basée sur ce qu'il a déjà acheté. Dans cette leçon, tu construis un funnel d'upsell post-achat dans FluentCRM. Et on utilise les tags produit qu'on a configurés dans la leçon 9.4.

**[ÉCRAN - screencast FluentCRM > Automations > New Automation]**

[Crée une nouvelle automation]

Étape 1 : crée une nouvelle automation "Upsell post-achat - Module CRM vers Automation". On part d'un cas concret schoolsWP : un client achète le module CRM, et tu veux lui proposer le module Automation 7 jours plus tard.

[Montre le choix du trigger]

Étape 2 : choisis le trigger "Tag Applied" et sélectionne le tag "a-achete-module-crm". Dès qu'un contact reçoit ce tag - donc dès qu'il achète le module CRM - il entre dans ce funnel.

**[ÉCRAN - screencast construction du funnel]**

[Montre le délai de 7 jours]

Étape 3 : ajoute un délai de 7 jours. Pourquoi 7 jours ? Parce que le client doit avoir le temps de consommer le contenu et d'en voir la valeur. Si tu proposes un upsell 2 heures après l'achat, tu donnes l'impression de ne vouloir que son argent. 7 jours, c'est le temps de découvrir la formation, de commencer à l'appliquer, et de réaliser qu'il a besoin de la suite.

[Ajoute un bloc conditionnel]

Étape 4 : ajoute une condition. Vérifie que le contact n'a PAS déjà le tag "a-achete-module-automation". Si quelqu'un a acheté les deux modules en même temps - ou s'il a acheté le module Automation entre-temps - pas besoin de lui envoyer un upsell.

[Montre la branche "n'a pas le tag"]

Sur la branche "n'a pas le tag" - c'est là qu'on construit la séquence d'upsell.

**[ÉCRAN - screencast création des emails d'upsell]**

[Montre le premier email]

Étape 5 : crée la séquence d'upsell. Trois emails, espacés de 3 jours chacun.

Email 1 - "Tu maîtrises ton CRM - voici l'étape suivante". Contenu : félicite le client pour son avancement. Explique le lien naturel entre CRM et automation. Montre un cas concret : "Avec le module Automation, tu peux déclencher un email de bienvenue personnalisé dès qu'un contact remplit ton formulaire - sans toucher à rien manuellement." Pas de CTA d'achat dans ce premier email. Juste de la valeur et une graine plantée.

[Montre le deuxième email avec délai]

Email 2 - 3 jours plus tard. "3 automations que tu pourrais mettre en place maintenant". Contenu : liste 3 scénarios concrets que le client pourrait réaliser avec le module Automation, en se basant sur ce qu'il connaît déjà du CRM. Par exemple : relance automatique des leads inactifs, séquence d'onboarding pour les nouveaux contacts, email d'anniversaire. CTA : lien vers la page du module Automation.

[Montre le troisième email avec délai]

Email 3 - 3 jours plus tard. "Question rapide sur ton avancement CRM". Contenu : un email court, personnel. "Comment avances-tu avec le module CRM ? Si tu bloques quelque part, réponds à cet email. Et si tu veux passer à la vitesse supérieure, le module Automation est conçu pour prendre la suite exactement où le CRM s'arrête." CTA discret vers la page produit.

**[ÉCRAN - screencast goal et fin du funnel]**

[Ajoute un goal dans l'automation]

Étape 6 : ajoute un goal "Tag Applied" > "a-achete-module-automation" en mode optionnel. Si le client achète après le premier ou le deuxième email, il sort du funnel immédiatement. Les emails suivants ne sont pas envoyés.

[Montre la fin du funnel]

Après le goal, tu peux ajouter un email de bienvenue dans le nouveau module - ou laisser l'automation d'onboarding du module Automation prendre le relais.

**[TRANSITION - face caméra]**

Ton funnel d'upsell est en place. Un client qui achète le module CRM reçoit, 7 jours plus tard, une séquence personnalisée qui l'amène naturellement vers le module Automation. Le goal protège ceux qui achètent en cours de route. Duplique cette automation pour chaque paire de produits complémentaires dans ton catalogue. Dans la prochaine leçon, on explore tous les triggers WooCommerce disponibles dans les automations FluentCRM.

---

**Points clés** :
- Trigger : tag produit appliqué (configurer dans 9.4)
- Délai de 7 jours avant le premier upsell - le client doit d'abord consommer
- Condition de sortie : vérifier que le client n'a pas déjà le produit upsell
- 3 emails : valeur (J7), cas concrets (J10), question personnelle (J13)
- Goal optionnel pour sortir les acheteurs de la séquence

**Mots clés SEO** : FluentCRM upsell automation, funnel post-achat WooCommerce, email upsell formation WordPress

---

### Leçon 9.7 : Triggers WooCommerce dans les automations

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO - face caméra]**

Dans les leçons précédentes, on a utilisé deux triggers WooCommerce : "Order Completed" et "Abandoned Cart". Mais FluentCRM propose bien plus de déclencheurs liés à WooCommerce. Dans cette leçon, on fait le tour complet des triggers disponibles - et surtout, on voit dans quel cas concret utiliser chacun.

**[ÉCRAN - screencast FluentCRM > Automations > New > Triggers WooCommerce]**

[Ouvre le choix des triggers, filtre sur WooCommerce]

Étape 1 : quand tu crées une nouvelle automation, tu vois la liste des triggers. Filtre sur "WooCommerce" pour afficher uniquement les déclencheurs liés à ta boutique. Selon ta version de FluentCRM (free vs Pro) et les addons installés, tu verras entre 4 et 8 triggers.

**[ÉCRAN - screencast trigger par trigger]**

[Montre chaque trigger avec sa configuration]

Étape 2 : passons-les en revue.

**Trigger 1 - New Order Created.** Se déclenche quand une commande est créée dans WooCommerce, quel que soit son statut. Le client a cliqué sur "Commander" - la commande existe, mais le paiement n'est pas forcément confirmé. Usage : notification interne, logging. À éviter pour les automations client - le paiement peut échouer.

**Trigger 2 - Order Completed.** Se déclenche quand le paiement est confirmé et la commande passe en statut "Completed". C'est le trigger le plus fiable pour les actions post-achat : tagging, onboarding, upsell. C'est celui qu'on a utilisé dans les leçons précédentes.

[Montre la configuration avec filtre produit]

**Trigger 3 - Order Completed for Specific Product.** Même chose, mais filtre sur un produit spécifique. Si tu veux une automation qui se déclenche uniquement quand quelqu'un achète le Module CRM et pas un autre produit. Alternative à l'approche "tag applied" de la leçon 9.4 - les deux fonctionnent, mais le tag est plus flexible.

**Trigger 4 - Order Refunded.** Se déclenche quand une commande est remboursée. Usage concret : retirer le tag produit, envoyer un email de feedback ("Qu'est-ce qui n'a pas fonctionné ?"), retirer l'accès à la formation si tu gères les accès manuellement.

[Montre la configuration du trigger refund]

Important : si tu utilises des tags "a-achete-X", pense à les retirer automatiquement sur un remboursement. Sinon, ton upsell continuera à considérer le contact comme acheteur alors qu'il a été remboursé.

**Trigger 5 - Abandoned Cart.** On l'a vu en détail dans la leçon 9.5. Se déclenche quand un panier est abandonné après le délai configuré.

[Montre le trigger s'il existe]

**Trigger 6 - Order Status Changed.** Se déclenche quand le statut d'une commande change - de "Processing" à "Completed", de "Completed" à "Refunded", etc. Plus avancé. Usage : workflows internes, synchronisation avec un outil externe, mise à jour de scores dans un Google Sheet.

**[ÉCRAN - slide récapitulatif]**

[Montre un tableau des triggers avec usage recommandé]

Étape 3 : voici le récapitulatif des triggers et quand les utiliser.

| Trigger | Quand l'utiliser |
|---------|-----------------|
| New Order Created | Notification interne uniquement |
| Order Completed | Tagging, onboarding, upsell - le trigger principal |
| Specific Product | Automation dédiée à un produit |
| Order Refunded | Retrait tag, email feedback, retrait accès |
| Abandoned Cart | Relance panier abandonné |
| Status Changed | Workflows internes avancés |

Pour 90% de tes besoins en vente de formations, "Order Completed" et "Abandoned Cart" suffisent. Les autres sont des outils de précision pour des cas spécifiques.

**[ÉCRAN - screencast combinaison de triggers]**

[Montre un exemple d'automation avec trigger + condition]

Étape 4 : combine trigger et conditions. Par exemple, un trigger "Order Completed" + condition "Montant > 200 euros" + action "Apply Tag: client-premium" + action "Send email: bienvenue VIP". Tu peux construire des parcours très précis en combinant le déclencheur avec les blocs conditionnels du builder.

**[TRANSITION - face caméra]**

Tu connais maintenant tous les triggers WooCommerce disponibles dans FluentCRM. Le plus important : "Order Completed" pour le post-achat, "Abandoned Cart" pour la relance, "Order Refunded" pour le nettoyage. Les autres sont utiles dans des cas précis que tu rencontreras quand ta boutique grandira. Dans la prochaine leçon, tu mets tout ça en pratique avec un exercice complet.

---

**Points clés** :
- 6 triggers WooCommerce principaux dans FluentCRM
- "Order Completed" = trigger principal pour 90% des automations post-achat
- "Order Refunded" = penser à retirer les tags et accès
- "New Order Created" ≠ paiement confirmé - ne pas utiliser pour les automations client
- Combiner triggers + conditions pour des parcours précis

**Mots clés SEO** : FluentCRM triggers WooCommerce, déclencheurs WooCommerce automation, FluentCRM order trigger WordPress

---

### Leçon 9.8 : Exercice : Configure le panier abandonné pour ta boutique de formations

**Durée** : 6 min
**Type** : Exercice guidé
**Écran** : Face caméra pour intro, screencast pour la démo de correction

---

**[INTRO - face caméra]**

C'est l'heure de pratiquer. Dans cet exercice, tu configures un système complet de relance de panier abandonné pour ta propre boutique de formations. Pas une boutique fictive - la tienne. Si tu n'as pas encore de boutique WooCommerce, utilise un site de test local. L'objectif : à la fin de cet exercice, ton panier abandonné fonctionne et envoie le premier email de relance automatiquement.

**[ÉCRAN - slide "Cahier des charges"]**

[Affiche les consignes de l'exercice]

Voici ce que tu dois mettre en place :

**Partie 1 - Configuration technique**
- Active le tracking des paniers abandonnés dans FluentCRM
- Délai : 60 minutes
- Vérifie que l'intégration WooCommerce est active (leçon 9.1)

**Partie 2 - Automation de relance**
- Crée une automation avec le trigger "Abandoned Cart"
- 3 emails de relance aux délais suivants :
  - Email 1 : 1 heure après l'abandon
  - Email 2 : 24 heures après l'abandon
  - Email 3 : 72 heures après l'abandon
- Chaque email doit être adapté à la vente de formations (pas de ton e-commerce générique)

**Partie 3 - Protection**
- Ajoute un goal "Order Completed" en mode optionnel
- Le contact doit sortir de la séquence dès qu'il achète

**Partie 4 - Test**
- Passe une commande test : ajoute un produit au panier, saisis ton email, quitte la page
- Vérifie que le contact est capturé après 60 minutes
- Vérifie que le premier email est envoyé

**[ÉCRAN - slide "Critères de réussite"]**

[Affiche les critères]

Ton exercice est réussi si :
1. Le tracking de panier est actif dans les settings
2. L'automation existe avec le bon trigger
3. Les 3 emails ont un ton adapté aux formations (pas "Vous avez oublié quelque chose")
4. Le goal est en place et fonctionne
5. Le test confirme que le premier email part

**[ÉCRAN - screencast correction rapide]**

[Montre la configuration attendue étape par étape]

Voici la correction rapide. Je te montre le résultat attendu pour chaque partie.

Pour le tracking : le toggle est actif, le délai est à 60 minutes.

Pour l'automation : trigger "Abandoned Cart", puis bloc délai 1 heure, puis email 1, puis délai 23 heures, puis email 2, puis délai 48 heures, puis email 3. Le goal "Order Completed" est placé en parallèle sur toute la séquence.

[Montre le schéma de l'automation complète]

Attention aux délais : l'email 1 part 1 heure après le trigger. L'email 2 part 24 heures après le trigger, donc le délai entre email 1 et email 2 est de 23 heures, pas 24. Même logique pour l'email 3 : 72 heures après le trigger, soit 48 heures après l'email 2.

Pour les emails : l'email 1 est serviable ("Tu as une question ?"), l'email 2 montre la valeur ("Voici ce que tu vas apprendre"), l'email 3 est une clôture respectueuse ("Dernière question avant de fermer ton dossier"). Si tes emails ressemblent à "Reviens acheter !", c'est à revoir.

**[TRANSITION - face caméra]**

Si ton test fonctionne, bravo - tu as un système de récupération de panier abandonné opérationnel. Si ça ne marche pas, reprends la leçon 9.5 et vérifie chaque étape. Le panier abandonné est un des mécanismes les plus rentables de toute ta boutique - ça vaut le coup de le configurer correctement.

---

**Points clés** :
- Exercice pratique sur ta propre boutique (pas un cas fictif)
- 4 parties : config technique, automation, protection, test
- Attention aux calculs de délai entre les emails
- Ton des emails = adapté aux formations, pas au e-commerce générique
- Test obligatoire pour valider le fonctionnement

---

### Leçon 9.9 : Quiz : Valide tes acquis M9

**Durée** : 5 min
**Type** : Quiz (8 QCM)
**Plateforme** : TutorLMS Quiz

---

**[INTRO - face caméra]**

Dernière leçon du module 9. 8 questions pour vérifier que tu maîtrises l'intégration WooCommerce + FluentCRM. Prends ton temps - chaque question a une seule bonne réponse.

---

**Question 1 : Où active-t-on l'intégration WooCommerce dans FluentCRM ?**

A) FluentCRM > Dashboard > Widgets
B) FluentCRM > Settings > Integrations
C) WooCommerce > Settings > FluentCRM
D) WordPress > Plugins > FluentCRM > WooCommerce

**Réponse correcte : B**
Explication : L'intégration se configure dans FluentCRM > Settings > Integrations. Le toggle WooCommerce y apparaît si le plugin est actif.

---

**Question 2 : Quelle est la différence entre "sync auto" et "import ponctuel" pour les clients WooCommerce ?**

A) La sync auto est plus rapide que l'import ponctuel
B) L'import ponctuel fonctionne en temps réel, la sync auto est périodique
C) La sync auto crée les contacts à chaque nouvel achat, l'import ponctuel rattrape l'historique existant
D) Il n'y a pas de différence, les deux font la même chose

**Réponse correcte : C**
Explication : La sync auto tourne en permanence et crée un contact à chaque commande. L'import ponctuel sert à récupérer les clients qui ont acheté avant l'activation de l'intégration.

---

**Question 3 : Pourquoi la checkbox d'opt-in au checkout doit-elle être décochée par défaut ?**

A) Pour éviter de surcharger la base FluentCRM
B) Pour respecter le RGPD - le consentement doit être un acte délibéré
C) Pour améliorer la vitesse de chargement de la page
D) Parce que FluentCRM ne supporte pas les cases pré-cochées

**Réponse correcte : B**
Explication : Le RGPD exige un consentement actif. Une case pré-cochée est considérée comme du consentement forcé et pose un problème légal en Europe.

---

**Question 4 : Quel trigger utiliser pour le tagging automatique post-achat ?**

A) New Order Created
B) Order Completed
C) Cart Updated
D) Customer Registered

**Réponse correcte : B**
Explication : "Order Completed" se déclenche après confirmation du paiement. "New Order Created" se déclenche avant - le paiement peut encore échouer.

---

**Question 5 : Quel délai est recommandé avant de considérer un panier comme abandonné pour la vente de formations ?**

A) 5 minutes
B) 15 minutes
C) 60 minutes
D) 24 heures

**Réponse correcte : C**
Explication : 60 minutes est le délai recommandé pour les formations. L'achat est réfléchi - un délai trop court est trop agressif, un délai de 24h est trop long et laisse le contact refroidir.

---

**Question 6 : Quel est le bon ton pour un email de relance de panier abandonné sur une formation ?**

A) Urgence : "Plus que 2 places disponibles !"
B) Rappel direct : "Tu as oublié quelque chose dans ton panier"
C) Serviable : "Tu as une question sur la formation ?"
D) Promotionnel : "Profite de -30% si tu commandes dans l'heure"

**Réponse correcte : C**
Explication : Pour une formation, personne n'oublie son panier - le visiteur a hésité. Le message doit traiter l'hésitation avec un ton serviable, pas rappeler un oubli ou créer une urgence artificielle.

---

**Question 7 : Pourquoi attendre 7 jours avant d'envoyer un email d'upsell post-achat ?**

A) Pour respecter la loi anti-spam
B) Pour laisser le client consommer le contenu et en voir la valeur
C) Parce que FluentCRM impose un délai minimum de 7 jours
D) Pour que le taux d'ouverture soit meilleur le week-end

**Réponse correcte : B**
Explication : Le client doit avoir le temps de découvrir sa formation et d'en tirer de la valeur. Un upsell immédiat donne l'impression que tu ne veux que son argent.

---

**Question 8 : Que doit-on faire quand une commande WooCommerce est remboursée ?**

A) Rien - FluentCRM gère tout automatiquement
B) Supprimer le contact de FluentCRM
C) Retirer le tag produit et éventuellement l'accès à la formation
D) Envoyer un email de relance pour proposer un autre produit

**Réponse correcte : C**
Explication : Sur un remboursement, il faut retirer le tag "a-achete-X" pour que le contact ne soit plus considéré comme acheteur dans les automations (upsells, segments). L'accès à la formation doit aussi être retiré si tu le gères manuellement.

---

**[TRANSITION - face caméra]**

Module 9 terminé. Tu sais maintenant connecter WooCommerce à FluentCRM, synchroniser tes clients, capturer des leads au checkout, segmenter par produit et par montant, relancer les paniers abandonnés, et construire des upsells post-achat. C'est un des modules les plus concrets de la formation - chaque mécanisme que tu as configuré génère du chiffre d'affaires directement. Active-les sur ta boutique et observe les résultats.

---

**Points clés du quiz** :
- 8 questions couvrant les 7 leçons du module
- Thèmes : intégration, sync, checkout opt-in, triggers, panier abandonné, upsell, remboursement
- Score de passage recommandé : 6/8 (75%)

**Configuration TutorLMS** :
- Type : Multiple choice, single answer
- Tentatives : illimitées
- Score minimum : 75%
- Feedback : affiche l'explication après chaque réponse
