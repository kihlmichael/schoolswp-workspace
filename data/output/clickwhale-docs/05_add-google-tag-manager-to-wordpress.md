# How-To Add Google Tag Manager To WordPress with ClickWhale

> Source: https://clickwhale.pro/docs/article/add-google-tag-manager-to-wordpress/
> Updated on July 15, 2024

Tracking customer behavior and having the right data are vital for your website's success.

This is because being able to access accurate data will let you **see what your customers do on your website, what they like, and what you should change** to maximize conversions and improve the user experience.

**[Google Tag Manager](https://tagmanager.google.com/)** is one of **the best tools to get this data, offering several benefits:**

- **User behavior tracking.** Track clicks on specific buttons, form submissions, and video views.
- **Event tracking.** Track downloads, scroll depth, and other specific user interactions.
- **Ecommerce tracking.** Monitor product views, cart additions, and purchases.

In this post, you'll discover everything about adding Google Tag Manager to your WordPress website with ClickWhale. By using ClickWhale you can **skip the long and complicated process of adding it directly to your site's code.**

## What Is Google Tag Manager?

Google Tag Manager is a free tool that **enables you to install, store, and manage tags** -- small snippets of code that track user actions and collect data.

The most common tag you will almost certainly have previously encountered is the one used to install Google Analytics.

Other popular examples include **Google Ads conversion scripts, Meta Pixel code, and remarketing tags.** You need to place such tags in your website code for Google Analytics and other platforms to function and collect data.

## How to Install Google Tag Manager With ClickWhale

The problem with the usual approach to **installing GTM is that it's complicated and requires some technical knowledge.**

This is because you need to **access your website's code and add it there directly.**

If you aren't a very technical person, this might present a great challenge. It also **increases the risk of code not working properly** (if you fail to put it into the right place).

**The ClickWhale approach eliminates all of these issues.**

You don't need to access your site's code, nor have any technical knowledge. You just **add the Google Tag Manager to our platform, and we will do everything for you!**

_Let's now look at the step-by-step process of what to do to add Google Tag Manager to your WordPress site with ClickWhale._

### #1: Install ClickWhale

**Head over to your [WordPress Plugin](https://ppopotamus-haka.instawp.xyz/wp-admin/plugin-install.php?s=clickwhale&tab=search&type=term) menu or [https://clickwhale.pro/](https://clickwhale.pro/)**, download and install the ClickWhale plugin, and then activate it.

### #2: Create a New Google Tag Manager Account / Log In

The next step is to set up your Google Tag Manager account. **Head over to the [Tag Manager website](https://tagmanager.google.com/#/home) and click on the 'Create Account' button.**

You will then need to **fill in your Account Name, Country, Container Name** (the name of your website inside GTM), and **target platform**.

Hit '**Create**', agree with the terms and conditions, and then click the '**Yes**' button.

### #3: Get Your GTM Codes

After you finish creating your account, you will see **a pop-up for installing Google Tag Manager on your website.**

In case you inadvertently close this pop-up, you can always just **head over to Admin and select 'Install Google Tag Manager'.**

We're going to paste this code directly into ClickWhale in order to add Google Tag Manager and its functionality to your site.

### #4: Add Google Tag Manager Into ClickWhale

Head over to your site's WordPress menu, select **ClickWhale**, go to the **'Tracking Codes'**, and click on the **'Add New'** button.

You will now need to fill in the following fields:

- **The title.** The name of the tracking code inside ClickWhale.
- **Code.** The actual code you will paste from Google Tag Manager.
- **Code position.** Where you want to add the code.
- **The pages.** Which pages to add the code to.
- **User roles.** The user roles for which the script should **not** be executed _(you don't want to track behaviors of the website's admins or you)_.

Let's now quickly go over how to fill these fields in.

#### Creating The Title

**The title of this tracking code should be 'Google Tag Manager'.**

#### Adding The Code

Now it's time to paste the code from your GTM account.

Head over to your Google Tag Manager page, **copy the first code**, and **paste it into the 'code' section inside the ClickWhale plugin**.

You will now need to **select the position of your code** -- which should be **'Before </head>'**.

#### Selecting Pages And User Roles

After that, you will need to **select which pages should run GTM, and which user roles' behaviors** you're looking NOT to track.

To select specific pages, **select the 'Specific Page' option, and then add pages into the section 'Include Pages':**

_(If you're looking to run GTM on your whole site, select the '**Whole website**' option.)_

You can also **select the user roles you want to exclude from tracking.** As we said earlier, this can be particularly useful to avoid tracking your own behavior, or the behavior of the site's admins and content creators.

The last step is to **check the 'Enable Tracking Code' and hit 'Save'.**

### #5: Adding the "Second Code"

It's also vital to **add the second code from Google Tag Manager to your website.**

You might notice that even though you haven't added it yet, your GTM still works. However, there are a few rare instances where JavaScript isn't working. **If you don't add the second code to your website, GTM won't work in such instances.**

To add the second code, follow the same process as we did in the previous step. **The only thing that is different is the position of your code.**

You want to **add this code into the 'After <body>' portion of the code.**

The rest should be kept the same.

## That's It!

You have now successfully added Google Tag Manager to your website.

There are a lot of behaviors you can track with GTM. However, if you're looking for just basic click tracking, then there may be no need to install Google Tag Manager at all, since **ClickWhale lets you track your clicks on any links on your website.**

Here are a few **additional resources you might find super helpful.**

- [ClickWhale Analytics Data: How to Use It To Make A Profit](https://clickwhale.pro/blog/clickwhale-analytics-data-how-to-use-it-to-make-a-profit/)
- [Why You Might Need a Bio Link Page on Your WordPress Website?](https://clickwhale.pro/blog/bio-link-page-for-wordpress-for-free/)
- [5 Reasons Why You Need to be Using ClickWhale](https://clickwhale.pro/blog/5-reasons-why-you-need-to-be-using-clickwhale/)

If you have any questions or need anything, you can always **reach us [at our website](https://clickwhale.pro/contact/), where we are always happy to help!**
