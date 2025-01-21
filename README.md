# Gamedream - A portfolio project.

Welcome to my code institute website readme. This is for my milestone 4 project. For this I have decided to create a website for a anonymous clients textile business revolving around the sale of her textile art and cards alongside various kits used to create them. I have done this by creating a django framework powered by a sqlite database and the web application stripe designed to provide secure payments. This was done because the project goal was to create an effective ecommerce website.

!["The first thing users see when loading the site"](read_me/home_page.png)

[Click here to access the live website]()

## Table of Contents

1. [Planning & Development](#planning--development)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Languages](#languages)
6. [Media Queries](#media-queries)
7. [Software](#software)
8. [Code](#code)
9. [Credits](#credits)

# Planning & Development #

### Business Strategy

The concept behind this product was to try and emulate what it would be like to be a freelance web developer. To do this I worked with a client who asked me to make for her a website built for the sale of textile art sold as either cards or framed pieces. I accepted this offer because it felt like a website project with alot of wiggle room to then add my own personal flair to.

### Target Audience

For this project I opted to not do my own research and instead decided to ask the client what their target audience was at a planned interview. When I interviewed the client about their target market and inqured into who she was planning to sell these products to, she gave me the following response. She told me the target audience for her work was anyone above the age of 10 with an interest in Embroidery and textile art. After travelling with the client to a christmas market where similar businesses to hers operated, I noticed the customers there were as she described; They were of all ages and clearly displaying an interest in handmade crafts.

### User Stories

!["The user stories for my project"](read_me/user_stories.png)

The above image displays the user stories that I will be using for my project.

### Wireframe

These are the wireframes I created to help me plan out the design of my website. The designs were not final but there were a massive help in creating the project.

Home Screen
![This was the wireframe for my Home Screen page](read_me/wireframes/home_screen.png)
Product Selector
![This was the wireframe for my Product Selector page](read_me/wireframes/product_selector.png)
Product Details
![This was the wireframe for my Product Details page](read_me/wireframes/product_details.png)
Shopping bag
![This was the wireframe for my Shopping bag page](read_me/wireframes/shopping_bag.png)
Billing details
![This was the wireframe for my Billing details page](read_me/wireframes/checkout.png)
Order Details
![This was the wireframe for my Order Details page](read_me/wireframes/order_details.png)
Account Creation
![This was the wireframe for my Account Creation page](read_me/wireframes/account_creation.png)
Login
![This was the wireframe for my Login page](read_me/wireframes/login.png)
User Profile
![This was the wireframe for my User Profile page](read_me/wireframes/user_profile.png)
Contact
![This was the wireframe for my Contact page](read_me/wireframes/contact.png)
Newsletter confirmation
![This was the wireframe for my Newsletter confirmation page](read_me/wireframes/wishlist_confirmation.png)



### Color Scheme

![This was the palette I chose to use for my site.](read_me/color_palette.png)

The above color scheme was rather simple to create. My mother had suggested using 3 colors initially(Dun, Nyanza Green and Non-Photo Blue). Using those as a base, I then utilized 

### Typography

![This was the font I chose to use for my site.](read_me/typography.png)

When picking out an appropriate font for the website I wanted to avoid something like new times roman while also ensuring that it was still clear and easily read on smaller phone devices. To achieve that middle ground I settled upon using Overpass for my font of choice.

### Database

The below database models shows the relationships between all of the models in my database and their relationships. The database features for handling account logins are handled by allauth rather than my own personal code.

#### Order

|Key|Value Type|Description|
|:----|:----|:----|
|Order Number|Character|Used to track the unique order number for a customer’s transaction|
|User Profile|Foreign Key|Links the specific order to the account that created it.|
|Full Name|Character|The user’s full name.|
|Email|Character|The users email to track receipts.|
|Phone Number|Character|The users phone number.|
|Postcode|Character|The user’s postcode used for deliveries|
|Town/City|Character|The user’s Town or City used for deliveries|
|Street Address 1|Character|The first half of the user’s street address used for deliveries|
|Street Address 2|Character|The second half of the user’s street address used for deliveries|
|Date|Date|The date when the users order took place|
|Delivery Cost|Decimal|The delivery fee on the order based on distance from the seller.|
|Order Total|Decimal|The total amount of all the ordered products added together.|
|Grand Total|Decimal|The combined amount of the Order Total and Delivery Cost Keys.|
|Original Bag|Text|Remembers the original bag used before payment transaction.|
|Stripe PID|Character|The Stripe PaymentIntent used for the API that handles credit card payments.|

#### OrderLineItem

|Key|Value Type|Description|
|:----|:----|:----|
|Order|Foreign Key|The order associated with the line item.|
|Product|Foreign Key|The item from the shopping bag.|
|Quantity|Integer|The amount of said shopping bag item.|
|Line-Item Total|Decimal|The price of the product times the quantity of said product.|

#### ArtCollection

|Key|Value Type|Description|
|:----|:----|:----|
|Name|Character|The name of the category for backend purposes|
|Friendly Name|Character|The name of the category for frontend purposes|

#### Product

|Key|Value Type|Description|
|:----|:----|:----|
|Art Collection|Foreign Key|The category the product belongs to.|
|SKU|Character|The unique identifier number for the product|
|Name|Character|The product name|
|Description|Text|The product description|
|Price|Decimal|How much the product costs.|
|Upvotes|Integer|How many likes a product has|
|Downvotes|Integer|How many dislikes the product has|
|Image URL|URL|The URL storing the image.|
|Image|Image|The field displaying the image itself in HTML|

#### Profile

|Key|Value Type|Description|
|:----|:----|:----|
|User|One To One|Interacts with the User model in Django.allauth|
|Default Phone Number|Character|The users default phone number.|
|Default Postcode|Character|The user’s default postcode used for deliveries|
|Default Town/City|Character|The user’s default Town or City used for deliveries|
|Default Street Address 1|Character|The first half of the user’s default street address used for deliveries|
|Default Street Address 2|Character|The second half of the user’s default street address used for deliveries|

#### Contact

|Key|Value Type|Description|
|:----|:----|:----|
|Subject|Character|The subject of the contact email|
|Body|Text|The main body of the contact email|
|Email|Email|The users email to use when sending their email to the server|

#### Testimonies

|Key|Value Type|Description|
|:----|:----|:----|
|Creator|Foreign Key|A foreign key with the user at the time of creating the testimony|
|Name|Character|The name of the testimony creator|
|Date|Date|The date when the testimony was created|
|Body|Text|The main body of the testimony|
|Rating|Character|A rating for what the user thought about the website from 1 to 5|

# Features #

# Testing #

## Page Testing

### General

The general design of my website was inspired by the need for it to look both eye catching yet easy to read and understand. To facilitate this, a universal feature on the website is that all buttons are either large or distinctly colored. In additon to this, all important bodies of text were surrounded in a clear border to draw view attention to them first before any other on screen elements.

### Home page

!["The home page for my website"](read_me/home_page.png)

When a user first logs onto my website, the first thing that they will be met with is this screen showing the home page. It has a distinct header and a distinct footer. The header contains important links to the rest of the website chiefly among them being the links to the products page and the shopping bag. Other important links are the link back to the home page that can be used anywhere on the site, the contact and testimonial links that take users to the means to both speak directly to the store owners and leave reviews on the website respectively. The light mode button was originally meant to be used for a light and dark mode option, however due to time constraints this feature will be implemented at a later date. The header also contains dropdowns that allows users to search for products based on various factors and the specific art collection they're looking for. In the center of the page is a link informing the user that a new art collection has been added to the store, clicking it will send them to the product page to view the available items. In the footer are links to various social medias associated with the store owner, currently the link will just send users to the homepage of each site, but in the live version for the client it will link to their business social medias. While there were several issues with css initially, most noteably with a gap on the side of the web page, this was corrected by ensuring that the entireity of the header element was wrapped in a fluid container.

### Profile

!["The profile page for my website"](read_me/features/profile.png)

As the pages for login, logout and account creation are handled by allauth, I will only be speaking about the profile page in this readme. The profile page has two unique functions. One of which is to store the order history of the client so that they can check and remember what products they have brought and in what quantities. Clicking the respective order number with send the user to a seperate page showing the full details of that specific order. The other important feature of the page is to allow the logged in user to submit their delivery details here so that they can be used when they check out in future. The development of this app was a fairly smooth experience without much in the way of struggle.

### Contact

!["The contact page for my website"](read_me/features/contact.png)

The contact page was created with the purpose of allowing users to email the business owner with any of their inquiries. The ones signposted on the page are out of stock paintings and international delivery. (Limited stock will be implemented in a later version of the site.) The app works by assigning a database to the form to hold the email, subject and body of the desired email the user wishes to send. Upon hitting the "Submit Enquiry" button, the email will be sent out to the site owner, with the user email already assigned to it to allow for communication. Developing this app required me to understand the email receipt system present in the checkout app so that I could reincorporate it into the contact app, everything was form management I had learned from all the other apps on the site.

### Testimonials

!["The testimonials page for my website"](read_me/features/testimonials.png)

The testimonials page is the sites answer to how a user might leave a review on the site as a whole. While originally meant to be specifically product reviews, testimonials were decided upon instead due to certain time constraints. The testimonials page shows all testimonials within a box, allowing the user to scroll to find specific testimonials and preventing it from spilling far down the page. Each testimonial also generates with it's own specific edit and delete buttons that offer it full crud functionality. The form for creating these testimonials are made up of the users name, the rating out of 5 they would give the website website as well as the testimony body itself. Hitting the create testimony button will then post the testimony to the database to be displayed on the main app page. The edit button works the same only it takes the testimony id of the selected testimony and uses it to display that information already in the form via an instance. Coding in that feature took a while since I had forgotten to trigger that even in the GET method of my view rather than try and squeeze it into the post function. The delete button works by simply finding and deleting the testimony id associated with the button.

### Products

!["The Products page for my website"](read_me/features/products.png)

The products page is where all the available products on the site are displayed to the user. The individual products are displayed to the user in seperate cards which contain both the item price, the item name and the image of the item itself. Items are arranged 4 on a row which shrinks down the smaller the screen size gets to ensure proper responsiveness on mobile devices. At the top of the container there are a set of buttons. One takes the user back to the home page and the other allows the user to search for products by a variety of criteria.
When creating the product app, my primary goal was to read clearly to the user due to the desired target audience of my anonymous client. To do that I left the work fairly uncustomized, only really changing things to give the individual icons more space. This was because bootstrap defaults have a very bright white, which contrasted very nicely with my sandstone background.

### Product Details

!["The Product Details page for my website"](read_me/features/product_details.png)

When a user clicks on a product image on the product page, they will be taken to the product details page. This is the page where users can get more information about a chosen item, select the quantity of item they want and then add it to the shopping bag. Users on the details page can clearly see the item title, the collection the item belongs to, the item price, how many upvotes and downvotes the item has (Future feature to implement) and finally how many items in the quantity box. The user has the option to click the box and manually input a price however, an easier alternative is to click the button on either side of the box instead to increment it or decrement it by one. When the user choses to add the item to the bag, they will recieve a toast informing them if it has been successfully added or not.

### Bag

!["The Bag page for my website"](read_me/features/bag.png)

The bag app is where the customers items are held up until they are ready to go on to the checkout app. Here the products name, item, SKU code and item quantity can be seen and highlighed by the headers above each section of it. Here, due to the bags nature of an array, the user is easily able to increase or decrease the quantity of an item if they so want it or even delete the item all together if they change their mind. Towards the bottom, the delivery cost can be seen as a flat £10  to cover potential petrol costs in delivery as well has the cost of bubble wrapping the artwork. This delivery is then added together with the total cost of the items selected to display a grand total price for the user. A significant issue with the development of the bag, was the lack of javascript functionality. Initially, the update and delete buttons were non functional and instead merely just refreshed the page repeatedly. When I investigated the issue, I learned that the issue was in the use of an outdated version of popperJS. Once an older version was implemented, the javascript worked as intended save for the toast. They would disappear far too quickly for the users to read them and their close buttons did not work. This was fixed by giving them the missing classes to interact with bootstraps aria labels and giving them a data class to extend their timeout time to 5000ms as opposed to the default 500ms.

### Checkout

!["The Checkout page for my website"](read_me/features/checkout.png)

The checkout app is where, through the use of stripe, the users payments are handled and the order is then completed. On the left of the container is the stripe form, this form first asks for the users name and email for the use of identification. And then it requests the users delivery information. This can be handled in a couple ways, the user can either input their delivery details into their profile and have it automatically added to their checkout or they can input it directly into the checkout form and then use the remember me button to add it to their profile to use for later checkouts. Of course, the user can also access the checkout app however they cannot save their details for later if they do this and must ultimately re-enter their details on future purchases. The stripe form is handled by outside css and js specific to the checkout app, when generated, users can enter their credit card information. Upon submitting, the payment will be handled by stripe securely and webhooks on the site will interact with the associated stripe account to give feedback on the status on the transaction. On the right is the details for their purchase, handled in a similar manner to their bag. It includes an order summary of the total amount of items requested, then the item image, name, price and quantity of said item. Below it are the delivery charge and price totals as previously discussed. This app, after intial confusion with how to set up stripe due to not properly setting up it's webhooks, was mainly marred by an unresponsive layout as both sides of the container would start to merge onto each other. To rectify this I made the bootstrap columns that were normally 6 in width, instead only conditionally 6 depending on screen size whilst the normal column size was set to 12. This made it so that the order information was below the checkout form and thus easier to read on mobile devices.

### Checkout Success

!["The Checkout Success page for my website"](read_me/features/checkout_success.png)

This is the page that handles displaying post order information that would not normally be present in the previous two screens and also to inform the user that their order was indeed successful. The unique information displayed on this page consists of the order number and the order date, the former of which is randomly generated in order to have each transaction be completely unique for the purposes of the user later being able to access their own user history. This same page is also used for displaying a users order when they look in their profiles order history. At the bottom of the page, the user is given a buttom to take them back to the home page.


## User Stories Testing

|Test Case Type|Description|Test Step|Expected Result|Status|
|:----|:----|:----|:----|:----|
|Functionality|User should receive confirmation their account has been created|An email should be sent to the user with a profile link|Clicking on the link in the email should send users to their account profile|Pass or fail|
|Security|Verify that the user can only sign in with the correct login details|Make sure that created account details are within database rules for that users login.|The users account will be accepted if it follows the database rules for that users login.|Pass or fail|
|Usability|User should have feedback on their login status|Have a username unique to the user|The presence of the icon or not will indicate user login status|Pass or fail|
|Security|A users data should NOT be available to another user and only within their own session.|Logging onto an account then taking that page link to incognito mode.|Moving to incognito mode should result in that account data being inaccessible.|Pass or fail|
|Usability|Users must be easily differentiated from one another.|Unique user code and username|Users can see their username and admins can see user codes.|Pass or fail|
|Functionality|Check order histories and delivery dates.|Store orders and generated delivery dates on page in user profile.|The page will inform the user of their order history|Pass or fail|
|Functionality|Rate Items with a thumbs up or down.|Thumb icons connected to a database.|The amount of thumb ups and down will be shown on the product page.|Pass or fail|
|Usability|Arrange products based on features e.g. price.|Drop down menu with options e.g. A-Z|Clicking a drop down option will sort the catalogue in that way.|Pass or fail|
|Functionality|Search for specific products.|A search bar at the top of the screen.|Typing into the search bar will enable users to find specific items.|Pass or fail|
|Functionality|View items in the shopping bag|Users should be able to check what they are going into checkout with.|Clicking the shopping bag button should list out added items.|Pass or fail|
|Security|Secure shopping with stripe|Create test transactions that don’t take out money|If these transactions appear on the stripe website then they were successful.|Pass or fail|
|Useability|Contact the seller for international sales|Have a contact page on the site|Using the form on the contact page will get them in touch with the site owner.|Pass or fail|
|Useability|View the sites social medias.|Have links to social media in the website footer|The links will take the user to the social medias depending on icon|Pass or fail|
|Useability|Signing up for a email newsletter|Have a sign up at the bottom of the main page.|Providing an email to that link will sign a user up for the newsletter|Pass or fail|
|Functionality|Add items in the shopping bag|Users should be able to add items to their shopping bag|Enable users to add items of various quantities and sizes to a shopping bag.|Pass or fail|
|Functionality|Update items in the shopping bag|Users should be able to change product amounts if they change their mind.|Shopping bag should carry functionally to change quantity amounts.|Pass or fail|
|Functionality|Delete items in the shopping bag|Users should be able to delete products from the bag if they change their mind.|Shopping bag should carry functionally to delete added products.|Pass or fail|
|Functionality|Creating testimonials for the site|Users should be able to provide their feeback on the site via testimonials|Testimonials should possess full CRUD functionality.|Pass or fail|

### Developing Custom Apps

#### Contact

In order to create my contact app I first had to create the app itself by setting up it's views, templates and url's both in it's native folder and in the project folder. Within this project folder I also had to signify it as an allowed app. Once this was done I had to create my model. In order for the desired functionality, I would need 3 fields: An email field to handle the sender email, a subject field to handle the email subject and a body field to handle the main body of the email. Once this was created and migrated, I had to create the form itself inside of a form.py. Inside the file, I declared what model and fields I needed within the meta class of my larger ContactForm class. Inside the _init_ definition I then had to declare how my placeholder fields would be rendered and then how the form itself would be rendered when I used crispyforms inside the template. Using widgets to identify required fields, I assigned them a star so users would know if they were needed or not. Even though all the fields are required, I decided that it would be for the best to keep them on to remove the chance of confusion on the users part. 

!["Proof that the contact email works as intended."]()

With this back end in place, I now had to create a view to manage this form. This form had to be able to achieve two things; One, Process the form and save it to the database if it's valid information. Two, take this information and convert it into an email that can be sent to the host server as if it was sent from the submitted email. The first process was solved by storing each field as a request.POST that was then assigned in a single array called form_data. A contact_form variable was then made and assigned the argument that it should equal the contents of the form with the form_data with it. This is then checked to be valid and if so it is saved to the database. In order to send the email I had to use the aptly named function send_email. This function takes 4 variables; subject, body, from email and recipient list. In order to fill in these variables for the contact email, I set the recipient to be the default email in settings.py and then the other three were taken directly from the form itself. This way the email is sent as soon as the form is submitted. After that the view was finished by giving it a success message informing the user the email was sent successfully and then the relevant contexts and templates were established to allow the form to post as intended. Finally, the template was made to host the backend and this was rather simple. Crispy form was used to host the form and the form was set to use the contact view as an action. After that the general site stylings were applied and the app was completed.

#### Testimonials

The start for creating my testimonials app was similar to the contact app, however, the structure of it's models and form would be notably different to that of the contact form. Starting with the model, in order to gain the desired functionality, I would need the following fields; A creator app which used the allauth user as a foreign key so that they can make multiple testimonies but a testimony can only has a single user. A name field so that each testimony can have a distinct name, it was not linked up to the username of the current account so that users had the option to choose something different e.g. their account username contains sensitive information. A date field would be needed so that users can know when the testimony was created. A description text field to hold the main body of the testimony itself and finally a rating field to allow the users can rate the site out of 5. For the form, out of those 5 fields, only the rating, name and description would be asked for. The date would be automatically generated by the model up the creation of a new entry and the creator would be given it's data at a later date. The fields are handled the exact same way as the contact form, however, in order to facilitate the use of a dropdown on the form a seperate variable outside of the TestimonyForm class had to be created called RATING_CHOICES that would hold the numbers 1-5 in an order from 1 to 5. From there, ratings would be declared as a choice form within the class and assigned as a choice field, it's choices being that of the RATING_CHOICES.

The views created from this form were focused entirely on not just creating and handling the testimonies but also on affording them full CRUD functionality. The first one that had to be made was the display testimony view. The simplest view in the app, it merely recovered all the testimonies created on the model and then stored them as a variable to be called on the html page through ginja, displayed with the name and date beside each other and both ratings along with the description below. Adding a testimony used a similar method described in contact. The form data was saved to a variable containing post requests for each of the needed variables specified in form.py. Once this data was validated it was then saved to the database. The important change however, was that the creator field was established by manually assigning the data for that field as request.user, this was done so that only the user that created the testimony could edit or delete it. When editing the testimony, the view to handle it had to do two new things. It had to be able to call the id of the testimony the user wanted to edit, ensure it was the same as the user that created it. It then had to populate the form with the same info as the testimony id. And then save that edited id.

The way that I did this was ensure that when the template called for edit via the form, both the action call and the url called for the testimony id. This was provided by a variable in the view that called get_object_or_404 which collected the testimony id's. Next the view compared the current user with the user stored in the creator model. If they matched up, then the user would be given access to the edit testimony page, if they did not, they would be sent back to the testimony page with an error message. Then it checked if the page was making a GET or a POST request. If it was making a get request, then it would use the testimony id as an instance and populate the form using data from that instance. If the page was then making an POST request, it would save the edited data to the form as a POST request within the instance of that testimony id and a success message would deploy.

#### Light/Dark mode.

*

## Validator Testing

### W3C Validator

### Lighthouse Validator

### Javascript Validator

### Python Validator

### Wave

# Deployment #

(Subject to change in accordance with django specific deployment.)

To deploy my site I used heroku. This was done by using the following steps.

1. Use the code institute database generator to get a unique database url for deployment.
2. Install dj_database_url and psycopg2 to handle the generated database.
3. Set up settings.py to send database data to the generated URL.
4. Load all fixtures to the URL as well as migrate all databases to it. 
5. Generating a requirements.txt file containing the python dependencies needed for the project.
6. Create a Procfile to contain the command for starting up the website.
3. Log on to Heroku.com and create a new app, while also giving it a unique name and setting the region to europe.
4. In the settings section, create a config var on the heroku app to hold the DATABASE_URL and assign it the url given by Code Institute.
5. Establish the stripe variables and django secret key to this section also.
6. Create an AWS account.
7. Set up S3 and IAM services with the relevant Users, Buckets and Policies.
8. Install django-storages and Boto3 and create custom-storages.py
9. In this file, establish the location of where the media and static files will go. This is because heroku cannot handle the deployment of static files.
10. Back in settings, set up the static files so that in the presence of the USE_AWS variable in config vars, use the setup that targets S3 for storing static and media files.
11. Make sure that all other vital variables are dependant on them being present in os.environ() rather than declared in order to prevent security flaws.
12. Select your github repo from the list and use Manual Deploy to deploy the branch of choice.
13. Click run app and enjoy! Be sure to ensure that the site works as it should and that DEVELOPMENT is set to false.

It should also be noted that debug should be set to false before publishing the website. I have done this and provided the relevant evidence below.

![Proof that I have set the debug on my set to false.](read_me/debug_false_proof.png)

# Languages #

* For the development of this website I utilized HTML, CSS, JS and Python in order to create it. 

* Bootstrap 5.3.3 was used to create the accordion and for it's grid system in laying out site features.

* The framework used to construct the site was Django, which uses model-view-controller software design to build a full-stack developed website.

# Media Queries #

Media Queries were used exclusively in the role of increasing the responsiveness of web pages by...

# Software #

VS Code was used to create the website. It was the tool for typing out HTML, CSS, JS and Python code along with pushing site updates to the Github repository. Gitpod was used to provide backend and virtual environment support for the use of python without which the site would not function.

Balsamiq was used to create the wireframes saw earlier in this readme.

The microsoft snipping tool was used to take the relevant screenshots.

# Code #

https://www.wearedevelopers.com/magazine/how-to-create-a-test-plan-for-software-testing

https://boost-tool.com/en/tools/md_table

https://books.agiliq.com/projects/django-admin-cookbook/en/latest/current_user.html


# Credits #

Code Institute for the opportunity to learn and hone the craft of developing websites.

My loving and supportive family for supporting me in this endeavor.