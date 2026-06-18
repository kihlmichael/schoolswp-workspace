---
source_url: https://surecart.com/docs/api-token-wp-config
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/How to Configure the SureCart API Token in wp-config.php

# How to Configure the SureCart API Token in wp-config.php

This document explains how to define the SureCart API token as a PHP constant in the wp-config.php file, instead of storing it in the WordPress database through the admin interface. This approach keeps the token outside the database, preserves the connection during migrations, and prevents disconnection caused by plugins that regenerate WordPress salts.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- Access to the wp-config.php file via FTP, SFTP, SSH, or the hosting provider's file manager
- A valid SureCart API token. Refer to [How to Get the SureCart API Token](https://surecart.com/docs/add-surecart-api/).

## **When This Approach Is Recommended**

Defining the API token in wp-config.php is recommended in the following scenarios:

- **Security-sensitive environments.** The token is stored in the site files rather than in the WordPress database, reducing exposure in the event of a database compromise or unauthorized admin access.
- **Site migrations and cloning.** The token travels with the site files. A site cloned to staging or deployed to a new server remains connected to SureCart without manually re-entering the token.
- **Sites affected by salt regeneration.** Some security plugins periodically regenerate WordPress salts, which can invalidate the token stored in the database. A token defined in wp-config.php is unaffected.

On standard sites that do not face any of the situations above, configuring the token through **SureCart → Settings → Connection** in the WordPress admin remains a valid option.

## **Step-by-Step Instructions**

### **Step 1: Back Up the wp-config.php File**

Before any change is made, download a copy of the existing wp-config.php file. If the edited file contains a syntax error or an incorrect value, restoring the backup returns the site to a working state.

- Connect to the site via FTP, SFTP, SSH, or the hosting provider's file manager.
- Locate wp-config.php in the WordPress installation root directory (the same directory that contains the wp-content folder).
- Download a copy and store it in a safe location.

### **Step 2: Add the Token Constant**

Open wp-config.php in a text editor and locate the following line:

```
/* That's all, stop editing! Happy publishing. */
Add the following line just above this comment:
define( 'SURECART_API_TOKEN', 'st_xxxxxxxxxxxxxxxxxxxxxxxx' );
```

Replace st_xxxxxxxxxxxxxxxxxxxxxxxx with the actual API token retrieved from the SureCart account. The token always starts with st\_.

**Important:** Placing the constant **above** the "That's all, stop editing!" line is required. Constants defined below that line may not be loaded in time and will be ignored by SureCart.

### **Step 3: Save and Upload**

- Save the modified wp-config.php file.
- Upload the file back to the WordPress installation root, replacing the existing version.
- Confirm that file permissions remain set to the values used by the hosting provider (typically 644 or 600).

### **Step 4: Verify the Connection**

- Sign in to the WordPress admin.
- Go to **SureCart → Settings → Connection**.
- Confirm that the connection status is displayed as **Connected**.
- Optionally, run a quick checkout test to confirm that orders and other store operations function as expected.

**Expected outcome:** The SureCart admin connection shows as Connected, the database-stored token (if previously configured) is overridden by the constant defined in wp-config.php, and the site retains its SureCart connection across migrations and salt regenerations.

## **Removing the Token from wp-config.php**

To stop using the constant and return to managing the token through the WordPress admin:

- Open wp-config.php via FTP, SFTP, SSH, or the hosting provider's file manager.
- Locate the line define( 'SURECART_API_TOKEN', '…' );.
- Delete the line and save the file.
- Upload the file back to the WordPress installation root.
- Sign in to the WordPress admin and go to **SureCart → Settings → Connection**.
- Enter the API token in the connection field and save.

## **Notes and Limitations**

- When the constant is defined in wp-config.php, it overrides any token saved in the WordPress database via **SureCart → Settings → Connection**.
- Editing wp-config.php directly carries risk. A syntax error or accidental deletion of an existing constant can prevent the site from loading. The backup created in Step 1 allows the previous state to be restored.
- The wp-config.php file is loaded by WordPress on every request, so constants defined inside it are available globally without performance impact.
- Some security plugins protect wp-config.php with additional permissions or rules. These protections do not affect SureCart, but may require temporary adjustments to upload the edited file.

## **Related Documentation**

- [How to Get the SureCart API Token](https://surecart.com/docs/add-surecart-api/)
- [Connecting SureCart via the Admin Interface](https://surecart.com/docs/add-surecart-api/)

## **FAQ**

**Is configuring the token in wp-config.php required?**

No. The token can also be configured through **SureCart → Settings → Connection** in the WordPress admin. Using wp-config.php is recommended in specific scenarios (security-sensitive environments, frequent migrations, sites affected by salt regeneration), but is not mandatory.

**Which value takes precedence when the token is defined in both places?**

The constant defined in wp-config.php takes precedence over the token stored in the WordPress database. The database value is ignored as long as the constant is present.

**What happens if the token defined in wp-config.php is invalid?**

SureCart cannot authenticate with the cloud and the connection status displayed under **SureCart → Settings → Connection** reflects the failure. Store operations that require the SureCart cloud (such as checkout and order syncing) do not function. Replacing the constant with a valid token restores the connection.

**Why does the site display "SureCart disconnected"?**

Disconnection typically occurs when the API token is removed, replaced, or invalidated. Common causes include database overwrites, plugin updates, site migrations performed without preserving the token, or plugins that regenerate WordPress salts. Defining the token in wp-config.php prevents most of these scenarios. When disconnection occurs, the token can be re-entered through **SureCart → Settings → Connection** or restored by editing wp-config.php.

**Does defining the constant affect WordPress or other plugins?**

No. The constant is read only by SureCart and does not interact with WordPress core or other plugins.

**Can the token be defined in wp-config.php on multisite installations?**

Yes. When the same SureCart store is connected to all sites in a multisite network, the constant can be defined once in the shared wp-config.php file. For networks where different sites connect to different SureCart stores, the database-based configuration in each site's admin is more appropriate.

**What happens during a site migration when the token is defined in wp-config.php?**

The token moves with the site files. When the destination site loads, the constant is detected and the SureCart connection is preserved without manual re-entry. This avoids the disconnection that can occur when only the database token exists and the database is migrated separately from the files.
