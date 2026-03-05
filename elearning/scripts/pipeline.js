#!/usr/bin/env node
/**
 * pipeline.js
 * Pipeline complet : texte → voix ElevenLabs → avatar HeyGen
 *
 * Usage: node scripts/pipeline.js "Ton script texte ici" [nom-leçon]
 *        node scripts/pipeline.js --file script.txt [nom-leçon]
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { execSync } from "child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function loadEnv() {
  const envPath = path.join(__dirname, "..", ".env");
  if (!fs.existsSync(envPath)) {
    console.error("❌ Fichier .env introuvable dans elearning/");
    process.exit(1);
  }
  const lines = fs.readFileSync(envPath, "utf-8").split("\n");
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const [key, ...rest] = trimmed.split("=");
    process.env[key.trim()] = rest.join("=").trim();
  }
}

loadEnv();

const OUTPUT_DIR = path.join(__dirname, "..", process.env.OUTPUT_DIR || "output");

function getText() {
  const args = process.argv.slice(2);
  if (args[0] === "--file") {
    const filePath = args[1];
    if (!filePath || !fs.existsSync(filePath)) {
      console.error("❌ Fichier introuvable :", filePath);
      process.exit(1);
    }
    return { text: fs.readFileSync(filePath, "utf-8").trim(), lessonName: args[2] };
  }
  if (args[0]) {
    return { text: args[0], lessonName: args[1] };
  }
  console.error("Usage: node pipeline.js \"Texte\" [nom-lecon]");
  console.error("       node pipeline.js --file script.txt [nom-lecon]");
  process.exit(1);
}

async function runPipeline() {
  const { text, lessonName } = getText();
  const timestamp = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
  const slug = lessonName
    ? lessonName.toLowerCase().replace(/\s+/g, "-").replace(/[^a-z0-9-]/g, "")
    : `lesson-${timestamp}`;

  const audioFile = path.join(OUTPUT_DIR, `${slug}-voice.mp3`);
  const videoFile = path.join(OUTPUT_DIR, `${slug}-avatar.mp4`);

  console.log("=".repeat(60));
  console.log("🎓 Pipeline E-learning schoolsWP");
  console.log("=".repeat(60));
  console.log(`Leçon    : ${slug}`);
  console.log(`Texte    : ${text.substring(0, 100)}${text.length > 100 ? "..." : ""}`);
  console.log("");

  // Étape 1 : Génération voix
  console.log("── ÉTAPE 1/2 : Voix ElevenLabs ──────────────────────────");
  execSync(
    `node "${path.join(__dirname, "generate-voice.js")}" "${text.replace(/"/g, '\\"')}" "${audioFile}"`,
    { stdio: "inherit" }
  );

  // Étape 2 : Génération avatar
  console.log("\n── ÉTAPE 2/2 : Avatar HeyGen ─────────────────────────────");
  execSync(
    `node "${path.join(__dirname, "generate-avatar.js")}" "${audioFile}" "${videoFile}"`,
    { stdio: "inherit" }
  );

  console.log("\n" + "=".repeat(60));
  console.log("✅ Pipeline terminé !");
  console.log(`   Audio  : ${audioFile}`);
  console.log(`   Vidéo  : ${videoFile}`);
  console.log("=".repeat(60));
  console.log("\nProchaine étape : intégrer cette vidéo dans Remotion");
  console.log("(slides + branding + captions + intro/outro)");
}

runPipeline().catch((err) => {
  console.error("\n❌ Erreur pipeline:", err.message || err);
  process.exit(1);
});
