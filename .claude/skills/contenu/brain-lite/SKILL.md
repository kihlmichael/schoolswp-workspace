---
name: brain-lite
description: |
  Lance le pipeline brain-lite (5 étapes, sans NER/SERP) via `brain-lite.bat`. Produit stratégie → article → audit SEO → cluster, output sauvegardé dans `content/articles/`. Pipeline rapide pour drafts.
  Utilise ce skill quand l'utilisateur dit : "brain-lite", "pipeline simplifié", "article rapide", "brain lite", "lance brain lite sur [keyword]", ou veut un draft article express sans la couche NER/SERP.
  NE PAS utiliser pour : pipeline complet avec NER/SERP/audits multi-couches (utiliser le `brain` complet via `brain.bat`), arbitrage éditorial multi-cocon (utiliser `brain-autonome`), ou production article SEO long brand-strict (utiliser `schoolswp-article-workflow` ou `thruuu-writer`).
---

# /brain-lite — Lance le pipeline brain-lite

Demande le keyword et l'intent si non fournis dans les arguments.

Puis exécute depuis `projects/schoolswp/` :

```bash
brain-lite.bat --keyword "$KEYWORD" --intent "$INTENT" --pilier "$PILIER"
```

Arguments attendus : `$ARGUMENTS`
- Parser : `--keyword` (obligatoire), `--intent` (informationnelle/commerciale/décisionnelle/comparative/navigationnelle), `--pilier` (optionnel)
- Si des arguments manquent, demande-les avant d'exécuter.

Le pipeline produit : stratégie → article → audit SEO → cluster (5 étapes, sans NER/SERP).
Output sauvegardé dans `content/articles/`.
