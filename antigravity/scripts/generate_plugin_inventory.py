import json
import os
import csv

output_json_path = r"C:\Users\conta\.gemini\antigravity\brain\da237c9e-3c34-4c74-9a5e-bcf40c14d1fd\.system_generated\steps\290\output.txt"

if not os.path.exists(output_json_path):
    print("Error: JSON output file not found.")
    exit(1)

with open(output_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# The list of plugins is in raw_data["data"]["stdout"] (which is a JSON string)
stdout_str = raw_data["data"]["stdout"]
plugins = json.loads(stdout_str)

# Mapping of slug to beautiful display name, category, and descriptive comment
mappings = {
    # 1. Fluent Ecosystem
    "fluent-crm": ("FluentCRM", "Écosystème Fluent", "Gestionnaire de relation client local au cœur du système"),
    "fluentcampaign-pro": ("FluentCRM Campaign Pro", "Écosystème Fluent", "Fonctionnalités avancées de marketing automation et séquences d'emails"),
    "fluent-boards": ("Fluent Boards", "Écosystème Fluent", "Gestionnaire de projets et de tâches visuel (type Trello) local"),
    "fluent-boards-pro": ("Fluent Boards Pro", "Écosystème Fluent", "Fonctionnalités pro pour la gestion de tâches et de projets en équipe"),
    "fluent-booking": ("Fluent Booking", "Écosystème Fluent", "Planificateur de rendez-vous local (alternative Cal.com/Calendly)"),
    "fluent-booking-pro": ("Fluent Booking Pro", "Écosystème Fluent", "Intégrations avancées de calendrier, SMS, et visioconférences"),
    "fluent-cart": ("FluentCart", "Écosystème Fluent", "Moteur de vente de produits et tunnels de conversion local"),
    "fluent-cart-pro": ("FluentCart Pro", "Écosystème Fluent", "Tunnels pro, codes promos avancés et abonnements complexes"),
    "fluentform": ("Fluent Forms", "Écosystème Fluent", "Créateur de formulaires dynamique et hautement performant"),
    "fluentformpro": ("Fluent Forms Pro", "Écosystème Fluent", "Logique conditionnelle avancée, calculs et intégrations profondes"),
    "fluentforms-pdf": ("Fluent Forms PDF", "Écosystème Fluent", "Génération automatique de fichiers PDF à partir des formulaires"),
    "fluent-roadmap": ("Fluent Roadmap", "Écosystème Fluent", "Gestion et publication de feuilles de route produit publiques/privées"),
    "fluent-affiliate": ("Fluent Affiliate", "Écosystème Fluent", "Gestion de l'affiliation en local (version gratuite)"),
    "fluent-affiliate-pro": ("Fluent Affiliate Pro", "Écosystème Fluent", "Système d'affiliation pro complet, suivi des commissions et portails affiliés"),
    "fluent-smtp": ("FluentSMTP", "Écosystème Fluent", "Routage d'emails sécurisé et ultra-rapide avec rapports de délivrabilité"),
    "fluent-support": ("Fluent Support", "Écosystème Fluent", "Système de ticket de support client intégré en local"),
    "fluent-support-pro": ("Fluent Support Pro", "Écosystème Fluent", "Règles d'affectation automatique, portails pro, et réponses pré-enregistrées"),
    "fluent-toolkit": ("Fluent Toolkit", "Écosystème Fluent", "Outils d'optimisation et d'intégration transversaux pour l'écosystème Fluent"),
    "fluent-player": ("Fluent Player", "Écosystème Fluent", "Lecteur vidéo léger optimisé (version standard)"),
    "fluent-player-pro": ("Fluent Player Pro", "Écosystème Fluent", "Lecteur vidéo pro avec fonctionnalités d'apprentissage et analytics"),

    # 2. LMS & E-Learning
    "tutor": ("Tutor LMS", "LMS & E-learning", "Moteur de cours en ligne, gestion de leçons et d'étudiants (version gratuite)"),
    "tutor-pro": ("Tutor LMS Pro", "LMS & E-learning", "Gestion des quiz complexes, rapports d'apprentissage et certificats personnalisés"),
    
    # 3. SEO & Performance
    "seo-by-rank-math": ("Rank Math SEO", "SEO & Performance", "Extension de base d'optimisation pour les moteurs de recherche"),
    "seo-by-rank-math-pro": ("Rank Math SEO PRO", "SEO & Performance", "Gestionnaire de schémas avancés, suivi de positions et SEO local"),
    "fast-indexing-api": ("Instant Indexing (Fast Indexing API)", "SEO & Performance", "Indexation instantanée des articles sur Google et Bing via API"),
    "freshrank-ai-pro": ("FreshRank AI Pro", "SEO & Performance", "Optimisation sémantique et IA pour le classement Google"),
    "flying-press": ("FlyingPress", "SEO & Performance", "Extension de cache et d'optimisation de vitesse (Core Web Vitals)"),
    "link-whisper-premium": ("Link Whisper Premium", "SEO & Performance", "Suggestions de liens internes intelligentes et automatisées pour le SEO"),
    "easy-content-linker-premium": ("Easy Content Linker Premium", "SEO & Performance", "Génération automatique et maillage interne sémantique de liens contextuels"),

    # 4. Automations & Webhooks
    "suretriggers": ("OttoKit (SureTriggers)", "Automatisation & Webhooks", "Plateforme d'automatisation locale connectant WordPress aux APIs externes"),
    "wp-webhooks": ("WP Webhooks", "Automatisation & Webhooks", "Création et gestion de webhooks (triggers et actions) avancés en direct"),
    "integromat-connector": ("Make (Integromat) Connector", "Automatisation & Webhooks", "Pont officiel d'intégration avec les scénarios de Make.com"),

    # 5. Design & Constructeurs
    "kadence-blocks": ("Kadence Blocks", "Design & Constructeurs", "Bibliothèque de blocs Gutenberg de haute performance (Gratuit)"),
    "kadence-blocks-pro": ("Kadence Blocks Pro", "Design & Constructeurs", "Blocs avancés, animations et templates premium"),
    "kadence-pro": ("Kadence Pro", "Design & Constructeurs", "Fonctionnalités avancées du thème Kadence (headers/footers customs)"),
    "lg": ("Divi Lover / Custom LG Blocks", "Design & Constructeurs", "Intégrations esthétiques et blocs sur-mesure de Divi Lover"),
    "presto-player": ("Presto Player", "Design & Constructeurs", "Lecteur vidéo moderne et optimisé pour WordPress (Gratuit)"),
    "presto-player-pro": ("Presto Player Pro", "Design & Constructeurs", "Vidéos privées, intégration LMS et CRM avec analytics précis"),

    # 6. Social Media & Link Tracking
    "bit-social": ("Bit Social", "Réseaux Sociaux & Liens", "Planification et publication automatique de contenus sur les réseaux (Gratuit)"),
    "bit-social-pro": ("Bit Social Pro", "Réseaux Sociaux & Liens", "Publication multi-comptes, hashtags automatiques et rapports de clics"),
    "clickwhale-pro": ("ClickWhale Pro", "Réseaux Sociaux & Liens", "Gestionnaire de liens d'affiliation courts et bio pages premium"),
    "custom-feed-for-tiktok": ("Custom Feed for TikTok", "Réseaux Sociaux & Liens", "Affichage fluide de flux vidéo TikTok sur le site"),
    "wp-social-reviews": ("WP Social Ninja", "Réseaux Sociaux & Liens", "Agrégateur de témoignages clients et de réseaux sociaux (Gratuit)"),
    "wp-social-ninja-pro": ("WP Social Ninja Pro", "Réseaux Sociaux & Liens", "Intégration multi-plateformes de avis (Google, FB, Yelp) et chats"),

    # 7. Utilities & Security
    "admin-site-enhancements-pro": ("Admin Site Enhancements (ASE) PRO", "Utilitaires & Sécurité", "Le couteau suisse d'optimisation de l'administration WordPress"),
    "cookie-law-info": ("Cookie Law Info (GDPR Consent)", "Utilitaires & Sécurité", "Gestionnaire de consentement aux cookies et conformité RGPD"),
    "secupress-pro": ("SecuPress Pro", "Utilitaires & Sécurité", "Scanner de sécurité complet, pare-feu et protection du site"),
    "polylang": ("Polylang", "Utilitaires & Sécurité", "Gestion fine du multilinguisme sur les pages, articles et taxonomies"),
    "loco-translate": ("Loco Translate", "Utilitaires & Sécurité", "Traduction d'extensions et thèmes directement depuis l'administration"),
    "traduire-sans-migraine": ("Traduire Sans Migraine", "Utilitaires & Sécurité", "Outil de traduction automatique intelligent pour articles WordPress"),
    "safe-svg": ("Safe SVG", "Utilitaires & Sécurité", "Permet le téléversement sécurisé de fichiers vectoriels SVG"),
    "ninja-tables": ("Ninja Tables", "Utilitaires & Sécurité", "Créateur de tableaux de données réactifs et performants (Gratuit)"),
    "ninja-tables-pro": ("Ninja Tables Pro", "Utilitaires & Sécurité", "Tableaux connectés aux bases de données, requêtes customs et imports"),

    # 8. Monitoring & Core
    "wp-health": ("WP Health (WP-Umbrella)", "Gestion Technique & Monitoring", "Extension de surveillance et de monitoring global du site"),
    "novamira": ("NovaMira Core", "Gestion Technique & Monitoring", "Cerveau d'intégration technique et d'optimisation"),
    "novamira-pro": ("NovaMira Pro", "Gestion Technique & Monitoring", "Fonctionnalités avancées de contrôle technique et d'API"),
    
    # 9. Custom MU-Plugins
    "buddyboss-performance-api": ("BuddyBoss Performance API", "MU-Plugins Custom schoolsWP", "Optimisation de l'API REST de BuddyBoss pour soulager le serveur"),
    "schoolswp-ai-summary-langs": ("schoolsWP AI Summary Languages", "MU-Plugins Custom schoolsWP", "Support multilingue pour les synthèses IA schoolsWP"),
    "schoolswp-ai-summary": ("schoolsWP AI Summary", "MU-Plugins Custom schoolsWP", "Moteur d'automatisation des résumés d'articles générés par l'IA"),
    "schoolswp-fluentcart-fr-overrides": ("schoolsWP FluentCart FR Overrides", "MU-Plugins Custom schoolsWP", "Ajustements linguistiques et corrections de taxes françaises pour FluentCart"),
    "schoolswp-tutor-fr-overrides": ("schoolsWP Tutor FR Overrides", "MU-Plugins Custom schoolsWP", "Ajustements linguistiques français pour Tutor LMS"),
    "schoolswp-tutor-fluentcart-bridge": ("schoolsWP Tutor-FluentCart Bridge", "MU-Plugins Custom schoolsWP", "Liaison directe : inscription automatique à un cours Tutor LMS après achat FluentCart"),
    "schoolswp-affiliate-cloaks": ("schoolsWP Affiliate Cloaks", "MU-Plugins Custom schoolsWP", "Masquage et redirection avancée des liens affiliés de schoolsWP"),
    "schoolswp-header-button-i18n": ("schoolsWP Header Button i18n", "MU-Plugins Custom schoolsWP", "Internationalisation dynamique des boutons d'en-tête"),
    "schoolswp-list-cleanup-cron": ("schoolsWP List Cleanup Cron", "MU-Plugins Custom schoolsWP", "Tâche cron de nettoyage automatique de la base de données et des contacts obsolètes"),
    "schoolswp-person-schema": ("schoolsWP Person Schema", "MU-Plugins Custom schoolsWP", "Injection dynamique des métadonnées Schema.org (Person) de Michaël KIHL"),
    "(secupress_cookiehash_697bbac42d5bd)": ("SecuPress Cookie Hash Helper", "MU-Plugins Custom schoolsWP", "Sécurisation et salage des cookies administratifs"),
    "(secupress_salt_keys_6978cc00f0697)": ("SecuPress Salt Keys Rotation", "MU-Plugins Custom schoolsWP", "Rotation automatique des clés de salage du site"),
    "InitUmbrella": ("Init Umbrella MU", "MU-Plugins Custom schoolsWP", "Initialisation prioritaire des agents de monitoring WP-Umbrella"),
    "_WPHealthHandlerMU": ("WP Health Handler MU", "MU-Plugins Custom schoolsWP", "Gestionnaire prioritaire de santé système"),
    
    # Dropins
    "advanced-cache.php": ("Advanced Cache Drop-in", "Drop-ins (Prioritaires)", "Cache de page hautement performant (géré par FlyingPress)"),
    "db-error.php": ("DB Error Handler Drop-in", "Drop-ins (Prioritaires)", "Page d'erreur de base de données stylisée et personnalisée"),
    "maintenance.php": ("Maintenance Page Drop-in", "Drop-ins (Prioritaires)", "Page de maintenance automatique et stylisée")
}

# Grouping lists
categorized = {}

for p in plugins:
    slug = p["name"]
    version = p["version"]
    status = p["status"]
    
    # Try mapping
    if slug in mappings:
        name, cat, desc = mappings[slug]
    else:
        # Default fallback
        name = slug.replace("-", " ").title()
        cat = "Non Classé"
        desc = "Extension système active"
        
        # Infer status for mu-plugins and dropins
        if status == "must-use":
            cat = "MU-Plugins Custom schoolsWP"
        elif status == "dropin":
            cat = "Drop-ins (Prioritaires)"
            
    if cat not in categorized:
        categorized[cat] = []
        
    categorized[cat].append({
        "slug": slug,
        "name": name,
        "version": version,
        "status": status,
        "description": desc,
        "update_status": p.get("update", "none"),
        "update_version": p.get("update_version", "")
    })

# Define categories logical order
categories_order = [
    "Écosystème Fluent",
    "LMS & E-learning",
    "SEO & Performance",
    "Automatisation & Webhooks",
    "Design & Constructeurs",
    "Réseaux Sociaux & Liens",
    "Utilitaires & Sécurité",
    "Gestion Technique & Monitoring",
    "MU-Plugins Custom schoolsWP",
    "Drop-ins (Prioritaires)",
    "Non Classé"
]

# Generate Markdown Content
md = []
md.append("# 📋 Inventaire Complet des Extensions schoolsWP")
md.append("\nCe document répertorie l'intégralité de ton infrastructure technique WordPress. Il est généré de manière dynamique depuis le serveur de production de **schoolsWP.com**.")
md.append(f"\n- **Total d'extensions standard** : {len([p for p in plugins if p['status'] in ['active', 'inactive']])} actives")
md.append(f"- **Extensions Must-Use (MU-Plugins)** : {len([p for p in plugins if p['status'] == 'must-use'])}")
md.append(f"- **Drop-ins système** : {len([p for p in plugins if p['status'] == 'dropin'])}")
md.append("\n---\n")

for cat in categories_order:
    if cat not in categorized:
        continue
    md.append(f"## 📁 {cat}")
    md.append("| Extension | Version | Statut | Rôle & Utilité dans schoolsWP |")
    md.append("|---|---|---|---|")
    for item in sorted(categorized[cat], key=lambda x: x["name"]):
        status_fr = "Actif" if item["status"] == "active" else ("Must-Use (Prioritaire)" if item["status"] == "must-use" else ("Drop-in" if item["status"] == "dropin" else "Inactif"))
        update_flag = ""
        if item["update_status"] == "available":
            update_flag = f" 🔄 *(MàJ dispo: {item['update_version']})*"
        md.append(f"| **{item['name']}** <br> `{item['slug']}` | {item['version']}{update_flag} | `{status_fr}` | {item['description']} |")
    md.append("\n")

# Write Markdown to outputs/
outputs_dir = r"d:\ANTIGRAVITY\outputs"
os.makedirs(outputs_dir, exist_ok=True)

md_file_path = os.path.join(outputs_dir, "schoolswp_plugins_inventory.md")
with open(md_file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Markdown table generated successfully: {md_file_path}")

# Generate CSV Content
csv_file_path = os.path.join(outputs_dir, "schoolswp_plugins_inventory.csv")
with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    # Headers
    writer.writerow(["Nom d'affichage", "Slug", "Catégorie", "Version", "Type/Statut", "Mise à Jour Disponible", "Description / Utilité schoolsWP"])
    
    for cat in categories_order:
        if cat not in categorized:
            continue
        for item in sorted(categorized[cat], key=lambda x: x["name"]):
            status_fr = "Actif" if item["status"] == "active" else ("Must-Use" if item["status"] == "must-use" else ("Drop-in" if item["status"] == "dropin" else "Inactif"))
            maj = item["update_version"] if item["update_status"] == "available" else "Non"
            writer.writerow([
                item["name"],
                item["slug"],
                cat,
                item["version"],
                status_fr,
                maj,
                item["description"]
            ])

print(f"CSV inventory generated successfully: {csv_file_path}")
