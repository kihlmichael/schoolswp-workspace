/**
 * =============================================================
 * schoolsWP – Google Drive Structure Creator  v2.0
 * =============================================================
 *
 * OBJECTIF : Créer l'arborescence complète PROMPTS_schoolsWP
 * dans Google Drive, avec sous-dossiers de statut dans
 * TEMPLATES et PROMPTS.
 *
 * MODE D'EMPLOI :
 * 1. Ouvrir https://script.google.com
 * 2. Créer un nouveau projet : "schoolsWP Drive Organizer"
 * 3. Coller ce script dans Code.gs
 * 4. PARENT_FOLDER_ID est déjà configuré pour la racine du Drive.
 *    Le script cherchera (ou créera) PROMPTS_schoolsWP à la racine.
 *    → Si tu veux cibler un dossier parent spécifique, mets son ID.
 * 5. Exécuter la fonction : createFullStructure()
 * 6. Autoriser l'accès au Drive quand demandé
 *
 * SÉCURITÉ : Ce script ne supprime rien. Il crée uniquement des dossiers.
 * Si un dossier existe déjà (même nom au même endroit), il ne le recrée pas.
 * =============================================================
 */

// ══════════════════════════════════════════════════════════════
// CONFIGURATION
// ══════════════════════════════════════════════════════════════

/**
 * ID du dossier parent où créer PROMPTS_schoolsWP.
 * - null = racine de Mon Drive
 * - "1ABC...xyz" = ID d'un dossier spécifique
 */
const PARENT_FOLDER_ID = null;

/**
 * Nom du dossier racine
 */
const ROOT_FOLDER_NAME = "PROMPTS_schoolsWP";

/**
 * Sous-dossiers de statut (ajoutés dans chaque sous-catégorie de TEMPLATES et PROMPTS)
 * Règle : le statut est géré par le DOSSIER, jamais dans le nom du fichier.
 */
const STATUS_SUBFOLDERS = [
  "01_DRAFT",
  "02_VALIDÉ",
  "03_LIVE",
  "99_ARCHIVES"
];

/**
 * Catégories principales qui reçoivent les sous-dossiers de statut
 */
const CATEGORIES_WITH_STATUS = ["02_TEMPLATES", "03_PROMPTS"];

// ══════════════════════════════════════════════════════════════
// ARBORESCENCE COMPLÈTE
// ══════════════════════════════════════════════════════════════

const STRUCTURE = {
  "01_ADMIN": {
    "01_Regles-et-Index": {},
    "02_Checklists-Qualite": {}
  },
  "02_TEMPLATES": {
    "01_Editorial_SEO": {},
    "02_Email_CRM_FluentCRM": {},
    "03_Conversion_Landing": {},
    "04_YouTube_Social": {},
    "05_Affiliation_Monetisation": {},
    "06_Automation_SOP": {}
  },
  "03_PROMPTS": {
    "01_Editorial_SEO": {},
    "02_Email_CRM": {},
    "03_Conversion": {},
    "04_Affiliation": {},
    "05_Assets": {},
    "06_Automation": {}
  },
  "04_ASSETS": {
    "01_Logos-Brand": {},
    "02_Thumbnails": {},
    "03_Banners": {},
    "04_Illustrations": {}
  },
  "05_MONETISATION": {
    "01_Affiliation": {},
    "02_Partenariats": {},
    "03_Dashboards-Reporting": {},
    "04_Sequences_Email": {}
  },
  "06_SCHOOLS_WP_EDITORIAL": {
    "01_Briefs": {},
    "02_Plans": {},
    "03_Clusters": {},
    "04_Meta-FAQ-SERP": {}
  },
  "07_AUTOMATION": {
    "01_n8n-Make-Zapier": {},
    "02_SOP": {},
    "03_Scripts": {}
  },
  "99_ARCHIVES": {}
};

// ══════════════════════════════════════════════════════════════
// FONCTIONS PRINCIPALES
// ══════════════════════════════════════════════════════════════

/**
 * Point d'entrée principal – Crée toute l'arborescence
 */
function createFullStructure() {
  const startTime = new Date();
  Logger.log("═══ schoolsWP Drive Structure Creator v2.0 ═══");
  Logger.log("Début : " + startTime.toISOString());

  // Résoudre le dossier parent
  let parentFolder;
  if (PARENT_FOLDER_ID) {
    parentFolder = DriveApp.getFolderById(PARENT_FOLDER_ID);
    Logger.log("Dossier parent : " + parentFolder.getName());
  } else {
    parentFolder = DriveApp.getRootFolder();
    Logger.log("Dossier parent : Racine du Drive");
  }

  // Créer le dossier racine
  const rootFolder = getOrCreateFolder(parentFolder, ROOT_FOLDER_NAME);
  Logger.log("Dossier racine : " + rootFolder.getName() + " (ID: " + rootFolder.getId() + ")");

  // Compteurs
  let created = 0;
  let existing = 0;

  // Créer l'arborescence récursivement
  const result = createFoldersRecursive(rootFolder, STRUCTURE, "");
  created += result.created;
  existing += result.existing;

  // Ajouter les sous-dossiers de statut dans TEMPLATES et PROMPTS
  for (const categoryName of CATEGORIES_WITH_STATUS) {
    const categoryFolder = getOrCreateFolder(rootFolder, categoryName);
    const subFolders = categoryName === "02_TEMPLATES"
      ? STRUCTURE["02_TEMPLATES"]
      : STRUCTURE["03_PROMPTS"];

    for (const subName of Object.keys(subFolders)) {
      const subFolder = getOrCreateFolder(categoryFolder, subName);
      for (const statusName of STATUS_SUBFOLDERS) {
        const statusFolder = getOrCreateFolder(subFolder, statusName);
        if (statusFolder._wasCreated) {
          created++;
        } else {
          existing++;
        }
      }
    }
  }

  // Rapport
  const endTime = new Date();
  const duration = (endTime - startTime) / 1000;

  Logger.log("═══════════════════════════════════════════");
  Logger.log("RAPPORT DE CRÉATION");
  Logger.log("═══════════════════════════════════════════");
  Logger.log("Dossiers créés     : " + created);
  Logger.log("Dossiers existants : " + existing);
  Logger.log("Durée              : " + duration + "s");
  Logger.log("Racine Drive ID    : " + rootFolder.getId());
  Logger.log("URL                : " + rootFolder.getUrl());
  Logger.log("═══════════════════════════════════════════");

  // Créer un fichier de log dans 01_ADMIN
  createLogFile_(rootFolder, created, existing, duration);

  return rootFolder;
}

/**
 * Crée les dossiers récursivement à partir d'un objet de structure
 */
function createFoldersRecursive(parentFolder, structure, indent) {
  let created = 0;
  let existing = 0;

  for (const [name, children] of Object.entries(structure)) {
    const folder = getOrCreateFolder(parentFolder, name);

    if (folder._wasCreated) {
      Logger.log(indent + "[CREE] " + name);
      created++;
    } else {
      Logger.log(indent + "[EXISTE] " + name);
      existing++;
    }

    // Récursion sur les enfants
    if (children && Object.keys(children).length > 0) {
      const childResult = createFoldersRecursive(folder, children, indent + "  ");
      created += childResult.created;
      existing += childResult.existing;
    }
  }

  return { created, existing };
}

/**
 * Récupère un dossier existant par nom ou le crée.
 * Ajoute une propriété _wasCreated pour le tracking.
 */
function getOrCreateFolder(parentFolder, folderName) {
  const existingFolders = parentFolder.getFoldersByName(folderName);

  if (existingFolders.hasNext()) {
    const folder = existingFolders.next();
    folder._wasCreated = false;
    return folder;
  }

  const newFolder = parentFolder.createFolder(folderName);
  newFolder._wasCreated = true;
  return newFolder;
}

/**
 * Crée un fichier de log dans 01_ADMIN/01_Regles-et-Index
 */
function createLogFile_(rootFolder, created, existing, duration) {
  try {
    const adminFolder = getOrCreateFolder(rootFolder, "01_ADMIN");
    const indexFolder = getOrCreateFolder(adminFolder, "01_Regles-et-Index");

    const today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");
    const logName = today + " \u2013 Log-Creation-Structure \u2013 Checklist \u2013 ADMIN.md";

    const logContent = [
      "# Log de cr\u00e9ation \u2013 Arborescence PROMPTS_schoolsWP",
      "",
      "**Date** : " + today,
      "**Script** : schoolsWP Drive Structure Creator v2.0",
      "",
      "## R\u00e9sultats",
      "",
      "| M\u00e9trique | Valeur |",
      "|----------|--------|",
      "| Dossiers cr\u00e9\u00e9s | " + created + " |",
      "| Dossiers d\u00e9j\u00e0 existants | " + existing + " |",
      "| Dur\u00e9e d'ex\u00e9cution | " + duration + "s |",
      "",
      "## Arborescence cr\u00e9\u00e9e",
      "",
      "```",
      "PROMPTS_schoolsWP/",
      "+-- 01_ADMIN/",
      "|   +-- 01_Regles-et-Index/",
      "|   +-- 02_Checklists-Qualite/",
      "+-- 02_TEMPLATES/ (chaque sous-dossier contient 01_DRAFT, 02_VALIDE, 03_LIVE, 99_ARCHIVES)",
      "|   +-- 01_Editorial_SEO/",
      "|   +-- 02_Email_CRM_FluentCRM/",
      "|   +-- 03_Conversion_Landing/",
      "|   +-- 04_YouTube_Social/",
      "|   +-- 05_Affiliation_Monetisation/",
      "|   +-- 06_Automation_SOP/",
      "+-- 03_PROMPTS/ (idem sous-dossiers de statut)",
      "|   +-- 01_Editorial_SEO/",
      "|   +-- 02_Email_CRM/",
      "|   +-- 03_Conversion/",
      "|   +-- 04_Affiliation/",
      "|   +-- 05_Assets/",
      "|   +-- 06_Automation/",
      "+-- 04_ASSETS/",
      "|   +-- 01_Logos-Brand/",
      "|   +-- 02_Thumbnails/",
      "|   +-- 03_Banners/",
      "|   +-- 04_Illustrations/",
      "+-- 05_MONETISATION/",
      "|   +-- 01_Affiliation/",
      "|   +-- 02_Partenariats/",
      "|   +-- 03_Dashboards-Reporting/",
      "|   +-- 04_Sequences_Email/",
      "+-- 06_SCHOOLS_WP_EDITORIAL/",
      "|   +-- 01_Briefs/",
      "|   +-- 02_Plans/",
      "|   +-- 03_Clusters/",
      "|   +-- 04_Meta-FAQ-SERP/",
      "+-- 07_AUTOMATION/",
      "|   +-- 01_n8n-Make-Zapier/",
      "|   +-- 02_SOP/",
      "|   +-- 03_Scripts/",
      "+-- 99_ARCHIVES/",
      "```",
      "",
      "---",
      "*G\u00e9n\u00e9r\u00e9 automatiquement par schoolsWP Drive Organizer*"
    ].join("\n");

    indexFolder.createFile(logName, logContent, MimeType.PLAIN_TEXT);
    Logger.log("Fichier de log cr\u00e9\u00e9 : " + logName);
  } catch (e) {
    Logger.log("Erreur cr\u00e9ation log : " + e.message);
  }
}

// ══════════════════════════════════════════════════════════════
// UTILITAIRES
// ══════════════════════════════════════════════════════════════

/**
 * Fonction de test – Liste l'arborescence existante
 * Utile pour vérifier après exécution
 */
function verifyStructure() {
  let parentFolder;
  if (PARENT_FOLDER_ID) {
    parentFolder = DriveApp.getFolderById(PARENT_FOLDER_ID);
  } else {
    parentFolder = DriveApp.getRootFolder();
  }

  const rootFolders = parentFolder.getFoldersByName(ROOT_FOLDER_NAME);
  if (!rootFolders.hasNext()) {
    Logger.log("ERREUR : Dossier " + ROOT_FOLDER_NAME + " non trouve !");
    return;
  }

  const rootFolder = rootFolders.next();
  Logger.log("Verification de : " + rootFolder.getName());
  Logger.log("URL : " + rootFolder.getUrl());
  Logger.log("");

  let totalFolders = 0;
  let totalFiles = 0;
  const counts = listFoldersRecursive_(rootFolder, 0);
  totalFolders = counts.folders;
  totalFiles = counts.files;

  Logger.log("");
  Logger.log("Total dossiers : " + totalFolders);
  Logger.log("Total fichiers : " + totalFiles);
}

/**
 * Liste récursive des dossiers pour vérification
 */
function listFoldersRecursive_(folder, depth) {
  const indent = "  ".repeat(depth);
  const subFolders = folder.getFolders();
  let folders = 0;
  let files = 0;

  while (subFolders.hasNext()) {
    const sub = subFolders.next();
    folders++;
    Logger.log(indent + "[D] " + sub.getName());
    const childCounts = listFoldersRecursive_(sub, depth + 1);
    folders += childCounts.folders;
    files += childCounts.files;
  }

  const fileIterator = folder.getFiles();
  while (fileIterator.hasNext()) {
    const file = fileIterator.next();
    files++;
    Logger.log(indent + "[F] " + file.getName());
  }

  return { folders, files };
}
