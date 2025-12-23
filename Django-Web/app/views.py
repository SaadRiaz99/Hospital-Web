from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Index.html')
def Services(request):
    return render(request, 'Services.html')
def Feature(request):
    return render(request, 'Feature.html')