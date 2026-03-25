/**
 * schoolsWP Drive Organizer v3.0 – Audit & Analyse
 *
 * Point d'entree : runAudit()
 */

/** Audit complet du dossier source */
function runAudit() {
  Logger.log("=== AUDIT v3.0 - schoolsWP Drive ===");
  const startTime = new Date();

  const sourceFolder = DriveApp.getFolderById(SOURCE_FOLDER_ID);
  Logger.log("Source : " + sourceFolder.getName() + " (" + SOURCE_FOLDER_ID + ")");

  const allFiles = [];
  collectFilesRecursive_(sourceFolder, "", allFiles);
  Logger.log("Fichiers trouves : " + allFiles.length);

  const anomalies = {
    noDate: [],
    badSeparator: [],
    noType: [],
    noUsage: [],
    badExtension: [],
    duplicates: [],
    misplacedEmail: [],
    misplacedMonetisation: []
  };

  const filesBySubject = {};

  for (const file of allFiles) {
    const analysis = analyzeFileName_(file.name, file.path);
    file.analysis = analysis;

    if (!analysis.hasDate) anomalies.noDate.push(file);
    if (analysis.hasBadSeparator) anomalies.badSeparator.push(file);
    if (!analysis.hasType) anomalies.noType.push(file);
    if (!analysis.hasUsage) anomalies.noUsage.push(file);
    if (analysis.hasBadExtension) anomalies.badExtension.push(file);

    if (analysis.emailClassification && analysis.emailClassification.misplaced) {
      anomalies.misplacedEmail.push({
        file: file,
        currentPath: file.path,
        shouldBe: analysis.emailClassification.correctFolder,
        reason: analysis.emailClassification.reason
      });
    }

    if (analysis.monetisationMisplaced) {
      anomalies.misplacedMonetisation.push(file);
    }

    const normalizedKey = normalizeForDuplicates_(file.name);
    if (!filesBySubject[normalizedKey]) filesBySubject[normalizedKey] = [];
    filesBySubject[normalizedKey].push(file);
  }

  for (const [key, files] of Object.entries(filesBySubject)) {
    if (files.length > 1) {
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

  // Rapport
  Logger.log("");
  Logger.log("=== RAPPORT D'AUDIT ===");
  Logger.log("Total fichiers           : " + allFiles.length);
  Logger.log("Sans date                : " + anomalies.noDate.length);
  Logger.log("Mauvais separateurs      : " + anomalies.badSeparator.length);
  Logger.log("Sans type                : " + anomalies.noType.length);
  Logger.log("Sans usage               : " + anomalies.noUsage.length);
  Logger.log("Extension non standard   : " + anomalies.badExtension.length);
  Logger.log("Email/CRM mal ranges     : " + anomalies.misplacedEmail.length);
  Logger.log("Monetisation mal ranges  : " + anomalies.misplacedMonetisation.length);
  Logger.log("Groupes doublons         : " + anomalies.duplicates.length);

  if (anomalies.misplacedEmail.length > 0) {
    Logger.log("--- DETAIL Email/CRM mal ranges ---");
    for (const item of anomalies.misplacedEmail) {
      Logger.log("  " + item.file.name);
      Logger.log("    Actuel  : " + item.currentPath);
      Logger.log("    Correct : " + item.shouldBe);
      Logger.log("    Raison  : " + item.reason);
    }
  }

  storeAuditData_(allFiles, anomalies);

  const duration = (new Date() - startTime) / 1000;
  Logger.log("Duree audit : " + duration + "s");
  return { files: allFiles, anomalies };
}

// === ANALYSE DE NOM DE FICHIER ===

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
    emailClassification: null,
    monetisationMisplaced: false,
    isVariant: false,
    variantMarkers: [],
    severity: "OK",
    issues: []
  };

  // 1. Date
  const dateMatch = name.match(/^(\d{4}-\d{2}-\d{2})/);
  if (dateMatch) {
    analysis.hasDate = true;
    analysis.detectedDate = dateMatch[1];
    const year = parseInt(dateMatch[1].substring(0, 4));
    if (year < 2020 || year > 2030) {
      analysis.issues.push("Date suspecte : " + dateMatch[1]);
    }
  } else {
    analysis.issues.push("Date manquante en debut de nom");
  }

  // 2. Separateur
  const hasTiretCourt = / - /.test(name);
  const hasDoubleUnderscore = name.includes("__");
  const hasTiretLong = name.includes(SEP);
  const hasSuspectUnderscore = /_/.test(name) && !hasTiretLong;

  if (hasTiretCourt || hasDoubleUnderscore || hasSuspectUnderscore) {
    analysis.hasBadSeparator = true;
    const badTypes = [];
    if (hasTiretCourt) badTypes.push("tiret court");
    if (hasDoubleUnderscore) badTypes.push("double underscore");
    if (hasSuspectUnderscore) badTypes.push("underscore au lieu de tiret long");
    analysis.issues.push("Mauvais separateur : " + badTypes.join(", "));
  }

  // 3. Type
  for (const type of VALID_TYPES) {
    const re = new RegExp("[\u2013\\-_]\\s*" + type + "\\s*[\u2013\\-_.]", "i");
    if (re.test(name) || name.includes(SEP + type + SEP) || name.includes(SEP + type + ".")) {
      analysis.hasType = true;
      analysis.detectedType = type;
      break;
    }
  }

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

  // 4. Usage
  for (const usage of VALID_USAGES) {
    const re = new RegExp("[\u2013\\-_]\\s*" + usage + "\\s*[\u2013\\-_.]", "i");
    if (re.test(name) || name.includes(SEP + usage + SEP) || name.includes(SEP + usage + ".")) {
      analysis.hasUsage = true;
      analysis.detectedUsage = usage;
      break;
    }
  }
  if (!analysis.hasUsage) {
    analysis.issues.push("Usage non detecte (attendu : " + VALID_USAGES.join(", ") + ")");
  }

  // 5. Extension
  const extMatch = name.match(/\.([^.]+)$/);
  if (extMatch && !VALID_EXTENSIONS.includes(extMatch[1].toLowerCase())) {
    analysis.hasBadExtension = true;
    analysis.issues.push("Extension non standard : ." + extMatch[1]);
  }

  // 6. Variantes (V1/V2/FR/EN/Court/Long)
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

  // 7. Classification Email/CRM
  analysis.emailClassification = classifyEmailCRM_(name, filePath, analysis.detectedType);

  // 8. Monetisation mal rangee
  const nameLower = name.toLowerCase();
  const pathLower = (filePath || "").toLowerCase();
  const isMonetisationContent = MONETISATION_KEYWORDS.some(kw => nameLower.includes(kw));
  if (isMonetisationContent && !pathLower.includes("monetisation") && !pathLower.includes("mon\u00e9tisation")) {
    analysis.monetisationMisplaced = true;
    analysis.issues.push("Contenu monetisation detecte hors dossier MONETISATION");
  }

  // 9. Format complet
  analysis.hasCorrectFormat = NAME_REGEX.test(name);

  // 10. Severite
  const hasCritical = analysis.issues.some(i =>
    i.includes("Date manquante") || i.includes("Type non detecte")
  );
  const hasMedium = analysis.issues.some(i =>
    i.includes("Mauvais separateur") || i.includes("Usage non detecte")
  );

  if (hasCritical) analysis.severity = "CRITIQUE";
  else if (hasMedium) analysis.severity = "MOYEN";
  else if (analysis.issues.length > 0) analysis.severity = "MINEUR";

  return analysis;
}

// === CLASSIFICATION EMAIL/CRM ===

/**
 * Anti-fourre-tout : 3 destinations possibles
 * 1. Template reutilisable  -> 02_TEMPLATES/02_Email_CRM_FluentCRM
 * 2. Prompt one-shot date   -> 03_PROMPTS/02_Email_CRM
 * 3. Sequence monetisation  -> 05_MONETISATION/04_Sequences_Email
 */
function classifyEmailCRM_(name, filePath, detectedType) {
  const nameLower = name.toLowerCase();
  if (!EMAIL_KEYWORDS.some(kw => nameLower.includes(kw))) return null;

  let correctFolder, reason;

  if (MONETISATION_KEYWORDS.some(kw => nameLower.includes(kw))) {
    correctFolder = "05_MONETISATION/04_Sequences_Email";
    reason = "Sequence email liee a un dispositif monetisation";
  } else if (detectedType === "Template" || nameLower.includes("template")) {
    correctFolder = "02_TEMPLATES/02_Email_CRM_FluentCRM";
    reason = "Template email reutilisable";
  } else {
    correctFolder = "03_PROMPTS/02_Email_CRM";
    reason = "Prompt email one-shot date";
  }

  // Verifie que TOUS les segments du chemin cible sont presents
  const pathLower = (filePath || "").toLowerCase();
  const misplaced = !correctFolder.split("/").every(part =>
    pathLower.includes(part.toLowerCase())
  );

  return { isEmail: true, correctFolder, reason, misplaced, currentPath: filePath };
}

// === DETECTION DOUBLONS ===

/** Normalise un nom pour grouper les doublons (retire date, extension, variantes, types) */
function normalizeForDuplicates_(name) {
  return name
    .replace(/^\d{4}-\d{2}-\d{2}/, "")
    .replace(/\.[^.]+$/, "")
    .replace(/[\u2013\-_]/g, " ")
    .replace(/\b(V\d+|FR|EN|DE|ES|Court|Long)\b/gi, "")
    .replace(/\b(Prompt|Template|SOP|Brief|Checklist|Audit)\b/gi, "")
    .replace(/\b(Article|SEO|Email|Landing|Affiliation|Ads|YouTube|Social|Asset|Automation|ADMIN)\b/gi, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

/** Distingue variantes legitimes (V1/V2/FR/EN) des vrais doublons */
function detectVariants_(files) {
  const result = {
    hasTrueDuplicates: false,
    variantGroups: {},
    trueDuplicates: []
  };

  // Signature = nom sans date ni extension (AVEC variantes)
  const signatures = {};
  for (const file of files) {
    const sig = file.name
      .replace(/^\d{4}-\d{2}-\d{2}[\s\u2013\-_]*/, "")
      .replace(/\.[^.]+$/, "")
      .trim()
      .toLowerCase();

    if (!signatures[sig]) signatures[sig] = [];
    signatures[sig].push(file);
  }

  for (const [sig, sigFiles] of Object.entries(signatures)) {
    if (sigFiles.length > 1) {
      result.hasTrueDuplicates = true;
      result.trueDuplicates.push({
        signature: sig,
        files: sigFiles.map(f => f.name)
      });
    }
  }

  for (const file of files) {
    const markers = (file.analysis && file.analysis.variantMarkers) || [];
    const key = markers.length > 0 ? markers.sort().join("+") : "base";
    if (!result.variantGroups[key]) result.variantGroups[key] = [];
    result.variantGroups[key].push(file.name);
  }

  return result;
}

// === EXTRACTION / DEVINETTE ===

function extractSubject_(name) {
  let subject = name.replace(/^\d{4}-\d{2}-\d{2}[\s\u2013\-_]*/, "");
  subject = subject.replace(/\.[^.]+$/, "");
  for (const t of VALID_TYPES) {
    subject = subject.replace(new RegExp("\\s*[\u2013\\-_]\\s*" + t + "(?=\\s*[\u2013\\-_.]|$)", "gi"), "");
  }
  for (const u of VALID_USAGES) {
    subject = subject.replace(new RegExp("\\s*[\u2013\\-_]\\s*" + u + "(?=\\s*[\u2013\\-_.]|$)", "gi"), "");
  }
  subject = subject.replace(/\s*[\u2013\-_]\s*(V\d+|FR|EN|DE|ES|Court|Long)\b/gi, "");
  return subject.replace(/[\u2013\-_]+/g, " ").replace(/\s+/g, " ").trim();
}

/** Devine le type si non explicite dans le nom */
function guessType_(file) {
  const name = file.name.toLowerCase();
  const path = (file.path || "").toLowerCase();

  if (path.includes("template") || name.includes("template")) return "Template";
  if (path.includes("sop") || name.includes("sop") || name.includes("procedure") || name.includes("proc\u00e9dure")) return "SOP";
  if (path.includes("brief") || name.includes("brief")) return "Brief";
  if (path.includes("checklist") || name.includes("checklist") || name.includes("check-list")) return "Checklist";
  if (path.includes("audit") || name.includes("audit")) return "Audit";
  if (name.includes("tutoriel") || name.includes("tutorial") || name.includes("guide")) return "Template";
  if (name.includes("newsletter")) return "Prompt";
  if (name.includes("note")) return "Brief";
  if (path.includes("template")) return "Template";
  return "Prompt";
}

/** Devine l'usage si non explicite dans le nom */
function guessUsage_(file) {
  const name = file.name.toLowerCase();
  const path = (file.path || "").toLowerCase();

  // Tableau de regles : [keywords[], usage]
  const rules = [
    [["email", "mail", "crm", "fluent", "fluentcrm", "newsletter", "nurturing", "drip"], "Email"],
    [["youtube", "yt", "video", "vid\u00e9o", "thumbnail"], "YouTube"],
    [["seo", "serp", "meta", "cluster", "maillage", "netlinking"], "SEO"],
    [["landing", "conversion", "cta"], "Landing"],
    [["affili", "partenariat", "monetis"], "Affiliation"],
    [["social", "linkedin", "facebook", "instagram", "twitter", "x.com"], "Social"],
    [["ads", "pub", "campagne", "publicite", "publicit\u00e9"], "Ads"],
    [["asset", "logo", "banner", "banniere", "banni\u00e8re", "illustration", "charte", "cover"], "Asset"],
    [["autom", "n8n", "make", "zapier", "workflow", "script"], "Automation"],
    [["article", "blog", "post", "redac", "r\u00e9dac", "contenu"], "Article"]
  ];

  for (const [keywords, usage] of rules) {
    if (keywords.some(kw => name.includes(kw))) return usage;
  }

  // Fallback par chemin
  const pathRules = [
    [["email", "crm"], "Email"],
    [["seo", "editorial"], "SEO"],
    [["asset"], "Asset"],
    [["autom"], "Automation"],
    [["affili", "monetis"], "Affiliation"]
  ];

  for (const [keywords, usage] of pathRules) {
    if (keywords.some(kw => path.includes(kw))) return usage;
  }

  return "Article";
}
