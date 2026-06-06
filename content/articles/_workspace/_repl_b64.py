# -*- coding: utf-8 -*-
"""Apply tutoiement + voix je + cleanup replacements on post 2881499 content."""
import base64, hashlib, io, re

b64 = io.open("content/articles/_workspace/post-2881499-b64.txt", encoding="utf-8").read().strip()
content = base64.b64decode(b64).decode("utf-8")
md5 = hashlib.md5(content.encode("utf-8")).hexdigest()
print("decoded len:", len(content))
print("md5:", md5, "(expected: 4d2dc78ee5fa4f0784c3d4e150ac8dfd)")
print("match:", md5 == "4d2dc78ee5fa4f0784c3d4e150ac8dfd")

pairs = [
    ('<meta charset="utf-8"></meta>', '', 3),
    ('<meta charset="utf-8">', '', 5),
    ("casse-tête pour votre mise en page. Nous <strong>comparons ici tablepress wp table builder</strong> pour identifier la solution adaptée à vos besoins de performance ou de conversion.",
     "casse-tête pour ta mise en page. <strong>Je compare ici TablePress et WP Table Builder</strong> pour identifier la solution adaptée à tes besoins de performance ou de conversion.", 1),
    (">Résumé de notre comparaison TablePress vs WP Table Builder</h2>",
     ">Résumé de mon comparatif TablePress vs WP Table Builder</h2>", 1),
    ("Voici comment ces outils gèrent concrètement vos données.",
     "Voici comment ces outils gèrent concrètement tes données.", 1),
    ("Si vous cherchez l'efficacité brute d'un tableur traditionnel directement dans votre interface d'administration",
     "Si tu cherches l'efficacité brute d'un tableur traditionnel directement dans ton interface d'administration", 1),
    ("L'interface ressemble à Excel. Vous saisissez vos données dans des cellules classiques.",
     "L'interface ressemble à Excel. Tu saisis tes données dans des cellules classiques.", 1),
    ("TablePress gère ainsi des milliers de lignes sans ralentir votre site.",
     "TablePress gère ainsi des milliers de lignes sans ralentir ton site.", 1),
    ("Pour des besoins spécifiques, vous pouvez consulter cet ",
     "Pour des besoins spécifiques, tu peux consulter cet ", 1),
    ("Pour parfaire votre mise en page, découvrez comment maîtriser les ",
     "Pour parfaire ta mise en page, découvre comment maîtriser les ", 1),
    ("L'outil utilise un <strong>système de drag and drop fluide</strong>. Vous glissez simplement les éléments souhaités",
     "L'outil utilise un <strong>système de drag and drop fluide</strong>. Tu glisses simplement les éléments souhaités", 1),
    ("Ils offrent un design propre et moderne dès l'activation du plugin sur votre site.",
     "Ils offrent un design propre et moderne dès l'activation du plugin sur ton site.", 1),
    ("<p>Notre recommandation est d'utiliser ces composants pour <strong>booster vos ventes</strong> :</p>",
     "<p>Ma recommandation est d'utiliser ces composants pour <strong>booster tes ventes</strong> :</p>", 1),
    ("Pour <strong>départager ces deux solutions</strong>, regardons de plus près comment elles gèrent vos données et l'affichage sur les différents écrans.",
     "Pour <strong>départager ces deux solutions</strong>, regarde de plus près comment elles gèrent tes données et l'affichage sur les différents écrans.", 1),
    ("<strong>Le choix dépend de la densité de vos informations</strong>",
     "<strong>Le choix dépend de la densité de tes informations</strong>", 1),
    ("<strong>vitesse de chargement est un critère essentiel</strong> pour votre SEO.",
     "<strong>vitesse de chargement est un critère essentiel</strong> pour ton SEO.", 1),
    ("Pour garantir des résultats optimaux, surveillez l'impact de chaque extension.",
     "Pour garantir des résultats optimaux, surveille l'impact de chaque extension.", 1),
    ("<p>Voici le moment de <strong>trancher selon votre profil et vos objectifs réels</strong> sur votre site.</p>",
     "<p>Voici le moment de <strong>trancher selon ton profil et tes objectifs réels</strong> sur ton site.</p>", 1),
    ("<p>Privilégiez TablePress pour vos bases de données massives.",
     "<p>Privilégie TablePress pour tes bases de données massives.", 1),
    ("<p>Choisissez WP Table Builder pour vos projets d'affiliation. Le design visuel est ici votre meilleur allié. Les boutons d'appel à l'action et les notes étoilées <strong>boosteront vos conversions</strong>.</p>",
     "<p>Choisis WP Table Builder pour tes projets d'affiliation. Le design visuel est ici ton meilleur allié. Les boutons d'appel à l'action et les notes étoilées <strong>boosteront tes conversions</strong>.</p>", 1),
    ("<p>Prenez le temps de tester les versions gratuites avant de sortir la carte bleue. Chaque plugin impose sa propre logique de travail au quotidien. <strong>Le meilleur outil est celui qui s'intègre à votre flux de production habituel</strong>.</p>",
     "<p>Prends le temps de tester les versions gratuites avant de sortir la carte bleue. Chaque plugin impose sa propre logique de travail au quotidien. <strong>Le meilleur outil est celui qui s'intègre à ton flux de production habituel</strong>.</p>", 1),
    ("Pour comparer ces solutions en conditions réelles, vous pouvez utiliser <a ",
     "Pour comparer ces solutions en conditions réelles, tu peux utiliser <a ", 1),
    ("<p>Optez pour TablePress pour gérer des volumes massifs avec la légèreté d'un tableur, ou privilégiez WP Table Builder pour booster vos conversions grâce au glisser-déposer visuel. Entre performance technique et design marketing, <strong>choisissez l'outil adapté à vos objectifs</strong> dès maintenant. Transformez vos données en un atout stratégique mémorable.</p>",
     "<p>Opte pour TablePress pour gérer des volumes massifs avec la légèreté d'un tableur, ou privilégie WP Table Builder pour booster tes conversions grâce au glisser-déposer visuel. Entre performance technique et design marketing, <strong>choisis l'outil adapté à tes objectifs</strong> dès maintenant. Transforme tes données en un atout stratégique mémorable.</p>", 1),
    ("Obtenez des réponses à une liste des questions les plus fréquemment posées.",
     "Obtiens des réponses à une liste des questions les plus fréquemment posées.", 1),
    ("<strong>TablePress est la solution à privilégier</strong> si vous manipulez des fichiers Excel ou CSV volumineux.",
     "<strong>TablePress est la solution à privilégier</strong> si tu manipules des fichiers Excel ou CSV volumineux.", 1),
    ("Il utilise des scripts optimisés qui n'impactent pas vos Core Web Vitals",
     "Il utilise des scripts optimisés qui n'impactent pas tes Core Web Vitals", 1),
    ("Grâce à son constructeur en glisser-déposer, vous pouvez intégrer facilement des éléments interactifs comme des boutons d'appel à l'action, des systèmes de notation par étoiles et des badges de mise en avant directement dans vos cellules.",
     "Grâce à son constructeur en glisser-déposer, tu peux intégrer facilement des éléments interactifs comme des boutons d'appel à l'action, des systèmes de notation par étoiles et des badges de mise en avant directement dans tes cellules.", 1),
    ("WP Table Builder intègre une fonctionnalité native permettant d'<strong>importer directement vos tableaux créés avec TablePress</strong>. Cela facilite grandement la transition si vous décidez de passer",
     "WP Table Builder intègre une fonctionnalité native permettant d'<strong>importer directement tes tableaux créés avec TablePress</strong>. Cela facilite grandement la transition si tu décides de passer", 1),
    ("<p>Notez cependant que si TablePress supporte nativement",
     "<p>Note cependant que si TablePress supporte nativement", 1),
]

result = content
report = []
total_misses = 0
for i, (old, new, expected) in enumerate(pairs, 1):
    count = result.count(old)
    if count != expected:
        total_misses += 1
        report.append(f"  MISS #{i} expected={expected} actual={count} :: {old[:70]!r}")
    else:
        result = result.replace(old, new)
        report.append(f"  OK   #{i} x{count} :: {old[:70]!r}")

print("\n=== REPLACEMENT REPORT ===")
for line in report:
    print(line)
print(f"\nTotal misses: {total_misses}")
print(f"Original len: {len(content)} -> New len: {len(result)} (delta: {len(result)-len(content)})")

remaining_vous = len(re.findall(r"\b(vous|votre|vos)\b", result, re.I))
remaining_nous = len(re.findall(r"\bnous\b|\bnotre\b", result, re.I))
remaining_meta = result.count('<meta charset="utf-8"')
remaining_forced_kw = result.count('tablepress wp table builder')

print("\n=== POST-REWRITE CHECKS ===")
print(f"  remaining vouvoiement: {remaining_vous} (target: 0)")
print(f"  remaining nous/notre:  {remaining_nous} (target: 0)")
print(f"  remaining <meta charset utf-8: {remaining_meta} (target: 0)")
print(f"  remaining 'tablepress wp table builder' lowercase: {remaining_forced_kw} (target: 0)")

if total_misses == 0:
    io.open("content/articles/_workspace/post-2881499-corrected.html","w",encoding="utf-8").write(result)
    b64_new = base64.b64encode(result.encode("utf-8")).decode("ascii")
    io.open("content/articles/_workspace/post-2881499-corrected-b64.txt","w",encoding="utf-8").write(b64_new)
    md5_new = hashlib.md5(result.encode("utf-8")).hexdigest()
    print(f"\n  WROTE corrected content len={len(result)} md5={md5_new}")
else:
    print("\n  NOT WRITTEN (misses detected)")
