#!/usr/bin/env python3
import os

outdir = r"d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/skills/conversational-query-mapper-workspace/iteration-1/eval-crm-email-marketing/without_skill/outputs"
outpath = os.path.join(outdir, "result.md")

q = chr(8217)  # right single quote for French apostrophes

content = f"""# Carte des requetes conversationnelles IA -- CRM & Email Marketing WordPress

**Pilier** : CRM & Email Marketing WordPress
**Audience** : freelances WordPress, createurs de formations, e-commercants, agences
**Plateforme cible** : ChatGPT (et LLMs conversationnels)
**Date** : 2026-03-24

---

## Methodologie

Cette carte recense les questions que ton audience WordPress pose a ChatGPT autour du CRM et de l{q}email marketing. Les requetes sont classees par :

1. **Sous-theme** (aligne sur les piliers de contenu)
2. **Intent conversationnelle** (decouverte, comparaison, implementation, troubleshooting, optimisation)
3. **Segment d{q}audience** (freelance, formateur, e-commercant, agence)
"""

with open(outpath, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Written {{len(content)}} chars")
