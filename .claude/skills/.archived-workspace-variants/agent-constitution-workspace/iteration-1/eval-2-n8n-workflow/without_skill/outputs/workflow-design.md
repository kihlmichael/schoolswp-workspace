# Workflow n8n — Abonnés Fluent Forms → FluentCRM + Séquence de bienvenue

## Vue d'ensemble

Ce workflow couvre 4 objectifs :

1. Capter les soumissions Fluent Forms
2. Créer/mettre à jour le contact dans FluentCRM avec les bons tags
3. Démarrer une séquence email de bienvenue
4. Notifier par email en cas d'erreur

---

## Architecture du workflow

### Nœuds (dans l'ordre d'exécution)

```
[1] Webhook (Fluent Forms)
       ↓
[2] Set — Normaliser les données
       ↓
[3] HTTP Request — Créer/MAJ contact FluentCRM
       ↓
[4] IF — Contact créé avec succès ?
      ↓ YES                  ↓ NO
[5] HTTP Request          [6] Send Email
    Appliquer tags             (notification erreur)
       ↓
[7] HTTP Request
    Démarrer séquence email
       ↓
[8] IF — Séquence démarrée ?
      ↓ YES        ↓ NO
  (fin OK)      [9] Send Email
                    (notification erreur)
```

---

## Détail nœud par nœud

### Nœud 1 — Webhook trigger

**Type** : Webhook
**typeVersion** : 1
**Méthode** : POST
**Path** : `/fluent-forms-subscriber`
**Authentication** : Header Auth (clé secrète partagée avec Fluent Forms)

Configuration côté Fluent Forms : dans les paramètres du formulaire, ajouter une intégration "Webhook" pointant vers l'URL n8n avec le header `X-Webhook-Secret: <valeur>`.

Champs attendus dans le payload (exemple) :

```json
{
  "first_name": "Marie",
  "last_name": "Dupont",
  "email": "marie@exemple.fr",
  "form_id": "12",
  "source": "landing-lms"
}
```

---

### Nœud 2 — Set (normalisation des données)

**Type** : Set
**typeVersion** : 3.4

Objectif : créer des variables propres et stables pour la suite du workflow, indépendamment des noms de champs Fluent Forms qui peuvent varier selon les formulaires.

Champs à définir :

```
email       → {{ $json.email | trim | lower }}
first_name  → {{ $json.first_name | trim }}
last_name   → {{ $json.last_name | trim }}
full_name   → {{ $json.first_name }} {{ $json.last_name }}
form_id     → {{ $json.form_id }}
source      → {{ $json.source || 'fluent-forms' }}
tags        → déterminés par logique (voir ci-dessous)
```

**Logique de tags** : utiliser un nœud Code (typeVersion 2) juste après le Set si la logique est complexe, par exemple :

```javascript
const formId = $input.first().json.form_id;
const tagMap = {
  12: ["prospect-lms", "top-of-funnel"],
  15: ["prospect-crm", "top-of-funnel"],
  18: ["webinaire", "cold-lead"],
};
const tags = tagMap[formId] || ["subscriber-generique"];
return [{ json: { ...$input.first().json, tags } }];
```

---

### Nœud 3 — HTTP Request — Créer/MAJ contact FluentCRM

**Type** : HTTP Request
**typeVersion** : 4.2
**Méthode** : POST
**URL** : `https://votre-site.fr/wp-json/fluent-crm/v2/subscribers`

**Authentication** : Basic Auth (user WP avec accès API FluentCRM, ou Application Password)

**Body** (JSON) :

```json
{
  "email": "{{ $json.email }}",
  "first_name": "{{ $json.first_name }}",
  "last_name": "{{ $json.last_name }}",
  "status": "subscribed",
  "tags": "{{ $json.tags.join(',') }}",
  "custom_values": {
    "source": "{{ $json.source }}",
    "form_id": "{{ $json.form_id }}"
  }
}
```

**Options importantes** :

- Activer "Continue on Fail" = true (pour capturer les erreurs dans le IF suivant)
- Timeout : 10 secondes

**Note** : L'API FluentCRM fait un upsert par défaut — si le contact existe déjà, il est mis à jour. Les tags sont ajoutés sans écraser les existants si l'on passe par `tags` (pas `replace_tags`).

---

### Nœud 4 — IF — Succès de la création

**Type** : IF
**typeVersion** : 2.2

Condition :

```
$json.id  EXISTS  (le contact FluentCRM retourne un champ "id" si créé/mis à jour)
```

Ou en cas d'erreur HTTP :

```
$json.statusCode  NOT EQUAL  200
```

Branching :

- **TRUE** (succès) → vers nœud 5
- **FALSE** (erreur) → vers nœud 6 (notification erreur)

---

### Nœud 5 — HTTP Request — Appliquer les tags

**Type** : HTTP Request
**typeVersion** : 4.2
**Méthode** : POST
**URL** : `https://votre-site.fr/wp-json/fluent-crm/v2/subscribers/{{ $json.id }}/tags`

**Body** :

```json
{
  "tags": "{{ $('Set').first().json.tags.join(',') }}"
}
```

**Note** : Ce nœud est optionnel si le nœud 3 applique déjà les tags. Il devient utile si on veut appliquer des tags conditionnels supplémentaires (ex : tag "doublon" si le contact existait déjà avant cette soumission).

---

### Nœud 6 — Send Email — Erreur création contact

**Type** : Send Email (ou Gmail/SMTP selon config)
**typeVersion** : 2

**To** : `contact@michaelkihl.fr`
**Subject** : `[schoolsWP] Erreur workflow abonné — FluentCRM`
**Body** :

```
Un abonné n'a pas pu être créé dans FluentCRM.

Email soumis : {{ $('Set').first().json.email }}
Formulaire : {{ $('Set').first().json.form_id }}
Erreur : {{ $json.message || 'Réponse inattendue de l'API' }}
Timestamp : {{ $now.toISO() }}

Vérifier dans FluentCRM et relancer manuellement si nécessaire.
```

---

### Nœud 7 — HTTP Request — Démarrer la séquence email

**Type** : HTTP Request
**typeVersion** : 4.2
**Méthode** : POST
**URL** : `https://votre-site.fr/wp-json/fluent-crm/v2/sequences/{{ SEQUENCE_ID }}/subscribe`

Remplacer `SEQUENCE_ID` par l'ID de la séquence de bienvenue (visible dans FluentCRM > Email Sequences > URL de la séquence).

**Body** :

```json
{
  "subscriber_id": "{{ $('HTTP Request - FluentCRM').first().json.id }}"
}
```

**Continue on Fail** : true

---

### Nœud 8 — IF — Séquence démarrée ?

**Type** : IF
**typeVersion** : 2.2

Condition :

```
$json.success  EQUAL  true
```

Ou :

```
$json.statusCode  EQUAL  200
```

- **TRUE** → fin du workflow (succès complet)
- **FALSE** → nœud 9 (notification erreur séquence)

---

### Nœud 9 — Send Email — Erreur séquence

**Type** : Send Email
**Subject** : `[schoolsWP] Erreur démarrage séquence email`
**Body** :

```
La séquence de bienvenue n'a pas pu être démarrée.

Contact : {{ $('Set').first().json.email }} (ID: {{ $('HTTP Request - FluentCRM').first().json.id }})
Erreur : {{ $json.message || 'Réponse inattendue' }}
Timestamp : {{ $now.toISO() }}

Le contact est bien créé dans FluentCRM — seul le démarrage de séquence a échoué.
Relancer manuellement depuis FluentCRM > Contacts > [email] > Sequences.
```

---

## Configuration côté Fluent Forms

Dans l'interface Fluent Forms :

1. Aller dans **Intégrations** du formulaire concerné
2. Ajouter une intégration **Webhook**
3. URL : `https://schoolswp-n8n.wp1.host/webhook/fluent-forms-subscriber`
4. Méthode : POST
5. Ajouter un header : `X-Webhook-Secret: <valeur_secrète>`
6. Format : JSON
7. Mapper les champs du formulaire vers les noms attendus (`email`, `first_name`, etc.)

---

## Bonnes pratiques appliquées

### Nommage des nœuds

Utiliser des noms explicites en français ou en anglais clair :

- "Webhook — Fluent Forms"
- "Set — Normaliser données"
- "HTTP — Créer contact FluentCRM"
- "IF — Contact OK ?"
- "HTTP — Appliquer tags"
- "HTTP — Démarrer séquence bienvenue"
- "Email — Erreur contact"
- "Email — Erreur séquence"

### Gestion des erreurs

- Chaque nœud HTTP Request critique a `Continue on Fail` activé
- Les deux points de défaillance (création contact, démarrage séquence) ont chacun leur branche d'erreur avec notification distincte
- Le message d'erreur inclut systématiquement : email, timestamp, contexte de l'échec

### Sécurité

- Ne jamais stocker les credentials dans les nœuds directement — utiliser le gestionnaire de credentials n8n
- Le webhook utilise un secret partagé pour éviter les appels non authentifiés
- Les Application Passwords WordPress sont préférés aux mots de passe WP directs

### Idempotence

- FluentCRM fait un upsert par défaut : si l'email existe déjà, le contact est mis à jour sans doublon
- La séquence FluentCRM vérifie nativement si l'abonné est déjà inscrit à la séquence

### typeVersions compatibles (n8n 2.0.3)

| Nœud         | Version utilisée |
| ------------ | ---------------- |
| Webhook      | 1                |
| Set          | 3.4              |
| Code         | 2                |
| HTTP Request | 4.2              |
| IF           | 2.2              |
| Send Email   | 2                |

---

## Variante : tags par liste de formulaires

Si les formulaires schoolsWP varient fréquemment, externaliser la table de correspondance `form_id → tags` dans un Google Sheet (nœud googleSheets v4.5) en début de workflow :

```
[Webhook] → [Google Sheets — Lire table tags] → [Code — Résoudre tags] → [Set] → ...
```

Cela permet de modifier les tags sans toucher au workflow.

---

## Résumé des credentials à configurer dans n8n

| Credential       | Type        | Usage                                |
| ---------------- | ----------- | ------------------------------------ |
| `FluentCRM API`  | Basic Auth  | HTTP Requests vers WP REST API       |
| `Webhook Secret` | Header Auth | Authentifier les appels Fluent Forms |
| `SMTP schoolsWP` | SMTP        | Envoi des emails d'erreur            |
