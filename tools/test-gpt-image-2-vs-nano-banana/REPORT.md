# Test A/B GPT Image (OpenAI) vs Nano Banana (Gemini) — schoolsWP

**Date** : 2026-05-08
**Engines testés** :
- `gpt-image-1` (fallback : `gpt-image-2` requiert vérification d'organisation OpenAI, KYC photo + ID)
- `gemini-2.5-flash-image` (Nano Banana, déjà notre défaut)

**Coût réel** : ~$0.21 OpenAI + $0 Nano Banana (free tier).
**Latence** : OpenAI 15-22 s / image vs Nano Banana 5-7 s / image (3-4× plus rapide).

---

## Verdict global

| Critère | Cas 1 - Texte | Cas 2 - Cohérence | Cas 3 - Brand | Verdict engine |
|---|---|---|---|---|
| Texte propre | gpt-image-1 ✅ | gpt-image-1 ✅ | n/a | gpt-image-1 |
| Cohérence cross-image | n/a | **les deux fail** | n/a | non concluant |
| Fidélité au brief | gpt-image-1 ✅ | match | gpt-image-1 ✅ | gpt-image-1 |
| Brand vert respecté | gpt-image-1 ✅ | match | match | gpt-image-1 léger |
| Esthétique | gpt-image-1 4/5 | gpt-image-1 4/5 | gpt-image-1 4/5 | gpt-image-1 |
| Coût/image | ~$0.05 | n/a | ~$0.05 | Nano Banana ($0) |
| Vitesse | 20 s | 18 s | 22 s | Nano Banana (5 s) |

---

## Cas 1 — Miniature article schoolsWP avec texte intégré

**Prompt synthèse** : titre "FluentCRM : 1 an après" + sous-titre "Le CRM qui rentabilise" + accent vert schoolsWP, 16:9.

| Engine | Verdict | Détail |
|---|---|---|
| gpt-image-1 | ✅ **Gagnant net** | Titre parfait avec accent grave correct. Kerning clean, hiérarchie respectée. Illustration enveloppes/dashboard cohérente. Brand vert en accents typo. |
| Nano Banana | ❌ | **Typo "apprès"** (double-p). Texte mou, taille incohérente, hiérarchie cassée. |

**Implication schoolsWP** : pour les miniatures YouTube, vignettes article et carrousels avec texte critique, OpenAI domine. Nano Banana ne tient pas sa parole sur l'orthographe FR (cohérent avec la mémoire `feedback_gemini_hex_color_text_rendering.md` étendue).

---

## Cas 2 — Carrousel LinkedIn 2 slides (cohérence cross-image)

**Prompt synthèse** : même perso (35 ans, barbe courte, hoodie charcoal) sur 2 slides avec poses différentes.

| Engine | Slide 1 | Slide 2 | Cohérence | Verdict |
|---|---|---|---|---|
| gpt-image-1 | "LE FONDATEUR – EPISODE 1" net, badge "S" vert | "Episode 2 – La réalité" net, badge "schools..." vert | ⚠️ Visages **différents** (jeune homme rond vs homme plus mature) | Texte OK, perso fail |
| Nano Banana | "Le Fondauter - Episode 1" (typo Fondauter), badge "schoolsWP" complet vert | "Episode 2 - La réalité" net, badge "schoolsWP" complet vert | ⚠️ Visages **différents** | Texte mixed, perso fail |

**Implication schoolsWP** : le test single-shot ne permet pas la cohérence. La vraie cohérence cross-image promise par GPT Image 2 nécessite **le mode multi-image natif** (référencer l'image 1 dans la requête 2). Ce mode requiert la vérification d'organisation OpenAI.

**Test non concluant** : à refaire après KYC OpenAI sur le mode multi-image dédié.

---

## Cas 3 — Illustration commerciale brand (workflow 3 nodes)

**Prompt synthèse** : 3 nodes left-to-right (CRM → WP dashboard → cours), connections vertes pulse.

| Engine | Verdict | Détail |
|---|---|---|
| gpt-image-1 | ✅ Fidèle au brief | Composition 16:9 respectée, 3 nodes alignés, **logo W WordPress reconnaissable** sur node central, connection lines vertes en pulse, fond off-white avec subtle grid. Brand vert en accents (un peu pâle vs "vibrant grass green" demandé). |
| Nano Banana | ⚠️ Joli mais hors brief | Ratio carré au lieu de 16:9, lines en heartbeat ECG (pas pulse), node 2 sans logo WordPress, style 3D iconique au lieu de flat. Brand vert en accent ECG, plus vif que gpt-image-1. |

**Implication schoolsWP** : pour illustration éditoriale d'article (workflow, comparatifs, schémas), gpt-image-1 plus discipliné. Nano Banana plus jouable pour des décorations vives mais moins prédictible sur les contraintes structurelles.

---

## Décision recommandée

**Court terme (sans KYC OpenAI)** :
- Garder Nano Banana en défaut pour génération volume (logos plats, avatars solides, décorations sans texte critique). 0 $ et rapide.
- Utiliser **gpt-image-1** ponctuellement pour les visuels avec **texte intégré FR** (miniatures YouTube, vignettes article, carrousels avec headline). ~$0.05/image medium quality acceptable pour des assets utilisés des centaines de fois.

**Moyen terme (faire la vérification d'organisation OpenAI)** :
- Démarche : [platform.openai.com/settings/organization/general](https://platform.openai.com/settings/organization/general), bouton "Verify Organization", upload pièce d'identité + selfie. ~5 min, 15 min de propagation.
- Bénéfices au-delà de gpt-image-2 : accès aux modèles avancés (`o1-pro`, `gpt-image-1.5`, `gpt-image-2-2026-04-21`), au mode **multi-image consistency** (vrai test cross-image cohérent), et aux features qualité haute (`high` quality au lieu de `medium`).
- Refaire alors le cas 2 avec mode multi-image pour valider la promesse cohérence.

**Action prompts** :
- Le repo `awesome-gpt-image-2` contient des prompts JSON structurés (slot-fillable) qui marchent mieux que les prompts texte libre. Modèle à adopter pour nos prompts schoolsWP critiques (cf. cas 6 "Infographie escalier 3D" avec layout strict).

---

## Prochaines étapes possibles

1. **Tu fais la KYC OpenAI** → je relance le cas 2 en mode multi-image GPT Image 2 vrai pour trancher la cohérence cross-image définitivement.
2. **On adopte gpt-image-1 pour les miniatures YouTube** → adaptation de `tools/generate_telegram_avatars.py` pattern pour basculer entre les 2 engines selon le cas (variable `IMAGE_ENGINE=openai|gemini`).
3. **On ignore et on reste 100% Nano Banana** → si le ratio coût/bénéfice OpenAI ne te convainc pas pour l'usage schoolsWP réel.

Outputs visuels et meta dans `outputs/<case>/` pour archive.
