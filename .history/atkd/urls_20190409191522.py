from django.urls import path
from . import views

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
    path('students/', views.student_list, name='student_list')
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),

]