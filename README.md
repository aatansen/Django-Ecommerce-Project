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
    - [Get Absolute Url Note](#get-absolute-url-note)
    - [Adding Font Awesome \& Google font](#adding-font-awesome--google-font)
    - [Product Increment \& Decrement (jQuery)](#product-increment--decrement-jquery)
  - [User Authentication](#user-authentication)
    - [User Registration](#user-registration)
    - [Adding Bootstrap in Register Form](#adding-bootstrap-in-register-form)
    - [User Login](#user-login)
    - [Log out](#log-out)
  - [Showing Django Messages using Alertify JS](#showing-django-messages-using-alertify-js)
  - [Product Cart](#product-cart)
    - [Add to Cart using JQuery Ajax](#add-to-cart-using-jquery-ajax)
    - [Display Cart Item](#display-cart-item)
    - [Update Product Quantity in Cart](#update-product-quantity-in-cart)
    - [Remove Item from Cart](#remove-item-from-cart)
  - [Product Wishlist](#product-wishlist)
    - [Wishlist View Page](#wishlist-view-page)
    - [Add to Wishlist jQuery Ajax](#add-to-wishlist-jquery-ajax)
    - [Remove Item from Wishlist](#remove-item-from-wishlist)
  - [Navbar Item Active](#navbar-item-active)
  - [Product Checkout](#product-checkout)
    - [Adding Checkout Page](#adding-checkout-page)
    - [Adding Custom CSS](#adding-custom-css)
    - [Create Order and Order functionality](#create-order-and-order-functionality)
    - [Auto Fill User Data in Checkout (Profile Model)](#auto-fill-user-data-in-checkout-profile-model)
  - [User Order Page](#user-order-page)
    - [Display Order Products](#display-order-products)
    - [View Ordered Product Details](#view-ordered-product-details)
  - [Chat Features](#chat-features)
    - [Integrate Whatsapp Chat Feature](#integrate-whatsapp-chat-feature)
    - [Integrate Live Chat (tawk.to)](#integrate-live-chat-tawkto)
  - [Search Feature with Autocomplete](#search-feature-with-autocomplete)

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
  
  ```jinja
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

### Get Absolute Url Note

> [!NOTE]
> Here in `a tag` we set url for collection view `{% url 'collection_view' item.slug %}`
>
> We can use `get_absolute_url`
>
> ```py
> def get_absolute_url(self):
>     return reverse('collection_view', kwargs={'slug': self.slug})
>  ```
>
> Now we can access url `{{ item.get_absolute_url }}`
>
> Similarly for product view `get_absolute_url` can be setup for `a tag` in product model
>
> ```py
> def get_absolute_url(self):
>     return reverse('product_view', kwargs={'cat_slug': self.category.slug, 'prod_slug': self.slug})
> ```

[⬆️ Go to Context](#context)

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

## Showing Django Messages using [Alertify JS](https://alertifyjs.com/)

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

## Product Cart

### Add to Cart using JQuery Ajax

- Create `Cart_Model` model in `models.py`

  ```py
  class Cart_Model(models.Model):
      user=models.ForeignKey(User, on_delete=models.CASCADE)
      product=models.ForeignKey(Product_Model, on_delete=models.CASCADE)
      product_qty=models.IntegerField(null=False,blank=False)
      created_at=models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return f"{self.user} added {self.product_qty} of {self.product} in cart"
  ```

- Register `Cart_Model` in `admin.py`
- Migrate database
- Open `store_app/templates/store/products/view.html` and add `addToCartBtn` class in Add to cart button
- Now open `custom.js` and get `addToCartBtn` class using `jqclick` snippet
- Get value of product id & quantity using `jqvalget` snippet
- Write ajax using `jqajax` snippet

  ```js
  // add to cart button functionality
  $('.addToCartBtn').click(function (e) { 
      e.preventDefault();
      var product_id=$(this).closest('.product_data').find('.prod_id').val();
      var product_qty=$(this).closest('.product_data').find('.qty-input').val();
      var token=$('input[name=csrfmiddlewaretoken]').val();
      $.ajax({
          method: "POST",
          url: "/add-to-cart/",
          data: {
              'product_id':product_id,
              'product_qty':product_qty,
              csrfmiddlewaretoken: token,
          },
          success: function (response) {
              console.log(response);
              alertify.success(response.status)
          }
      });
  });
  ```

- Make sure `csrf_token` is written in product view html page
- Create url path `add-to-cart/` in `urls.py` which is mentioned in Ajax `url`
- Create view function `add_to_cart` in `store_app/controller/cart.py`

  ```py
  from django.shortcuts import render,redirect
  from django.http import JsonResponse
  from store_app.models import *

  def add_to_cart(request):
      if request.method=='POST':
          if request.user.is_authenticated:
              prod_id=int(request.POST.get('product_id'))
              product_check=Product_Model.objects.get(id=prod_id)
              if product_check:
                  if Cart_Model.objects.filter(user=request.user,product_id=prod_id):
                      return JsonResponse({'status':"Product already in cart"})
                  else:
                      prod_qty=int(request.POST.get('product_qty'))
                      if product_check.quantity>=prod_qty:
                          Cart_Model.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                          return JsonResponse({'status':"Product added successfully"})
                      else:
                          return JsonResponse({'status':f"Only {product_check.quantity} item is available"})
              else:
                  return JsonResponse({'status':"No such product found"})
          else:
              return JsonResponse({'status':"Login to Continue"})
      
      return redirect('index')
  ```

[⬆️ Go to Context](#context)

### Display Cart Item

- Add cart in `store_app/templates/store/inc/navbar.html` navbar

  ```jinja
  <li class="nav-item">
    <a class="nav-link" href="{% url 'cart_view' %}">Cart</a>
  </li>
  ```

- Create url path for `cart_view`
  - path('cart/',cart.cart_view,name="cart_view"),
- Create view function in `store_app/controller/cart.py`

  ```py
  ...
  from django.contrib.auth.decorators import login_required
  ...

  @login_required(login_url='login_page')
  def cart_view(request):
      cart=Cart_Model.objects.filter(user=request.user)
      context={
          'cart':cart,
      }
      return render(request,'store/cart.html',context)
  ```

  - Here `login_required` decorator is used to show the cart only login user

- Create html page for cart `store_app/templates/store/cart.html`

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  <div class="py-3 bg-primary">
      <div class="container">
          <a class="text-white" href="{% url 'index' %}">Home /</a>
          <a class="text-white" href="{% url 'cart_view' %}">Cart /</a>
      </div>
  </div>

  <div class="py-5">
      <div class="container">
          <div class="row">
              <div class="col-md-12">
                  <div class="card shadow">
                      <div class="card-body">
                          {% if cart %}
                              {% for item in cart %}
                                  <div class="row product_data">
                                      <div class="col-md-2 my-auto">
                                          <img src="{{item.product.product_image.url}}" height="70px" width="70px" alt="product image">
                                      </div>
                                      <div class="col-md-3 my-auto">
                                          <h6>{{item.product.name}}</h6>
                                      </div>
                                      <div class="col-md-2 my-auto">
                                          <h6>$ {{item.product.selling_price}}</h6>
                                      </div>
                                      <div class="col-md-3 my-auto">
                                          <input type="hidden" class="prod_id" value="{{item.product_id}}">
                                          {% csrf_token %}
                                          {% if item.product.quantity >= item.product_qty %}
                                              <label for="Quantity">Quantity</label>
                                              <div class="input-group text-center mb-3" style="width: 130px;">
                                                  <button class="input-group-text decrement-btn">-</button>
                                                  <input type="text" name="quantity" class="form-control qty-input text-center" value="1">
                                                  <button class="input-group-text increment-btn">+</button>
                                              </div>
                                              {% else %}
                                              <h6>Out of Stock</h6>
                                          {% endif %}
                                      </div>
                                      <div class="col-md-2 my-auto">
                                          <button class="btn btn-danger delete-cart-item"> <i class="fa fa-trash"></i> Remove</button>
                                      </div>
                                  </div>
                              {% endfor %}
                          {% else %}
                              <h4>Your cart is empty</h4>
                          {% endif %}
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
  {% endblock content %}
  ```

  - It is similar to `view.html` of the product
  - `product_data` class should be inside for loop otherwise increment and decrement won't work properly
  - JS functionalities are written in `static/js/custom.js` file

[⬆️ Go to Context](#context)

### Update Product Quantity in Cart

- Add new class in increment and decrement button `changeQuantity`
- Open `static/js/custom.js` and write exact same as add to cart functionality where class name is changed to `changeQuantity`

  ```js
  // update and change the quantity of the product
  $('.changeQuantity').click(function (e) { 
      e.preventDefault();
      var product_id=$(this).closest('.product_data').find('.prod_id').val();
      var product_qty=$(this).closest('.product_data').find('.qty-input').val();
      var token=$('input[name=csrfmiddlewaretoken]').val();
      $.ajax({
          method: "POST",
          url: "/update-cart/",
          data: {
              'product_id':product_id,
              'product_qty':product_qty,
              csrfmiddlewaretoken: token,
          },
          success: function (response) {
              console.log(response);
              alertify.success(response.status)
          }
      });
  });
  ```

- Create url path for `update-cart/` in `urls.py`
- `path('update-cart/',cart.update_cart,name="update_cart"),`
- Create view in `store_app/controller/cart.py`

  ```py
  def update_cart(request):
      if request.method == 'POST':
          prod_id = int(request.POST.get('product_id'))
          prod_qty = int(request.POST.get('product_qty'))
          
          # Check if the product exists in the cart for the user
          if Cart_Model.objects.filter(user=request.user, product_id=prod_id).exists():
              cart = Cart_Model.objects.get(product_id=prod_id, user=request.user)
              product = Product_Model.objects.get(id=prod_id)
              
              # Check if the requested quantity is available
              if product.quantity >= prod_qty:
                  cart.product_qty = prod_qty
                  cart.save()
                  return JsonResponse({'status': "Updated Successfully"})
              else:
                  return JsonResponse({'status': f"Sorry, only {product.quantity} units are available"})

          return JsonResponse({'status': "Product not found in cart"})
      
      return redirect('index')
  ```

[⬆️ Go to Context](#context)

### Remove Item from Cart

- Using `delete-cart-item` class create ajax click function in `static/js/custom.js`

  ```js
  $('.delete-cart-item').click(function (e) { 
      e.preventDefault();
      var product_id=$(this).closest('.product_data').find('.prod_id').val();
      var token=$('input[name=csrfmiddlewaretoken]').val();

      $.ajax({
          method: "POST",
          url: "/delete-cart-item/",
          data: {
              'product_id':product_id,
              csrfmiddlewaretoken:token,
          },
          success: function (response) {
              alertify.success(response.status)

              // reload only card body on remove item 
              $('.card-data').load(location.href+" .card-data");
          }
      });
  });
  ```

  - Here we get the product id and token for POST method
  - For show the updated page `card-data` class is used to reload the section of card body only not whole page

- Create `delete-cart-item/` url in `urls.py`
  - `path('delete-cart-item/',cart.delete_cart_item,name="delete_cart_item"),`
- Create view in `store_app/controller/cart.py`

> [!NOTE]
>
> Note that this won't work properly when multiple item occur. `jqon` instead of `jqclick` can be used to solve this issue
>
>```js
>  $(document).on('click','.delete-cart-item', function (e) {
>    //...rest of the code remain same
>  });
>```
>
> In future code implementation `jqclick` is fixed using different way for both cart & wish list delete

  ```py
  def delete_cart_item(request):
      if request.method=='POST':
          if request.user.is_authenticated:
              prod_id=int(request.POST.get('product_id'))
              cart_check=Cart_Model.objects.filter(user=request.user,product_id=prod_id).exists()
              if cart_check:
                  cart_item=Cart_Model.objects.get(user=request.user,product_id=prod_id)
                  cart_item.delete()
                  return JsonResponse({'status': "Item removed successfully"})
          else:
              return JsonResponse({'status': "Login to continue"})
      return redirect('index')
  ```

[⬆️ Go to Context](#context)

## Product Wishlist

### Wishlist View Page

- Create wishlist model `Wishlist_Model`

  ```py
  class Wishlist_Model(models.Model):
      user=models.ForeignKey(User, on_delete=models.CASCADE)
      product=models.ForeignKey(Product_Model, on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return f"{self.user} added {self.product} to their Wishlist"
  ```

- Register in `admin.py`
  - `admin.site.register(Wishlist_Model)`
- Create `store_app/controller/wishlist.py`

  ```py
  from django.shortcuts import render,redirect
  from django.http import JsonResponse
  from django.contrib.auth.decorators import login_required
  from store_app.models import *

  @login_required(login_url='login_page')
  def wishlist_view(request):
      wishlist=Wishlist_Model.objects.filter(user=request.user)
      context={
          'wishlist':wishlist,
      }
      return render(request,'store/wishlist.html',context)
  ```

- Create url path in `urls.py`
  - `path('wishlist/',wishlist.wishlist_view,name="wishlist_view"),`

- Create `store_app/templates/store/wishlist.html` page

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  <div class="py-3 bg-primary">
      <div class="container">
          <a class="text-white" href="{% url 'index' %}">Home /</a>
          <a class="text-white" href="{% url 'wishlist_view' %}">Wishlist /</a>
      </div>
  </div>

  <div class="py-5">
      <div class="container">
          <div class="row">
              <div class="col-md-12">
                  <div class="card shadow">
                      <div class="card-body card-data">
                          {% if wishlist %}
                              {% for item in wishlist %}
                                  <div class="row product_data">
                                      <div class="col-md-2 my-auto">
                                          <img src="{{item.product.product_image.url}}" height="70px" width="70px" alt="product image">
                                      </div>
                                      <div class="col-md-3 my-auto">
                                          <h6>{{item.product.name}}</h6>
                                      </div>
                                      <div class="col-md-2 my-auto">
                                          <h6>$ {{item.product.selling_price}}</h6>
                                      </div>
                                      <div class="col-md-3 my-auto">
                                          <input type="hidden" class="prod_id" value="{{item.product_id}}">
                                          {% csrf_token %}
                                          <a href="{% url 'product_view' item.product.category.slug item.product.slug %}" target="_blank" class="btn btn-primary"> <i class="fa fa-eye"></i> View product</a>
                                      </div>
                                      <div class="col-md-2 my-auto">
                                          <button class="btn btn-danger delete-wishlist-item"> <i class="fa fa-trash"></i> Remove</button>
                                      </div>
                                  </div>
                              {% endfor %}
                          {% else %}
                              <h4>Your wishlist is empty</h4>
                          {% endif %}
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>

  {% endblock content %}
  ```

[⬆️ Go to Context](#context)

### Add to Wishlist jQuery Ajax

- Create add functionalities in `static/js/custom.js`

  ```js
  // add to wishlist button functionality
  $('.addToWishlistBtn').click(function (e) { 
      e.preventDefault();
      var product_id=$(this).closest('.product_data').find('.prod_id').val();
      var token=$('input[name=csrfmiddlewaretoken]').val();
      $.ajax({
          method: "POST",
          url: "/add-to-wishlist/",
          data: {
              'product_id':product_id,
              csrfmiddlewaretoken: token,
          },
          success: function (response) {
              alertify.success(response.status)
          }
      });
  });
  ```

- Create view in `store_app/controller/wishlist.py`

  ```py
  def add_to_wishlist(request):
      if request.method=='POST':
          if request.user.is_authenticated:
              prod_id=int(request.POST.get('product_id'))
              product_check=Product_Model.objects.get(id=prod_id)
              if product_check:
                  wish_item=Wishlist_Model.objects.filter(user=request.user,product_id=prod_id)
                  if wish_item.exists():
                      return JsonResponse({'status': "Item already in wishlist"})
                  else:
                      wish=Wishlist_Model.objects.create(user=request.user,product_id=prod_id)
                      wish.save()
                      return JsonResponse({'status': "Item Added to wishlist"})
              else:
                  return JsonResponse({'status': "No such product found"})
                  
      return redirect('index')
  ```

- Add url path `path('add-to-wishlist/',wishlist.add_to_wishlist,name="add_to_wishlist"),`

[⬆️ Go to Context](#context)

### Remove Item from Wishlist

- Add delete functionality in `static/js/custom.js`

  ```js
  // delete wishlist item
  $('.delete-wishlist-item').click(function (e) {
      e.preventDefault();

      // Cache the specific wishlist item row and CSRF token
      var $wishlistItem = $(this).closest('.product_data');
      var product_id = $wishlistItem.find('.prod_id').val();
      var token = $('input[name=csrfmiddlewaretoken]').val();

      // Send AJAX request to delete the item
      $.ajax({
          method: "POST",
          url: "/delete-wishlist-item/",
          data: {
              'product_id': product_id,
              csrfmiddlewaretoken: token,
          },
          success: function (response) {
              // Show success message
              alertify.success(response.status);

              // Remove the specific wishlist item row from the DOM
              $wishlistItem.remove();

              // Check if the wishlist is now empty and display a message
              if ($('.product_data').length === 0) {
                  $('.card-data').html('<h4>Your wishlist is empty</h4>');
              }
          },
          error: function () {
              alertify.error("Failed to remove the item. Please try again.");
          }
      });
  });
  ```

- Create view function for `delete_wishlist_item` inside `wishlist.py`

  ```py
  def delete_wishlist_item(request):
      if request.method=='POST':
          if request.user.is_authenticated:
              prod_id=int(request.POST.get('product_id'))
              wishlist_check=Wishlist_Model.objects.filter(user=request.user,product_id=prod_id)
              if wishlist_check:
                  wishlist_item=Wishlist_Model.objects.get(user=request.user,product_id=prod_id)
                  wishlist_item.delete()
                  return JsonResponse({'status': "Product removed from wishlist"})
              else:
                  return JsonResponse({'status': "Product not found in wishlist"})
          else:
              return JsonResponse({'status': "Login to continue"})
      return redirect('index')
  ```

- Add url path `path('delete-wishlist-item/',wishlist.delete_wishlist_item,name="delete_wishlist_item"),`

[⬆️ Go to Context](#context)

## Navbar Item Active

- Using `resolver_match` url name

  ```jinja
  ...
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'index' %}active{% endif %}" aria-current="page" href="{% url 'index' %}">Home</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'collections' %}active{% endif %}" href="{% url 'collections' %}">Collections</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'cart_view' %}active{% endif %}" href="{% url 'cart_view' %}">Cart</a>
  </li>
  <li class="nav-item">
    <a class="nav-link {% if request.resolver_match.url_name == 'wishlist_view' %}active{% endif %}" href="{% url 'wishlist_view' %}">Wishlist</a>
  </li>
  ...
  ```

  > We can also use request.path where directly path is given `request.path == '/'`

- To hightlist the active nav font bold style is added in master template style section

  ```css
  .active{
      font-weight: 800;
  }
  ```

[⬆️ Go to Context](#context)

## Product Checkout

### Adding Checkout Page

- Add checkout button in `cart.html`
  - `<a href="{% url 'checkout_view' %}" class="btn btn-outline-success">Checkout</a>`
- Create url path for `checkout_view`
  - `path('checkout/',checkout.checkout_view,name="checkout_view"),`
- Create view function in `store_app/controller/checkout.py`

  ```py
  from django.shortcuts import render,redirect
  from django.contrib.auth.decorators import login_required
  from store_app.models import *

  def checkout_view(request):
      rawCart=Cart_Model.objects.filter(user=request.user)
      for item in rawCart:
          if item.product_qty>item.product.quantity:
              Cart_Model.objects.delete(id=item.id)
      cartItems=Cart_Model.objects.filter(user=request.user)
      total_price=0
      for item in cartItems:
          total_price=total_price+item.product.selling_price*item.product_qty

      context={
          'cartItems':cartItems,
          'total_price':total_price,
      }
      return render(request,'store/checkout.html',context)
  ```

  > This is initial view for cart, this will be extended with user information
- Create html page

  ```jinja
  {% extends 'store/layouts/main.html' %}

  {% block content %}
  <div class="py-3 bg-primary">
      <div class="container">
          <a class="text-white" href="{% url 'index' %}">Home /</a>
          <a class="text-white" href="{% url 'checkout_view' %}">Checkout /</a>
      </div>
  </div>

  <div class="container mt-3">
      <div class="row">
          <div class="col-md-7">
              <div class="card shadow">
                  <div class="card-body">
                      <h6>Basic Details</h6>
                      <hr>
                      <div class="row">
                          <div class="col-md-6">
                              <label for="">First Name</label>
                              <input type="text" class="form-control" placeholder="Enter first name">
                          </div>
                          <div class="col-md-6">
                              <label for="">Last Name</label>
                              <input type="text" class="form-control" placeholder="Enter last name">
                          </div>
                          <div class="col-md-6 mt-2">
                              <label for="">Phone</label>
                              <input type="text" class="form-control" placeholder="Enter Phone">
                          </div>
                          <div class="col-md-12 mt-2">
                              <label for="">Address</label>
                              <textarea class="form-control" placeholder="Enter Address"></textarea>
                          </div>
                          <div class="col-md-6 mt-2">
                              <label for="">City</label>
                              <input type="text" class="form-control" placeholder="Enter City">
                          </div>
                          <div class="col-md-6 mt-2">
                              <label for="">State</label>
                              <input type="text" class="form-control" placeholder="Enter State">
                          </div>
                          <div class="col-md-6 mt-2">
                              <label for="">Country</label>
                              <input type="text" class="form-control" placeholder="Enter Country">
                          </div>
                          <div class="col-md-6 mt-2">
                              <label for="">Pin Code</label>
                              <input type="text" class="form-control" placeholder="Enter Pin Code">
                          </div>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col-md-5">
              <div class="card shadow">
                  <div class="card-body">
                      <h6>Order Summary</h6>
                      <hr>
                      {% if cartItems %}
                          <table class="table table-stripeds table-bordereds">
                              <thead>
                                  <tr>
                                      <th>Product Image</th>
                                      <th>Product</th>
                                      <th>Qty.</th>
                                      <th>Price</th>
                                  </tr>
                              </thead>
                              <tbody>
                                  
                                  {% for item in cartItems %}
                                      <tr>
                                          <td>
                                              <img src="{{item.product.product_image.url}}" height="50px" width="50px" class="me-2" alt="">
                                          </td>
                                          <td>{{item.product.name}}</td>
                                          <td>{{item.product_qty}}</td>
                                          <td>$ {{item.product.selling_price}}</td>
                                      </tr>
                                  {% endfor %}
                              </tbody>
                          </table>
                          <h6 class="fw-bold">Grand Total
                              <span class="float-end fw-bold">$ {{total_price}} </span>
                          </h6>
                          <div class="mt-3">
                              <a href="" class="btn btn-success w-100">COD | Place Order</a>
                          </div>
                      {% else %}
                          <h4>Your cart is empty</h4>
                      {% endif %}
                  </div>
              </div>
          </div>
      </div>
  </div>

  {% endblock content %}
  ```

[⬆️ Go to Context](#context)

### Adding Custom CSS

- Create a class in `store_app/templates/store/checkout.html`
  - `<div class="card shadow checkoutform">`
- Create `static/css/custom.css`

  ```css
    .checkoutform label{
        font-size: 14px;
        font-weight: 600;
    }

    .checkoutform input{
        font-size: 14px;
    }
  ```

- Now add this `custom.css` in master template `main.html`

    ```jinja
    ...
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
    ...
    ```

[⬆️ Go to Context](#context)

### Create Order and Order functionality

- Order Model

  ```py
  class Order_Model(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      fname=models.CharField(max_length=150,null=False)
      lname=models.CharField(max_length=150,null=False)
      email=models.CharField(max_length=150,null=False)
      phone=models.CharField(max_length=150,null=False)
      address=models.TextField(null=False)
      city=models.CharField(max_length=150,null=False)
      state=models.CharField(max_length=150,null=False)
      country=models.CharField(max_length=150,null=False)
      pin_code=models.CharField(max_length=150,null=False)
      total_price=models.FloatField(null=False)
      payment_mode=models.CharField(max_length=150,null=False)
      payment_id=models.CharField(max_length=250,null=True)
      order_statuses=(
          ('Pending','Pending'),
          ('Out For Shipping','Out For Shipping'),
          ('Completed','Completed'),
      )
      status=models.CharField(max_length=150,choices=order_statuses,default=order_statuses[0][1])
      message=models.TextField(null=True)
      tracking_no=models.CharField(max_length=150,null=True)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return f"{self.id} - {self.tracking_no}"
  ```

- Order Item Model

  ```py
  class Order_Item_Model(models.Model):
      order=models.ForeignKey(Order_Model,on_delete=models.CASCADE)
      product=models.ForeignKey(Product_Model,on_delete=models.CASCADE)
      price=models.FloatField(null=False)
      quantity=models.IntegerField(null=False)
      
      def __str__(self):
          return f"{self.order.id} - {self.order.tracking_no}"
  ```

- Edit `store_app/templates/store/checkout.html` and add form tag with name attributes in each field

- Creating url for placing order
  - `path('place-order/',checkout.place_order,name="place_order"),`
- Creating view for placing order in `store_app/controller/checkout.py`

  ```py
  @login_required(login_url='login_page')
  def place_order(request):
      if request.method=="POST":
          new_order = Order_Model()
          new_order.user = request.user
          new_order.fname = request.POST.get('fname')
          new_order.lname = request.POST.get('lname')
          new_order.email = request.POST.get('email')
          new_order.phone = request.POST.get('phone')
          new_order.address = request.POST.get('address')
          new_order.city = request.POST.get('city')
          new_order.state = request.POST.get('state')
          new_order.country = request.POST.get('country')
          new_order.pin_code = request.POST.get('pin_code')

          new_order.payment_mode = request.POST.get('payment_mode')
          
          cart = Cart_Model.objects.filter(user=request.user)
          cart_total_price=0
          for item in cart:
              cart_total_price=cart_total_price+item.product.selling_price*item.product_qty
          new_order.total_price = cart_total_price
          
          new_order.tracking_no = str(uuid.uuid4())
          new_order.save()
          
          new_order_items=Cart_Model.objects.filter(user=request.user)
          for item in new_order_items:
              Order_Item_Model.objects.create(
                  order=new_order,
                  product=item.product,
                  price=item.product.selling_price,
                  quantity=item.product_qty,
              )
              
              # To decrease the product quantity from available stock
              order_product = Product_Model.objects.filter(id=item.product_id).first()
              order_product.quantity=order_product.quantity - item.product_qty
              order_product.save()
              
          # clear user cart
          Cart_Model.objects.filter(user=request.user).delete()
          messages.success(request,'Your order has been place successfully')

      return redirect('/')
  ```

  - Here we can also use old ways of creating tracking no (but using `uuid` is recommended)

    ```py
    track_no = 'aatansen' + str(random.randint(1111111, 9999999))
    while Order_Model.objects.filter(tracking_no=track_no).exists():  # Check if it exists
        track_no = 'aatansen' + str(random.randint(1111111, 9999999))  # Generate a new one
    new_order.tracking_no = track_no
    ```

[⬆️ Go to Context](#context)

### Auto Fill User Data in Checkout (Profile Model)

- Create and register a profile model `Profile_Model`

    ```py
    class Profile_Model(models.Model):
        user=models.OneToOneField(User,on_delete=models.CASCADE)
        phone=models.CharField(max_length=150,null=False)
        address=models.TextField(null=False)
        city=models.CharField(max_length=150,null=False)
        state=models.CharField(max_length=150,null=False)
        country=models.CharField(max_length=150,null=False)
        pin_code=models.CharField(max_length=150,null=False)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return f"{self.user.username} - {self.user.email}"
    ```

- In `store_app/controller/checkout.py` file edit `place_order` function to save user info in `Profile_Model`

    ```py
    @login_required(login_url='login_page')
    def place_order(request):
        if request.method=="POST":
            
            current_user=User.objects.filter(id=request.user.id).first()
            if not current_user.first_name:
                current_user.first_name=request.POST.get('fname')
                current_user.last_name=request.POST.get('lname')
                current_user.save()
            
            if not Profile_Model.objects.filter(user=request.user).exists():
                user_profile=Profile_Model()
                user_profile.user=request.user            
                user_profile.phone = request.POST.get('phone')
                user_profile.address = request.POST.get('address')
                user_profile.city = request.POST.get('city')
                user_profile.state = request.POST.get('state')
                user_profile.country = request.POST.get('country')
                user_profile.pin_code = request.POST.get('pin_code')
                user_profile.save()
            
            ...
        return redirect('/')
    ```

- Now return the profile model data in checkout page

    ```py
    def checkout_view(request):
        ...
        user_profile=Profile_Model.objects.filter(user=request.user).first()
        
        context={
            ...
            'user_profile':user_profile,
        }
        return render(request,'store/checkout.html',context)
    ```

- In `store_app/templates/store/checkout.html` use value attribute to show the user profile data

[⬆️ Go to Context](#context)

## User Order Page

### Display Order Products

- Add order view in `store_app/controller/orders.py`

    ```py
    @login_required(login_url='login_page')
    def my_orders(request):
        orders=Order_Model.objects.filter(user=request.user)
        
        context={
            "orders":orders,
        }
        return render(request,'store/orders/index.html',context)
    ```

- Add url path in `urls.py`
  - `path('orders/',orders.my_orders,name="my_orders"),`

- Create `store_app/templates/store/orders/index.html`

    ```jinja
    {% extends 'store/layouts/main.html' %}

    {% block content %}
    <div class="py-3 bg-primary">
        <div class="container">
            <a class="text-white" href="{% url 'index' %}">Home /</a>
            <a class="text-white" href="{% url 'my_orders' %}">Orders /</a>
        </div>
    </div>

    <div class="container mt-3">
        <div class="row">
            <div class="col-md-12">
                <div class="card shadow">
                <div class="card-header">
                    <h3 class="mb-0">My Orders</h3>
                </div>
                    <div class="card-body">
                        <table class="table table-bordered">
                            <thead>
                                <tr>
                                    <th>Order Date</th>
                                    <th>Tracking No</th>
                                    <th>Total Price</th>
                                    <th>Status</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for item in orders %}
                                <tr>
                                    <td>{{item.created_at}}</td>
                                    <td>{{item.tracking_no}}</td>
                                    <td>$ {{item.total_price}}</td>
                                    <td>{{item.status}}</td>
                                    <td>
                                        <a href="{% url 'view_order' item.tracking_no %}" class="btn btn-primary">View</a>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    {% endblock content %}
    ```

- Adding order navigation in navbar drop down

    ```jinja
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="{% url 'my_orders' %}">My Orders</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="{% url 'logout_page' %}">Logout</a></li>
    </ul>
    ```

[⬆️ Go to Context](#context)

### View Ordered Product Details

- Create view function in `store_app/controller/orders.py`

    ```py
    @login_required(login_url='login_page')
    def view_order(request,tr_no):
        order=Order_Model.objects.filter(tracking_no=tr_no).filter(user=request.user).first()
        orderItems=Order_Item_Model.objects.filter(order=order)
        context={
            "order":order,
            "orderItems":orderItems,
        }
        return render(request,'store/orders/view.html',context)
    ```

- Create html page `store_app/templates/store/orders/view.html`

    ```jinja
    {% extends 'store/layouts/main.html' %}

    {% block content %}
    <div class="py-3 bg-primary">
        <div class="container">
            <a class="text-white" href="{% url 'index' %}">Home /</a>
            <a class="text-white" href="{% url 'my_orders' %}">Orders /</a>
            <a class="text-white" href="{% url 'view_order' order.tracking_no %}">View</a>
        </div>
    </div>

    <div class="container mt-3">
        <div class="row">
            <div class="col-md-12">
                <div class="card shadow">
                <div class="card-header">
                    <h3 class="mb-0">Order View
                    <a href="{% url 'my_orders' %}" class="btn btn-warning float-end"> <i class="fa fa-reply"></i> Back</a>
                    </h3>
                </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-6">
                                <h4>Shipping Details</h4>
                                <hr>
                                <label class="mt-2" for="fname">First Name</label>
                                <div class="border">{{order.fname}}</div>
                                <label class="mt-2" for="lname">Last Name</label>
                                <div class="border">{{order.lname}}</div>
                                <label class="mt-2" for="email">Email</label>
                                <div class="border">{{order.email}}</div>
                                <label class="mt-2" for="phone">Contact No</label>
                                <div class="border">{{order.phone}}</div>
                                <label class="mt-2" for="address">Address</label>
                                <div class="border p-1">
                                    {{order.address}}
                                    {{order.city}}
                                    {{order.state}}
                                    {{order.country}}
                                </div>
                                <label class="mt-2" for="zip_code">Zip Code</label>
                                <div class="border p-1">{{order.pin_code}}</div>
                            </div>
                            <div class="col-md-6">
                                <h4>Order Details</h4>
                                <hr>
                                <table class="table table-bordered">
                                    <thead>
                                        <tr>
                                            <th>Product Name</th>
                                            <th>Quantity</th>
                                            <th>Price</th>
                                            <th>Image</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {% for item in orderItems %}
                                        <tr>
                                            <td>{{item.product.name}}</td>
                                            <td>{{item.quantity}}</td>
                                            <td>$ {{item.price}}</td>
                                            <td>
                                                <img src="{{item.product.product_image.url}}" width="50px" height="50px" alt="Product Image" class="img-fluid">
                                            </td>
                                        </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                                <h4>Grand Total: <span class="float-end">{{order.total_price}}</span></h4>
                                <h6 class="border p-1">Payment Mode: <span class="float-end">{{order.payment_mode}}</span></h6>
                                <h6 class="border p-1">Order Status: <span class="float-end">{{order.status}}</span></h6>
                                <h6 class="border p-1">Tracking No: <span class="float-end">{{order.tracking_no}}</span></h6>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    {% endblock content %}
    ```

[⬆️ Go to Context](#context)

## Chat Features

### Integrate Whatsapp Chat Feature

- Search `whatsapp api link` or `whatsapp click to chat`
  - Get the example link from the [Whatsapp API](https://faq.whatsapp.com/5913398998672934)

- Add link in `store_app/templates/store/layouts/main.html`

    ```html
    <a href="https://wa.me/8801812282511?text=I%20am%20interested%20to%20chat" 
    class="whatsapp-icon" 
    target="_blank">
    <i class="fab fa-whatsapp"></i>
    </a>
    ```

- Add style in `static/css/custom.css`

    ```css
    .whatsapp-icon {
        color: #25D366; /* WhatsApp green */
        font-size: 60px; /* Adjust size as needed */
        text-decoration: none;
        position: fixed;
        bottom: 20px;
        right: 20px;
    }
    ```

[⬆️ Go to Context](#context)

### Integrate Live Chat (tawk.to)

- Go to [tawk.to](https://www.tawk.to/)
- Open account and add website and get live chat script
- Add the scripts in `store_app/templates/store/layouts/main.html`

    ```html
    <!--Start of Tawk.to Script-->
    <script type="text/javascript">
    var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
    (function(){
    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
    s1.async=true;
    s1.src='https://embed.tawk.to/6765795f49e2fd8dfefaf255/1ifi647eg';
    s1.charset='UTF-8';
    s1.setAttribute('crossorigin','*');
    s0.parentNode.insertBefore(s1,s0);
    })();
    </script>
    <!--End of Tawk.to Script-->
    ```

[⬆️ Go to Context](#context)

## Search Feature with Autocomplete

- Add Search box input field in `store_app/templates/store/inc/navbar.html`

    ```html
    <!-- search bar -->
    <div class="mx-auto search-bar">
    <div class="input-group">
        <input type="text" class="form-control" id="search_product" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-secondary" type="button">
            <i class="fa fa-search"></i>
        </button>
    </div>
    </div>
    ```

- Search `jquery autocomplete`
- Get [JQuery Autocomplete](https://jqueryui.com/autocomplete/) code snippet from `view source`

    ```html
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.14.1/themes/base/jquery-ui.css">
    <link rel="stylesheet" href="/resources/demos/style.css">
    <script src="https://code.jquery.com/jquery-3.7.1.js"></script>
    <script src="https://code.jquery.com/ui/1.14.1/jquery-ui.js"></script>
    ```

- Add the style link in header `store_app/templates/store/layouts/main.html`

    ```html
    ...
    <!-- JQuery Autocomplete -->
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.14.1/themes/base/jquery-ui.css">
    ```

- We already have `jquery-3.7.1` in `store_app/templates/store/layouts/main.html` so only `jquery-ui` need to be add
  
    ```html
    <!-- JQuery -->
    <script src="{% static 'js/jquery-3.7.1.min.js' %}"></script>

    <!-- JQuery Autocomplete -->
    <script src="https://code.jquery.com/ui/1.14.1/jquery-ui.js"></script>
    ```

- Add Script code below `jquery-ui` script
  
    ```html
    <script>
    var availableTags = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"
        ];
        $( "#search_product" ).autocomplete({
        source: availableTags
        });
    </script>
    ```

  - Here `#search_product` is the id of the input field
  - `availableTags` those will be the searchable items
  - We will change it to `product`

- type `jqajax` in `static/js/custom.js` file to get the `jqajax` code snippet and use it in `script` tag in `store_app/templates/store/layouts/main.html`

    ```js
    <script>
    var availableItem = [];

        $.ajax({
            method: "GET",
            url: "/product-list",
            success: function (response) {
                // console.log(response);
                StartAutocomplete(response);
            }
        });   

        function StartAutocomplete(availableItem){
            $( "#search_product" ).autocomplete({
                source: availableItem
                });
        }
    </script>
    ```

- Add `/product-list` path in `store_app/urls.py`
  - `path('product-list/',views.product_list_ajax),`
- Add function `product_list_ajax` in `store_app/views.py`

    ```py
    def product_list_ajax(request):
        products=Product_Model.objects.filter(status='0').values_list('name',flat=True)
        products_list=list(products)
        return JsonResponse(products_list,safe=False)
    ```

- We will be able to get the product list from the database and use it in the autocomplete in search bar
- Now to make those suggested items clickable we will add a form tag in search div
  
    ```jinja
    <!-- search bar -->
    <div class="mx-auto search-bar">
    <form action="{% url 'search_product' %}" method="POST">
        {% csrf_token %}
    <div class="input-group">
        <input type="search" required name="search_product" class="form-control" id="search_product" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-secondary" type="submit">
            <i class="fa fa-search"></i>
        </button>
    </div>
    </form>
    </div>
    ```

- Now add the url pattern in `store_app/urls.py`
  - `path('search-product',views.search_product,name='search_product')`
- Now add the view function in `store_app/views.py`

    ```py
    def search_product(request):
        if request.method=="POST":
            search_term=request.POST.get('search_product')
            if search_term == "":
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                product = Product_Model.objects.filter(name__icontains=search_term).first()
                
                if product:
                    return redirect('collections/'+product.category.slug+'/'+product.slug)
                else:
                    messages.info(request,"No such product found")
                    return redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))
    ```

[⬆️ Go to Context](#context)
