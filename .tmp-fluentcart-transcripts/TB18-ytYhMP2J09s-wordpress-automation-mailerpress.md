# Genius WordPress Automation (FluentCart + MailerPress)

- YouTube ID : ytYhMP2J09s
- URL : https://www.youtube.com/watch?v=ytYhMP2J09s
- Durée : 20:02
- Chaîne : 
- Date extraction : 2026-05-19
- Mots : 4247

---

Today we're going to dig back into a little bit of automation and see how we can actually connect multiple different plugins together to create a seamless and quite powerful workflow. This is just a simple example, but it shows you the kind of things that you can do and what you can achieve to connect up various different WordPress tools. In this example, we're going to be using the new MailerPress, which has recently been released. Details down, if you want to check the video out on that and a link by here. And also we're going to connect this up to the free version of Fluent Cart.

So when someone purchases a product, we want to do something. And in this example, we're going to be using Flowmattic to handle that. There are other tools that allow you to do a lot of this kind of thing. You could look at BitFlows, for example. That is a very similar setup and supports the same tools we're going to cover here.

But let's take a look at what we're going to create, and then we'll go through and create it. So this is our workflow. It looks pretty simple, but it does a lot of cool things. First of all, it checks to see if a new order is being created, and that's the trigger. So when someone purchases something inside Fluent Cart, that will trigger this particular set of actions.

The next one then is just going to add and create a new contact inside MailerPress. Currently, at the time of releasing this, we don't have any automations in MailerPress. So this is a really cool way of being able to integrate those automations and connecting the tools up to this new platform. Once that's been done, if we open this up, you can see it does things like adds them to a particular list, their subscription status, and so on. Then we've got a branch.

Now, a branch is really, really useful. What this is going to do is it's going to check a parameter that we set up, which I'll show you as we go through this. If that parameter is true, it'll follow the yes section. If it's not true, it will follow the no section. In this example, no just basically stops.

But the yes will add a different tag in. It will create a coupon, a unique coupon inside Fluent Cart. and send an email out that includes that free coupon details. So there's a lot going on here. Let's go and create it.

I can show you step by step how it all works. To start off with, I've created a blank workflow in Flowmattic. So let's give this a name. We're going to call this VIP discount. Then we've got the trigger.

Now, if you're new to working with automations in any kind of tool like this, whether it's Flowmattic, Bitflows, or something like Zapier or Pably Connect, they all work in exactly the same way. You've got triggers, and you've got actions. In this example, we want the trigger, a new order, to sort of fire off a series of different actions. First of all, let's change this from Webhook by Flowmattics. We'll click on it, and now we can change this.

So I've installed a couple of integrations as part of Flowmattic. I've got Fluent Cart, Fluent Forms, and MailerPress. Fluent Forms, I'm just testing something out there. We only need Fluent Cart and MailerPress. And these are all part of Flowmattic.

You're just basically saying, what do we want to integrate with within Flowmattic itself? So you can add as many or as few as you need to connect things up. So the first thing you want to do is choose a fluent cart. So now we're going to say, what is the trigger event? Well, it's placing a new order.

So we open this up. You can see there's an awful lot of different triggers that we can use here. So we can set up multiple different kinds of triggers and actions and so on to do all manner of different things. You could create one very complicated workflow, but it's much better to have multiple workflows that are simpler. It just means that then if you want a fault find, you don't have tons and tons of steps to go through and look for the problem.

You have a much simpler, smaller set of actions. So for this example, it's a new order. Let's just choose order. And we say order created. So that is the first part.

That's our trigger. So the next thing to do is go to continue. That takes us over to the configure option. There's nothing to configure in this particular step. So we'll click continue one more time.

And now we've got to test our trigger out. And this is one of those areas that a lot of people get confused here is what do you actually need to do? Well, as its name suggests, we've got to capture a response. We've got to place an order. In this case, it's just a fictitious order.

And that will then capture that information from that order. And we can use that as sample data to test everything out from this point on. So we'll say capture response. That's going to now start listening for a response. So we'll head over into our shop.

And what we're going to do is we're going to add an option in. So let's go to this particular product, say buy now, and we'll just basically purchase the product. So we're going to say place an order. If we go back into Flowmattic, you'll see there's our response, and you can have multiple responses if you want to tie this again and again and again. But we've got this response, and if we open this up, this will show us a lot of information of what it's captured during that test transaction.

So for example, the status, the fulfillment type, the payment option, the mode, those kinds of things. So all this data is available to us to be able to do things with. In this example, we just want to keep this super simple. We've captured that. The order's been created.

We need to do nothing more with it. We're going to close that. I want to say continue. So then you've got the option for working with conditions. In this example, we don't need to worry about conditions, but we will take a look at those soon.

We'll say save and close, and that's our trigger setup. So our trigger now is set so when a new order comes in, it captures the data, and now we can move on to the actions. So the first action we want to do is add this user or update them if they've purchased before inside MailerPress. So we're going to click on the plus, and we're going to choose MailerPress from our list. We're now going to move on to our first action, which is to add or update a user in MailerPress.

So MailerPress is elected as our app. Let's choose the action or event. And again, you can see there's an awful lot of options here. But the difference now is that this is an action. So a trigger, in this case, a new order, is triggering the actions.

All it does is it trigger the next step, whereas an action does something. So in other words, it adds a new user, updates details, adds a tag to them or something. It's an actual physical action being taken place. So what we're going to do is we want o create or update a contact. We'll choose the option from the list and click continue.

And now we've got to configure things. Now, if you're new to this, basically what we're doing is we're grabbing that data that we captured inside the trigger stage. So things like the name, the email, the order status and those kinds of things. And we can now map those to this particular action. Hope this is making sense.

So the contact email. Let's click on the plus. We'll choose our order created trigger. And there's all our data. So now we can scroll through until we find exactly what we're looking for.

which in this example is the customer email. Choose that from our list, and now that's grabbed the data, the tag to actually map that data. So whenever a new order is placed, the email address that's used will be passed over to the action from MailerPress, and therefore that will be the email used to either add a new user into the database or to update one that already exists. So then we can do the same thing again. So the first name, click, choose the order created, which is our trigger, that's holding our data.

Scroll down until we find the name. We'll grab that and the last name. Now I didn't put any real details inside here so it's just going to pull in username and so on for this test site so don't worry too much about that. But it will be replaced by the real data when people actually place physical orders. Choose the last name.

There we go. Then the subscription status so we can choose what we want. Subscribed, unsubscribed or pending. It's up to you. In this example I'm going to leave it as subscribed but you do what is relevant o you.

Generally pending is probably going to be the one you want to choose to get them to confirm and they're happy to be subscribed. Add to lists. Now, the list is inside MailerPress. I only have one list inside here. So what we're going to do is we're going to open up the MailerPress lists.

You'll see that new entry is added inside here. Open this up, and there's my list. Choose it from our list, pardon, list pun. And there we go. Then we're going to say add tags.

Now, tags are used inside MailerPress or any kind of email marketing platform to segment your lists. So, for example, you have one list that has everybody in it, And then you use tags to have things like VIPs, customers, those kinds of things, anything you want in it, students, whatever it is, anything to segment your actual list. Keeps everything nice and neat and tidy, just having a single list with all of your subscribers in, and then you use tags to segment it. So in this example, we're going to click to add the plus, Mailer Press Tags this time, and we're going to say this is a customer because they've just bought something. Opt-in source, we're going to leave as Flowmattic.

That's fine. Click Continue. Now we can see we've got the conditions inside here. Ignore errors and skip execution. We're going to leave those as they are.

And I continue to the test phase. So now you can see this is what it's waiting for. So this is the kind of placeholder data. Let's click test action. And that's going to grab the data from our initial trigger from that sample data we used.

And it's going to pull that through in here and test everything to make sure it works. So we'll click test action. And there you go. There's all the data. So the email, you can see it's pulled my email in, the first name, the last name, subscription status, etc., etc.

So that stage is all working. No errors or anything. So we know that works okay. Save and close. So now, quick recap.

We've set the trigger up that says when someone places a new order, the first action is that we want to add them into our subscriber list, give them a tag of customer, and then move on. So next stage. Now, if you're enjoying this video and learning more about working with automations in WordPress, why not go down and hit that thumbs up button down below to tell YouTube you like it. While you're down there, why not hit the subscribe button as well. But if you're not getting value for this video, well, you can hit the thumbs down button twice as that seems to work pretty well too.

Anyway, let's get back on with automating WordPress. Okay, so this is where the fun starts. This is where we set up our condition. So we're going to click the plus and this time we're going to use an option from the Flowmattic built-in tools. For this, we're going to use a branch.

And you see that branch breaks off now into a yes and no statement. So what we need to do for our branch is actually tell it what sets this to be true. In other words, yes. So you can see the action will automatically execute the path yes if the conditions are met and no if the conditions are not met. So what condition do we need to do?

For this, we want to check how many orders have been placed in FluentCart by this particular customer. Choose our field. We're going to click the plus. We're going to come over to the order created. And inside here, we want to grab how many orders they've placed.

To do that, we want to grab the purchase count. So what we're going to do is we're going to click the top. We're going to type in purchase. Open this back up. And you can see inside here, we've got various different purchase ones.

So customer purchase count. That's what we're looking for. We're going to choose that option from the list of options available. And that's going to check to see how many orders that particular customer has placed. Now we can say the condition we want to use.

So we open this up, you can see there's a ton of different conditions inside here that we can actually use. This is where branches are incredibly powerful. You can check things like for containing text, does not contain, exactly matches text, is in, is not in, starts with. So you can check things like dates, amounts, all those kinds of good things. What we want, though, is to simply say greater than.

Click on that. And what number do we want? Two. So if they've placed more than two orders, then they're going to have something happen. So in other words, if they've placed more than two orders, this will be a yes.

The condition will be true. They will then go into the yes section, and anything we place in situ will be carried out, any actions we have. If we wanted to have it set up with a no, then we could just set up any actions we want in situ. We're just going to let it end there, though. So now we say continue.

You can test your action. And as you can see, it comes back and says condition met false, path to execute no. because they currently have no orders. So they're not going to be marked as a yes in this example. So again, everything is working, save and close.

So now we've got our branch set up to test how many orders they've placed. Now we can jump into the yes section and apply what's going to happen. This is again where the fun really starts. First thing we want to do is apply another tag to them. So they're going to say as a customer, that doesn't change.

But we're going to come in and click the plus. We're going to choose MailerPress. And from there, we're going to choose the option to add a tag. So we can say add tag to contact. Click on this.

Click continue. Contact email, like we've done before. We're going to open this up. Choose the order created. We're going to grab the email address from here because it's the same email.

All that data should be the same throughout. There's our customer email. There we go, the tag. What tag do we want to apply to them? Now, you can apply multiple tags if you want to here, but we just want one.

So we're going to click on the plus. There's our MailerPress tags again. and we're going to set them to be a VIP customer. They're going to be very important if they've made two or more orders. It's a simple example, but you get the idea.

Click on continue. Again, you can set up any conditions inside you, check for errors and so on. Click continue. And we say test action. There we go.

That's tested everything out. So it's pulled in the first name, email. So all that data is still available to us. We'll say save and close. So now if they have made two orders, they're tagged as a VIP.

So what do we want to do? we want to send them an email that gives them a unique discount code for one time. And we're going to set up the values inside there. And we want to create that unique code because the last thing we want is to have the same code that once someone gets it, they can share it with 100 other people and suddenly we're losing a chunk of cash. We don't want that.

So what we're going to do is we're going to come up to add another action inside here. Because the code needs to be in Fluent Cart, we're going to use the Fluent Cart integration. And again, like we've done before, action event. I'm going to click, search for coupon, and we'll say create a coupon. Okay, click continue.

So now we've got to fill out the relevant data. So the first thing we've got to, what we're going to give us is a coupon title. This is a title inside Fluent Cart that's just for our internal records. So we're going to say VIP discount. Then you've got the code.

Now obviously we don't want to put, like I say, a hard-coded code inside here. So we need to grab or create some dynamic data. Thankfully, Flowmattic has a really useful little option. Click on the plus. Again, this gives us all the data we can access.

And we can come into Flowmattic variables. If we scroll through here, you'll see at the end you've got random string 10. This is 10 characters in a random string. We're going to use that. I'm going to click on it.

So that will generate a random string of characters and create that unique code inside FluentCars. So discount settings. Now we can configure this. We're going to say this is a percentage. We're going to say 20% is the discount.

Then you can choose the status visibility. So we can say it's active, show a checkout. Is it stackable? No. Priority.

Do you want to set a schedule date? So you may say you've got to use this in the next seven days or something. You could set dates inside you. We're going to leave it as it is. Max uses, we want them to be using it one time.

It's a special deal. Max per customer, one time. And purchase conditions. So you can set up any conditions inside you. Like apply to the whole cart, for example.

Yes. apply to quantity, etc, etc. It's not too much of a problem. We're just doing this as a sample. Obviously, you've spent a little bit more time going through here and making sure that this matches exactly what you want for the kind of upsell VIP discount you want to apply on, whatever it is.

We're going to say we're going to continue this, but you can limit it to the specific categories and so on. We say continue. We're not going to set any conditions on here. Click on test. So we'll say test action.

You can see there's our discount code. It's unique. If we say test action a second, time, it's a different discount code. A third time, a different discount code. So you can see these discount codes are being generated for us.

So we say save and close. So the final step now is we need to send an email out that contains the actual code to our new VIP user. Now obviously you could do this in multiple different ways, but we're going to keep this inside Flowmattic because it keeps it all self-contained. So we're going to say add step. We're going to say we want to send an email out.

So we're going to choose the option for email. I don't have any email services set up on here, so this isn't going to work correctly for me. But obviously you'd set this up to send it via either email through Flowmattic, or you can change this and use various different email options inside you. So we're going to leave that as it is. The action event.

So we say send email. You could use a template if you wanted to, which you can create inside Flowmattic as well. But it's just a simple thank you email with details of the discount code. Choose that from our list and click continue. So your email provider, inside here, you can see we've got the WordPress default, which is your standard kind of PHP mail.

You can set your Flowmattic defaults if you want to set up Flowmattic to have its own SMTP details, you can do. Or you could use custom SMTP details from here. I'm going to leave as the WordPress default because we're just testing this stage out. So from name, from email, the email address, reply to email address. Well, we can copy that and do the same thing inside there if we want to.

The to email address, obviously we need to grab that and send it to the person that's actually made this purchase. So again, we'll click on the plus. We're going to come to the order created. We're going to come down for their email address. Choose that from our list.

No worry about CCs and so on. And we're going to say, hey, we're going to grab some dynamic data from here. So again, like we've done before, we'll grab the order created, grab their first name or a VIP. Cool. Then you've got your email body.

So this is our email body. But obviously, we need to be able to grab that particular unique code. So what we're going to do is we're going to do the add symbol. as soon as we do that we now have all these options available now we could grab the variable from Flowmattic variables but that may change so what we're going to do is we're going to come into Flowmattic create coupon grab the code so there's our code so now we can say so that will now send this email out with that unique code being added in there and set up automatically for us we can make that bold so it stands out. And we say continue.

Again, you've got your execution options here if you want to. Click continue. We can say test action. We're going to get an error because I don't have any email services set up on here. But obviously, you would on yours.

Everything will work correctly. Save and close. And now we're going to save that workflow. So, because we've run a couple of tests on here, if we jump over now into Fluent Cart, you can see there's all the discount codes we've set up. All the 20% discounts.

If we come and open one to edit it. You can see there's the code. There's the title. There's the percentage, 20%. Maximum uses total.

So all the options are here, all configured directly inside Flowmattic, but transitioned over now into Fluent Card. So you can see how we can grab all this different data from a simple trigger, like placing an order, going through and checking all these different parameters out, adding people into MailerPress, sending emails out, setting branches up to check conditions, generating unique codes, adding those into FluentCart, then sending that email out with the code included in the email. Now, obviously, we could go so much further here. What I would also do after this I would create another workflow to remove that code, check if it's being used. If it's being used, remove it completely.

So that way you don't end up with undreds and hundreds of codes that are no longer any use, and it'll remove those once they've been used. There's so many different ways in which you can use these automations to be able to streamline what you can do inside your online store, your email marketing, WordPress website in general. This is just a simple, maybe not a simple example, but an example of some of the things that you could do just by using native functions inside a tool like Flowmattic. As always, all applicable links are in the description. My name is Paul C.

This is WPTuts. And until next time, take care.
