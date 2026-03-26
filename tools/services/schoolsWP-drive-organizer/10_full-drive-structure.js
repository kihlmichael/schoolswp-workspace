/**
 * =============================================================
 * schoolsWP – FULL DRIVE Structure Creator  v1.0
 * =============================================================
 *
 * OBJECTIF : Créer/compléter l'arborescence complète du Google Drive
 * selon les règles des Docs 2-4 (structure Michaël KIHL).
 *
 * SÉCURITÉ : Ne supprime rien. Crée uniquement les dossiers manquants.
 * Si un dossier existe déjà, il est conservé tel quel.
 *
 * MODE D'EMPLOI :
 * 1. Coller dans un nouveau fichier script : FullDriveStructure.gs
 * 2. Exécuter createFullDriveStructure()
 * =============================================================
 */

// ══════════════════════════════════════════════════════════════
// ARBORESCENCE DRIVE COMPLÈTE (Docs 3/4)
// ══════════════════════════════════════════════════════════════

const FULL_DRIVE_STRUCTURE = {
  "00_START-HERE": {
    "01_Organisation-du-Drive": {},
    "02_Conventions-de-nommage": {},
    "03_Templates-et-modeles": {},
    "04_Onboarding": {}
  },
  "01_ADMIN": {
    "01_Identite": {},
    "02_Assurances": {},
    "03_Banque": {
      "01_Releves": {},
      "02_Justificatifs": {},
      "99_ARCHIVES": {}
    },
    "04_Factures": {
      "01_Emises": {},
      "02_Recues": {},
      "99_ARCHIVES": {}
    },
    "05_Contrats": {
      "01_Clients": {},
      "02_Prestataires": {},
      "03_Partenaires": {},
      "99_ARCHIVES": {}
    },
    "06_Impots-Fiscal": {},
    "99_ARCHIVES": {}
  },
  "02_PROJETS": {
    "schoolsWP": {
      "01_Strategie": {},
      "02_Contenus": {
        "01_Backlog": {},
        "02_En-cours": {},
        "03_A-revoir": {},
        "04_Publies": {
          "Articles": {
            "FR": {},
            "EN": {},
            "DE": {}
          }
        },
        "05_Lead-magnets": {},
        "06_Newsletters": {},
        "07_Scripts-video-audio": {},
        "99_ARCHIVES": {}
      },
      "03_SEO": {
        "01_Mots-cles": {},
        "02_Architecture-SEO": {},
        "03_Optimisations": {},
        "04_Suivi-performance": {},
        "05_IA-LLM-SEO": {},
        "99_ARCHIVES": {}
      },
      "04_Assets": {
        "01_Logos-Brand": {},
        "02_Thumbnails": {},
        "03_Banners": {},
        "04_Illustrations": {},
        "05_Captures-ecran": {},
        "06_Covers-articles": {},
        "99_ARCHIVES": {}
      },
      "05_Automations": {
        "01_CRM-FluentCRM": {},
        "02_Formulaires": {},
        "03_Workflows-n8n-Make": {},
        "99_ARCHIVES": {}
      },
      "06_Monetisation": {
        "01_Affiliation": {},
        "02_Partenariats": {},
        "03_Offres-Formations": {},
        "04_Campagnes": {},
        "05_Dashboards-Reporting": {},
        "99_ARCHIVES": {}
      },
      "07_Prompts": {},  // Lien vers PROMPTS_schoolsWP ou contenu existant
      "99_ARCHIVES": {}
    }
  },
  "03_RESSOURCES": {
    "01_Checklists": {},
    "02_Templates": {},
    "03_Prompts-IA": {},
    "04_Methodes": {},
    "05_Outils-Documentation": {},
    "06_Inspirations": {},
    "99_ARCHIVES": {}
  },
  "04_ASSETS": {
    "01_Logos-Branding": {},
    "02_Images": {},
    "03_Videos": {},
    "04_PDF-Documents": {},
    "05_Canva-Figma-PSD": {},
    "99_ARCHIVES": {}
  },
  "05_CLIENTS": {
    "_Template-Client": {
      "01_Brief": {},
      "02_Livrables": {},
      "03_Communication": {},
      "04_Factures": {},
      "99_ARCHIVES": {}
    }
  },
  "06_CONTENUS": {
    "01_Backlog": {},
    "02_En-cours": {},
    "03_A-optimiser": {},
    "04_Publies": {},
    "05_Lead-magnets": {},
    "06_Newsletters": {},
    "07_Scripts-video-audio": {},
    "99_ARCHIVES": {}
  },
  "99_ARCHIVES": {}
};

// ══════════════════════════════════════════════════════════════
// FONCTIONS
// ══════════════════════════════════════════════════════════════

/**
 * Point d'entrée – Crée toute l'arborescence Drive
 */
function createFullDriveStructure() {
  var startTime = new Date();
  Logger.log("=== FULL DRIVE Structure Creator v1.0 ===");
  Logger.log("Debut : " + startTime.toISOString());

  var root = DriveApp.getRootFolder();
  Logger.log("Racine : Mon Drive");

  var created = 0;
  var existing = 0;

  // Créer récursivement
  var result = createDriveFoldersRecursive_(root, FULL_DRIVE_STRUCTURE, "");
  created = result.created;
  existing = result.existing;

  // Vérifier que PROMPTS_schoolsWP existe (créé par le script précédent)
  var promptsSearch = root.getFoldersByName("PROMPTS_schoolsWP");
  if (promptsSearch.hasNext()) {
    Logger.log("[OK] PROMPTS_schoolsWP existe deja");
  } else {
    Logger.log("[INFO] PROMPTS_schoolsWP non trouve - executer createFullStructure() si besoin");
  }

  var duration = (new Date() - startTime) / 1000;

  Logger.log("");
  Logger.log("=========================================");
  Logger.log("RAPPORT DE CREATION - DRIVE COMPLET");
  Logger.log("=========================================");
  Logger.log("Dossiers crees     : " + created);
  Logger.log("Dossiers existants : " + existing);
  Logger.log("Duree              : " + duration + "s");
  Logger.log("=========================================");
}

/**
 * Création récursive des dossiers
 */
function createDriveFoldersRecursive_(parentFolder, structure, indent) {
  var created = 0;
  var existing = 0;

  for (var name in structure) {
    if (!structure.hasOwnProperty(name)) continue;
    var children = structure[name];

    var existingFolders = parentFolder.getFoldersByName(name);
    var folder;

    if (existingFolders.hasNext()) {
      folder = existingFolders.next();
      Logger.log(indent + "[EXISTE] " + name);
      existing++;
    } else {
      folder = parentFolder.createFolder(name);
      Logger.log(indent + "[CREE]   " + name);
      created++;
    }

    if (children && Object.keys(children).length > 0) {
      var childResult = createDriveFoldersRecursive_(folder, children, indent + "  ");
      created += childResult.created;
      existing += childResult.existing;
    }
  }

  return { created: created, existing: existing };
}

/**
 * Vérification de l'arborescence Drive complète
 */
function verifyFullDriveStructure() {
  Logger.log("=== VERIFICATION DRIVE COMPLET ===");
  var root = DriveApp.getRootFolder();

  var totalFolders = 0;
  var totalFiles = 0;

  // Lister les dossiers racine
  var rootFolders = root.getFolders();
  while (rootFolders.hasNext()) {
    var folder = rootFolders.next();
    var name = folder.getName();
    // Ne lister que les dossiers numérotés (notre structure)
    if (/^\d{2}_/.test(name) || name === "PROMPTS_schoolsWP") {
      Logger.log("[D] " + name);
      totalFolders++;
      var counts = countContentsRecursive_(folder, "  ");
      totalFolders += counts.folders;
      totalFiles += counts.files;
    }
  }

  Logger.log("");
  Logger.log("Total dossiers structures : " + totalFolders);
  Logger.log("Total fichiers            : " + totalFiles);
}

/**
 * Compte récursif du contenu
 */
function countContentsRecursive_(folder, indent) {
  var folders = 0;
  var files = 0;

  var subFolders = folder.getFolders();
  while (subFolders.hasNext()) {
    var sub = subFolders.next();
    folders++;
    Logger.log(indent + "[D] " + sub.getName());
    var childCounts = countContentsRecursive_(sub, indent + "  ");
    folders += childCounts.folders;
    files += childCounts.files;
  }

  var fileIterator = folder.getFiles();
  while (fileIterator.hasNext()) {
    files++;
    fileIterator.next(); // consume iterator
  }
  if (files > 0) {
    Logger.log(indent + "  (" + files + " fichiers)");
  }

  return { folders: folders, files: files };
}
