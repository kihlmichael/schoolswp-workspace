---
source_url: https://surecart.com/docs/hide-invoice-button-on-customer-dashboard
source: surecart-kb
scraped: true
---

# How to Hide/Change the Download Invoice Button on Your Customer Dashboard

## Overview

SureCart displays a download invoice button on the customer dashboard by default. For specific use cases, you may want to hide this button or replace it with custom invoicing solutions.

## Implementation Steps

### Using Code Snippets Plugin

1. Copy the PHP filter code that hooks into `surecart/order/set_attribute` and returns an empty string for the `statement_url` attribute (see source_url for exact code)

2. Navigate to your WordPress dashboard and go to **Snippets > All Snippets > Functions (PHP)**

3. Click "Add New" to create a new code snippet

4. Paste the code into the editor and optionally add a title and description

5. Click "Save Changes and Activate" to enable the snippet

### Alternative Methods

You can implement this code through:

- Your theme's functions.php file directly
- Any code snippets plugin of your choice

## Customization

The invoice URL can be modified according to your specific requirements rather than simply returning an empty string.

## Verification

After activation, visit your customer dashboard to confirm the download button has been removed or modified as intended.

## Support

If issues persist or implementation assistance is needed, contact SureCart's support team.
