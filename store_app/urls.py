from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from store_app.controller import authview

urlpatterns=[
    path('',views.index,name="index"),
    path('collections/',views.collections,name="collections"),
    path('collections/<str:slug>',views.collection_view,name="collection_view"),
    path('collections/<str:cat_slug>/<str:prod_slug>',views.product_view,name="product_view"),
    path('register/',authview.register,name="register"),
    path('login/',authview.login_page,name="login_page"),
    path('logout/',authview.logoutpage,name="logout_page"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)