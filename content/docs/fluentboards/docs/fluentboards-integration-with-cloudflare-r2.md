---
source_url: https://fluentboards.com/docs/fluentboards-integration-with-cloudflare-r2/
title: 'FluentBoards Integration with CloudFlare R2'
scraped_at: 2026-04-21
---

# FluentBoards Integration with CloudFlare R2

Table of Contents 
  * Get your CloudFlare Account ID
  * Create a Cloudflare R2 Bucket
  * Get the Cloudflare Bucket Public URL
  * Generate your Access Key & Secret Key
  * Configure the FluentBoards with Cloudflare R2
  * Additional Configuration (Optional)
    * Troubleshooting

FluentBoards integrates with Cloudflare R2, helps you to store your media files and manage storage more efficiently right from your WordPress site.
In this guide, we’ll walk you through everything you need to do. You’ll learn how to create and configure an R2 bucket, generate API tokens, and set up the plugin settings inside your WordPress site.
Follow these simple step by step process to connect Cloudflare R2 with your FluentBoards.
## Get your CloudFlare Account ID #
First, log in to your [CloudFlare Account](<https://dash.cloudflare.com/login>). Navigate to **Storage & Databases** > **R2 Object Storage** > **Overview**. On the right side of the page, you will find the **Account Details** section. Your **Account ID** is displayed here. Click the **copy icon** next to the ID to save it for later use.
![copy account id](https://fluentboards.com/wp-content/uploads/2024/09/copy-account-id-1-scaled.webp)
Alternatively, you can find your **Account ID** in the **URL** of your Cloudflare account, as shown in the screenshot below. You can also copy your Account ID from here.
![alternative account 0id 2](https://fluentboards.com/wp-content/uploads/2024/09/alternative-account-0id-2-scaled.webp)
## Create a Cloudflare R2 Bucket #
Navigate to **R2 Object Storage** from the left sidebar, find Overview under **R2 Object Storage** , and click on it. Now, click on the **Create Bucket** button to create a bucket. 
![create bucket 3](https://fluentboards.com/wp-content/uploads/2024/09/create-bucket-3-scaled.webp)
Enter a **Bucket name** that is easy to identify and unique across your projects. Leave the **Location** of the bucket as **the default** unless you have specific storage.
After that, click the **Create Bucket** button.
![create bucket 4](https://fluentboards.com/wp-content/uploads/2024/09/create-bucket-4-scaled.webp)
## Get the Cloudflare Bucket Public URL #
You can now see the Bucket Details. Scroll down to the **Public Development URL** section. Here, you need to enable access to this public URL.
Click the **Enable** link to open a pop-up. Type “allow” in the field to grant access to the **Public Development URL.**
![public development url 5](https://fluentboards.com/wp-content/uploads/2024/09/public-development-url-5-scaled.webp)
A pop-up will appear to **Enable Public Development URL**. Type in ‘allow’ to confirm. Then, press the **Allow** button.
![allow 6](https://fluentboards.com/wp-content/uploads/2024/09/allow-6.webp)
Here, you will get the **Cloudflare Bucket Public URL**.
![copy public url 7](https://fluentboards.com/wp-content/uploads/2024/09/copy-public-url-7-scaled.webp)
## Generate your Access Key & Secret Key #
To create a Cloudflare Access Key, go back to the **R2 Object Storage > Overview** page. In the **Account Details** box on the right, click the **{} Manage** button next to **API Tokens**.
![manage 8](https://fluentboards.com/wp-content/uploads/2024/09/manage-8-scaled.webp)
On the next page, click the **Create API token** button.
![create account api 9](https://fluentboards.com/wp-content/uploads/2024/09/create-account-api-9.webp)
Now, configure your token with the following settings:
  1. **Token Name:** Give your token a descriptive name.
  2. **Permissions:** Select **Object Read & Write**.
  3. **Bucket:** Choose the specific bucket you created from the dropdown menu.

Next, click the **Create Account API token** button at the bottom.
![create token 10](https://fluentboards.com/wp-content/uploads/2024/09/create-token-10-scaled.webp)
Here, you will find the **Access Key ID** and **Secret Access Key**. Make sure to **copy** them immediately, as you won’t be able to revisit this page later.
![access key and secrete key 11](https://fluentboards.com/wp-content/uploads/2024/09/access-key-and-secrete-key-11-scaled.webp)
## Configure the FluentBoards with Cloudflare R2 #
Now access FluentBoards and go to **Settings > Features & Modules**. Here you will see the **Media Storage** section then click on the **Settings** button.
![configure cloudflare r2 12](https://fluentboards.com/wp-content/uploads/2024/09/configure-cloudflare-R2-12-scaled.webp)
A pop-up will appear. Now, select **Cloudflare R2** and enter the credentials you collected from your Cloudflare account in the earlier steps of this guide.
**Cloudflare Account ID:** Input your CloudFlare Account ID.
**Cloudflare Access Key:** Paste the Access Key you received from your Cloudflare API token.
**Cloudflare Secret Key:** Enter the Secret Key from your Cloudflare API token.
**Cloudflare Bucket Name:** Enter the name of the R2 bucket you created.
**Cloudflare Bucket Public URL:** Provide the Public R2.dev Bucket URL.
**Bucket Sub-Folder (Optional):** If you created a subfolder for file uploads, provide its name. Otherwise, leave it empty.
After you’ve completed all the fields, simply click the **Save Settings** button to store your Cloudflare configuration.
![cloudflare r2 13](https://fluentboards.com/wp-content/uploads/2024/09/cloudflare-R2-13-scaled.webp)
## Additional Configuration (Optional) #
If you want to advanced setups, you can define your Cloudflare R2 settings in your**wp-config.php** file. This method provides an extra layer of security and is useful for managing configurations across different environments.
    
    // CloudFlare R2 Configuration
    
    define('FLUENT_BOARDS_CLOUD_STORAGE', 'cloudflare_r2');
    
    define('FLUENT_BOARDS_CLOUD_STORAGE_ACCOUNT_ID', 'ACCOUNT_ID'); // like: 1718cb5a51e65c8f19e8sahdakh763
    
    define('FLUENT_BOARDS_CLOUD_STORAGE_ACCESS_KEY', 'ACCESS_KEY_HERE');
    
    define('FLUENT_BOARDS_CLOUD_STORAGE_SECRET_KEY', 'SECRET_KEY_HERE');
    
    define('FLUENT_BOARDS_CLOUD_STORAGE_BUCKET', 'BUCKET_NAME');
    
    define('FLUENT_BOARDS_CLOUD_STORAGE_PUBLIC_URL', 'https://pub-SOME_RANDOM_STRINGS.r2.dev'); // You can use the r2 custom domain too
    
    define('FLUENT_BOARDS_CLOUD_STORAGE_SUB_FOLDER', 'my-folder-name'); // optional
If defined in `wp-config.php`, these values will override any settings in the plugin’s configuration form.
### Troubleshooting #
  * Ensure that your API token has the correct permissions for R2 access.
  * Double-check that the bucket name and public URL are correct.
  * If using a custom domain, make sure it’s properly configured in CloudFlare.

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [support team](<https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/>). Thank you.
