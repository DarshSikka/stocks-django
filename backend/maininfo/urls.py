from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("world", views.index),
    path("", views.get)
]
