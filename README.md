[![Build Status](https://travis-ci.com/chodar89/dot_geek.svg?branch=master)](https://travis-ci.com/chodar89/dot_geek)<br>
<img src="dot_geek\static\img\logo\dotgeek_black.png" width="200">

# DOT GEEK
So this is my fourth and last project for CodeInstitute. It is e-commerce website for geeks but not only. Potiential customers will find a products from retro and legendary games, films, cartoons and comics. <br> https://dot-geek.herokuapp.com
## UX
Website allows user to buy and browse all products that are in shop offer. User can create an account and pay securely for his shopping. As well thare is a cart tab where user can check what is in and adjust product amount or delete it. User can check his shopping history (only for user that holds an account). App is responsive and friendly to users. Design is inspired by retro 8bit games.
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
- Django 2.2.6
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
## Testing
### Auto Test
- urls tested with Django build in test framework
- views tested with Django build in test framework
- build and tested with Travic CI (Travis badge at the top of the page)
### Manual Test
- tested manually by: adding, editing, deleting records from database
- tested on different devices with iOS(13), Android(10), Windows(10) and Macintosh(10.15) system
- tested on Chrome(79.0.3945.88), Opera(65.0.3467.78), Mozilla(71.0 (64-bit)) and Safari browsers
- simulated on different mobile/pc devices with Device Mode in Dev Tools mode
## Deployment
- App is running and hosted on [Heroku](https://dot-geek.herokuapp.com)
### Steps to deploy
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
- next uncomment in <strong>`settings.py`</strong>:
    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'dot_geek',
                'USER': os.getenv('USER'),
                'PASSWORD': os.getenv('PASSWORD'),
                'HOST': os.getenv('HOST')
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
