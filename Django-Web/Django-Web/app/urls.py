from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Feature.html", views.Feature, name="feature"),
    path("Services.html", views.Services, name="services"),
]

