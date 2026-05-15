# Agent RDV Email > Google Agenda - Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construire un workflow n8n qui surveille `contact@michaelkihl.fr`, classe les mails entrants, négocie un créneau de démo par retour de mail via un agent IA, puis crée l'événement Google Agenda dans l'un des deux sous-agendas (Coaching schoolsWP / Coaching FluentCart) après validation par une gate déterministe. Escalade Discord sur cas limites.

**Architecture:** Approche hybride (C) : l'AI Agent gère la conversation avec un seul outil Google Calendar **lecture seule**, émet un JSON structuré. Une gate déterministe (5 checks, code JS testable) valide puis crée l'événement. État conversationnel persisté dans une n8n Data Table indexée sur `threadId`. Voir le design : `docs/superpowers/specs/2026-05-14-agent-rdv-email-google-agenda-design.md`.

**Tech Stack:** n8n 2.53.0 (instance `https://schoolswp-n8n.wp1.host`), Node.js 24 (runner local pour les tests), MCP `n8n-mcp`, AI Agent `@n8n/n8n-nodes-langchain.agent` avec sous-modèle Anthropic (Sonnet pour l'agent, Haiku pour le classifieur), Google Calendar API, IMAP xCloud.

---

## Conventions transversales

Lire ces conventions avant de démarrer une tâche.

- **n8n build via MCP uniquement** : `.claude/rules/n8n-integration.md` et `systems/n8n/CLAUDE.md`. Ne jamais hand-éditer le JSON du workflow. Utiliser `n8n_create_workflow`, `n8n_update_partial_workflow`, `n8n_get_workflow` (MCP `n8n-mcp`).
- **Nom du workflow** : `[InDev] Email contact@ > Google Agenda: Agent RDV démo` jusqu'à validation, puis `[InTesting]`, puis `[Prod]`.
- **typeVersions** : avant d'ajouter chaque node, confirmer la dernière version avec `get_node` (mode=versions) ou `search_nodes`. Confirmées à date côté projet : `code` 2, `set` 3.4, `if` 2.2, `httpRequest` 4.2. Les autres (`emailReadImap`, `googleCalendar`, `googleCalendarTool`, `switch`, `@n8n/n8n-nodes-langchain.agent`, `lmChatAnthropic`) : à confirmer à la volée.
- **Code node task runner** : `$input.all()` / `$input.first()` sont stripés, utiliser `items[0].json`. Pas de `$helpers.httpRequest`. Pour passer des données d'un node non-adjacent, insérer un Set node intermédiaire.
- **Secrets** : `DISCORD_WEBHOOK` et clés API dans n8n Variables, jamais hardcodés. Crédentiales nommées `Service_Environment_Type` (ex : `IMAP_xCloud_Contact_Production`, `GoogleCalendar_Production_OAuth`, `Anthropic_Production_API`).
- **Export du workflow** : à la fin de chaque tâche n8n, exporter via `n8n_get_workflow` et écraser `systems/n8n/workflows/agent-rdv-email.json` (mirror read-only pour version control).
- **Commits** : conventionnels en anglais (`feat:`, `fix:`, `chore:`, `docs:`, `test:`).
- **Pas de em-dash** dans la doc/le code (règle projet).
- **Tutoiement** dans tous les textes utilisateur produits par l'agent.

---

## File Structure

| Chemin | Rôle | Statut |
| --- | --- | --- |
| `systems/n8n/lib/booking-gate.js` | Fonction pure `validateBooking()` (les 5 checks). Importée par les tests ; **copiée verbatim** dans le Code node [6] (n8n ne permet pas `require` local). | À créer |
| `systems/n8n/lib/booking-gate.test.js` | Tests `node:test` couvrant les 5 checks + le cas vert. | À créer |
| `systems/n8n/lib/agent-output-schema.js` | Fonction pure `validateAgentOutput()`. Copiée verbatim dans le node de validation. | À créer |
| `systems/n8n/lib/agent-output-schema.test.js` | Tests `node:test`. | À créer |
| `systems/n8n/workflows/agent-rdv-email.json` | Export JSON du workflow (mirror). | À créer en Task 3, MAJ à chaque tâche n8n |
| `systems/n8n/workflows/agent-rdv-email.README.md` | Doc opérationnelle. | À créer en Task 0 |
| `systems/n8n/fixtures/agent-rdv-email/*.json` | 8 fixtures email. | À créer en Task 10 |

---

## Task 0 : Provisioning et doc opérationnelle

**Files:**
- Create: `systems/n8n/workflows/agent-rdv-email.README.md`

- [ ] **Step 1 : restaurer l'auth `gws` (humain Michael)**

Lancer `gws auth login` puis vérifier `gws auth status` : `token_valid` doit valoir `true`.

- [ ] **Step 2 : lire les calendarId des deux sous-agendas**

Lancer `gws calendar calendarList list --params '{}' --format json` et récupérer les `id` des entries dont `summary` vaut "Coaching schoolsWP" et "Coaching FluentCart". Format : `xxxxxxxxxx@group.calendar.google.com`. Noter pour Step 7.

- [ ] **Step 3 : créer les crédentiales IMAP et SMTP xCloud dans n8n**

Via l'UI n8n (Settings > Credentials > New) :

```text
Crédentiale IMAP
Nom        : IMAP_xCloud_Contact_Production
Host       : mail.xcloud.email          (à confirmer dans le panel xCloud)
Port       : 993
SSL/TLS    : ON
User       : contact@michaelkihl.fr
Password   : <mot de passe IMAP fourni par xCloud>

Crédentiale SMTP (sœur, pour les envois)
Nom        : SMTP_xCloud_Contact_Production
Host       : mail.xcloud.email
Port       : 465  (SSL) ou 587 (STARTTLS)
User/Pass  : mêmes que IMAP
```

Tester avec le bouton "Test connection".

- [ ] **Step 4 : créer la crédentiale Google Calendar OAuth dans n8n**

UI n8n > Credentials > New > Google Calendar OAuth2 API. Client OAuth Google du projet GCP `schoolswp`. Scope : `https://www.googleapis.com/auth/calendar`. Nom : `GoogleCalendar_Production_OAuth`.

- [ ] **Step 5 : confirmer la crédentiale Anthropic**

Vérifier qu'une crédentiale `Anthropic_Production_API` existe. Sinon la créer (UI > New > Anthropic API). Clé : valeur de `ANTHROPIC_API_KEY` (env projet).

- [ ] **Step 6 : créer la n8n Data Table `rdv_threads`**

Via MCP `n8n_manage_datatable` (operation `create`) :

| Colonne | Type | Note |
| --- | --- | --- |
| `threadId` | string | clé, indexée |
| `prospect_email` | string | |
| `prospect_name` | string | |
| `product` | string | `schoolswp` / `fluentcart` / `unknown` |
| `status` | string | `new` / `awaiting_info` / `slots_proposed` / `confirmed` / `escalated` |
| `proposed_slots` | json | liste `[{start,end}]` |
| `collected_info` | json | objet libre |
| `event_id` | string | rempli après création |
| `created_at` | string ISO | |
| `last_updated` | string ISO | |

Si Data Tables indisponibles sur l'instance, replier sur Google Sheets (onglet `rdv_threads`, `matchingColumns: ["threadId"]`). Documenter dans le README.

- [ ] **Step 7 : définir les n8n Variables**

UI n8n > Settings > Variables :

```text
DISCORD_WEBHOOK         = https://discord.com/api/webhooks/<id>/<token>   (canal #alerts schoolsWP-Routines)
CALENDAR_ID_SCHOOLSWP   = <id Coaching schoolsWP>@group.calendar.google.com
CALENDAR_ID_FLUENTCART  = <id Coaching FluentCart>@group.calendar.google.com
WORKING_DAYS            = 1,2,3,4,5
WORKING_START_HOUR      = 9
WORKING_END_HOUR        = 18
BUFFER_HOURS            = 24
HORIZON_DAYS            = 28
TIMEZONE                = Europe/Paris
SLOT_DURATION_MINUTES   = 60
```

- [ ] **Step 8 : créer le README opérationnel**

Écrire `systems/n8n/workflows/agent-rdv-email.README.md` :

```markdown
# Agent RDV Email > Google Agenda

Workflow n8n : prise de RDV démo automatisée par email. Voir le design
spec : `docs/superpowers/specs/2026-05-14-agent-rdv-email-google-agenda-design.md`.

## Prérequis

- Crédentiale IMAP : `IMAP_xCloud_Contact_Production`.
- Crédentiale SMTP : `SMTP_xCloud_Contact_Production`.
- Crédentiale Google Calendar : `GoogleCalendar_Production_OAuth`.
- Crédentiale Anthropic : `Anthropic_Production_API`.
- n8n Variables : DISCORD_WEBHOOK, CALENDAR_ID_SCHOOLSWP, CALENDAR_ID_FLUENTCART,
  WORKING_DAYS, WORKING_START_HOUR, WORKING_END_HOUR, BUFFER_HOURS,
  HORIZON_DAYS, TIMEZONE, SLOT_DURATION_MINUTES.
- n8n Data Table : `rdv_threads`.

## Source de vérité du code

- Gate déterministe : `systems/n8n/lib/booking-gate.js` (testée). Le Code node [6]
  contient une copie verbatim. En cas de modification, modifier la lib, relancer ses
  tests, puis répliquer dans le Code node via la MCP.
- Validateur de sortie agent : `systems/n8n/lib/agent-output-schema.js` (testée).
  Même règle de réplication.

## Statut

- `[InDev]` pendant la construction.
- `[InTesting]` une fois les 8 fixtures vertes en staging.
- `[Prod]` une fois la Definition of Done validée.

## Mirror JSON

`systems/n8n/workflows/agent-rdv-email.json` est un mirror read-only exporté via
`n8n_get_workflow`. Ne jamais hand-éditer. Ne jamais réimporter pour écraser
l'instance vivante.
```

- [ ] **Step 9 : commit du README**

```shell
git add systems/n8n/workflows/agent-rdv-email.README.md
git commit -m "docs(n8n): operational README for booking agent workflow"
```

---

## Task 1 : Gate déterministe - fonction pure et tests

**Files:**
- Create: `systems/n8n/lib/booking-gate.js`
- Create: `systems/n8n/lib/booking-gate.test.js`

- [ ] **Step 1 : écrire les tests d'abord (failing)**

Créer `systems/n8n/lib/booking-gate.test.js` :

```javascript
'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { validateBooking } = require('./booking-gate');

// Référence temporelle : jeudi 14 mai 2026, midi Paris.
const now = '2026-05-14T12:00:00+02:00';

const config = {
  workingDays: [1, 2, 3, 4, 5],
  workingStartHour: 9,
  workingEndHour: 18,
  bufferHours: 24,
  horizonDays: 28,
};

// Mercredi 20 mai 2026, 14h-15h Paris : jour ouvré, en heures, > 24h, < 28 jours.
const validSlot = {
  start: '2026-05-20T14:00:00+02:00',
  end:   '2026-05-20T15:00:00+02:00',
};

test('cas vert : tous les checks passent -> create', () => {
  const r = validateBooking({
    proposedSlot: validSlot,
    proposedSlots: [validSlot],
    busy: [],
    prospectStatus: 'slots_proposed',
    config, now,
  });
  assert.equal(r.ok, true);
  assert.equal(r.action, 'create');
  assert.equal(r.failedCheck, null);
});

test('check 1 : créneau hors proposedSlots -> escalate', () => {
  const r = validateBooking({
    proposedSlot: validSlot,
    proposedSlots: [{
      start: '2026-05-21T10:00:00+02:00',
      end:   '2026-05-21T11:00:00+02:00',
    }],
    busy: [],
    prospectStatus: 'slots_proposed',
    config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 1);
});

test('check 2 : créneau pris depuis la proposition -> reoffer', () => {
  const r = validateBooking({
    proposedSlot: validSlot,
    proposedSlots: [validSlot],
    busy: [{
      start: '2026-05-20T14:30:00+02:00',
      end:   '2026-05-20T15:30:00+02:00',
    }],
    prospectStatus: 'slots_proposed',
    config, now,
  });
  assert.equal(r.action, 'reoffer');
  assert.equal(r.failedCheck, 2);
});

test('check 3 : samedi -> escalate', () => {
  const sat = {
    start: '2026-05-23T14:00:00+02:00',
    end:   '2026-05-23T15:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: sat, proposedSlots: [sat], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 3);
});

test('check 3 : 22h (hors heures ouvrées) -> escalate', () => {
  const late = {
    start: '2026-05-20T22:00:00+02:00',
    end:   '2026-05-20T23:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: late, proposedSlots: [late], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 3);
});

test('check 4 : créneau dans moins de 24h -> escalate', () => {
  const soon = {
    start: '2026-05-14T14:00:00+02:00',
    end:   '2026-05-14T15:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: soon, proposedSlots: [soon], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 4);
});

test('check 4 : créneau au-delà de 28 jours -> escalate', () => {
  const far = {
    start: '2026-07-01T14:00:00+02:00',
    end:   '2026-07-01T15:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: far, proposedSlots: [far], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 4);
});

test('check 5 : fil déjà confirmé (doublon) -> escalate', () => {
  const r = validateBooking({
    proposedSlot: validSlot, proposedSlots: [validSlot], busy: [],
    prospectStatus: 'confirmed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 5);
});
```

- [ ] **Step 2 : lancer les tests, vérifier l'échec**

```shell
node --test systems/n8n/lib/booking-gate.test.js
```

Attendu : échec sur `Cannot find module './booking-gate'`.

- [ ] **Step 3 : écrire la fonction `validateBooking`**

Créer `systems/n8n/lib/booking-gate.js` :

```javascript
'use strict';

/**
 * Validation déterministe pour la gate de réservation (workflow node [6]).
 * Fonction pure : pas d'API n8n, pas de LLM, pas d'I/O. Testable en isolation.
 *
 * Actions :
 *   - 'create'   : tous les checks passent.
 *   - 'reoffer'  : créneau valide mais plus libre -> relancer l'agent.
 *   - 'escalate' : anomalie -> notifier Discord.
 */

function parseWallClock(iso) {
  const m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/.exec(iso);
  if (!m) return null;
  return {
    year: Number(m[1]),
    month: Number(m[2]),
    day: Number(m[3]),
    hour: Number(m[4]),
    minute: Number(m[5]),
  };
}

function isoWeekday(year, month, day) {
  // JS getUTCDay: 0=dim..6=sam. On convertit en ISO 1=lun..7=dim.
  const jsDay = new Date(Date.UTC(year, month - 1, day)).getUTCDay();
  return jsDay === 0 ? 7 : jsDay;
}

function overlaps(aStart, aEnd, bStart, bEnd) {
  return aStart < bEnd && bStart < aEnd;
}

function validateBooking(input) {
  const { proposedSlot, proposedSlots, busy, prospectStatus, config, now } = input;

  // Check 5 : anti-doublon.
  if (prospectStatus === 'confirmed') {
    return {
      ok: false, failedCheck: 5, action: 'escalate',
      reason: 'Thread déjà confirmé : doublon détecté.',
    };
  }

  // Check 1 : appartenance aux créneaux proposés.
  const inOffered = (proposedSlots || []).some(
    (s) => s.start === proposedSlot.start && s.end === proposedSlot.end,
  );
  if (!inOffered) {
    return {
      ok: false, failedCheck: 1, action: 'escalate',
      reason: 'Créneau non présent dans les créneaux proposés.',
    };
  }

  // Check 3 : dans les jours/heures ouvrés.
  const wc = parseWallClock(proposedSlot.start);
  const wcEnd = parseWallClock(proposedSlot.end);
  if (!wc || !wcEnd) {
    return {
      ok: false, failedCheck: 3, action: 'escalate',
      reason: 'Format de date du créneau invalide.',
    };
  }
  const weekday = isoWeekday(wc.year, wc.month, wc.day);
  const startsInHours = wc.hour >= config.workingStartHour && wc.hour < config.workingEndHour;
  const endsInHours =
    wcEnd.hour < config.workingEndHour ||
    (wcEnd.hour === config.workingEndHour && wcEnd.minute === 0);
  if (!config.workingDays.includes(weekday) || !startsInHours || !endsInHours) {
    return {
      ok: false, failedCheck: 3, action: 'escalate',
      reason: 'Créneau hors jours/heures ouvrés.',
    };
  }

  // Check 4 : buffer et horizon.
  const startMs = Date.parse(proposedSlot.start);
  const nowMs = Date.parse(now);
  const hoursAhead = (startMs - nowMs) / 3600000;
  if (hoursAhead < config.bufferHours) {
    return {
      ok: false, failedCheck: 4, action: 'escalate',
      reason: 'Créneau dans le buffer (' + config.bufferHours + 'h).',
    };
  }
  if (hoursAhead > config.horizonDays * 24) {
    return {
      ok: false, failedCheck: 4, action: 'escalate',
      reason: 'Créneau au-delà de l\'horizon (' + config.horizonDays + ' jours).',
    };
  }

  // Check 2 : encore libre ? Sinon reoffer.
  const endMs = Date.parse(proposedSlot.end);
  const taken = (busy || []).some(
    (b) => overlaps(startMs, endMs, Date.parse(b.start), Date.parse(b.end)),
  );
  if (taken) {
    return {
      ok: false, failedCheck: 2, action: 'reoffer',
      reason: 'Créneau occupé entre la proposition et la confirmation.',
    };
  }

  return { ok: true, failedCheck: null, action: 'create', reason: null };
}

module.exports = { validateBooking, parseWallClock, isoWeekday, overlaps };
```

- [ ] **Step 4 : relancer les tests, vérifier qu'ils passent**

```shell
node --test systems/n8n/lib/booking-gate.test.js
```

Attendu : 8 tests OK.

- [ ] **Step 5 : commit**

```shell
git add systems/n8n/lib/booking-gate.js systems/n8n/lib/booking-gate.test.js
git commit -m "feat(n8n): pure booking-gate validator with node:test coverage"
```

---

## Task 2 : Validateur de schéma de la sortie agent

**Files:**
- Create: `systems/n8n/lib/agent-output-schema.js`
- Create: `systems/n8n/lib/agent-output-schema.test.js`

Validation structurelle uniquement. La sémantique `proposed_slot in proposed_slots` vit dans la gate (Task 1, check 1).

- [ ] **Step 1 : écrire les tests**

Créer `systems/n8n/lib/agent-output-schema.test.js` :

```javascript
'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { validateAgentOutput } = require('./agent-output-schema');

test('action=ask_more_info avec email_draft -> valide', () => {
  const r = validateAgentOutput({
    action: 'ask_more_info',
    email_draft: 'Salut, peux-tu me préciser ton besoin ?',
  });
  assert.equal(r.valid, true);
  assert.deepEqual(r.errors, []);
});

test('action=confirm_booking avec proposed_slot ISO -> valide', () => {
  const r = validateAgentOutput({
    action: 'confirm_booking',
    email_draft: 'C\'est confirmé pour mardi.',
    proposed_slot: {
      start: '2026-05-20T14:00:00+02:00',
      end:   '2026-05-20T15:00:00+02:00',
    },
  });
  assert.equal(r.valid, true);
});

test('action=propose_slots avec slots_offered valide', () => {
  const r = validateAgentOutput({
    action: 'propose_slots',
    email_draft: 'Voici mes dispos.',
    slots_offered: [
      { start: '2026-05-20T14:00:00+02:00', end: '2026-05-20T15:00:00+02:00' },
      { start: '2026-05-21T10:00:00+02:00', end: '2026-05-21T11:00:00+02:00' },
    ],
  });
  assert.equal(r.valid, true);
});

test('action=propose_slots sans slots_offered -> invalide', () => {
  const r = validateAgentOutput({
    action: 'propose_slots',
    email_draft: 'Voici mes dispos.',
  });
  assert.equal(r.valid, false);
  assert.ok(r.errors.some((e) => /slots_offered/.test(e)));
});

test('action=escalate sans escalation_reason -> invalide', () => {
  const r = validateAgentOutput({
    action: 'escalate',
    email_draft: 'Je reviens vers toi très vite.',
  });
  assert.equal(r.valid, false);
  assert.ok(r.errors.some((e) => /escalation_reason/.test(e)));
});

test('action=confirm_booking sans proposed_slot -> invalide', () => {
  const r = validateAgentOutput({
    action: 'confirm_booking',
    email_draft: 'OK pour mardi.',
  });
  assert.equal(r.valid, false);
  assert.ok(r.errors.some((e) => /proposed_slot/.test(e)));
});

test('email_draft vide -> invalide', () => {
  const r = validateAgentOutput({
    action: 'ask_more_info',
    email_draft: '   ',
  });
  assert.equal(r.valid, false);
});

test('action inconnue -> invalide', () => {
  const r = validateAgentOutput({
    action: 'send_invoice',
    email_draft: 'Voici la facture.',
  });
  assert.equal(r.valid, false);
});

test('entrée non-objet -> invalide', () => {
  assert.equal(validateAgentOutput(null).valid, false);
  assert.equal(validateAgentOutput('foo').valid, false);
});
```

- [ ] **Step 2 : lancer les tests, vérifier l'échec**

```shell
node --test systems/n8n/lib/agent-output-schema.test.js
```

Attendu : échec import module.

- [ ] **Step 3 : écrire la fonction `validateAgentOutput`**

Créer `systems/n8n/lib/agent-output-schema.js` :

```javascript
'use strict';

/**
 * Validation structurelle du JSON émis par le node AI Agent.
 * Pure : pas d'API n8n. Vérifie la shape uniquement.
 */

const ACTIONS = ['ask_more_info', 'propose_slots', 'confirm_booking', 'escalate'];
const ISO_RE = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2}|Z)$/;

function isIsoSlot(s) {
  return s && typeof s === 'object' && ISO_RE.test(s.start || '') && ISO_RE.test(s.end || '');
}

function validateAgentOutput(obj) {
  const errors = [];
  if (typeof obj !== 'object' || obj === null) {
    return { valid: false, errors: ['Sortie agent absente ou non-objet.'] };
  }
  if (!ACTIONS.includes(obj.action)) {
    errors.push('Champ "action" invalide : ' + JSON.stringify(obj.action) + '.');
  }
  if (typeof obj.email_draft !== 'string' || obj.email_draft.trim() === '') {
    errors.push('Champ "email_draft" manquant ou vide.');
  }
  if (obj.action === 'confirm_booking' && !isIsoSlot(obj.proposed_slot)) {
    errors.push('action=confirm_booking exige proposed_slot.{start,end} au format ISO 8601 avec offset.');
  }
  if (obj.action === 'propose_slots') {
    const slots = obj.slots_offered;
    if (!Array.isArray(slots) || slots.length === 0 || !slots.every(isIsoSlot)) {
      errors.push('action=propose_slots exige slots_offered : tableau non vide de {start,end} ISO.');
    }
  }
  if (obj.action === 'escalate'
      && (typeof obj.escalation_reason !== 'string'
          || obj.escalation_reason.trim() === '')) {
    errors.push('action=escalate exige un "escalation_reason" non vide.');
  }
  return { valid: errors.length === 0, errors };
}

module.exports = { validateAgentOutput, ACTIONS };
```

- [ ] **Step 4 : relancer les tests, vérifier qu'ils passent**

```shell
node --test systems/n8n/lib/agent-output-schema.test.js
```

Attendu : 9 tests OK.

- [ ] **Step 5 : commit**

```shell
git add systems/n8n/lib/agent-output-schema.js systems/n8n/lib/agent-output-schema.test.js
git commit -m "feat(n8n): pure agent-output schema validator with tests"
```

---

## Task 3 : Squelette du workflow + Email Trigger + Thread lookup

**Files:**
- Create (via MCP) : workflow `[InDev] Email contact@ > Google Agenda: Agent RDV démo`
- Create: `systems/n8n/workflows/agent-rdv-email.json` (mirror)

- [ ] **Step 1 : créer le workflow vide**

Via MCP `n8n_create_workflow` :

- name : `[InDev] Email contact@ > Google Agenda: Agent RDV démo`
- description : `Agent IA de prise de RDV démo par email. Lit contact@michaelkihl.fr (IMAP), classe, négocie, valide et crée l'événement dans Coaching schoolsWP ou Coaching FluentCart.`
- active : false

Noter le `workflowId` retourné.

- [ ] **Step 2 : ajouter le node Email Trigger (IMAP)**

Confirmer la typeVersion via `get_node nodeType="nodes-base.emailReadImap" mode="versions"`. Ajouter via `n8n_update_partial_workflow` (operation `addNode`) :

```text
type        : n8n-nodes-base.emailReadImap
name        : Email Trigger (IMAP)
position    : [240, 300]
credentials : { imap: "IMAP_xCloud_Contact_Production" }
parameters  :
  mailbox             : INBOX
  postProcessAction   : nothing
  downloadAttachments : false
  format              : resolved
  options.customEmailConfig : "[\"UNSEEN\"]"
```

- [ ] **Step 3 : ajouter le node Set "Extract Email Fields"**

```text
type        : n8n-nodes-base.set
name        : Extract Email Fields
typeVersion : 3.4
position    : [460, 300]
assignments :
  - threadId    : "={{ $json.headers['message-id'] || $json.messageId }}"
  - fromAddress : "={{ $json.from.value[0].address }}"
  - fromName    : "={{ $json.from.value[0].name }}"
  - subject     : "={{ $json.subject }}"
  - bodyText    : "={{ $json.text }}"
  - inReplyTo   : "={{ $json.headers['in-reply-to'] || '' }}"
  - references  : "={{ $json.headers['references'] || '' }}"
options.includeOtherFields : false
```

- [ ] **Step 4 : ajouter un Code "Normalize ThreadId"**

```text
type        : n8n-nodes-base.code
name        : Normalize ThreadId
typeVersion : 2
position    : [680, 300]
```

JS du Code node :

```javascript
const item = items[0].json;
const refs = (item.references || '').match(/<[^>]+>/g) || [];
const inReply = (item.inReplyTo || '').match(/<[^>]+>/);
const threadId = refs[0] || (inReply && inReply[0]) || item.threadId;
return [{ json: { ...item, threadId } }];
```

- [ ] **Step 5 : ajouter le node Data Table "Lookup Thread"**

```text
operation       : getRow
dataTableName   : rdv_threads
matchingColumns : threadId
threadId        : ={{ $json.threadId }}
onNotFound      : returnEmptyItem
```

Si Data Table indisponible : replier sur Google Sheets > Read Row (sheet `rdv_threads`, matching column `threadId`).

- [ ] **Step 6 : pin data de test sur Email Trigger**

```json
[{
  "from": { "value": [{ "address": "prospect@example.com", "name": "Jane Doe" }] },
  "subject": "Démo schoolsWP",
  "text": "Bonjour, je voudrais voir une démo de schoolsWP.",
  "headers": { "message-id": "<msg-001@example.com>", "in-reply-to": "", "references": "" },
  "messageId": "<msg-001@example.com>"
}]
```

- [ ] **Step 7 : exécuter la chaîne, vérifier**

Sortie attendue après Lookup :

```json
{
  "threadId": "<msg-001@example.com>",
  "fromAddress": "prospect@example.com",
  "fromName": "Jane Doe",
  "subject": "Démo schoolsWP",
  "bodyText": "Bonjour, ...",
  "_dataTableRow": null
}
```

- [ ] **Step 8 : exporter et committer le mirror**

Via `n8n_get_workflow id=<workflowId>` et écraser `systems/n8n/workflows/agent-rdv-email.json`. Puis :

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): bootstrap booking agent workflow with IMAP trigger and thread lookup"
```

---

## Task 4 : Classifieur IA + branchement RDV / pas RDV

**Files:**
- Modify : workflow n8n via MCP
- Modify : `systems/n8n/workflows/agent-rdv-email.json`

- [ ] **Step 1 : ajouter un IF "Thread Already Known"**

```text
type        : n8n-nodes-base.if
name        : Thread Already Known?
typeVersion : 2.2
position    : [900, 300]
conditions  :
  - left  : "={{ $json._dataTableRow }}"
    op    : object notEquals
    right : null
```

- Branch TRUE : connectée plus tard au Context Loader (Task 5).
- Branch FALSE : connectée au classifieur.

- [ ] **Step 2 : ajouter un Chat Model Anthropic (Haiku)**

```text
type        : @n8n/n8n-nodes-langchain.lmChatAnthropic
name        : Haiku (classifier)
position    : [900, 540]
credentials : { anthropicApi: "Anthropic_Production_API" }
parameters.model                       : claude-haiku-4-5-20251001
parameters.options.temperature         : 0
parameters.options.maxTokensToSample   : 200
```

- [ ] **Step 3 : ajouter le node "Classifier" (chainLlm)**

```text
type        : @n8n/n8n-nodes-langchain.chainLlm
name        : Classifier
position    : [1120, 480]
parameters.promptType : define
parameters.text       :
```

Texte du prompt :

```text
Tu classes un email pour décider s'il s'agit d'une demande de prise de rendez-vous
de démo schoolsWP ou FluentCart. Ton seul output est un JSON :

{
  "is_booking_request": true | false,
  "product": "schoolswp" | "fluentcart" | "unknown",
  "confidence": 0.0..1.0
}

Règles :
- "is_booking_request" = true seulement si le mail demande explicitement un rdv,
  un appel, une démo, une présentation, ou propose des disponibilités.
- "product" = "schoolswp" si le mail parle de schoolsWP, plugins WordPress LMS,
  tutorat, formations en ligne. "fluentcart" si le mail parle de FluentCart, e-commerce
  WordPress, checkout. "unknown" sinon.
- Renvoie UNIQUEMENT le JSON.

Email :
Objet : {{ $json.subject }}
De    : {{ $json.fromName }} <{{ $json.fromAddress }}>
Corps :
{{ $json.bodyText }}
```

Connecter `Haiku (classifier)` comme `ai_languageModel`.

- [ ] **Step 4 : ajouter un Code "Parse Classifier"**

```text
type        : n8n-nodes-base.code
name        : Parse Classifier
typeVersion : 2
position    : [1340, 480]
```

```javascript
// Note : dans le contexte n8n, on récupère le node amont via l'expression cross-node de n8n.
// L'expression utilise le dollar suivi de parenthèses ouvrantes (syntaxe n8n).
const upstream = items[0].json._normalize_upstream;
let parsed;
try {
  parsed = JSON.parse(items[0].json.text);
} catch (e) {
  parsed = { is_booking_request: false, product: 'unknown', confidence: 0 };
}
return [{ json: { ...upstream, classifier: parsed } }];
```

Note : `_normalize_upstream` est posé en amont par un Set node qui copie la sortie de "Normalize ThreadId" dans une clé qui survit au chainLlm. Cette indirection est nécessaire car la sortie du chainLlm écrase l'item courant. Concrètement : insérer entre "Thread Already Known? FALSE" et le Classifier un Set node "Carry Email Fields" qui place tout l'item courant sous la clé `_normalize_upstream`.

- [ ] **Step 5 : ajouter un IF "Is Booking Request?"**

```text
type        : n8n-nodes-base.if
name        : Is Booking Request?
typeVersion : 2.2
position    : [1560, 480]
conditions:
  - left  : "={{ $json.classifier.is_booking_request }}"
    op    : boolean equals
    right : true
```

- Branch TRUE : créer une ligne dans `rdv_threads` (Step 6) puis Context Loader.
- Branch FALSE : "Move to NotRDV folder" puis STOP.

- [ ] **Step 6 : ajouter "Create Thread Row"**

```text
operation     : addRow
dataTableName : rdv_threads
values:
  threadId       : "={{ $json.threadId }}"
  prospect_email : "={{ $json.fromAddress }}"
  prospect_name  : "={{ $json.fromName }}"
  product        : "={{ $json.classifier.product }}"
  status         : "new"
  proposed_slots : "[]"
  collected_info : "{}"
  event_id       : ""
  created_at     : "={{ $now.toISO() }}"
  last_updated   : "={{ $now.toISO() }}"
```

- [ ] **Step 7 : déplacer les mails non-RDV**

Si le node IMAP de déplacement n'est pas exposé nativement, replier sur un NoOp + un filtre serveur xCloud (cPanel > Filtres) qui déplace les mails traités dans un dossier `non-rdv`. Documenter ce repli dans le README.

- [ ] **Step 8 : pin data et tests des deux branches**

Fixture A (RDV schoolsWP explicite) :

```json
{
  "threadId": "<msg-002@example.com>",
  "fromAddress": "prospect@a.test",
  "fromName": "Alice",
  "subject": "Démo schoolsWP",
  "bodyText": "Bonjour, j'aimerais voir une démo de schoolsWP la semaine prochaine.",
  "_dataTableRow": null
}
```

Attendu : `classifier.is_booking_request=true`, `classifier.product="schoolswp"`, ligne créée.

Fixture B (newsletter) :

```json
{
  "threadId": "<msg-003@example.com>",
  "fromAddress": "news@partner.test",
  "fromName": "Partner",
  "subject": "Notre newsletter de mai",
  "bodyText": "Découvrez nos nouveautés ce mois-ci...",
  "_dataTableRow": null
}
```

Attendu : `classifier.is_booking_request=false`, branche STOP, aucune ligne créée.

- [ ] **Step 9 : exporter et commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): add classifier branch with product detection"
```

---

## Task 5 : Context Loader

**Files:**
- Modify : workflow n8n via MCP
- Modify : `systems/n8n/workflows/agent-rdv-email.json`

- [ ] **Step 1 : ajouter le Code "Build Context"**

```text
type        : n8n-nodes-base.code
name        : Build Context
typeVersion : 2
position    : [1780, 380]
```

```javascript
const item = items[0].json;

// Côté "Thread Already Known", state est dans _dataTableRow.
// Côté "Create Thread Row", on a une ligne fraîche -> état "new".
const state = item._dataTableRow || {
  threadId: item.threadId,
  prospect_email: item.fromAddress,
  prospect_name: item.fromName,
  product: item.classifier ? item.classifier.product : 'unknown',
  status: 'new',
  proposed_slots: [],
  collected_info: {},
  event_id: '',
};

// Reconstitution naïve de l'historique : on coupe sur "Le ... a écrit :" ou "On ... wrote:".
const body = item.bodyText || '';
const sep = /\n[\s>]*(?:Le |On )[^\n]*(?:a écrit|wrote)\s*:\s*\n/;
const parts = body.split(sep).map((p) => p.replace(/^>\s?/gm, '').trim()).filter(Boolean);
const latest = parts[0] || body;
const history = parts.slice(1);

return [{
  json: {
    threadId: item.threadId,
    state,
    mail_courant: {
      from: item.fromAddress,
      name: item.fromName,
      subject: item.subject,
      body: latest,
    },
    historique_fil: history,
  },
}];
```

- [ ] **Step 2 : connecter Build Context aux deux branches amont**

- "Thread Already Known? TRUE" -> Build Context.
- "Create Thread Row" (branche classifier TRUE) -> Build Context.

- [ ] **Step 3 : pin data et test**

```json
{
  "threadId": "<msg-002@example.com>",
  "fromAddress": "prospect@a.test",
  "fromName": "Alice",
  "subject": "Re: Démo schoolsWP",
  "bodyText": "Parfait, le mardi 20 mai à 14h me va.\n\nLe 14 mai 2026, contact@michaelkihl.fr a écrit :\n> Voici mes créneaux dispos...",
  "_dataTableRow": {
    "threadId": "<msg-002@example.com>",
    "prospect_email": "prospect@a.test",
    "prospect_name": "Alice",
    "product": "schoolswp",
    "status": "slots_proposed",
    "proposed_slots": [
      {"start":"2026-05-20T14:00:00+02:00","end":"2026-05-20T15:00:00+02:00"}
    ],
    "collected_info": {"besoin": "démo schoolsWP"},
    "event_id": ""
  }
}
```

Attendu : `state.status = "slots_proposed"`, `state.proposed_slots.length === 1`, `mail_courant.body` commence par "Parfait...", `historique_fil.length === 1`.

- [ ] **Step 4 : export + commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): context loader assembles thread state and history"
```

---

## Task 6 : AI Agent + outil Calendar lecture seule + validateur de schéma

**Files:**
- Modify : workflow n8n via MCP
- Modify : `systems/n8n/workflows/agent-rdv-email.json`

- [ ] **Step 1 : ajouter un Chat Model Anthropic (Sonnet)**

```text
type        : @n8n/n8n-nodes-langchain.lmChatAnthropic
name        : Sonnet (agent)
position    : [1780, 620]
credentials : { anthropicApi: "Anthropic_Production_API" }
parameters.model                       : claude-sonnet-4-6
parameters.options.temperature         : 0.3
parameters.options.maxTokensToSample   : 1500
```

- [ ] **Step 2 : ajouter l'outil Google Calendar (Tool variant, lecture seule)**

Confirmer la version via `get_node nodeType="nodes-base.googleCalendarTool" mode="versions"`.

```text
type        : n8n-nodes-base.googleCalendarTool
name        : Calendar Availability (read-only)
position    : [2000, 620]
credentials : { googleCalendarOAuth2Api: "GoogleCalendar_Production_OAuth" }
parameters.resource           : event
parameters.operation          : getAll
parameters.calendar           : "={{ $json.state.product === 'fluentcart' ? $vars.CALENDAR_ID_FLUENTCART : $vars.CALENDAR_ID_SCHOOLSWP }}"
parameters.toolDescription    : "Get busy time ranges for the calendar matching the prospect's product (schoolsWP or FluentCart). Returns a list of events with start/end. Use this to find free slots. READ ONLY: never create events."
parameters.options.timeMin    : passed by the agent dynamically
parameters.options.timeMax    : passed by the agent dynamically
```

Le node `googleCalendarTool` n'expose pas d'opération `create` au tool : c'est le garde-fou structurel.

- [ ] **Step 3 : ajouter le node "AI Agent"**

Confirmer la version via `get_node nodeType="nodes-langchain.agent" mode="versions"`.

```text
type        : @n8n/n8n-nodes-langchain.agent
name        : RDV Agent
position    : [2000, 380]
parameters.agent : toolsAgent     (ou conversationalAgent selon version)
parameters.options.systemMessage :
```

Texte du system message :

```text
Tu es l'assistant de prise de rendez-vous démo de schoolsWP / FluentCart, propriété de Michael KIHL.
Tu réponds aux prospects par email en français, au tutoiement (cohérent avec la marque schoolsWP).
Ta seule mission : caler un créneau de démo de 60 minutes, en jours/heures ouvrés (lundi-vendredi, 9h-18h Europe/Paris), entre 24h et 28 jours à partir d'aujourd'hui.

Tu disposes d'un seul outil : "Calendar Availability (read-only)". Tu l'utilises pour vérifier les créneaux libres. Tu ne peux PAS créer d'événement toi-même : c'est une étape déterministe qui suit ta réponse.

Tu reçois en entrée un objet JSON :
{
  "threadId": "...",
  "state": { "status": "...", "product": "schoolswp|fluentcart|unknown", "proposed_slots": [...], "collected_info": {...} },
  "mail_courant": { "from", "name", "subject", "body" },
  "historique_fil": [ "...", "..." ]
}

Tu DOIS produire UNIQUEMENT un JSON valide (rien d'autre, pas de markdown autour) :

{
  "action": "ask_more_info" | "propose_slots" | "confirm_booking" | "escalate",
  "email_draft": "corps texte du mail de réponse (français, tutoiement)",
  "proposed_slot": { "start": "ISO8601+offset", "end": "ISO8601+offset" },     // SI action=confirm_booking
  "slots_offered": [ { "start": "...", "end": "..." }, ... ],                   // SI action=propose_slots
  "collected_info": { "besoin": "...", "contexte": "...", "entreprise": "..." },
  "escalation_reason": "string"                                                 // SI action=escalate
}

Règles :
- Si product="unknown", commence par demander de quoi parle la démo. action="ask_more_info".
- Si tu n'as pas encore le besoin/contexte/entreprise, demande-les. action="ask_more_info".
- Quand tu as assez d'info, propose 3 créneaux distincts dans les jours/heures ouvrés. action="propose_slots", slots_offered renseigné. Ne propose JAMAIS un créneau occupé (vérifie avec l'outil) ni hors heures/jours ouvrés.
- Si le prospect choisit un créneau parmi state.proposed_slots, action="confirm_booking" et proposed_slot doit être EXACTEMENT l'un des state.proposed_slots.
- Si la demande devient floue, agressive, hors-sujet, ou si après 2 relances tu n'as toujours pas d'info, action="escalate" avec une escalation_reason claire.
- email_draft est toujours rempli (en cas d'escalade, c'est un mail d'attente).
```

Connecter `Sonnet (agent)` en `ai_languageModel`, `Calendar Availability (read-only)` en `ai_tool`.

- [ ] **Step 4 : ajouter un Code "Validate Agent Output"**

```text
type        : n8n-nodes-base.code
name        : Validate Agent Output
typeVersion : 2
position    : [2220, 380]
```

Coller la fonction `validateAgentOutput` de `systems/n8n/lib/agent-output-schema.js` (Task 2) verbatim, puis le harnais :

```javascript
'use strict';
// ===== begin systems/n8n/lib/agent-output-schema.js (copie verbatim) =====
const ACTIONS = ['ask_more_info', 'propose_slots', 'confirm_booking', 'escalate'];
const ISO_RE = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}([+-]\d{2}:\d{2}|Z)$/;
function isIsoSlot(s) {
  return s && typeof s === 'object' && ISO_RE.test(s.start || '') && ISO_RE.test(s.end || '');
}
function validateAgentOutput(obj) {
  const errors = [];
  if (typeof obj !== 'object' || obj === null) {
    return { valid: false, errors: ['Sortie agent absente ou non-objet.'] };
  }
  if (!ACTIONS.includes(obj.action)) {
    errors.push('Champ "action" invalide : ' + JSON.stringify(obj.action) + '.');
  }
  if (typeof obj.email_draft !== 'string' || obj.email_draft.trim() === '') {
    errors.push('Champ "email_draft" manquant ou vide.');
  }
  if (obj.action === 'confirm_booking' && !isIsoSlot(obj.proposed_slot)) {
    errors.push('action=confirm_booking exige proposed_slot.{start,end} au format ISO 8601 avec offset.');
  }
  if (obj.action === 'propose_slots') {
    const slots = obj.slots_offered;
    if (!Array.isArray(slots) || slots.length === 0 || !slots.every(isIsoSlot)) {
      errors.push('action=propose_slots exige slots_offered : tableau non vide de {start,end} ISO.');
    }
  }
  if (obj.action === 'escalate'
      && (typeof obj.escalation_reason !== 'string'
          || obj.escalation_reason.trim() === '')) {
    errors.push('action=escalate exige un "escalation_reason" non vide.');
  }
  return { valid: errors.length === 0, errors };
}
// ===== end copy =====

// Note : les expressions cross-node n8n utilisent le dollar suivi de parens (syntaxe n8n).
// Ici on lit le contexte produit par "Build Context" et la sortie brute de l'AI Agent.
const ctx = items[0].json._ctx_from_build_context;  // posé par un Set "Carry Context" amont
let parsed;
try {
  parsed = JSON.parse(items[0].json.output || items[0].json.text);
} catch (e) {
  return [{ json: { ...ctx, agent_output: null, valid: false, errors: ['JSON inparsable: ' + e.message] } }];
}
const v = validateAgentOutput(parsed);
return [{ json: { ...ctx, agent_output: parsed, valid: v.valid, errors: v.errors } }];
```

Insérer en amont de l'AI Agent un Set "Carry Context" qui copie l'item courant sous la clé `_ctx_from_build_context` (même pattern qu'en Task 4 Step 4).

- [ ] **Step 5 : ajouter un IF "Agent Output Valid?"**

```text
type        : n8n-nodes-base.if
name        : Agent Output Valid?
typeVersion : 2.2
conditions  :
  - left  : "={{ $json.valid }}"
    op    : boolean equals
    right : true
```

- TRUE : Switch (Task 7).
- FALSE : escalade Discord (Task 9) avec `escalation_reason = "JSON agent invalide : " + errors.join('; ')`.

- [ ] **Step 6 : pin data et test**

Pin une sortie agent valide pour tester sans appeler le LLM :

```json
[{
  "output": "{\"action\":\"propose_slots\",\"email_draft\":\"Salut, voici 3 créneaux ...\",\"slots_offered\":[{\"start\":\"2026-05-20T14:00:00+02:00\",\"end\":\"2026-05-20T15:00:00+02:00\"}],\"collected_info\":{\"besoin\":\"démo schoolsWP\"}}"
}]
```

Attendu : `valid=true`. Puis JSON invalide :

```json
[{ "output": "{\"action\":\"send_invoice\",\"email_draft\":\"...\"}" }]
```

Attendu : `valid=false`, `errors` contient "action invalide".

- [ ] **Step 7 : export + commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): AI Agent with read-only calendar tool and schema validation"
```

---

## Task 7 : Switch + branches d'envoi mail (ask_more_info / propose_slots) + MAJ état

**Files:**
- Modify : workflow n8n via MCP
- Modify : `systems/n8n/workflows/agent-rdv-email.json`

- [ ] **Step 1 : ajouter le Switch "Action Router"**

```text
type        : n8n-nodes-base.switch
name        : Action Router
typeVersion : 3   (confirmer via get_node)
parameters.mode : rules
rules :
  - left: "={{ $json.agent_output.action }}", op: equals, right: "ask_more_info"   -> output 0
  - left: "={{ $json.agent_output.action }}", op: equals, right: "propose_slots"   -> output 1
  - left: "={{ $json.agent_output.action }}", op: equals, right: "confirm_booking" -> output 2
  - left: "={{ $json.agent_output.action }}", op: equals, right: "escalate"        -> output 3
```

- [ ] **Step 2 : branche ask_more_info -> Send Email**

```text
type        : n8n-nodes-base.emailSend
name        : Send (ask_more_info)
typeVersion : 2.1   (confirmer)
credentials : { smtp: "SMTP_xCloud_Contact_Production" }
parameters  :
  fromEmail        : contact@michaelkihl.fr
  fromName         : Michael KIHL
  toEmail          : "={{ $json.mail_courant.from }}"
  subject          : "={{ 'Re: ' + $json.mail_courant.subject }}"
  text             : "={{ $json.agent_output.email_draft }}"
  options.replyTo  : "={{ $json.threadId }}"
```

- [ ] **Step 3 : branche ask_more_info -> Update Thread Row (status=awaiting_info)**

```text
operation       : updateRow
dataTableName   : rdv_threads
matchingColumns : threadId
values:
  threadId       : "={{ $json.threadId }}"
  status         : "awaiting_info"
  collected_info : "={{ JSON.stringify({ ...$json.state.collected_info, ...$json.agent_output.collected_info }) }}"
  last_updated   : "={{ $now.toISO() }}"
```

- [ ] **Step 4 : branche propose_slots -> Send Email + Update Row**

Send Email identique au Step 2.

Update Row :

```text
operation       : updateRow
dataTableName   : rdv_threads
matchingColumns : threadId
values:
  threadId       : "={{ $json.threadId }}"
  status         : "slots_proposed"
  proposed_slots : "={{ JSON.stringify($json.agent_output.slots_offered) }}"
  collected_info : "={{ JSON.stringify({ ...$json.state.collected_info, ...$json.agent_output.collected_info }) }}"
  last_updated   : "={{ $now.toISO() }}"
```

- [ ] **Step 5 : tests des deux branches en pin data**

Pin ask_more_info :

```json
[{ "agent_output": { "action": "ask_more_info", "email_draft": "Salut, peux-tu me préciser le besoin ?", "collected_info": {} }, "valid": true, "state": {"collected_info":{}}, "threadId":"<t1>", "mail_courant":{"from":"x@y.test","subject":"Démo"} }]
```

Attendu : mail envoyé, row `status=awaiting_info`.

Pin propose_slots :

```json
[{ "agent_output": { "action": "propose_slots", "email_draft": "Voici 3 créneaux ...", "slots_offered": [{"start":"2026-05-20T14:00:00+02:00","end":"2026-05-20T15:00:00+02:00"},{"start":"2026-05-21T10:00:00+02:00","end":"2026-05-21T11:00:00+02:00"},{"start":"2026-05-22T15:00:00+02:00","end":"2026-05-22T16:00:00+02:00"}], "collected_info": {"besoin":"démo schoolsWP"} }, "valid": true, "state": {"collected_info":{}}, "threadId":"<t1>", "mail_courant":{"from":"x@y.test","subject":"Démo"} }]
```

Attendu : mail envoyé, row `status=slots_proposed`, `proposed_slots` à 3 entrées.

- [ ] **Step 6 : export + commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): switch and send branches for ask_more_info and propose_slots"
```

---

## Task 8 : Booking Gate + Calendar Create + mail de confirmation

**Files:**
- Modify : workflow n8n via MCP
- Modify : `systems/n8n/workflows/agent-rdv-email.json`

- [ ] **Step 1 : ajouter "Get FreeBusy" (Google Calendar)**

Sur la branche confirm_booking :

```text
type        : n8n-nodes-base.googleCalendar
name        : Get FreeBusy
typeVersion : confirmer via get_node
credentials : { googleCalendarOAuth2Api: "GoogleCalendar_Production_OAuth" }
parameters.resource           : event
parameters.operation          : getAll
parameters.calendar           : "={{ $json.state.product === 'fluentcart' ? $vars.CALENDAR_ID_FLUENTCART : $vars.CALENDAR_ID_SCHOOLSWP }}"
parameters.options.timeMin    : "={{ $json.agent_output.proposed_slot.start }}"
parameters.options.timeMax    : "={{ $json.agent_output.proposed_slot.end }}"
parameters.options.singleEvents : true
```

- [ ] **Step 2 : ajouter le Code "Booking Gate"**

```text
type        : n8n-nodes-base.code
name        : Booking Gate
typeVersion : 2
```

Coller `validateBooking` de Task 1 verbatim, puis le harnais :

```javascript
'use strict';
// ===== begin systems/n8n/lib/booking-gate.js (copie verbatim) =====
function parseWallClock(iso) {
  const m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/.exec(iso);
  if (!m) return null;
  return { year: Number(m[1]), month: Number(m[2]), day: Number(m[3]), hour: Number(m[4]), minute: Number(m[5]) };
}
function isoWeekday(year, month, day) {
  const jsDay = new Date(Date.UTC(year, month - 1, day)).getUTCDay();
  return jsDay === 0 ? 7 : jsDay;
}
function overlaps(aStart, aEnd, bStart, bEnd) { return aStart < bEnd && bStart < aEnd; }
function validateBooking(input) {
  const { proposedSlot, proposedSlots, busy, prospectStatus, config, now } = input;
  if (prospectStatus === 'confirmed') {
    return { ok: false, failedCheck: 5, action: 'escalate', reason: 'Thread déjà confirmé : doublon détecté.' };
  }
  const inOffered = (proposedSlots || []).some(
    (s) => s.start === proposedSlot.start && s.end === proposedSlot.end,
  );
  if (!inOffered) {
    return { ok: false, failedCheck: 1, action: 'escalate', reason: 'Créneau non présent dans les créneaux proposés.' };
  }
  const wc = parseWallClock(proposedSlot.start);
  const wcEnd = parseWallClock(proposedSlot.end);
  if (!wc || !wcEnd) {
    return { ok: false, failedCheck: 3, action: 'escalate', reason: 'Format de date du créneau invalide.' };
  }
  const weekday = isoWeekday(wc.year, wc.month, wc.day);
  const startsInHours = wc.hour >= config.workingStartHour && wc.hour < config.workingEndHour;
  const endsInHours = wcEnd.hour < config.workingEndHour
    || (wcEnd.hour === config.workingEndHour && wcEnd.minute === 0);
  if (!config.workingDays.includes(weekday) || !startsInHours || !endsInHours) {
    return { ok: false, failedCheck: 3, action: 'escalate', reason: 'Créneau hors jours/heures ouvrés.' };
  }
  const startMs = Date.parse(proposedSlot.start);
  const nowMs = Date.parse(now);
  const hoursAhead = (startMs - nowMs) / 3600000;
  if (hoursAhead < config.bufferHours) {
    return { ok: false, failedCheck: 4, action: 'escalate', reason: 'Créneau dans le buffer (' + config.bufferHours + 'h).' };
  }
  if (hoursAhead > config.horizonDays * 24) {
    return { ok: false, failedCheck: 4, action: 'escalate', reason: 'Créneau au-delà de l\'horizon (' + config.horizonDays + ' jours).' };
  }
  const endMs = Date.parse(proposedSlot.end);
  const taken = (busy || []).some(
    (b) => overlaps(startMs, endMs, Date.parse(b.start), Date.parse(b.end)),
  );
  if (taken) {
    return { ok: false, failedCheck: 2, action: 'reoffer', reason: 'Créneau occupé entre la proposition et la confirmation.' };
  }
  return { ok: true, failedCheck: null, action: 'create', reason: null };
}
// ===== end copy =====

// Lecture du contexte via Set node amont qui aura copié le résultat de "Validate Agent Output"
// et la liste busy de "Get FreeBusy" dans des clés survivantes (_ctx, _busy).
const ctx = items[0].json._ctx;
const busy = items[0].json._busy;

const config = {
  workingDays: $vars.WORKING_DAYS.split(',').map(Number),
  workingStartHour: Number($vars.WORKING_START_HOUR),
  workingEndHour: Number($vars.WORKING_END_HOUR),
  bufferHours: Number($vars.BUFFER_HOURS),
  horizonDays: Number($vars.HORIZON_DAYS),
};

const result = validateBooking({
  proposedSlot: ctx.agent_output.proposed_slot,
  proposedSlots: ctx.state.proposed_slots,
  busy,
  prospectStatus: ctx.state.status,
  config,
  now: new Date().toISOString(),
});

return [{ json: { ...ctx, gate: result } }];
```

Insérer en amont un Set "Carry Gate Inputs" qui pose `_ctx` (sortie de "Validate Agent Output") et `_busy` (sortie aplatie de "Get FreeBusy" : `items.map(it => ({ start: it.json.start.dateTime, end: it.json.end.dateTime }))`).

- [ ] **Step 3 : Switch "Gate Result"**

```text
type        : n8n-nodes-base.switch
name        : Gate Result
rules :
  - left: "={{ $json.gate.action }}", op: equals, right: "create"   -> output 0
  - left: "={{ $json.gate.action }}", op: equals, right: "reoffer"  -> output 1
  - left: "={{ $json.gate.action }}", op: equals, right: "escalate" -> output 2
```

- [ ] **Step 4 : branche create -> Google Calendar Create Event**

```text
type        : n8n-nodes-base.googleCalendar
name        : Create Event
parameters.resource           : event
parameters.operation          : create
parameters.calendar           : "={{ $json.state.product === 'fluentcart' ? $vars.CALENDAR_ID_FLUENTCART : $vars.CALENDAR_ID_SCHOOLSWP }}"
parameters.start              : "={{ $json.agent_output.proposed_slot.start }}"
parameters.end                : "={{ $json.agent_output.proposed_slot.end }}"
parameters.summary            : "={{ 'Démo ' + ($json.state.product === 'fluentcart' ? 'FluentCart' : 'schoolsWP') + ' - ' + $json.state.prospect_name }}"
parameters.description        : "={{ 'Prospect : ' + $json.state.prospect_email + '\\n\\nBesoin : ' + (JSON.parse($json.state.collected_info || '{}').besoin || '-') }}"
parameters.attendees          : "={{ [$json.state.prospect_email] }}"
parameters.additionalFields.conferenceData : true
parameters.additionalFields.sendUpdates    : all
```

- [ ] **Step 5 : branche create -> Send Email (confirmation)**

```text
type        : n8n-nodes-base.emailSend
name        : Send (confirmation)
parameters.toEmail         : "={{ $json.state.prospect_email }}"
parameters.subject         : "={{ 'Re: ' + $json.mail_courant.subject }}"
parameters.text            : "={{ $json.agent_output.email_draft }}"
parameters.options.replyTo : "={{ $json.threadId }}"
```

- [ ] **Step 6 : branche create -> Update Thread Row (status=confirmed, event_id)**

Insérer un Set "Carry Event Id" qui pose `_event_id` (sortie de "Create Event"), puis :

```text
operation       : updateRow
dataTableName   : rdv_threads
matchingColumns : threadId
values:
  threadId     : "={{ $json.threadId }}"
  status       : "confirmed"
  event_id     : "={{ $json._event_id }}"
  last_updated : "={{ $now.toISO() }}"
```

- [ ] **Step 7 : branche reoffer -> Code "Compute Reoffer Slots" + Send Email**

```javascript
const ctx = items[0].json._ctx;
const busy = items[0].json._busy;
const taken = ctx.agent_output.proposed_slot;
function overlapsBusy(slot) {
  return busy.some((b) =>
    Date.parse(slot.start) < Date.parse(b.end)
    && Date.parse(b.start) < Date.parse(slot.end),
  );
}
const remaining = (ctx.state.proposed_slots || []).filter(
  (s) => !(s.start === taken.start && s.end === taken.end) && !overlapsBusy(s),
);
return [{ json: { ...ctx, remaining_slots: remaining } }];
```

IF `remaining_slots.length >= 1` :
- TRUE : Send Email (corps "Désolé, ce créneau vient d'être pris ; en voici d'autres : " + liste formatée), Update Thread Row (`status=slots_proposed`, `proposed_slots=remaining`).
- FALSE : route vers Build Escalation Payload (Task 9) avec `escalation_reason="Tous les créneaux proposés sont occupés."`.

- [ ] **Step 8 : branche escalate -> Task 9**

Connecter la sortie `escalate` du Switch "Gate Result" à Build Escalation Payload en propageant `escalation_reason = $json.gate.reason`.

- [ ] **Step 9 : test bout en bout sur calendar de test**

Provisionner un agenda Google "TEST - Coaching schoolsWP", pointer temporairement `CALENDAR_ID_SCHOOLSWP` n8n Variable dessus. Pin data :

```json
{
  "threadId": "<msg-002@example.com>",
  "state": { "status":"slots_proposed", "product":"schoolswp", "proposed_slots":[{"start":"2026-05-20T14:00:00+02:00","end":"2026-05-20T15:00:00+02:00"}], "prospect_email":"prospect@a.test", "prospect_name":"Alice", "collected_info":"{\"besoin\":\"démo schoolsWP\"}" },
  "agent_output": { "action":"confirm_booking", "email_draft":"C'est confirmé, à mardi 14h. Tu recevras l'invitation Google Calendar.", "proposed_slot":{"start":"2026-05-20T14:00:00+02:00","end":"2026-05-20T15:00:00+02:00"} },
  "valid": true,
  "mail_courant": {"from":"prospect@a.test","subject":"Re: Démo schoolsWP"}
}
```

Attendu :
- `gate.action = "create"`
- Event créé dans le calendar test, avec lien Meet, prospect en invité
- Mail de confirmation reçu (boîte test)
- Row mise à jour : `status=confirmed`, `event_id` non vide
- Re-pin de la même fixture -> `gate.action = "escalate"` (check 5 doublon)

Remettre `CALENDAR_ID_SCHOOLSWP` sur le vrai agenda après ce test.

- [ ] **Step 10 : export + commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): booking gate + calendar event creation + reoffer fallback"
```

---

## Task 9 : Escalade Discord + branches d'erreur technique

**Files:**
- Modify : workflow n8n via MCP
- Modify : `systems/n8n/workflows/agent-rdv-email.json`

- [ ] **Step 1 : ajouter un Set "Build Escalation Payload"**

```text
type        : n8n-nodes-base.set
name        : Build Escalation Payload
typeVersion : 3.4
assignments :
  - reason       : "={{ $json.agent_output.escalation_reason || $json.gate.reason || ($json.errors || []).join('; ') || 'Erreur technique' }}"
  - thread_url   : "(n8n) workflowId={{ $workflow.id }}, threadId={{ $json.threadId }}"
  - prospect     : "={{ $json.state.prospect_name }} <{{ $json.state.prospect_email }}>"
  - product      : "={{ $json.state.product }}"
  - last_message : "={{ ($json.mail_courant && $json.mail_courant.body || '').slice(0, 500) }}"
```

- [ ] **Step 2 : ajouter un HTTP Request "Discord Webhook"**

```text
type        : n8n-nodes-base.httpRequest
name        : Discord Webhook
typeVersion : 4.2
parameters.method          : POST
parameters.url             : "={{ $vars.DISCORD_WEBHOOK }}"
parameters.sendHeaders     : true
parameters.headerParameters.parameters : [ { name: "Content-Type", value: "application/json" } ]
parameters.sendBody        : true
parameters.bodyContentType : json
parameters.jsonBody        :
```

Corps JSON :

```json
{
  "username": "RDV Agent",
  "embeds": [{
    "title": "Escalade prise de RDV",
    "color": 16753920,
    "fields": [
      { "name": "Raison",       "value": "={{ $json.reason }}",       "inline": false },
      { "name": "Prospect",     "value": "={{ $json.prospect }}",     "inline": true  },
      { "name": "Produit",      "value": "={{ $json.product }}",      "inline": true  },
      { "name": "Thread",       "value": "={{ $json.thread_url }}",   "inline": false },
      { "name": "Dernier mail", "value": "={{ $json.last_message }}", "inline": false }
    ]
  }]
}
```

- [ ] **Step 3 : ajouter "Send (holding reply)"**

Insérer en amont un Set "Carry Holding Inputs" qui pose `_to_email` (extrait depuis `prospect`) et `_subject` (extrait du contexte amont) :

```text
type        : n8n-nodes-base.emailSend
name        : Send (holding reply)
parameters.toEmail : "={{ $json._to_email }}"
parameters.subject : "={{ 'Re: ' + $json._subject }}"
parameters.text    : "Salut, je reviens vers toi très vite. \n-- Michael"
```

- [ ] **Step 4 : Update Thread Row (status=escalated)**

```text
operation       : updateRow
dataTableName   : rdv_threads
matchingColumns : threadId
values:
  threadId     : "={{ $json.threadId }}"
  status       : "escalated"
  last_updated : "={{ $now.toISO() }}"
```

- [ ] **Step 5 : connecter toutes les sources d'escalade à Build Escalation Payload**

- "Action Router" output `escalate` -> Build Escalation Payload.
- "Agent Output Valid?" branche FALSE -> Build Escalation Payload.
- "Gate Result" output `escalate` -> Build Escalation Payload.
- Reoffer / no slots remaining branche FALSE -> Build Escalation Payload.

- [ ] **Step 6 : branches d'erreur technique**

Sur chaque node critique (Google Calendar Create Event, emailSend confirmation, Data Table updateRow status=confirmed), activer "Continue On Fail" et router la sortie d'erreur vers Build Escalation Payload (préfixer `reason` avec "Erreur technique : ").

- [ ] **Step 7 : test en pin data**

Pin un payload avec `valid=false` :

```json
[{
  "threadId":"<msg-x>","state":{"prospect_email":"x@x.test","prospect_name":"X","product":"schoolswp"},
  "mail_courant":{"body":"texte","subject":"sujet"},
  "valid":false, "errors":["JSON inparsable: Unexpected token"]
}]
```

Attendu : message Discord dans #alerts avec "Raison : JSON inparsable...", mail d'attente envoyé, row `status=escalated`.

- [ ] **Step 8 : export + commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json
git commit -m "feat(n8n): unified Discord escalation hub and technical error branches"
```

---

## Task 10 : Fixtures email pour tests d'intégration

**Files:**
- Create: `systems/n8n/fixtures/agent-rdv-email/01-newsletter.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/02-rdv-schoolswp.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/03-rdv-fluentcart.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/04-rdv-ambigu.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/05-confirm-slot.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/06-slot-jamais-propose.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/07-samedi-22h.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/08-slot-deja-pris.json`
- Create: `systems/n8n/fixtures/agent-rdv-email/README.md`

- [ ] **Step 1 : écrire les 8 fixtures**

Exemple `02-rdv-schoolswp.json` :

```json
{
  "name": "RDV schoolsWP explicite",
  "input": {
    "from": { "value": [{ "address": "alice@example.test", "name": "Alice Martin" }] },
    "subject": "Démo schoolsWP",
    "text": "Bonjour, j'aimerais voir une démo de schoolsWP la semaine prochaine. Je cherche un outil LMS pour mon site WordPress. Cordialement.",
    "headers": { "message-id": "<fx02@example.test>", "in-reply-to": "", "references": "" },
    "messageId": "<fx02@example.test>"
  },
  "expected": {
    "classifier": { "is_booking_request": true, "product": "schoolswp" },
    "data_table_row_created": true,
    "agent_action_in": ["ask_more_info", "propose_slots"]
  }
}
```

Exemple `06-slot-jamais-propose.json` :

```json
{
  "name": "Confirme un créneau jamais proposé",
  "preconditions": {
    "data_table_row": {
      "threadId": "<fx06@example.test>",
      "prospect_email": "eve@example.test",
      "prospect_name": "Eve",
      "product": "schoolswp",
      "status": "slots_proposed",
      "proposed_slots": [
        {"start":"2026-05-20T14:00:00+02:00","end":"2026-05-20T15:00:00+02:00"}
      ],
      "collected_info": {"besoin":"démo"},
      "event_id": ""
    }
  },
  "input": {
    "from": { "value": [{ "address": "eve@example.test", "name": "Eve" }] },
    "subject": "Re: Démo schoolsWP",
    "text": "OK pour le jeudi 28 mai à 16h.",
    "headers": { "message-id": "<fx06-r1@example.test>", "in-reply-to": "<fx06@example.test>", "references": "<fx06@example.test>" },
    "messageId": "<fx06-r1@example.test>"
  },
  "expected": {
    "gate_failed_check": 1,
    "gate_action": "escalate",
    "discord_message_sent": true,
    "no_event_created": true
  }
}
```

Reproduire le pattern pour les 6 autres. Pour `08-slot-deja-pris.json`, la `precondition` inclut un event existant dans l'agenda test recouvrant le créneau visé.

- [ ] **Step 2 : écrire le README des fixtures**

```markdown
# Fixtures - Agent RDV Email

8 fixtures couvrant les chemins critiques (voir le plan d'implémentation Task 11).

| Fixture | Chemin testé |
| --- | --- |
| 01 | Newsletter -> classifier `is_booking_request=false` -> label + STOP |
| 02 | RDV schoolsWP -> product=schoolswp, agent demande infos ou propose |
| 03 | RDV FluentCart -> product=fluentcart |
| 04 | RDV ambigu -> product=unknown -> ask_more_info |
| 05 | Confirmation d'un créneau valide -> gate.create -> event créé |
| 06 | Confirme un créneau jamais proposé -> gate check 1 -> escalade |
| 07 | Demande un créneau samedi 22h -> gate check 3 -> escalade |
| 08 | Demande un créneau déjà pris dans l'agenda -> gate check 2 -> reoffer |

Les `preconditions` (le cas échéant) doivent être appliquées à la Data Table
`rdv_threads` avant d'injecter `input` dans l'Email Trigger en pin data.
```

- [ ] **Step 3 : commit**

```shell
git add systems/n8n/fixtures/agent-rdv-email/
git commit -m "test(n8n): 8 fixtures covering booking agent paths"
```

---

## Task 11 : Intégration staging + DoD + passage en Prod

**Files:**
- Modify : workflow n8n (rename, activate)
- Modify : `systems/n8n/workflows/agent-rdv-email.json`
- Modify : `systems/n8n/workflows/agent-rdv-email.README.md`

- [ ] **Step 1 : renommer le workflow `[InTesting]`**

Via MCP `n8n_update_partial_workflow`, parameter `name` = `[InTesting] Email contact@ > Google Agenda: Agent RDV démo`.

- [ ] **Step 2 : configurer le staging**

- Pointer `CALENDAR_ID_SCHOOLSWP` et `CALENDAR_ID_FLUENTCART` sur deux agendas test ("TEST-Coaching schoolsWP", "TEST-Coaching FluentCart"), à créer par Michael dans Google Calendar.
- Pointer `DISCORD_WEBHOOK` sur un canal staging (`#staging-rdv` ou `#staging`).
- SMTP/IMAP : utiliser une boîte mail de test si possible, sinon valider les envois dans la sentbox SMTP.

- [ ] **Step 3 : exécuter les 8 fixtures**

Pour chaque fixture `01..08` :

1. Appliquer les `preconditions` (insérer la row dans `rdv_threads` si requis).
2. Pin la fixture `input` sur l'Email Trigger.
3. "Execute Workflow" depuis le trigger.
4. Vérifier `expected` :
   - `classifier.*` : valeur retournée par Parse Classifier.
   - `data_table_row_created` : nouvelle row.
   - `agent_action_in` : `agent_output.action` dans la liste.
   - `gate_failed_check` / `gate_action` : sortie du Booking Gate.
   - `discord_message_sent` : message vu dans #staging.
   - `no_event_created` / event créé : agenda test.
5. Documenter chaque exécution dans `agent-rdv-email.README.md` (tableau pass/fail daté).

- [ ] **Step 4 : test d'idempotence**

Rejouer `05-confirm-slot.json` une seconde fois (sans nettoyer la row). Attendu : `gate.failedCheck=5` (status déjà `confirmed`), escalade Discord "doublon détecté", **aucun deuxième event créé**. Vérifier visuellement.

- [ ] **Step 5 : Definition of Done - checklist**

Cocher dans le README :

```markdown
## Definition of Done - Validation 2026-XX-XX

- [ ] Fixture 01 : classifier `is_booking_request=false`, STOP atteint, aucun mail envoyé.
- [ ] Fixture 02 : product=schoolswp, row créée, agent renvoie ask_more_info ou propose_slots.
- [ ] Fixture 03 : product=fluentcart.
- [ ] Fixture 04 : product=unknown -> ask_more_info.
- [ ] Fixture 05 : gate.create -> event dans TEST-Coaching schoolsWP, mail confirmation envoyé, row status=confirmed avec event_id.
- [ ] Fixture 06 : gate check 1 fail -> escalade Discord, aucun event.
- [ ] Fixture 07 : gate check 3 fail -> escalade Discord, aucun event.
- [ ] Fixture 08 : gate check 2 -> reoffer, mail "ce créneau est pris, voici d'autres options".
- [ ] Test idempotence : rejeu fixture 05 -> escalade doublon, aucun deuxième event.
- [ ] Aucun event créé hors des deux agendas Coaching.
- [ ] Escalade Discord arrive bien dans #staging.
```

- [ ] **Step 6 : bascule en Prod**

Une fois la DoD validée :

1. Repointer `CALENDAR_ID_SCHOOLSWP` / `CALENDAR_ID_FLUENTCART` sur les vrais agendas (IDs lus en Task 0 step 2).
2. Repointer `DISCORD_WEBHOOK` sur `#alerts` (canal `schoolsWP-Routines`).
3. Renommer le workflow `[Prod] Email contact@ > Google Agenda: Agent RDV démo`.
4. Activer le workflow (`active: true`).
5. Test avec un mail réel envoyé à `contact@michaelkihl.fr` depuis une boîte tierce.

- [ ] **Step 7 : export final + commit**

```shell
git add systems/n8n/workflows/agent-rdv-email.json systems/n8n/workflows/agent-rdv-email.README.md
git commit -m "feat(n8n): activate booking agent in production after DoD validation"
```

- [ ] **Step 8 : ouvrir une PR**

Écrire d'abord le corps de la PR dans `.git/PR_BODY.md`, puis :

```shell
git push -u origin feature/agent-rdv-email-google-agenda
gh pr create --title "feat(n8n): email booking agent with deterministic gate" --body-file .git/PR_BODY.md
```

Contenu suggéré de `.git/PR_BODY.md` :

```markdown
## Summary
- Workflow n8n agent IA + gate déterministe pour la prise de RDV démo par email.
- Spec : docs/superpowers/specs/2026-05-14-agent-rdv-email-google-agenda-design.md
- Plan : docs/superpowers/plans/2026-05-14-agent-rdv-email-google-agenda.md
- Routage à 2 sous-agendas (Coaching schoolsWP / Coaching FluentCart).
- Gate testée en isolation (8 tests node:test).

## Test plan
- [ ] Tests `node --test systems/n8n/lib/` verts.
- [ ] Les 8 fixtures passent en staging (voir trace dans le README workflow).
- [ ] Test d'idempotence OK (rejeu = no-op).
- [ ] Bascule [Prod] effectuée, test bout-en-bout avec mail réel.
```

---

## Self-Review

**Spec coverage:** lecture en parallèle du spec et des tâches.

| Section spec | Couvert par |
| --- | --- |
| §4 Topologie | Tasks 3-9 |
| §5 [T] Email Trigger | Task 3 step 2 |
| §5 [1] Thread lookup | Task 3 step 5 + IF Task 4 step 1 |
| §5 [2] Classifieur (avec product schoolswp/fluentcart/unknown) | Task 4 steps 2-4 |
| §5 [3] Context loader | Task 5 |
| §5 [4] Agent + outil read-only | Task 6 steps 1-3 |
| §5 Validateur de schéma | Task 2 + Task 6 step 4 |
| §5 [5] Switch | Task 7 step 1 |
| §5 [6] Booking Gate | Task 1 (lib) + Task 8 step 2 |
| §5 [7] Escalade Discord | Task 9 |
| §5 State store rdv_threads | Task 0 step 6 + updates Tasks 4/7/8/9 |
| §6 Contrat JSON | Task 2 (incluant slots_offered) + Task 6 (system prompt) |
| §6 Garde-fou membership | Task 1 check 1 |
| §7 Config | Task 0 step 7 + lecture Task 8 step 2 |
| §7 5 checks de la gate | Task 1 + tests |
| §7 Cas d'escalade | Task 9 step 5 |
| §7 Sécurité (tool read-only) | Task 6 step 2 |
| §8 Continue On Fail + idempotence | Task 9 step 6 + Task 11 step 4 |
| §9 8 fixtures | Task 10 |
| §9 Gate isolée | Task 1 |
| §9 Validateur isolé | Task 2 |
| §9 Idempotence | Task 11 step 4 |
| §9 DoD + Prod | Task 11 steps 5-6 |
| §10 Provisionning (gws, IMAP cred) | Task 0 steps 1-4 |
| §11 Conséquences | Task 0 |

Pas de section spec sans tâche.

**Placeholder scan:** aucune occurrence de "TBD", "TODO", "implement later". Les balises `<id Coaching schoolsWP>` sont des valeurs de config à lire en Task 0 step 2, pas des placeholders de code. Les notes "confirmer via get_node" sont des steps réels avec commande MCP exacte.

**Type consistency:**

- `validateBooking` renvoie `{ ok, failedCheck, action, reason }`. Référencé identiquement en Task 8 step 2 et Task 9 step 1.
- `validateAgentOutput` renvoie `{ valid, errors }`. Référencé identiquement en Task 6 step 4 et Task 9 step 1.
- Status enum `new / awaiting_info / slots_proposed / confirmed / escalated` cohérent entre Task 0 step 6, Task 4 step 6 (`new`), Task 7 steps 3-4 (`awaiting_info`, `slots_proposed`), Task 8 step 6 (`confirmed`), Task 9 step 4 (`escalated`).
- Champs JSON agent : `action`, `email_draft`, `proposed_slot`, `slots_offered`, `collected_info`, `escalation_reason` cohérents entre Task 2 (validator), Task 6 (prompt), Task 7 (propose_slots), Task 8 (confirm_booking).
- Variables n8n cohérentes : Task 0 step 7 / Task 6 step 2 / Task 8 step 1 / Task 8 step 2.

Aucune incohérence détectée.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-05-14-agent-rdv-email-google-agenda.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
