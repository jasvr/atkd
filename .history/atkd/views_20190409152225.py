from django.shortcuts import render

from .models import Parent, Student

def parent_list(request):
    parents