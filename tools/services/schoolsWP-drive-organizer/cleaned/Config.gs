/**
 * schoolsWP Drive Organizer v3.0 – Configuration
 *
 * Toutes les constantes partagees entre les fichiers du projet.
 * Modifier ici pour adapter le projet a un autre contexte.
 */

// === DOSSIERS ===

/** null = racine Mon Drive | "1ABC...xyz" = ID dossier specifique */
const PARENT_FOLDER_ID = null;
const ROOT_FOLDER_NAME = "PROMPTS_schoolsWP";

/** ID du dossier SOURCE existant a auditer/migrer */
const SOURCE_FOLDER_ID = "1O_GbYXkAnnsix1Gowuv7EuvXL5qRdS_N";

/** null = cherche PROMPTS_schoolsWP a la racine. Meme ID que SOURCE si reorg in-place */
const TARGET_ROOT_ID = null;

const MAPPING_SHEET_NAME = "schoolsWP \u2013 Mapping Migration";
const INDEX_SHEET_NAME = "schoolsWP \u2013 Index Global";

// === SEPARATEUR UNIVERSEL ===

const SEP = " \u2013 ";

// === ARBORESCENCE COMPLETE ===
// Les sous-dossiers de statut sont directement integres dans TEMPLATES et PROMPTS.
// Plus besoin de double passe.

const STATUS_DIRS = {
  "01_DRAFT": {},
  "02_VALID\u00c9": {},
  "03_LIVE": {},
  "99_ARCHIVES": {}
};

const STRUCTURE = {
  "01_ADMIN": {
    "01_Regles-et-Index": {},
    "02_Checklists-Qualite": {}
  },
  "02_TEMPLATES": {
    "01_Editorial_SEO": STATUS_DIRS,
    "02_Email_CRM_FluentCRM": STATUS_DIRS,
    "03_Conversion_Landing": STATUS_DIRS,
    "04_YouTube_Social": STATUS_DIRS,
    "05_Affiliation_Monetisation": STATUS_DIRS,
    "06_Automation_SOP": STATUS_DIRS
  },
  "03_PROMPTS": {
    "01_Editorial_SEO": STATUS_DIRS,
    "02_Email_CRM": STATUS_DIRS,
    "03_Conversion": STATUS_DIRS,
    "04_Affiliation": STATUS_DIRS,
    "05_Assets": STATUS_DIRS,
    "06_Automation": STATUS_DIRS
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

// === REFERENTIELS DE NOMMAGE ===

const VALID_TYPES = ["Prompt", "Template", "SOP", "Brief", "Checklist", "Audit"];

const EDITORIAL_TYPES_MAP = {
  "article": "Prompt",
  "tutoriel": "Prompt",
  "guide": "Template",
  "video": "Prompt",
  "vid\u00e9o": "Prompt",
  "newsletter": "Prompt",
  "note": "Brief"
};

const VALID_USAGES = [
  "Article", "SEO", "Email", "Landing", "Affiliation",
  "Ads", "YouTube", "Social", "Asset", "Automation", "ADMIN"
];

const MONETISATION_KEYWORDS = [
  "lancement", "promo", "evergreen", "s\u00e9quence", "sequence",
  "campagne", "black friday", "soldes", "offre", "formation",
  "produit", "business", "partenariat"
];

const EMAIL_KEYWORDS = [
  "email", "mail", "crm", "fluent", "fluentcrm",
  "newsletter", "s\u00e9quence", "sequence", "welcome",
  "onboarding", "relance", "nurturing", "drip"
];

const VALID_EXTENSIONS = ["md", "docx", "txt", "json", "pdf", "xlsx", "py", "js"];

/** Regex format complet : AAAA-MM-JJ – Sujet – Type – Usage [– Infos].ext */
const NAME_REGEX = /^\d{4}-\d{2}-\d{2} \u2013 .+ \u2013 (Prompt|Template|SOP|Brief|Checklist|Audit) \u2013 (Article|SEO|Email|Landing|Affiliation|Ads|YouTube|Social|Asset|Automation|ADMIN)/;
