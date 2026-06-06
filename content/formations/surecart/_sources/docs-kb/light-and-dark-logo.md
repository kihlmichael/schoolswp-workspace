---
source_url: https://surecart.com/docs/light-and-dark-logo
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/How to Configure Email Logos for Light and Dark Mode

# How to Configure Email Logos for Light and Dark Mode

This document explains how to configure light mode and dark mode logos in SureCart to ensure consistent brand rendering across email clients.

## Overview

Email clients (such as Gmail, Apple Mail, and Outlook) handle dark mode inconsistently. To avoid rendering issues, SureCart allows merchants to configure separate logos and brand colors for light mode and dark mode.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- A light mode logo file
- A dark mode logo file (recommended)

## **Step-by-Step Instructions**

1. Go to **WordPress Dashboard → SureCart → Settings**.
2. Open the **Design & Branding** tab.
3. Locate the **Brand Settings** section.
4. Under **Theme**, two options are displayed: **Light Mode** and **Dark Mode**.
5. In the **Light Mode** card: set the **Brand Color** and upload the **Logo** designed for light backgrounds.
6. In the **Dark Mode** card: set the **Brand Color** and upload the **Logo** designed for dark backgrounds.
7. Click **Save**.

## **Expected Outcome**

Once both versions are configured, SureCart will serve the appropriate logo and brand color based on the recipient's email client and system theme. This applies to the WordPress site, transactional emails, and the affiliate portal.

## **Best Practices for Logo Preparation**

- Provide a dedicated dark mode logo and color.
- Ensure the light mode logo has sufficient contrast.
- Avoid relying on transparent backgrounds alone.

## **Notes and Limitations**

- Dark mode support varies between email clients. Even with both logos configured, rendering may differ across Gmail, Apple Mail, Outlook, and others.
- Brand color and logo changes apply to new emails sent after saving. Previously sent emails are not affected.

## **FAQ**

**What happens if only a light mode logo is configured?**

The light mode logo will be used in all email clients. In clients that force dark mode, the logo may lose contrast.

**Do these settings affect the storefront and checkout pages as well?**

Yes. The brand settings apply globally across SureCart, including hosted pages, emails, and the affiliate portal.
