# SureCart - Base de connaissances (partie 3 sur 4)


===== SOURCE: integrate-affiliatewp-with-surecart.md =====

---
source_url: https://surecart.com/docs/integrate-affiliatewp-with-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Integrate AffiliateWP with SureCart

# How to Integrate AffiliateWP with SureCart

SureCart has its own [affiliate platform](https://surecart.com/affiliate/), offering rewards to affiliates for customer referrals or successful sales. Affiliates also receive unique tracking links to ensure accurate compensation for their efforts here.

While we highly recommend using our affiliate platform to boost your affiliate experience, SureCart also offers you the option to integrate itself with [AffiliateWP](https://affiliatewp.com/).

Let's see how you can do this easily!

- Download and activate the [AffiliateWP plugin](https://affiliatewp.com/) on your WordPress dashboard.

- From your dashboard, navigate to the AffiliateWP **Settings**.

- Move to the **Integrations** section and check the box next to **SureCart**. This will enable the SureCart integration with AffiliateWP.

- Click on the **Save Changes** button.

Congratulations! Your SureCart store is now successfully connected with AffiliateWP.

That's it. We hope the above guide helped you. If you face any issues during the integration process, please free to reach out to our support team.


===== SOURCE: integrating-analytics.md =====

---
source_url: https://surecart.com/docs/integrating-analytics
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/General Support Guide for Integrating Analytics with Any Solution

# General Support Guide for Integrating Analytics with Any Solution

Many SureCart users want to integrate their store analytics with platforms beyond Google Analytics, such as Facebook Pixel, Fathom, or custom analytics solutions. SureCart provides flexibility for tracking a variety of events and data points to help store owners analyze their business performance across various platforms.

This guide will outline the general steps for integrating SureCart with any analytics platform.

### **Understanding the Basics**

SureCart automatically tracks several key events related to customer behavior in your store. These include:

- Add to Cart
- Checkout Initiated
- Purchase Completed
- Subscription Started

While SureCart offers built-in integrations for popular platforms like Google Analytics and Facebook Pixel, you can integrate other solutions by leveraging SureCart's ability to fire custom JavaScript events or send data to third-party platforms via webhooks or API connections.

### **General Steps for Analytics Integration**

**Step 1: Identify the Key Events to Track**

Decide which events are critical to your store. Some common events include:

- View Product
- Add to Cart
- Begin Checkout
- Purchase Completed
- Subscription Start

SureCart fires these events automatically, and you can listen to them or customize the events you want to track.

Here is a table for all the events that can be tracked in SureCart:

| **Event**             | **Event Name**       | **Description**                                                                       |
| --------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| scAddedToCart         | Added to Cart        | Triggered when a customer adds an item to their shopping cart.                        |
| scRemovedFromCart     | Removed from Cart    | Triggered when a customer removes an item from their shopping cart.                   |
| scViewedCart          | Viewed Cart          | Triggered when a customer views their shopping cart.                                  |
| scProductViewed       | Product Viewed       | Triggered when a customer views a product page.                                       |
| scCheckoutInitiated   | Checkout Initiated   | Triggered when a customer begins the checkout process.                                |
| scCheckoutCompleted   | Checkout Completed   | Triggered when a customer successfully completes the checkout process.                |
| scShippingInfoAdded   | Shipping Info Added  | Triggered when a customer adds or updates their shipping information during checkout. |
| scPaymentInfoAdded    | Payment Info Added   | Triggered when a customer adds or updates their payment information during checkout.  |
| scTrialStarted        | Trial Started        | Triggered when a customer starts a free trial for a subscription-based product.       |
| scSubscriptionStarted | Subscription Started | Triggered when a customer starts a paid subscription for a product.                   |

**Step 2: Set Up Your Analytics Platform**

Each analytics platform will have a method for tracking events or actions on your site. Make sure your analytics platform is properly installed on your site, typically by embedding a tracking code snippet in the header of your WordPress site.

**Step 3: Listen for SureCart Events**

SureCart triggers several events when actions are performed by customers. You can use JavaScript event listeners to capture these events and send data to your preferred analytics platform.

For example, the following event listener captures when the checkout process is completed:

```javascript
window.addEventListener("scCheckoutCompleted", function (e) {
  const checkoutData = e.detail; // Checkout data is available here.
  // Use the data to send to your analytics platform
});
```

**Step 4: Send the Data to Your Analytics Platform**

Once you capture the event, the next step is to send the relevant data to your analytics platform. This can vary depending on the platform you're using. For example, for Facebook Pixel, Fathom, or custom solutions, use their respective JavaScript APIs or HTTP requests.

**Step 5: Test and Verify**

After setting up the event listeners and data-sending functions, perform actions on your SureCart store (like adding items to the cart or completing a purchase). Use your analytics platform's dashboard or logs to verify that the events are tracked correctly.

### **Additional Tools for Integration**

If you need more flexibility, consider the following options:

- **Webhooks**: SureCart supports sending data via webhooks, allowing you to push event data to a variety of endpoints. You can configure webhooks in SureCart's settings to notify your analytics solution when certain actions occur.

- **API Integrations**: If your analytics platform provides an API, you can integrate it directly with SureCart using custom code. Make API calls from your store to log events and track actions.

SureCart makes it easy to integrate with any analytics platform. By leveraging custom JavaScript and event listeners, you can capture essential user interactions and send them to your analytics solution of choice.

For more detailed tracking or custom requirements, consider working with a developer or using available SureCart webhooks to automate event tracking.

If you need help with specific integrations, check out SureCart's [Developer Documentation](https://developer.surecart.com/) or consult the community for support.


===== SOURCE: invalid-credentials-paypal-test-mode.md =====

---
source_url: https://surecart.com/docs/invalid-credentials-paypal-test-mode
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Invalid Credentials Error while Using PayPal Test Connection with SureCart

# Invalid Credentials Error while Using PayPal Test Connection with SureCart

You can easily [integrate SureCart with PayPal](https://surecart.com/docs/connect-paypal/), which allows you to accept payments from your customers.

However, when testing the SureCart-PayPal connection, you may encounter an "Invalid Credentials Error."

This article will explain the causes of this error and how to fix it.

## Causes of Invalid Credentials Error

When the login information entered to establish the connection between SureCart and PayPal is incorrect, the "Invalid Credentials Error" occurs. This error can happen for several reasons, including the following:

### Incorrect PayPal Login Credentials

If the PayPal email address or password that you entered is incorrect, you will not be able to establish a connection with SureCart. It is essential to double-check your login credentials to ensure that they are correct.

If you do not remember your PayPal credentials, you can reset them [here](https://www.paypal.com/authflow/password-recovery/).

### The Test Account is Not Set Up

To test the connection between SureCart and PayPal, you need to have a PayPal Sandbox account set up. If you have not set up a Sandbox account, you will not be able to establish a connection.

Follow these steps to set up a sandbox Paypal account:

- Navigate to the [Sandbox page](https://www.sandbox.paypal.com/signin) of PayPal and create an account. It is free and super easy to set up.

- On your WordPress dashboard, navigate to SureCart **Settings** > **Payment Processors,** and then **Paypal**.

- Click on the **PayPal** payment processor here.

- On the Processors page on the SureCart App Dashboard, click **PayPal**.

- From here, click on the drop down on the top-right and select **Test Mode**.

- This will automatically redirect you to the Sandbox page of PayPal. Enter the email address and password of your newly created Sandbox account.

That will do the trick. You will be able to log in to your PayPal sandbox account.

Hope this guide helped. If you are still facing the same issue, please contact our support team. We're always here to help!


===== SOURCE: inventory-management.md =====

---
source_url: https://surecart.com/docs/inventory-management
source: surecart-kb
scraped: true
---

# Inventory Management in SureCart

This article will teach you how to keep track of the products you have for sale in SureCart. By the end, you'll know how to make sure you can limit the number of items you can sell to ensure you have the proper inventory.

### **What is a Product Inventory and Why is it Important?**

Product inventory, in short, refers to the quantity of items available for sale. In SureCart, you can track the quantity and add a SKU (Stock Keeping Unit) to your products.

Inventory management is crucial because it ensures that products are available when customers want to purchase them. This prevents stockouts and overstock situations, which can impact sales and customer satisfaction.

### **How to Manage Inventory in SureCart**

To manage your product's inventory in SureCart:

1. Go to the menu **SureCart > Products**
2. On the Products page, find and click the "Edit" button for the product you want to manage inventory for.
3. Scroll down to the "Inventory" section on the Edit Product page.
4. Click on the "Track Quantity" toggle to start tracking inventory for this product.
5. If you wish to permit selling items even when they are out of stock, click on the corresponding toggle to activate this feature.
6. In the "Available Stock" field, enter the quantity of the product that you have in stock.
7. You can also make stock adjustments by clicking on the pencil icon located to the right of the "Available Stock" field.

### **Stock Adjustment options**

Here's what each adjustment means:

**Adjust By**: This will either add or decrease the exact amount of stock you enter in both Available and On Hand. For example, if your store contains 5 items Available and 5 On Hand, and you enter 2 in the "Adjust By" field, the Available and On Hand will update to 7.

**Available**: This is the amount of stock that can be sold. For instance, let's say you have 3 products in stock and you sold 1 item, but have not fulfilled or shipped anything. Now, only 2 are "Available" to be sold, and 3 are "On Hand". This is because you still have 3 items at your location, but only 2 are available for sale.

**On Hand**: These are the items that are physically at your location. This is made up of the total of sold and unsold inventory that has not yet been fulfilled. When the order is fulfilled, the On Hand decreases.

### **SKU or Stock Keeping Unit**

An SKU is like a special name or code for a product that helps stores keep track of what they have. It's like a product's ID number.

1. In the SKU field, type your product SKU.
2. Click on the "Save Product" button to save your progress.

### **Frequent Asked Questions**

**In which case a product can have a negative stock?**

In two scenarios, a product can result in a negative stock. The first occurs when a merchant enables "Allow Out of Stock Selling" in the Inventory section on the Edit Product page. The second situation arises from recurring purchases, such as subscriptions or installments.

Even if selling is permitted in both scenarios, SureCart will restrict merchants from fulfilling these items to prevent potential inventory complications.


===== SOURCE: invite-team-members.md =====

---
source_url: https://surecart.com/docs/invite-team-members
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Invite Team Members To Your SureCart Store

# How to Invite Team Members To Your SureCart Store

In SureCart, Team Members are like co-workers, who assist the store owner in running SureCart store.

Only the admins can invite team members to help ensure the store's smooth operation and assign them specific roles and responsibilities. This ensures they only have access to the necessary settings and options for your store.

For instance, you can add an accountant who can oversee the financial aspects, check order history, and manage subscriptions. However, they are unable to modify products or alter the website's appearance.

Similarly, you can add other team members to your SureCart store with [different roles and permissions](https://surecart.com/docs/user-roles-and-permissions/) to run your store.

Note: To invite more than 3 members, you need to [upgrade your SureCart plan](https://surecart.com/docs/how-to-upgrade-your-stores-on-surecart/).

So if you have the right plan, you can follow these steps to invite team members to your SureCart store.

### How to Invite Team Members to SureCart

As we mentioned before, only those with the Admin role can invite new team members.

- Log in to SureCart at [app.surecart.com](http://app.surecart.com/).

- Select the organization.

- Navigate to sidebar and choose **Members**

- Click on the **New Invite** button to invite new users.

- In the popup window provide the Email address of the new member.
- define the role, **Member** to simply view and make simple changes, or the store or **Admin** with all privileges.
- Define in which store you want new members to work in the organization.
- Store edit permission – Grants complete editing access to all assigned stores, allowing updates to store settings, member invitations, test data purging, and more.

Once you hit the **Send Invitation** button, SureCart will send an email invite to the person to join your store as a member/admin/developer.

They can simply accept this invitation and manage your store.

- After accepting the invite, the user will be prompted to sign up or log in to SureCart.

In case, a team member doesn't get the invite for some reason, you can send it again by clicking on the **Resend** button in the **Invites.**

You can also **Delete** the invite if it isn't accepted yet.

Adding team members with SureCart is very straightforward. But If you have any questions, please feel free to reach out to us through our [support portal](https://surecart.com/support/open-a-ticket).


===== SOURCE: is-not-a-valid-json-response.md =====

---
source_url: https://surecart.com/docs/is-not-a-valid-json-response
source: surecart-kb
scraped: true
---

# Fixing the "This response is not a valid JSON response" Error

## Overview

This error appears when using the SureCart checkout form on WordPress sites. The guide outlines potential causes and solutions.

## Reason 1: REST API Outages in WordPress

The REST API serves as the communication channel between SureCart and your WordPress installation. If disabled or encountering errors, it can prevent valid JSON responses.

**How to check:**

- Navigate to Tools > Site Health in the WordPress Dashboard
- Look for issues mentioning REST API or JSON responses
- If REST API is disabled, re-enable it through settings or deactivate plugins blocking it

## Reason 2: Server Firewall Blocking REST API

Firewalls and security plugins may mistakenly identify REST API requests as threats, blocking or altering them.

**How to check:**

- Access your hosting dashboard or server settings
- Review firewall logs for blocks corresponding to error timestamps
- Whitelist necessary URLs or adjust firewall settings accordingly
- Contact hosting support if you need assistance with firewall configuration

## Reason 3: WP_DEBUG Interference

Having WP_DEBUG enabled on a live environment can cause unnecessary messages to be output in API responses, potentially disrupting response structure.

**How to disable:**

1. Access your website root directory via FTP or file manager
2. Edit the wp-config.php file
3. Find the WP_DEBUG constant set to true
4. Change the value to false
5. Save changes

## Additional Recommendations

Regularly check the Site Health page in your WordPress Dashboard to identify potential REST API issues or other critical concerns. If problems persist after implementing these solutions, contact SureCart support or consult a developer for advanced troubleshooting.


===== SOURCE: learndash-courses-and-groups.md =====

---
source_url: https://surecart.com/docs/learndash-courses-and-groups
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Sell LearnDash Courses and Groups with SureCart

# How to Sell LearnDash Courses and Groups with SureCart

Selling online courses is a big deal. SureCart attempts to make it even better.

With features designed to improve LearnDash course sales, this guide will walk you through the integration process and highlight the practical advantages of integrating SureCart with LearnDash.

## **Why Connect SureCart with LearnDash?**

Integrating SureCart with LearnDash is a smart move for several reasons.

SureCart easily integrates with LearnDash, providing course creators with multiple features to sell their LearnDash courses to a larger audience.

SureCart also extends payment options beyond LearnDash, allowing users to offer payment plans. Payment plans are not available by default in LearnDash. This flexibility caters to a wider customer audience, making courses more financially accessible.

This integration also simplifies the process of upgrading to higher-priced plans or different terms.

Along with these, SureCart also provides course groups, discounting rules, automated tax calculations, and collection, and much more.

## **Integrating LearnDash Courses/Groups With SureCart**

Integrating Learndash with SureCart is a simple process.

- In SureCart, navigate to **Products** and select the product you want to edit. You can also create a new product and edit it.
- Here, scroll down and click on **Add New Integration**.

- Here, select LearnDash Courses or [LearnDash Groups](https://www.learndash.com/support/docs/users-groups/groups/group-courses/) as per your need. You can add as many courses or groups as you want.

- Now, select the course you would like to add and click on the **Add Integration** button.

- You can also remove these integrations by clicking on three dots and selecting **Delete**.

Thats it! Enrolling in your course just got super easy for customers.

## **Refunding and Revoking Course Access**

In many situations, you may want to revoke and refund access for certain Learndash customers. SureCart allows you to do this:

- In SureCart, go to **Orders**, and find the relevant order.

- Click on the **Revoke** button. This removes customers from courses or groups.

- You can also **Refund** the order. Do remember that refunding orders does not revoke the access to these courses for your customers.

SureCart with LearnDash makes selling courses super easy. Providing an improved experience that's better for customers as well as course owners.

We hope this guide helped you. If you have any questions, please don't hesitate to reach out to our support team. We're here to help!


===== SOURCE: licensing-setup-and-functionality.md =====

---
source_url: https://surecart.com/docs/licensing-setup-and-functionality
source: surecart-kb
scraped: true
---

# Understanding SureCart Licensing: Setup and Functionality

## Overview

SureCart's licensing system enables plugin and theme developers to manage product access and updates. The system uses the WordPress SDK and a release.json file to handle license activation, verification, and automatic updates.

## Key Components

### WordPress SDK

The WordPress SDK functions as a toolkit that allows plugins and themes to implement licensing by:
- Handling licensing verification (checking if users have a valid license)
- Facilitating automatic updates for licensed users
- Simplifying license activation through license codes

### Release.json File

This configuration file serves as an identity document for your plugin/theme, containing:
- Plugin/theme name and version information
- WordPress and PHP compatibility requirements
- Changelog and description sections
- Update management metadata

## Setup Process

### Creating a Simple Plugin

1. Create a PHP file with plugin header information
2. Include the WordPress SDK (see source_url for code snippet)
3. Initialize the licensing client with your plugin name and public token
4. Add settings page for license management

### Plugin Structure Requirements

Your plugin folder should contain:
- Main plugin PHP file
- wordpress-sdk folder (uncompressed from GitHub)
- release.json configuration file

### Enabling Licensing in SureCart

1. Create or edit a product in your SureCart store
2. Upload your plugin file to the Downloads section using "Secure Storage"
3. Enable the "Enable license creation" toggle
4. Set desired activation limits
5. Select the plugin file as "Current Release"
6. Save the product

## Testing and Activation

Customers can:
1. Purchase the product
2. Access their license key through the Customer Dashboard
3. Download the plugin file
4. Activate the license in their WordPress site's license settings
5. Receive automatic update notifications when new versions are available

## Plugin Updates

To release updates:
1. Increment the version number in both the plugin PHP file and release.json
2. Recompress and upload the updated plugin to your product
3. Set it as the current release
4. Customers automatically receive update notifications in their WordPress dashboard

## Merchant Visibility

Store owners can monitor license usage through the SureCart Licenses menu, viewing activation details and usage statistics for distributed licenses.


===== SOURCE: light-and-dark-logo.md =====

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


===== SOURCE: lsp-config.md =====

---
source_url: https://surecart.com/docs/lsp-config
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Configuring LiteSpeed Cache for SureCart

# Configuring LiteSpeed Cache for SureCart

SureCart uses WordPress REST API endpoints and core scripts to deliver real-time cart data, customer information, product details, and checkout flows. Improper caching configuration can cause outdated information, broken checkout forms, or missing cart updates.

## Requirements

- LiteSpeed Cache plugin installed and activated
- SureCart plugin installed and activated

## Step 1: Exclude REST API Requests from Caching

Go to **WordPress Dashboard → LiteSpeed Cache → Cache → Excludes**.

Under **Do Not Cache URIs**, add:

```
/wp-json/*
```

Click **Save Changes**.

## Step 2: Prevent Deferring of Core WordPress Scripts

SureCart depends on core WordPress scripts (`wp-api-fetch`, `wp-a11y`, `wp-i18n`, `wp-url`, `dom-ready`, `hooks`).

**Option A: Disable JS Deferral Completely**

Go to **LiteSpeed Cache → Page Optimization → JS Settings**, set **Load JS Deferred** to **Off**, click **Save Changes**.

**Option B: Exclude Specific Scripts from Deferral**

Under the **Tuning** tab, add to **JS Excludes**:

```
/wp-includes/js/dist/api-fetch.min.js
/wp-includes/js/dist/a11y.min.js
/wp-includes/js/dist/i18n.min.js
/wp-includes/js/dist/url.min.js
/wp-includes/js/dist/dom-ready.min.js
/wp-includes/js/dist/hooks.min.js
```

## Step 3: Disable JavaScript Combining

Go to **LiteSpeed Cache → Page Optimization → JS Settings**, set **Combine JS Files** to **Off**, click **Save Changes**.

## Step 4: Exclude Dynamic SureCart Pages from Caching

Go to **LiteSpeed Cache → Cache → Excludes**, add to **Do Not Cache URIs**:

```
/checkout/
/login/
/account/
/customer-dashboard/
```

Note: If custom permalinks are used, substitute the appropriate URLs.

## Step 5: Disable Aggressive Browser Caching for Dynamic Content

Go to **LiteSpeed Cache → Browser**, set **Enable Browser Cache** to **Off**, click **Save Changes**.

## Step 6: Clear Cache and Test Changes

Go to **LiteSpeed Cache → Toolbox → Purge**, click **Purge All**.

Test in an incognito window:

- Visit a product page and add an item to the cart. Verify the cart updates in real time.
- Navigate to the checkout page and confirm the form loads without errors.
- Log in and visit the Customer Dashboard. Verify account data displays correctly.

## Expected Outcome

Once configured correctly, LiteSpeed Cache will not interfere with SureCart's dynamic functionality.

## FAQ

**What happens if I don't exclude REST API endpoints from caching?**

Customers may see outdated cart data, incorrect product information, or broken checkout flows.

**Why do core WordPress scripts need to be excluded from deferral?**

SureCart depends on these scripts to handle interactive features. Deferring them can cause checkout forms and cart updates to fail.


===== SOURCE: manage-customer-orders.md =====

---
source_url: https://surecart.com/docs/manage-customer-orders
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Orders](https://surecart.com/docs-category/orders/)/How to Manage Customer Orders with SureCart

# How to Manage Customer Orders with SureCart

## How to Find Your Orders

Navigate to **WordPress Dashboard → SureCart → Orders** to see the list of all orders.

## How to Sort & Look for Orders Based on Status

Use the filter at the top left corner to sort by: All, Paid, Processing, Failed, and Canceled. Additional filters for Fulfillment status and Shipment Status are also available.

## How to Search for a Specific Order

Search for any specific order using the order ID.

## How to See All Details of a Single Order

Click on any order to access detailed options including:

- **Fulfillment Status, Order Status, & Order Receipts/Invoice** — order number, creation date, payment status, fulfillment status. Download receipt or invoice from here.
- **Customer Details, Shipping & Tax information, & Purchases** — customer name, shipping/tax address, and purchased products.
- **Orders Under Processing** — manually created orders not yet paid will show a Processing section.
- **Subscription Details** — shows status (Active, Canceled, Paused), product name, renewal date, and creation date.

## How to Cancel an Order

Click the **Actions** button on the top right corner, then choose **Cancel Order**. Canceling prevents the customer from accessing the product, downloading files, or continuing subscriptions linked to it.

## How to Refund an Order

In the Charge section, click the refund button to issue a refund.

## How to Revoke an Order

In the Purchases section, click the **Revoke** button to cancel the purchase and any related subscriptions. This also removes access to LMS courses and download files.

## **How to Add or Update Additional Order Data**

SureCart allows editing order metadata from the **Edit Order** page using a JSON editor.

1. Go to **WordPress Dashboard → SureCart → Orders**.
2. Click the order to update.
3. Scroll to the **Additional Order Data** section.
4. Click **Add Custom Data**.
5. Enter valid JSON format:

```json
{
  "reference_number": "ABC-123"
}
```

6. Click **Save**.

### Limitations When Editing Metadata

- Existing metadata **cannot be removed** — only **updated or cleared**.
- The platform **merges** new metadata with existing data.

**Workarounds to clear a value:**

```json
{ "roles": [] }
{ "roles": false }
{ "roles": "" }
```

## **Notes and Limitations**

- Canceling or revoking an order may affect customer access to digital products, downloads, subscriptions, or connected LMS content.
- Additional Order Data is merged with existing metadata and cannot be fully removed once saved.
- Some actions (refunds, cancellations) depend on the connected payment processor's capabilities.


===== SOURCE: manage-store-owners-notifications.md =====

---
source_url: https://surecart.com/docs/manage-store-owners-notifications
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/How to Manage Store Owner's Notifications on SureCart

# How to Manage Store Owner's Notifications on SureCart

As a Store owner, you will receive these types of emails:

- New Order Notifications
- Subscription Payment Failure Notifications
- Subscription Cancellation Notifications
- Subscription Saved Notifications
- Subscription Renewal Notifications
- Webhook Endpoint Error Notifications

## How to Enable/Disable Store Owner Notifications

1. Log in at [app.surecart.com](https://app.surecart.com/).
2. Go to the bottom left corner of your screen and click on **Notifications**.
3. On the right sidebar, you will see all notification options for store owners.
4. Toggle each notification type on or off according to your preferences.
5. Click the **Save** button after making your changes.

## How to Change Your Email Notification Address

If you want to receive email notifications on a different email address, add the new email address in the notification field and save it. This is separate from the email address configured under SureCart > Settings > Design & Branding.


===== SOURCE: managing-subscriptions.md =====

---
source_url: https://surecart.com/docs/managing-subscriptions
source: surecart-kb
scraped: true
---

# How to Manage Subscriptions in SureCart

SureCart allows you to setup customer subscription models. You can simply create product purchase plans that customers can buy as subscriptions.

When you enable product subscriptions, managing them becomes necessary.

After setting up your SureCart store, go to your WordPress dashboard.

- Navigate to the **SureCart** plugin, and click on **Subscriptions**.

This area displays a list of your subscriptions along with their current status.

### **Changing Renewal Date**

There may be situations where you want to change your customer's renewal date for a particular subscription.

To change your customer's renewal date:

- Select **Actions** and then **Change Renewal Date**.
- Select a new date and time from the calendar.

You can adjust this renewal date without affecting your subscriber's existing settings.

### **How to Pause User Subscription**

Subscribers might need a break for various reasons. Pausing a subscription offers customers a practical solution without making them cancel your product subscription.

- Select **Actions** and then select **Pause Subscription**.
- Select the new date and time until which you'd like to pause the subscription.

This action pauses the customer's subscription. You can either resume your paused subscription immediately or set a date and time at which it will be resumed automatically.

### **Restarting Installments Automatically**

By default, installment subscriptions end once the final payment is completed. However, some businesses may want these plans to continue automatically.

That's where the **Restart when completed** setting comes in.

- **Enabled:** After the last installment is paid, the plan restarts automatically with the same payment schedule.
- **Disabled (default):** The subscription ends once all installments are completed.

**Where to Enable:**

**1. From the Subscription Details Page**: For existing installment subscriptions, go to **Subscriptions > Select Subscription > Subscription Settings** and toggle **Restart subscription when completed**.

**2. When Creating or Editing a Product Price**: Navigate to **Products > Edit Product > Add a Price**, set **Payment type: Installment**, scroll to **Advanced**, and toggle **Restart plan when completed**.

### **How to Cancel User Subscription**

Canceling subscriptions in SureCart is straightforward:

- Click on **Actions** and then choose **Cancel Subscription.**

You can decide whether to cancel the subscription immediately or at the end of the current period.

### **Updating Subscription Details**

The update subscriptions feature allows you to modify various subscription details, such as adjusting product quantities, adding free trials, editing payment methods, and enabling prorate charges.

You can update these changes immediately or schedule them for later on.

Prorate charges are like getting a fair bill when you change your subscription in the middle of the month. If a customer upgrades their plan during the month, prorate makes sure they're billed or credited fairly for the time left in that month.

### **Edit Your Customer Details**

You can also edit the individual customer details in SureCart. Click on the **View Customer** button in your Subscription details dashboard.

You can update the customer's name, email, and phone number. Additionally, you can also view customer transactions, check purchases, add shipping addresses for customers, and choose customer email notification preferences.

Click on the **Save Customer** button after you've made the changes.


===== SOURCE: managing-the-affiliates.md =====

---
source_url: https://surecart.com/docs/managing-the-affiliates
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Affiliate Platform (for merchants)](https://surecart.com/docs-category/affiliates-for-merchants/)/Managing Affiliates in SureCart

# Managing Affiliates in SureCart

This document explains how to manage affiliates in SureCart after the initial setup. It covers reviewing affiliate requests, monitoring activity, processing payouts, and understanding the affiliate portal.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An active affiliate program

### **Affiliate Management Overview**

Affiliate management in SureCart is handled from the **Affiliates** section in the WordPress dashboard. The main areas available are:

- Requests
- Clicks
- Referrals
- Payouts

Navigate to **WordPress Dashboard → SureCart → Affiliates** to access these sections.

### **Review and Approve Affiliate Requests**

When affiliates sign up using the affiliate registration form, their requests appear in the Requests section.

- Go to **SureCart → Affiliates → Requests**.
- Click an affiliate name to view the request details.
- Use the **Actions** menu to approve, deny, or delete the request.

Once approved, the affiliate receives an email notification with instructions to access the affiliate portal.

To complete access, the affiliate must:

- Click **Go to Affiliate Portal** in the email.
- Verify their email address using the provided verification code.

After verification, the affiliate is logged into the affiliate portal.

### Monitor Affiliate Clicks

The Clicks section displays activity generated from affiliate referral links.

- Go to **SureCart → Affiliates → Clicks**.

This section shows:

- Affiliate name
- Referral URL
- Click status

You can filter clicks using the following tabs:

- All
- Converted
- Not Converted

This helps identify which affiliates are generating traffic and conversions.

### **Manage Referrals**

A referral is recorded when a customer clicks an affiliate link and completes a purchase.

- Go to **SureCart → Affiliates → Referrals**.

From this screen, you can:

- Approve referrals
- Deny referrals
- Edit referrals
- Delete referrals

An optional test mode is available to track referrals without affecting live data.

### Pay Affiliates Individually

Approved referrals generate commissions that can be paid through the Payouts section.

- Go to **SureCart → Payouts**.
- Click **Add New**.
- Select the affiliate to be paid.
- Choose the end date for referral consideration.
- Click **Create**.

SureCart generates a list of eligible payouts and assigns them a **Processing** status.

### **Process Bulk Affiliate Payouts**

Bulk payouts allow payments to multiple affiliates at once using payout batches.

- Go to **SureCart → Affiliates → Payouts**.
- Click **Add New** and select **Payout Batch**.
- Enter the minimum commission amount required for inclusion.
- Select the end date and time for referral consideration.
- Click **Create**.

Only affiliates who meet the minimum commission threshold within the selected period are included in the batch.

> **Note:** Payments are not processed automatically. Merchants must complete payments manually outside the platform.

### **Understand the Affiliate Portal**

From the affiliate portal, affiliates can:

- View clicks, referrals, and earnings
- Access their unique referral URL
- Enter or update their payout email address

This portal allows affiliates to track performance and manage their account independently.

### **Expected Outcome**

After following this guide, affiliate activity can be reviewed, approved, tracked, and paid efficiently. Affiliates gain access to their portal, while merchants maintain full control over approvals and payouts.

### **Notes and Limitations**

- Affiliate payouts must be completed manually by the merchant.
- Test mode referrals do not affect live affiliate data.
- Only approved referrals are eligible for payouts.

### **FAQ**

**What happens after an affiliate request is approved?**

The affiliate receives an email with instructions to verify their account and access the affiliate portal.

**Can referrals be edited after approval?**

Yes. Referrals can be edited, approved, denied, or deleted from the Referrals section.

**Are affiliate payouts automatic?**

No. SureCart generates payout records, but payments must be processed manually by the merchant.


===== SOURCE: manual-payment-methods.md =====

---
source_url: https://surecart.com/docs/manual-payment-methods
source: surecart-kb
scraped: true
---

# How to Create Manual Payment Methods in SureCart

Manual payment methods allow merchants to offer alternatives like Cash on Delivery, Local Pickup, or Mail-In Payments when online processors aren't suitable.

## Setup Process

Navigate to **Settings > Payment Processors** and click "Add New" under Manual Payment Methods. Fill in these fields:

- **Custom Payment Method Name**: The option label customers see at checkout
- **Description**: Instructions displayed when customers select this method
- **Payment Instructions**: Text shown after purchase completion
- **Reusable**: Toggle for subscription/installment use

## Important Consideration

Subscriptions and installment plans using manual payment methods will run indefinitely. Merchants should closely monitor these transactions and manually manage cancellations or access revocation as needed.

## Customer Experience

After checkout, buyers access payment instructions via their customer dashboard and receive email notifications. Orders appear in your **SureCart > Orders** section, marked as unfulfilled by default until you fulfill them manually.

Manual payment subscriptions function identically to standard payment methods regarding notifications and management, requiring active merchant oversight for proper administration.


===== SOURCE: manually-assign-affiliates-past-orders.md =====

---
source_url: https://surecart.com/docs/manually-assign-affiliates-past-orders
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Affiliate Platform (for merchants)](https://surecart.com/docs-category/affiliates-for-merchants/)/Manually Assign Affiliates to Orders/Customers

# Manually Assign Affiliates to Orders/Customers

This document explains how to manually assign affiliates to customers, orders, or subscriptions in SureCart, allowing affiliates to receive credit for future purchases or subscription renewals.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An active affiliate program
- At least one existing customer, order, or subscription

### **Manually Assign an Affiliate to a Customer for Future Purchases**

You can assign an affiliate to a customer so that the affiliate receives commission for future purchases made by that customer.

- Go to **WordPress Dashboard → SureCart → Customers**.
- Select the customer you want to edit.
- In the **Affiliate Commissions** section, select the affiliate you want to credit.
- (Optional) Click the **three-dot menu** and select **Update** to set an expiration date.
- Choose the date and time until which the affiliate should receive commissions.
  - Leave this field empty to pay commissions indefinitely.
- Click **Save Customer** to apply the changes.

### **Manually Assign an Affiliate to a Subscription for Future Renewals**

You can also assign an affiliate to receive commissions for subscription renewals.

- Go to **WordPress Dashboard → SureCart → Subscriptions**.
- Select the subscription you want to edit.
- Choose the affiliate you want to credit for subscription renewals.
- (Optional) Click the **three-dot menu** to set a commission expiration date.
  - Leave this field unchanged to allow commissions indefinitely.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, the selected affiliate will receive commission credit for future customer purchases or subscription renewals according to the configured settings.

### **Notes and Limitations**

- Existing orders and past commissions are not affected.
- Manual affiliate assignments apply only to future purchases or renewals.
- Leaving the expiration date empty enables commissions indefinitely.

### **FAQ**

**Do manual affiliate assignments affect past orders?**

No. Manual assignments apply only to future purchases or subscription renewals.

**Can I change or remove an assigned affiliate later?**

Yes. Affiliate assignments can be updated or removed at any time from the customer or subscription record.

**Can different affiliates be assigned to customers and subscriptions?**

Yes. Affiliates can be assigned independently at the customer and subscription level.


===== SOURCE: manually-retry-failed-payments.md =====

---
source_url: https://surecart.com/docs/manually-retry-failed-payments
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Subscriptions](https://surecart.com/docs-category/subscriptions/)/How to Manually Retry Failed Subscription Payments

# How to Manually Retry Failed Subscription Payments

When there is a subscription payment failure or installment payment failure, the merchant will receive an email notification and the customer will receive a notification.

The payment will be automatically retried as part of our subscription recovery feature.

You will also have the option to retry the payment manually.

- Navigate to your customer's subscription under **SureCart** > **Subscriptions** on your WordPress dashboard.

- Scroll down to the **Billing Periods** section, click the three-dot icon next to the customer's failed payment, and choose **Retry Payment**.

This action should resolve the payment issue.

We hope this guide helped you. If the above solution doesn't work for you, please don't hesitate to contact our support team. We're here to help!


===== SOURCE: migrate-to-another-wordpress-install.md =====

---
source_url: https://surecart.com/docs/migrate-to-another-wordpress-install
source: surecart-kb
scraped: true
---

# Migrating SureCart to Another WordPress Install

Migrating your SureCart store to another WordPress site is possible using migration plugins.

One such plugin that is recommended by many SureCart users is the Duplicator plugin.

**Please note:** This documentation was created using the Pro version of the Duplicator plugin for simplicity. If you have the Free version, you must manually upload the Installer and Archive files to the root directory of your destination site.

For detailed usage instructions, please refer to the Duplicator documentation.

After successfully migrating your installation, make sure to verify your SureCart store by following the steps covered in the next section.

### Verifying Your SureCart Store

After logging into your new site, navigate to SureCart to ensure all data has been migrated successfully.

Start by going to the SureCart Dashboard page. If you are on a different URL, select the action button that is most appropriate for your situation.

Check your products, orders, and settings to ensure everything works correctly.

### Additional Tips

- **Update Permalinks**: Go to **Settings > Permalinks** and click **Save Changes** to ensure your permalinks are updated.
- **Recheck Plugins and Themes**: Ensure all your plugins and themes are active and updated as per the source site.

By following these steps, you should be able to migrate your SureCart store to another WordPress installation with ease using the Duplicator plugin.

If you encounter any issues, refer to the Duplicator documentation or seek support from the plugin's developers.

### Frequent Asked Questions

**Can I use another backup plugin/tool?**

Yes, you can use any backup plugin or tool you prefer. Just make sure to verify that everything has been migrated correctly.

**What if I encounter issues during the migration?**

If you encounter any issues during the migration process, refer to the Duplicator documentation or contact their support for assistance.

**Is it necessary to use the Pro version of Duplicator?**

While the Pro version simplifies the process with its Import feature, you can still use the Free version by manually uploading the Installer and Archive files to the root directory of your destination site.

**Can I migrate my site if it's on the same server?**

Yes, you can migrate your SureCart store even if both WordPress installations are on the same server. The steps remain the same.

**Do I need to update my permalinks after migration?**

Yes, it's a good practice to update your permalinks. Go to **Settings > Permalinks** and click **Save Changes** to ensure they are updated.

**What should I do with the old site after migration?**

Once you have verified that the migration was successful and everything is working correctly on the new site, you can choose to keep the old site as a backup or delete it.


===== SOURCE: migrate-to-surecart.md =====

---
source_url: https://surecart.com/docs/migrate-to-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Migrate from Other Platforms to SureCart

# How to Migrate from Other Platforms to SureCart

This document outlines the recommended sequence of steps to migrate an existing eCommerce store from another platform to SureCart. Each step links to a detailed guide for that specific stage of the migration.

## **Migration Overview**

The migration process is divided into the following steps. Following them in order is recommended, since some steps depend on data created in earlier ones.

1. Set up the store
2. Configure branding and notifications
3. Connect payment processors
4. Import customers
5. Import products
6. Import purchases
7. Import active subscriptions
8. Synchronize WordPress users with SureCart

## **Step 1: Set Up the Store**

- Install and activate SureCart. Refer to [How to Install SureCart](https://surecart.com/docs/installing-surecart/).
- Configure store details (name, currency, address, and others). Refer to [How to Update Store Details](https://surecart.com/docs/update-store-details/).

## **Step 2: Configure Branding and Notifications**

- Configure brand colors and logo. Refer to [How to Set Up Branding in SureCart](https://surecart.com/docs/set-up-your-branding/).
- Configure customer email notifications. Refer to [How to Manage Customer Email Notifications](https://surecart.com/docs/customer-email-notifications/).

## **Step 3: Connect Payment Processors**

SureCart supports: Stripe, PayPal, Mollie, Paystack, Razorpay.

## **Step 4: Import Customers**

Customer data is imported via a CSV file. Refer to [How to Import Customers in Bulk](https://surecart.com/docs/import-customers-in-bulk/).

## **Step 5: Import Products**

Product data is imported via a CSV file. Refer to [How to Import Products in Bulk](https://surecart.com/docs/import-products-in-bulk/).

## **Step 6: Import Purchases**

Historical purchase data is imported via a CSV file. Refer to [How to Import Purchases in Bulk](https://surecart.com/docs/import-purchases-in-bulk-surecart/).

## **Step 7: Import Active Subscriptions**

Active subscriptions are imported via a CSV file. Refer to [How to Import Subscriptions in Bulk](https://surecart.com/docs/import-subscriptions-in-bulk/).

## **Step 8: Synchronize WordPress Users with SureCart**

Run the user sync from the SureCart settings. Refer to [How to Sync WordPress Users with SureCart](https://surecart.com/docs/sync-users-with-surecart/).

## **Notes and Limitations**

- The migration order matters. Customers must be imported before purchases and subscriptions, and products must exist before purchases or subscriptions can reference them.
- CSV files must follow the format specified in each bulk import guide.
- Saved payment method transfer is supported only when migrating from Stripe.
- Testing the migration in a staging environment before applying it to a live store is recommended.


===== SOURCE: multi-currency.md =====

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


===== SOURCE: notification-language.md =====

---
source_url: https://surecart.com/docs/notification-language
source: surecart-kb
scraped: true
---

# Change Language For Email Notifications and Invoices - SureCart

## Overview

SureCart allows businesses to send email notifications and invoices in multiple languages, making it easier to serve international customers.

## Two Methods to Change Language

### Method 1: WordPress Dashboard

1. Navigate to WordPress dashboard
2. Go to **SureCart > Settings > Store Settings**
3. Select preferred language in **Store Language** settings
4. Click **Save**

### Method 2: SureCart Platform Dashboard

1. Access SureCart dashboard
2. Navigate to **Settings > General**
3. Locate the **Language** field
4. Choose desired language
5. Save settings

## Key Point

Changing the language in one location (either in the WordPress dashboard or in the SureCart Dashboard) will automatically update the language in the other location as well.

## Result

Once configured, customers receive email notifications and invoices in the selected language.


===== SOURCE: order-bump-placement.md =====

---
source_url: https://surecart.com/docs/order-bump-placement
source: surecart-kb
scraped: true
---

# Customizing Order Bump Placement - SureCart

## Overview

Order bumps are automatically included in checkout forms, but can be repositioned for improved visibility and customer engagement.

## Key Steps

**Creating the Form:**
Navigate to SureCart's Custom Forms section and select "Add New." Choose a template (such as "Full Page") and proceed.

**Adding Products:**
Click "+ Add Product" to select items for your order bump. Use the product selection toggle to browse available options.

**Customizing Configuration:**
Adjust quantities, remove products, add additional items, and set product-specific options. You may also create a custom thank-you page linked to this form before clicking "Create."

**Positioning the Order Bumps Block:**
To add an Order Bumps element, hover between existing form elements until a blue line with a plus icon appears. Click it, then search for and select "Order Bumps" from the popup menu.

**Final Placement:**
Reposition the Order Bumps block using arrows or drag-and-drop functionality. Once satisfied with placement, click "Publish" in the top right corner to save changes.

This process allows merchants to strategically place order bump elements anywhere within their checkout forms to maximize conversion opportunities.


===== SOURCE: order-bumps.md =====

---
source_url: https://surecart.com/docs/order-bumps
source: surecart-kb
scraped: true
---

# Order Bumps - SureCart

## Overview

An order bump is a strategic, last-minute upsell offer presented during the checkout process that aims to increase the average transaction value and boost overall revenue.

## Creating an Order Bump

1. Navigate to **SureCart > Order Bumps > Add New**
2. Enter a descriptive name and select a product from the dropdown
3. Type the product name to search or select from the menu
4. Click the **Create** button to finalize

## Display Conditions

Display conditions determine when an order bump appears during checkout. To configure them:

1. Click **+ Add A Condition**
2. Choose between **Price** or **Product** criteria
3. Select specific products from the dropdown menu
4. Choose when to display: "Any of these items in the cart"
5. Click **Add Condition** to confirm

Multiple conditions can be added, allowing bumps to display when customers add any of several specified products.

## Applying Discounts

The discount section offers two options:

- **Percentage**: Apply a percentage reduction
- **Fixed**: Apply a flat dollar amount

After entering the discount value, users can toggle **Auto Apply Discount** to automatically apply it during checkout. Remember to save changes afterward.

## Description and Call-To-Action

Enhance appeal by adding:
- A bump description explaining the offer
- Compelling call-to-action text

These elements significantly improve customer engagement with the bump offer.

## Bump Priority

Priority is set using a 1-5 scale located below the save button:
- 1 = lowest priority
- 5 = highest priority

Higher priority bumps display preferentially when multiple bumps qualify for a customer.


===== SOURCE: order-confimation-button-redirection-issue.md =====

---
source_url: https://surecart.com/docs/order-confimation-button-redirection-issue
source: surecart-kb
scraped: true
---

# Order Confirmation Button is Redirecting Users to the Homepage

## Issue Description

When customers complete a purchase and click the confirmation button in their email, they are redirected to the homepage instead of accessing the SureCart Customer Dashboard. This commonly occurs when using SEO plugins like RankMath.

## Solution

### Step 1: Verify Store URL Configuration

Navigate to **SureCart > Settings > Store Settings** and confirm the store URL is correctly mapped.

### Step 2: Access RankMath Settings

Open RankMath and click on General Settings.

### Step 3: Locate Redirections Tab

Scroll down to find the Redirections section.

### Step 4: Adjust Fallback Behavior

Change the FallBack Behaviour setting from "Homepage" to "Default 404 page."

### Step 5: Test and Save

Save your changes and test the order confirmation button again to verify proper functionality.

## Important Note

If you do not have RankMath installed but still experience this issue, review the redirection settings in whatever SEO plugin you are using, as similar redirect rules may apply.

## Additional Support

If the problem persists after following these steps, contact the SureCart Support Portal for further assistance.


===== SOURCE: order-confirmation-shortcodes.md =====

---
source_url: https://surecart.com/docs/order-confirmation-shortcodes
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/Order Confirmation Shortcodes

# Order Confirmation Shortcodes

While SureCart offers highly customizable WordPress blocks for the customer dashboard and order confirmation, some users still prefer to do everything in their page builder of choice.

For example, the order confirmation block. While we do offer a dedicated block for order confirmation, we completely understand if you prefer achieving this using page builders.

To make this possible, we have introduced the order confirmation shortcodes that you can add to your page builder.

## Order Confirmation Shortcode

This is for making custom thank you pages and will allow you to display the order data anywhere on the page.

Everything must be wrapped inside a **`sc_order_confirmation`** shortcode.

```
[sc_order_confirmation]

Please check your inbox for more instructions.
[sc_order_confirmation_line_items]
[sc_customer_dashboard_button]Go To Dashboard[/sc_customer_dashboard_button]

[/sc_order_confirmation]
```

This component passes the purchased order data from the checkout page into the individual components. We'll show you how it works in a bit.

## Adding Order Confirmation Shortcode To Your Website

To use this shortcode, you need to create a new custom thank you page and link it to your checkout form.

- Navigate to **Pages** > **All Pages** in your WordPress dashboard and click **Add New Page** to create a new page.
- Name this page as you like, you can give it any name.
- Click on the toggle block inserter icon and add a new **Shortcode** element to your page.
- Paste the above shortcode here.
- Navigate to your checkout and connect this page to it. Follow this [article](https://surecart.com/docs/custom-thank-you-page/) for more details.

Now, when a customer purchases from your store, they will be redirected to this thank you page with details of the purchased product.

You can easily customize this shortcode to display only the elements you want your customers to see.

That's it! We hope this helped you. If you have any questions, feel free to reach out to our support team. We're always here to help!


===== SOURCE: order-fulfillment-and-shipping.md =====

---
source_url: https://surecart.com/docs/order-fulfillment-and-shipping
source: surecart-kb
scraped: true
---

# SureCart Order Fulfillment and Shipping Guide

Order fulfillment encompasses all the activities that take place after an order is placed in your store, culminating in the customer receiving the shipped item.

Customers can monitor the status of their orders at every stage using the customer dashboard.

This guide provides a detailed overview of the entire process and walks you through fundamental steps to ensure smooth order fulfillment.

## **Understanding Fulfillment and Shipping Statuses**

You can filter all of your orders either via Fulfillment or Shipping statuses from the **Orders** section.

Here's what both of these terms mean:

- **Fulfillment Status**: This tells you where your order stands within the seller's process. If your order is "unfulfilled," it means the seller hasn't started preparing it yet.
- **Shipping Status**: This tells you where your order is in terms of getting it to you. For example, "Not shipped" means the seller hasn't handed it over to the delivery people yet.

### **Types of Fulfillment Statuses**

Following are the types of fulfillment statuses in SureCart:

- **Unfulfilled**: Indicates an order that has been received but not yet processed. No actions such as packaging or label generation have been initiated.
- **Fulfilled**: Denotes an order that has undergone the complete fulfillment process.
- **Partially Fulfilled**: Indicates an order where only a portion of the items has been shipped, often applicable in cases of multiple products or split shipments.

### **Types of Shipping Statuses**

Following are the types of shipping statuses in SureCart:

- **Not Shipped**: The product is prepared for shipping but has not yet been dispatched to the carrier.
- **Shipped**: The product has been handed over to the shipping carrier for delivery.
- **Partially Shipped**: Some items within the order have been shipped, while others remain pending.
- **Delivered**: Signifies successful delivery of the product to the customer.

Based on the current situation of your product in the delivery lifecycle you can set the fulfillment and shipping status of the individual order from the **Orders** section.

## **How to Fulfill Orders In SureCart?**

Follow these steps to mark an order as Fulfilled in SureCart:

- Select your order.
- Click on the **Fulfill Item** button here.
- You can optionally add your order's tracking number and tracking link here if you prefer. These help you keep an eye on where your order is during shipping.

**Note:** If you add a tracking number, you must also include a tracking link; they go together to help both you and the seller keep track of your order until it reaches you.

- Once your order is ready to be prepared and shipped, click on the **Fulfill Item** button here.
- Click on this **Cancel fulfillment** option if you want to revert your order's fulfillment status to Unfulfilled.

**Note**: SureCart does not display the fulfillment status on your buyer's customer dashboard account. This decision was made with the understanding that their primary concern is usually the shipping status of their order

## **How to Change Shipping Statues In SureCart?**

Once your order is marked as **Fulfilled**, a new dropdown is highlighted.

- You can update your order's shipping status here based on its delivery cycle. You can also notify your customer via email about these updates.

Your order will now be marked as **Delivered** in both your Orders as well your buyer's customer dashboard account.


===== SOURCE: order-placement-texts.md =====

---
source_url: https://surecart.com/docs/order-placement-texts
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Change Order Placement Texts for Checkout Forms

# How to Change Order Placement Texts for Checkout Forms

This document explains how to customize the text messages displayed during and after order placement in SureCart checkout forms, including loading and success messages.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **Order Placement Text Overview**

During checkout, customers see different messages after clicking the purchase button, such as loading and success confirmations.

SureCart allows you to customize these texts to better match your store's tone and messaging.

### **Change the Loading Text**

The loading text appears immediately after a customer places an order and while the payment is being processed.

- Go to **WordPress Dashboard → SureCart → Forms**.
- Open the checkout form you want to edit.
- Click the form header to display the checkout form settings.
- Open the **Loading Text** section.
- Customize the following fields as needed:
  - **Submitting Order**
  - **Processing Payment**
  - **Confirming Payment**
  - **Success Text**
- Click **Update** to save the changes.

You can perform a test purchase to preview how the updated messages appear during checkout.

### **Change the Success Text Popup**

The success text is displayed in a popup window after an order is successfully completed.

- Open the checkout form you want to edit.
- Click the form header to display the form settings.
- Open the **Success Text** section.
- Customize the following fields:
  - **Title** – The popup title
  - **Description** – The message shown to the customer
  - **Button Text** – The call-to-action button label
- Click **Update** to save the changes.

After saving, you can run a test purchase to verify how the success popup appears to customers.

### **Expected Outcome**

After completing these steps, the checkout form will display customized loading and success messages during order placement, reflecting the configured text settings.

### **Notes and Limitations**

- Text changes apply only to the checkout form being edited.
- Existing orders are not affected by text updates.
- Testing is recommended to confirm the visual flow and wording.

### **FAQ**

**Do these text changes affect all checkout forms?**

No. Each checkout form has its own order placement text settings.

**Can I revert to the default text?**

Yes. You can manually replace the custom text with the original default values at any time.

**Do text changes affect completed orders?**

No. Text changes apply only to new checkouts.


===== SOURCE: orders-receipts.md =====

---
source_url: https://surecart.com/docs/orders-receipts
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/Orders & Receipts

# Orders & Receipts

Orders and receipts are essential for businesses to track sales and provide customers with proof of purchase.

Implementing sequential or random order numbers on receipts improves organization and security.

In this article, we'll explore how to configure them in SureCart.

## Sequential vs Random Order Numbers

Depending on your business needs and preferences, you can choose between two types of order numbers with SureCart:

- Sequential
- Random

### Sequential Order Numbers

To configure the Sequential Order Number, follow the steps below.

Navigate to the WordPress dashboard and click on **SureCart** > **Settings** > **Orders & Receipts.**

Select **Sequential** from the dropdown menu.

#### Add Prefix

To set the **Order Number Prefix**, add the wordings of your choice here.

#### Start Order Number At

To configure the Sequential Order Numbers, navigate to the **Start Order Numbers At** section and select the starting number of your choice.

The default is 1, but you're free to choose any number that suits your needs.

### Random Order Numbers

To have a Random Order Number, just follow the steps below.

Click in the dropdown menu **Orders Numbers Counter** then select **Random Numbers And Letters** and click Save.

## Setting a Language

To set the language of your Emails and Receipts follow the steps below:

- Go to your browser, type [app.surecart.com](https://app.surecart.com/), and login with your credentials.

- Go to **Settings** and in the **Store Language**, select in the dropdown the language you want and click **Save**.

To know more about language customization, check out our separate article on [changing language for email notifications and invoices](https://surecart.com/docs/notification-language/).

That's it with this guide! If you face any issues while implementing these steps please contact our support team. We're always here to help!


===== SOURCE: override-commissions-for-specific-affiliates.md =====

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


===== SOURCE: override-product-and-shipping-taxes.md =====

---
source_url: https://surecart.com/docs/override-product-and-shipping-taxes
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Tax](https://surecart.com/docs-category/tax/)/How to Override Product and Shipping Taxes in SureCart

# How to Override Product and Shipping Taxes in SureCart

SureCart helps you adjust how much tax you pay for different types of products and for [shipping](https://surecart.com/docs/how-to-create-shipping-profiles/), so you follow the rules about taxes where you run your business. Certain products may have different tax rates requirements based on your tax jurisdiction.

For example, let's say you sell both outdoor and indoor clothes. If your region charges less tax for outdoor clothes because they're considered essential, you can group them together and pay the lower tax rate.

Similarly, if there are different tax requirements for shipping costs, SureCart allows you to apply the correct tax rate and exemptions to shipping, aligning with legal standards and avoiding any legal complications.

This article shows you how you can easily enable overriding product and shipping tax charges with SureCart.

## **Enabling Taxes In SureCart**

To enable tax overriding, you first need to enable taxes for your online store. If you haven't done that already, here's how you can do it.

### **Enable Taxes from the SureCart Settings**

Begin by enabling the following tax option in your SureCart settings.

- Navigate to SureCart **Settings** > **Taxes** and enable the **Tax Collection** option.

- Enter your address details here and click **Save**.

**Note:** Filling in your address is important for the next steps. If you face any errors while filling your address details, please [contact us](https://surecart.com/contact-us/).

### **Enabling Taxes for Individual Products**

Now that you've enabled taxes for your online store, it's time to make sure that it's enabled for individual products as well.

- Navigate to **Products** and select the product you want.

- Ensure that the **Charge tax on this product** option is enabled.

For more details on these tax options, check our article on [configuring tax settings in SureCart.](https://surecart.com/docs/configure-tax-settings-in-surecart/)

## **Creating Product Collections**

SureCart allows you to override taxes for a [collection](https://surecart.com/docs/product-collections/) of products. For example, if you run a clothing store, you might have product collections such as Men's Clothes, Women's Apparel etc.

This will let you override taxes for an entire category of products simultaneously.

If you want to override taxes for just one particular product, you can still create a collection with only that product.

If you haven't set up a product collection yet, follow these steps to create one in SureCart:

- Navigate to **Products** > **Collections** > **Add New** to create a new product collection. In this example, let's name the collection "Men's Clothes".

- Head to any individual product via **Products** and click on the **Add to Collection** button. Select the collection in which you want to add this product.

The product has now been added to the collection we created.

## **How to Override Taxes for a Collection of Products In SureCart**

Once you've enabled taxes and created product collections, you can override the taxes for them. Here's how you can do it:

- Navigate to **Settings** > **Taxes** again and select your desired region. For this example, let's choose Australia.

- Enable the **Collect Tax** option for your business.

- Select the same country and enter your tax number on this popup screen, tax charges will be automatically calculated for you. Click on the **Collect Tax** button once you're done.

- Head to the **Product Overrides** section and click on the **Add** **Override** button.

- Select the collection of products that you want to override. We are going to be selecting the example collection "Men's Clothes" we just created, but you can choose any collection you want.

- Enter the individual product's tax rate and click on the **Add Override** button.

Now, all products in this collection will have a tax rate of 15% for the Australia region. You can follow this same process for any regions you want.

## **Previewing Your Changes**

Now, when an Australian customer attempts to purchase any product from this collection, they will see a different tax rate specifically applied to that product.

Compare this to any other product outside of the collection and you'll notice the difference. This product will have the usual Australian tax rate that is automatically calculated according to the country.

Now that we have changed the taxes for product collections, let's do the same for shipping charges..

## **How to Override Shipping Taxes in SureCart**

To override shipping charges, you need to **Enable** **Shipping Rates** and create a [shipping profile and configure its shipping zones and rates](https://surecart.com/docs/how-to-create-shipping-profiles/).

You can find these options under **Settings** > **Shipping**.

**Note:** SureCart lets you ship products with the **General** profile by default. If you want to create new profiles, upgrade to any one of our premium [plans](https://surecart.com/pricing/).

Once you've configured your shipping profile, follow these steps:

- Make sure to enable the **Physical products** options for individual products you intend to ship.

- Navigate to **Settings** > **Taxes** and select your desired region.

- Ensure that you've enabled the **Collect Tax** option.

- Click on the **Add Override** button within the "Shipping Overrides" area.

- Enter your shipping charges here and click on the **Add Override** button.

Now all of the physical products in the above country will have these custom shipping charges applied to them. You can preview the same on your website as well.

That's it with this guide. If you have any questions, feel free to reach out to our support team at [support@surecart.com](mailto:support@surecart.com). We're always here to help!


===== SOURCE: overview-customer-dashboard.md =====

---
source_url: https://surecart.com/docs/overview-customer-dashboard
source: surecart-kb
scraped: true
---

# Overview of the Customer Dashboard - SureCart

## Dashboard Page Features

The system automatically creates one editable dashboard page upon plugin activation. To locate it, navigate to Pages > Dashboard. The page features three key blocks:

- Customer Subscriptions
- Customer Orders
- Customer Downloads

## Customization Options

Users can modify block titles by selecting a block and using the right menu panel. Block order can be rearranged through dragging or the left-side list view menu.

Additional elements—such as buttons linking to courses or LMS shortcodes—can be added to enhance the dashboard experience.

## Editing the Dashboard Page

To edit the page: hover over the Dashboard page and click on the Edit button.

## Deprecated Feature

The Tabbed Customer Dashboard block is no longer actively supported but can be re-enabled through custom code if needed.

## FAQ Notes

Menu items (Dashboard, Orders, Plans, etc.) cannot currently be edited directly, though menu item names can be modified through translation files. Full customization of the Customer Dashboard is planned for future updates.


===== SOURCE: overview-of-customers-section.md =====

---
source_url: https://surecart.com/docs/overview-of-customers-section
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/Overview of the Customers Section In SureCart

# Overview of the Customers Section In SureCart

The Customers section in SureCart includes information about all customers linked with your store. You can choose to view or edit these details as needed.

This guide shows you the basic overview of this section and some simple steps to view and edit these details. Let's start!

## How to Access the Customers Section in SureCart?

To access the customer section of SureCart, go to the **SureCart** menu, then click on **Customers**.

Here you will find the list of your customers. Choose any one of them and click on it.

## Overview of Customers

- In the **Customer Details** area, you can edit the First Name, Last Name, and Email.

### Balance

The **Balance** section in Customers provides you with an overview of your customer's account balance.

Here you can view their **Credit Balance** and any charges or refunds that have been applied to their account. To see a detailed list of transactions, simply click on the **View Transactions** button.

### Purchases

The **Purchases** section in SureCart provides a comprehensive list of all products that a customer has purchased.

Additionally, the "Revoke" button allows you to manually revoke a customer's access to a specific product.

### Orders

The **Orders** section in SureCart provides a detailed overview of all customer orders in a convenient table format. This table includes essential information such as:

- Order Number
- Items Purchased
- Total Cost
- Order Status
- Date.

Additionally, the **View** button provides you with access to more detailed information about each order.

### Tax Details

Both of these sections deal with the tax details for the customers.

By clicking on the **Add Address** button, you can add a new shipping and tax address for the customers.

To apply tax for purchases made by the customer, toggle on the **Apply Tax** button. If it's toggled off, the customer won't be taxed for any future purchases.

### Charges

The **Charges** section provides a detailed list of all customer charges in a convenient table format including the charge amount, date, payment method, and status.

### WordPress User

The **WordPress User** section in SureCart displays the associated WordPress user details for each customer.

This section includes the WordPress user avatar, name, and email for quick identification. Additionally, the **Disconnect** button allows you to easily disassociate the SureCart user from their associated WordPress user account.

### Subscriptions

The **Subscriptions** section in SureCart provides you with an overview of all active customer subscriptions in a convenient table format.

This table includes essential information such as:

- Subscription Status
- Associated Product
- Renewal Date
- Creation Date

### Payment Methods

The **Payment Methods** section in SureCart provides you with an overview of all payment methods associated with a customer's account.

### Notifications

The **Notifications** section in SureCart allows customers to manage their email preferences for store notifications.

This section includes a simple toggle switch named **Subscribed to emails** that customers can use to subscribe or unsubscribe from receiving emails for purchases, charges, subscriptions, and other store-related notifications.

That's it with this guide. If you have any more questions regarding the Customers section or face any issues, please feel free to reach out to our support team. We're always here to help.


===== SOURCE: partner-program-tiers.md =====

---
source_url: https://surecart.com/docs/partner-program-tiers
source: surecart-kb
scraped: true
---

# SureCart Partner Program Tiers

The SureCart partner programs (Affiliate Program and Agency Partner Program) operate with a tiered commission structure. Both programs share the same tiers, rewarding partners as they contribute more transaction volume to SureCart.

### **Partner Tiers with Commission Structure**

The commission rates in the SureCart Affiliate Program depend on the partner tier, starting at 25% for Bronze and scaling up to 40% for Platinum:

| Tier     | Commission Rate |
| -------- | --------------- |
| Bronze   | 25%             |
| Silver   | 30%             |
| Gold     | 35%             |
| Platinum | 40%             |

### **Understanding the Tiers**

- **Bronze (Starting Tier)**: All new partners begin at this tier and earn 25% commission on both referral and platform fees.
- **Silver, Gold, and Platinum Tiers**: Partners move up these tiers based on the total transaction volume they generate through their referrals or managed client stores. As you progress to higher tiers, your commission percentages increase, unlocking greater rewards.

**Note**: The specific transaction volume thresholds required for each tier may vary and might not be immediately visible in your affiliate or agency dashboard.

### **How to Move Up the Tiers**

Your tier is based on the total transaction volume generated by your referrals (for affiliates) or the stores you manage (for agencies). As this transaction volume grows, you move into higher tiers, unlocking greater commission percentages and additional perks.

**Example**:

- A partner generating $60,000 in total transaction volume would qualify for the **Silver tier (30%)**.
- A partner generating over $1 million in total transaction volume would qualify for the **Platinum tier (40%)**.

### **Frequently Asked Questions**

**How is my tier determined?**

Your tier is based on the total transaction volume generated by your referrals (Affiliate Program) or the stores you manage (Agency Program). The more transaction volume you contribute, the higher your tier.

**Are both referral and platform commissions tiered?**

Yes, both referral and platform fee commissions follow the same tiered commission percentages: 25% at Bronze, 30% at Silver, 35% at Gold, and 40% at Platinum.

**How do I check my current tier?**

Your current tier is displayed in your affiliate or agency portal under Settings > Agency Tier.

**When do I see my updated tier?**

Tier updates occur automatically as your total transaction volume meets the thresholds for the next tier.


===== SOURCE: password-field-checkout.md =====

---
source_url: https://surecart.com/docs/password-field-checkout
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Set Up a Password Field During the Checkout Process

# How to Set Up a Password Field During the Checkout Process

This document explains how to add a password field to a SureCart checkout form, allowing customers to create their customer dashboard password during checkout.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **Customer Dashboard Access Overview**

SureCart provides customers with a dashboard where they can access order history, subscriptions, and account details.

Customers can access this dashboard in two ways:

- **Email link** – Customers receive a login link by email after completing a purchase and can set a password from the dashboard.
- **Checkout password field** – Customers create their password directly during checkout using a password field.

This guide focuses on configuring the password field during checkout.

### **Add a Password Field to the Checkout Form**

Follow the steps below to add a password field to a checkout form.

- Go to **WordPress Dashboard → SureCart → Checkout**.
- Open the **Store Checkout** form.
- Click the **+** button to add a new block.
- Navigate to the **SureCart** block section.
- Drag and drop the **Password** block into the checkout form where customers should enter their password.

### **Configure Password Field Settings**

After adding the password block, configure its settings as needed.

- Select the **Password** block.
- Enable **Required** to require customers to create a password during checkout.
- Enable **Password Confirmation** to require customers to confirm their password.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, customers will be prompted to create a password during checkout. They can then use their email address and password to log in directly to their customer dashboard.

### **Notes and Limitations**

- The password field applies only to checkout forms where it is added.
- Customers who do not create a password during checkout can still access the dashboard using the email login link.
- Existing customers are not affected by adding the password field.

### **FAQ**

**Is the password field required for all customers?**

No. The password field is optional unless the **Required** option is enabled in the block settings.

**Can customers still log in without setting a password during checkout?**

Yes. Customers can use the email-based login link to access their dashboard if no password is created during checkout.

**Does adding a password field affect existing orders?**

No. This setting applies only to new checkouts.


===== SOURCE: pause-subscription.md =====

---
source_url: https://surecart.com/docs/pause-subscription
source: surecart-kb
scraped: true
---

# How to Pause a Subscription - SureCart

## Overview

SureCart enables merchants to modify customer subscriptions through pausing, resuming, changing renewal dates, and canceling subscriptions.

## Pausing a Subscription

1. Navigate to SureCart menu > Subscriptions
2. Select the customer whose subscription you want to pause
3. Click the "Actions" button in the upper right corner
4. Select "Pause Subscription"
5. The subscription will pause at the end of the current billing cycle
6. Choose a date for reactivation in the popup window
7. Click "Pause" to confirm

The system displays status information showing when the subscription pauses and when it resumes.

## Resuming a Paused Subscription

1. Go to SureCart menu > Subscriptions
2. Select the paused subscription
3. Click the "Actions" button
4. Select "Don't Pause"
5. Click "Resume Subscription"

The subscription becomes active again and the customer continues with the same plan but with an adjusted date.

## Key Details

During a pause period, no charges will be incurred. When reactivated, customers maintain their existing subscription plan with a modified renewal schedule.


===== SOURCE: pay-off-remaining-balance-on-installment-plan.md =====

---
source_url: https://surecart.com/docs/pay-off-remaining-balance-on-installment-plan
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Subscriptions](https://surecart.com/docs-category/subscriptions/)/How to Pay Off Remaining Balance on an Installment Plan

# How to Pay Off Remaining Balance on an Installment Plan

Are you selling products through installment plans? If so, you might encounter customers who want to pay off the remaining balance of their plan early. No worries, it's a quick and easy process. Here's how you can do it:

SureCart offers this feature in our premium plans.

- Navigate to your SureCart dashboard and click on the **Subscriptions** tab.
- You can search for the customer's plan by entering their name or email address in the search bar below.

- Once you've found the customer's installment plan, click on the **Actions** button located in the top right corner of the plan overview.

- From the dropdown menu that appears after clicking on the **Actions** button, select **Pay Off Subscription**.

- A modal will appear to confirm the payment. Click on **Pay Off** to complete the transaction. The customer will be immediately charged for the remaining payments in the installment plan.

And that's it! You've successfully helped a customer pay off their installment plan.

Remember, if you have any questions or concerns, SureCart's support team is always available to help. Happy selling!


===== SOURCE: payment-types-in-surecart.md =====

---
source_url: https://surecart.com/docs/payment-types-in-surecart
source: surecart-kb
scraped: true
---

# Different Prices Available in SureCart

In SureCart, we offer various ways to set up payment types for your products. Whether you're selling products with one-time payments, installment plans, or subscription services, SureCart has you covered.

### **What is the Pricing in SureCart**

Pricing is determining how much customers need to pay for your products. It's a crucial aspect of your online store setup that influences how you sell to your customers.

Pricing tells what would be the overall cost for any product. While setting up pricing, you can include paid product trials, set donation pricing for the product, collect taxes, etc.

With SureCart, you can collect one-time payments, recurring payments, donations, etc.

### **What are the Different Payment Types in SureCart**

Payment type decides what would be the billing period or frequency of your pricing. SureCart offers three main types of payments: **One Time**, **Installment**, and **Subscription**.

#### **One-Time Payment Type**

This is like when you buy something in one shot. You tell people the price, and they pay that amount all at once.

One-time pricing is particularly effective for products or services that don't require ongoing maintenance. Examples include software licenses, digital downloads, unique artworks, or exclusive courses.

Options available:

- **Allow customers to Pay what they want** – Enabling this option allows your customers to pay what they want instead of a predefined price.
- **Tax Included** – Use this option if Tax is included in the pricing

#### **Installment Payment Type**

With this, customers can break the cost into smaller payments over time. You decide how often they pay and how many times. In SureCart, you can also give them a trial period or ask for a little extra fee at the start.

For example, if you're offering a high-end phone priced at $600, customers can pay in 6 monthly payments of $100.

Installments work well for products that might be a bit pricey, like gadgets, furniture, or a stylish wardrobe upgrade.

#### **Subscription Payment Type**

Instead of paying all at once, you pay a little bit regularly. Like a Netflix subscription where you pay to watch movies and shows every month.

For example, if you're selling a music service for $10 a month with a free first week trial. You charge a fixed amount on a regular basis and can offer trial periods or charge additional setup fees.

Available options:

- **Setup Fee** – A small initial payment collected when customers start using something new.
- **Free Trial** – A "try it out" offer where you can provide something for a limited time without charging any money.

### **How to Setup Payment Type**

To set up payment type for your products, click on the Add Price button on the Product Page.

#### **One Time Payment Type**

- Name the product price
- After adding the price, optionally set a compare price
- Enable "Pay What You Want" toggle if desired
- Toggle the "Tax is Included" option if needed
- Save the price by clicking the "Create Price" button

#### **Installment Payment**

- Choose the charging interval (day, week, month, year)
- Define the number of installments/payments
- Add a setup fee and set the trial period (if needed)
- Decide whether to charge the setup fee during the trial
- Include taxes in the pricing and toggle the option if required

#### **Subscription Payment**

- Set the subscription price and compare the price
- Select the interval for recurring payments
- Add setup and trial fees if desired
- Include taxes in the pricing and toggle the option if required

### **Creating Multiple Pricings for One Product**

In SureCart, you can create multiple pricing for the same product. For instance, if you're selling laptops, you can create a one-time payment type and an installment payment type and share them with your customers as a purchase option.


===== SOURCE: paypal-and-subscriptions.md =====

---
source_url: https://surecart.com/docs/paypal-and-subscriptions
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Online Store](https://surecart.com/docs-category/online-store/)/SureCart branding when accepting subscriptions payments with PayPal

# SureCart branding when accepting subscriptions payments with PayPal

**TL;DR: SureCart branding is only visible when you do not have reference transactions enabled on your PayPal account. When you get reference transactions enabled on your PayPal account, there will be no SureCart branding.**

If you are using SureCart to accept subscription payments with PayPal, you may have noticed that the checkout flow and subscription management pages display the SureCart branding. While this is not necessarily a problem, some merchants may prefer to remove this branding for branding consistency or other reasons.

Fortunately, it is possible to remove the SureCart branding from the PayPal checkout flow and subscription management pages easily.

In this article, we will explain how to remove the SureCart branding from your PayPal checkout flow and subscription management pages.

## **Where SureCart branding might be visible when accepting subscriptions payments with PayPal?**

When you use SureCart to accept subscription payments through PayPal, the PayPal checkout flow might display the SureCart branding to your customers. This branding shows up in two places:

- The PayPal checkout popup
- The customer's PayPal account where they manage their subscription.

## **How to remove this branding?**

If you wish to remove the SureCart branding, you'll need to enable reference transactions on your PayPal account.

**What are Reference Transactions?**

Reference Transactions is a feature of PayPal that allows merchants to process recurring payments, such as subscriptions or installments. With Reference Transactions, the merchant stores the customer's payment information on PayPal's secure servers, and PayPal processes the payment automatically according to the terms of the subscription or installment plan.

To use Reference Transactions, merchants must obtain approval from PayPal, which involves a review of the merchant's business practices and a verification process. The approval process may vary depending on the merchant's location, business model, and other factors.

Obtaining approval for Reference Transactions from PayPal can be a complex and time-consuming process, especially for merchants who are new to PayPal or who are located in certain countries. PayPal typically requires a review of the merchant's business practices and financial history, as well as verification of their identity and contact information. Additionally, PayPal may require merchants to demonstrate that they have a legitimate need for Reference Transactions, and that they are capable of managing recurring payments effectively.

Given the complexity and difficulty of obtaining approval for Reference Transactions, many merchants are not able to accept recurring payments with PayPal.

We noticed this and built the CIB (Client-Initiated Billing) feature in SureCart.

With CIB, SureCart acts as the intermediary between the merchant and PayPal, allowing merchants to accept recurring payments without the need for Reference Transactions. This can be a simpler and more convenient solution for merchants who do not have the time or resources to go through the approval process for Reference Transactions.

## **How to enable the Reference Transactions on your PayPal account?**

To enable Reference Transactions on your PayPal account, please follow these steps:

1. Log into your PayPal account and find your local PayPal Support Help Center phone number. You can find this information on the PayPal website or by doing a quick internet search.
2. Call your local PayPal Support Help Center and explain that you are specifically calling to enable Reference Transactions on your account.
3. The representative may try to help you set up recurring payments with a button, but you need to insist that you want Reference Transactions enabled specifically.
4. The PayPal Specialist will ask for your PayPal account information and other questions related to your business, and will file a ticket to enable Reference Transactions on your account.
5. You will receive an email from PayPal within a few days, letting you know whether or not your account has been approved for Reference Transactions. If your account has been approved, you can begin using this feature to process recurring payments for your customers.

It is important to note that the approval process for Reference Transactions can vary depending on the merchant's location, business model, and other factors. Be prepared to provide any necessary documentation or additional information that PayPal may require to enable this feature on your account.

After you've been approved for reference transactions, SureCart will automatically use this feature to process subscription payments on your behalf. When reference transactions are enabled, the SureCart branding will not appear in the PayPal checkout flow.

Please note that the approval process for reference transactions can take several business days, and not all merchants may be eligible. If you're unable to enable reference transactions, you can still use SureCart's CIB (client-initiated billing) feature to accept subscription payments with the SureCart branding.

If you have any questions or need assistance with enabling reference transactions on your PayPal account, please don't hesitate to contact our support team. We're here to help!


===== SOURCE: paypal-ipn-warning-emails.md =====

---
source_url: https://surecart.com/docs/paypal-ipn-warning-emails
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/PayPal IPN Warning Emails

# PayPal IPN Warning Emails

This document explains PayPal Instant Payment Notification (IPN) warning emails that some SureCart users may receive.

## Introduction

Some users may receive warning emails from PayPal regarding Instant Payment Notification (IPN) failures at `https://app.surecart.com/`. These emails can be safely ignored and do not indicate a problem with SureCart transactions or account security.

## Understanding the Issue

SureCart does not use PayPal's IPN system. These warning emails are sent in error by PayPal and do not reflect an actual issue with SureCart or the connected PayPal account.

## What to Do

No action is required. These emails can be safely ignored.

PayPal may send multiple warning emails over time. This does not indicate a problem and will not affect payment processing or transaction functionality.

## Notes

- SureCart does not rely on PayPal's IPN system for transaction notifications.
- PayPal may continue to send these warning emails intermittently. This is expected behavior due to the error on PayPal's side.
- No configuration changes are needed in SureCart or PayPal to resolve this issue.

## FAQ

**Will ignoring these emails affect my payments or transactions?**

No. SureCart does not use IPNs, so these warning emails have no impact on payment processing or transaction functionality.

**Why is PayPal sending these emails if SureCart doesn't use IPNs?**

This is an error on PayPal's side. PayPal is incorrectly attempting to send IPNs to SureCart and generating warning emails when the notifications are not received.

**Should I disable IPN settings in my PayPal account?**

No action is needed. IPN settings do not need to be modified.


===== SOURCE: plugin-performance.md =====

---
source_url: https://surecart.com/docs/plugin-performance
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Change Your Plugin Performance Settings

# How to Change Your Plugin Performance Settings

If you aim to increase the load speed for products, shop, and checkout pages on your SureCart website, this guide is for you.

We're going to head into your WordPress to tweak some settings. Additionally, we'll guide you on integrating JavaScript with certain CDN providers where JavaScript is not enabled by default.

Let's get started!

### How to enable Plugin Performance in the SureCart Settings

In your WordPress website, within SureCart settings, you have the option to change the SureCart plugin performance by enabling the JavaScript ESM loader.

This JavaScript ESM loader is a tool or a method that enables loading and executing ECMA Script modules (ESM) in JavaScript environments. ESM has several benefits over the traditional CommonJS (CJS) modules, such as better performance, tree-shaking, and native browser support.

So, to enable this option in SureCart, follow the steps below:

- Go to the WordPress dashboard, and from SureCart, click on Settings.

- Click on the Advanced Tab.

- From the Performance section, toggle on the Use JavaScript ESM Loader and click on "Save" button.

After turning the ESM loader on, make sure to test your checkout forms in a private window on your browser. Because of browser caching, changes may not be applied immediately.

### How to Enable CORS Headers for JavaScript in Bunny.Net CDN

CORS headers, or Cross-Origin Resource Sharing headers, are HTTP headers used by web servers to define which origins (websites) are permitted to access a resource on a server. They provide a way for servers to overcome the default restrictions placed by the same-origin policy, a security measure that prevents web pages from making requests to a different domain than the one that served the web page. In essence, CORS headers allow web servers to specify who can access their resources and under what conditions, facilitating secure cross-origin requests in web applications.

Under the toggle switch of "Use JavaScript ESM loader" option, you can see a small note:

_This can slightly increase page load speed, but may require you to enable CORS headers for .js files on your CDN. Please check your checkout forms after you enable this option in a private browser window._

In the case of Cloudflare, JavaScript is pre-configured in the CORS headers. However, with certain CDNs, you must manually add the JavaScript in the CORS headers.

We'll take the example of Bunny CDN, where JavaScript is not automatically incorporated. It must be added to ensure the efficient working of the SureCart Performance – JavaScript ESM loader.

To add JavaScript to Bunny CDN's CORS headers, follow these steps.

- Log into your account from [Bunny CDN.](https://bunny.net/)

- Select the CDN tab and then click on the pull zones for which your website has been configured.

- Click on the Headers tab.

- Write "js" in the Extension List field, separated by a comma, and click the "Save" button to save the changes.

And that's it! This is how you can add CORS headers for JavaScript in Bunny.Net CDN.

We don't provide documentation for every CDN on adding JavaScript in CORS Headers; however, the process remains the same. You simply need to add ".js" to CORS headers in your CDN.

And if you get stuck, you can contact your CDN provider support for assistance.

Hope this helps you improve your website performance.

If you have any questions, do not hesitate to contact us!


===== SOURCE: pre-fill-checkout-fields.md =====

---
source_url: https://surecart.com/docs/pre-fill-checkout-fields
source: surecart-kb
scraped: true
---

# How to Pre-Fill the Checkout Fields via URL Parameters

With SureCart, you can share checkout page links with customers whose names, emails, and other details are filled in, so they don't have to type it all out. This can speed up the checkout process.

Benefits of pre-filling checkout fields:

- **Time-saving:** Automatically populating the form with user information.
- **Reduced friction:** Minimizes the effort required from users, making it more likely for them to complete the checkout process.
- **Personalization:** Creates a more personalized customer experience.

### Available Fields to Prefill via URL Parameters

| Fields      | Parameters |
| ----------- | ---------- |
| First name: | first_name |
| Last name:  | last_name  |
| Full name:  | full_name  |
| Email:      | email      |
| Coupon:     | coupon     |

### How to Construct a Proper URL with Parameters

1. Add a question mark (?) to the end of the product URL to start adding parameters:

```
https://example.com/product?
```

2. Add the desired URL parameter, for instance first_name, followed by an equal (=) sign:

```
https://example.com/product?first_name=
```

3. Input the user's first name, such as John:

```
https://example.com/product?first_name=John
```

4. If you want to add more parameters, add the ampersand symbol (&) and insert more parameters and their values:

```
https://example.com/product?first_name=Peter&
```

5. For additional parameters, repeat Steps 2 and 3:

```
https://example.com/product?first_name=Peter&email=peter@example.com
```

### How to Correctly Insert Spaces in URL Parameters

URL parameters can include spaces. For example, to represent a full name such as "Otto S. Hatfield" within a URL:

```
https://example.com/product/?full_name=Otto%20S.%20Hatfield
```

### How to Share a Product with Prefilled Parameters

- Access your product on SureCart and select 'Copy Links' from the Pricing section.
- Locate the "Buy Link" field and click the 'Copy' button to grab the URL.
- Paste the copied URL into your browser.

To add customer information and promotional details to the URL, add the following parameters: first_name for First Name, last_name for Last Name, full_name for Full Name, email for Email, and coupon for Coupon.

For example, to pre-fill the parameters with the first name as Peter, last name as Smith, email as peter@example.com, and a coupon code as 20-OFF-SECRET:

```
https://example.com/checkout/?line_items%5B0%5D%5Bprice_id%5D=1a830bba-ede0-4640-88ff-c1d5a94fe993&line_items%5B0%5D%5Bquantity%5D=1&first_name=Peter&last_name=Smith&full_name=Peter%20Smith&email=peter%40example.com&coupon=20-OFF-SECRET
```

Once the customer accesses the shared link, they will be redirected to a checkout page already populated with their information.


===== SOURCE: price-boost.md =====

---
source_url: https://surecart.com/docs/price-boost
source: surecart-kb
scraped: true
---

# Price Boost

In this guide, we'll explain what the Price Boost is, how you can benefit from it, and provide step-by-step instructions for setting it up.

### What is the Price Boost?

The Price Boost feature allows users to easily switch the pricing option of a product on the checkout page with a single click.

For example, suppose you offer a product with a monthly subscription but want to encourage customers to switch to a yearly subscription by providing a 20% discount for upfront payment.

With the Price Boost feature, customers can instantly swap from a monthly to a yearly plan at checkout, bringing in more upfront revenue for your business and helping to reduce churn typically associated with monthly subscriptions.

### Benefits of Price Boost

- **Increases upfront revenue:** Encourages customers to make larger, annual payments rather than smaller monthly ones.
- **Reduces churn:** Customers on annual plans are less likely to cancel frequently.
- **Enhances customer experience:** Offers flexibility and choice at the point of purchase.
- **Supports promotional strategies:** Makes it easy to implement discounts and incentives for longer-term commitments.

### How to Set Up Price Boost

To add a price boost, you can either edit the price of an existing product or create a new price option:

- Click the Edit button next to the price you want to modify.
- Scroll down to the Price Boost section.
- In this section, you'll find the **Swap to** option, where you can select the price that customers will be able to switch to during the checkout process.
- Click the **Select a price** dropdown to display all available pricing options. The price(s) associated with the product you are currently editing will appear at the top of the list.
- Add a description for the price boost. This description will be displayed to the customer on the checkout page, helping them understand the benefit of switching to the new pricing option.
- Click the **Update Price** button to save your changes.

That's it! Now the user will be able to swap the price with a single click during checkout.

### Frequently Asked Questions

**Does the price boost need to be for the same product?**

No! You can set a swap price for any price and any product.

**Why isn't the price boost visible for variant products?**

This feature is not currently available in the initial release, but is planned for a future update.


===== SOURCE: product-access-actions.md =====

---
source_url: https://surecart.com/docs/product-access-actions
source: surecart-kb
scraped: true
---

# How to Revoke, Unrevoke or Expire Product Access

If you are selling a digital product, SureCart also manages to grant product access to your customers after their purchase.

This will be very useful when you are selling digital products. For example, if you want to start selling a copy of your music album for download.

You can easily do this by creating a SureCart product, uploading your downloadable file, in this case, your album, and then saving it for purchase.

After your customers purchase your album, they'll get a link where they can download the file directly from your shop.

This all happens automatically and the access and links are both sent to their emails and added to their customer dashboard for easy access.

Part of being able to manage this access is also the ability to revoke it. There may be times when you may want to remove and control the access should there be any issues that arise after the purchase.

Other reasons may be:

- Limit distribution of your downloadable products
- Preventing unauthorized usage
- Discontinuing a user's privileges for a particular service

With SureCart you have full control over your products and everything you sell. You can revoke or even restore/unrevoke or expire access any time you want.

### Revoking Product Access

The process for revoking access to digital products and subscriptions is the same and pretty straightforward. You can simply follow the steps below:

1. On your WordPress Dashboard, locate **SureCart** > **Customers**.
2. Look for the Customer that you want to remove access to and click their name.
3. On the Customer Page, look for the section that says **Purchases**, and click **Revoke** on the products that you want to remove their access to.
4. Click **Revoke Purchase** on the popup modal.

From here the customer will no longer be able to access the product or subscription, nor will they be able to see it from their Customer Dashboard.

### Unrevoking Product Access

If you've made a mistake or would like to restore access to that certain customer, you can also easily do that.

1. On your WordPress Dashboard, locate **SureCart** > **Customers**.
2. Look for the Customer that you want to restore access to and click their name.
3. On the Customer Page, look for the section that says **Products**, and click **Unrevoke** on the products that you want to restore their access to.
4. Click **Unrevoke Purchase** on the popup modal.

After this, the customer's access should be restored and they will be able to access the product once again.

### Expiring Access for One-Time Product Purchases

This feature works for all one-time payments in SureCart.

If you ever need to sell a one-time product for a limited time, For example, a 1-month LearnDash webinar, you can use the **Expire access** option and set it to end after 30 days.

After 30 days, the customer's access to the purchased webinar will expire.

Such a feature can be especially useful for digital products with one-time prices.

You can activate this directly from your product's interface instead of going to the Customer section.

Navigate to the **Products** section and select your desired product.

Toggle the **Expire access** button and enter the number of days after which you want to revoke the product's access.

Now, your customer's webinar product will automatically expire after 30 days.


===== SOURCE: product-card.md =====

---
source_url: https://surecart.com/docs/product-card
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Elementor](https://surecart.com/docs-category/elementor/)/Product Card

# Product Card

This guide explains how to use the SureCart Product Card within Elementor. This functionality is especially useful if you want to create a custom shop page or display individual products on any page or post.

Let's get started!

### **Elementor Loop Grid**

In order to use the SureCart Product Card element, you need to use it inside an Elementor Loop Grid. You can do this on any page or post, so it's very handy.

- First, create a page or post and edit it with Elementor. Once you are inside Elementor, add a container and then add the Loop Grid inside it.
- In the 'Choose template type' dropdown, select 'Posts' and then click on the 'Query' tab.

- In the Source dropdown, select SureCart Product.
- We will leave the other settings as they are, but you can adjust them according to your preferences.

- Now, click on the Create a template button. This will open a modal window.

- Click Save to apply the changes.

- In the template, you can either add the Product Card element directly or click on the SureCart icon. For this example, we will select the SureCart icon since it shows the available templates. This is the recommended approach if you want to quickly use existing layouts.

- Click the Insert button to add the Product Card to your design.

- Click the Publish button located in the top-right corner of your screen to save and publish your changes.

That's it! You can now view the page on the front end to see it in action.

### **Frequently Asked Questions**

**Where can I add the SureCart Product Card?**

The SureCart Product Card can be used to create a grid of your products in your store. You can add it to any page or post where you want to showcase products.

**Can I customize the Product Card layout?**

Yes, you can easily customize and design e-commerce collection pages by taking advantage of SureCart's dynamic elements within your page builder.

**Can I create custom templates for my Product Cards?**

Yes, you can apply personalized designs to your product collections to ensure a cohesive and optimized shopping experience for your users.


===== SOURCE: product-collections.md =====

---
source_url: https://surecart.com/docs/product-collections
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Add and Manage Product Collections Or Categories

# How to Add and Manage Product Collections Or Categories

Product Collections are a way to group related products together. For example, if you run a clothing store, you might have collections like "Men's Apparel," "Women's Apparel," "Footwear," etc.

Collections help organize your products, making it easier for customers to navigate your store and find what they're looking for.

### **How to Create a Collection**

1. Click on "Products" in the SureCart menu.
2. Click on the "Collections" menu.
3. Click on the "Add New" button.
4. Optionally modify the suggested permalink by clicking the edit icon.
5. Add a description if desired.
6. Click the "Create" button.

### **How to Add Products to Collections**

1. Go to **SureCart → Products**.
2. Click "Edit" for the product you wish to add to a collection.
3. Click the "Add to Collection" button under the Collections section.
4. Select the Collection(s) from the dropdown menu.
5. Click "Save Product".

### **Adding Product Collections to the Site Menu**

For Classic Themes:

1. Go to **Appearance → Menus**.
2. Click the "Screen Options" tab.
3. Check "Product Collections".
4. Expand "Product Collections" and check the collections to add.
5. Click "Add to menu" then "Save Menu".

### **How To Change Collections Permalink**

Go to **Settings → Permalinks**, choose the desired option, and click "Save Changes".

### **How to Modify a Collection Template**

1. Click on the "Default" option from the Template dropdown menu.
2. Select the SureCart Layout options.
3. Click "Edit template" to open the edit template screen.
4. Make desired changes and click "Save".

### **Frequent Asked Questions**

**Can I create a template for Collections in Elementor or another page builder?**

Not at the moment. Only Gutenberg is currently supported.

**Are there any available shortcodes for Collections?**

Yes. Refer to the [list of all shortcodes](https://surecart.com/docs/all-shortcodes/) for the "Product Collections Page" section.


===== SOURCE: product-content-bricks.md =====

---
source_url: https://surecart.com/docs/product-content-bricks
source: surecart-kb
scraped: true
---

# How to Create and Edit Product Content (Long Description) in Bricks - SureCart

## Overview

This guide explains how to create and edit product long descriptions in SureCart using Bricks Builder, enabling you to enhance product pages with images, videos, links, and custom layouts.

## Creating the Content

### Step 1: Enable SureCart Product Post Type
Navigate to **Bricks > Settings**, locate the **Post Types** section, and enable **SureCart Product**. Save your settings.

### Step 2: Open Content Designer
Go to the product where you want to create content and click **Open Content Designer** to begin customization.

### Step 3: Edit with Bricks
Click the **EDIT WITH BRICKS** button in the top bar to open the Bricks editor and create your content.

## Adding Content to the Product Template

1. **Insert Post Content Element**: Edit your Product Template and add the **Post Content** element to your desired section. **Important**: Avoid placing content inside the Product Form wrapper, as this may cause unexpected behavior.

2. **Select Data Source**: In the Data source dropdown, select "Bricks" to automatically display your content on the product page.

## Frequently Asked Questions

**Storage Location**: Content is stored exclusively in the WordPress database and does not rely on the SureCart server.

**Description vs. Content**: Description is basic text-only formatting stored on SureCart servers. Content offers full design flexibility with styling and animations, stored in WordPress.

**Content Not Displaying?**: Verify the product template is set to **Theme Layout** rather than **SureCart Layout**.


===== SOURCE: product-content-description.md =====

---
source_url: https://surecart.com/docs/product-content-description
source: surecart-kb
scraped: true
---

# How To Customize Product Content (Long Description) - SureCart

## Overview

This guide explains how to create and edit product long descriptions in SureCart using the WordPress block editor.

## Creating the Content

### Initial Steps

1. Navigate to the product you want to edit
2. Locate the Content section and click "Open Content Designer"
3. The editor will open where you can modify content

### Editing Process

The editor provides three key functions:

- **Content Area**: Type or add blocks directly into the space provided
- **Toolbar**: Access styling and modification options on the right side
- **Save Button**: Located in the top-right corner to preserve changes
- **Return Arrow**: Top-left corner button to go back to the product edit page

### Content Flexibility

You can use native WordPress blocks or integrate third-party tools like Spectra or other block libraries for enhanced customization options.

## Adding Content to Product Template

The content block typically appears automatically in product templates. To add or relocate it:

1. Edit your Product Template
2. Drag and drop the content block to your desired location

## Frequently Asked Questions

**Storage Location**: Content is stored exclusively in the WordPress database, not on SureCart servers.

**Description vs. Content**: The description field supports basic formatting (bold, italic, bullet points) and stores data on SureCart servers. Content offers full design flexibility with animations and page builder capabilities, stored in WordPress.

**Content Not Displaying**: Ensure your product template is set to "Theme Layout" rather than "SureCart Layout" on the Edit Product page.


===== SOURCE: product-content-elementor.md =====

---
source_url: https://surecart.com/docs/product-content-elementor
source: surecart-kb
scraped: true
---

# How to Create and Edit Product Content (Long Description) in Elementor - SureCart

## Overview

This guide explains how to create and edit product long descriptions using Elementor within SureCart, allowing you to build visually rich product pages with images, videos, links, and custom design elements.

## Creating Content for Elementor

### Step 1: Enable SureCart Product Post Type
Navigate to **Elementor > Settings** and check the box for **SureCart Product** under Post Types to enable Elementor editing capabilities.

### Step 2: Access the Product
Go to the product where you want to create content and click **Open Content Designer**.

### Step 3: Edit with Elementor
In the top bar, click **Edit with Elementor** to open the editor and create your content using Elementor's drag-and-drop interface.

## Adding Content to the Product Template

### Step 1: Edit Product Template
Open your Product Template in Elementor.

### Step 2: Place Content Element
Use the drag-and-drop editor to position the content element exactly where you want it displayed on the product page.

### Step 3: Configure Template Settings
Select to display the template for all products, then click **Save & Close** to apply the changes across your store.

## Key Differences: Description vs. Content

| Aspect | Description | Content |
|--------|-------------|---------|
| Storage | SureCart server | WordPress database |
| Formatting | Basic text (bold, italic, bullets) | Full design flexibility with animations |
| Capability | Limited styling | Page builder integration |

## Troubleshooting

**"Edit with Elementor" button not visible?**
Ensure "SureCart Product" is checked in Elementor Settings > General > Post Types.

**Content not displaying?**
Verify the product's template is set to "Theme Layout" rather than "SureCart Layout."


===== SOURCE: product-list-guide-shop-page.md =====

---
source_url: https://surecart.com/docs/product-list-guide-shop-page
source: surecart-kb
scraped: true
---

# Product List Guide – Shop Page

### **What is Product List**?

SureCart offers a flexible product list block to showcase a grid of your products in your store.

When you set up your store in SureCart, a default shop page named **Shop — Sample Page** is automatically created for you. This page contains some sample product items, displaying them based on the chosen theme. You can find this page under the **Pages** section in your WordPress dashboard.

### **Product List Customization Features**

#### **Sidebar**

You can configure the default state of the Sidebar, either open or closed, by selecting the Sidebar component and enabling or disabling the "Open by default" toggle. You can also adjust the position of the block to either Default (fixed) or Sticky.

#### **Products per Page**

You can choose how many products are displayed per page to suit your layout preferences.

#### **Auto Fixed Columns**

You can choose a fixed number of columns to display or set a minimum column width to automatically adjust to your page size.

#### **Pagination Options**

If you have a large number of products, you can enable the **Paginate** option to organize them across multiple pages. This feature adds **Next** and **Previous** buttons, allowing users to easily navigate between pages. You can also customize the pagination font size.

#### **Sort and Filter**

Sorting and filtering options help your customers navigate your products more easily. Customers can sort products by their latest additions, oldest items, price (low to high) and price (high to low). You can also set the default sorting option.

#### **Taxonomy Filtering**

SureCart allows you to assign custom taxonomies to products and filter them within the product list block. To add a filter, duplicate an existing filter block, and in the settings panel on the right, select the desired taxonomy under the **Taxonomy** dropdown.

#### **Search Products**

Your customers have the ability to search for specific products within your list. In case you don't want to show the search, you can simply remove this block.

#### **Choose the Products You Want to Display**

Select which products you want to display on your product list. You can either show all, featured, or hand-picked products based on your preference.

#### **Edit Products**

SureCart allows you to edit each product card individually, giving you complete control over how your products are displayed. In the editor, you can:

- Change the text size and font of product titles
- Update product image like aspect ratio, border, margin etc
- Set custom price ranges
- Adjust the padding between product items

### **Integrating ShortCodes**

For those who prefer shortcodes, SureCart provides the flexibility to configure your product list.

```
[sc_product_list] - Display a list of products in a grid.
   "columns": It sets the number of columns, defaulting to 4.
   "limit": It sets the maximum limit, defaulting to 15.
   "pagination_enabled": It enables or disables pagination, defaulting to enabled (true).
   "ajax_pagination": It activates or deactivates AJAX pagination, defaulting to enabled (true).
   "pagination_auto_scroll": It turns on or off automatic scrolling when new results are loaded, defaulting to on (true).
   "search_enabled": It allows or disallows the use of a search function, defaulting to allowed (true).
   "sort_enabled": It permits or prohibits sorting functionality, defaulting to permitted (true).
   "ids": The product ids you want to show here, separated by a comma.
   type="custom": This is useful if you do not wish to display all of the products from the shop page on a page but only custom ones.
```

Example shortcode for a page builder:

```
[sc_product_list columns="3" limit="9" ids="049627ac-f5e0-4157-a530-c4b2dbef82bb,c960b061-d321-43e3-a151-8c40b35f0c22,a114295c-198a-4e33-aa47-ab7d07172193" search_enabled="true" sort_enabled="true" type="custom"]
```


===== SOURCE: product-page-custom-fields.md =====

---
source_url: https://surecart.com/docs/product-page-custom-fields
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How To Add Custom Fields To Your Product Page

# How To Add Custom Fields To Your Product Page

This guide will show you how to create a custom field and display it on your SureCart product page.

For this tutorial, we'll use the **MetaBox** plugin as an example, but you can use any tool you prefer, such as **ACF**. These tools can recognize your SureCart product post type and make it easy to add custom fields.

For instance, if you want to run a scarcity campaign, you could add a custom field like **"Product on Sale"** to highlight products that are part of a limited-time promotion. This helps buyers quickly identify products with active sale offers.

In this example, we'll add a "Product on Sale" field to a product page, but you can also use custom fields for other purposes, like file uploads, maps, or images.

Let's get started!

### List of All Product Custom Fields

The following table outlines all SureCart native product custom fields. For each field, we've included a description to help you understand its purpose, along with a practical example to show how it might be displayed on your website.

| **Custom Field**           | **Description**                                                            | **Example**        |
| -------------------------- | -------------------------------------------------------------------------- | ------------------ |
| **min_price_amount**       | The lower price of the product, excluding the currency symbol.             | `99.90`            |
| **max_price_amount**       | The higher price of the product, excluding the currency symbol.            | `149.90`           |
| **display_amount**         | How the price is displayed, including the currency symbol.                 | `$99.90`           |
| **scratch_display_amount** | The "original" price or list price, displayed with a currency symbol.      | `$120.00`          |
| **range_display_amount**   | A range showing the lowest to the highest price of the product.            | `$99.90 - $149.90` |
| **available_stock**        | The current stock level of the product.                                    | `25`               |
| **sku**                    | The product's SKU (Stock Keeping Unit) code.                               | `SC-001`           |
| **weight**                 | The product's weight without the unit (e.g., kilograms, grams, or pounds). | `1.5`              |
| **weight_unit**            | The unit of the product's weight (e.g., kg, g, lb).                        | `kg`               |

### **Configuring Custom Fields In Meta Box**

**Note**: You need to have the Metabox plugin installed and activated on your site before we proceed.

To do this, go to your WordPress dashboard, and:

- Navigate to **Meta Box** > **Custom Fields**.

- Here, click **Add New** to create a new field group.

- Name the field group anything descriptive, like "Product on Sale." This is for your internal reference.

- Click the **Add Field** button and choose any field type. In this example, we'll use a "Switch" field type, so you can enable or disable the campaign on each product.

You can search and choose any other field type you wish.

- Click the newly created field to open its settings and customize how it will appear in your product editor.

- Under **Settings**, choose "SureCart Product (sc_product)" along with the "Post Type" dropdown. This ensures the custom field will show up on your product pages.

**Note**: You can choose to add it for all your products or just specific [product collections](https://surecart.com/docs/product-collections/).

Click the "Publish" button on the right to add the custom field to your SureCart product settings.

### **Customizing The Custom Fields In Your Product Settings**

Now, you should see the custom field added to your product settings, to verify it:

- Go to **SureCart** > **Products** and select any preferred product.

- Scroll down to the Content section and click on the Open Content Designer button.

You can now view the custom field and manage whether the sale offer is visible for each product.

Once done, click the **"Save Product"** button in the top-right corner. The custom field will then appear only for the product where you enabled it.

### Displaying Custom Fields With The Block Editor

If you are using the block editor (Gutenberg), you can display SureCart product custom fields on your product pages using the **Meta Field Block** plugin. This plugin allows you to display any custom field in the Gutenberg editor easily and works seamlessly with SureCart custom fields.

#### Using Meta Field Block Plugin

The **Meta Field Block** plugin provides a straightforward way to display custom fields as blocks directly within the Gutenberg editor.

**Steps to Use Meta Field Block**:

1. Install and activate the **Meta Field Block** plugin from the WordPress repository.
2. Edit your product template.
3. Add a new block and search for **Meta Field Block**.
4. In the block settings, input the **Field Name** corresponding to the SureCart custom field you want to display. For example:
   - `min_price_amount`
   - `max_price_amount`
   - `display_amount`
   - `available_stock`
   - `sku`

5. Save the changes and preview your product page to ensure the field is displayed correctly.

#### Example Use Case

If you want to display the **Available Stock** of a product on the product page:

- Add a **Meta Field Block** in the Gutenberg editor.
- Enter `available_stock` as the Field Name in the block settings.
- Save the changes.

On the frontend, the stock level will display dynamically.

### **Displaying The Custom Fields** With Bricks Builder

Now, you'll need to decide where and how to display the custom field on your product's front end.

To do that, open your product template in the page builder of your choice. For this guide, we'll demonstrate using the Bricks builder, but this can also be done using the block editor.

- Drag the "Basic Text" field anywhere on the product page where you want to display the custom field.

- Select the basic text element, delete any text inside of it, and click on the following "Dynamic Data" symbol inside.

- Select the custom field label that you want to add here. For example, we'll search and select the "Fabric Details" custom field here.

A new shortcode will be added inside the basic text field. Your custom field will be embedded and displayed here. Finally, click on the "Save" or "Publish" button.

The custom field content should now appear on the product front end. Verify it yourself to check the same.

That's it! You can create many more custom fields to enhance your product pages, making them more dynamic and tailored to your needs regarding the builder you are using.


===== SOURCE: product-page-in-elementor.md =====

---
source_url: https://surecart.com/docs/product-page-in-elementor
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Elementor](https://surecart.com/docs-category/elementor/)/Product Page

# Product Page

Learn how to create stunning SureCart product pages using our native Elementor components. This guide will walk you through the complete setup process.

**Important**: Elementor Pro is required to create custom templates.

Let's get started!

### **First Steps**

Before creating your product page template, ensure proper integration by completing these initial setup steps:

- Navigate to Elementor > Settings
- Under Post Types, locate and check "SureCart Product"
- Click "Save Changes" to apply

- Navigate to the Features tab in Elementor settings
- Scroll down to locate the Container section

- Look for the green indicator dot next to "Container" in the Features list
- If the indicator is not green:
  - Click the dropdown menu and enable the feature
  - Click "Save Changes" to apply

You're now ready to build your SureCart product template with Elementor!

### **Creating a Product Template in Elementor**

Creating a SureCart product template follows the same process as other Elementor templates, with the key difference being the selection of the SureCart Product layout.

- Navigate to Templates > Theme Builder

- Click the Add New button (+) in the top-right corner of the Theme Builder interface

- Locate the SureCart Product card in the template options
- Click the plus icon (+) within the SureCart Product box to begin customization

SureCart offers two pre-designed product templates:

- Product Form (Left)
- Product Form (Right)

To implement your chosen template:

- Review both layout options
- Select the template that best suits your needs
- Click the Insert button beneath your preferred layout

The Structure panel provides access to all SureCart elements for customization, including:

- Product Form
- Product Name
- Pricing
- Product Description
- Price Selector
- Variant Pills
- Quantity
- Custom Amount
- Add to Cart Button
- Buy Now Button
- Product Media

**Note**: We won't cover the customizations in this documentation as it is outside its scope.

- When you're satisfied with your template design, click the Publish button in the top-right corner of the screen.

- A prompt will appear asking, "Where Do You Want to Display Your Template?" Click the Add Condition button to specify where your template will appear on your site.

To apply the template to all products (recommended for most cases):

- Select All Products from the dropdown menu
- Click Save & Close to confirm your selection

Preview your product page on the frontend to verify all elements appear as intended. In this example, we've implemented:

1. Right-aligned gallery layout
2. Truncated product description (30 characters with ellipsis)
3. Rounded variant pills for better visual appeal

That completes the product template setup! You can now explore individual SureCart Elements and Settings to further customize your template. If you'd like, share your template design with the community in our Facebook group.

### **Frequently Asked Questions**

**Why are my SureCart widgets not showing up, or why isn't the SureCart template being inserted in Elementor?**

SureCart widgets require specific elements to be enabled in Elementor's Element Manager. Ensure that the following elements are enabled:

– Post title

– Post Excerpt

– Text Editor

– Heading

– Container

– All SureCart blocks

Without these elements enabled, the SureCart Form Widget will not be inserted properly.

To configure these settings, go to **Elementor > Element Manager** and enable the required elements.

**Why isn't my template showing up on my product page?**

Here are a few reasons your template isn't showing up. Let's review some possibilities:

– Check if your product is set to the theme layout instead of the SureCart layout in the Template area of the edit product page.

– Verify that you don't have another template created for SureCart Product that takes precedence over the one you just created.

– Ensure you have selected the correct display condition for the template.

**Can I have different templates for different products?**

Yes! Create multiple templates and set specific display conditions for each product, product collection and others conditions.

**What does the warning "SureCart widgets must be placed inside a 'Product Form' container to function properly" mean?**

This warning indicates that your SureCart widgets, such as Product Name, Pricing, Add-to-cart and others, are not placed within the required "Product Form" container in your Elementor template. **Importantly, this notice is only visible to logged-in admins and will not be shown to regular site visitors or customers**.

To fix this, make sure that the main container holding your SureCart widgets in your Elementor Product template has the "Container Type" setting changed from "default" to "Product Form". This ensures that the widgets function correctly on your product page.


===== SOURCE: product-page-template-bricks.md =====

---
source_url: https://surecart.com/docs/product-page-template-bricks
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/How to Create a Product Page Template in Bricks Builder

# How to Create a Product Page Template in Bricks Builder

This document explains how to create and assign a custom product page template using Bricks Builder for SureCart products.

### **Requirements**

- WordPress admin access
- SureCart is installed and activated
- Bricks Builder installed and activated
- At least one published SureCart product

### **Configure SureCart Settings in Bricks Builder**

Before you begin designing your product page in Bricks Builder, you'll need to enable the SureCart Product post type in the Bricks Builder settings.

To do this, navigate to **Bricks > Settings**. Under the **General** tab, in the **Post types** section, activate the toggle for **SureCart Product**.

### **Creating SureCart Single Product Template**

To apply a consistent layout to all your product pages in Bricks, you need to create a SureCart Single Product template.

**Please note**: You can also create different layouts based on taxonomies and/or collections, but that is beyond the scope of this article.

To create the SureCart Single Product template, follow these steps:

- Go to **Bricks > Templates**;
- Click the **Add New Template** button.
- Give the template a name; in this case, "Product Template" (1).
- In the **Template type** dropdown, select **SureCart – Single Product** (2).
- Click the **Publish** button (3).
- Then click the **Edit with Bricks** button (4).
- Search for "section" in the elements panel (1).
- Click on the **Section** element to add it to the canvas (2).
- Click on the **Container** (1) in the Structure panel on the right.
- Click on the **Elements** button (2) to add a SureCart Element to the container.
- Search for "product" (1) in the elements panel for quicker selection.
- Click on the **Product Form** element (2) to add it to the container.

A pre-built product page layout is available to help adjust styles more efficiently.

- Click the **save** button to save your changes.
- Test the template on the frontend to confirm it is working as expected.

### Notes and Limitations

- SureCart elements such as Add to Cart, Collection Tags, Product Media, and others must be placed inside the Product Form or Product Card block.
- These elements will not function correctly if placed outside these containers.

### Expected Outcome

Once completed, SureCart products will use the custom Bricks product page template, displaying product information and purchase elements according to the configured layout.

### **FAQ**

**Why aren't my Add to Cart, Collection Tags, Product Media, and other elements working correctly?**

For SureCart elements to function properly, they must be placed inside the Product Form or Product Card block. Elements placed outside these containers will not work as expected.

**My Single Product template is not loading.**

This usually happens when multiple templates share overlapping conditions. If no specific condition is set, Bricks applies a catch-all condition that may conflict with other templates.

Review your existing templates and ensure there are no conflicting conditions. Also, confirm that the Product Form or Product Card wrapper is present in the template.


===== SOURCE: product-pages-guide.md =====

---
source_url: https://surecart.com/docs/product-pages-guide
source: surecart-kb
scraped: true
---

# Product Pages Guide

Product pages are an important part of your SureCart online store, and customizing them can enhance your overall customer experience.

This is the individual product page that shows up when you click on a particular product.

If you're using a page builder like **Elementor** or **Bricks Builder** to customize your product pages, dedicated step-by-step guides are available.

### **Customizing Product Permalinks**

Permalinks are like personalized address links for each product on your website. They help people find and access specific products easily.

- Navigate to the **Permalinks** section in your WordPress dashboard under **Settings** to customize product permalinks.

### **Product Template Customization**

When a customer clicks on an individual product, they are directed to a page that SureCart allows them to customize.

- To edit individual products, navigate to the desired product from your WordPress dashboard.
- To personalize your product page, click in the **Edit Template** button within the Template section.

The options may vary depending on your WordPress theme, Classic or FSE Theme.

#### Add New Template

With SureCart, you can create a brand-new template for your product page. Click on the **Add new template** icon and give it a name.

Click on the **Edit template** button to start customizing your product page.

In the editor, click on the **List view** icon to view various customization options.

#### **Editing the Product Title**

Upon selecting the **Product Title**, a mini editor block will appear on the right-hand side with basic title customization settings: text position, alignment, heading levels, and more.

#### **Customizing Product Price Choices**

These are the prices associated with your product. You can customize how these prices are displayed — choose the number of columns, display format, edit product prices, and edit the **sale text**.

#### **Editing Product Description**

You can change the text, experiment with background colors, try different fonts, adjust margins and spacing, align the product description, and more.

#### **Customizing Product Variants**

SureCart's Product Variants feature allows you to offer different color options for your product. You can modify the text color, background, and font for indicating the color of the variant. You can also adjust margin and padding settings.

#### **Customizing Pricing Options**

These are the pricing options available for your product (e.g., one-time payment or subscription). You can add/remove pricing options by adjusting the columns section, decide whether to show or hide the price numbers, and change the label.

#### **Product Quantity and Add to Cart/Purchase Buttons**

You can modify product quantity label as well as the wording for the Add to Cart and Buy Now buttons. You can also edit the terminologies for "out of stock" and "unavailable" labels.

#### **Change Product Featured Image**

With image customization, you can:

- Adjust the image mode to **Gallery or Slideshow view**
- Activate **Auto Height** that allows the image to fit to the page according to its height
- Set your desired maximum image width
- Easily control the number of thumbnails on display

### **Product Page Shortcodes**

If you prefer creating product pages in your page builders theme builder feature, you can use the following shortcodes:

```
[sc_product_description] - The product description
[sc_product_price] - The currently selected price
[sc_product_variant_choices] – Displays the variant choices of a product that contains variants
[sc_product_price_choices] - Shows the pricing choice of a product
[sc_product_media] - The product image or slideshow
[sc_product_quantity] - The product quantity selector
[sc_product_cart_button] - The add to cart button
```

**Important Note**: The ID parameter in SureCart shortcodes won't work in SureCart version 3 and above. Starting in version 3, SureCart uses WordPress Interactivity API. Please update your shortcodes to work with the new version.


===== SOURCE: product-reviews-shortcodes.md =====

---
source_url: https://surecart.com/docs/product-reviews-shortcodes
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Display Product Reviews Using Shortcodes

# How to Display Product Reviews Using Shortcodes

This document explains how to use SureCart product review shortcodes to display reviews on any page, including pages built with Divi, Beaver Builder, Oxygen, and other page builders that do not support the WordPress Block Editor.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- Reviews enabled on the product in SureCart
- The Product UUID, if the shortcodes will be placed on a non-product page (see _Finding the Product UUID_ below).

## **Finding the Product UUID**

All shortcodes accept an optional product_id attribute, which corresponds to the SureCart product UUID. The UUID is a string of letters, numbers, and hyphens (for example, eee96da1-be2b-488d-bd76-cdb0c96b118f).

When the shortcode placement requires the UUID:

- **On product pages:** The product_id attribute is optional. The shortcode automatically detects the current product.
- **On non-product pages (landing pages, custom pages, etc.):** The product_id attribute is required. Without it, the shortcode renders no output.

### **How to Locate the Product UUID**

1. Go to **WordPress Dashboard → SureCart → Products**.
2. Click the product to open the Edit Product page.
3. Look at the browser address bar. The UUID is the value of the id parameter at the end of the URL.

Example URL: /wp-admin/admin.php?page=sc-products&action=edit&id=eee96da1-be2b-488d-bd76-cdb0c96b118f. The UUID is the value after id=.

**Note:** The Product UUID is not the same as the WordPress post ID. The Product UUID is assigned by SureCart and is always a string of letters, numbers, and hyphens. Using a numeric WordPress post ID with the product_id attribute does not work.

## **Available Shortcodes**

### **sc_product_review_rating_stars**

Displays the average rating as filled, half, or empty stars.

**Basic usage:**

```
[sc_product_review_rating_stars]
```

**With attributes:**

```
[sc_product_review_rating_stars product_id="eee96da1-be2b-488d-bd76-cdb0c96b118f" size="24px" fill_color="#f59e0b" link_to_reviews="true"]
```

| **Attribute**   | **Type** | **Default**         | **Description**                                                                                            |
| --------------- | -------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| product_id      | string   | —                   | Product UUID. Required on non-product pages. Auto-detected when the shortcode is placed on a product page. |
| size            | string   | 20px                | Size of each star icon.                                                                                    |
| fill_color      | string   | Theme primary color | Color for filled stars (for example, #f59e0b).                                                             |
| link_to_reviews | boolean  | false               | Wraps the stars in a link to the reviews section.                                                          |

### **sc_product_review_rating_value**

Displays the average rating as a numeric value (for example, 4.5).

### **sc_product_review_total_count**

Displays the total number of reviews (for example, 156 reviews).

### **sc_product_review_breakdown**

Displays a 5-star breakdown with progress bars showing the distribution of ratings.

### **sc_product_review_list**

Displays the full review experience, including a summary section, filter sidebar, individual reviews with pagination, and the Write a Review form modal.

### **sc_product_review_add_button**

Displays a Write a Review button that opens the review form modal. If the user is not logged in, the user is redirected to the customer dashboard to sign in first.

## **Notes and Limitations**

- Reviews must be enabled on the product in SureCart for any shortcode to render output.
- The product_id attribute uses the SureCart product UUID, not the WordPress post ID.
- These shortcodes use the WordPress Interactivity API.

## **Related Documentation**

- [How to Enable and Configure Product Reviews](https://surecart.com/docs/product-reviews/)
- [How to Import Reviews in SureCart](https://surecart.com/docs/how-to-import-reviews-in-surecart/)
- [All SureCart Shortcodes](https://surecart.com/docs/all-shortcodes/)


===== SOURCE: product-reviews.md =====

---
source_url: https://surecart.com/docs/product-reviews
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Enable and Configure Product Reviews

# How to Enable and Configure Product Reviews

This document explains how to enable Product Reviews in SureCart and configure the display of ratings on product pages.

**Important — Existing Stores Must Update Templates:** If your store was created before the Reviews feature was introduced, you must manually update your product templates. Reviews are not automatically added to existing templates.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- At least one published product

## **Enable Product Reviews**

1. Go to **WordPress Dashboard → SureCart → Settings → Reviews**.
2. Enable Product Reviews.
3. Click Save.

## **Product-Level Review Settings**

1. Go to **WordPress Dashboard → SureCart → Products**.
2. Click on the product to configure.
3. In the Reviews panel on the right sidebar:
   - Enable Reviews: Toggle to show or hide reviews for this product on the frontend
   - Review Request Email: Toggle to enable or disable automatic review request emails
4. Click Save Product.

## **Configure Review Settings**

### **Send Review Request Emails**

Sends an automatic email asking customers to leave a review after their order is fulfilled.

1. Go to **SureCart → Settings → Reviews**.
2. Enable **Send Review Request Email**.
3. Set the number of days under "When should we ask for a review?"
4. Click Save.

### **Verified Buyer Badge**

Displays a badge next to reviews from customers who purchased the specific product.

1. Go to **SureCart → Settings → Reviews**.
2. Enable **Verified Buyer**.
3. Click Save.

## **Managing Reviews**

All reviews are managed from: **SureCart → Products → Reviews**

From this screen, you can: Edit, Approve, Reject, or Delete reviews.

## **Displaying Reviews on Product Pages**

To display reviews on the frontend, add review blocks to your Single Product template.

Access via: **SureCart → Products → Edit (any product) → Template → Edit Product Template**

Available review blocks:

| Block                  | Description                                    | Typical Placement     |
| ---------------------- | ---------------------------------------------- | --------------------- |
| Star Rating            | Average star rating                            | Below product title   |
| Average Rating (Value) | Numeric rating value (e.g., 4.5)               | Alongside Star Rating |
| Reviews Count          | Total number of reviews                        | Next to Star Rating   |
| Product Review Summary | Full rating overview                           | Top of review section |
| Review Breakdown       | Distribution of ratings by star level          | Beside Summary        |
| Product Review List    | Individual reviews with filters and pagination | Main review section   |

## **Notes, Limitations, and Edge Cases**

- Reviews must be enabled globally before they can be displayed.
- Disabling reviews prevents new submissions but does not delete existing reviews.
- Review request emails only trigger after an order is marked as fulfilled.
- Existing stores must manually add review blocks to product templates.

## **Related Documentation**

- [How to Create a Product Page in SureCart](https://surecart.com/docs/create-product/)
- [Product Pages Guide](https://surecart.com/docs/product-pages-guide/)


===== SOURCE: product-seo.md =====

---
source_url: https://surecart.com/docs/product-seo
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Make Your Product Visible to Search Engines for Better SEO

# How to Make Your Product Visible to Search Engines for Better SEO

Do you want people to see your products in search results when they search for similar products online? If yes, SureCart has a handy feature to help you with this!

When you create a product in SureCart, you will see a section called "Search Engine Listing," where you can write a Page Title and Meta Description for your product.

People see these bits of info when your product pops up in a search engine.

In this guide, we'll walk you through some easy steps to use this feature in SureCart on your WordPress site, and by the end, you'll know how to make your product look great in search results so more people will want to click on it!

Let's start!

- Go to your WordPress dashboard, and from SureCart, click on Products.

- Click on any product you want to add Page Title and Meta Description.

- Scroll down and look for the 'Search Engine Listing' section.

- Write a clear and catchy 'Page Title' and 'Meta Description.' This is what people will see in search results. You'll see a preview of how it looks.

- Once you're happy with the title and description, click 'Save Product.'

That's all there is to it!

With these easy steps, you can make your product shine in search results and help more people find what you're selling.

Using the "Search Engine Listing" section in SureCart, you can write catchy Page Titles and Meta Descriptions that grab people's attention and make them want to learn more about your product.

Remember, the more appealing and clear your product looks in search results, the more likely people are to click on it.

Don't hesitate to reach out to us if you have any questions! We're here to help.


===== SOURCE: product-with-free-trials.md =====

---
source_url: https://surecart.com/docs/product-with-free-trials
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How To Create a Product With Free Trials

# How To Create a Product With Free Trials

Follow these easy steps to include a free trial for your product:

1. Let's begin the process of creating a new price. To do this, simply click on the "Add Another Price" button.

2. Let's choose the installment option, but keep in mind that this process also works for subscriptions.

3. To activate the free trial, toggle the "Free Trial" switch and enter the desired number of days for the trial period. You can choose any number from 1 to 365 days. Once you're satisfied, click on the "Create Price" button.

By following these straightforward steps, you've successfully set up a free trial for your product.

To get a customer's perspective, go to the checkout page and choose the relevant pricing option.

You'll observe a message in the pricing selector indicating that the trial will begin in 15 days, and the total price will be displayed as zero.

After completing the checkout process, your customers will notice a tag in the Plans section indicating that the plan is in the Trialing phase and displaying. You will also see a message telling the date when your subscription will begin.

Great! You just created an installment plan with a trial period.

In the next section, we are going to cover the setup fee with a free trial combination.


===== SOURCE: products-with-tax-included.md =====

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


