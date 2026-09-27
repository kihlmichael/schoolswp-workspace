#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { normalizeTranscript } from "../lib/timeline.mjs";

const input = process.argv[2];
const output = process.argv[3] || (input ? path.join(path.dirname(input), "transcript-source.json") : null);
if (!input) {
  console.error("Usage: node scripts/normalize-transcript.mjs <input.json> [output.json]");
  process.exit(2);
}
const normalized = normalizeTranscript(JSON.parse(fs.readFileSync(input, "utf8")));
fs.writeFileSync(output, JSON.stringify(normalized, null, 2) + "\n");
console.log(JSON.stringify({ status: "PASS", output, words: normalized.words.length, duration: normalized.duration }, null, 2));
