/**
 * schoolsWP — Bootstrap Google Sheets "veille editoriale bihebdo"
 *
 * Usage :
 *  1. Ouvre un nouveau Google Sheet vierge
 *  2. Extensions > Apps Script
 *  3. Colle ce fichier, sauvegarde
 *  4. Lance la fonction `bootstrap()` une seule fois (autorise les scopes)
 *  5. Reviens sur le Sheet : 7 onglets + vues + validations sont en place
 *
 * Reset : lance `resetAll()` pour tout recreer (destructif).
 */

const TABS = {
  sources: 'sources',
  raw: 'raw_items',
  canonical: 'canonical_items',
  itemSources: 'item_sources',
  issues: 'newsletter_issues',
  issueItems: 'issue_items',
  incidents: 'incidents',
};

const VIEWS = {
  candidats: 'vue_candidats_edition',
  doublons: 'vue_doublons_probables',
  offres: 'vue_offres_actives',
  backlogPedago: 'vue_backlog_pedagogie',
  erreurs: 'vue_erreurs_collecte',
};

const HEADERS = {
  [TABS.sources]: [
    'source_id', 'source_name', 'brand_name', 'source_type', 'source_url',
    'collection_method', 'priority_level', 'collection_frequency_hours',
    'is_active', 'last_collected_at', 'error_count_7d', 'notes',
  ],
  [TABS.raw]: [
    'raw_id', 'source_id', 'ingested_at', 'source_published_at',
    'source_url', 'canonical_url', 'email_message_id',
    'title_raw', 'excerpt_raw', 'body_raw', 'hash_raw',
    'language', 'fetch_status',
  ],
  [TABS.canonical]: [
    'item_id', 'cluster_key', 'primary_brand', 'primary_product',
    'version_detected', 'event_type', 'impact_level', 'release_date',
    'first_seen_at', 'last_seen_at',
    'headline_normalized', 'summary_normalized', 'key_points',
    'offer_type', 'offer_deadline', 'links_primary',
    'source_count',
    'impact_score', 'freshness_score', 'audience_fit_score',
    'actionability_score', 'novelty_score',
    'business_value_score', 'pedagogical_value_score', 'noise_penalty',
    'editorial_score', 'confidence_score',
    'status_editorial', 'reason_rejected',
  ],
  [TABS.itemSources]: [
    'item_source_id', 'item_id', 'raw_id', 'source_role',
  ],
  [TABS.issues]: [
    'issue_id', 'issue_number', 'period_start', 'period_end',
    'theme_main', 'editorial_angle', 'status',
    'draft_doc_url', 'sent_at', 'open_rate', 'click_rate',
  ],
  [TABS.issueItems]: [
    'issue_item_id', 'issue_id', 'item_id', 'section_type', 'display_order',
    'editor_note_fait', 'editor_note_pourquoi', 'editor_note_pour_qui',
    'editor_note_retenir', 'performance_note',
  ],
  [TABS.incidents]: [
    'incident_id', 'detected_at', 'source_id', 'severity', 'message', 'resolved_at',
  ],
};

const ENUMS = {
  source_type: ['rss', 'blog', 'changelog', 'email', 'promo', 'api'],
  collection_method: ['rss', 'http', 'gmail_label', 'api'],
  priority_level: [1, 2, 3],
  is_active: [true, false],
  fetch_status: ['ok', 'partial', 'error'],
  event_type: [
    'product_update', 'major_release', 'bugfix_release', 'security_update',
    'launch', 'feature_announcement', 'partnership', 'promotion',
    'acquisition', 'tutorial_resource', 'business_signal', 'ecosystem_news',
  ],
  impact_level: ['low', 'medium', 'high', 'critical'],
  offer_type: ['discount', 'ltd', 'bundle', 'free_trial', 'coupon', ''],
  status_editorial: ['backlog', 'candidate', 'selected', 'rejected', 'archived'],
  source_role: ['primary', 'confirmation', 'duplicate', 'commercial_angle', 'technical_angle'],
  issue_status: ['draft', 'scheduled', 'sent'],
  section_type: [
    'sujet_principal', 'breves', 'mises_a_jour_plugins',
    'offre', 'reco', 'pedagogie', 'business',
  ],
  severity: ['info', 'warning', 'error', 'critical'],
};

function bootstrap() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  Object.values(TABS).forEach(name => ensureSheet_(ss, name, HEADERS[name]));
  applyValidations_(ss);
  applyFormulas_(ss);
  createViews_(ss);
  formatHeaders_(ss);
  seedExampleSources_(ss);
  removeDefaultSheet_(ss);
  SpreadsheetApp.getUi().alert('Bootstrap OK — 7 onglets + 5 vues prets.');
}

function resetAll() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  [...Object.values(TABS), ...Object.values(VIEWS)].forEach(name => {
    const sh = ss.getSheetByName(name);
    if (sh) ss.deleteSheet(sh);
  });
  bootstrap();
}

function ensureSheet_(ss, name, headers) {
  let sh = ss.getSheetByName(name);
  if (!sh) sh = ss.insertSheet(name);
  sh.clear();
  sh.getRange(1, 1, 1, headers.length).setValues([headers]);
  sh.setFrozenRows(1);
  sh.autoResizeColumns(1, headers.length);
}

function formatHeaders_(ss) {
  Object.values(TABS).forEach(name => {
    const sh = ss.getSheetByName(name);
    if (!sh) return;
    const last = sh.getLastColumn();
    sh.getRange(1, 1, 1, last)
      .setFontWeight('bold')
      .setBackground('#1f2937')
      .setFontColor('#ffffff');
  });
}

function applyValidations_(ss) {
  const setList = (sheetName, col, list) => {
    const sh = ss.getSheetByName(sheetName);
    const rule = SpreadsheetApp.newDataValidation()
      .requireValueInList(list.map(String), true)
      .setAllowInvalid(false)
      .build();
    sh.getRange(2, col, sh.getMaxRows() - 1, 1).setDataValidation(rule);
  };

  const head = name => HEADERS[name];
  const idx = (name, col) => head(name).indexOf(col) + 1;

  setList(TABS.sources, idx(TABS.sources, 'source_type'), ENUMS.source_type);
  setList(TABS.sources, idx(TABS.sources, 'collection_method'), ENUMS.collection_method);
  setList(TABS.sources, idx(TABS.sources, 'priority_level'), ENUMS.priority_level);
  setList(TABS.sources, idx(TABS.sources, 'is_active'), ENUMS.is_active);

  setList(TABS.raw, idx(TABS.raw, 'fetch_status'), ENUMS.fetch_status);

  setList(TABS.canonical, idx(TABS.canonical, 'event_type'), ENUMS.event_type);
  setList(TABS.canonical, idx(TABS.canonical, 'impact_level'), ENUMS.impact_level);
  setList(TABS.canonical, idx(TABS.canonical, 'offer_type'), ENUMS.offer_type);
  setList(TABS.canonical, idx(TABS.canonical, 'status_editorial'), ENUMS.status_editorial);

  setList(TABS.itemSources, idx(TABS.itemSources, 'source_role'), ENUMS.source_role);

  setList(TABS.issues, idx(TABS.issues, 'status'), ENUMS.issue_status);

  setList(TABS.issueItems, idx(TABS.issueItems, 'section_type'), ENUMS.section_type);

  setList(TABS.incidents, idx(TABS.incidents, 'severity'), ENUMS.severity);
}

function applyFormulas_(ss) {
  const sh = ss.getSheetByName(TABS.canonical);
  const headers = HEADERS[TABS.canonical];
  const col = name => headers.indexOf(name) + 1;
  const letter = n => {
    let s = '';
    while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); }
    return s;
  };
  const parts = [
    'impact_score', 'freshness_score', 'audience_fit_score',
    'actionability_score', 'novelty_score',
    'business_value_score', 'pedagogical_value_score', 'noise_penalty',
  ].map(c => letter(col(c)) + '2').join(',');
  const edCol = col('editorial_score');
  const formula = `=IFERROR(SUM(${parts}), 0)`;
  const range = sh.getRange(2, edCol, Math.max(sh.getMaxRows() - 1, 1000), 1);
  const formulas = [];
  const n = range.getNumRows();
  for (let i = 0; i < n; i++) {
    const row = i + 2;
    const partsRow = [
      'impact_score', 'freshness_score', 'audience_fit_score',
      'actionability_score', 'novelty_score',
      'business_value_score', 'pedagogical_value_score', 'noise_penalty',
    ].map(c => letter(col(c)) + row).join(',');
    formulas.push([`=IFERROR(SUM(${partsRow}), 0)`]);
  }
  range.setFormulas(formulas);
}

function createViews_(ss) {
  const canonical = TABS.canonical;
  const sources = TABS.sources;

  const view = (name, formula) => {
    let sh = ss.getSheetByName(name);
    if (!sh) sh = ss.insertSheet(name);
    sh.clear();
    sh.getRange('A1').setFormula(formula);
    sh.getRange('A1').setNote('Vue dynamique — ne pas editer manuellement.');
  };

  view(VIEWS.candidats,
    `=QUERY(${canonical}!A:AC, "select * where AB = 'candidate' and Z >= 65 order by Z desc", 1)`);

  view(VIEWS.doublons,
    `=QUERY(${canonical}!A:AC, "select B, C, D, E, F, Q where Q > 1 order by Q desc", 1)`);

  view(VIEWS.offres,
    `=QUERY(${canonical}!A:AC, "select A, C, D, N, O, Z where N is not null and N <> '' and O >= now() order by O asc", 1)`);

  view(VIEWS.backlogPedago,
    `=QUERY(${canonical}!A:AC, "select A, C, D, K, W, Z where W >= 7 and AB = 'backlog' order by W desc", 1)`);

  view(VIEWS.erreurs,
    `=QUERY(${sources}!A:L, "select A, B, C, D, K where K > 3 order by K desc", 1)`);
}

function seedExampleSources_(ss) {
  const sh = ss.getSheetByName(TABS.sources);
  if (sh.getLastRow() > 1) return;
  const rows = [
    ['SRC-001', 'FluentSupport Changelog', 'FluentSupport', 'changelog',
     'https://fluentsupport.com/changelog/', 'rss', 1, 2, true, '', 0, ''],
    ['SRC-002', 'FluentCRM Blog', 'FluentCRM', 'blog',
     'https://fluentcrm.com/blog/feed/', 'rss', 1, 4, true, '', 0, ''],
    ['SRC-003', 'Kadence Blocks Blog', 'Kadence', 'blog',
     'https://www.kadencewp.com/blog/feed/', 'rss', 2, 6, true, '', 0, ''],
    ['SRC-004', 'Newsletters fabricants (Gmail)', 'multiple', 'email',
     'label:newsletter/plugins', 'gmail_label', 1, 1, true, '', 0,
     'Configurer un label Gmail dedie et filtres entrants.'],
  ];
  sh.getRange(2, 1, rows.length, rows[0].length).setValues(rows);
}

function removeDefaultSheet_(ss) {
  const def = ss.getSheetByName('Sheet1') || ss.getSheetByName('Feuille 1');
  if (def && ss.getSheets().length > 1) ss.deleteSheet(def);
}

/** Menu personnalise a l'ouverture */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('schoolsWP')
    .addItem('Bootstrap (init complet)', 'bootstrap')
    .addItem('Reset (destructif)', 'resetAll')
    .addToUi();
}
