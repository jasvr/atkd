from django.urls import path
from . import views

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
    path('parents/<int:pk>', views.parent_detail, name='parent_detail'),
    path('parents/new', views.parent_create, name='parent_create'),


    path('students/', views.student_list, name='student_list'),
    path('students/<int:pk>', views.student_detail, name='student_detail'),
    path('students/new', views.parent_create, name='parent_create'),

]