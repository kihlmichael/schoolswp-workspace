---
source_url: https://surecart.com/docs/lsp-config
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Configuring LiteSpeed Cache for SureCart

# Configuring LiteSpeed Cache for SureCart

SureCart uses WordPress REST API endpoints and core scripts to deliver real-time cart data, customer information, product details, and checkout flows. Improper caching configuration can cause outdated information, broken checkout forms, or missing cart updates.

## Requirements

- LiteSpeed Cache plugin installed and activated
- SureCart plugin installed and activated

## Step 1: Exclude REST API Requests from Caching

Go to **WordPress Dashboard → LiteSpeed Cache → Cache → Excludes**.

Under **Do Not Cache URIs**, add:

```
/wp-json/*
```

Click **Save Changes**.

## Step 2: Prevent Deferring of Core WordPress Scripts

SureCart depends on core WordPress scripts (`wp-api-fetch`, `wp-a11y`, `wp-i18n`, `wp-url`, `dom-ready`, `hooks`).

**Option A: Disable JS Deferral Completely**

Go to **LiteSpeed Cache → Page Optimization → JS Settings**, set **Load JS Deferred** to **Off**, click **Save Changes**.

**Option B: Exclude Specific Scripts from Deferral**

Under the **Tuning** tab, add to **JS Excludes**:

```
/wp-includes/js/dist/api-fetch.min.js
/wp-includes/js/dist/a11y.min.js
/wp-includes/js/dist/i18n.min.js
/wp-includes/js/dist/url.min.js
/wp-includes/js/dist/dom-ready.min.js
/wp-includes/js/dist/hooks.min.js
```

## Step 3: Disable JavaScript Combining

Go to **LiteSpeed Cache → Page Optimization → JS Settings**, set **Combine JS Files** to **Off**, click **Save Changes**.

## Step 4: Exclude Dynamic SureCart Pages from Caching

Go to **LiteSpeed Cache → Cache → Excludes**, add to **Do Not Cache URIs**:

```
/checkout/
/login/
/account/
/customer-dashboard/
```

Note: If custom permalinks are used, substitute the appropriate URLs.

## Step 5: Disable Aggressive Browser Caching for Dynamic Content

Go to **LiteSpeed Cache → Browser**, set **Enable Browser Cache** to **Off**, click **Save Changes**.

## Step 6: Clear Cache and Test Changes

Go to **LiteSpeed Cache → Toolbox → Purge**, click **Purge All**.

Test in an incognito window:

- Visit a product page and add an item to the cart. Verify the cart updates in real time.
- Navigate to the checkout page and confirm the form loads without errors.
- Log in and visit the Customer Dashboard. Verify account data displays correctly.

## Expected Outcome

Once configured correctly, LiteSpeed Cache will not interfere with SureCart's dynamic functionality.

## FAQ

**What happens if I don't exclude REST API endpoints from caching?**

Customers may see outdated cart data, incorrect product information, or broken checkout flows.

**Why do core WordPress scripts need to be excluded from deferral?**

SureCart depends on these scripts to handle interactive features. Deferring them can cause checkout forms and cart updates to fail.
