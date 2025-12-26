from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Feature.html", views.Feature, name="feature"),
    path("Form.html", views.Form, name="form"),
    path("Services.html", views.Services, name="services"),
    path("Doctor_Detail.html" , views.Doctor_Detail , name= "doctor_Detail"),
    path("Patient.html" , views.Patient , name= "patient")
]

