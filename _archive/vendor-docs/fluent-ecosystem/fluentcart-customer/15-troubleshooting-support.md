# Section Troubleshooting & Support

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Troubleshooting & Support - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/troubleshooting-support/

[Skip to content](https://docs.fluentcart.com/guide/troubleshooting-support/#VPContent)

# Troubleshooting & Support [​](https://docs.fluentcart.com/guide/troubleshooting-support/\#troubleshooting-support)

The **Troubleshooting & Support** section in FluentCart is designed to help you resolve common issues, understand system logs, and find assistance when you encounter challenges. Our goal is to ensure you have a smooth and efficient experience running your online store.

This section provides resources and guides for:

- **[Understanding Logs](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs):** Learn how to interpret FluentCart's system logs to diagnose issues and track events.
- **[Common Issues & FAQs](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs):** Find solutions to frequently asked questions and common problems encountered by FluentCart users.
- **[How to Get Support](https://docs.fluentcart.com/guide/troubleshooting-support/how-to-get-support):** Information on how to reach out to the WPManageNinja support team for personalized assistance.

By utilizing these resources, you can quickly address many operational questions and keep your FluentCart store running optimally.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Common Issues & FAQs - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs

[Skip to content](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs#VPContent)

# Common Issues & FAQs [​](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs\#common-issues-faqs)

This section provides solutions to frequently encountered issues and answers to common questions about FluentCart. If you're experiencing a problem, check this guide first before reaching out for direct support.

## Frequently Asked Questions [​](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs\#frequently-asked-questions)

### Q: Why are my PayPal/Stripe payments not going through in Live mode? [​](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs\#q-why-are-my-paypal-stripe-payments-not-going-through-in-live-mode)

**A:**

- **Check API Credentials:** Ensure you have entered your **Live credentials** (API keys/secrets) correctly in **FluentCart Pro > Settings > Payment Settings > [Stripe Settings](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings)** or **[PayPal Settings](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paypal-settings)**.
- **Switch Order Mode to 'Live':** Make sure your FluentCart store's "Order Mode" is set to "Live" (this setting is typically found under **FluentCart Pro > Settings > Store Settings > Store Setup**). Payments will not process in Live mode if your store is still configured for "Test" mode.
- **Configure Webhooks (for Stripe):** For Stripe, it's critical that you have correctly configured the Webhook URL in your Stripe Dashboard as instructed in the [Stripe Settings](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings) documentation.

### Q: My digital product downloads are not working, or files are missing. [​](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs\#q-my-digital-product-downloads-are-not-working-or-files-are-missing)

**A:**

- **Verify Downloadable Assets:** In the **Product Edit** screen for your digital product, go to the "Downloadable Asset(s)" section and confirm that the correct files are uploaded or linked.
- **Check Storage Settings:** Ensure your [Storage Settings](https://docs.fluentcart.com/guide/settings-configuration/storage-settings) (Local or S3) are correctly configured and accessible. If using S3, verify your bucket credentials and permissions.
- **File Permissions:** On your server (for local storage), ensure the directories containing your digital files have the correct read/write permissions.

### Q: A customer can't access their license key or software updates. [​](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs\#q-a-customer-can-t-access-their-license-key-or-software-updates)

**A:**

- **Check Order Status:** Ensure the customer's order for the licensed product is marked as "Completed" and fully paid.
- **Verify License Status:** On the [License Details screen](https://docs.fluentcart.com/guide/product-types-creation/creating-digital-products-with-licenses#product-specific-license-settings) for that customer's license, ensure its status is "Active" and the "Activation Limit" has not been exceeded.
- **License Key Activation:** Guide the customer to activate their license key on their site if it's for a WordPress plugin, as outlined in the plugin's instructions.
- **FluentCart License Activation:** Ensure _your_ FluentCart plugin license is active in [FluentCart Pro > Settings > Licensing](https://docs.fluentcart.com/guide/settings-configuration/licensing-settings) to receive updates.

## General Troubleshooting Tips [​](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs\#general-troubleshooting-tips)

- **Check System Status:** Look for a "System Status" or "Health Check" tool within FluentCart (if available) or WordPress that can provide diagnostic information.
- **Deactivate Conflicts:** Temporarily deactivate other plugins one by one to check for conflicts that might be causing unexpected behavior.
- **Review Logs:** Utilize the [Understanding Logs](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs) guide to check for any related "Warning" or "Failed" entries.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## How to Get Support - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/troubleshooting-support/how-to-get-support

[Skip to content](https://docs.fluentcart.com/guide/troubleshooting-support/how-to-get-support#VPContent)

# How to Get Support [​](https://docs.fluentcart.com/guide/troubleshooting-support/how-to-get-support\#how-to-get-support)

If you've reviewed the [Docs & FAQs](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs) guides and still encountering a problem with FluentCart, our dedicated support team is here to help.

## How to Contact Support [​](https://docs.fluentcart.com/guide/troubleshooting-support/how-to-get-support\#how-to-contact-support)

To ensure you receive the quickest and most effective assistance, please follow these guidelines when contacting us:

1. **Visit the FluentCart Support Portal:** Go to the official FluentCart website. This is the primary channel for submitting support tickets.

   - [FluentCart Account](https://fluentcart.com/account/)
2. **Submit a Support Ticket:**

   - Log in to your FlunetCart account.
   - Navigate to the "Support Tickets" section.
   - Click on "Create Ticket."
3. **Provide Detailed Information:** When submitting your ticket, please include as much detail as possible. This helps our team understand your issue quickly and provide a precise solution. Include:

   - **A Clear Description of the Problem:** Explain what you are trying to achieve and what is happening instead.
   - **Steps to Reproduce:** List the exact steps you take that lead to the issue.
   - **Screenshots or Screen Recordings:** Visual aids are incredibly helpful for diagnosing problems.
   - **Error Messages:** If you see any error messages on your screen or in your WordPress debug log, copy and paste them.
   - **Relevant Log Entries:** Check your FluentCart [Logs](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs) screen for any "Warning" or "Failed" entries related to the issue and include them.
   - **Your WordPress Version.**
   - **Your FluentCart Plugin Version.**
   - **Any Other Plugins Active on Your Site:** List them, especially if they are related to e-commerce, payments, or forms.
4. **Support Hours:** Our support team operates during business hours, typically Monday to Friday. We strive to respond to all inquiries as quickly as possible.


We are committed to helping you succeed with FluentCart!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Understanding Logs - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs

[Skip to content](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs#VPContent)

# Understanding Logs [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#understanding-logs)

Think of the **Logs** screen as the diary for your store. It keeps a detailed record of every important event and action that happens, like when an order is paid or a setting is updated. This is an essential tool for keeping an eye on your store's operations and for figuring out what happened if something ever goes wrong.

## Accessing the Logs [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#accessing-the-logs)

1. From your WordPress dashboard, navigate to **FluentCart Pro > Logs** in the left sidebar.
2. This will open the **Logs** screen, displaying a detailed table of all recorded events.

## Understanding the Logs List Table [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#understanding-the-logs-list-table)

The Logs list table presents key information for each event entry:

- **ID:** A unique identification number for each log entry.

- **Date & Title:** The date and time when the event occurred, along along with a brief title describing the action.

- **Content:** A detailed description of the event that took place.

- **Status:** The outcome or severity of the action.

- **Module:** The FluentCart module or area from which the action originated.

- **Actions:** For many log entries, particularly those related to orders, a **"View Order"** link is provided. Clicking this link will navigate you directly to the [Order Details screen](https://docs.fluentcart.com/guide/store-management/orders-management/order-details-overview) for that specific transaction.

![Screenshot of Logs List Page](https://docs.fluentcart.com/images/troubleshooting-support/understanding-logs/Logs.webp)


## Filtering Logs [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#filtering-logs)

If you are looking for a specific event, you can easily filter the log entries to narrow down your search.

### Filtering by Status Tabs [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#filtering-by-status-tabs)

At the top of the logs screen, you will find several tabs to filter by the most common statuses:

- **All:** Displays every log entry.
- **Success:** Shows only successfully completed actions.
- **Warning:** Filters for entries that indicate a minor issue.
- **Error:** Shows only entries that are reporting an error

### Using 'More Views' [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#using-more-views)

For more specific filters, click the **More views** dropdown menu. Here you will find these options:

- **Failed:** Shows only actions that resulted in a failure.
- **Info:** Displays informational messages that aren't errors or successes.
- **API Only:** Narrows the list to only show events related to API interactions.

## Using Logs for Troubleshooting [​](https://docs.fluentcart.com/guide/troubleshooting-support/understanding-logs\#using-logs-for-troubleshooting)

- **Diagnosing Errors:** If you encounter unexpected behavior or errors in your store, checking the "Failed" or "Warning" log types can help identify the root cause.
- **Auditing Changes:** The "Success" logs keep a record of all successful actions. This is helpful for audits or seeing who did what and when.
- **Tracking Workflows:** By reviewing the sequence of events in the log, you can understand how certain processes (like order fulfillment or refunds) unfolded.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
