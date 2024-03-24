from django.contrib import admin
from django.urls import path, include
from Space import views

# user -> jatin password -> jatin@user

urlpatterns = [
    path('', views.index, name="home"),
    # path('login', views.loginUser, name="login"),
    # path('logout',views.logoutUser, name="logout"),
    path('Universe',views.Universe, name="Universe"),
    path('SolarSys',views.SolarSys, name="SolarSys"),
    path('FAQs', views.FAQs, name="FAQs"),
    path('contact', views.contact, name="contact"),
        
]
