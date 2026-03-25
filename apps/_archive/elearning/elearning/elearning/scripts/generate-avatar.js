#!/usr/bin/env node
/**
 * generate-avatar.js
 * Génère une vidéo avatar HeyGen depuis un fichier audio MP3
 *
 * Usage: node scripts/generate-avatar.js audio.mp3 [output-name]
 *
 * Workflow HeyGen :
 *   1. Upload l'audio → audio_asset_id
 *   2. POST /v2/video/generate → video_id
 *   3. Poll GET /v1/video_status.get → attend "completed"
 *   4. Download la vidéo MP4
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

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

const HEYGEN_API_KEY = process.env.HEYGEN_API_KEY;
const AVATAR_ID = process.env.HEYGEN_AVATAR_ID;
const OUTPUT_DIR = path.join(__dirname, "..", process.env.OUTPUT_DIR || "output");

if (!HEYGEN_API_KEY) {
  console.error("❌ HEYGEN_API_KEY manquant dans .env");
  process.exit(1);
}
if (!AVATAR_ID) {
  console.error("❌ HEYGEN_AVATAR_ID manquant dans .env");
  process.exit(1);
}

const audioFile = process.argv[2];
if (!audioFile || !fs.existsSync(audioFile)) {
  console.error("Usage: node generate-avatar.js <audio.mp3> [nom-sortie]");
  process.exit(1);
}

const outputName = process.argv[3];

// Étape 1 : Upload l'audio sur HeyGen
async function uploadAudio(filePath) {
  console.log("📤 Upload audio vers HeyGen...");

  const fileBuffer = fs.readFileSync(filePath);
  const fileName = path.basename(filePath);

  // HeyGen attend un upload via URL publique ou base64 selon la version API
  // On utilise l'endpoint v1/asset pour uploader le fichier
  const formData = new FormData();
  const blob = new Blob([fileBuffer], { type: "audio/mpeg" });
  formData.append("file", blob, fileName);
  formData.append("type", "audio");

  const response = await fetch("https://upload.heygen.com/v1/asset", {
    method: "POST",
    headers: {
      "X-Api-Key": HEYGEN_API_KEY,
    },
    body: formData,
  });

  if (!response.ok) {
    const err = await response.text();
    console.error(`❌ Erreur upload HeyGen ${response.status}:`, err);
    process.exit(1);
  }

  const data = await response.json();
  const assetId = data?.data?.asset_id || data?.asset_id;
  if (!assetId) {
    console.error("❌ asset_id introuvable dans la réponse:", JSON.stringify(data));
    process.exit(1);
  }

  console.log(`   ✅ Audio uploadé — asset_id: ${assetId}`);
  return assetId;
}

// Étape 2 : Générer la vidéo avatar
async function generateVideo(audioAssetId) {
  console.log("🎬 Génération vidéo avatar HeyGen...");
  console.log(`   Avatar ID : ${AVATAR_ID}`);

  const response = await fetch("https://api.heygen.com/v2/video/generate", {
    method: "POST",
    headers: {
      "X-Api-Key": HEYGEN_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      video_inputs: [
        {
          character: {
            type: "avatar",
            avatar_id: AVATAR_ID,
            avatar_style: "normal",
          },
          voice: {
            type: "audio",
            audio_asset_id: audioAssetId,
          },
          background: {
            type: "color",
            value: "#f5f5f5",
          },
        },
      ],
      dimension: {
        width: 1920,
        height: 1080,
      },
      aspect_ratio: "16:9",
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    console.error(`❌ Erreur génération HeyGen ${response.status}:`, err);
    process.exit(1);
  }

  const data = await response.json();
  const videoId = data?.data?.video_id || data?.video_id;
  if (!videoId) {
    console.error("❌ video_id introuvable dans la réponse:", JSON.stringify(data));
    process.exit(1);
  }

  console.log(`   ✅ Vidéo en cours de rendu — video_id: ${videoId}`);
  return videoId;
}

// Étape 3 : Attendre que la vidéo soit prête (polling)
async function waitForVideo(videoId, maxWaitMs = 10 * 60 * 1000) {
  console.log("⏳ En attente du rendu (peut prendre 2-5 min)...");

  const startTime = Date.now();
  const pollInterval = 10_000; // 10 secondes

  while (Date.now() - startTime < maxWaitMs) {
    await new Promise((r) => setTimeout(r, pollInterval));

    const response = await fetch(
      `https://api.heygen.com/v1/video_status.get?video_id=${videoId}`,
      {
        headers: { "X-Api-Key": HEYGEN_API_KEY },
      }
    );

    if (!response.ok) {
      console.warn(`   ⚠️  Erreur polling ${response.status}, on réessaie...`);
      continue;
    }

    const data = await response.json();
    const status = data?.data?.status || data?.status;
    const elapsed = Math.round((Date.now() - startTime) / 1000);

    process.stdout.write(`\r   Statut: ${status} (${elapsed}s écoulées)     `);

    if (status === "completed") {
      console.log("\n   ✅ Rendu terminé !");
      return data?.data?.video_url || data?.video_url;
    }

    if (status === "failed") {
      console.error("\n❌ Rendu échoué:", JSON.stringify(data));
      process.exit(1);
    }
  }

  console.error("\n❌ Timeout : la vidéo n'a pas été rendue dans les délais");
  process.exit(1);
}

// Étape 4 : Télécharger la vidéo
async function downloadVideo(url, outputFile) {
  console.log(`📥 Téléchargement de la vidéo...`);

  const response = await fetch(url);
  if (!response.ok) {
    console.error(`❌ Erreur téléchargement ${response.status}`);
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(outputFile, buffer);
  console.log(`✅ Vidéo sauvegardée : ${outputFile}`);
  console.log(`   Taille : ${(buffer.length / 1024 / 1024).toFixed(1)} MB`);
}

// Pipeline principal
async function run() {
  const timestamp = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
  const outputFile = path.join(OUTPUT_DIR, outputName || `avatar-${timestamp}.mp4`);

  const audioAssetId = await uploadAudio(audioFile);
  const videoId = await generateVideo(audioAssetId);
  const videoUrl = await waitForVideo(videoId);
  await downloadVideo(videoUrl, outputFile);

  console.log("\n🎉 Avatar généré avec succès !");
  console.log(`   Fichier : ${outputFile}`);
}

run().catch((err) => {
  console.error("❌ Erreur inattendue:", err);
  process.exit(1);
});
