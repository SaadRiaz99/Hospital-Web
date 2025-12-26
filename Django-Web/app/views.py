from django.shortcuts import render, redirect
# from app.models import Service
import datetime

# Create your views here.
def home(request):
    return render(request, 'Index.html')

def Form(request):
    return render(request, 'Form.html')

def Feature(request):
    return render(request, 'Feature.html')

def Services(request):
    return render(request, 'Services.html')