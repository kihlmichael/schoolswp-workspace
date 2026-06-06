# avis-booknetic-wordpress — index audits

- **URL** : https://schoolswp.com/?p=2969996 (brouillon, FR)
- **post_id** : 2969996
- **Mot-clé cible** : `avis booknetic`
- **Pilier** : plugins / automatisation (avis affilié)
- **Statut courant** : `refonte-decidee` (corrections ciblées pré-publication)

## Historique des snapshots

| Date                                 | Trigger                           | Score estimé | Décision                                       | Synthèse                              |
| ------------------------------------ | --------------------------------- | ------------ | ---------------------------------------------- | ------------------------------------- |
| [2026-06-03](2026-06-03/synthese.md) | Demande Michaël (pré-publication) | ≈ 52/100     | Ne pas publier en l'état — corrections ciblées | [synthese.md](2026-06-03/synthese.md) |

## Résumé du dernier audit (2026-06-03)

Marché minuscule et déclinant : `avis booknetic` = 0 volume mesurable, `booknetic` = 90/mois (**-55 % sur 1 an**). SERP FR 100 % annuaires d'avis + officiel (0 blog éditorial FR). Valeur de l'article = **capture affiliée**, pas trafic.

**5 bloquants avant publication** : (1) mix tutoiement/vouvoiement, (2) FAQ en anglais, (3) **aucun CTA/lien affilié**, (4) prix incohérents et faux, (5) note 4,91 vs 4,5 contradictoire. + 6 importants (table wp:html, lien interne incohérent, URL polluée, meta absente, voix « notre », mot « sans effort ») + améliorations SERP (schema Review, comparatif concurrents, screenshots).

## Actions réalisées / en attente

- [x] Lot 1 — bloquants : tutoiement (B1), FAQ FR (B2), prix réels 45/99/199/299 $ (B4), note 4,93/5 unifiée (B5) — **appliqué le 2026-06-03 via Novamira (str_replace in-place + wp_slash, Kadence intact)**
- [x] **B3 — CTA / lien affilié Booknetic** : cloak `/booknetic/` → `https://www.booknetic.com?ref=aajfwp` (mu-plugin v1.2.0, 302) + 2 boutons CTA insérés (après l'encart + conclusion) — appliqué 2026-06-03
- [x] Lot 2 — importants : table native (I1), lien interne incohérent retiré (I2), URL Masteriyo nettoyée + rel (I3), « sans effort » reformulé (I6), meta description + focus keyword Rank Math (I4), balises meta charset parasites supprimées (A6)
- [~] Lot 3 — compétitivité (appliqué le 2026-06-05) :
  - [x] schema **Review + AggregateRating (4,93/5, 444 avis CodeCanyon) + 4 offres** + schema **FAQPage** (5 Q/R) + **BlogPosting** (préservé) — postmeta Rank Math, dates en variables
  - [x] mini-comparatif **Amelia / Bookly / BookingPress** (tableau natif, avant « Avis final »)
  - [x] correctif : les 2 boutons CTA (convertis en boutons Kadence côté éditeur) avaient perdu leur lien → réinjecté vers le cloak `/booknetic/`, dégradé intact
  - [ ] **captures d'écran du plugin en fonctionnement — Michaël (E-E-A-T, screenshots réels, jamais générés)** → traitement SEO + EXIF + placement via `tools/wp-media-upload` une fois fournies

> Détail des changements : [2026-06-03/fr-corrections-plan.md](2026-06-03/fr-corrections-plan.md). Article toujours en **brouillon** (validation humaine requise avant publication).
