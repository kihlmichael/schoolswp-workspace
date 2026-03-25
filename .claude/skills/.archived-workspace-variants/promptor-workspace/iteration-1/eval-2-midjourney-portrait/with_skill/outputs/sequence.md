# Eval 2 — Midjourney portrait (new_skill v2.1)

## Calibrage Midjourney V7

| Caractéristique | Pourquoi c'est important | Comment l'appliquer |
|---|---|---|
| Sujet précis | V7 comprend mieux "35-45 years old, confident posture" que "homme d'affaires" | Décrire l'âge, posture, expression |
| Style visuel ancré | "Magazine économique" est trop vague | "Forbes editorial portrait", "HBR cover style" |
| Éclairage spécifié | Définit 50% de l'ambiance pro | "soft window light from left", "rembrandt-style shadow" |
| Référence caméra | Améliore fortement le réalisme | "shot on Sony A7R V, 85mm f/1.8" |
| Fond cohérent | LinkedIn = fond qui ne distrait pas | "soft bokeh blurred background" |
| `--ar 4:5` | Format portrait vertical LinkedIn | |
| `--s 150` | Réalisme pro sans sur-artistifier | |
| `--exp 15` | Détails fins (peau, tissu, yeux) — sweet spot 10-25 | |
| `--chaos 0` | Cohérence des 4 variations — indispensable pour usage pro | |

---

## Itération 1 — 20/25

```
/imagine French tech entrepreneur, male, confident subtle smile, dark suit, modern office background, editorial portrait photography, soft window light, shot on Canon EOS R5 85mm f/1.4, sharp focus on eyes, Forbes magazine style, professional LinkedIn headshot --ar 4:5 --s 150 --exp 15
```

Lacunes identifiées :
- Âge non spécifié
- Couleur dominante absente
- `--chaos 0` manquant (risque de variations incohérentes)
- Fond trop générique
- Type de lumière trop vague

---

## Prompt final — 25/25

```
/imagine French tech entrepreneur, male, 35-45 years old, confident subtle smile, dark navy suit no tie open collar, standing in modern glass office building, soft bokeh blurred background, editorial portrait photography, soft window light from left with studio fill, rembrandt-style shadow, shot on Sony A7R V 85mm f/1.8 lens, sharp focus on eyes, Forbes magazine cover portrait, cool blue-grey tones, professional LinkedIn headshot quality --ar 4:5 --s 150 --exp 15 --chaos 0
```

## Grille d'évaluation finale

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 5/5 | Âge, genre, expression, tenue — aucune ambiguïté |
| Spécificité | 5/5 | Éclairage nommé, caméra/objectif précis, couleurs, `--chaos 0` |
| Structure | 5/5 | Subject → Posture → Environment → Lighting → Camera → Style → Color → Params |
| Contexte | 5/5 | Toutes les dimensions visuelles couvertes |
| Actionnable | 5/5 | `--chaos 0` + `--exp 15` + format `4:5` — prêt à coller dans Midjourney |
| **TOTAL** | **25/25** | Prompt parfait — 2 itérations |
