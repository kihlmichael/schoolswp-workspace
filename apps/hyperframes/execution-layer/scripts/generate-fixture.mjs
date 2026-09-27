#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { spawn } from "node:child_process";

const root = path.resolve(process.argv[2] || "fixtures/swp-video-smoke");
const assets = path.join(root, "assets");
fs.mkdirSync(assets, { recursive: true });

function run(args) {
  return new Promise((resolve, reject) => {
    const child = spawn("ffmpeg", args, { stdio: ["ignore", "ignore", "pipe"] });
    let stderr = "";
    child.stderr.on("data", (d) => { stderr += d.toString(); });
    child.on("error", reject);
    child.on("close", (code) => code === 0 ? resolve() : reject(new Error(stderr.slice(-1200))));
  });
}

const raw = path.join(assets, "raw.mp4");
const footage = path.join(assets, "fixture-footage.mp4");

await run([
  "-y",
  "-f", "lavfi", "-i", "color=c=0x12111f:s=640x360:d=4:r=30",
  "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000:duration=4",
  "-c:v", "libx264", "-pix_fmt", "yuv420p",
  "-c:a", "aac", "-shortest", raw
]);

await run([
  "-y",
  "-f", "lavfi", "-i", "testsrc2=size=640x360:rate=30:duration=1",
  "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", footage
]);

const hash = crypto.createHash("sha256").update(fs.readFileSync(footage)).digest("hex");
fs.writeFileSync(path.join(assets, "footage-ledger.json"), JSON.stringify([{
  scene: "SC-002",
  sourceSceneId: "fixture-moving-pattern",
  asset: "assets/fixture-footage.mp4",
  sha256: hash,
  sourceStart: 0,
  sourceEnd: 1,
  production_mode: "FOOTAGE",
  provenance: { type: "synthetic-fixture", source: "ffmpeg-testsrc2" },
  framing: { "16x9": "full synthetic frame" }
}], null, 2) + "\n");

fs.writeFileSync(path.join(assets, "plan.json"), JSON.stringify({
  schema_version: "1.1",
  project_id: "SWP-FIXTURE-001",
  duration: 3.4,
  fps: 30,
  format: "16:9",
  scenes: [
    { id: "SC-001", start: 0, end: 2.4, layout: "face", production_mode: "SPEAKER" },
    { id: "SC-002", start: 2.4, end: 3.4, layout: "broll", production_mode: "FOOTAGE" }
  ],
  events: []
}, null, 2) + "\n");

console.log(JSON.stringify({ status: "PASS", raw, footage, footageSha256: hash }, null, 2));
