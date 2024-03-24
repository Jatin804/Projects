from django.contrib import admin
from django.urls import path, include
from Space import views


urlpatterns = [
    path('', views.index, name="home"),
    path('Universe',views.Universe, name="Universe"),
    path('SolarSys',views.SolarSys, name="SolarSys"),
    path('FAQs', views.FAQs, name="FAQs"),
    path('contact', views.contact, name="contact"),
        
]
