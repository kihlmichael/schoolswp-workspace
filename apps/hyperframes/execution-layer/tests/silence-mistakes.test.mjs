import test from "node:test";
import assert from "node:assert/strict";
import { planSilenceCuts } from "../lib/silence.mjs";
import { findCutCandidates } from "../lib/mistakes.mjs";

test("silence planner removes only long dead air", () => {
  const tx = {
    duration: 4,
    words: [
      { text: "Bonjour", start: 0.2, end: 0.6 },
      { text: "WordPress.", start: 1.5, end: 2.0 },
      { text: "Suite", start: 2.2, end: 2.6 }
    ]
  };
  const cuts = planSilenceCuts(tx, { gapThreshold: 0.55, headPad: 0.1, tailPad: 0.2 });
  assert.ok(cuts.some((c) => c.reason.startsWith("pause")));
  assert.ok(cuts.every((c) => c.type === "silence"));
});

test("mistake detector proposes duplicate words but never approves them", () => {
  const tx = {
    duration: 2,
    words: [
      { text: "je", start: 0.1, end: 0.3 },
      { text: "je", start: 0.35, end: 0.55 },
      { text: "teste", start: 0.6, end: 1.0 }
    ]
  };
  const candidates = findCutCandidates(tx);
  assert.equal(candidates[0].type, "stutter");
  assert.equal(candidates[0].recommendation, "REVIEW");
  assert.equal("approved" in candidates[0], false);
});
