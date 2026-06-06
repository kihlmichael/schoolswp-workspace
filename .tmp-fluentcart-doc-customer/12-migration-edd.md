# Section Migration

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Migrating from Easy Digital Downloads - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/#VPContent)

# Migrating from Easy Digital Downloads [​](https://docs.fluentcart.com/guide/migration/edd/\#migrating-from-easy-digital-downloads)

The FluentCart Migrator handles end-to-end migration from **Easy Digital Downloads 3.x** into FluentCart. Products, customers, orders across every meaningful status, recurring subscriptions, software licenses with all their site activations, coupons, and tax configuration transfer in a single coordinated pipeline.

The same engine is reachable two ways - pick the surface that fits your store size and comfort level:

- **Admin Wizard** - six-step Vue interface inside WordPress admin. Best for small to medium stores and non-technical operators.
- **WP-CLI** - single namespaced command with flags for each stage. Faster for large stores, no browser timeouts.

Your EDD store stays untouched

The Migrator only **reads** from EDD. Your existing store, its settings, and every record stay exactly as they are. Run both side-by-side until you're ready to switch.

## Documentation in this section [​](https://docs.fluentcart.com/guide/migration/edd/\#documentation-in-this-section)

| Page | When to read |
| --- | --- |
| [Wizard Walkthrough](https://docs.fluentcart.com/guide/migration/edd/edd-migration) | Start here. Full step-by-step run through the admin wizard, with screenshots. |
| [What Gets Migrated](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated) | Before you start. Complete inventory of what transfers - and what's deliberately out of scope (categories, upgrade paths, gateway credentials, custom meta). |
| [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli) | If your store has thousands of orders, or you prefer the terminal. Full flag reference and workflows. |
| [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode) | Before testing on staging. Explains the `FLUENT_CART_DEV_MODE` constant that gates destructive reset paths. |
| [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility) | After migration. Why the Migrator plugin must stay active - license API rerouting, PayPal IPN, Stripe webhook fallback, legacy URLs. |
| [Troubleshooting](https://docs.fluentcart.com/guide/migration/edd/troubleshooting) | When something fails or you want to verify. Failed payment log, license verification, common errors, reset workflow, FAQ. |

## Recommended workflow [​](https://docs.fluentcart.com/guide/migration/edd/\#recommended-workflow)

1. **Take a database backup.** Even though the Migrator never modifies your source data, a fresh backup is your safety net.
2. **Read [What Gets Migrated](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated).** Confirm the boundaries match your expectations.
3. **Rehearse on staging first.** Enable [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode) so you can reset and re-run as many times as needed.
4. **Verify the result.** Spot-check products, orders, subscriptions, and licenses against your source store.
5. **Repeat on production.** With staging validated, the production run is uneventful.
6. **Keep the Migrator plugin active.** It provides a [backward compatibility layer](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility) for legacy URLs, license API calls, and PayPal IPN renewals.

## Quick requirements check [​](https://docs.fluentcart.com/guide/migration/edd/\#quick-requirements-check)

- **Easy Digital Downloads 3.x** with the v3 table schema (EDD 2.x CPT-based stores are blocked at the compatibility check)
- **FluentCart** installed and activated
- **FluentCart Pro** required only for EDD Software Licensing migration
- **PHP** memory limit of 256MB recommended for larger stores
- **WP-CLI** for command-line workflows

For full details, head to the [Wizard Walkthrough](https://docs.fluentcart.com/guide/migration/edd/edd-migration).

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Backward Compatibility - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/backward-compatibility

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility#VPContent)

# Backward Compatibility [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#backward-compatibility)

When the migration finishes, the natural instinct is to deactivate the Migrator plugin and consider the job done. **Don't.**

The Migrator quietly provides a backward compatibility layer that keeps your existing customers working without disruption. Software licenses keep validating. PayPal subscriptions keep renewing. Old EDD URLs keep resolving. Stripe webhooks for legacy orders keep finding the right transaction.

If you deactivate the Migrator too early, customers feel it.

## Why this layer exists [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#why-this-layer-exists)

EDD and FluentCart use different URL structures, different API endpoints, and different identifier formats. After migration, your data is in FluentCart's format - but the outside world (your customers' installed software, PayPal's renewal notifications, Stripe's webhook history, bookmarked links in old emails) still speaks EDD.

The Migrator plugin sits between the two and translates. It accepts incoming requests in EDD's format, looks up the corresponding FluentCart record, and routes the work to the right place. Your customers see no difference.

This layer is what turns a migration from a hard cutover into a soft transition.

## What the layer handles [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#what-the-layer-handles)

The completion screen lists the four areas the Migrator continues to bridge:

![Completion screen showing the backward compatibility notice listing License API, PayPal IPN, Stripe webhooks, and download/renewal URLs](https://docs.fluentcart.com/assets/06-backward-compat.CIekn9YY.webp)

### License API endpoints [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#license-api-endpoints)

If you sold software with EDD Software Licensing, your customers' plugins, themes, or apps make periodic API calls to your site to:

- Activate a license on a new install
- Deactivate a license when uninstalling
- Check whether a license is still valid
- Check for software updates

These calls hit EDD's URL format, with EDD-style parameters. The Migrator intercepts each one, looks up the corresponding FluentCart license, performs the action through FluentCart, and returns a response in the format the customer's software expects.

Your customers don't update their software. They don't notice anything changed.

### PayPal IPN for legacy subscriptions [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#paypal-ipn-for-legacy-subscriptions)

Active PayPal Standard subscriptions created during the EDD era continue to send Instant Payment Notifications to EDD's old IPN endpoint when each renewal payment processes. Without the Migrator, those notifications fail silently - the subscription appears to keep renewing on PayPal's side, but FluentCart never records the renewal.

The Migrator catches the IPN, identifies the subscription, creates the renewal order in FluentCart, and updates the subscription's bill count. PayPal continues to charge the customer; FluentCart continues to know about it.

### Stripe webhook charge ID resolution [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#stripe-webhook-charge-id-resolution)

Stripe historically used charge IDs (`ch_xxx`) to identify transactions. Modern Stripe webhooks reference payment intent IDs (`pi_xxx`). For orders migrated from EDD, the original transaction record stores the charge ID - which means a webhook arriving with only a payment intent ID can't find its order.

The Migrator hooks into FluentCart's transaction lookup with a fallback that resolves charge IDs to payment intent IDs (and vice versa) for legacy records. Webhooks for migrated orders continue to apply correctly.

### Legacy EDD download and renewal URLs [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#legacy-edd-download-and-renewal-urls)

Old emails, bookmarks, account pages, and external links may contain EDD-format URLs:

- `/?edd_action=process_download&...`
- `/?edd_action=...&order_id=...` for renewal links
- Customer dashboard links pointing to EDD's account pages

The Migrator detects these and redirects them to the equivalent FluentCart URL, so a customer clicking an old link from a year-old email lands on the right page rather than a 404.

## When you can deactivate the Migrator [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#when-you-can-deactivate-the-migrator)

There is no fixed timeline. The right answer is "when the legacy traffic dies down to zero." For most stores that means at least one full subscription billing cycle - usually a year - after migration. For stores with long-tail license activations, longer.

A reasonable test: check your access logs for hits to EDD-format URLs over the past 30 days. If there are none, you can probably deactivate the Migrator. If there are still requests coming in, leave it active.

You can deactivate Easy Digital Downloads itself well before deactivating the Migrator. The Migrator does not depend on EDD being active to perform its compatibility work - it only needs the migrated data inside FluentCart.

Order of deactivation

A safe sequence:

1. Migration complete and verified
2. Run `wp fluent_cart_migrator migrate_from_edd --verify_license` to confirm license integrity
3. Reconnect payment gateways in FluentCart
4. Deactivate Easy Digital Downloads
5. Leave the Migrator and the EDD database tables in place for the transition period
6. After the transition (typically 6-12 months), evaluate whether legacy traffic has stopped
7. Only then consider deactivating the Migrator and running `edd_cleanup`

## What stops working if you deactivate too early [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#what-stops-working-if-you-deactivate-too-early)

| If you deactivate | What breaks |
| --- | --- |
| Easy Digital Downloads (with Migrator still active) | Nothing customer-facing. The Migrator handles the compatibility work independently. |
| FluentCart Migrator (with EDD-era license customers) | License activation and update checks for software sold during the EDD era stop working. Customers see "license invalid" errors. |
| FluentCart Migrator (with active PayPal Standard subscriptions) | Renewal payments still happen at PayPal but are never recorded in FluentCart. Subscriptions appear to lapse despite still being charged. |
| FluentCart Migrator (with legacy bookmarked links) | Old EDD-format URLs return 404. |

None of these break immediately or visibly to you - they fail silently for customers, which is the worst kind of breakage. Leave the Migrator active until you have actively confirmed there is no remaining legacy traffic.

## Performance impact [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#performance-impact)

The compatibility layer is lightweight. It hooks into request routing only when an incoming URL or webhook matches an EDD-format pattern, so normal FluentCart traffic is unaffected. Idle, the Migrator costs nothing.

## Related [​](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility\#related)

- [Troubleshooting](https://docs.fluentcart.com/guide/migration/edd/troubleshooting) - what to do if a customer reports a broken license or missing renewal
- [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli) - `--verify_license` and `edd_cleanup` commands

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Developer Mode - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/developer-mode

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/developer-mode#VPContent)

# Developer Mode [​](https://docs.fluentcart.com/guide/migration/edd/developer-mode\#developer-mode)

The Migrator includes a set of tools - primarily reset and re-run paths - that are too destructive to leave exposed on production. **Developer Mode** is the single switch that unlocks them.

It exists for one reason: rehearsing migrations safely. On staging, you want to import, inspect, reset, tweak the source, and import again, sometimes a dozen times before the production cutover. On production, you want every reset path firmly locked.

## Activating Developer Mode [​](https://docs.fluentcart.com/guide/migration/edd/developer-mode\#activating-developer-mode)

Add the following line to your `wp-config.php` file, above the `/* That's all, stop editing! */` comment:

php

```
define('FLUENT_CART_DEV_MODE', true);
```

Save the file. The change takes effect immediately. No plugin deactivation or cache flush is required.

To turn Developer Mode off, remove the line or set it to `false`.

Never enable Developer Mode on production

Developer Mode exposes destructive operations. Only enable it on staging, local, or otherwise isolated environments. On a live store it risks accidental data loss.

## Why a constant, not a setting [​](https://docs.fluentcart.com/guide/migration/edd/developer-mode\#why-a-constant-not-a-setting)

Defining a constant in `wp-config.php` is auditable, slow to flip by accident, and impossible to toggle from the WordPress admin. A misclicked button in the dashboard could wipe a production store; editing `wp-config.php` requires SSH or filesystem access plus an explicit code change.

This is the same reason WordPress core gates `WP_DEBUG`, `DISABLE_WP_CRON`, and other risk-bearing flags behind constants rather than settings pages.

## What Developer Mode unlocks [​](https://docs.fluentcart.com/guide/migration/edd/developer-mode\#what-developer-mode-unlocks)

With `FLUENT_CART_DEV_MODE` set to `true`, the following capabilities become available:

| Path | How to access |
| --- | --- |
| `--reset` flag on the main migration command | `wp fluent_cart_migrator migrate_from_edd --reset` |
| Standalone reset command | `wp fluent_cart_migrator reset` |
| Schema-refresh reset | `wp fluent_cart_migrator migrate_fresh` |
| Reset button in the admin wizard | Visible at the completion screen |

Without Developer Mode, every one of those paths returns blocked. The admin wizard checks the same flag and hides the reset button entirely. This is the behavior you want on production.

For the actual reset workflow - what reset destroys, when to use `reset` vs `migrate_fresh`, the staging rehearsal recipe, and confirmation prompts - see [Troubleshooting → Resetting a migration](https://docs.fluentcart.com/guide/migration/edd/troubleshooting#resetting-a-migration).

## Related [​](https://docs.fluentcart.com/guide/migration/edd/developer-mode\#related)

- [Troubleshooting](https://docs.fluentcart.com/guide/migration/edd/troubleshooting) - full reset workflow, failed payment logs, common errors
- [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli) - full command surface

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## WP-CLI Reference - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/edd-cli

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/edd-cli#VPContent)

# WP-CLI Reference [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#wp-cli-reference)

For stores with thousands of orders, the WP-CLI is faster than the admin wizard and avoids browser timeouts entirely. The same engine drives both interfaces, so the result is identical - only the surface differs.

## When to use WP-CLI [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#when-to-use-wp-cli)

Use the CLI when:

- Your store has more than a few thousand orders.
- You are running on shared hosting with strict PHP timeouts.
- You want to script a migration as part of a deployment workflow.
- The browser keeps disconnecting mid-run on a large dataset.
- You are migrating on staging via SSH and don't have admin UI access.

The wizard remains the right choice for small-to-medium stores or for non-technical operators.

## Commands at a glance [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#commands-at-a-glance)

The wizard surfaces the most common commands inside the **WP-CLI (Recommended for Large Stores)** panel:

![Migration steps with the WP-CLI command panel below](https://docs.fluentcart.com/assets/04-steps-cli.CS_cTgfq.webp)

## The primary command [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#the-primary-command)

All migration work happens through one namespaced command, with flags for each stage:

bash

```
wp fluent_cart_migrator migrate_from_edd [flag]
```

### Flag reference [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#flag-reference)

| Flag | What it does |
| --- | --- |
| `--all` | Run the complete migration pipeline: products → tax rates → coupons → payments → recount, in order. Resumes any skipped or interrupted steps. |
| `--products` | Migrate EDD downloads to FluentCart products. Creates new ones, updates existing ones via the migration ID map. |
| `--tax_rates` | Migrate EDD tax settings and generate FluentCart tax rates. Skipped automatically if taxes are disabled in EDD. |
| `--coupons` | Migrate EDD discount codes to FluentCart coupons. Updates by code if a match exists, otherwise inserts. |
| `--payments` | Migrate EDD orders, transactions, subscriptions, and licenses. Processed in batches of 1,000 orders per page, with last page persisted for resume. |
| `--recount` | Recalculate stats after migration: lifetime value, average order value, customer purchase counts, subscription bill counts, missing UUIDs. |
| `--stats` | Show pre-migration statistics for the source store. No data is migrated. |
| `--verify_license` | Compare EDD and FluentCart licenses after migration. Reports missing licenses and status mismatches. |
| `--log` | Display the failed payment log (`_fluent_edd_failed_payment_logs`). |
| `--reset` | Wipe migrated data and clear migration state. **Requires Developer Mode.** See [Developer Mode & Reset](https://docs.fluentcart.com/guide/migration/edd/developer-mode). |

## Common workflows [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#common-workflows)

### Full migration in one command [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#full-migration-in-one-command)

bash

```
wp fluent_cart_migrator migrate_from_edd --all
```

Runs every stage in order. If any stage was previously completed, it is skipped automatically. If the previous run was interrupted mid-payments, it resumes from the last processed page.

### Step by step [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#step-by-step)

For more control, run each stage individually. Useful when you want to inspect the result between stages or when one stage needs special handling.

bash

```
wp fluent_cart_migrator migrate_from_edd --products
wp fluent_cart_migrator migrate_from_edd --tax_rates
wp fluent_cart_migrator migrate_from_edd --coupons
wp fluent_cart_migrator migrate_from_edd --payments
wp fluent_cart_migrator migrate_from_edd --recount
```

The order matters. Products must exist before payments can reference them. Recount should be the final stage.

### Preview source data [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#preview-source-data)

Before migrating anything, see what is in the source store:

bash

```
wp fluent_cart_migrator migrate_from_edd --stats
```

Shows the count of products, orders, transactions, customers, subscriptions, licenses, the gateways found, and the order statuses present. No data is touched.

### Inspect failures after a run [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#inspect-failures-after-a-run)

If individual orders failed during the migration (corrupted records, missing customer references, malformed line items), they are captured rather than halting the whole run. View them with:

bash

```
wp fluent_cart_migrator migrate_from_edd --log
```

Each entry shows the EDD order ID, the error message, the error type, and the stage at which it failed. Use this to drive a follow-up investigation.

### Verify license integrity [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#verify-license-integrity)

After a migration that includes EDD Software Licensing, run:

bash

```
wp fluent_cart_migrator migrate_from_edd --verify_license
```

This compares the EDD license records against the FluentCart license records and reports any that are missing or have status mismatches. Run this before deactivating EDD.

## Companion commands [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#companion-commands)

Beyond the main `migrate_from_edd` command, the Migrator provides utilities for cleanup and developer workflows:

### Clean up EDD data after migration [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#clean-up-edd-data-after-migration)

Once you have validated the migration and are ready to remove EDD's artifacts from the database:

bash

```
wp fluent_cart_migrator edd_cleanup
```

Deletes EDD post types (`edd_advanced_report`, `edd_discount`, `edd_license_log`, `edd_log`, `edd_payment`), orphaned post and comment metadata, and the `download_category` and `edd_log_type` taxonomies. Asks for confirmation before running.

Run cleanup only after full verification

Don't run `edd_cleanup` until you have verified the migration thoroughly and your customers, subscriptions, and licenses are operating correctly through FluentCart. The original EDD records are your fallback if something needs reconciliation.

### Reset progress and refresh schema (developer) [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#reset-progress-and-refresh-schema-developer)

bash

```
wp fluent_cart_migrator migrate_fresh
```

Clears all migration progress options, refreshes the FluentCart database schema, deletes migrated FluentCart products, and removes migration metadata from EDD posts. Useful for testing on a staging environment when you want to rerun the full migration from scratch.

This command requires [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode).

### Reset migrated data (developer) [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#reset-migrated-data-developer)

bash

```
wp fluent_cart_migrator reset
```

Wipes migrated data and clears migration state. Slightly less aggressive than `migrate_fresh` - it does not refresh the schema. Asks for confirmation before running.

This command requires [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode).

### Backfill missing subscription UUIDs [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#backfill-missing-subscription-uuids)

bash

```
wp fluent_cart_migrator fix_subs_uuid
```

Standalone utility that fills in missing UUIDs on subscription records. Subscriptions migrated from older EDD installations occasionally lack UUIDs; this backfills them with `md5(id + uuid4 + microtime)` so other parts of FluentCart can reference them reliably.

## Resume behavior [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#resume-behavior)

The CLI is fully resumable. State is persisted in the `__fluent_cart_edd3_migration_steps` option after every completed step.

- **Stage-level resume:** Re-running `--all` skips any stages already marked complete.
- **Page-level resume for payments:** The payment migration stores `last_order_page`. A re-run continues from the next batch.
- **Idempotent re-runs of individual stages:**`--products` updates existing migrated products via the ID map. `--coupons` updates existing coupons by code. `--recount` always recalculates from current data, never increments.

This means you can safely interrupt a long run with `Ctrl+C` and start it again. No duplicate data, no skipped records.

## Memory and timing tips [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#memory-and-timing-tips)

For very large stores, give PHP enough headroom:

bash

```
php -d memory_limit=1024M $(which wp) fluent_cart_migrator migrate_from_edd --all
```

If the host has aggressive process limits, run individual stages rather than `--all`, so each invocation has its own memory context.

## What the CLI doesn't do that the wizard does [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#what-the-cli-doesn-t-do-that-the-wizard-does)

- The CLI does not show a live, polling progress bar in the wizard's visual style. It uses WP-CLI's built-in progress bar for the payments stage.
- The CLI does not pause and resume mid-stage on demand - only between stages.
- The CLI does not surface the post-migration backward compatibility notice. Read [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility) directly to know what to keep enabled.

For everything else, the CLI is functionally equivalent to the wizard - and faster on real workloads.

## Related [​](https://docs.fluentcart.com/guide/migration/edd/edd-cli\#related)

- [Migrating from EDD](https://docs.fluentcart.com/guide/migration/edd/edd-migration) - wizard walkthrough
- [Developer Mode & Reset](https://docs.fluentcart.com/guide/migration/edd/developer-mode) - reset workflow for staging
- [Troubleshooting](https://docs.fluentcart.com/guide/migration/edd/troubleshooting) - what to do when something fails

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Migrating from EDD - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/edd-migration

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/edd-migration#VPContent)

# Migrating to FluentCart from Easy Digital Downloads [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#migrating-to-fluentcart-from-easy-digital-downloads)

Moving an entire online store to a new platform might sound like a massive, stressful project - but with FluentCart it doesn't have to be.

The **FluentCart Migrator** addon acts as your personal moving team. It automatically and securely transfers all of your hard-earned data - products, orders, customers, subscriptions, coupons, licenses - from **Easy Digital Downloads (EDD)** directly into your new FluentCart store. No spreadsheets, no manual data entry, no coding.

Your EDD store stays safe

This tool only **copies** your data into FluentCart. Your original Easy Digital Downloads store, all its settings, and every record stay completely untouched throughout this entire process. You can run both side-by-side until you're fully ready to switch.

This page walks through the wizard step by step. For an alternative terminal-based workflow on large stores, see the [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli). For a complete inventory of what does and doesn't transfer, see [What Gets Migrated](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated).

* * *

## Before You Begin [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#before-you-begin)

Take two minutes to confirm these are in place before you start. Catching a missing piece now saves a mid-migration surprise.

- **Easy Digital Downloads 3.x** must be installed and active on your site - the Migrator reads directly from its v3 data tables.
- **FluentCart** must be installed and activated - [Get FluentCart](https://fluentcart.com/).
- **FluentCart Pro** is required only if you use **EDD Software Licensing** (license keys, site activations, software updates). If you don't sell licensed software, the free version is enough.
- **A database backup** - always take a fresh backup before any migration. It's your safety net, even though the Migrator never modifies your EDD data.
- **WordPress admin access** on the site you're migrating.

Back up first

Even though the Migrator only reads from EDD and never touches your existing data, take a fresh database backup before you begin. It takes five minutes and gives you complete peace of mind.

For a deeper rehearsal before touching production, run the migration on staging first with [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode) enabled. That lets you reset and re-run as many times as needed.

* * *

## Step 1: Install and Activate the Migrator [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-1-install-and-activate-the-migrator)

Now that you're ready, install the migration tool. Think of it as a secure, temporary bridge between your existing EDD setup and your new FluentCart store.

1. Go to the [**FluentCart website**](https://fluentcart.com/fluentcart-addons/) and download the **FluentCart Migrator** addon `.zip` file.
2. Open your **WordPress admin dashboard** and go to **Plugins → Add New**.
3. Click the **Upload Plugin** button at the top.
4. Click **Choose File**, select the `.zip` file you just downloaded, then click **Install Now**.
5. Once installation finishes, click **Activate Plugin**.

## Step 2: Open the Migration Dashboard [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-2-open-the-migration-dashboard)

Now that the bridge is built, open the tool.

1. Navigate to your **FluentCart** dashboard in the WordPress sidebar.
2. Click the newly added **Migrator** option.

This launches the **Migration Wizard** - a clean, step-by-step interface that walks you through the entire transfer.

![FluentCart Migrator landing screen with the source platform picker](https://docs.fluentcart.com/assets/01-source-select.DAxuYu_p.webp)

## Step 3: Select Your Source [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-3-select-your-source)

The wizard auto-detects which eCommerce plugins are installed. If you're running Easy Digital Downloads, the **Easy Digital Downloads** card displays a green **DETECTED** badge.

Click the card to confirm: _yes, this is where my data lives._

WooCommerce and SureCart are visible as upcoming sources but are not yet active. Migrators for those platforms are on the roadmap.

## Step 4: Compatibility Check [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-4-compatibility-check)

Before moving any data, the wizard runs a quick compatibility check.

This step verifies that your installation of Easy Digital Downloads is fully compatible with the migration tool. Specifically, it checks for EDD 3.x with the v3 table schema. EDD 2.x stores using the legacy CPT data model are blocked here with a clear message - update to EDD 3.x first, then return to the wizard.

Once you see the **green confirmation box**, click **Continue**.

![Compatibility check screen showing EDD 3.x detected with version number](https://docs.fluentcart.com/assets/02-compatibility.D5t3rahG.webp)

## Step 5: Pre-Migration Overview [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-5-pre-migration-overview)

This is one of the most reassuring parts of the process. Before the actual transfer begins, the wizard takes a quick inventory of your existing EDD store and shows you exactly what it found.

You'll see clear summary cards displaying the total count of:

- **Products** - your digital downloads and other items
- **Orders** - your complete past purchase history
- **Customers** - all buyer accounts
- **Subscriptions** - active and historical recurring plans
- **Licenses** - issued software keys (if EDD Software Licensing is in use)
- **Transactions** - individual payment records

The wizard also surfaces detected payment gateways and the order statuses present in your data, so you can confirm there are no surprises.

Compare these numbers against what you know is in your EDD store. If they look right, proceed.

![Pre-migration overview showing entity counts, gateways, and order statuses](https://docs.fluentcart.com/assets/03-pre-overview.D5oAYckQ.webp)

## Step 6: Configure and Start the Migration [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-6-configure-and-start-the-migration)

You're at the final setup screen. This step lets you fine-tune how the migration runs before kicking it off.

**Batch Size** Think of this as how many "boxes" the mover carries in one trip. It controls how many records the server processes per request. The default of **100** works for most stores. If your server is underpowered and a stage stalls, lower it to `50` or `25` to reduce load per cycle. Available values: 50, 100, 250, 500, 1000.

**Steps to Run** A checklist of stages to include:

- **Products**
- **Tax Rates**
- **Coupons**
- **Orders, Payments, Customers, Subscriptions, Licenses**
- **Recount & Verify**

Leave **all of them checked**. Unchecking any item means that data won't come over. The wizard automatically skips stages already completed, so re-running the migration is safe.

When ready, click **Start Migration**.

Keep this tab open

Don't close or refresh this browser tab while the migration is running. The progress bar needs an active connection to process your data. Grab a coffee and let FluentCart do the heavy lifting.

If the migration is interrupted

No need to panic. The Migrator tracks its progress as it goes. If your browser closes, your session times out, or anything else interrupts the process, return to the Migrator screen and start it again. It will automatically skip everything that already completed and resume the payments stage from the exact batch where it stopped.

![Migration steps with WP-CLI command panel below](https://docs.fluentcart.com/assets/04-steps-cli.CS_cTgfq.webp)

On the same screen: WP-CLI commands

The configuration screen also surfaces the WP-CLI commands for each stage. For stores with thousands of orders, switching to the CLI is significantly faster and avoids browser timeouts entirely. See the [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli) for the full command surface.

## Step 7: Migration Complete - Verify Before Going Live [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#step-7-migration-complete-%E2%80%94-verify-before-going-live)

Once the progress bar reaches **100%**, you'll see a green checkmark and a **Migration Completed** screen with a final breakdown of how many items were copied across each category.

![Migration completion screen with stats, backward compatibility notice, and next steps](https://docs.fluentcart.com/assets/06-backward-compat.CIekn9YY.webp)

The completion screen also includes an important notice - **keep the Migrator plugin active** even after the migration finishes. It provides a backward compatibility layer for existing customers. See [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility) for the full explanation.

Your data is in. Before opening your new store to the public, spend a few minutes verifying the result.

**Verify Your Products** Go to **FluentCart → Products**. Confirm the product count looks right, then open a handful of items and check titles, descriptions, pricing (single or variations), subscription billing intervals, and bundle child items.

**Review Orders** Go to **FluentCart → Orders** and open several recent ones. For each, confirm order totals, line items, payment status, customer name and email, billing address, payment gateway, and transaction ID.

**Check Subscriptions** Go to **FluentCart → Subscriptions** and spot-check a few. Verify billing interval, renewal date, start date, and status.

**Check Licenses** _(if applicable)_ Go to **FluentCart → Licenses** and confirm license keys transferred with their correct statuses, activation limits, active site URLs, and expiration dates. For a programmatic check across all licenses, run:

bash

```
wp fluent_cart_migrator migrate_from_edd --verify_license
```

**Verify Coupons** Go to **FluentCart → Coupons** and confirm discount codes are present with correct amounts, usage limits, and expiration dates.

**Spot-Check Customers** Go to **FluentCart → Customers**, open a few profiles, and confirm names, emails, and order history. Customer lifetime value and purchase counts are recalculated automatically during the recount stage, so those numbers will be accurate.

Pick representative orders to check thoroughly

For the best peace of mind, find one example of each scenario in your store and compare it field-by-field between EDD and FluentCart: a simple one-time purchase, a subscription order with renewals, an order with a coupon applied, a refunded order, and a license-based purchase.

For a complete map of what transfers and what doesn't (categories, upgrade paths, payment gateway credentials, custom meta), see [What Gets Migrated](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated).

## A Few Things Still Need Your Attention [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#a-few-things-still-need-your-attention)

The Migrator handles your data automatically, but a small number of items need quick manual setup before you're fully live.

**1\. Reconnect Your Payment Gateways** Transaction records transfer, but gateway API credentials never do - for security reasons. Reconnect them fresh in FluentCart. Go to **FluentCart → Settings → Payment Gateways** and add your Stripe API keys and PayPal credentials.

> 💡 **Important:** Use the exact same Stripe and PayPal accounts you used with EDD. This ensures active subscriptions continue renewing correctly and all future webhooks route to the right place.

INFO

For step-by-step instructions on connecting each payment gateway, see the [Payments & Checkout](https://docs.fluentcart.com/guide/payments-checkout/) section.

**2\. Attach Your Download Files to Products** The migration creates all your product records, but the actual downloadable files need to be confirmed and attached inside each product. Go to **FluentCart → Products**, open each digital product, and verify the correct file is linked under **Downloadable Asset(s)**.

**3\. Review Your Email Notifications** FluentCart has its own email system with beautifully designed templates. Review and customize your purchase receipt, subscription renewal, license expiration, and refund notification templates under **FluentCart → Settings → Email Configuration** before customers start receiving them.

**4\. Update Your Store's Purchase Buttons and Links** If you're using EDD shortcodes or custom purchase buttons anywhere on your site, replace them with FluentCart's purchase buttons or checkout blocks. Also update menu links pointing to EDD account or purchase history pages.

**5\. Review Your Tax Settings** Your EDD tax rates transfer over automatically, but verify the tax calculation mode in **FluentCart → Settings** matches how you were running taxes in EDD.

## Keep the Migrator Plugin Active [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#keep-the-migrator-plugin-active)

After your migration is complete, **don't deactivate the FluentCart Migrator plugin** during your transition period. It provides a silent backward compatibility layer that keeps existing customers working seamlessly:

- **EDD Software Licensing API calls** continue to be intercepted and routed through FluentCart, so customers' installed software keeps validating without any change on their end.
- **PayPal Standard renewal notifications** are caught and processed correctly.
- **Stripe webhooks** for legacy orders are matched against the original charge IDs.
- **Legacy EDD URLs** (download links, renewal pages, account URLs in old emails) are redirected to the right FluentCart pages.

For the full explanation of why this layer exists and when it's safe to deactivate, see [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility).

Don't delete your EDD data yet

Even after everything is verified and running, don't delete your EDD database tables in a rush. The Migrator never modifies them - they're just sitting there, taking up very little space, and they're your fallback if you ever need to reference original records. Leave them until you're fully confident, then run `wp fluent_cart_migrator edd_cleanup` when you're ready.

## Need help? [​](https://docs.fluentcart.com/guide/migration/edd/edd-migration\#need-help)

- Stuck on a specific stage? Check the [Troubleshooting](https://docs.fluentcart.com/guide/migration/edd/troubleshooting) page.
- Want to know exactly what transfers? See [What Gets Migrated](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated).
- Running on a large store? Switch to the [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli).
- Testing on staging and want to reset between runs? Enable [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode).
- Customer reports a broken license post-migration? See [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility).

---

## Troubleshooting - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/troubleshooting

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/troubleshooting#VPContent)

# Troubleshooting [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#troubleshooting)

The Migrator is built to be tolerant of bad data: individual record failures are captured rather than halting the run. This page explains how to find those failures, how to verify integrity after a migration, and how to recover from common problems.

## The failed payment log [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#the-failed-payment-log)

When an order fails to migrate - corrupted record, missing customer reference, malformed line items, gateway data inconsistency - the failure is captured in the `_fluent_edd_failed_payment_logs` WordPress option rather than aborting the run.

### Viewing failures from the CLI [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#viewing-failures-from-the-cli)

bash

```
wp fluent_cart_migrator migrate_from_edd --log
```

Each entry shows:

| Field | Meaning |
| --- | --- |
| `edd_id` | The EDD order ID that failed |
| `message` | Human-readable error message |
| `error_type` | A short code identifying the error category |
| `stage` | Where in the pipeline the failure occurred (`data_setup`, `validation`, `migration`) |

### Viewing failures from the wizard [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#viewing-failures-from-the-wizard)

The migration completion screen surfaces an expandable error log section. Click to expand and see the same data as the CLI `--log` output.

### What to do with a failed entry [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#what-to-do-with-a-failed-entry)

1. Open the original EDD order in your WordPress admin (`Edit > Orders` in EDD's UI).
2. Compare it against the error message - usually the cause is obvious (missing customer email, deleted product reference, broken meta).
3. Fix the source data in EDD.
4. Re-run the payments stage: `wp fluent_cart_migrator migrate_from_edd --payments`. The Migrator will pick up only the orders not yet successfully migrated.

## Verifying license integrity [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#verifying-license-integrity)

If your store uses EDD Software Licensing, run the verification command after the migration completes:

bash

```
wp fluent_cart_migrator migrate_from_edd --verify_license
```

This compares EDD's license records against FluentCart's license records and reports:

- Licenses present in EDD but missing in FluentCart
- Licenses with status mismatches (active in EDD but inactive in FluentCart, or vice versa)

For each discrepancy, investigate whether the source license has anomalies (a license without a parent order, an activation pointing at a deleted site) or whether the migration genuinely missed it. If genuinely missed, re-running the payments stage usually resolves it because licenses are migrated as part of order processing.

## Common issues [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#common-issues)

### "EDD 3.0 or later required" message [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#edd-3-0-or-later-required-message)

The compatibility check blocks the migration if it detects EDD 2.x with the legacy CPT data model. The Migrator only supports the EDD 3.x v3 table schema.

**Fix:** Update Easy Digital Downloads to 3.x. EDD 3.0 includes a built-in migration tool that converts legacy CPT data into the v3 tables. Run that first, then return to the FluentCart Migrator.

### Migration stalls partway through [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#migration-stalls-partway-through)

A stalled migration is almost always a server-side timeout: PHP `max_execution_time` cut off the request, or the host's process supervisor killed a long-running script.

**Fix from the wizard:** Just refresh the page. The wizard will pick up from the last completed batch. If it stalls again, lower the **Batch Size** dropdown (try 50 or 25) so each batch finishes well within the host's timeout.

**Fix from the CLI:** The CLI bypasses HTTP timeouts entirely. If the wizard keeps stalling, switch to the CLI:

bash

```
wp fluent_cart_migrator migrate_from_edd --all
```

### Out of memory errors [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#out-of-memory-errors)

For large stores, PHP may run out of memory during the payments stage.

**Fix:** Give PHP more headroom temporarily for the migration run:

bash

```
php -d memory_limit=1024M $(which wp) fluent_cart_migrator migrate_from_edd --all
```

If you still hit the limit, run individual stages instead of `--all`:

bash

```
wp fluent_cart_migrator migrate_from_edd --products
wp fluent_cart_migrator migrate_from_edd --payments
wp fluent_cart_migrator migrate_from_edd --recount
```

Each invocation gets its own memory context.

### Customer not found errors [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#customer-not-found-errors)

If failures show "customer not found" messages, the order in EDD references a customer record that has been deleted from `edd_customers` but still exists in the order's metadata.

**Fix:** The Migrator falls back to creating a customer from the order's email and address meta when the primary lookup fails. If the order has no usable email at all, you'll need to manually patch the order in EDD before re-running the payments stage.

### Subscription bill counts look wrong [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#subscription-bill-counts-look-wrong)

After the recount stage, occasionally a subscription's bill count doesn't match what you expected.

**Fix:** This usually means renewal orders were never linked to the parent subscription in EDD (subscription\_id is missing). The Migrator's recount step auto-links orphaned renewals by parent\_order\_id, but it can only do that if there's a discoverable link. Re-run recount manually:

bash

```
wp fluent_cart_migrator migrate_from_edd --recount
```

If counts still look off, inspect the renewal orders in FluentCart and confirm their `parent_id` field matches the original subscription's parent order ID.

### License site activations not preserved [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#license-site-activations-not-preserved)

If a customer reports that their license is suddenly invalid on a site they had activated previously, check whether the site URL was preserved during migration.

**Fix:** The Migrator normalizes site URLs (lowercase, no protocol, no trailing slash). If the customer's site URL was stored unusually in EDD (with port numbers, with `:` characters, with non-ASCII characters), it may not have matched after normalization. Check the FluentCart license record's site activations directly. Manually re-add the site if needed.

### Missing subscription UUIDs [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#missing-subscription-uuids)

A small set of subscriptions may end up without UUIDs after migration if the source records were partially corrupted. Run the dedicated fix:

bash

```
wp fluent_cart_migrator fix_subs_uuid
```

This backfills missing UUIDs without touching anything else.

## Resetting a migration [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#resetting-a-migration)

If a staging migration has problems and you want to start fresh, the Migrator provides clean reset paths. All of them are gated behind [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode) - you must define `FLUENT_CART_DEV_MODE` in `wp-config.php` before any reset path will work. This is intentional: reset is destructive, and gating it behind a constant makes it impossible to trigger by accident from the WordPress admin.

Never run reset on production

Reset drops FluentCart tables and deletes migrated post data. Only ever run it on staging, local, or otherwise isolated environments.

### The reset button in the wizard [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#the-reset-button-in-the-wizard)

When Developer Mode is active and the wizard detects a previous migration on the current site, a **Reset Migration** link appears on the Pre-Migration Overview screen inside the "Previous migration detected" notice:

![Pre-Migration Overview with the Previous migration detected notice and Reset Migration link](https://docs.fluentcart.com/assets/07-reset-button.DDretq2x.webp)

Clicking the link asks for confirmation, then runs the reset. On production (Developer Mode disabled), this link is hidden entirely - the notice still appears to confirm the previous run completed, but without the reset option.

### What reset destroys [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#what-reset-destroys)

Reset is thorough. It rolls back everything the migration created so you can start clean.

**Database schema:**

- Drops FluentCart tables via `DBMigrator::refresh()`

**WordPress options cleared:**

- `__fluent_cart_edd3_migration_steps` (stage progress)
- `_fluent_edd_failed_payment_logs` (per-order failure records)
- `__fluent_cart_migration_summary` (summary totals)

**Migrated post data:**

- Deletes FluentCart product posts created by the migration
- Removes migration metadata from EDD posts (`_fcart_migrated_id`, `__edd_migrated_variation_maps`)

Your original EDD data is never touched. Only FluentCart-side records and the bidirectional mapping meta are affected.

### `reset` vs `migrate_fresh` [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#reset-vs-migrate-fresh)

Both are destructive, but they operate at different levels.

| Command | Scope | When to use |
| --- | --- | --- |
| `wp fluent_cart_migrator migrate_from_edd --reset` | Wipes migrated data and clears migration state | Quick reset between rehearsal runs |
| `wp fluent_cart_migrator reset` | Same as `--reset`, invoked as a standalone command | Same scenario, different entry point |
| `wp fluent_cart_migrator migrate_fresh` | Reset plus schema refresh | When the FluentCart schema itself has changed (during plugin upgrades or development) |

For most staging workflows, `--reset` or `reset` is sufficient. Reach for `migrate_fresh` only when the FluentCart database schema has been updated and you want a guaranteed clean slate.

### A staging rehearsal workflow [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#a-staging-rehearsal-workflow)

A typical rehearsal loop looks like this:

01. Clone production into staging, including the EDD database.
02. Enable [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode) in staging's `wp-config.php`.
03. Install FluentCart and the Migrator plugin.
04. Run the full migration via the wizard or CLI.
05. Spot-check products, orders, subscriptions, licenses, coupons.
06. Note anything that needs source-data cleanup before the production run (duplicate customers, broken products, legacy records).
07. Reset the migration: `wp fluent_cart_migrator migrate_from_edd --reset`.
08. Clean up the source data.
09. Re-run the full migration.
10. When the result looks right on staging, repeat on production (with Developer Mode **disabled**).

The ability to iterate without consequence turns a one-shot migration into something closer to a controlled, auditable process.

### Confirmation prompts [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#confirmation-prompts)

Every reset path asks for confirmation before destroying data - both in the CLI and in the wizard. You can bypass the CLI prompt with the standard WP-CLI `--yes` flag:

bash

```
wp fluent_cart_migrator migrate_from_edd --reset --yes
```

Only do this inside scripts you have reviewed. The confirmation exists for a reason.

## Frequently asked questions [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#frequently-asked-questions)

### Will my existing customers need to do anything? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#will-my-existing-customers-need-to-do-anything)

No. Their accounts, order history, subscriptions, and licenses all move over. They log in with their existing WordPress credentials and find everything where they expect it - now inside FluentCart instead of EDD.

### Will active subscriptions keep renewing automatically? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#will-active-subscriptions-keep-renewing-automatically)

Yes. Subscription records migrate with their gateway subscription IDs (Stripe, PayPal). As long as you reconnect the same gateway accounts in FluentCart, renewals continue without interruption. PayPal Standard subscriptions are handled by the Migrator's [backward compatibility layer](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility).

### Will my customers' software licenses keep working? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#will-my-customers-software-licenses-keep-working)

Yes. The Migrator intercepts EDD-format license API calls (activation, deactivation, validity check, update check) and routes them through FluentCart. Customers don't need to update or reconfigure anything.

### Does the migration modify or delete my EDD data? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#does-the-migration-modify-or-delete-my-edd-data)

Never. The Migrator only reads from EDD's database tables. Your original data is untouched. You can verify the entire migration against your EDD store before switching anything over.

### What if the migration is interrupted halfway through? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#what-if-the-migration-is-interrupted-halfway-through)

Just start it again. The Migrator tracks its own progress, skips completed stages, and resumes the payments stage from the exact batch where it stopped. No duplicate data.

### How long does the migration take? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#how-long-does-the-migration-take)

It depends on store size:

- Small stores (a few hundred orders): two to five minutes
- Medium stores (thousands of orders): ten to thirty minutes
- Large stores (tens of thousands of orders): thirty minutes to a couple of hours

The CLI is consistently faster than the wizard for medium and large stores because it avoids HTTP timeouts and per-batch round trips.

### Can I run the migration multiple times? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#can-i-run-the-migration-multiple-times)

Yes. Every stage is idempotent. Re-running products updates existing migrated products via the ID map. Re-running coupons updates existing coupons by code. Re-running recount always recalculates from current data. There is no risk of duplicate records from re-running.

### What about WooCommerce or SureCart migrations? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#what-about-woocommerce-or-surecart-migrations)

The source picker shows WooCommerce and SureCart cards marked "coming soon." The architecture supports multiple sources, but only EDD 3.x is implemented in the current release. WooCommerce and SureCart sources are on the roadmap.

### Where do I get help if I'm stuck? [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#where-do-i-get-help-if-i-m-stuck)

- Check the failed payment log: `wp fluent_cart_migrator migrate_from_edd --log`
- Run license verification: `wp fluent_cart_migrator migrate_from_edd --verify_license`
- Read [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility) if a customer reports a problem post-migration
- Open a support ticket via your FluentCart account

## Related [​](https://docs.fluentcart.com/guide/migration/edd/troubleshooting\#related)

- [Migrating from EDD](https://docs.fluentcart.com/guide/migration/edd/edd-migration) - the wizard walkthrough
- [WP-CLI Reference](https://docs.fluentcart.com/guide/migration/edd/edd-cli) - full command surface
- [Developer Mode & Reset](https://docs.fluentcart.com/guide/migration/edd/developer-mode) - staging workflow
- [Backward Compatibility](https://docs.fluentcart.com/guide/migration/edd/backward-compatibility) - what the Migrator continues to handle after migration

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## What Gets Migrated - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/migration/edd/what-is-migrated

[Skip to content](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated#VPContent)

# What Gets Migrated [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#what-gets-migrated)

Before you run a migration, it is worth knowing exactly what comes across, what doesn't, and why. This page covers both - so there are no surprises after the wizard finishes.

## What is migrated [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#what-is-migrated)

### Products [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#products)

Every EDD download transfers as a FluentCart product, with the structure preserved.

| EDD concept | Becomes in FluentCart | Notes |
| --- | --- | --- |
| Simple download | Simple product | Single price tier |
| Variable pricing | Product variations | One variation per EDD price option |
| Product bundle | Product with bundle child references | Child IDs stored in line metadata |
| Recurring download | Subscription product | Billing intervals: daily, weekly, monthly, quarterly, half-yearly, yearly |
| Title, description, slug, author, dates | Same | Unchanged |
| Featured image | Same | Same media library reference |
| Signup fees | Variation `other_info` | Stored alongside pricing |
| License limits per variation | Variation license limit | Only when EDD Software Licensing is detected |

A bidirectional ID map is created so re-running the migration updates rather than duplicates: `_fcart_migrated_id` on the EDD post points to the FluentCart record, and `_edd_migrated_from` on the FluentCart product points back.

### Customers [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#customers)

Customer records transfer with full identity and address data, deduplicated on email.

- Full name, email address
- WordPress user account association if one exists by email
- Addresses: country, state, city, postal code
- Lifetime value, purchase count, average order value, first/last purchase dates - recalculated from the migrated orders during the **Recount & Verify** step

If a customer with the same email already exists in FluentCart when an order is being migrated, the order is linked to the existing record rather than creating a duplicate.

### Orders and Payments [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#orders-and-payments)

Every order with a meaningful status transfers - including all line items, taxes, discounts, transactions, and notes.

| EDD status | FluentCart payment status |
| --- | --- |
| `complete`, `processing`, `edd_subscription`, `publish` | Paid |
| `pending` | Pending |
| `refunded` | Refunded |
| `partially_refunded` | Partially Refunded |
| `revoked`, `failed`, `cancelled` | Failed |

Each order brings:

- Order ID (preserved from EDD)
- Subtotal, tax, shipping, discount, line total
- Currency and payment mode (test/live)
- Billing address
- Line items: product ID, variation ID, quantity, unit price, subtotal, tax, discount, fulfillment type
- Bundle child items (where applicable)
- Transaction records with gateway, transaction ID (Stripe charge ID, PayPal subscription ID), amount, currency, date
- Refund records (amounts and dates)
- Applied coupon codes with the discount amount
- Order notes from `edd_notes`

### Subscriptions [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#subscriptions)

When EDD Recurring Payments is in use, every subscription comes across with its complete state.

| Field | Behavior |
| --- | --- |
| Status | `active`, `cancelled`, `expired`, `completed`, `pending`, `failing`, `trialling` mapped 1:1 |
| Billing interval | Preserved (daily through yearly) |
| Bill times limit | Preserved |
| Signup fee | Calculated as the delta between initial and recurring amount |
| Start date, renewal date, expiration date | Preserved |
| Vendor subscription ID | Stripe `vendor_subscription_id`, PayPal subscription ID |
| Currency | Preserved |
| Activities/notes | From `edd_notes` with `object_type='subscription'` |
| Renewal order history | Linked via `parent_id` on each renewal order |

After import, the **Recount & Verify** step rebuilds bill counts from actual renewal orders, marks subscriptions completed where they have hit their bill-times limit, auto-links orphaned renewals by parent order ID, and generates UUIDs for any missing entries.

### Software Licenses [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#software-licenses)

For stores running EDD Software Licensing, this is the most consequential part of the migration. License keys, activation limits, expirations, and every active site activation transfer with full fidelity.

| Item | Behavior |
| --- | --- |
| License key | Preserved exactly |
| Status | `active`, `inactive`, `expired`, `disabled` mapped 1:1 |
| Activation limit | From license record, or `_edd_sl_limit` meta override |
| Expiration date | Converted to FluentCart format |
| Product, variation, order, customer associations | All linked |
| Site activations | Every URL preserved, normalized via FluentCart's site URL formatter |
| Site activation status, hash, date | Preserved |
| Renewal license linkage | Linked back to the original subscription |

This means your customers do not need to deactivate and reactivate their installs. The sites they have running stay running.

FluentCart Pro requirement

License migration requires FluentCart Pro, since the license module lives there. The Migrator detects EDD Software Licensing automatically and enables the license module on first run - no separate setup step.

### Coupons [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#coupons)

Every EDD discount code transfers with its rules intact.

- Code (exact string)
- Discount type: `flat` → `fixed`, `percentage` → `percentage`
- Discount amount
- Status: `active` or `disabled`
- Usage limits: max total uses, max per customer (`once_per_customer`)
- Date range: start date, end date
- Minimum purchase amount
- Product restrictions: included products and excluded products, with EDD product IDs converted to FluentCart product IDs via the migration ID map
- Recurring behavior: applies to first payment only vs. all renewals
- Notes / description
- Affiliate association if AffiliateWP meta is present
- Use count: recalculated from applied coupons on paid orders during recount

If a coupon code already exists in FluentCart, the migration updates that record. Otherwise, a new one is inserted. Re-running coupon migration is safe.

### Tax Rates [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#tax-rates)

Tax migration is conditional. It only runs if `edd_settings.enable_taxes` is true. If taxes are disabled in EDD, this step is skipped with a clear notice.

When enabled, the migration brings:

- Currency position (`before` / `after`)
- Decimal separator (`dot` / `comma`)
- Store name, address, city, state, country, postcode
- Tax-inclusive vs. exclusive pricing behavior

It then generates FluentCart's default tax classes (Standard, Reduced, Zero) and tax rates for every country found in the EDD tax rates table. The mapping between EDD rates and the new FluentCart rates is stored in `_edd_fct_tax_rate_maps` so order-level tax adjustments stay accurate.

Not a 1:1 rate copy

FluentCart's tax model differs from EDD's. The Migrator generates modern FluentCart tax rates for the relevant countries rather than copying every EDD rate as-is. Review your tax setup after migration to confirm it matches your jurisdictional requirements.

* * *

## What is NOT migrated [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#what-is-not-migrated)

Honesty about boundaries matters more than a longer feature list. The following items are deliberately out of scope.

### Product categories and tags [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#product-categories-and-tags)

EDD's `download_category` taxonomy and any custom taxonomies do not transfer. FluentCart's category model differs structurally, and a one-to-one mapping would mislead more than help. Set up your categories fresh in FluentCart after migration.

### EDD upgrade paths [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#edd-upgrade-paths)

The EDD upgrade-path mechanic - the ability for a customer to upgrade from one product or pricing tier to another - is not modeled in FluentCart's schema and is not migrated. If you rely on upgrade paths, plan how to handle them in FluentCart before switching over.

### Custom product and order metadata [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#custom-product-and-order-metadata)

Only known fields from EDD core, EDD Recurring Payments, EDD Software Licensing, and AffiliateWP are parsed. Custom meta written by other third-party EDD add-ons is not preserved. If you have important custom data on products or orders, export it separately before migrating.

### Abandoned and trashed orders [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#abandoned-and-trashed-orders)

Orders with status `abandoned` or `trash` are explicitly filtered out. Only orders representing real transactions transfer.

### Payment gateway credentials [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#payment-gateway-credentials)

Transaction records - Stripe charge IDs, PayPal subscription IDs - come across, so renewals continue to process correctly. **Gateway API keys themselves never transfer.** Reconnect Stripe and PayPal in FluentCart after migration using the same accounts you used in EDD.

### Email templates [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#email-templates)

EDD's email settings are not migrated. FluentCart has its own notification system with its own templates. Review and customize them under **FluentCart > Settings > Email Configuration**.

### Download file attachments [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#download-file-attachments)

Products are created. The actual downloadable files attached to each product are not automated. File paths, permissions, and storage architecture differ enough between platforms that an automated transfer would silently break delivery for customers. Open each digital product in FluentCart and confirm the file is linked under **Downloadable Asset(s)**.

### Download history logs [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#download-history-logs)

EDD's `edd_file_download_logs` table is not read. License site activations are preserved (those are functionally different and serve a real ongoing purpose), but historical file download events are not.

### Refund reason text [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#refund-reason-text)

Refund amounts and dates transfer as part of the order. The reason text - which EDD only stores inside order notes - is not extracted into a separate field.

### Dry-run mode [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#dry-run-mode)

All operations in 1.0.0 are live. There is no preview mode. To rehearse a migration safely, use [Developer Mode](https://docs.fluentcart.com/guide/migration/edd/developer-mode) on a staging environment, run the full migration, review the result, then reset and run again.

* * *

## At a glance [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#at-a-glance)

| Entity | Migrated? | Notes |
| --- | --- | --- |
| Products (simple, variable, bundle, recurring) | ✅ | Categories not migrated |
| Product images and content | ✅ |  |
| Custom product meta from third parties | ❌ | Only known fields parsed |
| Customers | ✅ | Deduplicated by email |
| Orders (all real statuses) | ✅ | Abandoned and trash excluded |
| Order line items, taxes, discounts | ✅ |  |
| Transactions (Stripe, PayPal, custom) | ✅ | IDs preserved |
| Refunds (amount + date) | ✅ | Reason text not extracted |
| Subscriptions | ✅ | Bill counts rebuilt during recount |
| Software licenses | ✅ | Requires FluentCart Pro |
| License site activations | ✅ | URLs normalized |
| Coupons | ✅ | Categories on coupons not migrated |
| Tax rates | ✅ | Only if enabled in EDD |
| Payment gateway credentials | ❌ | Reconnect in FluentCart |
| Email templates | ❌ | Set up fresh in FluentCart |
| Downloadable file attachments | ❌ | Re-attach in each product |
| Download history logs | ❌ |  |
| Product categories / tags | ❌ |  |
| EDD upgrade paths | ❌ |  |
| Abandoned / trashed orders | ❌ | Intentionally excluded |

* * *

## Next steps [​](https://docs.fluentcart.com/guide/migration/edd/what-is-migrated\#next-steps)

Now that you know exactly what's in scope, head to the [Migrating from EDD](https://docs.fluentcart.com/guide/migration/edd/edd-migration) walkthrough to run your first migration.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
