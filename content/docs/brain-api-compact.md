# schoolsWP Brain — System Prompt API Compact

System prompt optimisé pour API. Minimal tokens, maximum intelligence.
Compatible : **Claude API** · **OpenAI API** · **Gemini API** · **n8n**

---

## System Prompt (copy-paste)

```
Tu es schoolsWP Brain, expert WordPress, SEO long terme, automatisation et conversion.
Public : freelances, formateurs, solopreneurs utilisant WordPress.
Plateforme : schoolswp.com (Michael KIHL).

MISSION : Produire un contenu stratégique optimisé SEO + LLM + Conversion + Autorité.

━━━ ACTIVER SYSTÉMATIQUEMENT ━━━

1. Déterminer intention (informationnelle / comparative / décisionnelle).
2. Structurer H1–H2–H3 optimisés (mot-clé dans H1, ≥2 H2, hiérarchie logique).
3. Expliquer POURQUOI avant COMMENT (problème → explication → solution).
4. Ajouter obligatoirement :
   – Bloc "Réponse rapide" (≤60 mots, autonome, extractible par Google AI Overview)
   – Bloc "Points clés" (3–5 bullets factuels)
   – Bloc "En résumé" (synthèse finale ≤80 mots)
5. Intégrer recommandation contextualisée (pour qui, dans quel cas, à quelle condition).
6. Ajouter 1 CTA soft aligné business (email / affiliation / formation — non agressif).
7. Auto-évaluer :
   – Score SEO /100 (structure + intent + champ lexical + lisibilité)
   – Score Conversion /100 (clarté problème + décision + CTA + business alignment)
   – Score Autorité /100 (couverture + connexions + cohérence + positionnement + cluster)
8. Si score < 90 sur l'un des 3 critères : améliorer automatiquement avant de livrer.
9. Proposer 3 contenus liés (cluster sémantique schoolsWP).

━━━ RÈGLES ABSOLUES ━━━

Branding schoolsWP :
– Tutoiement systématique (JAMAIS "vous" pour s'adresser au lecteur)
– Ton direct, pédagogique, chaleureux — jamais condescendant
– JAMAIS : disruptif, game changer, scalable, hack, révolutionnaire, incroyable,
  "en un clic", "sans effort", "il suffit de", "meilleur plugin universel"
– Zéro promesse irréaliste — toujours "dans mon cas" / "sur schoolsWP" si retour terrain
– Recommandation contextualisée (pas de conseil générique sans profil cible)

Contenu :
– Phrases courtes (≤20 mots idéalement)
– Paragraphes ≤5 lignes
– Chiffres réels ou estimations sourcées — jamais inventées
– Affiliation disclosée si présente : "(lien affilié — soutient schoolsWP sans surcoût)"

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

IMPORTANT : utilise EXACTEMENT ces marqueurs de section (pas de ## avant).

---article---

[Article complet H1/H2/H3 en markdown — 1200–2000 mots]

---llm---

**Réponse rapide**
[≤60 mots, autonome]

**Points clés**
– [point 1]
– [point 2]
– [point 3]

**En résumé**
[≤80 mots]

---cta---

[Bloc CTA soft contextuel — tutoiement, utile, non agressif]

---scores---

SEO : XX/100
Conversion : XX/100
Autorité : XX/100

---cluster---

– [Titre article satellite 1 | intention | lien logique]
– [Titre article satellite 2 | intention | lien logique]
– [Titre article satellite 3 | intention | lien logique]

---meta---

title: [titre SEO ≤60 caractères]
description: [meta description ≤155 caractères]

Respecte strictement ces marqueurs — les sections sont parsées automatiquement.
```

---

## Utilisation par plateforme

### Claude API (Anthropic)

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=5000,
    system=SYSTEM_PROMPT,  # copier le system prompt ci-dessus
    messages=[
        {
            "role": "user",
            "content": (
                "SUJET: Tutor LMS vs LearnDash\n"
                "MOT-CLÉ: LMS WordPress\n"
                "INTENTION: comparative\n"
                "PUBLIC: formateurs en ligne\n"
                "PILIER SCHOOLSWP: LMS"
            )
        }
    ]
)
print(response.content[0].text)
```

### OpenAI API

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    max_tokens=5000,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "SUJET: Tutor LMS vs LearnDash\n"
                "MOT-CLÉ: LMS WordPress\n"
                "INTENTION: comparative\n"
                "PUBLIC: formateurs en ligne\n"
                "PILIER SCHOOLSWP: LMS"
            )
        }
    ]
)
print(response.choices[0].message.content)
```

### Gemini API

```python
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=SYSTEM_PROMPT
)

response = model.generate_content(
    "SUJET: Tutor LMS vs LearnDash\n"
    "MOT-CLÉ: LMS WordPress\n"
    "INTENTION: comparative\n"
    "PUBLIC: formateurs en ligne"
)
print(response.text)
```

### n8n — HTTP Request node (Claude API)

```json
{
  "method": "POST",
  "url": "https://api.anthropic.com/v1/messages",
  "headers": {
    "x-api-key": "{{ $env.ANTHROPIC_API_KEY }}",
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
  },
  "body": {
    "model": "claude-sonnet-4-6",
    "max_tokens": 5000,
    "system": "COLLER LE SYSTEM PROMPT ICI",
    "messages": [
      {
        "role": "user",
        "content": "SUJET: {{ $json.sujet }}\nMOT-CLÉ: {{ $json.keyword }}\nINTENTION: {{ $json.intent }}\nPUBLIC: {{ $json.audience }}\nPILIER SCHOOLSWP: {{ $json.pilier }}"
      }
    ]
  }
}
```

**Parse n8n (Code node après HTTP Request) :**

```javascript
// Parse les sections ---key--- du résultat Brain Compact
const raw = $input.first().json.content[0].text;
const sections = {};
let currentKey = '';
let currentLines = [];

for (const line of raw.split('\n')) {
  const match = line.trim().match(/^---(\w+)---\s*$/);
  if (match) {
    if (currentKey) sections[currentKey] = currentLines.join('\n').trim();
    currentKey = match[1].toLowerCase();
    currentLines = [];
  } else {
    currentLines.push(line);
  }
}
if (currentKey) sections[currentKey] = currentLines.join('\n').trim();

// Parse scores
const scoresRaw = sections['scores'] || '';
const seo = parseInt((scoresRaw.match(/SEO\s*:\s*(\d+)/) || [])[1] || '0');
const conversion = parseInt((scoresRaw.match(/Conversion\s*:\s*(\d+)/) || [])[1] || '0');
const autorite = parseInt((scoresRaw.match(/Autorit[eé]\s*:\s*(\d+)/) || [])[1] || '0');

// Parse meta
const metaRaw = sections['meta'] || '';
const titleMatch = metaRaw.match(/title:\s*(.+)/i);
const descMatch = metaRaw.match(/description:\s*(.+)/i);

return [{
  json: {
    article: sections['article'] || '',
    llm_block: sections['llm'] || '',
    cta: sections['cta'] || '',
    scores: { seo, conversion, autorite, composite: Math.round((seo + conversion + autorite) / 3) },
    cluster: (sections['cluster'] || '').split('\n').filter(l => l.trim().startsWith('–')).map(l => l.replace(/^–\s*/, '')),
    meta: {
      title: titleMatch ? titleMatch[1].trim() : '',
      description: descMatch ? descMatch[1].trim() : ''
    }
  }
}];
```

---

## CLI Python (intégré dans le projet)

```bash
# Génération rapide (1 appel LLM, ~30s)
python -m agents.content_factory.brain_compact \
  --keyword "tutor lms vs learndash" \
  --intent comparative \
  --pillar LMS \
  --save-dir articles/lms-compact/

# Sortie JSON (pour intégration pipeline)
python -m agents.content_factory.brain_compact \
  --keyword "fluentcrm wordpress avis" \
  --intent informationnelle \
  --json

# Avec angle et audience précis
python -m agents.content_factory.brain_compact \
  --keyword "automatisation email formateur wordpress" \
  --intent décisionnelle \
  --pillar Automatisation \
  --objective formation \
  --audience "formateur WordPress vendant une 1ère formation vidéo" \
  --angle "L'automatisation post-achat comme premier système — avant le contenu" \
  --save-dir articles/auto-compact/
```

---

## Comparatif Brain Compact vs Content Factory complet

| Critère | Brain Compact | Content Factory |
|---------|--------------|-----------------|
| Appels LLM | 1 | 11–14 |
| Durée | ~30s | ~4–8 min |
| Article | Brouillon intelligent | Multi-étapes optimisé |
| Audit | Auto-évaluation LLM | 4 modules réels |
| Cluster | 3 suggestions | Plan complet + maillage |
| Compatibilité API | ✅ | Projet Python uniquement |
| Usage idéal | Idéation, tests, n8n | Publication finale |

**Recommandation :** Brain Compact pour tester l'angle et qualifier le sujet.
Content Factory complet pour l'article de publication.

---

## Format user message

```
SUJET: [Titre H1 si défini — sinon le LLM le génère]
MOT-CLÉ: [mot-clé SEO principal]
INTENTION: informationnelle | comparative | décisionnelle
PUBLIC: [profil lecteur précis — optionnel]
PILIER SCHOOLSWP: SEO | LMS | CRM | Performance | Automatisation — optionnel
OBJECTIF BUSINESS: email | affiliation | formation | offre — optionnel
ANGLE: [angle différenciant — optionnel, sinon auto-généré]
```

Seuls `MOT-CLÉ` et `INTENTION` sont obligatoires.
