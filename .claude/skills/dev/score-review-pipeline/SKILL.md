---
name: score-review-pipeline
description: |
  Use when designing a CLI-driven data pipeline qui ingère un corpus, score chaque item
  selon plusieurs critères déterministes, sort une liste haute confiance et une file de
  review humaine pour les cas ambigus. Pattern dérivé du repo spoti-bye (Alex Hillman)
  applicable au scoring de cocons SEO, qualification de leads FluentCRM, audit batch
  d'articles publiés, ou tout pipeline ingest -> score -> review -> action. Déclenche
  pour : "scoring multi-critères", "pipeline ingest + review", "CLI + SQLite + scoring",
  "comment industrialiser le tri de X items", "filtrer un batch avec review humaine".
---

# Score-Review Pipeline

Pattern d'architecture pour transformer un corpus en décisions tranchables, sans LLM dans la boucle critique. Origine : [alexknowshtml/spoti-bye](https://github.com/alexknowshtml/spoti-bye) (migration playlists Spotify -> YouTube, Bun + bun:sqlite + yt-dlp).

**Idée centrale** : 4 commandes CLI, 1 base SQLite locale, scoring déterministe avec signaux positifs/négatifs, threshold configurable, file JSON pour review humaine sur les cas borderline, action finale sur les items confirmés.

---

## Quand utiliser

✅ **Use cases qui matchent** :

- Tu as un corpus (URLs, leads, mots-clés, articles, contacts) à trier en 3 buckets : keep / review / reject.
- Le scoring est explicable (signaux pondérés, pas un modèle ML).
- Le pipeline est rejouable (idempotent, dry-run dispo).
- Une décision humaine doit pouvoir trancher les cas ambigus.
- Le résultat alimente une action (publication, contact, refresh, suppression).

❌ **Quand NE PAS l'utiliser** :

- Tu veux du temps réel (ce pattern est batch, pas streaming).
- Le scoring nécessite un LLM par item (use case agent, pas ce pattern).
- Une seule commande suffit (alors c'est un script, pas un pipeline).
- Pas de notion de review humaine envisageable (alors le pattern perd sa valeur).

---

## Pattern en 4 étapes

```
sync     ->   resolve    ->   review     ->   action
ingest        scoring         human           apply
to DB         + buckets       decision        decision
```

### 1. Sync (ingest)

- Lit la source (CSV, API, GSC export, FluentCRM list).
- Upsert SQLite : `COALESCE` pour ne JAMAIS écraser un champ déjà résolu humainement.
- Idempotent : relancer ne casse rien, ne perd rien.

### 2. Resolve (scoring)

- Pour chaque item non résolu, score = somme pondérée de N signaux :
  - Signaux positifs (poids +)
  - Signaux négatifs (mots-clés exclus, poids fort)
  - Signaux contextuels (durée, popularité, récence, etc.)
- 3 buckets selon thresholds :
  - `score >= HIGH` -> confiance forte, marqué `resolved`
  - `LOW <= score < HIGH` -> file de review JSON
  - `score < LOW` -> `rejected`
- `--verbose` expose le score détaillé pour debug.
- `--dry-run` n'écrit rien.

### 3. Review (humain)

- Génère un JSON éditable : borderline + top 3-5 candidats par item.
- L'humain édite (choix manuel ou rejet définitif).
- Re-import met à jour la DB.

### 4. Action

- Filtre les `resolved` -> push vers la cible (API, fichier, publication).
- OAuth si nécessaire (token stocké hors DB).
- Logs détaillés, batch + delay configurables (rate-limiting friendly).

---

## Schéma SQLite type

```sql
CREATE TABLE items (
  id          TEXT PRIMARY KEY,        -- clé stable (URI, URL, email, keyword)
  source_data JSON NOT NULL,            -- payload brut depuis la source
  score       REAL,
  status      TEXT,                     -- pending | resolved | review | rejected
  resolved_id TEXT,                     -- ID cible (YouTube ID, post ID, contact ID)
  resolved_at INTEGER,
  metadata    JSON                      -- enrichissements réutilisables
);

CREATE TABLE batches (
  id         TEXT PRIMARY KEY,
  name       TEXT,
  created_at INTEGER
);

CREATE TABLE batch_items (
  batch_id  TEXT,
  item_id   TEXT,
  position  INTEGER,
  PRIMARY KEY (batch_id, item_id)
);
```

**Pourquoi `resolved_id` sur `items` (pas sur `batch_items`)** : un item résolu une fois est résolu pour TOUS les batches qui le contiennent. Énorme gain en pratique.

---

## Skills 1:1

Chaque commande CLI = sa skill Claude Code dédiée :

| Commande | Skill | Rôle |
| --- | --- | --- |
| `cli sync` | `<projet>-sync` | Ingest source -> DB |
| `cli resolve` | `<projet>-resolve` | Scoring + buckets |
| `cli review` | `<projet>-review` | Génération + import file review |
| `cli action` | `<projet>-action` | Push vers cible finale |

Optionnel : skill méta `<projet>-pipeline` qui orchestre les 4.

---

## Application schoolsWP : audit batch articles publiés

Use case concret. Auditer les articles schoolswp.com pour décider `keep / refresh / merge / unpublish`.

| Étape | Implémentation |
| --- | --- |
| **sync** | Pull GSC analytics (90j) via `gsc-mcp` + Publish Score archivé -> SQLite local. |
| **resolve** | Score = f(impressions, CTR, position, age, publish_score). Signaux + : impressions > 500/mois, CTR > 3%, position < 20. Signaux - : 0 impression sur 90j, position > 80, slug doublon. Buckets : `keep` (haut), `refresh` (intermédiaire -> review), `unpublish` (signaux - cumulés). |
| **review** | JSON éditable avec action proposée + 3 articles candidats à merger si doublon. |
| **action** | `refresh` -> relance `brain.bat` sur le keyword. `unpublish` -> 301 vers parent + WP REST update. `merge` -> consolidation manuelle. |

Pattern transposable à : cocon scoring (radar + DataForSEO), qualification leads FluentCRM, priorisation backlinks à demander.

---

## Anti-patterns

| ❌ Faux ami | ✅ Bon réflexe |
| --- | --- |
| LLM dans le scoring | Scoring déterministe, LLM seulement en review humaine |
| Scoring opaque (boîte noire) | Chaque signal nommé + pondéré + traçable via `--verbose` |
| Pas de file review (tout auto) | Toujours prévoir le bucket intermédiaire |
| Action irréversible sans dry-run | `--dry-run` partout, par défaut sur les commandes destructives |
| Réécrire la DB à chaque sync | Upsert + COALESCE pour préserver le travail humain |
| Multi-stack inutile (Postgres + Redis) | SQLite local suffit < 100k items |

---

## Stack recommandée pour schoolsWP

- **Python** + `sqlite3` (stdlib) ou `sqlmodel` (typage)
- CLI via `argparse` ou `typer`
- Pattern dans `tools/<projet>/` ou agent dans `core/agents-py/<projet>/cli.py`
- Logs via `logging.getLogger("agents.<projet>")` (rotation déjà configurée)

Skills complémentaires : `cluster-cocon-automatique` (un cluster), `brain-autonome` (priorisation editorial site-wide), `radar` agent (signaux SEO bruts).
