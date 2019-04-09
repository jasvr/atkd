from django.urls import path
from . import views

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
]