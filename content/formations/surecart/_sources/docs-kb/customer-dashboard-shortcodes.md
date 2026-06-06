---
source_url: https://surecart.com/docs/customer-dashboard-shortcodes
source: surecart-kb
scraped: true
---

# Customer Dashboard Shortcodes

SureCart offers customizable customer dashboard functionality that works with various page builders like Divi, Elementor, and Bricks Builder through dedicated shortcodes.

## Main Shortcodes

The primary wrapper shortcode is:

[code snippet omitted — see source_url]

Individual component shortcodes that nest inside the wrapper:

[code snippet omitted — see source_url]

## Order Confirmation Shortcodes

For custom thank you pages, use the `[sc_order_confirmation]` wrapper with nested `[sc_order_confirmation_line_items]` and `[sc_customer_dashboard_button]` shortcodes.

## Implementation Requirements

**Important considerations:**

- All shortcodes must be wrapped inside `[sc_customer_dashboard_page]` to display login forms for non-authenticated users
- If `sc_customer_orders`, `sc_customer_subscriptions`, and `sc_customer_downloads` aren't included on the order confirmation page, email links redirect only to the main dashboard
- Emails redirect to whichever page is designated as the **Customer Dashboard** page, regardless of separate custom pages

## Adding Shortcodes

The guide demonstrates implementation in Elementor:

1. Navigate to your Customer Dashboard page in WordPress admin
2. Click "Edit with Elementor"
3. Add a Shortcode block from the left panel
4. Paste your desired shortcode combination
5. Customize by removing unwanted sections

## Customization Options

You can:

- **Display specific sections only** by including only those shortcodes
- **Organize with tabs** by using Elementor's Tabs block and placing individual shortcodes in separate tabs
- **Modify titles** using the `title` parameter in each shortcode

These shortcodes work across all major page builders beyond Elementor.
