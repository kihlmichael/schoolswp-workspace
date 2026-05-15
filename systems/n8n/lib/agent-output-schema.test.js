'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { validateAgentOutput } = require('./agent-output-schema');

test('action=ask_more_info avec email_draft -> valide', () => {
  const r = validateAgentOutput({
    action: 'ask_more_info',
    email_draft: 'Salut, peux-tu me preciser ton besoin ?',
  });
  assert.equal(r.valid, true);
  assert.deepEqual(r.errors, []);
});

test('action=confirm_booking avec proposed_slot ISO -> valide', () => {
  const r = validateAgentOutput({
    action: 'confirm_booking',
    email_draft: 'C est confirme pour mardi.',
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
    email_draft: 'Je reviens vers toi tres vite.',
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

test('entree non-objet -> invalide', () => {
  assert.equal(validateAgentOutput(null).valid, false);
  assert.equal(validateAgentOutput('foo').valid, false);
});
