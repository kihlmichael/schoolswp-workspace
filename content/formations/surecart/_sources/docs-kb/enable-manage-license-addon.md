---
source_url: https://surecart.com/docs/enable-manage-license-addon
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Licensing](https://surecart.com/docs-category/licensing/)/How Licenses Work in SureCart

# How Licenses Work in SureCart

SureCart can help you automatically generate licenses for your customers upon product purchase.

It's a really simple setup that requires you to use the SureCart License Addon with SureCart.

This document will help you understand what licenses are, how they work with SureCart, and how you can set up licensing in SureCart.

Let's start with the basics.

### What is the SureCart Licensing and How Does it Work

The SureCart Licensing feature lets you create and manage license keys for any digital items you sell.

Now, let's understand how licensing works in SureCart!

Let's imagine that you sell WordPress plugins. You can enable licensing for your products, and when someone buys your WordPress, they get a unique key in their email after purchase.

Now, when your customers use that license, you can use SureCart's APIs and SDKs to check if the license was created by SureCart or not after a valid purchase.

All plans include access to the licensing feature, but the level of access may vary depending on the specific plan.

So, if you need help setting up product licensing, we're here to walk you through the process.

#### How to Enable Licensing of Products from Your Website

Setting up licensing in SureCart can be done directly from the product page, we just need to enable the license for the products needing a license, Let's take a closer look at this process.

- Open the product page and scroll down to the Licensing section. Toggle on the switch to enable license creation.

- Limit the licenses by entering any desired number in the Activation Limit field. Leave it blank for infinite activations.

- Then click on the Add Downloads button and add your plugins or themes.

- Once you add more files to the Downloads section, you will be able to select the next version from the Current Release dropdown select field.

Once the customer has purchased, they can access the license keys by selecting the purchased product in the Downloads Tab.

### How to Access the Customers' Licenses

You will also have a "Licenses" page where you can view a complete list of all licenses that were generated for your customers after their purchase.

- Go to SureCart from your WordPress website and click on Licenses.

- For each customer you wish to see the license, click on its license key.

When viewing the details of a specific license, you will see a page like this with full activation details.

### How to Validate Licenses with SDK/APIs:

If you're a developer or product owner and you want to make sure your product only runs if a valid SureCart license key is used, you can check out our SDK guide or API docs.

These will show you how to validate SureCart-generated license keys within your product.

- [API Documentation](https://api-docs.surecart.com/reference/introduction) – There are public and private API endpoints for managing licenses and activations.

- [WordPress SDK](https://github.com/surecart/wordpress-sdk) – This SDK can be used to integrate SureCart licensing with your WordPress plugins and themes.

In a nutshell, the License Addon in SureCart basically helps you protect and manage your digital products like a pro.

It ensures only people who've bought your stuff can use it, thanks to unique license keys. It's a handy tool for anyone looking to sell digital goods without the headache of unauthorized sharing.

If you have any questions as you explore the Addon, please get in touch with support.
