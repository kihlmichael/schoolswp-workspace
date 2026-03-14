/**
 * sync-gsc-notion.gs — Synchronisation GSC → Notion : schoolsWP Content Engine
 *
 * Fonctionnement :
 *   1. Récupère toutes les pages Notion (base Articles) qui ont une URL
 *   2. Interroge GSC pour les 28 derniers jours (ou LOOKBACK_DAYS)
 *   3. Joint les deux datasets sur l'URL
 *   4. Patche chaque page Notion avec les métriques GSC réelles
 *   5. Log un résumé dans la console Apps Script
 *
 * Setup :
 *   1. script.google.com → Nouveau projet
 *   2. Extensions → Services avancés → activer "Search Console API" v3
 *   3. Remplir la section CONFIG ci-dessous
 *   4. Lancer syncGSCtoNotion() une première fois (autorisation OAuth)
 *   5. Déclencheur : Triggers → createWeeklyTrigger() ou manuellement
 *
 * Permissions OAuth requises :
 *   - https://www.googleapis.com/auth/webmasters.readonly
 *   - https://www.googleapis.com/auth/script.external_request
 */

// ─── CONFIGURATION ────────────────────────────────────────────────────────────

const CONFIG = {
  NOTION_TOKEN:  'VOTRE_NOTION_API_KEY',          // secret_xxx
  DATABASE_ID:   'VOTRE_ARTICLES_DB_ID',           // ID base Articles Notion
  SITE_URL:      'https://schoolswp.com/',          // URL exacte dans GSC (avec slash final)
  LOOKBACK_DAYS: 28,                               // Fenêtre rolling
  ROW_LIMIT:     25000,                            // Max lignes GSC

  // Noms exacts des propriétés dans la base Articles Notion
  PROPS: {
    url:              'URL',
    impressions:      'Impressions',
    clics:            'Clics',
    ctr:              'CTR',
    position:         'Position moyenne',
    positionActuelle: 'Position actuelle',  // Module Priorité Automatique (si installé)
    derniereMaj:      'Dernière MAJ'
  }
};

// ─── POINT D'ENTRÉE PRINCIPAL ─────────────────────────────────────────────────

function syncGSCtoNotion() {
  Logger.log('🚀  schoolsWP — Sync GSC → Notion\n');

  // Calcul de la fenêtre de dates
  const today  = new Date();
  const start  = new Date(today.getTime() - CONFIG.LOOKBACK_DAYS * 86400000);
  const endDate   = _formatDate(today);
  const startDate = _formatDate(start);
  Logger.log(`📅  Période : ${startDate} → ${endDate}`);

  // Phase 1 : Récupérer les articles Notion avec URL
  Logger.log('\n📋  Chargement des articles Notion...');
  const notionMap = _getAllNotionArticles();
  const notionCount = Object.keys(notionMap).length;
  Logger.log(`    → ${notionCount} articles avec URL trouvés`);
  if (notionCount === 0) {
    Logger.log('⚠️  Aucun article avec URL dans Notion. Vérifier la colonne "URL".');
    return;
  }

  // Phase 2 : Récupérer les données GSC
  Logger.log('\n🔍  Interrogation GSC...');
  const gscMap = _getGSCData(startDate, endDate);
  const gscCount = Object.keys(gscMap).length;
  Logger.log(`    → ${gscCount} URLs dans GSC (28 jours)`);

  // Phase 3 : Mise à jour Notion
  Logger.log('\n📤  Mise à jour Notion...');
  let updated = 0, notFound = 0, errors = 0;
  const dateSync = endDate;

  for (const [url, pageId] of Object.entries(notionMap)) {
    const gsc = gscMap[url];
    if (!gsc) {
      notFound++;
      continue;
    }
    try {
      _updateNotionPage(pageId, gsc, dateSync);
      updated++;
      // Throttle : 3 req/sec max (Notion API rate limit)
      Utilities.sleep(400);
    } catch (e) {
      errors++;
      Logger.log(`    ❌  ${url} → ${e.message}`);
    }
  }

  // Résumé
  Logger.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  Logger.log(`✅  Sync terminée`);
  Logger.log(`    Mises à jour : ${updated}`);
  Logger.log(`    Non trouvés dans GSC : ${notFound}`);
  Logger.log(`    Erreurs : ${errors}`);
  Logger.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
}

// ─── HELPERS GSC ──────────────────────────────────────────────────────────────

function _getGSCData(startDate, endDate) {
  const response = SearchConsole.Searchanalytics.query(
    {
      startDate:  startDate,
      endDate:    endDate,
      dimensions: ['page'],
      rowLimit:   CONFIG.ROW_LIMIT,
      startRow:   0
    },
    CONFIG.SITE_URL
  );

  const map = {};
  for (const row of (response.rows || [])) {
    const url = row.keys[0];
    if (!url) continue;
    map[url] = {
      clics:       Math.round(row.clicks       || 0),
      impressions: Math.round(row.impressions  || 0),
      ctr:         Math.round((row.ctr || 0) * 10000) / 10000, // décimal 0-1
      position:    Math.round((row.position    || 0) * 10) / 10
    };
  }
  return map;
}

// ─── HELPERS NOTION ───────────────────────────────────────────────────────────

/**
 * Récupère toutes les pages Articles avec une URL renseignée.
 * Gère la pagination Notion (100 pages max par requête).
 * @returns {{ [url: string]: string }} map URL → pageId
 */
function _getAllNotionArticles() {
  const map = {};
  let cursor = null;

  do {
    const body = {
      page_size: 100,
      filter: {
        property: CONFIG.PROPS.url,
        url: { is_not_empty: true }
      }
    };
    if (cursor) body.start_cursor = cursor;

    const resp = UrlFetchApp.fetch(
      `https://api.notion.com/v1/databases/${CONFIG.DATABASE_ID}/query`,
      {
        method: 'post',
        headers: _notionHeaders(),
        payload: JSON.stringify(body),
        muteHttpExceptions: true
      }
    );

    if (resp.getResponseCode() !== 200) {
      throw new Error(`Notion Query → ${resp.getResponseCode()}: ${resp.getContentText().slice(0, 200)}`);
    }

    const data = JSON.parse(resp.getContentText());
    for (const page of (data.results || [])) {
      const urlProp = page.properties[CONFIG.PROPS.url];
      const url = urlProp?.url || '';
      if (url && url.startsWith('http')) {
        map[url] = page.id;
      }
    }

    cursor = data.has_more ? data.next_cursor : null;
    if (cursor) Utilities.sleep(350); // Throttle pagination

  } while (cursor);

  return map;
}

/**
 * Met à jour une page Notion avec les métriques GSC.
 */
function _updateNotionPage(pageId, gsc, dateSync) {
  const props = {};
  const P = CONFIG.PROPS;

  props[P.impressions]   = { number: gsc.impressions };
  props[P.clics]         = { number: gsc.clics };
  props[P.ctr]           = { number: gsc.ctr };           // format percent = valeur décimale
  props[P.position]      = { number: gsc.position };
  props[P.derniereMaj]   = { date:   { start: dateSync } };

  // Sync "Position actuelle" (module Priorité Automatique) si présent dans la base
  // La requête ne plantera pas si la propriété n'existe pas — Notion l'ignorera.
  props[P.positionActuelle] = { number: gsc.position };

  const resp = UrlFetchApp.fetch(
    `https://api.notion.com/v1/pages/${pageId}`,
    {
      method: 'patch',
      headers: _notionHeaders(),
      payload: JSON.stringify({ properties: props }),
      muteHttpExceptions: true
    }
  );

  const code = resp.getResponseCode();
  if (code !== 200) {
    throw new Error(`PATCH page ${pageId} → ${code}: ${resp.getContentText().slice(0, 150)}`);
  }
}

function _notionHeaders() {
  return {
    'Authorization':  `Bearer ${CONFIG.NOTION_TOKEN}`,
    'Notion-Version': '2022-06-28',
    'Content-Type':   'application/json'
  };
}

function _formatDate(d) {
  return d.toISOString().split('T')[0];
}

// ─── DÉCLENCHEUR AUTOMATIQUE ─────────────────────────────────────────────────

/**
 * createWeeklyTrigger() — Lance syncGSCtoNotion chaque lundi à 8h.
 * À exécuter une seule fois depuis l'éditeur Apps Script.
 */
function createWeeklyTrigger() {
  // Supprimer les déclencheurs existants pour cette fonction
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'syncGSCtoNotion')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('syncGSCtoNotion')
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .atHour(8)
    .create();

  Logger.log('✅  Déclencheur créé : syncGSCtoNotion → lundi 8h');
}

/**
 * createDailyTrigger() — Alternative : sync quotidienne à 7h.
 */
function createDailyTrigger() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'syncGSCtoNotion')
    .forEach(t => ScriptApp.deleteTrigger(t));

  ScriptApp.newTrigger('syncGSCtoNotion')
    .timeBased()
    .everyDays(1)
    .atHour(7)
    .create();

  Logger.log('✅  Déclencheur créé : syncGSCtoNotion → quotidien 7h');
}
