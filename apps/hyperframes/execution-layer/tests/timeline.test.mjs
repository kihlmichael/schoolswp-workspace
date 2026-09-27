import test from "node:test";
import assert from "node:assert/strict";
import {
  normalizeTranscript,
  buildInitialEdl,
  applyTimelineCuts,
  retimeTranscript,
  validateEdl
} from "../lib/timeline.mjs";

const source = normalizeTranscript({
  audio_duration_secs: 4,
  words: [
    { text: "Je", start: 0.2, end: 0.35 },
    { text: "teste", start: 0.4, end: 0.6 },
    { text: "WordPress", start: 1.0, end: 1.4 },
    { text: "maintenant", start: 2.6, end: 3.0 }
  ]
});

test("initial EDL is contiguous and retimes words with provenance", () => {
  const edl = buildInitialEdl({
    projectId: "T1",
    source: { duration: 4, fps: 30 },
    cuts: [
      { start: 0, end: 0.2, type: "silence" },
      { start: 0.6, end: 1.0, type: "silence" }
    ]
  });
  assert.equal(edl.edited_duration, 3.4);
  assert.equal(validateEdl(edl).ok, true);

  const tx = retimeTranscript(source, edl);
  assert.equal(tx.words[0].start, 0);
  assert.equal(tx.words[0].sourceStart, 0.2);
  assert.equal(tx.words[2].start, 0.4);
});

test("second-stage cuts compose back to original source time", () => {
  const first = buildInitialEdl({
    projectId: "T2",
    source: { duration: 4, fps: 30 },
    cuts: [{ start: 0.6, end: 1.0, type: "silence" }]
  });
  const second = applyTimelineCuts(first, [{ start: 0.2, end: 0.3, type: "mistake", reason: "reviewed" }]);
  assert.equal(second.revision, 2);
  assert.equal(validateEdl(second).ok, true);
  const mapped = second.cuts.find((c) => c.type === "mistake");
  assert.ok(mapped);
  assert.ok(mapped.sourceStart >= 0.2 - 0.001);
});
