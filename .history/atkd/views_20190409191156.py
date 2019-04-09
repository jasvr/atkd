from django.shortcuts import render
from .models import Parent, Student

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'atkd/parent_list.html', {'parents': parents})

def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})    

def student_list(request):
    students = Student.objects.all()
    return render(request,'atkd/student_list.html',{'students':students})