#!/usr/bin/env node
/**
 * schoolsWP — Airtable Content Engine Setup
 *
 * Crée automatiquement les 5 tables du Content Engine dans une base Airtable :
 *   Articles · Clusters · KPIs · Automatisations · Backlog
 *
 * PRÉREQUIS :
 *   1. Node.js ≥ 18 (fetch natif intégré)
 *   2. Créer une base Airtable vide sur https://airtable.com
 *   3. Générer un Personal Access Token (PAT) sur https://airtable.com/create/tokens
 *      Scopes requis : schema.bases:write · data.records:write
 *   4. Récupérer le BASE_ID dans l'URL de ta base : https://airtable.com/appXXXXXX/...
 *
 * EXÉCUTION :
 *   AIRTABLE_BASE_ID=appXXX AIRTABLE_TOKEN=patXXX node setup-airtable.js
 *   # ou via .env :
 *   node -e "require('dotenv').config()" setup-airtable.js
 */

const BASE_ID = process.env.AIRTABLE_BASE_ID || 'VOTRE_BASE_ID';
const TOKEN   = process.env.AIRTABLE_TOKEN   || 'VOTRE_PERSONAL_ACCESS_TOKEN';
const META    = `https://api.airtable.com/v0/meta/bases/${BASE_ID}`;
const DATA    = `https://api.airtable.com/v0/${BASE_ID}`;

const HEADERS = {
  'Authorization': `Bearer ${TOKEN}`,
  'Content-Type':  'application/json',
};

// ─── Helpers ────────────────────────────────────────────────────────────────

async function api(method, url, body) {
  const res = await fetch(url, {
    method,
    headers: HEADERS,
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json();
  if (!res.ok) throw new Error(`[${res.status}] ${url}\n${JSON.stringify(data, null, 2)}`);
  return data;
}

async function createTable(name, description, fields) {
  process.stdout.write(`\n📋 Création "${name}" ... `);
  const t = await api('POST', `${META}/tables`, { name, description, fields });
  console.log(`✅ (id: ${t.id})`);
  return t;
}

async function addField(tableId, field) {
  process.stdout.write(`   ➕ "${field.name}" ... `);
  const f = await api('POST', `${META}/tables/${tableId}/fields`, field);
  console.log('✅');
  return f;
}

async function addRecords(tableId, records) {
  process.stdout.write(`   📝 ${records.length} enregistrement(s) ... `);
  const r = await api('POST', `${DATA}/${tableId}`, { records });
  console.log('✅');
  return r;
}

const select = (name, choices) => ({
  name,
  type: 'singleSelect',
  options: { choices: choices.map(([n, color]) => ({ name: n, color })) },
});

const number = (name, precision = 0) => ({
  name,
  type: 'number',
  options: { precision },
});

const link = (name, linkedTableId) => ({
  name,
  type: 'multipleRecordLinks',
  options: { linkedTableId },
});

// ─── Schémas ────────────────────────────────────────────────────────────────

const ARTICLES_BASIC = [
  { name: 'Titre',                type: 'singleLineText' },                           // PRIMARY
  { name: 'Slug',                 type: 'singleLineText' },
  select('Type', [
    ['Pilier',    'purpleBright'],
    ['Satellite', 'blueBright'],
    ['Hub',       'cyanBright'],
  ]),
  select('Statut', [
    ['Idée',         'grayBright'],
    ['Rédaction',    'blueBright'],
    ['Audit',        'yellowBright'],
    ['Publié',       'greenBright'],
    ['Optimisation', 'orangeBright'],
  ]),
  { name: 'URL publiée',          type: 'url' },
  { name: 'Mot-clé principal',    type: 'singleLineText' },
  select('Intent', [
    ['Informationnelle', 'tealBright'],
    ['Comparative',      'blueBright'],
    ['Décisionnelle',    'purpleBright'],
  ]),
  // ── Bloc SEO ──
  number('Score SEO'),
  number('Position moyenne', 1),
  number('Impressions'),
  number('CTR %', 1),
  number('Clics'),
  // ── Bloc LLM ──
  { name: 'Optimisé LLM ?',        type: 'checkbox', options: { icon: 'check', color: 'greenBright' } },
  { name: 'AI Overview visible ?', type: 'checkbox', options: { icon: 'star', color: 'yellowBright' } },
  { name: 'Bloc réponse rapide ?', type: 'checkbox', options: { icon: 'check', color: 'cyanBright' } },
  { name: 'FAQ structurée ?',      type: 'checkbox', options: { icon: 'check', color: 'cyanBright' } },
  // ── Bloc Conversion ──
  number('Score Conversion'),
  select('CTA type', [
    ['Lead',        'greenBright'],
    ['Affiliation', 'orangeBright'],
    ['Autorité',    'purpleBright'],
  ]),
  number('Leads générés'),
  number('Clics affiliés'),
  number('Taux conversion %', 1),
  // ── Bloc Autorité ──
  number('Score Autorité'),
  number('Maillage sortant'),
  number('Maillage entrant'),
  select('Pilier', [
    ['SEO',            'blueBright'],
    ['LMS',            'purpleBright'],
    ['CRM',            'greenBright'],
    ['Performance',    'orangeBright'],
    ['Automatisation', 'redBright'],
    ['Ecommerce',      'tealBright'],
  ]),
  // ── Meta ──
  { name: 'Date publication', type: 'date',          options: { dateFormat: { name: 'european', format: 'D/M/YYYY' } } },
  { name: 'Lien Google Doc',  type: 'url' },
  { name: 'Notes',            type: 'multilineText' },
];

const CLUSTERS_BASIC = [
  { name: 'Nom du cluster',         type: 'singleLineText' },                   // PRIMARY
  select('Type', [
    ['SEO WordPress',           'blueBright'],
    ['LMS / Formation',         'purpleBright'],
    ['CRM / Email Marketing',   'greenBright'],
    ['Performance WordPress',   'orangeBright'],
    ['Automatisation',          'redBright'],
    ['E-commerce WordPress',    'tealBright'],
  ]),
  number('Trafic cluster'),
  { name: 'Revenus affiliés €', type: 'currency', options: { precision: 2, symbol: '€' } },
  number('% complétude', 0),
  { name: 'Notes', type: 'multilineText' },
];

const KPIS_FIELDS = [
  { name: 'Mois',                type: 'singleLineText' },                        // PRIMARY (format : YYYY-MM)
  number('Articles publiés'),
  number('Score Global moyen', 1),
  number('Trafic organique'),
  number('Leads'),
  { name: 'Revenus affiliés €', type: 'currency', options: { precision: 2, symbol: '€' } },
  number('AI Visibility %', 1),
  number('CTR moyen %', 1),
  number('Position moyenne', 1),
  { name: 'Notes', type: 'multilineText' },
];

const AUTO_FIELDS = [
  { name: 'Nom',                   type: 'singleLineText' },                     // PRIMARY
  { name: 'Trigger',               type: 'multilineText' },
  { name: 'Action',                type: 'multilineText' },
  select('Statut', [
    ['Actif',       'greenBright'],
    ['En test',     'yellowBright'],
    ['Désactivé',   'grayBright'],
    ['Erreur',      'redBright'],
  ]),
  select('Outil', [
    ['n8n',         'redBright'],
    ['Zapier',      'orangeBright'],
    ['Make',        'purpleBright'],
    ['Airtable',    'tealBright'],
  ]),
  { name: 'Dernier run',           type: 'singleLineText' },
  { name: 'Résultat dernier run',  type: 'singleLineText' },
  { name: 'Lien workflow',         type: 'url' },
  { name: 'Notes',                 type: 'multilineText' },
];

const BACKLOG_FIELDS = [
  { name: 'Sujet',            type: 'singleLineText' },                           // PRIMARY
  { name: 'Mot-clé',          type: 'singleLineText' },
  select('Intent', [
    ['Informationnelle', 'tealBright'],
    ['Comparative',      'blueBright'],
    ['Décisionnelle',    'purpleBright'],
  ]),
  number('Score opportunité'),
  select('Priorité', [
    ['Haute',   'redBright'],
    ['Moyenne', 'yellowBright'],
    ['Basse',   'grayBright'],
  ]),
  { name: 'Potentiel business', type: 'multilineText' },
  number('Volume estimé'),
  number('Difficulté KD'),
  { name: 'Cluster cible (texte)',  type: 'singleLineText' },
  { name: 'Date ajout',            type: 'date', options: { dateFormat: { name: 'european', format: 'D/M/YYYY' } } },
  { name: 'Notes',                 type: 'multilineText' },
];

// ─── Main ────────────────────────────────────────────────────────────────────

async function main() {
  console.log('\n🧠 schoolsWP — Airtable Content Engine Setup');
  console.log('═'.repeat(50));

  if (BASE_ID === 'VOTRE_BASE_ID' || TOKEN === 'VOTRE_PERSONAL_ACCESS_TOKEN') {
    console.error('\n❌ Configure tes identifiants Airtable :');
    console.error('   AIRTABLE_BASE_ID=appXXX AIRTABLE_TOKEN=patXXX node setup-airtable.js\n');
    process.exit(1);
  }

  // ── Étape 1 : Créer les 5 tables ──────────────────────────────────────────

  console.log('\n⏳ Étape 1/4 — Création des 5 tables...');

  const articles = await createTable(
    'Articles',
    'Table principale — articles SEO schoolsWP avec scores internes + données GSC',
    ARTICLES_BASIC
  );

  const clusters = await createTable(
    'Clusters',
    'Clusters sémantiques WordPress — piliers + satellites + métriques agrégées',
    CLUSTERS_BASIC
  );

  const kpis = await createTable(
    'KPIs',
    'Vue mensuelle des KPI globaux — trafic, leads, revenus, scores moyens',
    KPIS_FIELDS
  );

  const automatisations = await createTable(
    'Automatisations',
    'Référentiel des automatisations n8n / Zapier / Make connectées au Content Engine',
    AUTO_FIELDS
  );

  const backlog = await createTable(
    'Backlog',
    'Pipeline éditorial — sujets qualifiés en attente de production V2',
    BACKLOG_FIELDS
  );

  // ── Étape 2 : Ajouter les champs de relation ───────────────────────────────

  console.log('\n⏳ Étape 2/4 — Ajout des relations entre tables...');

  await addField(articles.id, link('Cluster lié', clusters.id));
  await addField(clusters.id, link('Article pilier', articles.id));
  await addField(clusters.id, link('Satellites', articles.id));
  await addField(backlog.id,  link('Cluster cible', clusters.id));

  // ── Étape 3 : Ajouter les champs calculés ─────────────────────────────────

  console.log('\n⏳ Étape 3/4 — Ajout des formules...');

  // Score Global Articles
  await addField(articles.id, {
    name: 'Score Global',
    type: 'formula',
    options: {
      formula:
        'ROUND(' +
        '({Score SEO}*0.25)+' +
        '({Score Conversion}*0.30)+' +
        '({Score Autorité}*0.30)+' +
        'IF({Optimisé LLM ?},15,0)' +
        ',0)',
    },
  });

  // Tier / Action articles
  await addField(articles.id, {
    name: 'Tier',
    type: 'formula',
    options: {
      formula:
        'IF({Score Global}>=95,"✅ Actif Premium",' +
        'IF({Score Global}>=85,"🟢 Actif Performant",' +
        'IF({Score Global}>=70,"🟡 Optimiser",' +
        '"🔴 Révision")))',
    },
  });

  // Score Global Backlog (opportunité)
  await addField(backlog.id, {
    name: 'Priorité calculée',
    type: 'formula',
    options: {
      formula:
        'IF({Score opportunité}>=80,"🔴 Haute",' +
        'IF({Score opportunité}>=60,"🟡 Moyenne","⚪ Basse"))',
    },
  });

  // ── Étape 4 : Ajouter données initiales ───────────────────────────────────

  console.log('\n⏳ Étape 4/4 — Création des enregistrements initiaux...');

  // 6 clusters schoolsWP par défaut
  await addRecords(clusters.id, [
    { fields: { 'Nom du cluster': 'SEO WordPress',            'Type': 'SEO WordPress',           '% complétude': 0 } },
    { fields: { 'Nom du cluster': 'LMS / Formation',          'Type': 'LMS / Formation',          '% complétude': 0 } },
    { fields: { 'Nom du cluster': 'CRM / Email Marketing',    'Type': 'CRM / Email Marketing',    '% complétude': 0 } },
    { fields: { 'Nom du cluster': 'Performance WordPress',    'Type': 'Performance WordPress',    '% complétude': 0 } },
    { fields: { 'Nom du cluster': 'Automatisation',           'Type': 'Automatisation',           '% complétude': 0 } },
    { fields: { 'Nom du cluster': 'E-commerce WordPress',     'Type': 'E-commerce WordPress',     '% complétude': 0 } },
  ]);

  // 5 automatisations pré-configurées
  await addRecords(automatisations.id, [
    { fields: {
      'Nom':     'V2 → Airtable Publisher',
      'Trigger': 'Fin de pipeline Content Machine V2 (webhook HTTP)',
      'Action':  'Upsert record dans table Articles (PATCH performUpsert)',
      'Statut':  'En test',
      'Outil':   'n8n',
      'Notes':   'Workflow : airtable-publisher.json',
    }},
    { fields: {
      'Nom':     'GSC → KPI Dashboard',
      'Trigger': 'Lundi 7h00 (schedule weekly)',
      'Action':  'Refresh position/CTR/impressions/clics dans Articles + Slack digest',
      'Statut':  'En test',
      'Outil':   'n8n',
      'Notes':   'Workflow : kpi-dashboard-updater.json',
    }},
    { fields: {
      'Nom':     'Score < 85 → Statut Optimisation',
      'Trigger': 'Score Global < 85 à la création/modification d\'un article',
      'Action':  'Champ Statut → "Optimisation"',
      'Statut':  'Actif',
      'Outil':   'Airtable',
      'Notes':   'Automatisation native Airtable : Triggers > When a record matches conditions',
    }},
    { fields: {
      'Nom':     'Impressions > 1000 & CTR < 3% → Alerte titre',
      'Trigger': 'Impressions > 1000 ET CTR % < 3',
      'Action':  'Notification Slack : "Optimiser titre de [Article]"',
      'Statut':  'En test',
      'Outil':   'n8n',
      'Notes':   'Requiert un poll Airtable hebdomadaire depuis n8n',
    }},
    { fields: {
      'Nom':     'AI Overview = non → Ajouter bloc LLM',
      'Trigger': 'AI Overview visible ? = false ET Optimisé LLM ? = false',
      'Action':  'Créer tâche Backlog "Ajouter bloc réponse rapide + FAQ"',
      'Statut':  'En test',
      'Outil':   'Airtable',
      'Notes':   'Automatisation native Airtable avec condition sur checkbox',
    }},
  ]);

  // ── Résumé ────────────────────────────────────────────────────────────────

  console.log('\n' + '═'.repeat(50));
  console.log('✅ Setup Airtable complet !\n');
  console.log('📋 Tables créées :');
  console.log(`   Articles       → ID : ${articles.id}`);
  console.log(`   Clusters       → ID : ${clusters.id}`);
  console.log(`   KPIs           → ID : ${kpis.id}`);
  console.log(`   Automatisations → ID : ${automatisations.id}`);
  console.log(`   Backlog        → ID : ${backlog.id}`);

  console.log('\n📝 Prochaines étapes :');
  console.log('   1. Ouvre ta base Airtable → vérifie les 5 tables');
  console.log('   2. Crée les vues dans Articles :');
  console.log('      · "🔥 Actifs Premium"    → filtre Score Global ≥ 95');
  console.log('      · "⚠️ Sous-performants"  → filtre Score Global < 80');
  console.log('      · "🚀 Potentiel élevé"   → filtre Impressions > 500 ET Position > 10');
  console.log('      · "📋 Pipeline"          → groupe par Statut');
  console.log('   3. Dans n8n → importe airtable-publisher.json');
  console.log(`   4. Configure AIRTABLE_BASE_ID=${BASE_ID} dans .env`);
  console.log('   5. Active le workflow V2 → les articles alimentent Airtable auto\n');

  console.log('💡 IDs à noter dans ton .env :');
  console.log(`   AIRTABLE_BASE_ID=${BASE_ID}`);
  console.log(`   AIRTABLE_TABLE_ARTICLES=${articles.id}`);
  console.log(`   AIRTABLE_TABLE_CLUSTERS=${clusters.id}`);
  console.log(`   AIRTABLE_TABLE_KPIS=${kpis.id}`);
  console.log(`   AIRTABLE_TABLE_BACKLOG=${backlog.id}\n`);
}

main().catch(err => {
  console.error('\n❌ Erreur :', err.message);
  process.exit(1);
});
