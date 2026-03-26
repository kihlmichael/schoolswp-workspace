#!/usr/bin/env node
/**
 * add-notion-content-calendar.js — Content Calendar ROI schoolsWP
 *
 * Ajoute à la base Articles :
 *   5 critères de scoring rapide (1-10, même échelle)
 *   2 propriétés de planification (Trimestre cible · Sprint)
 *   1 formule : Score ROI (weighted /100 — distinct de Score Opportunité)
 *   1 formule : Label ROI (interprétation actionnable)
 *
 * Critères (1-10 chacun) :
 *   Potentiel SEO        × 0.30  Volume + Difficulté + Intent + Concurrence
 *   Potentiel Conversion × 0.25  Affilié + Lead + Intent achat
 *   Impact Autorité      × 0.20  Cluster + Pilier + Satellites
 *   Potentiel LLM        × 0.15  FAQ-ready + Réponse extractible + Comparatif
 *   Effort estimé        × 0.10  INVERSÉ : faible effort = score élevé
 *
 * Score ROI /100 = round(somme pondérée × 10)
 *   85+  → 🔥 Priorité immédiate
 *   70+  → 🟢 Planifier
 *   50+  → 🟡 Secondaire
 *   <50  → ⚫ Backlog
 *
 * Note : Score ROI est DISTINCT de Score Opportunité (sum critères 0-25/15/20).
 *        Les deux coexistent — Score ROI pour le calendar, Score Opportunité pour l'audit.
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_ARTICLES_DB_ID=xxx \
 *   node scripts/add-notion-content-calendar.js
 *
 * Pré-requis : Node 18+
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

// Score ROI — weighted sum × 10 pour normaliser en /100
// Chaque critère 1-10 · Effort est inversé (moins d'effort = meilleur score)
// Plage théorique : ~10 (tout au minimum) → ~99 (tout au maximum)
const FORMULA_SCORE_ROI =
  'if(' +
    'prop("Potentiel SEO") + prop("Potentiel Conversion") + prop("Impact Autorité") + prop("Potentiel LLM") + prop("Effort estimé") > 0, ' +
    'round((' +
      'prop("Potentiel SEO")        * 0.30 + ' +
      'prop("Potentiel Conversion") * 0.25 + ' +
      'prop("Impact Autorité")      * 0.20 + ' +
      'prop("Potentiel LLM")        * 0.15 + ' +
      '(10 - prop("Effort estimé")) * 0.10' +
    ') * 10), ' +
    '0' +
  ')';

// Label ROI — interprétation directement actionnable
const FORMULA_LABEL_ROI =
  'if(prop("Score ROI") >= 85, "🔥 Priorité immédiate", ' +
    'if(prop("Score ROI") >= 70, "🟢 Planifier", ' +
      'if(prop("Score ROI") >= 50, "🟡 Secondaire", ' +
        'if(prop("Score ROI") > 0, "⚫ Backlog", "— Non évalué"))))';

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Content Calendar ROI\n');
  console.log(`  Base Articles : ${DB_ID}\n`);

  // ── Phase 1 : 5 critères de scoring (1-10, même échelle) ──────────────────
  console.log('  📊  Phase 1 — 5 critères de scoring (1-10)...\n');

  await updateDb({
    'Potentiel SEO':        { number: { format: 'number' } },
    'Potentiel Conversion': { number: { format: 'number' } },
    'Impact Autorité':      { number: { format: 'number' } },
    'Potentiel LLM':        { number: { format: 'number' } },
    'Effort estimé':        { number: { format: 'number' } }
  });

  console.log('        ✅  Potentiel SEO        (1-10)  ×0.30  Volume · Difficulté · Intent · Concurrence');
  console.log('        ✅  Potentiel Conversion  (1-10)  ×0.25  Affilié · Lead · Intent achat');
  console.log('        ✅  Impact Autorité       (1-10)  ×0.20  Cluster · Pilier · Satellites');
  console.log('        ✅  Potentiel LLM         (1-10)  ×0.15  FAQ-ready · Réponse extractible');
  console.log('        ✅  Effort estimé         (1-10)  ×0.10  INVERSÉ — faible effort = élevé');
  await sleep(600);

  // ── Phase 2 : Propriétés de planification ─────────────────────────────────
  console.log('\n  📅  Phase 2 — Planification (Trimestre · Sprint)...');

  await updateDb({
    'Trimestre cible': {
      select: {
        options: [
          { name: 'Q1', color: 'blue'   },
          { name: 'Q2', color: 'green'  },
          { name: 'Q3', color: 'orange' },
          { name: 'Q4', color: 'red'    }
        ]
      }
    },
    'Sprint': {
      select: {
        options: [
          { name: 'M1', color: 'blue'   },
          { name: 'M2', color: 'green'  },
          { name: 'M3', color: 'orange' }
        ]
      }
    }
  });

  console.log('        ✅  Trimestre cible (Q1 / Q2 / Q3 / Q4)');
  console.log('        ✅  Sprint (M1 / M2 / M3)');
  await sleep(500);

  // ── Phase 3 : Formule Score ROI ───────────────────────────────────────────
  console.log('\n  🧮  Phase 3 — Formule Score ROI (/100)...');

  await updateDb({
    'Score ROI': { formula: { expression: FORMULA_SCORE_ROI } }
  });

  console.log('        ✅  Score ROI = round((SEO×0.30 + Conv×0.25 + Auth×0.20 + LLM×0.15 + (10-Effort)×0.10) × 10)');
  console.log('            → 0 si aucun critère renseigné (pas de faux positifs)');
  await sleep(500);

  // ── Phase 4 : Formule Label ROI ───────────────────────────────────────────
  console.log('\n  🏷️   Phase 4 — Formule Label ROI...');

  await updateDb({
    'Label ROI': { formula: { expression: FORMULA_LABEL_ROI } }
  });

  console.log('        ✅  🔥 ≥85 Priorité immédiate · 🟢 ≥70 Planifier · 🟡 ≥50 Secondaire · ⚫ <50 Backlog');

  // ── Résultat ───────────────────────────────────────────────────────────────
  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Content Calendar ROI activé !\n');

  console.log('  📊  Barème de scoring (critères 1-10) :\n');
  console.log('  Critère              Poids   Quand mettre 8-10');
  console.log('  ──────────────────────────────────────────────────────────────────');
  console.log('  Potentiel SEO         30%    Volume >1k · KD<50 · Intent claire · concurrents faibles');
  console.log('  Potentiel Conversion  25%    Lien affilié direct · lead magnet évident · intent achat');
  console.log('  Impact Autorité       20%    Renforce cluster actif · pilier ou satellite clé');
  console.log('  Potentiel LLM         15%    FAQ structurable · réponse directe extractible');
  console.log('  Effort estimé         10%    INVERSÉ : 1 = très difficile · 10 = rapide et maîtrisé');
  console.log('  ──────────────────────────────────────────────────────────────────');
  console.log('');
  console.log('  Exemple — "FluentCRM vs MailerLite" :');
  console.log('  SEO=8 · Conv=9 · Auth=8 · LLM=7 · Effort=6');
  console.log('  = round((2.4+2.25+1.6+1.05+0.4) × 10) = round(7.7 × 10) = 77  → 🟢 Planifier');
  console.log('');
  console.log('  Exemple — "Changer la couleur d\'un bouton" :');
  console.log('  SEO=5 · Conv=2 · Auth=2 · LLM=4 · Effort=9');
  console.log('  = round((1.5+0.5+0.4+0.6+0.1) × 10) = round(3.1 × 10) = 31  → ⚫ Backlog');
  console.log('');
  console.log('  Note : Score ROI (calendar /100) ≠ Score Opportunité (audit, sum /100)');
  console.log('         Les deux coexistent — utiliser Score ROI pour prioriser chaque semaine.');
  console.log('');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  📋  4 vues à créer dans Notion :\n');

  console.log('  1️⃣  Vue "📅 Roadmap ROI"  (vue principale du calendar)');
  console.log('      Type    : Table (ou Board groupé par Label ROI)');
  console.log('      Filtres : Statut = Idée OU Planifié');
  console.log('                ET Score ROI > 0');
  console.log('      Tri     : Score ROI DESC · Sprint ASC');
  console.log('      Colonnes: Titre · Label ROI · Score ROI · Sprint · Trimestre cible');
  console.log('               · Cluster · Intent · Potentiel SEO · Potentiel Conversion\n');

  console.log('  2️⃣  Vue "💰 Money Focus"  (articles à fort levier revenu)');
  console.log('      Type    : Table');
  console.log('      Filtres : Potentiel Conversion >= 8');
  console.log('                ET Statut = Idée OU Planifié');
  console.log('      Tri     : Score ROI DESC');
  console.log('      Colonnes: Titre · Label ROI · Score ROI · Potentiel Conversion');
  console.log('               · Cluster · Intent\n');

  console.log('  3️⃣  Vue "⚡ Sprint actif"  (tracker de la semaine)');
  console.log('      Type    : Table');
  console.log('      Filtres : Sprint = M1 (ou M2/M3 selon le mois)');
  console.log('                ET Trimestre cible = Q actuel');
  console.log('      Tri     : Score ROI DESC');
  console.log('      Colonnes: Titre · Statut · Label ROI · Score ROI · Cluster · Sprint\n');

  console.log('  4️⃣  Vue "🧱 Mix contenu"  (équilibre pilier/satellite/comparatif)');
  console.log('      Type    : Board groupé par Intent');
  console.log('      Filtres : Trimestre cible = Q actuel');
  console.log('                ET Score ROI >= 50');
  console.log('      → Vérifier l\'équilibre : ≥1 pilier · ≥3 satellites · ≥2 comparatifs\n');

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  🚀  Workflow hebdo recommandé (15 min le lundi) :\n');
  console.log('  1.  Ouvrir vue "📅 Roadmap ROI" — filtrer Score ROI >= 80');
  console.log('  2.  Vérifier que le prochain article renforce un cluster actif');
  console.log('  3.  Vérifier l\'équilibre Pilier / Satellite / Comparatif (vue Mix)');
  console.log('  4.  Vérifier Potentiel Conversion ≥ 7 (sinon → déprioritiser)');
  console.log('  5.  Lancer la production : brain-lite.bat --keyword "..." --intent ...');
  console.log('');
  console.log('  📊  Vision trimestrielle type (9 articles) :');
  console.log('      1 Pilier cluster (Sprint M1)');
  console.log('      3 Satellites    (Sprint M1-M2)');
  console.log('      2 Comparatifs forts conversion (Sprint M2)');
  console.log('      2 Optimisations articles anciens (Sprint M2-M3)');
  console.log('      1 Article AI / Automatisation  (Sprint M3)');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
