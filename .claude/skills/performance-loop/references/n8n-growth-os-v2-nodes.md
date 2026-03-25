# schoolsWP Growth OS — V2 node par node

4 workflows. Manuel au début, automatisé progressivement.

---

## Ordre de montage

```text
Jour 1 → 01 Daily SEO Watch
Jour 2 → 02 SEO Patch Generator (Manual Trigger)
Jour 3 → test draft WP
Jour 4 → 03 Weekly Topic Discovery
Jour 5 → 04 New Article Draft Builder (Manual Trigger)
```

Pas de publication automatique tant que les drafts ne sont pas validés.

---

## 01 — Daily SEO Watch

**But :** détecter les pages existantes à optimiser.

| #   | Node                       | Type                  | Config clé                                        |
| --- | -------------------------- | --------------------- | ------------------------------------------------- |
| 1   | Cron                       | scheduleTrigger       | tous les jours 07:30                              |
| 2   | GSC Pages (28j)            | httpRequest → GSC API | dimensions=page, 28j                              |
| 3   | GSC Pages (28j précédents) | httpRequest → GSC API | dimensions=page, J-29 à J-56                      |
| 4   | Merge                      | merge                 | Combine, match sur keys[0]                        |
| 5   | Clean + Delta              | code                  | calcul deltas clics/imp/ctr/pos                   |
| 6   | IF — pages utiles          | if                    | impressions_28d > 100, url contains schoolswp.com |
| 7   | Score                      | code                  | P1/P2/P3 + opportunity_type                       |
| 8   | IF — P1/P2                 | if                    | priority = P1 ou P2                               |
| 9   | Append seo_pages           | googleSheets          | append                                            |
| 10  | Append seo_tasks           | googleSheets          | append                                            |

### Node 5 — Code : Clean + Delta

```javascript
function safeNum(v, fallback = 0) {
  const n = Number(v);
  return Number.isFinite(n) ? n : fallback;
}

return items.map((item) => {
  const j = item.json;
  const current = j;
  const previous = j.pairedItem ? j.pairedItem.item : {};

  const page = current.keys?.[0] || current.page || "";
  const clicks = safeNum(current.clicks);
  const impressions = safeNum(current.impressions);
  const ctr = safeNum(current.ctr);
  const position = safeNum(current.position, 99);

  const prevClicks = safeNum(previous.clicks);
  const prevImpressions = safeNum(previous.impressions);
  const prevCtr = safeNum(previous.ctr);
  const prevPosition = safeNum(previous.position, 99);

  return {
    json: {
      url: page,
      clicks_28d: clicks,
      impressions_28d: impressions,
      ctr_28d: ctr,
      position_28d: position,
      clicks_prev_28d: prevClicks,
      impressions_prev_28d: prevImpressions,
      ctr_prev_28d: prevCtr,
      position_prev_28d: prevPosition,
      delta_clicks: clicks - prevClicks,
      delta_impressions: impressions - prevImpressions,
      delta_ctr: ctr - prevCtr,
      delta_position: position - prevPosition,
      scan_date: new Date().toISOString().slice(0, 10),
    },
  };
});
```

### Node 7 — Code : Score + opportunité

```javascript
return items.map((item) => {
  const j = item.json;

  const impressions = Number(j.impressions_28d || 0);
  const ctr = Number(j.ctr_28d || 0) * 100;
  const position = Number(j.position_28d || 99);
  const deltaClicks = Number(j.delta_clicks || 0);
  const deltaImpressions = Number(j.delta_impressions || 0);

  let score = 0;
  let opportunity = "NO_ACTION";
  let priority = "IGNORE";
  let recommended_action = "";

  if (position >= 4 && position <= 12) score += 40;
  if (impressions > 1000) score += 30;
  if (ctr < 2) score += 30;
  if (deltaClicks < -20) score += 15;
  if (deltaImpressions > 100 && deltaClicks <= 0) score += 15;

  if (score >= 70) priority = "P1";
  else if (score >= 50) priority = "P2";
  else if (score >= 30) priority = "P3";

  if (position >= 4 && position <= 12 && ctr < 2.5) {
    opportunity = "CTR_PATCH";
    recommended_action =
      "Réécrire le title/meta et enrichir le snippet avec FAQ.";
  } else if (deltaClicks < -20) {
    opportunity = "CONTENT_REFRESH";
    recommended_action =
      "Mettre à jour la page et renforcer les sections manquantes.";
  } else if (deltaImpressions > 100 && deltaClicks <= 0) {
    opportunity = "SECTION_EXPANSION";
    recommended_action =
      "Ajouter une section dédiée à la nouvelle intention détectée.";
  }

  j.score = score;
  j.priority = priority;
  j.opportunity_type = opportunity;
  j.recommended_action = recommended_action;

  return { json: j };
});
```

### Onglet `seo_pages` — colonnes

```text
scan_date | url | clicks_28d | impressions_28d | ctr_28d | position_28d
clicks_prev_28d | impressions_prev_28d | ctr_prev_28d | position_prev_28d
delta_clicks | delta_impressions | delta_ctr | delta_position
score | priority | opportunity_type | recommended_action | status
```

---

## 02 — SEO Patch Generator

**But :** prendre une page P1/P2 et créer un patch + un draft WP.

| #   | Node                | Type             | Config clé                                                     |
| --- | ------------------- | ---------------- | -------------------------------------------------------------- |
| 1   | Manual Trigger      | manualTrigger    | —                                                              |
| 2   | Read seo_pages      | googleSheets     | read, priority=P1, status=detected                             |
| 3   | Extract slug        | code             | URL → slug                                                     |
| 4   | Fetch WP post       | httpRequest GET  | `/wp-json/wp/v2/posts?slug={{$json.slug}}`                     |
| 5   | Clean HTML          | code             | strip tags, slice 12000                                        |
| 6   | OpenAI — Résumé     | openAi           | résumé 8 lignes                                                |
| 7   | OpenAI — Patch SEO  | openAi           | JSON : patch_title + patch_meta + faq                          |
| 8   | Parse JSON          | code             | parser sortie LLM                                              |
| 9   | OpenAI — Draft HTML | openAi           | brouillon HTML complet                                         |
| 10  | Create WP draft     | httpRequest POST | `/wp-json/wp/v2/posts` status=draft                            |
| 11  | Update seo_pages    | googleSheets     | update : patch_title + patch_meta + draft_url + status=drafted |

### Node 3 — Code : Extract slug

```javascript
return items.map((item) => {
  const url = item.json.url || "";
  const clean = url.replace(/^https?:\/\/[^/]+/, "").replace(/^\/|\/$/g, "");
  const parts = clean.split("/");
  item.json.slug = parts[parts.length - 1] || "";
  return item;
});
```

### Node 5 — Code : Clean HTML

```javascript
return items.map((item) => {
  const post = Array.isArray(item.json) ? item.json[0] : item.json;
  const title = post?.title?.rendered || "";
  const content = post?.content?.rendered || "";
  const id = post?.id || "";

  const clean = content
    .replace(/<[^>]*>/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 12000);

  return {
    json: {
      ...item.json,
      wp_id: id,
      title_current: title,
      content_clean: clean,
    },
  };
});
```

### Node 7 — Prompt : Patch SEO

```text
Tu es un expert SEO WordPress pour schoolsWP.

URL : {{$json.url}}
Titre actuel : {{$json.title_current}}
Type d'opportunité : {{$json.opportunity_type}}
Résumé : {{$json.text}}

Tâche : propose un patch SEO en JSON strict.

{
  "patch_title": "",
  "patch_meta": "",
  "faq": ["", "", ""]
}

Contraintes : français, ton direct, pas de clickbait, orienté CTR et clarté.
```

### Node 8 — Code : Parse JSON

```javascript
return items.map((item) => {
  const raw = item.json.text || item.json.output || "{}";
  let parsed = {};
  try {
    parsed = JSON.parse(raw);
  } catch (e) {
    parsed = { patch_title: "", patch_meta: "", faq: [] };
  }

  item.json.patch_title = parsed.patch_title || "";
  item.json.patch_meta = parsed.patch_meta || "";
  item.json.patch_faq = JSON.stringify(parsed.faq || []);
  return item;
});
```

### Node 9 — Prompt : Draft HTML

```text
Tu rédiges un brouillon de patch SEO pour schoolsWP.

URL : {{$json.url}}
Titre actuel : {{$json.title_current}}
Nouveau title : {{$json.patch_title}}
Nouvelle meta : {{$json.patch_meta}}
FAQ : {{$json.patch_faq}}

Tâche : brouillon HTML simple avec :
- rappel du title proposé
- rappel de la meta proposée
- section FAQ (3 Q/R courtes)
- note finale "à valider manuellement"

Réponds en HTML simple.
```

---

## 03 — Weekly Topic Discovery

**But :** détecter 1 nouveau sujet SEO / semaine.

| #   | Node                 | Type                  | Config clé                               |
| --- | -------------------- | --------------------- | ---------------------------------------- |
| 1   | Cron                 | scheduleTrigger       | lundi 08:00                              |
| 2   | GSC Queries          | httpRequest → GSC API | dimensions=page+query, 28j               |
| 3   | IF — filtre          | if                    | impressions > 50, position 8-30          |
| 4   | Exclure marque       | code                  | filter brandTerms                        |
| 5   | Groupement           | code                  | normalisation requêtes proches           |
| 6   | OpenAI — Choix sujet | openAi                | JSON : decision + working_title + intent |
| 7   | Parse JSON           | code                  | —                                        |
| 8   | IF — NEW_ARTICLE     | if                    | decision = NEW_ARTICLE                   |
| 9   | Append topic_ideas   | googleSheets          | append                                   |

### Node 4 — Code : Exclure marque

```javascript
const brandTerms = ["schoolswp", "michaël kihl", "michael kihl"];

return items.filter((item) => {
  const q = (item.json.keys?.[1] || item.json.query || "").toLowerCase();
  return !brandTerms.some((term) => q.includes(term));
});
```

### Node 5 — Code : Groupement sémantique

```javascript
return items.map((item) => {
  const query = (item.json.keys?.[1] || item.json.query || "")
    .toLowerCase()
    .trim();

  let grouped = query
    .replace(/\bavis\b/g, "avis")
    .replace(/\btest\b/g, "avis")
    .replace(/\s+/g, " ")
    .trim();

  item.json.detected_query = query;
  item.json.grouped_topic = grouped;
  item.json.source_url = item.json.keys?.[0] || "";
  return item;
});
```

### Node 6 — Prompt : Choix du sujet

```text
Tu es un stratège SEO pour schoolsWP.

Source URL : {{$json.source_url}}
Detected query : {{$json.detected_query}}
Grouped topic : {{$json.grouped_topic}}
Impressions : {{$json.impressions}}
Clics : {{$json.clicks}}
CTR : {{$json.ctr}}
Position : {{$json.position}}

Décide : IGNORE / ADD_SECTION / NEW_ARTICLE

{
  "decision": "",
  "working_title": "",
  "target_intent": "",
  "reason_why": "",
  "cta": ""
}

Privilégie seulement les sujets utiles : WordPress, SEO, automatisation, business WordPress.
```

### Onglet `topic_ideas` — colonnes

```text
created_at | source_url | detected_query | grouped_topic
impressions_28d | clicks_28d | position_28d | decision
working_title | target_intent | cta | brief_h2_h3 | faq | draft_url | status
```

Statuts : `detected` → `selected` → `drafted` → `reviewed` → `published`

---

## 04 — New Article Draft Builder

**But :** 1 brouillon d'article neuf à partir du meilleur sujet.

| #   | Node                | Type             | Config clé                                              |
| --- | ------------------- | ---------------- | ------------------------------------------------------- |
| 1   | Manual Trigger      | manualTrigger    | —                                                       |
| 2   | Read topic_ideas    | googleSheets     | read, status=detected, limit 1                          |
| 3   | OpenAI — Brief      | openAi           | JSON : angle + promise + h2_h3 + faq + cta              |
| 4   | Parse JSON          | code             | —                                                       |
| 5   | OpenAI — Draft HTML | openAi           | article complet en HTML                                 |
| 6   | Create WP draft     | httpRequest POST | `/wp-json/wp/v2/posts` status=draft                     |
| 7   | Update topic_ideas  | googleSheets     | update : draft_url + brief_h2_h3 + faq + status=drafted |

### Node 3 — Prompt : Brief SEO

```text
Tu es rédacteur SEO pour schoolsWP.

Sujet : {{$json.grouped_topic}}
Titre de travail : {{$json.working_title}}
Intention : {{$json.target_intent}}

Brief en JSON strict :
{
  "angle": "",
  "promise": "",
  "h2_h3": ["", "", "", ""],
  "faq": ["", "", "", "", ""],
  "cta": ""
}

Style : direct, pédagogique, concret, orienté autonomie.
```

### Node 5 — Prompt : Draft complet HTML

```text
Tu rédiges un brouillon d'article pour schoolsWP.

Titre : {{$json.working_title}}
Angle : {{$json.angle}}
Promesse : {{$json.promise}}
Plan : {{$json.h2_h3}}
FAQ : {{$json.faq}}
CTA : {{$json.cta}}

Contraintes :
- français, ton schoolsWP
- phrases courtes, actionnable, pas de blabla
- structure propre H2/H3
- conclusion avec CTA

Rédige en HTML simple prêt pour WordPress.
```

### Node 6 — WordPress REST API (draft)

```text
Method : POST
URL    : https://schoolswp.com/wp-json/wp/v2/posts
Auth   : Basic Auth (Application Password)

Body JSON :
{
  "title": "={{ $json.working_title }}",
  "status": "draft",
  "content": "={{ $json.text }}"
}
```
