'use strict';

/**
 * Validation structurelle du JSON emis par le node AI Agent du workflow [4].
 * Pure : pas d'API n8n. Verifie la shape uniquement.
 *
 * La semantique 'proposed_slot doit appartenir a proposed_slots' vit dans la gate
 * (booking-gate.js, check 1) ou la donnee est presente. Ici on n'verifie que la
 * forme : action valide, champs requis par action, formats ISO.
 *
 * Retourne { valid: boolean, errors: string[] }.
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
