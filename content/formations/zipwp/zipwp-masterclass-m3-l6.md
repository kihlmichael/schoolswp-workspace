# Lecon 3.6 — AI Troubleshooter : diagnostiquer les erreurs

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 3 — De la demo au site en production
- **Lecon** : 6/7
- **Duree cible** : 6 min
- **Objectif pedagogique** : Utiliser l'AI Troubleshooter de ZipWP pour detecter et corriger automatiquement les problemes WordPress courants.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Ton site plante. Une page affiche une erreur. Un plugin ne fonctionne plus apres une mise a jour. Le site est devenu lent sans raison apparente.

Avant, tu aurais passe des heures a chercher sur Google, a desactiver les plugins un par un, a fouiller les logs. ZipWP integre un outil qui fait ca pour toi : l'AI Troubleshooter. Une IA qui scanne ton site, identifie les problemes, et te propose des corrections.

---

[SECTION 1 — Ce que l'AI Troubleshooter detecte]

L'AI Troubleshooter analyse trois categories de problemes.

Les conflits de plugins. Quand deux plugins utilisent les memes ressources ou les memes hooks WordPress, ca cree des conflits. Un formulaire qui ne s'affiche plus, un slider qui disparait, un menu qui se decale. L'IA identifie quel plugin cause le conflit et te dit quoi faire.

Les erreurs PHP. Des warnings, des notices, parfois des erreurs fatales qui cassent une page. L'IA lit les logs d'erreurs, identifie le fichier et la ligne problematique, et te dit si c'est un bug de plugin, un probleme de version PHP, ou un conflit de code.

Les problemes de performance. Un temps de chargement qui augmente, des requetes SQL lentes, des fichiers non optimises. L'IA mesure les metriques cles et te montre ou sont les goulots d'etranglement.

---

[SECTION 2 — Comment l'utiliser]

Va dans ton dashboard ZipWP. Selectionne le site qui pose probleme. Clique sur "Troubleshoot".

L'IA lance un scan complet. Ca prend generalement 30 secondes a 2 minutes selon la taille du site.

Le rapport s'affiche ensuite. Pour chaque probleme detecte, tu vois trois choses : la description du probleme, le niveau de severite — critique, important, ou mineur — et la suggestion de correction.

Pour les corrections automatiques, l'IA te propose un bouton "Fix". Un clic, et la correction est appliquee. L'IA desactive le plugin problematique, corrige le parametre de configuration, ou ajuste le reglage qui pose probleme.

Pour les corrections manuelles, l'IA te donne les instructions etape par etape. "Allez dans Reglages → Permaliens et cliquez sur Enregistrer." Ou "Mettez a jour le plugin X vers la version Y."

Conseil : lis toujours la description du probleme et la correction proposee avant de cliquer sur "Fix". Comprends ce que l'IA va modifier. Fais un backup avant d'appliquer des corrections sur des problemes critiques.

---

[SECTION 3 — Les limites]

L'AI Troubleshooter est pratique pour les problemes courants. Mais il ne remplace pas un developpeur pour tout.

Ce qu'il ne fait pas : corriger du code personnalise — si tu as modifie des fichiers PHP ou ajoute du code custom, l'IA ne sait pas quoi en faire. Diagnostiquer des problemes de serveur — si le probleme vient de la configuration du serveur et pas de WordPress, l'IA ne peut pas agir. Resoudre des problemes complexes multi-facteurs — quand trois plugins interagissent de facon imprevisible, l'IA peut identifier le symptome mais pas toujours la cause racine.

Pour ces cas-la, il te faudra un developpeur WordPress. Mais pour 80% des problemes quotidiens — un plugin qui fait des siennes, une page lente, une erreur apres une mise a jour — le Troubleshooter te fait gagner des heures.

---

[OUTRO]

L'AI Troubleshooter, c'est ton premier reflexe quand quelque chose ne va pas. Scan, diagnostic, correction — en quelques clics.

Derniere lecon du module : la maintenance hebdomadaire. Une routine de 15 minutes par semaine pour garder ton site en bonne sante, sans y passer des heures.

---

## Notes de production

### Captures d'ecran suggerees

1. **Dashboard ZipWP** — Bouton "Troubleshoot" dans les options du site
2. **Scan en cours** — Animation de scan avec barre de progression
3. **Rapport** — Liste des problemes detectes avec severite (rouge/orange/vert)
4. **Bouton Fix** — Interface de correction automatique
5. **Instructions manuelles** — Exemple de correction guidee etape par etape

### Transitions

- Intro → Section 1 : animation "erreur detectee" sur un ecran WordPress
- Section 1 → Section 2 : zoom sur le dashboard ZipWP, bouton Troubleshoot
- Section 2 → Section 3 : transition vers ecran "limites" avec fond nuance
- Section 3 → Outro : retour avatar

### Notes HeyGen / ElevenLabs

- Ton pragmatique — pas de promesses exagerees sur l'outil
- Section 1 : articuler les trois categories clairement, rythme structure
- Section 2 : ton guiding, comme si on montrait l'interface en direct
- Section 3 : ton honnete sur les limites — credibilite avant tout
