"""
One-shot : traduire les descriptions EN -> FR dans le frontmatter des SKILL.md.

Modifie le bloc `description:` (single-line ou multi-line `|`/`>`) avec la traduction FR.
Idempotent : applique le contenu cible sans verifier l'ancien etat.
"""

import os
import re
import sys

ROOT = ".claude/skills"

# {chemin relatif a ROOT : description FR à injecter}
FR = {
    # === Natifs schoolsWP ===
    "ops/skill-creator/SKILL.md": "Crée, modifie et évalue les skills Claude Code. Utilise ce skill pour créer un skill from scratch, mettre à jour ou optimiser un skill existant, lancer des évals, benchmarker la performance ou optimiser la description d'un skill.",
    "aidesigner-frontend/SKILL.md": "Utilise ce skill quand l'utilisateur veut créer ou redesigner un frontend, landing page, dashboard, page marketing ou toute UI avec AIDesigner. Préférer le serveur MCP aidesigner pour generate/refine, puis utiliser le CLI AIDesigner local pour la capture d'artefacts, le rendu preview et l'adoption repo-native.",
    "dev/skill-creator-ccguide/SKILL.md": "Génère un nouveau skill Claude Code avec SKILL.md, frontmatter et ressources bundled. Utilise ce skill pour créer un skill custom, standardiser la structure des skills d'une équipe ou packager un skill pour distribution.",
    "dev/design-patterns/SKILL.md": "Référence des design patterns logiciels : Singleton, Factory, Observer, Strategy, etc. Utilise ce skill pour identifier le bon pattern selon le problème à résoudre ou refactorer du code legacy.",
    "ia-llm/conversational-query-mapper/SKILL.md": "Utilise ce skill pour mapper, lister ou générer les requêtes conversationnelles - les questions que les vraies personnes posent à ChatGPT, Perplexity ou aux assistants IA sur un sujet WordPress. Déclencheurs : carte des requêtes conversationnelles, mapper les intentions/questions, GEO/AIO query map.",
    # === Google Workspace ===
    "gws/gws-keep/SKILL.md": "Gère les notes Google Keep.",
    "gws/gws-meet/SKILL.md": "Gère les visioconférences Google Meet.",
    "gws/gws-calendar-insert/SKILL.md": "Google Calendar : insère un événement avec invités, lieu et rappels.",
    "gws/gws-modelarmor-create-template/SKILL.md": "Crée un template Model Armor pour la sécurité des prompts IA dans Google Cloud.",
    "gws/personas/persona-customer-support/SKILL.md": "Gère le support client - suit les tickets, répond, escalade les problèmes.",
    "gws/personas/persona-exec-assistant/SKILL.md": "Gère l'agenda, la boîte mail et les communications d'un dirigeant.",
    "gws/personas/persona-sales-ops/SKILL.md": "Gère les workflows commerciaux - suit les deals, planifie les calls, gère les communications clients.",
    "gws/recipes/recipe-block-focus-time/SKILL.md": "Crée des blocs récurrents de temps de concentration sur Google Calendar pour protéger les heures de deep work.",
    "gws/recipes/recipe-create-classroom-course/SKILL.md": "Crée un cours Google Classroom et invite les étudiants.",
    "gws/recipes/recipe-create-expense-tracker/SKILL.md": "Configure un Google Sheets de suivi de dépenses avec en-têtes et entrées initiales.",
    "gws/recipes/recipe-create-feedback-form/SKILL.md": "Crée un Google Form de feedback et le partage par Gmail.",
    "gws/recipes/recipe-create-gmail-filter/SKILL.md": "Crée un filtre Gmail pour libeller, marquer ou catégoriser automatiquement les messages entrants.",
    "gws/recipes/recipe-create-meet-space/SKILL.md": "Crée un espace de réunion Google Meet et partage le lien de connexion.",
    "gws/recipes/recipe-create-presentation/SKILL.md": "Crée une nouvelle présentation Google Slides et ajoute les diapositives initiales.",
    "gws/recipes/recipe-create-shared-drive/SKILL.md": "Crée un Drive Partagé Google et ajoute les membres avec les rôles appropriés.",
    "gws/recipes/recipe-create-task-list/SKILL.md": "Configure une nouvelle liste Google Tasks avec des tâches initiales.",
    "gws/recipes/recipe-forward-labeled-emails/SKILL.md": "Trouve les messages Gmail avec un libellé spécifique et les transfère à une autre adresse.",
    "gws/recipes/recipe-generate-report-from-sheet/SKILL.md": "Génère un rapport Google Docs depuis les données d'un Google Sheets.",
    "gws/recipes/recipe-organize-drive-folder/SKILL.md": "Crée une structure de dossiers Google Drive et déplace les fichiers vers les bons emplacements.",
    "gws/recipes/recipe-post-mortem-setup/SKILL.md": "Met en place un Google Doc de post-mortem avec sections types et participants invités.",
    "gws/recipes/recipe-review-overdue-tasks/SKILL.md": "Identifie les tâches Google Tasks en retard et propose un plan de rattrapage.",
    "gws/recipes/recipe-save-email-attachments/SKILL.md": "Trouve les pièces jointes Gmail et les sauvegarde dans Google Drive.",
    "gws/recipes/recipe-schedule-recurring-event/SKILL.md": "Planifie un événement Google Calendar récurrent avec invités et rappels.",
    # === HeyGen ===
    "external-heygen/heygen-avatar/SKILL.md": "Crée un avatar HeyGen persistant - une identité visage + voix réutilisable pour l'agent, l'utilisateur ou tout personnage nommé - propulsée par la techno HeyGen Avatar V. Création par prompt par défaut (description -> HeyGen le construit), upload photo optionnel pour digital twin de personne réelle.",
    "external-heygen/heygen-video/SKILL.md": "Génère des vidéos présentateur HeyGen via le pipeline v3 Video Agent - gère Frame Check (correction d'aspect ratio), prompt engineering, résolution avatar et sélection de voix. Requis pour toute génération vidéo HeyGen.",
    # === HyperFrames ===
    "external-hyperframes/hyperframes/SKILL.md": "Crée des compositions vidéo, animations, title cards, overlays, captions, voix off, visuels audio-réactifs et transitions de scènes en HyperFrames HTML. Utilise ce skill pour tout contenu vidéo HTML, ajouter des sous-titres synchronisés audio, générer du TTS ou créer des visuels audio-réactifs.",
    "external-hyperframes/hyperframes-registry/SKILL.md": "Registre des compositions HyperFrames disponibles dans le projet (templates, snippets, presets).",
    "external-hyperframes/website-to-hyperframes/SKILL.md": "Convertit le contenu d'un site web en compositions vidéo HyperFrames (extraction texte, images, animations).",
    # === LiveAvatar ===
    "external-liveavatar/liveavatar-integrate/SKILL.md": "Construit une intégration LiveAvatar end-to-end - évalue la stack existante, recommande le chemin optimal et guide l'implémentation. Utilise ce skill pour ajouter un avatar temps réel à une app ou un site, ou connecter LiveAvatar à un pipeline IA existant.",
    "external-liveavatar/liveavatar-debug/SKILL.md": "Débogue les problèmes d'intégration LiveAvatar : connexion WebSocket, sync audio, latence, état de session.",
    "external-liveavatar/liveavatar-feedback/SKILL.md": "Collecte et analyse les retours utilisateurs sur les sessions LiveAvatar pour optimiser l'expérience.",
    # === Antigravity ===
    "external-antigravity/popup-cro/SKILL.md": "Crée et optimise les popups, modales, overlays, slide-ins et bannières pour augmenter les conversions sans nuire à l'UX ni à la confiance dans la marque.",
    "external-antigravity/seo-aeo-schema-generator/SKILL.md": "Génère du JSON-LD complet et conforme schema.org pour pages SEO/AEO/GEO (FAQPage, HowTo, Article, Product, Organization, etc.). Utilise ce skill pour produire des données structurées qui maximisent la visibilité dans Google et les moteurs IA.",
    "external-antigravity/wordpress-centric-high-seo-optimized-blogwriting-skill/SKILL.md": "Rédige des articles de blog WordPress hautement optimisés SEO avec structure pédagogique, truth boxes, output WordPress-ready (Gutenberg blocks). Utilise ce skill pour produire un article SEO long format prêt à publier.",
    # === CC Design ===
    "external-cc-design/SKILL.md": "Design HTML haute fidélité pour slide decks, prototypes, landing pages. Brand-grade strict, sortie production-ready (HTML/CSS/JS). Privilégier ce skill pour la production finale (T1) après exploration aidesigner (T0).",
    # === Vague 2 : compléments GWS + recipes + personas + autres EN ===
    "gws/gws-calendar/SKILL.md": "Google Calendar : gère les calendriers et les événements.",
    "gws/gws-chat/SKILL.md": "Google Chat : gère les espaces et les messages Chat.",
    "gws/gws-chat-send/SKILL.md": "Google Chat : envoie un message dans un espace.",
    "gws/gws-classroom/SKILL.md": "Google Classroom : gère les classes, listes d'élèves et devoirs.",
    "gws/gws-docs-write/SKILL.md": "Google Docs : ajoute du texte à un document.",
    "gws/gws-drive/SKILL.md": "Google Drive : gère les fichiers, dossiers et drives partagés.",
    "gws/gws-gmail/SKILL.md": "Gmail : envoie, lit et gère les emails.",
    "gws/gws-gmail-reply/SKILL.md": "Gmail : répond à un message (threading géré automatiquement).",
    "gws/gws-gmail-reply-all/SKILL.md": "Gmail : répond à tous sur un message (threading géré automatiquement).",
    "gws/gws-gmail-send/SKILL.md": "Gmail : envoie un email.",
    "gws/gws-people/SKILL.md": "Google People : gère les contacts et les profils.",
    "gws/gws-sheets-append/SKILL.md": "Google Sheets : ajoute une ligne à un classeur.",
    "gws/gws-sheets-read/SKILL.md": "Google Sheets : lit les valeurs d'un classeur.",
    "gws/gws-tasks/SKILL.md": "Google Tasks : gère les listes et les tâches.",
    "gws/personas/persona-event-coordinator/SKILL.md": "Planifie et gère des événements - scheduling, invitations et logistique.",
    "gws/personas/persona-it-admin/SKILL.md": "Administre l'IT - surveille la sécurité et configure Workspace.",
    "gws/personas/persona-researcher/SKILL.md": "Organise la recherche - gère les références, notes et collaboration.",
    "gws/recipes/recipe-batch-invite-to-event/SKILL.md": "Ajoute une liste de participants à un événement Google Calendar existant et envoie les notifications.",
    "gws/recipes/recipe-bulk-download-folder/SKILL.md": "Liste et télécharge tous les fichiers d'un dossier Google Drive.",
    "gws/recipes/recipe-collect-form-responses/SKILL.md": "Récupère et passe en revue les réponses d'un Google Form.",
    "gws/recipes/recipe-copy-sheet-for-new-month/SKILL.md": "Duplique un onglet template Google Sheets pour un nouveau mois de tracking.",
    "gws/recipes/recipe-create-events-from-sheet/SKILL.md": "Lit les données d'événements depuis un Google Sheets et crée les entrées Google Calendar correspondantes.",
    "gws/recipes/recipe-draft-email-from-doc/SKILL.md": "Lit le contenu d'un Google Doc et l'utilise comme corps d'un message Gmail.",
    "gws/recipes/recipe-find-free-time/SKILL.md": "Interroge la disponibilité Google Calendar de plusieurs utilisateurs pour trouver un créneau de réunion commun.",
    "gws/recipes/recipe-log-deal-update/SKILL.md": "Ajoute une mise à jour de statut de deal dans un Google Sheets de suivi commercial.",
    "gws/recipes/recipe-plan-weekly-schedule/SKILL.md": "Passe en revue ta semaine Google Calendar, identifie les trous et ajoute les événements pour les combler.",
    "gws/recipes/recipe-reschedule-meeting/SKILL.md": "Déplace un événement Google Calendar à un nouveau créneau et notifie automatiquement tous les participants.",
    "gws/recipes/recipe-save-email-to-doc/SKILL.md": "Sauvegarde le corps d'un message Gmail dans un Google Doc pour archivage ou référence.",
    "gws/recipes/recipe-send-team-announcement/SKILL.md": "Envoie une annonce d'équipe à la fois par Gmail et dans un espace Google Chat.",
    "gws/recipes/recipe-sync-contacts-to-sheet/SKILL.md": "Exporte le carnet d'adresses Google Contacts vers un Google Sheets.",
    # === Antigravity restants ===
    "external-antigravity/email-sequence/SKILL.md": "Tu es un expert en email marketing et automation. Ton objectif est de créer des séquences email qui nurturent les leads, augmentent les conversions et engagent les clients via des campagnes ciblées et personnalisées.",
    "external-antigravity/seo-snippet-hunter/SKILL.md": "Formate le contenu pour qu'il soit éligible aux featured snippets et SERP features. Crée des contenus optimisés snippet (paragraphe, liste, tableau, FAQ) à partir d'un sujet ou d'une page existante.",
    # === Manim ===
    "external-video-use/skills/manim-video/SKILL.md": "Pipeline de production pour animations mathématiques et techniques avec Manim Community Edition. Crée des vidéos pédagogiques style 3Blue1Brown avec rendu LaTeX, animations de courbes, transformations géométriques et synchronisation audio.",
    # === Vague 3 : derniers EN détectés ===
    "gws/recipes/recipe-backup-sheet-as-csv/SKILL.md": "Exporte un Google Sheets en fichier CSV pour backup local ou traitement.",
    "external-antigravity/wordpress-plugin-development/SKILL.md": "Workflow de développement de plugins WordPress couvrant l'architecture du plugin, les hooks, les interfaces admin, REST API, bonnes pratiques de sécurité, internationalisation, tests et publication. Utilise ce skill pour développer un plugin WordPress complet, configurer la structure, hooks et tests automatisés.",
    "external-video-use/SKILL.md": "Édite n'importe quelle vidéo par conversation. Transcription, coupes, color grading, génération d'animations overlay, sous-titres incrustés - pour talking heads, montages, tutoriels, voyages, interviews. Pas de presets, pas de menus. Pose des questions, confirme le plan, exécute, itère, persiste. Les règles de correctness production sont strictes, le reste est liberté artistique.",
    "external-hyperframes/hyperframes-cli/SKILL.md": "Outil CLI HyperFrames - hyperframes init, lint, preview, render, transcribe, tts, doctor, browser, info, upgrade, compositions. Utilise ce skill pour scaffolder, valider, prévisualiser et rendre des compositions HyperFrames depuis la ligne de commande.",
}


def patch_description(content: str, new_desc: str) -> str:
    """Replace description block in YAML frontmatter."""
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return content
    fm = fm_match.group(1)
    fm_start, fm_end = fm_match.span(1)

    # Replace description : single-line "..." | '...' | bare, OR block | / >
    desc_re = re.compile(
        r"^description:\s*[|>]?[+-]?\s*([\s\S]+?)(?=\n[a-zA-Z_-]+:|\Z)",
        re.MULTILINE,
    )
    m = desc_re.search(fm)
    if not m:
        return content
    # Escape double quotes in new_desc for safe quoting
    safe = new_desc.replace('"', '\\"')
    new_fm = fm[: m.start()] + f'description: "{safe}"' + fm[m.end():]
    return content[:fm_start] + new_fm + content[fm_end:]


def main():
    apply = "--apply" in sys.argv
    changed, skipped = 0, 0
    for rel_path, fr_desc in FR.items():
        full = os.path.join(ROOT, rel_path)
        if not os.path.isfile(full):
            print(f"MISS  {rel_path}")
            skipped += 1
            continue
        with open(full, encoding="utf-8") as f:
            content = f.read()
        new_content = patch_description(content, fr_desc)
        if new_content == content:
            print(f"NOOP  {rel_path}")
            skipped += 1
            continue
        if apply:
            with open(full, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"OK    {rel_path}")
        else:
            print(f"WILL  {rel_path}")
        changed += 1

    print(f"\nTotal : {changed} fichier(s) {'patches' if apply else 'a patcher'}, {skipped} skip(s).")
    if not apply:
        print("Dry-run : relancer avec --apply pour ecrire.")


if __name__ == "__main__":
    main()
