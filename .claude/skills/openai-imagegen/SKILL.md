---
name: openai-imagegen
description: Génération d'images en batch via l'API OpenAI Images. Échantillonneur de prompts aléatoires + galerie `index.html`.
homepage: https://platform.openai.com/docs/api-reference/images
metadata: {"openclaw":{"emoji":"🖼️","requires":{"bins":["python3"],"env":["OPENAI_API_KEY"]},"primaryEnv":"OPENAI_API_KEY","install":[{"id":"python-brew","kind":"brew","formula":"python","bins":["python3"],"label":"Installer Python (brew)"}]}}
---

# OpenAI Image Gen

Génère une série de prompts "aléatoires mais structurés" et les rend via l'API OpenAI Images.

## Exécution

```bash
python3 {baseDir}/scripts/gen.py
open ~/Projects/tmp/openai-image-gen-*/index.html  # si ~/Projects/tmp existe ; sinon ./tmp/...
```

Options utiles :

```bash
# Modèles GPT image avec diverses options
python3 {baseDir}/scripts/gen.py --count 16 --model gpt-image-1
python3 {baseDir}/scripts/gen.py --prompt "photo studio ultra-détaillée d'un homard astronaute" --count 4
python3 {baseDir}/scripts/gen.py --size 1536x1024 --quality high --out-dir ./out/images
python3 {baseDir}/scripts/gen.py --model gpt-image-1.5 --background transparent --output-format webp

# DALL-E 3 (note : count est automatiquement limité à 1)
python3 {baseDir}/scripts/gen.py --model dall-e-3 --quality hd --size 1792x1024 --style vivid
python3 {baseDir}/scripts/gen.py --model dall-e-3 --style natural --prompt "paysage de montagne serein"

# DALL-E 2
python3 {baseDir}/scripts/gen.py --model dall-e-2 --size 512x512 --count 4
```

## Paramètres spécifiques aux modèles

Différents modèles supportent différentes valeurs de paramètres. Le script sélectionne automatiquement les défauts appropriés selon le modèle.

### Taille

- **Modèles GPT image** (`gpt-image-1`, `gpt-image-1-mini`, `gpt-image-1.5`) : `1024x1024`, `1536x1024` (paysage), `1024x1536` (portrait), ou `auto`
  - Défaut : `1024x1024`
- **dall-e-3** : `1024x1024`, `1792x1024`, ou `1024x1792`
  - Défaut : `1024x1024`
- **dall-e-2** : `256x256`, `512x512`, ou `1024x1024`
  - Défaut : `1024x1024`

### Qualité

- **Modèles GPT image** : `auto`, `high`, `medium`, ou `low`
  - Défaut : `high`
- **dall-e-3** : `hd` ou `standard`
  - Défaut : `standard`
- **dall-e-2** : `standard` uniquement
  - Défaut : `standard`

### Autres différences notables

- **dall-e-3** ne supporte que la génération d'1 image à la fois (`n=1`). Le script limite automatiquement count à 1 lors de l'utilisation de ce modèle.
- **Modèles GPT image** supportent des paramètres additionnels :
  - `--background` : `transparent`, `opaque`, ou `auto` (défaut)
  - `--output-format` : `png` (défaut), `jpeg`, ou `webp`
  - Note : `stream` et `moderation` sont disponibles via API mais pas encore implémentés dans ce script
- **dall-e-3** a un paramètre `--style` : `vivid` (hyper-réel, dramatique) ou `natural` (aspect plus naturel)

## Sortie

- Images `*.png`, `*.jpeg`, ou `*.webp` (format de sortie dépend du modèle + `--output-format`)
- `prompts.json` (mapping prompt → fichier)
- `index.html` (galerie de miniatures)
