from django.contrib import admin
from .models import Parent, Student

admin.site.register([Parent,Student])