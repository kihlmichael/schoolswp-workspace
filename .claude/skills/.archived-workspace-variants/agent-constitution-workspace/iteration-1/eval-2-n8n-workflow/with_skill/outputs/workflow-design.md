# Workflow n8n — Capture abonné Fluent Forms → FluentCRM → Séquence bienvenue

Appliqué via : schoolswp-agent-constitution (cadre automatisation n8n 9 dimensions + CRM segment/état/intention)

---

## 1. Objectif

Transformer chaque soumission de formulaire en contact qualifié dans FluentCRM, déclencher une séquence email de bienvenue automatisée, et capturer toute erreur de manière visible et actionnable.

---

## 2. Plan avant exécution

**Entrées requises :**

- Formulaire Fluent Forms configuré avec les champs : prénom, email (obligatoires), source ou pilier optionnel
- FluentCRM opérationnel avec les listes et tags cibles déjà créés
- Séquence email de bienvenue existante dans FluentCRM
- Adresse email de notification d'erreur définie

**Contraintes :**

- Doublons possibles (même email soumis plusieurs fois)
- Champs manquants ou mal formatés côté formulaire
- API FluentCRM peut échouer (timeout, limite de taux)
- La séquence ne doit se déclencher qu'une seule fois par contact

**Sorties attendues :**

- Contact créé ou mis à jour dans FluentCRM
- Tags et liste attribués correctement
- Séquence de bienvenue démarrée
- Notification email envoyée en cas d'erreur

---

## 3. Architecture du workflow

### Vue d'ensemble des blocs

```
[Trigger] → [Valider entrées] → [Vérifier doublon] → [Créer/MAJ contact]
         → [Attribuer tags] → [Ajouter à la liste] → [Démarrer séquence]
         → [Log succès]

Toute branche d'erreur → [Formater message erreur] → [Notifier par email] → [Log erreur]
```

---

## 4. Détail nœud par nœud

### BLOC 1 — DÉCLENCHEUR

**Node : `Fluent Forms — Webhook Trigger`**

- Type : Webhook (POST)
- URL exposée : `/webhook/fluent-forms-new-subscriber`
- Méthode : POST, réponse immédiate 200 (ne pas laisser le form en attente)
- Données attendues : `{ "first_name": "...", "email": "...", "source": "..." }`

Contrainte : configurer Fluent Forms pour envoyer vers cette URL à la soumission du formulaire cible.

---

### BLOC 2 — VALIDATION DES ENTRÉES

**Node : `Validate — Check Required Fields`**

- Type : Code (JavaScript)
- Rôle : vérifier que `email` est présent et au format valide, que `first_name` n'est pas vide
- Logique :

```javascript
const email = $json.email?.trim().toLowerCase();
const firstName = $json.first_name?.trim();
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

if (!email || !emailRegex.test(email)) {
  throw new Error(`Email invalide ou manquant : "${email}"`);
}
if (!firstName) {
  throw new Error(`Prénom manquant pour ${email}`);
}

return [
  {
    json: {
      email,
      first_name: firstName,
      source: $json.source?.trim() || "fluent-forms",
      received_at: new Date().toISOString(),
    },
  },
];
```

- Branche erreur : si exception → aller vers `Format Error Message`

---

### BLOC 3 — VÉRIFICATION DOUBLON

**Node : `FluentCRM — Search Contact by Email`**

- Type : HTTP Request
- Méthode : GET
- URL : `https://[domaine]/wp-json/fluentcrm/v2/subscribers?search={{ $json.email }}`
- Auth : Basic Auth (utilisateur WordPress avec rôle CRM Manager minimum)
- Retourne : liste de contacts correspondants

**Node : `Route — New or Existing Contact`**

- Type : IF
- Condition : `{{ $json.data.length }}` > 0
- Branche TRUE (contact existant) → `Update Existing Contact`
- Branche FALSE (nouveau contact) → `Create New Contact`

---

### BLOC 4A — CRÉER UN NOUVEAU CONTACT

**Node : `FluentCRM — Create New Contact`**

- Type : HTTP Request
- Méthode : POST
- URL : `https://[domaine]/wp-json/fluentcrm/v2/subscribers`
- Body :

```json
{
  "email": "{{ $json.email }}",
  "first_name": "{{ $json.first_name }}",
  "status": "subscribed",
  "tags": ["nouveau-abonné", "source-{{ $json.source }}"],
  "lists": [1]
}
```

- `lists: [1]` → ID de la liste principale (à adapter selon config FluentCRM)
- En cas d'erreur API → branche vers `Format Error Message`

---

### BLOC 4B — METTRE À JOUR UN CONTACT EXISTANT

**Node : `FluentCRM — Update Existing Contact`**

- Type : HTTP Request
- Méthode : PUT
- URL : `https://[domaine]/wp-json/fluentcrm/v2/subscribers/{{ $json.data[0].id }}`
- Body :

```json
{
  "first_name": "{{ $json.first_name }}",
  "status": "subscribed"
}
```

Logique : on réactive un éventuel contact désinscrit, on ne re-déclenche pas la séquence (voir bloc 5).

---

### BLOC 5 — ATTRIBUER LES TAGS

**Node : `FluentCRM — Apply Tags to Contact`**

- Type : HTTP Request
- Méthode : POST
- URL : `https://[domaine]/wp-json/fluentcrm/v2/subscribers/{{ $json.contact_id }}/tags`
- Body :

```json
{
  "tags": ["nouveau-abonné", "source-{{ $json.source }}"],
  "action": "attach"
}
```

Logique de tag basée sur la source :

| Valeur `source`  | Tag appliqué          | Segment CRM       |
| ---------------- | --------------------- | ----------------- |
| `formulaire-lms` | `source-lms`          | Intérêt LMS       |
| `formulaire-crm` | `source-crm`          | Intérêt CRM       |
| `pop-up-blog`    | `source-blog`         | Lecteur blog      |
| (vide/inconnu)   | `source-fluent-forms` | Segment générique |

Tous les nouveaux contacts reçoivent aussi : `nouveau-abonné`, `onboarding-en-cours`

---

### BLOC 6 — DÉMARRER LA SÉQUENCE DE BIENVENUE

**Node : `Route — Only Start Sequence for New Contacts`**

- Type : IF
- Condition : le contact vient du nœud `Create New Contact` (pas de `Update`)
- Branche TRUE → `FluentCRM — Start Welcome Sequence`
- Branche FALSE → `Log — Contact Updated, No Sequence`

**Node : `FluentCRM — Start Welcome Sequence`**

- Type : HTTP Request
- Méthode : POST
- URL : `https://[domaine]/wp-json/fluentcrm/v2/subscribers/{{ $json.contact_id }}/sequences`
- Body :

```json
{
  "sequence_id": 12
}
```

- `sequence_id: 12` → ID de la séquence de bienvenue dans FluentCRM (à adapter)
- En cas d'erreur → branche vers `Format Error Message`

---

### BLOC 7 — LOG SUCCÈS

**Node : `Log — Record Successful Subscription`**

- Type : Code ou Google Sheets (selon préférence)
- Données loguées : `email`, `first_name`, `source`, `contact_id`, `is_new`, `timestamp`
- Destination recommandée : Google Sheets "Abonnés — Log temps réel"

Colonnes : `date`, `email`, `prénom`, `source`, `statut` (nouveau/existant), `séquence démarrée` (oui/non)

---

### BLOC 8 — GESTION DES ERREURS

**Node : `Format Error Message`**

- Type : Code
- Rôle : formater un message d'erreur lisible

```javascript
const errorMessage = $json.message || $json.error || "Erreur inconnue";
const step = $runIndex || "étape inconnue";

return [
  {
    json: {
      subject: `[schoolsWP] Erreur workflow abonné — ${new Date().toLocaleDateString("fr-FR")}`,
      body: `Une erreur s'est produite dans le workflow "Capture Abonné Fluent Forms".\n\nÉtape : ${step}\nErreur : ${errorMessage}\n\nDonnées reçues :\n${JSON.stringify($("Fluent Forms — Webhook Trigger").item.json, null, 2)}\n\nAction requise : vérifier le contact dans FluentCRM et relancer manuellement si nécessaire.`,
      error_at: new Date().toISOString(),
    },
  },
];
```

**Node : `Email — Notify Admin on Error`**

- Type : Send Email (SMTP ou Gmail node)
- Destinataire : `contact@michaelkihl.fr`
- Sujet : `{{ $json.subject }}`
- Corps : `{{ $json.body }}`

**Node : `Log — Record Error`**

- Type : Google Sheets ou Code
- Destination : onglet "Erreurs" du même Google Sheet
- Colonnes : `date`, `email_reçu`, `étape_échouée`, `message_erreur`

---

## 5. Schéma complet des flux

```
Fluent Forms — Webhook Trigger
  │
  ▼
Validate — Check Required Fields
  │ [ERREUR] ──────────────────────────────────────────┐
  ▼                                                     │
FluentCRM — Search Contact by Email                     │
  │ [ERREUR] ──────────────────────────────────────────┤
  ▼                                                     │
Route — New or Existing Contact                         │
  │                    │                               │
  ▼ [NOUVEAU]          ▼ [EXISTANT]                    │
Create New Contact   Update Existing Contact           │
  │ [ERREUR] ──────────────────────────────────────────┤
  ▼                    ▼                               │
FluentCRM — Apply Tags to Contact                      │
  │ [ERREUR] ──────────────────────────────────────────┤
  ▼                                                     │
Route — Only Start Sequence for New Contacts           │
  │ [NOUVEAU]          │ [EXISTANT]                    │
  ▼                    ▼                               │
Start Welcome Seq   Log — Contact Updated              │
  │ [ERREUR] ──────────────────────────────────────────┤
  ▼                                                     │
Log — Record Successful Subscription                   │
                                                       ▼
                              Format Error Message
                                     │
                                     ▼
                         Email — Notify Admin on Error
                                     │
                                     ▼
                              Log — Record Error
```

---

## 6. Logique CRM — Segment / État / Intention

### Qui est ce contact ?

- Nouveau abonné issu d'un formulaire Fluent Forms
- Segment déterminé par la valeur du champ `source`

### Où en est-il ?

- État initial : `subscribed`, tag `onboarding-en-cours`
- Après complétion de la séquence de bienvenue : retirer `onboarding-en-cours`, ajouter `bienvenue-complété` (géré dans FluentCRM directement, hors scope de ce workflow)

### Quelle est son intention ?

- Déterminée par la valeur `source` du formulaire
- Exemple : `formulaire-lms` → intention de découvrir les LMS WordPress → séquence bienvenue peut être déclinée par pilier si plusieurs séquences existent

### Quelle progression vise-t-on ?

- Court terme : valider l'inscription, livrer la promesse du formulaire (lead magnet ou confirmation)
- Moyen terme : amener le contact à lire un article pilier, cliquer sur une ressource, répondre à un email

### Règle anti-spam

- La séquence de bienvenue ne se déclenche que pour les nouveaux contacts
- Un contact existant est mis à jour (statut, prénom) mais pas re-onboardé

---

## 7. Nommage des nœuds (récapitulatif)

| Nœud                                           | Type          | Rôle                                |
| ---------------------------------------------- | ------------- | ----------------------------------- |
| `Fluent Forms — Webhook Trigger`               | Webhook       | Réception soumission formulaire     |
| `Validate — Check Required Fields`             | Code          | Validation email + prénom           |
| `FluentCRM — Search Contact by Email`          | HTTP Request  | Vérification doublon                |
| `Route — New or Existing Contact`              | IF            | Branchement création vs mise à jour |
| `FluentCRM — Create New Contact`               | HTTP Request  | Création du contact                 |
| `FluentCRM — Update Existing Contact`          | HTTP Request  | Mise à jour contact existant        |
| `FluentCRM — Apply Tags to Contact`            | HTTP Request  | Attribution des tags                |
| `Route — Only Start Sequence for New Contacts` | IF            | Protection anti-doublon séquence    |
| `FluentCRM — Start Welcome Sequence`           | HTTP Request  | Démarrage séquence email            |
| `Log — Record Successful Subscription`         | Google Sheets | Log succès                          |
| `Log — Contact Updated, No Sequence`           | Google Sheets | Log contact existant                |
| `Format Error Message`                         | Code          | Formatage message erreur lisible    |
| `Email — Notify Admin on Error`                | Send Email    | Notification admin                  |
| `Log — Record Error`                           | Google Sheets | Log erreur                          |

---

## 8. Checklist de validation avant mise en production

- [ ] Fluent Forms configuré pour envoyer en POST vers l'URL webhook n8n
- [ ] Les IDs de liste FluentCRM et de séquence sont renseignés dans les nœuds HTTP
- [ ] Les tags cibles (`nouveau-abonné`, `onboarding-en-cours`, `source-*`) existent dans FluentCRM
- [ ] Auth Basic Auth testée sur l'API FluentCRM (200 en retour sur un GET /subscribers)
- [ ] Adresse email de notification d'erreur configurée et testée
- [ ] Google Sheet de log créé avec les bons onglets (Succès + Erreurs)
- [ ] Test bout-en-bout avec un email de test (nouveau + doublon)
- [ ] Vérifier que la séquence ne se déclenche pas deux fois sur un contact existant
- [ ] Nommage de tous les nœuds vérifié (aucun "Set1", "HTTP Request2", etc.)

---

## 9. Points de maintenance

- Si Fluent Forms change la structure du payload → mettre à jour `Validate — Check Required Fields`
- Si FluentCRM change son API REST → mettre à jour les URLs dans les nœuds HTTP
- Les IDs de liste et séquence sont des constantes : les documenter dans un nœud `Sticky Note` en tête de workflow
- Vérifier le log d'erreurs hebdomadairement au début, puis mensuel si stable
- Ajouter un nouveau tag `source-*` dans la table de correspondance à chaque nouveau formulaire créé

---

_Conçu selon le cadre schoolswp-agent-constitution — automatisation n8n 9 dimensions + CRM segment/état/intention._
