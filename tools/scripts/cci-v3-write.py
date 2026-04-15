"""Write v3 tab: v2 content + 12 Nancy formations from cciformation-eesc.fr."""

from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SHEET_ID = "1YLtlrrOgZAdyamYdEu_uOLz5lzvSJKfS4ykDCSfjKm8"
TOKEN = Path(__file__).parent / "token-cci-v2.json"
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
svc = build("sheets", "v4", credentials=creds)

# Read v2 data to carry it over
v2 = svc.spreadsheets().values().get(spreadsheetId=SHEET_ID, range="v2!A1:R100").execute().get("values", [])

# New Nancy rows (continue ID numbering after 24)
NANCY = [
    [
        "25",
        "Construire une strategie marketing digitale",
        "10/10 ESSENTIELLE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Marketing digital",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "2 jours",
        "A verifier (CCI EESC non affiche)",
        "A verifier",
        "A verifier (catalogue 2026)",
        "🔥 CŒUR SCHOOLSWP : strategie marketing digital complete. Directement applicable au positionnement schoolsWP.",
        "A etudier en priorite - demander fiche 2026",
        "Complete v2 #13 (marketing operationnel Metz)",
        "Tarif/dates non affiches - contact EESC Laxou requis",
        "https://cciformation-eesc.fr/formations/construire-une-strategie-marketing-digitale",
    ],
    [
        "26",
        "Developper son chiffre d'affaires grace a l'IA",
        "10/10 ESSENTIELLE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Intelligence artificielle / Business",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "A verifier (probablement 1-2j)",
        "A verifier",
        "A verifier",
        "A verifier",
        "🔥 TITRE DIRECT : 'Developper son CA grace a l'IA'. Exactement l'angle schoolsWP - si catalogue 2026 confirme, incontournable.",
        "A etudier en priorite - PRIORITE ABSOLUE 2026",
        "Complete v1 #3 (IA-Commerciaux) avec angle CA business",
        "Duree/tarif/sessions a confirmer",
        "https://cciformation-eesc.fr/formations/developper-son-chiffre-daffaire-grace-a-lia",
    ],
    [
        "27",
        "Construire sa strategie commerciale",
        "9/10 TRES HAUTE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Commercial / Strategie",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "2 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "Structurer l'offre schoolsWP, cibles, canaux, tarification. Indispensable avant IA-vente. Pilier strategie.",
        "A etudier en priorite",
        "Nouveau theme (strategie commerciale structuree)",
        "Tarif/dates non affiches",
        "https://cciformation-eesc.fr/formations/construire-sa-strategie-commerciale",
    ],
    [
        "28",
        "Integrer l'IA dans mon activite professionnelle",
        "9/10 TRES HAUTE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Intelligence artificielle / Operationnel",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "A verifier (probablement 1-2j)",
        "A verifier",
        "A verifier",
        "A verifier",
        "IA operationnelle hands-on. Complement direct des formations IA-metier. Probablement la plus actionnable du catalogue Nancy.",
        "A etudier en priorite",
        "Complement IA-CODIR (v1 #2), cible solo/independant",
        "Duree et contenu precis a demander",
        "https://cciformation-eesc.fr/formations/integrer-lintelligence-artificielle-dans-mon-activite-professionnelle",
    ],
    [
        "29",
        "Intelligence artificielle et Excel",
        "9/10 TRES HAUTE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Bureautique / IA",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "1 jour",
        "A verifier (env 300-500 EUR marche CCI)",
        "A verifier",
        "A verifier",
        "🔥 Excel + IA hands-on : reporting GA4, KPI schoolsWP, automatisation analyses. Format court 1j ideal.",
        "A etudier en priorite - alternative v1 #5 (Excel TCD)",
        "Fait doublon potentiel avec v1 #5 (Excel TCD + IA Metz)",
        "Comparer contenu precis v1 #5 vs cette offre Nancy",
        "https://cciformation-eesc.fr/formations/intelligence-artificielle-et-excel",
    ],
    [
        "30",
        "CCE - Mettre en oeuvre actions de communication numerique",
        "10/10 ESSENTIELLE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Communication numerique / CCE",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "4 jours",
        "A verifier (CCE)",
        "CCE",
        "A verifier",
        "🔥 CCE CERTIFIANTE + communication numerique entreprise : site web, reseaux sociaux, SEO, analytics. Directement au cœur schoolsWP.",
        "A etudier en priorite - CCE = diplome CCI",
        "Nouveau theme (CCE communication numerique)",
        "Tarif/sessions a demander - format 4j interessant",
        "https://cciformation-eesc.fr/formations/cce-mettre-en-oeuvre-des-actions-de-communication-numerique-dans-lentreprise",
    ],
    [
        "31",
        "Creation de site web WordPress",
        "9/10 TRES HAUTE",
        "Priorite 1",
        "Nouvelle Nancy",
        "WordPress / Web",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "3 jours / 21h",
        "A verifier",
        "A verifier",
        "A verifier",
        "🔥 WORDPRESS DIRECT ! Seule formation CCI 57+54 qui cible explicitement WordPress. Meme si tu maitrises deja, utile pour valider/certifier la competence pour les eleves schoolsWP.",
        "A etudier - valeur validation pour schoolsWP",
        "Aucun equivalent v1 ou v2",
        "Verifier le niveau (debutant vs pro) - si debutant, ecarter",
        "https://cciformation-eesc.fr/formations/formation-creation-de-site-web-wordpress-dreamweaver",
    ],
    [
        "32",
        "Initiation a Office 365 et Copilot",
        "7/10 HAUTE",
        "Priorite 2",
        "Nouvelle Nancy",
        "Bureautique / IA",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "3 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "Copilot M365 hands-on : Word/Excel/PPT/Teams + IA. Utile si passage Office 365 ou formation d'eleves.",
        "A confirmer - utilite marginale si deja ChatGPT/Claude",
        "Complement suite IA",
        "Verifier version Copilot (Pro M365 vs gratuit)",
        "https://cciformation-eesc.fr/formations/initiation-a-office-365-et-copilot",
    ],
    [
        "33",
        "Piloter la mise en conformite RGPD en TPE/PME",
        "8/10 HAUTE",
        "Priorite 1",
        "Nouvelle Nancy",
        "Juridique / Donnees",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "5 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "RGPD TPE/PME : registre traitements, DPIA, droits des personnes. OBLIGATOIRE pour FluentCRM/TutorLMS (donnees eleves). Protection juridique schoolsWP.",
        "A etudier en priorite - enjeu legal direct",
        "Nouveau theme (conformite/RGPD)",
        "Format 5j peut-etre overkill pour solopreneur - verifier si format court dispo",
        "https://cciformation-eesc.fr/formations/piloter-la-mise-en-conformite-des-modalites-de-traitement-et-de-protection-des-donnees-personnelles-en-tpe-pme-en-presentiel-ou-en-distanciel",
    ],
    [
        "34",
        "S'initier a la cybersecurite en entreprise",
        "7/10 HAUTE",
        "Priorite 2",
        "Nouvelle Nancy",
        "Cybersecurite",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "2 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "Hygiene cyber TPE : essentiel pour proteger site WordPress (schoolswp.com) + donnees clients. Recommande si pas deja maitrise.",
        "A confirmer - utile mais non critique si deja Wordfence/SecuPress configures",
        "Nouveau theme",
        "Verifier niveau (basique vs avance)",
        "https://cciformation-eesc.fr/formations/sinitier-a-la-cybersecurite-en-entreprise",
    ],
    [
        "35",
        "Ameliorer ses ecrits professionnels",
        "7/10 HAUTE",
        "Priorite 2",
        "Nouvelle Nancy",
        "Communication ecrite",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "2 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "Copywriting, emails commerciaux, briefs. Utile pour les 500+ articles schoolsWP + emails FluentCRM. A comparer avec formation IA-marketing qui couvre en partie.",
        "A confirmer - doublon partiel avec marketing+IA",
        "Complement marketing operationnel",
        "Format 2j classique",
        "https://cciformation-eesc.fr/formations/ameliorer-ses-ecrits-professionnels",
    ],
    [
        "36",
        "Optimiser son organisation et gerer son temps",
        "6/10 MOYENNE",
        "Priorite 2",
        "Nouvelle Nancy",
        "Productivite",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "2 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "Productivite solo-entrepreneur : priorisation, planification, gestion interruption. Solide mais largement couvert par tes propres contenus.",
        "A surveiller - non critique",
        "Nouveau theme (productivite)",
        "Valeur marginale si methodes deja en place",
        "https://cciformation-eesc.fr/formations/optimiser-son-organisation-et-gerer-son-temps",
    ],
    [
        "37",
        "Maitriser les fondamentaux de la vente (Nancy)",
        "8/10 HAUTE",
        "Priorite 2",
        "Nouvelle Nancy - doublon potentiel v2#12",
        "Commercial / Vente",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "3 jours",
        "A verifier",
        "A verifier",
        "A verifier",
        "Equivalent v2 #12 (Metz) mais format 3 jours au lieu de 1-2. Plus approfondi. Choisir entre les 2 selon disponibilite/deplacement.",
        "A comparer avec v2 #12 - ne faire qu'un des 2",
        "Doublon fonctionnel v2 #12",
        "Verifier si programme et tarif differents",
        "https://cciformation-eesc.fr/formations/maitriser-les-fondamentaux-de-la-vente",
    ],
    [
        "38",
        "CCE - Developper la qualite au service du client (Nancy)",
        "7/10 HAUTE",
        "Priorite 2",
        "Nouvelle Nancy - doublon v2#22",
        "Relation client / CCE",
        "Presentiel ou distanciel",
        "Nancy (Laxou)",
        "cciformation-eesc.fr",
        "2 jours",
        "A verifier",
        "CCE",
        "A verifier",
        "Equivalent v2 #22 (Metz) version Nancy. 2 jours. Meme CCE. Choisir selon dispo.",
        "A comparer avec v2 #22 - ne faire qu'un",
        "Doublon fonctionnel v2 #22",
        "Comparer tarif/sessions 2026",
        "https://cciformation-eesc.fr/formations/cce-developper-la-qualite-au-service-du-client-2",
    ],
]

# Create v3 tab
try:
    svc.spreadsheets().batchUpdate(
        spreadsheetId=SHEET_ID,
        body={
            "requests": [
                {"addSheet": {"properties": {"title": "v3", "gridProperties": {"rowCount": 80, "columnCount": 20}}}}
            ]
        },
    ).execute()
    print("Tab 'v3' created.")
except Exception as e:
    if "already exists" not in str(e):
        raise
    print("Tab 'v3' already exists - overwriting.")

# Build content: same meta + legend + v2 rows + Nancy rows
meta = [
    [
        "CCI Grand Est - Formations 2026 - schoolsWP v3 | v2 + scrape 2026-04-12 cciformation-eesc.fr (Nancy/Laxou) | Sources: campus-moselle.cci.fr + moselle.cci.fr + cciformation-eesc.fr"
    ]
]
legend = [
    [
        "LEGENDE : Pertinence /10 (10=essentielle). Priorite 1 (immediat), 2 (cette annee), 3 (surveiller/ecarter). 'A verifier' = non affiche publiquement CCI - contact requis. 14 nouvelles formations Nancy (#25-38)."
    ]
]

body_rows = v2[3:]  # skip meta+legend+blank from v2, keep headers + data
values = meta + legend + [[""]] + body_rows + NANCY

svc.spreadsheets().values().update(
    spreadsheetId=SHEET_ID, range="v3!A1", valueInputOption="RAW", body={"values": values}
).execute()

# Format
sheet_id = next(
    s["properties"]["sheetId"]
    for s in svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()["sheets"]
    if s["properties"]["title"] == "v3"
)
svc.spreadsheets().batchUpdate(
    spreadsheetId=SHEET_ID,
    body={
        "requests": [
            {
                "repeatCell": {
                    "range": {"sheetId": sheet_id, "startRowIndex": 3, "endRowIndex": 4},
                    "cell": {
                        "userEnteredFormat": {
                            "textFormat": {"bold": True},
                            "backgroundColor": {"red": 0.82, "green": 0.95, "blue": 0.82},
                        }
                    },
                    "fields": "userEnteredFormat(textFormat,backgroundColor)",
                }
            },
            {
                "updateSheetProperties": {
                    "properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": 4}},
                    "fields": "gridProperties.frozenRowCount",
                }
            },
        ]
    },
).execute()

print(
    f"v3 written: {len(body_rows) - 1} v2 rows + {len(NANCY)} new Nancy rows = {len(body_rows) - 1 + len(NANCY)} total formations"
)
print(f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid={sheet_id}")
