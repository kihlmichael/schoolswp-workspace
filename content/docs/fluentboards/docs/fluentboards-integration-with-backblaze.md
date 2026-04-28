---
source_url: https://fluentboards.com/docs/fluentboards-integration-with-backblaze/
title: 'FluentBoards Integration with Backblaze'
scraped_at: 2026-04-21
---

# FluentBoards Integration with Backblaze

Table of Contents 
  * Backblaze Settings 
  * Get Backblaze Creadentials 
  * Configure Backblaze in your FluentBoards

Backblaze is a cloud storage solution designed for media hosting, data backups, and building applications using S3-compatible APIs. It offers a secure and convenient way to store and access your data, making backup management seamless.
By integrating FluentBoards with Backblaze B2 Cloud Storage, you can directly interact with your cloud storage and efficiently store your attached data. 
In this article, we’ll guide you through the process of integrating your FluentBoards with Backblaze B2 Cloud Storage. 
## Backblaze Settings #
To connect your **FluentBoards** with Backblaze, go to the **Settings** section of FluentBoards. Then, click on the **Features and Addons** tab from the left sidebar. Here, you’ll find the **Media Storage** option click on the **Settings** button next to it.
![fluentboards digitalocean settings 1 1 1](https://fluentboards.com/wp-content/uploads/2025/01/FluentBoards-DigitalOcean-Settings-1-1-1-scaled.webp)
A pop-up will appear. From here, select **Storage Location: Backblaze B2** from the dropdown menu. You’ll now need some credentials to connect with Backblaze.
Let’s get started with collecting the required credentials.
![fluentboards backblaze settings 1 ](https://fluentboards.com/wp-content/uploads/2025/01/FluentBoards-Backblaze-Settings-1--scaled.webp)
## **Get Backblaze Creadentials** #
Log in to your [Backblaze account](<https://secure.backblaze.com/user_signin.htm>). Once you’re in, you’ll need to create a **Bucket** to upload and save your files. Go to the **Buckets** section from the left-hand sidebar and click on the **Create New Bucket** button.
![backblaze 1](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-1-scaled.webp)
After clicking the **Create New Bucket** button, a pop-up window will appear where you can configure your bucket settings. Enter a **Bucket Name** that reflects its purpose (e.g., “FluentBoardsData”). 
You must have to set the **Files in Bucket** option to **Public**. This ensures that files stored in the bucket are accessible as needed. 
Once configured, click the **Create a Bucket** button to finalize the setup.
![backblaze 2](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-2-scaled.webp)
Now you will see that your bucket has been created, and some credentials of your bucket will be displayed. 
From here, you need to copy the **Endpoint** , which is one of the necessary credentials. Make sure to copy the Endpoint and save it for later use.
![backblaze 3](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-3-scaled.webp)
Select the **Application Keys** from the left sidebar and then you will see a button **Add a New Application Key** , click on it.
![backblaze 4](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-4-scaled.webp)
A pop-up will arrive to give the details about the **Application Key**. Here, first, you need to give the **Key Name** in the dedicated key name field. Then select the **Bucket** that you have created earlier.
After that, in the **Type of Access** , select **Read and Write** and then click on the **Create New Key** button.
![backblaze 5](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-5-scaled.webp)
Now you will see that your **Key ID** and **Application Key** will be given here. 
> Note that this pop-up will appear only once. So make sure to copy the credentials as soon as the pop-up arrives.
![backblaze 6](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-6-scaled.webp)
## Configure Backblaze in your FluentBoards #
Now, paste the credentials into the **FluentBoards Backblaze Configuration** section. When you enter the **Endpoint** of Backblaze, you’ll see that the **Region** and **Bucket Name** fields are automatically populated based on the Endpoint details.
![backblaze 8](https://fluentboards.com/wp-content/uploads/2025/01/Backblaze-8.png)
That’s it! Your FluentBoards is now integrated with Backblaze cloud storage, and all your attachments will be uploaded to the Backblaze cloud server. If you have any queries, suggestions, or questions regarding this article, please feel free to [contact us](<https://wpmanageninja.com/support-tickets/>).
