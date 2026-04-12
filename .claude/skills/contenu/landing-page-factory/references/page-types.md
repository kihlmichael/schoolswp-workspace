# Page Types — Layouts par type de produit

Le layout d'une landing page doit correspondre a ce que le visiteur attend pour ce type de produit.
Un plugin WP et un SaaS ne se presentent pas de la meme facon.

## Plugin WordPress

**Comportement visiteur** : cherche a resoudre un probleme precis, veut voir que ca marche avec son setup.

```
Layout recommande :
┌─────────────────────────────────┐
│ Hero : headline + screenshot WP │
│ Preuve : installs actives + note│
├─────────────────────────────────┤
│ Probleme → Solution (3 blocs)   │
├─────────────────────────────────┤
│ Feature Grid (3-4 colonnes)     │
│ icone + titre + 1 phrase        │
├─────────────────────────────────┤
│ Compatibilite / Integrations    │
│ logos des plugins compatibles   │
├─────────────────────────────────┤
│ Temoignages (2-3 verbatim)      │
├─────────────────────────────────┤
│ Pricing (si freemium : CTA free)│
│ CTA : "Telecharger" ou "Essayer"│
├─────────────────────────────────┤
│ FAQ (3-5 questions)             │
└─────────────────────────────────┘
```

**CTA principal** : "Installer gratuitement" ou "Essayer la version gratuite"
**Couleur CTA** : derivee de la couleur primaire du plugin
**Preuves prioritaires** : installations actives, note WordPress.org, temoignages

---

## Theme WordPress

**Comportement visiteur** : veut VOIR le resultat visuel avant tout.

```
Layout recommande :
┌─────────────────────────────────┐
│ Hero : demo visuelle plein ecran│
│ (screenshot ou mockup du theme) │
├─────────────────────────────────┤
│ Galerie : 3-4 demos/variantes  │
│ (cliquables vers live preview)  │
├─────────────────────────────────┤
│ Features techniques (grille)    │
│ responsive, speed, customizable │
├─────────────────────────────────┤
│ Avant/Apres ou Comparaison      │
├─────────────────────────────────┤
│ Temoignages visuels             │
│ (avec screenshots des sites)    │
├─────────────────────────────────┤
│ Pricing + CTA live preview      │
└─────────────────────────────────┘
```

**CTA principal** : "Voir la demo live" ou "Previsualiser le theme"
**Element cle** : les visuels dominent — le texte est secondaire
**Preuves prioritaires** : screenshots de vrais sites, vitesse PageSpeed

---

## SaaS (proche ecosysteme WP)

**Comportement visiteur** : compare avec des alternatives, cherche le ROI.

```
Layout recommande :
┌─────────────────────────────────┐
│ Hero : probleme + solution      │
│ (pas de screenshot produit)     │
│ CTA : "Commencer l'essai"      │
├─────────────────────────────────┤
│ Social proof bar                │
│ logos clients ou chiffres cles  │
├─────────────────────────────────┤
│ 3 benefices (icone + texte)     │
│ centres sur le RESULTAT         │
├─────────────────────────────────┤
│ Comment ca marche (3 etapes)    │
│ 1. Connecte → 2. Configure → 3.│
├─────────────────────────────────┤
│ Temoignage long (cas client)    │
├─────────────────────────────────┤
│ Comparaison vs alternative      │
│ (tableau 2 colonnes)            │
├─────────────────────────────────┤
│ Pricing + garantie              │
│ CTA : "Essai gratuit 14 jours" │
├─────────────────────────────────┤
│ FAQ (objections deguisees)      │
└─────────────────────────────────┘
```

**CTA principal** : "Essai gratuit" ou "Demarrer maintenant"
**Element cle** : le probleme doit etre ressenti des la hero section
**Preuves prioritaires** : ROI chiffre, cas clients, comparaison factuelle

---

## Formation / Cours en ligne

**Comportement visiteur** : veut savoir ce qu'il va apprendre et si ca vaut son temps.

```
Layout recommande :
┌─────────────────────────────────┐
│ Hero : promesse de resultat     │
│ "Apprends a [X] en [temps]"    │
│ CTA : "S'inscrire gratuitement"│
├─────────────────────────────────┤
│ Pour qui ? (3 personas)         │
├─────────────────────────────────┤
│ Programme / Curriculum          │
│ (modules avec duree estimee)    │
├─────────────────────────────────┤
│ Instructeur (photo + bio courte)│
├─────────────────────────────────┤
│ Temoignages d'apprenants        │
├─────────────────────────────────┤
│ Ce que tu sauras faire apres    │
│ (liste concrete, pas abstraite) │
├─────────────────────────────────┤
│ Pricing / Inscription           │
│ CTA : "Commencer la formation"  │
└─────────────────────────────────┘
```

**CTA principal** : "S'inscrire" ou "Commencer gratuitement"
**Element cle** : le curriculum detaille rassure
**Preuves prioritaires** : resultats d'apprenants, nombre d'inscrits, note

---

## Regles transversales (tous types)

1. **Mobile first** : designer pour 375px d'abord, puis elargir
2. **Un seul CTA par section** : ne pas noyer l'action
3. **Espacement genereux** : padding section >= 60px desktop, 40px mobile
4. **Contraste CTA** : le bouton doit avoir un ratio >= 4.5:1
5. **Pas de carousel** : afficher les temoignages en grille ou en stack
6. **Lazy load images** : `loading="lazy"` sur toutes les images sauf hero
7. **Schema markup** : `Product` pour plugins/themes, `Course` pour formations, `SoftwareApplication` pour SaaS
