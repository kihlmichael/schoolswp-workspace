# Visual Prompts — ThriveCart (iteration 2)

## Angle 1 : Hero (consolidation)

```
Flat isometric illustration of a freelance web developer workspace with a single laptop screen showing a unified checkout dashboard. Dark background color #12111F, bright green accent elements color #00D400, magenta subtle highlights color #E668D4. Minimalist style, no text overlay, no human faces visible. Central composition: laptop displays a simplified checkout form with a green Pay button. Around the laptop float 5 small flat icons (shopping cart, envelope, bar chart, graduation cap, chain link) connected by thin lines merging into the laptop, representing tool consolidation. Professional modern SaaS illustration, generous whitespace, clean vector look. No stock photography aesthetic, no purple AI gradients.
```

**Commande** :
```bash
"D:/VS Code/CLAUDE CODE/projects/schoolswp/.venv/Scripts/python" -c "
import openai, base64, pathlib
client = openai.OpenAI()
result = client.images.generate(model='gpt-image-1', prompt='Flat isometric illustration of a freelance web developer workspace with a single laptop screen showing a unified checkout dashboard. Dark background color #12111F, bright green accent elements color #00D400, magenta subtle highlights color #E668D4. Minimalist style, no text overlay, no human faces visible. Central composition: laptop displays a simplified checkout form with a green Pay button. Around the laptop float 5 small flat icons (shopping cart, envelope, bar chart, graduation cap, chain link) connected by thin lines merging into the laptop, representing tool consolidation. Professional modern SaaS illustration, generous whitespace, clean vector look. No stock photography aesthetic, no purple AI gradients.', n=1, size='1536x1024', quality='high')
outdir = pathlib.Path('D:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/skills/landing-page-factory/-workspace/iteration-2/eval-thrivecart/outputs/images/angle-1')
outdir.mkdir(parents=True, exist_ok=True)
(outdir / 'hero-consolidation.png').write_bytes(base64.b64decode(result.data[0].b64_json))
print('Done: hero-consolidation.png')
"
```

## Angle 2 : Hero (funnel)

```
Flat isometric illustration of a sales funnel mechanism on dark background color #12111F. Three connected descending platforms forming a funnel: Top platform in bright green #00D400 shows a simple product box icon. Middle platform in magenta #E668D4 shows an upward arrow icon representing upsell. Bottom platform in bright green #00D400 shows a growing bar chart icon representing increased revenue. Clean geometric connecting lines between platforms. No text, no human faces. Minimalist modern tech illustration style, generous spacing, professional. No stock photography, no purple AI gradients, no photorealistic elements.
```

**Commande** :
```bash
"D:/VS Code/CLAUDE CODE/projects/schoolswp/.venv/Scripts/python" -c "
import openai, base64, pathlib
client = openai.OpenAI()
result = client.images.generate(model='gpt-image-1', prompt='Flat isometric illustration of a sales funnel mechanism on dark background color #12111F. Three connected descending platforms forming a funnel: Top platform in bright green #00D400 shows a simple product box icon. Middle platform in magenta #E668D4 shows an upward arrow icon representing upsell. Bottom platform in bright green #00D400 shows a growing bar chart icon representing increased revenue. Clean geometric connecting lines between platforms. No text, no human faces. Minimalist modern tech illustration style, generous spacing, professional. No stock photography, no purple AI gradients, no photorealistic elements.', n=1, size='1536x1024', quality='high')
outdir = pathlib.Path('D:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/skills/landing-page-factory/-workspace/iteration-2/eval-thrivecart/outputs/images/angle-2')
outdir.mkdir(parents=True, exist_ok=True)
(outdir / 'hero-funnel.png').write_bytes(base64.b64decode(result.data[0].b64_json))
print('Done: hero-funnel.png')
"
```
