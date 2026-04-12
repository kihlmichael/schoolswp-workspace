# schoolsWP CTR TDD Tracker — Template Google Sheets

Template de suivi des tests CTR avec logique TDD. Documenter chaque test, isoler la variable, mesurer l'impact, itérer.

---

## Onglet 1 — Tests CTR

| Colonne             | Description                         |
| ------------------- | ----------------------------------- |
| Date test           | Date de lancement du test           |
| URL                 | Page testée                         |
| Keyword principal   | Mot-clé cible                       |
| Position (avant)    | Position GSC avant le test          |
| CTR (avant)         | CTR GSC avant le test               |
| Impressions (avant) | Impressions GSC avant le test       |
| Title initial       | Title avant modification            |
| Meta initiale       | Meta description avant modification |
| Variable testée     | Title OU Meta (jamais les deux)     |
| Nouvelle version    | La nouvelle valeur testée           |
| Position (après)    | Position GSC après 14-21 jours      |
| CTR (après)         | CTR GSC après 14-21 jours           |
| Impressions (après) | Impressions GSC après 14-21 jours   |
| Verdict             | Concluant / Neutre / Négatif        |
| Prochaine action    | Ce qu'on fait ensuite               |

**Exemple de ligne :**

| 2026-03-13 | /maintenance-wordpress/ | maintenance wordpress | 7.1 | 3.2% | 3 200 | Maintenance WordPress : guide complet | … | Title | Maintenance WordPress : guide complet (+ checklist) | 7.3 | 4.8% | 3 500 | Concluant | Conserver + tester meta |

**Règles :**

- Variable testée : Title OU Meta — jamais les deux en même temps
- Observation : 14 à 21 jours minimum
- Verdict : Concluant / Neutre / Négatif

---

## Onglet 2 — Quick Wins

Filtre les pages à potentiel (export GSC sur 90 jours).

| URL                     | Keyword               | Position | Impressions | CTR  | CTR cible | Score opportunité | Priorité |
| ----------------------- | --------------------- | -------- | ----------- | ---- | --------- | ----------------- | -------- |
| /maintenance-wordpress/ | maintenance wordpress | 7.1      | 5 000       | 2.5% | 8%        | 275               | Haute    |

**Formule Score opportunité (Google Sheets) :**

```text
=Impressions * (CTR_cible - CTR_actuel)
```

Si le CTR est en pourcentage (ex : 2.5% en colonne E, CTR cible en F) :

```text
=E2 * (F2 - D2)
```

**Critères de détection quick wins :**

- Position : 3 → 12
- Impressions : > 500
- CTR : < 3 %

---

## Onglet 3 — Variantes Titles

| URL                     | Keyword               | Title A                     | Title B            | Title C        | Title D                 | Title E        | Title testé |
| ----------------------- | --------------------- | --------------------------- | ------------------ | -------------- | ----------------------- | -------------- | ----------- |
| /maintenance-wordpress/ | maintenance wordpress | Guide complet (+ checklist) | 7 erreurs à éviter | Méthode simple | Checklist indispensable | Routine simple | B           |

**But :** générer 5 variantes minimum, en tester une seule à la fois.

---

## Routine hebdomadaire (30 min)

1. Exporter les données GSC (90 jours) → Onglet Quick Wins
2. Identifier 1 page prioritaire (score opportunité le plus élevé)
3. Générer 5 variantes de title (prompt CTR Title Generator)
4. Lancer 1 test TDD
5. Revenir 14-21 jours plus tard → noter le résultat → décider

---

## Interprétation des résultats

| Situation                | Action                              |
| ------------------------ | ----------------------------------- |
| CTR ↑ et position stable | Conserver le title — tester la meta |
| CTR ↑ et position ↑      | Très bon signal — scaler l'approche |
| CTR stable               | Tester un angle différent           |
| CTR ↓                    | Revenir au title précédent          |

**Toujours analyser les 3 métriques ensemble :**

- CTR
- Position moyenne
- Impressions

Ne jamais interpréter le CTR seul — une baisse d'impressions peut fausser la lecture.
