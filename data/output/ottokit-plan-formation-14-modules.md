# Plan de formation — Maitriser OttoKit

**Version** : 1.0
**Date** : 2026-03-30
**Auteur** : schoolsWP (Michael KIHL)
**Plateforme** : TutorLMS Pro
**Format** : Videos HeyGen + voix ElevenLabs
**Langue** : Francais (tutoiement)
**Modele** : Freemium (M1-M3 gratuits, M4-M14 premium)
**Plugin** : OttoKit (ex-SureTriggers) par Brainstorm Force

## Vue d'ensemble

| Module | Titre | Lecons | Duree | Niveau |
|--------|-------|--------|-------|--------|
| M1 | Decouverte : OttoKit et l'automatisation WordPress | 7 | 40 min | Debutant |
| M2 | Installation et premier workflow | 8 | 45 min | Debutant |
| M3 | Triggers : les evenements qui declenchent tes automations | 8 | 45 min | Debutant |
| M4 | Actions : ce que tes automations executent | 8 | 45 min | Intermediaire |
| M5 | Data mapping et formatters : manipuler tes donnees | 8 | 45 min | Intermediaire |
| M6 | Logique conditionnelle : Filter, Condition et Branch | 8 | 50 min | Intermediaire |
| M7 | Workflows multi-etapes et patterns avances | 8 | 50 min | Intermediaire |
| M8 | Integrations WordPress : WooCommerce, LMS, CRM | 9 | 55 min | Intermediaire |
| M9 | Integrations SaaS : Google, Slack, Stripe, WhatsApp | 8 | 50 min | Intermediaire |
| M10 | Webhooks et API : connecter n'importe quel service | 8 | 50 min | Avance |
| M11 | AI Agents et MCP : l'automatisation intelligente | 9 | 55 min | Avance |
| M12 | Monitoring, debugging et optimisation | 8 | 45 min | Avance |
| M13 | Organisation : workspaces, templates et deploiement | 8 | 45 min | Avance |
| M14 | OttoKit vs n8n vs Zapier : choisir le bon outil | 7 | 40 min | Avance |

**Total** : 112 lecons, ~10h00 de contenu

---

## Module 1 — Decouverte : OttoKit et l'automatisation WordPress

**Objectif pedagogique** : Tu comprends ce qu'est OttoKit, pourquoi l'automatisation WordPress est indispensable, et tu sais faire la difference entre OttoKit et les alternatives.
**Prerequis** : Un site WordPress fonctionnel
**Duree estimee** : 40 minutes
**Niveau** : Debutant

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 1.1 | Pourquoi automatiser ton WordPress | 5 min | Video | Le probleme des taches repetitives, le cout du temps perdu | On identifie 3 taches qu'on fait manuellement chaque semaine |
| 1.2 | OttoKit : plateforme cloud + plugin WordPress | 6 min | Video | Architecture cloud vs local, pourquoi ton site reste rapide | On visualise le schema cloud ↔ plugin ↔ apps |
| 1.3 | Le glossaire indispensable : workflow, trigger, action, task | 5 min | Video | Les termes cles et leurs equivalents Zapier/n8n | On associe chaque terme a un exemple concret |
| 1.4 | De SureTriggers a OttoKit : ce qui a change | 5 min | Video | Historique, rebranding, nouvelles fonctionnalites (AI, MCP) | On repere les differences cles dans l'interface |
| 1.5 | Free vs Premium : le verdict honnete | 7 min | Video | Limites du plan gratuit, seuils de rentabilite | On calcule si le plan gratuit suffit pour son usage |
| 1.6 | 1 310 integrations : tour d'horizon des possibilites | 7 min | Video | Categories d'integrations, plugins WP supportes, apps SaaS | On repere les integrations utiles pour son site |
| 1.7 | Quiz M1 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- OttoKit est cloud : le plugin WP ne fait que le pont, tout le traitement est dans le cloud
- Difference avec les solutions 100% WP (Uncanny Automator, Bit Flows) : OttoKit connecte WP ET les apps externes
- Le rebranding SureTriggers → OttoKit (avril 2025) : memes comptes, memes workflows
- 100 000+ utilisateurs, 4.9/5 sur WordPress.org, par l'equipe Astra/Spectra/CartFlows

### Angle schoolsWP
- Demo sur le site schoolsWP reel (pas un site vierge)
- Positionnement dans la stack : OttoKit = couche automatisation, FluentCRM = CRM, TutorLMS = LMS
- Comparaison cout annuel : OttoKit vs Zapier vs Make pour un createur de formation

### Quiz M1 — 5 questions
1. OttoKit est-il un plugin WordPress ou une plateforme cloud ? (Reponse : les deux — plugin + cloud)
2. Quel est le nouveau nom de SureTriggers ? (Reponse : OttoKit)
3. Combien d'integrations OttoKit supporte-t-il ? (Reponse : plus de 1 310)
4. Le traitement des automations se fait-il sur ton serveur WordPress ? (Reponse : non, dans le cloud OttoKit)
5. Quel est l'avantage principal d'une plateforme cloud pour les automations ? (Reponse : ton site reste rapide)

---

## Module 2 — Installation et premier workflow

**Objectif pedagogique** : Tu sais installer le plugin OttoKit, connecter ton site WordPress a la plateforme, connecter une premiere app, et creer ton premier workflow fonctionnel.
**Prerequis** : M1
**Duree estimee** : 45 minutes
**Niveau** : Debutant

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 2.1 | Cree ton compte OttoKit (gratuit) | 5 min | Video | Inscription, choix du plan, tableau de bord | On cree un compte et on explore le dashboard |
| 2.2 | Installe le plugin WordPress OttoKit | 5 min | Video | Installation depuis WP admin, activation | On installe et active le plugin |
| 2.3 | Connecte ton site WordPress a la plateforme | 6 min | Video | Authentification, verification de la connexion | On connecte et on verifie que les plugins WP sont detectes |
| 2.4 | Connecte ta premiere app externe (Google Sheets) | 6 min | Video | Processus OAuth, permissions, verification | On connecte Google Sheets a OttoKit |
| 2.5 | Cree ton premier workflow : formulaire → Google Sheets | 8 min | Demo | Trigger + action, nommage, configuration | On cree un workflow complet de A a Z |
| 2.6 | Teste et publie ton workflow | 5 min | Video | Test d'action, donnees de test, publication | On teste avec des donnees reelles et on publie |
| 2.7 | Troubleshooting : les 5 erreurs les plus courantes a l'installation | 5 min | Video | SSL, timeout, pare-feu, plugin desactive, cron | On diagnostique et corrige les problemes courants |
| 2.8 | Quiz M2 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- L'installation prend moins de 5 minutes si tout va bien
- La connexion WP → cloud necessite HTTPS (certificat SSL obligatoire)
- Les plugins WP compatibles sont auto-detectes a la connexion
- Toujours tester un workflow avant de le publier
- Si la connexion echoue : verifier cron WP, pare-feu, plugin de securite

### Angle schoolsWP
- Installation sur le meme hebergeur que le site de formation (contexte reel)
- Premier workflow adapte au metier : soumission formulaire contact → notification Sheets
- Checklist pre-installation (PHP 7.4+, WP 6.0+, cron actif, SSL)

### Quiz M2 — 5 questions
1. Quel est le prerequis technique obligatoire pour connecter OttoKit ? (Reponse : un certificat SSL / HTTPS)
2. Ou installe-t-on le plugin OttoKit ? (Reponse : depuis le menu Plugins de WordPress)
3. Combien de fois faut-il tester un workflow avant de le publier ? (Reponse : au moins une fois)
4. Si la connexion echoue, quelle est la premiere chose a verifier ? (Reponse : le cron WordPress)
5. Les plugins WP compatibles sont-ils detectes automatiquement ? (Reponse : oui)

---

## Module 3 — Triggers : les evenements qui declenchent tes automations

**Objectif pedagogique** : Tu maitrises les differents types de triggers (instant, schedule, webhook, RSS, button) et tu sais configurer chacun pour des cas reels.
**Prerequis** : M2
**Duree estimee** : 45 minutes
**Niveau** : Debutant

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 3.1 | Triggers instantanes vs planifies : comprendre la difference | 6 min | Video | Temps reel vs polling, impact sur la latence | On compare les deux types sur un meme workflow |
| 3.2 | Configure un trigger WordPress (nouvelle commande WooCommerce) | 6 min | Demo | Selection du plugin, de l'evenement, fetch des donnees | On configure un trigger WooCommerce |
| 3.3 | Configure un trigger SaaS (nouvelle ligne Google Sheets) | 5 min | Demo | Trigger schedule, intervalle de verification | On configure un trigger Google Sheets |
| 3.4 | Schedule App : declenche un workflow a heure fixe | 6 min | Demo | Cron visuel, recurrence, fuseau horaire | On programme un workflow quotidien/hebdomadaire |
| 3.5 | Webhook trigger : recois des donnees de n'importe ou | 7 min | Demo | URL webhook, payload, test avec un outil externe | On cree un webhook et on le teste |
| 3.6 | Trigger Button et RSS Feed : cas d'usage pratiques | 5 min | Video | Declenchement manuel, veille automatisee | On cree un trigger bouton et un trigger RSS |
| 3.7 | Types de donnees trigger : comprendre ce que tu recois | 5 min | Video | Structure des donnees, champs disponibles, fetch | On inspecte les donnees d'un trigger reel |
| 3.8 | Quiz M3 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Un trigger instantane se declenche en temps reel (ex: WooCommerce, Slack)
- Un trigger planifie verifie a intervalles reguliers (ex: Google Sheets toutes les 60 min)
- Le Schedule App remplace un cron : ideal pour backups, rapports, relances
- Les webhooks sont le pont universel : n'importe quel service peut envoyer des donnees a OttoKit
- Toujours faire un "Fetch Data" apres configuration pour verifier les champs recus

### Angle schoolsWP
- Trigger reel : "un eleve termine un cours TutorLMS" → declenche une sequence
- Schedule : "chaque lundi, envoie le rapport des inscriptions de la semaine"
- Webhook : "n8n envoie un signal a OttoKit quand un workflow externe se termine"

### Quiz M3 — 5 questions
1. Quelle est la difference entre un trigger instantane et un trigger planifie ? (Reponse : instantane = temps reel, planifie = verification periodique)
2. A quoi sert le Schedule App ? (Reponse : declencher un workflow a heure fixe ou de facon recurrente)
3. Qu'est-ce qu'un webhook ? (Reponse : une URL qui recoit des donnees d'un service externe)
4. Pourquoi faut-il faire "Fetch Data" apres avoir configure un trigger ? (Reponse : pour verifier les champs de donnees disponibles)
5. Le trigger RSS est-il instantane ou planifie ? (Reponse : planifie)

---

## Module 4 — Actions : ce que tes automations executent

**Objectif pedagogique** : Tu sais configurer des actions simples et complexes, tester avant publication, et gerer les cas d'erreur.
**Prerequis** : M3
**Duree estimee** : 45 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 4.1 | Anatomie d'une action : app, evenement, connexion, configuration | 5 min | Video | Structure d'une action, vocabulaire | On decompose une action existante |
| 4.2 | Configure une action WordPress (creer un article) | 6 min | Demo | Selection app WP, evenement, champs | On cree une action qui publie un brouillon |
| 4.3 | Configure une action SaaS (ajouter une ligne Google Sheets) | 6 min | Demo | Mapping des champs, selection du spreadsheet | On mappe les donnees du trigger vers Sheets |
| 4.4 | Configure une action email (envoyer un Gmail) | 6 min | Demo | Destinataire dynamique, sujet, corps | On envoie un email avec des donnees du trigger |
| 4.5 | Multi-actions : enchaine plusieurs actions dans un workflow | 6 min | Demo | Ajout sequentiel, ordre d'execution, dependances | On cree un workflow avec 3 actions enchaines |
| 4.6 | Test d'action : valide AVANT de publier | 5 min | Video | Bouton test, verifier le resultat, corriger | On teste chaque action individuellement |
| 4.7 | Gerer les erreurs : que se passe-t-il si une action echoue ? | 6 min | Video | Auto-replay, notification, impact sur les actions suivantes | On simule une erreur et on observe le comportement |
| 4.8 | Quiz M4 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Une action = une tache executee dans une app quand le trigger se declenche
- Toujours tester chaque action individuellement avant de publier le workflow complet
- Si une action echoue, les actions suivantes ne s'executent pas (par defaut)
- L'auto-replay retente 6 fois automatiquement avant d'abandonner
- Les donnees dynamiques viennent du trigger ou des actions precedentes

### Angle schoolsWP
- Action reelle : "quand un eleve s'inscrit → creer un contact FluentCRM + envoyer un email de bienvenue + ajouter dans Sheets"
- Strategie de test : utiliser un email de test, pas son vrai email

### Quiz M4 — 5 questions
1. Qu'est-ce qu'une action dans OttoKit ? (Reponse : une tache executee dans une app quand le trigger se declenche)
2. Combien de fois l'auto-replay retente-t-il une action echouee ? (Reponse : 6 fois)
3. Peut-on ajouter plusieurs actions dans un seul workflow ? (Reponse : oui, sans limite)
4. Que faut-il toujours faire avant de publier un workflow ? (Reponse : tester chaque action)
5. Si l'action 2 echoue, l'action 3 s'execute-t-elle ? (Reponse : non, par defaut)

---

## Module 5 — Data mapping et formatters : manipuler tes donnees

**Objectif pedagogique** : Tu sais mapper des donnees entre etapes, utiliser les formatters pour transformer dates/nombres/texte, et gerer les donnees manquantes.
**Prerequis** : M4
**Duree estimee** : 45 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 5.1 | Data mapping : passer des donnees d'une etape a l'autre | 6 min | Video | Donnees dynamiques, tokens, champs disponibles | On mappe un champ du trigger vers une action |
| 5.2 | Donnees statiques vs dynamiques | 5 min | Video | Quand utiliser du texte fixe vs des tokens | On combine texte statique et dynamique dans un email |
| 5.3 | Formatter date et heure : affiche les dates en francais | 6 min | Demo | Format FR, fuseau horaire, conversion | On formate une date "March 30, 2026" en "30/03/2026" |
| 5.4 | Formatter nombre : arrondir, calculer, formater des prix | 6 min | Demo | Arrondi, devise, operations mathematiques | On calcule un prix TTC a partir d'un prix HT |
| 5.5 | Formatter texte : extraire, concatener, transformer | 6 min | Demo | Majuscule, minuscule, extraction, trim, accents | On extrait le prenom d'un champ "Nom complet" |
| 5.6 | Generer un nombre aleatoire | 4 min | Video | Cas d'usage : codes promo, identifiants | On genere un code unique pour un coupon |
| 5.7 | Gerer les donnees manquantes : valeurs par defaut et fallback | 6 min | Video | Champ vide, condition, valeur de remplacement | On cree un fallback pour un champ optionnel |
| 5.8 | Quiz M5 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Le data mapping est le coeur d'OttoKit : c'est ce qui rend les workflows intelligents
- Toujours verifier les champs disponibles apres le Fetch Data du trigger
- Les formatters evitent de manipuler les donnees dans une app externe
- Penser aux fuseaux horaires : OttoKit utilise UTC par defaut

### Angle schoolsWP
- Formater les dates pour les emails en francais
- Calculer automatiquement le prix d'une formation avec remise
- Extraire le prenom d'un contact pour personnaliser les emails

### Quiz M5 — 5 questions
1. Qu'est-ce que le data mapping ? (Reponse : le transfert de donnees d'une etape a une autre)
2. Quelle est la difference entre donnees statiques et dynamiques ? (Reponse : statiques = texte fixe, dynamiques = viennent du trigger/actions)
3. A quoi sert le formatter date ? (Reponse : convertir et formater les dates dans le format souhaite)
4. Quel fuseau horaire OttoKit utilise-t-il par defaut ? (Reponse : UTC)
5. Comment gerer un champ optionnel qui peut etre vide ? (Reponse : definir une valeur par defaut / fallback)

---

## Module 6 — Logique conditionnelle : Filter, Condition et Branch

**Objectif pedagogique** : Tu sais utiliser Filter, Condition et Branch pour creer des workflows intelligents qui reagissent differemment selon les donnees.
**Prerequis** : M5
**Duree estimee** : 50 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 6.1 | Filter vs Condition : comprendre la difference fondamentale | 6 min | Video | Filter = stop/continue, Condition = ajuste les donnees | On compare les deux sur un meme scenario |
| 6.2 | Filter App : bloque un workflow si la condition n'est pas remplie | 6 min | Demo | Operateurs, comparaisons, AND/OR | On filtre les commandes < 50 EUR |
| 6.3 | Condition App : change le comportement sans bloquer | 6 min | Demo | Conditions imbriquees, valeurs conditionnelles | On personnalise un email selon le pays du client |
| 6.4 | Branch App : cree des chemins multiples | 7 min | Demo | 2+ branches, conditions par branche, actions differentes | On segmente VIP / standard / inactif |
| 6.5 | Paths : un chemin parmi plusieurs | 6 min | Demo | Difference avec Branch, cas d'usage | On route un ticket support selon la categorie |
| 6.6 | Delay App : ajoute un delai dans ton workflow | 6 min | Demo | Minutes, heures, jours, cas d'usage | On envoie un email de relance J+3 apres achat |
| 6.7 | Combiner logique et delai : workflow complet de nurturing | 8 min | Demo | Sequence : achat → email J+0 → delay → check review → email J+15 | On cree le workflow complet d'OttoKit "Jane" |
| 6.8 | Quiz M6 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Filter = gardien (laisse passer ou bloque), Condition = aiguillage (adapte sans bloquer)
- Branch = routes multiples (chaque branche a ses propres actions)
- Path = un seul chemin parmi plusieurs (la premiere condition vraie gagne)
- Delay = indispensable pour les sequences email, relances, rappels
- Toujours penser le workflow comme un diagramme AVANT de le construire

### Angle schoolsWP
- Scenario formateur : inscription gratuite → delay 3j → email "as-tu commence le M1 ?" → branch (oui/non) → relance differenciee
- Segmentation eleves : actif / inactif / abandonniste

### Quiz M6 — 5 questions
1. Quelle est la difference entre Filter et Condition ? (Reponse : Filter bloque ou laisse passer, Condition ajuste sans bloquer)
2. A quoi sert le Branch App ? (Reponse : creer plusieurs chemins avec des actions differentes selon les conditions)
3. Que fait le Delay App ? (Reponse : ajoute un temps d'attente entre deux actions)
4. Si un Filter bloque, les actions suivantes s'executent-elles ? (Reponse : non)
5. Faut-il penser son workflow avant de le construire dans OttoKit ? (Reponse : oui, toujours)

---

## Module 7 — Workflows multi-etapes et patterns avances

**Objectif pedagogique** : Tu sais construire des workflows complexes a plus de 5 etapes, utiliser les loops, dupliquer des etapes et appliquer les patterns d'architecture workflow.
**Prerequis** : M6
**Duree estimee** : 50 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 7.1 | Penser son workflow : la methode avant de construire | 6 min | Video | Diagramme, inputs/outputs, etapes, conditions | On dessine un workflow sur papier avant OttoKit |
| 7.2 | Patterns courants : lineaire, conditionnel, parallele | 6 min | Video | Les 3 architectures de base, quand les utiliser | On identifie le pattern adapte a son besoin |
| 7.3 | Dupliquer et reutiliser des etapes | 5 min | Demo | Copy/paste d'etapes, templates personnels | On duplique un bloc d'actions entre workflows |
| 7.4 | Loop : repeter une action pour chaque element d'une liste | 7 min | Demo | Iteration sur un tableau, limites | On envoie un email a chaque participant d'un evenement |
| 7.5 | Email Parser : transforme un email en donnees exploitables | 7 min | Demo | Parsing automatique, extraction de champs | On parse un email de commande en donnees structurees |
| 7.6 | Export et import de workflows | 5 min | Demo | JSON export, import sur un autre compte | On exporte puis reimporte un workflow |
| 7.7 | Partager un workflow par URL | 5 min | Demo | Lien de partage, cas d'usage communaute/agence | On partage un workflow avec un collaborateur |
| 7.8 | Quiz M7 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Un bon workflow se pense AVANT de se construire (diagramme sur papier)
- 3 patterns : lineaire (A→B→C), conditionnel (A→ si X alors B sinon C), parallele (A→ B+C en meme temps)
- Le Loop est indispensable pour traiter des listes (ex: envoyer un email a chaque contact d'un segment)
- L'export/import permet de deployer des workflows entre sites ou entre comptes clients

### Angle schoolsWP
- Pattern formateur : inscription → email bienvenue → delay 3j → verification progression → branche relance/felicitations
- Export d'un workflow "modele schoolsWP" pour le partager avec les apprenants

### Quiz M7 — 5 questions
1. Quels sont les 3 patterns de workflow de base ? (Reponse : lineaire, conditionnel, parallele)
2. A quoi sert le Loop ? (Reponse : repeter une action pour chaque element d'une liste)
3. Comment reutiliser un workflow sur un autre site ? (Reponse : export JSON puis import)
4. L'Email Parser sert a quoi ? (Reponse : transformer un email en donnees structurees exploitables)
5. Faut-il dessiner son workflow avant de le construire ? (Reponse : oui, c'est la premiere etape)

---

## Module 8 — Integrations WordPress : WooCommerce, LMS, CRM

**Objectif pedagogique** : Tu sais connecter et automatiser les plugins WordPress cles de ton ecosysteme : WooCommerce, TutorLMS, FluentCRM, Fluent Forms, Elementor.
**Prerequis** : M7
**Duree estimee** : 55 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 8.1 | Connecter tes plugins WordPress a OttoKit | 5 min | Video | Auto-detection, activation, verification | On verifie les plugins detectes sur son site |
| 8.2 | WooCommerce : commande → notification + Sheets + email | 8 min | Demo | Trigger commande, actions multiples | On cree le workflow complet "Jane" |
| 8.3 | WooCommerce : coupon automatique apres premier achat | 6 min | Demo | Condition premier achat, creation coupon | On automatise la fidelisation |
| 8.4 | TutorLMS : inscription cours → email + tag CRM | 7 min | Demo | Trigger inscription, actions FluentCRM | On connecte le LMS au CRM |
| 8.5 | TutorLMS : relance des eleves inactifs | 6 min | Demo | Schedule + condition progression + email | On cree une relance automatique |
| 8.6 | FluentCRM : tag → sequence email → suivi | 6 min | Demo | Trigger tag, actions email | On declenche une sequence depuis un tag |
| 8.7 | Fluent Forms / SureForms : formulaire → CRM + Sheets | 6 min | Demo | Trigger soumission, multi-actions | On connecte un formulaire a 3 destinations |
| 8.8 | Automatisation inter-sites : site A → site B | 6 min | Demo | Webhook entre 2 sites WordPress | On connecte 2 sites WP via OttoKit |
| 8.9 | Quiz M8 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- OttoKit detecte automatiquement les plugins WordPress installes sur le site connecte
- WooCommerce est l'integration la plus utilisee : commandes, coupons, stock, clients
- La combinaison TutorLMS + FluentCRM + OttoKit est la stack formation complete
- L'automatisation inter-sites est un avantage unique d'OttoKit (impossible avec Zapier)

### Angle schoolsWP
- Stack reelle : TutorLMS (LMS) + FluentCRM (CRM) + OttoKit (automatisation)
- Workflow complet formateur : inscription gratuite → tag "lead" → sequence nurturing → achat premium → tag "client" → acces cours

### Quiz M8 — 5 questions
1. Les plugins WP sont-ils detectes automatiquement par OttoKit ? (Reponse : oui)
2. Peut-on connecter 2 sites WordPress entre eux avec OttoKit ? (Reponse : oui, via webhooks)
3. Quel trigger utilise-t-on pour "un eleve termine un cours TutorLMS" ? (Reponse : le trigger TutorLMS "Course Completed")
4. Peut-on creer un coupon WooCommerce automatiquement ? (Reponse : oui, via une action WooCommerce)
5. Quelle est la stack formation complete recommandee ? (Reponse : TutorLMS + FluentCRM + OttoKit)

---

## Module 9 — Integrations SaaS : Google, Slack, Stripe, WhatsApp

**Objectif pedagogique** : Tu sais connecter et automatiser les apps SaaS les plus courantes avec tes workflows WordPress.
**Prerequis** : M8
**Duree estimee** : 50 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 9.1 | Google Sheets : dashboard automatise de tes ventes | 7 min | Demo | Trigger + actions Sheets, formatage donnees | On cree un tableau de bord auto-alimente |
| 9.2 | Gmail / SMTP : emails transactionnels automatiques | 6 min | Demo | Templates dynamiques, personnalisation | On envoie un email personnalise post-achat |
| 9.3 | Slack : notifications equipe en temps reel | 5 min | Demo | Channel, formatage message, mentions | On notifie l'equipe pour chaque vente > 100 EUR |
| 9.4 | Stripe : paiement → actions automatiques | 7 min | Demo | Trigger checkout, actions post-paiement | On gere le cycle de vie abonnement |
| 9.5 | WhatsApp Cloud API : messages automatiques | 7 min | Demo | Configuration API, templates, envoi | On envoie une confirmation commande WhatsApp |
| 9.6 | Google Calendar : evenements automatiques | 5 min | Demo | Creation evenement, invitation | On cree un RDV automatique apres inscription |
| 9.7 | Trello / ClickUp / Asana : gestion de projet automatisee | 6 min | Demo | Creation tache, assignation, mise a jour | On cree une tache pour chaque nouveau client |
| 9.8 | Quiz M9 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- La connexion OAuth se fait une seule fois par app — ensuite c'est automatique
- Google Sheets est l'outil de reporting le plus accessible : zero cout, zero courbe d'apprentissage
- WhatsApp Cloud API necessite un compte Meta Business verifie
- Slack est parfait pour les notifications internes equipe

### Angle schoolsWP
- Dashboard Google Sheets : suivi des inscriptions formations en temps reel
- WhatsApp : message personnalise quand un eleve termine un module
- Trello : tache automatique "produire la video du module X" quand un script est valide

### Quiz M9 — 5 questions
1. Combien de fois faut-il configurer la connexion OAuth pour Google Sheets ? (Reponse : une seule fois)
2. WhatsApp Cloud API necessite quel type de compte ? (Reponse : Meta Business verifie)
3. Peut-on formater les messages Slack envoyes par OttoKit ? (Reponse : oui)
4. Google Sheets est-il gratuit ? (Reponse : oui)
5. Peut-on creer automatiquement une tache Trello depuis OttoKit ? (Reponse : oui)

---

## Module 10 — Webhooks et API : connecter n'importe quel service

**Objectif pedagogique** : Tu sais utiliser les webhooks entrants/sortants et l'API App pour connecter OttoKit a n'importe quel service, meme non supporte nativement.
**Prerequis** : M9
**Duree estimee** : 50 minutes
**Niveau** : Avance

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 10.1 | Webhooks : le pont universel entre les outils | 6 min | Video | Concept, URL, payload, headers | On comprend le mecanisme webhook |
| 10.2 | Webhook entrant : OttoKit recoit des donnees | 7 min | Demo | Creation webhook, test payload, mapping | On recoit des donnees depuis Postman |
| 10.3 | API App : OttoKit envoie des requetes HTTP | 7 min | Demo | GET, POST, headers, authentification | On appelle une API externe (ex: OpenAI) |
| 10.4 | Connecter OttoKit a n8n via webhook | 6 min | Demo | Workflow n8n → webhook OttoKit → actions WP | On cree un pont n8n ↔ OttoKit |
| 10.5 | Parser la reponse d'une API | 6 min | Demo | JSON response, extraction de champs | On extrait un resultat d'API pour l'utiliser dans le workflow |
| 10.6 | Webhook sortant : OttoKit notifie un service externe | 6 min | Demo | Custom API, headers, body | On envoie des donnees vers un endpoint custom |
| 10.7 | Securiser ses webhooks : secrets, validation, HTTPS | 6 min | Video | Bonnes pratiques securite webhook | On ajoute un secret a un webhook |
| 10.8 | Quiz M10 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Les webhooks sont le moyen de connecter des outils qui ne sont pas dans les 1 310 integrations natives
- L'API App permet d'appeler n'importe quelle API REST (OpenAI, Google, services custom)
- Toujours securiser ses webhooks (secret, HTTPS, validation du payload)
- Le pont n8n ↔ OttoKit est puissant : n8n pour les traitements complexes, OttoKit pour les actions WP

### Angle schoolsWP
- Pont n8n → OttoKit : n8n genere un article avec l'IA → webhook → OttoKit publie sur WordPress
- API OpenAI : generer un resume de cours automatiquement

### Quiz M10 — 5 questions
1. A quoi sert un webhook entrant ? (Reponse : recevoir des donnees d'un service externe)
2. Quelle methode HTTP utilise-t-on pour envoyer des donnees ? (Reponse : POST)
3. Faut-il securiser ses webhooks ? (Reponse : oui, avec un secret et HTTPS)
4. L'API App permet-elle d'appeler n'importe quelle API ? (Reponse : oui, toute API REST)
5. Peut-on connecter OttoKit a n8n ? (Reponse : oui, via webhooks)

---

## Module 11 — AI Agents et MCP : l'automatisation intelligente

**Objectif pedagogique** : Tu sais creer des AI Agents dans OttoKit, configurer le MCP (Model Context Protocol), et connecter Claude ou ChatGPT a tes workflows.
**Prerequis** : M10
**Duree estimee** : 55 minutes
**Niveau** : Avance

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 11.1 | AI Agents : qu'est-ce que c'est et pourquoi c'est different | 6 min | Video | Agent vs workflow classique, capacite de decision | On compare un workflow manuel vs un agent |
| 11.2 | Cree ton premier AI Agent dans OttoKit | 8 min | Demo | Interface agent, objectif, outils, configuration | On cree un agent basique |
| 11.3 | Donne des outils a ton agent : actions et integrations | 7 min | Demo | Associer des actions a un agent, permissions | On connecte Gmail + Sheets a l'agent |
| 11.4 | Human-in-the-Loop : garde le controle sur ton agent | 7 min | Demo | Approbation avant action, notification, review | On configure une approbation humaine |
| 11.5 | MCP (Model Context Protocol) : connecte Claude et ChatGPT | 7 min | Video | Qu'est-ce que MCP, pourquoi c'est important | On comprend l'architecture MCP |
| 11.6 | Configure un MCP server OttoKit | 7 min | Demo | Developer Mode, creation du serveur, connexion | On active le MCP et on connecte un LLM |
| 11.7 | Cas d'usage AI : agent support, agent contenu, agent SEO | 7 min | Video | 3 scenarios reels avec AI Agents | On choisit le cas le plus adapte a son business |
| 11.8 | Agent vs workflow : quand utiliser lequel | 6 min | Video | Arbre de decision, limites des agents, cout en tasks | On decide quand utiliser un agent vs un workflow |
| 11.9 | Quiz M11 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Un AI Agent prend des decisions, un workflow execute des etapes predefinies
- Human-in-the-Loop = filet de securite : l'agent propose, tu approuves
- MCP permet a Claude, ChatGPT ou Cursor d'appeler directement OttoKit
- Les agents consomment plus de tasks que les workflows classiques
- Ne pas utiliser un agent quand un simple workflow conditionnel suffit

### Angle schoolsWP
- Agent "support formateur" : repond aux questions FAQ des eleves automatiquement
- MCP + Claude Code : publier sur WordPress depuis Claude sans quitter le terminal
- Arbre de decision : workflow si le processus est previsible, agent si les inputs varient

### Quiz M11 — 5 questions
1. Quelle est la difference entre un AI Agent et un workflow ? (Reponse : l'agent decide, le workflow execute des etapes fixes)
2. A quoi sert le Human-in-the-Loop ? (Reponse : approuver les actions d'un agent avant execution)
3. Que signifie MCP ? (Reponse : Model Context Protocol)
4. Les AI Agents consomment-ils plus de tasks ? (Reponse : oui)
5. Quand utiliser un workflow plutot qu'un agent ? (Reponse : quand le processus est previsible et les etapes fixes)

---

## Module 12 — Monitoring, debugging et optimisation

**Objectif pedagogique** : Tu sais lire les logs, identifier les erreurs, corriger les workflows defaillants, et optimiser la consommation de tasks.
**Prerequis** : M11
**Duree estimee** : 45 minutes
**Niveau** : Avance

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 12.1 | Workflow History : lire et comprendre les logs | 6 min | Demo | Interface history, statuts, details des runs | On analyse les logs d'un workflow reel |
| 12.2 | Identifier une erreur : les 5 causes les plus frequentes | 6 min | Video | Connexion expiree, champ manquant, API limit, format invalide, permission | On diagnostique chaque type d'erreur |
| 12.3 | Auto-replay et replay manuel : corriger et relancer | 6 min | Demo | Auto-replay (6 tentatives), replay avec modification donnees | On corrige un email invalide et on relance |
| 12.4 | Notifications : sois alerte avant que ca casse | 5 min | Demo | Configuration alertes email, WhatsApp, push | On configure les notifications d'echec |
| 12.5 | Optimiser sa consommation de tasks | 6 min | Video | Qu'est-ce qui compte comme task, strategies d'economie | On calcule et optimise son usage |
| 12.6 | Tester en staging : ne jamais casser la production | 5 min | Video | Environnement de test, donnees de test, publication progressive | On teste un workflow en staging avant production |
| 12.7 | Les 10 bonnes pratiques workflow | 6 min | Video | Nommage, documentation, versionning, simplicite | On applique les bonnes pratiques a un workflow existant |
| 12.8 | Quiz M12 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Lire les logs est la competence #1 pour debugger
- Les 5 erreurs les plus frequentes couvrent 90% des problemes
- Optimiser ses tasks : eviter les triggers trop frequents, filtrer tot dans le workflow
- Nommer et documenter ses workflows pour s'y retrouver dans 6 mois

### Angle schoolsWP
- Monitoring reel : surveiller le workflow inscription → email → CRM sur le site schoolsWP
- Economiser ses tasks : filtrer les commandes test WooCommerce avant d'executer les actions

### Quiz M12 — 5 questions
1. Ou trouve-t-on les logs d'execution des workflows ? (Reponse : dans Workflow History)
2. Combien de fois l'auto-replay retente-t-il ? (Reponse : 6 fois)
3. Peut-on modifier les donnees avant de relancer manuellement ? (Reponse : oui)
4. Qu'est-ce qui compte comme une "task" dans OttoKit ? (Reponse : chaque action executee dans un workflow)
5. Quelle est la bonne pratique #1 pour ses workflows ? (Reponse : les nommer clairement)

---

## Module 13 — Organisation : workspaces, templates et deploiement

**Objectif pedagogique** : Tu sais organiser tes workflows avec des dossiers, gerer plusieurs clients avec les workspaces, et deployer des templates.
**Prerequis** : M12
**Duree estimee** : 45 minutes
**Niveau** : Avance

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 13.1 | Dossiers : organise tes workflows par projet/client | 5 min | Demo | Creation, nommage, hierarchie | On organise 10+ workflows en dossiers |
| 13.2 | Convention de nommage : retrouve n'importe quel workflow | 5 min | Video | Prefixes, categories, dates | On renomme ses workflows avec la convention |
| 13.3 | Organisations : gere plusieurs equipes ou entreprises | 6 min | Demo | Creation org, switch, permissions | On cree une organisation et on switch |
| 13.4 | Workspaces : isole les workflows par client | 6 min | Demo | Creation workspace, connexions par workspace | On cree un workspace pour un client fictif |
| 13.5 | Templates de workflow : cree tes propres modeles | 6 min | Demo | Export, documentation, partage | On cree un template "onboarding client" |
| 13.6 | Deployer un workflow chez un client | 6 min | Demo | Export → import → configuration → test | On deploie un template sur un autre compte |
| 13.7 | Cacher OttoKit dans le WP admin du client | 5 min | Demo | Option hide, acces restreint | On masque OttoKit pour le client final |
| 13.8 | Quiz M13 — Valide tes acquis | 5 min | Quiz | — | — |

### Points cles a couvrir
- Les dossiers sont essentiels des qu'on depasse 10 workflows
- Les organisations separent completement les comptes (pas juste les dossiers)
- Les workspaces isolent les connexions et workflows par projet/client
- On peut cacher OttoKit dans le WP admin du client pour eviter les modifications accidentelles

### Angle schoolsWP
- Organisation freelance : un workspace par client, un dossier par type de workflow
- Template "stack schoolsWP" : TutorLMS + FluentCRM + OttoKit pre-configure

### Quiz M13 — 5 questions
1. A quoi servent les dossiers dans OttoKit ? (Reponse : organiser ses workflows par projet/client)
2. Quelle est la difference entre Organisation et Workspace ? (Reponse : Organisation = equipe/entreprise, Workspace = projet/client)
3. Peut-on cacher OttoKit dans le WP admin ? (Reponse : oui)
4. Comment deployer un workflow chez un client ? (Reponse : export JSON → import → configuration → test)
5. A partir de combien de workflows les dossiers deviennent-ils essentiels ? (Reponse : ~10)

---

## Module 14 — OttoKit vs n8n vs Zapier : choisir le bon outil

**Objectif pedagogique** : Tu sais choisir entre OttoKit, n8n, Zapier et Make selon ton besoin reel, et tu connais les forces et limites de chacun.
**Prerequis** : M13
**Duree estimee** : 40 minutes
**Niveau** : Avance

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|------------------|---------------|
| 14.1 | Le paysage des outils d'automatisation en 2026 | 6 min | Video | Zapier, Make, n8n, OttoKit, Uncanny Automator, Bit Flows | On cartographie les outils disponibles |
| 14.2 | OttoKit vs Zapier : cout, integrations, WordPress | 6 min | Video | Comparatif factuel, cas d'usage, pricing | On compare sur 5 criteres objectifs |
| 14.3 | OttoKit vs n8n : cloud vs self-hosted, simple vs puissant | 6 min | Video | Architecture, complexite, cas d'usage | On decide lequel utiliser selon le scenario |
| 14.4 | OttoKit vs Make : interface, pricing, performance | 5 min | Video | Comparatif visuel, avantages/inconvenients | On compare l'experience utilisateur |
| 14.5 | Arbre de decision : quel outil pour quel besoin | 7 min | Video | Matrice de decision (cout, complexite, WP natif, AI, self-hosted) | On choisit l'outil adapte a 3 scenarios types |
| 14.6 | Combiner OttoKit + n8n : le meilleur des deux mondes | 6 min | Video | OttoKit pour WP, n8n pour le reste, webhook pont | On dessine l'architecture hybride |
| 14.7 | Quiz final M14 — 10 questions | 5 min | Quiz | — | — |

### Points cles a couvrir
- OttoKit = natif WordPress, simple, no-code, AI Agents, MCP, cloud
- n8n = self-hosted, puissant, code possible, 400+ nodes, gratuit
- Zapier = cloud, universel, cher, pas natif WordPress
- Make = cloud, visuel, prix intermediaire, bonne API
- Le choix depend du contexte : budget, competences, besoin WP natif, volume

### Angle schoolsWP
- schoolsWP utilise les deux : n8n pour les pipelines de contenu, OttoKit pour les automations WP
- Arbre de decision adapte au createur de formation en ligne
- Calcul ROI : combien coute Zapier vs OttoKit pour 10 000 tasks/mois

### Quiz M14 — 10 questions (quiz final)
1. Quel outil est natif WordPress ? (Reponse : OttoKit)
2. Quel outil est self-hosted et gratuit ? (Reponse : n8n)
3. Quel outil est le plus cher pour un gros volume ? (Reponse : Zapier)
4. Peut-on combiner OttoKit et n8n ? (Reponse : oui, via webhooks)
5. OttoKit supporte-t-il les AI Agents ? (Reponse : oui)
6. n8n a-t-il une integration native WordPress ? (Reponse : oui, mais moins poussee qu'OttoKit)
7. Quel critere est le plus important pour choisir un outil ? (Reponse : le besoin reel, pas les features)
8. Make est-il self-hosted ? (Reponse : non, c'est du cloud)
9. Quel outil recommandes-tu pour un formateur en ligne avec WordPress ? (Reponse : OttoKit)
10. Quelle est la strategie hybride recommandee ? (Reponse : OttoKit pour WP + n8n pour le reste)
