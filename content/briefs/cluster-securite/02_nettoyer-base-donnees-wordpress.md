---
slug: nettoyer-base-de-donnees-wordpress
keyword_principal: nettoyer base de données WordPress
keywords_secondaires:
  - optimiser wordpress
  - wp optimize
  - wps cleaner
  - advanced database cleaner
  - revisions wordpress supprimer
intent: informationnelle
pillar: SEO / Performance / Sécurité WordPress
role_cluster: Satellite #2 du cluster sécurité WordPress
pilier_cible: avis Samaritain Security (defensive brand)
date_brief: 2026-05-26
auteur: Michaël KIHL
statut: prêt à produire
---

# Brief satellite #2 — Nettoyer sa base de données WordPress

## 1. Contexte SERP (DataForSEO 2026-05-26)

### Volumes mesurés

| Keyword             | Volume/mois | Difficulty | Competition | CPC    | Intent                   |
| ------------------- | ----------- | ---------- | ----------- | ------ | ------------------------ |
| wp optimize         | 210         | KD 18      | LOW (0.07)  | 6,55 € | informational            |
| optimiser wordpress | 170         | non mesuré | LOW (0.03)  | 2,49 € | informational            |
| nettoyer wordpress  | 10          | KD 46      | LOW (0.29)  | —      | commercial/transactional |

**Lecture** : pas de volume direct sur la requête exacte « nettoyer base de données wordpress », mais signal fort sur les keywords proches (`wp optimize` 210, `optimiser wordpress` 170). Le sujet vit principalement via les SERP « nettoyage / optimisation » avec un intent informational pur. Cibler la requête longue précise + viser le ranking via le pattern tutoriel.

### Top 10 SERP (Google.fr, 2026-05-26)

| Pos      | Domaine                                  | Angle                                          |
| -------- | ---------------------------------------- | ---------------------------------------------- |
| 1        | tutoriels.lws.fr                         | WP DB Cleaner pas-à-pas                        |
| 2        | wp-umbrella.com                          | Meilleures pratiques (étapes 1-N)              |
| 3        | blog.crea-troyes.fr                      | WP-Optimize (CyberSécurité)                    |
| 4 (vid)  | YouTube                                  | 4 tutos vidéo                                  |
| 5        | reddit.com (r/Wordpress)                 | Discussion communautaire                       |
| 6        | metaforweb.com                           | Outils > Santé du site                         |
| 7        | wppourlesnuls.com                        | WP-Optimize tutoriel                           |
| 8        | niverel.eu                               | Suppression tables phpMyAdmin                  |
| 9        | moncoachwp.fr                            | Tables WP + WooCommerce                        |
| 10 (PAA) | hostinger, free-work, wpformation, ionos | Backup, types BDD, WPS Cleaner, changement URL |

**Pattern dominant** :

- H1 type « Comment nettoyer sa base de données WordPress » ou « Le guide ultime »
- Toujours commencer par **sauvegarder** (étape #1 obligatoire)
- 2 méthodes proposées : plugin (facile) vs phpMyAdmin/SQL (avancé)
- Plugins cités : WP-Optimize, WPS Cleaner, Advanced Database Cleaner, WP DB Cleaner
- Tables ciblées : révisions, brouillons, commentaires spam, options transients, post meta orphelins

### People Also Ask

- Comment sauvegarder le contenu d'un site web ?
- Quels sont les 4 types de bases de données ?
- Qu'est-ce que WPS Cleaner ?
- Comment changer l'URL de la base de données WordPress ?

## 2. Persona cible

- **Propriétaire WP de 6 mois - 3 ans** dont le site ralentit progressivement (admin lent, dashboard lourd).
- **Freelance** qui récupère un site client en audit et constate une BDD obèse (transients orphelins, révisions à 100+ par post).
- **Formateur LMS** dont la base TutorLMS gonfle (quiz attempts, course meta) sans nettoyage planifié.

Pain point commun : peur de **casser le site** en nettoyant. Cherchent un protocole **sécurisé** + un plugin de confiance.

## 3. Angle différenciant schoolsWP

Les 10 résultats SERP listent les mêmes étapes en mode tutoriel générique. Notre angle :

1. **Sauvegarde obligatoire d'abord** avec WPVivid (formation schoolsWP déjà existante → lien interne fort).
2. **Triage par criticité** : tables système intouchables vs tables encombrantes vs tables orphelines de plugins désinstallés.
3. **Méthode plugin (90 % des cas) vs phpMyAdmin (10 % avancé)** — pas mélanger les deux.
4. **Section sécurité** : une BDD lourde est aussi une surface d'attaque (plus de lignes = plus de payloads injectables). Couplage avec Samaritain Security.
5. **Pattern d'automatisation** : nettoyage planifié vs ponctuel (cron WP-Optimize).
6. **Cas TutorLMS / WooCommerce** : tables spécifiques à gérer (wp*tutor*_, wp*woocommerce*_).

## 4. Structure H2/H3 proposée

### H1

Nettoyer sa base de données WordPress : guide complet 2026

### Réponse rapide (≤ 60 mots)

Une base WordPress nettoyée tous les 1-3 mois libère 30-60 % d'espace, accélère le dashboard et réduit ta surface d'attaque. **Sauvegarde avant tout** (WPVivid), puis utilise WP-Optimize pour 90 % des cas, ou phpMyAdmin uniquement si tu maîtrises le SQL. Ne touche jamais aux tables système (wp_users, wp_options critiques).

### H2 — Pourquoi nettoyer ta base de données WordPress

- Performances admin (dashboard, backend)
- Taille des sauvegardes
- Surface d'attaque réduite (lien Samaritain Security)
- Coût stockage hébergeur

### H2 — Étape 1 obligatoire : sauvegarder avant de toucher quoi que ce soit

- Pourquoi (cas réel : suppression accidentelle d'une table critique)
- Outil recommandé : WPVivid (formation schoolsWP)
- Protocole : export complet (fichiers + BDD) + téléchargement local

### H2 — Comprendre ce qu'il y a dans ta base WordPress

- Tables système (wp_users, wp_options, wp_posts, wp_postmeta)
- Tables annexes (wp_term_relationships, wp_comments)
- Tables plugins (wp*tutor*_, wp*woocommerce*_, wp*yoast*\*)
- Tables orphelines de plugins désinstallés (le vrai gisement)

### H2 — Méthode 1 : nettoyer ta base WordPress avec WP-Optimize (recommandée)

- Installation et configuration
- Tableau de bord WP-Optimize
- Sélection des nettoyages (révisions, brouillons, transients, spam)
- Aperçu avant exécution
- Programmation hebdomadaire

### H2 — Méthode 2 : nettoyer ta base WordPress via phpMyAdmin (avancé)

- Accès phpMyAdmin (cPanel / Plesk / WP Manager)
- Requêtes SQL prêtes à l'emploi (révisions, transients, spam)
- Optimisation des tables (OPTIMIZE TABLE)
- Risques + checkpoint sauvegarde
- > Bloc encadré : "Si tu n'es pas sûr, retourne à la méthode 1"

### H2 — Tables à NE JAMAIS toucher

- wp_users, wp_usermeta (utilisateurs)
- wp_options (avec exceptions ciblées sur transients périmés)
- wp_posts (sauf révisions explicites)

### H2 — Cas spécifique TutorLMS et WooCommerce

- Tables wp*tutor*\* (résultats quiz, progression cours)
- Tables wp*woocommerce*\* (commandes, sessions)
- Quand archiver vs supprimer

### H2 — Lien sécurité : pourquoi une base nettoyée renforce ta protection WordPress

- Moins de payloads stockés = moins de surface d'attaque
- Couplage avec Samaritain Security (plugin de durcissement, lien vers l'avis)
- Maintenance régulière = bouclier proactif

### H2 — Automatiser le nettoyage de ta base de données

- WP-Optimize Premium : planification
- WP-CLI : `wp db optimize` (avancé, hébergeur compatible)
- Routine hebdomadaire ou mensuelle (selon volumétrie)

### H2 — Comment schoolsWP peut t'aider

- Newsletter (lead magnet)
- Cluster sécurité : Samaritain Security + hébergeur sécurisé + 2FA
- Formation WPVivid (sauvegarde)

### H2 — FAQ

- À quelle fréquence nettoyer sa base WordPress ?
- Le nettoyage peut-il casser mon site ?
- WP-Optimize ou Advanced Database Cleaner ?
- Faut-il désactiver les révisions WordPress complètement ?
- Comment savoir si ma base de données est trop lourde ?

## 5. Maillage interne

### Articles à lier (déjà publiés)

- [Avis Samaritain Security](https://schoolswp.com/samaritain-security-avis/) — article pilier
- [Formation WPVivid](content/formations/wpvivid/wpvivid-base-connaissances.md) — sauvegarde obligatoire
- WP-Optimize avis (si existant — sinon angle de futur article)

### Articles à lier (cluster)

- Satellite #1 : Hébergeur WordPress sécurisé
- Satellite #3 : Double authentification WordPress

### Ancres internes recommandées

- « sauvegarde obligatoire » → WPVivid formation
- « plugin de durcissement » → Samaritain Security
- « stack sécurité schoolsWP » → cluster index

## 6. Lead magnet & conversion

- **CTA primaire** : newsletter schoolsWP
- **CTA secondaire** : formation WPVivid (sauvegarde)
- **CTA tertiaire** : avis Samaritain Security (cross-cluster)
- **Lead magnet futur** (à créer) : checklist « 7 tables WordPress à nettoyer chaque mois » PDF

## 7. Sources externes (à citer ou consulter)

- developer.wordpress.org/reference (tables wp_options, transients)
- WP-Optimize doc officielle (updraftplus.com/wp-optimize/)
- WPS Cleaner (WPServeur, plugin FR gratuit)
- Advanced Database Cleaner (sigmaplugin.com)

## 8. Image à la une

Format brand schoolsWP (1920×1080) :

- Verdict card : « Base WordPress propre = sécurité + perf »
- Schéma simplifié : avant / après nettoyage avec poids
- Badge : « PERFORMANCE · MAINTENANCE WORDPRESS »

## 9. Estimation effort

- Recherche complémentaire (top 5 SERP + doc plugins) : 1 h
- Rédaction draft v1 : 2,5 h (tutoriel pas-à-pas avec captures)
- Captures d'écran WP-Optimize + phpMyAdmin : 1 h
- Audit machine 4 axes + corrections : 1 h
- Featured image + meta SEO : 30 min
- Publication WP : 1 h

**Total : ~7 h** pour un guide ~3500 mots avec captures.

## 10. Notes business

- Pas d'affiliation directe (WP-Optimize a un programme — à vérifier).
- Lien naturel vers WPVivid (formation déjà existante) = upsell formation.
- Article evergreen, refresh tous les 6 mois (versions plugins).

## 11. Vérifications pré-publication

- [ ] BRAND_RULES (tutoiement, schoolsWP, em-dash absent, Michaël tréma)
- [ ] Captures d'écran WP-Optimize en français
- [ ] Schéma Rank Math : HowTo (étapes pas-à-pas)
- [ ] Bloc encadré « danger zone » pour la méthode phpMyAdmin
- [ ] Polylang : décider si version EN/DE
- [ ] Lien interne vers Samaritain Security (section sécurité)
- [ ] Newsletter CTA Kadence
