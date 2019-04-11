from django.shortcuts import render
from .models import Parent, Student

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'atkd/parent_list.html', {'parents': parents})

def parent_detail(request, pk):
    parent = Parent.objects.get(id=pk)
    return render(request, 'atkd/parent_detail.html', {'parent': parent})    

def student_list(request):
    students = Student.objects.all()
    return render(request,'atkd/student_list.html',{'students':students})

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    