#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { validateEdl } from "../lib/timeline.mjs";

export function validateEdlFile(file) {
  if (!fs.existsSync(file)) return { ok: false, errors: ["Missing EDL: " + file] };
  return validateEdl(JSON.parse(fs.readFileSync(file, "utf8")));
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(import.meta.filename)) {
  const file = path.resolve(process.argv[2] || "");
  const result = validateEdlFile(file);
  console.log(JSON.stringify({ status: result.ok ? "PASS" : "FAIL", ...result }, null, 2));
  process.exitCode = result.ok ? 0 : 1;
}
