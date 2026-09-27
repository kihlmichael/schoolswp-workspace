#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const layerRoot = path.resolve(here, "..");
const repoRoot = path.resolve(layerRoot, "../../..");
const sourceRoot = path.join(layerRoot, "skills", "canonical");
const targets = [
  path.join(repoRoot, ".claude", "skills"),
  path.join(repoRoot, ".agents", "skills")
];
const check = process.argv.includes("--check");

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const full = path.join(dir, e.name);
    return e.isDirectory() ? walk(full) : [full];
  });
}

let differences = 0;
let files = 0;

for (const skillName of fs.readdirSync(sourceRoot)) {
  const skillDir = path.join(sourceRoot, skillName);
  if (!fs.statSync(skillDir).isDirectory()) continue;

  for (const source of walk(skillDir)) {
    const rel = path.relative(skillDir, source);
    const bytes = fs.readFileSync(source);

    for (const targetRoot of targets) {
      const dest = path.join(targetRoot, skillName, rel);
      if (check) {
        if (!fs.existsSync(dest) || !fs.readFileSync(dest).equals(bytes)) {
          console.error("Out of sync: " + path.relative(repoRoot, dest));
          differences++;
        }
      } else {
        fs.mkdirSync(path.dirname(dest), { recursive: true });
        fs.writeFileSync(dest, bytes);
      }
    }
    files++;
  }
}

console.log(JSON.stringify({
  mode: check ? "check" : "sync",
  canonicalFiles: files,
  mirrors: targets.map((t) => path.relative(repoRoot, t)),
  differences
}, null, 2));
process.exitCode = differences ? 1 : 0;
