from django.shortcuts import render, redirect
from app.models import contact
import datetime

# Create your views here.
def home(request):
    return render(request, 'Index.html')

def Form(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        father_name = request.POST.get('Father_name')
        cnic = request.POST.get('Cnic')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dob = request.POST.get('dob')

        patient = contact(
            first_name=first_name,
            father_name=father_name,
            cnic=cnic,
            phone=phone,
            email=email,
            dob=dob
        )
        patient.save()
    return render(request, 'Form.html')

def Feature(request):
    return render(request, 'Feature.html')

def Services(request):
    return render(request, 'Services.html')

def Doctor_Detail(request):
    return render(request, 'Doctor_Detail.html')

def Patient(request):
    return render(request, 'Patient.html')

def Appointment(request):
    return render(request, 'Apointment.html')