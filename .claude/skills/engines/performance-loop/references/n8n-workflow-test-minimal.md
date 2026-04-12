# Workflow de test minimal — schoolsWP

Créer un brouillon WordPress à partir de fausses données, récupérer l'URL admin.

```
Manual Trigger → Set Fake SEO Data → Set Draft Content → Create WordPress Draft → Set Admin URL → Log Draft (optionnel)
```

---

## Node 1 — Manual Trigger

Aucun réglage.

---

## Node 2 — Set Fake SEO Data

Mode : Manual Mapping

| Champ                | Valeur (texte fixe)                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `url`                | `https://schoolswp.com/fluent-forms-avis/`                                                                         |
| `title_current`      | `Fluent Forms avis : test complet`                                                                                 |
| `patch_title`        | `Fluent Forms avis 2026 : test complet et verdict`                                                                 |
| `patch_meta`         | `Découvrez mon avis complet sur Fluent Forms, ses points forts, ses limites et pour qui il vaut vraiment le coup.` |
| `patch_faq`          | `["Fluent Forms est-il fiable ?","À qui s'adresse Fluent Forms ?","Fluent Forms est-il meilleur que WPForms ?"]`   |
| `recommended_action` | `Réécrire le title/meta et enrichir le snippet avec FAQ.`                                                          |

---

## Node 3 — Set Draft Content

Mode : Expression

| Champ           | Expression                            |
| --------------- | ------------------------------------- |
| `draft_title`   | `SEO Patch - {{$json.title_current}}` |
| `draft_content` | voir bloc HTML ci-dessous             |

`draft_content` :

```
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

<hr>

<p><strong>Action recommandée :</strong> {{$json.recommended_action}}</p>
<p><strong>Statut :</strong> Brouillon généré automatiquement. Validation humaine requise.</p>
```

---

## Node 4 — Create WordPress Draft (HTTP Request)

| Paramètre         | Valeur                                       |
| ----------------- | -------------------------------------------- |
| Method            | POST                                         |
| URL               | `https://schoolswp.com/wp-json/wp/v2/posts`  |
| Authentication    | Basic Auth                                   |
| Username          | `seo-agent`                                  |
| Password          | Application Password WP                      |
| Send Body         | activé                                       |
| Body Content Type | JSON                                         |
| Specify Body      | Using Fields Below (ou JSON raw — voir note) |

Body (Using Fields Below) :

| Nom       | Valeur                     |
| --------- | -------------------------- |
| `title`   | `={{$json.draft_title}}`   |
| `status`  | `draft`                    |
| `content` | `={{$json.draft_content}}` |

> **Alternative JSON raw** — si "Using Fields Below" pose problème avec le HTML :
> Body type → JSON → coller le JSON directement avec les expressions.

---

## Node 5 — Set Admin URL

Mode : Expression

| Champ          | Expression                                                               |
| -------------- | ------------------------------------------------------------------------ |
| `draft_wp_id`  | `={{$json.id}}`                                                          |
| `draft_url`    | `=https://schoolswp.com/wp-admin/post.php?post={{$json.id}}&action=edit` |
| `draft_status` | `={{$json.status}}`                                                      |

---

## Node 6 — Log Draft (Google Sheets, optionnel)

Operation : Append Row
Onglet : `seo_pages` ou `test_drafts`

| Colonne         | Expression                 |
| --------------- | -------------------------- |
| `scan_date`     | `={{$now.toISODate()}}`    |
| `url`           | `={{$json.url}}`           |
| `title_current` | `={{$json.title_current}}` |
| `patch_title`   | `={{$json.patch_title}}`   |
| `patch_meta`    | `={{$json.patch_meta}}`    |
| `draft_wp_id`   | `={{$json.draft_wp_id}}`   |
| `draft_url`     | `={{$json.draft_url}}`     |
| `status`        | `drafted`                  |

---

## Résultat attendu

**Node Create WordPress Draft** → réponse :

```json
{
  "id": 4123,
  "status": "draft",
  "title": { "rendered": "SEO Patch - Fluent Forms avis : test complet" }
}
```

**Node Set Admin URL** :

```
draft_wp_id : 4123
draft_url   : https://schoolswp.com/wp-admin/post.php?post=4123&action=edit
```

---

## Diagnostic erreurs rapide

| Code             | Cause                             | Fix                                 |
| ---------------- | --------------------------------- | ----------------------------------- |
| 401              | Login / Application Password faux | Vérifier la credential Basic Auth   |
| 403              | Rôle WP insuffisant               | Passer le compte à Éditeur          |
| 404              | Mauvais endpoint                  | Vérifier l'URL REST API             |
| 200 / draft vide | `content` mal mappé               | Vérifier l'expression draft_content |

---

## Checklist de validation

- [ ] HTTP renvoie 200 ou 201
- [ ] `id` présent dans la réponse
- [ ] Draft visible dans WP Admin → Articles → Brouillons
- [ ] Titre correct dans l'éditeur WP
- [ ] HTML affiché proprement (pas de tags en clair)
- [ ] `draft_url` ouvre bien l'éditeur du bon post
- [ ] Ligne Google Sheets remplie (si node Log activé)
