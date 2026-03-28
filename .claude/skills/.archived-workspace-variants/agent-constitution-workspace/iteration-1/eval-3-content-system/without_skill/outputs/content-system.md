# Système de contenu récurrent — schoolsWP

## Principe directeur : 1 idée, 3 formats

Chaque semaine part d'un seul sujet central. L'article SEO est la source primaire. La newsletter et le post LinkedIn en sont des dérivés. Tu écris une fois, tu distribues trois fois.

---

## Structure hebdomadaire

### Lundi — Choix du sujet (15 min)

Sélectionne le sujet de la semaine depuis ton plan éditorial ROI (`agents.roi_editorial_plan`).

Critères de sélection (dans l'ordre) :

1. Mot-clé avec volume + intent claire (décisionnelle > informationnelle)
2. Cohérence avec le pilier en cours (LMS, CRM, Freelance…)
3. Lien avec une question réelle reçue (email, commentaire, DM LinkedIn)

Documente dans un fichier `weekly-brief.md` :

```
- Sujet : [titre provisoire]
- Mot-clé cible : [keyword]
- Intent : [décisionnelle / informationnelle / comparative]
- Pilier : [LMS / CRM / Freelance / WP Business]
- Angle : [problème spécifique que ça résout pour le lecteur]
- Accroche LinkedIn : [1 phrase tension ou question]
- Fait ou chiffre clé à mettre en avant : [...]
```

---

### Mardi–Mercredi — Article SEO (production principale)

**Outil** : `brain.bat` ou `brain-lite.bat` selon profondeur souhaitée.

```bash
brain-lite.bat --keyword "..." --intent décisionnelle --pillar lms
```

Résultat attendu : article ≥1500 mots, structuré H2/H3, avec intro orientée intent, CTA utile, disclosure si affiliation.

**Règle branding** : vérifier les 5 critères Brand QA avant publication (Ton / Clarté / Valeurs / Interdits / Vocabulaire). Mots interdits : disruptif, scalable, hack, en un clic, il suffit de.

**Checklist avant mise en ligne** :

- [ ] Publish Score ≥ 80 (`agents.publish_ready`)
- [ ] Titre H1 contient le mot-clé
- [ ] Meta description rédigée (≤155 caractères)
- [ ] Maillage interne vers 1–2 articles du même pilier
- [ ] CTA en bas d'article (newsletter ou ressource)

---

### Jeudi — Newsletter FluentCRM (dérivé de l'article)

**Format** : email court (250–400 mots), pas un résumé — une extension ou un angle différent.

**Structure type** :

```
Objet : [Question ou tension — ex: "Tu penses que TutorLMS est trop cher ?"]

[Accroche 2-3 lignes — contexte ou observation terrain]

[Corps : 1 insight ou conseil concret que l'article développe mais ne donne pas tout]

[1 paragraphe "sur schoolsWP" — ce que tu as fait/testé/observé personnellement]

[CTA unique : lien vers l'article + 1 phrase d'invitation]

—
[Signature courte]
```

**Règles FluentCRM** :

- Segment : liste principale ou segment pilier si tu as segmenté par intérêt
- Heure d'envoi : jeudi 9h ou 17h (teste sur ta liste, retiens le meilleur)
- Objet A/B si ta liste dépasse 500 contacts
- Pas de CTA multiple — un seul lien principal

**Temps estimé** : 30–45 min en partant du draft article déjà écrit.

---

### Vendredi — Post LinkedIn (dérivé de l'article)

**Format** : post texte natif, 800–1500 caractères, sans lien dans le corps du post.

**Structure type** :

```
[Accroche ligne 1 — fait contre-intuitif, question ou tension]
[Ligne 2 — développe ou crée la curiosité]

[Corps — 3 à 5 points courts, ou mini-storytelling terrain]
[Chaque point = 1-2 lignes max]

[Conclusion — ton verdict ou recommandation directe]

[CTA discret : "L'article complet en commentaire" ou "Je détaille ça dans la newsletter"]
```

**Règles LinkedIn schoolsWP** :

- Tutoiement systématique
- Premier mot de chaque bloc = fort (verbe d'action ou chiffre)
- Pas de hashtags en bloc final — intégrés naturellement si utilisés (max 2-3)
- Lien en commentaire épinglé, pas dans le post
- Publier vendredi 8h–10h ou mardi 9h (selon ta fenêtre d'audience)

**Temps estimé** : 20–30 min.

---

## Vue calendrier type

| Jour      | Action                               | Durée estimée |
| --------- | ------------------------------------ | ------------- |
| Lundi     | Choix sujet + brief semaine          | 15 min        |
| Mardi     | Lancement `brain.bat` + review       | 45 min        |
| Mercredi  | Finalisation article + mise en ligne | 30 min        |
| Jeudi     | Rédaction + envoi newsletter         | 45 min        |
| Vendredi  | Rédaction + publication LinkedIn     | 30 min        |
| **Total** |                                      | **~2h45/sem** |

---

## Cohérence entre les 3 formats

| Élément        | Article SEO         | Newsletter           | LinkedIn             |
| -------------- | ------------------- | -------------------- | -------------------- |
| Sujet          | Complet, structuré  | 1 angle ou insight   | 1 tension ou verdict |
| Longueur       | 1500–3000 mots      | 250–400 mots         | 800–1500 caractères  |
| Ton            | Pédagogique/direct  | Proche/personnel     | Direct/terrain       |
| CTA            | Ressource ou outil  | Lien article         | Lien en commentaire  |
| Intent lecteur | Cherche à apprendre | Veut aller plus loin | Découvre le sujet    |

La règle : **jamais le même contenu copié-collé**. L'article prouve l'expertise, la newsletter crée la relation, LinkedIn attire de nouveaux lecteurs.

---

## Outillage recommandé

**Génération article** :

```bash
# Depuis projects/schoolswp/
brain-lite.bat --keyword "[mot-clé]" --intent [intent] --pillar [pilier]
# ou version complète avec SERP + NER :
brain.bat --keyword "[mot-clé]" --intent [intent] --pillar [pilier] --include-ner
```

**Audit avant publication** :

```bash
.venv/Scripts/python -m agents.publish_ready.cli --file content/articles/[fichier].md --keyword "[mot-clé]"
```

**Suivi pilier** :

```bash
.venv/Scripts/python -m agents.pillar_authority.cli --all
```

---

## Système de planification (suggestion minimaliste)

Un simple fichier `content/planning/weekly-log.md` avec une entrée par semaine :

```markdown
## Semaine 12 — 2026

- Sujet : TutorLMS vs LearnDash en 2026
- Mot-clé : tutor lms vs learndash
- Pilier : LMS
- Article : content/articles/lms/tutor-vs-learndash.md
- Publish Score : 84/100
- Newsletter envoyée : jeudi 20 mars, 9h
- LinkedIn publié : vendredi 21 mars, 8h30
- Notes : fort engagement LinkedIn (87 réactions) — relancer en cluster
```

Pas d'outil externe nécessaire pour démarrer. Notion ou Google Sheets si tu veux visualiser sur plusieurs semaines.

---

## Règles de maintenance

- **Mensuel** : relire les 4 articles publiés, identifier le meilleur performer, l'enrichir (maillage, données) — 1h.
- **Trimestriel** : relancer `agents.roi_editorial_plan` pour reprioriser le planning selon les résultats réels.
- **Si tu rates une semaine** : pas de rattrapage double. Tu décales juste d'une semaine. La régularité sur 3 mois vaut plus que l'intensité sur 2 semaines.
