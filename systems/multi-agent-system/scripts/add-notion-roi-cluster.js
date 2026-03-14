#!/usr/bin/env node
/**
 * add-notion-roi-cluster.js — Module Score ROI Cluster schoolsWP
 *
 * Ajoute à la base Clusters :
 *   6 rollups : Impressions totales · CTR moyen cluster · Position moyenne cluster
 *               Score Autorité moyen · Leads cluster total · Nombre d'articles
 *   1 formule : Taux conversion (%)
 *   1 formule : Score ROI Cluster (/100)
 *   1 formule : Label ROI
 *
 * Pré-requis :
 *   - Base Clusters déjà créée (via setup-notion.js)
 *   - Propriétés existantes : Trafic total cluster · Revenus cluster · % Complétude
 *   - Relation "Articles satellites" (dual_property vers Articles) déjà configurée
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_CLUSTERS_DB_ID=xxx \
 *   node scripts/add-notion-roi-cluster.js
 *
 * Calibrage des normalisateurs (ajuster selon volumes réels du site) :
 *   Trafic total = 1000 → cluster à 1000 clics/mois = poids max (0.25)
 *   Revenus      = 500  → cluster à 500€/mois = poids max (0.30)
 */

const API_KEY = process.env.NOTION_API_KEY;
const DB_ID   = process.env.NOTION_CLUSTERS_DB_ID;

if (!API_KEY || !DB_ID) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY + NOTION_CLUSTERS_DB_ID');
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

// Taux conversion (%) = Leads / Trafic total × 100
// Arrondi 2 décimales via ×10000/100
const FORMULA_TAUX_CONVERSION =
  'if(prop("Trafic total cluster") > 0, ' +
    'round((prop("Leads cluster total") / prop("Trafic total cluster")) * 10000) / 100, ' +
    '0)';

// Score ROI Cluster /100 — pondération 4 axes :
//   25% Trafic      (normalisé / 1000 clics — ajuster selon volumes réels)
//   30% Revenus     (normalisé / 500€       — ajuster selon revenus réels)
//   20% Autorité    (Score Autorité moyen / 100)
//   25% Complétude  (1 si "Complet ✅", 0.5 sinon)
const FORMULA_ROI_CLUSTER =
  'min(100, round(' +
    '(' +
      '((prop("Trafic total cluster") / 1000) * 0.25) + ' +
      '((prop("Revenus cluster") / 500) * 0.30) + ' +
      '((prop("Score Autorité moyen") / 100) * 0.20) + ' +
      '(if(prop("% Complétude") == "Complet ✅", 1, 0.5) * 0.25)' +
    ') * 100' +
  '))';

// Label ROI — interprétation actionnable du Score ROI Cluster
const FORMULA_LABEL_ROI =
  'if(prop("Score ROI Cluster") >= 90, "🚀 Cluster Stratégique", ' +
    'if(prop("Score ROI Cluster") >= 80, "🟢 Haute Performance", ' +
      'if(prop("Score ROI Cluster") >= 70, "🟡 À renforcer", ' +
        '"🔴 Sous-exploité")))';

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Module Score ROI Cluster\n');
  console.log(`  Base Clusters : ${DB_ID}\n`);

  // ── Phase 1 : Rollups (référencent la relation "Articles satellites") ────────
  console.log('  📊  Phase 1 — Ajout des 6 rollups...\n');

  // Rollup 1 : Impressions totales (sum)
  await updateDb({
    'Impressions totales': {
      rollup: {
        relation_property_name: 'Articles satellites',
        rollup_property_name:   'Impressions',
        function:               'sum'
      }
    }
  });
  console.log('        ✅  Impressions totales (sum Impressions)');
  await sleep(500);

  // Rollup 2 : CTR moyen cluster (average)
  await updateDb({
    'CTR moyen cluster': {
      rollup: {
        relation_property_name: 'Articles satellites',
        rollup_property_name:   'CTR',
        function:               'average'
      }
    }
  });
  console.log('        ✅  CTR moyen cluster (avg CTR)');
  await sleep(500);

  // Rollup 3 : Position moyenne cluster (average)
  await updateDb({
    'Position moyenne cluster': {
      rollup: {
        relation_property_name: 'Articles satellites',
        rollup_property_name:   'Position moyenne',
        function:               'average'
      }
    }
  });
  console.log('        ✅  Position moyenne cluster (avg Position moyenne)');
  await sleep(500);

  // Rollup 4 : Score Autorité moyen (average)
  await updateDb({
    'Score Autorité moyen': {
      rollup: {
        relation_property_name: 'Articles satellites',
        rollup_property_name:   'Score Autorité',
        function:               'average'
      }
    }
  });
  console.log('        ✅  Score Autorité moyen (avg Score Autorité)');
  await sleep(500);

  // Rollup 5 : Leads cluster total (sum)
  await updateDb({
    'Leads cluster total': {
      rollup: {
        relation_property_name: 'Articles satellites',
        rollup_property_name:   'Leads générés',
        function:               'sum'
      }
    }
  });
  console.log('        ✅  Leads cluster total (sum Leads générés)');
  await sleep(500);

  // Rollup 6 : Nombre d'articles (count_all)
  await updateDb({
    "Nombre d'articles": {
      rollup: {
        relation_property_name: 'Articles satellites',
        rollup_property_name:   'Titre',
        function:               'count_all'
      }
    }
  });
  console.log("        ✅  Nombre d'articles (count_all Titre)");
  await sleep(500);

  // ── Phase 2 : Formule Taux conversion ─────────────────────────────────────
  console.log('\n  🧮  Phase 2 — Formule Taux conversion (%)...');
  await updateDb({
    'Taux conversion (%)': {
      formula: { expression: FORMULA_TAUX_CONVERSION }
    }
  });
  console.log('        ✅  if(Trafic > 0, round(Leads / Trafic × 10000) / 100, 0)');
  await sleep(500);

  // ── Phase 3 : Formule Score ROI Cluster ───────────────────────────────────
  console.log('\n  🧮  Phase 3 — Formule Score ROI Cluster (/100)...');
  await updateDb({
    'Score ROI Cluster': {
      formula: { expression: FORMULA_ROI_CLUSTER }
    }
  });
  console.log('        ✅  min(100, round((Trafic×0.25 + Revenus×0.30 + Autorité×0.20 + Complétude×0.25) × 100))');
  await sleep(500);

  // ── Phase 4 : Formule Label ROI ───────────────────────────────────────────
  console.log('\n  🏷️   Phase 4 — Formule Label ROI...');
  await updateDb({
    'Label ROI': {
      formula: { expression: FORMULA_LABEL_ROI }
    }
  });
  console.log('        ✅  🚀 ≥90 · 🟢 ≥80 · 🟡 ≥70 · 🔴 <70');

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Module Score ROI Cluster activé !\n');

  console.log('  📊  Score ROI Cluster — pondération :\n');
  console.log('  25% Trafic      → Trafic total cluster / 1000 clics');
  console.log('  30% Revenus     → Revenus cluster / 500€');
  console.log('  20% Autorité    → Score Autorité moyen / 100');
  console.log('  25% Complétude  → 1.0 si "Complet ✅"  ·  0.5 sinon');
  console.log('');
  console.log('  Labels :');
  console.log('    🚀 ≥ 90  Cluster Stratégique   — ton moteur principal, protéger et amplifier');
  console.log('    🟢 ≥ 80  Haute Performance      — très rentable, optimiser le CRO');
  console.log('    🟡 ≥ 70  À renforcer            — bon potentiel, compléter les satellites');
  console.log('    🔴 < 70  Sous-exploité          — décision : investir ou déprioritiser');
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  📋  3 vues à créer manuellement dans Notion :\n');

  console.log('  1️⃣  Vue "🎯 Priorité Business"');
  console.log('      Type    : Table');
  console.log('      Tri     : Score ROI Cluster → Décroissant');
  console.log('      Colonnes: Nom cluster · Score ROI Cluster · Label ROI');
  console.log("               · Trafic total cluster · Revenus cluster");
  console.log("               · Taux conversion (%) · % Complétude");
  console.log('      Filtre  : (aucun — tous les clusters)\n');

  console.log("  2️⃣  Vue \"🔍 Potentiel sous-exploité\"");
  console.log('      Type    : Table');
  console.log('      Filtres : Score ROI Cluster < 70');
  console.log('                ET Impressions totales > 500');
  console.log('      Tri     : Impressions totales → Décroissant');
  console.log("      → Clusters avec du trafic potentiel mais ROI insuffisant\n");

  console.log('  3️⃣  Vue "📈 À compléter en priorité"');
  console.log('      Type    : Table');
  console.log('      Filtres : % Complétude = "À renforcer 🔧"');
  console.log('                ET Score Autorité moyen > 60');
  console.log('      Tri     : Score ROI Cluster → Décroissant');
  console.log('      → Clusters solides mais incomplets : écrire les satellites manquants\n');

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  💡  Calibrage selon ton site :\n');
  console.log('  Si ton meilleur cluster fait 300 clics/mois → passer Trafic/1000 à Trafic/300');
  console.log('  Si aucun cluster ne dépasse 100€/mois      → passer Revenus/500 à Revenus/100');
  console.log('  (modifier FORMULA_ROI_CLUSTER dans ce script puis relancer)');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
