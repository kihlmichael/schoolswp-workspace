# Section Tax & Duties

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Configuring Tax Settings & Classes - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes#VPContent)

# Configuring Tax Settings & Classes [​](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes\#configuring-tax-settings-classes)

The **Configuration & Classes** screen is the control center for your store's entire tax system. Here, you will set the fundamental rules for how taxes are calculated, manage EU VAT compliance for B2B sales, and create **Tax Classes** to handle different tax rates for different types of products.

Getting these settings right is the first step to ensuring your tax calculations are accurate.

### Accessing Tax & Duties Settings [​](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes\#accessing-tax-duties-settings)

1. From your WordPress dashboard, navigate to **FluentCart Pro** \> **Settings**.
2. Click on the **Tax & Duties** tab from the left-hand menu.
3. Select the **Configuration & Classes** sub-menu.

### Tax Configuration [​](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes\#tax-configuration)

This section contains the main rules that determine how taxes are calculated across your store.

- **Enable Tax:** This is the master switch for your store's tax system. When enabled, FluentCart will begin applying your tax rules at checkout.
- **Prices entered with tax:** This tells FluentCart whether your product prices already include tax ( **Included**) or if tax should be added at checkout ( **Excluded**).
- **Calculate Tax Based On:** This determines which customer address is used for tax calculations: **Customer Shipping Address**, **Customer Billing Address**, or **Store Base Address**.
- **Price Suffix:** This allows you to add a short piece of text that will be displayed next to your product prices on the storefront. For example, you could add `+ VAT` or `(incl. Tax)` to provide clarity for your customers.

![Configuration and Classes](https://docs.fluentcart.com/assets/configuration-classes-1.2xwbLwXr.webp)

### EU VAT Settings [​](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes\#eu-vat-settings)

This section is specifically for handling European Union VAT regulations for your business-to-business (B2B) sales.

- **Enable EU VAT Number:** When enabled, this adds a VAT number field to your checkout page for customers in the EU. If a customer provides a valid VAT ID, the VAT will be removed from their order (a **"reverse charge"**).
- **Local Reverse Charge:** In some cases, reverse charge rules can apply even if the business customer is in your own country. Enable this to ensure FluentCart handles these specific transactions correctly.
- **Exclude Categories from VAT reverse:** This allows you to select specific product categories that should always be charged VAT, even if a customer provides a valid VAT ID. This is useful for certain types of products or services that are not eligible for the reverse charge mechanism.

After configuring these settings, be sure to click the **Save Settings** button.

### Managing Tax Classes [​](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes\#managing-tax-classes)

**Tax Classes** are the best way to group products that have similar tax treatments. This is essential if you sell items that are not all taxed at the same rate (e.g., standard-rate electronics vs. zero-rated books).

#### Adding a New Tax Class [​](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes\#adding-a-new-tax-class)

In the **Existing Tax Classes** section, click the **Add Tax Class** button.

![Configuration and Classes](https://docs.fluentcart.com/assets/configuration-classes-2.ZZbxGPYz.webp)

1. A pop-up window will appear. Fill in the details:
   - **Tax Class Name:** A clear name, like "Digital Services" or "Clothing."
   - **Priority:** A number (0-10) that determines the order in which tax classes are applied. **Higher numbers have a higher priority** and will be applied first.
   - **Product Category (Optional):** You can link this tax class directly to one or more product categories. When you do, any product in the selected category will automatically use this tax class.
   - **Description:** An internal note for your reference.
2. Click **Create**.

![Configuration and Classes](https://docs.fluentcart.com/assets/configuration-classes-3.D99JRy9H.webp)

> **Info:** For a tax class to work correctly, you must complete two key steps: first, assign this class to a product (either by linking it to a **Product Category** here or by editing an individual product), and second, make sure you set a specific **Tax Rate** for this class in that country's regional settings.

Your new tax class will now appear in the list, where you can **Edit** or **Delete** it at any time using the action icons.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Configuring European Union (EU) VAT - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat#VPContent)

# Configuring European Union (EU) VAT [​](https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat\#configuring-european-union-eu-vat)

Selling to customers within the European Union (EU) requires careful handling of Value Added Tax (VAT). FluentCart provides a dedicated and powerful wizard to simplify EU VAT compliance, guiding you through the process of setting up your tax collection method based on your business type and registration.

### Accessing EU VAT Settings [​](https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat\#accessing-eu-vat-settings)

1. From your WordPress dashboard, navigate to **FluentCart Pro** \> **Settings**.
2. Click on the **Tax & Duties** tab.
3. From the sub-menu, select **European Union**.

![European Union Settings](https://docs.fluentcart.com/assets/european-union-settings.C29PZB_b.png)

### Choosing Your VAT Collection Method [​](https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat\#choosing-your-vat-collection-method)

The first time you visit this screen, FluentCart will launch a setup wizard to help you choose how you want to collect VAT in the EU. This choice is crucial as it determines how tax rates are applied to your customers.

Here’s a breakdown of the three options to help you choose the right one for your business:

**1\. Collect using a One Stop Shop (OSS) registration**

This is the most common and recommended method for businesses that sell to customers in multiple EU countries. The OSS system simplifies your VAT obligations by allowing you to declare and pay the VAT for all your EU sales through a single registration in one EU member state.

- **Who it's for:** Businesses of any size that have a single OSS VAT number and want to streamline their tax reporting for the entire EU.

**2\. Collect using your home country registration**

This option is specifically designed for small and micro-businesses based within the EU that have a low volume of cross-border sales.

- **Who it's for:** EU-based micro-businesses with total cross-border EU sales of less than €10,000 per year. This allows you to apply your home country's VAT rate to all sales within the EU, simplifying your tax process significantly.

**3\. Collect specific country rate**

This is an advanced method for businesses that are individually registered for VAT in each specific EU country where they sell goods or services.

- **Who it's for:** Larger businesses or those who prefer (or are required) to manage separate VAT registrations in each EU country they operate in.

### Detailed Configuration Guides [​](https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat\#detailed-configuration-guides)

Once you have selected the method that best fits your business, follow the detailed guide below to complete your setup:

- [**Configuring the OSS Method:**](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss) Follow this guide if you have a single OSS VAT registration for all EU countries.
- [**Configuring with a Home Country Registration:**](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country) Follow this guide if you are an EU-based micro-business selling less than €10,000 per year to other EU countries.
- [**Configuring Specific Country Rates:**](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country) Follow this guide if you manage separate VAT registrations for each EU country you sell to.

### Customer VAT Numbers on PDF Receipts [​](https://docs.fluentcart.com/guide/tax-&-duties/european-union-vat\#customer-vat-numbers-on-pdf-receipts)

When a customer enters a VAT number at checkout, FluentCart now renders that VAT number directly inside the **billing address block** of every generated PDF receipt (Order Receipt, Renewal Receipt, Refund Notice, and Invoice).

This makes FluentCart receipts drop-in ready for B2B buyers in the EU, UK, and other VAT jurisdictions who need a properly formatted receipt for their own bookkeeping - no custom template work or manual workaround needed. For B2C orders where no VAT number is provided, receipts continue to look exactly the same. See [PDF Invoice Templates](https://docs.fluentcart.com/guide/settings-configuration/email-configuration/pdf-invoice) for the full PDF setup.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Configuring EU VAT with a Home Country Registration - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country#VPContent)

# Configuring EU VAT with a Home Country Registration [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country\#configuring-eu-vat-with-a-home-country-registration)

This VAT collection method is specifically designed for small and micro-businesses based within the European Union (EU) that have a low volume of cross-border sales to other EU countries. It simplifies the tax process significantly by allowing you to apply your own country's VAT rate to all sales you make within the EU.

### Who Should Use This Method? [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country\#who-should-use-this-method)

You should select this option if your business meets the following criteria:

- Your business is located in an EU member state.
- Your total cross-border sales to other EU countries are less than **€10,000 per year**.

If you meet these requirements, you can use your local VAT registration to collect taxes, which is much simpler than managing an OSS registration or registering in multiple countries.

### How to Configure Your Home Country Registration [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country\#how-to-configure-your-home-country-registration)

If you selected **"Collect using your home country registration"** from the main EU VAT setup wizard, you will be taken to a simple configuration screen.

- **Country of registration:** From the dropdown menu, select the EU country where your business is officially registered for VAT.
- **VAT number:** Enter your local VAT number.

Click **Save**.

![European Home Country VAT](https://docs.fluentcart.com/assets/home-country-tax-1.B3qJs0_I.png)

Once you save these settings, FluentCart will be configured to handle your EU VAT obligations correctly.

![European Home Country VAT](https://docs.fluentcart.com/assets/home-country-tax-2.CW39a0Ju.png)

### How It Works at Checkout [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country\#how-it-works-at-checkout)

With this method active, FluentCart will automatically apply your home country's VAT rates to all sales made to customers in any EU member state. For example, if your business is registered in Austria and a customer from Germany makes a purchase, they will be charged the Austrian VAT rate, not the German one.

### Managing Your Registration [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-home-country\#managing-your-registration)

After the initial setup, you will be taken to the main EU VAT dashboard. Here, you will see a summary of your active registration.

- **Change Registration:** If your business grows and your sales exceed the €10,000 threshold, you will need to switch to an OSS registration. You can click the **Change Registration** link to return to the initial setup wizard and select a different VAT collection method.
- **Edit:** If you need to update your VAT number or change your country of registration, you can click the **Edit** button to modify your existing settings.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Configuring EU VAT with Specific Country Rates - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country#VPContent)

# Configuring EU VAT with Specific Country Rates [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country\#configuring-eu-vat-with-specific-country-rates)

This VAT collection method is an advanced option for businesses that are individually registered for VAT in each specific European Union (EU) country where they sell goods or services. It gives you granular control to manage tax rates on a country-by-country basis.

### Who Should Use This Method? [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country\#who-should-use-this-method)

You should select this option if your business meets the following criteria:

- You are registered for VAT in one or more specific EU countries.
- You do not use the simplified OSS (One Stop Shop) or the micro-business home country registration scheme.

This method is typically used by larger businesses or those with specific legal requirements to maintain separate VAT registrations.

### How to Configure Specific Country Rates [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country\#how-to-configure-specific-country-rates)

Select **"Collect specific country rate"** from the main EU VAT setup wizard, you will be taken to a configuration screen where you can choose the countries you are registered in.

![Specific Country Settings](https://docs.fluentcart.com/assets/specific-country-1.D1dP_Oeh.png)

#### Step 1: Configure Your Registered Countries [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country\#step-1-configure-your-registered-countries)

First, you need to tell FluentCart which EU countries you will be collecting VAT for.

1. On the **"Collect specific country VAT"** screen, click the **Configure Countries** button.

![Specific Country Settings](https://docs.fluentcart.com/assets/specific-country-2.tdfv1b2Q.png)

2. A pop-up window will appear, listing all the countries in the European Union.
3. Click the **Select** button next to each country where you have a VAT registration.

![Specific Country Settings](https://docs.fluentcart.com/assets/specific-country-3.BH7JwDWp.png)

4. Once you have selected all the relevant countries, close the pop-up.

The countries you selected will now be listed on the main screen, ready for you to manage their individual tax rates.

> **Info** To save you time, FluentCart comes with pre-configured default tax rates for many countries. After you select a country, you will often find that the standard tax rates have already been set up for you.

#### Step 2: Manage Tax Rates for a Specific Country [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-specific-country\#step-2-manage-tax-rates-for-a-specific-country)

From the list of your configured countries, click the arrow icon for the country you wish to manage (e.g., Austria). This will take you to the detailed tax rate settings page for that country.

![Specific Country Settings](https://docs.fluentcart.com/assets/specific-country-4.CvBFk28P.png)

On this page, you can manage several key settings:

- **Tax ID** Enter your business's official **VAT ID** number for this specific country. This ID will be used on invoices and other legal documents for sales within this region. Click **Save** after entering it.
- **Regional Settings** This is where you define the primary tax rates for the selected country. You can add, edit, or delete rates as needed. To add a new rate, click the **\+ Add New Rate** button and configure the options (Tax Label, Rate, Tax Class, Compound, Priority).
- **Shipping Tax Overrides** This section allows you to set a different tax rate that applies only to shipping fees for specific provinces or states within the selected country. This is useful for regions with complex shipping tax laws.
- **Action Buttons** For every rate you create, you can use the **Edit** (pencil icon) and **Delete** (trash can icon) buttons to manage your tax rules easily.

By following this process for each country you are registered in, you can build a comprehensive and accurate tax system that is perfectly tailored to your business's specific VAT obligations.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Configuring EU VAT with the OSS Method - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss#VPContent)

# Configuring EU VAT with the OSS Method [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss\#configuring-eu-vat-with-the-oss-method)

The **One Stop Shop (OSS)** is a simplified system that allows businesses selling to multiple European Union (EU) countries to manage their VAT obligations through a single registration. If you have an OSS registration, FluentCart can automatically handle the complex task of applying the correct VAT rates for every EU country your customers purchase from.

This guide will show you how to set up and manage your OSS VAT collection in FluentCart.

### Who Should Use This Method? [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss\#who-should-use-this-method)

This method is recommended for most businesses of any size that sell to customers in multiple EU countries and have a single OSS VAT number. It streamlines your tax reporting by allowing you to file one VAT return for all your cross-border EU sales.

### How to Configure Your OSS Registration [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss\#how-to-configure-your-oss-registration)

If you have already selected **"Collect using a One Stop Shop (OSS) registration"** from the main EU VAT setup wizard, you will be prompted to enter your registration details.

- **Country of OSS registration:** From the dropdown menu, select the EU country where you are officially registered for the OSS scheme.
- **VAT number:** Enter your official OSS VAT number.

Click **Save**.

![OSS Settings](https://docs.fluentcart.com/assets/oss-settings.CFhQgXjr.png)

Once you save these settings, FluentCart takes care of the rest. It will now automatically apply the correct, up-to-date VAT rates based on each customer's country, all managed under your single OSS registration.

### Managing Your OSS Configuration [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss\#managing-your-oss-configuration)

After the initial setup, you will be taken to the main OSS management dashboard. Here, you can review your settings and make adjustments if needed.

#### Tax Overrides [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss\#tax-overrides)

FluentCart automatically uses the official standard, reduced, and zero tax rates for every country in the EU. However, in some rare situations, you may need to manually override these default rates for a specific country.

**Example Use Case:** Imagine a country announces a temporary change to its "reduced" VAT rate from 9% to 7% for a promotional period, but the official databases used for automatic updates haven't caught up yet. You can use an override to apply the correct rate immediately.

1. Click the **Add Custom Rate** button.

![OSS Settings](https://docs.fluentcart.com/assets/oss-settings-1.DI-SvGiI.png)

2. A pop-up window will appear. Select the **Country** you want to override (e.g., Bulgaria).
3. You will see the default rates for that country's tax classes (e.g., standard 20%, reduced 9%, zero 0%). You can now enter your own custom percentage for one or more of these classes.
4. Click **Save Overrides**.

The country will now appear in the **"Tax Overrides"** list at the top of the page, indicating that it is using your custom rates instead of the defaults. You can **Edit** or **Delete** this override at any time using the action icons on the right.

![OSS Settings](https://docs.fluentcart.com/assets/oss-settings-2.CAVNwfdI.png)

#### Country Rates [​](https://docs.fluentcart.com/guide/tax-&-duties/european-vat-with-oss\#country-rates)

This section provides a convenient, collapsible list of all the EU countries where you are collecting VAT. You can expand any country to view the specific standard, reduced, and zero tax rates that FluentCart is currently applying automatically. This is a great way to quickly verify the rates being used across the EU without having to look them up individually.

![OSS Settings](https://docs.fluentcart.com/assets/oss-settings-3.BPAMwvsd.png)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Tax & Duties Overview - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/tax-&-duties-overview

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/tax-&-duties-overview#VPContent)

# Tax & Duties Overview [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-&-duties-overview\#tax-duties-overview)

FluentCart’s **Tax & Duties** section is a powerful tool designed to help you manage your store’s taxes with ease and accuracy. Staying compliant with tax laws is essential for any business, and these settings give you the flexibility to handle everything from simple sales tax to complex international VAT rules.

Setting up your taxes is a straightforward, two-part process:

1. **First, you set the global rules.** On the **Configuration & Classes** page, you will decide how taxes work across your entire store. This includes setting your main calculation rules and creating different tax classes for your products (e.g., standard rate, reduced rate, or tax-exempt).
2. **Next, you set the specific rates.** On the **Rates** page, you will define the actual tax percentages for each country, state, or province you sell to.

This section contains two main guides to walk you through the entire setup:

- [**Configuring Tax Settings & Classes:**](https://docs.fluentcart.com/guide/tax-&-duties/configuration-and-classes) Learn how to set your store’s main tax rules, create tax classes for different product types, and configure EU VAT settings.
- [**Setting Up Tax Rates:**](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates) Learn how to define the specific tax rates for each region you sell to and set up advanced rules like compound taxes and shipping tax overrides.

By following these guides, you can create a flexible and automated tax system that keeps your store compliant and your checkout process seamless for customers.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Tax Filing Feature - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/tax-filing

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing#VPContent)

# Tax Filing Feature [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#tax-filing-feature)

Keeping accurate records of the taxes you've collected is essential for accounting and filing your tax returns. FluentCart's **Tax Filing** feature simplifies this process by providing a detailed log of every tax collected and a tool to mark them as "Filed" once you've reported them. It also allows you to download a CSV report for your records.

This guide will show you how to use this feature to make your tax season much easier to manage.

### Accessing the Taxes Screen [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#accessing-the-taxes-screen)

1. From your WordPress dashboard, navigate to **FluentCart Pro**.
2. Hover over the **More** menu item in the top navigation bar.
3. Click on **Taxes**.

This will take you to the main Taxes screen, where you'll see a comprehensive table of all the taxes your store has collected.

![Tax Filing](https://docs.fluentcart.com/assets/tax-filing-1.CJ0u7peS.png)

### Reviewing Your Collected Taxes [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#reviewing-your-collected-taxes)

The main screen displays a detailed, line-by-line log of every individual tax collected. This serves as your primary record when it's time to file your returns.

Here’s a breakdown of the columns:

- **Order ID:** The ID of the order the tax was applied to. You can click this ID to navigate directly to the full order details page.
- **Tax Country, Region, Zip Code:** The location details used for the tax calculation.
- **Tax Name:** The name of the specific tax rule that was applied (e.g., "State Tax," "VAT").
- **Tax Rate:** The percentage rate of the tax.
- **Sale Taxes:** The total monetary amount of tax collected for that specific order line.
- **Filed:** This is an internal marker to help you stay organized. A "No" status means the tax is still waiting to be reported. A "Yes" status means you have already included it in a tax filing.

### How to Use the Tax Filing Feature [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#how-to-use-the-tax-filing-feature)

Once you are ready to file your taxes for a specific period, you can use the Tax Filing feature to generate a report and mark the relevant taxes as "Filed."

#### Step 1: Select the Taxes to File [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#step-1-select-the-taxes-to-file)

Before clicking the main button, you must select which tax records you want to include in your filing.

1. Go through the list and check the box next to each individual tax record you want to process.
2. To make this easier, you can use the **Quick Filters** (e.g., "Not Filed") and the **Advanced Filter** to narrow down the list to a specific country, region, or date range first.

#### Step 2: Tax Filing [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#step-2-tax-filing)

Once you have selected the desired tax records, click the **Tax Filing** button at the top right of the screen.

![Tax Filing](https://docs.fluentcart.com/assets/tax-filing-2.BmvzsSWy.png)

A pop-up window will appear, showing a summary of the taxes you have selected.

#### Step 3: Review and Download [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#step-3-review-and-download)

In the pop-up, you will see:

- **Taxable Amount:** The total sum of the "Sale Taxes" for all the records you selected.
- **Total Orders:** The number of unique orders included in your selection.
- A list of the specific tax records you are about to process.

Review this information to ensure it is correct.

#### Step 4: Download & Continue [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-filing\#step-4-download-continue)

Click the **Download & Continue** button. This action performs two important tasks simultaneously:

![Tax Filing](https://docs.fluentcart.com/assets/tax-filing-3.CX9nvIYE.png)

1. It downloads a **CSV file** to your computer. This file contains a detailed breakdown of all the tax records you selected, which you can use for your accounting or to file your tax returns with the relevant authorities.
2. It marks all the selected tax records as **"Filed"** within FluentCart. Their "Filed" status will change to "Yes," so you know they have been processed.

This workflow helps you keep your financial records clean, prevents you from accidentally reporting the same taxes twice, and provides you with the necessary documentation for your tax filings.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Setting Up Tax Rates - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/tax-&-duties/tax-rates

[Skip to content](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates#VPContent)

# Setting Up Tax Rates [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#setting-up-tax-rates)

Once you have configured your main tax settings and created your tax classes, the next step is to define the specific tax rates for the regions where you sell your products. The **Rates** screen in FluentCart is where you manage these specific tax rates for different countries, states, and provinces.

## Accessing Tax Rates Settings [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#accessing-tax-rates-settings)

1. From your WordPress dashboard, navigate to **FluentCart Pro** \> **Settings**.
2. Click on the **Tax & Duties** tab from the left-hand menu.
3. Select the **Rates** sub-menu.

## Configuring Countries [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#configuring-countries)

Before you can add rates, you must specify which countries you will be collecting taxes in.

1. On the **Existing Tax Rates** screen, click the **Configure Countries** button.
2. A pop-up window will appear, listing all available countries grouped by continent. You can also select countries by clicking on the **+Add Country** button.
3. Select the checkbox next to each country where you need to apply tax rates.
4. Click **Save**. The selected countries will now appear on the main Rates screen, ready for you to add specific tax rules.

> **Info:** To save you time, FluentCart comes with pre-configured default tax rates for many countries. After you select a country, you will often find that the standard tax rates have already been set up for you. You can then edit these default rates as needed.

![Add Country](https://docs.fluentcart.com/assets/tax-rates-1.DQe9BUuE.webp)

### Managing Tax Rates for a Country [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#managing-tax-rates-for-a-country)

After adding a country, you can define the specific tax rates that apply to it.

1. From the main **Rates** screen, find the country you wish to configure and click the **View** button or the number under the **Rates** column.
2. This will take you to the tax rate management page for that specific country.

#### Tax ID [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#tax-id)

At the top of this page, you can enter your business's official **Tax ID** number for this specific country or region. This ID will be used to identify your business on invoices and other legal documents, which is often a requirement for tax compliance. Simply enter your ID and click **Save**.

#### Regional Settings [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#regional-settings)

This is where you define the primary tax rates for the selected country. You can add multiple rates to handle different tax classes or regional requirements.

To add a new rate, click the **\+ Add New Rate** button and fill in the following details:

- **Tax Label:** A descriptive name for the tax that your customers will see on their invoices (e.g., "VAT," "State Tax," "GST").
- **Rate (%):** The tax rate as a percentage (e.g., enter **20** for 20%).
- **Tax Class:** Assign this rate to one of the tax classes you created earlier (e.g., Standard, Reduced, Zero). This ensures the rate is only applied to the correct products.
- **Compound:** This is an advanced option for applying multiple taxes sequentially. If you enable this, the tax will be calculated on top of the subtotal plus any other taxes that have a lower priority.
- **Priority:** A number that determines the order in which multiple taxes are applied to a single order. Taxes with a lower priority number (e.g., 1) are applied before taxes with a higher number (e.g., 2).

![Configure Rates](https://docs.fluentcart.com/assets/tax-rates-2.DYxa8P_F.webp)

#### Understanding Compound Taxes: A Practical Example [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#understanding-compound-taxes-a-practical-example)

In some regions, you may need to apply one tax on top of another. This is called a **"compound tax."** Let's walk through a simple use case to understand how it works.

**Scenario:**

Imagine you are a Canadian store selling a product for $100. You need to apply two taxes:

- A 5% **GST** (Goods and Services Tax) which is a federal tax.
- A 7% **PST** (Provincial Sales Tax) which is a provincial tax and must be calculated _after_ the GST has been added.

**Setup in FluentCart:**

You would create two tax rates:

- **GST:** Rate 5%, Priority 1, Compound **No**.
- **PST:** Rate 7%, Priority 2, Compound **Yes**.

**How FluentCart Calculates the Total:**

1. First, it applies the Priority 1 tax (GST): $100 \* 5% = $5.00. The price including the first tax is now $105.00.
2. Next, it applies the Priority 2 tax (PST): Because PST is set to **Compound**, it is calculated on the new total from step 1: $105.00 \* 7% = $7.35.

**Final Totals:**

- **Total Tax:** $5.00 (GST) + $7.35 (PST) = **$12.35**.
- **Final Order Total:** $100 (Product) + $12.35 (Total Tax) = **$112.35**.

By setting the PST to **"Compound"** and giving it a higher priority number, you ensure the calculation is performed correctly and in the right order.

### Shipping Tax Overrides [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#shipping-tax-overrides)

In some regions, the tax rate for shipping costs may be different from the tax rate for products. This section allows you to set a specific tax rate that will apply only to the shipping fees for specific provinces or states within the selected country.

1. Click the **Add Tax Override** button.

2. A pop-up window will appear. Configure the following:


   - **Tax Label:** A clear name for the shipping tax (e.g., "Provincial Shipping Tax").
   - **Shipping Tax Rate (%):** The specific tax rate that applies only to the shipping cost.
   - **For Province:** Select the state or province where this override rule should apply.
   - **Tax Class:** Select the tax class this override should apply to. This is useful if your shipping tax also needs to follow rules for standard, reduced, or zero-rated items.

![Add Tax Override](https://docs.fluentcart.com/assets/tax-rates-3.Bxhx_eAC.webp)

This override gives you granular control to ensure maximum flexibility and accuracy, even in regions with complex shipping tax laws.

### Managing Rates with Action Buttons [​](https://docs.fluentcart.com/guide/tax-&-duties/tax-rates\#managing-rates-with-action-buttons)

For every rate you create in both the **Regional Settings** and **Shipping Tax Overrides** sections, you will see a set of action icons on the far right of the row. These allow you to easily manage your tax rules.

- **Edit (Pencil Icon):** Click this icon to open the settings for that specific rate, allowing you to make changes to the label, rate, tax class, or other options.
- **Delete (Trash Can Icon):** Click this icon to permanently remove the tax rate. A confirmation pop-up will appear to prevent accidental deletion.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
