[![Build Status](https://travis-ci.org/kajamiko/u_m_website.svg?branch=master)](https://travis-ci.org/kajamiko/u_m_website)

# The Usos Modern website

## What is Usos Modern?
Usos Modern is a website of a non-existing, but very useful (if it existed) mobile app - USOS Modern App, that is supposed to  be a helper when using an infamous USOS system, used for some reasons by polish universities.

Most important USOS Modern App features are: scheduling, message sending and receiving and making changes to the university account. And anything users would like to know about USOS Modern App, it can be found on Usos Modern website.

Usos Modern website is a project run by USOS Modern App's developers, to help making their app even better. It contains FAQ about their app and about their sales policy, a blog and most importantly - a heart of the project, an amazing issue tracker, where users can take active part in their favourite app's development.



Ad cat icon: changed from materialize to fontawesome because I wanted a badge with info on a cart icon

UX
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

1. Home - on this part of the project, users can find all informations about the website and app that the website is created for, including statistics.

2. Accounts - users can register and log ino their accounts. They can also keep some details stored in their 'accounts' section, to make checkout easier.

3. Cart - cart is an separate app holding cart logic - users can add, remove or modify their selected tickets along with donation amount, as needed.

4. Checkout - the Usos Modern's checkout is made through Stripe. No sensitive payment or credit card details are stored in database, nor are processed by the app itself.

5. Issue tracker - it is where all the issue tracker logic is stored. Tickets can be created by logged in users. They can also be upvoted or donated and - last but not least - commented.

6. Blog - users cannot add posts, but register users can add comments.


## Existing Features


1. Home ('home' app)
 1. Homepage - good looking homepage with a carousel, gives users a chance to get familiar with navigation, which is similar across the whole site. There is a top navbar with a logo and account navigation links. There is also a side navigation list, with links to info pages, as informatin is what user may want to know first.
 2. About UM App - App's FAQ, links to Google Play and Apple Stores, as it would be on a real project's website.
 3. Our Promise - developer's business plan described and some useful information about the Issue Tracker.
 4. Statistics - contains charts summarising Issue Tracker.
 

2. Accounts ('accounts' app)
 1. Registering - users can register by filling the form on the "Register" page. There is a link on a navbar, available from every location on the website. 
 2. Logging in - to log in, user has to submit his username and password, by filling a form on a "Log in" page.
 3. Account - users can see their accounts by clicking on "Account" link the top navbar. Here, they can find some details useful when purchasing upvotes and their previous orders, if any.
 4. Having an account allows users, among others, to comment blog posts and to edit their Issue Tracker comments.
 

3. Cart ('cart' app)
  1. Users can add a ticket to the cart, by clicking 'Up(add to cart)' link on the "ticket details" page. The number of items displayed on a cart icon in a top right corner will increase. By default, the ticket's donatino is £5, but it can be easily updated.
  2. User can see his cart's content by clicking on the cart icon in the top right corner (on the navbar). This will redirect to 'cart detail page'.
  3. While on ''cart detail page', user can update ticket's donation. To do so, user can choose amount from the choice field and click 'Set donation'. Page will refresh and the new amount can be seen next to the ticket's title.
  4. From this point, user can either click 'Continue browsing' to see other tickets, or go to checkout by clicking 'Checkout' button.
  5. To complete the order, user should fill the order form, and then click 'Pay with card' button. After the payment is accepted, order is completed. The tickets paid are upvoted now.
 
3. Checkout ('checkout' app)
   1. To go to checkout, user should first click the icon cart, and then click 'Go to checkout' button on the cart view.
   1. To complete the order, user should fill the order form, and then click 'Pay with card' button. After the payment is accepted, order is completed. The tickets paid are upvoted now.
   2. User can see transaction summary soon after it is completed. The order details will be displayed after the page is refreshed.
   3. Orders can be made anonymously or by users with active accounts. However, only registered users can see their orders after, on their "Account" page.

4. Issue Tracker ('tickets' app) 
   1. All users can browse the tickets and comment them. 
   2. Only registered users can add tickets. Tickets can be modified only by admins.
   3. All users can comment, but only registered users can upvote 'Bug' tickets and modify their previous comments.
   4. All users can donate to 'Feature' tickets, but only registered users can track on their previous orders.

5. Blog ('w3blog' app)
   1. All users can see posts.
   2. Only registered users can comment.

### Features Left to Implement

I would like to implement methods to make chart responsive.


## Technologies Used


- HTML and CSS
    - project uses **HTML** and **CSS** to build webpages.
-  [Materialize](https://materializecss.com/)
    -project uses **Materialize** for webpages' layout.
- [Javascript](https://www.javascript.com/) 
    -The project uses **Javascript** to enhance pages functionality.
- [JQuery](https://jquery.com)
    - The project is using Materialize's **JQuery** for responsiveness.
- [Python](https://www.python.org/)
    - The project's back-end was written in **Python** .
- [Django](https://www.djangoproject.com/)
    - project was built using **Django** framework.
    Following Django packages was used to build the project:
     1. [django-material](http://forms.viewflow.io/) - django support for materialize
     2. [django-summernote](https://pypi.org/project/django-summernote/) - requirement for w3blog
     3. [pygal](http://pygal.org/en/stable/) - used for plotting beatiful charts 
     4. [stripe](https://stripe.com/) 
        - online payments handling
     5. [w3blog](https://pypi.org/project/w3blog/)
          - instead of designing a blog again, the project is using **w3blog**.
     6. [boto3](https://readthedocs.org/projects/boto3) and [django-storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
         - Boto3 to connect to Amazon SDK and django-storages to store files away form Heroku.
     7.[dj-database-url](https://pypi.org/project/dj-database-url/)
         - used to connect to Heroku's Postrgres DB


## Testing

The project has been tested carefuly. For each app, in the app's main directiry there are separate files with names: 
- `test_app.py` - where app name is tested 
- `test_forms.py` - forms are tested for validation
- `test_models.py` - where models fields and methods are tested
- `test_views.py` - where tests for views' templates, POST/GET request and expected display can be found.
- `test*.py` - tests for other functions


For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:


Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.

For different screen sizes, I designed a sidebar and made sure it's always visible on wide screen, but hidden and available to toggle on smaller screens.

Materialize bug:

When displaying some pages, a jQuery error may appear in the console. I have not designed any jQuery logic on my own, and this is a known Materialize bug.


#### Bugs

During testing, I found out that form's automated results are not giving expected results, when it comes to adding a not required foreign key(see comments in test_forms.py). However, it seems to work when testing views and in live tests.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

To deploy the project, I have to find a way to keep static file in place. I created a Amazon S3 bucket for this, and added new configuration variables to the project's settings.py file.

The database setting has been changed from default Django file to Heroku Postgres Database.
In development, I have used a separate configuration file to keep sensitive data. These variables are set as Heroku Confog Vars. 

Suprisingly, I did not encounter any problems with the code itself during deployment, and I did not set a separate git branch for the purpose. 
The same code works locally on Cloud9 and on Heroku.

## Credits

### Code snippets used in Projects

1. Cart
 Cart logic was designed, following the [tutorial](https://blog.muva.tech/lesson-1-building-e-commerce-shopping-cart-using-django-2-0-python-3-6/), however I modified the original code to suit my needs.


2. Charts
 For charts logic, I have copied and modified the example made by Ray Chen and published on [Hackernoon](https://hackernoon.com/server-rendered-charts-in-django-2604f903389d). All the modifications are made by myself.


Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from [Pixabay]()
Acknowledgements
I received inspiration for this project from X