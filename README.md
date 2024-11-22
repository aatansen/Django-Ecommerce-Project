<div align="center">
<h1>Django Ecommerce Project</h1>
</div>

# Context

- [Context](#context)
  - [Project Setup](#project-setup)
    - [Environment](#environment)
    - [Create Project](#create-project)
    - [MySQL Database setup](#mysql-database-setup)
    - [Set Time Zone](#set-time-zone)
    - [Database Initialize](#database-initialize)
  - [App Setup](#app-setup)
    - [Creating app](#creating-app)
    - [Include App Url in Project Url](#include-app-url-in-project-url)
    - [Creating Templates](#creating-templates)
    - [Adding Bootstrap](#adding-bootstrap)
    - [Setup Include Templates](#setup-include-templates)
    - [Adding First Created index Under Master Template (extends)](#adding-first-created-index-under-master-template-extends)
    - [Final Store App Structure](#final-store-app-structure)
  - [Model, Superuser \& Admin Modify](#model-superuser--admin-modify)
    - [Category \& Product Model](#category--product-model)
    - [Migrate New Model to Database](#migrate-new-model-to-database)
    - [Creating Superuser](#creating-superuser)
    - [Admin Modify](#admin-modify)
  - [Display Product Frontend](#display-product-frontend)
    - [Adding Slider](#adding-slider)
    - [Creating Collection Page](#creating-collection-page)

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

### Set Time Zone

- In `settings.py` edit `TIME_ZONE`
  - `TIME_ZONE = 'Asia/Dhaka'`

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

## Model, Superuser & Admin Modify

### Category & Product Model

- Category model

  ```py
  class Category_Model(models.Model):
      slug = models.CharField(max_length=150, null=True, blank=True)  # Allow null/blank for auto-generation
      name = models.CharField(max_length=150, unique=True, null=False, blank=False)
      category_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
      description = models.TextField(max_length=500, null=False, blank=False)
      status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
      trending = models.BooleanField(default=False, help_text="0=default,1=Trending")
      meta_title = models.CharField(max_length=150, null=False, blank=False)
      meta_keywords = models.CharField(max_length=150, null=False, blank=False)
      meta_description = models.TextField(max_length=500, null=False, blank=False)
      created_at = models.DateTimeField(auto_now_add=True)
      
      def save(self, *args, **kwargs):
          if not self.slug:  # Only generate slug if it's not already set
              self.slug = slugify(self.name)
          super(Category_Model, self).save(*args, **kwargs)
      
      def __str__(self):
          return self.name
  ```

- Product model

  ```py
  class Product_Model(models.Model):
      category = models.ForeignKey(Category_Model, on_delete=models.CASCADE)
      slug = models.CharField(max_length=150, null=True, blank=True)  # Allow null/blank for auto-generation
      name = models.CharField(max_length=150, null=False, blank=False)
      product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
      small_description = models.TextField(max_length=250, null=False, blank=False)
      quantity = models.IntegerField(null=False, blank=False)
      description = models.TextField(max_length=500, null=False, blank=False)
      original_price = models.FloatField(null=False, blank=False)
      selling_price = models.FloatField(null=False, blank=False)
      status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
      trending = models.BooleanField(default=False, help_text="0=default,1=Trending")
      tag = models.CharField(max_length=150, null=False, blank=False)
      meta_title = models.CharField(max_length=150, null=False, blank=False)
      meta_keywords = models.CharField(max_length=150, null=False, blank=False)
      meta_description = models.TextField(max_length=500, null=False, blank=False)
      created_at = models.DateTimeField(auto_now_add=True)
      
      def save(self, *args, **kwargs):
          if not self.slug:  # Generate slug only if it's not set
              base_slug = slugify(self.name)
              slug = base_slug
              counter = 1
              # Check if slug already exists
              while Product_Model.objects.filter(slug=slug).exists():
                  slug = f"{base_slug}-{counter}"
                  counter += 1
              self.slug = slug
          super(Product_Model, self).save(*args, **kwargs)
      
      def __str__(self):
          return self.name
  ```

- Image upload path function

  ```py
  def get_file_path(request, filename):
      original_filename = filename
      now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
      new_filename = f"{now_time}_{original_filename}"  # Concatenate timestamp with the original filename
      return os.path.join('uploads', new_filename)  # Join directory and filename
  ```

- Media,static path define in `settings.py`

  ```py
  STATIC_URL = 'static/'
  MEDIA_URL='/images/'
  MEDIA_ROOT=BASE_DIR/'static'
  STATICFILES_DIRS = [
      BASE_DIR / "static",
  ]
  ```

- Register model in `admin.py`

  ```py
  from django.contrib import admin
  from .models import *

  # Register your models here.
  @admin.register(Category_Model)
  class CategoryModelAdmin(admin.ModelAdmin):
      prepopulated_fields = {"slug": ("name",)}  # Auto-fill slug based on name
      list_display = ("name", "slug", "status", "trending", "created_at")

  @admin.register(Product_Model)
  class ProductModelAdmin(admin.ModelAdmin):
      prepopulated_fields = {"slug": ("name",)}  # Pre-fills slug based on name
      list_display = ("name", "slug", "category", "created_at")
  ```

  - Here `prepopulated_fields` will show the auto generated slug from name field

[⬆️ Go to Context](#context)

### Migrate New Model to Database

- `py manage.py makemigrations`
- `py manage.py migrate`

[⬆️ Go to Context](#context)

### Creating Superuser

- Create superuser
  - `py manage.py createsuperuser`

[⬆️ Go to Context](#context)

### Admin Modify

- Install [django-jazzmin](https://pypi.org/project/django-jazzmin/)
  - `pip install django-jazzmin`
- Add `jazzmin` in `INSTALLED_APPS`

  ```py
  INSTALLED_APPS = [
      'jazzmin',
      ...
  ]
  ```

[⬆️ Go to Context](#context)

## Display Product Frontend

### Adding Slider

- Go to [bootstrap carousel](https://getbootstrap.com/docs/5.3/components/carousel/) and get the `Indicators` one
- Create `slider.html` inside `inc` directory
- Create a folder `images` inside `static` and store `slider1.jpg`

  ```jinja
  {% load static %}
  <div id="carouselExampleIndicators" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="{% static 'images/slider1.jpg' %}" height="400px" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="{% static 'images/slider1.jpg' %}" height="400px" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="{% static 'images/slider1.jpg' %}" height="400px" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
  </div>
  ```

- Include slider in  `index.html`

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  {% include 'store/inc/slider.html' %}
  <h1>Hello world</h1>
  {% endblock content %}
  ```

- Modify navbar to align nav to right side

  ```html
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container">
        ...
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
          ...
          </ul>
        </div>
      </div>
  </nav>
  ```

  - `<div class="container-fluid">` changed to `<div class="container">`
  - `<ul class="navbar-nav">` changed to `<ul class="navbar-nav ms-auto">`

[⬆️ Go to Context](#context)

### Creating Collection Page

- Create `collections.html` file in `store` directory

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  <div class="container">
      <div class="row">
          <div class="col-md-12">
              <h1>Collections</h1>
              <hr>
              <div class="row">
                  {% for item in category %}
                      <div class="col-md-3">
                          <div class="card">
                              <div class="card-body">
                                  <div class="category-image">
                                      <img src="{{item.category_image.url}}" alt="Category image" class="w-100">
                                  </div>
                                  <h4 class="text-center">{{item.name}}</h4>
                              </div>
                          </div>
                      </div>
                  {% endfor %}
              </div>
          </div>
      </div>
  </div>
  {% endblock content %}
  ```

- Create view function
  
  ```py
  from django.shortcuts import render
  from .models import *

  # Create your views here.
  ...
  def collections(request):
      category=Category_Model.objects.filter(status='0')
      
      context={
          'category':category
      }
      return render(request,'store/collections.html',context)
  ```

- Add collection url pattern in `urls.py`

  ```py
  from django.urls import path
  from .views import *
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns=[
      path('',index,name="index"),
      path('collections/',collections,name="collections"),
  ]

  if settings.DEBUG:
      urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  - Here `DEBUG` is checked for `MEDIA_URL` and `MEDIA_ROOT`
  - In production `DEBUG` will be `False`

[⬆️ Go to Context](#context)
