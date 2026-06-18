---
source_url: https://surecart.com/docs/is-not-a-valid-json-response
source: surecart-kb
scraped: true
---

# Fixing the "This response is not a valid JSON response" Error

## Overview

This error appears when using the SureCart checkout form on WordPress sites. The guide outlines potential causes and solutions.

## Reason 1: REST API Outages in WordPress

The REST API serves as the communication channel between SureCart and your WordPress installation. If disabled or encountering errors, it can prevent valid JSON responses.

**How to check:**

- Navigate to Tools > Site Health in the WordPress Dashboard
- Look for issues mentioning REST API or JSON responses
- If REST API is disabled, re-enable it through settings or deactivate plugins blocking it

## Reason 2: Server Firewall Blocking REST API

Firewalls and security plugins may mistakenly identify REST API requests as threats, blocking or altering them.

**How to check:**

- Access your hosting dashboard or server settings
- Review firewall logs for blocks corresponding to error timestamps
- Whitelist necessary URLs or adjust firewall settings accordingly
- Contact hosting support if you need assistance with firewall configuration

## Reason 3: WP_DEBUG Interference

Having WP_DEBUG enabled on a live environment can cause unnecessary messages to be output in API responses, potentially disrupting response structure.

**How to disable:**

1. Access your website root directory via FTP or file manager
2. Edit the wp-config.php file
3. Find the WP_DEBUG constant set to true
4. Change the value to false
5. Save changes

## Additional Recommendations

Regularly check the Site Health page in your WordPress Dashboard to identify potential REST API issues or other critical concerns. If problems persist after implementing these solutions, contact SureCart support or consult a developer for advanced troubleshooting.
