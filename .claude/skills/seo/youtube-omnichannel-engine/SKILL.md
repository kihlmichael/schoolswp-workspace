---
name: youtube-omnichannel-engine
description: |
  Système de PILOTAGE ROI/scoring YouTube multi-canal schoolsWP (pas de production brute). Construit le tableau complet avec 4 onglets : PARAMS (poids et taux), CONTENT (ROI + scoring + priorité + completion), LIBRARY (angles/hooks/CTA/offres), ACTUALS (réel + deltas avec auto-remplissage). Organise le funnel YouTube → Article → LinkedIn → Newsletter avec métriques consolidées et dashboard.
  Utiliser ce skill quand l'utilisateur demande : "machine YouTube omnicanale", "ROI YouTube", "scoring YouTube", "tableau YouTube complet", "pilotage vidéo multi-canal", "système YouTube → Article → LinkedIn → Newsletter", "distribution omnicanale", "deltas YouTube", "machine de guerre YouTube", "dashboard YouTube".
  NE PAS utiliser pour : production d'une vidéo longue (voir `schoolswp-youtube-studio`), création d'un Short (voir `youtube-shorts-schoolswp`), miniatures (voir `thumbnail-strategist`), extraction de données d'une vidéo existante (voir `youtube-extractor`).
---

# YouTube Omnichannel Engine (schoolsWP)

Tu fournis un systeme complet :
1) Tableau CONTENT avec ROI + scoring + priorite + completion
2) Onglet PARAMS avec poids et taux
3) Onglet LIBRARY (angles/hooks/CTA/offres)
4) Onglet ACTUALS (reel) + deltas
5) Validation + mise en forme + dashboard

Style schoolsWP : direct, concret, phrases courtes.

## Regles de redaction

- Phrases courtes
- Bullets
- Zero blabla
- Si info manque : “Hypothese : …”

## Sortie obligatoire


Toujours produire ces sections :

1) Onglet PARAMS
2) Onglet CONTENT (colonnes + formules)
3) Validation des donnees
4) Mise en forme conditionnelle
5) Onglet DASHBOARD (KPI)
6) Onglet LIBRARY (banque)
7) Onglet ACTUALS (reel)
8) Auto-remplissage (LIBRARY -> CONTENT)
9) Deltas (reel vs estime)
10) Actions suivantes (3 max)
11) Automations Google Sheets (Apps Script)

## Reference a utiliser


### PARAMS (A1)
Cle	Valeur
Poids_Autorite_Intention	0,25
Poids_Autorite_Evergreen	0,25
Poids_Autorite_Differenciation	0,20
Poids_Autorite_Demande_SEO	0,30
Poids_Conv_Intent_Business	0,30
Poids_Conv_LeadMagnet_Fit	0,25
Poids_Conv_Offre_Fit	0,25
Poids_Conv_Urgence_Pain	0,20
CTR_YT	0,05
CTR_Endscreen	0,012
CTR_Description	0,008
CTR_Comment_Pinned	0,004
CVR_Landing_Lead	0,22
CVR_Lead_to_Sale	0,06
Valeur_Lead	7
Profit_Moyen_Vente	120
Temps_Prod_Heures	6
Cout_Horaire	45
Budget_Outsourcing	0

### CONTENT (A1)
ID	Keyword principal	Persona	Intention	Angle	Promesse	Hook	Format	Duree	CTA	Lead magnet	Offre	Funnel Stage	Status	Omni Status	Est_Impressions	Est_Vues	Est_Clicks_CTA	Est_Leads	Est_Ventes	Est_Revenu	Est_Cout	Est_Profit	ROI_%	Score_Autorite	Score_Conversion	Score_Global	Priorite	%_Completion	Autorite_Intention(1-5)	Autorite_Evergreen(1-5)	Autorite_Diff(1-5)	Autorite_DemandeSEO(1-5)	Conv_IntentBusiness(1-5)	Conv_LeadMagnetFit(1-5)	Conv_OffreFit(1-5)	Conv_UrgencePain(1-5)	URL_Video	URL_Article	URL_LinkedIn	URL_Newsletter

### Formules (ligne 2)
Q2 (Est_Vues)
=SI(P2="";"";ARRONDI(P2*RECHERCHEV("CTR_YT";PARAMS!A:B;2;FAUX);0))

R2 (Est_Clicks_CTA)
=SI(Q2="";"";ARRONDI(Q2*(RECHERCHEV("CTR_Endscreen";PARAMS!A:B;2;FAUX)+RECHERCHEV("CTR_Description";PARAMS!A:B;2;FAUX)+RECHERCHEV("CTR_Comment_Pinned";PARAMS!A:B;2;FAUX));0))

S2 (Est_Leads)
=SI(R2="";"";ARRONDI(R2*RECHERCHEV("CVR_Landing_Lead";PARAMS!A:B;2;FAUX);0))

T2 (Est_Ventes)
=SI(S2="";"";ARRONDI(S2*RECHERCHEV("CVR_Lead_to_Sale";PARAMS!A:B;2;FAUX);0))

U2 (Est_Revenu)
=SI(S2="";"";ARRONDI(S2*RECHERCHEV("Valeur_Lead";PARAMS!A:B;2;FAUX)+T2*RECHERCHEV("Profit_Moyen_Vente";PARAMS!A:B;2;FAUX);0))

V2 (Est_Cout)
=ARRONDI(RECHERCHEV("Temps_Prod_Heures";PARAMS!A:B;2;FAUX)*RECHERCHEV("Cout_Horaire";PARAMS!A:B;2;FAUX)+RECHERCHEV("Budget_Outsourcing";PARAMS!A:B;2;FAUX);0)

W2 (Est_Profit)
=SI(U2="";"";U2-V2)

X2 (ROI_%)
=SI(U2="";"";SI(V2=0;"";W2/V2))

Y2 (Score_Autorite)
=SI(AB2="";"";ARRONDI((AB2/5)*RECHERCHEV("Poids_Autorite_Intention";PARAMS!A:B;2;FAUX)+(AC2/5)*RECHERCHEV("Poids_Autorite_Evergreen";PARAMS!A:B;2;FAUX)+(AD2/5)*RECHERCHEV("Poids_Autorite_Differenciation";PARAMS!A:B;2;FAUX)+(AE2/5)*RECHERCHEV("Poids_Autorite_Demande_SEO";PARAMS!A:B;2;FAUX);3))

Z2 (Score_Conversion)
=SI(AF2="";"";ARRONDI((AF2/5)*RECHERCHEV("Poids_Conv_Intent_Business";PARAMS!A:B;2;FAUX)+(AG2/5)*RECHERCHEV("Poids_Conv_LeadMagnet_Fit";PARAMS!A:B;2;FAUX)+(AH2/5)*RECHERCHEV("Poids_Conv_Offre_Fit";PARAMS!A:B;2;FAUX)+(AI2/5)*RECHERCHEV("Poids_Conv_Urgence_Pain";PARAMS!A:B;2;FAUX);3))

AA2 (Score_Global)
=SI(Y2="";"";ARRONDI(Y2*0,4+Z2*0,6;3))

AB2 (Priorite)
=SI(X2="";"";SI(X2>=2;"🔥 Priorite 1";SI(X2>=1;"✅ Priorite 2";SI(AA2>=0,7;"⭐ Priorite 3";"⏳ Backlog"))))

AC2 (%_Completion)
=SI(N2="";"";SOMME(SI(N2="Idée";0,10;SI(N2="Script";0,25;SI(N2="Tournage";0,45;SI(N2="Montage";0,65;SI(N2="Publié";0,75;0)))));SI(O2="Non décliné";0;SI(O2="Article publié";0,08;SI(O2="LinkedIn publié";0,08;SI(O2="Newsletter envoyée";0,09;SI(O2="Complet";0,25;0)))))))

### Validation des donnees
Status : Idée, Script, Tournage, Montage, Publié
Omni Status : Non décliné, Article publié, LinkedIn publié, Newsletter envoyée, Complet
Funnel Stage : TOFU, MOFU, BOFU

### Mise en forme conditionnelle
ROI_% : vert >=2, jaune 1-2, rouge <1
Priorite : couleurs par label
Status : Published vert, Montage/Tournage orange, Idee/Script gris
%_Completion : vert >=0,9, jaune 0,5-0,9, rouge <0,5

### DASHBOARD (KPI)
Nb contenus = NBVAL(CONTENT!A2:A)
Nb publies = NB.SI(CONTENT!N2:N;"Publié")
Nb omnicanal complet = NB.SI(CONTENT!O2:O;"Complet")
ROI moyen = MOYENNE.SI(CONTENT!X2:X;">0")
Profit total = SOMME(CONTENT!W2:W)
Leads estimes = SOMME(CONTENT!S2:S)
Ventes estimees = SOMME(CONTENT!T2:T)
Revenu estime = SOMME(CONTENT!U2:U)
Cout total = SOMME(CONTENT!V2:V)

### LIBRARY (banque)
Type	ID	Label/Titre	Contenu	Persona	Funnel	Tags
ANGLE	A01	No-code en 5 minutes	Meme sans dev : workflow en 5 min	Freelance / Solopreneur	MOFU	automation,roi
ANGLE	A02	Erreur classique	“Tu fais ca a la main ? Voila pourquoi tu perds du temps.”	Freelance	TOFU	productivite
ANGLE	A03	Demo avant explication	Je montre le resultat, puis je deconstruis	Mix	MOFU	demo,retention
HOOK	H01	Show result first	“Regarde : c’est deja automatise. Maintenant je te montre comment.”	Mix	MOFU	hook,result
HOOK	H02	Chiffre choc	“Tu perds 30% de ton temps avec ca.”	Freelance	TOFU	chiffre,autorite
HOOK	H03	Anti-blabla	“Pas de theorie. Demo. Maintenant.”	Mix	MOFU	punchy
CTA	C01	Template	“Telecharge le template (lien en description).”	Mix	MOFU	template
CTA	C02	Checklist	“Recupere la checklist schoolsWP.”	Debutant	TOFU	checklist
CTA	C03	Audit	“Si tu veux que je l’installe pour toi : audit en description.”	Agence / Freelance	BOFU	service
LEAD	L01	Template Automation CRM	Template : tags + triggers + workflow	Freelance	MOFU	crm,automation
LEAD	L02	Prompt Pack IA	Prompts + exemples + variantes	Solopreneur	TOFU	ia,contenu
OFFER	O01	Formation Automatisation	Formation + modules + templates	Freelance	MOFU	formation
OFFER	O02	Service setup automation	Setup complet + suivi	Agence / Freelance	BOFU	service
STRUCT	S01	Structure Demo 5 blocs	Probleme > Demo > Setup > Test > Optimisation	Mix	MOFU	structure
STRUCT	S02	Structure Guide	Contexte > Etapes > Erreurs > Checklist > CTA	Debutant	TOFU	guide

### ACTUALS (reel)
ID	Date publication	Impressions	Vues	CTR moyen	Duree moyenne	Clicks CTA	Leads	Ventes	Revenu	Cout reel

### Auto-remplissage (exemple)
Angle (texte) = SI(Angle_ID="";"";INDEX(FILTRE(LIBRARY!D:D;LIBRARY!B:B=Angle_ID);1))
Hook (texte) = SI(Hook_ID="";"";INDEX(FILTRE(LIBRARY!D:D;LIBRARY!B:B=Hook_ID);1))
CTA (texte) = SI(CTA_ID="";"";INDEX(FILTRE(LIBRARY!D:D;LIBRARY!B:B=CTA_ID);1))
Structure = SI(Struct_ID="";"";INDEX(FILTRE(LIBRARY!D:D;LIBRARY!B:B=Struct_ID);1))

### Deltas (reel vs estime)
Act_Vues = SIERREUR(RECHERCHEV($A2;ACTUALS!A:K;4;FAUX);"")
Act_Leads = SIERREUR(RECHERCHEV($A2;ACTUALS!A:K;8;FAUX);"")
Act_Ventes = SIERREUR(RECHERCHEV($A2;ACTUALS!A:K;9;FAUX);"")
Act_Revenu = SIERREUR(RECHERCHEV($A2;ACTUALS!A:K;10;FAUX);"")
Act_Cout = SIERREUR(RECHERCHEV($A2;ACTUALS!A:K;11;FAUX);"")
Act_Profit = SI(ET(Act_Revenu="";Act_Cout="");"";Act_Revenu-Act_Cout)
Delta_Profit = SI(OU(Act_Profit="";Est_Profit="");"";Act_Profit-Est_Profit)
Delta_ROI = SI(OU(Act_Cout="";Act_Cout=0;Act_Profit="");"";Act_Profit/Act_Cout - ROI_%)

### Automations Google Sheets (Apps Script)
Onglet SAISIE (A1:Q1) :
ID	Keyword principal	Keyword secondaire	Persona	Funnel Stage	Intention	Angle_ID	Hook_ID	Struct_ID	Format	Duree	CTA_ID	Lead_ID	Offer_ID	Est_Impressions	Status	Omni Status

Script (menu + ajout + marquage) :
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('schoolsWP')
    .addItem('➕ Ajouter idee (SAISIE → CONTENT)', 'addIdeaToContent')
    .addSeparator()
    .addItem('✅ Marquer comme Publie', 'markPublished')
    .addItem('🧩 Marquer Omnicanal = Complet', 'markOmniComplete')
    .addSeparator()
    .addItem('🔒 Proteger colonnes calculees', 'protectComputedColumns')
    .addToUi();
}

function addIdeaToContent() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const shInput = ss.getSheetByName('SAISIE');
  const shContent = ss.getSheetByName('CONTENT');
  if (!shInput || !shContent) throw new Error('Onglet SAISIE ou CONTENT introuvable.');

  const inputRange = shInput.getRange('A2:Q2');
  const v = inputRange.getValues()[0];

  const [
    id, keyword, keyword2, persona, funnel, intention,
    angleId, hookId, structId, format, duree,
    ctaId, leadId, offerId, estImpressions, status, omniStatus
  ] = v;

  const finalId = id || getNextId_();
  if (!keyword) {
    SpreadsheetApp.getUi().alert('Keyword principal obligatoire.');
    return;
  }

  const lastRow = shContent.getLastRow();
  const nextRow = Math.max(lastRow + 1, 2);
  const lastCol = shContent.getLastColumn();
  const templateRow = 2;

  shContent.getRange(templateRow, 1, 1, lastCol)
    .copyTo(shContent.getRange(nextRow, 1, 1, lastCol), { contentsOnly: false });

  const setCell = (col, val) => shContent.getRange(nextRow, col).setValue(val);
  setCell(1, finalId);
  setCell(2, keyword);
  setCell(3, keyword2);
  setCell(4, persona);
  setCell(5, funnel);
  setCell(6, intention);
  setCell(7, angleId);
  setCell(9, hookId);
  setCell(11, structId);
  setCell(13, format);
  setCell(14, duree);
  setCell(15, ctaId);
  setCell(17, leadId);
  setCell(19, offerId);
  setCell(21, status || 'Idée');
  setCell(22, omniStatus || 'Non décliné');
  setCell(23, estImpressions);

  inputRange.clearContent();
  shInput.getRange('P2').setValue('Idée');
  shInput.getRange('Q2').setValue('Non décliné');
  SpreadsheetApp.getUi().toast('Ajoute dans CONTENT ✅', 'schoolsWP', 3);
}

function getNextId_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName('CONTENT');
  const ids = sh.getRange('A2:A').getValues().flat().filter(String);
  const nums = ids.map(x => parseInt(x, 10)).filter(n => !isNaN(n));
  const next = (nums.length ? Math.max(...nums) + 1 : 1);
  return String(next).padStart(2, '0');
}

function markPublished() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName('CONTENT');
  const row = sh.getActiveRange().getRow();
  if (row < 2) return;
  sh.getRange(row, 21).setValue('Publié');
  if (!sh.getRange(row, 22).getValue()) sh.getRange(row, 22).setValue('Non décliné');
  SpreadsheetApp.getUi().toast('Status = Publié ✅', 'schoolsWP', 2);
}

function markOmniComplete() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName('CONTENT');
  const row = sh.getActiveRange().getRow();
  if (row < 2) return;
  sh.getRange(row, 22).setValue('Complet');
  SpreadsheetApp.getUi().toast('Omnicanal = Complet ✅', 'schoolsWP', 2);
}

function protectComputedColumns() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName('CONTENT');
  if (!sh) throw new Error('Onglet CONTENT introuvable.');
  const startCol = 24; // X
  const endCol = 51;   // AY
  const numCols = endCol - startCol + 1;
  const range = sh.getRange(1, startCol, sh.getMaxRows(), numCols);
  const protection = range.protect().setDescription('schoolsWP — Colonnes calculees (ne pas toucher)');
  protection.removeEditors(protection.getEditors());
  protection.setWarningOnly(true);
}

## Checklist d’installation (Google Sheets)


1) Creer les onglets : PARAMS, LIBRARY, ACTUALS, CONTENT, DASHBOARD, SAISIE
2) Coller PARAMS (A1), LIBRARY (A1), ACTUALS (A1), CONTENT (A1)
3) Valider les listes deroulantes (FUNNEL, STATUS, OMNI)
4) Copier les formules de la ligne 2 dans CONTENT
5) Ajouter le script Apps Script et autoriser
6) Tester SAISIE -> CONTENT
7) Activer la protection des colonnes calculees
8) Appliquer la mise en forme conditionnelle
9) Verifier le DASHBOARD (KPI + Top ROI + Top Score)
