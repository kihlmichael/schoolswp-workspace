---
campaign: Linksclub - liens forum
provider: linksclub.fr (by Linksgarden)
date_commande: 2026-06-04
date_debut: 2026-06-08
date_fin_publication: 2026-10-08
type: lien forum (10 a 12 reponses + 1 reponse/mois pendant 12 mois par cible)
nb_cibles: 5
cout_total: 50.00 EUR
thematiques: Business Entreprise Marketing, Web Agence et SEO
status: en-monitoring
---

# Campagne Linksclub liens forum - juin 2026

Suivi d'impact de la campagne de liens forum sur les pages cibles schoolsWP.
Baseline capturee le **2026-06-04** (avant demarrage 2026-06-08), sur fenetre GSC 90 jours **2026-03-06 -> 2026-06-03**.

## Cibles de la campagne

| #   | URL cible                                                   | Ancre                         | Titre du fil                                                       | Publication |
| --- | ----------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------ | ----------- |
| 1   | https://schoolswp.com/                                      | schoolsWP                     | Quelle ressource francophone pour mieux utiliser WordPress ?       | 2026-06-08  |
| 2   | https://schoolswp.com/                                      | schoolswp.com                 | Tu connais un bon site pour apprendre WordPress simplement ?       | 2026-07-08  |
| 3   | https://schoolswp.com/                                      | le media schoolsWP            | Des conseils concrets pour WordPress, le SEO et l'automatisation ? | 2026-08-08  |
| 4   | https://schoolswp.com/apprendre-wordpress-autonomie/        | un guide publie sur schoolsWP | Quel site consulter pour mieux structurer son WordPress ?          | 2026-09-08  |
| 5   | https://schoolswp.com/fluentcrm-automations-indispensables/ | cette ressource WordPress     | Des ressources utiles pour ameliorer un site WordPress ?           | 2026-10-08  |

## Baseline GSC (fenetre 2026-03-06 -> 2026-06-03, 90 jours)

| Page cible                               | Clics | Impressions | CTR    | Position moy. |
| ---------------------------------------- | ----- | ----------- | ------ | ------------- |
| Accueil (`/`)                            | 8     | 226         | 3,54 % | 3,4           |
| `/apprendre-wordpress-autonomie/`        | 2     | 378         | 0,53 % | 25,5          |
| `/fluentcrm-automations-indispensables/` | 1     | 68          | 1,47 % | 16,3          |

## Baseline backlinks (Ubersuggest, 2026-06-04)

| Metrique           | Valeur |
| ------------------ | ------ |
| Domain Authority   | 13     |
| Backlinks totaux   | 172    |
| Domaines referents | 90     |
| dont nofollow      | 85     |

> Objectif mecanique de la campagne : +5 domaines referents uniques (90 -> ~95).

## Protocole de mesure

A chaque checkpoint, re-collecter et comparer a la baseline :

1. **GSC** : clics / impressions / CTR / position des 3 URLs cibles (meme fenetre glissante 90j ou `compare_search_periods`).
2. **GSC** : evolution des positions sur les requetes cles de chaque page (notamment `fluentcrm` pour la page guide, en pos. 8,3 sur ce terme tete).
3. **Backlinks** (Ubersuggest) : nb de domaines referents + apparition des domaines forum.
4. **Referral** (GA4, hors outillage Claude) : trafic direct depuis les forums = mesure la plus fiable de l'impact reel d'un lien forum.

### Limites d'attribution (a garder en tete)

- Les liens forum sont **majoritairement nofollow** : impact ranking direct faible. Le vrai signal sera le **trafic referent** (GA4), pas la position GSC.
- **Lag GSC** de 2-3 jours + inertie SEO : aucun effet mesurable avant 4-6 semaines apres le 1er lien (donc pas avant ~mi-juillet 2026).
- **Attribution non isolee** : d'autres facteurs (maillage interne, autres backlinks, updates Google) bougent les positions en parallele. On observe une tendance, pas une causalite stricte.

## Checkpoints

| Date                     | Accueil (clics/pos) | apprendre-wp (clics/pos) | fluentcrm (clics/pos) | Ref. domains | Note                      |
| ------------------------ | ------------------- | ------------------------ | --------------------- | ------------ | ------------------------- |
| 2026-06-04 (baseline)    | 8 / 3,4             | 2 / 25,5                 | 1 / 16,3              | 90           | Avant campagne            |
| 2026-07-15 (CP1)         |                     |                          |                       |              | 1er lien depuis ~5 sem.   |
| 2026-08-15 (CP2)         |                     |                          |                       |              |                           |
| 2026-09-15 (CP3)         |                     |                          |                       |              |                           |
| 2026-11-08 (CP4 - bilan) |                     |                          |                       |              | 1 mois apres dernier lien |

## Dispositif d'alerte (rappel + mesure en session)

Mecanisme choisi : un rappel automatique sur Discord #alerts a chaque checkpoint, la collecte/mesure restant manuelle en session (creds GSC locales).

- **Script** : `tools/scripts/linksclub-checkpoint-reminder.ps1` (lit `DISCORD_ROUTINES_WEBHOOK` depuis `.env` au runtime, poste le rappel ; ne collecte aucune donnee). Test manuel : `powershell -File ... -Test`.
- **Tache planifiee** : `schoolsWP Linksclub Checkpoint` (Task Scheduler local). Declenche le **15 du mois, 09h, juillet -> novembre 2026**. Rattrapage si PC eteint (`StartWhenAvailable`), execution autorisee sur batterie. `EndBoundary` 2026-11-30 = la tache **s'arrete d'elle-meme** apres le bilan de novembre (aucune desactivation manuelle requise).
- **Quand le ping arrive** : ouvrir une session, recollecter GSC + Ubersuggest sur les 3 pages cibles, remplir la ligne de checkpoint ci-dessus, commit `audit(linksclub): checkpoint <date>`.

## Decision connexe - produit "Liens sur pages positionnees" ECARTE (2026-06-04)

Test du produit Linksgarden "Liens sur pages positionnees" (lien dofollow sur une page externe deja classee) pour booster les pages formation (ZipWP, Tutor LMS, ecosysteme Fluent).

**Conclusion : ecarte pour la niche schoolsWP.** Sur 4 recherches et 3 categories (Web agence & SEO, Logiciel & developpement, Education & formation) :

- Les mots-cles de marque (zipwp, fluentcrm...) = **zero inventaire** (aucun editeur du reseau ne ranke dessus).
- Les mots-cles larges (creation site internet, wordpress) = uniquement des **pages d'agences locales a 0 top 10**, en position 31-100, a 50-272 EUR. Mauvais ROI.
- Seul hote correct trouve : e-forma.fr (20 top 10, 78 EUR) sur "formation en ligne", mais **hors-niche** (formation bien-etre) et 94% du solde sur un seul lien -> non retenu.

**Regle de tri retenue** pour ce type de produit : n'acheter qu'un hote avec **Nb Top 10 >= 1 (ideal 3+)**, **Position <= 15**, **Volume >= 100**, thematique alignee, prix raisonnable. Sinon passer.

**Pivot decide** : budget conserve (83 EUR), report sur le **maillage interne** (gratuit, sous controle) -> voir `content/decisions/netlinking/maillage-interne-formations-2026-06.md`.
