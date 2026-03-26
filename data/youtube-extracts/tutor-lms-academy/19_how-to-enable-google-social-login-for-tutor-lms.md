# How To Enable Google Social Login For Tutor LMS

## Metadonnees

| Champ | Valeur |
|-------|--------|
| URL | https://www.youtube.com/watch?v=mbZhH-wgayA |
| Chaine | Tutor LMS |
| Vues | 10 097 |
| Likes | 89 |
| Date | 2023-06-13 |
| Duree | 4:03 |

## Description

This tutorial is all about how you can get the Google Social Login key for Tutor LMS social login feature.

## Transcript

foreign [Music] LMS Academy today we'll go over how you can get the Google social login key for tutor LMS social login feature so without further Ado let's get right to it so here we are at the Google developer console dashboard so to start off we first need to create a project if you've seen our Google meet or Google Classroom integration videos this process will be very familiar to you anyways so let's go ahead and click on create a project we create the project select a name and set up organization names too if you're connected with an organization once we've created the project moving on we need to click on apis and services and then we need to go to the oauth constant screen here we need to select the user type and we're going to set it to external and hit create on the next screen we have to fill up some information so go ahead and set an app name select the user support email developer email and so on after you're done hit save and continue then we come to the scope screen now we need to add two scopes for this setup click on add or remove Scopes and select the first two check boxes the user info dot email and the userinfo.profilescopes so make sure that you've ticked the check boxes beside the email and the profile scope after choosing all the Scopes scroll down hit update and then save and continue on the following screen you can add users who can test your app remember this will only work when the app is in the testing phase in this tutorial though we will not be keeping the app in the testing phase rather we're going to publish the app at the end of the setup which we'll get to in a bit anyways hit save and continue and we're done with the initial setup check the summary see if all your information is good and click on back to dashboard before we go go to the next step as we've said we're going to publish this app so just hit the publish app button confirm and your app will be now published now it's time to create your oauth client ID to do so select the credentials tab from this left bar and click on create credentials from the drop down select oauth client ID and now let's set this up so first we have to enter our application type we're going to select web application and then we can set a name for our app and we can add a URI for the JavaScript Origins and the most important part we need to add an authorized redirect URI click the add URI button and the URI that we need to add here we can quickly get from the tutor LMS settings tab so here we are at the tutor LMS settings tab from here we need to click on authentication make sure that Google login is enabled and click this button to copy the redirect URL that we need to paste back into the Google developer console so we had copied the redirect URL which we're going to paste here and just clicking create will finish this process for us once we've created the oauth client ID you'll see that your client ID has been generated just copy this and we need to go back to tutor LMS and paste this so back in the authentication tab of tutor LMS in this text box we're going to paste the client ID that we've just copied and hit save changes and that's it Google social login is now activated for your e-learning site thanks for tuning in we hope you found this tutorial on obtaining a Google social login key useful be sure to stay tuned for more tutorials on tutor LMS if you have any suggestions for future videos please let us know in the comments we're always working on new tutorials so please stay tuned for more great content please
