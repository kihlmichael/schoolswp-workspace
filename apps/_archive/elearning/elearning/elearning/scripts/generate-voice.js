#!/usr/bin/env node
/**
 * generate-voice.js
 * Convertit un script texte en audio MP3 via ElevenLabs (voice clone)
 *
 * Usage: node scripts/generate-voice.js "Ton texte ici" [output.mp3]
 *        node scripts/generate-voice.js --file script.txt [output.mp3]
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Charger .env manuellement (sans dépendance externe)
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

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
const VOICE_ID = process.env.ELEVENLABS_VOICE_ID;
const OUTPUT_DIR = path.join(__dirname, "..", process.env.OUTPUT_DIR || "output");

if (!ELEVENLABS_API_KEY || !VOICE_ID) {
  console.error("❌ ELEVENLABS_API_KEY ou ELEVENLABS_VOICE_ID manquant dans .env");
  process.exit(1);
}

// Récupérer le texte depuis args ou fichier
function getText() {
  const args = process.argv.slice(2);
  if (args[0] === "--file") {
    const filePath = args[1];
    if (!filePath || !fs.existsSync(filePath)) {
      console.error("❌ Fichier script introuvable :", filePath);
      process.exit(1);
    }
    return { text: fs.readFileSync(filePath, "utf-8").trim(), outputName: args[2] };
  }
  if (args[0]) {
    return { text: args[0], outputName: args[1] };
  }
  console.error("Usage: node generate-voice.js \"Texte\" [output.mp3]");
  console.error("       node generate-voice.js --file script.txt [output.mp3]");
  process.exit(1);
}

async function generateVoice(text, outputFile) {
  console.log(`🎙️  Génération voix ElevenLabs...`);
  console.log(`   Voice ID : ${VOICE_ID}`);
  console.log(`   Texte    : ${text.substring(0, 80)}${text.length > 80 ? "..." : ""}`);

  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`,
    {
      method: "POST",
      headers: {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        Accept: "audio/mpeg",
      },
      body: JSON.stringify({
        text,
        model_id: "eleven_multilingual_v2",
        voice_settings: {
          stability: 0.5,
          similarity_boost: 0.85,
          style: 0.2,
          use_speaker_boost: true,
        },
      }),
    }
  );

  if (!response.ok) {
    const err = await response.text();
    console.error(`❌ Erreur ElevenLabs ${response.status}:`, err);
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(outputFile, buffer);
  console.log(`✅ Audio généré : ${outputFile}`);
  console.log(`   Taille : ${(buffer.length / 1024).toFixed(1)} KB`);
}

const { text, outputName } = getText();
const timestamp = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
const outputFile = path.join(OUTPUT_DIR, outputName || `voice-${timestamp}.mp3`);

generateVoice(text, outputFile);
