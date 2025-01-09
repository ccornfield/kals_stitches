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

Databases Needed

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
|County|Character|The user’s postcode used for deliveries|
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
|Default County|Character|The user’s postcode used for default deliveries|

#### Newsletter

|Key|Value Type|Description|
|:----|:----|:----|
|Profile|Foreign Key|Links the specific email to the account that created it.|
|Email|Character|The users email to send newletter updates too|

# Features #

# Testing #

## Page Testing

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
|Functionality|Cancel orders pre dispatch|Delete functionality for stored order history.|Deleting order history sends alert email to admin.|Pass or fail|



## Validator Testing

### W3C Validator

### Lighthouse Validator

### Javascript Validator

### Python Validator

### Wave

# Deployment #

(Subject to change in accordance with django specific deployment.)

To deploy my site I used heroku. This was done by using the following steps.

1. Generating a requirements.txt file containing the python dependencies needed for the project.
2. Create a Procfile to contain the command for starting up the website.
3. Create a new variable in __init__.py called DATABASE_URL to allow the project to read an external database.
4. Log on to Heroku.com and create a new app, while also giving it a unique name and setting the region to europe.
5. In the settings section, create a config var on the heroku app and assign it the url given by Code Institute.
6. Add to the config var all the details contained in env.py except DEVELOPMENT and DB_URL.
7. Go onto the deploy section, and use Connect to Github as the deployment method.
8. Select your github repo from the list and use Manual Deploy to deploy the branch of choice.
9. Use the run command feature and type python3 into the console to get the python interpreter.
10. Run Terminal.py to build the database for the site.
11. Click run app and enjoy! Be sure to ensure that the site works as it should and that DEBUG is set to false.

It should also be noted that debug should be set to false before publishing the website. I have done this and provided the relevant evidence below.

![Proof that I have set the debug on my set to false.]()

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



# Credits #

Code Institute for the opportunity to learn and hone the craft of developing websites.

My loving and supportive family for supporting me in this endeavor.