#!/usr/bin/env node
/**
 * add-notion-opportunity-score.js — Score Opportunité schoolsWP
 *
 * Ajoute à la base Articles :
 *   5 propriétés de scoring manuel (number, saisie directe dans Notion)
 *   1 date   : Scoré le
 *   1 formule: Score Opportunité (sum des 5 critères, max 100)
 *   1 formule: Label Opportunité (interprétation actionnable)
 *
 * Critères (total max 100) :
 *   SEO      (0-25)  Volume · Difficulté · Intent claire · Concurrents faibles
 *   Business (0-25)  Affilié direct · Lead magnet · Intent achat/décision
 *   Autorité (0-20)  Cluster · Pilier · Satellites futurs · Positionnement
 *   LLM      (0-15)  FAQ-friendly · Réponse extractible · Comparatif structuré
 *   Effort   (0-15)  Inversé — rapide + fort impact = score élevé
 *
 * Note : si "Score Opportunité" existe déjà (via add-notion-seo-priority.js),
 *        la formule est remplacée par la somme des 5 critères manuels.
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_ARTICLES_DB_ID=xxx \
 *   node scripts/add-notion-opportunity-score.js
 *
 * Pré-requis : Node 18+ (fetch natif)
 */

const API_KEY = process.env.NOTION_API_KEY;
const DB_ID   = process.env.NOTION_ARTICLES_DB_ID;

if (!API_KEY || !DB_ID) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY + NOTION_ARTICLES_DB_ID');
  process.exit(1);
}

// ─── API helper ───────────────────────────────────────────────────────────────

async function updateDb(properties) {
  const resp = await fetch(`https://api.notion.com/v1/databases/${DB_ID}`, {
    method: 'PATCH',
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ properties })
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`PATCH /databases/${DB_ID} → ${resp.status}: ${err.message || JSON.stringify(err)}`);
  }
  return resp.json();
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// ─── Formules ─────────────────────────────────────────────────────────────────

// Score Opportunité = somme des 5 critères (max 100)
// Retourne 0 si aucun critère n'a été renseigné (évite les faux positifs)
const FORMULA_SCORE =
  'if(' +
    'prop("SEO") + prop("Business") + prop("Autorité") + prop("LLM") + prop("Effort") > 0, ' +
    'prop("SEO") + prop("Business") + prop("Autorité") + prop("LLM") + prop("Effort"), ' +
    '0' +
  ')';

// Label Opportunité — interprétation actionnable pour la priorisation éditoriale
const FORMULA_LABEL =
  'if(prop("Score Opportunité") >= 85, "🔥 Priorité absolue", ' +
    'if(prop("Score Opportunité") >= 70, "🟢 Planifier", ' +
      'if(prop("Score Opportunité") >= 50, "🟡 À challenger", ' +
        'if(prop("Score Opportunité") > 0, "⚫ Éviter", "— Non scoré"))))';

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Score Opportunité\n');
  console.log(`  Base Articles : ${DB_ID}\n`);

  // ── Phase 1 : 5 critères + date (un seul appel API) ───────────────────────
  console.log('  📊  Phase 1 — 5 critères de scoring + date de scoring...\n');

  await updateDb({
    'SEO':      { number: { format: 'number' } },
    'Business': { number: { format: 'number' } },
    'Autorité': { number: { format: 'number' } },
    'LLM':      { number: { format: 'number' } },
    'Effort':   { number: { format: 'number' } },
    'Scoré le': { date: {} }
  });

  console.log('        ✅  SEO      (0-25)  Volume · Difficulté · Intent · Concurrents');
  console.log('        ✅  Business (0-25)  Affilié · Lead magnet · Intent achat/décision');
  console.log('        ✅  Autorité (0-20)  Cluster · Pilier · Satellites futurs');
  console.log('        ✅  LLM      (0-15)  FAQ-friendly · Réponse extractible · Comparatif');
  console.log('        ✅  Effort   (0-15)  Inversé : rapide + fort impact = élevé');
  console.log('        ✅  Scoré le (date)  Date de la dernière évaluation');
  await sleep(600);

  // ── Phase 2 : Score Opportunité (références les 5 critères) ──────────────
  console.log('\n  🧮  Phase 2 — Formule Score Opportunité (/100)...');

  await updateDb({
    'Score Opportunité': {
      formula: { expression: FORMULA_SCORE }
    }
  });

  console.log('        ✅  SEO + Business + Autorité + LLM + Effort  (max 100)');
  console.log('            → 0 si aucun critère renseigné (pas de faux positifs)');
  await sleep(500);

  // ── Phase 3 : Label Opportunité (références Score Opportunité) ─────────────
  console.log('\n  🏷️   Phase 3 — Formule Label Opportunité...');

  await updateDb({
    'Label Opportunité': {
      formula: { expression: FORMULA_LABEL }
    }
  });

  console.log('        ✅  🔥 ≥85  ·  🟢 ≥70  ·  🟡 ≥50  ·  ⚫ <50  ·  — Non scoré');

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Score Opportunité activé !\n');

  console.log('  📊  Barème de scoring (max 100) :\n');
  console.log('  Critère      Max   Ce qu\'on évalue');
  console.log('  ──────────────────────────────────────────────────────');
  console.log('  SEO          25    Volume · Difficulté · Intent · Concurrence');
  console.log('  Business     25    Affilié · Lead magnet · Intent achat/décision');
  console.log('  Autorité     20    Cluster · Pilier · Satellites futurs');
  console.log('  LLM          15    FAQ-friendly · Réponse extractible · Comparatif');
  console.log('  Effort       15    Inversé : rapide + fort impact = élevé');
  console.log('  ──────────────────────────────────────────────────────');
  console.log('  Total        100');
  console.log('');
  console.log('  Interprétation :');
  console.log('    🔥 85-100   Priorité absolue   → écrire ce trimestre');
  console.log('    🟢 70-84    Planifier           → backlog Q suivant');
  console.log('    🟡 50-69    À challenger        → requalifier l\'angle');
  console.log('    ⚫ <50      Éviter              → levier trop faible');
  console.log('    —  0        Non scoré           → à évaluer avant planification');
  console.log('');
  console.log('  Exemple — "FluentCRM vs MailerLite" :');
  console.log('    SEO=20 · Business=24 · Autorité=18 · LLM=13 · Effort=12 → 87 🔥');
  console.log('');
  console.log('  Exemple — "Changer la couleur d\'un bouton WordPress" :');
  console.log('    SEO=15 · Business=5 · Autorité=4 · LLM=10 · Effort=14  → 48 ⚫');
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  📋  2 vues à créer dans Notion :\n');

  console.log('  1️⃣  Vue "🔥 Priorité rédaction"');
  console.log('      Type    : Table');
  console.log('      Filtre  : Score Opportunité > 0 (articles déjà scorés)');
  console.log('      Tri     : Score Opportunité DESC');
  console.log('      Colonnes: Titre · Label Opportunité · Score Opportunité');
  console.log('               · SEO · Business · Autorité · LLM · Effort');
  console.log('               · Cluster · Scoré le\n');

  console.log('  2️⃣  Vue "🟡 Idées à scorer"');
  console.log('      Type    : Table');
  console.log('      Filtres : Statut = Idée  ET  Score Opportunité = 0');
  console.log('      Colonnes: Titre · Cluster · Intent · Score Opportunité');
  console.log('      → File d\'attente — scorer avant de planifier\n');

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  💡  Workflow recommandé :\n');
  console.log('  1.  Nouvelle idée → créer article dans Notion (Statut : Idée)');
  console.log('  2.  Scorer interactivement : node scripts/score-idea.js');
  console.log('  3.  Reporter les 5 scores dans Notion → Score calculé automatiquement');
  console.log('  4.  N\'écrire que les articles avec Label "🔥" ou "🟢"');
  console.log('  5.  Réviser les scores en début de chaque trimestre');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
