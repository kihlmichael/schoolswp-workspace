#!/usr/bin/env node
/**
 * add-notion-seo-priority.js — Module Priorité Automatique schoolsWP
 *
 * Ajoute 6 propriétés SEO à la base Articles existante :
 *   Volume · Difficulté · Position actuelle · Intent stratégique
 *   Potentiel brut (formula) · Score Opportunité (formula)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_ARTICLES_DB_ID=xxx \
 *   node scripts/add-notion-seo-priority.js
 *
 * Prérequis : base Articles déjà créée (via setup-notion.js)
 * Compatible avec une base existante — n'écrase aucune propriété existante.
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

// Potentiel brut = Volume / (Difficulté + 1) — arrondi
// Plus c'est élevé → plus le mot-clé est accessible à fort volume
const FORMULA_POTENTIEL = 'round(prop("Volume") / (prop("Difficulté") + 1))';

// Score Opportunité — pondération 3 axes :
//   40% Potentiel volume/difficulté
//   30% Position actuelle (non classé = max gain possible)
//   30% Intent stratégique (Business direct = priorité max)
const FORMULA_OPPORTUNITE =
  'round(' +
    '((prop("Volume") / (prop("Difficulté") + 1)) * 0.4) + ' +
    '(if(prop("Position actuelle") > 20, 10, if(prop("Position actuelle") > 10, 6, if(prop("Position actuelle") > 3, 3, 1))) * 0.3) + ' +
    '(if(prop("Intent stratégique") == "Business direct", 10, if(prop("Intent stratégique") == "Autorité", 7, if(prop("Intent stratégique") == "Satellite", 5, 8))) * 0.3)' +
  ')';

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Module Priorité Automatique\n');
  console.log(`  Base Articles : ${DB_ID}\n`);

  // ── Phase 1 : Propriétés de base (number + select) ────────────────────────
  console.log('  📊  Ajout des 4 propriétés de base...');
  await updateDb({
    'Volume': {
      number: { format: 'number' }
    },
    'Difficulté': {
      number: { format: 'number' }
    },
    'Position actuelle': {
      number: { format: 'number' }
      // Convention : si non classé → saisir 100
    },
    'Intent stratégique': {
      select: {
        options: [
          { name: 'Business direct',    color: 'red'    },
          { name: 'Autorité',           color: 'blue'   },
          { name: 'Satellite',          color: 'purple' },
          { name: 'Opportunité rapide', color: 'green'  }
        ]
      }
    }
  });
  console.log('        ✅  Volume · Difficulté · Position actuelle · Intent stratégique');
  await sleep(500);

  // ── Phase 2 : Formule Potentiel brut ──────────────────────────────────────
  console.log('\n  🧮  Ajout de la formule Potentiel brut...');
  await updateDb({
    'Potentiel brut': {
      formula: { expression: FORMULA_POTENTIEL }
    }
  });
  console.log('        ✅  round(Volume / (Difficulté + 1))');
  await sleep(500);

  // ── Phase 3 : Formule Score Opportunité ───────────────────────────────────
  console.log('\n  🧮  Ajout de la formule Score Opportunité...');
  await updateDb({
    'Score Opportunité': {
      formula: { expression: FORMULA_OPPORTUNITE }
    }
  });
  console.log('        ✅  Pondération 40% volume · 30% position · 30% intent');

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Module Priorité Automatique activé !\n');

  console.log('  📊  Formules installées :');
  console.log('');
  console.log('  Potentiel brut    = round(Volume / (Difficulté + 1))');
  console.log('');
  console.log('  Score Opportunité = round(');
  console.log('    (Volume / (Difficulté + 1)) × 0.4  ← volume accessible');
  console.log('    + position_score                   × 0.3  ← gap à combler');
  console.log('    + intent_score                     × 0.3  ← valeur business');
  console.log('  )');
  console.log('');
  console.log('  Position → score :  > 20 = 10 · 11-20 = 6 · 4-10 = 3 · ≤ 3 = 1');
  console.log('  Intent   → score :  Business direct = 10 · Autorité = 7 · Satellite = 5 · Opportunité = 8');
  console.log('');

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  📋  2 vues à créer manuellement dans Notion :\n');

  console.log('  1️⃣  Vue "🚀 Priorité rédaction"');
  console.log('      Type    : Table ou Gallery');
  console.log('      Tri     : Score Opportunité → Décroissant');
  console.log('      Colonnes: Titre · Volume · Difficulté · Position actuelle');
  console.log('                Intent stratégique · Potentiel brut · Score Opportunité');
  console.log('      Filtre  : (aucun — tous les articles)');
  console.log('');
  console.log('  2️⃣  Vue "⚡ Quick Wins"');
  console.log('      Type    : Table');
  console.log('      Filtres : Position actuelle > 5');
  console.log('                ET Position actuelle < 20');
  console.log('                ET Volume > 200');
  console.log('      Tri     : Score Opportunité → Décroissant');
  console.log('      → Optimisations les plus rentables à court terme');
  console.log('');

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  📖  Lecture stratégique du Score Opportunité :\n');
  console.log('  Score élevé   = écrire ou optimiser EN PRIORITÉ');
  console.log('  Cas 1 (Jackpot)   : Volume ↑  Difficulté ↓  Position > 20');
  console.log('  Cas 2 (Quick Win) : Volume ↑  Position 8-15 → optimisation title/FAQ');
  console.log('  Cas 3 (Stratégique) : Volume ↓  Intent = Business direct → long terme');
  console.log('');
  console.log('  Convention saisie :');
  console.log('    Position actuelle = 100 si article non encore créé');
  console.log('    Position actuelle = position GSC si article publié');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
