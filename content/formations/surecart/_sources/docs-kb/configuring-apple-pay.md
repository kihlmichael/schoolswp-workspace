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
