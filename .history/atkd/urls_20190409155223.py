from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='parent_list'),
]