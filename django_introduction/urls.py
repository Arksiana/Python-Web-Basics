from django.contrib import admin
from django.urls import path
from django_introduction.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
