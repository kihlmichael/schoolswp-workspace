'use strict';

/**
 * Validation deterministe pour la gate de reservation (workflow node [6]).
 * Fonction pure : pas d'API n8n, pas de LLM, pas d'I/O. Testable en isolation.
 *
 * Ordre des checks volontaire : 5 (idempotence) -> 1 -> 3 -> 4 -> 2.
 * Le check 2 est en dernier car c'est la seule branche 'reoffer' ;
 * mettre les escalades avant evite d'evaluer le free/busy quand le creneau
 * est de toute facon disqualifie.
 *
 * Actions :
 *   - 'create'   : tous les checks passent.
 *   - 'reoffer'  : creneau valide mais plus libre -> relancer l'agent.
 *   - 'escalate' : anomalie -> notifier Discord.
 *
 * failedCheck :
 *   - 1..5 : check metier correspondant (1 inclut le guard de shape sur proposedSlot).
 *   - null : cas vert (action 'create').
 */

function parseWallClock(iso) {
  // Exige un offset explicite (+HH:MM / -HH:MM). Refuse 'Z' et l'absence d'offset.
  const m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):\d{2}([+-]\d{2}:\d{2})$/.exec(iso);
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

  // Guard : entree malformee -> escalate (la gate doit toujours retourner un resultat, jamais crasher).
  if (!proposedSlot || typeof proposedSlot.start !== 'string' || typeof proposedSlot.end !== 'string') {
    return {
      ok: false, failedCheck: 1, action: 'escalate',
      reason: 'proposedSlot manquant ou malforme.',
    };
  }

  // Ordre volontaire : 5 d'abord (idempotence anti-doublon, evite tout travail si deja confirme)
  // -> 1/3/4 (escalades pour anomalies) -> 2 en dernier (seule branche 'reoffer' :
  // inutile d'appeler ce check si le creneau est deja disqualifie en amont).
  if (prospectStatus === 'confirmed') {
    return {
      ok: false, failedCheck: 5, action: 'escalate',
      reason: 'Thread deja confirme : doublon detecte.',
    };
  }

  // Check 1 : appartenance aux creneaux proposes.
  const inOffered = (proposedSlots || []).some(
    (s) => s.start === proposedSlot.start && s.end === proposedSlot.end,
  );
  if (!inOffered) {
    return {
      ok: false, failedCheck: 1, action: 'escalate',
      reason: 'Creneau non present dans les creneaux proposes.',
    };
  }

  // Check 3 : dans les jours/heures ouvres.
  const wc = parseWallClock(proposedSlot.start);
  const wcEnd = parseWallClock(proposedSlot.end);
  if (!wc || !wcEnd) {
    return {
      ok: false, failedCheck: 3, action: 'escalate',
      reason: 'Format de date du creneau invalide.',
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
      reason: 'Creneau hors jours/heures ouvres.',
    };
  }

  // Check 4 : buffer et horizon.
  const startMs = Date.parse(proposedSlot.start);
  const nowMs = Date.parse(now);
  if (Number.isNaN(startMs) || Number.isNaN(nowMs)) {
    return {
      ok: false, failedCheck: 4, action: 'escalate',
      reason: 'Date du creneau ou now non parsable.',
    };
  }
  const hoursAhead = (startMs - nowMs) / 3600000;
  if (hoursAhead < config.bufferHours) {
    return {
      ok: false, failedCheck: 4, action: 'escalate',
      reason: 'Creneau dans le buffer (' + config.bufferHours + 'h).',
    };
  }
  if (hoursAhead > config.horizonDays * 24) {
    return {
      ok: false, failedCheck: 4, action: 'escalate',
      reason: 'Creneau au-dela de l horizon (' + config.horizonDays + ' jours).',
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
      reason: 'Creneau occupe entre la proposition et la confirmation.',
    };
  }

  return { ok: true, failedCheck: null, action: 'create', reason: null };
}

module.exports = { validateBooking, parseWallClock, isoWeekday, overlaps };
