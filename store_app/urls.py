from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index,name="index"),
    path('collections/',collections,name="collections"),
    path('collections/<str:slug>',collection_view,name="collection_view"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)