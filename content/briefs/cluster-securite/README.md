---
cluster: Sécurité WordPress
date_creation: 2026-05-26
auteur: Michaël KIHL
statut: phase brief (3/3 briefs prêts à produire)
article_pilier: avis Samaritain Security
---

# Cluster éditorial — Sécurité WordPress

## Vue d'ensemble

Cluster topique défensif construit autour de l'article pilier **[Avis Samaritain Security](https://schoolswp.com/samaritain-security-avis/)** (publié 2026-05-26, Publish Score v4 estimé 87/100). Le pilier est positionné en couverture défensive de marque sur une SERP off-topic (homonymes film Stallone, grand magasin, etc.) — les 3 satellites lui donnent l'autorité topique réelle sur la sémantique « sécurité WordPress ».

## Pilier vs Satellites — rôles

| Article                                           | Rôle topique                            | Volume kw principal                              | Intent           |
| ------------------------------------------------- | --------------------------------------- | ------------------------------------------------ | ---------------- |
| Avis Samaritain Security (pilier)                 | Avis plugin commercial, brand defensive | 0/mois (requête de marque, off-topic)            | navigationnelle  |
| Satellite #1 : Hébergeur WordPress sécurisé       | Choix infrastructure                    | 720/mois (meilleur hébergeur wp, KD 5)           | commerciale      |
| Satellite #2 : Nettoyer base de données WordPress | Maintenance & sécurité                  | 210/mois (wp optimize, KD 18)                    | informationnelle |
| Satellite #3 : Double authentification WordPress  | Tutoriel + récupération                 | 140/mois cumulé (2fa + double auth, KD très bas) | navigationnelle  |

**Lecture stratégique** : 3 satellites cumulent ~1070 vol/mois mesurés, contre 0 pour le pilier. Les satellites apportent le trafic, le pilier capture la conversion brand-aware. Pattern défensif typique schoolsWP : on absorbe la requête de marque + on construit l'autorité topique en parallèle.

## Briefs disponibles

| #   | Brief                                                                        | Slug                               | Volume   | Effort estimé |
| --- | ---------------------------------------------------------------------------- | ---------------------------------- | -------- | ------------- |
| 1   | [Hébergeur WordPress sécurisé](01_hebergeur-wordpress-securise.md)           | hebergeur-wordpress-securise       | 720/mois | ~5,5 h        |
| 2   | [Nettoyer base de données WordPress](02_nettoyer-base-donnees-wordpress.md)  | nettoyer-base-de-donnees-wordpress | 210/mois | ~7 h          |
| 3   | [Double authentification WordPress](03_double-authentification-wordpress.md) | double-authentification-wordpress  | 140/mois | ~8 h          |

**Total effort cluster : ~20,5 h** pour 3 articles ~3000-3500 mots chacun, avec audit machine 4 axes, image à la une, captures et publication.

## Priorisation recommandée

### Ordre de production conseillé

1. **Satellite #3 — 2FA WordPress** (en premier) — angle « récupération d'accès » absent de la SERP, opportunité de ranker rapidement sur un kw KD très bas. Bénéfice : trafic immédiat + signal topique fort.
2. **Satellite #1 — Hébergeur sécurisé** (en deuxième) — KD 5 sur « meilleur hébergeur wordpress », gros volume (720), affiliation Copilhost active — ROI commercial le plus élevé du cluster.
3. **Satellite #2 — Nettoyer base** (en dernier) — solide en évergreen, KD 18, mais ROI plus lent. Bénéfice : ferme la boucle technique du cluster.

### Justification

- Le 2FA a un angle exclusif (« récupération ») qui n'est pas dans le top 10 — on peut prendre la place de la PAA « comment récupérer l'accès si on perd la 2FA » dès indexation.
- L'hébergeur est commercial (CPC 9,42 €) avec une affiliation Copilhost déjà active — cash flow direct.
- Le nettoyage base est important pour cohérence cluster mais plus standard et déjà bien couvert en SERP.

### Alternative : tout publier la même semaine

Si tu veux maximiser le signal de cluster simultané pour Google, publier les 3 dans la même semaine + un internal linking croisé (chaque article pointe vers les 2 autres + vers le pilier Samaritain) renforce l'autorité topique perçue. Coût : ~20,5 h sur 5 jours = charge soutenue mais faisable.

## Maillage interne du cluster

Cross-link à respecter (graphe directionnel) :

- **Pilier Samaritain Security** pointe vers les 3 satellites (section dédiée « Cluster sécurité » à ajouter après publication).
- **Satellite #1 Hébergeur** pointe vers : Samaritain (plugin compatible), #3 2FA (compléter la protection).
- **Satellite #2 Base** pointe vers : Samaritain (durcissement), #1 Hébergeur (infra propre), WPVivid formation (sauvegarde).
- **Satellite #3 2FA** pointe vers : Samaritain (couplage), #2 Base (méthode de récupération via BDD), #1 Hébergeur (support pour récupération).

### Ancres recommandées

- Pilier Samaritain → satellites : « hébergeur sécurisé compatible », « base de données propre = sécurité renforcée », « activer la 2FA en complément »
- Satellite #1 → autres : « plugin de durcissement compatible » (Samaritain), « 2FA pour fermer l'accès admin » (#3)
- Satellite #2 → autres : « plugin de durcissement » (Samaritain), « sauvegarde obligatoire » (WPVivid formation existante)
- Satellite #3 → autres : « masquer la page de connexion » (Samaritain), « accéder à la base de données » (#2), « support hébergeur réactif » (#1 via Copilhost)

## Données SERP brutes (DataForSEO 2026-05-26)

### Satellite #1 — Hébergeur

- Top 10 saturé : amphibee, 01net, lesnumeriques, clubic, tool-advisor, websiteplanet, experte, codeur, wpmarmite
- Angle Copilhost visible (cité Codeur.com en position 9)
- Pattern dominant : tableau comparatif + recommandation par profil

### Satellite #2 — Base de données

- Top 10 plus accessible : lws, wp-umbrella, crea-troyes, reddit, metaforweb, wppourlesnuls, niverel, moncoachwp
- Plugins dominants : WP-Optimize, WPS Cleaner, Advanced Database Cleaner
- PAA : sauvegarde, types BDD, WPS Cleaner, changement URL

### Satellite #3 — 2FA

- Top 10 : wpmarmite, wordpress.com, wpformation, webooste, mirobolus, mickael-maury, lws, wp-umbrella, it-connect
- Plugins dominants : WP 2FA, Two-Factor, Wordfence, miniOrange Google Authenticator
- **Aucun article ne traite la récupération d'accès en cas de perte 2FA** — angle exclusif schoolsWP

## Conversion & business

Tous les satellites pointent vers :

- **Newsletter schoolsWP** (CTA primaire, tunnel FluentCRM welcome lead magnet déjà actif)
- **Avis Samaritain Security** (CTA cross-cluster, lien direct vers samaritain-security.com sans cloak)
- **Copilhost** (affiliation active, satellite #1 en premier lieu)
- **Formation WPVivid** (satellite #2, upsell formation existante)

Lead magnets potentiels à créer (un par satellite) :

- #1 : Checklist « 10 critères de sécurité serveur WordPress »
- #2 : Checklist « 7 tables WordPress à nettoyer chaque mois »
- #3 : Checklist « Protocole 2FA WordPress + plan de récupération »

## État d'avancement

- [x] Audit topical de l'article pilier Samaritain Security (74/100, rôle Satellite fort confirmé)
- [x] DataForSEO keyword overview + suggestions pour les 3 satellites
- [x] SERP top 10 pull pour les 3 keywords pivots
- [x] Brief #1 — Hébergeur WordPress sécurisé
- [x] Brief #2 — Nettoyer base de données WordPress
- [x] Brief #3 — Double authentification WordPress
- [x] Index cluster (ce fichier)
- [ ] Décision Michaël : ordre de production + déclenchement
- [ ] Production satellite (au choix : brain-lite, radar agent, ou schoolswp-article-workflow skill)
- [ ] Audit machine 4 axes par satellite
- [ ] Featured images
- [ ] Publication WP avec maillage croisé
- [ ] Mise à jour de l'article pilier Samaritain (section « Cluster sécurité » avec liens vers les 3 satellites publiés)

## Commandes de production (à exécuter par Michaël quand prêt)

Une fois la décision prise, voici les options de pipeline pour lancer la production d'un satellite. Voir CLAUDE.md du projet pour le détail de chaque option et les flags disponibles.

- **Option 1 : pipeline complet** — brain.bat avec keyword + intent + pillar
- **Option 2 : pipeline léger** — brain-lite.bat avec keyword + intent + pilier
- **Option 3 : sub-agent radar** (préparation SEO) puis studio (rédaction), dispatch via le tool Agent en session

## Liens audits associés

- Audit pilier Samaritain Security (v4 estimé 87/100) : `content/audits/samaritain-security-avis/2026-05-26/audit-consolide.md`
- Audit topical (satellites identifiés) : `content/audits/samaritain-security-avis/2026-05-26/audit-topical.md`
- Synthèse outbox Obsidian (en attente arbitrage L0) : `obsidian-bridge/outbox-to-obsidian/2026-05-26_synthese_audit-samaritain-security-avis.md`
