# SureCart - Base de connaissances (partie 1 sur 4)


===== SOURCE: abandoned-checkout.md =====

---
source_url: https://surecart.com/docs/abandoned-checkout
source: surecart-kb
scraped: true
---

# How to Set Up Abandoned Checkout - SureCart

## Overview

An abandoned checkout occurs when customers begin purchasing but don't complete the transaction. SureCart marks checkouts as abandoned after 30 minutes if the customer provided their email address, enabling follow-up communications to recover lost sales.

## Setup Steps

1. **Access Settings**: Navigate to your SureCart dashboard and select "Settings"
2. **Find Abandoned Checkout**: Locate the "Abandoned Checkout" section in the settings menu
3. **Enable Feature**: Toggle the "Enabled" switch to activate abandoned checkout functionality
4. **Set First Email Delay**: Choose when to send the initial reminder (default is 1 hour)
5. **Configure Second Email**: Select timing for the second message (example: 3 hours)
6. **Set Final Email Delay**: Choose when to send the last reminder, or select "Don't send" to disable it
7. **Save Changes**: Click "Save" to apply your configuration

## Adding Discount Codes

To incentivize returns:

1. Enable "Abandoned Checkout Discount" toggle
2. Configure discount type (fixed amount or percentage)
3. Select which email should include the discount code
4. Save your settings

Auto-generated unique discount codes will accompany notification emails, encouraging customers to complete purchases.

## Advanced Options

- **Test Mode**: Validate functionality before going live
- **Ignore Purchased Products**: Skip abandoned carts containing already-purchased items
- **Grace Period**: Set a waiting period before sending initial reminders


===== SOURCE: add-checkout-form.md =====

---
source_url: https://surecart.com/docs/add-checkout-form
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Add a New Checkout Form

# How to Add a New Checkout Form

This document explains how to create a new checkout form in SureCart, allowing you to select the products you want to sell and share a direct checkout link with customers.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- At least one published product

### **Create a New Checkout Form**

Follow the steps below to create a new checkout form.

- Go to **WordPress Dashboard → SureCart → Forms**.
- Click **Add New**.
- Enter a title for the checkout form.
- Select a starting design from the available checkout templates.
- Click **Next** to continue.

### **Add Products to the Checkout Form**

After selecting a design, add the products you want to sell through this checkout form.

- Click **Add Product**.
- Select the product you want to include.

If you add multiple products, configure the **Product Options** behavior:

- **Customer must purchase all options** — Forces customers to buy all listed products.
- **Customer must select one of the options** — Allows customers to choose only one product.
- **Customer can select multiple options** — Allows customers to select more than one product.

These settings control how customers interact with multiple products on the same checkout form.

### **Configure Cart Persistence (Optional)**

You can enable cart persistence to retain selected products as users navigate your site.

- Locate the **Form Cart** settings.
- Enable **Persist Across Pages**.

When enabled, selected products remain in the cart even if the customer navigates to other pages or returns later.

### **Publish the Checkout Form**

Once your checkout form is configured:

- Review the form settings.
- Click **Publish**.

The checkout form will now appear in the Forms list and can be shared with customers.

### **Expected Outcome**

After completing these steps, a new checkout form will be available with the selected products, design, and cart behavior, allowing customers to complete purchases directly through the form.

### **Notes and Limitations**

- Changes to a checkout form affect only future checkouts.
- Each checkout form can have its own design and product selection.
- Cart persistence applies only when the **Persist Across Pages** option is enabled.

### **FAQ**

**Can I create multiple checkout forms?**

Yes. You can create as many checkout forms as needed, each with different products and designs.

**Can I change the products after publishing the form?**

Yes. Checkout forms can be edited and updated at any time.

**Does cart persistence work across browser sessions?**

Yes. When enabled, selected products remain available even if the customer leaves and returns later.


===== SOURCE: add-custom-css.md =====

---
source_url: https://surecart.com/docs/add-custom-css
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/How to Add Custom CSS to Checkout Forms

# How to Add Custom CSS to Checkout Forms

It is a common practice to modify specific parts of a website using custom CSS during the website building process. There are a number of reasons why you might want to add custom CSS to your website:

- To match the overall design of your website or storefront.
- To customize an element that can't be customized without CSS.
- Or to simply change the font color or typography on a specific area of your website.

Integrating custom CSS into your SureCart checkout forms allows you to provide a better user experience and maintain branding consistency on your website. This results in a more professional and user-friendly experience.

This documentation provides a step-by-step guide on adding custom CSS to SureCart checkout forms, including various examples to make this process more understandable.

### **What Is a Shadow DOM?**

Before we learn how to add CSS to checkout forms, we should know how SureCart uses CSS.

SureCart uses a Shadow DOM to load the CSS. It is a way to encapsulate CSS and HTML in a separate tree from the main document. This method provides a few advantages:

- **Style protection**: Styles are protected from any potential style conflicts with theme or plugin styles.
- **Future-proofing**: If the internal HTML structure of any components changes, you won't need to update any custom CSS.

In the case of SureCart checkout forms, the shadow DOM is used to isolate the checkout form styles from the rest of your website's styles.

This means that you can add custom CSS to the checkout form without having to worry about conflicting with other styles on your website.

To add custom CSS to SureCart checkout forms, we will use CSS custom properties, also known as CSS variables.

### **How to Add CSS**

To work well with CSS customization, it's important to know about two important things: [dev tools](https://developer.chrome.com/docs/devtools/) and [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php).

If you're not familiar with them, you can find helpful explanations and tutorials on various websites. It's worth checking them to get a better understanding.

Making a CSS modification consists of 3 steps.

1\. **Getting the CSS selector** – when customizing elements with a normal CSS customization you need to find a selector and add styles. In most cases it is enough to get the ID or class of the HTML element.

When using the Shadow DOM method, we must locate a CSS variable of the element.

Shadow Dom doesn't use a selector, it has only one selector, and it looks like this:

```
:root:root {

}
```

In this simple CSS code, we will add CSS variables with customized values.

2\. **Generating CSS code** – In a normal CSS customization we need a CSS selector and rules of styles, at the end your CSS code will look like this:

```
.selector {
  Color: red;
  Font-family: Noto Sans;
}
```

We have a different approach in the Shadow DOM method, we need to get CSS variables and modify them, for example if we want to change the font size, then this will be our css:

```
:root:root {
  --sc-input-label-font-size-medium: 25px;
}
```

This means in the Shadow Dom method we only need to get CSS variable since the selector is always the same.

You can refer to this [Custom CSS](https://developer.surecart.com/docs/styling-ui) article for more information on variables. This doc page contains a list of all the variables used in SureCart and their default values.

3\. **Adding the code** – This is the easiest part, we need to save our code in the appropriate place to apply changes. By default in WordPress we save CSS customizations in Appearance > Customize > Additional CSS.

By following these 3 steps, we can modify not only the checkout form but also the shop page, product page, and Customer Dashboard page. This method of CSS modification applies to all of them.

### **Examples**

So far, we have covered the theory of CSS customization. Now, let's get practical and strengthen our knowledge through several examples of CSS customization.

In the examples below, we will follow these steps, we will identify a CSS variable, then create a code, and lastly, we will add it to the CSS box.

#### **Typography**

In this example let's discuss how can we change the typography on the checkout form with custom css.

Here is our CSS that will change font family, font size, and font weight.

```
:root:root {
  --sc-font-sans: fuggles;
  --sc-font-size-medium: 25px;
  --sc-font-weight-normal: 600;
}
```

For better presentation, we are loading Google Fonts with this css code:

```
@import url('https://fonts.googleapis.com/css2?family=Inconsolata:wght@600&display=swap');
```

#### **Change border-radius**

Now, let's imagine we want to change the border radius and border color of the input fields on the checkout page.

```
:root:root {
  --sc-border-radius-medium: 30px;
  --sc-input-border-color: red;
  --sc-select-border-color:red;
}
```

###### Note:

With SureCart v3, we have fully adapted with WordPress' Interactivity API. Meaning we no longer use ShadowDOM on most SureCart pages and sections, except the Checkout Forms and Pages.

These pages still use ShadowDOM.

Please refer to our [**upgrade guide**](https://surecart.com/docs/upgrading-to-surecart-v3/) to learn more about SureCart v3.

And that's the end!

Don't worry if it looked a bit complicated at first. In reality, it's often easier than the usual CSS approach. All you really need to do is to get CSS variables to change default values.

I hope this guide has made it clear how to add your own custom styles to your checkout forms. With this knowledge, you can make your SureCart checkout pages look and style just the way you want them to.


===== SOURCE: add-custom-fields-to-customer-invoices.md =====

---
source_url: https://surecart.com/docs/add-custom-fields-to-customer-invoices
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Uncategorized](https://surecart.com/docs-category/uncategorized/)/How to Add Custom Fields to Customer Invoices

# How to Add Custom Fields to Customer Invoices

This guide will help you add custom fields, such as a company registration number or tax number, to your customer invoices in SureCart. Follow these steps to capture the data at checkout and display it on future invoices.

### **How Can You Add Custom Fields at Checkout?**

To add custom fields, follow these steps:

1. **Edit the Checkout Form**:

- Go to your checkout form in SureCart and add a Conditional block.
- Insert a TextField or other suitable fields for the additional information you need to capture from customers.
- These will be displayed during checkout for customers to fill in.

**2. Store Data as Metadata:**

- The custom fields will be stored as metadata on the checkout object. For example, with keys like `invoice_column_1` and `invoice_column_2`.

### **How Can You Display Custom Fields on Invoices?**

1. **Access the Invoice Template**:
   - Navigate to the invoice template editor at [SureCart Invoice Template](https://app.surecart.com/order_statement_template/edit).

2. **Use Metadata in the Template**:
   - To display the metadata, include the following pattern where you'd like the custom fields to appear, using `checkout.metadata.your_key_name` syntax.

   - This will display the values entered by the customer at checkout on their invoice.

**Important Notes:**

- **Placeholder Keys**: The provided keys are placeholders used for demonstration purposes. You must replace these with the actual keys corresponding to the custom fields you've configured in your setup.
- **Custom Field Setup**: Ensure that the custom fields you want to display are properly set up and added to the invoice metadata.
- **Validation**: Test the output on your invoices to confirm that the correct data appears in the desired format.

### **What About Existing Subscriptions?**

For customers who already have active subscriptions and did not fill in these custom fields, here are your options:

- **Manual Update**: You can manually update the customer information using SureCart's API. Head to [SureCart API Reference](https://developer.surecart.com/reference/update_checkout) to update the metadata for existing customers.
- **Customer Dashboard**: You could also allow customers to update their information directly through their dashboard. This feature may require custom development, as there's no UI for metadata updates at this time.

### **How Can You Manually Add Data via API?**

If you need to update customer metadata manually, follow these steps:

1. **Get Authorization**: Include your secret token in the Authorization field.
2. **Provide Checkout ID**: Add the appropriate checkout ID for the customer.
3. **Add Metadata**: In the request body, include the metadata fields that need updating.
4. **Submit**: Hit "Try it" in the API console to save your changes.

For more details, check the SureCart API documentation [here](https://developer.surecart.com/reference/update_checkout).

We hope this guide helps you add custom fields to your invoices and manage customer data seamlessly. If you run into any issues, feel free to leave a comment below, and we'll be happy to assist you further!


===== SOURCE: add-first-time-subscription-discounts.md =====

---
source_url: https://surecart.com/docs/add-first-time-subscription-discounts
source: surecart-kb
scraped: true
---

# Add First-Time Payment Discounts in SureCart Subscriptions

## Overview

SureCart enables merchants to offer special discounts exclusively on the first subscription payment. They are a way to apply a special discount to the first subscription payment from a customer. The next payment made by the customer is the normal amount.

## Setup Instructions

1. **Navigate to Products**: Access the SureCart Products section from your WordPress dashboard

2. **Select a Product**: Choose the product where you want to enable this feature

3. **Enable the Toggle**: Activate the "Setup fees or discount" toggle button for your desired subscription plan

4. **Choose Discount**: Select "Discount" from the dropdown menu that appears

5. **Configure Discount Details**: Enter a discount name and specify the discount amount you wish to offer

6. **Save Changes**: Click the "Save Product" button to apply your changes

## Customer Experience

Once configured, customers will see the reduced price during checkout for their initial purchase. Subsequent renewal payments will reflect the regular subscription price.

## Removal

To disable this offer, simply toggle off the "Setup fees or discount" button.


===== SOURCE: add-surecart-api.md =====

---
source_url: https://surecart.com/docs/add-surecart-api
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/Connecting – How to Add Your SureCart API Token

# Connecting – How to Add Your SureCart API Token

This document explains how to connect the SureCart plugin to a store account using an API token.

##### Requirements

- A SureCart store account
- SureCart plugin installed and activated
- WordPress admin access

##### Step 1: Navigate to the API Section

Go to App.surecart.com → Click **API** in the sidebar menu.

Select the **Secret Token** tab.

##### Step 2: Copy the API Token

Copy the API token displayed on the screen.

**Important:** Store this token securely. It provides access to the store and should not be shared publicly.

##### Step 3: Add the Token to WordPress

Open your WordPress site.

Go to WordPress Dashboard → SureCart → Settings → Connection.

Paste the API token into the **API Token** field.

Click **Save**.

Expected Outcome

Once the token is saved, the SureCart plugin will be connected to the store account. The connection status will display as "Connected" in the Settings area.

##### FAQ

**What happens if I delete my API token?**

Deleting the token will immediately disconnect all sites currently using the token. The new token must be manually added to each WordPress installation to restore the connection.

**Can I use the same API token on multiple WordPress sites?**

Yes. The same API token can be used to connect multiple WordPress installations to the same SureCart store.

**What should I do if my site shows as disconnected?**

This typically occurs when the API token has been removed. Navigate to WordPress Dashboard → SureCart → Settings → Connection, and re-enter the current API token from the SureCart cloud platform.


===== SOURCE: add-thank-you-page-url.md =====

---
source_url: https://surecart.com/docs/add-thank-you-page-url
source: surecart-kb
scraped: true
---

# How to Add a Custom Thank You Page URL in Instant Checkout - SureCart

## Overview

SureCart's Instant Checkout feature allows you to create unique checkout links for products and share them broadly. The platform also enables you to redirect customers to a custom thank you page following successful purchases.

**Important Note:** This feature differs from setting up a thank you page for standard checkout forms — it's specifically designed for instant checkouts.

## Steps to Add a Custom Thank You Page URL

### Step 1: Access Your Product

Navigate to **Products** in your WordPress dashboard and select the product where you want to add the thank you page.

### Step 2: Enable Custom Thank You Page

Click on **Instant Checkout** and toggle on the **Custom thank you page** button.

### Step 3: Enter Your URL

Input your thank you page's URL in the provided field.

### Step 4: Save Changes

Click the **Save Product** button to apply your changes.

## Result

Once configured, customers will be automatically redirected to your selected thank you page immediately after completing their purchase through the instant checkout link.


===== SOURCE: add-tracking-number.md =====

---
source_url: https://surecart.com/docs/add-tracking-number
source: surecart-kb
scraped: true
---

# How to Add Tracking Number to an Order - SureCart

## For Store Owners

**Steps to add tracking numbers:**

1. Navigate to the Orders page and locate the unfulfilled order
2. Click the Order ID to open the View Order page
3. Select "Fulfill Item" to open the right-side flyout menu
4. Choose which items to fulfill
5. Enter the tracking number and tracking link
6. Add multiple tracking numbers if items ship separately
7. Reference the provided shipping address for fulfillment
8. Click "Fulfill Item" to finalize - order status changes to "Fulfilled"

**Order status progression:**
Orders can transition from "Not Shipped" to "Shipped" to "Delivered" as products move toward customers.

**Additional actions:**
Store owners can click the Actions button in the top-right corner to "Mark as Paid" once payment is received.

## For Customers

Customers can track their orders through the Customer Dashboard:

- View order fulfillment and shipping status
- Click on shipped orders to access the Order Details page
- Access tracking numbers and links for real-time package monitoring


===== SOURCE: adding-shipping-methods-and-rates.md =====

---
source_url: https://surecart.com/docs/adding-shipping-methods-and-rates
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/Adding Shipping Methods and Rates

# Adding Shipping Methods and Rates

SureCart allows you to provide customers with shipping choices like Expedited, Express, same-day delivery, and more. Check out our guide on [adding and managing shipping methods and rates](https://surecart.com/docs/shipping-zone-methods-rates/) for more details.


===== SOURCE: adding-terms-conditions-in-checkout.md =====

---
source_url: https://surecart.com/docs/adding-terms-conditions-in-checkout
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/Adding Terms & Conditions to Your Checkout Form in SureCart

# Adding Terms & Conditions to Your Checkout Form in SureCart

This document explains how to add a Terms & Conditions checkbox to a SureCart checkout form, requiring customers to agree before completing their purchase.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **How to Add a Terms & Conditions Checkbox**

Follow the steps below to add a Terms & Conditions checkbox to your checkout form.

- Go to WordPress Dashboard → SureCart → Checkout Forms.
- Open the checkout form you want to edit.
- Insert a **Checkbox** block where you want the Terms & Conditions option to appear.
- Select the checkbox block.
- In the block settings panel on the right, enable the **Required** option.

Once enabled, customers will not be able to complete the checkout unless the checkbox is selected.

### **Customize the Checkbox Label**

You can customize the text displayed next to the checkbox.

- Double-click the checkbox label.
- Enter the text you want customers to see (for example, "I agree to the Terms & Conditions").

The checkbox label and value are saved with the order, creating a record of the customer's agreement.

### **Optional: Set the Checkbox as Checked by Default**

If needed, the checkbox can be pre-selected.

- Select the checkbox block.
- Enable the **Checked by default** option.

When enabled, the checkbox will be selected automatically when the checkout loads.

### **How to Link Your Terms & Conditions Page**

You can link the checkbox text to your Terms & Conditions page so customers can review it before agreeing.

- Select the text next to the checkbox.
- Click the **Link** icon in the toolbar.
- Enter the URL of your Terms & Conditions page.
  - Alternatively, use **Ctrl + K** to insert the link.
- Click **Update** to save your changes.

### **Expected Outcome**

After completing these steps, the checkout form will display a Terms & Conditions checkbox. Customers must agree to the terms before completing their purchase.

### Notes and Limitations

- The checkbox value is stored with the order for reference.
- If the checkbox is marked as required, checkout cannot be completed unless it is selected.

### **FAQ**

**What happens if the Terms & Conditions checkbox is not checked?**

If the checkbox is marked as required, the customer will not be able to complete the checkout until it is selected.

**Can I change the checkbox text after publishing the checkout?**

Yes. Updating the checkbox label affects future checkouts and does not modify existing orders.


===== SOURCE: affiliate-program.md =====

---
source_url: https://surecart.com/docs/affiliate-program
source: surecart-kb
scraped: true
---

# Affiliate Program

The SureCart Affiliate Program allows you to earn commissions by referring customers to SureCart. This documentation provides clear instructions on how to become an affiliate, access your referral tools, and understand the commission structure.

### **What is the Affiliate Program?**

The SureCart Affiliate Program allows individuals and organizations to earn commissions by referring customers to SureCart.

As an affiliate, you promote SureCart's services using unique referral links and earn a percentage of the transaction volume generated from your referrals.

This program is designed for content creators, business owners, tech reviewers, and others interested in partnering with SureCart.

### **How to Join the Affiliate Program**

1. **Sign Up for the Program**: Navigate to the SureCart Affiliate Signup Page. Complete the registration form with your details and accept the program terms.

2. **Access Your Referral URL**: After approval, log in to your affiliate portal. Navigate to Settings and locate your unique referral URL under the Referral URL section. SureCart automatically generates this URL for you.

3. **Start Promoting SureCart**: Share your referral URL through your website, email campaigns, social media channels, or other platforms. Highlight SureCart's key benefits to attract potential customers.

4. **Track Your Earnings**: Use the affiliate dashboard to monitor your referrals, clicks, and commissions. Commissions are paid monthly via PayPal, provided your earnings meet the $200 minimum payout threshold.

### **Earnings and Payouts**

Both the Agency and Affiliate programs use the same tier structure. For a full breakdown of program tiers, benefits, and requirements, see the SureCart Partner Program Tiers documentation.

### **How Commissions Are Calculated**

Commissions are based on two components: Plan Sales and Platform Fees, both tied to your partner tier (Bronze, Silver, Gold, or Platinum).

**Plan Sales**: Plan sales commissions are earned on the subscription transaction volume from referred customers. The percentage earned is determined by your partner tier.

Example: If a customer referred by you purchases the SureCart Scale Plan for $59/month, and your tier is Silver (30%), you will earn a commission of $17.70/month as long as the plan remains active.

**Platform Fees**: Platform fees refer **only** to the **1.9% fee collected on the Launch plan** for store transactions. Affiliates earn a percentage of this fee based on their partner tier. **Subscription fees are not included** in the commission calculation.

Example: If a referred customer processes $1,000 in transactions in a month on the Launch plan, the 1.9% platform fee totals **$19.00**. Your commission at the Gold tier (35%) would amount to **$6.65** (35% of $19.00).

### **Payout Schedule**

Commissions are paid monthly during the third week of each month for referrals that occurred over 45 days ago. The minimum payout threshold is $200 USD and at least two referrals.

**Note**: Referral URLs track clicks for 30 days and attribute referrals to the last click. You can view your current partner tier and commission rate in the affiliate portal under Settings > Partner Tier.


===== SOURCE: agency-program.md =====

---
source_url: https://surecart.com/docs/agency-program
source: surecart-kb
scraped: true
---

# Agency Partner Program

In this guide we will walk through all the things you need to know about the SureCart agency partner program and how to create a new transaction volume using it.

### **What is the Agency Partner Program?**

The Agency Partner Program is a partnership between SureCart and your organization. In this partnership, you can earn money in three different ways:

- Agency Commission
- Referral Commission
- Platform Commission

#### **Agency Commission**

Agency commissions are a percentage you earn on every sale made by stores that fall under your agency's management. You determine the agency commission percentage for each store.

**Example**: If you set an agency commission rate of 2% for Store XYZ, and Store XYZ sells a product for $100, your organization will receive a $2 commission.

#### **Referral Commission**

Referral commissions are credited when your agency creates a store for a client and subsequently transfers ownership to that client.

No affiliate link or referral code is involved in this process; commissions only apply if you initiate the store setup for a client, and the client then upgrades to a paid plan.

**Example**: If your agency creates and transfers a store to a client, and the client purchases a SureCart Lifetime Pro Plan (e.g., $499), your agency will receive the referral commission based on your agency tier (e.g., 30% of $499 if you're at the Silver tier).

#### **Platform Commission**

Platform commissions are generated **only from the 1.9% platform fee collected on the Launch plan** for stores under your management. Subscription fees are **not included** when calculating this commission.

**Example**: If a store under your organization sells a subscription product for $100/month on the Launch plan, the 1.9% platform fee equals **$1.90**. Your agency (at the Silver tier, 30%) would receive **$0.57** in commission from that platform fee.

### **About Agency Tiers**

Both the Agency and Affiliate programs use the same tier structure. For a full breakdown of program tiers, benefits, and requirements, see the SureCart Partner Program Tiers documentation.

### **Joining the Agency Partner Program**

To join the Agency Partner Program:

- Go to the application form URL to access the agency application form.
- Fill out: Agency Name, Agency Email, Agency URL, Agency Bio.
- Click Apply Now to submit your application.

After submitting the form, the SureCart team will review your application. If approved, you will receive a notification by email.

Once your application is approved, you can log in and access your agency dashboard with an overview of:

- Agency Commission: Earnings from sales by stores you manage.
- Referral Commission: Earnings from transferring newly created stores to client accounts.
- Platform Commission: Earnings from platform-related extras such as subscriptions, upsells, and more.
- Payouts: Overview of your total earnings.

### **How to Receive Your Payouts for the Agency Program**

To receive your earnings, add your payout email:

- Go to the **Settings** menu in your SureCart dashboard.
- Under **Payout Details**, enter the email address where you would like to receive your payouts. This email will be used for payments via PayPal, bank transfer, etc.
- Click **Save** to update your payout information.

#### **Payout Process**

- SureCart issues payouts monthly, using your designated payout email.
- Payments are processed during the third week of each month.
- Earnings must be at least 45 days old at the time of payout.

### **Setting Up the Agency Commission**

To configure the agency commission for a client website that you manage:

- Click the dropdown with your agency name in the top left corner of your screen.
- Select the store where you want to apply the agency commission.
- Once you are on the selected store, click on **Settings**, then click on **General**.
- In the **Agency Commission** section, enter the desired agency commission percentage and click **Save** to apply your changes.


===== SOURCE: all-shortcodes.md =====

---
source_url: https://surecart.com/docs/all-shortcodes
source: surecart-kb
scraped: true
---

# SureCart List Of All Shortcodes

## What is a Shortcode?

A shortcode is a simple and abbreviated code enclosed in square brackets. Shortcodes allow you to add dynamic content to posts, pages, or widgets without writing complex code.

## How to Use Shortcodes

1. Copy the desired shortcode
2. Add any parameters you want (optional)
3. Paste it into your post, page, or widget content
4. Save and view the front end to see the result

**Important Note:** The ID parameter does not work in SureCart version 3 and above due to the WordPress Interactivity API requirement.

## Available Shortcodes

### Shop Page

**sc_product_list** — Display products in a grid format

Parameters: columns, limit, pagination_enabled, ajax_pagination, pagination_auto_scroll, type, search_enabled, sort_enabled, ids, collection_enabled

### Product Page Shortcodes

**sc_product_title** — Display product title (requires id parameter)

**sc_product_description** — Display product description (requires id parameter)

**sc_product_price** — Display currently selected price (supports id and sale_text parameters)

**sc_product_variant_choices** — Display variant options (requires id parameter)

**sc_product_price_choices** — Show pricing options (supports id, label, columns, show_price)

**sc_product_media** — Display product images/slideshow (supports id, auto_height, height, width, thumbnails_per_page)

**sc_product_quantity** — Show quantity selector (supports id, label)

**sc_product_cart_button** — Add to cart or buy now button (supports id, text, add_to_cart)

### Checkout Forms

**sc_form** — Display checkout form (requires id parameter). Example: id=123

### Cart Menu Icon

**sc_cart_menu_icon** — Display cart icon (supports cart_icon, cart_menu_always_shown)

### Customer Dashboard

**sc_customer_dashboard_button** — Add dashboard button (supports label parameter)

**sc_customer_dashboard_page** — Wrapper for all dashboard components

**sc_customer_orders** — Show orders section (supports title parameter)

**sc_customer_subscriptions** — Show subscriptions section (supports title parameter)

**sc_customer_downloads** — Show downloads section (supports title parameter)

**sc_customer_payment_methods** — Show payment methods section (supports title parameter)

**sc_customer_billing_details** — Show billing details section (supports title parameter)

**sc_customer_wordpress_account** — Show account details section (supports title parameter)

### Order Confirmation

**sc_order_confirmation** — Show order confirmation wrapper (no parameters)

**sc_order_confirmation_line_items** — Show order items (no parameters)

### Product Collections

**sc_product_collection** — Display product collection page. Parameters: collection_id (required), columns, sort_enabled, pagination_enabled, ajax_pagination, limit

### Buy Button

**sc_buy_button** — Display a Buy Now button. Parameters: price_id (required), quantity, ad_hoc_amount

### Currency Switcher

**sc_currency_switcher** — Integrate currency switching (no parameters)

## Finding Product IDs

Product IDs appear in the edit product URL. The ID is the value after `id=` at the end of the URL when editing a product in the WordPress dashboard.


===== SOURCE: api-token-wp-config.md =====

---
source_url: https://surecart.com/docs/api-token-wp-config
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/How to Configure the SureCart API Token in wp-config.php

# How to Configure the SureCart API Token in wp-config.php

This document explains how to define the SureCart API token as a PHP constant in the wp-config.php file, instead of storing it in the WordPress database through the admin interface. This approach keeps the token outside the database, preserves the connection during migrations, and prevents disconnection caused by plugins that regenerate WordPress salts.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- Access to the wp-config.php file via FTP, SFTP, SSH, or the hosting provider's file manager
- A valid SureCart API token. Refer to [How to Get the SureCart API Token](https://surecart.com/docs/add-surecart-api/).

## **When This Approach Is Recommended**

Defining the API token in wp-config.php is recommended in the following scenarios:

- **Security-sensitive environments.** The token is stored in the site files rather than in the WordPress database, reducing exposure in the event of a database compromise or unauthorized admin access.
- **Site migrations and cloning.** The token travels with the site files. A site cloned to staging or deployed to a new server remains connected to SureCart without manually re-entering the token.
- **Sites affected by salt regeneration.** Some security plugins periodically regenerate WordPress salts, which can invalidate the token stored in the database. A token defined in wp-config.php is unaffected.

On standard sites that do not face any of the situations above, configuring the token through **SureCart → Settings → Connection** in the WordPress admin remains a valid option.

## **Step-by-Step Instructions**

### **Step 1: Back Up the wp-config.php File**

Before any change is made, download a copy of the existing wp-config.php file. If the edited file contains a syntax error or an incorrect value, restoring the backup returns the site to a working state.

- Connect to the site via FTP, SFTP, SSH, or the hosting provider's file manager.
- Locate wp-config.php in the WordPress installation root directory (the same directory that contains the wp-content folder).
- Download a copy and store it in a safe location.

### **Step 2: Add the Token Constant**

Open wp-config.php in a text editor and locate the following line:

```
/* That's all, stop editing! Happy publishing. */
Add the following line just above this comment:
define( 'SURECART_API_TOKEN', 'st_xxxxxxxxxxxxxxxxxxxxxxxx' );
```

Replace st_xxxxxxxxxxxxxxxxxxxxxxxx with the actual API token retrieved from the SureCart account. The token always starts with st\_.

**Important:** Placing the constant **above** the "That's all, stop editing!" line is required. Constants defined below that line may not be loaded in time and will be ignored by SureCart.

### **Step 3: Save and Upload**

- Save the modified wp-config.php file.
- Upload the file back to the WordPress installation root, replacing the existing version.
- Confirm that file permissions remain set to the values used by the hosting provider (typically 644 or 600).

### **Step 4: Verify the Connection**

- Sign in to the WordPress admin.
- Go to **SureCart → Settings → Connection**.
- Confirm that the connection status is displayed as **Connected**.
- Optionally, run a quick checkout test to confirm that orders and other store operations function as expected.

**Expected outcome:** The SureCart admin connection shows as Connected, the database-stored token (if previously configured) is overridden by the constant defined in wp-config.php, and the site retains its SureCart connection across migrations and salt regenerations.

## **Removing the Token from wp-config.php**

To stop using the constant and return to managing the token through the WordPress admin:

- Open wp-config.php via FTP, SFTP, SSH, or the hosting provider's file manager.
- Locate the line define( 'SURECART_API_TOKEN', '…' );.
- Delete the line and save the file.
- Upload the file back to the WordPress installation root.
- Sign in to the WordPress admin and go to **SureCart → Settings → Connection**.
- Enter the API token in the connection field and save.

## **Notes and Limitations**

- When the constant is defined in wp-config.php, it overrides any token saved in the WordPress database via **SureCart → Settings → Connection**.
- Editing wp-config.php directly carries risk. A syntax error or accidental deletion of an existing constant can prevent the site from loading. The backup created in Step 1 allows the previous state to be restored.
- The wp-config.php file is loaded by WordPress on every request, so constants defined inside it are available globally without performance impact.
- Some security plugins protect wp-config.php with additional permissions or rules. These protections do not affect SureCart, but may require temporary adjustments to upload the edited file.

## **Related Documentation**

- [How to Get the SureCart API Token](https://surecart.com/docs/add-surecart-api/)
- [Connecting SureCart via the Admin Interface](https://surecart.com/docs/add-surecart-api/)

## **FAQ**

**Is configuring the token in wp-config.php required?**

No. The token can also be configured through **SureCart → Settings → Connection** in the WordPress admin. Using wp-config.php is recommended in specific scenarios (security-sensitive environments, frequent migrations, sites affected by salt regeneration), but is not mandatory.

**Which value takes precedence when the token is defined in both places?**

The constant defined in wp-config.php takes precedence over the token stored in the WordPress database. The database value is ignored as long as the constant is present.

**What happens if the token defined in wp-config.php is invalid?**

SureCart cannot authenticate with the cloud and the connection status displayed under **SureCart → Settings → Connection** reflects the failure. Store operations that require the SureCart cloud (such as checkout and order syncing) do not function. Replacing the constant with a valid token restores the connection.

**Why does the site display "SureCart disconnected"?**

Disconnection typically occurs when the API token is removed, replaced, or invalidated. Common causes include database overwrites, plugin updates, site migrations performed without preserving the token, or plugins that regenerate WordPress salts. Defining the token in wp-config.php prevents most of these scenarios. When disconnection occurs, the token can be re-entered through **SureCart → Settings → Connection** or restored by editing wp-config.php.

**Does defining the constant affect WordPress or other plugins?**

No. The constant is read only by SureCart and does not interact with WordPress core or other plugins.

**Can the token be defined in wp-config.php on multisite installations?**

Yes. When the same SureCart store is connected to all sites in a multisite network, the constant can be defined once in the shared wp-config.php file. For networks where different sites connect to different SureCart stores, the database-based configuration in each site's admin is more appropriate.

**What happens during a site migration when the token is defined in wp-config.php?**

The token moves with the site files. When the destination site loads, the constant is detected and the SureCart connection is preserved without manual re-entry. This avoids the disconnection that can occur when only the database token exists and the database is migrated separately from the files.


===== SOURCE: attach-files-to-products.md =====

---
source_url: https://surecart.com/docs/attach-files-to-products
source: surecart-kb
scraped: true
---

# How to Attach a Downloadable File for Your SureCart Products

SureCart makes it effortless to sell a variety of downloadable products, such as E-books, software files, games, and more.

We offer two convenient methods for uploading content to your products:

- **Secure Upload**: You can securely store your downloadable files within your SureCart account. This ensures a reliable and controlled access process for your customers.
- **External Links**: Alternatively, you have the option to add links to files stored in your preferred storage solution, such as Google Drive or Dropbox.

### **How to Add Downloadable Files to a Product in SureCart**

If you want to upload your files directly, SureCart will store them in your SureCart account and display the download option to your customers in their customer dashboard.

- First, open the product page from WordPress Dashboard > SureCart > Products.
- Scroll down to the Downloads section and click on the "Add Downloads" button.
- Choose "Secure Storage" if you want your files to be stored in SureCart's secure storage.
- A new popup will appear where you will be able to upload your file or select from already uploaded files. Once you've selected your file, click on the "Choose File" button.

Your file is now attached to the product and stored in SureCart secure storage.

### **How to Add External Storage Links for Your Products**

When you click on the "Add Downloads" button, instead of "Secure Storage" use the "External link" option.

This is a great option if you already have saved your file in your own secure storage and you just want to display that link to your customers as a download option.

- Click on the "Add Downloads" button and choose "External link."
- A popup will appear where you need to provide the name of the downloadable file and the link to the file. Then click on the "Add Link" button and the file will be added to your product.

In the link URL, you can also put a direct web address — it could be a link to a Google Docs page, a YouTube video, or any link.

**Note**: It's possible to add both Secure Storage and External link files as a downloadable file, and you can add as many files as you want for a product.

### **How Downloadable Files Will Appear to Customers**

After purchasing the product with the downloadable files, customers will be able to see them on their Dashboard page, in the Downloads section.


===== SOURCE: automatically-change-subscription.md =====

---
source_url: https://surecart.com/docs/automatically-change-subscription
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Subscriptions](https://surecart.com/docs-category/subscriptions/)/How to Change Subscription From Yearly to Monthly

# How to Change Subscription From Yearly to Monthly

This guide shows how to create a pricing structure that starts with an annual subscription and then automatically transitions to a monthly subscription after the first year.

## Pricing Structure

Here's the setup approach:

1. Create a monthly subscription.
2. Add a setup fee and clearly name it to show it covers the whole year (e.g., $60 for Year 1).
3. Offer a free trial for 365 days. This prevents the monthly subscription from starting during this period.
4. Allow the setup fee to be charged during the free trial. This acts like a yearly plan.

The customer will see that they will be charged $60 now (the setup fee / yearly amount), and then $10 every month starting in 365 days (after the free trial ends).

This approach does not require special tools or additional plugins.


===== SOURCE: bricks-builder-templates-not-showing.md =====

---
source_url: https://surecart.com/docs/bricks-builder-templates-not-showing
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/Troubleshooting Bricks Builder Templates

# Troubleshooting Bricks Builder Templates

If you've created a product page template in Bricks and want to apply it to your SureCart products, you might run into an issue where the Bricks template isn't visible.

Instead of showing your product page template, the SureCart layout might take its place.

The issue arises when the product template is set to "SureCart Layout" instead of "Theme Layout" in the individual product settings.

Fortunately, you can fix this just by changing the template option to "Theme Layout". Here's how you can do it.

## **How to Change the Template Setting**

To ensure that your Bricks template is used, you need to update the template setting to "Theme Layout." Here's a step-by-step guide:

- Go to **SureCart** > **Products** and select your preferred product.

- Once inside, click on "Template". This lets you [customize product templates](https://surecart.com/docs/customize-product-template/) inside SureCart.

By default, the page layout here will be set to "Theme Layout". If you've set this to "SureCart Layout", switch it back to Theme Layout again.

Once done, click on the **Save Product** button on the top.

When you view the product page now, you should see your Bricks template displayed.

That's all. If you're still facing the same issue, please feel free to open a support ticket. We're always here to help!


===== SOURCE: bricks-dynamic-data.md =====

---
source_url: https://surecart.com/docs/bricks-dynamic-data
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/Dynamic Data for Bricks Builder

# Dynamic Data for Bricks Builder

In this documentation, we will explore and explain all the dynamic data available for use within the Bricks Builder.

For more detailed information about Bricks Builder's dynamic data, be sure to consult the [official documentation](https://academy.bricksbuilder.io/article/dynamic-data/) on their website.

### **Understanding Dynamic Data**

Dynamic data refers to the data fields that can change based on the product or context. By utilizing dynamic data in Bricks Builder, you can efficiently display product-specific information that automatically updates, allowing for a highly customizable and personalized user experience.

### **List of All Available Dynamic Data**

| **Dynamic Data**                             | **Description**                                                            | **Example**                             |
| -------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------- |
| {sc_product_price}                           | The default or first price of a product.                                   | $39                                     |
| {sc_product_selected_price}                  | The price currently selected in the Price Selector element.                | $30                                     |
| {sc_product_scratch_price}                   | The price before any discounts are applied (crossed-out price).            | $29                                     |
| {sc_product_selected_scratch_price}          | The original price for the currently selected pricing option.              | $24                                     |
| {sc_product_price_range}                     | For products with variable prices, the range from lowest to highest.       | $24 - $39                               |
| {sc_product_description}                     | The description of the product.                                            | Offer your customers the flexibility... |
| {sc_product_stock}                           | The current stock level of the product.                                    | 33                                      |
| {sc_product_sku}                             | The SKU (Stock Keeping Unit), a unique identifier for your product.        | ABC12345                                |
| {sc_product_on_sale}                         | Whether or not the product is on sale (1 = true, 0 = false).               | 1                                       |
| {sc_product_trial}                           | If the product includes a trial period, the length or start date.          | Starting in 15 days                     |
| {sc_product_selected_price_trial}            | The trial info for the currently selected pricing option.                  | Starting in 15 days                     |
| {sc_product_billing_interval}                | How frequently the customer will be billed.                                | Every month                             |
| {sc_product_selected_price_billing_interval} | The billing interval for the selected pricing option.                      | Every year                              |
| {sc_product_setup_fee}                       | The setup fee associated with the product's first price.                   | $9 Setup Fee                            |
| {sc_product_selected_price_setup_fee}        | The setup fee for the selected price in the Price Selector.                | $9 Setup Fee                            |
| {sc_price_name}                              | The name of the price or pricing option (within the Price Choice element). | Subscribe & Save                        |
| {sc_price_amount}                            | The actual price amount for the selected Price Choice element option.      | $24 / month                             |
| {sc_price_trial}                             | The trial period for the selected Price Choice element.                    | Starting in 7 days                      |
| {sc_price_setup_fee}                         | The setup fee for the selected price in the Price Choice element.          | $9 Setup Fee                            |

### **How to Use This Data in Bricks Builder**

To ensure dynamic data works correctly with SureCart in Bricks Builder, there are a few important conditions you must meet. Dynamic data must be used either:

1. Inside a **Query Loop** where the **SureCart Product** is set as the post type, or
2. Within a **Bricks Template** part for:
   - **SureCart - Single Product**, or
   - **SureCart - Collection Archive**.

Additionally, dynamic data should be placed inside **Product Form** or **Product Card** elements to ensure it pulls the correct product information.

If these conditions are not met, the dynamic data fields won't pull in the correct product information.

#### **Steps to Insert Dynamic Data:**

1. Navigate to the relevant page or template in Bricks Builder: For dynamic product displays, use a **Query Loop** with **SureCart Product** as the post type, or use the SureCart Single Product or Collection Archive template parts.
2. Enable the **Query Loop** if applicable, and set the post type to **SureCart Product**.
3. Ensure that the dynamic data is placed inside **Product Form** or **Product Card** elements.
4. Select the element where you want to display dynamic data (e.g., a text block, pricing table, etc.).
5. Choose the relevant dynamic data field from the available options within the Bricks interface.
6. Preview your page to ensure that the correct product data is dynamically displayed.

By adhering to these steps and using the right template structure or query settings, you can effectively create pages that dynamically pull in and display product information in real time.


===== SOURCE: bullet-points-not-showing-divi.md =====

---
source_url: https://surecart.com/docs/bullet-points-not-showing-divi
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Fixing Bullet Point Issue With Divi Theme And SureCart

# Fixing Bullet Point Issue With Divi Theme And SureCart

When using the Divi theme with SureCart, some users may encounter an issue where bullet points are not displayed properly. Instead, no marker may be shown.

This can make your content look messy and unprofessional.

Fortunately, this issue can be fixed by adding this custom CSS snippet in your **Additional CSS** settings.

```css
sc-prose ul {
  list-style: initial;
  margin-left: 14px;
}
```

### How To Solve The Bullet Point Issue In Divi

- Navigate to **Appearance** > **Customize** from your WordPress dashboard.

- Click on **Additional CSS** at the bottom of the menu.

- Add the mentioned code here and click on the **Publish** button:

```css
sc-prose ul {
  list-style: initial;
  margin-left: 14px;
}
```

- Check your checkout page; now it will work as expected.

Your bullet point display issue with the Divi Theme and SureCart should now be resolved.

Hope this solution helped. If you are still facing this issue, please reach out to our support team. We're always here to help!


===== SOURCE: caching.md =====

---
source_url: https://surecart.com/docs/caching
source: surecart-kb
scraped: true
---

# Caching Configuration for SureCart

## Overview

This guide provides guidance on configuring caching plugins to work properly with SureCart. It identifies potential conflicts and offers solutions.

## Key Configuration Requirements

**REST API Protection**: Exclude all REST API requests from being cached to prevent stale customer data, cart information, and checkout problems.

**Core Script Handling**: WordPress foundational scripts (wp-api-fetch, wp-a11y, wp-i18n, wp-url-js, dom-ready-js, hooks-js) must load synchronously and should not be deferred.

**JavaScript Optimization**: Disable script combining since HTTP/2 enables parallel resource loading, making file combination unnecessary and potentially harmful.

**Dynamic Page Exclusion**: Login, registration, checkout, and customer dashboard pages require exclusion from caching due to their user-specific, real-time nature.

**Browser Caching**: Aggressive browser caching for eCommerce data should be disabled to prevent displaying outdated cart contents or order information that cannot be remotely refreshed.

## Implementation Approach

Test thoroughly after adjusting caching settings. Contact SureCart support for additional assistance with implementation challenges.


===== SOURCE: cancellation-downgrade-upgrade.md =====

---
source_url: https://surecart.com/docs/cancellation-downgrade-upgrade
source: surecart-kb
scraped: true
---

# How to Set Cancellation, Downgrade, and Upgrade Rules - SureCart

## What is Prorated Billing?

Prorated billing divides costs proportionally based on specific rules.

SureCart offers two proration methods:

**Cost-Based Proration**: Charge customers based on the difference between which plan they currently have and which plan they wish to switch to. A customer upgrading from $8 to $12 annually pays only the $4 difference immediately.

**Time-Based Proration**: The upgrade cost is determined by the price difference between the two options and the time left in their current subscription before it renews. Using the same scenario with 6 months remaining, the customer pays only $2.

## Immediate Execution vs. Next Billing Period

**Immediate Execution**: Changes take effect instantly, without waiting for the next billing cycle. Customers gain immediate access to upgraded features with adjusted billing dates.

**Next Billing Cycle**: Changes or actions in the subscription commence at the beginning of the next billing cycle. Customers retain current access until the next billing period begins.

### When to Use Each Method

**Immediate Execution** works best for services and memberships where customers expect instant feature access, such as streaming services.

**Next Billing Cycle** suits subscriptions with physical items, maintaining billing consistency and avoiding pro-rated charges within a period.

## Managing Upgrades, Downgrades, and Cancellations

Access settings via: **SureCart > Settings > Subscription**

Configuration allows merchants to choose between immediate execution or next billing period for each subscription action.

### Downgrade Process

A downgrade means moving from a better plan to a basic one. You pay less to get less.

When downgrades happen immediately, the invoice will likely have a $0 balance and a credit may be applied to the customer. Customers access downgrades through their dashboard Plans menu.

### Upgrade Process

An upgrade means moving from a basic plan to a better one. You pay more to get more.

When upgrades happen immediately, a prorated invoice will be generated and paid. If the invoice payment fails, the subscription will not be updated. Users access upgrades through their customer dashboard.

### Cancellation Process

Cancellation means stopping the service or membership altogether.

Immediate cancellation stops service right away, while next billing period cancellation remains active until the end of the current billing period.

## Implementation

After adjusting settings to your preferences, click the "Save" button. Subscriptions will stick to these preferences when they're upgraded, downgraded, or canceled.


===== SOURCE: cart-menu-icon-shortcode.md =====

---
source_url: https://surecart.com/docs/cart-menu-icon-shortcode
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/The Cart Menu Icon Shortcode

# The Cart Menu Icon Shortcode

Sometimes you will want to add the cart menu icon outside of your WordPress menus, or perhaps you are using a page builder that does not pull in default WordPress menus.

If you are not using the block editor, you can use the `sc_cart_menu_icon` shortcode to achieve this.

```
[sc_cart_menu_icon cart_icon="shopping-bag" cart_menu_always_shown=1]
```

This shortcode uses the following parameters:

- **cart_icon** - Either "shopping-bag" or "shopping-cart". Shows the specific cart icon of your choice.
- **cart_menu_always_shown** - Either 1 or 0. If you choose 0, the icon won't show up unless you have added something to your cart.

Find more of such helpful shortcodes in our [list of shortcodes](https://surecart.com/docs/all-shortcodes/).


===== SOURCE: cart-toggle-icon.md =====

---
source_url: https://surecart.com/docs/cart-toggle-icon
source: surecart-kb
scraped: true
---

# How to Add Cart Toggle Icon to FSE Theme Menus - SureCart

## Overview

SureCart provides a solution for Full Site Editing (FSE) compatible themes that lack a default cart menu icon. The platform offers a custom Gutenberg block specifically designed for this purpose.

## Solution

FSE themes don't automatically display the cart icon in menus. To resolve this, SureCart created a specialized Gutenberg block called "Cart Toggle Icon" that integrates seamlessly with FSE themes.

## Implementation Steps

1. **Access Your Theme Header**: Open the header section of your FSE theme
2. **Locate the Block**: Find "Cart Toggle Icon" among available Gutenberg blocks
3. **Add to Menu**: Drag the block to your desired location in the header

## Customization Options

Once added, the block offers flexibility:
- Customize the appearance of the cart icon
- Choose visibility settings (always visible or only when items are in cart)

## Additional Resources

SureCart provides an instructional video demonstrating the process step-by-step at the documentation page.

**Note**: This feature is exclusive to FSE-compatible themes and addresses a known limitation affecting all such themes using SureCart.


===== SOURCE: change-customer-dashboard-permalinks.md =====

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


===== SOURCE: change-form-template.md =====

---
source_url: https://surecart.com/docs/change-form-template
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Change a Form Template

# How to Change a Form Template

This document explains how to change the template of an existing checkout form in SureCart and what to expect when performing this action.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **Important Behavior to Understand**

Changing a checkout form template **replaces the current form entirely**.

When you change the template:

- All existing form customizations are removed
- The form must be configured again from scratch

This action cannot be undone.

### **Change the Checkout Form Template**

Follow the steps below to change a checkout form template.

- Go to **WordPress Dashboard → SureCart → Forms**.
- Select the checkout form you want to edit.
- In the form settings panel, click **Change Template**.
- Review the confirmation message.
- Click **OK** to confirm the action.
- Select a new checkout template from the available designs.
- Click **Next**.
- Click **Create**.

The new template will replace the existing form.

### **Reconfigure the Checkout Form**

After the new template is created, configure the checkout form again according to your needs, including products, layout, and settings.

### **Expected Outcome**

After completing these steps, the checkout form will use the newly selected template, with all previous configurations removed and replaced by the new design.

### **Notes and Limitations**

- Changing the template permanently removes existing form configurations.
- The previous template and settings cannot be restored.
- This action affects only the selected checkout form.

### **FAQ**

**Can I revert to the previous form template?**

No. Once a template is changed, the previous configuration cannot be restored.

**Will changing the template affect existing orders?**

No. Existing orders are not affected by form template changes.

**Can I customize the new template after changing it?**

Yes. The new template can be customized after it is created.


===== SOURCE: change-permalinks-url-slug.md =====

---
source_url: https://surecart.com/docs/change-permalinks-url-slug
source: surecart-kb
scraped: true
---

# How to Change the Permalinks & URL Slug for SureCart Product & Instant Checkout Page

Have you ever wanted your online store URLs to look flashy, unique, yet simpler?

SureCart lets you do just that with custom Products and Instant Checkout Permalinks. Here's why you might love it:

- **Memorable URLs:** Customize and make your product links easy to recall. Imagine telling someone, "Just go to yourwebsiteurl/shop/sample-product/". Neat, right?
- **Flexibility:** Not feeling the 'shop' vibe? Or 'products' not your jam? Go wild and pick a URL that you like.

### How to Change the Permalinks for SureCart Products

A permalink is a permanent web address (URL) for a specific webpage or post, meant to remain unchanged over time. So you should ensure you don't change it unless very important.

Changing the Permalinks for SureCart Products is very straightforward.

- Head to 'Settings' on your site, then click 'Permalinks'.
- Scroll down and look for 'SureCart Product Permalinks'.

The default permalink will be /products/ followed by the product name.

- Do you want to use /shop/ instead? If yes, just click 'Shop'.
- For something unique, hit 'Custom base' and type in what you like.
- Once done with the changes, hit 'Save Changes'.

### How to Change the Permalinks for Instant Checkout Pages

For Instant Checkout Pages, the same method applies.

Right under the Product Permalinks, you've got 'SureCart Instant Checkout Permalinks'.

- Not a fan of the default? Switch it to 'Purchase' or 'Custom Base'. And make the desired changes.
- Remember to hit 'Save Changes'.

### How to Change the URL Slug for SureCart Products

- Click on SureCart and choose "Products".
- Choose any products you've created.
- On the right, tap "URL Slug".
- In the Permalink Field, type a short, catchy description.
- Click on the "Save Product" to keep your changes.


===== SOURCE: change-product-availability.md =====

---
source_url: https://surecart.com/docs/change-product-availability
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Change Product Availability

# How to Change Product Availability

There are two main ways to change product availability in SureCart.

## How to Make Your Product Unavailable for Purchasing

1. Navigate to **SureCart → Products** from your WordPress dashboard.
2. Click on the product you want to modify.
3. In the right side section, under **Availability**, click **Purchasable** and select **Unavailable for Purchase**.
4. Click on the **Save Product** button.

Once saved, the product will no longer appear on the shop page. If a user has the direct link and tries to access it, they will see that the product is unavailable for purchase.

## How to Hide the Product from the Shop Page

To hide a product from the shop page, change its status from "published" to "draft". The product won't appear on the shop page, but if it's still set as "purchasable," you can still send a direct link for purchase.

1. Choose the product and click on it through SureCart.
2. Click on **Published** from the Product Page option and select **Draft**.
3. Click on the **Save Product** button.

**Note:** If a product is in Draft status and marked as Purchasable, accessing the product page directly will result in a "Page not found" error. However, you can still use Price links and the instant checkout page.

## Archive Product

Archiving a product hides it from the shop page, product page, and any other listing, making it completely unavailable for purchase — including through custom forms.

If a customer tries to purchase an archived product or price, they may encounter the error message: "Product Can't Be Blank." Archived products are inaccessible to non-logged-in users.


===== SOURCE: change-subscription-date.md =====

---
source_url: https://surecart.com/docs/change-subscription-date
source: surecart-kb
scraped: true
---

# How to Change the Renewal Date of Subscription - SureCart

## Overview

SureCart provides functionality to modify subscription renewal dates for customers. Changing the renewal date on a subscription updates **all subsequent renewal dates**.

## Steps to Change Renewal Date

1. Navigate to SureCart menu and select "Subscriptions"
2. Locate and select the customer whose subscription needs modification
3. Click the "Actions" button in the upper right corner
4. Choose "Change Renewal Date" from the menu
5. Select your preferred date and time in the popup window
6. Click "Update Subscription" to confirm changes

## Key Details

This feature is useful when users encounter difficulties making a payment (e.g., they change their bank account or card). The renewal date adjustment accommodates such scenarios.

## Important Note

When you modify a renewal date, the change applies globally. For example, if you update the renewal date to April 12, future renewals will follow the adjusted schedule: May 12, June 12, etc.

## Additional Outcomes

After updating a subscription renewal date, customers retain access to their materials and receive an email notification about the changes.


===== SOURCE: change-surecart-url.md =====

---
source_url: https://surecart.com/docs/change-surecart-url
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Change the Store URL in SureCart

# How to Change the Store URL in SureCart

This document explains how to update the store URL when the domain or address of an existing SureCart store changes (for example, from store.example.com to shop.example.com). The procedure updates how the store URL is displayed in customer-facing locations such as invoices, receipts, and email notifications.

## **Requirements**

- WordPress admin access
- SureCart installed, activated, and connected
- The new domain configured at the hosting and DNS level, pointing to the WordPress installation

## **Updating the Store URL**

The fields that reference the store URL are located on the **Store Settings** page. The page contains three sections, each with its own **Save** button. The store URL appears in two of these sections, and both must be updated.

### **Step 1: Update the Store Details Section**

1. Go to **WordPress Dashboard → SureCart → Settings → Store Settings**.
2. Locate the **Store URL** field. Replace the existing URL with the new domain.
3. Locate the **Terms Page** field. Update the URL to use the new domain.
4. Locate the **Privacy Policy Page** field. Update the URL to use the new domain.
5. Click **Save** at the bottom of the Store Details section.

### **Step 2: Update the Contact Information Section**

6. On the same **Store Settings** page, scroll down to the **Contact Information** section.
7. Locate the **Website** field.
8. Update the URL to match the new domain.
9. Click **Save** at the bottom of the Contact Information section.

**Expected outcome:** After saving both sections, all new invoices, receipts, and email notifications display the updated URL.

## **Notes and Limitations**

- The **Store Settings** page contains three sections (Store Details, Notification Settings, Contact Information), and each is saved independently.
- Existing invoices and emails already sent to customers are not updated retroactively.
- The WordPress Site Address must already point to the new domain before updating the SureCart settings.

## **Related Documentation**

- [How to Update Store Details](https://surecart.com/docs/update-store-details/)
- [Migrating to Another WordPress Install](https://surecart.com/docs/migrate-to-another-wordpress-install/)
- [How to Transfer Store Ownership](https://surecart.com/docs/transfer-store-ownership/)


===== SOURCE: checkout-form-gutenberg.md =====

---
source_url: https://surecart.com/docs/checkout-form-gutenberg
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Insert the Checkout Form in a Page Using Gutenberg

# How to Insert the Checkout Form in a Page Using Gutenberg

Since checkout forms are not directly hosted on web URLs, you cannot share them with others, but you can insert the checkout form on a page and share it with people.

There are two ways to add a checkout form on WordPress:

- Inserting the Checkout Form Shortcode in a shortcode block
- Using the checkout form widget in the page editor

You can use any of the ways to add your forms on pages.

Let's begin with how to add a checkout form to a WordPress page using the shortcode method.

1. Go to SureCart from your website, click on Forms, then copy the shortcode checkout form.

2. Go to Pages and add a new page.

3. If you are using Gutenberg Editor, insert a Name for your page, click on the plus button and the shortcode element.

4. You now need to paste the shortcode copied from Step 1 and click on Publish.

Once you publish the page, you will be able to see your checkout form on the published page.

Alternatively, you can add the Checkout Form element to your page and select the checkout form you want to add to this page.

The checkout page will be integrated into the page and fully functional.


===== SOURCE: checkout-form-in-elementor.md =====

---
source_url: https://surecart.com/docs/checkout-form-in-elementor
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/Inserting Checkout Form On a Page Using Elementor

# Inserting Checkout Form On a Page Using Elementor

Adding a checkout form to your site can greatly enhance the customer experience and improve your sales process.

By using the Elementor Page Builder, you can easily insert and display the checkout form on a page.

In this article, we'll show you how to do just that:

1. Insert the **Shortcode** widget into the page.

2. Paste the checkout form shortcode you copied from **Forms** and then **Publish** the page.

3. Alternatively, you can add the **Checkout Form** widget and insert it to the page.

4. In the widget settings, select the necessary checkout form and **Publish** the Page.

If you cannot find the "Checkout Form" widget for other page builders, you can insert the checkout form using shortcodes.

That's it! Now, you can share the page with your customers and start making sales!

We hope this article was helpful. For any questions, please feel free to contact us. We're always here to help.


===== SOURCE: choose-form-processors.md =====

---
source_url: https://surecart.com/docs/choose-form-processors
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Payments](https://surecart.com/docs-category/payments/)/How to Enable/Disable Specific Processors For a Form

# How to Enable/Disable Specific Processors For a Form

Enabling or disabling specific processors in your checkout form is like hand-picking the payment methods you want to show to your customers on the checkout page.

Let's say you have multiple payment gateways connected to your SureCart store, like Mollie, Stripe, and others.

But you only want to show the payment methods that suit your customers' preferences or your business needs instead of all the connected payment processors so that you can do that easily.

For example, you can only display Stripe as the payment method on the checkout form and hide others.

By the way, only paid plans have access to this feature.

So if you want to hide specific payment processors from your checkout form, then simply follow the steps below:

1. Go to SureCart on your website and click 'Forms'.

2. Click on the form where you need to enable or disable the specific processor.

3. Scroll down to Payment Elements and click on it.

4. Enable or disable the payment processor you want. On the right side of the screen, you'll see a list of payment processors. Just click the ones you need.

That's it!

Now your customers will only see the selected payment processor on this checkout form.


===== SOURCE: clear-test-data.md =====

---
source_url: https://surecart.com/docs/clear-test-data
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Clear Test Data

# How to Clear Test Data

When you switch your Checkout to Test Mode and make some test purchases, you end up creating orders, users, and transactions.

These get recorded both on app.surecart.com and your website. If you're looking to delete this data, We are here to guide you through the process.

1. Click on SureCart and choose **Settings**.

2. Next, access the **Advanced** tab and scroll down to "Clear Test Data".

3. Click on the **Clear Test Data** button.

4. You will be redirected to a new tab where you must log into your app.surecart.com account by entering your login information.

5. After logging in, you will be redirected to the **Settings** page, where you can click "Clear Test Data".

6. When you click the Clear Test Data button, a prompt appears. You must type CONFIRM to remove the test data. After typing, click the confirm button, and the system removes the data.

To wrap it up, removing test data from SureCart makes your account neat by getting rid of unwanted test records.

This is easy but important to avoid confusion later.

Now, you can take your account to live mode and start selling! Got questions? Feel free to ask us. We're here to help!


===== SOURCE: collect-tax-or-vat.md =====

---
source_url: https://surecart.com/docs/collect-tax-or-vat
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Tax](https://surecart.com/docs-category/tax/)/How to Collect Tax ID/VAT Numbers from Your Customers

# How to Collect Tax ID/VAT Numbers from Your Customers

To collect your customers' tax ID/VAT number, navigate to **SureCart > Forms** and select the form you wish to edit.

Then, add a "VAT or Tax ID Input" field to your form. You can control where you want this form field to appear.

### Changing VAT behavior

To change VAT behavior navigate to **SureCart > Settings > Tax**. Be sure that "Tax Collection" is turned on. Please enable any necessary settings:

**Require VAT Number**: This will require the VAT field to be required on all forms. It will also automatically add a VAT field to your form if you have not already added one.

**Local Reverse Charge**: By default, reverse charges will not apply when customers are in your home country. However, enabling this setting enables you to apply a reverse charge when a customer is in your home country.

**VAT Number Verification Failure**: By default, SureCart will validate an EU VAT number EU VAT Number Validation API, which takes data from VIES. If it matches, a VAT exemption is done automatically.

If it fails to validate, the user sees an error. Sometimes a user can have a valid VAT number in their home country, but not registered through VIES. This will also make validation fail. You can change this behavior:

- Reject the order and show an error
- Accept the order but don't apply reverse charge (don't remove VAT)
- Accept the order and remove VAT as normal (remove VAT)

### Invoices

If a customer properly configures their tax ID/VAT number during checkout, it automatically appears on the invoice.

We hope this guide helped you. If you have any questions, please don't hesitate to contact our support team. We're here to help!


===== SOURCE: collection-template-bricks.md =====

---
source_url: https://surecart.com/docs/collection-template-bricks
source: surecart-kb
scraped: true
---

# How to Create the Collection Template in Bricks Builder

This guide will cover the key steps for setting up a collection template in Bricks Builder with SureCart's integration.

Using this integration, you can easily customize and design e-commerce collection pages by taking advantage of SureCart's dynamic elements within Bricks.

### **Creating SureCart Collection Archive Template**

To apply a consistent layout to all your collections pages in Bricks, you need to create a SureCart Collection Archive Template.

To create the SureCart Collection Archive template, follow these steps:

- Go to **Bricks > Templates**.
- Click the **Add New** button.
- Give the template a name; in this case, "Collections Template".
- In the **Template type** dropdown, select **SureCart – Collection Archive**.
- Click the **Publish** button.
- Then click the **Edit with Bricks** button to start designing your template.

- Search for "section" in the elements panel.
- Click on the **Section** element to add it to the canvas.
- Click on the **Container** in the Structure panel on the right.
- Click on the **Elements** button to add a SureCart Element to the container.
- In the **Container**, select the **Grid** option in the **Display** setting.
- In the **Grid Template Columns**, type repeat(4, 1fr) to create 4 columns.
- Add the **Post Title** element.

- Add a **DIV** element inside the container and click to select it.
- Click to add another element and search for "product".
- Click on **Product Card** to add it to the **DIV**.
- Click on the parent **DIV** again.
- Now, enable the **Query Loop** option.
- With the **Query Loop** enabled, click on the infinity button to set the loop.
- In the **Post Type**, select **SureCart Product**.

Now, you just need to save your template and complete one final step to apply the Bricks layout to your collection.

- Go to **Products > Collections** menu.
- Select the collection where you want to apply the Bricks template and click **Edit**.
- In the **Template** section, click on the **Default** dropdown menu.
- Under **Page Layout**, click the dropdown and select **SureCart Layout**.
- Click the **Save Collection** button to save the changes.

That's it! Your collections will now use the Bricks template you've customized.

### **FAQ**

**Can I create a different layout for each collection?**

Yes, you can. To do this, you'll need to add template conditions. Open the collection template, click the gear icon for settings, go to **Template Settings**, then **Conditions**. Add a condition, select **Terms**, and choose the term(s) you want this template to apply to.


===== SOURCE: conditional-block.md =====

---
source_url: https://surecart.com/docs/conditional-block
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/Create Advanced Checkouts With the Conditional Block

# Create Advanced Checkouts With the Conditional Block

This document explains how to use the Conditional block in SureCart to display checkout fields or messages based on specific conditions, such as customer location or selected products.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **What Is the Conditional Block**

The Conditional block allows checkout content to appear or remain hidden based on defined rules.

Conditions can be created using factors such as:

- Selected products
- Shipping country
- Order value
- Applied coupons
- Payment method

When the defined rules are met, the blocks inside the Conditional block are displayed during checkout.

### **Use Case: Show a Tax ID Field Based on Customer Country**

This example demonstrates how to display a Tax ID field only when the customer's shipping country matches specific values.

- Go to **WordPress Dashboard → SureCart → Checkout**.
- Open the checkout form you want to edit.
- Click the **+** icon to add a new block.
- Search for **Conditional** and add the Conditional block.
- Select the Conditional block and click **Add Conditions**.
- In the **Condition** dropdown, select **Shipping Country**.
- Choose the countries where the field should appear (for example, United States, India, and Brazil).
- Click **Set Rules**.
- Click the **+** icon inside the Conditional block.
- Search for **Tax** and insert the **Tax ID** or **VAT** field.
- Update the label if needed (for example, SSN, CPF, or Tax ID).
- Click **Update** to save the checkout form.

The Tax ID field will now appear only when customers from the selected countries reach the checkout.

### **Use Case: Show a Pre-Order or Backorder Notice**

You can also use the Conditional block to display messages for specific products, such as pre-order or backordered items.

- Go to **SureCart → Checkout**.
- Open the checkout form.
- Insert a **Conditional** block after the order summary.
- Add a condition based on **Product(s)**.
- Select the product that should trigger the message.
- Click **Set Rules**.
- Inside the Conditional block, insert a **Paragraph** block.
- Enter the message you want customers to see (for example, pre-order details or delivery expectations).
- Click **Update** to save your changes.

When the selected product is added to the cart, the message will appear during checkout.

### **Expected Outcome**

After configuring Conditional blocks, checkout fields and messages will appear dynamically based on the defined rules, providing a more context-aware checkout experience for customers.

### **Notes and Limitations**

- Conditional blocks only affect the content placed inside them.
- Conditions are evaluated in real time during checkout.
- Multiple Conditional blocks can be used in the same checkout form.

### **FAQ**

**Can I use multiple conditions in the same checkout form?**

Yes. You can add multiple Conditional blocks, each with its own set of rules.

**Do Conditional blocks affect existing orders?**

No. Conditions apply only during checkout and do not modify existing orders.

**Can Conditional blocks be used for non-product rules?**

Yes. Conditions can be based on factors such as shipping country, payment method, or order value.


===== SOURCE: configure-tax-settings-in-surecart.md =====

---
source_url: https://surecart.com/docs/configure-tax-settings-in-surecart
source: surecart-kb
scraped: true
---

# How to Configure Tax Settings in SureCart

## Overview

SureCart offers integrated tax management using TaxJar for real-time calculations at no additional cost. The platform supports predefined tax regions and allows both automatic and manual tax calculation methods.

## Enabling Tax Collection

To activate tax settings:

1. Navigate to WordPress Dashboard
2. Click SureCart
3. Select SureCart Settings
4. Go to Taxes settings
5. Enable the Tax Collection toggle

## Fallback Tax Rate

The fallback tax rate serves as a backup when specific tax registrations are not found. This ensures consistent tax charges across customers from countries without customized rates.

## Invoice Address Setup

Enter your business address in the designated field — this information displays on tax invoices.

## Setting Up Tax Regions

SureCart provides predefined regions:

- Australia
- Canada
- European Union
- United Kingdom
- United States
- Rest of the World

**Tax Calculation Options:**

- Automatic (via TaxJar with registration number)
- Manual (specify tax percentage)

### Canadian Tax Example

1. Select Canada as tax region
2. Toggle "Collect Canada GST/HST" and enter GST numbers
3. For provincial taxes, select province and configure individual settings
4. Click "Collect Tax" to save

## Charging Tax on Products

To enable taxes on specific products:

1. Edit the product
2. Locate the Taxes tab
3. Toggle "Charge tax on this product"
4. Configure tax ID and address fields

Tax details will appear in checkout subtotals.

## Important Note

This article is not intended to provide tax advice. Consultation with tax professionals regarding specific obligations is recommended.


===== SOURCE: configuring-apple-pay.md =====

---
source_url: https://surecart.com/docs/configuring-apple-pay
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Payments](https://surecart.com/docs-category/payments/)/Setting Up Apple Pay on Your Stripe Account

# Setting Up Apple Pay on Your Stripe Account

Offering a variety of payment options is crucial for the success of your online store. Apple Pay, known for its convenience and security, has become a popular choice among consumers.

Integrating Apple Pay with your Stripe account can enhance the checkout experience for your customers and lead to higher conversions.

### **Activating Apple Pay in Stripe**

The first step in enabling Apple Pay for your online store is to activate it within your Stripe account settings.

### **Configure Your Domain**

- After logging into your Stripe account, navigate to the settings by clicking on the cog icon located in the top right corner.

- Click on the Settings

- On the new page, click on Payments

- Click on the Payment methods tab.

- Locate Apple Pay and click to open the toggle and view the options.

- Click on the Configure domains button

- Click on Add a new domain

- Enter your domain precisely as it appears, for example, "www.example.com".
- Click on Save and continue to save your changes.

Next, you must verify ownership of your domain. This requires access to your hosting environment and the ability to upload a file to a specific directory. Therefore, before moving forward, ensure you have the necessary access and permissions.

- To download the verification file, click the "Download" button.

- Now, in your hosting environment, create a folder named ".well-known" and upload the downloaded file into this folder.

- Lastly, click on Verify button.

If everything is done correctly, an "Enabled" badge will appear next to your domain.

Now, visit your checkout page to check if Apple Pay is visible both in the Stripe payment element and in the Express Payment Button.

### **Testing Apple Pay**

To test Apple Pay, you must use a genuine credit card in your Apple Pay wallet because it doesn't accept Stripe's test cards.

However, when you're in Stripe's test mode using your test API keys, Stripe will convert the real card into a Stripe test card.

This way, you can proceed with your testing without making actual transactions with your real card.

## **Apple Pay Troubleshooting**

If you've activated Apple Pay in your Stripe account but it's not appearing on your checkout page, there may be a configuration issue with Apple Pay.

The primary reason Apple Pay might not be functioning could be related to your domain settings. It's crucial to configure the domain exactly as it's currently used.

### **Verify The Correct Domain**

One of the more common issues is the domain for apple pay is incorrect. For example, if your main domain is "example.com" and your store is hosted on a subdomain like "store.example.com" or more commonly "**www**.example.com,". Ensure that you use the specific subdomain in your settings.

It's important to be aware that some browsers might omit the "www" prefix from the domain name. Therefore, it's essential to enter your domain details precisely as they are used.

### **Ensure You Are Using Safari**

Apple Pay on the web is exclusively supported by Safari web browsers, including both desktop and mobile versions.

### **Verify Apple Pay Is Set Up In Your Browser**

Make sure Apple Pay is ready to go in your Safari browser. This means you've added your payment card to your Apple device and signed in with your Apple ID. When you shop online with Safari, look for Apple Pay at checkout to know it's working.

If you can't see Apple Pay or have trouble using it, you might need to check a few more things or get help from your bank.

For easy steps on making sure Apple Pay is set up right in Safari, and what to do if it's not, visit Apple's help page: [https://support.apple.com/apple-pay](https://support.apple.com/apple-pay)

### **Verify Apple Pay Is Supported In Your Country**

To use Apple Pay, it's important to make sure it's available where you live. Apple Pay works in many countries, but not everywhere. This means you need to check if you can use Apple Pay in your country before you try setting it up or using it.

If you're not sure whether Apple Pay is supported in your country, you can easily find out by visiting Apple's official website. They have a list that shows all the countries where Apple Pay can be used.

Here's a quick link to check: [https://support.apple.com/en-us/102775](https://support.apple.com/en-us/102775)

We hope this guide helped you. If you have any questions, please don't hesitate to reach out to our support team. We're here to help!


===== SOURCE: connect-mollie.md =====

---
source_url: https://surecart.com/docs/connect-mollie
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect Mollie Payment Processor

# How to Connect Mollie Payment Processor

If you're considering Mollie as your preferred payment processing solution for selling on SureCart, this article is for you.

Mollie, a trusted and globally recognized payment gateway, empowers businesses to securely accept payments from customers. Offering a comprehensive suite of features and tools, Mollie streamlines payment collection, making it a good choice for online businesses and e-commerce platforms.

### **How to Begin The Setup**

To connect Mollie with SureCart effortlessly, follow these straightforward steps within your WordPress admin area:

1. From the SureCart Dashboard, navigate to the Settings menu.

2. Then click on Payment Processors. This will open a screen with all available processors.

#### **How to Connect Mollie in Test Mode**

Before you link the live Mollie payment system, you can connect Mollie in test mode. This lets you establish the payment system in a secure testing setup.

**Please note**: Configuring the live Mollie payment is a similar process.

For now, follow these steps to connect the test payment:

1. Click on the Mollie toggle to access the SureCart platform.

2. Click on the "Mollie" tab.

3. Click the **Connect** button dropdown and select "Test Mode". Here, you can also select "Live Mode", if you want to enable Mollie in real-time.

4. Enter your Mollie email address and password and click the "Log In" button.

5. Insert your verification code. Once you do, you will be automatically redirected to the next screen.

6. Select the Mollie store you want to connect with SureCart, and then click on the Connect button.

7. After being redirected from Mollie, you will notice a green notice at the top of your screen, confirming that you have successfully connected your Mollie account. The button will now be enabled.

8. Now, head back to your WordPress page and refresh it. After doing so, you will notice a green tag indicating that you have successfully connected your Mollie account in test mode.

Congratulations! You've successfully enabled Mollie in Test mode, and you're now ready to make a test purchase using Mollie.

That covers everything you need to know to connect Mollie with SureCart. However, if you still have questions or encounter any issues, please don't hesitate to contact us.

We'll be glad to assist you with any inquiries or problems you may have.


===== SOURCE: connect-paypal.md =====

---
source_url: https://surecart.com/docs/connect-paypal
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect PayPal Payment Processor

# How to Connect PayPal Payment Processor

If you're considering PayPal as your preferred payment processing solution for selling on SureCart, this article is for you.

PayPal, a trusted and globally recognized payment gateway, allows businesses to securely accept customer payments. Offering a comprehensive suite of features and tools, PayPal streamlines payment collection, making it a good choice for online businesses and e-commerce platforms.

In this guide, we'll walk you through the process of integrating PayPal with SureCart, ensuring you can safely collect payments from your customers on the platform.

Let's dive in!

### **How to Begin The Setup**

To connect PayPal with SureCart effortlessly, follow these straightforward steps within your WordPress admin area:

- Navigate to the **Settings** menu from your dashboard.

- Click on **Payment Processors**. This will open a screen with all available processors.

### **Connecting PayPal with SureCart**

Here's how you can connect your PayPal with the SureCart store:

- Click on the PayPal processor under the **Payment Processors** section from your dashboard.

- Select the **PayPal** tab here.

- Click on the **Connect** and select "Live Mode" from the dropdown.

- Fill in your PayPal account information here.

After successfully logging in with your PayPal credentials, you will be redirected to your SureCart platform.

You should see PayPal enabled both here and on your WordPress dashboard. Customers can now easily use PayPal to purchase products from your online store!

**Note**: If you come across the "Not Approved" warning, it means PayPal hasn't yet approved your account for transactions. To resolve this, contact PayPal's support team for assistance on the next steps to get your account approved.

### **How to Connect Paypal in Test Mode**

You can also connect PayPal in test mode. This lets you establish the payment system in a secure testing setup.

Process to connect PayPal test mode is is exactly same as connecting live, you just need to choose Test mode when connecting to PayPal.

- Click on the PayPal tab, then select "Test Mode" from the **Connect** dropdown menu.

Fill in your PayPal account credentials here. Once completed, you'll be redirected to the SureCart platform where you'll see the test mode enabled.

- Now, head back to your WordPress page and refresh it. After doing so, you will notice a green tag indicating that you have successfully connected your PayPal account in test mode.

Congratulations! You've successfully enabled PayPal in Test mode, and you're now ready to make a test purchase using PayPal.

That covers everything you need to know to connect PayPal with SureCart. However, if you still have questions or encounter any issues, please don't hesitate to contact us.

We are glad to assist you with any inquiries or problems you may have.


===== SOURCE: connect-paystack.md =====

---
source_url: https://surecart.com/docs/connect-paystack
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect Paystack Payment Processor

# How to Connect Paystack Payment Processor

If you're considering using Paystack to accept payments while selling on SureCart, this article is for you.

[Paystack](https://paystack.com/) is a service that helps businesses in Nigeria, Ghana, and South Africa securely receive payments from customers worldwide.

### **Know This Before You Connect Paystack with SureCart**

Paystack and Stripe don't work well together.

If you have Stripe and Paystack both active in SureCart, customers will only see the Stripe payment option during checkout.

To ensure a smooth payment process with Paystack, we suggest you disable Stripe before connecting your PayStack account.

If you're not sure how to disable a payment gateway, check out [this article](https://surecart.com/docs/how-to-disable-a-payment-processor/).

### **How to Begin The Setup**

When you're ready to connect SureCart and Paystack together, simply login to your WordPress admin area and follow these easy steps:

1. Go to the WordPress admin area and click on the SureCart dashboard.
2. Click on the Settings menu under SureCart settings that you see on the WordPress sidebar.
3. Click on Payment Processors in SureCart settings and you will see the Paystack listed as one of the payment processors.

#### **Connecting Paystack in Test Mode**

Before you connect the live Paystack payment processor, you can connect Paystack in test mode. This allows you to set up the payment processor in a safe testing environment.

1. Click on the **Paystack** option.
2. Click the "Paystack" tab.
3. Select "Test Mode" from the **Connect** button dropdown.
4. A pop-up window will appear.
5. To get your Test API Keys, go to your Paystack dashboard settings and click on the [API Keys & Webhooks](https://dashboard.paystack.com/#/settings/developer) tab.
6. Scroll to where it says "API Configuration - Test Mode", here you will find your Test Secret Key and Test Public Key. Copy these keys.
7. Go back to the SureCart screen and paste your Paystack Secret Key in the corresponding field.
8. Similarly, paste your Paystack Public Key in the corresponding field.
9. Copy the Webhook URL from the "Webhook Instructions" section, and then click on the "Create" button.
10. Return to your Paystack tab and paste your webhook URL in the corresponding field.

Once you've followed these steps, You will have Paystack connected with SureCart in the test mode.

#### **How to Connect Paystack in Live Mode**

After successfully setting up Paystack in test mode and ensuring a smooth payment process, it's time to move on to the live payment integration.

1. Click on the Paystack option.
2. Select the "Paystack" tab.
3. From the **Connect** dropdown, select "Live Mode".
4. Go to your Paystack dashboard settings and click on the [API Keys & Webhooks](https://dashboard.paystack.com/#/settings/developer) tab.
5. Scroll to where it says "API Configuration - Live Mode", and find your Live Secret Key and Live Public Key.
6. Go back to the SureCart tab and paste your Paystack Secret Key in the corresponding field.
7. Paste your Paystack Public Key in the corresponding field.
8. Copy the Webhook URL from the "Webhook Instructions" section, and then click on the "Create" button.
9. Return to your Paystack tab and paste your webhook URL in the corresponding field.

Once you have completed these steps, you will have successfully set up Paystack as your payment processor in live mode, and you can start accepting payments in Paystack via SureCart.

If you still have questions, don't hesitate to contact us. We'll be glad to help you with any questions or issues you may have.


===== SOURCE: connect-razorpay.md =====

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


===== SOURCE: connect-stripe.md =====

---
source_url: https://surecart.com/docs/connect-stripe
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect Stripe Payment Processor

# How to Connect Stripe Payment Processor

If you're considering using Stripe to accept payments while selling on SureCart, this article is for you.

Stripe is a renowned payment processing service that empowers businesses worldwide to securely receive payments from customers. It offers a wide range of features and tools to streamline payment collection, making it a popular choice for online businesses and e-commerce platforms.

In this article, we'll guide you through the process of connecting Stripe and SureCart, so you can effortlessly collect payments from your customers while selling on SureCart.

Let's get started!

## Connecting Your Stripe Account in SureCart

When you're ready to connect SureCart and Stripe together, simply log in to your WordPress admin area and follow these easy steps:

1. From the SureCart Dashboard, navigate to the Settings menu.

2. Then click on Payment Processors. This will open a screen with all available processors.

### Connecting In Live Mode

Live mode in SureCart enables real transactions to be processed using actual payment methods.

Here's how you can connect your Stripe with your SureCart store in live mode:

1. Click on the Stripe toggle to access the SureCart platform.

2. Click on the "Stripe" tab.

3. Access the **Connect** dropdown and select "Live Mode".

4. Enter your Stripe email address and click "Continue." Fill in your Password and Verification Code received on your mobile phone in the subsequent steps.

5. You will see a message indicating that you will be redirected to the SureCart platform.

6. After being redirected, you will see the Stripe account enabled here.

7. Now, head back to your WordPress page and refresh it. After doing so, you will notice a green tag indicating that you have successfully connected your Stripe account in live mode.

**Note**: Stripe might take some minutes to show up on your checkout. If it doesn't show up at all, please contact the Stripe support team.

### **Connecting In Test Mode**

You can also connect Stripe in test mode. This lets you check the payment system in a secure testing setup.

Follow these steps to connect the test processor:

1. Click on the Stripe toggle to open the SureCart platform.

2. Click on the Stripe tab here.

3. Select "Test Mode" from the **Connect** dropdown menu.

4. Since we are in the test mode, you can "skip this form".

5. After being redirected, you'll see that the Stripe test processor is enabled here.

6. Go to your WordPress page and refresh it. Once you do, you will see a green tag indicating that you have successfully connected your Stripe account in live mode.

Congratulations! You've successfully enabled Stripe in both Live and Test modes, and you're now ready to make sales, whether in live or test mode.

### **Verifying the SureCart Configuration in Stripe**

If you're facing issues displaying Stripe payment methods on your checkout, follow these steps:

- Login to your [Stripe account](https://dashboard.stripe.com/login).

- Click on the Settings icon and access the **Payments** tab.

- Under **Payment methods**, ensure you have the "SureCart configuration" selected as the default.

- You should now see the SureCart configuration set as the default.

Now, you can enable and use any of the available payment methods here!

### **Troubleshooting Checkout Errors**

If you still encounter checkout errors, follow these steps to troubleshoot:

- Click on the three dots and choose **Review transactions**.

Here, you'll be able to review how your payment methods appear. If any payment methods do not appear, this section will provide insights into the problem.

- Select the **Order amount and currency** tab.
- Enter the preferred location, amount, and currency.
- Click on the **Review** button.

- Stripe will show you the list of payment methods that do not appear and the reasons.

The first section also shows the payment methods that appear on checkout.

If the desired payment method is shown here but still doesn't appear on your checkout, here's what you can do:

- Go to **Transactions** and select any individual transaction.

- Copy the transaction ID.

- Go back to the Troubleshooting screen and select the **Transaction ID** tab.
- Paste the transaction ID that we copied and click the **Go** button.

This will show all payment methods that are displayed and not displayed for that particular transaction.

That covers everything you need to know to connect Stripe with SureCart. However, if you still have questions or encounter any issues, please don't hesitate to contact us.

We'll be glad to assist you with any inquiries or problems you may have.

### Frequently Asked Questions

**Can I Switch Payment Processors?**

Yes, you can switch to a different payment processor or connect a new Stripe account. It's important to understand how existing subscriptions and payment methods will be affected.

For detailed guidance, read: [Switching Payment Processors](https://surecart.com/docs/switching-payment-processors).

**Can I connect to a more than one Stripe account?**

You can connect multiple Stripe accounts, but only one can be active at a time.

To learn more about managing multiple accounts and the expected behavior of subscriptions, see: [Switching Payment Processors](https://surecart.com/docs/switching-payment-processors).


===== SOURCE: connection-link.md =====

---
source_url: https://surecart.com/docs/connection-link
source: surecart-kb
scraped: true
---

# How to Invite Others to Connect Payment Processors

Connecting payment processors can be challenging if you don't have direct access to the account. The "Create Connection Link" feature addresses this issue by enabling you to securely invite others to connect a payment processor on your behalf.

### **Creating the Invitation Link**

- Navigate to **SureCart > Settings > Payment Processors**, and select any of the available processors.
- Once on the platform, scroll down to the **Payment Processors** section.
- Click the **Create Connection Link** button at the bottom of the page.
- When the "Create Connection Link" window appears, locate the Processor Type dropdown.
- Click the dropdown and select the payment processor you want to generate the link for (e.g., Stripe, PayPal, Mollie).
- Check or uncheck the **Live Mode** box to determine whether the connection will process real transactions or remain in Test Mode.
- If you want the invitation link to be emailed directly to the recipient, ensure the **Send Email** box is checked. Enter the recipient's email address.
- Once all details are verified, click the **Create Connection Link** button to generate the link.

### **Share the Invitation Link**

After creating the connection link:

- Copy the invitation link by clicking the copy icon next to the link.
- Share the link with the intended user through the desired communication channel (e.g., email, chat, or message).
- Inform the recipient to check their email for the connection link and instructions.

### **Steps for Users to Connect the Processor**

After receiving the email or the invitation link:

- Open the browser using the provided link.
- Click the button that contains the name of the processor and the mode (e.g., Test Mode or Live Mode). For example, if "Stripe" was selected and set to Test Mode, the button will display **Connect to Stripe (Test Mode)**.
- Enter your processor account information in the provided fields.

Once the process is complete, you will see a confirmation message: "**Processor connected successfully!**"

### **Frequently Asked Questions**

**The PayPal linking is not working.**

When connecting to PayPal, after you see the message "You're ready to get paid with PayPal on [Your Store Name]!", you must click the "Return to [Your Store Name]" button at the bottom of that page. This action is essential to finalize the connection.

**Can I send the connection link to anyone, or do they need a SureCart account?**

The connection link can be sent to anyone who manages the payment processor account. They do not need to have an existing SureCart account.

**Does the connection link expire after a certain time?**

Yes, each generated connection link **expires after 6 hours**. If the link expires, you will need to generate a new one.

**What is the difference between connecting in Live Mode and Test Mode?**

**Live Mode** means the payment processor will fully process real transactions. **Test Mode** connections are for testing purposes only.

**Is it secure to share this connection link?**

The connection link provides a direct path for the recipient to connect their payment processor account without having to share sensitive login credentials.


===== SOURCE: coupon-included-urls.md =====

---
source_url: https://surecart.com/docs/coupon-included-urls
source: surecart-kb
scraped: true
---

# How to Include Coupons to Product URLs and Share With Users

Want to send customers product page links with coupons already applied? SureCart offers a straightforward solution to this.

You can simply do this by adding coupon codes at the end of the product page URLs.

Incorporating coupons directly into product URLs can offer significant advantages.

**For businesses:** it can increase sales conversions, make tracking of marketing campaigns simpler, enhance customer satisfaction, and provide seamless promotional opportunities. It allows for direct and personalized promotions, improving the page's visibility on search engines.

**For customers:** it offers convenience, immediate savings, and a smoother, more transparent shopping experience.

### How to Share a Product with Prefilled Parameters

Sharing a product link with an already-filled coupon code can make the purchasing journey smoother and more user-friendly. Here's a step-by-step guide to accomplish this:

- Navigate to your WordPress dashboard and select Products under SureCart.
- Identify and select the product you wish to share.
- Under the Pricing section, click on the 'Copy Links' button.
- Find the "Buy Link" field and click the 'Copy' button to obtain the URL.
- Paste the copied URL into your browser.

Example URL:

```
https://example.com/checkout/?line_items%5B0%5D%5Bprice_id%5D=1a830bba-ede0-4640-88ff-c1d5a94fe993&line_items%5B0%5D%5Bquantity%5D=1
```

### How to Insert Coupon Into the Product URL

- From SureCart, navigate to Coupons, select coupons, and copy the coupon code.

To embed the coupon code into the URL, append the parameter "**&coupon=YOUR_COUPON_CODE**" to the end of the product page's URL. For instance, if your coupon code is "**20-OFF-SECRET**", the appended portion would be "**&coupon=20-OFF-SECRET**".

Final URL:

```
https://example.com/checkout/?line_items%5B0%5D%5Bprice_id%5D=1a830bba-ede0-4640-88ff-c1d5a94fe993&line_items%5B0%5D%5Bquantity%5D=1&coupon=20-OFF-SECRET
```

Once the customer clicks on the shared link, they will be redirected to a checkout page with the coupon code pre-applied, making the purchasing process seamless and efficient.


===== SOURCE: create-affiliate-coupon-codes.md =====

---
source_url: https://surecart.com/docs/create-affiliate-coupon-codes
source: surecart-kb
scraped: true
---

# How to Create Affiliate Coupon Codes in SureCart

## Overview

This guide explains how to create and manage affiliate coupon codes in SureCart, enabling affiliates to distribute discounts while tracking commissions accurately.

## Create an Affiliate Coupon

**Prerequisites:** You must have affiliates added to your store first.

**Steps:**

1. Navigate to **SureCart > Coupons** and click **Add New**
2. Enter a coupon name, code, and desired discount amount
3. Select specific products for the coupon under **Product Restrictions** (leave empty to apply to all products)
4. Choose an affiliate from the **Link to Affiliate** dropdown
5. Click **Create Coupon**

When customers use this coupon, the selected affiliate receives a commission on the sale. The coupon will appear in that affiliate's profile at **SureCart > Affiliates**.

_Note:_ See the coupon creation documentation for additional details on discount setup.

## Tracking and Paying Affiliates

### Verify Affiliate Referrals

1. Go to **SureCart > Affiliates** and select the relevant affiliate
2. Check the **Referrals** tab to confirm successful purchases
3. The coupon usage count increments with each use
4. View all referrals at **SureCart > Affiliates > Referrals** to approve, deny, or delete entries

### Process Payouts

1. Navigate to **SureCart > Affiliates > Payouts** and click **Add New**
2. Select the affiliate and specify the payout period
3. Click **Create** to generate the payout with "Processing" status

### Zero Commission Referrals

Enable tracking of referrals earning zero commission at **SureCart Settings > Affiliates > Commissions & Payouts**.

## Frequently Asked Questions

**Can affiliate coupons be edited?**
Yes, changes apply only to new checkouts and don't affect existing orders.

**What happens if deleted?**
The coupon becomes unusable; past orders and commissions remain unchanged.

**Can multiple customers use the same coupon?**
Yes, unless usage limits are configured.

**Do changes affect previous commissions?**
No, updates only apply to future purchases.


===== SOURCE: create-coupons.md =====

---
source_url: https://surecart.com/docs/create-coupons
source: surecart-kb
scraped: true
---

# How To Create Coupons In SureCart

## Overview

SureCart enables merchants to create and manage discount coupons. The system supports various configuration options including discount types, duration settings, product restrictions, and redemption limits.

## Creating a New Coupon

Navigate to **SureCart > Coupons** in the WordPress dashboard and click **Add New**.

## Configuration Fields

**Coupon Name**: Internal identifier not visible to customers.

**Promotion Code**: Customer-facing code for checkout. Leave blank for automatic generation.

**Customer Restriction**: Optionally limit coupon to a specific customer via dropdown selection.

**Product Restrictions**: Restrict coupon to specific products, or leave blank for store-wide applicability. When a customer adds even just one of the products with the coupons restricted to the cart, the coupon is still applicable.

**Discount Amount**: Choose percentage or fixed dollar amount discount.

## Discount Duration Options

- **Forever**: Applies continuously
- **Once**: Single-use only
- **Multiple months**: Duration-based application varying by subscription type (monthly, weekly, or yearly subscriptions process differently)

## Redemption Limits

**Usage limit per coupon**: Maximum total uses across all customers

**Usage limit per customer**: Maximum uses per individual customer

**Minimum order subtotal**: Threshold amount required for coupon applicability

**End Date**: Expiration date and time (UTC+0)

Click **Create Coupon** to finalize.


===== SOURCE: create-customer.md =====

---
source_url: https://surecart.com/docs/create-customer
source: surecart-kb
scraped: true
---

# How to Create a SureCart Customer

## What is a SureCart Customer

A SureCart customer represents anyone who shops at a SureCart-powered online store. They browse products, add items to their cart, and complete secure transactions.

## How Customers are Created in SureCart

SureCart supports multiple customer creation methods:

### Automatic Creation During Checkout

When shoppers complete a purchase, SureCart automatically generates a customer account. This enables buyers to:

- Track order history
- Save payment and shipping information
- Receive personalized offers

### Manual Creation by Merchants

**From the Customer Menu**: Store owners can manually create customer accounts through the dedicated customer management area. This approach works well for prospects who have not yet made a purchase.

**During Manual Order Processing**: Merchants can create customer accounts while processing orders received through alternative channels (phone orders, etc.).

## Steps to Create a Customer from the Customer Menu

1. Navigate to your SureCart Dashboard and select "Customers"
2. Click the "Add New" button to begin creating a new customer
3. Complete the required fields:
   - Customer Name
   - Customer Email
4. Optionally enable "Test mode" for this customer
5. Click "Create" to finalize the account

SureCart automatically generates an associated WordPress user account linked to the new customer profile. This integration enables seamless account management and order tracking across both platforms.


===== SOURCE: create-discount-coupons.md =====

---
source_url: https://surecart.com/docs/create-discount-coupons
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Revenue Boosters](https://surecart.com/docs-category/revenue-booster/)/How to Create Discount Coupons

# How to Create Discount Coupons

Do you want to offer discounts or special deals to your customers by generating exclusive coupon codes? SureCart makes this process simple!

With SureCart, you can create coupon codes that customers can use to receive discounts when making purchases from your SureCart store. It's a fantastic way to attract customers and boost your sales.

So, if you'd like to create coupons for your SureCart store, follow the steps provided in this [article](https://surecart.com/docs/create-coupons/).


===== SOURCE: create-donation-form.md =====

---
source_url: https://surecart.com/docs/create-donation-form
source: surecart-kb
scraped: true
---

# How to Create a Donation Form in SureCart

## Overview

SureCart enables users to create customizable donation forms supporting both one-time and recurring contributions. The platform offers significant design flexibility for tailoring forms to match your website's aesthetic.

## Key Benefits of Recurring Donations

When an individual commits to recurring contributions, it signifies their long-term support and allows for better planning. This feature helps organizations secure consistent funding while improving donor retention.

Donation forms serve various organizations including charities, political movements, and content creators.

## Creation Steps

### Initial Setup

1. Create a new page or post
2. Insert the Checkout Form block
3. Name your form (e.g., "Donation form")
4. Select the Donation form template
5. Choose your Pay What You Want product

### Customization Options

- Edit donation amount labels and values
- Adjust column layouts
- Add custom price tiers
- Modify recurring donation options
- Change background colors and styling

### Publishing

After configuration, switch to Test mode and publish your form to make it live on your website.

The completed form displays donation options with clear labeling, allowing donors to select amounts and contribution frequency before checkout.


===== SOURCE: create-invoices.md =====

---
source_url: https://surecart.com/docs/create-invoices
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Orders](https://surecart.com/docs-category/orders/)/How to Create invoices in SureCart

# How to Create invoices in SureCart

In this article, we'll help you understand how you can create invoices in SureCart in a detailed yet simple manner.

## How to Create a Invoice?

- Go to the WordPress Dashboard and select SureCart > Orders > Invoices from the menu. Then click on the "Add New" button in the top left corner.

- You'll be directed to a new page where you can fill all the details of the invoice.

- First, click on "Add Product" to [add the product](https://surecart.com/docs/create-product/) to your invoice.

- **Products** - You can use the search function to choose a product from the list.

- Once the product is added to the invoice, you can change the quantity or add more products.

- **Address** - In the Address field, provide all relevant information related to the address.

- **Payment** - In the Payment section, enter the coupon code if you wish to apply a discount to the invoice.

- **Additional Information** - At the end you have an option to add additional information such as:
  - **Memo** - This is displayed in the memo section of your payment page, invoices, and receipts.
  - **Footer** - The footer message is displayed at the bottom of your invoices and receipts.

- **Invoice Summary** - In this section, you can specify various important parameters related to your invoice:
  - **Status** - While creating your invoice it will be in the Draft mode, once you save it will be published.
  - **Issue Date** - Select the date on which the invoice is issued or released to ensure accurate record-keeping and payment tracking.
  - **Due Date** - Choose the due date for the invoice, which indicates when payment is expected.

- **Customer** - Use the search function to find the user for whom you wish to create this invoice. Once you've located them, click on their name to select it.

- **Tax** - In the Tax section you can select to charge tax for this invoice or not.

- **Tax Inclusion** - In this section, you can specify whether the tax is included or excluded from the invoice.

- **Tax ID** - You can input the Tax ID in this field.

- **Create Invoice** - In this final step, review your information carefully, and if you are confident that everything is correct, you can click the Create Invoice button to generate the invoice.

Congratulations! You have successfully created your invoice.

Once you publish invoice several things will happen:

- Email will be sent to the customer
- You will be able to share invoice by the link
- Your Invoice will get the number
- Your invoice will get Shipping and Billing address


===== SOURCE: create-product.md =====

---
source_url: https://surecart.com/docs/create-product
source: surecart-kb
scraped: true
---

# How to Create Products in SureCart

In this article, we'll help you understand how you can create products for your SureCart account in a detailed yet simple manner.

### **Types of Products You Can Create/Sell with SureCart**

Currently, SureCart offers the ability to create three types of products:

**Physical Products**: These are tangible items that require shipping and order fulfillment options to be enabled.

**Digital Products**: If you have downloadable content, such as e-books or software, you can create downloadable products.

**Subscription Products**: SureCart also supports subscription-based products. You can create products for which you want to collect monthly/weekly/yearly recurring payments. For example – streaming services, billing systems for software, monthly course fees, etc.

## How to Create a Product?

If you're on a free SureCart plan, you can add up to 100 products, but if you upgrade to a paid plan, you can create unlimited products.

- Go to the WordPress Dashboard and select **SureCart > Products** from the menu. Then click on the "Add New" button in the top left corner.
- You'll be directed to a new page where you can enter your product name. Fill in the Product Name field and click the "Create" button.
- On the Edit Product page, add all details related to the product like name, and description.
- Add images that you want to display on the purchase page for this product.
- Decide pricing for the product. You can set up pricing for different types of products like One-time/Subscription/Installment/Trial.
- If you're creating a digital product like an E-book, you can add product download links for this product. If not, you can skip this step.
- If you want to take action in other apps when someone buys this product, you can add integrations to this product. For example – If you want someone to get enrolled in a LearnDash course when they buy this product, you can add LearnDash integration.
- Next, if you want to generate and send license keys to people who buy your product, you can add licensing to this product.
- For SEO purposes, you can specify the page title and meta description for this product that can be displayed in search engine results.
- Then you can decide the shipping settings for this product. If it's a physical product, you can add the weight of the product so the shipping amount is calculated as per your shipping profile.
- Next comes tax, if you want to collect taxes for this product, you can enable the tax option.
- If you wish to add purchase limits per customer for this product, you have the option to set limits. For example – if you want 1 person to buy this product once, simply add '1' in the field.
- At last, you can set up publishing settings based on your preference.
- Click on the 'Save Product' button.

Congratulations! You have successfully created your product. Now you can share this product with anyone using instant checkout pages, or simply link the pricing of this product as buy buttons using shortcodes, hyperlinks, etc.


===== SOURCE: creating-and-managing-variants.md =====

---
source_url: https://surecart.com/docs/creating-and-managing-variants
source: surecart-kb
scraped: true
---

# Creating and Managing Variants in SureCart

## Overview

Product variants allow customers to choose from options like colors and sizes without requiring separate product listings.

**Important Limitation:** SureCart supports up to 300 variations per product. However, adding more than 200 variations may lead to PHP memory or performance issues on some hosting environments.

## How to Create Variations

1. Navigate to the "Variants" section below "Inventory"
2. Click "Add Options Like Size or Color"
3. Enter an "Option Name" (e.g., "Color")
4. Add "Option Values" (e.g., "White," "Black")
5. Click "Done"
6. Click "Add More Options" for additional variant types
7. Enter details for new options (e.g., sizes S, M, L)
8. Click "Done" to confirm

The system automatically generates a table displaying all variant combinations.

## Customizing Variations

Once variants are created, you can:

- **Assign images:** Click image placeholders to upload variant-specific photos
- **Set prices:** Enter custom prices for individual variants (only available if the product has single pricing)
- **Manage inventory:** Adjust stock quantities per variant
- **Add SKUs:** Create unique identifiers like "TSHIRT-WHITE-S"

## Deleting and Adding Variants

**To delete a specific variant:**
1. Click the three-dot menu next to the variant
2. Select "Delete"
3. The variant displays crossed out until you save
4. Click "Save Product" to confirm deletion

**To add a custom variant:**
1. Click "Add Variant" at the top right
2. Enter all variant details
3. Click "Add Variant" to confirm
4. Click "Save Product" to save changes

## Customizing the Product Page Variant Block

1. Navigate to "Edit template" in the product screen
2. Click the "Product Variants" block
3. Adjust settings in the right column to match your brand

## Creating Manual Orders With Variants

When creating manual orders, variant products display stock quantities and variant names alongside standard order information.

## Upgrading Variant Subscriptions

Customers can upgrade or downgrade variant subscriptions following standard upgrade procedures, with an additional "Choose a Variation" step required during the process.

## Frequently Asked Questions

**Variant Limits:** SureCart allows up to 300 variants per product.

**Mix and Match:** Customers can select multiple variants of the same product in a single order.

**Variant Images:** Yes, you can assign unique images to specific variants through variant image documentation.


===== SOURCE: creating-custom-buy-links.md =====

---
source_url: https://surecart.com/docs/creating-custom-buy-links
source: surecart-kb
scraped: true
---

# Creating Custom Buy Links

While SureCart provides copy/paste buy links when you create your product prices, sometimes you may want to create custom purchase links that allow your users to purchase a product.

You can even specify several different products or prices and the quantities for each. You can accomplish this using URL parameters.

### Creating The Link

In this section, we'll walk you through the process of creating custom purchase links for your products.

#### Finding the Price ID

The first step is to find the **price ID** that you want to use for the line item. You can do this by navigating to your Edit Product page and clicking on **Copy Links** next to the price.

This will open a new section that contains all of the links associated with your product. Next, click **Copy** next to the **Price ID** box.

#### Creating the URL

To add line items, you will want to use the _line_items_ parameter in the URL. The URL accepts multiple options, so it will follow the format:

```
https://yoursite.com/checkout?line_items[0][price_id]=5366e5a3
```

Replace 'https://yoursite.com/checkout?' with your actual WordPress site link.

Enter the price id you copied after "\[price_id\]= "

When you click on the newly created link, it will redirect you to the usual product page.

#### Changing the quantity

You can also specify the quantity of a line item in the URL as well. This would give the line item a quantity of "2".

```
https://yoursite.com/checkout?line_items[0][price_id]=5366e5a3&line_items[0][quantity]=2
```

#### Adding multiple items

You may want to add more than a single line item to the checkout. To do that, you can do this:

```
https://yoursite.com/checkout?line_items[0][price_id]=5366e5a3&line_items[1][price_id]=402d8e25
```

As you can see, we are adding an additional _line_items_ parameter, but instead of using the "key" \[0\], we are using \[1\] to indicate it's a separate line item.


===== SOURCE: custom-events-with-gtm.md =====

---
source_url: https://surecart.com/docs/custom-events-with-gtm
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Track Custom Events with Google Tag Manager

# How to Track Custom Events with Google Tag Manager

In this article, we'll guide you through the process of sending tracking events from your SureCart store to Google Analytics using Google Tag Manager (GTM).

To connect SureCart with Google Analytics, you can use the [Google Site Kit plugin](https://wordpress.org/plugins/google-site-kit/) on your WordPress site.

### Why Connect SureCart with Facebook Pixel & Google Analytics?

Connecting SureCart with Facebook Pixel (FB Pixel) and Google Analytics (GA) is a great way to track your e-commerce sales and marketing performance.

With Facebook Pixel, you can track website visitors and their interactions with your Facebook ads, create more targeted ads, and optimize your campaigns.

Google Analytics provides insights into your website traffic, visitors' locations, purchase behaviors, etc. You can use this information to improve your website's performance and optimize your overall business strategy.

### **Events That Can Be Tracked**

SureCart automatically broadcasts the "Add To Cart" and "Purchase" events for Google Analytics. This means that if you want to track these events, you just need to install the Google Site Kit plugin on your WordPress. No additional configuration is needed.

Here's a list of additional events you can broadcast through a custom code:

| **Event**             | **Event Name**       | **Description**                                                        |
| --------------------- | -------------------- | ---------------------------------------------------------------------- |
| scAddedToCart         | Added to Cart        | Triggered when a customer adds an item to their shopping cart.         |
| scRemovedFromCart     | Removed from Cart    | Triggered when a customer removes an item from their shopping cart.    |
| scViewedCart          | Viewed Cart          | Triggered when a customer views their shopping cart.                   |
| scProductViewed       | Product Viewed       | Triggered when a customer views a product page.                        |
| scCheckoutInitiated   | Checkout Initiated   | Triggered when a customer begins the checkout process.                 |
| scCheckoutCompleted   | Checkout Completed   | Triggered when a customer successfully completes the checkout process. |
| scShippingInfoAdded   | Shipping Info Added  | Triggered when a customer adds or updates their shipping information.  |
| scPaymentInfoAdded    | Payment Info Added   | Triggered when a customer adds or updates their payment information.   |
| scTrialStarted        | Trial Started        | Triggered when a customer starts a free trial.                         |
| scSubscriptionStarted | Subscription Started | Triggered when a customer starts a paid subscription.                  |

### How to Connect SureCart Store to Google Analytics

If you did not connect your Google Analytics account with the Google Site Kit plugin upon installation, then you can follow the steps below.

- In the Site Kit setup wizard, you'll have an option to connect to Google Analytics. Click on the **Connect Service** button for Google Analytics.
- Follow the prompts to grant permission to access your Google Analytics account.
- Choose the Google Analytics property (website) you want to link to your WordPress site.
- Click **Configure Analytics** to finish the setup.

### How to Connect SureCart Store to Google Tag Manager

Once Google Analytics is connected to your Google Site plugin, go back to the Site Kit dashboard.

- From the **Settings**, navigate to **Connect More Services**.
- Locate **Tag Manager** in the list of services and click on it.
- Follow the prompts to grant permission to access your Google Tag Manager account.
- Select the Google Tag Manager container you want to use with your WordPress site.
- Click **Configure Tag Manager** to finish the setup.

After completing these steps, you should see a dashboard within Google Site Kit that displays information about your website's performance, including data from Google Analytics and Google Tag Manager.

From here, you will need to "forward" any events from Google Tag Manager to GA4. To do this add a new "Tag" to your workspace, then select your existing Google Analytics GA4 Pageview configuration tag, then use `{{Event}}` for the Event name.


===== SOURCE: custom-thank-you-page.md =====

---
source_url: https://surecart.com/docs/custom-thank-you-page
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How To Set Up a Custom Thank You Page For a Form

# How To Set Up a Custom Thank You Page For a Form

This document explains how to create and assign a custom Thank You page for purchases made through a SureCart form, replacing the default post-purchase modal.

### **Requirements**

- An existing checkout form
- WordPress admin access
- SureCart installed and activated

### **Create a Custom Thank You Page**

Follow the steps below to create a custom Thank You page.

- Go to **WordPress Dashboard → Pages → All Pages**.
- Click **Add New**.
- Enter a name for the page.
- Design the page using the available SureCart blocks.

#### **Optional: Add an Order Confirmation Block**

You can include order details on the Thank You page.

- Click the **+** button to add a new block.
- Insert the **Order Confirmation** block.
- Customize the text, call-to-action, and layout as needed.
- Click **Publish** to save the page.

### **Assign the Custom Thank You Page to a Form**

After creating the page, assign it to a checkout form.

- Go to **WordPress Dashboard → SureCart → Custom Forms**.
- Select the form you want to edit.
- Click the form header to open the checkout form settings.
- Enable the **Thank You Page** option.
- Select the custom Thank You page you created.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, customers who complete a purchase through the selected checkout form will be redirected to the custom Thank You page instead of seeing the default confirmation modal.

### **Notes and Limitations**

- The default modal will continue to appear for forms without a custom Thank You page assigned.
- The custom Thank You page applies only to the form where it is enabled.
- Existing orders are not affected by changes to the Thank You page configuration.

### **FAQ**

**Can I use a different Thank You page for each form?**

Yes. Each checkout form can have its own custom Thank You page.

**Does changing the Thank You page affect past purchases?**

No. Changes apply only to future purchases.

**Can I include order details on the Thank You page?**

Yes. The Order Confirmation block can be added to display order information.


===== SOURCE: customer-dashboard-shortcodes.md =====

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


===== SOURCE: customer-email-notifications.md =====

---
source_url: https://surecart.com/docs/customer-email-notifications
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Manage Customer Email Notifications

# How to Manage Customer Email Notifications

SureCart gives you the power to control how emails are sent to SureCart store owners and customers. This helps make your business run smoother.

You can significantly improve your customers' shopping experience by deciding which emails they receive. It's an easy way to ensure your customers only receive email notifications that are important and relevant.

In this article, we will learn how to enable or disable these customer notifications.

Some of the emails that customers receive when different events happen are:

- Product Access Emails

- Order Confirmation Emails

- Free Order Emails

- Refund Emails

- Subscription Renewal Emails

- Subscription Cancellation Notifications

- Subscription Reminder Notifications

- Subscription Recovery Emails

## **How to Enable/Disable Customer Notifications**

You can control customer notifications via the SureCart Settings. Here's how:

- Login into your WordPress website and click on SureCart.

- Click on Settings.

- Click on Notifications.

- Here, you can turn on or off various types of customer notifications by toggling and un-toggling the respective email notifications.

- Once you've selected which notifications to turn on, click on the 'Save' button.

Now, your customers will only receive active notifications!

SureCart also sends notifications to the SureCart store owners. To learn more about managing email notifications sent to store owners, click [here](https://surecart.com/docs/how-to-manage-notifications-on-surecart/).


