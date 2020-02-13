[![Build Status](https://travis-ci.com/chodar89/dot_geek.svg?branch=master)](https://travis-ci.com/chodar89/dot_geek)<br>
<img src="dot_geek\static\img\logo\dotgeek_black.png" width="200">

# DOT GEEK
So this is my fourth and last project for CodeInstitute. It is e-commerce website for geeks but not only. Potiential customers will find a products from retro and legendary games, films, cartoons and comics. <br> https://dot-geek.herokuapp.com
## UX
Website allows user to buy and browse all products that are in shop offer. User can create an account and pay securely for his shopping. As well thare is a cart tab where user can check what is in and adjust product amount or delete it. User can check his shopping history (only for user that holds an account). App is responsive and friendly to users. Design is inspired by retro 8bit games. All vector graphic was created with CorelDraw.
## User Stories
1. Customer/User. As a user:
- I would like to have an option to register and login.
- I would like to have a feedback when I am registred/login/logout via any message on the page.
- I would like to reset my password if I forgot it via my registration email
- I want to have an option to search for an items/products that I am interested in via search option.
- I would like to have an option to click an item and check details of this product and have gallery for it via it's own page.
- I want to have a cart that can restore my shopping on the same computer even that I am a guest.
- I want to have a cart that can restore my shopping when I am registred on the page on any device.
- I would like to have an option to adjust shopping items by buttons in the shopping cart page - [Video](https://drive.google.com/file/d/1Ds_UxLdtKUup8J3yR_hzDW3he4EvPMUr/view)
- I would likte to have a feedback after my purchase is done via message on the page an email with order number.
- I would like to see my order if I am registred user via my dashboard page.
- I want to see if product is in stock or outofstock by nice feedback on the product page.

2. Admin/User. As an admin:\
- I want to have an option to add product and decide is it for sale or no without deleting it from DB via admin panel.
- I want to decide what is and what is first in the main img carousel
- I want to see orders with order items via admin panel
- I want to decide what is in dropdwon nav bar via admin panel
- I would like to have an option to change price without going in too every single product.
## Mockup and DB structure
- [Admin Panel Video](https://www.youtube.com/watch?v=7PIUYP_sfno)
- [App overview](https://drive.google.com/file/d/1AWLIc07KaIVx7QEYhff_okDDGqbieKDy/view)
- Database schema structure can be found [here](https://dbdiagram.io/d/5d8b50f6ff5115114db49d17)
- Mockup is hosted with Adobe XD [link](https://xd.adobe.com/spec/cf7ca274-c296-4b73-7515-36372375f89c-b94d/)
## Features
- Customized Django Admin Panel
- User dashboard
- Carousel panel on the index page (can be customized from admin panel)
- New in products on the main page
- Bestseller products - index page
- Search mode
- Pay with Stripe
- Login adn register panel
- Email notifications
- Stripe payment
- Custom cart
- User dashboard with order history
## Technologies Used
- HTML
- CSS
- JavaScript
- Django 3.0.3
- Python 3.7.5
- PostgreSQL
- pgAdmin4
- VS Code
- Bootstrap
- Fontawesom
- Jinja2
- jQuery
- CorelDraw
- AWS S3 Bucket
- Travis CI
- Adobe XD
- dbdiagram.io
## Testing
### Auto Test
- urls tested with Django build in test framework
- tested all views status codes and is correct template used
- created temp DB and tested register process and login process and dashboard page
- build tested with Travic CI (Travis badge at the top of the page)
- get product or 404 tested if raises 404 page if product not found, as well tested query of product exists
- filter and get all products from DB
- tested context data for dropdwon search queries
- tested dashboard get order item data
- tested cart (add, increase, remove, delete qnty/item from DB) with temp SQLite DB 
### Manual Test
- tested manually by: adding, editing, deleting records from database
- tested on different devices with iOS(13), Android(10), Windows(10) and Macintosh(10.15) system
- tested on Chrome(79.0.3945.88), Opera(65.0.3467.78), Mozilla(71.0 (64-bit)) and Safari browsers
- simulated on different mobile/pc devices with Device Mode in Dev Tools mode
## Deployment
- App is running and hosted on [Heroku](https://dot-geek.herokuapp.com)
### Steps to deploy
#### Static files
- Static files are in dot-geek app folder:<br> <strong>`dot-geek/static`</strong>
#### Database pre set values
- only Size Chart requires pre set data
- insert sizes in brackets (CAPITAL LETTERS!) to Size Chart table: ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')
#### Steps to deploy app on Heroku
- create an account on [heroku](https://heroku.com)
- after sign up, login and create a new app with unique name:<br>
  New > Create new app<br>
  or create app from CLI - [manual](https://devcenter.heroku.com/articles/creating-apps)
- go to Resources tab and get <strong>Heroku Postgres</strong> add-on
- you need to create requirements.txt file and the Procfile<br>
  From command line:
  ```
  $ pip freeze --local > requirements.txt
  $ echo "web: gunicorn your_app_name.wsgi:application" > Procfile
  ```
- push te code to <strong>GitHub</strong> and from <strong>Deploy Card</strong> in Heroku deploy your branch
- Set up config vars. Go to <strong>Heroku > Settings</strong> tab and cicl <strong>Reveal Config Vars</strong><br>
1. AWS_ACCESS_KEY_ID (only if you use AWS S3 Bucket)
2. AWS_SECRET_ACCESS_KEY (only if you use AWS S3 Bucket)
3. DATABASE_URL
4. DISABLE_COLLECTSTATIC
5. STRIPE_PUBLISHABLE_KEY (only if you use stripe payment)
6. STRIPE_SECRET_KEY (only if you use stripe payment)
### Run app local
#### Before start
- if you would like to run app with the same settings, than you will need to read how to set up [Stripe](https://stripe.com/) and [AWS S3](https://aws.amazon.com) buckets
- you can check Stripe Django tutorial [here](https://testdriven.io/blog/django-stripe-tutorial/)
- and AWS S3 tutorial [here](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)
#### How to run app on your local machine
- install or update Python to version 3.x
- create [virtual env](https://docs.python.org/3/tutorial/venv.html)
- download all files to local dir
- now install all packs from requirements.txt
  ```
  $ pip install -r requiremenst.txt
  ```
- you will need to create <code>.env</code> file next and set up your own config vars
1. SECRET_KEY
2. USER
3. PASSWORD
4. HOST
5. STRIPE_PUBLISHABLE_KEY
6. STRIPE_SECRET_KEY
- in <strong>`settings.py`</strong> we have statement that checks if we are in dev mode, see belowe<br>
  if you would like to use local DB than just remove/comment or do not add 'DATABASE_URL' to your env file.
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
        }
    else:
        # Local DB
        DATABASES = {
            'default': {
                'ENGINE': os.getenv('ENGINE'),
                'NAME': 'dot_geek',
                'USER': os.getenv('USER'),
                'PASSWORD': os.getenv('PASSWORD'),
                'HOST': os.getenv('HOST'),
                'TEST': {
                    'ENGINE': 'django.db.backends.sqlite3',
                }
            }
        }
    ```
- and comment out other DATABASES setting at line 105 in <strong>`settings.py`</strong>
- in the same time you should install PostgreSQL and pgAdmin on your computer [link](https://www.postgresql.org)
- once you set this up run 
  ```
  $ python manage.py createsuperuser
  ``` 
- follow the command line and provide data
- than you will need to do migrations to your DB run in terminal:
  ```
  $ python manage.py makemigrations
  ``` 
  and 
  ```
  $ python manage.py migrate
  ```
- if you dont want to use S3 bucket instead you would like to hold everything in local dirs, you need to comment out all AWS settings lines in <bold>settings.py</bold> plus <code>STATICFILES_LOCATION, STATICFILES_STORAGE, MEDIAFILES_LOCATION, DEFAULT_FILE_STORAGE</code>
- to collect all static files run in terminal:
  ```
  $ python manage.py collectstatic
  ```
- finally run the app:
  ```
  $ python manage.py runserver
  ```
### Credits
- All vector graphic was created by Tobiasz Chodarewicz
- Images downloaded from Unsplash, Pixabay and Pexels
- Products from Pop Vinyl page and Wish
- Password reset, from tutorial that can be found [here](https://medium.com/@renjithsraj/how-to-reset-password-in-django-bd5e1d6ed652)
