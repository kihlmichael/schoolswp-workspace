# Lecon 4.4 — Sandbox : tester sans risque

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 4 — Blueprints et workflow professionnel
- **Lecon** : 4/6
- **Duree cible** : 6 min
- **Objectif pedagogique** : Utiliser les sandboxes ZipWP pour tester des plugins, des changements de design et des demos client sans risque pour le site en production.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Tu veux tester un nouveau plugin sur ton site. Ou essayer une refonte du header. Ou montrer une maquette a un client avant de lancer la production. Tu ne vas pas faire ca sur ton site en ligne. Si ca casse, tout le monde le voit.

C'est exactement a ca que servent les sandboxes dans ZipWP. Un site temporaire, isole, ou tu peux tout tester sans consequences.

---

[SECTION 1 — Qu'est-ce qu'un sandbox]

Un sandbox, c'est un site WordPress temporaire. Il fonctionne comme un vrai site — memes plugins, meme admin, meme editeur. Mais il a une duree de vie limitee et il n'est pas indexe par Google.

La duree depend de ton plan ZipWP. En plan gratuit, le sandbox expire apres 24 heures. En plan payant, tu as plus de temps. Verifie les conditions de ton plan pour savoir exactement combien de temps tu disposes.

Le sandbox est totalement independant de tes autres sites. Ce que tu fais dessus — installer un plugin, modifier le theme, casser la base de donnees — n'affecte rien d'autre. C'est un bac a sable au sens propre.

---

[SECTION 2 — Cas d'usage concrets]

Trois scenarios ou le sandbox est indispensable.

Premier scenario : tester un nouveau plugin. Tu as repere un plugin de reservation ou un plugin de galerie. Avant de l'installer sur ton site en production, deploie un sandbox, installe le plugin, teste-le. Si le plugin est bugge ou incompatible avec ta stack, tu le decouvres sans dommage.

Deuxieme scenario : tester un changement de design. Tu veux passer d'un header transparent a un header fixe. Ou changer la typographie du site. Ou reorganiser la page d'accueil. Deploie un sandbox, fais tes modifications, compare avec l'original. Montre les deux versions au client et laisse-le choisir.

Troisieme scenario : demo client. Tu as un prospect qui veut voir a quoi ressemblerait son site avant de signer. Deploie un sandbox, personnalise-le rapidement avec le nom et le secteur du prospect, et envoie-lui le lien. C'est une demo vivante — pas un PDF, pas une maquette Figma. Un vrai site WordPress navigable.

---

[SECTION 3 — Creer et gerer un sandbox]

Pour creer un sandbox, va dans le dashboard ZipWP. Clique sur "Create New Site". Tu peux partir d'un Blueprint existant — c'est souvent le plus rapide — ou partir de zero.

Marque le site comme sandbox dans tes notes ou dans la description. ZipWP ne fait pas forcement la distinction visuelle entre un sandbox et un site permanent. C'est a toi de t'organiser.

Astuce de nommage : prefixe tes sandboxes avec "TEST -" ou "SANDBOX -". Exemple : "TEST - Plugin Bookly" ou "SANDBOX - Refonte header client Dupont". Tu retrouves immediatement ce que c'est dans ta liste de sites.

Quand le test est termine et que tu as tes conclusions, deux options. Si le test est concluant et que tu veux garder le site : convertis le sandbox en site permanent. Chez ZipWP, ca se fait depuis les reglages du site — tu actives l'hebergement permanent.

Si le test n'est pas concluant : laisse le sandbox expirer, ou supprime-le manuellement pour liberer un slot dans ton plan.

---

[SECTION 4 — La regle d'or]

Ne teste jamais sur ton site en production. Jamais. Pas meme "juste pour voir". Pas meme "c'est un petit changement".

Un plugin mal code peut casser ton site en une seconde. Un changement CSS mal place peut rendre tes pages illisibles sur mobile. Une mise a jour de theme non testee peut faire disparaitre ton header.

Le sandbox est la pour ca. Deployer un sandbox prend moins d'une minute. Reparer un site en production casse prend des heures — si tu as un backup. Et beaucoup plus si tu n'en as pas.

---

[OUTRO]

Le sandbox, c'est ton filet de securite. Teste tout ce que tu veux, casse tout ce que tu veux — sans jamais affecter ton site en ligne.

Prochaine lecon : le workflow freelance complet. De l'appel decouverte a la livraison du site — comment livrer un projet en une journee au lieu de deux semaines.

---

## Notes de production

### Captures d'ecran suggerees

1. **Create New Site** — Ecran de creation avec option Blueprint
2. **Liste des sites** — Dashboard avec sandboxes identifies par le prefixe "TEST -"
3. **Plugin test** — Installation d'un plugin dans un sandbox
4. **Demo client** — Site sandbox avec le nom du prospect
5. **Conversion** — Option pour convertir un sandbox en site permanent

### Transitions

- Intro → Section 1 : animation "bac a sable" — zone de test delimitee
- Section 1 → Section 2 : apparition des 3 scenarios avec icones
- Section 2 → Section 3 : zoom sur le dashboard ZipWP
- Section 3 → Section 4 : fond rouge "regle d'or"
- Section 4 → Outro : retour avatar

### Notes HeyGen / ElevenLabs

- Ton protecteur — on veut eviter les erreurs couteuses
- Section 2 : ton concret, exemples parlants
- Section 4 : ton appuye et direct sur la regle d'or
- Articuler "sandbox" clairement — certains debutants ne connaissent pas le terme
