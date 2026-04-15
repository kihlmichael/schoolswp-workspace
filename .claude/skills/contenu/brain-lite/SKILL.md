---
name: brain-lite
description: |
  Lance le pipeline brain-lite (5 étapes, sans NER/SERP). Produit stratégie → article → audit SEO → cluster.
  Déclenche pour "brain-lite", "pipeline simplifié", "article rapide", "brain lite".
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
