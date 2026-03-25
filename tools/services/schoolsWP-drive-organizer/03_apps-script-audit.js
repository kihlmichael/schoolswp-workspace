/**
 * =============================================================
 * schoolsWP – Google Drive Audit & Migration Script  v2.0
 * =============================================================
 *
 * OBJECTIF : Auditer les fichiers existants dans PROMPTS_schoolsWP,
 * détecter les anomalies, proposer un mapping de migration,
 * exécuter la migration, et générer un index dual (Sheet + Markdown).
 *
 * RÈGLES INTÉGRÉES (sources : 5 Google Docs de référence) :
 * - Nomenclature : AAAA-MM-JJ – Sujet – Type – Usage – Infos.ext
 * - Séparateur unique : " – " (tiret long \u2013 avec espaces)
 * - FR systématique pour Sujet/Type/Usage, EN autorisé dans Infos
 * - Email/CRM anti-fourre-tout :
 *     Templates réutilisables → 02_TEMPLATES/02_Email_CRM_FluentCRM
 *     Prompts one-shot datés  → 03_PROMPTS/02_Email_CRM
 *     Séquences monétisation  → 05_MONETISATION/04_Sequences_Email
 * - Variantes (V1/V2/FR/EN/Court/Long) = déclinaisons, pas doublons
 * - Statut géré par DOSSIER (01_DRAFT/02_VALIDÉ/03_LIVE/99_ARCHIVES)
 * - Zéro suppression : doublons → 99_ARCHIVES, backup avant migration
 *
 * MODE D'EMPLOI :
 * 1. Ce fichier va dans le même projet Apps Script que 02_apps-script-structure.js
 * 2. Créer un nouveau fichier script : AuditMigration.gs
 * 3. Coller ce code
 * 4. Exécuter dans l'ordre strict :
 *    a) runAudit()              → inventaire + détection anomalies
 *    b) generateMapping()       → tableau dry-run dans un Google Sheet
 *    c) [VALIDATION HUMAINE]    → vérifier le Sheet, mettre OUI/NON
 *    d) executeMigration()      → exécution safe (uniquement lignes OUI)
 *    e) generateGlobalIndex()   → Google Sheet + miroir Markdown
 *
 * =============================================================
 */

// ══════════════════════════════════════════════════════════════
// CONFIGURATION
// ══════════════════════════════════════════════════════════════

/**
 * ID du dossier SOURCE (PROMPTS_schoolsWP existant à auditer/migrer).
 * Michaël KIHL – copié depuis l'URL Drive.
 */
const SOURCE_FOLDER_ID = "1O_GbYXkAnnsix1Gowuv7EuvXL5qRdS_N";

/**
 * ID du dossier cible PROMPTS_schoolsWP (après création par createFullStructure).
 * null = le script cherche PROMPTS_schoolsWP à la racine du Drive.
 * Si c'est le MÊME dossier que la source (réorg in-place), mettre le même ID.
 */
const TARGET_ROOT_ID = null;

/**
 * Nom du Google Sheet de mapping (créé automatiquement)
 */
const MAPPING_SHEET_NAME = "schoolsWP \u2013 Mapping Migration";

/**
 * Nom du Google Sheet d'index global
 */
const INDEX_SHEET_NAME = "schoolsWP \u2013 Index Global";

// ══════════════════════════════════════════════════════════════
// RÉFÉRENTIELS DE NOMMAGE (sources : Doc 1 + Doc 2)
// ══════════════════════════════════════════════════════════════

/**
 * Types valides (bloc "Type" du nom de fichier)
 * Source : Doc 1 §3 + Doc 2 §4.2
 */
const VALID_TYPES = [
  "Prompt", "Template", "SOP", "Brief", "Checklist", "Audit"
];

/**
 * Types éditoriaux élargis (Doc 2 §4.2 – pour détection intelligente)
 * Ces types sont utilisés dans le Drive global mais pas dans PROMPTS_schoolsWP.
 * Le script les mappe vers les types VALID_TYPES appropriés.
 */
const EDITORIAL_TYPES_MAP = {
  "article": "Prompt",
  "tutoriel": "Prompt",
  "guide": "Template",
  "video": "Prompt",
  "vidéo": "Prompt",
  "newsletter": "Prompt",
  "note": "Brief"
};

/**
 * Usages valides (bloc "Usage" du nom de fichier)
 * Source : Doc 1 §3
 */
const VALID_USAGES = [
  "Article", "SEO", "Email", "Landing", "Affiliation",
  "Ads", "YouTube", "Social", "Asset", "Automation", "ADMIN"
];

/**
 * Leviers monétisation (Doc 2 §4.5) – pour router vers 05_MONETISATION
 */
const MONETISATION_KEYWORDS = [
  "lancement", "promo", "evergreen", "séquence", "sequence",
  "campagne", "black friday", "soldes", "offre", "formation",
  "produit", "business", "partenariat"
];

/**
 * Keywords Email/CRM pour classification anti-fourre-tout
 */
const EMAIL_KEYWORDS = [
  "email", "mail", "crm", "fluent", "fluentcrm",
  "newsletter", "séquence", "sequence", "welcome",
  "onboarding", "relance", "nurturing", "drip"
];

/**
 * Extensions recommandées (Doc 1 §3)
 */
const VALID_EXTENSIONS = ["md", "docx", "txt", "json", "pdf", "xlsx", "py", "js"];

/**
 * Séparateur universel (tiret long avec espaces)
 */
const SEP = " \u2013 ";

/**
 * Regex de validation du format de nom complet
 * AAAA-MM-JJ – Sujet – Type – Usage [– Infos].ext
 */
const NAME_REGEX = /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 (Prompt|Template|SOP|Brief|Checklist|Audit) \u2013 (Article|SEO|Email|Landing|Affiliation|Ads|YouTube|Social|Asset|Automation|ADMIN)/;

// ══════════════════════════════════════════════════════════════
// 1. AUDIT
// ══════════════════════════════════════════════════════════════

/**
 * Exécute l'audit complet du dossier source.
 * Produit un inventaire détaillé avec anomalies classées par sévérité.
 */
function runAudit() {
  Logger.log("=== AUDIT v2.0 - schoolsWP Drive ===");
  const startTime = new Date();

  const sourceFolder = DriveApp.getFolderById(SOURCE_FOLDER_ID);
  Logger.log("Dossier source : " + sourceFolder.getName());
  Logger.log("ID : " + SOURCE_FOLDER_ID);

  // Collecter tous les fichiers récursivement
  const allFiles = [];
  collectFilesRecursive_(sourceFolder, "", allFiles);

  Logger.log("Fichiers trouves : " + allFiles.length);

  // Analyser chaque fichier
  const anomalies = {
    noDate: [],
    badSeparator: [],
    noType: [],
    noUsage: [],
    badExtension: [],
    duplicates: [],
    misplacedEmail: [],
    misplacedMonetisation: [],
    misplacedGeneral: []
  };

  // Grouper par sujet normalisé pour détecter les doublons
  // MAIS : V1/V2/FR/EN/Court/Long = déclinaisons légitimes (Doc 1 §1)
  const filesBySubject = {};

  for (const file of allFiles) {
    const analysis = analyzeFileName_(file.name, file.path);
    file.analysis = analysis;

    if (!analysis.hasDate) anomalies.noDate.push(file);
    if (analysis.hasBadSeparator) anomalies.badSeparator.push(file);
    if (!analysis.hasType) anomalies.noType.push(file);
    if (!analysis.hasUsage) anomalies.noUsage.push(file);
    if (analysis.hasBadExtension) anomalies.badExtension.push(file);

    // Détecter fichiers Email/CRM mal rangés (anti-fourre-tout)
    if (analysis.emailClassification && analysis.emailClassification.misplaced) {
      anomalies.misplacedEmail.push({
        file: file,
        currentPath: file.path,
        shouldBe: analysis.emailClassification.correctFolder,
        reason: analysis.emailClassification.reason
      });
    }

    // Détecter fichiers monétisation mal rangés
    if (analysis.monetisationMisplaced) {
      anomalies.misplacedMonetisation.push(file);
    }

    // Doublons : même sujet normalisé SANS variantes
    const normalizedKey = normalizeForDuplicates_(file.name);
    if (!filesBySubject[normalizedKey]) {
      filesBySubject[normalizedKey] = [];
    }
    filesBySubject[normalizedKey].push(file);
  }

  // Identifier les vrais doublons (même fonction, pas juste variantes)
  for (const [key, files] of Object.entries(filesBySubject)) {
    if (files.length > 1) {
      // Vérifier si ce sont des variantes légitimes ou des vrais doublons
      const variants = detectVariants_(files);
      if (variants.hasTrueDuplicates) {
        anomalies.duplicates.push({
          subject: key,
          files: files.map(f => ({ name: f.name, path: f.path, id: f.id })),
          count: files.length,
          variants: variants.variantGroups,
          trueDuplicates: variants.trueDuplicates
        });
      }
    }
  }

  // Rapport d'audit détaillé
  Logger.log("");
  Logger.log("=== RAPPORT D'AUDIT ===");
  Logger.log("Total fichiers             : " + allFiles.length);
  Logger.log("Sans date                  : " + anomalies.noDate.length);
  Logger.log("Mauvais separateurs        : " + anomalies.badSeparator.length);
  Logger.log("Sans type                  : " + anomalies.noType.length);
  Logger.log("Sans usage                 : " + anomalies.noUsage.length);
  Logger.log("Extension non standard     : " + anomalies.badExtension.length);
  Logger.log("Email/CRM mal ranges       : " + anomalies.misplacedEmail.length);
  Logger.log("Monetisation mal ranges    : " + anomalies.misplacedMonetisation.length);
  Logger.log("Groupes doublons           : " + anomalies.duplicates.length);
  Logger.log("");

  // Lister les anomalies Email/CRM en détail (important pour Michaël)
  if (anomalies.misplacedEmail.length > 0) {
    Logger.log("--- DETAIL Email/CRM mal ranges ---");
    for (const item of anomalies.misplacedEmail) {
      Logger.log("  " + item.file.name);
      Logger.log("    Actuel  : " + item.currentPath);
      Logger.log("    Correct : " + item.shouldBe);
      Logger.log("    Raison  : " + item.reason);
    }
  }

  // Stocker pour la phase mapping
  const props = PropertiesService.getScriptProperties();
  // PropertiesService a une limite de 9KB par propriété.
  // Pour les gros volumes, on chunke.
  storeAuditData_(props, allFiles, anomalies);

  const duration = (new Date() - startTime) / 1000;
  Logger.log("Duree audit : " + duration + "s");

  return { files: allFiles, anomalies: anomalies };
}

/**
 * Stocke les données d'audit en chunks si nécessaire
 */
function storeAuditData_(props, files, anomalies) {
  const filesJson = JSON.stringify(files);
  const anomaliesJson = JSON.stringify(anomalies);

  // PropertiesService : 9KB par clé, 500KB total
  if (filesJson.length > 8000) {
    // Chunker les fichiers
    const chunks = chunkString_(filesJson, 8000);
    props.setProperty("audit_files_chunks", chunks.length.toString());
    for (let i = 0; i < chunks.length; i++) {
      props.setProperty("audit_files_" + i, chunks[i]);
    }
  } else {
    props.setProperty("audit_files_chunks", "0");
    props.setProperty("audit_files", filesJson);
  }

  props.setProperty("audit_anomalies", anomaliesJson);
  Logger.log("Donnees d'audit sauvegardees (" + files.length + " fichiers)");
}

/**
 * Récupère les données d'audit stockées
 */
function loadAuditData_() {
  const props = PropertiesService.getScriptProperties();
  const chunks = parseInt(props.getProperty("audit_files_chunks") || "0");

  let filesJson;
  if (chunks > 0) {
    const parts = [];
    for (let i = 0; i < chunks; i++) {
      parts.push(props.getProperty("audit_files_" + i));
    }
    filesJson = parts.join("");
  } else {
    filesJson = props.getProperty("audit_files");
  }

  const anomaliesJson = props.getProperty("audit_anomalies");

  if (!filesJson) return null;

  return {
    files: JSON.parse(filesJson),
    anomalies: anomaliesJson ? JSON.parse(anomaliesJson) : null
  };
}

/**
 * Découpe une chaîne en chunks
 */
function chunkString_(str, size) {
  const chunks = [];
  for (let i = 0; i < str.length; i += size) {
    chunks.push(str.substring(i, i + size));
  }
  return chunks;
}

/**
 * Collecte récursive de tous les fichiers
 */
function collectFilesRecursive_(folder, path, results) {
  const currentPath = path ? path + "/" + folder.getName() : folder.getName();

  const files = folder.getFiles();
  while (files.hasNext()) {
    const file = files.next();
    // Ignorer les fichiers Google Docs natifs de type "dossier" ou raccourcis
    const mime = file.getMimeType();
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
  }

  const subFolders = folder.getFolders();
  while (subFolders.hasNext()) {
    const sub = subFolders.next();
    // Ignorer les dossiers de backup existants
    if (sub.getName().startsWith("_BACKUP")) continue;
    collectFilesRecursive_(sub, currentPath, results);
  }
}

/**
 * Analyse complète d'un nom de fichier selon TOUTES les règles
 */
function analyzeFileName_(name, filePath) {
  const analysis = {
    hasDate: false,
    hasType: false,
    hasUsage: false,
    hasBadSeparator: false,
    hasBadExtension: false,
    hasCorrectFormat: false,
    detectedDate: null,
    detectedType: null,
    detectedUsage: null,
    detectedInfos: null,
    emailClassification: null,
    monetisationMisplaced: false,
    isVariant: false,
    variantMarkers: [],
    severity: "OK",
    issues: []
  };

  // ── 1. Date ──
  const dateMatch = name.match(/^(\d{4}-\d{2}-\d{2})/);
  if (dateMatch) {
    analysis.hasDate = true;
    analysis.detectedDate = dateMatch[1];
    // Valider que la date est réaliste
    const year = parseInt(dateMatch[1].substring(0, 4));
    if (year < 2020 || year > 2030) {
      analysis.issues.push("Date suspecte : " + dateMatch[1]);
    }
  } else {
    analysis.issues.push("Date manquante en debut de nom");
  }

  // ── 2. Séparateur ──
  const hasTiretLong = name.includes(SEP);
  const hasTiretCourt = / - /.test(name);
  const hasDoubleUnderscore = name.includes("__");
  // Underscores simples dans les noms de dossier (ex: 01_ADMIN) sont OK
  // Mais dans un NOM DE FICHIER, on veut le tiret long
  const hasSuspectUnderscore = /_/.test(name) && !hasTiretLong;

  if (hasTiretCourt || hasDoubleUnderscore || hasSuspectUnderscore) {
    analysis.hasBadSeparator = true;
    const badTypes = [];
    if (hasTiretCourt) badTypes.push("tiret court \" - \"");
    if (hasDoubleUnderscore) badTypes.push("double underscore \"__\"");
    if (hasSuspectUnderscore) badTypes.push("underscore \"_\" au lieu de tiret long");
    analysis.issues.push("Mauvais separateur : " + badTypes.join(", "));
  }

  // ── 3. Type ──
  for (const type of VALID_TYPES) {
    // Chercher le type après un séparateur
    const typeRegex = new RegExp("[\u2013\\-_]\\s*" + type + "\\s*[\u2013\\-_.]", "i");
    if (typeRegex.test(name) || name.includes(SEP + type + SEP) || name.includes(SEP + type + ".")) {
      analysis.hasType = true;
      analysis.detectedType = type;
      break;
    }
  }

  // Fallback : détecter les types éditoriaux (Doc 2) et les mapper
  if (!analysis.hasType) {
    const nameLower = name.toLowerCase();
    for (const [editType, mappedType] of Object.entries(EDITORIAL_TYPES_MAP)) {
      if (nameLower.includes(editType)) {
        analysis.hasType = true;
        analysis.detectedType = mappedType;
        analysis.issues.push("Type editorial '" + editType + "' mappe vers " + mappedType);
        break;
      }
    }
  }

  if (!analysis.hasType) {
    analysis.issues.push("Type non detecte (attendu : " + VALID_TYPES.join(", ") + ")");
  }

  // ── 4. Usage ──
  for (const usage of VALID_USAGES) {
    const usageRegex = new RegExp("[\u2013\\-_]\\s*" + usage + "\\s*[\u2013\\-_.]", "i");
    if (usageRegex.test(name) || name.includes(SEP + usage + SEP) || name.includes(SEP + usage + ".")) {
      analysis.hasUsage = true;
      analysis.detectedUsage = usage;
      break;
    }
  }
  if (!analysis.hasUsage) {
    analysis.issues.push("Usage non detecte (attendu : " + VALID_USAGES.join(", ") + ")");
  }

  // ── 5. Extension ──
  const extMatch = name.match(/\.([^.]+)$/);
  if (extMatch) {
    const ext = extMatch[1].toLowerCase();
    if (!VALID_EXTENSIONS.includes(ext)) {
      // Google Docs natifs n'ont pas d'extension visible
      analysis.hasBadExtension = true;
      analysis.issues.push("Extension non standard : ." + ext + " (recommande : " + VALID_EXTENSIONS.join(", ") + ")");
    }
  }

  // ── 6. Variantes (V1/V2/FR/EN/Court/Long) ──
  const variantPatterns = [
    { regex: /\bV(\d+)\b/i, marker: "version" },
    { regex: /\bFR\b/, marker: "FR" },
    { regex: /\bEN\b/, marker: "EN" },
    { regex: /\bDE\b/, marker: "DE" },
    { regex: /\bES\b/, marker: "ES" },
    { regex: /\bCourt\b/i, marker: "Court" },
    { regex: /\bLong\b/i, marker: "Long" }
  ];
  for (const vp of variantPatterns) {
    if (vp.regex.test(name)) {
      analysis.isVariant = true;
      analysis.variantMarkers.push(vp.marker);
    }
  }

  // ── 7. Classification Email/CRM anti-fourre-tout ──
  analysis.emailClassification = classifyEmailCRM_(name, filePath, analysis.detectedType);

  // ── 8. Détection monétisation mal rangée ──
  const nameLower = name.toLowerCase();
  const pathLower = (filePath || "").toLowerCase();
  const isMonetisationContent = MONETISATION_KEYWORDS.some(kw => nameLower.includes(kw));
  if (isMonetisationContent && !pathLower.includes("monetisation") && !pathLower.includes("monétisation")) {
    analysis.monetisationMisplaced = true;
    analysis.issues.push("Contenu monetisation detecte hors dossier MONETISATION");
  }

  // ── 9. Format complet ──
  analysis.hasCorrectFormat = NAME_REGEX.test(name);

  // ── 10. Sévérité ──
  const criticalIssues = analysis.issues.filter(i =>
    i.includes("Date manquante") || i.includes("Type non detecte")
  ).length;
  const mediumIssues = analysis.issues.filter(i =>
    i.includes("Mauvais separateur") || i.includes("Usage non detecte") || i.includes("mal range")
  ).length;

  if (criticalIssues > 0) analysis.severity = "CRITIQUE";
  else if (mediumIssues > 0) analysis.severity = "MOYEN";
  else if (analysis.issues.length > 0) analysis.severity = "MINEUR";

  return analysis;
}

/**
 * Classification Email/CRM anti-fourre-tout (RÈGLE CLÉ)
 *
 * 3 destinations possibles :
 * 1. Template Email réutilisable → 02_TEMPLATES/02_Email_CRM_FluentCRM
 * 2. Prompt Email one-shot daté  → 03_PROMPTS/02_Email_CRM
 * 3. Séquence Email monétisation  → 05_MONETISATION/04_Sequences_Email
 */
function classifyEmailCRM_(name, filePath, detectedType) {
  const nameLower = name.toLowerCase();
  const pathLower = (filePath || "").toLowerCase();

  // Est-ce un fichier Email/CRM ?
  const isEmail = EMAIL_KEYWORDS.some(kw => nameLower.includes(kw));
  if (!isEmail) return null;

  // Déterminer la destination correcte
  let correctFolder = "";
  let reason = "";

  // Cas 3 : Séquence monétisation (lancement/promo/evergreen)
  const isMonetisationSequence = MONETISATION_KEYWORDS.some(kw => nameLower.includes(kw));
  if (isMonetisationSequence) {
    correctFolder = "05_MONETISATION/04_Sequences_Email";
    reason = "Sequence email liee a un dispositif monetisation";
  }
  // Cas 1 : Template réutilisable
  else if (detectedType === "Template" || nameLower.includes("template")) {
    correctFolder = "02_TEMPLATES/02_Email_CRM_FluentCRM";
    reason = "Template email reutilisable";
  }
  // Cas 2 : Prompt one-shot daté (défaut pour les emails)
  else {
    correctFolder = "03_PROMPTS/02_Email_CRM";
    reason = "Prompt email one-shot date";
  }

  // Vérifier si le fichier est déjà bien rangé
  const isCorrectlyPlaced = pathLower.includes(correctFolder.toLowerCase().replace(/\//g, "/"));
  // Fallback : vérifier les parties clés du chemin
  const pathParts = correctFolder.split("/");
  const isCorrectByParts = pathParts.every(part =>
    pathLower.includes(part.toLowerCase())
  );

  return {
    isEmail: true,
    correctFolder: correctFolder,
    reason: reason,
    misplaced: !isCorrectlyParts_(pathLower, correctFolder),
    currentPath: filePath
  };
}

/**
 * Vérifie si un chemin contient les éléments clés du dossier cible
 */
function isCorrectlyParts_(pathLower, correctFolder) {
  // Extraire le dernier segment significatif du chemin cible
  const parts = correctFolder.split("/");
  const lastPart = parts[parts.length - 1].toLowerCase();
  return pathLower.includes(lastPart);
}

/**
 * Normalise un nom pour la détection de doublons.
 * RETIRE les variantes (V1/V2/FR/EN/Court/Long) qui sont des déclinaisons légitimes.
 */
function normalizeForDuplicates_(name) {
  return name
    .replace(/^\d{4}-\d{2}-\d{2}/, "")           // Retirer la date
    .replace(/\.[^.]+$/, "")                       // Retirer l'extension
    .replace(/[\u2013\-_]/g, " ")                  // Normaliser séparateurs
    .replace(/\s+/g, " ")                          // Normaliser espaces
    .replace(/\b(V\d+|FR|EN|DE|ES|Court|Long)\b/gi, "")  // Retirer variantes
    .replace(/\b(Prompt|Template|SOP|Brief|Checklist|Audit)\b/gi, "")  // Retirer types
    .replace(/\b(Article|SEO|Email|Landing|Affiliation|Ads|YouTube|Social|Asset|Automation|ADMIN)\b/gi, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

/**
 * Analyse un groupe de fichiers au même sujet normalisé.
 * Distingue les variantes légitimes des vrais doublons.
 */
function detectVariants_(files) {
  const result = {
    hasTrueDuplicates: false,
    variantGroups: {},
    trueDuplicates: []
  };

  // Créer une signature plus fine (sujet + type + usage, AVEC variantes)
  const signatures = {};
  for (const file of files) {
    // Signature = nom sans date ni extension, mais AVEC variantes
    const sig = file.name
      .replace(/^\d{4}-\d{2}-\d{2}[\s\u2013\-_]*/, "")
      .replace(/\.[^.]+$/, "")
      .trim()
      .toLowerCase();

    if (!signatures[sig]) {
      signatures[sig] = [];
    }
    signatures[sig].push(file);
  }

  // Si même signature exacte (après retrait date) = vrai doublon
  for (const [sig, sigFiles] of Object.entries(signatures)) {
    if (sigFiles.length > 1) {
      result.hasTrueDuplicates = true;
      result.trueDuplicates.push({
        signature: sig,
        files: sigFiles.map(f => f.name)
      });
    }
  }

  // Grouper les variantes
  for (const file of files) {
    const markers = (file.analysis && file.analysis.variantMarkers) || [];
    const variantKey = markers.length > 0 ? markers.sort().join("+") : "base";
    if (!result.variantGroups[variantKey]) {
      result.variantGroups[variantKey] = [];
    }
    result.variantGroups[variantKey].push(file.name);
  }

  return result;
}

// ══════════════════════════════════════════════════════════════
// 2. MAPPING (DRY-RUN)
// ══════════════════════════════════════════════════════════════

/**
 * Génère le tableau de mapping dans un Google Sheet.
 * C'est le DRY-RUN : aucune modification n'est faite sur le Drive.
 */
function generateMapping() {
  Logger.log("=== GENERATION DU MAPPING (DRY-RUN) ===");

  // Récupérer les données d'audit
  const auditData = loadAuditData_();
  if (!auditData) {
    Logger.log("ERREUR : Executer runAudit() d'abord !");
    return;
  }

  const files = auditData.files;
  const anomalies = auditData.anomalies;

  Logger.log("Fichiers a mapper : " + files.length);

  // Créer ou ouvrir le Google Sheet
  let ss;
  const existingFiles = DriveApp.getFilesByName(MAPPING_SHEET_NAME);
  if (existingFiles.hasNext()) {
    const existingFile = existingFiles.next();
    ss = SpreadsheetApp.open(existingFile);
    Logger.log("Sheet existant : " + existingFile.getUrl());
  } else {
    ss = SpreadsheetApp.create(MAPPING_SHEET_NAME);
    Logger.log("Sheet cree : " + ss.getUrl());
  }

  // ── Onglet MAPPING ──
  let mappingSheet = ss.getSheetByName("Mapping");
  if (!mappingSheet) {
    mappingSheet = ss.insertSheet("Mapping");
  } else {
    mappingSheet.clear();
  }

  const headers = [
    "ID Fichier",
    "Ancien nom",
    "Ancien chemin",
    "Nouveau nom propose",
    "Nouveau chemin propose",
    "Confiance %",
    "Action",
    "Severite",
    "Anomalies detectees",
    "Email/CRM classif.",
    "Valide ? (OUI/NON)",
    "Notes"
  ];
  mappingSheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  mappingSheet.getRange(1, 1, 1, headers.length).setFontWeight("bold");
  mappingSheet.getRange(1, 1, 1, headers.length).setBackground("#1a73e8");
  mappingSheet.getRange(1, 1, 1, headers.length).setFontColor("#ffffff");

  // Remplir les lignes
  const rows = [];
  for (const file of files) {
    const proposal = proposeNewNameAndPath_(file);
    const emailInfo = file.analysis && file.analysis.emailClassification
      ? file.analysis.emailClassification.reason || ""
      : "";

    rows.push([
      file.id,
      file.name,
      file.path,
      proposal.newName,
      proposal.newPath,
      proposal.confidence,
      proposal.action,
      (file.analysis && file.analysis.severity) || "N/A",
      (file.analysis && file.analysis.issues) ? file.analysis.issues.join("; ") : "",
      emailInfo,
      proposal.confidence >= 80 ? "OUI" : "",
      proposal.notes || ""
    ]);
  }

  if (rows.length > 0) {
    mappingSheet.getRange(2, 1, rows.length, headers.length).setValues(rows);
  }

  // Mise en forme conditionnelle : confiance < 80% = rouge
  if (rows.length > 0) {
    const confRange = mappingSheet.getRange(2, 6, rows.length, 1);
    const ruleConf = SpreadsheetApp.newConditionalFormatRule()
      .whenNumberLessThan(80)
      .setBackground("#ffcccc")
      .setRanges([confRange])
      .build();

    // Sévérité CRITIQUE = orange
    const sevRange = mappingSheet.getRange(2, 8, rows.length, 1);
    const ruleSev = SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("CRITIQUE")
      .setBackground("#ff9900")
      .setFontColor("#ffffff")
      .setRanges([sevRange])
      .build();

    mappingSheet.setConditionalFormatRules([ruleConf, ruleSev]);
  }

  // Figer la première ligne
  mappingSheet.setFrozenRows(1);

  // Ajuster les colonnes
  for (let i = 1; i <= headers.length; i++) {
    mappingSheet.autoResizeColumn(i);
  }

  // ── Onglet DOUBLONS ──
  let dupSheet = ss.getSheetByName("Doublons");
  if (!dupSheet) {
    dupSheet = ss.insertSheet("Doublons");
  } else {
    dupSheet.clear();
  }

  const dupHeaders = [
    "Sujet normalise", "Nb fichiers", "Fichiers",
    "Vrais doublons ?", "Variantes detectees"
  ];
  dupSheet.getRange(1, 1, 1, dupHeaders.length).setValues([dupHeaders]);
  dupSheet.getRange(1, 1, 1, dupHeaders.length).setFontWeight("bold");

  if (anomalies && anomalies.duplicates) {
    const dupRows = anomalies.duplicates.map(function(d) {
      return [
        d.subject,
        d.count,
        d.files.map(function(f) { return f.name || f; }).join("\n"),
        d.trueDuplicates ? d.trueDuplicates.map(function(td) { return td.files.join(" | "); }).join("\n") : "Non",
        d.variants ? Object.keys(d.variants).join(", ") : ""
      ];
    });

    if (dupRows.length > 0) {
      dupSheet.getRange(2, 1, dupRows.length, dupHeaders.length).setValues(dupRows);
    }
  }

  // ── Onglet EMAIL/CRM ──
  let emailSheet = ss.getSheetByName("Email-CRM");
  if (!emailSheet) {
    emailSheet = ss.insertSheet("Email-CRM");
  } else {
    emailSheet.clear();
  }

  const emailHeaders = [
    "Fichier", "Chemin actuel", "Classification",
    "Dossier correct", "Mal range ?", "Action"
  ];
  emailSheet.getRange(1, 1, 1, emailHeaders.length).setValues([emailHeaders]);
  emailSheet.getRange(1, 1, 1, emailHeaders.length).setFontWeight("bold");
  emailSheet.getRange(1, 1, 1, emailHeaders.length).setBackground("#34a853");
  emailSheet.getRange(1, 1, 1, emailHeaders.length).setFontColor("#ffffff");

  const emailRows = [];
  for (const file of files) {
    if (file.analysis && file.analysis.emailClassification && file.analysis.emailClassification.isEmail) {
      const ec = file.analysis.emailClassification;
      emailRows.push([
        file.name,
        file.path,
        ec.reason,
        ec.correctFolder,
        ec.misplaced ? "OUI - A DEPLACER" : "OK",
        ec.misplaced ? "MOVE" : "OK"
      ]);
    }
  }
  if (emailRows.length > 0) {
    emailSheet.getRange(2, 1, emailRows.length, emailHeaders.length).setValues(emailRows);
  }

  // ── Onglet RESUME ──
  let summarySheet = ss.getSheetByName("Resume");
  if (!summarySheet) {
    summarySheet = ss.insertSheet("Resume");
  } else {
    summarySheet.clear();
  }

  const summaryData = [
    ["Metrique", "Valeur"],
    ["Total fichiers", files.length],
    ["Format correct", rows.filter(function(r) { return r[6] === "OK"; }).length],
    ["A renommer", rows.filter(function(r) { return r[6] === "RENAME" || r[6] === "RENAME+MOVE"; }).length],
    ["A deplacer", rows.filter(function(r) { return r[6] === "MOVE" || r[6] === "RENAME+MOVE"; }).length],
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
    ["Confiance >= 80%", rows.filter(function(r) { return r[5] >= 80; }).length],
    ["A valider manuellement", rows.filter(function(r) { return r[5] < 80; }).length],
    ["Severite CRITIQUE", rows.filter(function(r) { return r[7] === "CRITIQUE"; }).length],
    ["Severite MOYEN", rows.filter(function(r) { return r[7] === "MOYEN"; }).length],
    ["", ""],
    ["Date audit", new Date().toISOString()],
    ["Sheet URL", ss.getUrl()]
  ];
  summarySheet.getRange(1, 1, summaryData.length, 2).setValues(summaryData);
  summarySheet.getRange(1, 1, 1, 2).setFontWeight("bold");
  summarySheet.getRange(1, 1, 1, 2).setBackground("#1a73e8");
  summarySheet.getRange(1, 1, 1, 2).setFontColor("#ffffff");

  // Supprimer la feuille par défaut
  const defaultSheet = ss.getSheetByName("Feuille 1") || ss.getSheetByName("Sheet1");
  if (defaultSheet && ss.getSheets().length > 1) {
    ss.deleteSheet(defaultSheet);
  }

  Logger.log("");
  Logger.log("=== MAPPING GENERE ===");
  Logger.log("URL           : " + ss.getUrl());
  Logger.log("Total lignes  : " + rows.length);
  Logger.log("Auto (OUI)    : " + rows.filter(function(r) { return r[10] === "OUI"; }).length);
  Logger.log("A valider     : " + rows.filter(function(r) { return r[10] === ""; }).length);
  Logger.log("");
  Logger.log(">>> PROCHAINE ETAPE : ouvrir le Sheet, verifier, puis executeMigration()");

  return ss.getUrl();
}

/**
 * Propose un nouveau nom et chemin pour un fichier.
 * Respecte strictement les règles de nommage.
 */
function proposeNewNameAndPath_(file) {
  const result = {
    newName: file.name,
    newPath: "",
    confidence: 100,
    action: "OK",
    notes: ""
  };

  const analysis = file.analysis || analyzeFileName_(file.name, file.path);
  let confidence = 100;

  // Extraire l'extension
  const extMatch = file.name.match(/\.([^.]+)$/);
  const ext = extMatch ? extMatch[1] : "";

  // Si Google Doc natif, pas d'extension dans le nom
  const isGoogleNative = file.mimeType && file.mimeType.startsWith("application/vnd.google-apps.");

  // ── Date ──
  let dateStr = analysis.detectedDate;
  if (!dateStr) {
    // Fallback : date de création
    dateStr = file.created ? file.created.substring(0, 10) : Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");
    confidence -= 15;
    result.notes += "Date estimee depuis creation. ";
  }

  // ── Sujet ──
  let subject = extractSubject_(file.name);
  if (!subject || subject.length < 3) {
    // Fallback : nom nettoyé
    subject = file.name
      .replace(/\.[^.]+$/, "")
      .replace(/^\d{4}-\d{2}-\d{2}[\s\u2013\-_]*/, "")
      .replace(/__/g, " ")
      .replace(/_/g, " ")
      .replace(/ - /g, " ")
      .trim();
    confidence -= 10;
  }
  // Capitaliser la première lettre (FR)
  subject = capitalizeFirst_(subject);

  // ── Type ──
  let type = analysis.detectedType;
  if (!type) {
    type = guessType_(file);
    confidence -= 15;
    result.notes += "Type devine : " + type + ". ";
  }

  // ── Usage ──
  let usage = analysis.detectedUsage;
  if (!usage) {
    usage = guessUsage_(file);
    confidence -= 15;
    result.notes += "Usage devine : " + usage + ". ";
  }

  // ── Infos (variantes, langue, etc.) ──
  let infos = "";
  if (analysis.variantMarkers && analysis.variantMarkers.length > 0) {
    infos = analysis.variantMarkers.join("-");
  }

  // ── Construire le nouveau nom ──
  let newName;
  if (analysis.hasCorrectFormat) {
    newName = file.name; // Déjà conforme
  } else {
    // Format : AAAA-MM-JJ – Sujet – Type – Usage [– Infos].ext
    newName = dateStr + SEP + subject + SEP + type + SEP + usage;
    if (infos) {
      newName += SEP + infos;
    }
    if (!isGoogleNative && ext) {
      newName += "." + ext;
    }
    confidence -= 5;
  }

  // Nettoyer les séparateurs si mauvais
  if (analysis.hasBadSeparator && !analysis.hasCorrectFormat) {
    // Déjà reconstruit ci-dessus, pas besoin de re-nettoyer
  }

  // ── Dossier cible ──
  // Priorité Email/CRM anti-fourre-tout
  let targetPath;
  if (analysis.emailClassification && analysis.emailClassification.isEmail) {
    targetPath = "PROMPTS_schoolsWP/" + analysis.emailClassification.correctFolder;
  } else {
    targetPath = determineTargetFolder_(type, usage, file);
  }

  if (!targetPath) {
    confidence -= 20;
    targetPath = "A_DETERMINER";
    result.notes += "Dossier cible incertain. ";
  }

  // ── Action ──
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

  // Seuil de confiance pour auto-validation
  result.newName = newName;
  result.newPath = targetPath;
  result.confidence = Math.max(0, Math.min(100, confidence));

  if (result.confidence < 80) {
    result.action = "A_VALIDER";
  }

  return result;
}

/**
 * Extrait le sujet d'un nom de fichier
 */
function extractSubject_(name) {
  // Retirer la date
  let subject = name.replace(/^\d{4}-\d{2}-\d{2}[\s\u2013\-_]*/, "");
  // Retirer l'extension
  subject = subject.replace(/\.[^.]+$/, "");
  // Retirer les types et usages connus (avec séparateurs)
  for (const t of VALID_TYPES) {
    subject = subject.replace(new RegExp("\\s*[\u2013\\-_]\\s*" + t + "(?=\\s*[\u2013\\-_.]|$)", "gi"), "");
  }
  for (const u of VALID_USAGES) {
    subject = subject.replace(new RegExp("\\s*[\u2013\\-_]\\s*" + u + "(?=\\s*[\u2013\\-_.]|$)", "gi"), "");
  }
  // Retirer les variantes
  subject = subject.replace(/\s*[\u2013\-_]\s*(V\d+|FR|EN|DE|ES|Court|Long)\b/gi, "");
  // Nettoyer
  subject = subject.replace(/[\u2013\-_]+/g, " ").replace(/\s+/g, " ").trim();
  return subject;
}

/**
 * Devine le type si non explicite (enrichi avec Doc 2)
 */
function guessType_(file) {
  var name = file.name.toLowerCase();
  var path = (file.path || "").toLowerCase();

  if (path.includes("template") || name.includes("template")) return "Template";
  if (path.includes("sop") || name.includes("sop") || name.includes("procedure") || name.includes("procédure")) return "SOP";
  if (path.includes("brief") || name.includes("brief")) return "Brief";
  if (path.includes("checklist") || name.includes("checklist") || name.includes("check-list")) return "Checklist";
  if (path.includes("audit") || name.includes("audit")) return "Audit";

  // Types éditoriaux (Doc 2 §4.2) → mappés
  if (name.includes("tutoriel") || name.includes("tutorial")) return "Template";
  if (name.includes("guide")) return "Template";
  if (name.includes("newsletter")) return "Prompt";
  if (name.includes("note")) return "Brief";

  // Si dans un dossier TEMPLATES → Template, sinon Prompt
  if (path.includes("template")) return "Template";
  return "Prompt";
}

/**
 * Devine l'usage si non explicite (enrichi avec Doc 2)
 */
function guessUsage_(file) {
  var name = file.name.toLowerCase();
  var path = (file.path || "").toLowerCase();

  // Email/CRM en priorité (anti-fourre-tout)
  if (name.includes("email") || name.includes("mail") || name.includes("crm") ||
      name.includes("fluent") || name.includes("fluentcrm") || name.includes("newsletter") ||
      name.includes("nurturing") || name.includes("drip")) return "Email";

  if (name.includes("youtube") || name.includes("yt") || name.includes("video") ||
      name.includes("vidéo") || name.includes("thumbnail")) return "YouTube";

  if (name.includes("seo") || name.includes("serp") || name.includes("meta") ||
      name.includes("cluster") || name.includes("maillage") || name.includes("netlinking")) return "SEO";

  if (name.includes("landing") || name.includes("conversion") || name.includes("cta")) return "Landing";

  if (name.includes("affili") || name.includes("partenariat") || name.includes("monetis")) return "Affiliation";

  if (name.includes("social") || name.includes("linkedin") || name.includes("facebook") ||
      name.includes("instagram") || name.includes("twitter") || name.includes("x.com")) return "Social";

  if (name.includes("ads") || name.includes("pub") || name.includes("campagne") ||
      name.includes("publicite") || name.includes("publicité")) return "Ads";

  if (name.includes("asset") || name.includes("logo") || name.includes("banner") ||
      name.includes("banniere") || name.includes("bannière") || name.includes("illustration") ||
      name.includes("charte") || name.includes("cover")) return "Asset";

  if (name.includes("autom") || name.includes("n8n") || name.includes("make") ||
      name.includes("zapier") || name.includes("workflow") || name.includes("script")) return "Automation";

  if (name.includes("article") || name.includes("blog") || name.includes("post") ||
      name.includes("redac") || name.includes("rédac") || name.includes("contenu")) return "Article";

  // Fallback par chemin
  if (path.includes("email") || path.includes("crm")) return "Email";
  if (path.includes("seo") || path.includes("editorial")) return "SEO";
  if (path.includes("asset")) return "Asset";
  if (path.includes("autom")) return "Automation";
  if (path.includes("affili") || path.includes("monetis")) return "Affiliation";

  return "Article"; // Défaut schoolsWP = éditorial
}

/**
 * Détermine le dossier cible selon type, usage, et contexte fichier.
 * Respecte STRICTEMENT les règles Email/CRM anti-fourre-tout.
 */
function determineTargetFolder_(type, usage, file) {
  var root = "PROMPTS_schoolsWP";

  // ── Templates réutilisables ──
  if (type === "Template") {
    switch (usage) {
      case "Article": case "SEO": return root + "/02_TEMPLATES/01_Editorial_SEO";
      case "Email": return root + "/02_TEMPLATES/02_Email_CRM_FluentCRM";
      case "Landing": return root + "/02_TEMPLATES/03_Conversion_Landing";
      case "YouTube": case "Social": return root + "/02_TEMPLATES/04_YouTube_Social";
      case "Affiliation": return root + "/02_TEMPLATES/05_Affiliation_Monetisation";
      case "Automation": return root + "/02_TEMPLATES/06_Automation_SOP";
      case "Ads": return root + "/02_TEMPLATES/03_Conversion_Landing";
      case "Asset": return root + "/04_ASSETS/04_Illustrations";
      case "ADMIN": return root + "/01_ADMIN/01_Regles-et-Index";
      default: return root + "/02_TEMPLATES/01_Editorial_SEO";
    }
  }

  // ── SOP ──
  if (type === "SOP") {
    return root + "/07_AUTOMATION/02_SOP";
  }

  // ── Brief ──
  if (type === "Brief") {
    if (usage === "Asset") return root + "/04_ASSETS/04_Illustrations";
    return root + "/06_SCHOOLS_WP_EDITORIAL/01_Briefs";
  }

  // ── Checklist ──
  if (type === "Checklist") {
    return root + "/01_ADMIN/02_Checklists-Qualite";
  }

  // ── Audit ──
  if (type === "Audit") {
    return root + "/01_ADMIN/02_Checklists-Qualite";
  }

  // ── Prompts one-shot datés ──
  if (type === "Prompt") {
    switch (usage) {
      case "Article": case "SEO": return root + "/03_PROMPTS/01_Editorial_SEO";
      case "Email": return root + "/03_PROMPTS/02_Email_CRM";
      case "Landing": case "Ads": return root + "/03_PROMPTS/03_Conversion";
      case "Affiliation": return root + "/03_PROMPTS/04_Affiliation";
      case "Asset": return root + "/03_PROMPTS/05_Assets";
      case "Automation": return root + "/03_PROMPTS/06_Automation";
      case "YouTube": case "Social": return root + "/03_PROMPTS/01_Editorial_SEO";
      case "ADMIN": return root + "/01_ADMIN/01_Regles-et-Index";
      default: return root + "/03_PROMPTS/01_Editorial_SEO";
    }
  }

  return null;
}

/**
 * Capitalise la première lettre d'une chaîne
 */
function capitalizeFirst_(str) {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// ══════════════════════════════════════════════════════════════
// 3. MIGRATION (EXÉCUTION SAFE)
// ══════════════════════════════════════════════════════════════

/**
 * Exécute la migration selon le mapping validé dans le Google Sheet.
 *
 * SÉCURITÉ :
 * - Backup complet AVANT toute modification
 * - Seules les lignes avec "OUI" dans "Validé" sont traitées
 * - Les fichiers <80% confiance sont ignorés sauf validation manuelle
 * - Aucune suppression : doublons → 99_ARCHIVES
 */
function executeMigration() {
  Logger.log("=== MIGRATION SAFE - schoolsWP Drive ===");
  Logger.log("ATTENTION : cette fonction modifie les fichiers.");
  Logger.log("Verifier le Sheet de mapping AVANT d'executer !");

  var startTime = new Date();

  // Trouver le Sheet de mapping
  var sheetFiles = DriveApp.getFilesByName(MAPPING_SHEET_NAME);
  if (!sheetFiles.hasNext()) {
    Logger.log("ERREUR : Sheet de mapping non trouve ! Executer generateMapping() d'abord.");
    return;
  }

  var ss = SpreadsheetApp.open(sheetFiles.next());
  var mappingSheet = ss.getSheetByName("Mapping");
  if (!mappingSheet) {
    Logger.log("ERREUR : Onglet 'Mapping' non trouve dans le Sheet !");
    return;
  }
  var data = mappingSheet.getDataRange().getValues();

  // Trouver le dossier racine cible
  var targetRoot;
  if (TARGET_ROOT_ID) {
    targetRoot = DriveApp.getFolderById(TARGET_ROOT_ID);
  } else {
    var rootSearch = DriveApp.getRootFolder().getFoldersByName("PROMPTS_schoolsWP");
    if (rootSearch.hasNext()) {
      targetRoot = rootSearch.next();
    } else {
      Logger.log("ERREUR : Dossier PROMPTS_schoolsWP non trouve !");
      Logger.log("Executer createFullStructure() d'abord.");
      return;
    }
  }

  // Créer un backup horodaté
  var today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");
  var backupFolder = getOrCreateFolder(targetRoot, "_BACKUP_" + today);
  Logger.log("Backup : " + backupFolder.getName() + " (" + backupFolder.getUrl() + ")");

  // Compteurs
  var renamed = 0;
  var moved = 0;
  var archived = 0;
  var skipped = 0;
  var errors = 0;
  var backed = 0;

  // Traiter chaque ligne (skip header, colonnes v2 : 12 colonnes)
  for (var i = 1; i < data.length; i++) {
    var row = data[i];
    var fileId = row[0];         // A: ID Fichier
    var oldName = row[1];        // B: Ancien nom
    var newName = row[3];        // D: Nouveau nom proposé
    var newPath = row[4];        // E: Nouveau chemin proposé
    var confidence = row[5];     // F: Confiance %
    var action = row[6];         // G: Action
    var validated = row[10];     // K: Validé ? (OUI/NON) → colonne 11 (index 10)

    // Ne traiter que les lignes validées OUI
    if (String(validated).toUpperCase() !== "OUI") {
      skipped++;
      continue;
    }

    // Ignorer les actions "OK" (déjà conforme)
    if (action === "OK") {
      continue;
    }

    try {
      var file = DriveApp.getFileById(fileId);

      // Backup d'abord (copie dans _BACKUP)
      file.makeCopy(file.getName(), backupFolder);
      backed++;

      // Renommer
      if (action === "RENAME" || action === "RENAME+MOVE") {
        if (newName && newName !== oldName) {
          file.setName(newName);
          renamed++;
          Logger.log("[RENAME] " + oldName + " -> " + newName);
        }
      }

      // Déplacer
      if (action === "MOVE" || action === "RENAME+MOVE") {
        if (newPath && newPath !== "A_DETERMINER") {
          var targetFolder = navigateToFolder_(targetRoot, newPath);
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
          } else {
            Logger.log("[WARN] Chemin cible non trouve : " + newPath);
            errors++;
          }
        }
      }

      // Archiver
      if (action === "ARCHIVE") {
        var archiveFolderPath = "99_ARCHIVES";
        var archiveFolder = navigateToFolder_(targetRoot, archiveFolderPath);
        if (archiveFolder) {
          archiveFolder.addFile(file);
          var archParents = file.getParents();
          while (archParents.hasNext()) {
            var archParent = archParents.next();
            if (archParent.getId() !== archiveFolder.getId()) {
              archParent.removeFile(file);
            }
          }
          archived++;
          Logger.log("[ARCHIVE] " + oldName);
        }
      }

    } catch (e) {
      Logger.log("[ERREUR] " + oldName + " : " + e.message);
      errors++;
    }
  }

  // Rapport
  var duration = (new Date() - startTime) / 1000;

  Logger.log("");
  Logger.log("=========================================");
  Logger.log("RAPPORT DE MIGRATION");
  Logger.log("=========================================");
  Logger.log("Fichiers sauvegardes  : " + backed);
  Logger.log("Fichiers renommes     : " + renamed);
  Logger.log("Fichiers deplaces     : " + moved);
  Logger.log("Fichiers archives     : " + archived);
  Logger.log("Fichiers ignores      : " + skipped);
  Logger.log("Erreurs               : " + errors);
  Logger.log("Duree                 : " + duration + "s");
  Logger.log("Backup                : " + backupFolder.getUrl());
  Logger.log("=========================================");

  // Ajouter un onglet Résultats dans le Sheet
  var resultsSheet = ss.getSheetByName("Resultats") || ss.insertSheet("Resultats");
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

  Logger.log("");
  Logger.log(">>> PROCHAINE ETAPE : generateGlobalIndex()");
}

/**
 * Navigue vers un dossier à partir d'un chemin relatif.
 * Crée les dossiers intermédiaires si nécessaire.
 */
function navigateToFolder_(rootFolder, path) {
  var cleanPath = path.replace(/^PROMPTS_schoolsWP\/?/, "");
  if (!cleanPath) return rootFolder;

  var parts = cleanPath.split("/");
  var current = rootFolder;

  for (var p = 0; p < parts.length; p++) {
    var part = parts[p];
    if (!part) continue;
    var subFolders = current.getFoldersByName(part);
    if (subFolders.hasNext()) {
      current = subFolders.next();
    } else {
      current = current.createFolder(part);
      Logger.log("[MKDIR] Dossier cree a la volee : " + part);
    }
  }

  return current;
}

// ══════════════════════════════════════════════════════════════
// 4. INDEX GLOBAL (Google Sheet + Miroir Markdown)
// ══════════════════════════════════════════════════════════════

/**
 * Génère l'index global en DEUX formats :
 * 1. Google Sheet filtrable (format principal)
 * 2. Fichier Markdown miroir dans 01_ADMIN/01_Regles-et-Index
 */
function generateGlobalIndex() {
  Logger.log("=== GENERATION INDEX GLOBAL (Sheet + Markdown) ===");

  // Trouver le dossier racine
  var targetRoot;
  if (TARGET_ROOT_ID) {
    targetRoot = DriveApp.getFolderById(TARGET_ROOT_ID);
  } else {
    var rootSearch = DriveApp.getRootFolder().getFoldersByName("PROMPTS_schoolsWP");
    if (rootSearch.hasNext()) {
      targetRoot = rootSearch.next();
    } else {
      Logger.log("ERREUR : Dossier PROMPTS_schoolsWP non trouve !");
      return;
    }
  }

  // Collecter tous les fichiers
  var allFiles = [];
  collectFilesRecursive_(targetRoot, "", allFiles);

  // Filtrer les fichiers système, backups, raccourcis
  var indexFiles = allFiles.filter(function(f) {
    return !f.name.startsWith("_") &&
           !f.path.includes("_BACKUP") &&
           f.mimeType !== "application/vnd.google-apps.shortcut";
  });

  // Trier par chemin puis par nom
  indexFiles.sort(function(a, b) {
    return (a.path + "/" + a.name).localeCompare(b.path + "/" + b.name);
  });

  var today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");

  // ════════════════════════════════════════
  // 4a. Google Sheet filtrable
  // ════════════════════════════════════════
  var ss;
  var existingSheets = DriveApp.getFilesByName(INDEX_SHEET_NAME);
  if (existingSheets.hasNext()) {
    ss = SpreadsheetApp.open(existingSheets.next());
    Logger.log("Sheet index existant : " + ss.getUrl());
  } else {
    ss = SpreadsheetApp.create(INDEX_SHEET_NAME);
    Logger.log("Sheet index cree : " + ss.getUrl());
  }

  var indexSheet = ss.getSheetByName("Index") || ss.insertSheet("Index");
  indexSheet.clear();

  var sheetHeaders = [
    "#", "Nom du fichier", "Chemin", "Categorie",
    "Statut", "Type", "Usage", "Derniere MAJ", "Lien", "Notes"
  ];
  indexSheet.getRange(1, 1, 1, sheetHeaders.length).setValues([sheetHeaders]);
  indexSheet.getRange(1, 1, 1, sheetHeaders.length).setFontWeight("bold");
  indexSheet.getRange(1, 1, 1, sheetHeaders.length).setBackground("#1a73e8");
  indexSheet.getRange(1, 1, 1, sheetHeaders.length).setFontColor("#ffffff");
  indexSheet.setFrozenRows(1);

  var sheetRows = [];
  for (var i = 0; i < indexFiles.length; i++) {
    var file = indexFiles[i];
    var analysis = analyzeFileName_(file.name, file.path);
    var category = detectCategory_(file.path);
    var status = detectStatus_(file.path);
    var modified = file.modified ? file.modified.substring(0, 10) : today;

    sheetRows.push([
      i + 1,
      file.name,
      file.path.replace(/^PROMPTS_schoolsWP\/?/, ""),
      category,
      status,
      analysis.detectedType || guessType_(file),
      analysis.detectedUsage || guessUsage_(file),
      modified,
      file.url,
      ""
    ]);
  }

  if (sheetRows.length > 0) {
    indexSheet.getRange(2, 1, sheetRows.length, sheetHeaders.length).setValues(sheetRows);
  }

  // Auto-resize colonnes
  for (var c = 1; c <= sheetHeaders.length; c++) {
    indexSheet.autoResizeColumn(c);
  }

  // Ajouter un filtre automatique
  if (sheetRows.length > 0) {
    var filterRange = indexSheet.getRange(1, 1, sheetRows.length + 1, sheetHeaders.length);
    if (indexSheet.getFilter()) indexSheet.getFilter().remove();
    filterRange.createFilter();
  }

  // Onglet Stats
  var statsSheet = ss.getSheetByName("Stats") || ss.insertSheet("Stats");
  statsSheet.clear();

  // Compter par catégorie
  var catCounts = {};
  for (var s = 0; s < sheetRows.length; s++) {
    var cat = sheetRows[s][3];
    catCounts[cat] = (catCounts[cat] || 0) + 1;
  }
  var statsData = [["Metrique", "Valeur"], ["Total fichiers indexes", indexFiles.length], ["Date generation", today], ["", ""]];
  statsData.push(["Par categorie", ""]);
  for (var catName in catCounts) {
    statsData.push([catName, catCounts[catName]]);
  }
  statsSheet.getRange(1, 1, statsData.length, 2).setValues(statsData);
  statsSheet.getRange(1, 1, 1, 2).setFontWeight("bold");

  // Supprimer la feuille par défaut
  var defaultSheet = ss.getSheetByName("Feuille 1") || ss.getSheetByName("Sheet1");
  if (defaultSheet && ss.getSheets().length > 1) {
    ss.deleteSheet(defaultSheet);
  }

  Logger.log("Sheet index : " + ss.getUrl());
  Logger.log("Fichiers indexes : " + indexFiles.length);

  // ════════════════════════════════════════
  // 4b. Miroir Markdown
  // ════════════════════════════════════════
  var mdLines = [];
  mdLines.push("# Index Global \u2013 PROMPTS_schoolsWP");
  mdLines.push("");
  mdLines.push("**Derniere mise a jour** : " + today);
  mdLines.push("**Total fichiers** : " + indexFiles.length);
  mdLines.push("**Sheet filtrable** : " + ss.getUrl());
  mdLines.push("");
  mdLines.push("---");
  mdLines.push("");

  var currentCategory = "";
  for (var m = 0; m < sheetRows.length; m++) {
    var row = sheetRows[m];
    var cat = row[3];

    if (cat !== currentCategory) {
      mdLines.push("");
      mdLines.push("## " + cat);
      mdLines.push("");
      mdLines.push("| # | Nom | Statut | Type | Usage | MAJ |");
      mdLines.push("|---|-----|--------|------|-------|-----|");
      currentCategory = cat;
    }

    mdLines.push("| " + row[0] + " | " + row[1] + " | " + row[4] + " | " + row[5] + " | " + row[6] + " | " + row[7] + " |");
  }

  mdLines.push("");
  mdLines.push("---");
  mdLines.push("*Index genere automatiquement le " + today + " par schoolsWP Drive Organizer v2.0*");

  var mdContent = mdLines.join("\n");

  // Sauvegarder le .md dans 01_ADMIN/01_Regles-et-Index
  var adminFolder = getOrCreateFolder(targetRoot, "01_ADMIN");
  var indexFolder = getOrCreateFolder(adminFolder, "01_Regles-et-Index");

  var mdFileName = today + " \u2013 Index \u2013 Checklist \u2013 ADMIN \u2013 Global.md";

  // Remplacer l'ancien miroir s'il existe
  var existingMd = indexFolder.getFilesByName(mdFileName);
  if (existingMd.hasNext()) {
    existingMd.next().setTrashed(true);
  }

  indexFolder.createFile(mdFileName, mdContent, MimeType.PLAIN_TEXT);
  Logger.log("Miroir Markdown : " + mdFileName);

  Logger.log("");
  Logger.log("=== INDEX GENERE ===");
  Logger.log("Sheet  : " + ss.getUrl());
  Logger.log("MD     : " + mdFileName);
  Logger.log("Total  : " + indexFiles.length + " fichiers");
}

/**
 * Détecte la catégorie depuis le chemin
 */
function detectCategory_(path) {
  if (path.includes("01_ADMIN")) return "ADMIN";
  if (path.includes("02_TEMPLATES")) return "TEMPLATES";
  if (path.includes("03_PROMPTS")) return "PROMPTS";
  if (path.includes("04_ASSETS")) return "ASSETS";
  if (path.includes("05_MONETISATION")) return "MONETISATION";
  if (path.includes("06_SCHOOLS_WP_EDITORIAL")) return "EDITORIAL";
  if (path.includes("07_AUTOMATION")) return "AUTOMATION";
  if (path.includes("99_ARCHIVES")) return "ARCHIVES";
  return "NON CLASSE";
}

/**
 * Détecte le statut depuis le chemin
 */
function detectStatus_(path) {
  if (path.includes("01_DRAFT")) return "DRAFT";
  if (path.includes("02_VALID")) return "VALIDE";
  if (path.includes("03_LIVE")) return "LIVE";
  if (path.includes("99_ARCHIVES")) return "ARCHIVES";
  return "N/A";
}

// ══════════════════════════════════════════════════════════════
// 5. RACCOURCIS DRIVE
// ══════════════════════════════════════════════════════════════

/**
 * Crée un raccourci Drive (shortcut) vers un fichier dans un dossier cible.
 *
 * PRÉREQUIS : Activer le service "Drive API" dans le projet Apps Script :
 *   Services (+) > Drive API > Ajouter
 *
 * @param {string} fileId - ID du fichier source
 * @param {string} targetFolderId - ID du dossier où créer le raccourci
 */
function createShortcut_(fileId, targetFolderId) {
  var file = DriveApp.getFileById(fileId);
  var shortcutMetadata = {
    name: file.getName(),
    mimeType: "application/vnd.google-apps.shortcut",
    shortcutDetails: {
      targetId: fileId
    },
    parents: [targetFolderId]
  };

  Drive.Files.create(shortcutMetadata, null, { supportsAllDrives: true });
  Logger.log("[SHORTCUT] " + file.getName() + " -> " + targetFolderId);
}

/**
 * Point d'entrée pour créer des raccourcis.
 * À personnaliser selon les besoins spécifiques.
 *
 * Exemple d'utilisation :
 *   createShortcut_("ID_DU_FICHIER", "ID_DU_DOSSIER_CIBLE");
 *
 * Cas d'usage typique :
 * - Template email utilisé aussi en monétisation
 * - Asset utilisé dans plusieurs catégories
 */
function createAllShortcuts() {
  Logger.log("=== CREATION DES RACCOURCIS ===");
  Logger.log("A personnaliser avec vos IDs de fichiers et dossiers.");
  Logger.log("");
  Logger.log("Syntaxe : createShortcut_('ID_FICHIER', 'ID_DOSSIER_CIBLE');");
  Logger.log("");
  Logger.log("Exemples de cas :");
  Logger.log("- Template email welcome aussi accessible depuis MONETISATION");
  Logger.log("- Asset logo accessible depuis TEMPLATES et ASSETS");

  // Décommenter et adapter :
  // createShortcut_("1ABC...xyz", "1DEF...uvw");
}
