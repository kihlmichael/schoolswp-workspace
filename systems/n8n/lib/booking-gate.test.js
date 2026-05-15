'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { validateBooking } = require('./booking-gate');

// Reference temporelle : jeudi 14 mai 2026, midi Paris.
const now = '2026-05-14T12:00:00+02:00';

const config = {
  workingDays: [1, 2, 3, 4, 5],
  workingStartHour: 9,
  workingEndHour: 18,
  bufferHours: 24,
  horizonDays: 28,
};

// Mercredi 20 mai 2026, 14h-15h Paris : jour ouvre, en heures, > 24h, < 28 jours.
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

test('check 1 : creneau hors proposedSlots -> escalate', () => {
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
  assert.equal(r.ok, false);
  assert.equal(r.failedCheck, 1);
});

test('check 2 : creneau pris depuis la proposition -> reoffer', () => {
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
  assert.equal(r.ok, false);
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
  assert.equal(r.ok, false);
  assert.equal(r.failedCheck, 3);
});

test('check 3 : 22h hors heures ouvrees -> escalate', () => {
  const late = {
    start: '2026-05-20T22:00:00+02:00',
    end:   '2026-05-20T23:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: late, proposedSlots: [late], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.ok, false);
  assert.equal(r.failedCheck, 3);
});

test('check 4 : creneau dans moins de 24h -> escalate', () => {
  const soon = {
    start: '2026-05-14T14:00:00+02:00',
    end:   '2026-05-14T15:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: soon, proposedSlots: [soon], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.ok, false);
  assert.equal(r.failedCheck, 4);
});

test('check 4 : creneau au-dela de 28 jours -> escalate', () => {
  const far = {
    start: '2026-07-01T14:00:00+02:00',
    end:   '2026-07-01T15:00:00+02:00',
  };
  const r = validateBooking({
    proposedSlot: far, proposedSlots: [far], busy: [],
    prospectStatus: 'slots_proposed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.ok, false);
  assert.equal(r.failedCheck, 4);
});

test('check 5 : fil deja confirme (doublon) -> escalate', () => {
  const r = validateBooking({
    proposedSlot: validSlot, proposedSlots: [validSlot], busy: [],
    prospectStatus: 'confirmed', config, now,
  });
  assert.equal(r.action, 'escalate');
  assert.equal(r.ok, false);
  assert.equal(r.failedCheck, 5);
});

test('guard C1 : proposedSlot undefined -> escalate sans crash', () => {
  const r = validateBooking({
    proposedSlot: undefined,
    proposedSlots: [validSlot],
    busy: [],
    prospectStatus: 'slots_proposed',
    config, now,
  });
  assert.equal(r.ok, false);
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 1);
});

test('guard I1 : now non parsable -> escalate (check 4)', () => {
  const r = validateBooking({
    proposedSlot: validSlot,
    proposedSlots: [validSlot],
    busy: [],
    prospectStatus: 'slots_proposed',
    config,
    now: 'pas une date',
  });
  assert.equal(r.ok, false);
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 4);
});

test('guard I2 : ISO en Z (UTC) sans offset -> escalate (check 3)', () => {
  const iso = {
    start: '2026-05-20T14:00:00Z',
    end:   '2026-05-20T15:00:00Z',
  };
  const r = validateBooking({
    proposedSlot: iso,
    proposedSlots: [iso],
    busy: [],
    prospectStatus: 'slots_proposed',
    config, now,
  });
  assert.equal(r.ok, false);
  assert.equal(r.action, 'escalate');
  assert.equal(r.failedCheck, 3);
});
