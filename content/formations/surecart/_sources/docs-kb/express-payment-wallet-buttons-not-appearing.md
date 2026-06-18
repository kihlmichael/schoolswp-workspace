---
source_url: https://surecart.com/docs/express-payment-wallet-buttons-not-appearing
source: surecart-kb
scraped: true
---

# Express Payment (Wallet) Buttons Not Appearing

## Overview

Express payments in SureCart offer quick and secure payment options like Apple Pay and Google Pay, enabling users to complete transactions with minimal steps using stored information.

## Enabling the Express Payment Block

The Express Payment block has been removed from SureCart's standard block list as it is now deprecated. To add it manually, use a PHP snippet via your theme's functions.php or a code snippets plugin that registers the block with the inserter enabled.

**Note:** Since this is deprecated, usage occurs at your own discretion without active support.

## Adding the Express Payment Block

1. Navigate to **Custom Forms** in your WordPress dashboard
2. Select the form where you want to enable express payments
3. Click the **+** icon to add a block
4. Search for and select **Express Payment**
5. Users will now see wallet buttons compatible with their browser

## Why Buttons Are Not Appearing

These buttons only appear on their supported browsers and devices. If wallet buttons are not visible, the issue likely stems from browser compatibility:

- **Apple Pay** appears in Safari
- **Google Pay** appears in Chrome
- Other wallets depend on specific browser support

Ensure you are using a supported browser for the specific wallet button you expect to see.

For additional assistance, contact SureCart support.
