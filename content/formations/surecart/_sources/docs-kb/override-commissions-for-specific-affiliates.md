---
source_url: https://surecart.com/docs/override-commissions-for-specific-affiliates
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Affiliate Platform (for merchants)](https://surecart.com/docs-category/affiliates-for-merchants/)/How to Override Commission Amounts for Certain Affiliates

# How to Override Commission Amounts for Certain Affiliates

This document explains how to override commission amounts for specific affiliates in SureCart, including standard, subscription, lifetime, and product-specific commissions.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An active affiliate program
- At least one affiliate created

### Commission Types Overview

SureCart supports the following commission types:

- **Commission rate** – The amount an affiliate earns for each successful referral.
- **Subscription commission** – The amount an affiliate earns when a referred customer renews a subscription.
- **Lifetime commission** – The amount an affiliate earns from all future purchases made by a referred customer.

These commissions can be overridden for individual affiliates and, optionally, limited by duration.

### **Provide Custom Commissions to a Specific Affiliate**

Follow the steps below to override commission amounts for a single affiliate.

- Go to **WordPress Dashboard → SureCart → Affiliates**.
- Select the affiliate you want to configure.
- Under **Custom Commission**, click **Add Commission**.

### **Set a Custom Commission Amount**

- Choose the commission type (percentage or flat rate).
- Enter the custom commission amount.
- Click **Save**.

Once saved, the selected affiliate will receive the custom commission amount, while other affiliates continue using the default commission settings.

### **Set Custom Subscription Commissions and Duration**

You can configure subscription commissions for specific affiliates.

- Enable **Subscription Commissions**.
- Enter the number of days the affiliate should receive commissions for subscription renewals.
  - Leave this field empty to pay commissions indefinitely.
- Click **Save**.

### **Set Custom Lifetime Commissions and Duration**

Lifetime commissions can also be overridden per affiliate.

- Enable **Lifetime Commissions**.
- Enter the duration for how long commissions should be paid.
  - Leave this field empty to allow lifetime commissions indefinitely.
- Click **Save**.

### **Set Product-Specific Affiliate Commissions**

Product-specific commissions allow affiliates to earn different amounts for specific products.

- Under **Product Commissions**, click **Add Commission**.
- Select the product you want to override commissions for.
- Enter the custom commission amount.
- Enable **Subscription Commissions** if the product uses subscriptions.
- Enable **Lifetime Commissions** if commissions should apply to future purchases.
- Click **Create**.

The configured product commission will appear in the **Product Commissions** list for that affiliate.

### Expected Outcome

After completing these steps, selected affiliates will receive custom commission amounts based on your configuration. Overrides apply only to the affiliates and products specified.

### Notes and Limitations

- Custom commissions override global affiliate commission settings.
- Leaving duration fields empty enables commissions indefinitely.
- Product-specific commissions take precedence over general affiliate commissions.

### **FAQ**

**Do custom commissions affect other affiliates?**

No. Custom commissions apply only to the selected affiliate.

**Do commission changes affect past orders?**

No. Changes apply only to new referrals and future purchases.

**Which commission is applied if multiple rules exist?**

Product-specific commissions take precedence over affiliate-level and global commission settings.
