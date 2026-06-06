---
source_url: "https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms.html"
title: "How to Collect Testimonials with Fluent Forms"
---

# How to Collect Testimonials with Fluent Forms

Using Fluent Forms, **WP Social Ninja** has introduced an incredible feature for collecting Testimonials. You must need to know how to integrate Fluent Forms with WP Social Ninja to collect testimonials using Fluent Forms on your website.

Let's look at how **WP Social Ninja** may help your business by gathering Testimonials using Fluent Forms.

## Enable the Fluent Forms Integration Module [​](https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms#enable-the-fluent-forms-integration-module)

First, go to **Integrations** from the **Fluent Forms** Navbar. Search for **WP Social Ninja** through the search bar or scroll down to find the **WP Social Ninja** module from the list. Then, **Toggle** the switch to **Enable the module**.

This action connects Fluent Forms with WP Social Ninja, allowing them to share data.

![enable testinmonial template](https://docs.wpsocialninja.com/assets/enable-wp-social-ninja-in-fluentforms.D7IgjKuB.webp)

### Create Your Testimonial Collection Form [​](https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms#create-your-testimonial-collection-form)

Next, you need to configure the specific form you want to use for collecting reviews.

Go to your Fluent Forms dashboard. You can either **Add a New Form** or **edit an existing one**. Ensure your form contains all the fields you want to collect.

Recommended fields include:

*   **Author Name** (Text Field)
*   **Author URL** (URL Field)
*   **Author Image** (File Upload Field)
*   **Author Company Name** (Text Field)
*   **Title** (Text Field)
*   **Testimonial Text** (Text Area Field)
*   **Ratings** (Ratings Field)

![form 2](https://docs.wpsocialninja.com/assets/Form-2.B9qkFy9c.webp)

### Configure the WP Social Ninja Integration Feed [​](https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms#configure-the-wp-social-ninja-integration-feed)

Once your form is ready, go to the **Settings & Integrations** section, navigate to the **Configuration Integrations** tab. Click the **Add New Integration** button, and select the **WP Social Ninja Integration** feed from the dropdown list.

![add new integration 03](https://docs.wpsocialninja.com/assets/add-new-integration.BcfgFXj5.webp)

After you select the WP Social Ninja integration, a configuration panel will appear. Then, you will find the configuration panel where you must map your form fields to the corresponding testimonial fields in WP Social Ninja.

Here is a breakdown of the fields you need to configure:

*   **Name:** Enter a name for this specific integration feed.
*   **Switch to Testimonial Mode:** Select **Yes** from the dropdown. This is crucial for mapping testimonial-specific fields like Author Position and Company.
*   **Ratings (Required):** Map this to the Ratings field on your form.
*   **Author Name (Required):** Map this to the name field on your form.
*   **Comment (Required):** Map this to the text area field where users write their testimonial.
*   **Title, Author Email, Author Image, etc.:** Map the remaining fields (like Author Position, Company, Website URL) to their corresponding fields on your form.
*   **Conditional Logic:** You can enable this to set rules for submissions. For example, you can set a rule to only accept submissions with a 4-star rating or higher.

After mapping the fields, click the **Save Feed** button. Your integration is now active and will appear in the list, where you can edit or delete it later.

![add new wp social ninja integration feed fluent forms 04](https://docs.wpsocialninja.com/assets/configure-wp-social-ninja-integration-feed.DUtMtKYa.webp)

The form has been integrated successfully. You can modify or remove the feed by selecting the **Settings** or **Delete** icon. After that, you can **copy** the Form's **shortcode** and paste it into any **page/post**.

![form integration successful ](https://docs.wpsocialninja.com/assets/settings.CwyCENZJ.webp)

### Add a Custom Testimonial [​](https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms#add-a-custom-testimonial)

First, go to your WP Social Ninja dashboard. From the top menu bar, click on the **Testimonials** tab. This will take you to the "All Testimonials" page. To add a new entry, click the **Add Testimonial** button located in the top-right corner. Learn more about [adding testimonials](https://docs.wpsocialninja.com/guide/advanced-features/add-testimonials).

![add custom testimonial ](https://docs.wpsocialninja.com/assets/add-testimonial.BGpXZME3.webp)

### Enter the Testimonial Details [​](https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms#enter-the-testimonial-details)

After clicking the button, a pop-up form will appear. Here, you can fill in all the details for the testimonial. Once you have entered all the information, click the **Save Testimonial** button at the bottom of the form to add it to your collection. After saving, your new testimonial will appear in the "**All Testimonials**" list.

![add testimonial ](https://docs.wpsocialninja.com/assets/enter-testimonial-details.DMAvfeVt.webp)

### Display Your Testimonials on Your Website [​](https://docs.wpsocialninja.com/guide/advanced-features/collect-testimonials-fluent-forms#display-your-testimonials-on-your-website)

Finally, to display the testimonials collected through your form, you need to create a [template](https://docs.wpsocialninja.com/guide/getting-started/templates-overview) in WP Social Ninja. Copy the template's [shortcode](https://docs.wpsocialninja.com/guide/integrations/shortcode-usage) and paste it onto any page or post where you want your testimonials to appear.

*   Go to your **WP Social Ninja dashboard → Templates**.
    
*   Click the **Add New Template** button and select **Add Testimonial Template**.
    
*   Customize the layout and style of your template in the editor. The testimonials submitted through Fluent Forms will automatically be pulled into this template.
    

![add new testimonial 08](https://docs.wpsocialninja.com/assets/add-testimonial-template-2.BKQ3sjhm.webp)

After clicking on the **Add Testimonial Template**, let’s look at how it looks on the frontend.

![Displaying Collection of Testimonial](https://docs.wpsocialninja.com/assets/WP-Social-Ninja-Edit-Review-Template-3-1.CWFVfz0R.png)

Collecting Testimonials in Fluent Forms is as simple as a slice of pie!

You can also check out - **[How to Add Fluent Forms Reviews with WP Social Ninja](https://docs.wpsocialninja.com/guide/business-reviews/fluent-forms-review)** here.
