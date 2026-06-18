# 02 - Bonus et séquencement

**Offre** : La Méthode MIRROR - Connecte ton IA à WordPress sans casser de site
**Stack** : FluentCart + WordPress + TutorLMS + FluentCRM
**Prix** : ~~297 €~~ → 67 € · Garantie 7 jours
**Généré le** : 2026-05-15

---

## Les 4 bonus inclus

### Bonus 1 - Pack "Configs MCP prêtes à coller"

5 templates JSON commentés que tu copies, tu remplaces 2 valeurs (URL site + Application Password) et tu lances :

- `.mcp.json` pour Claude Code (config projet)
- `claude_desktop_config.json` pour Claude Desktop (config user global)
- Settings JSON Cursor MCP
- Snippet de config Gemini CLI
- Script setup Antigravity (avec gestion d'erreur)

Plus 1 fichier `.env.example` pour stocker proprement tes 5+ Application Passwords si tu jongles entre sites clients.

**Pourquoi en bonus** : la doc officielle Novamira a la base. Mes templates incluent les commentaires explicatifs FR, les pièges fréquents (escape characters, espaces dans l'AP) et la gestion multi-sites.

### Bonus 2 - Pack "10 prompts Novamira prêts à l'emploi"

10 prompts numérotés avec contexte attendu, dry-run intégré et résultat type :

1. Audit site complet (plugins obsolètes, thème inactif, users sans 2FA, options vides, transients orphelins)
2. Migration Classic Editor → Gutenberg (par lots de 10 posts)
3. Nettoyage transients orphelins (dry-run avant suppression)
4. Création posts en masse depuis CSV (mapping colonnes → champs WP)
5. Désactivation plugins inutilisés (avec sauvegarde liste avant)
6. Snapshot DB avant intervention (export structuré)
7. Comparaison thème actif vs alternatif (composants, options, customizer)
8. Export users vers CSV (filtré par rôle, statut, dernière connexion)
9. Réécriture meta SEO en masse avec Rank Math (par template)
10. Hooks WordPress : trouve où s'accroche un plugin (debug et compréhension)

**Pourquoi en bonus** : ces 10 prompts sont l'essentiel des cas d'usage quotidiens. Sans eux, tu redécouvres la formulation à chaque fois. Avec eux, tu gagnes 30 min par session.

### Bonus 3 - Pack "Prompts builders" (Elementor + Bricks)

10 prompts builders prêts à coller :

**Elementor (5 prompts)** :
- Créer un hero responsive à partir d'une description
- Convertir un bouton v3 en bouton v4 atomic
- Migrer une section v3 vers v4 atomic
- Appliquer un global style sur une page existante
- Fixer un problème responsive (mobile breakdown)

**Bricks (5 prompts)** :
- Créer un template Bricks à partir d'une description
- Réutiliser un composant existant dans 3 pages
- Brancher des dynamic data (CPT + ACF)
- Construire une query loop performante
- Définir une global class et l'appliquer en masse

**Pourquoi en bonus** : Novamira Pro 1.1+ a un vocabulaire commun pour builders. Mes prompts exploitent ce vocabulaire et évitent les pièges (ex: ne pas mélanger v3/v4 dans la même section).

### Bonus 4 - Routine PDF complète

Le pack opérationnel qui transforme la formation en discipline :

- Checklist pré-session 7 points (PDF imprimable A4)
- Template rapport client 1 page (markdown + version PDF brandée)
- Script bash `pre-session-backup.sh` (wp-cli : DB dump + tar files + tag git)
- Template journal de session markdown (à dupliquer pour chaque session)
- Export WP de site démo "demo-bakery" (.wpress 30 Mo, à importer dans LocalWP) pour ton projet final
- Template rapport audit Novamira 1 page (à livrer en fin de mandat client)

**Pourquoi en bonus** : la méthode n'est rien sans la routine. Ce pack est ce qui te fait passer de *"j'ai vu la formation"* à *"je facture des audits Novamira à mes clients"*.

---

## Séquencement de livraison

L'apprenant reçoit immédiatement après achat (FluentCart → FluentCRM trigger) :

| Email | Délai | Contenu |
| :-- | :-- | :-- |
| Email 1 | J0 (instantané) | Confirmation + accès cours TutorLMS (M0 à M3 débloqués) + bonus 1 (Configs MCP) + lien Discord |
| Email 2 | J1 (matin) | Démarrage M0 + M1 → conseil de tournage : *fais M0 ce matin, M1 ce soir* |
| Email 3 | J3 | Déblocage M2 (Installation) + bonus 2 (10 prompts) + lien atelier groupé Discord (si proposé) |
| Email 4 | J5 | Déblocage M3 (Réglages) + bonus 3 (Prompts builders) si tu utilises Elementor/Bricks |
| Email 5 | J8 | Déblocage M4 à M8 d'un coup + bonus 4 (Routine PDF) + invitation projet final |

Cette cadence assure la complétion sans surcharger. Le drip est désactivable depuis le compte si l'apprenant veut tout débloquer d'un coup (M0 le précise).

**Note importante** : le drip est gradué pour que l'apprenant ait toujours quelque chose à faire entre 2 modules (exercice du module en cours + lecture de la fiche du module suivant). C'est conçu pour éviter le décrochage typique J+3.

---

## Modules de la formation

**Durée totale** : 4 h vidéo Premium (M4 à M8) + ~2 h vidéo gratuite (M0 à M3) + ressources écrites + 8 exercices + 1 projet final

### Modules gratuits (teaser sérieux)

- M0 - Pré-requis et positionnement Novamira (4 leçons, 25 min)
- M1 - Maitriser : comprendre Novamira MCP / WordPress / IA (6 leçons, 40 min)
- M2 - Installer : setup serveur + plugin + premier "hello world" (7 leçons, 50 min)
- M3 - Régler : abilities, application password, MCP config (6 leçons, 45 min)

### Modules Premium (4 h)

- M4 - Relier ton client IA : Claude Code, Codex, Cursor, Gemini, Antigravity (7 leçons, 55 min)
- M5 - Workflows fondamentaux : PHP, filesystem, DB, 5 recettes types (8 leçons, 65 min)
- M6 - Outils Pro · Builders : Elementor v3→v4 + Bricks (6 leçons, 55 min)
- M7 - Outils Pro · Champs custom & Memory projet (6 leçons, 50 min)
- M8 - Routine sécurisée + Projet final livrable (7 leçons, 55 min)

---

## Order bump (+27 €)

**Pack 5 prompts avancés "Migrations et imports massifs"**

5 cas particuliers qui tombent une fois sur 10 mais qui te bloquent 2 heures quand ils arrivent :

1. Migration Polylang (FR↔EN↔DE) avec préservation des relations posts
2. Import 1000 produits WooCommerce depuis CSV + images + variants
3. Conversion d'une taxonomie custom vers une nouvelle (avec relations posts)
4. Fusion de 2 sites WP (users + content + media) sans collision d'IDs
5. Déduplication users (emails identiques, comptes orphelins, sessions zombies)

Chaque prompt : contexte attendu + dry-run + script PHP commenté + procédure rollback.

**Pourquoi en order bump et pas en bonus inclus** : c'est une ressource avancée qui ne sert qu'à ceux qui ont déjà mis en place la base. L'inclure dans l'offre principale diluerait la promesse. En bump, c'est explicite : tu ajoutes 27 € pour aller plus loin si tu sais déjà que tu en auras besoin (typiquement, freelance migrations / e-commerçant gérant gros catalogue).

---

## Upsell post-achat (+97 €)

**Audit personnalisé d'un site client + briefing routine Novamira sur mesure**

Tu m'envoies un site sur lequel tu interviens (avec accord client), je te rends :

- Une vidéo Loom de 45 min : audit Novamira complet (lecture seule) + 5 actions prioritaires identifiées
- Ta routine Novamira personnalisée selon ton stack (builder, plugins, hébergeur)
- 1 séance de Q&A texte sous 7 jours (réponses sous 24 h ouvrées)
- Template rapport client adapté à ton activité (freelance / agence)

**Pourquoi en upsell et pas dans la formation** : c'est de l'accompagnement personnalisé sur ton stack réel. Proposé uniquement après l'achat, jamais sur la page publique (rareté = motivation à décider à chaud).

---

## Cohérence avec la promesse

Tous les bonus, l'order bump et l'upsell sont alignés sur la promesse principale : connecter ton IA à WordPress via Novamira et automatiser tes interventions sans casser de site, en 8 jours.

Aucun bonus "remplissage". Chaque ressource a un usage concret dans la routine MIRROR.

---

*schoolsWP · La Méthode MIRROR · Document de travail interne*
