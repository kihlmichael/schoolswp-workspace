---
source_url: https://surecart.com/docs/add-custom-css
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Developer Docs](https://surecart.com/docs-category/developer-docs/)/How to Add Custom CSS to Checkout Forms

# How to Add Custom CSS to Checkout Forms

It is a common practice to modify specific parts of a website using custom CSS during the website building process. There are a number of reasons why you might want to add custom CSS to your website:

- To match the overall design of your website or storefront.
- To customize an element that can't be customized without CSS.
- Or to simply change the font color or typography on a specific area of your website.

Integrating custom CSS into your SureCart checkout forms allows you to provide a better user experience and maintain branding consistency on your website. This results in a more professional and user-friendly experience.

This documentation provides a step-by-step guide on adding custom CSS to SureCart checkout forms, including various examples to make this process more understandable.

### **What Is a Shadow DOM?**

Before we learn how to add CSS to checkout forms, we should know how SureCart uses CSS.

SureCart uses a Shadow DOM to load the CSS. It is a way to encapsulate CSS and HTML in a separate tree from the main document. This method provides a few advantages:

- **Style protection**: Styles are protected from any potential style conflicts with theme or plugin styles.
- **Future-proofing**: If the internal HTML structure of any components changes, you won't need to update any custom CSS.

In the case of SureCart checkout forms, the shadow DOM is used to isolate the checkout form styles from the rest of your website's styles.

This means that you can add custom CSS to the checkout form without having to worry about conflicting with other styles on your website.

To add custom CSS to SureCart checkout forms, we will use CSS custom properties, also known as CSS variables.

### **How to Add CSS**

To work well with CSS customization, it's important to know about two important things: [dev tools](https://developer.chrome.com/docs/devtools/) and [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php).

If you're not familiar with them, you can find helpful explanations and tutorials on various websites. It's worth checking them to get a better understanding.

Making a CSS modification consists of 3 steps.

1\. **Getting the CSS selector** – when customizing elements with a normal CSS customization you need to find a selector and add styles. In most cases it is enough to get the ID or class of the HTML element.

When using the Shadow DOM method, we must locate a CSS variable of the element.

Shadow Dom doesn't use a selector, it has only one selector, and it looks like this:

```
:root:root {

}
```

In this simple CSS code, we will add CSS variables with customized values.

2\. **Generating CSS code** – In a normal CSS customization we need a CSS selector and rules of styles, at the end your CSS code will look like this:

```
.selector {
  Color: red;
  Font-family: Noto Sans;
}
```

We have a different approach in the Shadow DOM method, we need to get CSS variables and modify them, for example if we want to change the font size, then this will be our css:

```
:root:root {
  --sc-input-label-font-size-medium: 25px;
}
```

This means in the Shadow Dom method we only need to get CSS variable since the selector is always the same.

You can refer to this [Custom CSS](https://developer.surecart.com/docs/styling-ui) article for more information on variables. This doc page contains a list of all the variables used in SureCart and their default values.

3\. **Adding the code** – This is the easiest part, we need to save our code in the appropriate place to apply changes. By default in WordPress we save CSS customizations in Appearance > Customize > Additional CSS.

By following these 3 steps, we can modify not only the checkout form but also the shop page, product page, and Customer Dashboard page. This method of CSS modification applies to all of them.

### **Examples**

So far, we have covered the theory of CSS customization. Now, let's get practical and strengthen our knowledge through several examples of CSS customization.

In the examples below, we will follow these steps, we will identify a CSS variable, then create a code, and lastly, we will add it to the CSS box.

#### **Typography**

In this example let's discuss how can we change the typography on the checkout form with custom css.

Here is our CSS that will change font family, font size, and font weight.

```
:root:root {
  --sc-font-sans: fuggles;
  --sc-font-size-medium: 25px;
  --sc-font-weight-normal: 600;
}
```

For better presentation, we are loading Google Fonts with this css code:

```
@import url('https://fonts.googleapis.com/css2?family=Inconsolata:wght@600&display=swap');
```

#### **Change border-radius**

Now, let's imagine we want to change the border radius and border color of the input fields on the checkout page.

```
:root:root {
  --sc-border-radius-medium: 30px;
  --sc-input-border-color: red;
  --sc-select-border-color:red;
}
```

###### Note:

With SureCart v3, we have fully adapted with WordPress' Interactivity API. Meaning we no longer use ShadowDOM on most SureCart pages and sections, except the Checkout Forms and Pages.

These pages still use ShadowDOM.

Please refer to our [**upgrade guide**](https://surecart.com/docs/upgrading-to-surecart-v3/) to learn more about SureCart v3.

And that's the end!

Don't worry if it looked a bit complicated at first. In reality, it's often easier than the usual CSS approach. All you really need to do is to get CSS variables to change default values.

I hope this guide has made it clear how to add your own custom styles to your checkout forms. With this knowledge, you can make your SureCart checkout pages look and style just the way you want them to.
