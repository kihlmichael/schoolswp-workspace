#!/usr/bin/env python3
"""
Enrichment patcher for post 2871653 (FluentCRM 10 automations).

Strategy: targeted, conservative regex inserts on KNOWN safe anchor strings.
Each insertion is wrapped in EDIT MARKERS (HTML comments) so the diff is auditable
and the changes can be reverted by another script if needed.

NO modification to:
- Rank Math meta (rule: edit via plugin sidebar only)
- Kadence gradients (rule: wp_unslash strips \ — use $wpdb->update direct)
- Ninja Tables block (external DB)
- Top "L'essentiel a retenir" box
- Existing internal links
- Excerpt / categories / status
"""

import json
import re
import sys
from difflib import unified_diff
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "articles" / "_workspace" / "post-2871653-current.json"
DST = ROOT / "content" / "articles" / "_workspace" / "post-2871653-enriched.json"
DIFF_OUT = ROOT / "content" / "articles" / "_workspace" / "post-2871653-diff.md"

data = json.loads(SRC.read_text(encoding="utf-8"))
c = data["content"]["raw"]
orig = c

# Each rule = (label, regex_to_find_anchor, replacement_callable_or_string)
# We always check that the anchor exists exactly once to avoid silent failures.

inserts = []


def add_rule(label, pattern, replacement, *, count_expected=1):
    inserts.append((label, pattern, replacement, count_expected))


# --- Rule 1: in "Comprendre les bases" intro paragraph, mention SMTP prereq with link ---
# Anchor: the paragraph right after the H2 "Comprendre les bases" + first sentence
# Insert a short follow-up sentence with a link to fluentsmtp-avis at end of intro section.
# Safer: locate the H3 "Statuts d'abonnement et conformite RGPD" closing paragraph.
add_rule(
    "L1-fluentsmtp-link-after-RGPD-section",
    # match the last paragraph BEFORE the H2 "1. Bienvenue newsletter"
    r'(<!-- /wp:paragraph -->\s*)(<!-- wp:heading -->\s*<h2 class="wp-block-heading"[^>]*>1\. Bienvenue newsletter)',
    (
        r'\1'
        + '<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12">'
        + 'Un dernier prérequis avant de plonger dans les workflows : '
        + 'une délivrabilité propre. Si tu n\'as pas encore branché un vrai SMTP, '
        + 'commence par <a href="https://schoolswp.com/fluentsmtp-avis/" '
        + 'target="_blank" rel="noopener">FluentSMTP</a> '
        + '(gratuit, made by le même éditeur que FluentCRM) et passe-le sur '
        + '<a href="https://fluentcrm.com/docs/introduction-to-fluentcrm-automation/" '
        + 'target="_blank" rel="noopener noreferrer">la doc officielle FluentCRM</a> '
        + 'pour bien comprendre la logique trigger / action / benchmark avant de cliquer dans le builder.'
        + '</p>\n'
        + '<!-- /wp:paragraph -->\n\n'
        + r'\2'
    ),
)

# --- Rule 2: workflow #3 (panier abandonne WC), suggest FluentCart alternative ---
add_rule(
    "L2-fluentcart-alt-in-cart-abandon",
    r'(<h2 class="wp-block-heading"[^>]*>3\. Récupération de panier abandonné[^<]*</h2>\s*<!-- /wp:heading -->)',
    (
        r'\1'
        + '\n\n<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12"><em>Tu n\'es pas sur WooCommerce ? '
        + 'Si tu tournes sur <a href="https://schoolswp.com/fluentcart-gratuit-vs-pro/" '
        + 'target="_blank" rel="noopener">FluentCart</a>, le déclencheur natif '
        + '"Cart Abandoned" existe et le funnel ci-dessous se construit à l\'identique, '
        + 'avec une intégration encore plus fluide côté tags et statuts.</em></p>\n'
        + '<!-- /wp:paragraph -->'
    ),
)

# --- Rule 3: workflow #4 onboarding post-achat -> mention OttoKit pour triggers externes ---
add_rule(
    "L3-ottokit-link-onboarding",
    r'(<h2 class="wp-block-heading"[^>]*>4\. Onboarding client post-achat[^<]*</h2>\s*<!-- /wp:heading -->)',
    (
        r'\1'
        + '\n\n<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12"><em>Pour brancher des déclencheurs qui ne sont '
        + 'pas natifs FluentCRM (Stripe direct, Calendly, Notion, etc.), je passe par '
        + '<a href="https://schoolswp.com/ottokit-avis-automatisation-wordpress/" '
        + 'target="_blank" rel="noopener">OttoKit</a> en amont du funnel : il pousse '
        + 'l\'événement vers FluentCRM via webhook, ce qui élargit drastiquement les '
        + 'cas d\'usage d\'onboarding.</em></p>\n'
        + '<!-- /wp:paragraph -->'
    ),
)

# --- Rule 4: workflow #10 TutorLMS deeper link ---
# Anchor: H2 "10. Synchronisation CRM <-> TutorLMS / MemberPress"
add_rule(
    "L4-tutorlms-deep-link",
    r'(<h2 class="wp-block-heading"[^>]*>10\. Synchronisation CRM[^<]*</h2>\s*<!-- /wp:heading -->)',
    (
        r'\1'
        + '\n\n<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12"><em>Si tu n\'as pas encore choisi ton LMS, '
        + 'lis d\'abord <a href="https://schoolswp.com/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/" '
        + 'target="_blank" rel="noopener">mon retour complet sur TutorLMS</a> : '
        + 'c\'est celui que je fais tourner sur schoolsWP, '
        + 'précisément parce que sa synchro FluentCRM (enrollment, completion, drop-off) '
        + 'est la plus propre côté triggers natifs.</em></p>\n'
        + '<!-- /wp:paragraph -->'
    ),
)

# --- Rule 5: section "Quand passer a FluentCRM Pro ?" - add comparator link Groundhogg vs FluentCRM ---
add_rule(
    "L5-groundhogg-vs-fluentcrm-link",
    r'(<h2 class="wp-block-heading"[^>]*>Quand passer à FluentCRM Pro\s*\?\s*</h2>\s*<!-- /wp:heading -->)',
    (
        r'\1'
        + '\n\n<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12"><em>Avant d\'arbitrer free vs Pro, certains '
        + 'lecteurs se demandent s\'il ne faut pas carrément regarder ailleurs. '
        + 'J\'ai comparé les deux principaux CRM auto-hébergés WordPress dans '
        + '<a href="https://schoolswp.com/comparatif-groundhogg-vs-fluentcrm/" '
        + 'target="_blank" rel="noopener">Groundhogg vs FluentCRM</a> : '
        + 'spoiler, je suis resté sur FluentCRM, mais la grille de décision t\'évitera '
        + 'des regrets si ton volume dépasse les 50 000 contacts.</em></p>\n'
        + '<!-- /wp:paragraph -->'
    ),
)

# --- Rule 6: in H3 "Les declencheurs (triggers) qui demarrent un funnel",
#            add an external link to fluentcrm docs primary triggers (E-E-A-T) ---
add_rule(
    "L6-fluentcrm-docs-triggers-link",
    r'(<h3 class="wp-block-heading"[^>]*>Les déclencheurs \(triggers\) qui démarrent un funnel</h3>\s*<!-- /wp:heading -->)',
    (
        r'\1'
        + '\n\n<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12"><em>La liste exhaustive et à jour des '
        + 'déclencheurs disponibles vit côté <a href="https://fluentcrm.com/docs/fluentcrm-automation-triggers/" '
        + 'target="_blank" rel="noopener noreferrer">documentation officielle FluentCRM (primary triggers)</a>. '
        + 'Ce que je liste ci-dessous, ce sont les déclencheurs que j\'ai effectivement '
        + 'connectés sur schoolsWP, pas la totalité possible.</em></p>\n'
        + '<!-- /wp:paragraph -->'
    ),
)

# --- Rule 7: in "Etape 1 : configurer le declencheur initial",
#            add link to fluentcrm automation editor docs ---
add_rule(
    "L7-fluentcrm-docs-editor-link",
    r'(<h3 class="wp-block-heading"[^>]*>Étape 1 : configurer le déclencheur initial</h3>\s*<!-- /wp:heading -->)',
    (
        r'\1'
        + '\n\n<!-- wp:paragraph {"className":"sw-enrich-2026-05-12"} -->\n'
        + '<p class="sw-enrich-2026-05-12"><em>Capture d\'écran à jour de l\'éditeur '
        + 'FluentCRM côté <a href="https://fluentcrm.com/docs/automation-editor/" '
        + 'target="_blank" rel="noopener noreferrer">documentation officielle (Automation Editor)</a> '
        + 'si tu veux comparer avec ta version de plugin avant de cliquer.</em></p>\n'
        + '<!-- /wp:paragraph -->'
    ),
)

# Apply
report = []
for label, pat, repl, count_expected in inserts:
    found = len(re.findall(pat, c))
    if found != count_expected:
        report.append((label, found, count_expected, "SKIPPED"))
        continue
    c = re.sub(pat, repl, c, count=1)
    report.append((label, found, count_expected, "APPLIED"))

print("ENRICHMENT RULES")
print("-" * 80)
for label, found, expected, status in report:
    print(f"  [{status}] {label}  (anchor found {found}x, expected {expected}x)")
print()

# Write enriched JSON (preserving everything else)
new_data = json.loads(SRC.read_text(encoding="utf-8"))
new_data["content"]["raw"] = c
DST.write_text(json.dumps(new_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"[OK] wrote -> {DST}")
print(f"      orig content : {len(orig)} chars")
print(f"      new  content : {len(c)} chars  (delta +{len(c) - len(orig)} chars)")

# Approx word delta
def words(t):
    return len(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).strip().split())

print(f"      orig words   : {words(orig)}")
print(f"      new  words   : {words(c)}  (delta +{words(c) - words(orig)})")

# Compact diff focused on inserted blocks
print()
print("INSERTED HUNKS (extract)")
print("-" * 80)
new_blocks = re.findall(
    r'<!-- wp:paragraph \{"className":"sw-enrich-2026-05-12"\} -->.*?<!-- /wp:paragraph -->',
    c, re.DOTALL,
)
for i, b in enumerate(new_blocks, 1):
    plain = re.sub(r"<[^>]+>", " ", b)
    plain = re.sub(r"\s+", " ", plain).strip()
    print(f"  Insert #{i}: {plain[:280]}{'...' if len(plain) > 280 else ''}")
    print()

DIFF_OUT.write_text(
    "# Post 2871653 enrichment diff (preview)\n\n"
    + "## Rules\n\n"
    + "\n".join(f"- **[{s}]** {l}  (anchor found {f}/{e})" for l, f, e, s in report)
    + "\n\n## Inserted hunks\n\n"
    + "\n\n".join(
        "```html\n" + b + "\n```"
        for b in new_blocks
    )
    + f"\n\n---\n\nNew content size: {len(c)} chars ({len(c) - len(orig):+}c) | "
    + f"words {words(c)} ({words(c) - words(orig):+})\n",
    encoding="utf-8",
)
print(f"[OK] diff written -> {DIFF_OUT}")
