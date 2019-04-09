from django.urls import path
from . import views

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
    path('parents/<int:pk>', views._detail, name='artist_detail'),

    path('students/', views.student_list, name='student_list')
    
]