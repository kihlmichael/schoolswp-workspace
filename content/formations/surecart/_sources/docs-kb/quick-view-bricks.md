---
source_url: https://surecart.com/docs/quick-view-bricks
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/How to Create a Quick View in Bricks Builder

# How to Create a Quick View in Bricks Builder

In this guide, we will explore how to create a quick view effect for SureCart in Bricks Builder without the need for any external plugins, leveraging only Bricks and SureCart's native elements.

Let's get started.

### **Create the Pop-Up Template**

The first element we need to design is the pop-up itself because it needs to be selected within the page where we want the quick view effect. So, let's create our pop-up in Bricks Builder.

- Go to the **Bricks** menu, then select **Templates**, and click the **Add New Template** button.

- Give your template a name (1), such as "Quick View."
- Select the template type as **Popup** (2).
- Click the **Publish** button to save your changes.
- Finally, click the **Edit with Bricks** button (3) to start customizing the template.

- Click on the **plus (+) icon** to add a new section to your design.

- Add the **Product Form** element (1).
- Click on the **Save** button (2) to save your changes.
- Exit the pop-up editing page.

- Add the **Template** element to the page where you want the pop-up to open. The specific location of this element on the page is not important.

- After adding the **Template** element, click on it to open its settings and select the **Quick View** pop-up template you created earlier.

### **Triggering the Popup Template**

To display the popup template, we will use Bricks' native Interactions. To learn more about Bricks Interactions, check out this [documentation](https://academy.bricksbuilder.io/article/interactions/).

- On the element that you want to function as a button to open the popup (in this example, we used a text link), go to the **Interactions** tab (1) and configure the following settings (2):
  - **Trigger**: Click
  - **Action**: Show element
  - **Target**: Popup
  - **Popup**: Select "Quick View" (or the name you assigned).

- Save the page and preview it on the frontend.

That's it!

You can now enhance your popup by adding a close button and styling it to your preference.
