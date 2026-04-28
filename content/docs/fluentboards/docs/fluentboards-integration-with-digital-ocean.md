---
source_url: https://fluentboards.com/docs/fluentboards-integration-with-digital-ocean/
title: 'FluentBoards Integration with DigitalOcean'
scraped_at: 2026-04-21
---

# FluentBoards Integration with DigitalOcean

Table of Contents 
  * DigitalOcean Settings 
  * Get Credentials from DigitalOceans 
  * Configure Digital Ocean in your FluentBoards

DigitalOcean is a reliable cloud storage solution perfect for hosting media, managing backups, and building applications with its scalable and secure infrastructure.
Integrating FluentBoards with DigitalOcean Spaces allows you to directly connect with your cloud storage, enabling seamless data management and efficient file storage for your projects.
In this article, we will guide you through the step-by-step process of connecting your FluentBoards with DigitalOcean.
## DigitalOcean Settings #
To connect your **FluentBoards** with DigitalOcean, go to the **Settings** section of FluentBoards. Then, click on the **Features and Addons** tab from the left sidebar. Here, you’ll find the **Media Storage** option click on the **Settings** button next to it.
![media storage settings](https://fluentboards.com/wp-content/uploads/2025/01/Media-Storage-settings-scaled.webp)
A pop-up will appear. From here, select **Storage Location: DigitalOcean Space** from the dropdown menu. You’ll now need some credentials to connect with DigitalOcean.
Let’s get started with collecting the required credentials.
![fluentboards digitalocean settings 2](https://fluentboards.com/wp-content/uploads/2025/01/FluentBoards-DigitalOcean-Settings-2-scaled.webp)
## Get Credentials from DigitalOceans #
First, log in to the [Digital Oceans account](<https://cloud.digitalocean.com/login>) and then click on the **Create** drop-down**** button. Then select **Space Object Storage from here to** create a space bucket for storing your data. 
![digitalocean 1](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-1-scaled.webp)
Now you will be redirected to the Space Bucket creating page where you have to give the information for your Bucket. 
From here first **Choose a Data Center Region** from the dropdown menu and select your suitable data region from the available regions. 
Then you have to give a unique **Space Bucket Name** to identify your bucket. Now select the Project from here. 
Lastly, click on the **Create a Space Bucket** button to create a Bucket. 
![digitalocean 2](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-2-scaled.webp)
Now you will be redirected to a page where you will see the **Origin Endpoint**. Copy the Endpoint from here and save it for later use.
![digitalocean 3](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-3-scaled.webp)
Next, go to the **Settings** tab. Here, you need to create an **Access Key**. Click on the **Create Access Key** button to proceed to the next step.
![digitalocean 4](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-4-scaled.webp)
A pop-up will appear after clicking on the button and here you will see the settings for your Access Key. Now select **Read/Write/Delete (Objects)** from here. After that select the Bucket for which you want to create this **Access Key**. 
Giving the Name of the Access Key is optional you can give the name as you want or you can keep the name as it is. Click on the **Create Access Key** button now. 
![digitalocean 5](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-5-scaled.webp)
Now your **Access Key ID** and **Secret Key** will be displayed. **Copy** them from here and save them securely for later use.
![digitalocean 6](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-6-scaled.webp)
## Configure Digital Ocean in your FluentBoards #
Now paste the credentials into the dedicated fields of your **FluentBoards**. When you enter the **Endpoint** , you’ll notice that the **Storage Bucket Name** and **Region** are automatically filled in.
The **Bucket Subfolder** field is optional—you can add a subfolder if needed. Finally, click the **Save Settings** button to successfully add your DigitalOcean bucket as the cloud storage for your FluentBoards.
![digitalocean 7](https://fluentboards.com/wp-content/uploads/2025/01/DigitalOcean-7-scaled.webp)
If you have any further queries regarding this article, please feel free to [contact us](<https://wpmanageninja.com/support-tickets/>).
