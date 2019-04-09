from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Model):
    parent = models.ForeignKey(Parents, on_delete=models.CASCADE, related_name='students')
