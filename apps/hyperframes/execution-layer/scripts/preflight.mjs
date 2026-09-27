#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { validateTranscriptFile } from "./validate-transcript.mjs";
import { validateEdlFile } from "./validate-edl.mjs";
import { validateFootageProject } from "./validate-footage.mjs";

export function preflightProject(root) {
  const checks = [];
  const blockers = [];
  const warnings = [];

  const transcriptPath = path.join(root, "assets", "transcript.json");
  const edlPath = path.join(root, "assets", "edit-decisions.json");
  const planPath = path.join(root, "assets", "plan.json");

  const transcript = validateTranscriptFile(transcriptPath);
  checks.push({ id: "transcript", ...transcript });
  if (!transcript.ok) blockers.push(...transcript.errors.map((e) => "transcript: " + e));

  const edl = validateEdlFile(edlPath);
  checks.push({ id: "edl", ...edl });
  if (!edl.ok) blockers.push(...edl.errors.map((e) => "edl: " + e));

  if (fs.existsSync(planPath)) {
    const plan = JSON.parse(fs.readFileSync(planPath, "utf8"));
    if (!Number.isFinite(plan.duration) || plan.duration <= 0) blockers.push("plan: invalid duration");
    if (!Array.isArray(plan.scenes) || !plan.scenes.length) blockers.push("plan: no scenes");
    if (transcript.ok) {
      const tx = JSON.parse(fs.readFileSync(transcriptPath, "utf8"));
      if (Math.abs(Number(plan.duration) - Number(tx.duration)) > 0.05) blockers.push("plan: duration differs from canonical transcript");
    }
  } else {
    warnings.push("plan.json absent — allowed in P0, required from P1");
  }

  const footage = validateFootageProject(root);
  checks.push({ id: "footage", ...footage });
  if (!footage.ok) blockers.push(...footage.errors.map((e) => "footage: " + e));

  const status = blockers.length ? "FAIL" : warnings.length ? "PASS_WITH_WARNINGS" : "PASS";
  return { status, blockers, warnings, checks };
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(import.meta.filename)) {
  const root = path.resolve(process.argv[2] || ".");
  const result = preflightProject(root);
  console.log(JSON.stringify(result, null, 2));
  process.exitCode = result.blockers.length ? 1 : 0;
}
