import test from "node:test";
import assert from "node:assert/strict";
import { validateFootageRows } from "../scripts/validate-footage.mjs";

const hash = "a".repeat(64);

test("footage ledger rejects duplicate source scene identity", () => {
  const result = validateFootageRows([
    { scene: "A", sourceSceneId: "same", asset: "assets/a.mp4", sha256: hash, sourceStart: 0, sourceEnd: 1 },
    { scene: "B", sourceSceneId: "same", asset: "assets/b.mp4", sha256: hash, sourceStart: 2, sourceEnd: 3 }
  ]);
  assert.equal(result.ok, false);
  assert.ok(result.errors.some((e) => e.includes("Repeated footage")));
});

test("empty ledger is valid when no footage scene is selected", () => {
  const result = validateFootageRows([]);
  assert.equal(result.ok, true);
});
