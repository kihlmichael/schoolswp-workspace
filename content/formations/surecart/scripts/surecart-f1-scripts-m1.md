# Scripts vidéo - F1 Module 1 : Installer et connecter SureCart

**Formation** : Vendre sans WooCommerce (SureCart) - méthode CAISSE (parcours F1)
**Module** : M1 - Installer et connecter (payant, 1er module de la méthode)
**Leçons** : 8 vidéos + 1 quiz + 1 checklist d'installation
**Durée totale** : ~31 min
**Type** : Vidéo HeyGen + voix ElevenLabs
**Date** : 2026-06-04
**Sources** : `_sources/docs-kb/` (installing-surecart, getting-started, second-steps, third-steps, add-surecart-api, api-token-wp-config, connect-stripe, configuring-apple-pay, connect-paypal, set-up-your-branding, light-and-dark-logo, switching-store-currency, translating-surecart, notification-language, set-dark-mode, caching, plugin-performance, how-to-make-test-payments, clear-test-data)

> Rôle de ce module : poser une base technique propre et prête à encaisser. C'est le premier module payant, donc on passe du pourquoi au comment. Beaucoup de manipulation à l'écran : privilégier le screencast guidé, étape par étape, sans survol. À la fin, l'élève a une boutique connectée, brandée, traduite, et un paiement test réussi.

---

### Leçon 1.1 : Installer le plugin et créer ton compte SureCart

**Durée** : ~4 min (~650 mots)
**Objectif pédagogique** : Installer le plugin, dérouler l'assistant de configuration, et surtout rattacher la boutique à un compte SureCart (étape critique souvent zappée).
**Écran** : Screencast WordPress (installation plugin, assistant), zoom sur le bandeau Complete Setup.

---

**[INTRO - face caméra]**

On entre dans le concret. Dans cette leçon, on installe SureCart sur ton site et on crée ton compte. Rien de compliqué, mais il y a une étape à la fin que beaucoup de gens sautent, et qui peut leur coûter leur boutique. Je te montre tout, dans l'ordre.

**[SECTION 1 - Installer le plugin]**

**[ÉCRAN - screencast : Extensions, Ajouter, recherche SureCart]**

Dans ton tableau de bord WordPress, va dans Extensions, puis Ajouter une extension. Dans le champ de recherche, tape SureCart. Tu cliques sur Installer, puis sur Activer. C'est exactement la même manipulation que pour n'importe quelle extension WordPress.

Une fois l'extension activée, un nouveau menu SureCart apparaît dans la barre latérale de WordPress. C'est de là qu'on va tout piloter.

**[SECTION 2 - L'assistant de configuration]**

**[ÉCRAN - screencast de l'assistant SureCart]**

Passe la souris sur le menu SureCart et clique sur Get Started, démarrer. Sur l'écran d'accueil, choisis Create New Store, créer une nouvelle boutique.

L'assistant te pose quatre questions simples. La couleur de ta marque, qui sera reprise sur tes pages. La devise de ta boutique, celle qui servira à toutes tes transactions. Choisis-la bien dès maintenant, je t'expliquerai pourquoi dans la leçon sur les réglages. Ensuite, tu choisis entre partir de zéro, une boutique vide, ou démarrer avec des produits de démonstration. Pour apprendre, les produits de démo sont pratiques, tu pourras les supprimer ensuite. Enfin, tu confirmes une adresse email pour recevoir les notifications de commande.

Tu cliques sur Continuer à chaque étape, puis sur View My Products pour arriver sur ton tableau de bord. La couleur et l'email pourront être changés plus tard, donc ne bloque pas dessus.

**[SECTION 3 - L'étape à ne surtout pas zapper]**

**[ÉCRAN - zoom sur le bandeau vert "Complete Setup"]**

Voilà l'étape critique. Après l'assistant, tu vois un bandeau vert en haut de ton écran avec un bouton Complete Setup, finaliser la configuration. Clique dessus.

Là, tu crées ton compte SureCart ou tu te connectes si tu en as déjà un, et tu valides ton adresse email via le mail de confirmation que tu reçois. C'est cette action qui revendique ta boutique, qui la rattache officiellement à ton compte.

Pourquoi c'est important ? Parce qu'une boutique non rattachée est considérée comme abandonnée, et elle peut être supprimée. Tu ne veux pas construire toute ta boutique sur une base qui peut disparaître. Donc tu fais ça maintenant, avant d'aller plus loin. Quand c'est fait, le bandeau disparaît et la vérification de ton email débloque toutes les fonctions de ton compte.

**[OUTRO - face caméra]**

Voilà, le plugin est installé et ton compte est créé et rattaché. Mais pour l'instant, le plugin sur ton site et la plateforme SureCart ne se parlent pas encore vraiment. Pour les relier proprement, il faut une clé, le jeton API. C'est ce qu'on fait dans la prochaine leçon, et je vais te montrer deux façons de le faire, dont une plus solide que l'autre.

---

**Points clés** :

- Installation classique : Extensions, Ajouter, rechercher SureCart, Installer, Activer.
- L'assistant demande couleur, devise, départ de zéro ou démo, email de notification.
- Étape critique : cliquer sur Complete Setup dans le bandeau vert pour rattacher la boutique à un compte SureCart. Une boutique non rattachée peut être supprimée.
- Valider l'email débloque toutes les fonctions du compte.

**Mots clés SEO** : installer SureCart, configurer SureCart, créer un compte SureCart, assistant configuration SureCart, Complete Setup SureCart

---

### Leçon 1.2 : Connecter le plugin à la plateforme avec la clé API

**Durée** : ~4 min (~700 mots)
**Objectif pédagogique** : Récupérer le jeton API et connecter le plugin, via l'admin (méthode standard) puis via wp-config.php (méthode plus robuste pour les sites protégés par un plugin de sécurité).
**Écran** : Screencast app.surecart.com (section API), screencast réglages Connection, capture wp-config.php.

---

**[INTRO - face caméra]**

Ton plugin et la plateforme SureCart doivent se parler. Le pont entre les deux, c'est une clé, ce qu'on appelle un jeton API. On la met en place une fois, et on n'y touche plus. Je te montre la méthode simple, par l'interface, puis une méthode plus solide si tu utilises un plugin de sécurité qui a tendance à casser ce genre de connexion.

**[SECTION 1 - Récupérer ton jeton API]**

**[ÉCRAN - screencast app.surecart.com, menu API, onglet Secret Token]**

Rends-toi sur app point surecart point com, la plateforme. Dans le menu latéral, clique sur API. Sélectionne l'onglet Secret Token, jeton secret. Tu vois ta clé affichée à l'écran. Elle commence toujours par s-t-tiret. Copie-la.

Un mot de prudence : ce jeton donne accès à ta boutique. Tu le traites comme un mot de passe. Tu ne le partages pas, tu ne le colles pas dans un email ou un message public. À l'écran, je floute le mien.

**[SECTION 2 - La méthode standard : par l'interface]**

**[ÉCRAN - screencast WordPress : SureCart, Settings, Connection]**

Retourne sur WordPress. Va dans SureCart, Settings, réglages, puis l'onglet Connection, connexion. Colle ton jeton dans le champ API Token et clique sur Save, enregistrer.

C'est fait. Le statut affiche maintenant Connected, connecté. Pour la grande majorité des sites, cette méthode suffit parfaitement. Si un jour ton site affiche déconnecté, tu reviens ici et tu recolles la clé.

**[SECTION 3 - La méthode robuste : dans wp-config.php]**

**[ÉCRAN - capture d'un wp-config.php avec la ligne define]**

Maintenant, une méthode plus solide, utile dans un cas précis. Certains plugins de sécurité régénèrent régulièrement les clés internes de WordPress, ce qu'on appelle les salts. Quand ça arrive, le jeton stocké en base de données peut être invalidé, et ta boutique se déconnecte toute seule. C'est frustrant.

La parade, c'est de définir ton jeton directement dans le fichier wp-config.php, à la racine de ton site. Là, il survit aux régénérations de salts et aux migrations de site.

Avant toute chose, sauvegarde une copie de ton wp-config.php. Si tu fais une faute de frappe dans ce fichier, ton site peut ne plus se charger, et la copie te permet de revenir en arrière. Ensuite, ouvre le fichier et cherche la ligne qui dit, en anglais, That's all, stop editing. Juste au-dessus de cette ligne, tu ajoutes ta ligne avec define, le nom SURECART_API_TOKEN, et ta clé entre guillemets.

Important : la ligne doit être au-dessus du That's all, stop editing, sinon SureCart ne la lira pas à temps. Tu enregistres, tu réuploades le fichier, et tu vérifies dans SureCart, Settings, Connection que le statut est bien Connected.

Cette méthode, je la recommande surtout si tu utilises un plugin de sécurité costaud. Si tu n'es pas à l'aise avec l'édition de fichiers, reste sur la méthode par l'interface : elle fonctionne très bien.

**[OUTRO - face caméra]**

Ton site et la plateforme sont maintenant reliés. Mais relier SureCart à la plateforme, ce n'est pas encore relier l'argent. Pour encaisser, il te faut un processeur de paiement. On commence par le plus utilisé, Stripe, dans la prochaine leçon.

---

**Points clés** :

- Le jeton API se récupère sur app.surecart.com, menu API, onglet Secret Token. Il commence par st\_ et se traite comme un mot de passe.
- Méthode standard : SureCart, Settings, Connection, coller le jeton, Save. Statut Connected.
- Méthode robuste (wp-config.php) : définir la constante SURECART_API_TOKEN au-dessus de la ligne "That's all, stop editing". Survit aux migrations et aux régénérations de salts.
- Toujours sauvegarder wp-config.php avant de l'éditer.

**Mots clés SEO** : clé API SureCart, jeton API SureCart, connecter SureCart, SureCart déconnecté, SureCart wp-config

---

### Leçon 1.3 : Connecter Stripe et activer Apple Pay

**Durée** : ~5 min (~800 mots)
**Objectif pédagogique** : Connecter Stripe en mode live et en mode test, et activer Apple Pay côté Stripe (validation de domaine comprise).
**Écran** : Screencast réglages Payment Processors, screencast tableau de bord Stripe.

---

**[INTRO - face caméra]**

C'est le moment d'ouvrir le robinet : connecter ton premier processeur de paiement. On commence par Stripe, le plus répandu, qui gère la carte bancaire et Apple Pay. Je te montre la connexion, et ensuite comment activer Apple Pay proprement, parce que cette partie a un piège que je veux t'éviter.

**[SECTION 1 - Connecter Stripe en mode live]**

**[ÉCRAN - screencast : SureCart, Settings, Payment Processors]**

Dans WordPress, va dans SureCart, Settings, puis Payment Processors, processeurs de paiement. Tu vois la liste de tous les processeurs disponibles.

Active le bouton Stripe : ça t'envoie sur la plateforme SureCart. Clique sur l'onglet Stripe, ouvre le menu déroulant Connect, connexion, et choisis Live Mode, mode réel. Tu entres ensuite ton email Stripe, ton mot de passe, et le code de vérification reçu sur ton téléphone.

Une fois connecté, tu es redirigé vers la plateforme SureCart, où ton compte Stripe apparaît comme activé. Reviens sur ta page WordPress et rafraîchis-la. Tu vois alors une pastille verte : Stripe est connecté en mode live. Parfois, Stripe met quelques minutes à apparaître sur ton checkout, c'est normal.

**[SECTION 2 - Le mode test de Stripe]**

**[ÉCRAN - screencast : Connect, Test Mode]**

Tu peux aussi connecter Stripe en mode test, pour vérifier tes paiements sans manipuler de vrai argent. Même chemin : onglet Stripe, menu Connect, mais cette fois tu choisis Test Mode. En mode test, tu peux sauter le formulaire, tu n'as pas besoin d'entrer d'informations réelles. On reviendra sur les paiements de test dans la dernière leçon du module.

**[SECTION 3 - Activer Apple Pay côté Stripe]**

**[ÉCRAN - screencast tableau de bord Stripe : Settings, Payments, Payment methods]**

Apple Pay passe par Stripe, et se configure dans ton tableau de bord Stripe, pas dans SureCart. Connecte-toi à Stripe, clique sur l'icône d'engrenage en haut à droite, puis Settings, puis l'onglet Payments. Va dans Payment methods, méthodes de paiement, trouve Apple Pay et active le bouton.

**[ÉCRAN - zoom : Configure domains, Add a new domain]**

Ensuite, clique sur Configure domains, configurer les domaines, puis Add a new domain. Et là, attention au piège : tu dois entrer ton domaine exactement comme il apparaît dans la barre d'adresse de tes visiteurs. Si ton site est sur www point ton-domaine point com, tu mets le www. Si tu mets le mauvais, Apple Pay ne s'affichera pas.

Stripe te demande ensuite de prouver que ce domaine est bien le tien. Tu télécharges un petit fichier de vérification, tu crées un dossier nommé point well-known à la racine de ton site, et tu y déposes ce fichier. Puis tu cliques sur Verify. Si tout est bon, un badge Enabled, activé, apparaît à côté de ton domaine.

**[SECTION 4 - Tester Apple Pay sans piège]**

**[ÉCRAN - slide "Apple Pay : 3 conditions"]**

Trois choses à savoir pour ne pas t'arracher les cheveux pendant le test. Un : Apple Pay sur le web ne fonctionne que dans le navigateur Safari. Deux : tu dois avoir une vraie carte enregistrée dans le portefeuille Apple Pay de ton appareil. Trois : Apple Pay n'est pas disponible dans tous les pays. En mode test Stripe, ta vraie carte est transformée en carte de test, donc tu peux essayer sans débit réel.

**[OUTRO - face caméra]**

Stripe est connecté, Apple Pay est prêt. Beaucoup de créateurs s'arrêtent là, et c'est déjà suffisant pour vendre. Mais certains de tes clients préfèrent PayPal, alors on voit comment l'ajouter dans la prochaine leçon, avec un mot sur les autres processeurs selon ton pays.

---

**Points clés** :

- Stripe se connecte via SureCart, Settings, Payment Processors, onglet Stripe, Connect, Live Mode. Pastille verte après rafraîchissement.
- Mode test disponible (Connect, Test Mode, formulaire à sauter).
- Apple Pay s'active dans Stripe : Payment methods, activer Apple Pay, Configure domains, ajouter le domaine exact (avec www si utilisé), valider via le fichier dans le dossier .well-known.
- Test Apple Pay : uniquement Safari, vraie carte dans le portefeuille, pays compatible.

**Mots clés SEO** : connecter Stripe SureCart, SureCart Stripe, activer Apple Pay SureCart, Apple Pay Stripe domaine, paiement carte SureCart

---

### Leçon 1.4 : Connecter PayPal et les autres processeurs

**Durée** : ~3 min (~500 mots)
**Objectif pédagogique** : Connecter PayPal, comprendre l'avertissement Not Approved, et savoir qu'il existe d'autres processeurs régionaux à choisir selon son pays.
**Écran** : Screencast Payment Processors, onglet PayPal.

---

**[INTRO - face caméra]**

PayPal reste un réflexe d'achat pour une partie de tes clients. L'ajouter à côté de Stripe, c'est élargir tes options de paiement, et donc réduire les abandons. Bonne nouvelle : la logique est la même que pour Stripe.

**[SECTION 1 - Connecter PayPal]**

**[ÉCRAN - screencast : SureCart, Settings, Payment Processors, PayPal]**

Toujours dans SureCart, Settings, Payment Processors. Clique sur le processeur PayPal, puis sur l'onglet PayPal. Ouvre le menu Connect et choisis Live Mode. Tu renseignes les informations de ton compte PayPal, et après connexion, tu es redirigé vers la plateforme SureCart.

PayPal apparaît alors activé, à la fois sur la plateforme et sur ton tableau de bord WordPress. Tes clients peuvent maintenant payer avec PayPal.

**[ÉCRAN - slide "Si tu vois Not Approved"]**

Un cas à connaître : si tu vois un avertissement Not Approved, non approuvé, ça veut dire que PayPal n'a pas encore validé ton compte pour encaisser. Ce n'est pas un bug de SureCart. Tu contactes le support de PayPal pour finaliser l'approbation de ton compte, et c'est réglé.

**[SECTION 2 - Le mode test de PayPal]**

**[ÉCRAN - screencast : Connect, Test Mode]**

Comme pour Stripe, tu peux connecter PayPal en mode test. Même chemin, tu choisis simplement Test Mode dans le menu Connect. Pratique pour vérifier ton tunnel avant d'ouvrir en vrai.

**[SECTION 3 - Les autres processeurs]**

**[ÉCRAN - slide "Selon ton pays"]**

Stripe et PayPal couvrent la grande majorité des besoins. Mais selon ton pays, d'autres processeurs sont disponibles dans SureCart, comme Mollie, Razorpay ou Paystack. La logique de connexion est toujours la même : Settings, Payment Processors, tu choisis le processeur, Connect, et tu suis l'authentification.

Mon conseil : ne multiplie pas les processeurs pour le plaisir. Choisis celui ou ceux qui correspondent à ton pays et à tes clients. Pour la plupart des créateurs francophones, Stripe seul, ou Stripe plus PayPal, suffit largement.

**[OUTRO - face caméra]**

Ton encaissement est en place. Maintenant, on s'occupe de l'habillage : la devise, ta couleur, ton logo. C'est ce qui fait qu'une page de paiement inspire confiance plutôt que de faire fuir. Prochaine leçon.

---

**Points clés** :

- PayPal : SureCart, Settings, Payment Processors, onglet PayPal, Connect, Live Mode, connexion au compte.
- Avertissement Not Approved : compte PayPal pas encore approuvé pour encaisser, contacter le support PayPal.
- Mode test disponible (Test Mode dans Connect).
- Autres processeurs selon le pays : Mollie, Razorpay, Paystack, même logique. Ne pas en empiler inutilement.

**Mots clés SEO** : connecter PayPal SureCart, SureCart PayPal, processeurs de paiement SureCart, Mollie SureCart, PayPal Not Approved

---

### Leçon 1.5 : Réglages de base, devise, branding et logo clair et sombre

**Durée** : ~4 min (~650 mots)
**Objectif pédagogique** : Régler la devise en connaissance de cause (et comprendre pourquoi on ne la change pas à la légère), puis configurer les couleurs et les logos clair et sombre.
**Écran** : Screencast réglages Design & Branding, slide d'avertissement devise.

---

**[INTRO - face caméra]**

On passe à l'habillage de ta boutique. Deux sujets : ta devise, et ton branding, couleurs et logo. Le branding, c'est ce qui rassure ton client au moment de payer. Et la devise, je vais te montrer pourquoi on la règle avec sérieux dès le départ.

**[SECTION 1 - La devise, à choisir bien dès le début]**

**[ÉCRAN - slide "Changer de devise : ce que ça casse"]**

Ta devise détermine la monnaie de toutes tes transactions, tes prix et tes rapports. Tu l'as choisie dans l'assistant de configuration. Tu peux la changer ensuite, mais je veux être honnête avec toi sur ce que ça déclenche.

Quand tu changes de devise, tes prix ne sont pas convertis automatiquement : tu dois tous les ressaisir à la main, et tant que tu ne l'as pas fait, tes produits peuvent devenir non achetables. Tes anciens rapports, dans l'ancienne devise, n'apparaissent plus. Et surtout, tes abonnements actifs créés dans l'ancienne devise peuvent échouer au renouvellement.

La règle est simple. Sur une boutique neuve ou une boutique de test, changer de devise ne pose aucun souci. Sur une boutique déjà en live, avec des commandes ou des abonnements actifs, tu évites. Donc tu prends deux minutes maintenant pour vérifier que ta devise est la bonne, pendant que c'est encore sans risque.

**[SECTION 2 - Où vit le branding]**

**[ÉCRAN - screencast : SureCart, Settings, onglet Design & Branding]**

Le branding se règle dans SureCart, Settings, onglet Design & Branding, design et identité. Ce que tu configures ici se retrouve partout côté client : l'espace client, tes pages de paiement, tes emails de confirmation, et tes factures. Un seul réglage, une cohérence sur toute la chaîne.

**[SECTION 3 - Logo et couleur, clair et sombre]**

**[ÉCRAN - screencast : section Brand Settings, cartes Light Mode et Dark Mode]**

Dans la section Brand Settings, tu vois deux cartes sous Theme : Light Mode, mode clair, et Dark Mode, mode sombre. Pourquoi deux ? Parce que les messageries comme Gmail, Apple Mail ou Outlook gèrent le mode sombre chacune à leur façon. Un logo pensé pour fond clair peut devenir illisible sur fond sombre.

Dans la carte Light Mode, tu règles ta couleur de marque et tu téléverses ton logo pour fond clair. Dans la carte Dark Mode, tu mets ta couleur et un logo adapté au fond sombre. Tu cliques sur Save. SureCart servira automatiquement le bon logo selon la messagerie et le thème de ton client.

Trois bonnes pratiques : prévois un vrai logo pour le mode sombre, assure-toi que ton logo clair a assez de contraste, et ne compte pas seulement sur un fond transparent.

**[ÉCRAN - zoom : option "Powered by SureCart"]**

Dernier détail dans ce même onglet : tu peux retirer la mention Powered by SureCart au bas de tes emails et factures. Tu actives l'option, tu enregistres, et la mention disparaît des nouveaux envois. Les emails déjà partis, eux, ne changent pas.

**[OUTRO - face caméra]**

Ta boutique a maintenant ta tête et ta devise est bien posée. Mais par défaut, SureCart parle anglais. Pour tes clients francophones, on va passer l'interface et les emails en français dans la prochaine leçon.

---

**Points clés** :

- La devise conditionne tout. La changer après coup ne convertit pas les prix, fausse les rapports et peut casser les abonnements actifs. À régler sur boutique neuve ou de test.
- Branding dans Settings, Design & Branding. S'applique à l'espace client, au checkout, aux emails et aux factures.
- Logos et couleurs séparés pour mode clair et mode sombre (rendu email variable selon la messagerie). Save pour appliquer.
- Option pour retirer le Powered by SureCart sur les nouveaux emails et factures.

**Mots clés SEO** : branding SureCart, logo SureCart, changer devise SureCart, SureCart mode sombre email, personnaliser SureCart

---

### Leçon 1.6 : Traduire SureCart en français, interface et emails

**Durée** : ~3 min (~550 mots)
**Objectif pédagogique** : Mettre l'interface client en français avec Loco Translate, et régler la langue des emails et factures.
**Écran** : Screencast Loco Translate, screencast Store Settings, Store Language.

---

**[INTRO - face caméra]**

Par défaut, certains textes de SureCart s'affichent en anglais. Pour une boutique francophone, ça fait amateur et ça crée du doute au paiement. Bonne nouvelle : SureCart est entièrement traduisible. Je te montre la méthode la plus accessible, puis le réglage pour les emails.

**[SECTION 1 - Deux choses à traduire]**

**[ÉCRAN - slide "Côté client / côté admin"]**

Il y a deux familles de textes. Ceux que voient tes clients, sur la page de paiement et dans l'espace client. Et ceux que toi seul vois, dans tes réglages et tes fiches produit. Ce qui compte d'abord pour vendre, c'est le côté client. On se concentre là-dessus.

**[SECTION 2 - Traduire avec Loco Translate]**

**[ÉCRAN - screencast : installer Loco Translate]**

La méthode la plus accessible passe par une extension gratuite : Loco Translate. Tu l'installes comme n'importe quelle extension, depuis Extensions, Ajouter.

**[ÉCRAN - screencast : Loco Translate, SureCart, New Language]**

Ensuite, va dans Loco Translate et choisis SureCart dans la liste. Sous l'onglet Overview, clique sur New Language, nouvelle langue. Sélectionne le français, et règle l'emplacement sur Custom, personnalisé. Ce réglage Custom est important : il garde tes traductions au bon endroit pour qu'elles ne soient pas écrasées à la prochaine mise à jour.

Tu cliques sur Start translating. Loco Translate affiche alors tous les textes traduisibles. Tu cliques sur celui que tu veux changer, tu écris ta traduction dans le champ du bas, et tu enregistres. Pour finir, vide le cache de ton site, sinon tu risques de voir encore l'ancienne version. Tu vérifies sur ta page de paiement que le texte est bien passé en français.

Tu n'as pas besoin de tout traduire d'un coup. Commence par les textes visibles au checkout : les boutons, les libellés de champs, les messages. C'est ça qui rassure ton client.

Il existe une méthode plus avancée avec un logiciel comme Poedit et le fichier de traduction du plugin, mais pour la plupart des cas, Loco Translate suffit largement.

**[SECTION 3 - La langue des emails et des factures]**

**[ÉCRAN - screencast : SureCart, Settings, Store Settings, Store Language]**

L'interface, c'est une chose. Les emails de confirmation et les factures, c'en est une autre. Pour eux, va dans SureCart, Settings, Store Settings, et choisis ta langue dans le réglage Store Language. Tu enregistres.

Détail pratique : ce réglage est synchronisé. Que tu le changes côté WordPress ou côté plateforme SureCart, l'autre se met à jour automatiquement. Tes clients reçoivent alors leurs emails et factures dans la bonne langue.

**[OUTRO - face caméra]**

Ta boutique parle français, côté interface et côté emails. Il reste un dernier réglage technique qui fait la différence sur la vitesse et le rendu : comment SureCart cohabite avec ton thème et ton cache. C'est la prochaine leçon.

---

**Points clés** :

- Deux familles de textes : côté client (prioritaire) et côté admin.
- Loco Translate : installer, choisir SureCart, New Language, français, emplacement Custom, traduire les chaînes, enregistrer, vider le cache.
- Commencer par les textes du checkout. Méthode Poedit / .pot disponible pour les cas avancés.
- Langue des emails et factures : Settings, Store Settings, Store Language. Réglage synchronisé entre WordPress et la plateforme.

**Mots clés SEO** : traduire SureCart en français, SureCart français, Loco Translate SureCart, langue emails SureCart, SureCart traduction checkout

---

### Leçon 1.7 : SureCart et ton thème, dark mode, performance et cache

**Durée** : ~4 min (~700 mots)
**Objectif pédagogique** : Accorder SureCart avec un thème sombre, activer l'option de performance, et configurer le cache pour ne pas casser le checkout.
**Écran** : Screencast Design & Branding (dark mode), Advanced (performance), slide règles de cache.

---

**[INTRO - face caméra]**

Trois réglages techniques pour que ta boutique soit rapide et bien intégrée à ton site. Le dark mode, la performance, et le cache. C'est un peu plus technique, mais je vais à l'essentiel, et le cache en particulier peut t'éviter des bugs de paiement très pénibles.

**[SECTION 1 - Le dark mode du thème]**

**[ÉCRAN - screencast : Settings, Design & Branding, dropdown Dark]**

Si ton site a un fond majoritairement sombre, SureCart peut s'y adapter. Va dans SureCart, Settings, Design & Branding, et dans le menu déroulant du thème, sélectionne Dark, sombre. Clique sur Save.

Une mise en garde importante : n'active le dark mode que si ton site a vraiment un fond sombre. Sur un site à fond clair, le dark mode rend mal et nuit à la lisibilité. Dans le doute, laisse le réglage clair par défaut. Tu peux aussi affiner l'apparence avec du CSS personnalisé si tu es à l'aise, mais ce n'est pas nécessaire pour démarrer.

**[SECTION 2 - L'option de performance]**

**[ÉCRAN - screencast : Settings, Advanced, Performance]**

SureCart propose une option pour accélérer le chargement de tes pages produit, boutique et paiement. Va dans Settings, onglet Advanced, avancé, puis la section Performance. Active l'option Use JavaScript ESM Loader et enregistre.

Après activation, teste tes formulaires de paiement dans une fenêtre de navigation privée. Pourquoi privée ? Parce que le cache de ton navigateur peut te montrer l'ancienne version, et te faire croire à un bug qui n'existe pas. Petit point d'attention : si tu utilises un CDN comme Bunny, tu peux avoir à autoriser les fichiers point j-s dans les en-têtes CORS de ton CDN. Avec Cloudflare, c'est déjà géré. Si tu ne sais pas ce qu'est un CDN, tu n'es probablement pas concerné, et tu peux activer l'option sans souci.

**[SECTION 3 - Le cache, le réglage qui évite les bugs]**

**[ÉCRAN - slide "Pages à exclure du cache"]**

C'est le point le plus important de cette leçon. Un cache mal réglé est la cause numéro un des bugs de boutique : panier qui ne se met pas à jour, paiement qui plante, données client figées. Voici les règles à appliquer dans ton extension de cache.

Premièrement, exclus du cache les pages dynamiques : connexion, inscription, paiement et espace client. Ces pages changent pour chaque visiteur, elles ne doivent jamais être mises en cache. Deuxièmement, exclus les requêtes de l'API REST, pour éviter des données client périmées. Troisièmement, ne diffère pas le chargement des scripts de base de WordPress, ceux qui servent à faire fonctionner les blocs. Quatrièmement, désactive la combinaison des scripts JavaScript : aujourd'hui, ça n'apporte rien et ça peut casser le checkout. Enfin, évite un cache navigateur trop agressif sur les données de boutique.

**[ÉCRAN - slide "Après chaque réglage : tester"]**

Et la règle d'or après chaque changement de cache : tu testes ton tunnel de paiement, en navigation privée. Tu ajoutes un produit, tu vas au paiement, tu vérifies que tout répond. Si quelque chose casse, c'est presque toujours le cache. Tu reviens sur tes exclusions.

**[OUTRO - face caméra]**

Ta boutique est connectée, brandée, traduite, rapide et stable. Il ne reste qu'une chose avant de pouvoir vendre l'esprit tranquille : t'assurer que tout fonctionne de bout en bout. On va faire un vrai paiement de test ensemble dans la dernière leçon du module.

---

**Points clés** :

- Dark mode : Settings, Design & Branding, choisir Dark, Save. Uniquement si le site a un fond sombre.
- Performance : Settings, Advanced, Performance, activer Use JavaScript ESM Loader, Save, tester en navigation privée. CDN Bunny : autoriser les .js dans les en-têtes CORS.
- Cache : exclure les pages connexion, inscription, paiement, espace client ; exclure l'API REST ; ne pas différer les scripts de base ; désactiver la combinaison JS ; limiter le cache navigateur.
- Règle d'or : tester le tunnel en navigation privée après chaque réglage de cache.

**Mots clés SEO** : SureCart cache, SureCart performance, SureCart dark mode, optimiser SureCart, SureCart checkout bug cache

---

### Leçon 1.8 : Le mode test et ton premier paiement de test

**Durée** : ~4 min (~700 mots)
**Objectif pédagogique** : Activer le mode test, réussir un paiement de test de bout en bout, et savoir nettoyer les données de test avant de passer en live.
**Écran** : Screencast produit (Instant Checkout, Test Mode), screencast paiement test, screencast Clear Test Data.

---

**[INTRO - face caméra]**

On arrive au moment de vérité : faire passer une vraie commande de test, sans dépenser un centime. C'est l'exercice qui valide tout ce qu'on a fait depuis le début du module. Si ton paiement test passe, ta base technique est solide. Je te montre comment, puis comment nettoyer derrière toi.

**[SECTION 1 - Le processeur de test intégré]**

**[ÉCRAN - slide "Le test processor de SureCart"]**

Bonne nouvelle d'abord : SureCart a son propre processeur de test, actif par défaut. Tu n'as même pas besoin de carte pour l'utiliser. Au paiement, une option de paiement de test apparaît, et tu n'as aucune information bancaire à saisir. C'est l'idéal pour vérifier ton tunnel.

À garder en tête : ce processeur de test ne sert qu'à ça, vérifier. Il n'encaisse rien et n'a rien à faire sur une boutique ouverte au public.

**[SECTION 2 - Activer le mode test]**

**[ÉCRAN - screencast : produit, dropdown Instant Checkout, Test Mode]**

Le mode test s'active par produit. Va dans SureCart, Products, ouvre un produit. En haut à droite, ouvre le menu Instant Checkout et active l'option Test Mode. Clique sur Save Product. Un badge Test Mode apparaît : tu es en sécurité, aucun vrai paiement ne peut passer.

Tu peux aussi activer le mode test au niveau d'un formulaire de paiement, dans la section Custom Forms, en choisissant l'option Test puis Update. Et si tu es connecté en admin, un raccourci existe directement dans la barre d'administration en haut de ta page de paiement.

**[ÉCRAN - zoom : Advanced, Test Mode Restricted]**

Un réglage utile : dans Settings, Advanced, section Spam Protection & Security, l'option Test Mode Restricted. Quand elle est activée, seuls les administrateurs peuvent finaliser une commande de test. Ça évite que des visiteurs créent des commandes de test parasites.

**[SECTION 3 - Passer ta commande de test]**

**[ÉCRAN - screencast : preview Instant Checkout, remplir, Purchase]**

Maintenant, le test lui-même. Ouvre l'aperçu de ton Instant Checkout, ou rends-toi sur ta page de paiement. Remplis le nom, et l'adresse si elle est demandée. Avec le processeur de test intégré, pas besoin d'informations bancaires. Si tu testes via Stripe en mode test, tu utilises une carte de test fournie par Stripe. Clique sur Purchase, payer.

**[ÉCRAN - slide "Ce que tu dois voir"]**

Ce que tu dois voir : une fenêtre de confirmation Thank you, merci. Un reçu de test part vers l'email utilisé. Et en cliquant sur Continue, tu arrives dans l'espace client, où ta commande de test apparaît dans l'historique. Si tu vois tout ça, bravo : ton tunnel fonctionne de bout en bout. C'est exactement l'exercice de ce module.

Si ça bloque, reprends dans l'ordre : connexion à la plateforme, processeur connecté, et surtout le cache de la leçon précédente. Dans neuf cas sur dix, c'est l'un des trois.

**[SECTION 4 - Nettoyer avant le live]**

**[ÉCRAN - screencast : Settings, Advanced, Clear Test Data]**

Tes tests créent des commandes, des utilisateurs et des transactions, sur ton site et sur la plateforme. Avant de passer en live, on nettoie pour ne pas mélanger le test et le réel. Va dans SureCart, Settings, onglet Advanced, et descends jusqu'à Clear Test Data, effacer les données de test. Tu cliques, tu te connectes à ton compte plateforme si on te le demande, et tu confirmes en tapant le mot CONFIRM.

Attention : cette action est irréversible. Tu vérifies bien que tu n'effaces que des données de test, jamais de vraies commandes. Une fois nettoyé, ton compte est propre, prêt pour le live.

N'oublie pas non plus de repasser tes produits en mode normal en désactivant le Test Mode, sinon tu ne pourras pas encaisser pour de vrai.

**[OUTRO - face caméra]**

Et voilà : tu as une boutique installée, connectée à la plateforme, reliée à Stripe et PayPal, brandée, traduite, optimisée, et tu viens de valider un paiement de bout en bout. Ta base technique est posée. Récupère la checklist d'installation en 10 points que je t'ai préparée pour ce module. Dans le module 2, on passe à la partie qui rapporte : créer tes offres et tes prix. On se retrouve là-bas.

---

**Points clés** :

- Processeur de test intégré, actif par défaut, sans carte. Ne pas l'utiliser sur une boutique publique.
- Activer le mode test par produit (Instant Checkout, Test Mode, Save) ou par formulaire (Custom Forms, Test, Update). Badge Test Mode visible.
- Option Test Mode Restricted (Advanced) : seuls les admins finalisent les commandes de test.
- Paiement test réussi = modal Thank you + reçu + commande dans l'espace client. En cas de blocage : connexion, processeur, cache.
- Nettoyer via Clear Test Data (Advanced, taper CONFIRM, irréversible) et désactiver le Test Mode avant de passer en live.

**Mots clés SEO** : mode test SureCart, paiement test SureCart, tester SureCart, Clear Test Data SureCart, passer en live SureCart

---

## Notes de production (module)

### Captures et écrans à préparer

- Screencast installation plugin (Extensions, Ajouter, recherche SureCart) (1.1)
- Screencast assistant de configuration + zoom bandeau vert Complete Setup (1.1)
- Screencast app.surecart.com, menu API, onglet Secret Token (jeton flouté) (1.2)
- Screencast Settings, Connection (collage du jeton, statut Connected) (1.2)
- Capture wp-config.php avec la ligne define au-dessus de "That's all, stop editing" (1.2)
- Screencast Settings, Payment Processors, onglet Stripe, Connect, Live et Test (1.3)
- Screencast tableau de bord Stripe : Payment methods, Apple Pay, Configure domains (1.3)
- Slide "Apple Pay : 3 conditions" (Safari, vraie carte, pays compatible) (1.3)
- Screencast onglet PayPal, Connect, Live et Test + slide Not Approved (1.4)
- Slide "autres processeurs selon le pays" (Mollie, Razorpay, Paystack) (1.4)
- Slide "changer de devise : ce que ça casse" (1.5)
- Screencast Design & Branding, cartes Light Mode / Dark Mode, option Powered by SureCart (1.5)
- Screencast Loco Translate (SureCart, New Language, français, Custom) (1.6)
- Screencast Store Settings, Store Language (1.6)
- Screencast dark mode (Design & Branding, dropdown Dark) (1.7)
- Screencast Advanced, Performance, ESM Loader (1.7)
- Slide "pages à exclure du cache" + slide "tester en navigation privée" (1.7)
- Screencast produit Instant Checkout, Test Mode (1.8)
- Screencast paiement test (preview, Purchase, modal Thank you) (1.8)
- Screencast Advanced, Clear Test Data (prompt CONFIRM) (1.8)

### Ton et transitions

- Intro/outro de chaque leçon : face caméra, fond neutre schoolsWP.
- Sections : alternance screencast guidé (la majorité de ce module) et slides Kadence aux couleurs de marque.
- Leçon 1.2 (wp-config.php) et 1.7 (cache) : ralentir le débit, c'est le plus technique. Bien insister sur la sauvegarde (1.2) et sur le test en navigation privée (1.7).
- Leçon 1.8 : c'est le climax du module (le paiement test réussi). Soigner le moment "modal Thank you" comme une petite victoire.

### Livrables du module

- Checklist d'installation en 10 points (plugin installé, compte rattaché, jeton API connecté, Stripe connecté, Apple Pay validé, PayPal connecté ou écarté volontairement, devise vérifiée, branding clair et sombre posé, langue interface et emails en français, cache configuré et paiement test réussi).
- Quiz 5 questions (étape Complete Setup, où récupérer le jeton API, méthode Apple Pay domaine, risque du changement de devise, règles de cache).

### Garde-fous voix schoolsWP

- Tutoiement, singulier solo, jamais d'em-dash ni d'en-dash.
- Aucune promesse absolue (pas de "ça marchera à coup sûr", "sans jamais planter").
- Honnêteté sur les limites : Apple Pay dépend du pays et de Safari, le changement de devise a des conséquences, le cache mal réglé casse le checkout. On le dit clairement.
- Prudence sécurité : jeton API traité comme un mot de passe, flouté à l'écran ; sauvegarde de wp-config.php avant édition.

### Cohérence avec le plan et M0

- M0 annonçait "on installe, on connecte, et on encaisse ta première vente" : ce module tient la promesse jusqu'au paiement test (la première vente réelle arrive après la création d'offres au M2 et la page de paiement au M3).
- Le vocabulaire posé en 0.2 (checkout, instant checkout, panier flottant, espace client, processeur de paiement) est réutilisé tel quel ici, sans le redéfinir.
- La connexion par jeton API évoquée en 0.2 ("configuré une fois, on le fera dans le module 1") est honorée en 1.2.
