/**
 * =============================================================
 * schoolsWP – FULL DRIVE Audit & Migration  v1.2
 * =============================================================
 *
 * OBJECTIF : Auditer TOUT le Google Drive, détecter les anomalies
 * de nommage et de rangement, proposer un mapping, exécuter la
 * migration par lots (batch) pour éviter le timeout de 6 min.
 *
 * RÈGLES INTÉGRÉES (Docs 2-4) :
 * - Fichiers génériques : AAAA-MM-JJ – Sujet – Type – Information
 * - Factures : AAAA-MM-JJ – FournisseurOuClient – Facture – Montant.pdf
 * - Relevés : AAAA-MM – Relevé bancaire – NomBanque.pdf
 * - Contrats : AAAA-MM-JJ – NomEntité – Type de contrat
 * - Contenus : AAAA-MM-JJ – Sujet – Type (Article/Tutoriel/Guide/etc.)
 * - Assets : AAAA-MM-JJ – Sujet – Usage – Format
 * - Monétisation : AAAA-MM-JJ – Sujet – Levier – Type
 *
 * BATCH PROCESSING :
 * - Le Drive est audité dossier racine par dossier racine
 * - Chaque lot tient dans le timeout de 6 min
 * - Un Google Sheet accumule les résultats lot par lot
 *
 * MODE D'EMPLOI :
 * 1. Coller dans : FullDriveAudit.gs
 * 2. Exécuter : fullDriveAudit()        → audit par lots
 * 3. Exécuter : fullDriveMapping()       → mapping dans un Sheet
 * 4. [VALIDATION HUMAINE]
 * 5. Exécuter : fullDriveMigration()     → migration safe par lots
 * 6. Exécuter : fullDriveIndex()         → index global Sheet + .md
 * =============================================================
 */

// ══════════════════════════════════════════════════════════════
// CONFIGURATION
// ══════════════════════════════════════════════════════════════

/**
 * Nom du Google Sheet pour l'audit/mapping Drive complet
 */
var FULL_MAPPING_SHEET = "schoolsWP \u2013 Full Drive Mapping";

/**
 * Nom du Google Sheet pour l'index Drive complet
 */
var FULL_INDEX_SHEET = "schoolsWP \u2013 Full Drive Index";

/**
 * Dossiers racine structurés (à auditer)
 * Le script les parcourt un par un pour éviter le timeout.
 */
var STRUCTURED_ROOT_FOLDERS = [
  "00_START-HERE",
  "01_ADMIN",
  "02_PROJETS",
  "03_RESSOURCES",
  "04_ASSETS",
  "05_CLIENTS",
  "06_CONTENUS",
  "PROMPTS_schoolsWP",
  "99_ARCHIVES"
];

/**
 * Séparateur universel
 */
var DSEP = " \u2013 ";

/**
 * Formats de date acceptés
 */
var DATE_REGEX = /^(\d{4}-\d{2}-\d{2})/;
var DATE_MONTH_REGEX = /^(\d{4}-\d{2})(?!\d)/;

// ══════════════════════════════════════════════════════════════
// RÈGLES DE NOMMAGE PAR CATÉGORIE (Docs 2-4)
// ══════════════════════════════════════════════════════════════

/**
 * Règles de nommage par dossier racine.
 * Chaque règle contient :
 * - pattern : regex du format attendu
 * - format : description humaine
 * - fields : les champs attendus dans l'ordre
 */
var NAMING_RULES = {
  "01_ADMIN": {
    "04_Factures": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 Facture \u2013 /,
      format: "AAAA-MM-JJ \u2013 FournisseurOuClient \u2013 Facture \u2013 Montant.pdf",
      fields: ["date", "entite", "type:Facture", "montant"]
    },
    "03_Banque": {
      pattern: /^\d{4}-\d{2} \u2013 Relev\u00e9? bancaire \u2013 /i,
      format: "AAAA-MM \u2013 Relev\u00e9 bancaire \u2013 NomBanque.pdf",
      fields: ["date_month", "type:Relev\u00e9 bancaire", "banque"]
    },
    "05_Contrats": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 (Contrat|NDA)/,
      format: "AAAA-MM-JJ \u2013 NomEntit\u00e9 \u2013 Type de contrat",
      fields: ["date", "entite", "type_contrat"]
    },
    "_default": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 .+/,
      format: "AAAA-MM-JJ \u2013 Sujet \u2013 Type \u2013 Information",
      fields: ["date", "sujet", "type", "info"]
    }
  },
  "02_PROJETS": {
    "_default": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 (Article|Tutoriel|Guide|Vid\u00e9o|Video|Newsletter|Note)/i,
      format: "AAAA-MM-JJ \u2013 Sujet \u2013 Type",
      fields: ["date", "sujet", "type_contenu"]
    }
  },
  "04_ASSETS": {
    "_default": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 .+ \u2013 /,
      format: "AAAA-MM-JJ \u2013 Sujet \u2013 Usage \u2013 Format",
      fields: ["date", "sujet", "usage_asset", "format"]
    }
  },
  "06_CONTENUS": {
    "_default": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 (Article|Tutoriel|Guide|Vid\u00e9o|Video|Newsletter|Note)/i,
      format: "AAAA-MM-JJ \u2013 Sujet \u2013 Type",
      fields: ["date", "sujet", "type_contenu"]
    }
  },
  "_default": {
    "_default": {
      pattern: /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 .+/,
      format: "AAAA-MM-JJ \u2013 Sujet \u2013 Type \u2013 Information",
      fields: ["date", "sujet", "type", "info"]
    }
  }
};

/**
 * Types de contenus valides (Doc 2 §4.2)
 */
var CONTENT_TYPES = ["Article", "Tutoriel", "Guide", "Vid\u00e9o", "Video", "Newsletter", "Note"];

/**
 * Usages assets valides (Doc 2 §4.4)
 */
var ASSET_USAGES = [
  "Logo principal", "Charte graphique", "Illustration",
  "Capture ecran", "Cover article", "Thumbnail YouTube",
  "Lead magnet", "Ressource"
];

/**
 * Leviers monétisation (Doc 2 §4.5)
 */
var MONET_LEVERS = ["Affiliation", "Produit", "Campagne", "Business"];

/**
 * Types de contrats (Doc 2 §7)
 */
var CONTRACT_TYPES = [
  "Contrat prestation", "Contrat freelance", "Contrat partenariat",
  "NDA", "Contrat affiliation"
];

// ══════════════════════════════════════════════════════════════
// 1. AUDIT PAR LOTS
// ══════════════════════════════════════════════════════════════

/**
 * Audit complet du Drive, TOUS les dossiers racine (pas seulement les structurés).
 * Stocke les résultats dans PropertiesService pour le mapping.
 */
function fullDriveAudit() {
  Logger.log("=== FULL DRIVE AUDIT v1.1 ===");
  var startTime = new Date();
  var root = DriveApp.getRootFolder();

  var allResults = [];
  var totalFiles = 0;
  var totalAnomalies = 0;
  var timedOut = false;

  // Collecter TOUS les dossiers à la racine du Drive
  var allRootFolders = [];
  var rootIterator = root.getFolders();
  while (rootIterator.hasNext()) {
    var rf = rootIterator.next();
    var rfName = rf.getName();
    // Ignorer les dossiers de backup créés par nos scripts
    if (rfName.startsWith("_BACKUP")) continue;
    allRootFolders.push({ folder: rf, name: rfName });
  }

  Logger.log("Dossiers racine trouves : " + allRootFolders.length);
  for (var d = 0; d < allRootFolders.length; d++) {
    Logger.log("  - " + allRootFolders[d].name);
  }

  // Auditer CHAQUE dossier racine (structurés et non-structurés)
  for (var r = 0; r < allRootFolders.length; r++) {
    var folderEntry = allRootFolders[r];
    var folderName = folderEntry.name;
    var folder = folderEntry.folder;
    var isStructured = STRUCTURED_ROOT_FOLDERS.indexOf(folderName) !== -1;

    Logger.log("[AUDIT] " + folderName + (isStructured ? "" : " (NON-STRUCTURE)") + "...");

    try {
      var files = [];
      collectAllFiles_(folder, "", files);

      Logger.log("  Fichiers : " + files.length);

      // Analyser chaque fichier selon les règles de son dossier racine
      // Les dossiers non-structurés utilisent les règles _default
      var rulesKey = isStructured ? folderName : "_default";
      for (var f = 0; f < files.length; f++) {
        var file = files[f];
        var analysis = analyzeFullDriveFile_(file, rulesKey);

        // Signaler les fichiers dans des dossiers non-structurés
        if (!isStructured) {
          analysis.issues.push("Dans un dossier non-structure (" + folderName + ")");
          if (analysis.severity === "OK") analysis.severity = "MOYEN";
          if (!analysis.correctFolder) {
            analysis.correctFolder = guessCorrectRootFolder_(file);
          }
        }

        file.analysis = analysis;
        file.rootFolder = folderName;

        if (analysis.issues.length > 0) {
          totalAnomalies++;
        }
      }

      totalFiles += files.length;
      allResults = allResults.concat(files);
    } catch (folderErr) {
      Logger.log("  [ERREUR DOSSIER] " + folderName + " : " + folderErr.message);
      Logger.log("  Le dossier est ignore, l'audit continue...");
    }

    // Pause anti rate-limiting entre chaque dossier racine
    Utilities.sleep(500);

    // Vérifier le temps écoulé (arrêt de sécurité à 5 min)
    var elapsed = (new Date() - startTime) / 1000;
    if (elapsed > 300) {
      Logger.log("[TIMEOUT] Arret de securite a 5 min. Dossiers restants non audites.");
      Logger.log("  Relancer fullDriveAudit() pour continuer.");
      timedOut = true;
      break;
    }
  }

  // Auditer aussi les fichiers orphelins (directement à la racine du Drive)
  var elapsed2 = (new Date() - startTime) / 1000;
  if (!timedOut && elapsed2 < 300) {
    Logger.log("[AUDIT] Fichiers a la racine du Drive...");
    var rootFiles = root.getFiles();
    var orphanCount = 0;
    while (rootFiles.hasNext()) {
      var rootFile = rootFiles.next();
      if (rootFile.getMimeType() === "application/vnd.google-apps.shortcut") continue;

      var orphan = {
        id: rootFile.getId(),
        name: rootFile.getName(),
        path: "RACINE",
        fullPath: "RACINE/" + rootFile.getName(),
        mimeType: rootFile.getMimeType(),
        size: rootFile.getSize(),
        created: rootFile.getDateCreated().toISOString(),
        modified: rootFile.getLastUpdated().toISOString(),
        url: rootFile.getUrl()
      };
      orphan.analysis = {
        issues: ["Fichier a la racine du Drive (devrait etre dans un dossier)"],
        severity: "CRITIQUE",
        correctFolder: guessCorrectRootFolder_(orphan),
        hasDate: DATE_REGEX.test(orphan.name),
        hasCorrectFormat: false
      };
      orphan.rootFolder = "RACINE";
      allResults.push(orphan);
      orphanCount++;
      totalAnomalies++;
    }
    Logger.log("  Orphelins racine : " + orphanCount);
    totalFiles += orphanCount;
  }

  // Stocker les résultats
  storeFullAuditData_(allResults);

  var duration = (new Date() - startTime) / 1000;

  Logger.log("");
  Logger.log("=========================================");
  Logger.log("RAPPORT D'AUDIT - DRIVE COMPLET");
  Logger.log("=========================================");
  Logger.log("Total fichiers   : " + totalFiles);
  Logger.log("Anomalies        : " + totalAnomalies);
  Logger.log("Duree            : " + duration + "s");
  Logger.log("=========================================");
  Logger.log("");
  Logger.log(">>> Prochaine etape : fullDriveMapping()");
}

/**
 * Collecte récursive des fichiers (réutilisée)
 * Résilient aux erreurs Drive API (permissions, rate limiting, fichiers corrompus)
 */
function collectAllFiles_(folder, path, results) {
  var currentPath = path ? path + "/" + folder.getName() : folder.getName();

  // Collecter les fichiers avec retry sur "Service error: Drive"
  var fileRetries = 0;
  var fileSuccess = false;
  while (!fileSuccess && fileRetries < 3) {
    try {
      var files = folder.getFiles();
      while (files.hasNext()) {
        try {
          var file = files.next();
          var mime = file.getMimeType();
          if (mime === "application/vnd.google-apps.shortcut") continue;

          results.push({
            id: file.getId(),
            name: file.getName(),
            path: currentPath,
            fullPath: currentPath + "/" + file.getName(),
            mimeType: mime,
            size: file.getSize(),
            created: file.getDateCreated().toISOString(),
            modified: file.getLastUpdated().toISOString(),
            url: file.getUrl()
          });
        } catch (fileErr) {
          Logger.log("  [WARN] Fichier inaccessible dans " + currentPath + " : " + fileErr.message);
        }
      }
      fileSuccess = true;
    } catch (listErr) {
      fileRetries++;
      if (listErr.message && listErr.message.indexOf("Service error") !== -1 && fileRetries < 3) {
        Logger.log("  [RETRY " + fileRetries + "/3] " + currentPath + " : " + listErr.message);
        Utilities.sleep(1000 * fileRetries);
      } else {
        Logger.log("  [ERREUR] Impossible de lister les fichiers de " + currentPath + " : " + listErr.message);
      }
    }
  }

  // Collecter les sous-dossiers avec retry sur "Service error: Drive"
  var subRetries = 0;
  var subSuccess = false;
  while (!subSuccess && subRetries < 3) {
    try {
      var subFolders = folder.getFolders();
      while (subFolders.hasNext()) {
        try {
          var sub = subFolders.next();
          if (sub.getName().startsWith("_BACKUP")) continue;
          collectAllFiles_(sub, currentPath, results);
        } catch (subErr) {
          Logger.log("  [WARN] Sous-dossier inaccessible dans " + currentPath + " : " + subErr.message);
        }
      }
      subSuccess = true;
    } catch (listSubErr) {
      subRetries++;
      if (listSubErr.message && listSubErr.message.indexOf("Service error") !== -1 && subRetries < 3) {
        Logger.log("  [RETRY " + subRetries + "/3] sous-dossiers " + currentPath + " : " + listSubErr.message);
        Utilities.sleep(1000 * subRetries);
      } else {
        Logger.log("  [ERREUR] Impossible de lister les sous-dossiers de " + currentPath + " : " + listSubErr.message);
      }
    }
  }
}

/**
 * Analyse un fichier selon les règles de son dossier racine
 */
function analyzeFullDriveFile_(file, rootFolderName) {
  var analysis = {
    hasDate: false,
    hasCorrectFormat: false,
    correctFolder: null,
    expectedFormat: "",
    issues: [],
    severity: "OK",
    proposedName: null,
    proposedPath: null
  };

  var name = file.name;

  // 1. Vérifier la date
  var hasFullDate = DATE_REGEX.test(name);
  var hasMonthDate = DATE_MONTH_REGEX.test(name);
  analysis.hasDate = hasFullDate || hasMonthDate;

  if (!analysis.hasDate) {
    analysis.issues.push("Date manquante");
  }

  // 2. Vérifier le séparateur
  if (!name.includes(DSEP) && (name.includes(" - ") || name.includes("__") || name.includes("_"))) {
    analysis.issues.push("Mauvais separateur (attendu : tiret long)");
  }

  // 3. Trouver la règle applicable
  var rule = findApplicableRule_(rootFolderName, file.path);
  analysis.expectedFormat = rule.format;

  // 4. Vérifier le format
  analysis.hasCorrectFormat = rule.pattern.test(name);
  if (!analysis.hasCorrectFormat) {
    analysis.issues.push("Format non conforme (attendu : " + rule.format + ")");
  }

  // 5. Vérifier le rangement
  var correctFolder = guessCorrectFolder_(file, rootFolderName);
  if (correctFolder && !file.path.toLowerCase().includes(correctFolder.toLowerCase())) {
    analysis.correctFolder = correctFolder;
    analysis.issues.push("Mal range (devrait etre dans " + correctFolder + ")");
  }

  // 6. Proposer un nouveau nom si nécessaire
  if (!analysis.hasCorrectFormat) {
    analysis.proposedName = proposeFullDriveName_(file, rootFolderName, rule);
  }

  // 7. Sévérité
  var critical = analysis.issues.filter(function(i) {
    return i.includes("Date manquante") || i.includes("racine du Drive");
  }).length;
  var medium = analysis.issues.filter(function(i) {
    return i.includes("Format non conforme") || i.includes("Mal range");
  }).length;

  if (critical > 0) analysis.severity = "CRITIQUE";
  else if (medium > 0) analysis.severity = "MOYEN";
  else if (analysis.issues.length > 0) analysis.severity = "MINEUR";

  return analysis;
}

/**
 * Trouve la règle de nommage applicable
 */
function findApplicableRule_(rootFolderName, filePath) {
  var rootRules = NAMING_RULES[rootFolderName] || NAMING_RULES["_default"];

  // Chercher une règle spécifique au sous-dossier
  for (var subFolder in rootRules) {
    if (subFolder === "_default") continue;
    if (filePath && filePath.includes(subFolder)) {
      return rootRules[subFolder];
    }
  }

  return rootRules["_default"] || NAMING_RULES["_default"]["_default"];
}

/**
 * Propose un nouveau nom selon les règles
 */
function proposeFullDriveName_(file, rootFolderName, rule) {
  var name = file.name;

  // Extraire la date ou utiliser la date de création
  var dateStr = "";
  var dateMatch = name.match(DATE_REGEX);
  if (dateMatch) {
    dateStr = dateMatch[1];
  } else {
    var monthMatch = name.match(DATE_MONTH_REGEX);
    if (monthMatch) {
      dateStr = monthMatch[1];
    } else {
      dateStr = file.created ? file.created.substring(0, 10) : "2026-01-01";
    }
  }

  // Extraire l'extension
  var extMatch = name.match(/\.([^.]+)$/);
  var ext = extMatch ? extMatch[1] : "";
  var isGoogleNative = file.mimeType && file.mimeType.startsWith("application/vnd.google-apps.");

  // Nettoyer le sujet
  var subject = name
    .replace(/^\d{4}-\d{2}(-\d{2})?[\s\u2013\-_]*/, "")
    .replace(/\.[^.]+$/, "")
    .replace(/ - /g, " ")
    .replace(/__/g, " ")
    .replace(/_/g, " ")
    .trim();

  // Capitaliser
  if (subject) {
    subject = subject.charAt(0).toUpperCase() + subject.slice(1);
  }

  // Construire selon le dossier racine
  var newName = "";

  if (rootFolderName === "01_ADMIN" && file.path.includes("04_Factures")) {
    // Format facture : AAAA-MM-JJ – Entité – Facture – Montant.pdf
    newName = dateStr + DSEP + subject + DSEP + "Facture";
  } else if (rootFolderName === "01_ADMIN" && file.path.includes("03_Banque")) {
    // Format relevé : AAAA-MM – Relevé bancaire – Banque.pdf
    newName = dateStr.substring(0, 7) + DSEP + "Releve bancaire" + DSEP + subject;
  } else if (rootFolderName === "01_ADMIN" && file.path.includes("05_Contrats")) {
    // Format contrat : AAAA-MM-JJ – Entité – Type contrat
    newName = dateStr + DSEP + subject + DSEP + "Contrat";
  } else if (rootFolderName === "04_ASSETS") {
    // Format asset : AAAA-MM-JJ – Sujet – Usage – Format
    var usage = guessAssetUsage_(name);
    newName = dateStr + DSEP + subject + DSEP + usage;
  } else if (rootFolderName === "06_CONTENUS" || (rootFolderName === "02_PROJETS" && file.path.includes("02_Contenus"))) {
    // Format contenu : AAAA-MM-JJ – Sujet – Type
    var contentType = guessContentType_(name);
    newName = dateStr + DSEP + subject + DSEP + contentType;
  } else {
    // Format générique
    newName = dateStr + DSEP + subject;
  }

  // Ajouter l'extension
  if (!isGoogleNative && ext) {
    newName += "." + ext;
  }

  return newName;
}

/**
 * Devine le type de contenu
 */
function guessContentType_(name) {
  var lower = name.toLowerCase();
  if (lower.includes("tutoriel") || lower.includes("tutorial")) return "Tutoriel";
  if (lower.includes("guide")) return "Guide";
  if (lower.includes("video") || lower.includes("vid\u00e9o")) return "Video";
  if (lower.includes("newsletter")) return "Newsletter";
  if (lower.includes("note")) return "Note";
  return "Article";
}

/**
 * Devine l'usage d'un asset
 */
function guessAssetUsage_(name) {
  var lower = name.toLowerCase();
  if (lower.includes("logo")) return "Logo principal";
  if (lower.includes("charte")) return "Charte graphique";
  if (lower.includes("illustration")) return "Illustration";
  if (lower.includes("capture") || lower.includes("screenshot")) return "Capture ecran";
  if (lower.includes("cover")) return "Cover article";
  if (lower.includes("thumbnail") || lower.includes("miniature")) return "Thumbnail YouTube";
  if (lower.includes("lead") || lower.includes("magnet")) return "Lead magnet";
  return "Ressource";
}

/**
 * Devine le bon dossier racine pour un fichier
 */
function guessCorrectRootFolder_(file) {
  var name = file.name.toLowerCase();
  if (name.includes("facture")) return "01_ADMIN/04_Factures";
  if (name.includes("relev") || name.includes("bancaire")) return "01_ADMIN/03_Banque";
  if (name.includes("contrat") || name.includes("nda")) return "01_ADMIN/05_Contrats";
  if (name.includes("logo") || name.includes("banner") || name.includes("thumbnail")) return "04_ASSETS";
  if (name.includes("article") || name.includes("tutoriel") || name.includes("guide")) return "06_CONTENUS";
  if (name.includes("prompt") || name.includes("template")) return "PROMPTS_schoolsWP";
  return "03_RESSOURCES";
}

/**
 * Devine le bon sous-dossier pour un fichier
 */
function guessCorrectFolder_(file, rootFolderName) {
  var name = file.name.toLowerCase();
  var path = file.path.toLowerCase();

  if (rootFolderName === "01_ADMIN") {
    if (name.includes("facture")) return "04_Factures";
    if (name.includes("relev") || name.includes("bancaire")) return "03_Banque";
    if (name.includes("contrat") || name.includes("nda")) return "05_Contrats";
  }

  if (rootFolderName === "06_CONTENUS") {
    // Vérifier le statut par le contenu/nom
    if (path.includes("archive") || path.includes("99_")) return "99_ARCHIVES";
  }

  return null; // Pas de suggestion
}

/**
 * Nom du fichier temporaire pour stocker les données d'audit dans Drive.
 * Utilise un fichier Drive au lieu de PropertiesService pour éviter
 * la limite de 500KB du quota Properties.
 */
var AUDIT_DATA_FILENAME = "_schoolsWP_audit_data.json";

/**
 * Stocke les données d'audit dans un fichier JSON sur le Drive.
 * Pas de limite de taille (contrairement à PropertiesService 500KB).
 */
function storeFullAuditData_(files) {
  var json = JSON.stringify(files);

  // Chercher un fichier existant pour le remplacer
  var existing = DriveApp.getFilesByName(AUDIT_DATA_FILENAME);
  if (existing.hasNext()) {
    var oldFile = existing.next();
    oldFile.setTrashed(true);
  }

  // Créer le nouveau fichier JSON
  DriveApp.createFile(AUDIT_DATA_FILENAME, json, "application/json");

  Logger.log("Audit stocke dans Drive : " + files.length + " fichiers (" + Math.round(json.length / 1024) + " KB)");
}

/**
 * Charge les données d'audit depuis le fichier JSON Drive.
 */
function loadFullAuditData_() {
  var files = DriveApp.getFilesByName(AUDIT_DATA_FILENAME);
  if (!files.hasNext()) {
    // Fallback : essayer l'ancien stockage PropertiesService
    return loadFullAuditDataLegacy_();
  }

  var file = files.next();
  var json = file.getBlob().getDataAsString();
  if (!json) return null;
  return JSON.parse(json);
}

/**
 * Fallback : charge depuis PropertiesService (ancien format)
 */
function loadFullAuditDataLegacy_() {
  var props = PropertiesService.getScriptProperties();
  var chunks = parseInt(props.getProperty("full_audit_chunks") || "0");

  var json;
  if (chunks > 0) {
    var parts = [];
    for (var i = 0; i < chunks; i++) {
      parts.push(props.getProperty("full_audit_" + i));
    }
    json = parts.join("");
  } else {
    json = props.getProperty("full_audit_data");
  }

  if (!json) return null;
  return JSON.parse(json);
}

// ══════════════════════════════════════════════════════════════
// 2. MAPPING DRIVE COMPLET
// ══════════════════════════════════════════════════════════════

/**
 * Génère le mapping complet dans un Google Sheet
 */
function fullDriveMapping() {
  Logger.log("=== FULL DRIVE MAPPING ===");

  var files = loadFullAuditData_();
  if (!files) {
    Logger.log("ERREUR : executer fullDriveAudit() d'abord !");
    return;
  }

  Logger.log("Fichiers a mapper : " + files.length);

  // Créer ou ouvrir le Sheet
  var ss;
  var existing = DriveApp.getFilesByName(FULL_MAPPING_SHEET);
  if (existing.hasNext()) {
    ss = SpreadsheetApp.open(existing.next());
  } else {
    ss = SpreadsheetApp.create(FULL_MAPPING_SHEET);
  }

  // Onglet Mapping
  var sheet = ss.getSheetByName("Mapping") || ss.insertSheet("Mapping");
  sheet.clear();

  var headers = [
    "ID", "Ancien nom", "Dossier racine", "Ancien chemin",
    "Nouveau nom", "Nouveau chemin", "Confiance %",
    "Action", "Severite", "Anomalies", "Format attendu",
    "Valide (OUI/NON)", "Notes"
  ];
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(1, 1, 1, headers.length).setFontWeight("bold");
  sheet.getRange(1, 1, 1, headers.length).setBackground("#1a73e8");
  sheet.getRange(1, 1, 1, headers.length).setFontColor("#ffffff");
  sheet.setFrozenRows(1);

  var rows = [];
  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    var a = file.analysis || {};
    var issues = a.issues || [];
    var confidence = 100;

    if (!a.hasDate) confidence -= 20;
    if (!a.hasCorrectFormat) confidence -= 15;
    if (a.correctFolder) confidence -= 15;
    if (!file.name.includes(DSEP)) confidence -= 10;
    confidence = Math.max(0, Math.min(100, confidence));

    var action = "OK";
    if (a.proposedName && a.correctFolder) action = "RENAME+MOVE";
    else if (a.proposedName) action = "RENAME";
    else if (a.correctFolder) action = "MOVE";

    if (confidence < 80) action = "A_VALIDER";

    rows.push([
      file.id,
      file.name,
      file.rootFolder || "",
      file.path,
      a.proposedName || file.name,
      a.correctFolder || file.path,
      confidence,
      action,
      a.severity || "OK",
      issues.join("; "),
      a.expectedFormat || "",
      confidence >= 80 && action !== "OK" ? "OUI" : "",
      ""
    ]);
  }

  // Écrire par lots de 500 lignes (éviter timeout Sheet)
  var batchSize = 500;
  for (var b = 0; b < rows.length; b += batchSize) {
    var batch = rows.slice(b, Math.min(b + batchSize, rows.length));
    sheet.getRange(b + 2, 1, batch.length, headers.length).setValues(batch);
  }

  // Mise en forme conditionnelle
  if (rows.length > 0) {
    var confRange = sheet.getRange(2, 7, rows.length, 1);
    var ruleConf = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(80)
      .setBackground("#ffcccc")
      .setRanges([confRange])
      .build();

    var sevRange = sheet.getRange(2, 9, rows.length, 1);
    var ruleSev = SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("CRITIQUE")
      .setBackground("#ff9900")
      .setFontColor("#ffffff")
      .setRanges([sevRange])
      .build();

    sheet.setConditionalFormatRules([ruleConf, ruleSev]);
  }

  // Onglet Résumé
  var summary = ss.getSheetByName("Resume") || ss.insertSheet("Resume");
  summary.clear();

  // Compter par dossier racine
  var byRoot = {};
  var byAction = {};
  var bySeverity = {};
  for (var s = 0; s < rows.length; s++) {
    var rootF = rows[s][2];
    var act = rows[s][7];
    var sev = rows[s][8];
    byRoot[rootF] = (byRoot[rootF] || 0) + 1;
    byAction[act] = (byAction[act] || 0) + 1;
    bySeverity[sev] = (bySeverity[sev] || 0) + 1;
  }

  var summaryData = [
    ["Metrique", "Valeur"],
    ["Total fichiers", files.length],
    ["Confiance >= 80%", rows.filter(function(r) { return r[6] >= 80; }).length],
    ["A valider", rows.filter(function(r) { return r[6] < 80; }).length],
    ["", ""],
    ["Par dossier racine", ""]
  ];
  for (var rn in byRoot) { summaryData.push([rn, byRoot[rn]]); }
  summaryData.push(["", ""]);
  summaryData.push(["Par action", ""]);
  for (var an in byAction) { summaryData.push([an, byAction[an]]); }
  summaryData.push(["", ""]);
  summaryData.push(["Par severite", ""]);
  for (var sn in bySeverity) { summaryData.push([sn, bySeverity[sn]]); }

  summary.getRange(1, 1, summaryData.length, 2).setValues(summaryData);
  summary.getRange(1, 1, 1, 2).setFontWeight("bold");

  // Supprimer feuille par défaut
  var def = ss.getSheetByName("Feuille 1") || ss.getSheetByName("Sheet1");
  if (def && ss.getSheets().length > 1) ss.deleteSheet(def);

  Logger.log("Mapping genere : " + ss.getUrl());
  Logger.log("Total : " + rows.length + " fichiers");
  Logger.log("A valider : " + rows.filter(function(r) { return r[6] < 80; }).length);
  Logger.log("");
  Logger.log(">>> Prochaine etape : valider le Sheet puis fullDriveMigration()");
}

// ══════════════════════════════════════════════════════════════
// 3. MIGRATION DRIVE COMPLET (PAR LOTS)
// ══════════════════════════════════════════════════════════════

/**
 * Exécute la migration du Drive complet par lots.
 * Traite les lignes OUI du Sheet de mapping.
 * S'arrête à 5 min et peut être relancé (les lignes traitées sont marquées).
 */
function fullDriveMigration() {
  Logger.log("=== FULL DRIVE MIGRATION (par lots) ===");
  var startTime = new Date();

  var sheetFiles = DriveApp.getFilesByName(FULL_MAPPING_SHEET);
  if (!sheetFiles.hasNext()) {
    Logger.log("ERREUR : Sheet non trouve ! Executer fullDriveMapping() d'abord.");
    return;
  }

  var ss = SpreadsheetApp.open(sheetFiles.next());
  var sheet = ss.getSheetByName("Mapping");
  var data = sheet.getDataRange().getValues();

  // Backup global
  var today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");
  var root = DriveApp.getRootFolder();
  var backupSearch = root.getFoldersByName("_BACKUP_DRIVE_" + today);
  var backupFolder = backupSearch.hasNext()
    ? backupSearch.next()
    : root.createFolder("_BACKUP_DRIVE_" + today);

  var renamed = 0;
  var moved = 0;
  var skipped = 0;
  var errors = 0;

  // Colonnes v1 full drive : 13 colonnes
  // Index 0:ID, 1:Ancien nom, 4:Nouveau nom, 5:Nouveau chemin, 7:Action, 11:Validé, 12:Notes
  for (var i = 1; i < data.length; i++) {
    // Timeout check
    if ((new Date() - startTime) / 1000 > 300) {
      Logger.log("[TIMEOUT] Arret a 5 min. Ligne " + i + "/" + data.length);
      Logger.log("Relancer fullDriveMigration() pour continuer.");
      break;
    }

    var row = data[i];
    var fileId = row[0];
    var oldName = row[1];
    var newName = row[4];
    var newPath = row[5];
    var action = row[7];
    var validated = row[11];
    var notes = row[12];

    // Skip déjà traité ou non validé
    if (String(validated).toUpperCase() !== "OUI") { skipped++; continue; }
    if (action === "OK") continue;
    if (String(notes).includes("[DONE]")) continue;

    try {
      var file = DriveApp.getFileById(fileId);
      file.makeCopy(file.getName(), backupFolder);

      if (action === "RENAME" || action === "RENAME+MOVE") {
        if (newName && newName !== oldName) {
          file.setName(newName);
          renamed++;
          Logger.log("[RENAME] " + oldName + " -> " + newName);
        }
      }

      if (action === "MOVE" || action === "RENAME+MOVE") {
        if (newPath && newPath !== file.getParents().next().getName()) {
          // Naviguer vers le dossier cible
          var targetFolder = navigateFromRoot_(newPath);
          if (targetFolder) {
            targetFolder.addFile(file);
            var parents = file.getParents();
            while (parents.hasNext()) {
              var parent = parents.next();
              if (parent.getId() !== targetFolder.getId()) {
                parent.removeFile(file);
              }
            }
            moved++;
            Logger.log("[MOVE] " + oldName + " -> " + newPath);
          }
        }
      }

      // Marquer comme traité dans le Sheet
      sheet.getRange(i + 1, 13).setValue("[DONE] " + (notes || ""));

    } catch (e) {
      Logger.log("[ERREUR] " + oldName + " : " + e.message);
      sheet.getRange(i + 1, 13).setValue("[ERREUR] " + e.message);
      errors++;
    }
  }

  Logger.log("");
  Logger.log("=========================================");
  Logger.log("RAPPORT MIGRATION DRIVE");
  Logger.log("=========================================");
  Logger.log("Renommes  : " + renamed);
  Logger.log("Deplaces  : " + moved);
  Logger.log("Ignores   : " + skipped);
  Logger.log("Erreurs   : " + errors);
  Logger.log("Backup    : " + backupFolder.getUrl());
  Logger.log("=========================================");
}

/**
 * Navigue vers un dossier depuis la racine du Drive
 */
function navigateFromRoot_(path) {
  var parts = path.split("/");
  var current = DriveApp.getRootFolder();

  for (var p = 0; p < parts.length; p++) {
    var part = parts[p];
    if (!part) continue;
    var subs = current.getFoldersByName(part);
    if (subs.hasNext()) {
      current = subs.next();
    } else {
      current = current.createFolder(part);
      Logger.log("[MKDIR] " + part);
    }
  }
  return current;
}

// ══════════════════════════════════════════════════════════════
// 4. INDEX GLOBAL DRIVE
// ══════════════════════════════════════════════════════════════

/**
 * Génère l'index global de tout le Drive structuré
 */
function fullDriveIndex() {
  Logger.log("=== FULL DRIVE INDEX ===");
  var root = DriveApp.getRootFolder();
  var today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");

  var allFiles = [];

  // Scanner TOUS les dossiers racine (pas seulement les structurés)
  var rootIterator = root.getFolders();
  while (rootIterator.hasNext()) {
    var rf = rootIterator.next();
    var rfName = rf.getName();
    if (rfName.startsWith("_BACKUP")) continue;
    collectAllFiles_(rf, "", allFiles);
  }

  // Filtrer backups et raccourcis
  allFiles = allFiles.filter(function(f) {
    return !f.name.startsWith("_") && !f.path.includes("_BACKUP");
  });

  allFiles.sort(function(a, b) {
    return (a.path + "/" + a.name).localeCompare(b.path + "/" + b.name);
  });

  // Google Sheet
  var ss;
  var existingSheets = DriveApp.getFilesByName(FULL_INDEX_SHEET);
  if (existingSheets.hasNext()) {
    ss = SpreadsheetApp.open(existingSheets.next());
  } else {
    ss = SpreadsheetApp.create(FULL_INDEX_SHEET);
  }

  var indexSheet = ss.getSheetByName("Index") || ss.insertSheet("Index");
  indexSheet.clear();

  var headers = ["#", "Nom", "Chemin", "Dossier racine", "Derniere MAJ", "Lien"];
  indexSheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  indexSheet.getRange(1, 1, 1, headers.length).setFontWeight("bold");
  indexSheet.getRange(1, 1, 1, headers.length).setBackground("#1a73e8");
  indexSheet.getRange(1, 1, 1, headers.length).setFontColor("#ffffff");
  indexSheet.setFrozenRows(1);

  var rows = [];
  for (var i = 0; i < allFiles.length; i++) {
    var f = allFiles[i];
    var rootName = f.path.split("/")[0] || "";
    rows.push([
      i + 1,
      f.name,
      f.path,
      rootName,
      f.modified ? f.modified.substring(0, 10) : today,
      f.url
    ]);
  }

  var batchSize = 500;
  for (var b = 0; b < rows.length; b += batchSize) {
    var batch = rows.slice(b, Math.min(b + batchSize, rows.length));
    indexSheet.getRange(b + 2, 1, batch.length, headers.length).setValues(batch);
  }

  if (rows.length > 0) {
    var filterRange = indexSheet.getRange(1, 1, rows.length + 1, headers.length);
    if (indexSheet.getFilter()) indexSheet.getFilter().remove();
    filterRange.createFilter();
  }

  // Supprimer feuille par défaut
  var def = ss.getSheetByName("Feuille 1") || ss.getSheetByName("Sheet1");
  if (def && ss.getSheets().length > 1) ss.deleteSheet(def);

  Logger.log("Index Drive : " + ss.getUrl());
  Logger.log("Total : " + rows.length + " fichiers");
}

// ══════════════════════════════════════════════════════════════
// EXPLORATION 06_archive – Récursive complète
// ══════════════════════════════════════════════════════════════

/**
 * Explore TOUTE l'arborescence de 06_archive récursivement.
 * Affiche chaque dossier avec son nombre de fichiers et sous-dossiers.
 * Exécuter : explore06Archive()
 */
function explore06Archive() {
  Logger.log("=== EXPLORATION COMPLETE 06_archive ===");
  var root = DriveApp.getRootFolder();
  var iter = root.getFoldersByName("06_archive");
  if (!iter.hasNext()) {
    Logger.log("ERREUR : 06_archive non trouve");
    return;
  }
  var archiveRoot = iter.next();
  var totalFiles = 0;
  var totalFolders = 0;
  var result = exploreRecursive_(archiveRoot, "", 0);
  totalFiles = result.files;
  totalFolders = result.folders;

  Logger.log("");
  Logger.log("=== TOTAUX 06_archive ===");
  Logger.log("Total fichiers  : " + totalFiles);
  Logger.log("Total dossiers  : " + totalFolders);
  Logger.log("=========================");
}

function exploreRecursive_(folder, indent, depth) {
  var files = 0;
  var folders = 0;

  // Compter les fichiers directs
  var fileCount = 0;
  var sampleNames = [];
  try {
    var fileIter = folder.getFiles();
    while (fileIter.hasNext()) {
      var f = fileIter.next();
      fileCount++;
      if (sampleNames.length < 5) {
        sampleNames.push(f.getName());
      }
    }
  } catch (e) {
    Logger.log(indent + "[ERREUR fichiers] " + e.message);
  }
  files += fileCount;

  if (fileCount > 0) {
    Logger.log(indent + "[" + fileCount + " fichiers] ex: " + sampleNames.join(" | "));
  }

  // Parcourir les sous-dossiers
  try {
    var subIter = folder.getFolders();
    while (subIter.hasNext()) {
      var sub = subIter.next();
      folders++;
      var subName = sub.getName();
      Logger.log(indent + "📁 " + subName);
      var childResult = exploreRecursive_(sub, indent + "  ", depth + 1);
      files += childResult.files;
      folders += childResult.folders;
    }
  } catch (e) {
    Logger.log(indent + "[ERREUR sous-dossiers] " + e.message);
  }

  return { files: files, folders: folders };
}

/**
 * Explore aussi le dossier Photos pour confirmer le contenu.
 * Exécuter : explorePhotos()
 */
function explorePhotos() {
  Logger.log("=== EXPLORATION Photos ===");
  var root = DriveApp.getRootFolder();
  var iter = root.getFoldersByName("Photos");
  if (!iter.hasNext()) {
    Logger.log("ERREUR : Photos non trouve");
    return;
  }
  var photosRoot = iter.next();
  var result = exploreRecursive_(photosRoot, "", 0);
  Logger.log("");
  Logger.log("=== TOTAUX Photos ===");
  Logger.log("Total fichiers  : " + result.files);
  Logger.log("Total dossiers  : " + result.folders);
}

// ══════════════════════════════════════════════════════════════
// PHASE 2 : CLASSIFICATION & MIGRATION 06_archive + Photos
// ══════════════════════════════════════════════════════════════
//
// Ordre d'execution :
// 1. classifyArchive()          -> Classifie + Sheet de mapping
// 2. [VALIDATION HUMAINE]       -> Verifier le Sheet !
// 3. executeArchiveMigration()  -> Deplace + renomme (par lots)
// 4. movePhotosToPersonnel()    -> Photos -> 07_personnel
// ══════════════════════════════════════════════════════════════

var ARCHIVE_MAPPING_SHEET = "schoolsWP \u2013 Archive Migration";

/**
 * Classifie tous les fichiers de 06_archive et genere un Google Sheet
 * de mapping pour validation humaine.
 * Executuer : classifyArchive()
 */
function classifyArchive() {
  Logger.log("=== CLASSIFICATION 06_archive ===");
  var startTime = new Date();

  // Reutiliser les donnees d'audit deja stockees (evite timeout de re-scan)
  Logger.log("Chargement des donnees d'audit...");
  var auditData = loadFullAuditData_();
  var allFiles;

  if (auditData && auditData.length > 0) {
    // Filtrer pour ne garder que les fichiers de 06_archive
    allFiles = auditData.filter(function(f) {
      return f.path && f.path.indexOf("06_archive") === 0;
    });
    Logger.log("Donnees d'audit chargees : " + auditData.length + " fichiers au total");
    Logger.log("Fichiers 06_archive : " + allFiles.length);
  } else {
    Logger.log("ERREUR : pas de donnees d'audit. Executer fullDriveAudit() d'abord !");
    return;
  }

  // Classifier chaque fichier
  Logger.log("Classification en cours...");
  var classified = [];
  for (var i = 0; i < allFiles.length; i++) {
    var file = allFiles[i];
    var cls = classifyArchiveFile_(file);
    var proposedName = proposeArchiveName_(file, cls);

    classified.push({
      id: file.id,
      name: file.name,
      path: file.path,
      category: cls.category,
      destination: cls.dest,
      proposedName: proposedName,
      confidence: cls.confidence,
      mime: file.mimeType,
      created: file.created
    });
  }

  // Generer le Google Sheet
  Logger.log("Generation du Sheet...");
  var ss;
  var existing = DriveApp.getFilesByName(ARCHIVE_MAPPING_SHEET);
  if (existing.hasNext()) {
    ss = SpreadsheetApp.open(existing.next());
  } else {
    ss = SpreadsheetApp.create(ARCHIVE_MAPPING_SHEET);
  }

  // Onglet Mapping
  var sheet = ss.getSheetByName("Mapping") || ss.insertSheet("Mapping");
  sheet.clear();

  var headers = [
    "ID", "Nom actuel", "Chemin actuel", "Categorie",
    "Destination", "Nouveau nom", "Confiance %",
    "Valide (OUI/NON)", "Notes"
  ];
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(1, 1, 1, headers.length).setFontWeight("bold");
  sheet.getRange(1, 1, 1, headers.length).setBackground("#1a73e8");
  sheet.getRange(1, 1, 1, headers.length).setFontColor("#ffffff");
  sheet.setFrozenRows(1);

  var rows = [];
  for (var j = 0; j < classified.length; j++) {
    var c = classified[j];
    rows.push([
      c.id,
      c.name,
      c.path,
      c.category,
      c.destination,
      c.proposedName,
      c.confidence,
      c.confidence >= 85 ? "OUI" : "",
      ""
    ]);
  }

  // Ecrire par lots
  var batchSize = 500;
  for (var b = 0; b < rows.length; b += batchSize) {
    var batch = rows.slice(b, Math.min(b + batchSize, rows.length));
    sheet.getRange(b + 2, 1, batch.length, headers.length).setValues(batch);
  }

  // Mise en forme conditionnelle
  if (rows.length > 0) {
    var confRange = sheet.getRange(2, 7, rows.length, 1);
    var ruleRed = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(70)
      .setBackground("#ffcccc")
      .setRanges([confRange])
      .build();
    var ruleOrange = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberBetween(70, 84)
      .setBackground("#ffe0b2")
      .setRanges([confRange])
      .build();
    var ruleGreen = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberGreaterThanOrEqualTo(85)
      .setBackground("#c8e6c9")
      .setRanges([confRange])
      .build();
    sheet.setConditionalFormatRules([ruleRed, ruleOrange, ruleGreen]);
  }

  // Onglet Resume
  var summary = ss.getSheetByName("Resume") || ss.insertSheet("Resume");
  summary.clear();

  var byCategory = {};
  var byDest = {};
  var byConfidence = { high: 0, medium: 0, low: 0 };

  for (var k = 0; k < classified.length; k++) {
    var cat = classified[k].category;
    var dst = classified[k].destination;
    var conf = classified[k].confidence;
    byCategory[cat] = (byCategory[cat] || 0) + 1;
    byDest[dst] = (byDest[dst] || 0) + 1;
    if (conf >= 85) byConfidence.high++;
    else if (conf >= 70) byConfidence.medium++;
    else byConfidence.low++;
  }

  var summaryData = [
    ["Metrique", "Valeur"],
    ["Total fichiers 06_archive", classified.length],
    ["Confiance >= 85% (auto-valide)", byConfidence.high],
    ["Confiance 70-84% (a verifier)", byConfidence.medium],
    ["Confiance < 70% (manuel)", byConfidence.low],
    ["", ""],
    ["Par categorie", ""]
  ];
  for (var catName in byCategory) { summaryData.push([catName, byCategory[catName]]); }
  summaryData.push(["", ""]);
  summaryData.push(["Par destination", ""]);
  for (var destName in byDest) { summaryData.push([destName, byDest[destName]]); }

  summary.getRange(1, 1, summaryData.length, 2).setValues(summaryData);
  summary.getRange(1, 1, 1, 2).setFontWeight("bold");

  // Supprimer feuille par defaut
  var def = ss.getSheetByName("Feuille 1") || ss.getSheetByName("Sheet1");
  if (def && ss.getSheets().length > 1) ss.deleteSheet(def);

  var duration = (new Date() - startTime) / 1000;

  Logger.log("");
  Logger.log("=== RESULTATS CLASSIFICATION ===");
  Logger.log("Fichiers classifies : " + classified.length);
  Logger.log("Auto-valides (>=85%) : " + byConfidence.high);
  Logger.log("A verifier (70-84%)  : " + byConfidence.medium);
  Logger.log("Manuel (<70%)        : " + byConfidence.low);
  Logger.log("Duree : " + duration + "s");
  Logger.log("Sheet : " + ss.getUrl());
  Logger.log("");
  Logger.log(">>> Valider le Sheet puis executer executeArchiveMigration()");
}

// ══════════════════════════════════════════════════════════════
// CLASSIFICATION PAR CHEMIN (articles, images, sous-dossiers)
// ══════════════════════════════════════════════════════════════

/**
 * Classifie un fichier de 06_archive par son chemin et son contenu.
 * Retourne { dest, confidence, category }
 */
function classifyArchiveFile_(file) {
  var path = file.path || "";
  var pathUp = path.toUpperCase();
  var name = (file.name || "").toLowerCase();
  var mime = file.mimeType || "";
  var isImage = mime.indexOf("image") !== -1;
  var isZip = name.indexOf(".zip") !== -1;

  // ── ARTICLES TEXTE par langue ──

  if (pathUp.indexOf("ANGLAISE") !== -1 && pathUp.indexOf("/TEXTE") !== -1)
    return { dest: "02_PROJETS/schoolsWP/02_Contenus/04_Publies/Articles/EN", confidence: 95, category: "Article EN" };

  if (pathUp.indexOf("ALLEMANDE") !== -1 && pathUp.indexOf("/TEXTE") !== -1)
    return { dest: "02_PROJETS/schoolsWP/02_Contenus/04_Publies/Articles/DE", confidence: 95, category: "Article DE" };

  if (pathUp.indexOf("AISE") !== -1 && pathUp.indexOf("FRAN") !== -1 && pathUp.indexOf("/TEXTE") !== -1)
    return { dest: "02_PROJETS/schoolsWP/02_Contenus/04_Publies/Articles/FR", confidence: 95, category: "Article FR" };

  // ── MICHAELKIHL.FR (projet, pas archive) ──

  if (pathUp.indexOf("MICHAELKIHL") !== -1 && pathUp.indexOf("/TEXTE") !== -1)
    return { dest: "02_PROJETS/michaelkihl-fr/02_Contenus", confidence: 85, category: "Article MK" };

  if (pathUp.indexOf("MICHAELKIHL") !== -1 && pathUp.indexOf("ARTICLES") !== -1)
    return { dest: "02_PROJETS/michaelkihl-fr/02_Contenus", confidence: 80, category: "Article MK" };

  if (pathUp.indexOf("MICHAELKIHL") !== -1)
    return { dest: "02_PROJETS/michaelkihl-fr", confidence: 75, category: "Projet MK" };

  // ── AUDIO ──

  if (pathUp.indexOf("/AUDIO") !== -1)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/07_Audio", confidence: 90, category: "Audio" };

  // ── PINTEREST (images + zip) ──

  if (pathUp.indexOf("PINTEREST") !== -1 && isImage)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/02_Thumbnails", confidence: 95, category: "Pinterest" };

  if (pathUp.indexOf("PINTEREST") !== -1 && isZip)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/02_Thumbnails", confidence: 80, category: "Pinterest ZIP" };

  // ── INSTAGRAM ──

  if (pathUp.indexOf("INSTAGRAM") !== -1 && isImage)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/04_Illustrations", confidence: 85, category: "Instagram" };

  // ── IMAGES dans sous-dossier IMAGES (covers articles) ──

  if (pathUp.indexOf("/IMAGES") !== -1 && isImage)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/06_Covers-articles", confidence: 90, category: "Cover" };

  // ── IMAGES directement dans dossier article numerote (cover principale) ──

  if ((pathUp.indexOf("ANGLAISE") !== -1 || pathUp.indexOf("ALLEMANDE") !== -1 ||
       (pathUp.indexOf("FRAN") !== -1 && pathUp.indexOf("AISE") !== -1)) && isImage)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/06_Covers-articles", confidence: 85, category: "Cover" };

  // ── FLUENT CRM / FLUENT FORMS ──

  if (pathUp.indexOf("FLUENT CRM") !== -1)
    return { dest: "PROMPTS_schoolsWP/02_TEMPLATES/02_Email_CRM_FluentCRM", confidence: 85, category: "Email/CRM" };

  if (pathUp.indexOf("FLUENT FORMS") !== -1)
    return { dest: "PROMPTS_schoolsWP/02_TEMPLATES/02_Email_CRM_FluentCRM", confidence: 85, category: "Email/CRM" };

  // ── RESEAUX SOCIAUX ──

  if (pathUp.indexOf("SEAUX SOCIAUX") !== -1)
    return { dest: "02_PROJETS/schoolsWP/04_Assets", confidence: 75, category: "Social Media" };

  // ── MANYCHAT ──

  if (pathUp.indexOf("MANYCHAT") !== -1)
    return { dest: "02_PROJETS/schoolsWP/05_Automations", confidence: 80, category: "Automation" };

  // ── AMAZON ──

  if (pathUp.indexOf("AMAZON") !== -1)
    return { dest: "02_PROJETS/schoolsWP/06_Monetisation/01_Affiliation", confidence: 80, category: "Affiliation" };

  // ── DEVIS ──

  if (pathUp.indexOf("DEVIS") !== -1)
    return { dest: "05_CLIENTS", confidence: 75, category: "Devis" };

  // ── CANVA BULK ──

  if (pathUp.indexOf("CANVA") !== -1)
    return { dest: "02_PROJETS/schoolsWP/04_Assets", confidence: 75, category: "Asset Canva" };

  // ── SCHOOLSWP.COM/ARTICLES divers (zip, covers au niveau racine) ──

  if (pathUp.indexOf("SCHOOLSWP.COM/ARTICLES") !== -1 && isImage)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/06_Covers-articles", confidence: 75, category: "Cover" };

  if (pathUp.indexOf("SCHOOLSWP.COM/ARTICLES") !== -1)
    return { dest: "02_PROJETS/schoolsWP/04_Assets", confidence: 70, category: "Asset schoolsWP" };

  // ── SCHOOLSWP.COM root (pdf, images branding) ──

  if (pathUp.indexOf("SCHOOLSWP.COM") !== -1) {
    if (isImage) return { dest: "02_PROJETS/schoolsWP/04_Assets/01_Logos-Brand", confidence: 75, category: "Brand schoolsWP" };
    return { dest: "02_PROJETS/schoolsWP", confidence: 70, category: "schoolsWP" };
  }

  // ── TESTS & ANCIENS PROJETS ──

  if (pathUp.indexOf("/TESTS") !== -1)
    return { dest: "99_ARCHIVES", confidence: 70, category: "Test" };

  if (pathUp.indexOf("ANCIENS PROJETS") !== -1)
    return { dest: "99_ARCHIVES", confidence: 70, category: "Ancien projet" };

  // ── VRAC : fichiers dans "A trier plus tard" sans sous-dossier specifique ──
  return classifyByKeywords_(file);
}

// ══════════════════════════════════════════════════════════════
// CLASSIFICATION PAR MOTS-CLES (440 fichiers en vrac)
// ══════════════════════════════════════════════════════════════

/**
 * Classification par mots-cles pour les fichiers en vrac
 */
function classifyByKeywords_(file) {
  var name = (file.name || "").toLowerCase();
  var mime = file.mimeType || "";

  // Templates / Cheat sheets
  if (name.indexOf("template") !== -1 || name.indexOf("cheat sheet") !== -1 ||
      name.indexOf("cheatsheet") !== -1 || name.indexOf("mod\u00e8le") !== -1 ||
      name.indexOf("modele") !== -1)
    return { dest: "PROMPTS_schoolsWP/02_TEMPLATES/01_Editorial_SEO", confidence: 70, category: "Template" };

  // Checklists
  if (name.indexOf("checklist") !== -1 || name.indexOf("check-list") !== -1)
    return { dest: "03_RESSOURCES/01_Checklists", confidence: 75, category: "Checklist" };

  // Prompts / ChatGPT
  if (name.indexOf("prompt") !== -1 || name.indexOf("chatgpt") !== -1 ||
      name.indexOf("gpt") !== -1)
    return { dest: "PROMPTS_schoolsWP/03_PROMPTS/01_Editorial_SEO", confidence: 70, category: "Prompt" };

  // Email / Newsletter / CRM
  if (name.indexOf("email") !== -1 || name.indexOf("newsletter") !== -1 ||
      name.indexOf("crm") !== -1 || name.indexOf("autoresponder") !== -1 ||
      name.indexOf("sequence") !== -1)
    return { dest: "PROMPTS_schoolsWP/02_TEMPLATES/02_Email_CRM_FluentCRM", confidence: 70, category: "Email/CRM" };

  // SEO
  if (name.indexOf("seo") !== -1 || name.indexOf("keyword") !== -1 ||
      name.indexOf("backlink") !== -1 || name.indexOf("netlinking") !== -1 ||
      name.indexOf("serp") !== -1)
    return { dest: "02_PROJETS/schoolsWP/03_SEO", confidence: 65, category: "SEO" };

  // Affiliation / Monetisation
  if (name.indexOf("affiliation") !== -1 || name.indexOf("affiliate") !== -1 ||
      name.indexOf("monetis") !== -1 || name.indexOf("smma") !== -1)
    return { dest: "02_PROJETS/schoolsWP/06_Monetisation/01_Affiliation", confidence: 65, category: "Affiliation" };

  // WordPress / Plugin (mot large, confiance plus basse)
  if (name.indexOf("wordpress") !== -1 || name.indexOf("plugin") !== -1 ||
      name.indexOf("elementor") !== -1 || name.indexOf("gutenberg") !== -1 ||
      name.indexOf("woocommerce") !== -1 || name.indexOf("wp ") !== -1)
    return { dest: "03_RESSOURCES/05_Outils-Documentation", confidence: 60, category: "WordPress/Plugin" };

  // Automation
  if (name.indexOf("automation") !== -1 || name.indexOf("n8n") !== -1 ||
      name.indexOf("make") !== -1 || name.indexOf("zapier") !== -1 ||
      name.indexOf("pabbly") !== -1 || name.indexOf("workflow") !== -1)
    return { dest: "02_PROJETS/schoolsWP/05_Automations", confidence: 65, category: "Automation" };

  // Formations / Ebooks
  if (name.indexOf("formation") !== -1 || name.indexOf("cours") !== -1 ||
      name.indexOf("ebook") !== -1 || name.indexOf("e-book") !== -1 ||
      name.indexOf("training") !== -1)
    return { dest: "03_RESSOURCES/04_Methodes", confidence: 60, category: "Formation" };

  // Landing / Conversion / Funnel
  if (name.indexOf("landing") !== -1 || name.indexOf("conversion") !== -1 ||
      name.indexOf("funnel") !== -1 || name.indexOf("tunnel") !== -1)
    return { dest: "PROMPTS_schoolsWP/02_TEMPLATES/03_Conversion_Landing", confidence: 65, category: "Conversion" };

  // Social media par nom
  if (name.indexOf("instagram") !== -1 || name.indexOf("youtube") !== -1 ||
      name.indexOf("twitter") !== -1 || name.indexOf("facebook") !== -1 ||
      name.indexOf("linkedin") !== -1 || name.indexOf("pinterest") !== -1 ||
      name.indexOf("tiktok") !== -1)
    return { dest: "02_PROJETS/schoolsWP/04_Assets", confidence: 60, category: "Social Media" };

  // Images par defaut -> assets
  if (mime.indexOf("image") !== -1)
    return { dest: "02_PROJETS/schoolsWP/04_Assets/04_Illustrations", confidence: 55, category: "Image" };

  // PDF -> ressources
  if (mime.indexOf("pdf") !== -1 || name.indexOf(".pdf") !== -1)
    return { dest: "03_RESSOURCES", confidence: 50, category: "PDF" };

  // Contenu IA / SEO (noms frequents dans le vrac)
  if (name.indexOf("contenu") !== -1 || name.indexOf("content") !== -1 ||
      name.indexOf("ia ") !== -1 || name.indexOf("ai ") !== -1)
    return { dest: "03_RESSOURCES/05_Outils-Documentation", confidence: 55, category: "Contenu IA" };

  // Default -> inspirations
  return { dest: "03_RESSOURCES/06_Inspirations", confidence: 50, category: "Non classifie" };
}

// ══════════════════════════════════════════════════════════════
// PROPOSITION DE NOMS (convention AAAA-MM-JJ - Sujet - Type)
// ══════════════════════════════════════════════════════════════

/**
 * Propose un nouveau nom selon la convention de nommage.
 * Si le fichier a deja une date en prefixe, on garde tel quel.
 */
function proposeArchiveName_(file, classification) {
  var name = file.name || "";

  // Si le nom a deja une date AAAA-MM-JJ, garder tel quel
  if (/^\d{4}-\d{2}-\d{2}/.test(name)) return name;

  // Date de creation comme prefixe
  var dateStr = file.created ? file.created.substring(0, 10) : "2025-01-01";

  // Extension
  var extMatch = name.match(/\.([^.]+)$/);
  var ext = extMatch ? "." + extMatch[1] : "";
  var isGoogleNative = (file.mimeType || "").indexOf("application/vnd.google-apps.") === 0;
  if (isGoogleNative) ext = "";

  // Nettoyer le sujet
  var subject = name
    .replace(/^\d+\.\s*/, "")     // Retirer numero d'article (ex: "104. ")
    .replace(/\.[^.]+$/, "")      // Retirer extension
    .replace(/ - /g, " ")
    .replace(/_/g, " ")
    .trim();

  // Capitaliser premiere lettre
  if (subject) {
    subject = subject.charAt(0).toUpperCase() + subject.slice(1);
  }

  // Tronquer si trop long (max 80 car pour le sujet)
  if (subject.length > 80) {
    subject = subject.substring(0, 77) + "...";
  }

  // Type selon la categorie
  var type = "";
  var cat = classification.category;
  if (cat === "Article EN") type = "Article \u2013 EN";
  else if (cat === "Article DE") type = "Article \u2013 DE";
  else if (cat === "Article FR") type = "Article \u2013 FR";
  else if (cat === "Article MK") type = "Article \u2013 FR";
  else if (cat === "Cover") type = "Cover article";
  else if (cat === "Pinterest") type = "Thumbnail Pinterest";
  else if (cat === "Audio") type = "Audio";
  else if (cat === "Template") type = "Template";
  else if (cat === "Prompt") type = "Prompt";
  else if (cat === "Checklist") type = "Checklist";
  else if (cat === "Email/CRM") type = "Template Email";
  else if (cat === "SEO") type = "SEO";
  else if (cat === "Affiliation") type = "Affiliation";
  else type = "Ressource";

  var newName = dateStr + " \u2013 " + subject + " \u2013 " + type;
  if (ext) newName += ext;

  return newName;
}

// ══════════════════════════════════════════════════════════════
// EXECUTION MIGRATION 06_archive (par lots, safe)
// ══════════════════════════════════════════════════════════════

/**
 * Execute la migration des fichiers de 06_archive selon le Sheet valide.
 * Traite les lignes avec "OUI" en colonne 8 (Valide).
 * S'arrete a 5 min et peut etre relance.
 * Executuer : executeArchiveMigration()
 */
function executeArchiveMigration() {
  Logger.log("=== MIGRATION 06_archive (par lots) ===");
  var startTime = new Date();

  // Ouvrir le Sheet
  var sheetFiles = DriveApp.getFilesByName(ARCHIVE_MAPPING_SHEET);
  if (!sheetFiles.hasNext()) {
    Logger.log("ERREUR : Sheet non trouve ! Executer classifyArchive() d'abord.");
    return;
  }

  var ss = SpreadsheetApp.open(sheetFiles.next());
  var sheet = ss.getSheetByName("Mapping");
  var data = sheet.getDataRange().getValues();

  var moved = 0;
  var renamed = 0;
  var skipped = 0;
  var errors = 0;
  var alreadyDone = 0;

  // Colonnes: 0:ID, 1:Nom actuel, 2:Chemin, 3:Categorie,
  //           4:Destination, 5:Nouveau nom, 6:Confiance, 7:Valide, 8:Notes
  for (var i = 1; i < data.length; i++) {
    // Timeout check (290s = ~4min50, marge de securite)
    if ((new Date() - startTime) / 1000 > 290) {
      Logger.log("[TIMEOUT] Arret a ~5 min. Ligne " + i + "/" + (data.length - 1));
      Logger.log("Relancer executeArchiveMigration() pour continuer.");
      break;
    }

    var row = data[i];
    var fileId = String(row[0]);
    var oldName = String(row[1]);
    var destination = String(row[4]);
    var newName = String(row[5]);
    var validated = String(row[7]).toUpperCase().trim();
    var notes = String(row[8]);

    // Skip deja traite
    if (notes.indexOf("[DONE]") !== -1) { alreadyDone++; continue; }

    // Skip non valide
    if (validated !== "OUI") { skipped++; continue; }

    try {
      var file = DriveApp.getFileById(fileId);

      // 1. Renommer si necessaire
      if (newName && newName !== oldName) {
        file.setName(newName);
        renamed++;
      }

      // 2. Deplacer vers le dossier destination
      if (destination) {
        var targetFolder = navigateFromRoot_(destination);
        if (targetFolder) {
          file.moveTo(targetFolder);
          moved++;
        }
      }

      // Marquer comme traite
      sheet.getRange(i + 1, 9).setValue("[DONE] " + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd"));

    } catch (e) {
      Logger.log("[ERREUR] " + oldName + " : " + e.message);
      sheet.getRange(i + 1, 9).setValue("[ERREUR] " + e.message);
      errors++;
    }

    // Anti-rate-limiting toutes les 50 operations
    if (i % 50 === 0) {
      Utilities.sleep(1000);
      Logger.log("  Progression : " + i + "/" + (data.length - 1));
    }
  }

  var duration = (new Date() - startTime) / 1000;

  Logger.log("");
  Logger.log("=========================================");
  Logger.log("RAPPORT MIGRATION 06_archive");
  Logger.log("=========================================");
  Logger.log("Deplaces     : " + moved);
  Logger.log("Renommes     : " + renamed);
  Logger.log("Ignores      : " + skipped);
  Logger.log("Deja traites : " + alreadyDone);
  Logger.log("Erreurs      : " + errors);
  Logger.log("Duree        : " + duration + "s");
  Logger.log("=========================================");

  if (moved > 0 || errors > 0) {
    Logger.log("");
    Logger.log("Si erreurs ou timeout : relancer executeArchiveMigration()");
    Logger.log("Les lignes [DONE] ne seront pas re-traitees.");
  }
}

// ══════════════════════════════════════════════════════════════
// DEPLACEMENT PHOTOS -> 07_personnel
// ══════════════════════════════════════════════════════════════

/**
 * Deplace le dossier Photos vers 07_personnel (a la racine du Drive).
 * Cree 07_personnel s'il n'existe pas.
 * Executuer : movePhotosToPersonnel()
 */
function movePhotosToPersonnel() {
  Logger.log("=== DEPLACEMENT Photos -> 07_personnel ===");
  var root = DriveApp.getRootFolder();

  // Trouver ou creer 07_personnel
  var persIter = root.getFoldersByName("07_personnel");
  var persFolder;
  if (persIter.hasNext()) {
    persFolder = persIter.next();
    Logger.log("[EXISTE] 07_personnel");
  } else {
    persFolder = root.createFolder("07_personnel");
    Logger.log("[CREE] 07_personnel");
  }

  // Trouver Photos
  var photosIter = root.getFoldersByName("Photos");
  if (!photosIter.hasNext()) {
    Logger.log("ERREUR : dossier Photos non trouve");
    return;
  }
  var photosFolder = photosIter.next();

  // Deplacer Photos dans 07_personnel
  try {
    photosFolder.moveTo(persFolder);
    Logger.log("[DEPLACE] Photos -> 07_personnel/Photos");
  } catch (e) {
    // Fallback : utiliser Drive API avancee
    Logger.log("moveTo non disponible, essai via Drive API...");
    try {
      Drive.Files.update({}, photosFolder.getId(), null, {
        addParents: persFolder.getId(),
        removeParents: root.getId()
      });
      Logger.log("[DEPLACE via API] Photos -> 07_personnel/Photos");
    } catch (e2) {
      Logger.log("[ERREUR] " + e2.message);
      Logger.log("Verifier que le service Drive API est active dans Apps Script.");
    }
  }
  Logger.log("URL 07_personnel : " + persFolder.getUrl());
}

// ══════════════════════════════════════════════════════════════
// CORRECTION : Dossiers avec noms trop longs (Service error: Drive)
// ══════════════════════════════════════════════════════════════

/**
 * Trouve et raccourcit les noms de dossiers trop longs dans 06_archive.
 * Les erreurs "Service error: Drive" viennent de chemins > ~400 car.
 * Cette fonction parcourt 06_archive et renomme les dossiers dont
 * le nom depasse MAX_FOLDER_NAME_LENGTH caracteres.
 *
 * Executuer : fixLongFolderNames()
 */
var MAX_FOLDER_NAME_LENGTH = 60;

function fixLongFolderNames() {
  Logger.log("=== FIX LONG FOLDER NAMES ===");
  var startTime = new Date();
  var root = DriveApp.getRootFolder();

  var archiveIter = root.getFoldersByName("06_archive");
  if (!archiveIter.hasNext()) {
    Logger.log("ERREUR : 06_archive non trouve");
    return;
  }
  var archiveFolder = archiveIter.next();

  var fixed = 0;
  var scanned = 0;
  var errors = 0;

  fixLongNamesRecursive_(archiveFolder, "", function(result) {
    fixed += result.fixed;
    scanned += result.scanned;
    errors += result.errors;
  }, startTime);

  Logger.log("");
  Logger.log("=========================================");
  Logger.log("RAPPORT FIX NOMS LONGS");
  Logger.log("=========================================");
  Logger.log("Dossiers scannes : " + scanned);
  Logger.log("Renommes         : " + fixed);
  Logger.log("Erreurs          : " + errors);
  Logger.log("Duree            : " + ((new Date() - startTime) / 1000) + "s");
  Logger.log("=========================================");

  if (fixed > 0) {
    Logger.log("");
    Logger.log(">>> Relancer fullDriveIndex() pour re-indexer.");
  }
}

/**
 * Parcours recursif pour trouver et renommer les dossiers trop longs.
 */
function fixLongNamesRecursive_(folder, path, callback, startTime) {
  var result = { fixed: 0, scanned: 0, errors: 0 };

  // Timeout de securite a 4 min
  if ((new Date() - startTime) / 1000 > 240) {
    Logger.log("[TIMEOUT] Arret de securite. Relancer fixLongFolderNames().");
    callback(result);
    return;
  }

  try {
    var subFolders = folder.getFolders();
    while (subFolders.hasNext()) {
      var sub = subFolders.next();
      var name = sub.getName();
      result.scanned++;

      if (name.length > MAX_FOLDER_NAME_LENGTH) {
        var newName = shortenFolderName_(name);
        try {
          Logger.log("[RENAME] " + name.substring(0, 80) + "...");
          Logger.log("      -> " + newName);
          sub.setName(newName);
          result.fixed++;
        } catch (renameErr) {
          Logger.log("[ERREUR RENAME] " + renameErr.message);
          result.errors++;
        }
      }

      // Recursion dans les sous-dossiers
      var currentPath = path ? path + "/" + sub.getName() : sub.getName();
      fixLongNamesRecursive_(sub, currentPath, function(childResult) {
        result.fixed += childResult.fixed;
        result.scanned += childResult.scanned;
        result.errors += childResult.errors;
      }, startTime);
    }
  } catch (e) {
    Logger.log("[ERREUR] " + path + " : " + e.message);
    result.errors++;
  }

  callback(result);
}

/**
 * Raccourcit un nom de dossier en gardant le numero d'article
 * et les premiers mots du titre.
 *
 * "110. FluentCommunity Bauen Sie mit diesem Plugin schnell eine WordPress-Community auf"
 * -> "110. FluentCommunity Bauen Sie mit diesem Plugin"
 *
 * "11. Ce qu'il faut savoir sur la plateforme 5euros.com"
 * -> "11. Ce qu il faut savoir sur la plateforme"
 */
function shortenFolderName_(name) {
  // Nettoyer les caracteres problematiques pour Drive API
  var cleaned = name
    .replace(/['']/g, " ")
    .replace(/[""]/g, " ")
    .replace(/\s+/g, " ")
    .trim();

  // Si le nom commence par un numero d'article (ex: "110. ")
  var numMatch = cleaned.match(/^(\d+\.\s*)/);
  var prefix = numMatch ? numMatch[1] : "";
  var rest = numMatch ? cleaned.substring(prefix.length) : cleaned;

  // Garder les N premiers mots pour rester sous la limite
  var words = rest.split(" ");
  var shortened = prefix;
  for (var i = 0; i < words.length; i++) {
    var candidate = shortened + words[i];
    if (candidate.length > MAX_FOLDER_NAME_LENGTH - 3) break;
    shortened = candidate + " ";
  }

  return shortened.trim();
}
