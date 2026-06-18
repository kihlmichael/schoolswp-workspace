---
title: "Hub xCloud Hosting — plan de cluster schoolsWP"
date: 2026-06-01
status: validated
owner: Michaël
type: cluster-plan
pilier: hosting
affiliation: xCloud / FirstPromoter (ref schoolswp)
---

# Hub xCloud Hosting — plan de cluster

## Décisions verrouillées (2026-06-01)

- **GO cluster** (pas juste un article isolé)
- **Affiliation** : https://schoolswp.com/xcloud/ → cloak vers https://xcloud.host?fpr=schoolswp (FirstPromoter)
- **Captures réelles** : compte xCloud actif côté Michaël, screenshots de prod disponibles
- **Couche YouTube** : activée dès le pilier (handoff youtube-os-orchestrator)
- **Lead magnet** : checklist PDF « Migrer Cloudways → xCloud en 12 étapes »
- **Ordre de production** : pilier → comparatif Cloudways → tarifs → migration → satellites TOFU

## Données SERP (verrouillées)

- Mot-clé principal **xcloud avis** : 10/mo FR, LOW competition, intent informational + commercial
- Volume cluster cumulé exploitable : ~70/mo FR
- Concurrence FR éditoriale : busilearn.fr seul (article 2024 light, sans captures, sans avis utilisateur réel)
- Pollution sémantique Xbox xCloud : 30 % de la SERP → opportunité de désambiguïsation
- Vidéo : video carousel Google 100 % EN (Cloud Guru) → slot FR vacant

## Volumes long-tail FR (réf brief)

| Mot-clé                                                                    | Vol/mois           | Intent            | KD  |
| -------------------------------------------------------------------------- | ------------------ | ----------------- | --- |
| xcloud avis                                                                | 10                 | info + commercial | —   |
| xcloud prix                                                                | 10                 | commercial        | 52  |
| xcloud test                                                                | 10                 | informational     | 53  |
| xcloud review                                                              | 10                 | info + commercial | 82  |
| cloudways alternative                                                      | 10                 | info + commercial | —   |
| managed wordpress hosting                                                  | 20                 | commercial        | 99  |
| autres (xcloud hosting, xcloud vs cloudways, xcloud wordpress, xcloud n8n) | < 10 (non indexés) | —                 | —   |

## Architecture cluster

PILIER (BOFU décisionnel)

- /xcloud-avis/

SATELLITES BOFU

- /xcloud-vs-cloudways/
- /xcloud-tarifs/
- /migrer-cloudways-vers-xcloud/

SATELLITES TOFU/MOFU (angles uniques FR)

- /xcloud-n8n-hosting/
- /xcloud-openclaw-ai/
- /xcloud-agence-white-label/

OPTIONNELS PHASE 2 (à valider sur ICP)

- /xcloud-vs-runcloud/
- /xcloud-vs-spinupwp/
- /xcloud-vs-serveravatar/

## Maillage interne

- Chaque satellite link le pilier /xcloud-avis/ dans intro + FAQ
- Pilier link les 6 satellites en section « Aller plus loin »
- Pilier FluentCRM → lien sortant vers /xcloud-n8n-hosting/ (n8n = pile automatisation FluentCRM)
- Articles affiliation FluentSupport / FluentBoards / FluentCart → lien vers /xcloud-avis/ quand hébergement est mentionné
- Lead magnet « checklist migration » → ancré dans /migrer-cloudways-vers-xcloud/ (CTA principal) + pilier (CTA secondaire)

## Différenciateurs vs busilearn.fr

| Faiblesse busilearn                        | Réponse schoolsWP                                                                                           |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| 0 avis utilisateur réel                    | Trustpilot 349 avis 4.7/5 + 3-4 testimonials nominaux (Dave Swift, David Risley, Tony Lewis) avec citations |
| Pas de captures dashboard                  | Captures réelles compte actif Michaël                                                                       |
| Pas de test perf                           | TTFB / Lighthouse / benchmark migration                                                                     |
| Pas de comparatif                          | Tableau Cloudways / Kinsta / o2switch sur 5-7 critères                                                      |
| Pas de désambiguïsation Xbox               | Encart court intro « ne pas confondre »                                                                     |
| Pas de mention OpenClaw / n8n / AI agents  | Sections dédiées (angle innovation 2026)                                                                    |
| Pas de mention WPDeveloper / WPManageNinja | Angle écosystème, légitimité éditoriale schoolsWP                                                           |
| Lien affilié ciroapp                       | Cloak propre schoolswp.com/xcloud/                                                                          |
| Tarifs $ uniquement                        | Conversion EUR + estimation TTC pro français                                                                |

## Bémols à signaler honnêtement (BRAND_RULES 31)

- Ubuntu uniquement (pas Debian / CentOS)
- Interface anglaise uniquement
- Cloudflare jugée complexe pour débutants
- Documentation « à compléter »
- Société hors UE (WPDeveloper Bangladesh, US registration)
- Pas de localisation FR (support en anglais)

## Tarifs xCloud (capturés 2026-06-01)

Self-Managed (Bring Your Own Server) :

- Free : 1 serveur / 10 sites
- Starter : 5 $/serveur (1-5)
- Professional : 4 $/serveur (6-10)
- Agency : 3 $/serveur (11+)

Managed Server : voir tableau complet dans le brief pilier (15 plans, 5 $ à 399 $/mois, double tier SSD / Premium NVMe).

## TODO production

### Phase 1 — Pilier

- [ ] Brief SEO /xcloud-avis/ (handoff radar ou rédaction directe à partir de cette synthèse)
- [ ] Production captures réelles dashboard + Lighthouse + TTFB
- [ ] Rédaction pilier (handoff studio ou thruuu-article-orchestrator si brief thruuu généré)
- [ ] QA branding + cloak vérifié
- [ ] Schema Review actif (ratingValue + reviewBody, citer Trustpilot/G2)
- [ ] Handoff youtube-os-orchestrator pour vidéo pilier (slot carousel FR vacant)

### Phase 2 — Comparatifs et tarifs

- [ ] /xcloud-vs-cloudways/ (le plus chaud du segment)
- [ ] /xcloud-tarifs/ (BOFU achat frontal)

### Phase 3 — Migration et lead magnet

- [ ] /migrer-cloudways-vers-xcloud/ (tutoriel)
- [ ] Lead magnet checklist PDF « Migrer Cloudways → xCloud en 12 étapes » (pipeline tools/html-to-png/md-to-pdf.mjs)
- [ ] Funnel FluentCRM dédié (tag lead-magnet-xcloud-migration)

### Phase 4 — Satellites TOFU/MOFU

- [ ] /xcloud-n8n-hosting/ (premier sur FR, angle innovation)
- [ ] /xcloud-openclaw-ai/
- [ ] /xcloud-agence-white-label/

## Handoffs

- **radar** : brief SEO pilier + maillage cocon
- **studio** : rédaction articles
- **thruuu-article-orchestrator** : pipeline complet si brief thruuu .docx généré
- **youtube-os-orchestrator** : pilier vidéo + comparatif Cloudways vidéo
- **pulse** : posts LinkedIn / Pinterest / Bluesky de recyclage
- **flow** : funnel FluentCRM lead magnet + tag system
- **pinterest-strategy + pinterest-pipeline** : pins comparatif tarifs + checklist migration

## Réfs mémoire

- project_affiliate_links (xCloud ajouté 2026-06-01)
- reference_affiliate_cloak_pattern (schoolswp-affiliate-cloaks.php)
- feedback_competitor_reviews_respect (BRAND_RULES 31)
- project_review_accounts (captures pro)
- feedback_no_em_dash (typographie)
- feedback_no_english_jargon_sales (vocabulaire FR)
- reference_pdf_pipeline_schoolswp (lead magnet PDF)
