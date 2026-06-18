---
source_url: https://surecart.com/docs/add-surecart-api
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/Connecting – How to Add Your SureCart API Token

# Connecting – How to Add Your SureCart API Token

This document explains how to connect the SureCart plugin to a store account using an API token.

##### Requirements

- A SureCart store account
- SureCart plugin installed and activated
- WordPress admin access

##### Step 1: Navigate to the API Section

Go to App.surecart.com → Click **API** in the sidebar menu.

Select the **Secret Token** tab.

##### Step 2: Copy the API Token

Copy the API token displayed on the screen.

**Important:** Store this token securely. It provides access to the store and should not be shared publicly.

##### Step 3: Add the Token to WordPress

Open your WordPress site.

Go to WordPress Dashboard → SureCart → Settings → Connection.

Paste the API token into the **API Token** field.

Click **Save**.

Expected Outcome

Once the token is saved, the SureCart plugin will be connected to the store account. The connection status will display as "Connected" in the Settings area.

##### FAQ

**What happens if I delete my API token?**

Deleting the token will immediately disconnect all sites currently using the token. The new token must be manually added to each WordPress installation to restore the connection.

**Can I use the same API token on multiple WordPress sites?**

Yes. The same API token can be used to connect multiple WordPress installations to the same SureCart store.

**What should I do if my site shows as disconnected?**

This typically occurs when the API token has been removed. Navigate to WordPress Dashboard → SureCart → Settings → Connection, and re-enter the current API token from the SureCart cloud platform.
