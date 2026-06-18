# Fluent Cart in Bricks: The Good, The Bad & What's Missing

- YouTube ID : bcKAXsqo_O8
- URL : https://www.youtube.com/watch?v=bcKAXsqo_O8
- Durée : 14:47
- Chaîne : 
- Date extraction : 2026-05-19
- Mots : 3175

---

So I've seen in a couple of the Bricks groups how well can Fluent Cart actually integrate with Bricks. So that's exactly what we're going to look at in today's video. We're going to see what tools are available, some of the options today, and what I think is missing and what we need to see to make it a fully featured addition to Bricks to be able to customize our online stores. So let's jump into the dashboard and take a quick look. So by default, when you create a Fluent Cart store, and if you want to see a video on how you do this, check out the link down below and in the corner right now.

It will ask you to create various different pages, or you can already create them before you install it, and then you could reference them inside you. You could do it retrospectively as well. But as you can see, we've got a couple of pages already set up, like the shop, the account page, cart page, receipt, and checkout pages. So these are just going to use normal Gutenberg, and they're going to have this little shortcode inserted in there. We'll come back to why this important in a little bit, but let's also jump into Bricks itself and see what options are there.

So if we open up a page in Bricks, whether this is a template or an ordinary page, it doesn't matter. It's just the same options available. Unlike what you're used to with Bricks, if you go into an archive or a single template, it will give you different options. These are the options we have currently for FluentCard. As you can see, the first block of seven are all to do with the actual individual product itself.

Title, short description, price, those kinds of things. And also we've got the FluentCard for products. This is where you're going to have your typical kind of product loop. You can create your own loops, but there are a couple of limitations there, which, again, I will come on to in a moment. So let's take a quick look at the products, which is just your generic dump all the products into a particular page or template.

We'll add that into our design. There's our products, and as you can see, it now pulls in the various different products. I've just got some sample data inserted on here so you can see how it all looks. So there's our basic dump of content. Let's take a look at the options now to configure and tweak this.

As you can see on the left-hand side, we've got some pretty basic options here for, for example, the number of columns. We could say three is what we want. It will adjust accordingly. The gap, easily replace this if you want to be using a CSS framework or just get rid of the pixel values. You can absolutely do that.

So, for example, I'm using core framework here, so I may want to sort of set my using one of my variables, which, again, is something you're probably going to want to do. Your products per page, let's say you want to limit this to be six. And is this a main query? So a similar option to what you'd have if you're having sub-queries and so on. So we'll leave that as it is.

So as you can see, we have a basic page setup. We've got some pagination down the bottom. So all pretty simple and straightforward. You can set your ordering. So we can say by product name, for example, product price and so on.

Whether you want ascending or descending. So all basic things that we'd expect to see with any kind of repeating loop content. Then underneath you've got the queries, so we can apply queries to this. So if you want to create various different pages and templates and so on, have different kinds of queries, you could do that inside here. So you can see we can filter this upon the product types.

So we've got your simple, your physical variations and so on, whether there's subscriptions and things. So you can filter things down inside here. We've just basically got a product dump. But let's just say we wanted to have simple products. You can see I've already got one simple product at this point in time.

If you change that to something like variations, so it's a product with variations, you can see that pulls that up as well. Which leads me on to the first thing that I would want o see here, which is the ability to not have just a single product type. With Bricks 2.0 and beyond, we've had the ability to have multiple different parameters to apply to queries and things. I would love to see that follow over in here as well so we can choose simple products, digital products, digital subscription, for example, that are separate to physical products without having to maybe create multiple loops or, you know, you get the idea. Then if you want to, you can include or exclude specific products from here.

You can choose to specify specific categories. So you can see in this example, I've only got men's shoes, but you may have different products inside here. Again, if we choose that, you can see this now does give us the ability to have additional kinds of product categories. I'd love to see that in the variations as well so we can create more comprehensive queries. Okay, so that's basically the queries.

Then you've got the fields. Now, this is going to be very familiar to you if you're used to working with various different elements inside Bricks, and the same with lots of other tools. This shows you the sort of stack of data that's being used, the data that's being pulled in, so the image, the link, price, so on. So we can come in and edit any of these. So, for example, the price looks a bit weird there in that kind of light colour, or you could click inside here, and you can see it shows the dynamic data that's being pulled in, which again, we're using native kind of functions here.

So we can easily pull in additional data. All your data is available inside here. I'm using Advanced Themer. So yours is going to look a little different to this, but all the same options are going to be there, just listed in a kind of long list. So you can pull in additional data from here and you can see we've got products of Fluent.

So you can see we do have Fluent Cart products here. So that's quite cool to see. You can then choose the HTML tag if you want to add any sort of margins and so on. The typography settings, so we can come in. Again, we can use our variables if we want to.

So let's open this up. Let's choose a different colour from here. Make our text stand out a little bit. Want to apply some margin, for example. Well, again, we can use our variables.

So let's add a bit of space there. We'll just dump small in for now so you can see. And then, like I say, your typography is there should you want to make changes. And obviously, these are totally reorderable. You can set them however you want to.

And you can add additional fields inside here. So if we want to add more fields in, we can do just that. If you want to delete it, you can delete it. There we go. So the product loop we see here is pretty simple.

It's no real difference to what you'd have with the native post loop that you've got inside Bricks. But it's still going to be a little different to what we'd have if we want to create a custom post loop. So let's just get rid of this. Let's take a look at creating our own loop inside here and see how that works, any limitations we may have. Let's add in a block.

We'll call this product card. Okay, I'm not going to worry about applying classes and so on. We're just simply going to just style things up and see how it all works in a very basic fashion. Okay, so now let's just put in the elements we want to use. So we come back to our elements.

This is where we've got our Fluent Card product. So what we can do is we can say, let's put the product title in, product short description. Let's leave it at that for a moment. We'll come back and we'll tweak things in a moment. So now let's go up and set the product card to be a loop.

Open this up, and we'll say this is going to be posts, and the post type is going to be product. And we'll leave everything else as it is. So we've just got a really basic loop inside here. You can see this is pulling in the description. That's fine.

That's exactly what we'd expect to see. Let's come to our container, and let's set this to be a grid item. We'll pop in a little gap inside here, and we'll set this up to be three columns and etc. etc. You get the idea.

Okay so there's our basic setup. Product title, set that to be h3 for example. Go to style, typography and set our colour inside here. There we go. So that has pulled in the relevant data.

So let's go and add in the featured image now. So we'll just add an image in and we'll pop that above. So the image element added in. let's come over to our dynamic data. We'll choose our featured image.

And there's our featured image for our actual product. So you can see we don't have to rely upon the typical element that we have shipped with us for our products. We can easily create our own custom loops in, again, the same way as you'd expect o do in Bricks in any kind of post types, custom post types, normal post types, etc. Now, let's take a quick look at some of the other options that are available as our elements. Now, let's say, for example, you want to add a buy now or a buy now add to cart button like we've seen with the standard element that ships with Fluent Cart.

You'd think if we come over, for example, into our elements, then you've got the options for the product that you've already seen. So we've got the product title and so on. So you may think, well, we could use the buy section. Maybe that's actually going to pop in the sort of buy now button and so n. And you would be partially right.

So let's add that in, pop it at the bottom. And you see what this does is this pulls in the buy now and the add to cart like you would want it to do. But it also pulls in the variations and the quantity. So if we select that element and come over, you'll see that we've got the variation swatches. So we can see we can customize these, the look and so on.

But we can't actually disable them. Same thing goes for the quantity. Let's say, for example, you don't want to deal with the quantity. You can't disable it. or at least I can't see an easy way to disable it.

The direct buy button, again, those options are there, and the add to card button is there. But I can't see any way to actually remove that and just give us the buy now and the add to card buttons without any of the extra options. I would love to just see some elements inside here that is just the buy now button and the add to card button. Just as simple as that. Nothing else, nothing more.

That would be quite useful to see. So at this point in time, you're probably going to have to create a link to the product and then allow them to buy it from the product. So there's that limitation there, which I think is a bit of a shame. So this is something I would love to see updated. But at least we do have the option to be able to create our own custom loops and then do what we want to design and style those.

So that's quite cool. Okay, this time we're into the single product template. This is where you're going to use probably most of the options that are available in the elements that we have from Fluent Cart. So I'm not going to worry about styling or anything. I'm just simply going to dump the things inside just so you can see how it works Okay, so first of all, we've got things like your product title.

So let's just pop that in. Just open this out and select our container. Pop your product title in. Some reason it's coming in a little bit light, so let's just change the colour of this. There we go, so we can see it.

Your product short description. You can see that. Product content, which is basically your long description. Product stock. So if you're managing stock, which obviously, if you're using the free version of Fluent Cart, you can't have stock management, so that won't be something you could use, but it's there.

I just don't have any stock management set up for this. Then your price range, which is basically your pricing information in any kind of discount range or variations and so on. Your buy section, we've already seen that. That gives us the various different variations, the quantity options and so n. And your product gallery, which is, as its name would suggest, the product gallery.

So this will show us the primary image and then any ancillary images we have for that product. We do have a lot of options inside here. And if we come over to the settings, for example, for the buy section, we've already seen there's a ton of options inside here so you can customize how this looks and operates. You just can't choose whether you do or don't want to show those options. They're just in their carte blanche.

But like I say, I've got that wrong. Someone from WP Managed Ninja want to tell me this is how you do it, Paul. Please do. And I'll pop a comment right at the top and pin that so you can see exactly anything I might have missed or overlooked. Your price range, you can see we can hide various different options, your typography, your product stock.

Again, we can choose what we want for the in-stock text, the out-of-stock text, colours, typography, and so on. So you can customize it. Your product content, as its name would suggest, we can customize this. Your short description, again, we can customize the styling and so on. And your product gallery, you can see we can set up some other options inside there as well.

So you can tweak this. And in all honesty, there's not a massive difference to the kind of thing you can do with default kind of WooCommerce options out of the box, but it's probably going to be a little bit more. And because these are kind of native to Fluent Cart and not native to Bricks itself, there's still a little bit of work, I think, left to be done to bring this to become truly flexible for what Bricks users are probably going to expect and to be able to let them adopt this, even if it's only for simpler stores as Fluent Cart develops and expands the feature sets and things that we have available. So that's the options we have for the kind of default elements. Now let's take a quick look at something else I want to cover.

If we take a look at the pages that were created by Fluent Cart on setup, things like your cart page, checkout page, account page, and so on, they're just using a shortcode injected into a typical Gutenberg page. Nothing special, nothing going on there at all. So now if we choose to edit this with Bricks, that's basically what we're going to end up having to do. You'll see there's nothing inserted in here yet. So let's just go and add in our normal section of container.

And you'll notice if we come over to our elements, as we've already seen, we don't have any options here for the checkout, for the cart or anything like that. The only way we can actually put this into a design is by using that shortcode. So what we're going to need to do is add in an element, a shortcode element, come into our settings. And inside here, you can see there's the shortcodes we can use. So our cart page, let's click on that shortcode, head back into our builder, insert the shortcode.

And that will then show you a preview depending upon what it is you're actually pulling in. So we don't have a huge amount of control for this inside the actual builder itself. So any control you're going to have is going to be available inside the setting. So for example, your cart and checkout, you can control options inside here. Your checkout fields for your checkout page, you can see we can control the options inside here.

So again, I would love to see these same kind of options mimicked inside the Bricks editor with its own dedicated element that allows us to customize those options without having to come back out, set things up in here, go back over and have no control over things. So this is one of those areas that I think we really need to see those options being added in to Fluent Cart with Bricks in mind. So I think this is a great start from Fluent Cart. It's good to see that they've actually focused on using Bricks Builder and give us those options straight out of the box, but there are still quite a few things missing that we need to have to make it a truly viable and customizable option in Bricks itself. As always, I pass the question over to you.

Are you testing out Fluent Card? Is this something you're looking to potentially replace WooCommerce or another sort of e-commerce solution with? Let me know in the comment section down below. As always, all applicable links are in the description. My name is Paul C.

This is WPTuts and until next time, take care. Bye.
