# Section Changelog & Misc

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## User Guides & Developer Docs - FluentCart Documentation
URL : https://docs.fluentcart.com/

[Skip to content](https://docs.fluentcart.com/#VPContent)

# FluentCart Documentation

Everything you need to build and manage your online store with FluentCart

Version: Pre-Release BetaDoc Status: Under Development

🚀

### Getting Started

Learn the basics of FluentCart and set up your first store

[Get Started →](https://docs.fluentcart.com/guide/getting-started/installation-activation.html)

🛍️

### Store Management

Manage products, orders, and customers efficiently

[Learn More →](https://docs.fluentcart.com/guide/store-management/)

📦

### Inventory & Products

Handle inventory and create different product types

[Explore →](https://docs.fluentcart.com/guide/product-types-creation/)

💳

### Payments & Shipping

Set up payment gateways and shipping methods

[Configure →](https://docs.fluentcart.com/guide/payments-checkout/)

📊

### Analytics & Reports

Track your store's performance and growth

[View Reports →](https://docs.fluentcart.com/guide/reporting-analytics/)

🛠️

### Developer Docs

Extend FluentCart with custom functionality

[Start Coding →](https://dev.fluentcart.com/)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## CLAUDE.md - FluentCart Documentation - FluentCart Documentation
URL : https://docs.fluentcart.com/CLAUDE

[Skip to content](https://docs.fluentcart.com/CLAUDE#VPContent)

# CLAUDE.md - FluentCart Documentation [​](https://docs.fluentcart.com/CLAUDE\#claude-md-%E2%80%94-fluentcart-documentation)

This file tells Claude exactly how to work in this repo. Read it fully before any task.

* * *

## 1\. What this project is [​](https://docs.fluentcart.com/CLAUDE\#_1-what-this-project-is)

A **VitePress 1.6.4** static documentation site for **FluentCart**, a WordPress e-commerce plugin.

| Field | Value |
| --- | --- |
| Live site | [https://docs.fluentcart.com](https://docs.fluentcart.com/) |
| Dev docs (separate repo) | [https://dev.fluentcart.com/](https://dev.fluentcart.com/) |
| Marketing site | [https://fluentcart.com](https://fluentcart.com/) |
| Status | Pre-Release Beta |
| Working dir | `/Users/authlab-24/Desktop/fluent-cart-docs` |
| Git branch | `master` (also the PR base) |

**No backend, no CI/CD, no test suite.** Every change is a content edit or a config edit.

* * *

## 2\. Repo layout (memorize this) [​](https://docs.fluentcart.com/CLAUDE\#_2-repo-layout-memorize-this)

```
.
├── .vitepress/
│   └── config.mjs              # Site config: head meta, sitemap, nav, sidebar, markdown plugins
├── guide/                      # ALL user-facing docs live here
│   ├── public/images/<section>/...   # Images (.webp) - served at /images/<section>/
│   ├── getting-started/
│   ├── product-types-creation/
│   ├── store-management/
│   ├── payments-checkout/
│   │   └── connecting-payment-gateways/   # Per-gateway docs (stripe-settings.md, etc.)
│   ├── shipping/
│   ├── tax-&-duties/                      # Note the literal `&` in folder name
│   ├── customer-dashboard/
│   ├── marketing-sales-tools/
│   ├── integrations/
│   ├── reporting-analytics/
│   ├── settings-configuration/
│   ├── storage/
│   ├── customization-and-themes/
│   ├── browsing-history/
│   ├── migration/edd/
│   ├── troubleshooting-support/
│   └── changelog.md
├── developer/index.md          # Stub - main dev docs are at dev.fluentcart.com
├── public/                     # Site-level assets: logo-full.png, logo-full-dark.svg, robots.txt
└── index.md                    # Home page (uses layout: home)
```

`vite.publicDir` is set to `'guide/public'`, which is why image paths are `/images/...` (not `/guide/public/images/...`).

* * *

## 3\. Commands (only ones that exist) [​](https://docs.fluentcart.com/CLAUDE\#_3-commands-only-ones-that-exist)

bash

```
npm run docs:dev           # Local dev with HMR
npm run docs:build         # Production build → .vitepress/dist/
npm run docs:clean-build   # Wipe .vitepress/cache + .vitepress/dist, then build
npm run docs:preview       # Preview the built site
```

There is **no** lint, no typecheck, no test command. Don't invent ones.

* * *

## 4\. Page rules (follow exactly) [​](https://docs.fluentcart.com/CLAUDE\#_4-page-rules-follow-exactly)

### 4.1 Frontmatter [​](https://docs.fluentcart.com/CLAUDE\#_4-1-frontmatter)

- **Regular doc pages: NO frontmatter.** Start the file with an H1 (`# Page Title`). The introduction, integrations, and most pages follow this.
- **Home page (`index.md` only):** uses `layout: home` plus hero/features blocks.
- **SEO is automatic.**`config.mjs` injects canonical URL, OpenGraph, Twitter card, JSON-LD `TechArticle`, breadcrumbs, and sitemap entry per page. Do **not** add `<meta>` tags or duplicate JSON-LD in pages.

### 4.2 Heading hierarchy [​](https://docs.fluentcart.com/CLAUDE\#_4-2-heading-hierarchy)

- `#` once at the top = page title.
- `##` = main sections.
- `###` = sub-sections.
- `####` = procedural sub-steps inside a `###`.
- `outline: [2, 3]` - only H2/H3 appear in the right-hand outline. Don't put critical navigation under H4.

### 4.3 Links [​](https://docs.fluentcart.com/CLAUDE\#_4-3-links)

- Internal links use clean URLs: `/guide/<section>/<page-slug>` (no `.md`, no `.html`).
- Section index pages: link as `/guide/<section>/` or `/guide/<section>/index`.
- External links auto-open in a new tab via a global markdown rule - do **not** add `target="_blank"` manually.
- `ignoreDeadLinks: true` is set, so broken links don't fail the build. Still get them right.

### 4.4 Images [​](https://docs.fluentcart.com/CLAUDE\#_4-4-images)

- Store: `guide/public/images/<section>/<subsection>/<file>.webp`
- Reference: `![Descriptive alt text](/images/<section>/<subsection>/<file>.webp)`
- Prefer `.webp`. Always include meaningful alt text (existing convention is `Screenshot of <thing>`).

### 4.5 Bold formatting (existing convention - match it) [​](https://docs.fluentcart.com/CLAUDE\#_4-5-bold-formatting-existing-convention-%E2%80%94-match-it)

- UI navigation paths: `**FluentCart Pro → Integrations**`
- Field labels (with colon): `**Feed Title:**`
- Button names: `**Add Integration**`
- Emphasized terms inside paragraphs: `**Global Integrations**`

### 4.6 Lists [​](https://docs.fluentcart.com/CLAUDE\#_4-6-lists)

- Numbered (`1. 2. 3.`) for ordered procedures.
- Bullets (`*` or `-`) for unordered enumerations and feature lists.

### 4.7 Voice & tone [​](https://docs.fluentcart.com/CLAUDE\#_4-7-voice-tone)

- Second person ("you"), present tense, action-first.
- Friendly, concise, instructional. Avoid marketing fluff inside guides.
- Cross-link aggressively to related pages - see `guide/getting-started/introduction-fluentcart.md` as the model.

### 4.8 Directives in use [​](https://docs.fluentcart.com/CLAUDE\#_4-8-directives-in-use)

- `::: info ... :::` for informational callouts. Other VitePress containers (tip/warning/danger/details) are available; use sparingly and only when consistent with neighboring pages.

* * *

## 5\. Adding or editing pages - the workflow [​](https://docs.fluentcart.com/CLAUDE\#_5-adding-or-editing-pages-%E2%80%94-the-workflow)

1. **Locate the right section** under `guide/`. File slug = URL slug.
2. **Create/edit the `.md`** following section 4.
3. **Add to the sidebar** in `.vitepress/config.mjs` under `themeConfig.sidebar['/guide/']`. Sidebar shape:
js

```
{ text: 'Group Title', collapsed: true, items: [\
       { text: 'Page Title', link: '/guide/section/page-slug' },\
       // Nested sub-items are supported (see Product Types & Orders Management groups):\
       { text: 'Parent Page', link: '/guide/section/', items: [\
           { text: 'Child Page', link: '/guide/section/child-slug' }\
       ]}\
]}
```

4. **Add images** to `guide/public/images/<section>/`.
5. **Run `npm run docs:dev`** and verify the page renders, the sidebar updates, images load, and internal links resolve.

When deleting a page, also remove its sidebar entry - orphan entries produce dead nav links.

* * *

## 6\. Editing the changelog [​](https://docs.fluentcart.com/CLAUDE\#_6-editing-the-changelog)

`guide/changelog.md` is the public changelog. Append new releases at the **top**, following the existing heading + bullet format. Don't reformat past entries.

* * *

## 7\. Things NOT to do [​](https://docs.fluentcart.com/CLAUDE\#_7-things-not-to-do)

- Don't add a README.md or any new top-level docs unless explicitly asked - this CLAUDE.md is the project guide.
- Don't add frontmatter `title:` to regular pages (the H1 is the title). The Intro and integration files contain none.
- Don't add manual SEO meta tags, canonical links, or JSON-LD - `transformPageData` in `config.mjs` already handles all of it.
- Don't edit `.vitepress/dist/` or `.vitepress/cache/` - generated.
- Don't change `vite.publicDir`, `cleanUrls`, or `ignoreDeadLinks` without explicit user approval.
- Don't introduce new dependencies for trivial reasons. Current deps: `vitepress`, `ufo` (URL utils used in config), `turndown` (HTML→MD utility).
- Don't rename folders containing literal `&` (e.g. `tax-&-duties/`) - links in many pages depend on this exact spelling.
- Don't use Bash for content analysis when a Read or Edit fits.
- Don't commit unless the user asks.

* * *

## 8\. Things to ALWAYS do [​](https://docs.fluentcart.com/CLAUDE\#_8-things-to-always-do)

- Read this file first.
- Match existing tone/style by skimming a neighboring page in the same section before writing a new one.
- Update the sidebar whenever you add, rename, or remove a page.
- Keep image alt text descriptive.
- Use the exact section folder names already present.
- Run `npm run docs:dev` after structural changes (sidebar, new files, renames) to confirm the site still builds and navigates correctly.

* * *

## 9\. Quick reference [​](https://docs.fluentcart.com/CLAUDE\#_9-quick-reference)

- VitePress config: `.vitepress/config.mjs` (518 lines: `transformPageData`, sitemap, markdown plugin, nav, full sidebar)
- Sidebar lives at: `.vitepress/config.mjs` → `themeConfig.sidebar['/guide/']`
- Nav lives at: `.vitepress/config.mjs` → `themeConfig.nav`
- Image base: `/images/...` (mapped from `guide/public/images/`)
- Site assets (logos, robots.txt): `public/`
- Home: `index.md` • Changelog: `guide/changelog.md` • Dev stub: `developer/index.md`

* * *

## 10\. Code-aware doc updates (plugin → docs sync) [​](https://docs.fluentcart.com/CLAUDE\#_10-code-aware-doc-updates-plugin-%E2%86%92-docs-sync)

When a request requires reading the FluentCart **plugin source code** (e.g. "update docs for v1.3.27", "document the new tax country toggle", "what changed in the plugin since 1.3.26"), load the orchestrator skill **`fluentcart-code-to-docs`**. It coordinates reading the plugin → mapping changes to doc pages → writing updates via the existing template specialists.

**Plugin source location (hardcoded sibling repo):**

```
/Users/authlab-24/Desktop/fluent-cart
```

Default branch is `development`. Tags are plain numbers (`1.3.27`), no `v` prefix. The plugin clone is **read-only** from this session - never edit, commit, or push to it.

**Helper scripts** under `scripts/plugin/`:

| Script | Purpose |
| --- | --- |
| `./scripts/plugin/pull.sh` | Fetch + fast-forward pull on the plugin repo's current branch _(legacy - the user now owns pulls; see plugin-memory note below)_ |
| `./scripts/plugin/recent-changes.sh [N]` | Last N plugin commits with subject + file count (default 20) |
| `./scripts/plugin/diff-since.sh <ref>` | Commits + changed files between `<ref>` and HEAD |
| `./scripts/plugin/find-doc.sh <pattern>` | Locate doc pages mentioning a feature keyword |
| `./scripts/plugin/sync-memory.sh <prev-ref>` | Refresh the plugin-memory layer after a pull. Lists changed PHP/Vue files, prints the `ctx_index` invocation Claude should run, and prints a `CHANGES.md` skeleton |

**Plugin memory layer** (added to avoid re-exploring the plugin every release):

```
.claude/plugin-memory/
├── CATALOG.md   - module-level table of contents (always loaded by the orchestrator)
├── CHANGES.md   - per-release delta log, newest first (read first to see what's already addressed)
└── README.md    - overview of the 3-layer design
```

Plus an FTS5 index of `app/**/*.php` (and a small Vue allowlist) maintained via `mcp__plugin_context-mode_context-mode__ctx_index` and queried via `ctx_search`. Use `ctx_search` for symbol lookups in plugin source instead of `grep` / `find`.

**Pull rhythm:** the **user** owns `git pull` on the plugin repo. After pulling, the user runs `./scripts/plugin/sync-memory.sh <prev-ref>` and pastes the changelog. Claude does **not** auto-pull and does **not** auto-reindex - keeps memory state unambiguous.

**Workflow** is defined in `.claude/skills/fluentcart-code-to-docs/SKILL.md`. Always pair the orchestrator with the master `fluentcart-doc-writer` and the matching template specialist (integration, payment-gateway, product, settings, overview).

**Hard rules:** never copy plugin source code into user-facing docs (docs describe behavior, not implementation), never fabricate behavior the code doesn't support, never commit. End every code-to-docs run with the standard summary block defined in the skill, then append a new entry to `.claude/plugin-memory/CHANGES.md` and bump `Last fully audited:` in `CATALOG.md` for every module the run touched.

---

## FluentCart Documentation - FluentCart Documentation
URL : https://docs.fluentcart.com/developer/

[Skip to content](https://docs.fluentcart.com/developer/#VPContent)

## Under Development [​](https://docs.fluentcart.com/developer/\#under-development)

Developer documentation is currently under development and will be available soon.

---

## Sitemap.Xml
URL : https://docs.fluentcart.com/sitemap.xml

https://docs.fluentcart.com/CLAUDEhttps://docs.fluentcart.com/developer/https://docs.fluentcart.com/guide/browsing-history/https://docs.fluentcart.com/guide/changeloghttps://docs.fluentcart.com/guide/customer-dashboard/downloadshttps://docs.fluentcart.com/guide/customer-dashboard/https://docs.fluentcart.com/guide/customer-dashboard/licenseshttps://docs.fluentcart.com/guide/customer-dashboard/profile-managementhttps://docs.fluentcart.com/guide/customer-dashboard/purchase-confirmation-invoice-receipthttps://docs.fluentcart.com/guide/customer-dashboard/purchase-historyhttps://docs.fluentcart.com/guide/customer-dashboard/subscriptionshttps://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-csshttps://docs.fluentcart.com/guide/customization-and-themes/code-snippetshttps://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-brickshttps://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgetshttps://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgetshttps://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcodehttps://docs.fluentcart.com/guide/customization-and-themes/layout-template-customizationhttps://docs.fluentcart.com/guide/customization-and-themes/theme-compatibilityhttps://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcarthttps://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgetshttps://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blockshttps://docs.fluentcart.com/guide/getting-started/dashboard-overviewhttps://docs.fluentcart.com/guide/getting-started/fluentcart-glossaryhttps://docs.fluentcart.com/guide/getting-started/initial-setup-wizardhttps://docs.fluentcart.com/guide/getting-started/installation-activationhttps://docs.fluentcart.com/guide/getting-started/introduction-fluentcarthttps://docs.fluentcart.com/guide/integrations/amazon-s3-integrationhttps://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integrationhttps://docs.fluentcart.com/guide/integrations/fluentaffiliate-integrationhttps://docs.fluentcart.com/guide/integrations/fluentbooking-integrationhttps://docs.fluentcart.com/guide/integrations/fluentcommunity-integrationhttps://docs.fluentcart.com/guide/integrations/fluentcrm-integrationhttps://docs.fluentcart.com/guide/integrations/fluentsupport-integrationhttps://docs.fluentcart.com/guide/integrations/integration-overviewhttps://docs.fluentcart.com/guide/integrations/learndash-integrationhttps://docs.fluentcart.com/guide/integrations/lifterlms-integrationhttps://docs.fluentcart.com/guide/integrations/webhook-integrationhttps://docs.fluentcart.com/guide/marketing-sales-tools/creating-managing-coupons/adding-coupons/https://docs.fluentcart.com/guide/marketing-sales-tools/creating-managing-coupons/https://docs.fluentcart.com/guide/marketing-sales-tools/https://docs.fluentcart.com/guide/migration/edd/backward-compatibilityhttps://docs.fluentcart.com/guide/migration/edd/developer-modehttps://docs.fluentcart.com/guide/migration/edd/edd-clihttps://docs.fluentcart.com/guide/migration/edd/edd-migrationhttps://docs.fluentcart.com/guide/migration/edd/https://docs.fluentcart.com/guide/migration/edd/troubleshootinghttps://docs.fluentcart.com/guide/migration/edd/what-is-migratedhttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/cash-on-delivery-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfighttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paypal-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settingshttps://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settingshttps://docs.fluentcart.com/guide/payments-checkout/https://docs.fluentcart.com/guide/product-types-creation/advanced-inventoryhttps://docs.fluentcart.com/guide/product-types-creation/bulk-product-importhttps://docs.fluentcart.com/guide/product-types-creation/configuring-product-pricinghttps://docs.fluentcart.com/guide/product-types-creation/creating-digital-products-with-licenseshttps://docs.fluentcart.com/guide/product-types-creation/creating-digital-productshttps://docs.fluentcart.com/guide/product-types-creation/creating-managing-product-brandhttps://docs.fluentcart.com/guide/product-types-creation/creating-managing-product-categories/https://docs.fluentcart.com/guide/product-types-creation/creating-physical-productshttps://docs.fluentcart.com/guide/product-types-creation/creating-product-bundleshttps://docs.fluentcart.com/guide/product-types-creation/defining-upgrade-pathshttps://docs.fluentcart.com/guide/product-types-creation/https://docs.fluentcart.com/guide/product-types-creation/inventory-managementhttps://docs.fluentcart.com/guide/product-types-creation/managing-product-integrationshttps://docs.fluentcart.com/guide/product-types-creation/managing-subscriptionshttps://docs.fluentcart.com/guide/product-types-creation/product-list-overviewhttps://docs.fluentcart.com/guide/reporting-analytics/cohortshttps://docs.fluentcart.com/guide/reporting-analytics/customer-reporthttps://docs.fluentcart.com/guide/reporting-analytics/future-renewalshttps://docs.fluentcart.com/guide/reporting-analytics/https://docs.fluentcart.com/guide/reporting-analytics/orders-reporthttps://docs.fluentcart.com/guide/reporting-analytics/product-reporthttps://docs.fluentcart.com/guide/reporting-analytics/refunds-reporthttps://docs.fluentcart.com/guide/reporting-analytics/reports-dashboard-overviewhttps://docs.fluentcart.com/guide/reporting-analytics/retentionhttps://docs.fluentcart.com/guide/reporting-analytics/revenue-reporthttps://docs.fluentcart.com/guide/reporting-analytics/sales-reporthttps://docs.fluentcart.com/guide/reporting-analytics/subscription-reporthttps://docs.fluentcart.com/guide/settings-configuration/cart-checkout-settingshttps://docs.fluentcart.com/guide/settings-configuration/checkout-fieldshttps://docs.fluentcart.com/guide/settings-configuration/email-configuration/configuring-email-notificationhttps://docs.fluentcart.com/guide/settings-configuration/email-configuration/https://docs.fluentcart.com/guide/settings-configuration/email-configuration/mailing-settingshttps://docs.fluentcart.com/guide/settings-configuration/email-configuration/pdf-invoicehttps://docs.fluentcart.com/guide/settings-configuration/email-configuration/remindershttps://docs.fluentcart.com/guide/settings-configuration/features-addonshttps://docs.fluentcart.com/guide/settings-configuration/global-integrationshttps://docs.fluentcart.com/guide/settings-configuration/https://docs.fluentcart.com/guide/settings-configuration/invoice-packing-settingshttps://docs.fluentcart.com/guide/settings-configuration/licensing-settingshttps://docs.fluentcart.com/guide/settings-configuration/managing-licensing-siteshttps://docs.fluentcart.com/guide/settings-configuration/pages-setuphttps://docs.fluentcart.com/guide/settings-configuration/payment-settingshttps://docs.fluentcart.com/guide/settings-configuration/product-pagehttps://docs.fluentcart.com/guide/settings-configuration/roles-permissions/adding-new-roles/https://docs.fluentcart.com/guide/settings-configuration/roles-permissions/https://docs.fluentcart.com/guide/settings-configuration/storage-settingshttps://docs.fluentcart.com/guide/settings-configuration/store-settingshttps://docs.fluentcart.com/guide/shipping/advanced-shipping-calculationshttps://docs.fluentcart.com/guide/shipping/configuring-shipping-zoneshttps://docs.fluentcart.com/guide/shipping/https://docs.fluentcart.com/guide/shipping/packageshttps://docs.fluentcart.com/guide/shipping/setting-up-shipping-methodshttps://docs.fluentcart.com/guide/shipping/understanding-shipping-classeshttps://docs.fluentcart.com/guide/storage/aws-s3https://docs.fluentcart.com/guide/storage/cloudflare-r2https://docs.fluentcart.com/guide/storage/https://docs.fluentcart.com/guide/store-management/customers-management/customer-details-overviewhttps://docs.fluentcart.com/guide/store-management/customers-management/https://docs.fluentcart.com/guide/store-management/customers-management/using-advanced-customer-filtershttps://docs.fluentcart.com/guide/store-management/customers-management/viewing-searching-customershttps://docs.fluentcart.com/guide/store-management/https://docs.fluentcart.com/guide/store-management/orders-management/changing-order-statuseshttps://docs.fluentcart.com/guide/store-management/orders-management/collecting-payments-modified-ordershttps://docs.fluentcart.com/guide/store-management/orders-management/creating-new-ordershttps://docs.fluentcart.com/guide/store-management/orders-management/editing-existing-ordershttps://docs.fluentcart.com/guide/store-management/orders-management/https://docs.fluentcart.com/guide/store-management/orders-management/instant-modal-checkouthttps://docs.fluentcart.com/guide/store-management/orders-management/order-bumphttps://docs.fluentcart.com/guide/store-management/orders-management/order-details-overviewhttps://docs.fluentcart.com/guide/store-management/orders-management/processing-refundshttps://docs.fluentcart.com/guide/store-management/orders-management/viewing-filtering-ordershttps://docs.fluentcart.com/guide/store-management/understanding-statuseshttps://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classeshttps://docs.fluentcart.com/guide/tax-&-duties/european-union-vathttps://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-countryhttps://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-countryhttps://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-osshttps://docs.fluentcart.com/guide/tax-&-duties/tax-&-duties-overviewhttps://docs.fluentcart.com/guide/tax-&-duties/tax-filinghttps://docs.fluentcart.com/guide/tax-&-duties/tax-rateshttps://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqshttps://docs.fluentcart.com/guide/troubleshooting-support/how-to-get-supporthttps://docs.fluentcart.com/guide/troubleshooting-support/https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logshttps://docs.fluentcart.com/

---

## Browsing History - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/browsing-history/

[Skip to content](https://docs.fluentcart.com/guide/browsing-history/#VPContent)

# Browsing History [​](https://docs.fluentcart.com/guide/browsing-history/\#browsing-history)

The **Browsing History** add-on quietly keeps a record of the pages every visitor views on your store before they place an order. That record is then attached to the order itself, so when you open an order in your dashboard, you can see the exact path the customer took to reach checkout.

It helps you answer a question that is usually hard to answer inside WordPress: _how did this sale actually happen?_

## Where to find the Browsing History [​](https://docs.fluentcart.com/guide/browsing-history/\#where-to-find-the-browsing-history)

Once the add-on is active, every new order records the browsing trail automatically. To view it:

1. From your WordPress dashboard, go to **FluentCart Pro > Orders**.
2. Open any order by clicking its order number.
3. On the right side of the order detail page, scroll down to the **Browsing History** panel.

![Order detail page showing the Browsing History panel on the right sidebar](https://docs.fluentcart.com/images/browsing-history/order-page-with-history.webp)

The panel appears alongside the other order information (Labels, UTM Details, Tax Information), so the full context of the purchase stays in one place.

## What the Browsing History shows [​](https://docs.fluentcart.com/guide/browsing-history/\#what-the-browsing-history-shows)

The Browsing History panel displays the pages the customer visited during the session that led to the order, in the order they visited them. Each entry includes the page address and the time it was viewed.

![Close-up view of the Browsing History panel listing visited pages with timestamps](https://docs.fluentcart.com/images/browsing-history/browsing-history-widget.webp)

The number in the panel heading (for example, _Browsing History (9)_) tells you how many pages the customer viewed in total before checking out.

## How to read the trail [​](https://docs.fluentcart.com/guide/browsing-history/\#how-to-read-the-trail)

Even a quick glance at the list can tell you a lot about the buying decision:

- **The first page** is where the customer's journey started on your store. If most of your converting customers land on the same blog post or landing page, that page is doing a lot of the selling.
- **The middle pages** show what the customer looked at while deciding. A jump between two product pages often means they were comparing. A visit to a shipping or policy page usually means they were checking trust signals before buying.
- **The last page before checkout** shows what finally tipped them into buying. If a specific page keeps showing up right before checkout across many orders, it is likely the page that closes the deal.
- **The time on each page** hints at how much attention the customer gave it. A long pause on a product page tells one story; a short scan of the FAQ tells another.

Over time, these patterns help you understand which pages bring buyers in, which pages build confidence, and which pages could do more.

## How long the history is kept [​](https://docs.fluentcart.com/guide/browsing-history/\#how-long-the-history-is-kept)

- **Orders that resulted in a purchase** keep their full browsing history attached to the order permanently. Even if old browsing data is cleaned up in the background, the snapshot tied to the order stays exactly as it was on the day of the sale.
- **Sessions that never led to a purchase** are tidied up automatically after a short retention window, so your store does not accumulate unused data.

In short: only the history that matters for real orders is kept long-term.

## Privacy at a glance [​](https://docs.fluentcart.com/guide/browsing-history/\#privacy-at-a-glance)

The Browsing History add-on is designed to respect visitor privacy:

- It does not use any third-party tracking services.
- It does not store IP addresses, device fingerprints, or names.
- Visitors are linked between pageviews only by a short, anonymous identifier, which clears itself after a purchase.

Only the pages visitors open on your own store are recorded, and only for the purpose of showing the path that led to their order.

## Getting started [​](https://docs.fluentcart.com/guide/browsing-history/\#getting-started)

1. Install and activate the **FluentCart Page History** add-on from your plugins area.
2. That is all that is needed - tracking begins automatically on the next visitor, and new orders will start showing their browsing history right away.

No configuration, no setup wizard. Open a recent order after activation, and you will begin seeing the path that led to every new sale.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Changelog - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/changelog

[Skip to content](https://docs.fluentcart.com/guide/changelog#VPContent)

# Changelog [​](https://docs.fluentcart.com/guide/changelog\#changelog)

Stay updated with the latest improvements, new features, bug fixes, and performance enhancements in FluentCart.

## FluentCart v1.3.28 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-28)

_Released on May 14, 2026_

✨ Newly Added⚡ Improvements🐞 Bug fixes

markdown

```
• Adds Elementor widgets: Search Bar, Store Logo, Dashboard Button, and Package Description
• Adds Draggable and reorderable summary sections in the Elementor Product Info widget
• Adds Elementor Popup support for Single Product variations, gallery, and quantity
• Adds Sort By toggle for the Bricks Products Collection element
```

markdown

```
• Improves Elementor widget grouping under the "FluentCart Product" category
• Improves 1-column checkout layout rendering in Elementor templates
• Improves LearnDash course management support
• Improves Mollie payment list currency handling
• Improves Coupon failure messages at checkout
• Improves Bricks element grouping under the "FluentCart" category
• Improves Admin menu spacing on mobile
• Improves Decimal trimming logic for tax rate formatting
```

markdown

```
• Fixes Elementor Single Product widgets syncing with active variations
• Fixes Buy button state updates for active variations
• Fixes Stock badge clearing for variations without stock data
• Fixes Stock label rendering as raw markup
• Fixes Empty Elementor product widgets leaving empty wrappers
• Fixes Product-template widget visibility outside Single Product documents
• Fixes Elementor Product Info rendering and Select2 change events
• Fixes Pricing Table shortcode and block rendering with `group_by` tabs
• Fixes Single Product shortcode rendering for variations, thumbnails, and quantity
• Fixes Product description rendering with third-party shortcodes and blocks
• Fixes FSE rendering for Customer Dashboard, Product Card, Product Search, and Pricing Table blocks
• Fixes Admin receipt access on records showing not-found pages
• Fixes Search Bar widget "Same Tab" behavior
• Fixes Enter key submitting the product title form
• Fixes Bricks Product Title rendering consistency
• Fixes French overseas territory VAT mapping issue
```

## FluentCart v1.3.27 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-27)

_Released on May 8, 2026_

✨ Newly Added🐞 Bug fixes🚀 Improvements

markdown

```
• Adds List/Grid view switcher and advanced product filtering for Bricks
• Adds Copy Variation ID action for simple product pricing panel
• Adds Licensing Sites, Site pages, and advanced site filtering
• Adds SubscriptionReactivated event
```

markdown

```
• Fixes Order bump free-shipping checkbox issue
• Fixes Missing shortcode variables in PDF receipt emails
• Fixes Long file names overflowing receipt page download buttons
• Fixes Cart allowing mixed or multiple subscriptions
• Fixes Offline subscriptions with 100% recurring coupons issue when Subscription Activated
• Fixes Subscription reactivation after refunds
• Fixes PayPal IPN subscription handling
• Fixes Redundant admin table search requests
• Fixes Amount formatting and customer profile display in Site Detail view (Pro)
• Fixes PHP warnings from deleted/invalid store pages
• Fixes Admin menu active state style bleeding
• Fixes Bricks Builder dynamic tag name mismatch
• Fixes Authorize.net subscription issue
```

markdown

```
• Improves Animation experience for table filters
• Improves Bricks Builder pagination rendering and performance
• Improves Product Pricing edit UX
```

## FluentCart v1.3.26 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-26)

_Released on May 5, 2026_

✨ Newly Added🐞 Bug fixes🚀 Improvements

markdown

```
• Adds Square Payment gateway
• Adds Private products support in discounts, coupons, and order bumps
• Adds Subscription setup fee to receipts and emails
```

markdown

```
• Fixes Order/invoice dates showing previous day in profiles
• Fixes Coupon expiration timezone mismatch
• Fixes Duplicate success toast on product update
• Fixes Email preview created_at DateTime issue
• Fixes Safari chevron icon visibility issue
• Fixes Menu button and dropdown styling issues
• Fixes LearnDash course expiry resolution for users
```

markdown

```
• Improves button feedback with visual indicators only
```

## FluentCart v1.3.23 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-23)

_Released on April 28, 2026_

✨ Newly Added🐞 Bug fixes🚀 Improvements

markdown

```
• Adds Subscription access end date in cancellation emails
• Adds Learndash: User specific course expiration respect to subscription/license
• Adds VAT numbers in PDF receipt address field
• Adds One click Licensed addon installer in addon page
```

markdown

```
• Fixes Parse download token with ported site urls issue
• Fixes fee_total missing column issue for version upgrades
• Fixes Missing checkout info label in gateway settings
• Fixes Advance filter merge relation issue
• Fixes Timezone resolution against deprecated PHP 8.4 aliases
• Fixes Licenses package download issue for portes site urls
• Fixes Empty state rendering in dark mode for reports and dashboard
• Fixes Supports for comma decimal separator in product variant cost
• Fixes Use singular form for subscription interval units
• Fixes Close editor modal when navigating from iframe links
• Fixes Verify stock module active before inventory menu
• Fixes License status incorrectly shown as "Expired" during grace period.
• Fixes PDF custom template deletion faild issue
• Fixes Customer address update/delete permission issue
• Fixes Regular security audits and ongoing enhancements
• Fixes Activity title's route not working
```

markdown

```
• Enhanced Paddle - allows all default emails, modifiable via filter hook
• Enhanced Adjust product-card and single-product styles
```

## FluentCart v1.3.21 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-21)

_Released on April 22, 2026_

✨ Newly Added🐞 Bug fixes

markdown

```
• Adds Cloudflare R2 storage
• Adds Public access management in S3
```

markdown

```
• Fixes PDF template block styling issue
• Fixes Warning for orderId null in checkout issue
• Fixes PayPal checkout security to ensure pricing integrity
• Fixes SKU duplicate issue in product variation creation
• Fixes Provider badge not displaying correctly on files
• Fixes S3 file deletion behavior
```

## FluentCart v1.3.20 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-20)

_Released on April 21, 2026_

✨ Newly Added🐞 Bug fixes

markdown

```
• Adds EDD migrator
```

markdown

```
• Fixes Products SKU index naming consistency issue
• Fixes Allow multiple variations without SKU issue
• Fixes Bundle product title with variation title visibility in checkout
• Fixes Block editor CSS loading inside the editor iframe issue
• Fixes Related Products block inspector layout and image overflow issues
• Fixes Invoice and Packing sub-menus issue
```

## FluentCart v1.3.19 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-19)

_Released on April 20, 2026_

✨ Newly Added🐞 Bug fixes

markdown

```
• Adds New UI for variation editing
• Adds Packaging support and weight attributes for products
• Adds Search support in product list via simple filters
• Adds fluent_cart/product_url_with_front filter for post types register
```

markdown

```
• Fixes Pricing format in price input fields
• Fixes Saved view conflicts with filters
```

## FluentCart v1.3.18 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-18)

_Released on April 15, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Filter hooks to manage specific emails
• Adds Permission checks for the "Save as Views" filter
```

markdown

```
• Improves PDF download functionality on the receipt page
• Improves Turnstile CAPTCHA handling
```

markdown

```
• Fixes Loading animation issue across all pages
• Fixes License expiration handling issue
• Fixes Mollie subscription issues
• Fixes Paddle email notification compliance issue
• Fixes Deprecated timezone alias handling in OrderParser
• Fixes Issue where empty SKU string instead of null
• Fixes Modal checkout visibility toggle issue
• Fixes Typos and other issues in payment gateway settings
• Fixes PDF template preview issue
```

## FluentCart v1.3.17 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-17)

_Released on April 07, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Fees API for custom fees in checkout
• Adds Add filterable frontend asset loading context for cart bundle
• Adds Shipping method new options Include,Exclude countries
• Adds Delete all test order action inside More option (All orders page)
• Adds Visual PDF Invoice Customizer
• Adds E-Invoice (ZUGFeRD / Factur-X) with EN 16931 profiling
```

markdown

```
• Enhanced Development Hooks / Filter experience
```

markdown

```
• Fixes Stock not updated after test order deletion
• Fixes Product duplicate not working in bulk edit page
• Fixes Downloadable file edit issue
• Fixes And Improves Turnstile
• Fixes Decimal value not allowed in shipping fee
• Fixes Handles Paddle recovery link
• Fixes Checkout Summary block consolidated into a single block
• Fixes Added restrictions to product child blocks
• Fixes Pagination showing stale page number after changing per_page
• Fixes Paddle discount issue
```

## FluentCart v1.3.15 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-15)

_Released on March 13, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Schedule reminder email for payment and subscriptions
• Adds Email preview for default template
• Adds Email editor Gutenberg
• Adds Email for Subscription cancel
• Adds Subscription activity logs in subscription page
```

markdown

```
• Enhanced EU VAT reverse experience in checkout
```

markdown

```
• Fixes CRM integration missing fields phone, postcode, state
• Fixes Custom checkout discount calculation issue
• Fixes Address validation issue
• Fixes Customer first_name and last_name change update WP user data
• Fixes Order payment calculation issue on amount updates
• Fixes Timezone issue for customer email
• Fixes Modal checkout issue with billing field
• Fixes Report product thumbnail issue
```

## FluentCart v1.3.14 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-14)

_Released on March 04, 2026_

✨ Newly Added🐞 Bug fixes

markdown

```
• Adds Flutterwave for FluentCart
• Adds Early Payment for installment
• Adds Bulk product import
• Adds Customizable product shortcodes
• Adds Sale badge Gutenberg block
• Adds Out of Stock badge Gutenberg block
• Adds Product description Gutenberg block
• Adds Product image CDN support
```

markdown

```
• Fixes Coupon per user limit issue
• Fixes Modal checkout cart not found issue
```

## FluentCart v1.3.13 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-13)

_Released on February 26, 2026_

✨ Newly Added🐞 Bug fixes

markdown

```
• Adds SKU Gutenberg block
```

markdown

```
• Fixes SKU sanitization issue
• Fixes Manual payment checkout instruction issue
• Fixes Payment method settings customization issue
• Fixes Zero decimal amount issue for Japanese currency
```

## FluentCart v1.3.12 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-12)

_Released on February 26, 2026_

🐞 Bug fixes

markdown

```
• Fixes caching issue during new version upgrades
```

## FluentCart v1.3.11 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-11)

_Released on February 25, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds GB Blocks: Related Products, Customer Dashboard Button, Store Logo
• Adds Media Carousel Block
• Adds Elementor Widgets: Checkout, Add to Cart, Buy Now Button, Mini Cart, Products, Product Carousel, Product Categories List
• Adds Razorpay Subscription Supports
• Adds Product SKU feature
• Adds Customer LTV recalculation action
• Adds Sync order statuses action
• Adds Test Data Cleanup Tool
• Adds First Name & Last Name Field Settings
```

markdown

```
• Improves Inventory Manager Free (Previously Pro)
• Improves New Settings UI
• Schedules security audit for all modules
```

markdown

```
• Fixes Gallery Image Overflow Issue
• Fixes Subscription validity expire events issue
• Fixes Minor issues
```

## FluentCart v1.3.10 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-10)

_Released on February 04, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds FSE Block Theme Support
• Adds Blocks & shortcodes: Mini cart, Product Carousel, title, image
• Adds Shortcode product categories
```

markdown

```
• Improves Guttenberg Blocks into latest version (v3)
```

markdown

```
• Fixes Missing tax breakdown on renewal email
• Fixes Missing VAT info on renewal order
• Fixes Dark-light theme conflict for addons promo
• Fixes Modal checkout responsive issue
```

## FluentCart v1.3.9 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-9)

_Released on January 28, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Mercado Pago gateway (one-time payments)
• Adds Ghost product checkout
• Adds Gutenberg block: Add to Cart
• Adds Shortcode [fluent_cart_checkout_button]
• Adds Shortcode [fluent_cart_add_to_cart_button]
```

markdown

```
• Improves security
```

markdown

```
• Fixes IPN issues for some third-party gateways
• Fixes Dashboard styling issues
```

## FluentCart v1.3.8 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-8)

_Released on January 23, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Instant checkout feature
• Adds Product Button block (Guttenberg)
• Adds Product duplicate feature
• Adds Copy variation ID option in variation context menu
```

markdown

```
• Improves JS file size optimization
```

markdown

```
• Fixes S3 driver directory seperator issue
```

## FluentCart v1.3.7 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-7)

_Released on January 20, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Support for frontend templates
• Adds Order UUID / hash filter
• Adds Stripe metadata hook
• Adds Hook for autocomplete digital orders (default enabled)
```

markdown

```
• Improves Translation support for receipt page
• Improves Frontend loader UI
• Improves Cart item count sync between backend and UI badge
• Improves Stripe subscription price update event handling
• Improves Validation error handling and messaging
• Improves Retention report components
• Improves Checkout, product, and loader styles
• Improves Checkout field defaults and labels
• Improves Text change: "Half year" → "Six month"
```

markdown

```
• Fixes Hide consent section for stripe subscription
• Fixes Security issue in license APIs
• Fixes Product variation IDs not updating in DownloadFile
• Fixes ShopApp block list view & pagination issue
• Fixes Cart icon in body setting not working
• Fixes GroupKey bug in reports
• Fixes License rendering issue on customer profile
• Fixes Checkout empty state issue
• Fixes Address validation message and input label mismatch
• Fixes Missing required symbol for "Full Name" in checkout
```

## FluentCart v1.3.6 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-6)

_Released on January 8, 2026_

🐞 Bug fixes

markdown

```
• Fixes FSE theme support
• Fixes Checkout Agree Terms and Conditions issue
• Fixes Product Min-Max pricing issue
• Fixes Buy now section position issue
• Fixes Shortcode issue in cart and checkout page
• Fixes Subscription related order issue
• Fixes Checkout page broken on Breakdance builder
```

## FluentCart v1.3.5 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-5)

_Released on January 6, 2026_

🐞 Bug fixes

markdown

```
• Hotfix: Cart Model caching issue fixed
```

## FluentCart v1.3.4 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-4)

_Released on January 6, 2026_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Bundle products
• Adds Stripe hosted checkout
• Adds Stripe appearance customizations support
• Adds Razorpay payment gateway addon (onetime)
• Adds 100% recurring discount
• Adds Order reference to Stripe metadata
• Adds New currency Ghanaian Cedi (GHS)
• Adds Turnstile invisible captcha
• Adds Email notification for offline payment
• Adds Items information in stripe metadata
• Adds WP user creation
• Adds Subscription retention & Cohort report
```

markdown

```
• Enhanced Development hooks to customize checkout button text
• Enhanced Translations for different modules
• Enhanced More development related hooks and modules
```

markdown

```
• Fixes Double confirmation email issue
• Fixes Order bump with subscription products
• Fixes NO_SHIPPING for paypal subscription issue
• Fixes Amount precision issue for paypal
• Fixes Update button issue for affiliate in coupon
• Fixes Checkout missing company name store issue
• Fixes Conflicts with Divi-5 Builder issue
• Fixes Customer last purchase invalid date issue
• Fix Downloads handling for object-based order
• Fixes S3 empty file validation issue
• Fixes downloadable file issue and empty file visibility
• Fixes Get paypal plan api endpoints issue
• Fixes Variation View Image & Text issue for Gutenberg
```

## FluentCart v1.3.2 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-2)

_Released on December 2, 2025_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Adds Private Product Status
• Adds Authorize.net payment gateway (Pro)
• Adds Recurring discount coupon
• Adds Checkout block
• Adds Product variation customization hooks
• Adds Thank You page payment instructions
```

markdown

```
• Updates Reports graph design
• Updates Gateway customization design
• Updates Addon gateway management for future updates
```

markdown

```
• Fixes handling of zero-decimal currency for Stripe
• Fixes hookable customer profile menu & icon issue
• Fixes coupon priority issue
• Fixes coupon calculation issues
• Fixes report card design issue
• Fixes group key SQL security issue
• Fixes EU VAT renderer issue on initial load
• Fixes variation title not showing for bump product
• Fixes wrong Stripe canceled_at date
```

## FluentCart v1.3.0 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-3-0)

_Released on November 19, 2025_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Introducing Paystack Payment Gateway
• Added Quarterly and Half-Yearly subscription billing intervals
• Coupons now supports email based restrictions
• Introducing REST API Doc: https://dev.fluentcart.com/restapi/
• Added new hooks and filters for developers
```

markdown

```
• Security: Performed a paid third-party security audit (Patchstack) as part of ongoing hardening efforts
• Improved Translation support for multiple languages
• Improved Reporting performance and data accuracy
• Refreshed the checkout page design and optimized payment method re-rendering
• Better Multi-Site Support
• Improvement on Invoicing & Taxes
```

markdown

```
• Bug fixes and Improvements
```

## FluentCart v1.2.6 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-2-6)

_Released on October 30, 2025_

🐞 Bug fixes

markdown

```
• Hotfix: Coupon usage database issue fixed
```

## FluentCart v1.2.5 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-2-5)

_Released on October 29, 2025_

✨ Newly Added🐞 Bug fixes

markdown

```
• More currency formatting options
• Multiple tax rates on checkout
• Compound tax rates calculation
• Accessibility improvements
• Payment gateway reorder for checkout page
• EU tax home country override
• Date time and number translation
• UTM reports
• Accessibility on checkout
• Gateway logo and label customization
• Order_by filter to ShopAppBlock
• SortBy Filter to ShopAppBlock
• Product Price Block support to ProductInfoBlock
• Order_paid_done hook
• More context to fluent_cart/checkout/prepare_other_data hook
• Customization Hooks in Thank You page
• Customization Hooks in checkout page
• Button style support for ShopApp Block
• Link toggle and target option to Product Title Block
• Missing translation strings
• Mollie payment gateway
```

markdown

```
• Missing currency sign for new currencies
• Currency formatting issue for old thousand separator
• Subscription details for pricing type simple
• Setup fee displaying when disabled
• Tax name for AU set as “ABN”
• Buy now button style issue
• Product Excerpt style not working
• Inventory validation issue on default variation first load
• Always showing ‘in-stock’ in ShopApp and Product Single
• Quantity 10k leads to broken empty state
• JS event not calling after removing the last item
• Billing and Shipping address webhook issue
• Payment validation error message not showing
• Selected product not saving in ProductGallery and BuySection blocks
• Broken product gallery block
• Report colors issue for comparison
• Report child page navigation
• Loader not showing in product Modal
• VAT not showing in receipt
```

## FluentCart v1.2.4 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-2-4)

_Released on October 22, 2025_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• CSS variables on cart drawer/shop page
• Product name on admin create order items
• New hooks for single product and shop page products
• New hook (fluent_cart/hide_unnecessary_decimals)
• Total on cart drawer
```

markdown

```
• Refactor class name on frontend page
```

markdown

```
• Product compare at price issue
• Variation rearrange update issue
• Console error and shipping method issue
• Validation message issue when deleting an order
• Static dollar sign appearing in price range
• Free Shipping issue that destroyed cart
• Undefined property issue on product page
• Exception property issue
• Remove force POST request validation for IPN
• Translation strings issue for all modules
• Payment method not showing issue on stripe
```

## FluentCart v1.2.2 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-2-2)

_Released on October 16, 2025_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Shipping zone for whole world
• New currency support for BYN, IRR, MMK
• Shipping status to order summary (Frontend Customer Portal)
• Block icons and block preview
• Currency code and currency sign on pricing of product card
• Price format setting for product card block editor
• Clearable on tax and shipping class widget
• Pro notice on upgrade path
```

markdown

```
• Product selection modal on product card
  block editor instead of variation selection modal
```

markdown

```
• Tax calculation issue based on store state settings
• Skip Inventory not working
• Issue with category parsing '&'
• Translation issue
• Item doesn't get deleted from the cart
• Css loading issue for blocks in template editor
• Report page navigation issue
• Single Product js issue
• Input rounded issue on store address which render under then country input
• Popover text breaking issue now it is word breaks
• Color issue on ProductInventory pro icon
```

## FluentCart v1.2.1 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-2-1)

_Released on October 5, 2025_

✨ Newly Added🚀 Improvements🐞 Bug fixes

markdown

```
• Custom Fields Plugins support for Products
• Terms & Conditions checkbox in the checkout page as settings
```

markdown

```
• Reporting
```

markdown

```
• Order Confirmation issue
• Custom Integration Renderer
```

## FluentCart v1.2.0 [​](https://docs.fluentcart.com/guide/changelog\#fluentcart-v1-2-0)

_Released on October 14, 2025_

🎉 Initial Release

markdown

```
• Hello World!
• The first release of FluentCart is here!
```

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
