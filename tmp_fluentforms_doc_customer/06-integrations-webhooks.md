# Section Integrations, Webhooks & Zapier

Source : docs.fluentforms.com
Date scrape : 2026-05-24

---

## Pre-Fill Form Fields with FluentCRM Data
URL : https://fluentforms.com/docs/pre-fill-form-fields-with-fluentcrm-data/

Fluent Forms allows you to pre-fill form fields using subscriber data from [**FluentCRM**](https://fluentcrm.com/). This feature is useful for personalizing form experiences and improving user engagement.

This guide will walk you through the steps to automatically populate form fields with FluentCRM contact data.

> Only logged in users will get pre-populate form fields with FluentCRM data.

## Enable the FluentCRM Module #

Before using this feature, ensure that FluentCRM is installed and activated on your website. Follow these steps to enable the FluentCRM integration module-

First, go to **Integrations** from the Fluent Forms Navbar, search for **FluentCRM** through the search bar, and get the **FluentCRM integration module**.

Now, turn on the **Toggle** to enable the **FluentCRM** module.

![enable FluentCRM module 01 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/enable-FluentCRM-module-01-scaled.webp)

## Using FluentCRM Data Smartcode #

To pre-fill the FluentCRM data in your form fields, follow the steps given below-

First, go to**** the**Forms** section from the **Fluent Forms Navbar,** choose**** a**** desired**Form,** and click the **Edit** icon to open the **Editor** page of that form.

> If you do not have any existing forms, read [Create a Form from Scratch](https://fluentforms.com/docs/how-to-create-a-form-with-fluent-forms/) or [Create a Form using Templates](https://fluentforms.com/docs/using-and-customizing-pre-built-quick-forms-in-fluent-forms/) documentation to create a new one. 

![form editor 02 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/form-editor-02-scaled.webp)

Once you are on the **Editor** page, click the **Plus** **Icon** in your form editor and choose the desired **Field** by clicking on it or **Dragging & Drop**ping it into your editor.

![add field 03 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/add-field-03-scaled.webp)

Now, hover over the newly added field and click the **Pencil Icon**. Navigate to the **Input Customization** tab on the right sidebar. Scroll to **Advanced Options** and find the **Default Value** drop-down. In some**Input Fields** , you will find this **Default Value** option as**Dynamic Default**.

In the **Default Value** field, add FluentCRM shortcodes to automatically fetch and populate data from FluentCRM contact information into the form fields.

![access default value 04 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/access-default-value-04-scaled.webp)

Click the **Three-dot Icon** , then scroll down to locate **FluentCRM Data**. Then, click on the smartcode, and it will be automatically generated in your field.

![FluentCRM Data smartcode 05 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/FluentCRM-Data-smartcode-05-scaled.webp)

## Insert FluentCRM Data into Fields #

To get pre-filled data from **FluentCRM** , you need to use the shortcode with a small modification. **Fluent Forms** will automatically prefill with the **FluentCRM Contact** data available on your website. But remember, you will only get the pre-filled data **if you are logged in** and your **FluentCRM contact profile contains the data**.

For example, if you want to fetch the **email** from your **FluentCRM Contact’s profile** into the **Fluent Forms Email field** , first, add the shortcode **{fluentcrm.data}** in the **shortcode section** of the field. Now, modify the shortcode by adding the field name like this: {**fluentcrm.email}**. 

Once done, the **email field** will be pre-filled with data from FluentCRM. You can check out more **FluentCRM shortcodes** in this [article](https://fluentforms.com/docs/form-editor-smart-codes/).

If you want to pre-fill **Custom Fields** data from FluentCRM, first add the **desired field** to your form. Then, use the shortcode **{fluentcrm.data}** and modify it with the specific **Custom Field slug**. To learn how to find the **Custom Field slug** , check out this [documentation](https://fluentcrm.com/docs/global-custom-contact-fields/).

![email field 06 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/email-field-06-scaled.webp)

### Embed the Form into the Front #

Once you complete the customization, click the **Save** **Form** button to save all your changes. Click the **Preview & Design **button**** in the middle to see the form preview.

After that, copy the **Shortcode** from the top-right corner. **Paste** it into the **page** or **post** where you want the form to appear.

![save form 07 2 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/save-form-07-2-scaled.webp)

### Pre-populated FluentCRM Data Field Preview #

After embedding, you can preview the form with the pre-populated FluentCRM data fields. Here you will see the fields are automatically filled with **FluentCRM Data**.

![preview 08 2 50134](https://fluentforms.com/wp-content/uploads/2025/02/preview-08-2.webp)

## FluentCRM Contact Data #

To verify pre-populated data, go to the **FluentCRM** contacts. Locate the contact with the custom profile data. Now, match the field **slug** with the **FluentCRM** smartcode used in the form. If you want to learn the custom profile data read this [article](https://fluentcrm.com/docs/global-custom-contact-fields/#:~:text=When%20you%20need%20additional%20fields,as%20in%20the%20below%20screenshot.).

![custom fluentcrm data 09 scaled 50134](https://fluentforms.com/wp-content/uploads/2025/02/custom-fluentcrm-data-09-scaled.webp)

So, this feature helps your user auto-fille your users details and helps to not re enter the data again and again. 

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---

## How to Integrate Stripe with Fluent Forms
URL : https://fluentforms.com/docs/how-to-integrate-stripe-with-fluent-forms/

[Stripe](https://stripe.com) is a globally recognized payment gateway that offers **Fluent Forms** inline payment options and a smooth and secure payment experience using credit and debit cards.

This article will guide you through integrating**Stripe** into your **WordPress** **Site** with the **Fluent Forms** plugin.

> **Remember** , you can integrate **Stripe Payment Methods** with the [Free Version of Fluent Forms](https://fluentforms.com/docs/how-to-install-fluent-forms/) plugin, but a minimum platform fee of 1.9% per transaction applies. But, premium users of the [Fluent Forms Pro](https://fluentforms.com/docs/how-to-upgrade-to-fluent-forms-pro/) plugin do not need to pay any extra fees for using Stripe on your site

## Enabling Stripe Payment Method #

First, go to **Global Settings** from the **Fluent Forms Navbar** , open the **Payment** tab from the left sidebar, and click the **Payment Methods** option.

Now, go to **Stripe** in the top navbar and click **Enable** **Stripe Payment Method.** The **Stripe Payment Method** will be enabled globally for all forms. 

![1. Enable Stripe Payment method scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/1.-Enable-Stripe-Payment-method-scaled.webp)

## Configuring Stripe with Fluent Forms #

Once you enable Stripe, all the required settings will appear to configure Stripe with Fluent Forms. 

Before starting the configuration, select any **Payment Mode** between **Test** (for test payments) and **Live**(for real payments) as both options follow the same process, e.g., I choose the **Test Mode**.

Then, click the**Connect with Stripe** button to redirect you to the **Stripe Login Page** to connect your **Stripe Account**.

Do not forget to press the **Save Stripe Settings** button to save all your changes. 

![2. Connect with Stripe scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/2.-Connect-with-Stripe-scaled.webp)

Here, provide the login credentials of your desired **Stripe Account** that you want to connect with **Fluent Forms** , click the **Submit** button, and your **Stripe** account will be configured. 

> If you do not have an existing Stripe Account, [click here](https://dashboard.stripe.com/register) to open a new account.

![3. Submit button 48155](https://fluentforms.com/wp-content/uploads/2025/01/3.-Submit-button.webp)

**Remember** , **Fluent Forms** offers the above-mentioned **Connect with** **Stripe** option**** by default for secure and easy integration with **Stripe**. Also, Fluent Forms recommends using this option for all Stripe Verified Partners.

But, if you prefer the traditional **API Key method for the integration,** you can **Disable** this**Connect with Stripe** option by adding the following code snippet to your theme’s **functions.php** file or a code snippet plugin.

> We recommend you use the [Fluent Snippet Plugin](https://fluentsnippets.com/) to add any snippet code to your **WordPress Site**.
    
    
    **add_filter('fluentform/disable_stripe_connect', '__return_true');**

## Configuring Webhook to Set Up Stripe IPN #

After configuring Stripe, you can set up **IPN** (**Instant Payment Notification**) **Settings** to enable notifications for **subscription** or **recurring** **payments** in Stripe.

**IPN (Instant Payment Notification)** is a post-message notification sent by [Stripe](https://stripe.com) after a successful subscription or recurring payment. For Stripe to function completely for subscription/recurring payments, you must configure your Stripe webhooks.

**To learn how to configure Stripe Webhooks, follow the steps with screenshots below –**

First, go to **Global Settings** from the **Fluent Forms Navbar** , open the **Payment** tab from the left sidebar, and click the **Payment Methods** option.

Now, go to **Stripe** , and scroll down to the **Stripe Webhook (Recommended for Recurring Payments)** option. 

Then, copy the**Webhook URL** and the recommended **Webhook Events** for**** smooth transactions based on **Stripe** **Data** related to **Subscription/Recurring** payments. 

Do not forget to press the **Save Stripe Settings** button to save all your changes. 

![4. Add stripe webhook URL scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/4.-Add-stripe-webhook-URL-scaled.webp)

Now, visit your [Stripe Account Dashboard](https://dashboard.stripe.com/account/webhooks), click the **Developers** from the bottom-left corner, and press the **Webhooks**.

![5. Developers Webhooks scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/5.-Developers-Webhooks-scaled.webp)

Click the **\+ Add destination** button.

![6. Add Destination button scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/6.-Add-Destination-button-scaled.webp)

Now, choose the events recommended by the **Fluent Forms** for**Stripe** to send to your endpoint. 

You can find**** your **desired events** by entering their **Name** or **Description** into**** the**Events** fields and can **select** **events** by clicking the **checkbox**.

**The Events recommended by Fluent Forms are briefly explained below:**

  * **charge.succeeded** : This triggers when a charge is successfully processed. Basically, this event occurs when a payment is completed on Stripe.


  * **charge.captured** : This triggers when a previously authorized charge is successfully captured. You must use this for **Hold payments**.


  * **invoice.payment_succeeded** : This triggers when a payment for an invoice is successful. This is often used for **Subscription** **payments**.


  * **charge.refunded** : This triggers when a charge is refunded. This event helps track refund activity that happened on Stripe.


  * **customer.subscription.deleted** : This triggers when a customer’s subscription is canceled or ends. This could be due to customer action, automatic cancellation, or a failed payment after retries.


  * **customer.subscription.updated** : This triggers when a customer’s subscription is changed or updated.


  * **Checkout.session.completed** : This triggers when a checkout session is completed. This event confirms that the customer successfully paid for the session.


Once you select all the suggested**Webhook Events** , click the **Continue** button.

![7. Select Events scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/7.-Select-Events-scaled.webp)

Then, select the**Webhook endpoint** and again click the **Continue** button.

![8. Webhook endpoint scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/8.-Webhook-endpoint-scaled.webp)

Finally, paste the **Webhook URL** you copied from the **Stripe Settings** page into the **Endpoint URL** field and click the **Create destination** button. 

And, the **Stripe Webhooks** will be configured with your WordPress Site!

![9. Create Destination button scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/9.-Create-Destination-button-scaled.webp)

## Integrating Stripe in Forms #

Once you finish setting up your **Stripe** payment method, you can easily add this payment method to any of your existing**Payment Forms** (i.e., a form where [Payment Item](https://fluentforms.com/docs/add-payment-item-field-in-payment-forms/) and [Payment Method](https://fluentforms.com/docs/add-payment-method-field-in-payment-forms/) fields are added).

> If you do not have any existing **Payment Forms** , read this [Documentation](https://fluentforms.com/docs/how-to-create-a-payment-form-with-fluent-form/) to learn how to create one.

First, go to the **Editor** page of your desired form by clicking its **Edit** option.

![Open desired form scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/Open-desired-form-scaled.webp)

Once you are on the **Editor** page, go to the **Input** **Customization** menu on the right side of the added **Payment Method** field by hovering over it and clicking the **Pencil Icon**.

Now, go to the **Payment Methods** , check the **Stripe** option, click the **Dropdown Arrow,** and you will get three options. These are:

  * **Method Label** : Here, you can change the label based on your preference for your added payment method.


  * **Embedded Checkout** : Check this box to activate **Stripe** as an inline payment option.


  * **Verify Zip/Postal Code** : Check this box if you want to make providing the **Zip/Postal Code** information mandatory for your users to submit the forms. 


> To learn more details about the Payment Method field, read this [Documentation](https://fluentforms.com/docs/add-payment-method-field-in-payment-forms/).

![10. Embed checkout scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/10.-Embed-checkout-scaled.webp)

Once you complete the edit, press the **Save Form** button to save all the changes.

Now, to embed and display the form on a specific **Page/Post** , **copy** this **Shortcode** from the top right side and **paste** it into your desired**Page/Post**. 

Also, to see the **Preview** of the form, click the **Preview & Design **button in the middle.

![11. Save form scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/11.-Save-form-scaled.webp)

## Preview of Added Payment Method #

Here is the **preview** of the **Payment Method** that we just added. 

![12. Form Preview 48155](https://fluentforms.com/wp-content/uploads/2025/01/12.-Form-Preview-.webp)

## Form Specific Stripe Settings #

You can also customize the**Stripe Settings** for a specific form according to your needs.

To customize the **Stripe Settings** , go to the **Forms** from the **Fluent Forms Navbar** , and click the **Settings** option of a desired **Form**. 

![Open Form Settings scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/Open-Form-Settings-scaled.webp)

Once you are on the **Settings and Integrations** tab, click the **Payment Settings** option, scroll down to **Stripe Settings** , and customize it based on your needs.

Do not forget to click the **Save Settings** button to save all your changes. 

![13. Form Specific Stripe Settings scaled 48155](https://fluentforms.com/wp-content/uploads/2025/01/13.-Form-Specific-Stripe-Settings-scaled.webp)

**All the Stripe Settings options mentioned above are briefly explained below:**

### A. Stripe Meta Data #

Check the **Push Form Data to Stripe** to send the form submission date to your Stripe. 

![14. Stripe meta data option 48155](https://fluentforms.com/wp-content/uploads/2025/01/14.-Stripe-meta-data-option.webp)

### B. Stripe Account #

Here, you can select which stripe account credential (**Global** or **Custom**) will be used for this form. Select the **Custom Stripe Credentials** if you want to set up a different Stripe account for this specific form.

![15. Custom Stripe Credentials 48155](https://fluentforms.com/wp-content/uploads/2025/01/15.-Custom-Stripe-Credentials.webp)

### C. Stripe Payment Receipt #

Check this option if you want to disable the option of receiving payment receipt email notifications of this form.

> But we recommend you do not disable this option if you want to keep track of your payment transactions.

![16. Stripe Payment Receipt 48155](https://fluentforms.com/wp-content/uploads/2025/01/16.-Stripe-Payment-Receipt.webp)

### D. Stripe Descriptor #

Here, provide the text as per your wish (Contains between 5 and 22 characters) as a statement descriptor. If you keep it empty, your Form Name will be set as a statement descriptor.

![17. Statement Descriptor 48155](https://fluentforms.com/wp-content/uploads/2025/01/17.-Statement-Descriptor.webp)

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---

## How to Integrate PayPal with Fluent Forms
URL : https://fluentforms.com/docs/how-to-integrate-paypal-with-fluent-forms/

[PayPal](https://paypal.com) is a payment processing platform that offers **Fluent Forms** to receive payments from your users securely. This article will guide you through integrating**PayPal** into your **WordPress** **Site** with the **Fluent Forms** plugin.

> Remember, **PayPal Integration** is a **Premium Feature** of the **Fluent Forms Plugin**. So, you need the [Fluent Forms Pro](https://fluentforms.com/docs/how-to-upgrade-to-fluent-forms-pro/) plugin to integrate this.

## Enable PayPal Payment Method #

First, go to **Global Settings** from the **Fluent Forms Navbar** , open the **Payment** tab from the left sidebar, and click the **Payment Methods** option.

Now, go to **PayPal Standard** in the top navbar and click **Enable** **PayPal Payment Method.** The **PayPal Payment Method** will be enabled globally for all forms. 

![1. Enable Paypal Payment Method scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/1.-Enable-Paypal-Payment-Method-scaled.webp)

## Configure PayPal with Fluent Forms #

Once you enable the **PayPal** , all the required settings will appear to configure the PayPal with Fluent Forms. 

Before starting the configuration, select any **Payment Mode** between **Sandbox** (for test payments) and **Live (** for real payments) as both options follow the same configuration process, e.g., I choose the **Sandbox Mode**.

Then, enter the email you signed up with on the [PayPal Account](https://www.paypal.com/signin) into the **PayPal Email** field.

### **1\. Standard (Legacy Mode)** #

This legacy method relies on your primary PayPal email address and IPN responses to track single and recurring transactions.

  * **PayPal Email:** Enter the email address linked directly to your verified PayPal Business Account.

![paypal standard 3 scaled 48158](https://fluentforms.com/wp-content/uploads/2025/06/paypal-standard-3-scaled.webp)

### **2\. Checkout API (Recommended Mode)** #

Fluent Forms connects to PayPal through PayPal’s modern **Orders API v2** (one-time payments) and **Subscriptions API** (recurring payments). It gives you reliable webhook-based confirmations, native subscription support, and verified signatures on every event.

  * **Payment Mode:** Set **Mode** to **Sandbox Mode** (for test environments) or **Live Mode** (for processing real payments). Fluent Forms automatically routes API calls to the proper developer endpoints depending on this mode.


  * **Generate REST API Credentials in PayPal:**
    1. Log in to the[ PayPal Developer Dashboard](https://developer.paypal.com/dashboard/applications/).
    2. Switch to the **Sandbox** or **Live** tab to match your selected mode.
    3. Click **Create App** , name the app (for example, _Fluent Forms_), and select **Merchant** as the app type.
    4. Copy the generated **Client ID** and **Secret Key**.
  * **Enter Keys into Fluent Forms:** Paste the credentials into the matching fields inside Fluent Forms (**Test Client ID** / **Test Secret Key** or **Live Client ID** / **Live Secret Key**). **You** can fill both pairs at once; the system uses the **Mode** toggle to determine which pair is active.
  * **Webhook ID:** Input **your** verified Webhook ID.


**Webhook Settings:** To receive real-time payment, refund, and subscription events from PayPal, you must configure a webhook. In the PayPal Developer Dashboard, add a webhook with the **Webhook URL** provided in the settings box.

You must subscribe to at least to these events: 
    
    
    PAYMENT.SALE.COMPLETED
    
    BILLING.SUBSCRIPTION.ACTIVATED 
    
    BILLING.SUBSCRIPTION.CANCELLED 
    
    BILLING.SUBSCRIPTION.EXPIRED
    
    BILLING.SUBSCRIPTION.PAYMENT.FAILED 
    
    BILLING.SUBSCRIPTION.SUSPENDED

Copy your **Webhook ID** back into Fluent Forms. Webhook events are only processed when a Webhook ID is configured as a deliberate safety guard against unsigned events.

![paypal checkout api 4 scaled 48158](https://fluentforms.com/wp-content/uploads/2025/06/paypal-checkout-api-4-scaled.webp)

## Setup PayPal IPN Settings #

After configuring PayPal, you can set up **IPN** (**Instant Payment Notification**) **Settings** to enable notifications for **subscription** or **recurring** **payments** in **PayPal**.

**IPN (Instant Payment Notification)** is a post-message notification sent by **PayPal** after a successful transaction for standard merchant accounts, containing all the payment transaction details. Setting up [PayPal](https://www.paypal.com/) IPN with Fluent Forms allows you to receive Instant Payment Notifications from PayPal.

To learn how to set up **PayPal IPN** with Fluent**Forms** , follow the steps with the screenshots below – 

First, go to **Global Settings** from the **Fluent Forms Navbar** , open the **Payment** tab from the left sidebar, and click the **Payment Methods** option.

Now, go to **PayPal Standard** , and scroll down to the **PayPal IPN Settings (Recommended for Subscription Payment)** option. 

Then, copy the**IPN** URL for smooth transactions based on **PayPal** **Data** related to **Subscription/Recurring** payments. 

> If you do not set up the **IPN (Instant Payment Notification)** then it will still work for single payments but recurring payments will not be marked as paid for PayPal subscription payments.

Do not forget to press the **Save PayPal Settings** button to save all your changes. 

![3. PayPal IPN Settings scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/3.-PayPal-IPN-Settings--scaled.webp)

Now, visit the Dashboard of your [PayPal Business Account](https://www.sandbox.paypal.com/mep/dashboard), hover over the **Profile** **Icon,** and click the **Account Settings** option.

![4. Account Settings 48158](https://fluentforms.com/wp-content/uploads/2025/01/4.-Account-Settings.webp)

Then, scroll down and open the **Website Payments** tab. Go to **Instant Payment Notifications** and click the **Update** link.

![5. Website Payments 48158](https://fluentforms.com/wp-content/uploads/2025/01/5.-Website-Payments.webp)

Click the **Edit Settings** button to set up your IPN notification.

![6. Choose IPN Settings 48158](https://fluentforms.com/wp-content/uploads/2025/01/6.-Choose-IPN-Settings.webp)

Finally, **paste the URL** into the **Notification URL** field that you copied from the **Paypal IPN Settings** page.

After entering your**Notification URL,** select **Receive IPN messages (Enabled)** to activate the IPN messages for users.

Once you are done, click the **Save** button to confirm the setup.

![7. Paste IPN URL 48158](https://fluentforms.com/wp-content/uploads/2025/01/7.-Paste-IPN-URL.webp)

Here, you can see the **Notification URL** is updated and the IPN is enabled for your site.

Also, you can modify your notification URL anytime by clicking the **Edit Settings** button.  
Plus, if you want to disable the PayPal IPN, simply click the **Turn Off IPN** button.

![8. Edit Settings or Turn Off button 48158](https://fluentforms.com/wp-content/uploads/2025/01/8.-Edit-Settings-or-Turn-Off-button.webp)

## Integrate PayPal in Forms #

Once you finish setting up your **PayPal** payment method, you can easily add this payment method to any of your existing **Payment Forms** (i.e., a form where [Payment Item](https://fluentforms.com/docs/add-payment-item-field-in-payment-forms/) and [Payment Method](https://fluentforms.com/docs/add-payment-method-field-in-payment-forms/) fields are added).

> If you do not have any existing **Payment Forms** , read this [Documentation](https://fluentforms.com/docs/how-to-create-a-payment-form-with-fluent-form/) to learn how to create one.

First, go to the **Editor** page of your desired form by clicking its **Edit** option.

![Open desired form 1 scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/Open-desired-form-1-scaled.webp)

Once you are on the **Editor** page, go to the **Input** **Customization** menu on the right side of the added **Payment Method** field by hovering over it and clicking the **Pencil Icon**.

Now, go to the **Payment Methods** , check the **PayPal** option, click the **Dropdown Arrow,** and you will get two options. These are:

  * **Method Label** : Here, you can change the label based on your preference for your added payment method.


  * **Require Shipping Address** : Check this box if you want to make providing the **Shipping Address** information mandatory for your users to submit the forms. 


> To learn more details about the Payment Method field, read this [Documentation](https://fluentforms.com/docs/add-payment-method-field-in-payment-forms/).

![9. Check PayPal payment method in a desired form scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/9.-Check-PayPal-payment-method-in-a-desired-form-scaled.webp)

Once you complete the edit, press the **Save Form** button to save all the changes.

Now, to embed and display the form on a specific **Page/Post** , **copy** this **Shortcode** from the top right side and **paste** it into your desired**Page/Post**. 

Also, to see the **Preview** of the form, click the **Preview & Design **button in the middle.

![10. Save Form scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/10.-Save-Form-scaled.webp)

## Preview of Added Payment Method #

Here is the **preview** of the **Payment Method** that we just added. Once a user clicks the **Submit Form** button it will redirect to PayPal to complete the payment process. 

![11. PayPal Form Preview 48158](https://fluentforms.com/wp-content/uploads/2025/01/11.-PayPal-Form-Preview.webp)

## Form Specific PayPal Settings #

You can also customize the**PayPal Settings** for a specific form according to your needs.

To customize the **PayPal Settings** , go to the **Forms** from the **Fluent Forms Navbar** , and click the **Settings** option of a desired **Form**. 

![Open Form Settings 1 scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/Open-Form-Settings-1-scaled.webp)

Once you are on the **Settings and Integrations** tab, click the **Payment Settings** option, and scroll down to **PayPal Settings**.

Here, you can select which **PayPal Account**(**Global** or **Custom**) will be used for this form.   
Select the **Custom PayPal ID** option if you want to set up a different PayPal account for this specific form.

Do not forget to click the **Save Settings** button to save all your changes. 

![12. Form Specific PayPal Payment Settings scaled 48158](https://fluentforms.com/wp-content/uploads/2025/01/12.-Form-Specific-PayPal-Payment-Settings-scaled.webp)

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---

## How to Integrate Google Sheets with Fluent Forms
URL : https://fluentforms.com/docs/how-to-integrate-google-sheets-with-fluent-forms/

**Fluent Forms** allows you to integrate with **Google Sheets** to manage and organize form responses efficiently. This article will guide you through integrating**Google Sheets** in **Fluent Forms** on your **WordPress Site**. 

> Remember, **Google Sheets** is the **Premium Feature** of the **Fluent Forms Plugin**. So, you need the [Fluent Forms Pro](https://fluentforms.com/docs/how-to-upgrade-to-fluent-forms-pro/) plugin to integrate this.

## Enabling Google Sheets Integration #

To learn how to enable Google Sheets integration, follow the steps with the screenshots below – 

First, go to **Integrations** from the **Fluent Forms Navbar** , search for **Google Sheets** through the search bar, and get the **Google Sheets** integration module.

Now, turn on the **Toggle** to enable the **Google Sheets** module, and click the **Settings Icon** on the right side. 

![1. Enabled Google Sheet module scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/1.-Enabled-Google-Sheet-module-scaled.webp)

Once you enable Google Sheets, you will be asked for the **Access Code** from your Google account and the **Verify Code**.

> Get the Access code by clicking the [Get Google Sheet Access Code](https://accounts.google.com/o/oauth2/auth?access_type=offline&approval_prompt=force&client_id=157785030834-7bkpc1olhgp9kd683c78dclei5elhoku.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Ffluentforms.com%2Fgapi%2F&response_type=code&scope=https%3A%2F%2Fspreadsheets.google.com%2Ffeeds%2F) link. To learn the detailed process, keep reading.

![2. Access Code scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/2.-Access-Code--scaled.webp)

### Getting the Access Code from Google #

To learn how to get the Access Code from Google, follow the steps with screenshots below –

To get the Access Code from Google, [click here](https://accounts.google.com/o/oauth2/auth?access_type=offline&approval_prompt=force&client_id=157785030834-7bkpc1olhgp9kd683c78dclei5elhoku.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Ffluentforms.com%2Fgapi%2F&response_type=code&scope=https%3A%2F%2Fspreadsheets.google.com%2Ffeeds%2F), and select the desired **Google Account** where your desired **Google Sheet** exists.

![3. Desired gmail 47066](https://fluentforms.com/wp-content/uploads/2025/01/3.-Desired-gmail.webp)

Once you continue with the desired Google Account, it will take you to the **Fluent Forms Server** and generate an **Access Code**. Simply, copy the access code by clicking on the **Copy** button.

![4. Copy access code 47066](https://fluentforms.com/wp-content/uploads/2025/01/4.-Copy-access-code.webp)

## Connecting Google Sheets with Fluent Forms #

Return to the **Google Sheets** settings**** page under the**Configure Integrations** tab of the **Global Settings** section from the **Fluent Forms** **Navbar**. 

Finally, paste the **access code** you copied from **Google** into the **Access Code** field, press the **Verify Code** button, and your **Google Sheet Integration** module will be enabled. 

![5. Paste code scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/5.-Paste-code-scaled.webp)

Now, you can see that the Google Sheet has been successfully connected to your **Fluent Forms**. You can disconnect it anytime by clicking the**Disconnect Google Sheet** button. 

![6. Disconnect Goggle Sheet scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/6.-Disconnect-Goggle-Sheet-scaled.webp)

## Integrating Google Sheets with Forms #

To learn how to integrate Google Sheets into any specific Form in Fluent Forms, follow the steps with the screenshots below –

First, go to **Forms** from the **Fluent Forms Navbar** , **select** the**Desired Form** where you want to**** integrate your**Google Sheets,** and**** click the**Settings** button.

> If you do not have any existing forms, read the [Create a Form from Scratch](https://fluentforms.com/docs/how-to-create-a-form-with-fluent-forms/) or [Create a Form using Templates](https://fluentforms.com/docs/using-and-customizing-pre-built-quick-forms-in-fluent-forms/) documentation to create a new one.

![7. Open desired Form Settings scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/7.-Open-desired-Form-Settings-scaled.webp)

Once you are on the **Settings & Integrations**, go to the **Configuration Integrations** tab, click the **Add New Integration** button, and select **Google Sheet** integration feed**** from the dropdown list. 

![8. Add new integration button scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/8.-Add-new-integration-button-scaled.webp)

Now, a pop-up page will appear with various settings options for configuring the Google Sheet.  
Once you set up the page, click the **Save Feed** button, and the feed will be integrated into your form.

> **Remember** , to function Google Sheet integration with Form properly, you **must provide** the **Spreadsheet ID** and **Worksheet Name** of your**Google Sheets Account** and set up the**Spreadsheet Fields.**

![9. Save Feed button 1 scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/9.-Save-Feed-button-1-scaled.webp)

**All the settings options mentioned above are briefly explained below:**

### A. Name #

Here, you can set a name for your feed according to your preference. This field is required to be filled in.

### B. Spreadsheet ID and Worksheet Name #

Here, you need to provide the Spreadsheet ID and Worksheet Name of your Google Sheets Account that you want to integrate with the form, as it’s required to be filled in.

To learn how to get the **Spreadsheet ID** and**Worksheet Name** from Google, follow the steps in the screenshot below – 

#### Getting Spreadsheet ID #

First, open your Google Sheet where you want to receive the entries of your form.

Now you will get the **Spreadsheet ID** inside the **Spreadsheet URL**. Copy the marked portion as it is the**ID** of this particular **Spreadsheet**.

**For example** , if the spreadsheet URL is “https://docs.google.com/spreadsheets/d/19BXmmGQUB8v_jBNJZydbos-sFIzysSFTgeKmDsh-XLc/edit?gid=0#gid=0”, the **ID** of this spreadsheet will be “**19BXmmGQUB8v_jBNJZydbos-sFIzysSFTgeKmDsh-XLc/edit** ”.

#### Worksheet Name #

Now, copy the specific **Worksheet Name** where you want to receive the entries of your form. 

Feel free to name your **Worksheet** as you like. A single spreadsheet can contain multiple Worksheets, but you should select a specific one and copy only that worksheet’s name to receive the form entries.

![10. Copy Spreadsheet ID and Worsheet Name scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/10.-Copy-Spreadsheet-ID-and-Worsheet-Name-scaled.webp)

### C. Spreadsheet Fields #

This field is also required to be filled in to send the form entries to your selected worksheet under the chosen Google spreadsheet. 

You can name the field label as you want and map the value according to the field label by using the **Shortcode** button. 

**For example** , I just wanted to send the **Name** and **Email** inputs from the form to the sheets. So, I added these fields and values according to the field label.

You can add as many fields as you need by clicking the **Plus Icon** , and delete any field by clicking the**Minus Icon**.

### D. Conditional Logics #

This option allows Google Sheets integration to function conditionally based on your submission values according to your set conditional logic/s. To learn more, read this [Documentation](https://fluentforms.com/docs/set-up-forms-with-conditional-logic-in-fluent-forms/). 

### E. Enable This Feed #

Check this option to ensure this integration feed remains enabled and all its actions function properly. 

Once you set up everything and click the **Save Feed** button, you can see that your **Google Sheets Integration Feed** has been added here. 

You can modify your feed anytime by clicking the **Settings Icon** and delete it by clicking the **Trash Icon**. Also, you can disable or enable this feed anytime by turning off the **Toggle** if needed.

![11. Added Google Sheets Integration Feed scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/11.-Added-Google-Sheets-Integration-Feed-scaled.webp)

## Preview of Integrated Google Sheets #

Here, you can see the preview of the added Users in Google Sheets through the Form Entries based on the Integration.

For example, you can see four new**Form Submissions** under the **Entries** tab on this particular form.

![12. Entries tab scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/12.-Entries-tab-scaled.webp)

Now, go to the **Google Sheets Channel** you integrated and you can see the preview of the notification messages of Google Sheets through the Form entries.

![13. Preview of added entries scaled 47066](https://fluentforms.com/wp-content/uploads/2025/01/13.-Preview-of-added-entries-scaled.webp)

This way, you can easily integrate Google Sheets with Fluent Forms!  
If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---

## How to Integrate Webhook with Fluent Forms
URL : https://fluentforms.com/docs/how-to-integrate-webhook-with-fluent-forms/

**Fluent Forms** integrates with **Webhook** which will help you broadcast your **Form Submissions** to any**Web API Endpoint** with the powerful **Webhook** module. This article will guide you through integrating**Webhook** with**Fluent Forms** on your **WordPress Site**.

> Remember, **Webhook** is the**Premium Feature** of the **Fluent Forms Plugin**. So, you need the [Fluent Forms Pro](https://fluentforms.com/docs/how-to-upgrade-to-fluent-forms-pro/) plugin to integrate this.

## Enabling Webhook Integration #

To learn how to enable Webhook integration, follow the steps with the screenshots below – 

First, go to **Integrations** from the **Fluent Forms Navbar** , search for **Webhooks** through the search bar, and enable the **Webhooks** integration module by turning on the **Toggle**.

![1. Enabled Webhooks option scaled 47218](https://fluentforms.com/wp-content/uploads/2025/01/1.-Enabled-Webhooks-option-scaled.webp)

## Integrating Webhook with Forms #

To learn how to integrate Webhook into any specific Form in Fluent Forms, follow the steps with the screenshots below –

First, go to **Forms** from the **Fluent Forms Navbar** , **select** the**Desired Form** where you want to**** integrate your**Webhook** and**** click the**Settings** button.

> If you do not have any existing forms, read the [Create a Form from Scratch](https://fluentforms.com/docs/how-to-create-a-form-with-fluent-forms/) or [Create ](https://fluentforms.com/wp-admin/post.php?post=45127&action=edit)[a Form using Templates](https://fluentforms.com/docs/using-and-customizing-pre-built-quick-forms-in-fluent-forms/) documentation to create a new one.

![2. Open desired Form Settings 2 scaled 47218](https://fluentforms.com/wp-content/uploads/2025/01/2.-Open-desired-Form-Settings-2-scaled.webp)

Once you are on **Settings & Integrations**, go to the **WebHook** from the left menu, and click the **\+ Add New** button.

![3. Add New webhook scaled 47218](https://fluentforms.com/wp-content/uploads/2025/01/3.-Add-New-webhook-scaled.webp)

Now, a pop-up page will appear with various settings options for configuring Webhook. 

**All the settings options mentioned in the screenshot below are briefly explained:**

  1. **Name** : Here, you can set a name according to your preference for your feed. This field is required to be filled in.


  2. **Request URL** : This is also a required field. Here, provide the**URL** where you want to send the Fluent Form Submission data. More specifically, enter the URL that is provided by the Webhook recipient.


  3. **Request Method** : Here you need to select the HTTP method used for the Webhook request. Choose one method among the GET, POST, PUT, PATCH, and DELETE.


  4. **Request Format** : Select the data format for the Webhook request. You have to choose one format between JSON and FORM.


  5. **Request Header** : Choose whether you want to send any headers with the Webhook request.


  6. **Request Body** : Select body if you want to send any specific body text with the webhook request, otherwise, all fields will be sent. 


  7. **Conditional Logics** : This option allows Webhook integration to function conditionally based on your submission values according to your set conditional logic/s. To learn more, read this [Documentation](https://fluentforms.com/docs/set-up-forms-with-conditional-logic-in-fluent-forms/). 


Once the setup is done, click the **Save Feed** button, and your Webhook will be integrated into this specific form!

![4. Webhook Integration Feed scaled 47218](https://fluentforms.com/wp-content/uploads/2025/01/4.-Webhook-Integration-Feed-scaled.webp)

This way you can easily integrate Webhook with Fluent Forms!   
If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---

## How to Integrate Zapier with Fluent Forms
URL : https://fluentforms.com/docs/how-to-integrate-zapier-with-fluent-forms/

**Fluent Forms** integrates with [Zapier](https://zapier.com), a user-friendly, cloud-based platform that blends the simplicity of spreadsheets with the functionality of a database to help organize and collaborate on various tasks and projects. 

This article will guide you through integrating**Zapier** with**Fluent Forms** on your **WordPress Site**.

> Remember, **Zapier** is the**Premium Feature** of the **Fluent Forms Plugin**. So, you need the [Fluent Forms Pro](https://fluentforms.com/docs/how-to-upgrade-to-fluent-forms-pro/) plugin to integrate this.

## Enabling Zapier Integration #

To learn how to enable Zapier integration, follow the steps with the screenshots below – 

First, go to **Integrations** from the **Fluent Forms Navbar** , search for **Zapier** through the search bar, and enable the **Zapier** integration module by turning it on the **Toggle**. 

![1. enabled Zapier module scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/1.-enabled-Zapier-module-scaled.webp)

## Integrating Zapier with Forms #

To learn how to integrate Zapier into any specific Form in Fluent Forms, follow the steps with the screenshots below –

First, go to **Forms** from the **Fluent Forms Navbar** , **select** the**Desired Form** where you want to**** integrate your**Zapier,** and**** click the**Settings** button. 

> If you do not have any existing forms, read the [Create a Form from Scratch](https://fluentforms.com/docs/how-to-create-a-form-with-fluent-forms/) or [Create ](https://fluentforms.com/wp-admin/post.php?post=45127&action=edit)[a Form using Templates](https://fluentforms.com/docs/using-and-customizing-pre-built-quick-forms-in-fluent-forms/) documentation to create a new one.

![2. Open desired Form Settings scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/2.-Open-desired-Form-Settings-scaled.webp)

Once you are on **Settings & Integrations**, go to **Zapier** from the left menu, and click the **\+ Add Webhook** button.

![3. Add Webhook button scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/3.-Add-Webhook-button-scaled.webp)

Now, a pop-up page will appear with various settings options for configuring the Zapier.

**All the settings options mentioned in the screenshot below are briefly explained:**

  * **Name** : Here, you can set a name according to your preference for your feed. This field is required to be filled in.


  * **Webhook URL** : Here, provide the **Zapier Webhook URL** where you want to send the Fluent Forms submission data. Read this [Section](https://fluentforms.com/docs/how-to-integrate-zapier-with-fluent-forms/#2-toc-title) to learn how to get the **Zapier We** bhook URL.


  * **Conditional Logics** : This option allows Webhook integration to function conditionally based on your submission values according to your set conditional logic/s. To learn more, read this [Documentation](https://fluentforms.com/docs/set-up-forms-with-conditional-logic-in-fluent-forms/). 


Once the setup is done, click the **Save Feed** button, and your Zapier will be integrated into this specific form!

![4. Zapier Integration feed page scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/4.-Zapier-Integration-feed-page-scaled.webp)

### Getting the Webhook URL from Zapier #

To learn how to get the Webhook URL from Zapier, follow the steps below – 

First, go to your [Zapier account](https://zapier.com/app/dashboard) and log in to the dashboard.  
Now, click the **\+ Create** button and press the **Zaps** button to create a new Zap.

![5. create Zaps button scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/5.-create-Zaps-button-scaled.webp)

#### Adding Webhook Trigger #

Click the Trigger button to set the trigger

![6. Trigger button scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/6.-Trigger-button-scaled.webp)

Select **Webhooks** trigger.

![7. Webhook option 48175](https://fluentforms.com/wp-content/uploads/2025/02/7.-Webhook-option.webp)

Click on the **Choose an event** field, and a pop-up will appear to select your **Trigger event**. Select **Catch Hook** as a trigger event.

![8. Cache hook scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/8.-Cache-hook-scaled.webp)

Once you are done with the configuration, click the **Continue** button.

![9. Continue button 48175](https://fluentforms.com/wp-content/uploads/2025/02/9.-Continue-button.webp)

And you will**** get your**Webhook URL**. Now, simply copy it by clicking the **Copy** button.  
You can also test the trigger by clicking the **Test Trigger** button.

![10. copy Webhook URL 48175](https://fluentforms.com/wp-content/uploads/2025/02/10.-copy-Webhook-URL.webp)

Now, return to the **Zapier Integration** under the**Settings & Integrations **tab of the desired Form.  
Paste the **Webhook URL** you copied from **Zapier** into the **Webhook URL** field.

Finally, press the **Save Feed** button to make your **Zapier Integration** module functional.  
You can also test the integration by clicking the **Send Data Sample** button.

![11. Paste Webhook URL scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/11.-Paste-Webhook-URL-scaled.webp)

#### Adding Action #

Once you have successfully integrated Zapier with Fluent Forms, it is better to test the integration by submitting a demo form.

To test the Zapier Integration successfully, you need to add an action to this app.  
Click the **Action** button to set the action for testing the integration.

![12. Action button scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/12.-Action-button-scaled.webp)

Select an **App** through which you want to run the action and complete the full configuration process step-by-step.

![13. Select action scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/13.-Select-action-scaled.webp)

Once you have added the **Trigger** and **Action** , publish the**Zapier App** by clicking the **Publish** button.

![14.Publish app 48175](https://fluentforms.com/wp-content/uploads/2025/02/14.Publish-app.webp)

## Preview of Integrated Zapier #

Here, you can see the preview of the emails sent through the Form entries that I set up during the integration. 

![15. Preview of Zapier scaled 48175](https://fluentforms.com/wp-content/uploads/2025/02/15.-Preview-of-Zapier-scaled.webp)

This way you can easily integrate Zapier with Fluent Forms!  
If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---
