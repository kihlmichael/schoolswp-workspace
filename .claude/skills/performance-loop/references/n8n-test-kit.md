# schoolsWP — Mini Kit de Test n8n

Tester toute la chaîne sans attendre GSC.
Ordre recommandé : Test 1 → 2 → 3 → 4.

---

## Faux item `seo_pages`

```json
{
  "scan_date": "2026-03-14",
  "url": "https://schoolswp.com/fluent-forms-avis/",
  "slug": "fluent-forms-avis",
  "title_current": "Fluent Forms avis : test complet",
  "status_wp": "publish",
  "clicks_28d": 182,
  "impressions_28d": 6400,
  "ctr_28d": 0.0284,
  "position_28d": 6.3,
  "clicks_prev_28d": 165,
  "impressions_prev_28d": 5900,
  "ctr_prev_28d": 0.031,
  "position_prev_28d": 6.9,
  "delta_clicks": 17,
  "delta_impressions": 500,
  "delta_ctr": -0.0026,
  "delta_position": -0.6,
  "score": 87,
  "priority": "P1",
  "opportunity_type": "CTR_PATCH",
  "recommended_action": "Réécrire le title/meta et enrichir le snippet avec FAQ.",
  "status": "detected"
}
```

---

## Faux item `topic_ideas`

```json
{
  "created_at": "2026-03-14",
  "source_url": "https://schoolswp.com/fluentcrm-tutorlms/",
  "detected_query": "automatiser tutorlms",
  "grouped_topic": "automatiser tutorlms avec fluentcrm",
  "impressions_28d": 380,
  "clicks_28d": 12,
  "position_28d": 14.2,
  "decision": "NEW_ARTICLE",
  "working_title": "Automatiser TutorLMS avec FluentCRM : le guide complet",
  "target_intent": "informationnelle + solution",
  "cta": "Découvrir la méthode complète pour automatiser votre LMS WordPress",
  "status": "detected"
}
```

---

## Test 1 — Accès WordPress (draft fixe)

Valide que les credentials fonctionnent.

**Node HTTP Request**

- Method : POST
- URL : `https://schoolswp.com/wp-json/wp/v2/posts`
- Auth : Basic Auth (seo-agent)
- Body JSON :

```json
{
  "title": "Test draft accès API",
  "status": "draft",
  "content": "<p>Test de connexion WordPress REST API.</p>"
}
```

**Résultat attendu** : JSON avec `id`, `status: draft`, `link`.
**Erreur 401** = mauvais credentials. **Erreur 403** = rôle insuffisant.

---

## Test 2 — Draft patch SEO avec variables

### Node Set — Données patch

| Champ                | Valeur                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `url`                | `https://schoolswp.com/fluent-forms-avis/`                                                                         |
| `slug`               | `fluent-forms-avis`                                                                                                |
| `title_current`      | `Fluent Forms avis : test complet`                                                                                 |
| `opportunity_type`   | `CTR_PATCH`                                                                                                        |
| `recommended_action` | `Réécrire le title/meta et enrichir le snippet avec FAQ.`                                                          |
| `patch_title`        | `Fluent Forms avis 2026 : test complet et verdict`                                                                 |
| `patch_meta`         | `Découvrez mon avis complet sur Fluent Forms, ses points forts, ses limites et pour qui il vaut vraiment le coup.` |
| `patch_faq`          | `["Fluent Forms est-il fiable ?","À qui s'adresse Fluent Forms ?","Fluent Forms est-il meilleur que WPForms ?"]`   |

### Node Set — Générer le contenu draft

`draft_title` :

```text
SEO Patch - {{$json.title_current}}
```

`draft_content` :

```html
<h2>Page source</h2>
<p><a href="{{$json.url}}">{{$json.url}}</a></p>

<h2>Title SEO proposé</h2>
<p>{{$json.patch_title}}</p>

<h2>Meta description proposée</h2>
<p>{{$json.patch_meta}}</p>

<h2>FAQ proposées</h2>
<ul>
  <li>{{JSON.parse($json.patch_faq)[0] || ''}}</li>
  <li>{{JSON.parse($json.patch_faq)[1] || ''}}</li>
  <li>{{JSON.parse($json.patch_faq)[2] || ''}}</li>
</ul>

<hr />
<p><strong>Action recommandée :</strong> {{$json.recommended_action}}</p>
<p>
  <strong>Statut :</strong> Brouillon généré automatiquement. Validation humaine
  requise.
</p>
```

### Node HTTP Request — POST draft

```json
{
  "title": "={{$json.draft_title}}",
  "status": "draft",
  "content": "={{$json.draft_content}}"
}
```

### Node Set — URL admin (après POST)

| Champ         | Expression                                                               |
| ------------- | ------------------------------------------------------------------------ |
| `draft_url`   | `=https://schoolswp.com/wp-admin/post.php?post={{$json.id}}&action=edit` |
| `draft_wp_id` | `={{$json.id}}`                                                          |

---

## Test 3 — Lire une page existante par slug

**Node HTTP Request**

- Method : GET
- URL : `https://schoolswp.com/wp-json/wp/v2/posts?slug=fluent-forms-avis`
- Auth : Basic Auth (seo-agent)

**Code node — extraire les données**

```javascript
const post = Array.isArray(items[0].json) ? items[0].json[0] : items[0].json;
return [
  {
    json: {
      wp_id: post?.id || "",
      title_current: post?.title?.rendered || "",
      content_raw: (post?.content?.rendered || "")
        .replace(/<[^>]*>/g, " ")
        .replace(/\s+/g, " ")
        .trim()
        .slice(0, 12000),
    },
  },
];
```

---

## Test 4 — Nouvel article complet

### Faux brief

```json
{
  "working_title": "Automatiser TutorLMS avec FluentCRM : le guide complet",
  "angle": "Montrer comment relier TutorLMS et FluentCRM pour automatiser un LMS WordPress sans coder.",
  "promise": "Comprendre les automatisations les plus utiles entre TutorLMS et FluentCRM.",
  "h2_h3": "[\"Pourquoi connecter FluentCRM et TutorLMS\",\"Les automatisations les plus utiles\",\"Segmenter les étudiants automatiquement\",\"Envoyer des emails selon les actions des étudiants\"]",
  "faq": "[\"Pourquoi connecter FluentCRM à TutorLMS ?\",\"Peut-on automatiser les emails d'un LMS WordPress ?\",\"Comment segmenter les étudiants dans FluentCRM ?\",\"Faut-il coder pour connecter FluentCRM et TutorLMS ?\",\"Quels bénéfices pour un LMS automatisé ?\"]",
  "cta": "Découvrir la méthode complète pour automatiser votre LMS WordPress"
}
```

### Node Set — `article_html`

```html
<h1>{{$json.working_title}}</h1>

<p>{{$json.promise}}</p>

<h2>{{JSON.parse($json.h2_h3)[0] || ''}}</h2>
<p>Section à compléter.</p>

<h2>{{JSON.parse($json.h2_h3)[1] || ''}}</h2>
<p>Section à compléter.</p>

<h2>{{JSON.parse($json.h2_h3)[2] || ''}}</h2>
<p>Section à compléter.</p>

<h2>{{JSON.parse($json.h2_h3)[3] || ''}}</h2>
<p>Section à compléter.</p>

<h2>FAQ</h2>
<ul>
  <li>{{JSON.parse($json.faq)[0] || ''}}</li>
  <li>{{JSON.parse($json.faq)[1] || ''}}</li>
  <li>{{JSON.parse($json.faq)[2] || ''}}</li>
  <li>{{JSON.parse($json.faq)[3] || ''}}</li>
  <li>{{JSON.parse($json.faq)[4] || ''}}</li>
</ul>

<p><strong>{{$json.cta}}</strong></p>
```

### Payload WordPress

```json
{
  "title": "={{$json.working_title}}",
  "status": "draft",
  "content": "={{$json.article_html}}"
}
```

---

## Workflow de test minimal (séquence complète)

```
Manual Trigger
  → Set faux seo_pages
  → Set draft_title + draft_content
  → HTTP Request POST /wp-json/wp/v2/posts
  → Set draft_url (= wp-admin/post.php?post={{id}}&action=edit)
  → Google Sheets Append (patch_title, patch_meta, draft_wp_id, draft_url, status=drafted)
```

---

## Checklist de validation

- [ ] Node HTTP ne retourne pas 401/403
- [ ] Draft visible dans WP Admin
- [ ] Titre correct dans WordPress
- [ ] HTML s'affiche proprement (pas de tags échappés)
- [ ] URL admin `draft_url` pointe sur le bon post
- [ ] Ligne Google Sheets remplie avec les bons champs
- [ ] Colonne `status` = `drafted`

---

## Résultat WordPress attendu (simplifié)

```json
{
  "id": 4123,
  "date": "2026-03-14T15:22:00",
  "status": "draft",
  "link": "https://schoolswp.com/?p=4123",
  "title": {
    "rendered": "SEO Patch - Fluent Forms avis : test complet"
  }
}
```

Ligne Google Sheets attendue :

```
2026-03-14 | https://schoolswp.com/fluent-forms-avis/ | Fluent Forms avis 2026 : test complet et verdict | Découvrez mon avis... | 4123 | https://schoolswp.com/wp-admin/post.php?post=4123&action=edit | drafted
```
