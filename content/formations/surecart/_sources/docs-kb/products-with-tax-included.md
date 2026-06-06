---
source_url: https://surecart.com/docs/products-with-tax-included
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Tax](https://surecart.com/docs-category/tax/)/How to Sell Products with the "Tax Included" Message

# How to Sell Products with the "Tax Included" Message

Selling the product with "tax included" simplifies the purchasing process, providing customers with a clear and straightforward understanding of the total cost, inclusive of taxes.

By incorporating taxes upfront, customers can see the total cost without encountering issues during checkout, making the whole shopping experience super easy.

Before we dive into the settings, let's better explain what Tax Included means.

### What "Tax Included" Means (with Reverse Charge Explained)

When you set your product price to "Tax included," the advertised price already contains any applicable tax (like VAT).

This means customers always see and pay the same total price, whether they are consumers or businesses.

**Example:**

- Product advertised at **$100 (tax-inclusive)**
- Consumer (B2C): pays **$100 total** → base $83.33 + $16.67 VAT
- Business (B2B with valid VAT number): still pays **$100 total** → base $100 + $0 VAT (reverse charge applies)

When a business enters a valid VAT number, the **reverse charge** mechanism applies.

That means:

- You don't charge VAT on the invoice.
- The buyer self-reports the VAT in their own tax return.
- The total price stays the same because the advertised amount already includes VAT.

This is the **standard legal practice** in most tax jurisdictions. Stripe, Shopify, and other major platforms behave the same way:

> "When set to inclusive, the amount your buyer pays remains constant, regardless of the tax amount (zero or positive)." — _Stripe Docs_

So, entering a VAT number doesn't provide a discount; it simply ensures the **correct tax treatment** (avoiding double taxation) rather than reducing the total.

Now, let's get started on the settings side.

- Before you follow these steps, ensure you have **Tax Collection** enabled on your SureCart Tax settings page.

- Enable the **Tax Included** option located just below the previous one.

- Click on the **Save** button to apply these changes.

Tax Included will be displayed for all products to which tax applies. Customers will see the text "Price includes $tax" during checkout, as well as in the order summary, receipts, and all relevant sections.

The type of tax collected depends on your region. For instance, VAT is applied to the above product because the provided address falls within the European region. You can [configure tax regions](https://surecart.com/docs/configure-tax-settings-in-surecart/) in your SureCart settings based on your location.

We hope this guide helped you. If you have any questions, please don't hesitate to contact our support team. We're here to help!

### **Frequently Asked Questions**

**Why doesn't entering my VAT number reduce my total?**

Because the price you see is **tax-inclusive**, which means it already includes any applicable tax.

When you enter a valid VAT number, **reverse charge** applies — you're not charged VAT, but the product price remains the same.

You handle VAT reporting on your side instead of paying it to the seller.

This ensures compliance with EU/UK rules and keeps pricing consistent for all customers.

**What's the difference between "Tax Inclusive" and "Tax Exclusive" pricing?**

**Tax inclusive** – the displayed price already includes VAT. The advertised price is the total you pay. This is required in many countries for consumer pricing.

**Tax exclusive** – the displayed price is **before tax**. VAT is added at checkout only if it is due.

If a store is set up with **tax-exclusive** pricing and the net is **€130.25**:

– A consumer would see **€130.25 + VAT** at checkout – total **€155**

– A VAT-registered buyer using reverse charge would see **€130.25** and **Tax €0**

**If tax is included in the price, how does SureCart calculate the tax amount?**

SureCart automatically calculates the embedded tax portion based on the customer's country and your tax settings.

For example, if you set a $100 tax-inclusive price with a 20% tax rate, the system treats the base as $83.33 and tax as $16.67.

If the customer is exempt or uses reverse charge, it simply sets the tax to $0 while keeping the $100 total.

**Can I show prices without tax for business customers?**

No, not when using tax-inclusive pricing. The law in most EU/UK markets requires the advertised price to include tax, even if businesses later reclaim it.

If you want to show pre-tax prices to business users, you can switch to **tax-exclusive** pricing in your tax settings instead.

**Does the reverse charge apply automatically?**

Yes. When a customer enters a valid VAT number from a different EU country, SureCart automatically applies the reverse charge, setting VAT to $0 and marking the invoice accordingly.

**Is this behavior the same across all payment gateways (Stripe, PayPal, etc.)?**

Yes. SureCart follows the same tax logic used by major platforms and gateways like Stripe and Shopify, ensuring consistent compliance and customer experience.
