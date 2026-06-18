---
source_url: https://surecart.com/docs/connect-razorpay
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect Razorpay Payment Processor

# How to Connect Razorpay Payment Processor

This document explains how to connect Razorpay with SureCart so you can start accepting payments from your customers.

Razorpay is a popular payment processor in India that supports payments via cards, net banking, wallets, and UPI. SureCart connects to Razorpay using a secure authorization flow — no manual API keys or webhook configuration is required.

**Important:** Razorpay requires merchants to add and verify their Business Website URL in the Razorpay dashboard to process Live payments. If this URL is missing or does not match the checkout domain, Razorpay will block Live payments.

**OAuth limitation:** The connection works only if you are already logged into your Razorpay account in the same browser before connecting it to SureCart.

**Subscriptions:** To sell subscription products using Razorpay, your account must have Recurring Payments (Subscriptions) enabled by Razorpay.

## Requirements

- WordPress admin access
- SureCart installed and activated
- At least one published product
- An active Razorpay account
- Access to **SureCart → Settings → Payment Processors**

## How to Connect Razorpay in Test Mode

1. Go to **WordPress Dashboard → SureCart → Settings → Payment Processors**.
2. Locate **Razorpay** and click it.
3. Make sure you are already logged into your Razorpay account in the same browser.
4. Click the **Connect** button and select **Test Mode**.
5. You will be redirected to Razorpay — review permissions and click **Authorize**.
6. You will be redirected back to SureCart with a success message. The Razorpay account status will show as **Enabled** (Test mode).

## How to Connect Razorpay in Live Mode

The process is the same, with one important difference: select **Live Mode** when clicking Connect.

Before testing Live payments, make sure your Business Website URL is added and approved in your Razorpay account.

## Business Website URL Requirement for Live Payments

If the Business Website URL is missing or does not match the checkout domain, Razorpay will block Live payments with the error: "Payment blocked as website does not match registered website(s)."

This requirement applies **only to Live mode**. Test Mode payments are **not affected**.

## Notes, Limitations, and Edge Cases

- Razorpay requires **Indian Rupee (INR)** as the checkout currency.
- Razorpay requires a **customer phone number** to process payments. SureCart automatically adds a Phone field to the checkout form when Razorpay is enabled.
- Test Mode and Live Mode must be connected **separately**.
- Subscription payments require **Recurring Payments** to be enabled in the Razorpay account.
