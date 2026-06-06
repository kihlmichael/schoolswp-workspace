---
source_url: https://surecart.com/docs/bullet-points-not-showing-divi
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Fixing Bullet Point Issue With Divi Theme And SureCart

# Fixing Bullet Point Issue With Divi Theme And SureCart

When using the Divi theme with SureCart, some users may encounter an issue where bullet points are not displayed properly. Instead, no marker may be shown.

This can make your content look messy and unprofessional.

Fortunately, this issue can be fixed by adding this custom CSS snippet in your **Additional CSS** settings.

```css
sc-prose ul {
  list-style: initial;
  margin-left: 14px;
}
```

### How To Solve The Bullet Point Issue In Divi

- Navigate to **Appearance** > **Customize** from your WordPress dashboard.

- Click on **Additional CSS** at the bottom of the menu.

- Add the mentioned code here and click on the **Publish** button:

```css
sc-prose ul {
  list-style: initial;
  margin-left: 14px;
}
```

- Check your checkout page; now it will work as expected.

Your bullet point display issue with the Divi Theme and SureCart should now be resolved.

Hope this solution helped. If you are still facing this issue, please reach out to our support team. We're always here to help!
