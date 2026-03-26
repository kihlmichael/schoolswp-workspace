#!/usr/bin/env node
/**
 * setup-notion.js — Crée le Notion Content Engine schoolsWP
 *
 * Usage :
 *   NOTION_API_KEY=secret_xxx NOTION_PARENT_PAGE_ID=xxxx node scripts/setup-notion.js
 *
 * Prérequis :
 *   - Notion integration avec accès "Full page" à la page parente
 *   - Node.js 18+ (fetch natif)
 *
 * Phases d'exécution :
 *   1. Création des 3 bases (Articles, Clusters, Plugins)
 *   2. Relations croisées (Articles ↔ Clusters, Articles ↔ Plugins)
 *   3. Formules (Score Global, Action, % Complétude)
 *   4. Rollups (Trafic total, Score moyen, Revenus)
 *   5. Enregistrements initiaux (6 clusters + 5 plugins)
 */

const API_KEY = process.env.NOTION_API_KEY;
const PARENT_PAGE_ID = process.env.NOTION_PARENT_PAGE_ID;

if (!API_KEY || !PARENT_PAGE_ID) {
  console.error('❌  Variables manquantes\n');
  console.error('    export NOTION_API_KEY=secret_...');
  console.error('    export NOTION_PARENT_PAGE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx');
  process.exit(1);
}

// ─── API helper ──────────────────────────────────────────────────────────────

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

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// ─── Database / record helpers ───────────────────────────────────────────────

async function createDb(title, emoji, properties) {
  return notion('POST', 'databases', {
    parent: { type: 'page_id', page_id: PARENT_PAGE_ID },
    title: [{ type: 'text', text: { content: title } }],
    icon: { type: 'emoji', emoji },
    properties
  });
}

async function updateDb(dbId, properties) {
  return notion('PATCH', `databases/${dbId}`, { properties });
}

async function createRecord(dbId, properties) {
  return notion('POST', 'pages', {
    parent: { database_id: dbId },
    properties
  });
}

// ─── Property schema helpers ─────────────────────────────────────────────────

const sel  = (...opts) => ({ select: { options: opts.map(([n, c]) => ({ name: n, color: c })) } });
const num  = (format = 'number') => ({ number: { format } });
const txt  = () => ({ rich_text: {} });
const url_ = () => ({ url: {} });
const chk  = () => ({ checkbox: {} });
const date_= () => ({ date: {} });
const fml  = (expression) => ({ formula: { expression } });
const rel  = (dbId) => ({ relation: { database_id: dbId, type: 'dual_property', dual_property: {} } });
const roll = (relProp, rollProp, fn) => ({
  rollup: { relation_property_name: relProp, rollup_property_name: rollProp, function: fn }
});

// ─── Main ────────────────────────────────────────────────────────────────────

async function main() {
  console.log('🚀  schoolsWP — Notion Content Engine Setup\n');

  // ── Phase 1 : Créer les 3 bases ────────────────────────────────────────────

  console.log('  📄  Création Articles...');
  const arts = await createDb('Articles', '📄', {
    'Titre':                 { title: {} },
    'URL':                   url_(),
    'Statut':                sel(['Idée', 'gray'], ['En cours', 'yellow'], ['Publié', 'green'], ['Optimisation', 'orange']),
    'Type':                  sel(['Pilier', 'blue'], ['Satellite', 'purple'], ['Comparatif', 'pink'], ['Tutoriel', 'brown']),
    'Mot-clé principal':     txt(),
    'Intent':                sel(['Informationnelle', 'green'], ['Comparative', 'yellow'], ['Décisionnelle', 'red']),
    'Score SEO':             num(),
    'Score LLM':             num(),
    'Score Conversion':      num(),
    'Score Autorité':        num(),
    'Position moyenne':      num(),
    'Impressions':           num(),
    'Clics':                 num(),
    'CTR':                   num('percent'),
    'Temps moyen (min)':     num(),
    'Taux clic affilié':     num('percent'),
    'Leads générés':         num(),
    'Revenus estimés':       num('euro'),
    'Présent AI Overview ?': chk(),
    'Citation LLM ?':        chk(),
    'CTA optimisé ?':        chk(),
    'Maillage entrant':      num(),
    'Maillage sortant':      num(),
    'Lien Google Doc':       url_(),
    'Date création':         date_(),
    'Dernière MAJ':          date_()
  });
  console.log(`        ✅  ${arts.id}`);

  console.log('  🧠  Création Clusters...');
  const clust = await createDb('Clusters', '🧠', {
    'Nom cluster': { title: {} },
    'Priorité':    sel(['Haute', 'red'], ['Moyenne', 'yellow'], ['Basse', 'gray']),
    'Statut':      sel(['Actif', 'green'], ['En construction', 'yellow'], ['Planifié', 'gray'])
  });
  console.log(`        ✅  ${clust.id}`);

  console.log('  🔌  Création Plugins & Outils...');
  const plugs = await createDb('Plugins & Outils', '🔌', {
    'Nom outil':            { title: {} },
    'Catégorie':            sel(['CRM', 'blue'], ['LMS', 'purple'], ['Builder', 'orange'], ['SEO', 'green'], ['E-commerce', 'pink'], ['Performance', 'yellow'], ['Automatisation', 'brown']),
    'Type':                 sel(['Partenaire', 'green'], ['Testé', 'yellow'], ['Neutre', 'gray']),
    'Score recommandation': num(),
    'Lien affilié':         url_(),
    'Notes':                txt()
  });
  console.log(`        ✅  ${plugs.id}`);

  await sleep(600);

  // ── Phase 2 : Relations croisées ───────────────────────────────────────────

  console.log('\n  🔗  Ajout des relations...');

  await updateDb(arts.id, { 'Cluster': rel(clust.id) });
  await sleep(400);

  await updateDb(clust.id, { 'Article pilier': rel(arts.id) });
  await sleep(400);

  // Relation distincte pour éviter collision avec "Article pilier"
  await updateDb(clust.id, { 'Articles satellites': rel(arts.id) });
  await sleep(400);

  await updateDb(plugs.id, { 'Articles liés': rel(arts.id) });
  await sleep(400);

  console.log('        ✅  4 relations créées (dual_property)');
  await sleep(600);

  // ── Phase 3 : Formules ─────────────────────────────────────────────────────

  console.log('\n  🧮  Ajout des formules...');

  await updateDb(arts.id, {
    'Score Global': fml(
      'round((prop("Score SEO") * 0.25) + (prop("Score LLM") * 0.15) + (prop("Score Conversion") * 0.30) + (prop("Score Autorité") * 0.30))'
    )
  });
  await sleep(400);

  await updateDb(arts.id, {
    'Action': fml(
      'if(prop("Score Global") >= 95, "✅ Actif Premium", if(prop("Score Global") >= 85, "🟢 Actif Performant", if(prop("Score Global") >= 70, "🟡 Optimiser", "🔴 Révision Stratégique")))'
    )
  });
  await sleep(400);

  await updateDb(clust.id, {
    '% Complétude': fml(
      'if(length(prop("Articles satellites")) >= 5, "Complet ✅", "À renforcer 🔧")'
    )
  });
  await sleep(400);

  console.log('        ✅  3 formules créées');
  await sleep(600);

  // ── Phase 4 : Rollups ──────────────────────────────────────────────────────

  console.log('\n  📊  Ajout des rollups...');

  await updateDb(clust.id, {
    'Trafic total': roll('Articles satellites', 'Clics', 'sum')
  });
  await sleep(400);

  // Rollup sur formule — si erreur API, configurer manuellement dans Notion
  await updateDb(clust.id, {
    'Score moyen cluster': roll('Articles satellites', 'Score Global', 'average')
  }).catch(() => console.warn('        ⚠️  Score moyen cluster : configurer manuellement (rollup sur formule)'));
  await sleep(400);

  await updateDb(clust.id, {
    'Revenus cluster': roll('Articles satellites', 'Revenus estimés', 'sum')
  });
  await sleep(400);

  await updateDb(plugs.id, {
    'Revenus générés': roll('Articles liés', 'Revenus estimés', 'sum')
  });
  await sleep(400);

  console.log('        ✅  4 rollups créés');
  await sleep(600);

  // ── Phase 5 : Enregistrements initiaux ────────────────────────────────────

  console.log('\n  🌱  Création enregistrements initiaux...');

  const clusterSeeds = [
    ['SEO WordPress',  'Haute',   'Actif'],
    ['LMS WordPress',  'Haute',   'Actif'],
    ['CRM WordPress',  'Haute',   'En construction'],
    ['WooCommerce',    'Moyenne', 'Actif'],
    ['Performance',    'Moyenne', 'En construction'],
    ['Automatisation', 'Basse',   'Planifié']
  ];

  for (const [nom, priorite, statut] of clusterSeeds) {
    await createRecord(clust.id, {
      'Nom cluster': { title: [{ text: { content: nom } }] },
      'Priorité':    { select: { name: priorite } },
      'Statut':      { select: { name: statut } }
    });
    await sleep(350);
  }
  console.log('        ✅  6 clusters créés');

  const pluginSeeds = [
    ['Rank Math',  'SEO',         'Testé'],
    ['FluentCRM',  'CRM',         'Partenaire'],
    ['TutorLMS',   'LMS',         'Testé'],
    ['WP Rocket',  'Performance', 'Partenaire'],
    ['Elementor',  'Builder',     'Testé']
  ];

  for (const [nom, cat, type] of pluginSeeds) {
    await createRecord(plugs.id, {
      'Nom outil':  { title: [{ text: { content: nom } }] },
      'Catégorie':  { select: { name: cat } },
      'Type':       { select: { name: type } }
    });
    await sleep(350);
  }
  console.log('        ✅  5 plugins créés');

  // ── Résultat ───────────────────────────────────────────────────────────────

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log('✅  Notion Content Engine schoolsWP créé avec succès !\n');
  console.log('📋  IDs à noter :');
  console.log(`    NOTION_ARTICLES_DB_ID = ${arts.id}`);
  console.log(`    NOTION_CLUSTERS_DB_ID = ${clust.id}`);
  console.log(`    NOTION_PLUGINS_DB_ID  = ${plugs.id}`);
  console.log('\n🔧  Étapes manuelles restantes :');
  console.log('    1. Dans notion-kpi-tracker.json → remplacer VOTRE_NOTION_DATABASE_ID');
  console.log(`       par : ${arts.id}`);
  console.log('    2. Créer la page "📊 Dashboard KPI" (vues filtrées)');
  console.log('       → voir docs/notion-content-engine.md section 4');
  console.log('    3. Vérifier "Score moyen cluster" (rollup sur formule)');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');
}

main().catch(e => {
  console.error('\n❌  Erreur fatale :', e.message);
  process.exit(1);
});
