/**
 * schoolsWP Drive Organizer v3.0 – Utilitaires partages
 */

// === DOSSIERS ===

/** Recupere ou cree un dossier (sans tracking) */
function getOrCreateFolder(parent, name) {
  const it = parent.getFoldersByName(name);
  return it.hasNext() ? it.next() : parent.createFolder(name);
}

/** Recupere ou cree un dossier avec indicateur de creation */
function getOrCreateFolderTracked(parent, name) {
  const it = parent.getFoldersByName(name);
  if (it.hasNext()) return { folder: it.next(), created: false };
  return { folder: parent.createFolder(name), created: true };
}

/** Resout le dossier parent selon PARENT_FOLDER_ID */
function resolveParentFolder_() {
  return PARENT_FOLDER_ID
    ? DriveApp.getFolderById(PARENT_FOLDER_ID)
    : DriveApp.getRootFolder();
}

/** Resout le dossier racine cible selon TARGET_ROOT_ID */
function resolveTargetRoot_() {
  if (TARGET_ROOT_ID) return DriveApp.getFolderById(TARGET_ROOT_ID);
  const it = DriveApp.getRootFolder().getFoldersByName(ROOT_FOLDER_NAME);
  return it.hasNext() ? it.next() : null;
}

/** Navigue vers un dossier depuis un chemin relatif, cree les intermediaires si absents */
function navigateToFolder_(root, path) {
  const clean = path.replace(/^PROMPTS_schoolsWP\/?/, "");
  if (!clean) return root;

  let current = root;
  for (const part of clean.split("/")) {
    if (!part) continue;
    current = getOrCreateFolder(current, part);
  }
  return current;
}

// === FICHIERS ===

/** Collecte recursive de tous les fichiers (ignore shortcuts et _BACKUP) */
function collectFilesRecursive_(folder, path, results) {
  const currentPath = path ? path + "/" + folder.getName() : folder.getName();

  const files = folder.getFiles();
  while (files.hasNext()) {
    const file = files.next();
    if (file.getMimeType() === "application/vnd.google-apps.shortcut") continue;

    results.push({
      id: file.getId(),
      name: file.getName(),
      path: currentPath,
      fullPath: currentPath + "/" + file.getName(),
      mimeType: file.getMimeType(),
      size: file.getSize(),
      created: file.getDateCreated().toISOString(),
      modified: file.getLastUpdated().toISOString(),
      url: file.getUrl()
    });
  }

  const subs = folder.getFolders();
  while (subs.hasNext()) {
    const sub = subs.next();
    if (sub.getName().startsWith("_BACKUP")) continue;
    collectFilesRecursive_(sub, currentPath, results);
  }
}

// === STRINGS ===

function capitalizeFirst_(str) {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function chunkString_(str, size) {
  const chunks = [];
  for (let i = 0; i < str.length; i += size) {
    chunks.push(str.substring(i, i + size));
  }
  return chunks;
}

// === STORAGE (PropertiesService) ===

/** Sauvegarde les donnees d'audit (chunke si > 8KB) */
function storeAuditData_(files, anomalies) {
  const props = PropertiesService.getScriptProperties();
  const filesJson = JSON.stringify(files);

  if (filesJson.length > 8000) {
    const chunks = chunkString_(filesJson, 8000);
    props.setProperty("audit_files_chunks", String(chunks.length));
    chunks.forEach((chunk, i) => props.setProperty("audit_files_" + i, chunk));
  } else {
    props.setProperty("audit_files_chunks", "0");
    props.setProperty("audit_files", filesJson);
  }

  props.setProperty("audit_anomalies", JSON.stringify(anomalies));
}

/** Charge les donnees d'audit stockees */
function loadAuditData_() {
  const props = PropertiesService.getScriptProperties();
  const nbChunks = parseInt(props.getProperty("audit_files_chunks") || "0");

  let filesJson;
  if (nbChunks > 0) {
    const parts = [];
    for (let i = 0; i < nbChunks; i++) parts.push(props.getProperty("audit_files_" + i));
    filesJson = parts.join("");
  } else {
    filesJson = props.getProperty("audit_files");
  }

  if (!filesJson) return null;

  const anomaliesJson = props.getProperty("audit_anomalies");
  return {
    files: JSON.parse(filesJson),
    anomalies: anomaliesJson ? JSON.parse(anomaliesJson) : null
  };
}

// === CLASSIFICATION CHEMIN ===

function detectCategory_(path) {
  const map = {
    "01_ADMIN": "ADMIN",
    "02_TEMPLATES": "TEMPLATES",
    "03_PROMPTS": "PROMPTS",
    "04_ASSETS": "ASSETS",
    "05_MONETISATION": "MONETISATION",
    "06_SCHOOLS_WP_EDITORIAL": "EDITORIAL",
    "07_AUTOMATION": "AUTOMATION",
    "99_ARCHIVES": "ARCHIVES"
  };
  for (const [key, val] of Object.entries(map)) {
    if (path.includes(key)) return val;
  }
  return "NON CLASSE";
}

function detectStatus_(path) {
  if (path.includes("01_DRAFT")) return "DRAFT";
  if (path.includes("02_VALID")) return "VALIDE";
  if (path.includes("03_LIVE")) return "LIVE";
  if (path.includes("99_ARCHIVES")) return "ARCHIVES";
  return "N/A";
}

// === RACCOURCIS DRIVE ===

/**
 * Cree un raccourci Drive vers un fichier.
 * Prerequis : activer le service Drive API (Services > Drive API > Ajouter)
 */
function createShortcut_(fileId, targetFolderId) {
  const file = DriveApp.getFileById(fileId);
  Drive.Files.create({
    name: file.getName(),
    mimeType: "application/vnd.google-apps.shortcut",
    shortcutDetails: { targetId: fileId },
    parents: [targetFolderId]
  }, null, { supportsAllDrives: true });
  Logger.log("[SHORTCUT] " + file.getName() + " -> " + targetFolderId);
}
