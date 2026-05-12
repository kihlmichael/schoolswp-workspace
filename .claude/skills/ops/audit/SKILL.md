---
name: audit
description: |
  Lance `publish_ready.cli` sur un article pour calculer le Publish Score (SEO 0.30 + LLM 0.25 + Conversion 0.25 + Autorité 0.20). Quatre audits parallèles, sortie chiffrée avec recommandations de réécriture si <70.
  Utilise ce skill quand l'utilisateur dit : "audit", "publish score", "prêt à publier", "auditer l'article", "score de publication", ou veut savoir si un .md de `content/articles/` est publiable.
  NE PAS utiliser pour : audit SEO seul d'un fichier sans cross-check LLM/Conversion (utiliser `seo-auditor.cli` direct), audit code/dette technique (utiliser `code-audit`), ou audit GSC/positions (utiliser le système `content/audits/`).
---

# /audit — Audit de publication (4 audits parallèles)

Lance `publish_ready.cli` sur un fichier article.

Arguments : `$ARGUMENTS`
- Si un fichier `.md` est fourni en argument, l'utiliser directement.
- Sinon, chercher le fichier `.md` le plus récent dans `content/articles/` et demander confirmation.
- Le keyword doit être fourni ou déduit du nom du fichier/dossier.

Commande à exécuter depuis `projects/schoolswp/` :

```bash
.venv/Scripts/python -m agents.publish_ready.cli --file "$FILE" --keyword "$KEYWORD"
```

Résultat : Publish Score = SEO×0.30 + LLM×0.25 + Conversion×0.25 + Autorité×0.20
- ≥90 → publication immédiate
- 80-89 → ajustements mineurs
- 70-79 → révision ciblée
- <70 → réécriture
