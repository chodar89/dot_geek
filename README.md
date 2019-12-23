# DOT GEEK
So this is my fourth and last project for CodeInstitute. It is e-commerce website for geeks but not only. Potiential customers will find a products from retro and legendary games, films, cartoons and comics. <br> https://dot-geek.herokuapp.com
## UX
Website allows user to buy and browse all products that are in shop offer. User can create an account and pay securely for his shopping. As well thare is a cart tab where user can check what is in and check his shopping history (only for user that holds an account). App is responsive and friendly to users. Design is inspired by retro 8bit games.
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
## Deployment
- App is running and hosted on [Heroku](https://dot-geek.herokuapp.com)
### Steps to deploy
#### Steps to deploy app on Heroku
- Create an account on [heroku](https://heroku.com)
- After sign up, login and create a new app with unique name:<br>
  New > Create new app<br>
  or create app from CLI - [manual](https://devcenter.heroku.com/articles/creating-apps)
- You need to create requirements.txt file and the Procfile<br>
  From command line:
  ```
  $ pip freeze --local > requirements.txt
  $ echo "web: gunicorn your_app_name.wsgi:application" > Procfile
  ```
- Push te code to <strong>GitHub</strong> and from <strong>Deploy Card</strong> in Heroku deploy your branch
- Set up config vars. Go to <strong>Heroku > Settings</strong> tab and cicl <strong>Reveal Config Vars</strong><br>
1. AWS_ACCESS_KEY_ID (only if you use AWS S3 Bucket)
2. AWS_SECRET_ACCESS_KEY (only if you use AWS S3 Bucket)
3. DATABASE_URL
4. DISABLE_COLLECTSTATIC
5. STRIPE_PUBLISHABLE_KEY (only if you use stripe payment)
6. STRIPE_SECRET_KEY (only if you use stripe payment)
### Run app local
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
- next uncomment in `<settings.py>`:
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
- and delete other DATABASES setting line 100 in `<settings.py>`
- in the same time you should install PostgreSQL and pgAdmin on your computer [link](https://www.postgresql.org)
- once you set this up run <code>python manage.py createsuperuser</code> follow the command line and provide data
- than you will need to do migrations to our DB `<python manage.py makemigrations>` and `<python manage.py migrate>`
- if you dont want to use S3 bucket insted you would like to hold everything in local dirs, you need to comment out all AWS settings lines in <bold>settings.py</bold> plus <code>STATICFILES_LOCATION, STATICFILES_STORAGE, MEDIAFILES_LOCATION, DEFAULT_FILE_STORAGE</code>
- than run `<python manage.py collectstatic>`
- to run app `<python manage.py runserver>`
### Credits
- All vector graphic was created by Tobiasz Chodarewicz
- Images downloaded from Unsplash, Pixabay and Pexels
- Products from Pop Vinyl page and Wish
