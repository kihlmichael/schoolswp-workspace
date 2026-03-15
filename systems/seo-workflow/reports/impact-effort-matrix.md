# Tableau Impact / Effort / Priorité — 10 tâches SEO schoolsWP

## Légende

- Impact : H = Haut | M = Moyen | L = Faible
- Effort : XS < S < M < L
- Priorité : P1 = Immédiat | P2 = Moyen terme | P3 = Long terme
- ↑ = montée en priorité si condition remplie

---

## Tableau global

| Tâche | Action                     | Impact SEO | Impact Business | Effort | Priorité | Outils clés               | Dépendances |
| ----- | -------------------------- | ---------- | --------------- | ------ | -------- | ------------------------- | ----------- |
| T1    | Inventaire SEO observable  | M          | M               | S      | **P1**   | n8n, Sheets, Agent IA     | Aucune      |
| T2    | Crawl + Indexation         | **H**      | M               | M      | **P1**   | Screaming Frog, Sheets    | T1          |
| T3    | Analyse GSC                | **H**      | **H**           | S      | **P1**   | GSC, Sheets               | T1, T2      |
| T4    | Benchmark DataForSEO       | **H**      | **H**           | M      | P2       | DataForSEO API, Sheets    | T3          |
| T5    | Clusters & Cannibalisation | **H**      | **H**           | M      | P2       | Sheets, cluster-architect | T1, T3, T4  |
| T6    | Maillage interne           | **H**      | **H**           | M      | P2       | n8n, Sheets, crawl        | T2, T5      |
| T7    | SEO multilingue FR/EN/DE   | **H**      | M               | M      | P2 ↑P1   | Sheets, crawl hreflang    | T1, T2      |
| T8    | E-E-A-T templates          | M          | **H**           | S      | P2       | Docs, Agent IA            | T3, T5      |
| T9    | Conversion SEO             | M          | **H**           | M      | P2       | Sheets, money-pages skill | T3, T5, T6  |
| T10   | Priorisation & Roadmap     | **H**      | **H**           | S      | **P1**   | Sheets, Docs              | T2→T9       |

↑ T7 monte en P1 si perte de trafic EN/DE confirmée via GSC

---

## Classement par score impact/effort

Score = (Impact SEO H=3/M=2/L=1) + (Impact Business H=3/M=2/L=1) / Effort (XS=4/S=3/M=2/L=1)

| Rang | Tâche            | Score      | Raison               |
| ---- | ---------------- | ---------- | -------------------- |
| 1    | T3 — GSC         | 6/3 = 2.0  | H+H impact, S effort |
| 2    | T10 — Roadmap    | 6/3 = 2.0  | H+H impact, S effort |
| 3    | T8 — E-E-A-T     | 5/3 = 1.67 | M+H impact, S effort |
| 4    | T1 — Inventaire  | 4/3 = 1.33 | M+M impact, S effort |
| 5    | T2 — Crawl       | 5/2 = 1.25 | H+M impact, M effort |
| 6    | T5 — Clusters    | 6/2 = 1.0  | H+H impact, M effort |
| 7    | T6 — Maillage    | 6/2 = 1.0  | H+H impact, M effort |
| 8    | T4 — Benchmark   | 6/2 = 1.0  | H+H impact, M effort |
| 9    | T9 — Conversion  | 5/2 = 0.75 | M+H impact, M effort |
| 10   | T7 — Multilingue | 5/2 = 0.75 | H+M impact, M effort |

---

## Actions P1 recommandées (immédiat, effort ≤ S)

Ces actions peuvent démarrer maintenant sans données complémentaires :

| Action                                          | Type           | Effort | Condition                      |
| ----------------------------------------------- | -------------- | ------ | ------------------------------ |
| Noindexer pages login/feeds/archives            | Observable     | XS     | Pages visibles dans le sitemap |
| Ajouter disclosure affiliation                  | Observable     | XS     | Absence confirmée par lecture  |
| Exporter GSC 28j et identifier CTR faibles      | Bonne pratique | XS     | Accès GSC disponible           |
| Réécrire le title de la page CTR la plus faible | GSC data       | S      | Export GSC disponible          |
| Ajouter liens depuis homepage vers 3 piliers    | Observable     | S      | Structure menu connue          |

---

## Risques globaux

| Risque                            | Impact                  | Mitigation                                     |
| --------------------------------- | ----------------------- | ---------------------------------------------- |
| Crawl non disponible              | Bloque T2, T6, T7       | Screaming Frog gratuit (500 URLs) en attendant |
| GSC non configuré                 | Bloque T3               | Configurer GSC en priorité absolue             |
| DataForSEO sans crédits           | Bloque T4 partiellement | Commencer par les 3 clusters P1                |
| Cannibalisations trop nombreuses  | Ralentit T5             | Traiter par cluster P1 uniquement              |
| Ressources dev WordPress limitées | Ralentit T6, T8, T9     | Grouper les interventions template             |
