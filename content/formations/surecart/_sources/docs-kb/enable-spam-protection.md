---
source_url: https://surecart.com/docs/enable-spam-protection
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Enable Spam Protection and Security in SureCart

# How to Enable Spam Protection and Security in SureCart

Spam is definitely one of the most problematic things that we've come across on the internet whether it be on your email, your phone, or even on your online shop.

The good news is that SureCart comes with built-in spam prevention and other security options to help you feel at ease with running your online site.

### What is the Value of Maintaining Shop Security

There are many different types of exploits, hacks, or even simple annoyances that can happen if you don't beef up your store security:

1. Spam
2. Malware
3. Data Hacks
4. DOS Attacks
5. And much more...

A lot of these are very serious issues that could put you and your customers at risk. As the site owner, you hold the responsibility of making sure that you and everyone on your site are protected from any of these attacks and entities.

### What is Spam Protection

Spam is when you get unwanted, annoying messages or actions, often sent in large amounts, that can mess up websites, servers, or services for regular users.

To stop spam, people have come up with different methods. One common way is to add tests or actions that real users can pass but spammers can't.

### SureCart's Spam Protection & Security

You can find the spam protection settings by navigating to your **WordPress Dashboard > SureCart > Settings > Advanced**, from here, scroll down to "Spam Protection & Security."

#### Test Mode Restricted

The **Test Mode Restricted** setting gives you control over who can perform test orders on your site.

When this setting is **enabled** (default), only users with administrator roles can complete test orders that create actual order entries in your system. For non-administrative users, they can still simulate a test order and see a "Test checkout successful" confirmation popup; however, no order data will be saved or processed.

When this setting is **disabled**, anyone with access to the checkout form can perform test orders, and the test orders will create entries in the system.

By default, this setting is **enabled**, ensuring tighter control over test order functionality for enhanced security.

#### Honeypot

Honeypot is a tool that is used to add a field to your forms that are invisible to actual human users on a browser, but are visible to bots.

This is done in the hopes of tricking these bots into filling out the forms as they are programmed to do, and therefore identifying them as such.

In this case, they will be denied access to the site and to complete the form and purchase. As a result, we can prevent them from spamming the site and disallowing the spam transactions from pushing through.

This field is completely invisible to actual users since they are not displayed to people who visit your checkout form.

#### ReCaptcha v3

reCaptcha is probably something that you've seen before and are familiar with. Google was the first to develop this and it started out as a simple puzzle that you need to solve to prove that you are human.

In order to enable reCaptcha v3 in SureCart, you have to register your site and set it up on Google.

Here are the steps on how to register your site:

1. Sign in to your Google Account
2. Go to [Google reCaptcha site admin registration page](https://www.google.com/recaptcha/admin/create)
3. Add a Label, this can be anything but to avoid confusion, you may enter the name of your site in this field
4. Select the reCaptcha type, for this case, select "Score based (v3)"
5. Add the domain/s of your website
6. Agree to the terms of service
7. Click **Submit**

From the next page, you can see your **Site Key** and **Secret Key**. These are the keys that you need to enable your reCaptcha v3 on SureCart.

Back on SureCart, copy the keys and paste them into the corresponding fields from your "Advanced" Tab.

Once you click **Save**, you're all set. Google reCaptcha v3 has been successfully set up on your online shop.

#### Stripe Fraud Monitoring

The **Stripe Fraud Monitoring** setting helps protect your store from fraudulent transactions by utilizing Stripe's built-in fraud detection tools. When enabled, this setting loads **stripe.js** on every page, allowing Stripe to monitor and analyze user activity to identify potential fraud.

**Benefits of enabling Stripe Fraud Monitoring:**

- Prevents fraudulent transactions and chargebacks.
- Monitors user behavior to flag potentially risky activity.
- Seamlessly integrates with your existing Stripe payment gateway.

Enabling this setting is highly recommended for stores processing high transaction volumes or operating in regions with elevated fraud risks.

#### Strong Password Validation

With this option, your password fields, in the checkout form, gain an extra layer of security, ensuring that only strong, validated passwords are accepted.

These validations include requiring passwords to be more than 6 characters long and having a special character included in addition to the alphanumeric password.

With this enabled, you can be sure that you and your users adhere to these rules to help contain any potential for breaches in security related to weak and easily guessed passwords.

By following these guidelines, you can be rest assured that you may never have the problem of dealing with spam and security issues in your SureCart store.
