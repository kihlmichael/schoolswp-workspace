---
source_url: https://surecart.com/docs/customize-email-templates
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Email](https://surecart.com/docs-category/email/)/How to Customize Email Templates

# How to Customize Email Templates

SureCart allows you to personalize emails for your customers. You can adjust notification settings, edit content, and add a personal touch to the subject and body.

To customize any email that SureCart sends to customers, please follow the steps below:

### Choosing the Email to Edit

Navigate to SureCart **Settings** > **Notifications**.

You can see the name of the email, the description, and a button to edit. Click on the **Edit** button to customize it.

For example, here we are editing the email message which is sent to customers upon subscription cancellation.

### Overview of Email Editing

Upon clicking on the Edit button, you will be redirected to the [SureCart platform](http://app.surecart.com/) where you will find more of these email templates under the **Email > Customer Emails** section.

You can easily change the Email Subject. The Email Body might look a little daunting for some users but fear not, we are going to make it easy for you.

The **Liquid Variables** are the ones that allow us to output data for this specific template. Most of the work will be in the Email Body, so let's break it down.

### Editing Email Subject

Edit the Email Subject text to your liking. You can use the same example below for testing purposes.

Notice that we used a Liquid Variable called {{ subscription.name }}. We will cover that later.

### Previewing Email to See Changes

Click on the **Save** button to save your changes. You can preview the email by clicking on the **Preview Email** button.

You can see that your new Email Subject has been updated, and the Liquid Variable has been successfully replaced by the Product Name.

If you wish, you can send a test email by clicking on the **Send Test Email** button.

If you make a mistake, you can always revert to the default template by clicking on the **Revert to Default** button.

### Editing Email Body

Let's now change the h3 heading. Replace the text on line 2 from "**Your subscription was canceled**" to "**Your subscription just ended. Please renew!**".

Once you finish your customization, Click on the **Save** button, and then click on the **Preview Email** button to see a preview.

### Liquid Variables

Liquid variables, like {{ subscription.name }}, insert dynamic content in the email templates.

For example, here's how the Liquid Variables for this **Order Confirmation** email template are displayed:

```
   "store": {
    "brand": {
      "address": "Logoipsum\n2200 Tinker Loop\nAlamogordo New York 88310\nUnited States of America",
      "email": "suport@storename.com",
      "logo_url": "https://media.surecart.com/4zqjol8ny24sf7zibtkbop7vqmqw",
      "phone": "(575) 479-4701",
      "website": "https://storename.com"
    },
    "name": "Store Name",
    "url": "https://storename.com"
  }
```

Here is how we extract it to be used as a variable in our email body.

- `{{ store.brand.address }}`: This variable will output the store's brand address.
- `{{ store.brand.email }}`: This variable will output the store's brand email address.
- `{{ store.brand.logo_url }}`: This variable will output the store's brand logo URL.
- `{{ store.brand.phone }}`: This variable will output the store's brand phone number.
- `{{ store.brand.website }}`: This variable will output the store's brand website.
- `{{ store.name }}`: This variable will output the store's name.
- `{{ store.url }}`: This variable will output the store's URL.

You can follow the same idea to extract the variable and modify your email to best suit your company's needs.

### Filters

Let's see just a few filters that will help you personalize your email templates.

#### Capitalize Letters

Suppose the customer typed their name all in small caps, like "**adrian l. derossett**" and you want the email to capitalize. So here's how you can do it in the email body:

```
{{ "adrian l. derosset" | capitalize }}
```

The result will be: "**Adrian L. Derosset**".

#### Prepend and Append

Going one step further we can also append or prepend some text to it, see an example here of prepend:

```
{{ "adrian l. derosset" | capitalize | prepend: "Hello " }}
```

The result will be: "**Hello** **Adrian L.** **Derosset**".

#### Splitting the Name

Now, suppose you want only the first name – some people have big names, and it would be odd to add to an email a big name. So one way you can accomplish it is this:

```
{{ "adrian l. derossett" | split: " " | first | capitalize | prepend: "Hello "}}
```

The result will be: "**Hello Adrian**".

#### Finding More Filters

We covered just a few filters, but you can see all filters available [here](https://shopify.github.io/liquid/basics/introduction/).

That's it with this guide. If you have any more questions or come across any issues, please feel free to reach out to our support team. We're always here to help!
