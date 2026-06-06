---
source_url: https://surecart.com/docs/how-to-remove-surecart-user-roles
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Remove SureCart User Roles

# How to Remove SureCart User Roles

SureCart adds four user roles after installation, which are SureCart Customer, SureCart Shop Manager, SureCart Shop Accountant, and SureCart Shop Worker. If you would like to remove any of these user roles, you can simply follow the steps mentioned in this article. Let's get started.

In order to remove the default SureCart roles, you can either use a plugin called [User Role Editor](https://wordpress.org/plugins/user-role-editor/) or a custom code. For more information on how this plugin works, please visit the documentation page of the plugin from [here](http://shinephp.com/user-role-editor-wordpress-plugin/).

To use a custom code on your website, we highly recommend using a child theme. If you are not familiar with the child theme, here is an [article](https://wpastra.com/guides-and-tutorials/wordpress-create-child-theme/) that will guide you through the process.

**Step 1:** Navigate to the WordPress dashboard and click on Appearance > Theme File Editor

**Step 2**: Choose the child theme from the drop-down in the top-right corner and click on the select button to get it selected.

**Step 3**: Once the child theme is selected, click on the function.php file to add the custom code.

**Step 4**: Scroll down to the bottom of the page, copy the below code, and paste it at the bottom of the existing code. If you'd like to remove only one or some of them, you can remove the line that represents the user role you'd like to keep. For example, if you would like to keep the SureCart shop manager role, please remove the line of code that says "remove_role( 'sc_shop_manager');.

```
function wps_remove_role() {
remove_role( 'sc_customer' );
remove_role( 'sc_shop_manager' );
remove_role( 'sc_shop_accountant' );
remove_role( 'sc_shop_worker' );
}
add_action( 'init', 'wps_remove_role' );
```

**Step 5:** Click on the update button at the bottom and this code will remove the SureCart user roles from your website. You can remove the code once the user roles are removed later.

In conclusion, removing SureCart user roles from your WordPress website is a straightforward process that can be done through either a plugin or custom code. By following the steps outlined in this article, you can remove the default SureCart roles, including SureCart Customer, SureCart Shop Manager, SureCart Shop Accountant, and SureCart Shop Worker.

Alternatively, you can also run this code using a custom code plugin such as [Code Snippet](https://wordpress.org/plugins/code-snippets/).

Note: We strongly recommend that you take a backup of your site before editing the code of your website.
