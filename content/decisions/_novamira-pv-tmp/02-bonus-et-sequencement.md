# 02 - Bonus et séquencement

**Offre** : La Méthode MIRROR : connecte ton IA à WordPress avec une routine sécurisée
**Stack** : FluentCart + WordPress + TutorLMS + FluentCRM
**Prix de lancement** : 67 € · Garantie 14 jours
**Généré le** : 2026-05-16 (v4, refonte intégrale après 4 rounds d'audit éditorial)

---

## Les 4 bonus inclus

### Bonus 1 : Pack "Configurations MCP prêtes à coller"

5 modèles JSONC (JSON avec commentaires) que tu copies, tu remplaces 2 valeurs (URL site + mot de passe d'application) et tu lances :

- Fichier .mcp.json pour Claude Code (configuration projet)
- Fichier claude_desktop_config.json pour Claude Desktop (configuration utilisateur globale)
- Settings Cursor MCP
- Snippet de configuration Gemini CLI
- Script d'initialisation Antigravity (avec gestion d'erreur)

Plus 1 fichier .env.example contenant des placeholders : tu copies en .env local non versionné et tu remplaces par tes vrais mots de passe d'application WordPress. Les vrais identifiants ne sont jamais dans le .env.example.

**Pourquoi en bonus** : la documentation officielle Novamira donne la base. Mes modèles incluent les commentaires explicatifs FR, les pièges fréquents (caractères d'échappement, espaces dans le mot de passe d'application) et la gestion multi-sites.

### Bonus 2 : Pack "10 prompts Novamira prêts à l'emploi"

10 prompts numérotés avec contexte attendu, simulation avant action intégrée et résultat type :

1. Audit complet du site : plugins obsolètes, thème inactif, utilisateurs sans 2FA détectable (si le plugin 2FA expose l'information), options vides, transients orphelins
2. Conversion Classic Editor vers Gutenberg, par lots de 10 posts
3. Nettoyage des transients orphelins, avec simulation avant suppression
4. Création de posts en masse depuis CSV, avec mapping des colonnes vers les champs WordPress
5. Analyse des plugins potentiellement inutilisés, puis désactivation contrôlée après validation
6. Sauvegarde de la base de données avant intervention, via WP-CLI ou outil de backup validé
7. Comparaison entre thème actif et alternatif, composants, options et customizer
8. Export des utilisateurs vers CSV, filtré par rôle, statut et dernière connexion
9. Réécriture des meta SEO en masse avec Rank Math, par modèle
10. Hooks WordPress : trouve où s'accroche un plugin, pour debug et compréhension

**Pourquoi en bonus** : ces 10 prompts couvrent l'essentiel des cas d'usage quotidiens. Sans eux, tu redécouvres la formulation à chaque fois. Avec eux, tu gagnes 30 min par session.

### Bonus 3 : Pack "Prompts builders" (Elementor + Bricks)

10 prompts builders prêts à coller :

**Elementor (5 prompts)** :
- Construire un hero responsive à partir d'une description
- Préparer un bouton V3 vers V4 atomic, à tester sur staging
- Tester la transition d'une section V3 vers V4 atomic sur staging
- Appliquer un global style sur une page existante
- Résoudre un problème responsive (rendu mobile cassé)

**Bricks (5 prompts)** :
- Construire un template Bricks à partir d'une description
- Réutiliser un composant existant dans 3 pages
- Brancher des données dynamiques (CPT + ACF)
- Construire une query loop performante
- Définir une global class et l'appliquer en masse

**Pourquoi en bonus** : Novamira Pro 1.1+ a un vocabulaire commun pour ces deux builders. Mes prompts exploitent ce vocabulaire et évitent les pièges (ne pas mélanger V3 et V4 dans la même section, par exemple). Pour Elementor V4 spécifiquement, la formation reste en mode test sur staging tant que V4 n'est pas en stable release officielle (V4 est en Alpha en mai 2026).

### Bonus 4 : Routine PDF complète

Le pack opérationnel qui transforme la formation en discipline :

- Checklist pré-session 7 points (PDF imprimable A4)
- Modèle rapport client 1 page (markdown + version PDF brandée)
- Script de sauvegarde pré-session (fichier .sh utilisant WP-CLI pour exporter la base, archiver les fichiers et créer un tag git)
- Modèle journal de session markdown (à dupliquer pour chaque session)
- Export WordPress de site démo "demo-bakery" (.wpress 30 Mo, à importer dans LocalWP) pour ton projet final
- Modèle rapport audit Novamira 1 page (à livrer en fin de mandat client)

**Pourquoi en bonus** : la méthode n'est rien sans la routine. Ce pack est ce qui te fait passer de *"j'ai vu la formation"* à *"tu peux structurer un audit Novamira facturable pour un client"*.

---

## Séquencement de progression (parcours guidé 8 jours)

Tous les modules sont débloqués à J0. Tu peux tout regarder d'un coup si tu veux. Les emails ci-dessous sont un guide de progression, pas un déblocage technique. Tu accèdes à la formation complète dès le paiement validé.

L'apprenant reçoit après achat (FluentCart vers FluentCRM trigger) :

| Email | Délai | Contenu |
| :-- | :-- | :-- |
| Email 1 | J0 (instantané) | Confirmation + accès cours TutorLMS complet + bonus 1 (Configurations MCP) + lien Discord |
| Email 2 | J1 (matin) | Conseil de progression : commence M0 et M1 aujourd'hui (1h05 cumulés) |
| Email 3 | J3 | Conseil de progression : aborde M2 et M3 (1h35 cumulés) + bonus 2 (10 prompts) |
| Email 4 | J5 | Conseil de progression : enchaîne M4 et M5 (2h00 cumulés) + bonus 3 (Prompts builders) si tu utilises Elementor ou Bricks |
| Email 5 | J8 | Conseil de progression : termine par M6, M7, M8 et le projet final (2h40 cumulés) + bonus 4 (Routine PDF) |

Cette cadence est conçue pour éviter le décrochage typique J+3 sans contraindre. Tu peux accélérer ou ralentir sans aucune limitation côté plateforme.

**Important** : le rythme conseillé suppose que tu travailles environ 1h par jour sur la formation. Si tu peux dégager 2 ou 3 heures consécutives sur un weekend, tu termines la formation en 2 jours intensifs.

---

## Modules de la formation (9 modules, environ 7h20 de vidéo + ressources)

**Durée totale** : environ 7h20 de vidéo, dont 2h40 de modules gratuits et 4h40 de modules Premium, plus environ 10h de pratique guidée, 8 exercices et 1 projet final.

### Modules gratuits (teaser sérieux, visibles avant achat) - 2h40 cumulés

- M0 : Pré-requis et positionnement Novamira (4 leçons, 25 min)
- M1 : Maîtriser : comprendre Novamira MCP / WordPress / IA (6 leçons, 40 min)
- M2 : Installer : configuration serveur + plugin + premier "hello world" (7 leçons, 50 min)
- M3 : Régler : abilities, mots de passe d'application, configuration MCP (6 leçons, 45 min)

### Modules Premium (4h40 cumulés)

- M4 : Relier ton client IA : Claude Code, Codex, Cursor, Gemini, Antigravity (7 leçons, 55 min)
- M5 : Workflows fondamentaux : PHP, système de fichiers, base, 5 recettes types (8 leçons, 65 min)
- M6 : Outils Pro : Elementor V3/V4 + Bricks (6 leçons, 55 min)
- M7 : Outils Pro : champs custom + Memory projet (6 leçons, 50 min)
- M8 : Routine sécurisée + Projet final livrable (7 leçons, 55 min)

---

## Order bump (+27 €)

**Pack 5 prompts avancés "Migrations et imports massifs"**

5 cas particuliers qui tombent une fois sur 10 mais qui te bloquent 2 heures quand ils arrivent :

1. Migration Polylang (FR/EN/DE) avec préservation des relations posts
2. Import massif de produits WooCommerce, jusqu'à 1000 produits si testé, avec images + variants
3. Conversion d'une taxonomie custom vers une nouvelle, avec relations posts
4. Fusion de 2 sites WordPress (utilisateurs + contenu + médias), avec stratégie de prévention des collisions d'IDs
5. Déduplication utilisateurs : emails identiques, comptes orphelins, sessions zombies

Chaque prompt : contexte attendu + simulation avant action + script PHP commenté + procédure de retour arrière.

**Pourquoi en order bump et pas en bonus inclus** : c'est une ressource avancée qui ne sert qu'à ceux qui ont déjà mis en place la base. L'inclure dans l'offre principale diluerait la promesse. En bump, c'est explicite : tu ajoutes 27 € pour aller plus loin si tu sais déjà que tu en auras besoin (typiquement, freelance migrations et e-commerçant gérant un gros catalogue).

---

## Upsell post-achat (+97 €)

**Audit personnalisé d'un site client + briefing routine Novamira sur mesure**

Tu m'envoies un site sur lequel tu interviens (avec accord client), je te rends :

- Une vidéo Loom de 45 min : audit Novamira complet, sans modification exécutée pendant l'audit + 5 actions prioritaires identifiées
- Ta routine Novamira personnalisée selon ton environnement (builder, plugins, hébergeur, équipe)
- 1 session de questions/réponses par écrit sous 7 jours (réponses sous 2 jours ouvrés)
- Modèle de rapport client adapté à ton activité (freelance ou agence)

**Pourquoi en upsell et pas dans la formation** : c'est de l'accompagnement personnalisé sur ton environnement réel. Proposé après achat car il dépend du contexte concret de l'apprenant (site, équipe, plugins utilisés).

---

## Cohérence avec la promesse

Tous les bonus, l'order bump et l'upsell servent la même promesse :

connecter ton agent IA à WordPress via Novamira, en travaillant sur un environnement local ou staging, avec une routine claire de sauvegarde, de validation et de retour arrière.

L'objectif n'est pas de promettre qu'aucune erreur ne peut arriver. L'objectif est de te donner une méthode pour ne plus improviser avec un agent IA connecté à WordPress.

Chaque bonus correspond à une étape concrète de la méthode MIRROR.

---

*schoolsWP · La Méthode MIRROR · Document de travail interne · v3 refonte intégrale 2026-05-16*
