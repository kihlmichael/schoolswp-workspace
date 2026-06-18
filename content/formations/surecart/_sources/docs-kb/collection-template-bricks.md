---
source_url: https://surecart.com/docs/collection-template-bricks
source: surecart-kb
scraped: true
---

# How to Create the Collection Template in Bricks Builder

This guide will cover the key steps for setting up a collection template in Bricks Builder with SureCart's integration.

Using this integration, you can easily customize and design e-commerce collection pages by taking advantage of SureCart's dynamic elements within Bricks.

### **Creating SureCart Collection Archive Template**

To apply a consistent layout to all your collections pages in Bricks, you need to create a SureCart Collection Archive Template.

To create the SureCart Collection Archive template, follow these steps:

- Go to **Bricks > Templates**.
- Click the **Add New** button.
- Give the template a name; in this case, "Collections Template".
- In the **Template type** dropdown, select **SureCart – Collection Archive**.
- Click the **Publish** button.
- Then click the **Edit with Bricks** button to start designing your template.

- Search for "section" in the elements panel.
- Click on the **Section** element to add it to the canvas.
- Click on the **Container** in the Structure panel on the right.
- Click on the **Elements** button to add a SureCart Element to the container.
- In the **Container**, select the **Grid** option in the **Display** setting.
- In the **Grid Template Columns**, type repeat(4, 1fr) to create 4 columns.
- Add the **Post Title** element.

- Add a **DIV** element inside the container and click to select it.
- Click to add another element and search for "product".
- Click on **Product Card** to add it to the **DIV**.
- Click on the parent **DIV** again.
- Now, enable the **Query Loop** option.
- With the **Query Loop** enabled, click on the infinity button to set the loop.
- In the **Post Type**, select **SureCart Product**.

Now, you just need to save your template and complete one final step to apply the Bricks layout to your collection.

- Go to **Products > Collections** menu.
- Select the collection where you want to apply the Bricks template and click **Edit**.
- In the **Template** section, click on the **Default** dropdown menu.
- Under **Page Layout**, click the dropdown and select **SureCart Layout**.
- Click the **Save Collection** button to save the changes.

That's it! Your collections will now use the Bricks template you've customized.

### **FAQ**

**Can I create a different layout for each collection?**

Yes, you can. To do this, you'll need to add template conditions. Open the collection template, click the gear icon for settings, go to **Template Settings**, then **Conditions**. Add a condition, select **Terms**, and choose the term(s) you want this template to apply to.
