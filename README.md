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
    - [Fetch Products by Category](#fetch-products-by-category)
    - [Adding Breadcrumbs](#adding-breadcrumbs)
    - [Show Product Details](#show-product-details)
    - [Adding Font Awesome \& Google font](#adding-font-awesome--google-font)
    - [Product Increment \& Decrement (jQuery)](#product-increment--decrement-jquery)
  - [User Authentication](#user-authentication)
    - [User Registration](#user-registration)
    - [Adding Bootstrap in Register Form](#adding-bootstrap-in-register-form)
    - [User Login](#user-login)
    - [Log out](#log-out)
    - [Showing Messages using Alertify JS](#showing-messages-using-alertify-js)

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
    from . import views

    urlpatterns=[
        path('',views.index,name="index"),
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

- Now add `bootstrap.bundle.min.js` script in `body` before `scripts block` so it will be common for each page

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
  from . import views
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns=[
      path('',views.index,name="index"),
      path('collections/',views.collections,name="collections"),
  ]

  if settings.DEBUG:
      urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  - Here `DEBUG` is checked for `MEDIA_URL` and `MEDIA_ROOT`
  - In production `DEBUG` will be `False`

[⬆️ Go to Context](#context)

### Fetch Products by Category

- Update `collections.html` with link `a` tag for each collection

  ```jinja
  {% for item in category %}
      <div class="col-md-3">
          <div class="card">
          <a href="{% url 'collection_view' item.slug %}">
              <div class="card-body">
                  <div class="category-image">
                      <img src="{{item.category_image.url}}" alt="Category image" class="w-100">
                  </div>
                  <h4 class="text-center">{{item.name}}</h4>
              </div>
          </a>
          </div>
      </div>
  {% endfor %}
  ```

- Create a view function `collection_view`

  ```py
  def collection_view(request,slug):
      cat=Category_Model.objects.filter(status='0',slug=slug)
      
      if cat:
          products=Product_Model.objects.filter(category__slug=slug)
          category=cat.first()
          
          context={
              'products':products,
              'category':category,
          }
          return render(request,'store/products/index.html',context)
      else:
          messages.warning(request,"No such category found")
          return redirect('collections')
  ```

  - Checked if the category exists by filtering the `Category_Model` where `status='0'` (indicating it's not hidden) and the `slug` matches the given `slug` parameter.
  - If the category exists:
    - Queried the `Product_Model` to filter all products that belong to the category with the matching `slug` (using the `category__slug` lookup to filter based on the related `Category_Model`).
    - Retrieved the first matching `Category_Model` instance to use as the current category.
    - Prepared a context dictionary containing the filtered products and the category.
    - Rendered the `store/products/index.html` template with the context data.
  - If the category does not exist:
    - Displayed a warning message using Django's messages framework.
    - Redirected the user to the `collections` page.

- Create a html file `index.html` in `store/products/` directory
  
  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}

  <div class="py-3 bg-primary">
      <div class="container">
          <a class="text-white" href="{% url 'index' %}">Home /</a>
          <a class="text-white" href="{% url 'collections' %}">Collections /</a>
          <a class="text-white" href="{% url 'collection_view' category.slug %}">{{category.name}}</a>
      </div>
  </div>

  <div class="container">
      <div class="row">
          <div class="col-md-12">
              <h1>{{category.name}}</h1>
              <hr>
              <div class="row">
                  {% for item in products %}
                      <div class="col-md-3">
                          <div class="card">
                          <a href="{% url 'product_view' item.category.slug item.slug %}">
                              <div class="card-body">
                                  <div class="category-image">
                                      <img src="{{item.product_image.url}}" alt="Category image" class="w-100">
                                  </div>
                                  <h4 class="text-center">{{item.name}}</h4>
                                  <span class="float-start">{{item.selling_price | stringformat:'d'}}</span>
                                  <span class="float-end">{{item.original_price | stringformat:'d'}}</span>
                              </div>
                          </a>
                          </div>
                      </div>
                  {% endfor %}
              </div>
          </div>
      </div>
  </div>
  {% endblock content %}
  ```

  - Here `stringformat` can be set as
    - `d`: Decimal integer.
    - `s`: String.
    - `f`: Fixed-point float.

- Create url pattern for `collection_view`

  ```py
  urlpatterns=[
      ...
      path('collections/<str:slug>',views.collection_view,name="collection_view"),
  ]
  ```

[⬆️ Go to Context](#context)

### Adding Breadcrumbs

- Collection page breadcrumbs
  
  ```html
  <div class="py-3 bg-primary">
      <div class="container">
          <a class="text-white" href="{% url 'index' %}">Home /</a>
          <a class="text-white" href="{% url 'collections' %}">Collections /</a>
          <a class="text-white" href="{% url 'collection_view' category.slug %}">{{category.name}}</a>
      </div>
  </div>
  ...
  ```

- Breadcrumbs text will be underlined so add `text-decoration: none` in `main.html`

  ```html
    <style>
        a{
            text-decoration: none;
        }
    </style>
  ```

[⬆️ Go to Context](#context)

### Show Product Details

- Create url

  ```py
  urlpatterns=[
      ...
      path('collections/<str:cat_slug>/<str:prod_slug>',views.product_view,name="product_view"),
  ]
  ```

- Create view

  ```py
  def product_view(request,cat_slug,prod_slug):
      cat=Category_Model.objects.filter(slug=cat_slug,status="0")
      if cat:
          prod = Product_Model.objects.filter(slug=prod_slug,status="0")
          if prod:
              product=prod.first()
              context={
                  "product":product,
              }
          else:
              messages.error(request,"No such product found")
              return redirect("collections")
      else:
          messages.error(request,"No such category found")
          return redirect("collections")
      return render(request,"store/products/view.html",context)
  ```

- Create html page `view.html` inside `store/products/` directory

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  <div class="py-3 bg-primary">
      <div class="container">
          <a class="text-white" href="{% url 'index' %}">Home /</a>
          <a class="text-white" href="{% url 'collections' %}">Collections /</a>
          <a class="text-white" href="{% url 'collection_view' product.category.slug %}">{{product.category.name}}/</a>
          <a class="text-white" href="{% url 'product_view' product.category.slug product.slug %}">{{product.name}}</a>
      </div>
  </div>

  <div class="py-5">
      <div class="container">
          <div class="row">
              <div class="col-md-12">
                  <div class="card shadow">
                      <div class="card-body">
                          <div class="row">
                              <div class="col-md-4">
                                  {% if product.tag %}
                                      <label class="product-viewtag">{{product.tag}}</label>
                                  {% endif %}
                                  <img src="{{product.product_image.url}}" class="w-100" alt="image">
                              </div>
                              <div class="col-md-8">
                                  <h2 class="mb-0">
                                      {{product.name}}
                                      {% if product.trending %}
                                      <label style="font-size: 16px;" class="float-end badge bg-danger trending_tag"></label>                                        
                                      {% endif %}
                                  </h2>
                                  <hr>
                                  <label class="me-3">Original Price : <s>{{product.original_price | stringformat:"d"}}</s></label>
                                  <label class="fw-bold">Selling Price : {{product.selling_price | stringformat:"d"}}</label>
                                  <p class="mt-3">
                                      {{product.small_description}}
                                  </p>
                                  <hr>
                                  {% if product.quantity > 0 %}
                                      <label class="badge bg-success">In Stock</label>
                                      {% else %}
                                      <label class="badge bg-danger">Out of stock</label>
                                  {% endif %}
                                  <div class="row mt-2">
                                      <div class="col-md-3">
                                          <label for="Quantity">Quantity</label>
                                          <div class="input-group text-center mb-3" style="width: 130px;">
                                          <button class="input-group-text decrement-btn">-</button>
                                          <input type="text" name="quantity" class="form-control text-center" value="1">
                                          <button class="input-group-text increment-btn">+</button>
                                          </div>
                                      </div>
                                      <div class="col-md-9">
                                          <br>
                                          {% if product.quantity > 0 %}
                                              <button type="button" class="btn btn-primary me-3 float-start">Add to Cart <i class="fa fa-shopping-cart"></i></button>
                                          {% endif %}
                                          <button type="button" class="btn btn-success me-3 float-start">Add to Wishlist <i class="fa fa-heart"></i></button>
                                      </div>
                                  </div>
                              </div>
                          </div>
                          <div class="col-md-12">
                              <hr>
                              <h3>Description</h3>
                              <p class="mt-3">
                                  {{product.description}}
                              </p>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
  {% endblock content %}
  ```

- To style the product tag a custom css design added in `main.html`

  ```html
  <!-- Google font  -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
  <style>
    ...
    .product-viewtag{
        background-color: red;
        color: #fff;
        font-size: 11px;
        line-height: 1;
        position: absolute;
        text-align: center;
        text-transform: uppercase;
        top: 22px;
        margin-left: 17.5rem;
        padding: 7px 10px;
        font-weight: 600;
        min-width: 45px;
    }
  </style>
  ```

### Adding Font Awesome & Google font

- Font Awesome
  - Get [FontAwesome cdn](https://cdnjs.com/libraries/font-awesome/)
  - Add it in `main.html` head section

    ```html
    ...
    <!-- font awesome  -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css" integrity="sha512-5Hs3dF2AEPkpNAR7UiOHba+lRSJNeM2ECkwxUIxC1Q/FLycGTbNapWXB4tP889k5T5Ju8fs4b1P5z/iB4nMfSQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    ...
    ```

- Google fonts
  - Go to [Google Fonts](https://fonts.google.com/)
  - Select font and copy the link & css and add it in head section and css style section in `main.html`

  ```html
  <!-- Google font  -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
  <style>
      *{  font-family: "Roboto", sans-serif;
          font-weight: 400;
          font-style: normal;
      }
      a{
          text-decoration: none;
      }
  </style>
  ```

[⬆️ Go to Context](#context)

### Product Increment & Decrement (jQuery)

- Get [jQuery code](https://releases.jquery.com/) minified one `jquery-3.7.1.min.js`
- View the code and copy the content [jquery-3.7.1.min.js](https://code.jquery.com/jquery-3.7.1.min.js)
- Save as `jquery-3.7.1.min.js` in `static\js\jquery-3.7.1.min.js` directory
- Include it in `main.html` before the end of `body` tag

  ```jinja
  <script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
  ```

- Now create another js file in the same directory `custom.js`
- Install [jQuery Code Snippets](https://marketplace.visualstudio.com/items?itemName=donjayamanne.jquerysnippets)
- Now writing `jqdoc`,`jqclick`,`jqfind` will give the code snippet

  ```js
  $(document).ready(function () {
      $('.increment-btn').click(function (e) { 
          e.preventDefault();
          var inc_value=$(this).closest('.product_data').find('.qty-input').val();
          var value=parseInt(inc_value,10);
          value=isNaN(value)?0:value;
          if(value<10){
              value++;
              $(this).closest('.product_data').find('.qty-input').val(value);
          }
      });

      $('.decrement-btn').click(function (e) { 
          e.preventDefault();
          var dec_value=$(this).closest('.product_data').find('.qty-input').val();
          var value=parseInt(dec_value,10);
          value=isNaN(value)?0:value;
          if(value>1){
              value--;
              $(this).closest('.product_data').find('.qty-input').val(value);
          }
      });
  });
  ```

- Include this `custom.js` in `main.html` `body` after `jquery-3.7.1.min.js`

  ```jinja
  <script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>
  <script src="{% static 'js/custom.js' %}"></script>
  ```

[⬆️ Go to Context](#context)

## User Authentication

### User Registration

- In `models.py` import `User`
  - `from django.contrib.auth.models import User`
- Create a new file `forms.py`

  ```py
  from django.contrib.auth.forms import UserCreationForm
  from django import forms
  from .models import User

  class CustomUserForm(UserCreationForm):
      class Meta:
          model=User
          fields = ['username','email','password','password2']
  ```

- Create `register.html` in `store_app/templates/store/auth/register.html` directory
- To make everything organize the view of user registration created in `store_app/controller/authview.py` directory

  ```py
  from django.shortcuts import render,redirect
  from django.contrib import messages
  from store_app.models import *
  from store_app.forms import *

  def register(request):
      form = CustomUserForm()
      context={
          'form':form
      }
      return render(request,'store/auth/register.html',context)
  ```

- Set url in `urls.py`
  - `path('register/',authview.register,name="register"),`

- Now `form` will be visible in `register.html` page with `{{form.as_p}}`

### Adding Bootstrap in Register Form

- Write bootstrap form structure

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}

  <div class="container">
      <div class="row justify-content-center">
          <div class="col-md-6">
              <div class="">
                  <div class="card mt-3 shadow">
                      <div class="card-body">
                          <form action="" method="POST">
                              {% csrf_token %}
                              <div class="text-center">
                                  <h4>Registration form</h4>
                              </div>
                              <hr>
                              <div class="form-group">
                                  <label for="">Username:</label>
                                  {{form.username}}
                                  
                                  {% if form.errors.username %}
                                      <label for="" class="text-danger">{{form.errors.username}}</label>
                                  {% endif %}
                                      
                              </div>
                              <div class="form-group">
                                  <label for="">Email:</label>
                                  {{form.email}}
                                  {% if form.errors.email %}
                                      <label for="" class="text-danger">{{form.errors.email}}</label>
                                  {% endif %}
                              </div>
                              <div class="form-group">
                                  <label for="">Password:</label>
                                  {{form.password1}}
                                  {% if form.errors.password1 %}
                                  <label for="" class="text-danger">{{form.errors.password1}}</label>
                                  {% endif %}
                              </div>
                              <div class="form-group">
                                  <label for="">Confirm Password:</label>
                                  {{form.password2}}
                                  {% if form.errors.password2 %}
                                  <label for="" class="text-danger">{{form.errors.password2}}</label>
                                  {% endif %}
                              </div>
                              <div class="text-center">
                                  <button type="submit" class="btn shadow btn-success px-4">Register</button>
                              </div>
                          </form>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
  {% endblock content %}
  ```

- Go to `forms.py` and add widget

  ```py
  class CustomUserForm(UserCreationForm):
      username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter username'}))
      email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
      password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
      password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm password'}))
      class Meta:
          model=User
          fields = ['username','email','password1','password2']
  ```

[⬆️ Go to Context](#context)

### User Login

- Create `login_page` function in `store_app/controller/authview.py`

  ```py
  def login_page(request):
      if request.user.is_authenticated:
          return redirect('index')
      form = CustomLoginForm()
      if request.method == 'POST':
          form = CustomLoginForm(data=request.POST)
          if form.is_valid():
              user = form.get_user()
              login(request, user)
              messages.success(request, "Login Successful! Welcome back.")
              return redirect('index')
      context = {
          'form': form
      }
      return render(request, 'store/auth/login.html', context)
  ```

- Create url path in `urls.py`
  - `path('login/',authview.login_page,name="login_page"),`

- Create `login.html` html page in `store_app/templates/store/auth/login.html`

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}

  <div class="container">
      <div class="row justify-content-center">
          <div class="col-md-6">
              <div class="">
                  <div class="card mt-3 shadow">
                      <div class="card-body">
                          <form action="" method="POST">
                              {% csrf_token %}
                              <div class="text-center">
                                  <h4>Login Form</h4>
                              </div>
                              <hr>
                              {% if form.non_field_errors %}
                                  <div class="alert alert-danger">
                                      {{ form.non_field_errors }}
                                  </div>
                              {% endif %}
                              <div class="form-group">
                                  <label for="">Username:</label>
                                  {{ form.username }}
                                  {% if form.errors.username %}
                                      <label for="" class="text-danger">{{ form.errors.username }}</label>
                                  {% endif %}
                              </div>
                              <div class="form-group">
                                  <label for="">Password:</label>
                                  {{ form.password }}
                                  {% if form.errors.password %}
                                      <label for="" class="text-danger">{{ form.errors.password }}</label>
                                  {% endif %}
                              </div>
                              <div class="text-center">
                                  <button type="submit" class="btn shadow btn-success px-4">Login</button>
                              </div>
                          </form>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>

  {% endblock content %}
  ```

[⬆️ Go to Context](#context)

### Log out

- Create a view function

  ```py
  def logoutpage(request):
      if request.user.is_authenticated:
          logout(request)
          messages.success(request, "logged out successfully")
          return redirect('index')
      return redirect('index')
  ```

- Add url path `path('logout/',authview.logoutpage,name="logoutpage"),`
- Add `logoutpage` logout button in `navbar.html`

  ```jinja
  ...
  {% if user.is_authenticated %}
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
      {{user}}
    </a>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><hr class="dropdown-divider"></li>
      <li><a class="dropdown-item" href="{% url 'logout_page' %}">Logout</a></li>
    </ul>
  </li>
  {% else %}
  <li class="nav-item">
    <a class="nav-link" href="{% url 'login_page' %}">Login</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'register' %}">Register</a>
  </li>
  {% endif %}
  ...
  ```

  - Here new dropdown added from [bootstrap navbar docs](https://getbootstrap.com/docs/5.3/components/navbar/#supported-content)

[⬆️ Go to Context](#context)

### Showing Messages using [Alertify JS](https://alertifyjs.com/)

- Go to [Alertify JS Guide](https://alertifyjs.com/guide.html)
- Get AlertifyJS CDN in `store_app/templates/store/layouts/main.html`
- Add script in `body`

  ```jinja
  <!-- alertify js  -->
  <script src="//cdn.jsdelivr.net/npm/alertifyjs@1.14.0/build/alertify.min.js"></script>
  ```

- Add css in `head`

  ```html
  <!-- alertify CSS -->
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.14.0/build/css/alertify.min.css"/>
  <!-- alertify Default theme -->
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.14.0/build/css/themes/default.min.css"/>
  ```

- Go to [Notifier position](https://alertifyjs.com/notifier/position.html) section of Alertify JS Components and add the script after cdn

  ```jinja
  <script>
      alertify.set('notifier','position', 'top-right');
      {% for msg in messages %}
      alertify.success('{{msg}}');
      {% endfor %}
  </script>
  ```

[⬆️ Go to Context](#context)
