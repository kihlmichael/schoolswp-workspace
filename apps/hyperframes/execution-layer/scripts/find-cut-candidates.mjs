#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { findCutCandidates } from "../lib/mistakes.mjs";

const input = process.argv[2];
const outDir = process.argv[3] || (input ? path.dirname(input) : null);
if (!input) {
  console.error("Usage: node scripts/find-cut-candidates.mjs <transcript.json> [out-dir]");
  process.exit(2);
}
const candidates = findCutCandidates(JSON.parse(fs.readFileSync(input, "utf8")));
fs.mkdirSync(outDir, { recursive: true });
const jsonPath = path.join(outDir, "cut-candidates.json");
const mdPath = path.join(outDir, "cut-candidates.md");
fs.writeFileSync(jsonPath, JSON.stringify({ review_required: true, candidates }, null, 2) + "\n");
fs.writeFileSync(mdPath,
  "# Cut candidates — HUMAN REVIEW REQUIRED\n\n" +
  (candidates.length
    ? candidates.map((c, i) =>
        "## " + (i + 1) + ". " + c.type + "\n\n" +
        "- range: " + c.cut.start.toFixed(3) + "–" + c.cut.end.toFixed(3) + "\n" +
        "- removes: " + c.removes + "\n" +
        "- keeps: " + c.keeps + "\n" +
        "- context: " + c.context + "\n" +
        "- decision: REVIEW\n"
      ).join("\n")
    : "No candidate found. Zero cuts is a valid result.\n")
);
console.log(JSON.stringify({ status: "PASS", reviewRequired: true, candidates: candidates.length, jsonPath, mdPath }, null, 2));
