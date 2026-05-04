# Plan Cluster — Automatisation WordPress

## Pilier

**Titre** : Automatiser son site WordPress en 2025 : le guide complet pour freelances et solopreneurs
**Slug** : automatisation-wordpress-guide-complet
**Angle** : Le seul guide d'automatisation WordPress qui part des événements natifs (formulaires, commandes, statuts) et non des outils — pour que le lecteur choisisse sa stack selon son vrai cas d'usage, pas selon les pages de vente des plateformes.
**H2 principaux** :
- Pourquoi l'automatisation WordPress n'est pas la même chose que l'automatisation SaaS
- Les trois niveaux d'automatisation sur WordPress (natif, plugin dédié, plateforme externe)
- Cartographie des outils : OttoKit, Zapier, Make, n8n — qui fait quoi dans un écosystème WordPress
- Les déclencheurs WordPress les plus utiles à automatiser (formulaires, WooCommerce, LMS, membership)
- Comment choisir ton outil selon ta stack actuelle
- Les erreurs qui font planter une automatisation WordPress (et comment les éviter)
- Par où commencer quand tu pars de zéro

---

## Satellites recommandés

### Satellite 1
**Titre** : Connecter Gravity Forms à OttoKit : le workflow pas à pas que j'utilise sur mes sites clients
**Intent** : informationnelle
**Angle schoolsWP** : Tutoriel terrain documenté avec un workflow réel — de la soumission du formulaire jusqu'à l'entrée dans le CRM, captures à l'appui, sans abstraire les étapes qui coincent en pratique.
**Lien vers pilier** : Renvoie au pilier sur la section "déclencheurs WordPress les plus utiles" avec l'ancre "voir comment configurer Gravity Forms comme trigger OttoKit" ; reçoit un lien entrant depuis le comparatif OttoKit vs Zapier sur la recommandation formulaires.
**H2 suggérés** :
- Ce que OttoKit voit dans une soumission Gravity Forms (et ce que Zapier ne voit pas sans plugin)
- Créer le trigger pas à pas : de l'installation du plugin à la première tâche exécutée
- Exemple réel : formulaire de devis → ActiveCampaign → notification Slack
- Les points de friction fréquents et comment les résoudre avant qu'ils cassent ton workflow

---

### Satellite 2
**Titre** : Automatiser WooCommerce sans toucher au code : ce qu'OttoKit déclenche nativement que Zapier ne voit pas
**Intent** : informationnelle
**Angle schoolsWP** : Comparaison opérationnelle centrée sur les triggers WooCommerce — avec un workflow complet documenté (commande créée → CRM → email transactionnel → ligne Notion) pour montrer la différence concrète entre une intégration native et un passage par Webhook.
**Lien vers pilier** : Renvoie au pilier sur la section "déclencheurs WooCommerce" avec l'ancre "voir le workflow WooCommerce complet" ; reçoit un lien entrant depuis le comparatif sur la ligne "intégration WordPress native" du tableau.
**H2 suggérés** :
- Les événements WooCommerce qu'OttoKit comprend nativement (et la liste que Zapier exige en Webhook)
- Workflow documenté : commande → CRM → Notion → email, étape par étape
- Ce que tu gagnes en fiabilité quand le trigger est natif (latence, données manquantes, erreurs silencieuses)
- Quand Zapier reste utile malgré tout dans un contexte WooCommerce

---

### Satellite 3
**Titre** : Make vs OttoKit vs Zapier : quel outil d'automatisation choisir selon ton profil WordPress en 2025
**Intent** : comparative
**Angle schoolsWP** : Élargissement du comparatif avec Make comme troisième option réelle — repositionne OttoKit vs Zapier comme le choix "simple et WordPress-first" face à un outil technique, et devient le point d'entrée naturel du cluster pour les requêtes larges sur l'automatisation WordPress.
**Lien vers pilier** : Renvoie au pilier comme "guide de référence pour comprendre les niveaux d'automatisation avant de choisir un outil" ; reçoit les liens entrants de tous les satellites du cluster.
**H2 suggérés** :
- Ce que Make apporte que ni OttoKit ni Zapier ne font aussi bien (et pourquoi ça ne convient pas à tout le monde)
- Tableau à trois colonnes : critères terrain, pas marketing
- Quel outil selon ton profil : solopreneur WordPress, freelance multi-stack, agence multi-sites
- La question à te poser avant d'ouvrir un compte sur l'un de ces trois outils

---

### Satellite 4
**Titre** : OttoKit + Zapier ensemble via Webhook : quand et comment combiner les deux sans se compliquer la vie
**Intent** : informationnelle
**Angle schoolsWP** : Traitement de l'architecture combinée enterrée dans le comparatif — un article dédié qui documente un workflow hybride réel (trigger OttoKit → Webhook → Zap → HubSpot scoring) avec le raisonnement derrière le choix de combiner plutôt que de choisir.
**Lien vers pilier** : Renvoie au pilier sur la section "trois niveaux d'automatisation" avec l'ancre "voir comment articuler OttoKit et Zapier dans une architecture hybride" ; reçoit un lien depuis le comparatif OttoKit vs Zapier sur la section "les deux en combinaison".
**H2 suggérés** :
- Pourquoi "choisir entre les deux" est parfois la mauvaise question
- L'architecture Webhook OttoKit → Zapier : comment ça fonctionne techniquement sans être développeur
- Exemple documenté : formulaire WordPress → scoring HubSpot via Zapier, déclenché par OttoKit
- Les trois situations concrètes où cette combinaison fait sens (et les deux où elle ne sert à rien)

---

### Satellite 5
**Titre** : FluentCRM vs ActiveCampaign pour automatiser ses emails depuis WordPress : ce que le choix de ton CRM change à ton outil d'automatisation
**Intent** : comparative
**Angle schoolsWP** : Croise le pilier Automatisation avec le pilier CRM & Email — montre que le choix du CRM conditionne directement le choix de l'outil d'automatisation (FluentCRM natif WordPress réduit le besoin de Zapier, ActiveCampaign l'augmente).
**Lien vers pilier** : Renvoie au pilier sur la section "cartographie des outils" avec l'ancre "comment ton CRM influence le choix de ton outil d'automatisation" ; reçoit un lien entrant depuis le satellite WooCommerce et depuis le comparatif OttoKit vs Zapier.
**H2 suggérés** :
- Ce que FluentCRM automatise nativement dans WordPress (et pourquoi ça change tout à ta stack)
- Quand ActiveCampaign justifie de passer par OttoKit ou Zapier pour rester connecté à WordPress
- Tableau de décision : FluentCRM seul, FluentCRM + OttoKit, ActiveCampaign + Zapier
- Le vrai critère de choix : où vivent tes contacts, pas quel outil a plus de fonctionnalités

---

### Satellite 6
**Titre** : n8n pour WordPress : ce que cet outil open source vaut vraiment pour un freelance qui n'est pas développeur
**Intent** : décisionnelle
**Angle schoolsWP** : Évalue honnêtement n8n depuis le terrain — pas un tutoriel technique, mais une lecture de solopreneur sur ce que n8n apporte réellement versus sa courbe d'apprentissage, pour écarter ou valider cette option face à OttoKit et Zapier.
**Lien vers pilier** : Renvoie au pilier sur la section "cartographie des outils" avec l'ancre "n8n dans un écosystème WordPress : ce qu'il faut savoir avant de s'y engager" ; s'inscrit dans le cluster comme satellite de qualification d'audience avancée.
**H2 suggérés** :
- Ce que n8n peut faire que OttoKit et Zapier ne permettent pas (hébergement propre, logique avancée, coût zéro à l'usage)
- Ce que n8n exige que la plupart des freelances ne veulent pas gérer (serveur, maintenance, debug)
- Pour quel profil WordPress n8n a du sens en 2025
- La question à te poser avant de passer trois jours à configurer un outil que tu abandonneras

---

### Satellite 7
**Titre** : Automatiser son site LearnDash : les workflows qui libèrent du temps sans toucher au code
**Intent** : informationnelle
**Angle schoolsWP** : Cible les créateurs de formation en ligne WordPress — documente les automatisations LMS les plus utiles (inscription → email de bienvenue → accès déclenché → relance si inactif) avec OttoKit comme outil principal, en lien avec le pilier LMS de schoolsWP.
**Lien vers pilier** : Renvoie au pilier sur la section "déclencheurs WordPress les plus utiles" avec l'ancre "automatiser les événements LearnDash" ; croise le pilier LMS et reçoit un lien depuis le comparatif OttoKit vs Zapier sur la mention LearnDash dans les points forts OttoKit.
**H2 suggérés** :
- Les cinq événements LearnDash qu'il vaut la peine d'automatiser en priorité
- Workflow documenté : inscription → accès cours → séquence email → badge de complétion
- OttoKit comme chef d'orchestre de ton LMS : configuration pas à pas
- Ce que tu ne peux pas encore automatiser avec OttoKit sur LearnDash (et comment contourner)

---

## Maillage interne

| Article | Renvoie vers | Ancre suggérée |
|---|---|---|
| OttoKit vs Zapier (comparatif) | Satellite 1 — Gravity Forms + OttoKit | "connecter Gravity Forms à OttoKit" |
| OttoKit vs Zapier (comparatif) | Satellite 2 — WooCommerce + OttoKit | "automatiser ton site WooCommerce avec OttoKit" |
| OttoKit vs Zapier (comparatif) | Satellite 4 — Architecture hybride Webhook | "utiliser les Webhooks dans OttoKit" |
| OttoKit vs Zapier (comparatif) | Pilier — Guide complet automatisation | "guide complet de l'automatisation WordPress sur schoolsWP" |
| Pilier — Guide complet automatisation | Satellite 3 — Make vs OttoKit vs Zapier | "comparer Make, OttoKit et Zapier selon ton profil" |
| Pilier — Guide complet automatisation | Satellite 1 — Gravity Forms + OttoKit | "voir comment configurer Gravity Forms comme trigger OttoKit" |
| Pilier — Guide complet automatisation | Satellite 2 — WooCommerce + OttoKit | "voir le workflow WooCommerce complet" |
| Pilier — Guide complet automatisation | Satellite 4 — Architecture hybride Webhook | "articuler OttoKit et Zapier dans une architecture hybride" |
| Pilier — Guide complet automatisation | Satellite 5 — FluentCRM vs ActiveCampaign | "comment ton CRM influence le choix de ton outil d'automatisation" |
| Pilier — Guide complet automatisation | Satellite 6 — n8n pour WordPress | "n8n dans un écosystème WordPress : ce qu'il faut savoir avant de s'y engager" |
| Satellite 1 — Gravity Forms + OttoKit | OttoKit vs Zapier (comparatif) | "pourquoi OttoKit est recommandé en premier pour WordPress" |
| Satellite 1 — Gravity Forms + OttoKit | Pilier — Guide complet automatisation | "revenir au guide complet de l'automatisation WordPress" |
| Satellite 2 — WooCommerce + OttoKit | OttoKit vs Zapier (comparatif) | "voir la comparaison complète OttoKit vs Zapier" |
| Satellite 2 — WooCommerce + OttoKit | Satellite 5 — FluentCRM vs ActiveCampaign | "comment ton CRM se connecte à ce workflow WooCommerce" |
| Satellite 3 — Make vs OttoKit vs Zapier | OttoKit vs Zapier (comparatif) | "lire le comparatif détaillé OttoKit vs Zapier" |
| Satellite 3 — Make vs OttoKit vs Zapier | Satellite 6 — n8n pour WordPress | "évaluer n8n si tu cherches une alternative open source" |
| Satellite 3 — Make vs OttoKit vs Zapier | Pilier — Guide complet automatisation | "comprendre les niveaux d'automatisation WordPress avant de choisir" |
| Satellite 4 — Architecture hybride Webhook | OttoKit vs Zapier (comparatif) | "relire la section architecture combinée du comparatif" |
| Satellite 4 — Architecture hybride Webhook | Satellite 2 — WooCommerce + OttoKit | "voir un exemple de trigger natif WooCommerce en entrée de ce workflow" |
| Satellite 5 — FluentCRM vs ActiveCampaign | Satellite 2 — WooCommerce + OttoKit | "voir comment ce workflow WooCommerce se connecte à ton CRM" |
| Satellite 5 — FluentCRM vs ActiveCampaign | OttoKit vs Zapier (comparatif) | "choisir l'outil d'automatisation qui correspond à ton CRM" |
| Satellite 6 — n8n pour WordPress | Satellite 3 — Make vs OttoKit vs Zapier | "comparer n8n avec Make, OttoKit et Zapier dans un seul tableau" |
| Satellite 6 — n8n pour WordPress | Pilier — Guide complet automatisation | "revenir au guide complet pour choisir ta stack d'automatisation" |
| Satellite 7 — LearnDash automatisation | OttoKit vs Zapier (comparatif) | "pourquoi OttoKit est recommandé pour les événements LMS" |
| Satellite 7 — LearnDash automatisation | Pilier — Guide complet automatisation | "voir tous les déclencheurs WordPress utiles à automatiser" |

---

## Ordre de production

1. **Satellite 1 — Gravity Forms + OttoKit** — Résout immédiatement le gap critique de l'audit (absence de workflow concret documenté) ; active le premier lien interne balisé `[[LIEN INTERNE]]` dans le comparatif existant ; contenu terrain rapide à produire si le workflow existe déjà sur un site client.

2. **Satellite 2 — WooCommerce + OttoKit** — Résout le deuxième lien interne balisé dans le comparatif ; croise le pilier WooCommerce de schoolsWP et génère des liens entrants naturels depuis cet écosystème