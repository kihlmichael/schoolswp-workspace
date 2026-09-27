#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

export function validateFootageRows(rows) {
  const errors = [];
  const seenScenes = new Set();

  for (let i = 0; i < rows.length; i++) {
    const r = rows[i];
    if (!r.scene) errors.push("Row " + i + " missing scene");
    if (!r.sourceSceneId) errors.push("Row " + i + " missing sourceSceneId");
    else if (seenScenes.has(r.sourceSceneId)) errors.push("Repeated footage scene identity: " + r.sourceSceneId);
    else seenScenes.add(r.sourceSceneId);

    if (!/^[a-f0-9]{64}$/.test(r.sha256 || "")) errors.push("Invalid SHA256 for " + (r.scene || i));
    if (!(Number.isFinite(r.sourceStart) && Number.isFinite(r.sourceEnd) && r.sourceStart >= 0 && r.sourceEnd > r.sourceStart)) {
      errors.push("Invalid interval for " + (r.scene || i));
    }

    for (const prev of rows.slice(0, i)) {
      if (prev.sha256 !== r.sha256) continue;
      const overlap = Math.min(prev.sourceEnd, r.sourceEnd) - Math.max(prev.sourceStart, r.sourceStart);
      if (overlap > 0.001) errors.push("Overlapping footage intervals: " + prev.scene + " / " + r.scene);
    }
  }

  return { ok: errors.length === 0, errors, scenes: rows.length };
}

export function validateFootageProject(root) {
  const ledgerPath = path.join(root, "assets", "footage-ledger.json");
  const planPath = path.join(root, "assets", "plan.json");
  const rows = fs.existsSync(ledgerPath) ? JSON.parse(fs.readFileSync(ledgerPath, "utf8")) : [];
  const result = validateFootageRows(rows);

  const plan = fs.existsSync(planPath) ? JSON.parse(fs.readFileSync(planPath, "utf8")) : null;
  const footageScenes = (plan?.scenes || []).filter((s) => s.production_mode === "FOOTAGE" || String(s.layout || "").includes("broll"));

  for (const scene of footageScenes) {
    if (rows.filter((r) => r.scene === scene.id).length !== 1) result.errors.push("Missing or duplicate footage-ledger row for " + scene.id);
  }

  for (const row of rows) {
    const asset = path.resolve(root, row.asset);
    if (!asset.startsWith(path.resolve(root) + path.sep)) {
      result.errors.push("Asset escapes project root: " + row.scene);
      continue;
    }
    if (!fs.existsSync(asset)) {
      result.errors.push("Missing local asset: " + row.scene);
      continue;
    }
    const hash = crypto.createHash("sha256").update(fs.readFileSync(asset)).digest("hex");
    if (hash !== row.sha256) result.errors.push("Asset hash mismatch: " + row.scene);
  }

  result.ok = result.errors.length === 0;
  return result;
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(import.meta.filename)) {
  const root = path.resolve(process.argv[2] || ".");
  const result = validateFootageProject(root);
  console.log(JSON.stringify({ status: result.ok ? "PASS" : "FAIL", ...result }, null, 2));
  process.exitCode = result.ok ? 0 : 1;
}
