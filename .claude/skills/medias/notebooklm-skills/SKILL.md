---
name: notebooklm-skills
description: |
  Transforme fichiers et dossiers en matériaux pédagogiques avec NotebookLM via le MCP `notebooklm-mcp`. Crée podcasts audio, vidéos explicatives, slide decks (avec retrait auto du watermark), guides d'étude, quiz, flashcards, infographies, mind maps et rapports depuis des PDF, textes, URLs ou dossiers. Workflow 3 phases (configure / confirm / process).
  Utilise ce skill quand l'utilisateur dit : "crée un notebook NotebookLM", "génère un podcast NotebookLM", "transforme ces PDF en quiz/flashcards/mindmap", "matériaux pédagogiques NotebookLM", "audio overview de ces sources", ou veut produire un livrable pédagogique batch depuis sources hétérogènes.
  NE PAS utiliser pour : production scénarisée vidéo schoolsWP (utiliser `schoolswp-youtube-studio` ou Remotion), TTS standalone (utiliser `text-to-speech`), ou formation gratuite plugin avec scripts vidéo (utiliser `formation-pipeline`).
---

# Notebook Decks

Transform user files and folders into rich learning materials (podcasts, videos, slide decks, quizzes, etc.) using the NotebookLM MCP, with automatic watermark removal for slide decks.

## Rules (apply to ALL phases)

1. **MCP Only**: Use `notebooklm-mcp` MCP tool calls for ALL NotebookLM operations. NEVER use `nlm` CLI via Bash (except `nlm login` for auth). NEVER create automation script files (.js, .py, .sh, .bat).
2. **No Skipping**: Every question in every phase must be asked and answered before proceeding. Do not assume defaults.
3. **State First**: State files (`.notebook-decks-meta.json`, `tasks.md`, `generation-config.jsonl`) must be written to disk before any `notebook_create` call.

## Start Here

Check if `.notebook-decks-meta.json` exists in the project root, then follow the appropriate path:

### Path A: Fresh Start (no state file)

1. Read `phases/01-configure.md` — collect all user configuration (8 steps)
2. When Phase 1 complete, read `phases/02-confirm.md` — save state files and get user confirmation
3. When Phase 2 complete, read `phases/03-process.md` — process batches

### Path B: Resume (state exists with incomplete batches)

Read `phases/03-process.md` directly. Resume from the first batch with status != "downloaded" or "cleaned".

### Path C: Complete (all batches done)

Tell user: "All N batches were completed. Start a new session (clear state) or modify configuration?"

---

**IMPORTANT**: Read ONE phase file at a time. Complete ALL steps before reading the next. This skill controls routing — phase files do NOT chain to each other.
