# Section Payments & Checkout

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Configuring Payments Overview - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/#VPContent)

# Configuring Payments Overview [​](https://docs.fluentcart.com/guide/payments-checkout/\#configuring-payments-overview)

The **Payments** section in FluentCart is fundamental to your online store's operation. This is where you configure how your customers pay for their purchases and how the checkout experience is managed. FluentCart offers robust options for integrating popular payment gateways and customizing various aspects of the checkout process.

### Available Payment Gateways [​](https://docs.fluentcart.com/guide/payments-checkout/\#available-payment-gateways)

This section, found under **Payment Settings** in FLuentCart **Settings**, displays all the payment gateways supported by your store along with their current status and management options. You can see a status along with the payment gateways that whether each gateways are Active or Disabled. Here click on the **Manage** button to configure its specific settings.

The available gateways include:

- **[Stripe](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings/):** Accepts global payments via credit/debit cards and other methods.
- **[PayPal](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paypal-settings/):** Enables secure online transactions and money transfers.
- **[Paddle](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings/):** Offers a complete payment solution for worldwide transactions.
- **[Mollie](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings):** A popular European payment gateway supporting major cards and local methods.
- **[Paystack](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings):** A modern payment gateway focused on helping businesses in Africa accept payments from anyone, anywhere in the world.
- **[Razorpay](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings):** A popular payment solution for businesses in India, supporting UPI, Cards, NetBanking, and Wallets.
- **[Authorize.net](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings):** A trusted payment gateway (Visa solution) that securely accepts credit cards, debit cards, and e-checks (ACH).
- **[Square](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings):** A globally trusted payment gateway that accepts Credit and Debit Cards, Apple Pay, Google Pay, and Cash App Pay through a single inline checkout.
- **[Cash on Delivery (COD)](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/cash-on-delivery-settings/):** Lets customers pay in cash when their order is delivered.

By setting up these features correctly, you can ensure a smooth, secure, and flexible payment process for your customers, leading to higher conversion rates and a better shopping experience.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## 404 - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/#VPContent)

404

# PAGE NOT FOUND

> But if you don't change your direction, and if you keep looking, you may end up where you are heading.

[Take me home](https://docs.fluentcart.com/)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Authorize.net Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings#VPContent)

# Authorize.net Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings\#authorize-net-settings)

Authorize.net is one of the most trusted payment gateways, allowing you to securely accept credit cards, debit cards, and e-checks (ACH). Integrating it with FluentCart provides your customers with a professional and reliable checkout experience.

This guide provides a step-by-step walkthrough to connect your Authorize.net account, configure your checkout appearance, and set up webhooks for automated order processing.

## Step 1: Accessing Authorize.net Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings\#step-1-accessing-authorize-net-settings)

First, you need to locate the integration settings within your WordPress site.

1. Navigate to **FluentCart Pro > Settings** from your WordPress sidebar.
2. Select the **Payment Settings** tab from the sidebar.
3. Scroll down to find **Authorize.net** and click the **Manage** button.

![Authorize.net Settings](https://docs.fluentcart.com/assets/authorize-payment-method-1.DbXOJbro.webp)

## Step 2: Obtain API Credentials from Authorize.net [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings\#step-2-obtain-api-credentials-from-authorize-net)

To connect your store, you need to retrieve four specific keys from your Authorize.net Merchant Interface.

1. Log in to your [**Authorize.net Dashboard**](https://login.authorize.net/).
2. Go to the **Account** tab in the main navigation.
3. Click on **Account and API Settings** (located under the Account section).
4. Select **API Credentials and Keys**.

![Authorize.net Settings](https://docs.fluentcart.com/assets/authorize-payment-method-2.C-P8QiED.webp)

**Collect your Keys:**

- **API Login ID:** Copy the API Login ID displayed on this page.
- **Transaction Key:** Select "Generate New Transaction Key," click **Submit**, and copy the generated value.
- **Signature Key:** Select "Generate New Signature Key," click **Submit**, and copy it.
- **Public Client Key:** Click the "Generate New Public Client Key" button and copy the resulting string.

![Authorize.net Settings](https://docs.fluentcart.com/assets/authorize-payment-method-3.CAa46RUQ.webp)

## Step 3: Configure Credentials in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings\#step-3-configure-credentials-in-fluentcart)

Now, return to your WordPress site to input the credentials you just gathered.

1. **Choose Your Mode:**
   - **Test credentials:** Use this tab first to perform test transactions without using real money.
   - **Live credentials:** Switch to this tab once you are ready to go live.
2. **Enter the Keys:** Paste the **API Login ID**, **Transaction Key**, **Client Key**, and **Signature Key** into their respective fields.
3. **Enable e-Check (ACH):** If you want customers to pay directly via their bank accounts, check the **Enable e-Check (ACH)** box.
4. **Customize the Checkout UI:**
   - **Authorize.Net Checkout Form Button Text:** Change the text that appears on the Authorize.net popup (e.g., "Pay Now").
   - **Authorize.Net Checkout Form Header Text:** Set a custom title for the payment popup (e.g., "Secure Checkout").
   - **FluentCart Checkout Button Text:** This is the text for the main button on your checkout page (e.g., "Place Order").
   - **Button Colors:** Use the color pickers to match the button background and hover colors to your website's branding.
5. **Enable Debug Logging:** Log Authorize.Net API interactions for troubleshooting.

![Authorize.net Settings](https://docs.fluentcart.com/assets/authorize-payment-method-4.E3jacvB7.webp)

## Step 4: Configure Webhooks [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings\#step-4-configure-webhooks)

Webhooks are critical for communication. They allow Authorize.net to notify FluentCart the moment a payment is successful, failed, or a subscription is renewed.

1. **Copy the Webhook URL:** On the FluentCart Authorize.net settings page, locate the **Webhook URL** (it looks like `https://your-site.com/?fluentcart_api...`). Click the copy icon.
2. **Add Webhook in Authorize.net:**
   - In your Authorize.net dashboard, go to **Account > Webhook Notifications > Webhooks**.
   - Click the **\+ Create a webhook notification** button.

![Authorize.net Settings](https://docs.fluentcart.com/assets/authorize-payment-method-5.D1Y6ZYvH.webp)

3. **Fill in Webhook Details:**
   - **Name:** Give a name to your Webhook like "FluentCart Webhook."
   - **Endpoint URL:** Paste the URL you copied from FluentCart.
   - **Status:** Ensure this is set to **Active**.
4. **Select Events:**Check the boxes for the following recommended events:
   - `net.authorize.payment.authcapture.created`
   - `net.authorize.payment.fraud.approved`
   - `net.authorize.payment.fraud.declined`
   - `net.authorize.payment.void.created`
   - `net.authorize.payment.refund.created`
   - `net.authorize.customer.subscription.cancelled`
   - `net.authorize.customer.subscription.expired`
   - `net.authorize.customer.subscription.expiring`
5. Click **Save** to finalize.

![Authorize.net Settings](https://docs.fluentcart.com/assets/authorize-payment-method-6.yHrtn3Tj.webp)

## Step 5: Activation and Final Save [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/authorizenet-settings\#step-5-activation-and-final-save)

- **Payment Activation:** Look for the toggle at the top right of the FluentCart Authorize.net settings page. Switch it to **ON**.
- **Save Settings:** Click the **Save Settings** button at the bottom right.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Cash on Delivery (COD) & Offline Payments - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/cash-on-delivery-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/cash-on-delivery-settings#VPContent)

# Cash on Delivery (COD) & Offline Payments [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/cash-on-delivery-settings\#cash-on-delivery-cod-offline-payments)

Cash on Delivery allows customers to pay with cash directly upon receiving their order. This section also covers settings for other manual, offline payment processes like bank transfers.

1. On the **Payment Settings** screen, locate **"Cash on Delivery"** and click the **"Manage"** button next to it.

2. This will open the **Offline Payment Settings** screen.

![Screenshot of Cash on Delivery Settings Page](https://docs.fluentcart.com/images/payments-checkout/cash-on-delivery-settings.webp)

3. **Enable Cash on Delivery:** Check the box next to "Customers can pay for their orders by cash upon delivery." to activate this method.

4. **Payment Activation:** In the top right corner of this page, ensure the **Payment Activation** option is " **Enabled**".

5. Click the **"Save Settings"** button to apply your changes.


Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Configuring Stripe via wp-config.php - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig#VPContent)

# Configuring Stripe via wp-config.php [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig\#configuring-stripe-via-wp-config-php)

FluentCart integrates perfectly with **Stripe**. While you can connect your account directly from the settings panel, this guide will walk you through the more secure method of configuring Stripe by adding your API keys to your site's `wp-config.php` file.

> **Info:** Storing your API keys in the `wp-config.php` file is a security best practice. It keeps your credentials outside of the WordPress database, protecting them from potential database-related vulnerabilities.

### Step 1: Get Your API Keys from Stripe [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig\#step-1-get-your-api-keys-from-stripe)

First, you need to collect your **Publishable Key** and **Secret Key** from your Stripe dashboard.

1. Log in to your [Stripe Dashboard](https://dashboard.stripe.com/).
2. In the right corner, click on **Developers**, then select **API keys** from the menu.
3. On this page, you will find your keys. You will need to copy both the **Publishable key** (starts with `pk_...`) and the **Secret key** (starts with `sk_...`).

> **Note on Test vs. Live Keys:** Your Stripe account has two sets of keys: one for testing ( **Test data**) and one for real payments ( **Live data**). It is recommended to start with your Test keys to ensure the connection is working correctly before switching to your Live keys.

### Step 2: Add the Keys to Your wp-config.php File [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig\#step-2-add-the-keys-to-your-wp-config-php-file)

Next, you will add the copied keys to your WordPress site's configuration file.

1. Access the `wp-config.php` file using any WordPress file manager plugin or through your hosting file manager.
2. Locate the `wp-config.php` file in the root directory of your WordPress installation.
3. Open the file to edit it. Scroll down to the bottom, just above the line that says `/* That's all, stop editing! Happy publishing. */`.
4. Add the following two lines of code, replacing the placeholders with the keys you copied from Stripe:

php

```

define('FCT_STRIPE_LIVE_PUBLIC_KEY','ENTER YOUR PUBLIC API KEY HERE');
define('FCT_STRIPE_LIVE_SECRET_KEY','ENTER YOUR SECRET KEY HERE');
```

Example (using test keys for testing mode):

php

```

define('FCT_STRIPE_TEST_PUBLIC_KEY','ENTER YOUR PUBLIC API KEY HERE');
define('FCT_STRIPE_TEST_SECRET_KEY','ENTER YOUR SECRET KEY HERE');
```

Save the `wp-config.php` file and close it.

### Step 3: Configure Webhooks [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig\#step-3-configure-webhooks)

Webhooks are essential for the integration to function correctly. They allow Stripe to send real-time notifications to your store about payment events, such as successful charges, refunds, and subscription updates.

1. **Copy Your Webhook URL:** On the FluentCart Stripe settings page, you will see your unique **Webhook URL**. **Copy** this **URL** to your clipboard.
2. **Configure in Stripe:** Click the **Add Endpoint** link, and you’ll be redirected to your **Create an event destination** page.
3. **Select the Important Events:** Now, choose the events recommended by **FluentCart** for **Stripe** to send to your **endpoint**. Under **Events**, click the **All events** tab. Click the checkboxes to select these specific events:

The Events recommended by FluentCart are briefly explained below:

- **checkout.session.completed:** The customer finished checkout, and the order is ready to process.
- **charge.refunded:** A completed payment has been refunded to the customer.
- **charge.refund.updated:** Details of a refund were updated (like the amount or reason).
- **charge.succeeded:** The customer’s payment went through successfully.
- **invoice.paid:** A subscription invoice was paid by the customer.
- **invoice.payment.failed:** A subscription invoice payment failed (e.g., card declined).
- **customer.subscription.deleted:** The customer canceled their subscription.
- **customer.subscription.updated:** The customer’s subscription was changed (e.g., upgraded or downgraded).

Once you select all the suggested **Webhook Events**, click the **Continue** button.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/select-events.webp)

Then, select the **Webhook endpoint** and again click the **Continue** button.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/webhook-endpoint.webp)

Next, type a destination name, **paste** the **webhook URL** you copied earlier into the **Endpoint URL** field, and then click the “ **Create Destination**” button.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/create-destination.webp)

#### Step 4: Activate and Save [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig\#step-4-activate-and-save)

1. **Payment Activation:** Back on the **FluentCart Stripe settings** page, ensure the **Payment Activation** toggle at the top right is switched on.
2. **Save Settings:** Click the **Save Settings** button at the bottom to finalize the setup.

Your Stripe integration is now ready to securely process payments for your store!

---

## Flutterwave Integration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings#VPContent)

# Flutterwave Integration [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings\#flutterwave-integration)

Flutterwave is a powerful payment gateway that allows you to accept payments globally, with a strong focus on African markets. By connecting Flutterwave to your FluentCart store, your customers can pay securely using their Credit/Debit Cards, Bank Transfers, Mobile Money, USSD, M-Pesa, and more.

This step-by-step guide will walk you through everything you need to know to successfully integrate Flutterwave into your store.

## Step 1: Install and Activate Flutterwave [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings\#step-1-install-and-activate-flutterwave)

Before you can connect your account, you need to enable the Flutterwave module inside your FluentCart store.

1. Log in to your **WordPress Dashboard**.
2. Navigate to **FluentCart > Settings** in the left-hand menu.
3. Click on the **Payment Settings** tab.
4. Scroll down the list of available payment methods until you find **Flutterwave**.
5. Click the **Manage** button next to it.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-1.DBnncOXF.webp)

6. You will see a prompt saying the add-on is not installed. Click the blue **Install & Activate** button. This will instantly install the free integration.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-2.BdCT1fuJ.webp)

7. Once activated, the Flutterwave settings panel will open automatically.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-3.Dtef59m_.webp)

## Step 2: Locate Your API Keys in Flutterwave [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings\#step-2-locate-your-api-keys-in-flutterwave)

To link your store securely, you need special codes called "API Keys." You can get these directly from your Flutterwave account.

> **Note:** Flutterwave offers both Live keys (for taking real money) and Test keys (for making fake purchases to ensure your store works).

1. Open a new tab in your browser and log in to your [**Flutterwave Merchant Dashboard**](https://app.flutterwave.com/login).
2. In the left-hand menu, scroll down to the **Settings** section.
3. Under the Developers menu, click on **API keys**.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-4.D_Eo_dK_.webp)

4. Look for the section labeled **V3 API keys** (Make sure you are viewing the "Test API Keys" if you are setting up a test environment, or "Live API Keys" for your actual store).
5. You will see a **Public key**, **Secret key**, and **Encryption Key**.
6. Use the Copy buttons next to each key. Leave this browser tab open, as you will need it again.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-5.D-ACQdO_.webp)

## Step 3: Connect the Keys to FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings\#step-3-connect-the-keys-to-fluentcart)

Now, switch back to your WordPress dashboard to paste the keys you just copied.

1. On the FluentCart Flutterwave Settings page, toggle the **Payment Activation** switch (at the top right) to turn it on.
2. Choose either the **Live credentials** or **Test credentials** tab, depending on which keys you copied from Flutterwave.
3. Paste your keys into the correct boxes:
   - **Test/Live Public Key**
   - **Test/Live Secret Key**
   - **Webhook Secret Hash:** This is a security feature. You need to create your own unique, secure password or phrase here (for example: `my_store_secure_hash_2026`). Write this exact phrase down or copy it, because you must give this exact same phrase to Flutterwave in the next step.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-6.Bkr6PUQ4.webp)

## Step 4: Configure Webhooks (Crucial Step) [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings\#step-4-configure-webhooks-crucial-step)

**What is a webhook?** A webhook is how Flutterwave "talks" to your store. When a customer finishes paying, Flutterwave uses the webhook to silently tell FluentCart, "The payment was successful, you can mark this order as Processing!" If you skip this step, orders will not update automatically.

1. Still on the FluentCart settings page, look right below the Secret Hash field. You will see a **Webhook URL** (it looks like a long web link starting with `http://...`). Click the small copy icon next to it.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-webhook.00rGiOU_.webp)

2. Go back to your open Flutterwave Dashboard tab.
3. In the left-hand menu under Developers, click on **Webhooks**.
4. Paste your copied link into the **URL** field.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-7.D4vXb1gp.webp)

5. In the **Secret hash** field, type or paste the exact same password/phrase you created in Step 3.
6. Under **Webhook preferences**, it is highly recommended to check all of these boxes:
   - Receive webhook response in JSON format
   - Enable webhook retries
   - Enable v3 webhooks
   - Enable resend webhook from the dashboard
   - Add meta to webhook
7. _(Optional)_ If you want FluentCart to know if a payment failed or was refunded, click **View** on "Webhook preferences with custom url" and paste the exact same Webhook URL into the **Enable webhook for failed transactions** and **Enable webhook for refunds** fields.
8. Click the orange **Save** button in Flutterwave.

![Flutterwave](https://docs.fluentcart.com/assets/flutterwave-8.BQVRfCGA.webp)

## Step 5: Save and Test Your Store [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/flutterwave-settings\#step-5-save-and-test-your-store)

1. Return to your FluentCart Dashboard one last time.
2. Click the **Save Settings** button at the very bottom right corner.

You are all set! We highly recommend keeping your store in Test Mode first. Once confirmed, swap out your Test Keys for your Live Keys to start accepting real payments.

> **⚠️ Important: Server Configuration Required**
>
> To ensure webhooks are delivered successfully, you may need to whitelist Flutterwave on your server.
>
> - Ensure your server firewall or security plugins allow incoming requests from Flutterwave.
> - If using a WAF (Web Application Firewall) or security plugin, whitelist Flutterwave's webhook domain.
> - Check your server error logs if webhooks are failing to reach your site.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Mercado Pago Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings#VPContent)

# Mercado Pago Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings\#mercado-pago-settings)

Mercado Pago is a leading payment platform, making it the perfect choice for businesses operating in Latin America. By connecting **Mercado Pago to FluentCart**, you can securely accept a wide variety of local payment methods, including Credit Cards, Pix, Boleto, OXXO, and Bank Transfers.

This guide will walk you through the entire process of connecting your Mercado Pago account to FluentCart.

## Step 1: Activate Mercado Pago in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings\#step-1-activate-mercado-pago-in-fluentcart)

First, you need to enable Mercado Pago as a payment method in your store.

1. From your WordPress dashboard, navigate to **FluentCart Pro > Settings**.
2. Click on the **Payment Settings** tab.
3. Find **Mercado Pago** in the list of available gateways and click the **Manage** button.
4. If the addon is not yet installed, click the **Install & Activate** button to begin the setup.

![Mercado Pago Install & Activate](https://docs.fluentcart.com/assets/install-activate-mercado-pago-1.CThBLXQs.webp)

## Step 2: Configure Mercado Pago Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings\#step-2-configure-mercado-pago-settings)

Once activated, you need to provide your API credentials to sync your store with your Mercado Pago account.

1. Enable the gateway by toggling the **Payment Activation** switch at the top right.
2. Choose your credential mode:
   - **Test credentials:** Select this tab to test your checkout flow without processing real money.
   - **Live credentials:** Select this tab when you are ready to accept real payments from your customers.
3. You will need to enter the following information for your chosen mode:
   - Public Key
   - Access Token
   - Webhook Secret

NOTE

**Testing Your Setup:** When using **Test credentials**, you may notice many "false errors" appearing, or the API might suddenly become unavailable. These issues can prevent you from completing the proper checkout flow for your tests. Because of this, we highly recommend testing your store using your **real Production credentials** before officially going live to ensure everything is working perfectly.

> **Currency Match:** Ensure that your FluentCart store currency is set to the same currency used in your Mercado Pago account.

![Payment Activation](https://docs.fluentcart.com/assets/payment-activation-3.B_ArMq6Q.webp)

## Step 3: Create an Application in Mercado Pago [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings\#step-3-create-an-application-in-mercado-pago)

To get your keys, you must first create an application in the Mercado Pago Developers portal.

1. Log in to your **[Mercado Pago Developers dashboard](https://www.mercadopago.com/developers/panel/app)** and go to **Your integrations**. Click the **Create application** button.

![Create Application](https://docs.fluentcart.com/assets/create-application-4.1atVT70U.webp)

2. Enter your **Application name** and click **Continue**.

![Application Name](https://docs.fluentcart.com/assets/application-name-5.CqXh1vhs.webp)

3. Select **Online payments** and choose the option to create your store. Click on the **Continue** button.

![Online Payment](https://docs.fluentcart.com/assets/online-payment-6.BtIFM1Wv.webp)

4. Confirm your details and click **Confirm** to generate your application.
5. Navigate to **Production credentials** in the side menu to copy your **Public Key** and **Access Token** for later use.

![Copy Public Key & Access Token](https://docs.fluentcart.com/assets/copy-public-key-7.DRnlCFjE.webp)

## Step 4: Set up Webhooks [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mercado-pago-settings\#step-4-set-up-webhooks)

Webhooks are essential for FluentCart to receive real-time updates about transaction statuses.

1. **Copy the Webhook URL:** On your FluentCart Mercado Pago settings page, copy the unique **Webhook URL** provided.
2. **Configure in Mercado Pago:** In your Mercado Pago application, navigate to **Notifications > Webhooks** and click **Configure notifications**.

![Configure Notification](https://docs.fluentcart.com/assets/configure-notification-8.DYJFcESH.webp)

3. **Paste the URL:** Paste the link into the **URL for testing** (for Test mode) or **Production method** (for Live mode) field.
4. **Select Events:**Under "Recommended events," check the boxes for:
   - Payments
   - Plans and subscriptions
5. **Get Your Secret:** Click **Save settings**. A **Secret signature (Webhook Secret)** will be generated.

![Configure Webhook Notification](https://docs.fluentcart.com/assets/configure-webhook-notification-9.DTh2QNAa.webp)

6. **Add to FluentCart:** Copy this secret and paste it into the **Test/Live Webhook Secret** field back in your FluentCart settings.

Once all fields are filled, click the **Save Settings** button at the bottom of the page to finalize your integration.

![Add To FluentCart](https://docs.fluentcart.com/assets/save-settings-10.Cwow7KcT.webp)

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Mollie Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings#VPContent)

# Mollie Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings\#mollie-settings)

Mollie is a popular and flexible payment gateway, primarily used in Europe, that allows you to securely accept credit cards, debit cards, and various other local payment methods like ApplePay, and Bancontact.

This guide will walk you through every step of connecting your Mollie account to FluentCart.

### Step 1: Get Your API Keys from Mollie [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings\#step-1-get-your-api-keys-from-mollie)

First, you need to get your **API Key** from your Mollie dashboard. This key is like a password that allows your FluentCart store to securely communicate with Mollie.

1. Log in to your [Mollie Dashboard](https://www.mollie.com/dashboard).
2. In the top menu, click **Browse**. A dropdown menu will appear.
3. Under the **Developers** heading, click on **API keys**.
4. On this page, you will see your **Live API key** and your **Test API key**.

> **Info: Test Mode vs. Live Mode** It is highly recommended to start with your **Test API key**. This allows you to make test purchases on your store without using real money. Once you are sure the connection is working correctly, you can switch to your Live API key to begin accepting real payments.

![Mollie API Configuration](https://docs.fluentcart.com/assets/mollie-2.DVATqgLL.webp)

For now, click the **Copy** button next to your **Test API key**.

![Mollie API Configuration](https://docs.fluentcart.com/assets/mollie-3.Bz54gmxa.webp)

### Step 2: Configure Mollie in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings\#step-2-configure-mollie-in-fluentcart)

Now that you have your test key, let's go back to your WordPress dashboard to paste it into FluentCart.

1. From your WordPress dashboard, navigate to **FluentCart Pro** \> **Settings**.
2. Click on the **Payment Settings** tab.
3. You will see a list of available payment gateways. Find **Mollie** and click the **Manage** button.
4. This will take you to the Mollie configuration page.

**Configure the Settings:**

- **Payment Activation:** First, ensure the **Payment Activation** toggle at the top right is switched **ON**. This makes Mollie available as an option at checkout.
- **Select Credentials Tab:** You will see two tabs: **Live credentials** and **Test credentials**. Click on the **Test credentials** tab.
- **Paste Your Key:** Paste the Test API key you copied from Mollie into the **Test API Key** field.
- **You can configure methods here:** From here you can directly visit to select Payment page of Mollie.
- **Save Settings:** Click the **Save Settings** button at the bottom of the page.

![Mollie API Configuration](https://docs.fluentcart.com/assets/mollie-7.Di0d3nUr.webp)

### Step 3: Go Live with Real Payments [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/mollie-settings\#step-3-go-live-with-real-payments)

When you are ready to start accepting real money, follow these simple steps to switch from Test to Live mode:

1. Go back to your Mollie Dashboard and copy your **Live API key**.
2. Return to your FluentCart Mollie settings ( **FluentCart Pro > Settings > Payment Settings > Mollie**).
3. Click on the **Live credentials** tab.
4. Paste your **Live API key** into the **Live API key** field.
5. Click **Save Settings**.
6. Finally, make sure your store's main **Order Mode is set to Live** (`FluentCart Pro > Settings > Store Settings`).

Your Mollie integration is now live and ready to securely process payments for your store!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Paddle Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings#VPContent)

# Paddle Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#paddle-settings)

Paddle is an all-in-one payment solution that simplifies selling globally by handling payments, sales tax, and compliance for you. By connecting Paddle with FluentCart, you can offer your customers a seamless checkout experience with a wide range of payment methods.

This guide will walk you through the entire process of connecting your Paddle account to FluentCart.

## Step 1: Activate Paddle in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#step-1-activate-paddle-in-fluentcart)

1. First, you need to enable **Paddle** as a payment method in your store.
2. From your WordPress dashboard, navigate to **FluentCart Pro** \> **Settings**.
3. Click on the **Payment Settings** tab.
4. You will see a list of available payment gateways. Find Paddle and click the **Manage** button next to it.

This will take you to the main Paddle settings page, where you will configure the entire integration.

![Screenshot of Activate Paddle in FluentCart](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/activate-paddle.webp)

### Step 2: Configure Paddle Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#step-2-configure-paddle-settings)

On this page, you need to provide your Paddle API credentials and customize the checkout experience.

First, enable the payment gateway by toggling the **Payment Activation** switch at the top right. Here's a breakdown of the available settings:

- **Test/Live Credentials:** You can switch between Test credentials and Live credentials. It's recommended to start with the test mode to ensure everything is working correctly before accepting real payments.
- **Sandbox/Live API Key:** Enter your API Key from your Paddle dashboard.
- **Sandbox/Live Client Token / Public Key:** Enter your Client Token or Public Key from Paddle.
- **Sandbox/Live Webhook Secret:** Enter your Webhook Secret Key. You'll get this when you set up the webhook in your Paddle account (see next step).

To find your API Keys and Client Token, log in to your [Paddle account](https://login.paddle.com/login) and navigate to the **Developer Tools → Authentication** section.

![Screenshot of Payment Activation](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/payment-activation.webp)

#### Generating API Key [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#generating-api-key)

Once you log in to the Paddle Dashboard, open the **Developer Tools** dropdown list from the left sidebar, and click **Authentication**. Now, go to the **API keys** section and click the **\+ New API key** button.

![Screenshot of API key](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/api-key.webp)

Now, provide the **Name** and **Description** for your API key, click the **Save** button, and your desired API key will be generated.

Here, you can see the newly generated API Key. Now, press the **Copy key** button, and your desired **API Key** will be copied.

![Screenshot of Copy API key](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/copy-api-key.webp)

#### Generating Client Token / Public Token [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#generating-client-token-public-token)

Now, go to the **Client-side tokens** section and click the **\+ New client-side token** button.

Now, provide the **Name** and **Description** for your client token, click the **Save** button, and your desired client token will be generated.

![Screenshot of Client Token/ Public Token](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/client-token.webp)

Here, you can see the newly generated Client Token. Now, click the **Three-dot icon** and press the **Copy Token** button.

![Screenshot of Copy Client Token/ Public Token](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/copy-client-token.webp)

### Step 3: Set up Webhooks in Paddle [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#step-3-set-up-webhooks-in-paddle)

Webhooks are essential for FluentCart to receive real-time updates about transaction statuses, subscriptions, and other events from Paddle.

1. **Copy the Webhook URL:** First, copy the **Webhook URL** provided on your FluentCart Paddle settings page.
2. **Create a New Webhook in Paddle:** Log in to your Paddle dashboard. Navigate to **Developer Tools → Notifications**. Next, click on the **\+ New destination** button.

![Screenshot of Notification](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/new-destination.webp)

A modal will appear. **Paste** the URL you copied from FluentCart into the **Webhook URL** field.

3. **Select Webhook Events:**In the webhook creation form, you need to select the events that Paddle will send to FluentCart. Check the boxes for the following events:
   - `transaction.completed`
   - `transaction.paid`
   - `transaction.payment_failed`
   - `adjustment.created`
   - `adjustment.updated`
   - `subscription.created`
   - `subscription.activated`
   - `subscription.updated`
   - `subscription.paused`
   - `subscription.resumed`
   - `subscription.canceled`

After selecting the events, save the webhook by clicking the **Save destination** button. Paddle will provide you with a **Webhook Secret**. Simply copy this webhook secret for future use.

![Screenshot of Events](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/events.webp)

#### Add Webhook Secret to FluentCart: [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#add-webhook-secret-to-fluentcart)

Go back to your FluentCart **Paddle Settings** page in WordPress. Then, **paste** the API key, Secret key, and Webhook Secret into their respective fields.

## Customization Options [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paddle-settings\#customization-options)

You can also customize the appearance and text of the Paddle checkout button:

- **Tax Mode:** This setting determines how taxes are calculated for your transactions.

  - **Use paddle account settings:** This is the recommended option. It leverages Paddle's powerful tax platform to automatically calculate and remit sales tax and VAT for you worldwide. All tax settings will be managed directly from your Paddle dashboard.
  - **Internal:** Select this if you want to use the tax rates you have configured within FluentCart's own tax settings ( **FluentCart → Tax & Duties**).
  - **External:** Choose this option if you are using a third-party service to handle tax calculations or if you do not need to charge tax. FluentCart will not add any tax to the transaction.
- **Paddle Checkout Theme:** Select a **Light** or **Dark** theme for the Paddle checkout modal.

- **Paddle Checkout Button Text:** Customize the text that appears on the payment button (e.g., "Pay with Card", "Proceed to Paddle").

- **Button Styling:** Adjust the **Button Color**, **Button Hover Color**, **Button Text Color**, and **Button Font Size** to match your store's design.

- **Disable Webhook Verification:** This security feature ensures that webhook notifications are genuinely coming from Paddle. It should only be disabled for specific debugging or testing scenarios. For a live store, always keep this setting enabled to protect your store from fraudulent requests.

![Screenshot of Customization](https://docs.fluentcart.com/images/payments-checkout/paddle-payment/customization-options.webp)


Once you have configured all the settings, click the **Save Settings** button. Your Paddle integration is now complete!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## PayPal Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paypal-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paypal-settings#VPContent)

# PayPal Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paypal-settings\#paypal-settings)

PayPal provides a fast and secure way for customers to send and receive money or make online payments.

1. On the **Payment Settings** screen, locate **"PayPal"** and click the **"Manage"** button next to it.
2. This will open the **PayPal Settings** screen.

INFO

Please note that you must have a PayPal Business or Merchant account to accept payments through this integration. The following step will prompt you to log in to this account.

![Screenshot of PayPal Settings Page](https://docs.fluentcart.com/images/payments-checkout/paypal-settings.webp)

3. **Test Mode Warning:** If your store is in Test mode, a banner will remind you: "Your Store is in Test mode, Change Store's 'Order Mode' to 'Live' and update related settings to enable Live payment !!" This is crucial to switch to live mode for real transactions.
4. **Connect Your PayPal Account:** Here, you don't need any API keys. Just click on the **Connect with PayPal** button. You'll then be directed to "PayPal" to log in to your account. Once logged in, you will see that your PayPal account is successfully connected with your FluentCart store.
5. **Payment Activation:** In the top right corner of this page, ensure the PayPal **Payment Activation** option is "Active".
6. Click the **"Save Settings"** button to apply your changes.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Paystack Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings#VPContent)

# Paystack Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings\#paystack-settings)

Paystack is a popular and secure payment gateway that allows you and your customers to pay using credit cards, debit cards, bank transfers, USSD, and more. When you integrate Paystack with FluentCart, you can easily accept fast and reliable payments from customers across Africa, as well as international payments from customers worldwide.

This guide will walk you through the entire process of connecting your Paystack account to FluentCart.

## Step 1: Install & Activate Paystack in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings\#step-1-install-activate-paystack-in-fluentcart)

First, you need to install and enable Paystack as a payment method in your store.

1. From your WordPress dashboard, navigate to **FluentCart Pro > Settings**.
2. Click on the **Payment Settings** tab.
3. You will see a list of available payment gateways. Find **Paystack** and click the **Install & Activate** button next to it.
4. After a moment, the page will refresh, and the button will change to **Manage**. Click the **Manage** button to open the Paystack Settings page.

![Installing and activating Paystack in FluentCart Payment Settings](https://docs.fluentcart.com/assets/enable-paystack-payment.o1rxuQqq.webp)

## Step 2: Configure Paystack Settings in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings\#step-2-configure-paystack-settings-in-fluentcart)

On this page, you will connect your Paystack account to FluentCart.

First, enable the payment gateway by toggling the **Payment Activation** switch at the top right.

You will see two tabs: **Live credentials** and **Test credentials**. It is highly recommended to start with the **Test credentials** to ensure everything is working correctly before accepting real payments.

On this page, you will see some fields to fill in and one URL to copy:

- Test Public Key
- Test Secret Key
- Webhook URL

To get this information, you will need to log in to your Paystack dashboard.

## Step 3: Set up Webhooks [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings\#step-3-set-up-webhooks)

Webhooks are essential for Paystack to send real-time updates to FluentCart, such as confirming successful payments or subscription renewals.

- **Copy the Webhook URL:** In your FluentCart Paystack settings, copy the entire **Webhook URL** provided.

![Set Up Webhooks](https://docs.fluentcart.com/assets/payment-activation-2.BuuVYrCE.webp)

## Step 4: Get the Credential from Paystack [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/paystack-settings\#step-4-get-the-credential-from-paystack)

Now, open a new tab and log in to your **Paystack dashboard**. Go to **Settings > Developers** (or **Settings > API Keys & Webhooks**). You can access the Paystack Developer Settings Page.

1. **Paste the Webhook URL:** Find the **Test Webhook URL** field. Paste the URL you just copied from FluentCart into this field.
2. **Copy Your API Keys:** On this same page, you will find your **Test Public Key** and **Test Secret Key**. Click the " **copy**" icon next to each key.

![Finding API Keys and Webhook fields in the Paystack dashboard](https://docs.fluentcart.com/assets/paystack-settings-3.CAUCEqZc.webp)

3. **Paste Keys into FluentCart:** Now, go back to your FluentCart settings page. **Paste** the **Test Public Key** and **Test Secret Key** into their matching fields.
4. **Save Changes:** Click **Save changes** in your Paystack dashboard, and then click the **Save Settings** button in your FluentCart dashboard.

![Finding API Keys and Webhook fields in the Paystack dashboard](https://docs.fluentcart.com/assets/save-settings-4.qdNlg1Rp.webp)

Your Paystack integration is now complete and in **Test Mode**. We recommend running a test transaction with a Paystack test card to ensure the connection is working.

To go live, simply repeat Step 3 using the **Live credentials** tab in FluentCart and the **Live API Keys** and **Live Webhook URL** fields in your Paystack dashboard.

If you have any questions or need further assistance, feel free to reach out to our [support team](https://wpmanageninja.com/support-tickets/?utm_source=wpsnsite&utm_medium=popup&utm_campaign=spring#/).

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Razorpay Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings#VPContent)

# Razorpay Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#razorpay-settings)

Razorpay is a popular and powerful payment solution, especially perfect for businesses in India. It allows you to accept a wide variety of payments, including UPI, Credit/Debit Cards, NetBanking, and Wallets. By connecting Razorpay to FluentCart, you provide your customers with a fast and secure payment option for their orders.

This guide will walk you through how you can get Razorpay up and running on your store.

## Step 1: Activate Razorpay in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#step-1-activate-razorpay-in-fluentcart)

Before you can use Razorpay, you need to add the feature to your FluentCart store.

1. Log in to your WordPress dashboard and go to **FluentCart Pro > Settings**.
2. Click on the **Payment Settings** tab on the left.
3. You will see a list of available payment gateways. Find **Razorpay** and click the **Manage** button next to it.
4. If it isn't ready yet, you will see a screen with an **Install & Activate** button. Click on it.

![ Activate Razorpay](https://docs.fluentcart.com/assets/access-razorpay-1.DQqON1ve.webp)

## Step 2: Configure Razorpay Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#step-2-configure-razorpay-settings)

On this page, you need to provide your Razorpay API credentials to connect your store to your bank account.

First, enable the payment gateway by toggling the **Payment Activation** switch at the top right. Here is a breakdown of the available settings:

- **Live/Test Credentials:** You can switch between the Live credentials and Test credentials tabs. It is highly recommended to start with test mode to ensure your checkout is working perfectly before you start accepting real money from customers.
- **Test/Live API Key:** Enter the **Key ID** you copied from your Razorpay dashboard into this field.
- **Test/Live Key Secret:** Enter the **Key Secret** generated in your Razorpay account here.
- **Test/Live Webhook Secret:** Enter your **Webhook Secret** key. You will get this secret when you set up the webhook in your Razorpay dashboard to receive payment updates.

TIP

Now, copy the **Webhook URL** from this page for future use in Step 4.

![ Configure Razorpay Settings](https://docs.fluentcart.com/assets/payment-activation-2.nol9sfPU.webp)

## Step 3: Get Your Keys from Razorpay [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#step-3-get-your-keys-from-razorpay)

To integrate your store with Razorpay, you require two special codes: a **Key ID** and a **Key Secret**.

1. Log in to your **[Razorpay](https://rize-dashboard.razorpay.com/login/) Dashboard**.
2. In the left sidebar, go to **Accounts & Settings**.
3. Click on the **API Keys** tab.

![ Get API Keys From Razorpay](https://docs.fluentcart.com/assets/razorpay-account-settings-3.2RKDQz1G.webp)

4. Click the **Regenerate Test Key** (or "Generate Key") button.

![ Get API Keys From Razorpay](https://docs.fluentcart.com/assets/Regenarate-Test-Key-4.xvIOL8Gy.webp)

5. Copy the **Key ID** and **Key Secret** that appear. Keep these safe!

![ Copy Key ID and Secret](https://docs.fluentcart.com/assets/Copy-the-public-key-secret-key-5.CEcLC1Je.webp)

## Step 4: Set Up Webhooks [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#step-4-set-up-webhooks)

Webhooks are like "digital status updates." They tell FluentCart exactly when a customer has finished paying so the order can be marked as "Paid" automatically.

1. In your Razorpay Dashboard, go to **Settings > Webhooks**.
2. Click on the **Add New Webhook** button.

![ Add New Webhook](https://docs.fluentcart.com/assets/add-new-webhook-6.DDE3fX61.webp)

3. In the popup that appears, paste the **Webhook URL** you copied before from FluentCart.

4. In the **Active Events** section, select these specific events to ensure your store stays updated:

**Required Payment Events:**


   - `payment.authorized` - Payment authorized successfully.
   - `payment.captured` - Payment captured and confirmed.
   - `payment.failed` - Payment failed or declined.
   - `refund.processed` - Refund completed successfully.

**Required Subscription Events (if applicable):**

   - `subscription.authenticated` - Customer completed authentication.
   - `subscription.activated` - Subscription is now active.
   - `subscription.charged` - Recurring payment successful.
   - `subscription.cancelled` - Subscription was cancelled.
   - `subscription.halted` - Payment failures caused a halt.
   - `subscription.completed` - All billing cycles completed.
5. Click the **Create Webhook** button to save your changes.

6. Razorpay will provide a **Webhook Secret**. **Copy** it for later use.


IMPORTANT

Make sure to save the Webhook Secret in the credentials section in your FluentCart settings for secure webhook verification.

![ Create Webhook](https://docs.fluentcart.com/assets/create-webhook-7.4JQ8fSrb.webp)

## Step 5: Finalize Configuration in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#step-5-finalize-configuration-in-fluentcart)

Now, take those keys and put them into your store settings.

1. Go back to your **FluentCart Payment Settings** for Razorpay.
2. Choose between the **Live credentials** or **Test credentials** tab.
3. Paste your **Key ID** and **Key Secret** into the corresponding fields.
4. Paste the **Test or Live Webhook Secret** you copied earlier from Razorpay.

> \[Tip\] We recommend starting with "Test" mode to make sure everything works before you take real money!

![ Finalize Configuration](https://docs.fluentcart.com/assets/razorpay-settings-8.BPCNcSuP.webp)

* * *

### Important: International Payments [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/razorpay-settings\#important-international-payments)

If you want to sell to customers outside of India, there is an extra step:

- You must enable **International Payments** inside your actual **Razorpay Dashboard settings**.
- Without this, customers using cards from other countries might see their payments declined.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Square Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings#VPContent)

# Square Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#square-settings)

Square is a globally trusted payment gateway that lets you accept Credit and Debit Cards through a single, secure inline checkout, with no redirects. By connecting Square with FluentCart, you can offer your customers a fast and reliable checkout experience along with support for recurring subscriptions and automatic refunds via webhooks.

This guide will walk you through every step of connecting your Square account to FluentCart, from activating the gateway in your store to configuring credentials and setting up webhooks.

## Step 1: Activate Square in FluentCart [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#step-1-activate-square-in-fluentcart)

First, you need to install and enable **Square** as a payment method in your store.

1. From your WordPress dashboard, navigate to **FluentCart Pro > Settings**.
2. Click on the **Payment Settings** tab.
3. You will see a list of available payment gateways. Find **Square** and click the **Manage** button next to it.

![Find Square in FluentCart Payment Settings](https://docs.fluentcart.com/assets/square-1.74K9osaC.webp)

4. Since Square is a premium add-on, you will be taken to the Square Payment Gateway page. Click the **Install & Activate** button to enable it for your store.

![Install and activate Square Payment Gateway](https://docs.fluentcart.com/assets/square-2.DGz0w_WT.webp)

Once activated, you will land on the main **Square Settings** page where you will configure the connection.

![Square Settings page in FluentCart](https://docs.fluentcart.com/assets/square-3.D9ayW-XW.webp)

On this page you will see two tabs, **Test credentials** and **Live credentials**. It is highly recommended to start with **Test credentials** to make sure everything is working correctly before accepting real payments. You will need to fill in the following fields:

- **Test Application ID**
- **Test Access Token**
- **Test Location ID**
- **Test Webhook Signature Key**

You will also see a **Webhook URL** that you will copy into Square in a later step. To collect the credentials, log in to your Square Developer Dashboard.

## Step 2: Create an Application in Square Developer Dashboard [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#step-2-create-an-application-in-square-developer-dashboard)

To connect your store, you need to create a new application in the Square Developer Dashboard.

1. Log in to your [**Square Developer Dashboard**](https://developer.squareup.com/apps).
2. On the **Applications** page, click the **+** (plus) card to create a new application.

![Create a new application in Square Developer Dashboard](https://docs.fluentcart.com/assets/square-4.MHO3EDty.webp)

3. A modal titled **Name your application** will appear. Type a name for your application (e.g., `FluentCart`) and click **Next**. Follow the remaining prompts as per your requirements to finish creating the application.

![Name your Square application](https://docs.fluentcart.com/assets/square-5.B6NUpJfb.webp)

## Step 3: Get Your API Credentials from Square [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#step-3-get-your-api-credentials-from-square)

Once your application is created, you can grab the credentials FluentCart needs.

1. Open your newly created application from the Square Developer Dashboard.
2. Make sure the **Sandbox** toggle at the top is selected (you will switch to **Production** later when going live).
3. From the left sidebar, click **Credentials**.
4. On this page you will see two values. Click the **Copy** icon next to each:
   - **Sandbox Application ID** \- paste this into the **Test Application ID** field in FluentCart.
   - **Sandbox Access token** \- click **Replace** if needed, then paste this into the **Test Access Token** field in FluentCart.

![Copy Sandbox Application ID and Access token from Square](https://docs.fluentcart.com/assets/square-6.BqJg96gk.webp)

> **Info: Test Mode vs. Live Mode** The **Sandbox** credentials let you test transactions without using real money. When you are ready to go live, repeat these steps from the **Production** tab and paste the values into the **Live credentials** tab in FluentCart.

### Get Your Location ID [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#get-your-location-id)

Square uses **Locations** to represent the source of your orders.

1. Still inside your application, click **Locations** from the left sidebar.
2. Find your **Default Test Account (Main)** in the list.
3. Copy the value under the **Location ID** column.
4. Paste it into the **Test Location ID** field in FluentCart.

![Copy Location ID from Square Developer Dashboard](https://docs.fluentcart.com/assets/square-7.BUcJoiO5.webp)

## Step 4: Set Up the Webhook in Square [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#step-4-set-up-the-webhook-in-square)

Webhooks are essential for Square to send real-time updates to FluentCart, such as confirming successful payments, processing refunds, and handling subscription renewals.

1. Go back to your **FluentCart Square Settings** page and copy the **Webhook URL** shown at the bottom of the form.
2. In your Square Developer Dashboard, expand **Webhooks** in the left sidebar and click **Subscriptions**.
3. Click the **Add subscription** button on the right side of the page.

![Add a new webhook subscription in Square](https://docs.fluentcart.com/assets/square-8.BjFLjqXh.webp)

4. In the **Add a webhook subscription** form, fill in the following:
   - **Subscription name:** Give it a recognizable name like `FluentCart-WH`.
   - **Notification URL:** Paste the **Webhook URL** you copied from FluentCart.
   - **API version:** Leave this set to the default (latest) version.
5. Under the **Events** section, search for and select the following 5 events that FluentCart needs:
   - `payment.updated`
   - `refund.updated`
   - `subscription.updated`
   - `invoice.payment_made`
   - `invoice.scheduled_charge_failed`
6. Click **Save** at the top right to create the subscription.

![Configure webhook subscription details and events](https://docs.fluentcart.com/assets/square-9.BvDTxIZT.webp)

Once saved, your new webhook will appear in the **Webhooks** list with the **Enabled** status and **5** events selected.

![Square webhook subscription created and enabled](https://docs.fluentcart.com/assets/square-10.3K7TDCQo.webp)

### Copy the Signature Key [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#copy-the-signature-key)

Now you need to grab the **Signature Key** that secures the webhook communication.

1. Click the **FluentCart-WH** webhook entry from the list to open its details panel on the right.
2. Locate the **Signature key** field and click the **Copy** icon next to it.
3. Paste the value into the **Test Webhook Signature Key** field in FluentCart.

![Copy the webhook signature key from Square](https://docs.fluentcart.com/assets/square-11.BCrWlGiu.webp)

## Step 5: Activate Payment and Save Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#step-5-activate-payment-and-save-settings)

Now that you have all four credentials in place, it's time to activate the gateway.

1. Go back to your FluentCart **Square Settings** page.
2. Make sure all the fields under **Test credentials** are filled in:
   - **Test Application ID**
   - **Test Access Token**
   - **Test Location ID**
   - **Test Webhook Signature Key**
3. Switch the **Payment Activation** toggle at the top right to **ON**. This makes Square available as a payment option at checkout.
4. Click the **Save Settings** button at the bottom of the page.

![Enable Payment Activation and save Square settings](https://docs.fluentcart.com/assets/square-12.SG34pmcX.webp)

Your Square integration is now complete and running in **Test Mode**. We recommend running a test transaction with a Square test card to make sure everything is working correctly.

## Step 6: Go Live with Real Payments [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/square-settings\#step-6-go-live-with-real-payments)

When you're ready to start accepting real payments, follow these simple steps to switch from Test to Live mode:

1. In your Square Developer Dashboard, switch the toggle from **Sandbox** to **Production** at the top of your application.
2. Repeat **Step 3** and **Step 4** to collect your **Production Application ID**, **Production Access Token**, **Production Location ID**, and **Production Webhook Signature Key**.
3. Return to your FluentCart **Square Settings** page and click the **Live credentials** tab.
4. Paste the production credentials into their matching fields and click **Save Settings**.
5. Finally, make sure your store's main **Order Mode is set to Live** under **FluentCart Pro > Settings > Store Settings**.

Your Square integration is now live and ready to securely process payments for your store.

Note

Square Wallet payment support (Apple Pay, Google Pay, Cash App Pay) is disabled at the moment and will be available soon. Card payments and recurring subscriptions are fully supported.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Stripe Settings - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings

[Skip to content](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings#VPContent)

# Stripe Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings\#stripe-settings)

Stripe is a powerful and globally recognized payment platform that allows you to securely accept credit cards, debit cards, and various other payment methods through a single, seamless integration.

This guide will walk you through connecting your Stripe account to FluentCart to begin accepting payments.

## Step 1: Accessing Stripe Settings [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings\#step-1-accessing-stripe-settings)

1. From your WordPress dashboard, navigate to **FluentCart Pro > Settings**.
2. Click on the **Payment Settings** tab.
3. Locate **Stripe** in the list of payment gateways and click the **Manage** button next to it.

#### Step 2: Connect Your Stripe Account [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings\#step-2-connect-your-stripe-account)

The Stripe settings page allows you to connect your store in both Test and Live modes. You must select the appropriate mode before initiating the connection.

- **Test Mode Warning:** If your store is currently in Test mode, a banner will remind you to switch to Live mode for real transactions.

- **Select Credentials Mode:**

  - **Test credentials:** Select this tab if you want to connect your Stripe account in Test Mode. This is perfect for testing your checkout flow without processing real payments.
  - **Live credentials:** Select this tab when you are ready to start accepting real payments from customers.
- **Connect with Stripe:** After selecting the appropriate tab (Test or Live), click the **Connect with stripe** button. This will redirect you to Stripe's website, where you will be prompted to log in and authorize the connection with FluentCart. This is a secure process that automatically syncs your account for the selected mode.


INFO

FluentCart securely stores your Stripe connection information using a salt key encryption method. This ensures your informations remain fully encrypted in the database and protected from unauthorized access.

#### Step 3: Choose Your Checkout Mode [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings\#step-3-choose-your-checkout-mode)

FluentCart gives you two different ways for customers to pay:

- **Embedded checkout (Recommended):** This keeps the customer on your website. It’s a customizable block that lets you control the design.
- **Stripe Hosted checkout:** This sends the customer to a secure page managed by **Stripe**. This is great for high-volume stores or if you want Stripe to handle all the complex security rules for you.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/stripe-settings.webp)

#### Step 4: Configure Webhooks [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings\#step-4-configure-webhooks)

Webhooks are essential for the integration to function correctly. They allow Stripe to send real-time notifications to your store about payment events, such as successful charges, refunds, and subscription updates.

1. **Copy Your Webhook URL:** On the FluentCart Stripe settings page, you will see your unique **Webhook URL**. **Copy** this **URL** to your clipboard.

2. **Configure in Stripe:** Click the **Add Endpoint** link, and you’ll be redirected to your **Create an event destination** page.

3. **Select the Important Events:** Now, choose the events recommended by **FluentCart** for **Stripe** to send to your **endpoint**. Under **Events**, click the **All events** tab. Click the checkboxes to select these specific events:


The Events recommended by FluentCart are briefly explained below:

- **checkout.session.completed:** The customer finished checkout, and the order is ready to process.
- **charge.refunded:** A completed payment has been refunded to the customer.
- **charge.refund.updated:** Details of a refund were updated (like the amount or reason).
- **charge.succeeded:** The customer’s payment went through successfully.
- **invoice.paid:** A subscription invoice was paid by the customer.
- **invoice.payment.failed:** A subscription invoice payment failed (e.g., card declined).
- **customer.subscription.deleted:** The customer canceled their subscription.
- **customer.subscription.updated:** The customer’s subscription was changed (e.g., upgraded or downgraded).

Once you select all the suggested **Webhook Events**, click the **Continue** button.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/select-events.webp)

Then, select the **Webhook endpoint** and again click the **Continue** button.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/webhook-endpoint.webp)

Next, type a destination name, **paste** the **webhook URL** you copied earlier into the **Endpoint URL** field, and then click the “ **Create Destination**” button.

![Screenshot of Stripe Settings Page](https://docs.fluentcart.com/images/payments-checkout/stripe-payment/create-destination.webp)

#### Step 5: Activate and Save [​](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/stripe-settings\#step-5-activate-and-save)

1. **Payment Activation:** Back on the **FluentCart Stripe settings** page, ensure the **Payment Activation** toggle at the top right is switched on.
2. **Save Settings:** Click the **Save Settings** button at the bottom to finalize the setup.

Your store is now configured to securely accept payments through Stripe.

> **Note** You can also connect your Stripe account by adding your API keys directly to your site's `wp-config.php` file for more secure setup. For detailed instructions on this advanced method, please see our guide on [**Configuring Stripe via wp-config.php**](https://docs.fluentcart.com/guide/payments-checkout/connecting-payment-gateways/configure-stripe-via-wpconfig).

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
