# Design : Agent IA n8n de prise de rendez-vous par email via Google Agenda

- **Date** : 2026-05-14
- **Statut** : design validé, prêt pour plan d'implémentation
- **Approche retenue** : C (hybride : agent IA pour la conversation, gate déterministe pour la réservation)

## 1. Contexte

Besoin : automatiser la prise de rendez-vous de démo produit / formation. Un prospect
écrit un email, un agent IA négocie un créneau par retour de mail, puis l'événement est
posé dans Google Agenda. L'agent est autonome mais escalade les cas limites.

Stack cible : n8n (instance `https://schoolswp-n8n.wp1.host`). Conventions n8n du projet :
`systems/n8n/CLAUDE.md` et `.claude/rules/n8n-integration.md`.

## 2. Décision

Trois approches ont été évaluées :

- **A - Agent IA unique avec outils Calendar (ReAct)** : un seul node AI Agent équipé
  d'outils Calendar lecture + écriture. Rejetée : l'action irréversible (création
  d'événement) dépend directement du LLM, garde-fous seulement dans le prompt, peu testable.
- **B - Pipeline déterministe, LLM seulement pour parser/rédiger** : machine à états en
  nodes IF. Rejetée : rigide, gère mal les réponses hors-script du prospect, suivi d'état
  manuel et verbeux.
- **C - Hybride (retenue)** : l'agent IA gère la conversation avec un outil Calendar
  **lecture seule**. Il ne crée jamais l'événement : il émet une intention en JSON. Une
  gate déterministe valide cette intention (5 checks) puis crée l'événement. L'escalade
  est déclenchée soit par l'agent, soit par la gate.

Raison du choix : l'approche C traduit littéralement le niveau d'autonomie demandé
(« autonome + garde-fous »). Le LLM fait ce qu'il fait de mieux (conversation humaine
désordonnée), mais l'écriture irréversible dans l'agenda est encadrée par du code
déterministe et testable. Cohérent avec les patterns du projet (tri-agent, gate
déterministe, principes Karpathy).

## 3. Périmètre

**Dans le périmètre :**

- Surveillance d'une boîte `contact@michaelkihl.fr` (boîte hébergeur, IMAP).
- Classification des mails entrants : RDV démo / pas RDV, et détection du produit
  (schoolsWP / FluentCart / inconnu).
- Conversation par email asynchrone : qualification du besoin, proposition de créneaux,
  confirmation.
- Création autonome de l'événement Google Agenda dans l'un des deux agendas selon le
  produit, avec invitation au prospect et lien visio.
- Escalade Discord (#alerts, canal `schoolsWP-Routines`) sur les cas limites.

**Hors périmètre (évolutions possibles, non retenues pour cette V1) :**

- Relance automatique des prospects silencieux (sous-workflow planifié).
- Intégration CRM (création de contact / tag FluentCRM à la confirmation).
- Canaux autres qu'email (Telegram, WhatsApp, widget web).
- Annulation / replanification d'un RDV existant par email.

## 4. Architecture et topologie

Le workflow se déclenche à chaque mail entrant sur `contact@michaelkihl.fr`. La
conversation étant asynchrone, chaque réponse du prospect re-déclenche le même workflow.
Il n'y a pas de boucle interne : c'est le fil de mail qui porte la conversation. Un state
store (n8n Data Table) indexé sur le `threadId` garde l'état structuré de chaque
conversation.

```text
Email Trigger (contact@michaelkihl.fr, IMAP)
   |
   v
[1] Thread connu dans le state store ?
   |-- oui --> (skip classifieur, conversation en cours) --> [3]
   |-- non --> [2]
   |
[2] Classifieur IA (LLM léger)
   |-- pas RDV --> label "non-rdv" + STOP
   |-- RDV démo --> crée ligne state store (status=new) --> [3]
   |
[3] Context loader : fil de mail complet + état --> objet contexte
   |
   v
[4] Agent IA (outil : get_calendar_availability, lecture seule)
   |   sort un JSON structuré { action, email_draft, ... }
   |
   v
[5] Switch sur "action"
   |-- ask_more_info / propose_slots --> envoi mail + MAJ état
   |-- confirm_booking --> [6] Gate déterministe
   |       5 checks --> OK : créer event Agenda + mail confirmation + état=confirmed
   |                    KO créneau pris : relance [4] avec flag slot_taken
   |                    KO autre : escalade [7]
   |-- escalate --> [7] Webhook Discord + mail d'attente + état=escalated
```

Les blocs **[4] Agent** et **[6] Gate** sont les deux unités centrales et indépendantes :
l'agent ne touche jamais l'agenda en écriture, la gate ne discute jamais avec le prospect.
Le contrat entre les deux est le JSON émis par l'agent (section 6).

Nom du workflow (convention projet) : `[InDev] Email contact@ > Google Agenda: Agent RDV démo`.

## 5. Composants

| Bloc | Rôle | Dépend de |
| --- | --- | --- |
| **[T] Email Trigger** | Surveille `contact@michaelkihl.fr`. Node `Email Trigger (IMAP)` : les MX du domaine pointent vers `mx01/mx02.xcloud.email` (xCloud), pas Google Workspace, donc IMAP confirmé. Émet `threadId`, expéditeur, objet, corps. | Crédentiale IMAP xCloud |
| **[1] Thread lookup** | Node Code/lookup. Lit le state store sur `threadId`. Fil connu : conversation en cours, on saute le classifieur. Inconnu : on classe. | State store |
| **[2] Classifieur IA** | Node LLM léger (modèle Haiku). Entrée : objet + corps. Sortie : `{ is_booking_request: bool, product: "schoolswp"\|"fluentcart"\|"unknown" }`. Si `is_booking_request=false` : classe le mail dans un dossier/label "non-rdv" (déplacement IMAP) et STOP, aucune réponse. | LLM |
| **[3] Context loader** | Récupère le fil de mail complet (historique conversationnel) et la ligne du state store. Fusionne en un objet contexte `{ mail_courant, historique_fil[], etat }`. | State store, accès fil |
| **[4] Agent IA** | Node AI Agent, modèle Sonnet. Un seul outil : `get_calendar_availability` (Google Calendar lecture seule, free/busy sur une plage, sur l'agenda correspondant au `product`). Historique injecté explicitement par [3], agent stateless. Ton des mails : tutoiement (cohérent marque schoolsWP, voir `content/docs/BRAND_RULES.md`). Sortie : JSON structuré (section 6). | LLM, crédentiale Google Calendar |
| **[5] Switch** | Route sur le champ `action` du JSON. | - |
| **[6] Booking Gate** | Déterministe, sans LLM. Applique les 5 checks (section 7). Tout OK : crée l'événement Agenda (agenda selon `product`, prospect en invité, lien visio, Michael en organisateur) + mail de confirmation + état=`confirmed`. Échec « créneau pris » : relance [4] avec flag `slot_taken`. Autre échec : escalade. | Crédentiale Google Calendar, state store |
| **[7] Escalade Discord** | HTTP Request vers le webhook `schoolsWP-Routines` (#alerts) : résumé du fil, email prospect, raison, reco de l'agent. État=`escalated`, + mail d'attente au prospect. | `$vars.DISCORD_WEBHOOK` |
| **State store** | n8n Data Table, clé `threadId` (schéma section 6). | - |
| **Validation de schéma** | Node intercalé après [4] : rejette tout JSON malformé (champ manquant, `proposed_slot` hors `proposed_slots`) vers escalade. Garantit qu'un agent qui dérape ne casse pas le workflow. | - |

## 6. Contrat de données

### Sortie de l'agent [4] (contrat agent -> gate)

```json
{
  "action": "ask_more_info | propose_slots | confirm_booking | escalate",
  "email_draft": "corps du mail de réponse au prospect",
  "proposed_slot": { "start": "2026-05-20T14:00:00+02:00",
                     "end":   "2026-05-20T15:00:00+02:00" },
  "collected_info": { "besoin": "...", "contexte": "...", "entreprise": "..." },
  "escalation_reason": null
}
```

- `email_draft` : toujours rempli (même un mail d'attente en cas d'escalade).
- `proposed_slot` : rempli **uniquement** si `action = confirm_booking`.
- `escalation_reason` : rempli **uniquement** si `action = escalate`.

### State store (n8n Data Table, clé `threadId`)

```text
threadId        (clé)
prospect_email
prospect_name
product         schoolswp | fluentcart | unknown
status          new | awaiting_info | slots_proposed | confirmed | escalated
proposed_slots  JSON, liste de { start, end }
collected_info  JSON
event_id        rempli après création de l'événement
created_at
last_updated
```

### Parcours d'un mail

1. Mail entrant : le trigger extrait `threadId`, expéditeur, objet, corps.
2. Lookup `threadId` : trouvé -> on charge l'état, on saute le classifieur ; inconnu ->
   classifieur (RDV -> crée une ligne `status=new` ; pas RDV -> label + stop).
3. Context loader assemble `{ mail_courant, historique_fil[], etat }` et le passe à l'agent.
4. L'agent appelle `get_calendar_availability` autant que besoin, puis émet le JSON.
5. Switch sur `action` : envoi mail + MAJ état, ou gate.

### Garde-fou sur la donnée

Quand `status = slots_proposed`, les créneaux proposés sont figés dans le state store.
Si le prospect répond « ok mardi 14h », l'agent doit produire un `proposed_slot` qui
appartient à `state.proposed_slots`. La gate revérifie cette appartenance (check 1).
L'agent ne peut donc jamais inventer un créneau non proposé.

## 7. Configuration et garde-fous

### Config (Set node en tête de workflow, valeurs à valider)

| Clé | Défaut proposé | Note |
| --- | --- | --- |
| `CALENDAR_ID` | map `{ schoolswp: "<id Coaching schoolsWP>", fluentcart: "<id Coaching FluentCart>" }` | Un seul compte Google, deux sous-agendas. IDs réels à lire via `gws` une fois l'auth restaurée, ou via le menu déroulant du node Google Calendar |
| `MEET_LINK` | Google Meet auto-généré | lien visio créé automatiquement à la création de l'événement |
| `TIMEZONE` | `Europe/Paris` | |
| `WORKING_DAYS` | lundi à vendredi | |
| `WORKING_HOURS` | 9h - 18h | |
| `SLOT_DURATION` | 60 min | démo produit / formation |
| `BUFFER_MIN` | 24 h | pas de RDV à moins de 24h |
| `HORIZON_MAX` | 4 semaines | pas de RDV au-delà |
| `DISCORD_WEBHOOK` | via `$vars` | jamais hardcodé (convention n8n du projet) |

### Les 5 checks déterministes de la gate [6]

Appliqués avant toute création d'événement :

1. Le créneau appartient à `state.proposed_slots` (anti-invention).
2. Le créneau est **toujours** libre : re-check free/busy juste avant création
   (anti-collision entre proposition et confirmation).
3. Le créneau est dans les jours/heures ouvrés (`WORKING_DAYS`, `WORKING_HOURS`).
4. Le créneau respecte `BUFFER_MIN` et `HORIZON_MAX`.
5. Pas déjà un événement `confirmed` pour ce `prospect_email` (anti-doublon).

Résultats : tout OK -> création. Check 2 échoue -> relance de l'agent avec un flag
`slot_taken`, il re-propose. Checks 1/3/4/5 échouent -> escalade Discord.

### Cas d'escalade

Soit l'agent émet `action=escalate`, soit la gate la déclenche :

- Demande reste floue après 2 relances, ou prospect ne répond pas aux questions.
- Produit reste `unknown` après 2 relances (l'agent ne devine pas dans quel agenda poser
  le RDV).
- Prospect insiste pour un créneau hors heures ouvrées / hors horizon.
- Doublon détecté.
- Ton agressif / hors-sujet passé à travers le classifieur.
- Échec technique d'API.

### Sécurité

- L'agent n'a qu'un outil **lecture seule** : même halluciné, il ne peut pas écrire dans
  l'agenda.
- Pas de webhook public exposé (le déclencheur est un trigger email), donc le pattern
  `WEBHOOK_SECRET` ne s'applique pas ici.
- `DISCORD_WEBHOOK` et crédentiales stockés selon les conventions du projet (n8n
  Variables / credentials, jamais hardcodés).

## 8. Gestion d'erreur

- Branche d'erreur (`Continue On Fail`) sur les nodes critiques (Google Calendar, envoi
  mail) : notif Discord « échec technique », état inchangé.
- **Idempotence** : si l'événement est créé mais le mail de confirmation échoue,
  `event_id` est déjà dans le state store. Un re-run ne recrée pas l'événement (le check 5
  anti-doublon le couvre).
- Faux négatif du classifieur (vrai RDV classé « pas RDV ») : risque accepté, mitigé par
  un **label** plutôt qu'une suppression. Michael garde l'œil dessus.
- JSON malformé en sortie d'agent : intercepté par le node de validation de schéma ->
  escalade. Le workflow ne casse pas.

## 9. Stratégie de test

### Fixtures email (~8 mails types)

| Fixture | Comportement attendu |
| --- | --- |
| Newsletter / partenariat | classifieur -> pas RDV -> label + STOP |
| RDV schoolsWP explicite | `product=schoolswp` |
| RDV FluentCart explicite | `product=fluentcart` |
| RDV produit ambigu | `product=unknown` -> `ask_more_info` |
| « ok mardi 14h » sur fil `slots_proposed` | `confirm_booking` -> event créé |
| Confirme un créneau jamais proposé | gate check 1 bloque -> escalade |
| Demande un créneau samedi 22h | gate check 3 bloque -> escalade |
| Demande un créneau déjà pris | gate check 2 -> relance agent |

### Test de la gate en isolation

Composant critique (action irréversible). Sa logique (les 5 checks) est extraite en
fonction pure et testée : créneau hors `proposed_slots`, créneau occupé, hors heures
ouvrées, dans le buffer 24h, prospect déjà confirmé, et le cas vert. Six assertions,
zéro LLM.

### Validation du contrat de l'agent

Le node de validation de schéma après [4] est testé : un JSON malformé (champ manquant,
`proposed_slot` hors `proposed_slots`) doit bien être rejeté vers escalade.

### Classifieur

Non déterministe : évalué sur 10-15 mails étiquetés à la main. Seuil : 0 faux négatif
sur les RDV évidents (faux positifs tolérés, l'agent rattrape).

### Idempotence

Rejouer le workflow sur un mail d'un fil déjà `confirmed` = no-op (couvert par le check 5).
Test explicite.

### Bout-en-bout en staging

Sur un **agenda de test** (jamais les vrais « Coaching schoolsWP » / « Coaching
FluentCart ») et une boîte mail de test. Le workflow reste `[InTesting]` tant que les 8
fixtures ne sont pas vertes.

### Definition of done

- Les 8 fixtures passent en staging avec le comportement attendu.
- La gate bloque les 5 cas KO et laisse passer le cas OK.
- Aucun événement créé hors des deux agendas de coaching.
- Une escalade Discord arrive bien dans #alerts avec le résumé du fil.
- Rejeu d'un mail confirmé = no-op.
- Le workflow passe de `[InTesting]` à `[Prod]`.

## 10. Points tranchés et restant à provisionner

Points clarifiés au cadrage (2026-05-14) :

- **MX de `michaelkihl.fr`** : pointent vers `mx01/mx02.xcloud.email` (xCloud), pas
  Google Workspace. Trigger = `Email Trigger (IMAP)`, confirmé.
- **Compte Google** : un seul compte Google, les deux agendas « Coaching schoolsWP » et
  « Coaching FluentCart » en sont des sous-agendas. Une seule crédentiale Google Calendar.
- **Ton des mails** : tutoiement (marque schoolsWP).
- **Lien visio** : Google Meet auto-généré à la création de l'événement.

Restant à provisionner avant / pendant l'implémentation :

1. **Auth `gws`** : token OAuth expiré/révoqué (`token_valid: false`). Michael relance
   `gws auth login` (prévu). Une fois fait : lecture des `calendarId` réels des deux
   sous-agendas. Non bloquant pour le plan : le node Google Calendar de n8n permet de
   choisir l'agenda dans un menu déroulant une fois la crédentiale connectée.
2. **Crédentiale IMAP xCloud** : provisionner les paramètres de connexion de
   `contact@michaelkihl.fr` (serveur IMAP xCloud, port, login, mot de passe) dans n8n.

## 11. Conséquences

- Nouveau workflow n8n autonome, sans dépendance webhook entrante.
- Nouvelle n8n Data Table comme state store (premier usage de ce type dans le projet à
  vérifier ; sinon Google Sheet en repli).
- Deux crédentiales à provisionner : IMAP `contact@michaelkihl.fr` et Google Calendar.
- Une n8n Variable supplémentaire (`DISCORD_WEBHOOK` si pas déjà présente).
- Coût LLM par mail : un appel classifieur léger (Haiku) + un ou plusieurs appels agent
  (Sonnet) par tour de conversation. Volume faible attendu (email asynchrone).
- L'agent est stateless et son contrat de sortie est validé : un dérapage du LLM dégrade
  vers une escalade, jamais vers une action erronée dans l'agenda.
