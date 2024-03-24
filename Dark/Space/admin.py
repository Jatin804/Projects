from django.contrib import admin
from Space.models import Contact

# Register your models here.

# to make sure that makemigrations can be dected by Django
admin.site.register(Contact)