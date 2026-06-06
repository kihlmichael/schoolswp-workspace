---
source_url: https://surecart.com/docs/change-customer-dashboard-permalinks
source: surecart-kb
scraped: true
---

# Change Customer Dashboard Permalinks - SureCart

## Overview

This document explains how to customize the links associated with the "Go Back" button and store logo in the SureCart customer dashboard.

## Default Behavior

By default, the "Go Back" button and store logo in the SureCart customer dashboard link back to the website's homepage. You might prefer these elements to link to a different, more relevant page for your customers.

## How to Change Permalinks in Customer Dashboard

Two new filters have been added, allowing you to modify the URLs for both the "Go Back" button and the store logo:

- `sc_customer_dashboard_back_home_url`: Controls the URL for the "Go Back" button
- `sc_customer_dashboard_store_logo_url`: Controls the URL for the store logo

By adding custom code snippets utilizing these filters, you can redirect users to your preferred page when they click on the "Go Back" button or the store logo within the customer dashboard.

[code snippet omitted — see source_url]

**How to Add the Code:**

- **Child Theme's functions.php**: Add the code snippet to the functions.php file within your child theme
- **Code Snippet Plugin**: Alternatively, use a code snippet plugin specifically designed for adding custom PHP code to your website

## Alternative Workaround

1. **Change Default Template**: Modify the default template for your custom dashboard
2. **Create New Template**: Manually create a new template for your custom dashboard that defines a custom link for the "Go Back" button
