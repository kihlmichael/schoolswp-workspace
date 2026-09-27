#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { normalizeTranscript, buildInitialEdl, retimeTranscript } from "../lib/timeline.mjs";
import { planSilenceCuts } from "../lib/silence.mjs";
import { renderKeeps } from "../lib/ffmpeg.mjs";

const args = process.argv.slice(2);
const input = args.find((x) => !x.startsWith("--"));
const value = (flag, fallback = null) => {
  const i = args.indexOf(flag);
  return i >= 0 ? args[i + 1] : fallback;
};
const has = (flag) => args.includes(flag);

if (!input) {
  console.error("Usage: node scripts/cut-silences.mjs <transcript.json> [--profile file] [--video file] [--out-dir dir] [--output file] [--project-id id] [--apply]");
  process.exit(2);
}

const transcript = normalizeTranscript(JSON.parse(fs.readFileSync(input, "utf8")));
const defaultProfilePath = fileURLToPath(new URL("../profiles/educational.json", import.meta.url));
const profilePath = value("--profile", defaultProfilePath);
const profile = JSON.parse(fs.readFileSync(profilePath, "utf8"));
const outDir = path.resolve(value("--out-dir", path.dirname(input)));
fs.mkdirSync(outDir, { recursive: true });

const video = value("--video");
let sha256 = "";
if (video && fs.existsSync(video)) sha256 = crypto.createHash("sha256").update(fs.readFileSync(video)).digest("hex");

const cuts = planSilenceCuts(transcript, profile);
const edl = buildInitialEdl({
  projectId: value("--project-id", "UNASSIGNED"),
  source: {
    asset_id: "SOURCE_MEDIA",
    sha256,
    duration: transcript.duration,
    fps: Number(value("--fps", "30"))
  },
  cuts
});
const retimed = retimeTranscript(transcript, edl);

const edlPath = path.join(outDir, "silence-edl.json");
const transcriptPath = path.join(outDir, "transcript-silenced.json");
const decisionsPath = path.join(outDir, "silence-decisions.md");
fs.writeFileSync(edlPath, JSON.stringify(edl, null, 2) + "\n");
fs.writeFileSync(transcriptPath, JSON.stringify(retimed, null, 2) + "\n");
fs.writeFileSync(decisionsPath,
  "# Silence decisions\n\n" +
  "- source duration: " + transcript.duration.toFixed(3) + "s\n" +
  "- edited duration: " + edl.edited_duration.toFixed(3) + "s\n" +
  "- cuts: " + cuts.length + "\n\n" +
  cuts.map((c, i) => (i + 1) + ". " + c.start.toFixed(3) + "–" + c.end.toFixed(3) + " — " + c.reason).join("\n") + "\n"
);

let rendered = null;
if (has("--apply")) {
  if (!video) throw new Error("--apply requires --video");
  rendered = path.resolve(value("--output", path.join(outDir, "silenced.mp4")));
  await renderKeeps(video, rendered, edl.keeps);
}

console.log(JSON.stringify({
  status: "PASS",
  profile: profile.id,
  cuts: cuts.length,
  sourceDuration: transcript.duration,
  editedDuration: edl.edited_duration,
  edl: edlPath,
  transcript: transcriptPath,
  rendered
}, null, 2));
