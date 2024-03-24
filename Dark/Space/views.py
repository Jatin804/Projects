from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from Space.models import Contact


# Create your views here.

def index(request):
    context={
        "index":"link-secondary",
    }
    return render(request, 'index.html',context)

def Universe(request):
    context={
        "Universe":"link-secondary",
    }
    return render(request, 'Universe.html',context)

def SolarSys(request):
    context={
        "SolarSys":"link-secondary",
    }
    return render(request, 'SolarSys.html',context)

def FAQs(request):
    context={
        "FAQs":"link-secondary",
    }
    return render(request, 'FAQs.html',context)

def review(request):
    context={
        "review":"link-secondary",
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        review = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        review.save()
        return render(request, 'index.html')
    return render(request, 'review.html',context)