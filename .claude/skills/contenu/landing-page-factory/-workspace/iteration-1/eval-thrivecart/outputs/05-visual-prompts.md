# Visual Prompts — ThriveCart

Les images n'ont pas ete generees (pas de cle OpenAI). Voici les prompts prets a utiliser.

Palette de reference : #1a1a2e (dark navy), #4f46e5 (indigo), #10b981 (vert), #f59e0b (jaune), #ffffff (blanc)

---

## Angle 1 : "Arrete de payer un abonnement mensuel"

### Hero Image
```
Flat illustration, clean modern style. Split screen comparison: left side shows a calendar with recurring red payment notifications stacking up month after month (labeled $99, $149), right side shows a single green checkmark with "$495 — done". Color palette: dark navy #1a1a2e background, indigo #4f46e5 accents, green #10b981 for the checkmark. Minimalist, no text, no people, no stock photo aesthetic. 1536x1024.
```

### Section Probleme — illustration
```
Isometric illustration of a freelancer's desk with 5 different software windows open, each showing a different billing notification. Scattered invoices. Feeling of overwhelm and tool fatigue. Color palette: muted tones, dark navy #1a1a2e, soft indigo #4f46e5 accents. Clean line art style, no gradients, no purple AI glow. 1200x800.
```

### Section Solution — mockup produit
```
Clean mockup of a ThriveCart checkout page displayed on a laptop screen, sitting on a minimal desk. The checkout shows a product at $97 with an order bump checkbox. Professional, branded feel. Colors: white background, indigo #4f46e5 buttons, dark navy #1a1a2e text. No hands, no people. Flat design with subtle shadow. 1200x800.
```

---

## Angle 2 : "Transforme chaque vente en 3 ventes"

### Hero Image
```
Flat illustration showing a sales funnel concept: one customer enters at top, three purchases come out at bottom (represented as receipts or product boxes). Arrow flow from top to bottom. Clean geometric style. Color palette: dark navy #1a1a2e background, indigo #4f46e5 funnel, green #10b981 for the outputs/conversions, yellow #f59e0b accents. No text, no people. 1536x1024.
```

### Section Probleme — illustration
```
Minimalist illustration of a shopping cart with a single small item inside, and a large empty space around it. Conveying the idea of missed opportunity — one item when there could be three. Muted dark navy #1a1a2e background, the cart in indigo #4f46e5 outline. Clean vector style, no gradients. 1200x800.
```

### Section Features — funnel diagram
```
Clean infographic-style diagram showing a 3-step checkout funnel: Step 1 "Product + Bump" (checkbox icon), Step 2 "Upsell" (arrow up icon), Step 3 "Downsell" (arrow down icon). Each step shows a price increase. Professional data visualization style. Dark navy #1a1a2e background, indigo #4f46e5 elements, green #10b981 for positive metrics. No text labels (those will be added in HTML). 1200x800.
```

---

## Notes generation
- Model : gpt-image-1
- Size : 1536x1024 (hero) ou 1200x800 (sections)
- Quality : high
- Commande type :
```bash
python "scripts/gen.py" --prompt "[prompt ci-dessus]" --model gpt-image-1 --size 1536x1024 --quality high --count 1 --out-dir outputs/images/angle-N/
```
