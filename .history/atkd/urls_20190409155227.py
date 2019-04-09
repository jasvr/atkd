from django.urls import path
from . import views

urlpatterns = [
    path('', views.ar_list, name='parent_list'),
]