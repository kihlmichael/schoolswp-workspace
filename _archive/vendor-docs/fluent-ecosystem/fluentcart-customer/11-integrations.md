# Section Integrations

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## FluentCart with Amazon S3 - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/amazon-s3-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/amazon-s3-integration#VPContent)

# FluentCart with Amazon S3 [​](https://docs.fluentcart.com/guide/integrations/amazon-s3-integration\#fluentcart-with-amazon-s3)

This page has moved

Amazon S3 now has its own dedicated section under the **Storage** menu in FluentCart, alongside Cloudflare R2. The setup experience has been rebuilt into a guided wizard with live bucket browsing, in-UI bucket creation, and a dedicated security step.

Head to the new guide for the current setup:

- [Amazon S3 setup guide →](https://docs.fluentcart.com/guide/storage/s3)
- [Storage Overview →](https://docs.fluentcart.com/guide/storage/)
- [Cloudflare R2 setup guide →](https://docs.fluentcart.com/guide/storage/r2)

The old location is kept here only so existing bookmarks and inbound links keep resolving.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Cloudflare Turnstile Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration#VPContent)

# Cloudflare Turnstile Integration [​](https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration\#cloudflare-turnstile-integration)

Cloudflare Turnstile is a powerful, privacy-first security solution that provides an effortless alternative to traditional CAPTCHAs. By integrating Cloudflare Turnstile with FluentCart, you can protect your **Checkout Page** from spam and malicious bots without interrupting the customer's journey.

Turnstile works invisibly in the background, ensuring your shoppers enjoy a smooth, puzzle-free checkout while your store remains protected from automated "carding" attacks and fake order submissions.

## Step 1: Enabling Turnstile in FluentCart [​](https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration\#step-1-enabling-turnstile-in-fluentcart)

Before heading to Cloudflare, you need to prepare the integration within your WordPress site.

1. Log in to your **WordPress Dashboard**.
2. Navigate to **FluentCart > Settings** in the side menu.
3. Click on the **Features & Addon** section in the left-hand sidebar.
4. Find the **Cloudflare Turnstile** card and toggle the switch to **Active**.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-1.DFO8ZHF6.webp)

Once enabled, two configuration fields will appear: **Turnstile Site Key** and **Turnstile Secret Key**. You will need to keep this tab open as you’ll be pasting your keys here in Step 3.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-2.DVCmBilj.webp)

## Step 2: Generating Your Keys in Cloudflare [​](https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration\#step-2-generating-your-keys-in-cloudflare)

To connect your store, you need to register your domain with Cloudflare. You can do this with a free [Cloudflare account](https://dash.cloudflare.com/).

1. **Access the Turnstile Dashboard:** Log in to Cloudflare, and in the sidebar, navigate to **Protect & Connect > Turnstile**.
2. **Add Your Website:** Click the **Add Widget** button.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-3.Bg8vHn3L.webp)

3. **Configure the Widget:**
   - **Widget Name:** Enter a name to identify this site (e.g., "Main Store Checkout").
   - **Hostname Management:** Click the **Add Hostnames** button. A popup will appear-enter your store’s primary domain name (e.g., `mystore.com`) and click **Add**.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-4.6VTRxw8d.webp)

4. **Select Widget Mode:**
   - **Managed (Recommended):** Cloudflare will only show an interactive checkbox if the visitor looks suspicious. Otherwise, it stays invisible.
   - **Non-interactive:** Shows a loading bar to the user while verifying.
   - **Invisible:** Stays completely hidden from the user at all times.
5. **Finalize:** Click **Create** at the bottom of the page.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-5.Ce9GKR-G.webp)

Cloudflare will now display your **Site Key** and **Secret Key**. These are unique to your domain and should be kept secure.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-6.AX8Wnlb6.webp)

## Step 3: Connecting the Keys to FluentCart [​](https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration\#step-3-connecting-the-keys-to-fluentcart)

Now, let's link the two platforms to finalize the security layer.

1. Return to your **FluentCart Settings** tab.
2. **Copy and Paste:**
   - Copy the **Site Key** from Cloudflare and paste it into the **Turnstile Site Key** field in FluentCart.
   - Copy the **Secret Key** from Cloudflare and paste it into the **Turnstile Secret Key** field.
3. **Save Changes:** Click the **Save Settings** button at the bottom right.

You should see a "Settings Saved" confirmation. Your checkout page is now officially protected by Cloudflare Turnstile.

![Cloudflare Turnstile Integration](https://docs.fluentcart.com/assets/trunstile-integration-fluentcart-7.BBtrB5vj.webp)

## How to Verify the Integration [​](https://docs.fluentcart.com/guide/integrations/cloudflare-turnstile-integration\#how-to-verify-the-integration)

Because Turnstile is designed to be invisible, you might wonder if it’s actually working. Here is how to check:

- **Dashboard Stats:** After a few traffic spikes, you can return to your Cloudflare dashboard under **Turnstile** to see analytics on how many "challenges" were issued and how many bots were blocked.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Integrating with FluentAffiliate - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration#VPContent)

# Integrating with FluentAffiliate [​](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration\#integrating-with-fluentaffiliate)

Integrating FluentCart with FluentAffiliate allows you to create and manage a powerful, full-featured affiliate program for your store. By connecting the two, you can empower marketers and partners to promote your products and automatically track their referrals, commissions, and payouts.

This guide will walk you through how to set up the integration and explain the different ways referrals can be tracked.

INFO

This integration is configured from the FluentAffiliate dashboard, which then automatically communicates with your FluentCart store.

## Enable the FluentCart Integration in FluentAffiliate [​](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration\#enable-the-fluentcart-integration-in-fluentaffiliate)

First, you need to activate the connection between the two plugins.

1. From your WordPress dashboard, navigate to **FluentAffiliate > Settings**.
2. Click on the **Integration Settings** tab.
3. You will see a list of available integrations. Find **Fluent Cart** and make sure the toggle next to it is enabled.

![Enable FluentCart integration with FluentAffiliate](https://docs.fluentcart.com/images/integrations/fluentaffiliate/enable-the-fluentcart-settings.webp)

### Configure Integration Settings [​](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration\#configure-integration-settings)

Once enabled, you can click the **Manage** button to configure the main rules for your affiliate program.

In the management panel, you can fine-tune how commissions work for your FluentCart store. Here are the available options:

- **Enable Affiliate Integration for FluentCart:** This checkbox acts as the master switch for the integration. Ensure it is checked.
- **Enable Branded Coupon Codes for Affiliates:** When you enable this feature, you can offer branded coupon codes to your affiliates. This allows them to promote products with unique discount codes, giving them another powerful marketing opportunity.

![Enable Branded Coupons](https://docs.fluentcart.com/images/integrations/fluentaffiliate/enable-branded-coupons.webp)

- **Disable Referrals on Upgrades:** Check this box to ensure that no referrals will be added on purchased upgrades. This gives you more control over commission payouts for existing customers who upgrade their plan.
- **Enable custom rate for specific products or categories:** This is a powerful feature that lets you override your default commission rate. Check this box if you want to set special commission rates for specific products or entire product categories.

NOTE

This feature gives you the flexibility to offer different commission rates for different products. For example, you could offer a higher commission on a new product as an incentive for affiliates to promote it more heavily.

- **Select Products:** In the `Select` field, start typing the name of the product or category and choose it from the list.
- **Select Rate:** Enter the commission value in the `Enter Rate` field. Then, choose whether the commission is a **Percentage (%)** or a **Fixed** amount from the dropdown menu.
- **Save Settings:** Once you have configured all your custom rates, click the **Save Settings** button to make them live.

You can add more custom rates for different products or categories by clicking the **+Add New Group** button again. You can also remove any rate rule by clicking the red delete icon.

![Enable Custom rates for Specific Products or Categories](https://docs.fluentcart.com/images/integrations/fluentaffiliate/enable-custom-rates.webp)

## How to Set Up a Coupon Referral [​](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration\#how-to-set-up-a-coupon-referral)

This branded coupon code feature gives a special discount code to a partner, like a blogger or a social media influencer, and the affiliate can know exactly how many sales they brought in. FluentCart makes this incredibly simple.

You give this coupon code directly to one of your affiliates. This way, whenever a customer uses that specific coupon, your affiliate automatically gets credit for the sale. It’s a perfect way to track your collaborations and make sure your partners are rewarded for the business they send your way, all without any extra work. To create this coupon, follow the steps below in your FluentCart.

1. In your WordPress dashboard, navigate to **FluentCart Pro > Coupons**.
2. Create a new coupon or edit an existing one.
3. On the coupon edit screen, find the **FluentAffiliate** section on the right-hand side.
4. Click on the **Select Affiliate** field and begin typing the affiliate's name. Select their affiliate from the list when it appears.
5. **Save** the coupon. Now, when this coupon is used, the selected affiliate will be credited with the referral.

NOTE

Before you can assign a coupon, the user must already be an approved affiliate in your FluentAffiliate program.

![How to Set Up a Coupon Referral](https://docs.fluentcart.com/images/integrations/fluentaffiliate/setup-coupons.webp)

## How Affiliate Referrals Are Tracked [​](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration\#how-affiliate-referrals-are-tracked)

FluentAffiliate can track referrals for your FluentCart store in three different ways, giving your affiliates maximum flexibility to promote your products.

**1\. Using a Standard Affiliate Referral Link** This is the most common method. Every affiliate who signs up gets a unique referral link (e.g., `yourstore.com/?ref=7`).

_How it works:_ When a customer clicks this link, a cookie is stored in their browser. If they make a purchase on your FluentCart store within the cookie's duration, the affiliate is automatically credited with the commission for that sale.

**2\. Using a Custom Product Link** Affiliates can also generate unique links that go directly to a specific product page on your FluentCart store.

_Why it's useful:_ This is perfect for targeted promotions. Instead of sending traffic to your homepage, an affiliate can write a review of a specific product and use a direct affiliate link to that product's page, increasing the chances of a conversion.

**3\. Using a Coupon Code** This is a powerful and popular way to track referrals without relying on links at all. You can associate a specific coupon code directly with one of your affiliates.

_How it works:_ When a customer uses that affiliate's coupon code at checkout, the affiliate is automatically credited for the sale, even if the customer never clicked a referral link. This is perfect for social media influencers, podcasters, or anyone who promotes your brand offline.

By combining these three tracking methods, you provide a robust and flexible affiliate program that empowers your partners to promote your FluentCart products in a variety of ways.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## FluentBooking Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/fluentbooking-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration#VPContent)

# FluentBooking Integration [​](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration\#fluentbooking-integration)

**FluentCart** is designed to be fast, flexible, and scalable, making it easy to manage your eCommerce business. With this integration, you can sell consultations, classes, services, or products directly from your booking forms-no third-party plugins required.

By using FluentCart’s payment processing, you can maintain a unified ecosystem for both your products and your scheduled appointments.

## Step 1: Activate the FluentCart Module [​](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration\#step-1-activate-the-fluentcart-module)

The connection between the two plugins is designed to be seamless. Once FluentCart is active on your site, you simply need to toggle the feature inside FluentBooking.

1. Navigate to **FluentBooking > Settings** from your WordPress dashboard.
2. Click on **Advanced Features & Addons** in the left side bar.
3. The system should automatically detect the **FluentCart** plugin; ensure it is enabled to allow the two tools to communicate.

![Activating the FluentCart module within FluentBooking settings](https://docs.fluentcart.com/assets/activate-the-fluentcart-module.D07BkX71.webp)

## Step 2: Link a Product to Your Calendar [​](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration\#step-2-link-a-product-to-your-calendar)

After the module is active, you can decide which specific booking events should require payment.

1. Go to the **Booking Calendars** section in FluentBooking.
2. Click **Edit** on an existing event, or create a **\+ New event**.

![Calendar Edit](https://docs.fluentcart.com/assets/calendar-edit-2.CCYBBo9J.webp)

3. Select **Payment Settings** from the left sidebar.
4. Check the box labeled **Enable this payment as Paid and collect payment on booking**.
5. In the **Payment Method** dropdown, choose **FluentCart Checkout**.
6. **Select a Product:** Choose the appropriate FluentCart product from the dropdown list.

TIP

**Pro Tip:** If you haven't created the product yet, click the **\+ New** button to create it instantly from this screen.

NOTE

If you are using the free version of FluentBooking, you can link only one product per event.

![Payment Settings](https://docs.fluentcart.com/assets/payment-settings-3.Bn0VSKok.webp)

## Step 3: Handle Multiple Durations (Optional) [​](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration\#step-3-handle-multiple-durations-optional)

If your booking event offers different time lengths (e.g., a 30-minute vs. a 60-minute session), you can assign a unique product and price to each duration. Click **Save Changes** to finalize your setup.

* * *

## The Customer Experience [​](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration\#the-customer-experience)

When your clients book an appointment, the integration handles the entire transaction:

- **Transparent Pricing:** The price of the linked FluentCart product is displayed directly on your booking form.
- **Secure Checkout:** After picking a time slot, the user is redirected to the FluentCart checkout page to pay.
- **Instant Confirmation:** Once the payment is finished, the booking is processed, and the transaction is recorded via your chosen FluentCart payment gateway.

![Customer Experience](https://docs.fluentcart.com/assets/checkout-4.CkFBxAKm.webp)

## Managing Your Data [​](https://docs.fluentcart.com/guide/integrations/fluentbooking-integration\#managing-your-data)

One of the biggest benefits of this integration is that it keeps your records centralized:

- **In FluentBooking:** View all appointment details and schedules in the **Bookings** section.

![Booking Details](https://docs.fluentcart.com/assets/booking-details-5.BtFPiM23.webp)

- **In FluentCart:** Every successful booking is recorded as an official **Order**. This ensures your revenue, customer purchase history, and tax data remain in one place.

![Order Items](https://docs.fluentcart.com/assets/order-items-6.cEL-bsmU.webp)

If you have any questions or need further assistance, feel free to reach out to our [support team](https://fluentcart.com/account/).

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## FluentCommunity Integrating - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration#VPContent)

# FluentCommunity Integrating [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#fluentcommunity-integrating)

Connecting FluentCart with FluentCommunity lets you automatically manage your customers' access to community spaces and courses. When a customer buys a product, you can instantly enroll them in a specific course or add them to an exclusive space.

This automation is perfect for online courses, membership sites, or any store looking to build a community. It saves you from manually adding new members and ensures access is granted or removed based on their purchases or subscriptions.

FluentCart gives you two ways to set this up: **Global Integrations** (for all products) and **Product-Specific Integrations** (for certain products). This guide will show you how to use both.

#### When to Use Each Integration Type [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#when-to-use-each-integration-type)

Before you begin, it's helpful to decide which type of integration best suits your goal:

- **Use a Global Integration when:** You want a general rule to apply to _every single customer_, regardless of what they buy.
  - _Example:_ Adding all paying customers to a general "Welcome" or "All Customers" space in your community.
- **Use a Product-Specific Integration when:** You want a targeted action to apply _only to customers who buy a specific product or one of its variations_.
  - _Example:_ Enrolling customers who bought your "Beginner's Yoga Course" into the corresponding "Yoga Students" space and course within FluentCommunity.

> **Important Note on Priority** If a customer purchases a product that has a specific integration rule, the **product-specific rule will always take priority** over any global rules.

### Part 1: Global Integration (For All Products) [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#part-1-global-integration-for-all-products)

A global integration is perfect for broad actions that should apply to all your paying customers.

#### Navigating to Integrations [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#navigating-to-integrations)

First, you'll need to go to the correct screen in your WordPress dashboard.

1. Navigate to **FluentCart Pro**.
2. Click on **Integrations** from the sidebar menu.

#### Creating a New FluentCommunity Feed [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#creating-a-new-fluentcommunity-feed)

1. On the **Integrations & Addons** dashboard, click the **Add Integration** button at the top right.
2. Select **FluentCommunity** from the dropdown menu. This will take you to the configuration screen for your new automation feed.

![Global Integration FluentCommunity](https://docs.fluentcart.com/assets/integrateing-fluentcommunity-1.CW-FWDFx.webp)

### Part 2: Product-Specific Integration [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#part-2-product-specific-integration)

A product-specific integration is ideal for highly targeted automations, like granting access to a course that corresponds directly to the product purchased.

#### Navigating to the Product [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#navigating-to-the-product)

1. From your WordPress dashboard, navigate to **FluentCart Pro > Products**.
2. Click on the product for which you want to create a specific integration to open its editor.

#### Accessing Product Integrations [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#accessing-product-integrations)

1. Inside the product editor, you will see a series of tabs at the top. Click on the **Integrations** tab.
2. On the Product Integrations screen, click the **Add Integration** button and select **FluentCommunity Feed**. This will open the feed configuration screen.

![Product Specific Integration FluentCommunity](https://docs.fluentcart.com/assets/integrateing-fluentcommunity-2.B6eGXsT4.webp)

### Part 3: Configuring the Integration Feed [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#part-3-configuring-the-integration-feed)

Whether you are creating a global or a product-specific feed, the configuration screen is nearly identical. This is where you define exactly what actions FluentCommunity will perform when a purchase is made.

- **Feed Title:** Give your feed a descriptive name for your own internal reference (e.g., "Enroll in Beginner's Course" or "Add All Customers to Welcome Space").

- **Add to Spaces:** Select one or more FluentCommunity Spaces you would like to automatically add the customer to upon purchase.

- **Add to Courses:** Select one or more FluentCommunity Courses you would like to automatically enroll the customer in.

- **Remove from Spaces:** (Optional) Select any Spaces you would like to automatically remove the customer from. This is useful if a new purchase moves them to a more advanced group.

- **Remove from Courses:** (Optional) Select any Courses you would like to automatically unenroll the customer from.

- **Mark the community profile as verified:** Enable this option to automatically grant the customer a "verified" status within FluentCommunity, which can be used to signify them as a paying member.

- **Remove from selected Courses/Spaces on Refund or Subscription Access Expiration:** This is a crucial automation feature. If enabled, FluentCart will automatically revoke the user's access to the selected spaces and courses if their order is refunded or their subscription expires.

- **Event Trigger:** Select the specific store event that will trigger this automation. The available Event Triggers are:

  - Order Paid (Payment / Subscription)
  - Order Canceled
  - Order Refunded (Full)
  - Subscription Activated
  - Subscription Canceled
  - Subscription Renewed
  - Subscription End of Term (Completed)
  - Subscription Expired / End of Access Validity
  - Shipping
  - Order Shipped
  - Order Delivered
- **Run on Selected Variations Only (Product-Specific Only):** This powerful option appears only on product-specific integrations. It allows you to run the automation only when a customer purchases a specific variation of the product (e.g., a "Lifetime Access" tier). Leave this empty to have the feed run for all variations of this product.

- **Enable this Integration:** Ensure the toggle at the top right is switched on to make the automation active. If it is disabled, the feed will be saved but will not run.


![Configure Integration Feed Fluentcommunity](https://docs.fluentcart.com/assets/integrateing-fluentcommunity-3.DU5qeKQR.webp)

Once everything is configured, click the **Create FluentCommunity Feed** button. Your automation is now live!

### Use Case Example: A Clothing Store [​](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration\#use-case-example-a-clothing-store)

Imagine you run a clothing store selling two hoodie variations: _Classic Hoodie_ and _Premium Hoodie._

**Your Goal:**

- Add all customers to a general "Hoodie Lovers" space.
- Add customers who buy the _Classic Hoodie_ into the "Classic Hoodie Owners" space.
- Add customers who buy the _Premium Hoodie_ into the "Premium Hoodie Owners" space.

**The Solution:**

- **Global Integration**: Create one Global Feed that adds every customer to the "Hoodie Lovers" space when their order is paid.
- **Product-Specific Integrations**:
  - Inside the _Classic Hoodie_ product, create a Product-Specific Feed to add customers to the _Classic Hoodie Owners_ space.
  - Inside the _Premium Hoodie_ product, create another Product-Specific Feed to add customers to the _Premium Hoodie Owners_ space.

**The Result:**

When a customer buys the _Classic Hoodie_, both automations run. The global feed adds them to the _Hoodie Lovers_ space, and the product feed adds them to _Classic Hoodie Owners_, creating a smooth, automated onboarding experience.

---

## FluentCRM Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/fluentcrm-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration#VPContent)

# FluentCRM Integration [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#fluentcrm-integration)

Connecting FluentCart with FluentCRM allows you to create powerful marketing automations based on your customers' actions. When someone makes a purchase, you can automatically add them to specific lists, apply tags, and update their profiles in FluentCRM without lifting a finger.

This guide will walk you through setting up a Global Integration Feed, which runs for every order placed in your store.

FluentCart offers two powerful ways to connect with FluentCRM:

- **Global Integrations:** These rules apply to every single purchase in your store. They are ideal for general tasks, like adding all new customers to your main newsletter.
- [**Product Integrations**](https://docs.fluentcart.com/guide/product-types-creation/managing-product-integrations): These rules are more specific and are triggered only when a customer buys a particular item. This is perfect for targeted actions, like adding a customer to a special list after they buy a specific course or e-book.

This guide will focus on setting up a **Global Integration**.

### When to Use Each Integration Type [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#when-to-use-each-integration-type)

Before you begin, it's helpful to decide which type of integration best suits your goal:

- **Use a Global Integration when:** You want an action to apply to _every single customer_, regardless of what they buy.
  - _Example:_ Adding all paying customers to your main "Newsletter" list.
- **Use a Product Integration when:** You want an action to apply _only to customers who buy a specific item_. To learn more about setting up these powerful, product-specific automations, please follow our detailed [documentation](https://docs.fluentcart.com/guide/product-types-creation/managing-product-integrations).
  - _Example:_ Adding customers who bought your "Advanced SEO Course" to a "Course Students" list and tagging them accordingly.

### Enabling the FluentCRM Module [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#enabling-the-fluentcrm-module)

First, you need to make sure the FluentCRM integration module is active.

1. From your WordPress dashboard, navigate to **FluentCart Pro → Integrations**.
2. Scroll down to the **Integration Modules** section.
3. Find **FluentCRM** in the list and make sure it is enabled. If it's disabled, you may need to install or activate it first.

### Setting Up a Global Integration Feed [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#setting-up-a-global-integration-feed)

A global feed is perfect for tasks that should apply to all your customers, like adding every new buyer to your main newsletter.

#### Create a New FluentCRM Feed [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#create-a-new-fluentcrm-feed)

- Click the **Add Integration** button in the top-right corner.
- Select **FluentCRM** from the dropdown menu. This will open a new screen where you can set up the automation rules.

![Screenshot of Fluentcrm Integration Page](https://docs.fluentcart.com/images/integrations/fluentcrm/add-integration.webp)

#### Configure Your Feed [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#configure-your-feed)

Here, you'll decide exactly what happens in FluentCRM when the feed is triggered.

- **Feed Title:** Give your feed a descriptive name that you'll recognize later, like "Add All Customers to Newsletter.

- **Add to Lists:** Use this field to select the FluentCRM lists you want to add to a customer’s profile when this feed runs from the dropdown.

- **Add to Tags:** Select the FluentCRM tag(s) you want to apply to all new customers. This is a great way to segment all your buyers for future marketing campaigns.

- **Remove From Lists / Remove From Tags:** If needed, you can also select lists and tags to remove from a customer's profile.

- **Note:** You can add a note that will be attached to the contact's profile in FluentCRM. This is great for internal records. You can even make the note dynamic by using shortcodes (click the {(...)} icon) to include customer or order data.

- **Enable Double Opt-in:** It is highly recommended to keep this enabled. It sends a confirmation email to new contacts before they are subscribed, which is a best practice for maintaining a healthy and engaged email list.

- **Event Trigger:** Select the specific store event that will trigger this automation. For most use cases, "Order Completed / Paid" is the best option, as it ensures only paying customers are added to your CRM.

- **Remove from selected Tags/Lists on Refund or Subscription Access Expiration:** This is a handy automation. If you check this box, FluentCart will automatically remove the customer from the lists and tags you selected if their order is refunded or their subscription ends.

- **Run on Selected Variations Only:** This setting allows this integration rule to run only when a customer buys a **specific product variation**. Select one or more variations from the dropdown to apply this rule exclusively to them. If you leave this field empty, the rule will apply to all variations of this product.

- **Enable This Integration:** Ensure the toggle at the top right is switched on to make the automation active. If it is disabled, the integration will be saved but will not run.


![Screenshot of Fluentcrm Integration Feed Page](https://docs.fluentcart.com/images/integrations/fluentcrm/fluentcrm-integration-feed.webp)

Once configured, click the **Create FluentCRM Feed** button. This global automation is now live and will run for every order in your store.

Once everything is set up, you can manage the integration by clicking the **Edit** icon to make changes or the **Delete** icon to remove it.

![Screenshot of Fluentcrm Integration Feed Page](https://docs.fluentcart.com/images/integrations/fluentcrm/fluentcrm-integration-edit-or-delete.webp)

### Combining Global and Product Integrations [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#combining-global-and-product-integrations)

By combining both Global and Product-specific integrations, you can create a sophisticated marketing automation strategy. Use global feeds for general onboarding and product feeds for highly targeted, post-purchase follow-ups that enhance the customer experience.

### Advanced Marketing Automation with FluentCRM Triggers [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#advanced-marketing-automation-with-fluentcrm-triggers)

Beyond simply adding tags and lists, the FluentCart integration adds a powerful set of e-commerce triggers directly inside FluentCRM's automation builder. This allows you to create automated marketing funnels based on real-time events in your store. When you create a new automation in FluentCRM, you will find a new FluentCart trigger category. Here are the available triggers and what they do:

When you create a new automation in FluentCRM, you will find a new **FluentCart** trigger category.

Here are the available triggers and what they do:

- **Order Paid (Payment/Subscription):** Starts an automation when a new order is successfully paid. Perfect for sending a "Thank You" email or starting an onboarding sequence.
- **Order Shipped:** Triggers when a physical order's status is changed to "Shipped." Use this to send shipping confirmation emails with tracking information.
- **Order Delivered:** Triggers when an order's status is changed to "Delivered." A great opportunity to ask for a product review.
- **Order Refunded (Full):** Starts when a full refund is processed. You could use this to send a survey asking for feedback on why the customer requested a refund.
- **Order Canceled:** Triggers when an order is canceled.
- **Subscription Triggers:** A full suite of triggers for managing communication with your subscribers, including **Subscription Activated, Subscription Canceled, Subscription Renewed, and Subscription Expired**. These are essential for reducing churn and keeping subscribers engaged.

INFO

These triggers are the starting point for powerful marketing funnels. For detailed, step-by-step guides on how to use these triggers to build onboarding sequences, cart abandonment funnels, and other advanced marketing automations, please see this [documentation](https://fluentcrm.com/docs/fluentcart-integration-with-fluentcrm/).

![Screenshot of Fluentcrm Automation Trigger](https://docs.fluentcart.com/images/integrations/fluentcrm/automation-trigger.webp)

### Use Case Example: Segmenting Customers by Location [​](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration\#use-case-example-segmenting-customers-by-location)

To better understand how this integration works in practice, let's imagine you run an online store that sells physical goods, like custom-printed t-shirts. Your goal is to identify all customers from a specific city (e.g., London) so you can send them a targeted email about a local pop-up shop you are hosting.

Here is how you would configure the FluentCRM feed to achieve this:

- **Name:**`London Customer Segmentation`
- **List:**`Main Customer List`
- **Tags (Dynamic Tag Inputs):**
  - **Tag:**`london-customer`
  - **Condition:** IF `{order.billing.city}` _equals_`London`.
- **Event Trigger:**`Order Completed`
- **Status:**`Enable This feed`

**Result:**

With this configuration, every time an order with a London billing address is marked as "Completed" in FluentCart, the customer's information will be sent to FluentCRM. They will be added to your "Main Customer List" and will automatically be tagged as `london-customer`.

Inside FluentCRM, you can then create a new email campaign and, in the recipient settings, choose to send it _only_ to contacts who have the `london-customer` tag. This ensures your promotional email about the London pop-up shop is sent exclusively to the relevant local audience.

---

## Fluent Support Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/fluentsupport-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration#VPContent)

# Fluent Support Integration [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#fluent-support-integration)

Connecting FluentCart with Fluent Support links your e-commerce store to your helpdesk system. This integration provides crucial purchase information directly to your support agents and creates a unified experience for your customers, making your support process faster and more efficient.

This guide will walk you through setting up the integration and explain how to use its key features step-by-step.

### Step 1: Enabling the Integration in FluentCart [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#step-1-enabling-the-integration-in-fluentcart)

First, ensure both FluentCart and Fluent Support are installed and active on your WordPress site. The core connection happens automatically. To confirm it's active:

1. From your WordPress dashboard, navigate to **FluentCart Pro > Integrations**.
2. Scroll down to the **Integration Modules** section.
3. Locate the **Fluent Support** module.
4. You should see a green **Enabled** status badge. This means FluentCart recognizes Fluent Support, and the basic connection is active. No further action is needed here.

![Screenshot of Fluent Support Integration](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/enabling-the-integration.webp)

### Step 2: Creating Custom Fields in Fluent Support [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#step-2-creating-custom-fields-in-fluent-support)

To get the most out of the integration, you can create special "Custom Fields" in Fluent Support. These fields allow you (or your customers) to link a support ticket directly to a specific FluentCart Product or Order. Also, you can create Workflows in Fluent Support with these custom fields.

1. From your WordPress dashboard, navigate to **Fluent Support > Custom Fields**.
2. Click the **\+ Add New Field** button at the top right.
3. A pop-up window will appear. Configure the field:
   - **Field Type:** This is the most important setting. Choose either **FluentCart Products** or **FluentCart Orders** from the dropdown list.
   - **Public Label:** Enter the name that customers will see (e.g., "Related Product" or "Order Number").
   - **Admin Label (Optional):** Enter a different name that only your support agents will see internally.
   - **Slug (Optional):** A unique internal identifier (usually generated automatically).
   - **Placeholder (Optional):** Text that appears in the field before the user selects something.
   - **This is an agent only field:** Check this if you want the field to be visible only to your support agents inside the ticket, not on the public submission form.
   - **Required:** Check this if you want to force customers to select a product/order when submitting a ticket.
   - **Enable Conditional Logics (Optional):** Set up rules to show or hide this field based on other selections in the form.
4. Click the **Add** button to save your new custom field.

You can repeat this process to create separate fields for both Products and Orders if needed.

![Screenshot of Creating Custom Fields](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/creating-custom-field.gif)

### Step 3: Using Workflows [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#step-3-using-workflows)

Now that you have created FluentCart custom fields, you can use them to automate tasks in Fluent Support using **Automatic Workflows**. This allows you to automatically route tickets or apply tags based on the product a customer selects.

1. Navigate to **Fluent Support > Workflows**.
2. Click on the **\+ Add New Workflow** button.
3. Give your workflow a name (e.g., "Assign Product X Tickets") and choose **Automatic** as the **Workflow Type**. Click **Continue**.

![Screenshot of Fluent Support Workflows](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/add-new-workflow.webp)

4. **Set Trigger & Conditions:**
   - Set the **Workflow Trigger** from the dropdown field, like **On Ticket Creation**.
   - Under **Conditions**, click **\+ Add Condition**.
   - Select your custom field you have created for FluentCart products or orders, choose the rule (like **Equal**), and select the specific FluentCart product or order you want this rule to apply to.
5. **Set Workflow Actions (Tasks):** Choose what should happen automatically when a ticket matches your conditions from the **Action** dropdown field. For example, select **Assign Agent** and choose the team or agent who specializes in that product.
6. Set the workflow **Status** to **Published** and click **Update Workflow**.

![Screenshot of Update Workflows](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/update-workflow.webp)

Now, whenever a customer submits a ticket and selects that specific product, the workflow will run automatically!

### Step 4: Add Support Portal to the FluentCart User Dashboard [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#step-4-add-support-portal-to-the-fluentcart-user-dashboard)

Provide a great experience by adding a dedicated support section directly into the FluentCart customer account area.

1. Navigate to **Fluent Support > Global Settings**.
2. Scroll down to the bottom of the page.
3. Check the box labeled **Add support link to Fluent Cart account navigation**.
4. Click **Save Settings**.

The Result: A new **Support** tab will now appear in the FluentCart customer dashboard (`/account/Support`). Customers can click this tab to view their existing support tickets and submit new ones without leaving your store's account area.

![Screenshot of Global Settings](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/add-support-link-in-cart.webp)

### Step 5: Linking Tickets to Products/Orders (Customer Experience) [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#step-5-linking-tickets-to-products-orders-customer-experience)

With the custom fields added to your ticket form (Step 2), customers can easily link their support requests to their purchases when submitting a ticket through the portal.

1. When a customer navigates to the "Support" tab in their FluentCart dashboard and clicks **\+ Create Ticket** (or uses your main support page).
2. They will be able to see the custom fields you added (e.g., "Product/Order").
3. The dropdown menu for this field will show the products from your FluentCart store.
4. The customer selects the relevant product or order from the dropdown list.
5. They fill out the rest of the ticket details and click **Create Ticket**.

![Screenshot of Submit a Support Ticket](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/submit-a-support-ticket.webp)

This ensures that when the ticket arrives in your helpdesk, it's already linked to the specific purchase the customer needs help with, providing instant context for your agents.

### Step 6: Viewing Purchase History in Tickets (Widget) [​](https://docs.fluentcart.com/guide/integrations/fluentsupport-integration\#step-6-viewing-purchase-history-in-tickets-widget)

This feature requires no extra setup and works automatically thanks to the integration. It provides invaluable context for your support agents.

1. When a support agent opens any ticket in **Fluent Support > Tickets**.
2. Look at the right-hand sidebar. A **Purchases** widget will automatically appear if the customer who submitted the ticket has any purchase history in your FluentCart store.
3. **What it shows:**This widget displays key information:
   - Customer's **Lifetime Value**.
   - A list of their recent FluentCart purchases, including product names, prices, order statuses, and direct links (#) to the orders in FluentCart.
   - Subscription details (if applicable).
   - License keys (if applicable).
4. **Benefit:** Your agents get immediate access to the customer's purchase history without needing to ask or switch screens. This allows them to understand the context quickly and provide faster, more accurate support.

![Screenshot of Purchases History](https://docs.fluentcart.com/images/integrations/fluentsupport-integration/purchases-widget.webp)

By following these steps and understanding these features, you can fully leverage the FluentCart-Fluent Support integration to create a highly efficient support system and a seamless experience for your customers.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Integrations & Addons - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/integration-overview

[Skip to content](https://docs.fluentcart.com/guide/integrations/integration-overview#VPContent)

# Integrations & Addons [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#integrations-addons)

The **Integrations & Addons** screen is your central hub for connecting FluentCart with other powerful plugins and services. By activating these modules, you can automate your marketing, improve email deliverability, enhance customer support, and extend the functionality of your e-commerce store.

This guide will walk you through the two main sections of this page: **Global Integrations Feeds** and **Integration Modules**.

## Accessing the Integrations & Addons [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#accessing-the-integrations-addons)

1. From your WordPress dashboard, navigate to **FluentCart Pro**.
2. In the left-hand menu, click on **Integrations**.

### Global Integrations Feeds [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#global-integrations-feeds)

This section, located at the top of the page, is where you create powerful, store-wide automation rules. A "feed" is a rule that is triggered by an event in your store (like a new order) and performs an action in another integrated service (like adding a customer to a list in FluentCRM).

INFO

These integration rules apply globally to all your orders. For more targeted rules, you can also set up integrations on a [per-product basis](https://docs.fluentcart.com/guide/product-types-creation/managing-product-integrations).

![Integration Overview](https://docs.fluentcart.com/assets/integration-overview.Cs2w-HNL.png)

### Integration Modules [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#integration-modules)

This section, located at the bottom of the page, is where you manage the connections between FluentCart and other plugins. Before you can use an integration, you must first enable its module here.

#### Activating an Integration Module [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#activating-an-integration-module)

The activation process is largely automatic.

- **If the required plugin is already installed and active:** FluentCart will automatically detect it, and you will see a green **Enabled** status badge. The integration is ready to be used.
- **If the required plugin is not installed:** You will see a button like **Install FluentCommunity**. Clicking this will help you install and activate the necessary plugin. Once the plugin is active, the integration will automatically be enabled on this screen.

To help you find what you need, you can also use the filter tabs ( **ALL, CRM, LMS, CORE, MARKETING**) or the search bar to find a specific module.

![Available Integration Modules](https://docs.fluentcart.com/assets/integration-overview-1.E3Nrmpox.png)

### Available Integration Modules [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#available-integration-modules)

- [**Webhook:**](https://docs.fluentcart.com/guide/integrations/webhook-integration) For developers and advanced users, **Webhooks** allow you to send real-time data from your FluentCart store (like a new order) to any external service that can accept webhook notifications.
- [**FluentCRM:**](https://docs.fluentcart.com/guide/integrations/fluentcrm-integration) Automate your email marketing. This powerful integration allows you to add customers to lists, apply tags based on what they buy, and trigger targeted follow-up email sequences after a purchase.
- **FluentSMTP:** Ensure your store's emails get delivered. This module allows you to send all of FluentCart's transactional emails through a professional SMTP provider, improving deliverability. You don’t need any extra configuration to connect with FluentSMTP. Simply install FluentSMTP, and it will automatically integrate with your FluentCart.
- [**FluentCommunity:**](https://docs.fluentcart.com/guide/integrations/fluentcommunity-integration) Create a seamless membership experience. This integration lets you automatically grant or revoke access to private courses and community spaces based on a customer's purchase or subscription status.
- **FluentAuth:** Enhance your store's security and user experience. This integration allows you to customize the default WordPress login and registration pages, and add social login options for your customers. No extra settings are needed in FluentCart; simply install and configure the FluentAuth plugin, and it works automatically with your store.
- **FluentForm:** Create advanced forms and surveys with an easy-to-use drag & drop form builder.
- **FluentSupport:** Streamline your customer service. This integration connects your e-commerce data with your helpdesk, allowing your support agents to view a customer's purchase history directly from their support tickets in FluentSupport.

#### Other Key Integrations [​](https://docs.fluentcart.com/guide/integrations/integration-overview\#other-key-integrations)

Some integrations are configured in their own dedicated areas of the settings.

- [**Amazon S3:**](https://docs.fluentcart.com/guide/integrations/amazon-s3-integration) Securely host and deliver your digital products using Amazon S3. This integration provides faster, more reliable downloads for your customers and reduces the server load on your own website, which is essential for stores selling large files. For secure digital file hosting configure at `FluentCart Pro > Settings > Storage Settings`.
- [**FluentAffiliate:**](https://docs.fluentcart.com/guide/integrations/fluentaffiliate-integration) Launch and manage a powerful affiliate program for your store. This integration allows partners and marketers to promote your products and automatically tracks their referrals, commissions, and payouts. For your affiliate program configure at `FluentAffiliate > Settings > Integration Settings`.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## LearnDash Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/learndash-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/learndash-integration#VPContent)

# LearnDash Integration [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#learndash-integration)

Connecting FluentCart with LearnDash allows you to sell access to your online courses and automatically manage student enrollment. When an event happens in your FluentCart store (like a successful purchase), this integration can instantly enroll customers into the correct LearnDash courses or groups, providing a smooth and automated experience.

This guide will show you how to activate the integration and configure enrollment rules using Integration Feeds.

## Activating the LearnDash Integration [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#activating-the-learndash-integration)

First, ensure you have both **FluentCart** and **LearnDash** installed and active on your WordPress site. The basic connection is automatic.

## Configuring Enrollment Rules (Integration Feeds) [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#configuring-enrollment-rules-integration-feeds)

The core of the integration lies in creating **Integration Feeds**. Think of a "feed" as a specific instruction or rule that tells FluentCart: _"When this happens, enroll the customer in that LearnDash course or group."_

You can create these feeds in two places:

- **Globally:** These feeds apply based on events happening anywhere in your store. Useful for broad actions, like adding every new subscriber to a general student group.
- **Product Specific:** These feeds apply only for a specific product. This is the most common and recommended method for selling individual courses.

### How to Create an Enrollment Rule (Feed) [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#how-to-create-an-enrollment-rule-feed)

You have two ways to create these enrollment rules, depending on whether you want the rule to apply broadly or only to a specific product. Both methods use the same configuration settings.

#### Method 1: Creating a Global Feed [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#method-1-creating-a-global-feed)

Use this method if you want a rule to apply based on events happening anywhere in your store (e.g., enrolling every new subscriber into a general student group).

1. From your WordPress dashboard, go to **FluentCart Pro > Integrations**.
2. Find the **Global Integrations Feeds** section at the top of the page.
3. Click the **Add Integration** button located in the top-right corner of this section.
4. A dropdown menu will appear. Choose **LearnDash** from the list.
5. You will now be taken to the feed configuration screen where you can define the specifics of your global rule (explained in the below section).

![Global Integration](https://docs.fluentcart.com/assets/global-integration-1.BYcbtlNt.png)

#### Method 2: Creating a Product-Specific Feed (Recommended for Selling Courses) [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#method-2-creating-a-product-specific-feed-recommended-for-selling-courses)

Use this method to link a specific FluentCart product directly to the LearnDash course(s) it grants access to. This is the most common way to sell individual courses.

1. From your WordPress dashboard, go to **FluentCart Pro > Products**.
2. Find the product you want to link to LearnDash (e.g., your "Learn Python Course") and click on its name or the "Edit" link to open the product editor.
3. Inside the product editor, look for the row of tabs near the top (Edit Product, Upgrade Paths, etc.) and click on **Integrations**.
4. Within the product's Integrations area, click the **Add Integration** button.
5. A dropdown menu will appear. Choose **LearnDash** from the list.
6. You will now be taken to the feed configuration screen, specifically for this product, where you can define the enrollment rule (explained in the next section).

![Product Integration](https://docs.fluentcart.com/assets/product-integration-2.BEJXKaES.png)

### Configuring the Feed Settings [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#configuring-the-feed-settings)

Once you add a feed (either globally or per-product), you will see the configuration screen.

Here’s what each setting does:

- **Feed Title:** Give your rule a clear name that you'll easily recognize later (e.g., "Enroll in Learn Python Course" or "Add Subscribers to Student Group").
- **Add to Courses:** Use the dropdown menu to select the LearnDash courses you want to enroll the user in when this rule runs.
- **Add to LearnDash Groups:** Similarly, select any LearnDash group(s) you want to add the user to.
- **Remove from selected Courses/Groups on Refund or Subscription Access Expiration:** This is a vital setting for managing access automatically. Check this box if you want FluentCart to automatically remove the user from the selected courses/groups if their related order is refunded, or if their subscription expires or is canceled.
- **Set Course Expiration from Subscription / License Expiry:** Enable this option to automatically expire the customer's LearnDash course access on the same date as their **subscription expiration** or **license expiration**. When the underlying commercial relationship ends - the subscription lapses or the license reaches its expiry date - LearnDash receives the same expiry date for the enrolled course(s), so the customer loses access at exactly the right moment. This keeps course access aligned with billing instead of letting the two systems drift apart.
  - Use this for **membership-style course bundles** where access is tied to an ongoing subscription.
  - Use this for **time-limited licensed courses** where each license carries its own expiry (e.g., a one-year course license).
  - If both a subscription and a license are connected to the order, FluentCart will use whichever expiry is earliest, so the customer never keeps access past either deadline.
- **Event Trigger:** Select the FluentCart action from the dropdown that runs this rule. For course access after purchase, you can use `Order Paid (Payment / Subscription)`. Other order and subscription triggers are available for different needs.
- **Run on Selected Variations Only (Available for Product-Specific Feeds Only):** If the product has different variations (e.g., "Basic Access," "Premium Access"), you can use this dropdown to make the rule run only when a specific variation is purchased. Leave empty to apply to all variations.
- **Enable this Integration:** Make sure this toggle at the top right is switched **ON** (blue) to make the rule active.

Click **Create LearnDash Feed** (or similar button) to save your rule.

![Global Integration Feed](https://docs.fluentcart.com/assets/integration-feed-3.CbjKwNql.png)

### Use Case Example: Selling a Course Bundle [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#use-case-example-selling-a-course-bundle)

Let's illustrate how product-specific feeds make selling multiple courses easy. Imagine you offer two LearnDash courses, sold via three FluentCart products:

- **FluentCart Product 1:** "Beginner Photography Course"
- **FluentCart Product 2:** "Advanced Editing Masterclass"
- **FluentCart Product 3:** "Photography Bundle" (includes access to both courses)

Here’s how you would set up the feeds:

1. **Inside "Beginner Photography Course" Product:** Add a LearnDash feed. In "Add to Courses," select only the "Beginner Photography" LearnDash course. Set Trigger to **Order Paid**.
2. **Inside "Photography Bundle" Product:** Add a LearnDash feed. In "Add to Courses," select both the "Beginner Photography" AND the "Advanced Editing" LearnDash courses. Set Trigger to **Order Paid**.

With these simple, product-specific rules, FluentCart automatically handles the correct enrollment for every purchase, ensuring your students get exactly what they paid for instantly.

### Use Case Example: Time-Limited Membership Course [​](https://docs.fluentcart.com/guide/integrations/learndash-integration\#use-case-example-time-limited-membership-course)

If you sell course access as a yearly subscription or a time-limited license, you can use **Set Course Expiration from Subscription / License Expiry** to keep LearnDash and FluentCart perfectly in sync:

1. Create a subscription product (e.g., "Annual Photography Membership") in FluentCart.
2. On the product, add a LearnDash feed and select the courses included in the membership.
3. Enable **Set Course Expiration from Subscription / License Expiry** in the feed.
4. Set Trigger to **Order Paid (Payment / Subscription)**.

When a customer subscribes, LearnDash gives them access until the subscription's next expiry date. If they renew, the course expiry rolls forward automatically. If they cancel or fail to renew, course access ends on the same day as their subscription - no manual cleanup required, and no risk of a customer losing access early or keeping it for free.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## LifterLMS Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/lifterlms-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/lifterlms-integration#VPContent)

# LifterLMS Integration [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#lifterlms-integration)

Connecting FluentCart with LifterLMS allows you to sell access to your online courses and memberships, and automatically manage student enrollment. When an event happens in your FluentCart store (like a successful purchase), this integration can instantly enroll customers into the correct LifterLMS courses or memberships, providing a smooth and automated experience.

How To Sell an Online Course with FluentCart - YouTube

[How To Sell an Online Course with FluentCart](https://www.youtube.com/watch?v=zd8ogjvdSO4) [LifterLMS](https://www.youtube.com/channel/UC5cNcNLwaALpCRUYCo6qALg)

LifterLMS5.65K subscribers

[Watch on](https://www.youtube.com/watch?v=zd8ogjvdSO4)

This guide will show you how to activate the integration and configure enrollment rules using Integration Feeds.

### Activating the LifterLMS Integration [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#activating-the-lifterlms-integration)

First, ensure you have both FluentCart and LifterLMS installed and active on your WordPress site.

## Configuring Enrollment Rules (Integration Feeds) [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#configuring-enrollment-rules-integration-feeds)

The center of this integration is setting up **Integration Feeds**. An integration feed is just a simple instruction or a rule. It tells FluentCart: "When _this specific event_ happens, _then do this specific action_ (like enroll a customer into a course or membership)."

You can create these feeds in two different locations:

- **Globally:** These are rules that apply to your _entire_ store. They are useful for broad, general actions. For example, you could make a global rule to remove any user from a membership if their subscription is canceled, no matter what product they bought.
- **Product Specific:** This rule applies _only_ to one specific product. This is the most common and recommended way to sell your courses. For example, "When a customer buys the 'Content Writing Course' product, enroll them in the 'Writing 101' LifterLMS course."

* * *

## Setting Up Your LifterLMS Integration Feeds [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#setting-up-your-lifterlms-integration-feeds)

You have two ways to create these enrollment rules, depending on whether you want the rule to apply broadly or only to a specific product. Both methods use the same configuration settings.

#### Method 1: Creating a Global Feed [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#method-1-creating-a-global-feed)

Choose this option to create a "catch-all" rule that runs for _any_ order or subscription in your store. This is perfect for broad actions, like a site-wide rule that revokes access from a membership if _any_ subscription expires.

1. From your WordPress dashboard, go to **FluentCart Pro > Integrations**.
2. Look for the **Global Integrations Feeds** section at the top of the page.
3. Click the **Add Integration** button on the right side of that section.
4. A dropdown menu will open. Select **LifterLMS**.
5. This will take you to a new screen to set up your global rule (which we cover in the next section).

![Screenshot of LifterLMS Integration](https://docs.fluentcart.com/images/integrations/lifterlms-integration/enabling-liftelms.webp)

#### Method 2: Creating a Product-Specific Feed (Recommended) [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#method-2-creating-a-product-specific-feed-recommended)

This is the most common and recommended method. Choose this option to create a specific rule that runs _only_ when this one product is purchased. This is perfect for directly linking a product, like "Beginner Writing Course," to its matching "Writing 101" LifterLMS course.

1. **Go to your products list:** In your WordPress dashboard, navigate to **FluentCart Pro > Products**.
2. **Open your product:** Find the product you want to sell (e.g., "Content Writing Course") and click its name to go into the product editor.
3. **Find the Integrations tab:** At the top of the product editor, click the **Integrations** tab.
4. **Add a new integration:** In the **Product Integrations** area, click the **Add Integration** button.
5. **Select LifterLMS:** A dropdown will appear. Find and click on **LifterLMS**.
6. This will take you to the feed configuration screen just for this product, where you can set up your specific enrollment rule (covered in the next section).

![Screenshot of LifterLMS Integration Feed](https://docs.fluentcart.com/images/integrations/lifterlms-integration/lifterlms-integration-feed.webp)

* * *

### Configuring the Feed Settings [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#configuring-the-feed-settings)

Whether you're making a global or product-specific feed, you'll land on the configuration screen. This is where you tell FluentCart _exactly_ what to do.

Here’s a simple breakdown of each setting:

- **Feed Title:** This is just for you. Give your feed a name you'll remember, like `Enroll in Content Writing Course` or `Global Refund Rule`.
- **Add to Courses:** Click in this box to select one or more LifterLMS courses. When this rule runs, the customer will be enrolled in the course(s) you pick here.
- **Add to Memberships:** This works just like the 'Add to Courses' setting. Click here to select one or more LifterLMS memberships to add the customer to.
- **Remove from selected Courses/Memberships on Refund or Subscription Access Expiration:** This is a very important setting for protecting your content. Check this box if you want FluentCart to automatically _unenroll_ the customer from the courses or memberships you selected above. This will happen if their order is refunded or their subscription expires or is canceled.
- **Event Trigger:**Choose the specific action in FluentCart that should make this rule run. This is the "when" part of your automation. A full list of triggers includes:
  - **Orders**
    - `Order Paid (Payment / Subscription)`: **This is the most common trigger for selling courses.** It runs as soon as a customer's payment is successful.
    - `Order Canceled`: Runs if an order is canceled.
    - `Order Refunded (Full)`: Runs if an order is fully refunded. This is useful for global rules that revoke access.
  - **Subscriptions**
    - `Subscription Activated`: Runs when a subscription's status becomes active.
    - `Subscription Canceled`: Runs if a subscription is canceled (either by the admin or the user).
    - `Subscription Renewed`: Runs successfully on each subscription renewal payment.
    - `Subscription End of Term (Completed)`: Runs when a subscription with a fixed number of payments (e.g., 3 installments) is completed.
    - `Subscription Expired / End of Access Validity`: Runs when a subscription expires, and access should end.
  - **Shipping**
    - `Order Shipped`: Runs when an order's shipping status is marked as "Shipped."
    - `Order Delivered`: Runs when an order's shipping status is marked as "Delivered."
- **Run on Selected Variations Only** (Available for Product-Specific Feeds Only): If the product has different variations (e.g., "Basic Access," "Premium Access"), you can use this dropdown to make the rule run only when a specific variation is purchased. Leave empty to apply to all variations.
- **Enable this Integration:** Make sure this toggle at the top right is switched **ON** (blue) to make the rule active.

Click the **Create LifterLMS Feed** button to save your rule.

![Screenshot of Create LifterLMS Feed](https://docs.fluentcart.com/images/integrations/lifterlms-integration/specific-product-integration.webp)

### Use Case Example: Selling a Course Bundle [​](https://docs.fluentcart.com/guide/integrations/lifterlms-integration\#use-case-example-selling-a-course-bundle)

Let's illustrate how product-specific feeds make selling multiple courses simple. Imagine you offer two LifterLMS courses, but you sell them using three different FluentCart products:

- **FluentCart Product 1:** "Beginner Photography Course"
- **FluentCart Product 2:** "Advanced Editing Masterclass"
- **FluentCart Product 3:** "The Full Photography Bundle" (which gives access to both courses)

Here’s how you would set up the product-specific feeds:

1. **Inside "Beginner Photography Course" Product:**

   - Add a LifterLMS feed.
   - In **"Add to Courses,"** select only the "Beginner Photography" LifterLMS course.
   - Set **Event Trigger** to `Order Paid (Payment / Subscription)`.
   - Check the "Remove..." box to auto-revoke access on refunds.
2. **Inside "Advanced Editing Masterclass" Product:**

   - Add a LifterLMS feed.
   - In **"Add to Courses,"** select only the "Advanced Editing Masterclass" LifterLMS course.
   - Set **Event Trigger** to `Order Paid (Payment / Subscription)`.
   - Check the "Remove..." box.
3. **Inside "The Full Photography Bundle" Product:**

   - Add a LifterLFMS feed.
   - In **"Add to Courses,"** select _both_ the "Beginner Photography" course AND the "Advanced Editing Masterclass" course.
   - Set **Event Trigger** to `Order Paid (Payment / Subscription)`.
   - Check the "Remove..." box.

With these simple, product-specific rules, FluentCart automatically handles the correct enrollment for every single purchase. Your 'Bundle' customers get both courses, while 'Beginner' customers get just one, all without you lifting a finger.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Webhook Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/integrations/webhook-integration

[Skip to content](https://docs.fluentcart.com/guide/integrations/webhook-integration#VPContent)

# Webhook Integration [​](https://docs.fluentcart.com/guide/integrations/webhook-integration\#webhook-integration)

Webhooks are a powerful tool for developers and advanced users that allow you to send real-time data from your FluentCart store to external applications and services. When a specific event occurs in your store (like a new order), FluentCart can automatically send a notification containing relevant data to a URL you specify.

This is useful for creating custom integrations, connecting to services that aren't natively supported, or building your own data processing workflows. This guide will walk you through setting up a new webhook.

### Step 1: Navigate to Integartions [​](https://docs.fluentcart.com/guide/integrations/webhook-integration\#step-1-navigate-to-integartions)

First, you'll need to go to the correct screen in your WordPress dashboard.

1. Navigate to **FluentCart Pro**.
2. Click on **Integrations** from the sidebar menu.

### Step 2: Add a New Webhook Integration [​](https://docs.fluentcart.com/guide/integrations/webhook-integration\#step-2-add-a-new-webhook-integration)

On this page, you will see all of your global integration feeds. To get started, click the **Add Integration** button in the top right corner and choose **Webhook** from the dropdown list.

![Add Integration](https://docs.fluentcart.com/images/integrations/webhook/add-integration.webp)

### Step 3: Configure the Webhook [​](https://docs.fluentcart.com/guide/integrations/webhook-integration\#step-3-configure-the-webhook)

This is where you'll tell FluentCart what data to send, where to send it, and when.

- **Integration Title:** Give your webhook a name that's easy to remember, like "Send New Sales to Slack" or "Sync Orders with Accounting."

- **Request URL:** This is the most important part. Paste the unique URL from the other application where you want to send the data.

- **Request Method:** This tells the receiving server what kind of action to perform. POST is the most common method for sending new data. You can also choose **GET**, **PUT**, **PATCH**, or **DELETE** for other advanced uses.

- **Request Format:** Choose how your data will be structured. You have two options:

  - **JSON:** This is the modern standard for most web applications and is usually the best choice.
  - **Form Data:** Use this if the receiving service specifically requires data in this format.
- **Request Headers (Optional):** Some services require a special key or code (like an API key) to accept data. You can add these here.

  - **No Headers:** Choose this if none are needed.
  - **With Headers:** Select this to add custom headers. Simply enter a **Header Name** and its corresponding **Header Value**. You can add more by clicking **\+ Add more**.
- **Request Body:** This is the actual information that will be sent.

  - **All Data:** The easiest option. This sends the complete set of default information related to the event.
  - **Selected Fields:** This gives you full control. You can choose exactly which pieces of data to send. For each field, you'll define a **Payload Key** (the name of the data field) and then select the specific Value you want to send from the dropdown.
- **Event Trigger:** This is the "when." Click the **Select Event** box to choose the specific action in your store that will trigger this webhook. You can select one or more events.


Some of the available triggers include:

- Order Paid (Payment / Subscription)
- Order Canceled
- Order Refunded (Full)
- Subscription Activated
- Subscription Renewed
- Order Shipped
- Order Delivered

This screen contains all the settings required to define what data is sent, where it's sent, and what triggers it.

![Configuring Webhook](https://docs.fluentcart.com/images/integrations/webhook/configuring-webhook.webp)

#### Step 4: Save and Activate the Webhook [​](https://docs.fluentcart.com/guide/integrations/webhook-integration\#step-4-save-and-activate-the-webhook)

- **Enable This Feed:** At the top right of the screen, ensure the toggle is switched on to make the webhook active.
- Click the **Create Webhook Feed** button at the bottom to save your configuration.

That's it! Your webhook is now live. Whenever the event you selected occurs, FluentCart will automatically send the data you configured to your URL.

### Managing Your Webhooks [​](https://docs.fluentcart.com/guide/integrations/webhook-integration\#managing-your-webhooks)

After creating a webhook, it will appear in a list on the main Webhooks screen. This dashboard provides a clear overview of all your webhooks and allows you to manage them easily.

For each webhook, you can:

- **See its Status:** The "Enabled" column shows if a webhook is active or not.
- **Enable/Disable:** Use the toggle to quickly turn a webhook on or off without deleting it.
- **Edit:** Click on the webhook's title or an edit icon to change its settings.
- **Delete:** Use the trash can icon to permanently remove a webhook.

![Configuring Webhook](https://docs.fluentcart.com/images/integrations/webhook/managing-your-webhook.webp)

---
