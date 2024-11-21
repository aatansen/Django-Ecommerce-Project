<div align="center">
<h1>Django Ecommerce Project</h1>
</div>

# Context

- [Context](#context)
  - [Project Setup](#project-setup)
    - [Environment](#environment)
    - [Create Project](#create-project)
    - [MySQL Database setup](#mysql-database-setup)
    - [Database Initialize](#database-initialize)
  - [App Setup](#app-setup)
    - [Creating app](#creating-app)
    - [Include App Url in Project Url](#include-app-url-in-project-url)
    - [Creating Templates](#creating-templates)
    - [Adding Bootstrap](#adding-bootstrap)
    - [Setup Include Templates](#setup-include-templates)
    - [Adding First Created index Under Master Template (extends)](#adding-first-created-index-under-master-template-extends)
    - [Final Store App Structure](#final-store-app-structure)

## Project Setup

### Environment

- Create environment
  - `py -m venv env`
- Activate created `env` environment
  - `.\env\Scripts\activate`
- Install Django
  - `pip install django`

[⬆️ Go to Context](#context)

### Create Project

- Creating ecommerce project
  - `django-admin startproject ecommerce_project`

[⬆️ Go to Context](#context)

### MySQL Database setup

- Download and setup [Laragon](https://laragon.org/download/)
- Open Laragon and install phpMyAdmin
  - `Menu-->Tools-->Quick add-->phpmyadmin`
  - Or manually add phpMyAdmin
    - Download [phpMyAdmin](https://www.phpmyadmin.net/downloads/)
    - Create `phpMyAdmin` folder in `laragon\etc\apps` path and unzip the downloaded content 

  > Alternatively [MySQL](https://dev.mysql.com/downloads/installer/) or [XAMPP](https://www.apachefriends.org/download.html) can be used
- Open laragon and start all services
  - Open phpMyAdmin and enter default username:password(`root:''`)
  - Create a database `ecommerce_db`
- Now in django project `settings.py` add created db credentials

  ```py
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'prac_ecommerce_db',
          'USER': 'root',
          'PASSWORD': '',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

- Install [mysqlclient](https://pypi.org/project/mysqlclient/)
  - `pip install mysqlclient`

[⬆️ Go to Context](#context)

### Database Initialize

- Execute command one by one
  - `py manage.py makemigrations`
  - `py manage.py migrate`

  > If setup successfully done the database migrations won't occur any error

[⬆️ Go to Context](#context)

## App Setup

### Creating app

- Create `store_app`
  - `py manage.py startapp store_app`
- Include `store_app` app in `INSTALLED_APPS`

  ```py
  INSTALLED_APPS = [
      ...
      'store_app'
  ]
  ```

[⬆️ Go to Context](#context)

### Include App Url in Project Url

- Create a new file `urls.py` in `store_app` app

  ```py
  from django.urls import path

  urlspatterns=[
      path()
  ]
  ```

- Include app url in project

  ```py
  from django.contrib import admin
  from django.urls import path,include

  urlpatterns = [
      ...
      path('',include('store_app.urls')),
  ]
  ```

[⬆️ Go to Context](#context)

### Creating Templates

- Create `templates` in `store_app` app directory
- Create another folder in that `templates` directory `store` with a html file `index.html`
  
  ```txt
  📁templates
  └── 📁store
      └── index.html
    ```

- Now render that `index.html` file
  - In `store_app`'s `views.py` create a function to render it

    ```py
    from django.shortcuts import render

    # Create your views here.
    def index(request):
        return render(request,'store/index.html')
    ```

  - Set url in `store_app`'s `urls.py`

    ```py
    from django.urls import path
    from .views import *

    urlpatterns=[
        path('',index,name="index")
    ]
    ```

  - Open `http://127.0.0.1:8000/` in browser to see the content of `index.html`

[⬆️ Go to Context](#context)

### Master Template Setup

- Create a new folder `layouts` in `store` directory with `main.html`

  ```txt
  📁templates
  └── 📁store
      └── 📁layouts
          └── main.html
  ```

- `main.html` structure

  ```jinja
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>
      {% block title %}
          
      {% endblock title %}
      </title>
  </head>
  <body>
      {% block content %}
          
      {% endblock content %}


      {% block scripts %}
      
      {% endblock scripts %}
  </body>
  </html>
  ```

[⬆️ Go to Context](#context)

### Adding Bootstrap

- Go to [bootstrap website](https://getbootstrap.com/) and get cdn
- Add `bootstrap.min.css` style sheet in head section of `main.html`

  ```jinja
  <head>
      ...
      <title>
      {% block title %}
          
      {% endblock title %}
      </title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  ```

- Now add `bootstrap.bundle.min.js` script before `scripts block` so it will be common for each page

  ```jinja
  <body>
      {% block content %}
          
      {% endblock content %}
      
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

      {% block scripts %}
      
      {% endblock scripts %}
  </body>
  ```

[⬆️ Go to Context](#context)

### Setup Include Templates

- Create a new folder `inc` in `store_app`'s `templates` with `navbar.html`
  
  ```txt
  📁templates
  └── 📁store
      └── 📁inc
          └── navbar.html
  ```

- Get navbar from [bootstrap docs](https://getbootstrap.com/docs/5.3/components/navbar/)
- Now include `navbar.html` in `main.html`

  ```jinja
  <body>
      {% include 'store/inc/navbar.html' %}
      {% block content %}

      {% endblock content %}
      ...
  </body>
  ```

[⬆️ Go to Context](#context)

### Adding First Created index Under Master Template (extends)

- Use `extends` template tag in `index.html` to extends the `main.html` master template in it

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  <h1>Hello world</h1>
  {% endblock content %}
  ```

[⬆️ Go to Context](#context)

### Final Store App Structure

- This will be the structure of the `store_app` app till now

  ```txt
  └── 📁store_app
      └── 📁migrations
          └── 📁__pycache__
              └── __init__.cpython-312.pyc
          └── __init__.py
      └── 📁templates
          └── 📁store
              └── 📁inc
                  └── navbar.html
              └── 📁layouts
                  └── main.html
              └── index.html
      └── __init__.py
      └── admin.py
      └── apps.py
      └── models.py
      └── tests.py
      └── urls.py
      └── views.py
  ```

[⬆️ Go to Context](#context)
