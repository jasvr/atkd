from django.shortcuts import render

from .models import Parent, Student

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'atkd/parent_list.html', {'parents': parents})

def student_list(request):
    students = Student.objects.all()
    return render(request,'atkd/student_list.html',{'students':})