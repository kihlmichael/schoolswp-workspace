---
source_url: "https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption.html"
title: "Fixing Access Token Decryption Failed in WP Social Ninja"
---

# Fixing Access Token Decryption Failed in WP Social Ninja

Sometimes, when connecting Instagram, Facebook, or other platforms, WP Social Ninja may show an error like:

**“Access token decryption failed. Possibly mismatched WordPress logged-in salt/key.”**

This error typically appears:

*   After **migrating your site** from staging to live or moving to a new server.
    
*   When using a **security plugin** like Sucuri that modifies WordPress salts.
    
*   If the **WordPress authentication keys and salts** were changed manually or regenerated.
    

### **Why This Happens** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#why-this-happens)

WP Social Ninja saves your connected accounts' **access tokens** securely in your WordPress database. To keep them safe, the plugin encrypts these tokens using **WordPress authentication salts** (like LOGGED\_IN\_SALT).

Here’s the problem:

*   If another plugin (like any security plugins) changes these salts,
    
*   Or if you regenerate the salts in wp-config.php,
    

…the old tokens can no longer be decrypted. As a result, WP Social Ninja cannot read them, and the connection breaks.

## **The Solution: Use Dedicated WP Social Ninja Keys** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#the-solution-use-dedicated-wp-social-ninja-keys)

To avoid relying on salts that may change, you can add your **own custom encryption keys** specifically for WP Social Ninja.

This ensures:

*   Tokens stay valid, even if WordPress salts are updated.
    
*   Other plugins or security tools won’t interfere with WP Social Ninja’s encryption.
    

### **How to Fix the Error** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#how-to-fix-the-error)

#### **1\. Open Your wp-config.php** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#_1-open-your-wp-config-php)

*   Access your site files via **FTP** or your hosting **File Manager**.
    
*   Open the wp-config.php file in the root of your WordPress installation.
    
*   Scroll down to find the **Authentication Unique Keys and Salts** section.
    

It will look like this:

php

```
/*#@+

Authentication unique keys and salts.

Change these to different unique phrases! You can generate these using

the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.

You can change these at any point in time to invalidate all existing cookies.

This will force all users to have to log in again.

@since 2.6.0 */

define( 'AUTH_KEY',         'xxxxx' );

define( 'SECURE_AUTH_KEY',  'xxxxx' );

define( 'LOGGED_IN_KEY',    'xxxxx' );

define( 'NONCE_KEY',        'xxxxx' );

define( 'AUTH_SALT',        'xxxxx' );

define( 'SECURE_AUTH_SALT', 'xxxxx' );

define( 'LOGGED_IN_SALT',   'xxxxx' );
```

Right **below this section**, add two new lines with your own unique keys:

#### **2\. Add WP Social Ninja Keys** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#_2-add-wp-social-ninja-keys)

php

```
define('WPSR_ENCRYPTION_KEY',  'Paste_generated_key_here');

define('WPSR_ENCRYPTION_SALT', 'Paste_generated_key_here');
```

**Important:**

*   Do not copy the example values above.
    
*   Generate new fresh, random values using the [WordPress secret-key generator](https://api.wordpress.org/secret-key/1.1/salt/).
    

#### **3\. Save and Reconnect** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#_3-save-and-reconnect)

*   Save the wp-config.php file and re-upload it to your server if needed.
    
*   Go back to your WordPress dashboard.
    
*   Reconnect your **Instagram (or other social) accounts** in WP Social Ninja.
    

This will store the tokens again using your new, stable encryption keys.

### **Important Notes** [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/fixing-access-token-decryption#important-notes)

*   **Do not change these keys later.** If you update them, WP Social Ninja won’t be able to read existing tokens, and you’ll need to reconnect your accounts.
    
*   If you run multiple environments (staging, live, local), use the **same encryption keys** across all of them. Otherwise, tokens may fail when moving the database.
    
*   By defining your own WP Social Ninja keys, you isolate the plugin’s encryption from WordPress salts, avoiding conflicts with plugins.
    

After following these steps, WP Social Ninja will securely store and decrypt your tokens without being affected by other WordPress salts or security plugins.
