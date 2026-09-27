#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";
import { ffprobeDuration } from "../lib/ffmpeg.mjs";
import { preflightProject } from "./preflight.mjs";

const root = path.resolve(process.argv[2] || "fixtures/swp-video-smoke");
const scriptDir = path.dirname(new URL(import.meta.url).pathname);

function runNode(script, args = []) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [script, ...args], { stdio: "inherit" });
    child.on("error", reject);
    child.on("close", (code) => code === 0 ? resolve() : reject(new Error(path.basename(script) + " exited " + code)));
  });
}

await runNode(path.join(scriptDir, "generate-fixture.mjs"), [root]);

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "swp-video-smoke-"));
const raw = path.join(root, "assets", "raw.mp4");
const transcript = path.join(root, "assets", "transcript-source.json");
const silenced = path.join(tmp, "silenced.mp4");

await runNode(path.join(scriptDir, "cut-silences.mjs"), [
  transcript,
  "--video", raw,
  "--out-dir", tmp,
  "--output", silenced,
  "--project-id", "SWP-FIXTURE-001",
  "--apply"
]);

const rawDuration = await ffprobeDuration(raw);
const editedDuration = await ffprobeDuration(silenced);
if (!(editedDuration > 0 && editedDuration < rawDuration)) {
  throw new Error("Smoke edit duration check failed: raw=" + rawDuration + " edited=" + editedDuration);
}

const preflight = preflightProject(root);
if (preflight.blockers.length) throw new Error("Fixture preflight failed: " + preflight.blockers.join("; "));

console.log(JSON.stringify({
  status: "PASS",
  rawDuration,
  editedDuration,
  preflight: preflight.status
}, null, 2));
