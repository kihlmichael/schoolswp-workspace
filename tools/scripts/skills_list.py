from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 20)
        self.set_text_color(41, 128, 185)
        self.cell(0, 15, 'Claude Code - Liste des Skills', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(52, 73, 94)
        self.set_fill_color(236, 240, 241)
        self.cell(0, 10, title, fill=True, new_x='LMARGIN', new_y='NEXT')
        self.ln(3)

    def skill_entry(self, name, command, description):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(41, 128, 185)
        self.cell(60, 7, name)
        self.set_font('Courier', '', 10)
        self.set_text_color(39, 174, 96)
        self.cell(50, 7, command)
        self.ln()
        self.set_font('Helvetica', '', 9)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 5, description)
        self.ln(2)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# Skills n8n
pdf.section_title('Skills n8n (Automatisation)')
skills_n8n = [
    ('n8n-code-javascript', '/n8n-code-javascript', 'Ecrire du code JavaScript dans les nodes Code n8n (syntaxe $input/$json/$node, requetes HTTP, dates)'),
    ('n8n-code-python', '/n8n-code-python', 'Ecrire du code Python dans les nodes Code n8n (syntaxe _input/_json/_node)'),
    ('n8n-expression-syntax', '/n8n-expression-syntax', 'Valider et corriger la syntaxe des expressions n8n ({{$json}}, webhooks)'),
    ('n8n-mcp-tools-expert', '/n8n-mcp-tools-expert', 'Guide expert pour utiliser les outils MCP n8n (recherche nodes, templates, workflows)'),
    ('n8n-node-configuration', '/n8n-node-configuration', 'Configuration des nodes n8n (proprietes, champs requis, patterns)'),
    ('n8n-validation-expert', '/n8n-validation-expert', 'Interpreter les erreurs de validation n8n et les corriger'),
    ('n8n-workflow-patterns', '/n8n-workflow-patterns', 'Patterns architecturaux pour workflows (webhooks, API, DB, agents IA)'),
]
for name, cmd, desc in skills_n8n:
    pdf.skill_entry(name, cmd, desc)

# Skills Metiers schoolsWP
pdf.section_title('Skills Metiers schoolsWP')
skills_metiers = [
    ('01_LinkedIn', '/01_LinkedIn', 'Automatisation LinkedIn : posts, profil, analytics, leads'),
    ('02_YouTube', '/02_YouTube', 'Production video YouTube : upload, SEO, thumbnails, playlists'),
    ('03_Facebook', '/03_Facebook', 'Facebook : pages, groupes, publicite, Messenger'),
    ('04_WordPress', '/04_WordPress', 'WordPress : articles, pages, plugins, themes, WooCommerce'),
    ('05_Branding', '/05_Branding', 'Creation de contenu voix schoolsWP (draft, rewrite, repurpose, check, calendar, bio)'),
    ('06_Dev', '/06_Dev', 'Developpement WordPress avance (blocks, themes, plugins, REST API, Interactivity API)'),
    ('07_Marketing', '/07_Marketing', 'Marketing : CRO, copywriting, SEO, emails, pricing, analytics'),
    ('08_GoogleDrive', '/08_GoogleDrive', 'Google Drive : upload, dossiers, partage, organisation'),
]
for name, cmd, desc in skills_metiers:
    pdf.skill_entry(name, cmd, desc)

# Skills Communication
pdf.section_title('Skills Communication')
skills_comm = [
    ('09_Discord', '/09_Discord', 'Controle Discord : messages, reactions, sondages, threads, channels, moderation'),
    ('10_Slack', '/10_Slack', 'Controle Slack : messages, reactions, epinglage dans channels/DMs'),
    ('11_WhatsApp', '/11_WhatsApp', 'Envoi de messages WhatsApp via CLI wacli'),
    ('12_Notion', '/12_Notion', 'API Notion : pages, bases de donnees, blocs'),
]
for name, cmd, desc in skills_comm:
    pdf.skill_entry(name, cmd, desc)

# Skills IA / Generation
pdf.section_title('Skills IA / Generation')
skills_ia = [
    ('13_Gemini', '/13_Gemini', 'CLI Gemini : Q&A, resumes, generation one-shot'),
    ('14_OpenAI-ImageGen', '/14_OpenAI-ImageGen', 'Generation d\'images en batch via API OpenAI + galerie HTML'),
    ('15_OpenAI-Whisper', '/15_OpenAI-Whisper', 'Transcription audio locale avec Whisper (sans API)'),
    ('16_OpenAI-Whisper-API', '/16_OpenAI-Whisper-API', 'Transcription audio via API OpenAI Whisper'),
]
for name, cmd, desc in skills_ia:
    pdf.skill_entry(name, cmd, desc)

# Skill Utilitaire
pdf.section_title('Skill Utilitaire')
pdf.skill_entry('keybindings-help', '/keybindings-help', 'Personnaliser les raccourcis clavier Claude Code')

# Summary
pdf.ln(10)
pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(52, 73, 94)
pdf.cell(0, 10, 'Total : 24 skills repartis en 5 categories', align='C')

pdf.output('d:/VS Code/CLAUDE CODE/Claude_Code_Skills.pdf')
print('PDF cree avec succes!')
