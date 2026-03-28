---
name: email-to-content
description: Transformer un email promotionnel WordPress (plugin ou theme) en 3 contenus marketing schoolsWP (resume Markdown, post LinkedIn, thread X) via methode 5 etapes V1/auto-evaluation/corrections/V2/comparaison+V3. Utiliser quand l'utilisateur fournit un email promo et exige un format de sortie strict et anti-invention.
---

Pense en profondeur. Suis la checklist. Respecte toutes les contraintes. Ne devine rien.

# SchoolsWP Email to Content

## Regles de base
- Ecrire en francais par defaut.
- Style schoolsWP : clair, direct, pedagogique, humain, concret, zero blabla marketing.
- Ne jamais inventer. Utiliser uniquement les infos de l'email.
- Si une info manque, ecrire exactement : "Info non fournie".
- CTA affilie obligatoire et naturel, avec disclosure "(lien affilie)".
- Reponse unique, sections dans l'ordre impose, sans texte hors sections.

## Entrees attendues (schema)
```xml
<task>
  <email_promo>...</email_promo>
  <brand>schoolsWP</brand>
  <author>Michael KIHL</author>
  <audience>freelances et independants WordPress</audience>
  <constraints>
    <anti_invention>true</anti_invention>
    <cta_affilie>true</cta_affilie>
    <single_response>true</single_response>
  </constraints>
  <output_format>
    EXTRACTION
    V1 — Resume Markdown
    V1 — LinkedIn
    V1 — Thread X
    Auto-evaluation
    Corrections
    V2 — Resume Markdown
    V2 — LinkedIn
    V2 — Thread X
    Comparaison V1 vs V2
    V3 FINAL — Resume Markdown
    V3 FINAL — LinkedIn
    V3 FINAL — Thread X
  </output_format>
</task>
```

## Sorties attendues (format verrouille)
- Produire exactement les 11 sections dans l'ordre impose.
- Ne pas ajouter d'intro ni de conclusion hors sections.
- Respecter les contraintes de longueur et structure par section.

## Workflow RUN (execution)
1) Verifier que l'email est fourni.
2) EXTRACTION : extraire toutes les infos en puces (voir liste obligatoire).
3) V1 : produire les 3 contenus selon contraintes.
4) Auto-evaluation : noter /5 + commentaires courts + 5 faiblesses actionnables.
5) Corrections : plan numerote avec actions precises.
6) V2 : reecrire les 3 contenus en appliquant corrections.
7) Comparaison V1 vs V2 : 5-8 lignes, expliquer ameliorations.
8) V3 FINAL : livrer versions finales pretes a publier.

## Checklist de contraintes par livrable
### Resume Markdown
- H1 avec mot-cle principal.
- Meta description 150-160 caracteres.
- Slug conseille.
- 6-10 mots-cles pertinents integres naturellement.
- H2 : A qui ca s'adresse ?
- H2 : Ce que ca change concretement (liste).
- H2 : Fonctionnalites cles (liste).
- H2 : Prix/offre/deadline ou "Info non fournie".
- H2 : Mon avis rapide (factuel, usage).
- Conclusion + CTA avec "(lien affilie)".
- FAQ 2-3 questions uniquement si pertinent et base sur l'email.

### LinkedIn
- 1200-1800 caracteres.
- Hook 1-2 lignes.
- Contexte terrain sans inventer.
- 3-6 bullets valeur (benefices + pour qui + cas d'usage).
- CTA + "(lien affilie)".
- Question finale.
- 3-5 hashtags max.

### Thread X
- 6-8 tweets max, numerotation 1/7, 2/7, etc.
- ~260 caracteres max par tweet.
- 1/ : probleme + promesse.
- 2-5/ : valeur (benefices, points cles, erreurs evitees, cas d'usage).
- Avant-dernier : pour qui / pour qui pas.
- Dernier : CTA + lien + "(lien affilie)" ou #ad + question.

## Anti-hallucination
- Ne pas inventer prix, promesse, preuves, liens, garanties.
- Marquer "Info non fournie" si absent.
- Ne pas extrapoler d'usage non mentionne.
- Ne pas ajouter de superlatifs non justifies.

## Mandat Socratique (si email absent ou incomplet)
Poser max 7 questions prioritaires. Proposer 2 hypotheses optionnelles.
Questions minimales :
1) Peux-tu coller l'email promo complet ?
2) Le produit est-il un plugin ou un theme (si non explicite) ?
3) Y a-t-il un lien d'affiliation exact a utiliser ?
4) Y a-t-il un prix/promo/deadline/garantie dans l'email ?
5) Y a-t-il une promesse ou un resultat chiffre ?
6) Des preuves ou temoignages mentionnes ?
7) Langue et ton confirment-ils le style schoolsWP ?

Hypotheses optionnelles :
- A : pas de prix ni deadline -> "Info non fournie".
- B : lien non fourni -> "Info non fournie".

## Fail-safe
Si les contraintes sont incompatibles (ex: "une seule reponse" mais l'email manque), suspendre.
Expliquer en 2-4 lignes.
Proposer 2 solutions :
A) Fournir l'email complet.
B) Autoriser un brouillon base sur infos partielles avec "Info non fournie".
Demander validation.

## Auto-evaluation (obligatoire)
- Noter 6 criteres /5 avec commentaires courts.
- Lister 5 faiblesses actionnables.
- Si score global < 9/10, corriger avant V2.

## Tests rapides
- Test nominal : email complet avec prix, lien, deadline.
- Test edge : email sans prix ni lien.
- Test edge : email tres court (peu de features).

## Gouvernance
- Versionner les evolutions de format.
- Ne pas changer l'ordre des sections sans accord explicite.
- Journaliser les changements majeurs dans les demandes utilisateur.

## Architecture Cloud
```
schoolswp-email-to-content/
├── SKILL.md         # Instructions et workflow
```

## Workflow
### BUILD MODE
- Definir le format de sortie strict (11 sections).
- Lister contraintes non negociables (anti-invention, CTA, style).
- Specifier schema d'entrees et checklist par livrable.
- Prevoir mandat socratique et fail-safe.
- Definir tests et criteres de reussite.
- Versionner le format et les regles.

### RUN MODE
- Verifier presence de l'email.
- Executer EXTRACTION -> V1 -> Auto-evaluation -> Corrections -> V2 -> Comparaison -> V3.
- Respecter format verrouille et style schoolsWP.
- Inserer "Info non fournie" si besoin.

## Securite
- Anti-hallucination : zero invention, "Info non fournie" si manquant.
- Mandat Socratique : questions minimales si email absent.
- Fail-Safe : suspendre si contradictions.
- Contraintes negatives : pas de jargon inutile, pas de promesses non prouvees, pas de texte hors sections.

## Human-In-The-Loop
- Checkpoint 1 : valider l'email fourni (si ambigu).
- Checkpoint 2 : confirmer si une seule reponse est exigee.
- Checkpoint 3 : demander validation si le lien affilie est absent.
- Si l'utilisateur exige "une seule reponse", ne pas interrompre.

## Gouvernance & KPI
- Versioning : v1.0.0 a la creation, incrementer en cas de changement de format.
- KPIs : taux de conformite format, taux d'info manquante, taux de CTA correct.
- Changelog : conserver un resume des ajustements de contraintes.
- Upgrade si : format stable + retours d'usage positifs + zero violations d'anti-invention.

## Tests
- Cas nominal : email complet -> toutes sections remplies, CTA present.
- Cas edge 1 : email sans prix -> "Info non fournie".
- Cas edge 2 : email sans lien -> "Info non fournie".
- Cas edge 3 : email vague -> mandat socratique.
- Reussite : format exact + zero invention + CTA conforme.

## Grille d'auto-evaluation
- Clarte & lisibilite /10
- SEO (structure + mots-cles) /10
- Accroches /10
- CTA /10
- Engagement LinkedIn /10
- Engagement X /10
- Respect des contraintes /10
- Seuil : 9/10 minimum

## Exemple d'activation RUN MODE
```
<task>
  <email_promo>[COLLER ICI L'EMAIL PROMOTIONNEL]</email_promo>
  <brand>schoolsWP</brand>
  <author>Michael KIHL</author>
  <audience>freelances WordPress</audience>
  <constraints>
    <anti_invention>true</anti_invention>
    <cta_affilie>true</cta_affilie>
    <single_response>true</single_response>
  </constraints>
  <output_format>sections strictes en 11 blocs</output_format>
</task>
```
