## Build from sources

```bash
# Clone the sources
git clone https://github.com/messer979/flask-author-demo.git
cd flask-author-demo

# Virtualenv modules installation (windows)
virtualenv venv
. .\env\Scripts\activate

pip install -r requirements.txt
# Set the FLASK_APP environment variable
(Unix/Mac) export FLASK_APP=run.py
(Windows) set FLASK_APP=run.py
(Powershell) $env:FLASK_APP = ".\run.py"

# Set up the DEBUG environment
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"
# Run the application
# --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
# --port=5000    - specify the app port (default 5000)  
flask run --host=0.0.0.0 --port=5000
# Access the app in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project has a super simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- app/__init__.py
   |-- app/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |    |-- accounts/                 # Auth Pages (login, register)
   |    |    |    |
   |    |    |    |-- login.html           # Use layout `base-fullscreen.html`
   |    |    |    |-- register.html        # Use layout `base-fullscreen.html`  
   |    |    |
   |    |  index.html                      # The default page
   |    |  authors.html                    # Author page **
   |    |  page-404.html                   # Error 404 page (page not found)
   |    |  page-500.html                   # Error 500 page (server error)
   |    |    *.html                        # All other pages provided by the UI Kit
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Heroku](https://www.heroku.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-illustrations-iradesign.git
$ cd flask-illustrations-iradesign
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Heroku](https://www.heroku.com/)
---

Steps to deploy on **Heroku**

- [Create a FREE account](https://signup.heroku.com/) on Heroku platform
- [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) that match your OS: Mac, Unix or Windows
- Open a terminal window and authenticate via `heroku login` command
- Clone the sources and push the project for LIVE deployment

```bash
$ # Clone the source code:
$ git clone https://github.com/app-generator/flask-illustrations-iradesign.git
$ cd flask-illustrations-iradesign
$
$ # Check Heroku CLI is installed
$ heroku -v
heroku/7.25.0 win32-x64 node-v12.13.0 # <-- All good
$
$ # Check Heroku CLI is installed
$ heroku login
$ # this commaond will open a browser window - click the login button (in browser)
$
$ # Create the Heroku project
$ heroku create
$
$ # Trigger the LIVE deploy
$ git push heroku master
$
$ # Open the LIVE app in browser
$ heroku open
```

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />


---
[Flask App - Illustrations by IraDesign](https://appseed.us/apps/flask-apps/flask-illustrations-iradesign) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).


> Open-Source Web App generated in Flask by AppSeed [Web App Generator](https://appseed.us/app-generator) - Features:

- Illustrations by [IraDesign](https://iradesign.io/) - a Creative-Tim product
- UI Kit: **Quick** (Free Version) by **Webpixels**
- SQLite database, Flask-SQLAlchemy ORM
- Session-Based auth flow (login, register)
- Deployment scripts: Docker, Gunicorn / Nginx, Heroku
- **[MIT License](https://github.com/app-generator/license-mit)**
- Free support via **Github** issues tracker
- Paid 24/7 Live Support via [Discord](https://discord.gg/fZC6hup).

> Links

- [Flask App - Illustrations by IraDesign](https://flask-illustrations-iradesign.appseed.us) - LIVE Demo
- [Flask App - Illustrations by IraDesign](https://appseed.us/apps/flask-apps/flask-illustrations-iradesign) - Product page
- [Boierplate Code Flask](https://docs.appseed.us/boilerplate-code/flask/) - Documentation
- More [Flask Apps](https://appseed.us/apps/flask-apps) - index hosted by **[AppSeed](https://appseed.us)**
- [Flask Admin Dashboards](https://appseed.us/admin-dashboards/flask) - index hosted by **[AppSeed](https://appseed.us)**