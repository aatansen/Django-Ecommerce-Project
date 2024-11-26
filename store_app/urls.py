from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from store_app.controller.authview import *

urlpatterns=[
    path('',index,name="index"),
    path('collections/',collections,name="collections"),
    path('collections/<str:slug>',collection_view,name="collection_view"),
    path('collections/<str:cat_slug>/<str:prod_slug>',product_view,name="product_view"),
    path('register/',register,name="register"),
    path('login/',login_page,name="login_page"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)