# Exemple de sortie — Publish Score

**Article** : `content/articles/lms/tutor-lms-vs-learndash-comparatif.md`
**Mot-cle** : "tutor lms vs learndash"
**Intent** : comparative

---

## Scores d'audit

| Audit        | Score | Poids | Pondere |
| ------------ | ----- | ----- | ------- |
| SEO          | 82/100 | 0.30 | 24.6    |
| LLM          | 76/100 | 0.25 | 19.0    |
| Conversion   | 88/100 | 0.25 | 22.0    |
| Autorite     | 71/100 | 0.20 | 14.2    |

**Publish Score : 79.8/100**

---

## Verdict : Revision ciblee

Score entre 70 et 79 — l'article necessite des ajustements avant publication.

---

## Recommandations prioritaires

1. **SEO — Densite du mot-cle principal** : "tutor lms vs learndash" apparait 3 fois sur 2 800 mots. Viser 5-7 occurrences naturelles dans les H2, intro et conclusion.

2. **LLM — Structure citabilite** : ajouter un paragraphe de synthese en debut d'article (2-3 phrases) que les IA peuvent citer directement. Format "En resume, [verdict clair]."

3. **Autorite — Maillage interne insuffisant** : 2 liens internes detectes. Ajouter des liens vers la pillar page LMS (`/lms-wordpress/`) et le guide pricing (`/tarifs-lms-wordpress/`).

4. **Conversion — CTA absent en milieu d'article** : le seul CTA est en fin d'article. Inserer un bloc decision apres le tableau comparatif principal.

5. **SEO — Meta description** : meta actuelle (168 caracteres) depasse la limite. Raccourcir a 155 caracteres max avec le mot-cle en debut de phrase.

---

## Prochaines etapes

```bash
# Appliquer les corrections automatiques
.venv/Scripts/python -m agents.seo_auditor.cli --file content/articles/lms/tutor-lms-vs-learndash-comparatif.md --keyword "tutor lms vs learndash" --fix

# Relancer l'audit apres corrections
.venv/Scripts/python -m agents.publish_ready.cli --file content/articles/lms/tutor-lms-vs-learndash-comparatif.md --keyword "tutor lms vs learndash"
```
