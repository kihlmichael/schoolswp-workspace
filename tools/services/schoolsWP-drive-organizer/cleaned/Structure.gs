/**
 * schoolsWP Drive Organizer v3.0 – Creation de l'arborescence
 *
 * Point d'entree : createFullStructure()
 * Verification  : verifyStructure()
 *
 * Securite : ne supprime rien, idempotent (skip si dossier existe deja).
 */

/** Cree toute l'arborescence PROMPTS_schoolsWP en une seule passe */
function createFullStructure() {
  const startTime = new Date();
  Logger.log("=== schoolsWP Drive Structure Creator v3.0 ===");

  const parentFolder = resolveParentFolder_();
  const rootFolder = getOrCreateFolder(parentFolder, ROOT_FOLDER_NAME);
  Logger.log("Racine : " + rootFolder.getName() + " (ID: " + rootFolder.getId() + ")");

  const result = createFoldersRecursive_(rootFolder, STRUCTURE, "");

  const duration = (new Date() - startTime) / 1000;
  Logger.log("---");
  Logger.log("Crees     : " + result.created);
  Logger.log("Existants : " + result.existing);
  Logger.log("Duree     : " + duration + "s");
  Logger.log("URL       : " + rootFolder.getUrl());

  createLogFile_(rootFolder, result.created, result.existing, duration);
  return rootFolder;
}

/** Cree les dossiers recursivement depuis un objet de structure */
function createFoldersRecursive_(parent, structure, indent) {
  let created = 0;
  let existing = 0;

  for (const [name, children] of Object.entries(structure)) {
    const { folder, created: wasCreated } = getOrCreateFolderTracked(parent, name);
    Logger.log(indent + (wasCreated ? "[CREE] " : "[EXISTE] ") + name);
    wasCreated ? created++ : existing++;

    if (children && Object.keys(children).length > 0) {
      const child = createFoldersRecursive_(folder, children, indent + "  ");
      created += child.created;
      existing += child.existing;
    }
  }

  return { created, existing };
}

/** Verifie l'arborescence existante dans le Drive */
function verifyStructure() {
  const parentFolder = resolveParentFolder_();
  const it = parentFolder.getFoldersByName(ROOT_FOLDER_NAME);
  if (!it.hasNext()) {
    Logger.log("ERREUR : " + ROOT_FOLDER_NAME + " non trouve !");
    return;
  }

  const root = it.next();
  Logger.log("Verification : " + root.getName());
  Logger.log("URL : " + root.getUrl());
  Logger.log("");

  const counts = listFoldersRecursive_(root, 0);
  Logger.log("");
  Logger.log("Total dossiers : " + counts.folders);
  Logger.log("Total fichiers : " + counts.files);
}

/** Liste recursive pour verification (affiche l'arbre dans les logs) */
function listFoldersRecursive_(folder, depth) {
  const indent = "  ".repeat(depth);
  let folders = 0;
  let files = 0;

  const subs = folder.getFolders();
  while (subs.hasNext()) {
    const sub = subs.next();
    folders++;
    Logger.log(indent + "[D] " + sub.getName());
    const child = listFoldersRecursive_(sub, depth + 1);
    folders += child.folders;
    files += child.files;
  }

  const fileIt = folder.getFiles();
  while (fileIt.hasNext()) {
    files++;
    Logger.log(indent + "[F] " + fileIt.next().getName());
  }

  return { folders, files };
}

/** Cree un fichier de log dans 01_ADMIN/01_Regles-et-Index */
function createLogFile_(rootFolder, created, existing, duration) {
  try {
    const adminFolder = getOrCreateFolder(rootFolder, "01_ADMIN");
    const indexFolder = getOrCreateFolder(adminFolder, "01_Regles-et-Index");
    const today = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyy-MM-dd");

    const content = [
      "# Log de creation \u2013 PROMPTS_schoolsWP",
      "",
      "**Date** : " + today,
      "**Script** : schoolsWP Drive Organizer v3.0",
      "",
      "| Metrique | Valeur |",
      "|----------|--------|",
      "| Dossiers crees | " + created + " |",
      "| Dossiers existants | " + existing + " |",
      "| Duree | " + duration + "s |",
      "| URL racine | " + rootFolder.getUrl() + " |",
      "",
      "---",
      "*Genere automatiquement par schoolsWP Drive Organizer*"
    ].join("\n");

    const logName = today + " \u2013 Log-Creation \u2013 ADMIN.md";
    indexFolder.createFile(logName, content, MimeType.PLAIN_TEXT);
    Logger.log("Log cree : " + logName);
  } catch (e) {
    Logger.log("Erreur log : " + e.message);
  }
}
