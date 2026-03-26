/**
 * schoolsWP Drive Organizer v3.0 – Mapping, Migration & Index
 *
 * Ordre d'execution strict :
 * 1. runAudit()           -> inventaire + anomalies
 * 2. generateMapping()    -> Sheet dry-run
 * 3. [VALIDATION HUMAINE] -> verifier le Sheet, OUI/NON
 * 4. executeMigration()   -> execution safe (lignes OUI uniquement)
 * 5. generateGlobalIndex()-> Sheet filtrable + miroir Markdown
 */

// ══════════════════════════════════════════════════════════════
// MAPPING (DRY-RUN)
// ══════════════════════════════════════════════════════════════

function generateMapping() {
  Logger.log("=== MAPPING (DRY-RUN) ===");

  const auditData = loadAuditData_();
  if (!auditData) {
    Logger.log("ERREUR : Executer runAudit() d'abord !");
    return;
  }

  const { files, anomalies } = auditData;
  Logger.log("Fichiers a mapper : " + files.length);

  // Creer ou ouvrir le Sheet
  const ss = openOrCreateSpreadsheet_(MAPPING_SHEET_NAME);

  // -- Onglet MAPPING --
  const mappingSheet = clearOrCreateSheet_(ss, "Mapping");
  const headers = [
    "ID Fichier", "Ancien nom", "Ancien chemin",
    "Nouveau nom propose", "Nouveau chemin propose",
    "Confiance %", "Action", "Severite",
    "Anomalies detectees", "Email/CRM classif.",
    "Valide ? (OUI/NON)", "Notes"
  ];
  writeSheetHeader_(mappingSheet, headers, "#1a73e8");

  const rows = files.map(file => {
    const proposal = proposeNewNameAndPath_(file);
    const emailInfo = file.analysis && file.analysis.emailClassification
      ? file.analysis.emailClassification.reason || ""
      : "";
    return [
      file.id, file.name, file.path,
      proposal.newName, proposal.newPath,
      proposal.confidence, proposal.action,
      (file.analysis && file.analysis.severity) || "N/A",
      (file.analysis && file.analysis.issues) ? file.analysis.issues.join("; ") : "",
      emailInfo,
      proposal.confidence >= 80 ? "OUI" : "",
      proposal.notes || ""
    ];
  });

  if (rows.length > 0) {
    mappingSheet.getRange(2, 1, rows.length, headers.length).setValues(rows);

    // Mise en forme conditionnelle
    const confRule = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(80).setBackground("#ffcccc")
      .setRanges([mappingSheet.getRange(2, 6, rows.length, 1)]).build();
    const sevRule = SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("CRITIQUE").setBackground("#ff9900").setFontColor("#ffffff")
      .setRanges([mappingSheet.getRange(2, 8, rows.length, 1)]).build();
    mappingSheet.setConditionalFormatRules([confRule, sevRule]);
  }

  mappingSheet.setFrozenRows(1);
  autoResizeAllColumns_(mappingSheet, headers.length);

  // -- Onglet DOUBLONS --
  const dupSheet = clearOrCreateSheet_(ss, "Doublons");
  const dupHeaders = ["Sujet normalise", "Nb fichiers", "Fichiers", "Vrais doublons ?", "Variantes"];
  writeSheetHeader_(dupSheet, dupHeaders);

  if (anomalies && anomalies.duplicates && anomalies.duplicates.length > 0) {
    const dupRows = anomalies.duplicates.map(d => [
      d.subject, d.count,
      d.files.map(f => f.name || f).join("\n"),
      d.trueDuplicates ? d.trueDuplicates.map(td => td.files.join(" | ")).join("\n") : "Non",
      d.variants ? Object.keys(d.variants).join(", ") : ""
    ]);
    dupSheet.getRange(2, 1, dupRows.length, dupHeaders.length).setValues(dupRows);
  }

  // -- Onglet EMAIL/CRM --
  const emailSheet = clearOrCreateSheet_(ss, "Email-CRM");
  const emailHeaders = ["Fichier", "Chemin actuel", "Classification", "Dossier correct", "Mal range ?", "Action"];
  writeSheetHeader_(emailSheet, emailHeaders, "#34a853");

  const emailRows = files
    .filter(f => f.analysis && f.analysis.emailClassification && f.analysis.emailClassification.isEmail)
    .map(f => {
      const ec = f.analysis.emailClassification;
      return [f.name, f.path, ec.reason, ec.correctFolder,
        ec.misplaced ? "OUI - A DEPLACER" : "OK",
        ec.misplaced ? "MOVE" : "OK"
      ];
    });
  if (emailRows.length > 0) {
    emailSheet.getRange(2, 1, emailRows.length, emailHeaders.length).setValues(emailRows);
  }

  // -- Onglet RESUME --
  const summarySheet = clearOrCreateSheet_(ss, "Resume");
  const summaryData = [
    ["Metrique", "Valeur"],
    ["Total fichiers", files.length],
    ["Format correct", rows.filter(r => r[6] === "OK").length],
    ["A renommer", rows.filter(r => r[6] === "RENAME" || r[6] === "RENAME+MOVE").length],
    ["A deplacer", rows.filter(r => r[6] === "MOVE" || r[6] === "RENAME+MOVE").length],
    ["", ""],
    ["Sans date", anomalies ? anomalies.noDate.length : 0],
    ["Mauvais separateurs", anomalies ? anomalies.badSeparator.length : 0],
    ["Sans type", anomalies ? anomalies.noType.length : 0],
    ["Sans usage", anomalies ? anomalies.noUsage.length : 0],
    ["Extension non standard", anomalies ? anomalies.badExtension.length : 0],
    ["", ""],
    ["Email/CRM mal ranges", anomalies ? anomalies.misplacedEmail.length : 0],
    ["Groupes doublons", anomalies ? anomalies.duplicates.length : 0],
    ["", ""],
    ["Confiance >= 80%", rows.filter(r => r[5] >= 80).length],
    ["A valider manuellement", rows.filter(r => r[5] < 80).length],
    ["", ""],
    ["Date audit", new Date().toISOString()],
    ["Sheet URL", ss.getUrl()]
  ];
  summarySheet.getRange(1, 1, summaryData.length, 2).setValues(summaryData);
  writeSheetHeader_(summarySheet, summaryData[0], "#1a73e8");

  removeDefaultSheet_(ss);

  Logger.log("=== MAPPING GENERE ===");
  Logger.log("URL       : " + ss.getUrl());
  Logger.log("Total     : " + rows.length);
  Logger.log("Auto OUI  : " + rows.filter(r => r[10] === "OUI").length);
  Logger.log("A valider : " + rows.filter(r => r[10] === "").length);
  Logger.log(">>> PROCHAINE ETAPE : verifier le Sheet, puis executeMigration()");

  return ss.getUrl();
}

// ══════════════════════════════════════════════════════════════
// PROPOSITION NOM / CHEMIN
// ══════════════════════════════════════════════════════════════

function proposeNewNameAndPath_(file) {
  const result = { newName: file.name, newPath: "", confidence: 100, action: "OK", notes: "" };
  const analysis = file.analysis || analyzeFileName_(file.name, file.path);
  let confidence = 100;

  const extMatch = file.name.match(/\.([^.]+)$/);
  const ext = extMatch ? extMatch[1] : "";
  const isGoogleNative = file.mimeType && file.mimeType.startsWith("application/vnd.google-apps.");

  // Date
  let dateStr = analysis.detectedDate;
  if (!dateStr) {
    dateStr = file.created ? file.created.substring(0, 10) : Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");
    confidence -= 15;
    result.notes += "Date estimee depuis creation. ";
  }

  // Sujet
  let subject = extractSubject_(file.name);
  if (!subject || subject.length < 3) {
    subject = file.name.replace(/\.[^.]+$/, "").replace(/^\d{4}-\d{2}-\d{2}[\s\u2013\-_]*/, "")
      .replace(/__/g, " ").replace(/_/g, " ").replace(/ - /g, " ").trim();
    confidence -= 10;
  }
  subject = capitalizeFirst_(subject);

  // Type
  let type = analysis.detectedType;
  if (!type) {
    type = guessType_(file);
    confidence -= 15;
    result.notes += "Type devine : " + type + ". ";
  }

  // Usage
  let usage = analysis.detectedUsage;
  if (!usage) {
    usage = guessUsage_(file);
    confidence -= 15;
    result.notes += "Usage devine : " + usage + ". ";
  }

  // Infos (variantes)
  const infos = (analysis.variantMarkers && analysis.variantMarkers.length > 0)
    ? analysis.variantMarkers.join("-")
    : "";

  // Nouveau nom
  let newName;
  if (analysis.hasCorrectFormat) {
    newName = file.name;
  } else {
    newName = dateStr + SEP + subject + SEP + type + SEP + usage;
    if (infos) newName += SEP + infos;
    if (!isGoogleNative && ext) newName += "." + ext;
    confidence -= 5;
  }

  // Dossier cible
  let targetPath;
  if (analysis.emailClassification && analysis.emailClassification.isEmail) {
    targetPath = "PROMPTS_schoolsWP/" + analysis.emailClassification.correctFolder;
  } else {
    targetPath = determineTargetFolder_(type, usage);
  }

  if (!targetPath) {
    confidence -= 20;
    targetPath = "A_DETERMINER";
    result.notes += "Dossier cible incertain. ";
  }

  // Action
  const nameChanged = newName !== file.name;
  const pathCorrect = file.path && targetPath !== "A_DETERMINER" &&
    file.path.toLowerCase().includes(targetPath.replace("PROMPTS_schoolsWP/", "").toLowerCase());

  if (!nameChanged && pathCorrect) {
    result.action = "OK";
    confidence = 100;
  } else if (nameChanged && pathCorrect) {
    result.action = "RENAME";
  } else if (!nameChanged && !pathCorrect) {
    result.action = "MOVE";
  } else {
    result.action = "RENAME+MOVE";
  }

  result.newName = newName;
  result.newPath = targetPath;
  result.confidence = Math.max(0, Math.min(100, confidence));
  if (result.confidence < 80) result.action = "A_VALIDER";

  return result;
}

function determineTargetFolder_(type, usage) {
  const root = "PROMPTS_schoolsWP";

  const typeRoutes = {
    "Template": {
      "Article": "/02_TEMPLATES/01_Editorial_SEO",
      "SEO": "/02_TEMPLATES/01_Editorial_SEO",
      "Email": "/02_TEMPLATES/02_Email_CRM_FluentCRM",
      "Landing": "/02_TEMPLATES/03_Conversion_Landing",
      "Ads": "/02_TEMPLATES/03_Conversion_Landing",
      "YouTube": "/02_TEMPLATES/04_YouTube_Social",
      "Social": "/02_TEMPLATES/04_YouTube_Social",
      "Affiliation": "/02_TEMPLATES/05_Affiliation_Monetisation",
      "Automation": "/02_TEMPLATES/06_Automation_SOP",
      "Asset": "/04_ASSETS/04_Illustrations",
      "ADMIN": "/01_ADMIN/01_Regles-et-Index",
      "_default": "/02_TEMPLATES/01_Editorial_SEO"
    },
    "Prompt": {
      "Article": "/03_PROMPTS/01_Editorial_SEO",
      "SEO": "/03_PROMPTS/01_Editorial_SEO",
      "YouTube": "/03_PROMPTS/01_Editorial_SEO",
      "Social": "/03_PROMPTS/01_Editorial_SEO",
      "Email": "/03_PROMPTS/02_Email_CRM",
      "Landing": "/03_PROMPTS/03_Conversion",
      "Ads": "/03_PROMPTS/03_Conversion",
      "Affiliation": "/03_PROMPTS/04_Affiliation",
      "Asset": "/03_PROMPTS/05_Assets",
      "Automation": "/03_PROMPTS/06_Automation",
      "ADMIN": "/01_ADMIN/01_Regles-et-Index",
      "_default": "/03_PROMPTS/01_Editorial_SEO"
    },
    "SOP": { "_default": "/07_AUTOMATION/02_SOP" },
    "Brief": {
      "Asset": "/04_ASSETS/04_Illustrations",
      "_default": "/06_SCHOOLS_WP_EDITORIAL/01_Briefs"
    },
    "Checklist": { "_default": "/01_ADMIN/02_Checklists-Qualite" },
    "Audit": { "_default": "/01_ADMIN/02_Checklists-Qualite" }
  };

  const routes = typeRoutes[type];
  if (!routes) return null;
  const suffix = routes[usage] || routes["_default"];
  return suffix ? root + suffix : null;
}

// ══════════════════════════════════════════════════════════════
// MIGRATION (EXECUTION SAFE)
// ══════════════════════════════════════════════════════════════

/**
 * Execute la migration. Backup complet AVANT modification.
 * Seules les lignes avec "OUI" sont traitees. Zero suppression.
 */
function executeMigration() {
  Logger.log("=== MIGRATION SAFE v3.0 ===");
  const startTime = new Date();
  const today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");

  // Sheet de mapping
  const sheetFile = findFileByName_(MAPPING_SHEET_NAME);
  if (!sheetFile) {
    Logger.log("ERREUR : Sheet de mapping non trouve ! Executer generateMapping() d'abord.");
    return;
  }
  const ss = SpreadsheetApp.open(sheetFile);
  const mappingSheet = ss.getSheetByName("Mapping");
  if (!mappingSheet) {
    Logger.log("ERREUR : Onglet 'Mapping' non trouve !");
    return;
  }
  const data = mappingSheet.getDataRange().getValues();

  // Dossier racine cible
  const targetRoot = resolveTargetRoot_();
  if (!targetRoot) {
    Logger.log("ERREUR : PROMPTS_schoolsWP non trouve ! Executer createFullStructure() d'abord.");
    return;
  }

  // Backup
  const backupFolder = getOrCreateFolder(targetRoot, "_BACKUP_" + today);
  Logger.log("Backup : " + backupFolder.getUrl());

  let renamed = 0, moved = 0, archived = 0, skipped = 0, errors = 0, backed = 0;

  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    const fileId = row[0];
    const oldName = row[1];
    const newName = row[3];
    const newPath = row[4];
    const action = row[6];
    const validated = String(row[10]).toUpperCase();

    if (validated !== "OUI") { skipped++; continue; }
    if (action === "OK") continue;

    try {
      const file = DriveApp.getFileById(fileId);
      file.makeCopy(file.getName(), backupFolder);
      backed++;

      if ((action === "RENAME" || action === "RENAME+MOVE") && newName && newName !== oldName) {
        file.setName(newName);
        renamed++;
        Logger.log("[RENAME] " + oldName + " -> " + newName);
      }

      if ((action === "MOVE" || action === "RENAME+MOVE") && newPath && newPath !== "A_DETERMINER") {
        const targetFolder = navigateToFolder_(targetRoot, newPath);
        moveFileToFolder_(file, targetFolder);
        moved++;
        Logger.log("[MOVE] " + oldName + " -> " + newPath);
      }

      if (action === "ARCHIVE") {
        const archiveFolder = navigateToFolder_(targetRoot, "99_ARCHIVES");
        moveFileToFolder_(file, archiveFolder);
        archived++;
        Logger.log("[ARCHIVE] " + oldName);
      }
    } catch (e) {
      Logger.log("[ERREUR] " + oldName + " : " + e.message);
      errors++;
    }
  }

  // Rapport
  const duration = (new Date() - startTime) / 1000;
  Logger.log("---");
  Logger.log("Sauvegardes : " + backed);
  Logger.log("Renommes    : " + renamed);
  Logger.log("Deplaces    : " + moved);
  Logger.log("Archives    : " + archived);
  Logger.log("Ignores     : " + skipped);
  Logger.log("Erreurs     : " + errors);
  Logger.log("Duree       : " + duration + "s");
  Logger.log("Backup      : " + backupFolder.getUrl());

  // Onglet Resultats
  const resultsSheet = ss.getSheetByName("Resultats") || ss.insertSheet("Resultats");
  resultsSheet.clear();
  resultsSheet.getRange(1, 1, 10, 2).setValues([
    ["Metrique", "Valeur"],
    ["Date execution", today],
    ["Fichiers sauvegardes", backed],
    ["Fichiers renommes", renamed],
    ["Fichiers deplaces", moved],
    ["Fichiers archives", archived],
    ["Fichiers ignores", skipped],
    ["Erreurs", errors],
    ["Duree", duration + "s"],
    ["Backup URL", backupFolder.getUrl()]
  ]);
  resultsSheet.getRange(1, 1, 1, 2).setFontWeight("bold");

  Logger.log(">>> PROCHAINE ETAPE : generateGlobalIndex()");
}

/** Deplace un fichier vers un dossier (retire des anciens parents) */
function moveFileToFolder_(file, targetFolder) {
  targetFolder.addFile(file);
  const parents = file.getParents();
  while (parents.hasNext()) {
    const parent = parents.next();
    if (parent.getId() !== targetFolder.getId()) {
      parent.removeFile(file);
    }
  }
}

// ══════════════════════════════════════════════════════════════
// INDEX GLOBAL
// ══════════════════════════════════════════════════════════════

/** Genere un index en Sheet filtrable + miroir Markdown */
function generateGlobalIndex() {
  Logger.log("=== INDEX GLOBAL (Sheet + Markdown) ===");

  const targetRoot = resolveTargetRoot_();
  if (!targetRoot) {
    Logger.log("ERREUR : PROMPTS_schoolsWP non trouve !");
    return;
  }

  const allFiles = [];
  collectFilesRecursive_(targetRoot, "", allFiles);

  const indexFiles = allFiles
    .filter(f => !f.name.startsWith("_") && !f.path.includes("_BACKUP"))
    .sort((a, b) => (a.path + "/" + a.name).localeCompare(b.path + "/" + b.name));

  const today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");

  // -- Sheet filtrable --
  const ss = openOrCreateSpreadsheet_(INDEX_SHEET_NAME);
  const indexSheet = clearOrCreateSheet_(ss, "Index");

  const sheetHeaders = ["#", "Nom du fichier", "Chemin", "Categorie", "Statut", "Type", "Usage", "Derniere MAJ", "Lien", "Notes"];
  writeSheetHeader_(indexSheet, sheetHeaders, "#1a73e8");
  indexSheet.setFrozenRows(1);

  const sheetRows = indexFiles.map((file, i) => {
    const analysis = analyzeFileName_(file.name, file.path);
    return [
      i + 1,
      file.name,
      file.path.replace(/^PROMPTS_schoolsWP\/?/, ""),
      detectCategory_(file.path),
      detectStatus_(file.path),
      analysis.detectedType || guessType_(file),
      analysis.detectedUsage || guessUsage_(file),
      file.modified ? file.modified.substring(0, 10) : today,
      file.url,
      ""
    ];
  });

  if (sheetRows.length > 0) {
    indexSheet.getRange(2, 1, sheetRows.length, sheetHeaders.length).setValues(sheetRows);
    const filterRange = indexSheet.getRange(1, 1, sheetRows.length + 1, sheetHeaders.length);
    if (indexSheet.getFilter()) indexSheet.getFilter().remove();
    filterRange.createFilter();
  }
  autoResizeAllColumns_(indexSheet, sheetHeaders.length);

  // Onglet Stats
  const statsSheet = clearOrCreateSheet_(ss, "Stats");
  const catCounts = {};
  sheetRows.forEach(r => { catCounts[r[3]] = (catCounts[r[3]] || 0) + 1; });

  const statsData = [["Metrique", "Valeur"], ["Total fichiers indexes", indexFiles.length], ["Date generation", today], ["", ""]];
  statsData.push(["Par categorie", ""]);
  for (const [cat, count] of Object.entries(catCounts)) {
    statsData.push([cat, count]);
  }
  statsSheet.getRange(1, 1, statsData.length, 2).setValues(statsData);
  writeSheetHeader_(statsSheet, statsData[0], "#1a73e8");

  removeDefaultSheet_(ss);

  // -- Miroir Markdown --
  const mdLines = [
    "# Index Global \u2013 PROMPTS_schoolsWP",
    "",
    "**Derniere MAJ** : " + today,
    "**Total** : " + indexFiles.length + " fichiers",
    "**Sheet** : " + ss.getUrl(),
    "", "---", ""
  ];

  let currentCategory = "";
  for (const row of sheetRows) {
    if (row[3] !== currentCategory) {
      mdLines.push("", "## " + row[3], "",
        "| # | Nom | Statut | Type | Usage | MAJ |",
        "|---|-----|--------|------|-------|-----|");
      currentCategory = row[3];
    }
    mdLines.push("| " + row[0] + " | " + row[1] + " | " + row[4] + " | " + row[5] + " | " + row[6] + " | " + row[7] + " |");
  }

  mdLines.push("", "---", "*Index genere le " + today + " par schoolsWP Drive Organizer v3.0*");

  const adminFolder = getOrCreateFolder(targetRoot, "01_ADMIN");
  const indexFolder = getOrCreateFolder(adminFolder, "01_Regles-et-Index");
  const mdFileName = today + " \u2013 Index \u2013 ADMIN \u2013 Global.md";

  const existingMd = indexFolder.getFilesByName(mdFileName);
  if (existingMd.hasNext()) existingMd.next().setTrashed(true);

  indexFolder.createFile(mdFileName, mdLines.join("\n"), MimeType.PLAIN_TEXT);

  Logger.log("Sheet : " + ss.getUrl());
  Logger.log("MD    : " + mdFileName);
  Logger.log("Total : " + indexFiles.length + " fichiers");
}

// ══════════════════════════════════════════════════════════════
// HELPERS SHEET (evite la duplication entre mapping et index)
// ══════════════════════════════════════════════════════════════

function openOrCreateSpreadsheet_(name) {
  const existing = DriveApp.getFilesByName(name);
  if (existing.hasNext()) return SpreadsheetApp.open(existing.next());
  return SpreadsheetApp.create(name);
}

function clearOrCreateSheet_(ss, name) {
  let sheet = ss.getSheetByName(name);
  if (sheet) { sheet.clear(); return sheet; }
  return ss.insertSheet(name);
}

function writeSheetHeader_(sheet, headers, bgColor) {
  const range = sheet.getRange(1, 1, 1, headers.length);
  range.setValues([headers]);
  range.setFontWeight("bold");
  if (bgColor) {
    range.setBackground(bgColor);
    range.setFontColor("#ffffff");
  }
}

function autoResizeAllColumns_(sheet, count) {
  for (let i = 1; i <= count; i++) sheet.autoResizeColumn(i);
}

function removeDefaultSheet_(ss) {
  const def = ss.getSheetByName("Feuille 1") || ss.getSheetByName("Sheet1");
  if (def && ss.getSheets().length > 1) ss.deleteSheet(def);
}

function findFileByName_(name) {
  const it = DriveApp.getFilesByName(name);
  return it.hasNext() ? it.next() : null;
}
