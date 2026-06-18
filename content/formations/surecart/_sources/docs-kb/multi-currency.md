---
source_url: https://surecart.com/docs/multi-currency
source: surecart-kb
scraped: true
---

# Multi-Currency Localization

## Overview

The Multi-Currency feature allows customers to view product prices in different currencies based on their location or preference. Instead of a single currency display, shoppers see localized prices (e.g., USD $30.00, EUR €28.00, GBP £25.00), eliminating manual conversion calculations.

**Benefits:**

- Displays prices in familiar currencies
- Removes need for manual conversion
- Provides transparent pricing during checkout

## Adding Display Currencies

1. Navigate to the **Display Currencies** section
2. Click the **Add New** button
3. Select your desired currency

Once added, you will see the currency's label, automatically-updated exchange rate, and a frontend preview. The exchange rate is updated automatically by SureCart, so you do not need to manage it manually.

## Currency Switcher Implementation

### Classic Themes

- Click **Add Menu** and select your menu location
- Choose switcher position (left/right)
- Save changes

### Full Site Editing (FSE) Themes

1. Navigate to **Templates** and filter for SureCart templates
2. Open **Product Collections** template
3. Click **Document Overview** icon
4. Search for "currency" and select **Currency Switcher** block
5. Configure settings and save

### Page Builders

Use the `[sc_currency_switcher]` shortcode with Elementor, Divi, Bricks Builder, and similar platforms.

## Currency Formatting

Configure how currencies display via the **Formatting Locale** dropdown under Currency Settings. Formatting affects symbol placement, decimal usage, and locale-specific conventions.

## Geolocation

Geolocation automatically detects a user's location and sets the initial currency displayed on your site. This feature is enabled by default but can be disabled. Customers retain the ability to manually switch currencies regardless of geolocation settings. Note: VPNs and cached pages may impact accuracy.

## Important Checkout Details

**Payment Processing:** Customers are always charged in the store's base currency, not the displayed currency. The checkout clearly shows:

- Total in displayed currency
- **Payment Total** in base currency
- Notice: "Your payment will be processed in [Base Currency]"

**Dashboard & Invoices:** The Customer Dashboard, receipts, and invoices display amounts exclusively in the store's base currency to maintain accurate records.

## FAQ

**Are exchange rates automatic?**
Yes, SureCart updates rates automatically.

**Can customers change currencies with geolocation enabled?**
Yes, the Currency Switcher allows manual selection regardless.

**What currency charges the buyer?**
Always the store's base currency, clearly displayed at checkout.

**Why use this multi-currency approach?**

The design prioritizes merchant protection against high conversion fees, currency fluctuation risks during refunds, accounting complexity, and increased fraud exposure.
