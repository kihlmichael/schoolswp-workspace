#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { normalizeTranscript, applyTimelineCuts, retimeTranscript, buildKeeps } from "../lib/timeline.mjs";
import { renderKeeps } from "../lib/ffmpeg.mjs";

const args = process.argv.slice(2);
const input = args.find((x) => !x.startsWith("--"));
const value = (flag, fallback = null) => {
  const i = args.indexOf(flag);
  return i >= 0 ? args[i + 1] : fallback;
};
const has = (flag) => args.includes(flag);

if (!input || !value("--previous-edl") || !value("--cuts")) {
  console.error("Usage: node scripts/apply-cuts.mjs <current-transcript.json> --previous-edl <edl.json> --cuts <approved.json> [--video file] [--output file] [--out-dir dir] [--apply]");
  process.exit(2);
}

const transcript = normalizeTranscript(JSON.parse(fs.readFileSync(input, "utf8")));
const previousEdl = JSON.parse(fs.readFileSync(value("--previous-edl"), "utf8"));
const approved = JSON.parse(fs.readFileSync(value("--cuts"), "utf8"));
const localCuts = (approved.cuts || []).filter((c) => c.approved !== false).map((c) => ({ ...c, type: c.type || "mistake", approved: true }));

const finalEdl = applyTimelineCuts(previousEdl, localCuts, { type: "mistake" });
const finalTranscript = retimeTranscript(transcript, finalEdl);
const outDir = path.resolve(value("--out-dir", path.dirname(input)));
fs.mkdirSync(outDir, { recursive: true });

const edlPath = path.join(outDir, "edit-decisions.json");
const transcriptPath = path.join(outDir, "transcript.json");
fs.writeFileSync(edlPath, JSON.stringify(finalEdl, null, 2) + "\n");
fs.writeFileSync(transcriptPath, JSON.stringify(finalTranscript, null, 2) + "\n");

let rendered = null;
if (has("--apply")) {
  const video = value("--video");
  if (!video) throw new Error("--apply requires --video");
  const stageKeeps = buildKeeps(transcript.duration, localCuts).keeps;
  rendered = path.resolve(value("--output", path.join(outDir, "clean.mp4")));
  await renderKeeps(video, rendered, stageKeeps);
}

console.log(JSON.stringify({
  status: "PASS",
  approvedCuts: localCuts.length,
  revision: finalEdl.revision,
  editedDuration: finalEdl.edited_duration,
  edl: edlPath,
  transcript: transcriptPath,
  rendered
}, null, 2));
