#!/usr/bin/env node
/**
 * setup-notion-revenue-engine.js — Revenue Mapping schoolsWP
 *
 * Crée la base "🔌 Revenue Engine — Plugins & Écosystèmes" avec :
 *
 *   22 propriétés de base   : infos plugin · indicateurs business · potentiel · couverture contenu
 *   3  rollups               : Trafic total · Position moyenne · Score Autorité (si Articles DB fourni)
 *   4  formules              : Revenus trimestriels · ROI estimé · % Exploitation · Label Exploitation
 *   6  enregistrements seed  : plugins clés schoolsWP (FluentCRM · Tutor LMS · Rank Math · ...)
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx \
 *   NOTION_PARENT_PAGE_ID=xxx \
 *   NOTION_ARTICLES_DB_ID=xxx \          # optionnel — active rollups depuis Articles
 *   node scripts/setup-notion-revenue-engine.js
 *
 * Pré-requis : Node 18+ (fetch natif)
 *
 * Saisie des taux : entrer le chiffre brut, ex. 5 pour 5%
 * (La formule ROI divise par 100 automatiquement.)
 */

const API_KEY    = process.env.NOTION_API_KEY;
const PAGE_ID    = process.env.NOTION_PARENT_PAGE_ID;
const ART_DB_ID  = process.env.NOTION_ARTICLES_DB_ID;   // optionnel

if (!API_KEY || !PAGE_ID) {
  console.error('❌  Variables manquantes');
  console.error('    NOTION_API_KEY         — obligatoire');
  console.error('    NOTION_PARENT_PAGE_ID  — obligatoire (page parente dans Notion)');
  console.error('    NOTION_ARTICLES_DB_ID  — optionnel  (active rollups Trafic / Position / Autorité)');
  process.exit(1);
}

// ─── API helpers ──────────────────────────────────────────────────────────────

async function notion(method, endpoint, body) {
  const resp = await fetch(`https://api.notion.com/v1/${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json'
    },
    body: body ? JSON.stringify(body) : undefined
  });
  if (!resp.ok) {
    const err = await resp.json().catch(() => ({}));
    throw new Error(`${method} /${endpoint} → ${resp.status}: ${err.message || JSON.stringify(err)}`);
  }
  return resp.json();
}

const sleep   = (ms) => new Promise(r => setTimeout(r, ms));
const num     = (format = 'number') => ({ number: { format } });
const sel     = (...opts) => ({ select: { options: opts.map(([n, c]) => ({ name: n, color: c })) } });
const fml     = (expression) => ({ formula: { expression } });
const roll    = (rel, prop, fn) => ({ rollup: { relation_property_name: rel, rollup_property_name: prop, function: fn } });

// ─── Formules ─────────────────────────────────────────────────────────────────

// Revenus trimestriels = revenus mensuels × 3
const FORMULA_REVENUS_Q = 'round(prop("Revenus mensuels") * 3)';

// ROI estimé :
//   Si rollups dispo → utilise Trafic total réel
//   Sinon            → estime Trafic = Volume × 5% (CTR organique moyen)
const FORMULA_ROI_WITH_ROLLUP =
  'if(prop("Trafic total") > 0, ' +
    'round(prop("Trafic total") * (prop("Taux clic affilié") / 100) * (prop("Taux conversion affilié") / 100) * prop("Commission moyenne")), ' +
    'round((prop("Volume de recherche") * 0.05) * (prop("Taux clic affilié") / 100) * (prop("Taux conversion affilié") / 100) * prop("Commission moyenne"))' +
  ')';

const FORMULA_ROI_NO_ROLLUP =
  'round((prop("Volume de recherche") * 0.05) * (prop("Taux clic affilié") / 100) * (prop("Taux conversion affilié") / 100) * prop("Commission moyenne"))';

// % Exploitation = combien des 5 contenus clés sont couverts
const FORMULA_EXPLOITATION_PCT =
  'round((' +
    'if(prop("Pilier dédié"), 1, 0) + ' +
    'if(prop("3 satellites"), 1, 0) + ' +
    'if(prop("Comparatif publié"), 1, 0) + ' +
    'if(prop("Tutoriel publié"), 1, 0) + ' +
    'if(prop("Article décisionnel"), 1, 0)' +
  ') / 5 * 100)';

// Label Exploitation — actionnable
const FORMULA_LABEL_EXPLOITATION =
  'if(prop("% Exploitation") >= 80, "✅ Bien exploité", ' +
    'if(prop("% Exploitation") >= 60, "🟡 Partiellement", ' +
      'if(prop("% Exploitation") > 0, "🔴 Sous-exploité", "⬜ Non évalué")))';

// ─── Données seed ─────────────────────────────────────────────────────────────

const SEED_PLUGINS = [
  {
    nom: 'FluentCRM',
    categorie: 'CRM',
    type: 'Affilié',
    cluster: 'CRM WordPress',
    priorite: 'Haute',
    url: 'https://fluentcrm.com/?ref=schoolswp',
    volume: 5400,
    difficulte: 42,
    opportunite: 5,
    commission: 25,
    taux_clic: 4,
    taux_conv: 3,
    revenus: 0,
    notes: 'Plugin CRM natif WordPress — haute valeur affilié, audience idéale schoolsWP'
  },
  {
    nom: 'Tutor LMS',
    categorie: 'LMS',
    type: 'Affilié',
    cluster: 'LMS WordPress',
    priorite: 'Haute',
    url: 'https://tutorlms.com/?ref=schoolswp',
    volume: 3600,
    difficulte: 38,
    opportunite: 5,
    commission: 30,
    taux_clic: 5,
    taux_conv: 2,
    revenus: 0,
    notes: 'LMS principal de schoolsWP — cohérence parfaite avec le positionnement'
  },
  {
    nom: 'Rank Math',
    categorie: 'SEO',
    type: 'Affilié',
    cluster: 'SEO WordPress',
    priorite: 'Haute',
    url: 'https://rankmath.com/?ref=schoolswp',
    volume: 12000,
    difficulte: 58,
    opportunite: 4,
    commission: 20,
    taux_clic: 3,
    taux_conv: 2,
    revenus: 0,
    notes: 'Très gros volume — concurrence forte mais angle "pourquoi Rank Math pour WP" différenciant'
  },
  {
    nom: 'Elementor',
    categorie: 'Builder',
    type: 'Affilié',
    cluster: 'Builders WordPress',
    priorite: 'Moyenne',
    url: 'https://elementor.com/ref/schoolswp',
    volume: 40000,
    difficulte: 72,
    opportunite: 3,
    commission: 50,
    taux_clic: 2,
    taux_conv: 1,
    revenus: 0,
    notes: 'Très gros volume mais concurrence GAFA — miser sur angle "Elementor vs Bricks" niche'
  },
  {
    nom: 'WooCommerce',
    categorie: 'E-commerce',
    type: 'Partenaire',
    cluster: 'E-commerce WordPress',
    priorite: 'Moyenne',
    url: '',
    volume: 60000,
    difficulte: 80,
    opportunite: 3,
    commission: 0,
    taux_clic: 1,
    taux_conv: 1,
    revenus: 0,
    notes: 'Gratuit — monetisation via extensions WooCommerce (extensions affiliées)'
  },
  {
    nom: 'n8n',
    categorie: 'Automatisation',
    type: 'Affilié',
    cluster: 'Automatisation WordPress',
    priorite: 'Haute',
    url: 'https://n8n.io/?ref=schoolswp',
    volume: 8100,
    difficulte: 45,
    opportunite: 5,
    commission: 40,
    taux_clic: 4,
    taux_conv: 2,
    revenus: 0,
    notes: 'Niche forte schoolsWP — audience très qualifiée, intent technique élevé'
  }
];

// ─── Main ──────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Revenue Engine\n');

  // ── Phase 1 : Création base + propriétés de base ──────────────────────────
  console.log('  📊  Phase 1 — Création de la base Revenue Engine...\n');

  const db = await notion('POST', 'databases', {
    parent: { type: 'page_id', page_id: PAGE_ID },
    icon: { type: 'emoji', emoji: '🔌' },
    title: [{ type: 'text', text: { content: 'Revenue Engine — Plugins & Écosystèmes' } }],
    properties: {

      // ── Identité plugin ─────────────────────────────────────────────────
      'Nom plugin':           { title: {} },
      'Catégorie':            sel(['CRM','pink'],['LMS','blue'],['Builder','orange'],['SEO','green'],['E-commerce','purple'],['Automatisation','yellow']),
      'Type':                 sel(['Affilié','red'],['Partenaire','green'],['Neutre','gray']),
      'Cluster principal':    { rich_text: {} },
      'Niveau priorité':      sel(['Haute','red'],['Moyenne','yellow'],['Test','gray']),
      'URL Affilié':          { url: {} },

      // ── Indicateurs business ─────────────────────────────────────────────
      'Clics affiliés':       num(),
      'Taux clic affilié':    num(),      // entrer 5 pour 5% — formule divise par 100
      'Taux conversion affilié': num(),   // entrer 2 pour 2%
      'Commission moyenne':   num('euro'),
      'Revenus mensuels':     num('euro'),
      'Revenus cumulés':      num('euro'),

      // ── Potentiel SEO ────────────────────────────────────────────────────
      'Volume de recherche':  num(),
      'Difficulté SEO':       num(),
      'Opportunité (1-5)':    num(),

      // ── Couverture contenu (5 contenus clés) ────────────────────────────
      'Pilier dédié':         { checkbox: {} },
      '3 satellites':         { checkbox: {} },
      'Comparatif publié':    { checkbox: {} },
      'Tutoriel publié':      { checkbox: {} },
      'Article décisionnel':  { checkbox: {} },

      // ── Meta ─────────────────────────────────────────────────────────────
      'Notes stratégiques':   { rich_text: {} },
      'Dernière MAJ':         { date: {} }
    }
  });

  const DB_ID = db.id;
  console.log(`        ✅  Base créée : ${DB_ID}`);
  console.log('        ✅  22 propriétés de base configurées');
  await sleep(600);

  // ── Phase 2 : Relation Articles (optionnelle) ─────────────────────────────
  let hasRollups = false;

  if (ART_DB_ID) {
    console.log('\n  🔗  Phase 2 — Relation vers base Articles...');

    await notion('PATCH', `databases/${DB_ID}`, {
      properties: {
        'Articles liés': {
          relation: {
            database_id: ART_DB_ID,
            type: 'dual_property',
            dual_property: {}
          }
        }
      }
    });

    console.log('        ✅  Articles liés (relation dual_property → Articles)');
    await sleep(600);

    // ── Phase 3 : Rollups ─────────────────────────────────────────────────
    console.log('\n  📈  Phase 3 — Rollups SEO depuis Articles liés...');

    await notion('PATCH', `databases/${DB_ID}`, {
      properties: { 'Trafic total': roll('Articles liés', 'Clics', 'sum') }
    });
    console.log('        ✅  Trafic total (sum Clics)');
    await sleep(450);

    await notion('PATCH', `databases/${DB_ID}`, {
      properties: { 'Position moyenne cluster': roll('Articles liés', 'Position moyenne', 'average') }
    });
    console.log('        ✅  Position moyenne cluster (avg Position moyenne)');
    await sleep(450);

    await notion('PATCH', `databases/${DB_ID}`, {
      properties: { 'Score Autorité cluster': roll('Articles liés', 'Score Autorité', 'average') }
    });
    console.log('        ✅  Score Autorité cluster (avg Score Autorité)');
    await sleep(500);

    hasRollups = true;

  } else {
    console.log('\n  ⚠️   Phase 2/3 — NOTION_ARTICLES_DB_ID non fourni.');
    console.log('        Rollups Trafic/Position/Autorité ignorés.');
    console.log('        ROI estimé utilisera Volume de recherche × 5% comme approximation.\n');
  }

  // ── Phase 4 : Formules ────────────────────────────────────────────────────
  console.log('\n  🧮  Phase 4 — Formules...');

  await notion('PATCH', `databases/${DB_ID}`, {
    properties: { 'Revenus trimestriels': fml(FORMULA_REVENUS_Q) }
  });
  console.log('        ✅  Revenus trimestriels = Revenus mensuels × 3');
  await sleep(450);

  await notion('PATCH', `databases/${DB_ID}`, {
    properties: {
      'ROI estimé': fml(hasRollups ? FORMULA_ROI_WITH_ROLLUP : FORMULA_ROI_NO_ROLLUP)
    }
  });
  const roiNote = hasRollups
    ? 'Trafic réel × Taux clic × Taux conv × Commission (fallback Volume×5% si pas d\'articles)'
    : 'Volume × 5% × Taux clic × Taux conv × Commission (approximatif — sans rollups)';
  console.log(`        ✅  ROI estimé — ${roiNote}`);
  await sleep(450);

  await notion('PATCH', `databases/${DB_ID}`, {
    properties: { '% Exploitation': fml(FORMULA_EXPLOITATION_PCT) }
  });
  console.log('        ✅  % Exploitation = (5 contenus clés cochés) / 5 × 100');
  await sleep(450);

  await notion('PATCH', `databases/${DB_ID}`, {
    properties: { 'Label Exploitation': fml(FORMULA_LABEL_EXPLOITATION) }
  });
  console.log('        ✅  Label Exploitation → ✅ Bien exploité / 🟡 / 🔴 / ⬜');
  await sleep(500);

  // ── Phase 5 : Seed records ────────────────────────────────────────────────
  console.log('\n  🌱  Phase 5 — Seed : 6 plugins clés schoolsWP...\n');

  for (const p of SEED_PLUGINS) {
    const props = {
      'Nom plugin':             { title: [{ type: 'text', text: { content: p.nom } }] },
      'Catégorie':              { select: { name: p.categorie } },
      'Type':                   { select: { name: p.type } },
      'Cluster principal':      { rich_text: [{ type: 'text', text: { content: p.cluster } }] },
      'Niveau priorité':        { select: { name: p.priorite } },
      'Volume de recherche':    { number: p.volume },
      'Difficulté SEO':         { number: p.difficulte },
      'Opportunité (1-5)':      { number: p.opportunite },
      'Commission moyenne':     { number: p.commission },
      'Taux clic affilié':      { number: p.taux_clic },
      'Taux conversion affilié':{ number: p.taux_conv },
      'Revenus mensuels':       { number: p.revenus },
      'Revenus cumulés':        { number: 0 },
      'Clics affiliés':         { number: 0 },
      'Notes stratégiques':     { rich_text: [{ type: 'text', text: { content: p.notes } }] }
    };

    if (p.url) props['URL Affilié'] = { url: p.url };

    await notion('POST', 'pages', {
      parent: { type: 'database_id', database_id: DB_ID },
      icon: { type: 'emoji', emoji: p.categorie === 'CRM' ? '💬' : p.categorie === 'LMS' ? '🎓' : p.categorie === 'SEO' ? '📊' : p.categorie === 'Builder' ? '🧱' : p.categorie === 'E-commerce' ? '🛒' : '⚙️' },
      properties: props
    });

    const roi = Math.round((p.volume * 0.05) * (p.taux_clic / 100) * (p.taux_conv / 100) * p.commission);
    console.log(`        ✅  ${p.nom.padEnd(18)} Vol: ${String(p.volume).padStart(5)}  ROI potentiel: ~${roi}€/mois`);
    await sleep(400);
  }

  // ── Résultat ───────────────────────────────────────────────────────────────
  const dbUrl = db.url || `https://www.notion.so/${DB_ID.replace(/-/g, '')}`;

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Revenue Engine créé !\n');
  console.log(`  🔗  ${dbUrl}\n`);

  console.log('  📊  Propriétés configurées :\n');
  console.log('  Groupe              Propriétés');
  console.log('  ─────────────────────────────────────────────────────────────');
  console.log('  Identité            Nom plugin · Catégorie · Type · Cluster principal');
  console.log('                      Niveau priorité · URL Affilié');
  console.log('  Indicateurs biz     Clics affiliés · Taux clic affilié · Taux conversion affilié');
  console.log('                      Commission moyenne · Revenus mensuels · Revenus cumulés');
  console.log('  Potentiel SEO       Volume de recherche · Difficulté SEO · Opportunité (1-5)');
  console.log('  Couverture contenu  Pilier dédié · 3 satellites · Comparatif publié');
  console.log('                      Tutoriel publié · Article décisionnel');
  if (hasRollups) {
    console.log('  Rollups SEO         Trafic total · Position moyenne cluster · Score Autorité cluster');
  }
  console.log('  Formules            Revenus trimestriels · ROI estimé · % Exploitation · Label Exploitation');
  console.log('');

  console.log('  📋  3 vues stratégiques à créer manuellement :\n');

  console.log('  1️⃣  Vue "🔥 Top Revenus"');
  console.log('      Type    : Table');
  console.log('      Tri     : Revenus mensuels DESC');
  console.log('      Colonnes: Nom plugin · Catégorie · Revenus mensuels · Revenus trimestriels');
  console.log('               · ROI estimé · % Exploitation · Label Exploitation\n');

  console.log('  2️⃣  Vue "🚀 Potentiel non exploité"');
  console.log('      Type    : Table');
  console.log('      Filtres : Volume de recherche > 2000');
  console.log('                ET Revenus mensuels < 200');
  console.log('      Tri     : Volume de recherche DESC');
  console.log('      → Plugins avec gros volume mais revenus faibles = cluster à créer\n');

  console.log('  3️⃣  Vue "🧱 Dominance stratégique"');
  if (hasRollups) {
    console.log('      Type    : Table');
    console.log('      Filtres : Score Autorité cluster > 85');
    console.log('                ET % Exploitation >= 80');
    console.log('      → Plugins avec expertise validée + contenus complets = leaders');
  } else {
    console.log('      Type    : Table');
    console.log('      Filtres : Opportunité (1-5) = 5');
    console.log('                ET % Exploitation >= 80');
    console.log('      → Plugins prioritaires bien couverts = positionnement expert validé');
  }
  console.log('');

  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('  🧠  Workflow Revenue Mapping :\n');
  console.log('  1.  Pour chaque plugin → renseigner Taux clic affilié + Taux conversion + Commission');
  console.log('      (demander au programme d\'affiliation ou estimer depuis les rapports)');
  console.log('  2.  Cocher les 5 contenus clés (Pilier · Satellites · Comparatif · Tutoriel · Décisionnel)');
  console.log('  3.  Label Exploitation se calcule automatiquement → "🔴 Sous-exploité" = priorité');
  console.log('  4.  Vue "🚀 Potentiel non exploité" → identifier le prochain cluster à créer');
  console.log('  5.  Mettre à jour Revenus mensuels chaque mois (depuis tableau de bord affilié)');
  console.log('');
  console.log('  💡  Barème de scoring Opportunité (1-5) :');
  console.log('      5  → Cluster prioritaire · fort volume · affilié direct · cœur schoolsWP');
  console.log('      4  → Bon potentiel · à développer ce trimestre');
  console.log('      3  → Intéressant mais concurrence moyenne ou faible intent');
  console.log('      2  → Secondaire · couvrir après les priorités');
  console.log('      1  → Test · surveiller avant d\'investir du contenu');
  console.log('');
  console.log('  📌  Variable : DB Revenue Engine ID');
  console.log(`      NOTION_REVENUE_DB_ID=${DB_ID}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
