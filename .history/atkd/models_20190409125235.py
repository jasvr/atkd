from django.db import models

class Parents(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Models)