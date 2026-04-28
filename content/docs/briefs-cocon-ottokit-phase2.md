# Briefs — Cocon OttoKit, Phase 2 (Comparatifs priorité 1)

> **Contexte :** Phase 2 du MVP 12 pages, lancée après validation du pilier P0 (`/ottokit/`).
> **Cible trafic cumulé phase 2 :** ~190 recherches/mois (E3 + E4 + E1).
> **Date :** 2026-04-23
> **Source cocon :** [cocon-ottokit-schoolswp.md](./cocon-ottokit-schoolswp.md)

---

## Règles communes aux 3 briefs

- **Tutoiement systématique**, schoolsWP (jamais schoolswp), slugs sans année ni mention "schoolswp".
- **Mots interdits** (branding) : disruptif, game changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de.
- **Intent comparative** : le lecteur cherche à décider, pas à apprendre. Il veut un verdict étayé, pas un tutoriel.
- **Réponse rapide dans les 100 premiers mots** (verdict synthétique) — le reste développe la preuve.
- **Paragraphes courts** (2-4 phrases max), **tableaux** pour comparatifs chiffrés.
- **Liens affiliés OttoKit Pro** placés naturellement (pas en bloc promo). Lien direct vers schoolswp.com pour FluentCRM, SureCart, etc. — pas de `/go/` (cf. mémoire).
- **Schema** : `Article` + `FAQPage` obligatoire, `Review` optionnel si structure d'avis.
- **Une page formation F1 (lien interne)** sur chaque article.

---

## BRIEF E3 — OttoKit vs Uncanny Automator (PRIORITÉ 1)

### Métadonnées

| Champ | Valeur |
|---|---|
| **Slug** | `/ottokit-vs-uncanny-automator/` |
| **Mot-clé primaire** | `uncanny automator` (70/mois FR, **CPC 3,11 €**) |
| **Mot-clé secondaire** | `automator wordpress` (10/mois) |
| **Volume cumulé** | **80/mois** |
| **Intent** | comparative (commerciale) |
| **Longueur cible** | 1 500–2 000 mots |
| **Pillar** | automatisation |
| **Objective** | formation (CTA F1) + affiliation OttoKit Pro |

### 1. Intent utilisateur réel

Quelqu'un qui tape `uncanny automator` en France **connaît déjà ce plugin** ou vient de le découvrir. Il veut savoir si c'est la bonne solution avant d'acheter la version Pro. Il n'est pas (encore) sur le radar d'OttoKit.

**Conséquence éditoriale :** on commence par répondre sérieusement à *"Uncanny Automator c'est bien ?"* avant de pivoter sur OttoKit. Un comparatif qui flingue Uncanny d'entrée = rebond immédiat + perte de confiance.

### 2. Angle schoolsWP

> **Promesse :** "Avant d'acheter Uncanny Automator Pro, lis ce comparatif. Sur beaucoup de cas WordPress, OttoKit fait la même chose sans charger ton serveur — et souvent moins cher."

Différenciation vs la SERP actuelle :
- La SERP est dominée par **le site officiel d'Uncanny** + des tutoriels anglais + des reviews de blogs US.
- **Seule ressource FR structurée, et seule à comparer avec OttoKit en vrai** (angles cloud vs on-site).

### 3. Anti-angles (à éviter)

- Tableau de features sans verdict clair.
- Dénigrement d'Uncanny dès le titre — casse l'intent du lecteur.
- Parler d'OttoKit avant le paragraphe 3.
- "Uncanny est mort, tout le monde passe à OttoKit" — faux.
- Jargon SEO ou marketing (Zapier killer, alternative ultime…).

### 4. Données à collecter avant rédaction

- [ ] Prix Uncanny Automator Pro 2026 (tiers Silver/Gold/Platinum, nombre d'apps)
- [ ] Nombre d'intégrations Uncanny vs OttoKit (source officielle)
- [ ] Modèle exécution : triggers on-site Uncanny (cron, hooks WP) vs cloud OttoKit
- [ ] Impact perf serveur : benchmarks publics si existants, sinon raisonnement charge
- [ ] Roadmap Uncanny 2026 (Brainstorm Force vs Uncanny Owl, actualité)
- [ ] Cas où Uncanny reste meilleur (triggers on-site stricts, offline, conformité)

### 5. Plan H2/H3 détaillé

```
H1 : OttoKit vs Uncanny Automator : lequel choisir en 2026 ?

H2. Verdict en 30 secondes
  (tableau synthétique + 3 lignes : "choisis Uncanny si..." / "choisis OttoKit si...")

H2. Les deux approches : cloud vs on-site
  H3. Uncanny Automator : 100 % dans ton WordPress
  H3. OttoKit : moteur cloud connecté à WordPress
  H3. Impact concret sur ton site (perf, hébergement, sauvegardes)

H2. Intégrations WordPress : comparaison directe
  (tableau : WooCommerce, FluentCRM, LearnDash, TutorLMS, Kadence, WPForms, Fluent Forms, Elementor...)

H2. Apps externes (hors WordPress)
  H3. OttoKit : 1 300+ apps natives
  H3. Uncanny : dépend d'intégrations tierces
  H3. Verdict : écrasant côté OttoKit

H2. Prix et modèle économique
  H3. Uncanny : licence annuelle par site + crédits
  H3. OttoKit : SaaS mensuel par tâches
  H3. Simulation sur un site WP moyen (2 000 tâches/mois)

H2. Performance serveur : ce que la moyenne des plugins oublie
  H3. Pourquoi Uncanny charge ton serveur
  H3. Pourquoi OttoKit ne le touche pas
  H3. Quand c'est critique (LMS, e-commerce, membership)

H2. Facilité d'usage
  H3. Interface Uncanny (recipe-based)
  H3. OttoKit Canvas (visual flow)

H2. Quand Uncanny reste la meilleure option
  (cas honnêtes : pas d'internet fiable, conformité RGPD stricte sur les données,
   triggers ultra-custom on-site)

H2. Verdict schoolsWP : pour qui, quoi ?

H2. FAQ (schema FAQPage)
  - Uncanny Automator est-il meilleur qu'OttoKit ?
  - Peut-on utiliser les deux en même temps ?
  - OttoKit ralentit-il mon site comme Uncanny ?
  - Combien coûte vraiment Uncanny Automator Pro en 2026 ?
  - OttoKit fonctionne-t-il sans abonnement ?
```

### 6. Meta draft

- **Title** (≤ 60 car) : `OttoKit vs Uncanny Automator : lequel choisir (2026)`
- **Meta description** (≤ 155 car) : `Uncanny Automator tourne dans ton site, OttoKit tourne dans le cloud. Comparatif prix, perf, intégrations et verdict honnête.`

*Note hygiène URL :* slug sans année, conforme à la règle evergreen. La date dans le title est tolérée.

### 7. Maillage interne

- **Liens entrants** (à créer/vérifier depuis) : P0 (section comparatifs), E1, E2, E4.
- **Liens sortants** (dans l'article) : P0 (ancre *"le guide complet OttoKit"*), E1 (*"si tu compares plutôt à Zapier"*), E2 (*"ou à Make"*), F1 (*"formation OttoKit"*).
- **Ancres suggérées** :
  - Vers P0 : "guide OttoKit", "OttoKit en français"
  - Vers F1 : "apprendre OttoKit", "formation OttoKit pas à pas"
  - Vers E4 : "comparatif OttoKit vs n8n"

### 8. CTA / Affiliation

- **CTA principal** : lien formation F1 (encadré en milieu d'article, après section perf serveur).
- **Affiliation** : lien OttoKit Pro en fin d'article + dans le tableau de prix (pas de `/go/` — lien direct).
- **Pas de CTA agressif** dans les 500 premiers mots — on installe d'abord la crédibilité.

### 9. Commande de production

```
brain.bat --keyword "ottokit vs uncanny automator" --intent comparative --pillar automatisation --objective formation --include-serp
```

*Note :* `--include-ner` optionnel — utile si tu veux une couverture entité exhaustive, sinon `brain.bat` sans NER économise ~5 min.

---

## BRIEF E4 — OttoKit vs n8n (PRIORITÉ 1)

### Métadonnées

| Champ | Valeur |
|---|---|
| **Slug** | `/ottokit-vs-n8n/` |
| **Mot-clé primaire** | `n8n wordpress` (70/mois FR) |
| **Mot-clé secondaire** | `ottokit vs n8n` (10/mois) |
| **Volume cumulé** | **80/mois** |
| **Intent** | comparative (commerciale) |
| **Longueur cible** | 1 500–1 800 mots |
| **Pillar** | automatisation |
| **Objective** | formation (CTA F1) + affiliation OttoKit Pro |

### 1. Intent utilisateur réel

Quelqu'un qui tape `n8n wordpress` cherche **comment connecter n8n à WordPress**. Il connaît n8n (souvent un profil tech ou growth un peu technique) et veut savoir si ça marche avec son site. Il ne cherche pas forcément un comparatif.

**Conséquence éditoriale :** on répond d'abord à *"peut-on utiliser n8n avec WordPress ?"* — oui, mais c'est lourd. Puis on introduit OttoKit comme alternative plus directe pour un public WordPress.

**Sous-angle pour `ottokit vs n8n` (10/mois) :** profil déjà décidé à comparer — pour eux on met le tableau synthétique haut de page.

### 2. Angle schoolsWP

> **Promesse :** "n8n est un bijou technique, mais pour WordPress c'est souvent surdimensionné. OttoKit fait le même travail sans VPS, sans JSON, sans maintenance."

Différenciation :
- La SERP FR pour `n8n wordpress` est **dominée par des tutos techniques** (docker-compose, webhook setup, JSON payload).
- **Nous** on prend l'angle producteur/créateur WordPress non-dev qui a vu passer n8n et se demande s'il doit s'y mettre.
- On ne cache pas les forces de n8n (gratuit self-host, très puissant, open source).

### 3. Anti-angles (à éviter)

- "n8n c'est trop compliqué, OttoKit c'est mieux" — faux pour le public n8n.
- Sous-estimer n8n (open source, self-host gratuit, énorme communauté, licence fair-code).
- Comparer les prix sans dire que n8n peut être gratuit.
- Ne pas parler des enjeux **maintenance / hébergement / RGPD** — c'est le vrai vrai différenciateur.

### 4. Données à collecter avant rédaction

- [ ] n8n self-hosted : coût réel (VPS, Docker, SSL, backups) — chiffrer une config type
- [ ] n8n Cloud : pricing actuel 2026
- [ ] Intégration n8n avec WordPress : nodes officiels, community nodes, webhooks REST
- [ ] Learning curve : durée moyenne pour un workflow simple
- [ ] Cas d'usage où n8n est supérieur (traitements complexes, IA in-flow, API custom)
- [ ] Cas d'usage où OttoKit gagne (créateur WP non-dev, formation client, productivité solo)

### 5. Plan H2/H3 détaillé

```
H1 : OttoKit vs n8n : quel outil d'automatisation pour ton WordPress ?

H2. Verdict en 30 secondes
  (tableau + 3 lignes "choisis n8n si..." / "choisis OttoKit si...")

H2. n8n en bref : qu'est-ce que c'est ?
  H3. Open source, self-hosted ou cloud
  H3. Canvas ultra-puissant + JS inline
  H3. Public cible : devs, growth, équipes tech

H2. OttoKit en bref : qu'est-ce que c'est ?
  H3. Cloud natif, pensé WordPress
  H3. Public cible : créateurs WP, freelances, entrepreneurs

H2. Connecter n8n à WordPress : comment ça marche ?
  H3. Via REST API + webhooks
  H3. Via plugins communautaires
  H3. Limites côté maintenance

H2. OttoKit + WordPress : intégration native
  H3. Déclencheurs WP (post publié, user inscrit, commande WooCommerce...)
  H3. Actions WP sans config serveur

H2. Comparatif direct
  (tableau : prix, WP, apps, hébergement, maintenance, apprentissage, RGPD, scaling)

H2. Coût réel sur 1 an
  H3. n8n self-hosted (VPS + temps admin)
  H3. n8n Cloud
  H3. OttoKit
  H3. Simulation pour un freelance WP / une agence

H2. Qui doit choisir n8n ?
  (cas honnêtes : besoin de scripts JS, data engineering, IA en pipeline...)

H2. Qui doit choisir OttoKit ?

H2. Peut-on utiliser les deux en même temps ?
  (oui, cas hybrides)

H2. Verdict schoolsWP

H2. FAQ (schema FAQPage)
  - n8n est-il gratuit ?
  - Peut-on utiliser n8n sans coder ?
  - OttoKit remplace-t-il complètement n8n ?
  - Quel outil pour un freelance WordPress ?
  - n8n est-il plus puissant qu'OttoKit ?
```

### 6. Meta draft

- **Title** (≤ 60 car) : `OttoKit vs n8n : cloud ou self-hosted pour WordPress`
- **Meta description** (≤ 155 car) : `n8n est open source et très puissant. OttoKit est natif WordPress et sans maintenance. Comparatif coût, perf, intégrations et cas d'usage.`

### 7. Maillage interne

- **Liens entrants** (à créer/vérifier) : P0, E1, E2, E3, C1 (WooCommerce si future page).
- **Liens sortants** : P0 (*"guide OttoKit"*), E1 (*"comparatif avec Zapier"*), E2 (*"et avec Make"*), F1 (*"formation OttoKit"*).
- **Lien externe autorisé** : site officiel n8n + doc officielle (1 par 500 mots max, jamais d'affilié vers le concurrent).

### 8. CTA / Affiliation

- **CTA principal** : formation F1 (après section *"OttoKit + WordPress : intégration native"*).
- **Affiliation OttoKit Pro** : en fin d'article et dans le tableau de prix.
- **Pas de push OttoKit** tant que le lecteur n'a pas eu une vraie réponse sur n8n.

### 9. Commande de production

```
brain.bat --keyword "ottokit vs n8n" --intent comparative --pillar automatisation --objective formation --include-serp
```

*Alternative :* si la SERP pour `n8n wordpress` (70/mois, TOP kw) diverge trop de celle pour `ottokit vs n8n` (10/mois), lancer **deux runs** et choisir le meilleur. Typiquement `--keyword "n8n wordpress"` fera émerger un contenu plus utile pour le lecteur primaire.

---

## BRIEF E1 — OttoKit vs Zapier

### Métadonnées

| Champ | Valeur |
|---|---|
| **Slug** | `/ottokit-vs-zapier/` |
| **Mot-clé primaire** | `zapier wordpress` (20/mois FR, CPC 1,09 €) |
| **Mot-clé secondaire** | `ottokit vs zapier` (10/mois) |
| **Volume cumulé** | **30/mois** |
| **Intent** | comparative (commerciale) |
| **Longueur cible** | 2 000–2 500 mots (article phare) |
| **Pillar** | automatisation |
| **Objective** | formation + affiliation OttoKit Pro (CTA fort) |

### 1. Intent utilisateur réel

Quelqu'un qui tape `zapier wordpress` **utilise déjà Zapier** ou va y passer. Il cherche à connecter son WordPress à un outil externe et s'interroge sur l'app Zapier WP (limitée) ou sur des alternatives.

Public secondaire `ottokit vs zapier` : connaît les deux, prêt à basculer.

**Conséquence éditoriale :** pitch de l'économie (jusqu'à 4 000 $/an) + intégration WP native. On ne présuppose pas que le lecteur a déjà un compte OttoKit.

### 2. Angle schoolsWP

> **Promesse :** "Zapier est la référence mondiale mais pas pour WordPress. Voici pourquoi, et comment OttoKit peut te coûter 10 fois moins cher avec une meilleure intégration native WP."

Différenciation :
- Beaucoup de comparatifs Zapier existent en FR — mais **aucun ne prend l'angle WordPress first**.
- Angle prix **très frontal** : chiffrer l'économie annuelle sur un cas type.
- Garder une reconnaissance honnête de Zapier : **6 000+ apps**, écosystème imbattable hors WP.

### 3. Anti-angles (à éviter)

- "Zapier c'est has-been" — faux, leader de marché absolu.
- Oublier que Zapier a une intégration WP officielle.
- Masquer le fait qu'OttoKit a moins d'apps (1 300+ vs 6 000+).
- Clickbait titre ("Zapier killer"...).

### 4. Données à collecter avant rédaction

- [ ] Prix Zapier 2026 (Free, Starter, Professional, Team, Company — tiers et tâches)
- [ ] Prix OttoKit 2026 (Free, Pro tiers) + conversion EUR
- [ ] Simulation économie annuelle sur 3 profils (freelance 1 site, agence 5 sites, e-commerce moyen)
- [ ] App Zapier WordPress officielle : triggers et actions disponibles, limitations
- [ ] Nombre d'apps réelles : Zapier 6 000+ (à jour ?), OttoKit 1 300+ (à jour ?)
- [ ] UX : Zapier editor linéaire vs OttoKit Canvas (capture récente des deux)

### 5. Plan H2/H3 détaillé

```
H1 : OttoKit vs Zapier : lequel choisir pour WordPress en 2026 ?

H2. Verdict en 30 secondes
  (tableau + verdict en 3 lignes selon profil)

H2. Zapier : le leader mondial, mais pas conçu pour WordPress
  H3. L'app Zapier WordPress officielle
  H3. Ce qu'elle peut et ne peut pas
  H3. Pourquoi c'est souvent frustrant

H2. OttoKit : pensé par et pour WordPress
  H3. Déclencheurs natifs WP (post, user, WooCommerce...)
  H3. 1 300+ intégrations externes
  H3. Interface Canvas visuelle

H2. Nombre d'intégrations : où Zapier écrase encore
  (tableau des catégories d'apps)
  H3. Les 500 apps qu'OttoKit n'a pas (et si ça te concerne)
  H3. Les WP-spécifiques qu'OttoKit a et Zapier n'a pas

H2. Prix : la grande différence
  H3. Zapier : facturation à la tâche avec tiers très segmentés
  H3. OttoKit : pricing simple, tâches généreuses
  H3. Simulation sur 1 an — freelance
  H3. Simulation sur 1 an — agence (5 sites)
  H3. Simulation sur 1 an — e-commerce moyen
  H3. Économie potentielle : jusqu'à 4 000 $/an

H2. Interface et prise en main
  H3. Zapier editor
  H3. OttoKit Canvas
  H3. Courbe d'apprentissage

H2. Performance et fiabilité
  H3. Cloud Zapier (data centers US/EU)
  H3. Cloud OttoKit
  H3. Uptime, latence, support

H2. Cas où Zapier reste la meilleure option
  (apps exotiques, enterprise, conformité SOC2, volume énorme)

H2. Cas où OttoKit est le bon choix
  (freelances, agences WP, e-commerçants WooCommerce, LMS)

H2. Peut-on faire la transition Zapier vers OttoKit ?
  H3. Check-list de migration
  H3. Pièges à éviter

H2. Verdict schoolsWP

H2. FAQ (schema FAQPage)
  - Zapier est-il meilleur qu'OttoKit ?
  - Combien coûte Zapier pour WordPress en 2026 ?
  - OttoKit peut-il remplacer Zapier entièrement ?
  - Comment migrer mes Zaps vers OttoKit ?
  - Quel est le plus simple à utiliser ?
```

### 6. Meta draft

- **Title** (≤ 60 car) : `OttoKit vs Zapier : lequel choisir pour WordPress`
- **Meta description** (≤ 155 car) : `Zapier domine mondialement, OttoKit domine sur WordPress. Comparatif prix, intégrations et simulation d'économie annuelle par profil.`

### 7. Maillage interne

- **Liens entrants** (à créer/vérifier) : P0 (section comparatifs), E2, E3, E4, A4 (Gratuit vs Pro).
- **Liens sortants** : P0, A4, E2, E3, E4, F1.
- **Ancres suggérées** : "guide OttoKit", "OttoKit vs n8n", "OttoKit vs Make", "formation OttoKit".

### 8. CTA / Affiliation

- **CTA principal** : F1 formation (en milieu d'article, après la simulation d'économie).
- **Affiliation OttoKit Pro** : dans le tableau de prix + en fin d'article + bouton "Essayer OttoKit gratuitement".
- **Page la plus conversion-critique de la phase 2** — densité CTA supérieure aux 2 autres briefs (2 CTA internes + 2 liens affiliés max).

### 9. Commande de production

```
brain.bat --keyword "ottokit vs zapier" --intent comparative --pillar automatisation --objective formation --include-serp --include-ner
```

*Note :* `--include-ner` recommandé sur E1 pour couverture entité (6 000+ apps Zapier, tiers de prix, intégrations WooCommerce...).

---

## Ordre de production recommandé

1. **E3 — vs Uncanny Automator** (80/mois, CPC 3,11 € = top ROI)
2. **E4 — vs n8n** (80/mois, intent WP technique)
3. **E1 — vs Zapier** (30/mois mais **article phare** — conversion + longévité)

**Pourquoi cet ordre ?** E3 et E4 sont les quick wins SEO (volume + concurrence FR faible). E1 est plus long à produire (2 500 mots + 3 simulations de prix) mais amortit mieux côté conversion car c'est le comparatif le plus recherché long terme (intent transactionnel).

**Interne / externe :** pendant que tu produis E3, tu peux pré-collecter les données E4 (prix VPS, pricing n8n Cloud). Même chose entre E4 et E1 pour les prix Zapier.

---

## Ce qui n'est PAS dans ces briefs

- Images, screenshots, captures UX à produire séparément (pipeline `wp-image-metadata-seo` + `wp-media-upload`).
- Metadata JSON-LD Article/FAQPage — généré à l'étape publication.
- Maillage retour (liens depuis P0, A4, C1, etc. vers E1/E3/E4) — à ajouter lors de la mise à jour des pages sources.
- Traductions EN — à arbitrer après l'audit DataForSEO EN (cf. décision cocon : "Relancer un audit DataForSEO en EN pour justifier (ou non) une double version via WPML").
