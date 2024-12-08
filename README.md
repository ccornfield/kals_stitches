# Gamedream - A portfolio project.

Welcome to my code institute website readme. This is for my milestone 4 project. For this I have decided to create a website for my mothers textile business revolving around the sale of her textile art and cards alongside various kits used to create them. I have done this by creating a django framework powered by a sqlite database and the web application stripe designed to provide secure payments. This was done because the project goal was to create an effective ecommerce website.

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

...

### Target Audience

...

### User Stories

!["The user stories for my project"](read_me/user_stories.png)

The above image displays the user stories that I will be using for my project.

### Wireframe

These are the wireframes I created to help me plan out the design of my website. The designs were not final but there were a massive help in creating the project.

Needed Wireframes

1. Home Screen
2. Product Selector
3. Product Details
4. Shopping bag
5. Billing details
6. Order Confirmation
7. Account Creation
8. Login
9. User Profile
10. Order History
11. Contact
12. Wishlist confirmation.



### Color Scheme

![This was the palette I chose to use for my site.](read_me/color_palette.png)

The above color scheme was rather simple to create. My mother had suggested using 3 colors initially(Dun, Nyanza Green and Non-Photo Blue). Using those as a base, I then utilized 

### Typography

![This was the font I chose to use for my site.](read_me/typography.png)

When picking out an appropriate font for the website I wanted to avoid something like new times roman while also ensuring that it was still clear and easily read on smaller phone devices. To achieve that middle ground I settled upon using Overpass for my font of choice.

### Database

The below database model shows the relationships between all of the models in my database and their relationships. The database features for handling account logins are handled by allauth rather than my own personal code.

| Key      | Value Type |  Description    |
| :---        |    :----:   |          ---: |
| ID   | Text        | Lorem Ipsum     |

Databases Needed

1. Products


# Features #

# Testing #

## Page Testing

## User Stories Testing

## Validator Testing

### W3C Validator

### Lighthouse Validator

### Javascript Validator

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
# Credits #

Code Institute for the opportunity to learn and hone the craft of developing websites.

My loving and supportive family for supporting me in this endeavor.