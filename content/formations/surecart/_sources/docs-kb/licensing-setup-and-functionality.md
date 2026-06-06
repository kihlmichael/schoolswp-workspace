---
source_url: https://surecart.com/docs/licensing-setup-and-functionality
source: surecart-kb
scraped: true
---

# Understanding SureCart Licensing: Setup and Functionality

## Overview

SureCart's licensing system enables plugin and theme developers to manage product access and updates. The system uses the WordPress SDK and a release.json file to handle license activation, verification, and automatic updates.

## Key Components

### WordPress SDK

The WordPress SDK functions as a toolkit that allows plugins and themes to implement licensing by:
- Handling licensing verification (checking if users have a valid license)
- Facilitating automatic updates for licensed users
- Simplifying license activation through license codes

### Release.json File

This configuration file serves as an identity document for your plugin/theme, containing:
- Plugin/theme name and version information
- WordPress and PHP compatibility requirements
- Changelog and description sections
- Update management metadata

## Setup Process

### Creating a Simple Plugin

1. Create a PHP file with plugin header information
2. Include the WordPress SDK (see source_url for code snippet)
3. Initialize the licensing client with your plugin name and public token
4. Add settings page for license management

### Plugin Structure Requirements

Your plugin folder should contain:
- Main plugin PHP file
- wordpress-sdk folder (uncompressed from GitHub)
- release.json configuration file

### Enabling Licensing in SureCart

1. Create or edit a product in your SureCart store
2. Upload your plugin file to the Downloads section using "Secure Storage"
3. Enable the "Enable license creation" toggle
4. Set desired activation limits
5. Select the plugin file as "Current Release"
6. Save the product

## Testing and Activation

Customers can:
1. Purchase the product
2. Access their license key through the Customer Dashboard
3. Download the plugin file
4. Activate the license in their WordPress site's license settings
5. Receive automatic update notifications when new versions are available

## Plugin Updates

To release updates:
1. Increment the version number in both the plugin PHP file and release.json
2. Recompress and upload the updated plugin to your product
3. Set it as the current release
4. Customers automatically receive update notifications in their WordPress dashboard

## Merchant Visibility

Store owners can monitor license usage through the SureCart Licenses menu, viewing activation details and usage statistics for distributed licenses.
