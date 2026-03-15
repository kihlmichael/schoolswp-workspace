# Skill : gsc-opportunity-scanner

## Utilité

Analyser les exports GSC pour identifier les opportunités de trafic prioritaires : pages à CTR faible, positions 8-20, cannibalisations.

## Tâches concernées

- T3 (Analyse GSC) — usage principal

## Déclenchement

Utiliser ce skill quand :

- Des exports GSC CSV sont disponibles (Pages + Requêtes)
- On veut prioriser les interventions SEO par impact trafic réel
- On cherche des cannibalisations entre pages

## Processus

### Étape 1 — Segmentation des opportunités

**Type A — CTR faible malgré impressions**

- Condition : impressions > 500 ET ctr < 0.03 (3%)
- Diagnostic : title/meta non optimisé pour la requête
- Action : réécrire le title + meta description

**Type B — Pages en positions 8-20**

- Condition : position entre 8.0 et 20.0
- Diagnostic : contenu proche du Top 3 mais pas suffisamment fort
- Action : renforcer le contenu + améliorer le maillage interne entrant

**Type C — Cannibalisation**

- Condition : même requête génère des impressions sur 2+ URLs différentes
- Diagnostic : deux pages ciblent le même mot-clé
- Action : fusionner / définir une page canonique / améliorer la différenciation

**Type D — Pages sans impressions**

- Condition : page dans l'inventaire mais 0 impression sur 12m
- Diagnostic : page non indexée ou non pertinente
- Action : vérifier indexation via GSC Coverage

### Étape 2 — Scoring des opportunités

Score = (impressions / 1000) × (1 / ctr) × (1 / position)

Plus le score est élevé, plus l'opportunité est prioritaire.

### Étape 3 — Quick wins

Critères quick win :

- Type A avec impressions > 2000 et ctr < 2% → effort S, impact potentiel H
- Type B avec position 8-12 → effort M, impact H
- Type C avec requête à volume élevé → effort M, impact H

## Règles de preuve

- **Observable** : impressions, clics, CTR, position = données GSC réelles
- **À VALIDER** : volume exact de recherche (GSC = impressions filtrées, pas volume total)
- **À VALIDER** : impact réel d'une réécriture de title sur le CTR (tester, mesurer à 28j)
- Ne jamais extrapoler de trafic hors des données GSC fournies

## Format de sortie

JSON : `url, query, impressions, clics, ctr, position, type_opportunite, action, score, priority`

## Limites

- GSC ne montre que les requêtes avec ≥1 clic ou impression récente — les requêtes sans données sont invisibles
- CTR GSC inclut les rich snippets (peut biaiser la comparaison avec des pages normales)
- Cannibalisation confirmée uniquement si 2+ URLs ont des impressions sur la même requête dans la même période
