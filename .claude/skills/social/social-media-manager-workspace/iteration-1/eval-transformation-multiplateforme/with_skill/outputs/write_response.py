import os

path = r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\skills\social\social-media-manager-workspace\iteration-1\eval-transformation-multiplateforme\with_skill\outputsesponse.md"

content = (
  "# Transformation article -> Posts sociaux multi-plateformes
"
  "
"
  "**Source** : Article "Creer une formation en ligne rentable avec WordPress"
"
  "**URL** : https://schoolswp.com/tutor-lms-vs-learndash/
"
  "**Date** : 2026-04-06
"
  "**Plateformes** : LinkedIn, X/Twitter, Facebook
"
  "**Skill utilise** : social-media-manager
"
)

with open(path, "w", encoding="utf-8") as out:
    out.write(content)
print("OK")
