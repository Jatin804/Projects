from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
import datetime
from Space.models import Contact


# Create your views here.

def index(request):
    return render(request, 'index.html')

def Universe(request):
    return render(request, 'Universe.html')

def SolarSys(request):
    return render(request, 'SolarSys.html')

def FAQs(request):
    return render(request, 'FAQs.html')

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')