# Scripts video — Module 9 : WooCommerce + FluentCRM

**Formation** : Maitriser FluentCRM
**Module** : M9 — WooCommerce + FluentCRM (Premium)
**Lecons** : 7 videos + 1 exercice + 1 quiz
**Duree totale** : ~55 min
**Prerequis** : M6 (automations de base), M7 (automation avancee)
**Date** : 2026-03-23

---

### Lecon 9.1 — Active l'integration WooCommerce

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM settings

---

**[INTRO — face camera]**

Tu utilises WooCommerce pour vendre tes formations ou tes produits. Tu utilises FluentCRM pour gerer tes contacts. Mais les deux ne se parlent pas encore. Resultat : tes clients WooCommerce n'existent pas dans FluentCRM, et tes emails marketing ignorent completement l'historique d'achat. Dans cette lecon, tu actives l'integration WooCommerce dans FluentCRM — et tu ouvres la porte a tout ce qu'on va construire dans ce module.

**[ECRAN — screencast FluentCRM > Settings > Integrations]**

[Ouvre FluentCRM > Settings dans le menu WordPress]

Etape 1 : dans ton tableau de bord WordPress, va dans FluentCRM > Settings > Integrations. Tu verras la liste des integrations disponibles. WooCommerce apparait si le plugin est actif sur ton site.

[Montre le toggle WooCommerce]

Etape 2 : active l'integration WooCommerce. Un simple toggle. Des que c'est fait, FluentCRM peut lire les donnees de commande WooCommerce : produits achetes, montants, statuts de commande.

**[ECRAN — screencast configuration de l'integration]**

[Montre les options qui apparaissent apres activation]

Etape 3 : configure les options de base. Trois parametres importants.

Premier parametre : "Auto-create contact on purchase". Active-le. Chaque nouveau client WooCommerce sera automatiquement cree comme contact dans FluentCRM. Sans ca, tu dois les importer manuellement — on verra comment dans la lecon suivante, mais l'auto-creation est le mode recommande.

[Montre le champ liste par defaut]

Deuxieme parametre : la liste par defaut. Choisis dans quelle liste FluentCRM les nouveaux clients seront ajoutes. Cree une liste "Clients WooCommerce" si elle n'existe pas encore. Ca te permet de segmenter immediatement les acheteurs du reste de ta base.

[Montre le champ tag par defaut]

Troisieme parametre : le tag par defaut. Tu peux attribuer un tag automatique a chaque nouveau client. Par exemple "client" ou "acheteur". On affinera la segmentation par produit dans la lecon 9.4, mais ce tag de base est utile pour les filtres rapides.

**[ECRAN — screencast verification]**

[Passe une commande test dans WooCommerce]

Etape 4 : verifie que ca fonctionne. Passe une commande test — utilise un email que tu controles. Apres la commande, va dans FluentCRM > Contacts. Tu dois retrouver le contact avec la liste et le tag que tu as configures.

[Montre le contact cree dans FluentCRM avec les bonnes infos]

Si le contact apparait avec la bonne liste et le bon tag, l'integration est active. Si rien ne se passe, verifie que WooCommerce est bien actif et que le toggle d'integration est en position ON.

**[TRANSITION — face camera]**

L'integration est en place. A partir de maintenant, chaque achat sur ta boutique cree ou met a jour un contact dans FluentCRM. Mais qu'en est-il de tes clients existants — ceux qui ont achete avant l'activation ? C'est le sujet de la prochaine lecon.

---

**Points cles** :
- FluentCRM > Settings > Integrations > WooCommerce toggle
- Trois parametres : auto-creation contact, liste par defaut, tag par defaut
- Chaque achat WooCommerce cree automatiquement un contact FluentCRM
- Toujours verifier avec une commande test apres activation

**Mots cles SEO** : FluentCRM WooCommerce integration, connecter WooCommerce FluentCRM, FluentCRM e-commerce WordPress

---

### Lecon 9.2 — Synchronise tes clients existants

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM import + WooCommerce

---

**[INTRO — face camera]**

Tu viens d'activer l'integration WooCommerce. Les nouveaux clients seront automatiquement ajoutes a FluentCRM. Mais tu as probablement des dizaines, voire des centaines de clients qui ont achete avant cette activation. Ils ne sont pas dans FluentCRM — ou ils y sont sans les donnees d'achat. Dans cette lecon, tu synchronises ta base existante. Et on clarifie une question importante : sync automatique ou import ponctuel — quand utiliser chaque methode.

**[ECRAN — screencast FluentCRM > Import > WooCommerce Customers]**

[Ouvre FluentCRM > Contacts > Import]

Etape 1 : va dans FluentCRM > Contacts > Import. Tu verras plusieurs sources possibles. Choisis "WooCommerce Customers". Cette option lit directement la base de commandes WooCommerce et importe les clients comme contacts FluentCRM.

[Montre l'ecran d'import WooCommerce]

Etape 2 : configure l'import. Tu peux filtrer par statut de commande. Selectionne "Completed" pour n'importer que les clients dont la commande est finalisee. Pas les commandes en attente ou remboursees — ca polluerait ta base.

[Montre les champs de mapping]

Etape 3 : verifie le mapping des champs. FluentCRM associe automatiquement prenom, nom, email. Les donnees d'achat — produits, montants, dates — sont stockees dans les proprietes WooCommerce du contact. Tu n'as pas besoin de creer des champs personnalises pour ca.

**[ECRAN — screencast options d'import]**

[Montre les options liste et tag]

Etape 4 : attribue la meme liste et le meme tag que dans la lecon precedente — "Clients WooCommerce" et "client". Comme ca, les clients importes et les futurs clients automatiques ont la meme segmentation de base.

[Montre le bouton d'import et le compteur]

Etape 5 : lance l'import. FluentCRM traite les contacts par lots. Sur une base de 500 clients, ca prend quelques minutes. Tu vois le compteur avancer en temps reel.

**[ECRAN — screencast verification post-import]**

[Ouvre un contact importe, montre l'onglet WooCommerce]

Etape 6 : verifie le resultat. Ouvre un contact importe. Dans sa fiche, tu dois voir un onglet ou une section "Purchase History" avec ses commandes WooCommerce : produits, montants, dates. Si cette section est vide, l'import n'a pas fonctionne correctement — recommence en verifiant les filtres.

**[ECRAN — slide "Sync auto vs Import ponctuel"]**

[Montre un tableau comparatif]

Maintenant, la question : sync auto ou import ponctuel ?

Sync automatique — c'est ce qu'on a active dans la lecon 9.1. Chaque nouvelle commande cree ou met a jour le contact en temps reel. C'est le mode principal, celui qui tourne en permanence.

Import ponctuel — c'est ce qu'on vient de faire. Tu l'utilises une seule fois, pour rattraper l'historique. Ou ponctuellement si tu migres depuis un autre CRM et que tu veux reimporter une base propre.

La regle : active la sync auto et fais un import ponctuel initial. Apres, tu n'as plus besoin d'importer manuellement — sauf cas exceptionnel.

**[TRANSITION — face camera]**

Ta base est synchronisee. Clients existants importes, futurs clients ajoutes automatiquement. Tu as une vue unifiee dans FluentCRM de tous tes acheteurs WooCommerce. Prochaine etape : capturer des leads directement a l'etape du paiement, avant meme qu'ils aient achete.

---

**Points cles** :
- Import WooCommerce : FluentCRM > Contacts > Import > WooCommerce Customers
- Filtrer par "Completed" pour n'importer que les vrais clients
- Sync auto = mode permanent pour les nouveaux achats
- Import ponctuel = rattrapage initial de l'historique
- Regle : activer la sync auto + faire un seul import initial

**Mots cles SEO** : synchroniser WooCommerce FluentCRM, importer clients WooCommerce CRM, FluentCRM import contacts

---

### Lecon 9.3 — Checkout subscription checkbox : capture des leads a l'achat

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WooCommerce checkout + FluentCRM settings

---

**[INTRO — face camera]**

Un client passe commande sur ta boutique. Il remplit ses infos, son adresse, son moyen de paiement. Et juste avant de valider, il voit une case a cocher : "Recevoir nos conseils et offres par email". S'il coche, il est ajoute a ta liste marketing FluentCRM — avec son consentement explicite. C'est la checkout subscription checkbox. Dans cette lecon, tu la configures et tu comprends pourquoi c'est un des meilleurs endroits pour capturer des abonnes.

**[ECRAN — screencast FluentCRM > Settings > Integrations > WooCommerce]**

[Ouvre les settings de l'integration WooCommerce dans FluentCRM]

Etape 1 : retourne dans FluentCRM > Settings > Integrations > WooCommerce. Cherche la section "Checkout Subscription" ou "Opt-in at Checkout".

[Montre le toggle d'activation]

Etape 2 : active la checkbox de checkout. Un toggle qui ajoute automatiquement une case a cocher sur la page de paiement WooCommerce.

**[ECRAN — screencast configuration de la checkbox]**

[Montre les options de personnalisation]

Etape 3 : personnalise le texte de la checkbox. Le texte par defaut est generique. Remplace-le par quelque chose de concret. Exemples adaptes a la vente de formations :

- "Recevoir les prochaines formations et tutoriels WordPress par email"
- "Etre informe des nouveaux modules et mises a jour de la formation"

Evite les formulations vagues comme "Recevoir notre newsletter". Dis exactement ce que la personne va recevoir.

[Montre le champ liste et tag]

Etape 4 : choisis la liste et le tag pour les contacts qui cochent. Utilise une liste dediee — par exemple "Opt-in Checkout" — pour les distinguer des contacts qui se sont inscrits via un formulaire classique. Tag suggere : "lead-checkout".

[Montre l'option pre-cochee ou non]

Etape 5 : la case doit-elle etre pre-cochee ? Non. Pour le RGPD et la confiance, laisse la case decochee par defaut. Le client doit faire l'action deliberement. Une case pre-cochee, c'est du consentement force — et c'est un probleme legal en Europe.

**[ECRAN — screencast apercu du checkout]**

[Montre la page de checkout WooCommerce avec la checkbox visible]

Etape 6 : visualise le resultat. Va sur ta page de paiement. Tu dois voir la checkbox sous les champs de commande, avant le bouton de validation. Teste avec une commande : si tu coches la case, le contact doit apparaitre dans FluentCRM avec la liste "Opt-in Checkout" et le tag "lead-checkout".

[Montre le contact cree dans FluentCRM avec le bon tag]

Pourquoi c'est si efficace ? Parce que la personne est deja en mode achat. Elle a sorti sa carte bancaire. Elle est engagee. Le taux d'opt-in a ce moment-la est bien plus eleve qu'un formulaire dans la sidebar ou un popup. Et tu recuperes un contact qui a deja prouve un interet commercial fort.

**[TRANSITION — face camera]**

La checkbox de checkout est en place. Chaque client qui coche est automatiquement ajoute a ta liste marketing — avec son consentement. Combine ca avec les tags par produit qu'on va configurer dans la prochaine lecon, et tu obtiens une segmentation precise des que l'achat est finalise.

---

**Points cles** :
- Checkout subscription = case a cocher opt-in sur la page de paiement WooCommerce
- Texte concret et specifique — pas de "newsletter" generique
- Case decochee par defaut (RGPD)
- Liste et tag dedies pour distinguer ces leads des autres
- Taux d'opt-in eleve car le client est deja en mode achat

**Mots cles SEO** : FluentCRM checkout opt-in, WooCommerce subscription checkbox, capture leads checkout WordPress

---

### Lecon 9.4 — Segmente par produit et par montant d'achat

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automations + segments

---

**[INTRO — face camera]**

Tous tes clients ne sont pas les memes. Celui qui a achete un ebook a 19 euros n'a pas le meme profil que celui qui a pris une formation complete a 497 euros. Et celui qui a achete le module CRM n'a pas les memes besoins que celui qui a pris le module SEO. Dans cette lecon, tu mets en place un systeme de tags automatiques par produit achete et par montant. Ca te donne une segmentation fine sans aucun travail manuel apres la configuration initiale.

**[ECRAN — screencast FluentCRM > Automations > New Automation]**

[Cree une nouvelle automation]

Etape 1 : cree une nouvelle automation dediee au tagging post-achat. Nomme-la "Auto-tag WooCommerce" — c'est une automation utilitaire qui tourne en arriere-plan en permanence.

[Montre le choix du trigger]

Etape 2 : choisis le trigger "New Order (WooCommerce)" ou "Order Completed". La difference : "New Order" se declenche des que la commande est creee, "Order Completed" attend que le paiement soit confirme. Pour le tagging, utilise "Order Completed" — tu ne veux pas taguer quelqu'un qui n'a pas encore paye.

**[ECRAN — screencast configuration du tagging par produit]**

[Montre les conditions du trigger]

Etape 3 : le tagging par produit. Tu as deux approches.

Approche 1 — une automation par produit. Tu crees un trigger avec la condition "Specific Product" et tu choisis le produit. Puis tu ajoutes l'action "Apply Tag" avec un tag propre au produit. Par exemple : "a-achete-module-crm", "a-achete-module-seo", "a-achete-module-lms".

[Montre la configuration du trigger avec produit specifique]

Approche 2 — une seule automation avec des conditions. Tu utilises un trigger generique "Order Completed", puis des blocs conditionnels "If product is X, apply tag Y". Plus compact, mais plus complexe a maintenir si tu as beaucoup de produits.

Ma recommandation pour la vente de formations : une automation par produit. C'est plus clair a lire, plus facile a debugger, et tu vois immediatement quel produit declenche quoi.

[Montre la creation du tag et son application]

Etape 4 : cree tes tags produit avec une convention de nommage coherente. Le format "a-achete-[nom-produit]" est clair. Exemples :
- a-achete-module-crm
- a-achete-module-seo
- a-achete-formation-complete
- a-achete-ebook-wordpress

**[ECRAN — screencast segmentation par montant d'achat]**

[Montre la creation d'un segment dynamique]

Etape 5 : la segmentation par montant d'achat. Va dans FluentCRM > Contacts > Segments (ou Smart Segments si disponible). Cree des segments bases sur la valeur client.

[Montre la configuration des conditions de segment]

Trois segments utiles :
- "Petit acheteur" : total des achats inferieur a 50 euros
- "Acheteur confirme" : total entre 50 et 200 euros
- "Client premium" : total superieur a 200 euros

Pour les formations schoolsWP, adapte les seuils a tes prix. Si ta formation complete est a 497 euros, le seuil "premium" sera plus haut.

[Montre comment utiliser les proprietes WooCommerce dans les conditions]

FluentCRM donne acces aux donnees de commande dans les segments : nombre de commandes, montant total, derniere commande. Utilise "Total order value" ou "Lifetime value" selon ce qui est disponible dans ta version.

**[ECRAN — screencast cas concret schoolsWP]**

[Montre un exemple complet]

Etape 6 : cas concret pour la vente de formations. Un client achete le Module CRM a 97 euros. L'automation "Auto-tag WooCommerce" se declenche. Le tag "a-achete-module-crm" est applique. Le contact tombe dans le segment "Acheteur confirme" (entre 50 et 200 euros).

Plus tard, dans la lecon 9.6, on utilisera ces tags pour proposer un upsell cible : "Tu as le module CRM — voici le module Automation qui le complete."

**[TRANSITION — face camera]**

Tes clients sont maintenant segmentes automatiquement par produit achete et par montant. Chaque achat enrichit le profil du contact sans intervention manuelle. C'est la base de toute personnalisation email serieuse. Dans la prochaine lecon, on s'attaque au panier abandonne — le levier le plus sous-utilise dans la vente de formations en ligne.

---

**Points cles** :
- Trigger "Order Completed" (pas "New Order") pour tagger apres paiement confirme
- Convention de tag : "a-achete-[nom-produit]"
- Une automation par produit = plus clair et plus maintenable
- Segments par montant : petit acheteur, confirme, premium — adapter les seuils a tes prix
- Ces tags sont la base des upsells et de la personnalisation post-achat

**Mots cles SEO** : FluentCRM segmentation WooCommerce, tag automatique produit FluentCRM, segmenter clients WordPress CRM

---

### Lecon 9.5 — Configure le panier abandonne

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + WooCommerce

---

**[INTRO — face camera]**

Un visiteur ajoute ta formation au panier. Il va jusqu'a la page de paiement. Il remplit son email. Et il part. Pas de commande, pas de paiement. C'est le panier abandonne — et ca concerne en moyenne 70% des paniers en e-commerce. Pour la vente de formations, le taux est encore plus eleve parce que l'achat est rarement impulsif. La bonne nouvelle : avec FluentCRM, tu peux relancer ces contacts automatiquement. Et le message pour une formation n'a rien a voir avec celui d'un t-shirt — on va voir exactement quoi ecrire.

**[ECRAN — screencast FluentCRM > Settings > WooCommerce > Abandoned Cart]**

[Ouvre les settings d'integration WooCommerce]

Etape 1 : active le tracking des paniers abandonnes. Dans FluentCRM > Settings > Integrations > WooCommerce, cherche la section "Cart Tracking" ou "Abandoned Cart". Active le toggle.

[Montre les options de tracking]

Ce que FluentCRM fait concretement : des qu'un visiteur saisit son email sur la page de paiement, FluentCRM capture cet email et surveille si la commande aboutit. Si apres un delai defini il n'y a pas de commande finalisee, le contact est marque comme "panier abandonne".

**[ECRAN — screencast configuration du delai]**

[Montre le parametre de delai]

Etape 2 : configure le delai avant de considerer un panier comme abandonne. Le delai par defaut est generalement 15 a 30 minutes. Pour la vente de formations, monte a 60 minutes. Pourquoi ? Parce que l'achat d'une formation est reflechi. La personne compare, lit les avis, verifie son budget. Si tu la relances apres 15 minutes, c'est trop agressif. 60 minutes lui laissent le temps de revenir par elle-meme.

**[ECRAN — screencast creation de l'automation de relance]**

[Cree une nouvelle automation]

Etape 3 : cree l'automation de relance. Nouvelle automation, trigger "Abandoned Cart" (WooCommerce). Ce trigger se declenche quand le delai est depasse et que la commande n'a pas ete finalisee.

[Montre le builder avec les blocs]

Etape 4 : construis la sequence de relance. Trois emails, espaces dans le temps. Voici le timing optimal pour la vente de formations :

[Montre le premier email avec delai]

Email 1 — 1 heure apres l'abandon. Objet : "Ta formation t'attend". Pas de pression commerciale. Le ton est serviable. Contenu : rappel de ce qu'il y a dans le panier, lien direct pour finaliser, et une question simple — "Tu as une question sur la formation ? Reponds a cet email." Pour une formation, les objections sont souvent specifiques : "Est-ce que ca couvre mon cas ?", "Est-ce que c'est adapte a mon niveau ?". En ouvrant le dialogue, tu traites l'objection.

[Montre le deuxieme email avec delai de 24h]

Email 2 — 24 heures apres l'abandon. Objet : "Ce que tu vas apprendre dans [nom de la formation]". Ici, tu developpes la valeur. Pas un rappel du panier — un rappel de ce que la formation resout. Liste 3 a 5 benefices concrets. Si tu as des temoignages, c'est ici que tu les places. Un temoignage d'un apprenant qui avait la meme hesitation est tres efficace.

[Montre le troisieme email avec delai de 72h]

Email 3 — 72 heures apres l'abandon. Objet : "Derniere question avant de fermer ton dossier". Le dernier email est une cloture. Pas d'urgence artificielle, pas de fausse rarete. Une question directe : "J'ai vu que tu avais commence l'inscription a [formation]. Est-ce que quelque chose t'a bloque ? Si la formation ne correspond pas a ton besoin, dis-le moi — je peux t'orienter vers une meilleure option." Ce ton respectueux convertit mieux que n'importe quelle tactique de pression.

**[ECRAN — screencast ajout du goal de sortie]**

[Ajoute un Goal dans l'automation]

Etape 5 : ajoute un goal "Order Completed" dans l'automation. Si le contact finalise sa commande apres le premier email, il ne doit pas recevoir les suivants. Le goal fait exactement ca — on l'a vu dans le module 7. Place-le en mode optionnel : s'il achete, il sort de la sequence. S'il ne repond a aucun des 3 emails, il sort naturellement a la fin.

**[ECRAN — screencast difference formation vs e-commerce]**

[Montre un slide comparatif]

Etape 6 : comprends la difference entre un panier abandonne e-commerce classique et un panier abandonne formation. En e-commerce classique, le message c'est "Tu as oublie quelque chose dans ton panier" — parce que souvent, c'est un oubli reel. Pour une formation, personne n'oublie. Le visiteur a hesite. Le message doit traiter l'hesitation, pas rappeler l'oubli. D'ou le ton serviable et les questions ouvertes dans les emails qu'on a construits.

**[TRANSITION — face camera]**

Ton systeme de relance de panier abandonne est en place. Trois emails, espaces intelligemment, avec un ton adapte a la vente de formations. Le goal protege les acheteurs des relances inutiles. Ce seul mecanisme peut recuperer 10 a 15% des paniers abandonnes — sur une formation a 200 euros, ca represente du chiffre d'affaires reel. Dans la prochaine lecon, on construit le funnel d'upsell post-achat.

---

**Points cles** :
- Activer le cart tracking dans FluentCRM > WooCommerce settings
- Delai recommande pour les formations : 60 minutes (pas 15)
- 3 emails : serviable (1h), valeur (24h), cloture respectueuse (72h)
- Goal "Order Completed" pour sortir les acheteurs de la sequence
- Ton formation ≠ ton e-commerce : traiter l'hesitation, pas l'oubli

**Mots cles SEO** : FluentCRM panier abandonne, abandoned cart FluentCRM WooCommerce, relance panier WordPress, recuperer panier abandonne formation

---

### Lecon 9.6 — Cree un funnel d'upsell post-achat

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Un client vient d'acheter une formation. Il est satisfait, il progresse. C'est le meilleur moment pour lui proposer la suite logique. Pas un email de vente generique — une recommandation personnalisee basee sur ce qu'il a deja achete. Dans cette lecon, tu construis un funnel d'upsell post-achat dans FluentCRM. Et on utilise les tags produit qu'on a configures dans la lecon 9.4.

**[ECRAN — screencast FluentCRM > Automations > New Automation]**

[Cree une nouvelle automation]

Etape 1 : cree une nouvelle automation "Upsell post-achat — Module CRM vers Automation". On part d'un cas concret schoolsWP : un client achete le module CRM, et tu veux lui proposer le module Automation 7 jours plus tard.

[Montre le choix du trigger]

Etape 2 : choisis le trigger "Tag Applied" et selectionne le tag "a-achete-module-crm". Des qu'un contact recoit ce tag — donc des qu'il achete le module CRM — il entre dans ce funnel.

**[ECRAN — screencast construction du funnel]**

[Montre le delai de 7 jours]

Etape 3 : ajoute un delai de 7 jours. Pourquoi 7 jours ? Parce que le client doit avoir le temps de consommer le contenu et d'en voir la valeur. Si tu proposes un upsell 2 heures apres l'achat, tu donnes l'impression de ne vouloir que son argent. 7 jours, c'est le temps de decouvrir la formation, de commencer a l'appliquer, et de realiser qu'il a besoin de la suite.

[Ajoute un bloc conditionnel]

Etape 4 : ajoute une condition. Verifie que le contact n'a PAS deja le tag "a-achete-module-automation". Si quelqu'un a achete les deux modules en meme temps — ou s'il a achete le module Automation entre-temps — pas besoin de lui envoyer un upsell.

[Montre la branche "n'a pas le tag"]

Sur la branche "n'a pas le tag" — c'est la qu'on construit la sequence d'upsell.

**[ECRAN — screencast creation des emails d'upsell]**

[Montre le premier email]

Etape 5 : cree la sequence d'upsell. Trois emails, espaces de 3 jours chacun.

Email 1 — "Tu maitrises ton CRM — voici l'etape suivante". Contenu : felicite le client pour son avancement. Explique le lien naturel entre CRM et automation. Montre un cas concret : "Avec le module Automation, tu peux declencher un email de bienvenue personnalise des qu'un contact remplit ton formulaire — sans toucher a rien manuellement." Pas de CTA d'achat dans ce premier email. Juste de la valeur et une graine plantee.

[Montre le deuxieme email avec delai]

Email 2 — 3 jours plus tard. "3 automations que tu pourrais mettre en place maintenant". Contenu : liste 3 scenarios concrets que le client pourrait realiser avec le module Automation, en se basant sur ce qu'il connait deja du CRM. Par exemple : relance automatique des leads inactifs, sequence d'onboarding pour les nouveaux contacts, email d'anniversaire. CTA : lien vers la page du module Automation.

[Montre le troisieme email avec delai]

Email 3 — 3 jours plus tard. "Question rapide sur ton avancement CRM". Contenu : un email court, personnel. "Comment avances-tu avec le module CRM ? Si tu bloques quelque part, reponds a cet email. Et si tu veux passer a la vitesse superieure, le module Automation est concu pour prendre la suite exactement ou le CRM s'arrete." CTA discret vers la page produit.

**[ECRAN — screencast goal et fin du funnel]**

[Ajoute un goal dans l'automation]

Etape 6 : ajoute un goal "Tag Applied" > "a-achete-module-automation" en mode optionnel. Si le client achete apres le premier ou le deuxieme email, il sort du funnel immediatement. Les emails suivants ne sont pas envoyes.

[Montre la fin du funnel]

Apres le goal, tu peux ajouter un email de bienvenue dans le nouveau module — ou laisser l'automation d'onboarding du module Automation prendre le relais.

**[TRANSITION — face camera]**

Ton funnel d'upsell est en place. Un client qui achete le module CRM recoit, 7 jours plus tard, une sequence personnalisee qui l'amene naturellement vers le module Automation. Le goal protege ceux qui achetent en cours de route. Duplique cette automation pour chaque paire de produits complementaires dans ton catalogue. Dans la prochaine lecon, on explore tous les triggers WooCommerce disponibles dans les automations FluentCRM.

---

**Points cles** :
- Trigger : tag produit applique (configurer dans 9.4)
- Delai de 7 jours avant le premier upsell — le client doit d'abord consommer
- Condition de sortie : verifier que le client n'a pas deja le produit upsell
- 3 emails : valeur (J7), cas concrets (J10), question personnelle (J13)
- Goal optionnel pour sortir les acheteurs de la sequence

**Mots cles SEO** : FluentCRM upsell automation, funnel post-achat WooCommerce, email upsell formation WordPress

---

### Lecon 9.7 — Triggers WooCommerce dans les automations

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Dans les lecons precedentes, on a utilise deux triggers WooCommerce : "Order Completed" et "Abandoned Cart". Mais FluentCRM propose bien plus de declencheurs lies a WooCommerce. Dans cette lecon, on fait le tour complet des triggers disponibles — et surtout, on voit dans quel cas concret utiliser chacun.

**[ECRAN — screencast FluentCRM > Automations > New > Triggers WooCommerce]**

[Ouvre le choix des triggers, filtre sur WooCommerce]

Etape 1 : quand tu crees une nouvelle automation, tu vois la liste des triggers. Filtre sur "WooCommerce" pour afficher uniquement les declencheurs lies a ta boutique. Selon ta version de FluentCRM (free vs Pro) et les addons installes, tu verras entre 4 et 8 triggers.

**[ECRAN — screencast trigger par trigger]**

[Montre chaque trigger avec sa configuration]

Etape 2 : passons-les en revue.

**Trigger 1 — New Order Created.** Se declenche quand une commande est creee dans WooCommerce, quel que soit son statut. Le client a clique sur "Commander" — la commande existe, mais le paiement n'est pas forcement confirme. Usage : notification interne, logging. A eviter pour les automations client — le paiement peut echouer.

**Trigger 2 — Order Completed.** Se declenche quand le paiement est confirme et la commande passe en statut "Completed". C'est le trigger le plus fiable pour les actions post-achat : tagging, onboarding, upsell. C'est celui qu'on a utilise dans les lecons precedentes.

[Montre la configuration avec filtre produit]

**Trigger 3 — Order Completed for Specific Product.** Meme chose, mais filtre sur un produit specifique. Si tu veux une automation qui se declenche uniquement quand quelqu'un achete le Module CRM et pas un autre produit. Alternative a l'approche "tag applied" de la lecon 9.4 — les deux fonctionnent, mais le tag est plus flexible.

**Trigger 4 — Order Refunded.** Se declenche quand une commande est remboursee. Usage concret : retirer le tag produit, envoyer un email de feedback ("Qu'est-ce qui n'a pas fonctionne ?"), retirer l'acces a la formation si tu geres les acces manuellement.

[Montre la configuration du trigger refund]

Important : si tu utilises des tags "a-achete-X", pense a les retirer automatiquement sur un remboursement. Sinon, ton upsell continuera a considerer le contact comme acheteur alors qu'il a ete rembourse.

**Trigger 5 — Abandoned Cart.** On l'a vu en detail dans la lecon 9.5. Se declenche quand un panier est abandonne apres le delai configure.

[Montre le trigger s'il existe]

**Trigger 6 — Order Status Changed.** Se declenche quand le statut d'une commande change — de "Processing" a "Completed", de "Completed" a "Refunded", etc. Plus avance. Usage : workflows internes, synchronisation avec un outil externe, mise a jour de scores dans un Google Sheet.

**[ECRAN — slide recapitulatif]**

[Montre un tableau des triggers avec usage recommande]

Etape 3 : voici le recapitulatif des triggers et quand les utiliser.

| Trigger | Quand l'utiliser |
|---------|-----------------|
| New Order Created | Notification interne uniquement |
| Order Completed | Tagging, onboarding, upsell — le trigger principal |
| Specific Product | Automation dediee a un produit |
| Order Refunded | Retrait tag, email feedback, retrait acces |
| Abandoned Cart | Relance panier abandonne |
| Status Changed | Workflows internes avances |

Pour 90% de tes besoins en vente de formations, "Order Completed" et "Abandoned Cart" suffisent. Les autres sont des outils de precision pour des cas specifiques.

**[ECRAN — screencast combinaison de triggers]**

[Montre un exemple d'automation avec trigger + condition]

Etape 4 : combine trigger et conditions. Par exemple, un trigger "Order Completed" + condition "Montant > 200 euros" + action "Apply Tag: client-premium" + action "Send email: bienvenue VIP". Tu peux construire des parcours tres precis en combinant le declencheur avec les blocs conditionnels du builder.

**[TRANSITION — face camera]**

Tu connais maintenant tous les triggers WooCommerce disponibles dans FluentCRM. Le plus important : "Order Completed" pour le post-achat, "Abandoned Cart" pour la relance, "Order Refunded" pour le nettoyage. Les autres sont utiles dans des cas precis que tu rencontreras quand ta boutique grandira. Dans la prochaine lecon, tu mets tout ca en pratique avec un exercice complet.

---

**Points cles** :
- 6 triggers WooCommerce principaux dans FluentCRM
- "Order Completed" = trigger principal pour 90% des automations post-achat
- "Order Refunded" = penser a retirer les tags et acces
- "New Order Created" ≠ paiement confirme — ne pas utiliser pour les automations client
- Combiner triggers + conditions pour des parcours precis

**Mots cles SEO** : FluentCRM triggers WooCommerce, declencheurs WooCommerce automation, FluentCRM order trigger WordPress

---

### Lecon 9.8 — Exercice : Configure le panier abandonne pour ta boutique de formations

**Duree** : 6 min
**Type** : Exercice guide
**Ecran** : Face camera pour intro, screencast pour la demo de correction

---

**[INTRO — face camera]**

C'est l'heure de pratiquer. Dans cet exercice, tu configures un systeme complet de relance de panier abandonne pour ta propre boutique de formations. Pas une boutique fictive — la tienne. Si tu n'as pas encore de boutique WooCommerce, utilise un site de test local. L'objectif : a la fin de cet exercice, ton panier abandonne fonctionne et envoie le premier email de relance automatiquement.

**[ECRAN — slide "Cahier des charges"]**

[Affiche les consignes de l'exercice]

Voici ce que tu dois mettre en place :

**Partie 1 — Configuration technique**
- Active le tracking des paniers abandonnes dans FluentCRM
- Delai : 60 minutes
- Verifie que l'integration WooCommerce est active (lecon 9.1)

**Partie 2 — Automation de relance**
- Cree une automation avec le trigger "Abandoned Cart"
- 3 emails de relance aux delais suivants :
  - Email 1 : 1 heure apres l'abandon
  - Email 2 : 24 heures apres l'abandon
  - Email 3 : 72 heures apres l'abandon
- Chaque email doit etre adapte a la vente de formations (pas de ton e-commerce generique)

**Partie 3 — Protection**
- Ajoute un goal "Order Completed" en mode optionnel
- Le contact doit sortir de la sequence des qu'il achete

**Partie 4 — Test**
- Passe une commande test : ajoute un produit au panier, saisis ton email, quitte la page
- Verifie que le contact est capture apres 60 minutes
- Verifie que le premier email est envoye

**[ECRAN — slide "Criteres de reussite"]**

[Affiche les criteres]

Ton exercice est reussi si :
1. Le tracking de panier est actif dans les settings
2. L'automation existe avec le bon trigger
3. Les 3 emails ont un ton adapte aux formations (pas "Vous avez oublie quelque chose")
4. Le goal est en place et fonctionne
5. Le test confirme que le premier email part

**[ECRAN — screencast correction rapide]**

[Montre la configuration attendue etape par etape]

Voici la correction rapide. Je te montre le resultat attendu pour chaque partie.

Pour le tracking : le toggle est actif, le delai est a 60 minutes.

Pour l'automation : trigger "Abandoned Cart", puis bloc delai 1 heure, puis email 1, puis delai 23 heures, puis email 2, puis delai 48 heures, puis email 3. Le goal "Order Completed" est place en parallele sur toute la sequence.

[Montre le schema de l'automation complete]

Attention aux delais : l'email 1 part 1 heure apres le trigger. L'email 2 part 24 heures apres le trigger, donc le delai entre email 1 et email 2 est de 23 heures, pas 24. Meme logique pour l'email 3 : 72 heures apres le trigger, soit 48 heures apres l'email 2.

Pour les emails : l'email 1 est serviable ("Tu as une question ?"), l'email 2 montre la valeur ("Voici ce que tu vas apprendre"), l'email 3 est une cloture respectueuse ("Derniere question avant de fermer ton dossier"). Si tes emails ressemblent a "Reviens acheter !", c'est a revoir.

**[TRANSITION — face camera]**

Si ton test fonctionne, bravo — tu as un systeme de recuperation de panier abandonne operationnel. Si ca ne marche pas, reprends la lecon 9.5 et verifie chaque etape. Le panier abandonne est un des mecanismes les plus rentables de toute ta boutique — ca vaut le coup de le configurer correctement.

---

**Points cles** :
- Exercice pratique sur ta propre boutique (pas un cas fictif)
- 4 parties : config technique, automation, protection, test
- Attention aux calculs de delai entre les emails
- Ton des emails = adapte aux formations, pas au e-commerce generique
- Test obligatoire pour valider le fonctionnement

---

### Lecon 9.9 — Quiz : Valide tes acquis M9

**Duree** : 5 min
**Type** : Quiz (8 QCM)
**Plateforme** : TutorLMS Quiz

---

**[INTRO — face camera]**

Derniere lecon du module 9. 8 questions pour verifier que tu maitrises l'integration WooCommerce + FluentCRM. Prends ton temps — chaque question a une seule bonne reponse.

---

**Question 1 : Ou active-t-on l'integration WooCommerce dans FluentCRM ?**

A) FluentCRM > Dashboard > Widgets
B) FluentCRM > Settings > Integrations
C) WooCommerce > Settings > FluentCRM
D) WordPress > Plugins > FluentCRM > WooCommerce

**Reponse correcte : B**
Explication : L'integration se configure dans FluentCRM > Settings > Integrations. Le toggle WooCommerce y apparait si le plugin est actif.

---

**Question 2 : Quelle est la difference entre "sync auto" et "import ponctuel" pour les clients WooCommerce ?**

A) La sync auto est plus rapide que l'import ponctuel
B) L'import ponctuel fonctionne en temps reel, la sync auto est periodique
C) La sync auto cree les contacts a chaque nouvel achat, l'import ponctuel rattrape l'historique existant
D) Il n'y a pas de difference, les deux font la meme chose

**Reponse correcte : C**
Explication : La sync auto tourne en permanence et cree un contact a chaque commande. L'import ponctuel sert a recuperer les clients qui ont achete avant l'activation de l'integration.

---

**Question 3 : Pourquoi la checkbox d'opt-in au checkout doit-elle etre decochee par defaut ?**

A) Pour eviter de surcharger la base FluentCRM
B) Pour respecter le RGPD — le consentement doit etre un acte delibere
C) Pour ameliorer la vitesse de chargement de la page
D) Parce que FluentCRM ne supporte pas les cases pre-cochees

**Reponse correcte : B**
Explication : Le RGPD exige un consentement actif. Une case pre-cochee est consideree comme du consentement force et pose un probleme legal en Europe.

---

**Question 4 : Quel trigger utiliser pour le tagging automatique post-achat ?**

A) New Order Created
B) Order Completed
C) Cart Updated
D) Customer Registered

**Reponse correcte : B**
Explication : "Order Completed" se declenche apres confirmation du paiement. "New Order Created" se declenche avant — le paiement peut encore echouer.

---

**Question 5 : Quel delai est recommande avant de considerer un panier comme abandonne pour la vente de formations ?**

A) 5 minutes
B) 15 minutes
C) 60 minutes
D) 24 heures

**Reponse correcte : C**
Explication : 60 minutes est le delai recommande pour les formations. L'achat est reflechi — un delai trop court est trop agressif, un delai de 24h est trop long et laisse le contact refroidir.

---

**Question 6 : Quel est le bon ton pour un email de relance de panier abandonne sur une formation ?**

A) Urgence : "Plus que 2 places disponibles !"
B) Rappel direct : "Tu as oublie quelque chose dans ton panier"
C) Serviable : "Tu as une question sur la formation ?"
D) Promotionnel : "Profite de -30% si tu commandes dans l'heure"

**Reponse correcte : C**
Explication : Pour une formation, personne n'oublie son panier — le visiteur a hesite. Le message doit traiter l'hesitation avec un ton serviable, pas rappeler un oubli ou creer une urgence artificielle.

---

**Question 7 : Pourquoi attendre 7 jours avant d'envoyer un email d'upsell post-achat ?**

A) Pour respecter la loi anti-spam
B) Pour laisser le client consommer le contenu et en voir la valeur
C) Parce que FluentCRM impose un delai minimum de 7 jours
D) Pour que le taux d'ouverture soit meilleur le week-end

**Reponse correcte : B**
Explication : Le client doit avoir le temps de decouvrir sa formation et d'en tirer de la valeur. Un upsell immediat donne l'impression que tu ne veux que son argent.

---

**Question 8 : Que doit-on faire quand une commande WooCommerce est remboursee ?**

A) Rien — FluentCRM gere tout automatiquement
B) Supprimer le contact de FluentCRM
C) Retirer le tag produit et eventuellement l'acces a la formation
D) Envoyer un email de relance pour proposer un autre produit

**Reponse correcte : C**
Explication : Sur un remboursement, il faut retirer le tag "a-achete-X" pour que le contact ne soit plus considere comme acheteur dans les automations (upsells, segments). L'acces a la formation doit aussi etre retire si tu le geres manuellement.

---

**[TRANSITION — face camera]**

Module 9 termine. Tu sais maintenant connecter WooCommerce a FluentCRM, synchroniser tes clients, capturer des leads au checkout, segmenter par produit et par montant, relancer les paniers abandonnes, et construire des upsells post-achat. C'est un des modules les plus concrets de la formation — chaque mecanisme que tu as configure genere du chiffre d'affaires directement. Active-les sur ta boutique et observe les resultats.

---

**Points cles du quiz** :
- 8 questions couvrant les 7 lecons du module
- Themes : integration, sync, checkout opt-in, triggers, panier abandonne, upsell, remboursement
- Score de passage recommande : 6/8 (75%)

**Configuration TutorLMS** :
- Type : Multiple choice, single answer
- Tentatives : illimitees
- Score minimum : 75%
- Feedback : affiche l'explication apres chaque reponse
