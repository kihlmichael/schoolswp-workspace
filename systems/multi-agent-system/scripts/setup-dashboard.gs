/**
 * schoolsWP — KPI Dashboard Setup Script
 *
 * Crée automatiquement les 4 onglets du Dashboard KPI :
 *   Articles  · Clusters  · Synthèse  · Paramètres
 *
 * USAGE :
 *   1. Ouvre le Google Sheet cible
 *   2. Extensions > Apps Script
 *   3. Colle ce code complet, enregistre (Ctrl+S)
 *   4. Sélectionne setupDashboard → Exécuter
 *   5. Autorise les permissions si demandé
 *
 * FONCTIONS DISPONIBLES :
 *   setupDashboard()   — crée les 4 onglets (run en premier)
 *   refreshFormulas()  — répare Score Global + Action si écrasés
 */


// ╔══════════════════════════════════════════════════════════════╗
// ║                  POINT D'ENTRÉE PRINCIPAL                   ║
// ╚══════════════════════════════════════════════════════════════╝

function setupDashboard() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ui = SpreadsheetApp.getUi();

  const confirm = ui.alert(
    '🧠 schoolsWP — Dashboard KPI',
    'Créer les 4 onglets (Articles, Clusters, Synthèse, Paramètres) ?\n\n' +
    '⚠️ Les onglets existants portant ces noms seront réinitialisés.',
    ui.ButtonSet.OK_CANCEL
  );
  if (confirm !== ui.Button.OK) return;

  _setupParametres(ss);
  _setupArticles(ss);
  _setupClusters(ss);
  _setupSynthese(ss);
  _reorderSheets(ss);

  ui.alert(
    '✅ Dashboard KPI schoolsWP créé !',
    'Prochaines étapes :\n\n' +
    '① Onglet Articles → remplis tes articles (Score SEO / Conv / Auth depuis V2)\n' +
    '② Colonne "URL publiée" → URL WordPress complète (requis pour GSC)\n' +
    '③ Colonne "Cluster" → ex: "CRM / Email Marketing"\n' +
    '④ Lance le workflow n8n kpi-dashboard-updater pour auto-remplir les données GSC\n' +
    '⑤ Connecte ce fichier à Looker Studio comme source de données',
    ui.ButtonSet.OK
  );
}


// ╔══════════════════════════════════════════════════════════════╗
// ║                    ONGLET PARAMÈTRES                        ║
// ╚══════════════════════════════════════════════════════════════╝

function _setupParametres(ss) {
  const sheet = _getOrCreate(ss, 'Paramètres');
  sheet.clearContents();
  sheet.clearFormats();
  sheet.setTabColor('#607D8B');

  //  Row | A (label)                                       | B (valeur)
  const rows = [
    ['🎛️ Paramètres — schoolsWP KPI Dashboard',             ''],         // 1
    ['Modifie les poids et seuils. Toutes les formules se recalculent automatiquement.', ''], // 2
    ['',                                                     ''],         // 3
    ['⚖️ POIDS — Score Global',                              'Valeur'],   // 4  (section)
    ['Poids SEO',                                            0.25],       // 5  ← B5
    ['Poids Conversion',                                     0.30],       // 6  ← B6
    ['Poids Autorité',                                       0.30],       // 7  ← B7
    ['Poids LLM / AI Visibility',                            0.15],       // 8  ← B8
    ['✅ TOTAL (doit être 1,00)',                             '=B5+B6+B7+B8'], // 9
    ['',                                                     ''],         // 10
    ['🎯 SEUILS — Score Global',                             'Score'],    // 11 (section)
    ['Seuil Actif Premium',                                  95],         // 12 ← B12
    ['Seuil Actif Performant',                               85],         // 13 ← B13
    ['Seuil Révision nécessaire',                            70],         // 14 ← B14
    ['',                                                     ''],         // 15
    ['📦 SEUILS — Cluster',                                  'Valeur'],   // 16 (section)
    ['Seuil trafic faible (→ Renforcer SEO)',                500],        // 17 ← B17
    ['Seuil revenus faibles (→ Optimiser Conversion)',       100],        // 18 ← B18
  ];

  sheet.getRange(1, 1, rows.length, 2).setValues(rows);

  // Styles
  sheet.getRange('A1').setFontSize(14).setFontWeight('bold').setFontColor('#00A100');
  sheet.getRange('A2').setFontColor('#757575').setFontStyle('italic').setFontSize(10);

  [[4, '#E3F2FD', '#0D47A1'],
   [11, '#F3E5F5', '#4A148C'],
   [16, '#FFF8E1', '#E65100']].forEach(([r, bg, fc]) => {
    sheet.getRange(r, 1, 1, 2)
      .setBackground(bg).setFontWeight('bold').setFontColor(fc);
  });

  sheet.getRange('B5:B9').setNumberFormat('0.00');
  sheet.getRange('B9').setFontWeight('bold');

  // B9 rouge si total ≠ 1
  sheet.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberNotEqualTo(1)
      .setBackground('#FFCDD2').setFontColor('#B71C1C')
      .setRanges([sheet.getRange('B9')]).build()
  ]);

  sheet.setColumnWidth(1, 320);
  sheet.setColumnWidth(2, 120);
  sheet.setFrozenRows(1);
}


// ╔══════════════════════════════════════════════════════════════╗
// ║                     ONGLET ARTICLES                         ║
// ╚══════════════════════════════════════════════════════════════╝

function _setupArticles(ss) {
  const sheet = _getOrCreate(ss, 'Articles');
  sheet.clearContents();
  sheet.clearFormats();
  sheet.setTabColor('#00D400');

  // 25 colonnes
  const headers = [
    'Article',            // A  col 1   ← saisie
    'URL publiée',        // B  col 2   ← saisie (requis pour GSC)
    'Type',               // C  col 3   ← Pilier / Satellite / Hub
    'Mot-clé',            // D  col 4   ← saisie
    'Intent',             // E  col 5   ← informationnelle / comparative / décisionnelle
    'Score SEO',          // F  col 6   ← copié depuis V2
    'Score Conversion',   // G  col 7   ← copié depuis V2
    'Score Autorité',     // H  col 8   ← copié depuis V2
    'Score LLM',          // I  col 9   ← saisie manuelle (AI Overview + Citation LLM)
    'Score Global',       // J  col 10  ← ARRAYFORMULA auto
    'Action',             // K  col 11  ← ARRAYFORMULA auto
    '[GSC] Position',     // L  col 12  ← rempli par n8n kpi-dashboard-updater
    '[GSC] CTR %',        // M  col 13  ← rempli par n8n
    '[GSC] Impressions',  // N  col 14  ← rempli par n8n
    '[GSC] Clics',        // O  col 15  ← rempli par n8n
    'Leads',              // P  col 16  ← saisie ou GA4
    'Revenus €',          // Q  col 17  ← saisie
    'Satellites liés',    // R  col 18  ← saisie (#)
    'Maillage sortant',   // S  col 19  ← saisie (#)
    'Maillage entrant',   // T  col 20  ← saisie (#)
    'Cluster',            // U  col 21  ← ex: "CRM / Email Marketing"
    'Pilier',             // V  col 22  ← ex: "CRM"
    'Statut',             // W  col 23  ← Brouillon / Publié / À réviser
    'Lien Doc',           // X  col 24  ← lien Google Doc V2
    'Dernière MAJ',       // Y  col 25  ← rempli par n8n
  ];

  sheet.getRange(1, 1, 1, headers.length)
    .setValues([headers])
    .setBackground('#00A100').setFontColor('#FFFFFF')
    .setFontWeight('bold').setHorizontalAlignment('center');

  // ── ARRAYFORMULA — Score Global (J2) ──
  // = SEO×B5 + Conversion×B6 + Autorité×B7 + LLM×B8
  sheet.getRange('J2').setFormula(
    '=ARRAYFORMULA(IFERROR(' +
    'IF(F2:F="","",ROUND(' +
    '(F2:F*Paramètres!$B$5)+' +
    '(G2:G*Paramètres!$B$6)+' +
    '(H2:H*Paramètres!$B$7)+' +
    '(I2:I*Paramètres!$B$8)' +
    ',0)),""))'
  );

  // ── ARRAYFORMULA — Action (K2) ──
  sheet.getRange('K2').setFormula(
    '=ARRAYFORMULA(IFERROR(' +
    'IF(J2:J="","",IF(J2:J>=Paramètres!$B$12,"✅ Actif Premium",' +
    'IF(J2:J>=Paramètres!$B$13,"🟢 Optimisation mineure",' +
    'IF(J2:J>=Paramètres!$B$14,"🟡 Optimisation stratégique",' +
    '"🔴 Révision complète")))),""))'
  );

  // ── Mise en forme conditionnelle — Score Global (col J) ──
  const jRange = sheet.getRange('J2:J2000');
  sheet.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberGreaterThanOrEqualTo(95)
      .setBackground('#00D400').setFontColor('#FFFFFF').setFontWeight('bold')
      .setRanges([jRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberBetween(85, 94)
      .setBackground('#A5D6A7').setFontColor('#1B5E20')
      .setRanges([jRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberBetween(70, 84)
      .setBackground('#FFF9C4').setFontColor('#F57F17')
      .setRanges([jRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(70)
      .setBackground('#FFCDD2').setFontColor('#B71C1C')
      .setRanges([jRange]).build(),
  ]);

  sheet.setFrozenRows(1);
  sheet.setFrozenColumns(1);

  // Largeurs colonnes
  [[1,220],[2,280],[3,100],[4,180],[5,120],
   [6,100],[7,110],[8,110],[9,90],[10,100],[11,230],
   [12,100],[13,80],[14,120],[15,80],
   [16,70],[17,90],[18,100],[19,110],[20,110],
   [21,200],[22,120],[23,110],[24,200],[25,110]
  ].forEach(([c,w]) => sheet.setColumnWidth(c, w));

  // ── Ligne exemple (row 2) ──
  const exRow = [
    'Exemple : FluentCRM vs ActiveCampaign', // A
    'https://schoolswp.com/fluentcrm-vs-activecampaign/', // B
    'Satellite',            // C
    'fluentcrm vs activecampaign', // D
    'comparative',          // E
    88,                     // F Score SEO
    82,                     // G Score Conversion
    90,                     // H Score Autorité
    75,                     // I Score LLM
    '', '',                 // J K (ARRAYFORMULA)
    8.3, 3.8, 4200, 160,   // L M N O (GSC)
    3, 0,                   // P Leads, Q Revenus
    2, 4, 2,                // R S T Satellites/Maillage
    'CRM / Email Marketing', // U Cluster
    'CRM',                  // V Pilier
    'Publié',               // W Statut
    'https://docs.google.com/document/d/exemple/', // X
    new Date().toISOString().split('T')[0], // Y
  ];
  sheet.getRange(2, 1, 1, headers.length)
    .setValues([exRow])
    .setFontStyle('italic').setBackground('#F9FBE7').setFontColor('#9E9D24');

  sheet.getRange('A2').setNote(
    '⚡ Ligne d\'exemple — remplace par tes vrais articles.\n\n' +
    '• Colonnes J et K : calculées automatiquement (ne pas modifier)\n' +
    '• Colonnes L-O : remplies par le workflow n8n kpi-dashboard-updater\n' +
    '• Colonne I (Score LLM) : saisis 100 si présent dans AI Overview/Citation LLM, 0 sinon'
  );
}


// ╔══════════════════════════════════════════════════════════════╗
// ║                     ONGLET CLUSTERS                         ║
// ╚══════════════════════════════════════════════════════════════╝

function _setupClusters(ss) {
  const sheet = _getOrCreate(ss, 'Clusters');
  sheet.clearContents();
  sheet.clearFormats();
  sheet.setTabColor('#00A100');

  const headers = [
    'Cluster',            // A
    'Pilier',             // B
    'Nb Articles',        // C   COUNTIF(Articles!U)
    'Score SEO moy.',     // D   AVERAGEIF
    'Score Conv. moy.',   // E   AVERAGEIF
    'Score Auth. moy.',   // F   AVERAGEIF
    'Score Global moy.',  // G   AVERAGEIF
    'Clics 28j',          // H   SUMIF(Articles!O)
    'Revenus €',          // I   SUMIF(Articles!Q)
    'Priorité',           // J   calculée
    '% Actifs (≥ 85)',    // K   COUNTIFS / C
  ];

  sheet.getRange(1, 1, 1, headers.length)
    .setValues([headers])
    .setBackground('#00A100').setFontColor('#FFFFFF')
    .setFontWeight('bold').setHorizontalAlignment('center');

  // 6 clusters schoolsWP par défaut
  const clusters = [
    ['SEO WordPress',           'SEO'],
    ['LMS / Formation',         'LMS'],
    ['CRM / Email Marketing',   'CRM'],
    ['Performance WordPress',   'Performance'],
    ['Automatisation',          'Automatisation'],
    ['E-commerce WordPress',    'Ecommerce'],
  ];

  clusters.forEach(([cluster, pilier], i) => {
    const r = i + 2;
    sheet.getRange(r, 1).setValue(cluster);
    sheet.getRange(r, 2).setValue(pilier);
    // C — Nb articles
    sheet.getRange(r, 3).setFormula(`=COUNTIF(Articles!$U:$U,A${r})`);
    // D — Score SEO moyen
    sheet.getRange(r, 4).setFormula(`=IFERROR(ROUND(AVERAGEIF(Articles!$U:$U,A${r},Articles!$F:$F),1),"")`);
    // E — Score Conversion moyen
    sheet.getRange(r, 5).setFormula(`=IFERROR(ROUND(AVERAGEIF(Articles!$U:$U,A${r},Articles!$G:$G),1),"")`);
    // F — Score Autorité moyen
    sheet.getRange(r, 6).setFormula(`=IFERROR(ROUND(AVERAGEIF(Articles!$U:$U,A${r},Articles!$H:$H),1),"")`);
    // G — Score Global moyen
    sheet.getRange(r, 7).setFormula(`=IFERROR(ROUND(AVERAGEIF(Articles!$U:$U,A${r},Articles!$J:$J),1),"")`);
    // H — Clics 28j
    sheet.getRange(r, 8).setFormula(`=IFERROR(SUMIF(Articles!$U:$U,A${r},Articles!$O:$O),0)`);
    // I — Revenus
    sheet.getRange(r, 9).setFormula(`=IFERROR(SUMIF(Articles!$U:$U,A${r},Articles!$Q:$Q),0)`);
    // J — Priorité
    sheet.getRange(r, 10).setFormula(
      `=IF(A${r}="","",IF(H${r}<Paramètres!$B$17,` +
      `"🔴 Renforcer SEO",IF(I${r}<Paramètres!$B$18,` +
      `"🟡 Optimiser Conversion","🟢 Scaler")))`
    );
    // K — % Actifs performants
    sheet.getRange(r, 11).setFormula(
      `=IFERROR(TEXT(` +
      `COUNTIFS(Articles!$U:$U,A${r},Articles!$J:$J,">="&Paramètres!$B$13)` +
      `/MAX(C${r},1),"0%"),"-")`
    );
  });

  // Mise en forme conditionnelle — Score Global moyen (col G)
  const gRange = sheet.getRange('G2:G100');
  sheet.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberGreaterThanOrEqualTo(85)
      .setBackground('#A5D6A7').setFontColor('#1B5E20')
      .setRanges([gRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberBetween(70, 84)
      .setBackground('#FFF9C4').setFontColor('#F57F17')
      .setRanges([gRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(70)
      .setBackground('#FFCDD2').setFontColor('#B71C1C')
      .setRanges([gRange]).build(),
  ]);

  sheet.setFrozenRows(1);
  [[1,210],[2,130],[3,90],[4,110],[5,110],[6,110],[7,110],[8,90],[9,90],[10,220],[11,110]]
    .forEach(([c,w]) => sheet.setColumnWidth(c, w));
}


// ╔══════════════════════════════════════════════════════════════╗
// ║                     ONGLET SYNTHÈSE                         ║
// ╚══════════════════════════════════════════════════════════════╝

function _setupSynthese(ss) {
  const sheet = _getOrCreate(ss, 'Synthèse');
  sheet.clearContents();
  sheet.clearFormats();
  sheet.setTabColor('#E668D4');

  // Titre principal
  sheet.getRange('A1:C1').merge()
    .setValue('📊 schoolsWP — Synthèse KPI Content Engine')
    .setFontSize(16).setFontWeight('bold').setFontColor('#00A100')
    .setBackground('#F1F8E9').setHorizontalAlignment('left');

  let row = 3;

  // ── Helper interne : écrit une section ──
  const section = (title, kpis) => {
    // En-tête section
    sheet.getRange(row, 1, 1, 3).merge()
      .setValue(title)
      .setBackground('#00A100').setFontColor('#FFFFFF')
      .setFontWeight('bold').setFontSize(11)
      .setHorizontalAlignment('left');
    row++;
    // Sous-headers
    sheet.getRange(row, 1, 1, 3)
      .setValues([['Indicateur', 'Valeur', 'Objectif']])
      .setBackground('#E8F5E9').setFontWeight('bold')
      .setHorizontalAlignment('center');
    row++;
    // Données
    kpis.forEach(([label, formula, target]) => {
      sheet.getRange(row, 1).setValue(label);
      if (typeof formula === 'string' && formula.startsWith('=')) {
        sheet.getRange(row, 2).setFormula(formula);
      } else {
        sheet.getRange(row, 2).setValue(formula || '');
      }
      sheet.getRange(row, 3).setValue(target || '');
      // Alternance légère
      if (row % 2 === 0) sheet.getRange(row, 1, 1, 3).setBackground('#FAFAFA');
      row++;
    });
    row++; // ligne vide entre sections
  };

  // ── Section 1 — KPI Globaux ──
  section('📊 KPI GLOBAUX — Production', [
    ['Nb articles publiés',
      '=COUNTA(Articles!A2:A)',
      '≥ 50'],
    ['Score Content Engine Global',
      '=IFERROR(ROUND(' +
      '(AVERAGE(Articles!F2:F)*Paramètres!B5)+' +
      '(AVERAGE(Articles!G2:G)*Paramètres!B6)+' +
      '(AVERAGE(Articles!H2:H)*Paramètres!B7)+' +
      '(AVERAGE(Articles!I2:I)*Paramètres!B8)' +
      ',0),0)',
      '≥ 85'],
    ['Score Global moyen',
      '=IFERROR(ROUND(AVERAGE(Articles!J2:J),1),0)',
      '≥ 85'],
    ['Score SEO moyen',
      '=IFERROR(ROUND(AVERAGE(Articles!F2:F),1),0)',
      '≥ 88'],
    ['Score Conversion moyen',
      '=IFERROR(ROUND(AVERAGE(Articles!G2:G),1),0)',
      '≥ 85'],
    ['Score Autorité moyen',
      '=IFERROR(ROUND(AVERAGE(Articles!H2:H),1),0)',
      '≥ 85'],
    ['Score LLM moyen',
      '=IFERROR(ROUND(AVERAGE(Articles!I2:I),1),0)',
      '≥ 70'],
  ]);

  // ── Section 2 — Trafic & Revenus ──
  section('📈 TRAFIC & REVENUS (données GSC 28 jours)', [
    ['Clics organiques totaux',
      '=IFERROR(SUM(Articles!O2:O),0)',
      ''],
    ['Impressions totales',
      '=IFERROR(SUM(Articles!N2:N),0)',
      ''],
    ['CTR moyen',
      '=IFERROR(ROUND(AVERAGE(Articles!M2:M),1)&" %","—")',
      '> 4 %'],
    ['Position moyenne GSC',
      '=IFERROR(ROUND(AVERAGE(Articles!L2:L),1),"—")',
      'Top 15'],
    ['Leads totaux',
      '=IFERROR(SUM(Articles!P2:P),0)',
      ''],
    ['Revenus affiliés €',
      '=IFERROR(SUM(Articles!Q2:Q),0)',
      ''],
  ]);

  // ── Section 3 — Répartition scores ──
  section('🎯 RÉPARTITION DES SCORES', [
    ['✅ Actif Premium  (≥ 95)',
      '=COUNTIF(Articles!J2:J,">="&Paramètres!B12)',
      ''],
    ['🟢 Actif Performant  (85–94)',
      '=COUNTIFS(Articles!J2:J,">="&Paramètres!B13,Articles!J2:J,"<"&Paramètres!B12)',
      ''],
    ['🟡 À optimiser  (70–84)',
      '=COUNTIFS(Articles!J2:J,">="&Paramètres!B14,Articles!J2:J,"<"&Paramètres!B13)',
      ''],
    ['🔴 À réviser  (< 70)',
      '=COUNTIF(Articles!J2:J,"<"&Paramètres!B14)',
      ''],
  ]);

  // ── Section 4 — Clusters ──
  section('📦 CLUSTERS — Vue rapide', [
    ['Meilleur cluster (Score Global)',
      '=IFERROR(INDEX(Clusters!A2:A,MATCH(MAX(Clusters!G2:G),Clusters!G2:G,0)),"—")',
      ''],
    ['Cluster à renforcer (trafic le + faible)',
      '=IFERROR(INDEX(Clusters!A2:A,MATCH(MIN(IF(Clusters!H2:H>0,Clusters!H2:H,MAX(Clusters!H2:H)+1)),Clusters!H2:H,0)),"—")',
      ''],
    ['Total clics organiques',
      '=IFERROR(SUM(Clusters!H2:H),0)',
      ''],
    ['Total revenus affiliés €',
      '=IFERROR(SUM(Clusters!I2:I),0)',
      ''],
  ]);

  // Mise en forme conditionnelle — Score Content Engine Global (B5 = row 3+2+1 = 6 dans la section)
  // Ligne exacte de "Score Content Engine Global" = 3 (départ) + 1 (header section) + 1 (sous-headers) + 1 (première donnée) = 6
  // Pour être robuste, on applique sur toute la colonne B avec des seuils numériques
  const bRange = sheet.getRange('B4:B50');
  sheet.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberGreaterThanOrEqualTo(85)
      .setBackground('#A5D6A7').setFontColor('#1B5E20').setFontWeight('bold')
      .setRanges([bRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberBetween(70, 84)
      .setBackground('#FFF9C4').setFontColor('#F57F17').setFontWeight('bold')
      .setRanges([bRange]).build(),
    SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(70)
      .setBackground('#FFCDD2').setFontColor('#B71C1C').setFontWeight('bold')
      .setRanges([bRange]).build(),
  ]);

  sheet.setColumnWidth(1, 320);
  sheet.setColumnWidth(2, 140);
  sheet.setColumnWidth(3, 120);
  sheet.setFrozenRows(2);
}


// ╔══════════════════════════════════════════════════════════════╗
// ║               UTILITAIRE — RÉPARER LES FORMULES             ║
// ╚══════════════════════════════════════════════════════════════╝

/**
 * Répare les ARRAYFORMULA Score Global (col J) et Action (col K)
 * si elles ont été écrasées par une saisie manuelle.
 * Exécuter depuis Outils > Macros > refreshFormulas
 */
function refreshFormulas() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ui = SpreadsheetApp.getUi();
  const sheet = ss.getSheetByName('Articles');

  if (!sheet) {
    ui.alert('❌ Onglet "Articles" introuvable. Lance setupDashboard() d\'abord.');
    return;
  }

  sheet.getRange('J2').setFormula(
    '=ARRAYFORMULA(IFERROR(' +
    'IF(F2:F="","",ROUND(' +
    '(F2:F*Paramètres!$B$5)+' +
    '(G2:G*Paramètres!$B$6)+' +
    '(H2:H*Paramètres!$B$7)+' +
    '(I2:I*Paramètres!$B$8)' +
    ',0)),""))'
  );

  sheet.getRange('K2').setFormula(
    '=ARRAYFORMULA(IFERROR(' +
    'IF(J2:J="","",IF(J2:J>=Paramètres!$B$12,"✅ Actif Premium",' +
    'IF(J2:J>=Paramètres!$B$13,"🟢 Optimisation mineure",' +
    'IF(J2:J>=Paramètres!$B$14,"🟡 Optimisation stratégique",' +
    '"🔴 Révision complète")))),""))'
  );

  ui.alert('✅ Formules Score Global et Action réparées dans l\'onglet Articles.');
}


// ╔══════════════════════════════════════════════════════════════╗
// ║                        HELPERS                              ║
// ╚══════════════════════════════════════════════════════════════╝

function _getOrCreate(ss, name) {
  return ss.getSheetByName(name) || ss.insertSheet(name);
}

function _reorderSheets(ss) {
  const order = ['Articles', 'Clusters', 'Synthèse', 'Paramètres'];
  order.forEach((name, i) => {
    const sheet = ss.getSheetByName(name);
    if (sheet) {
      ss.setActiveSheet(sheet);
      try { ss.moveActiveSheet(i + 1); } catch(e) {}
    }
  });
  ss.setActiveSheet(ss.getSheetByName('Articles') || ss.getSheets()[0]);
}
