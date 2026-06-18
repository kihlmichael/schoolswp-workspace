@echo off
title Auto-Publisher YouTube schoolsWP (W209a)
echo ==============================================================================
echo Lancement de la Routine de Publication YouTube (W209a)...
echo ==============================================================================
d:
cd "d:\VS Code\CLAUDE CODE\projects\schoolswp"
.venv\Scripts\python .claude\skills\social\youtube-brief-publisher\scripts\run_publisher.py
echo ==============================================================================
echo Routine terminee. Appuyez sur une touche pour quitter.
echo ==============================================================================
pause
