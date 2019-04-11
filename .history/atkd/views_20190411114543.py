from django.shortcuts import render, redirect
from .forms import ParentForm
from .models import Parent, Student

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'atkd/parent_list.html', {'parents': parents})

def parent_detail(request, pk):
    parent = Parent.objects.get(id=pk)
    return render(request, 'atkd/parent_detail.html', {'parent': parent}) 

def parent_create(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save()
            return redirect('parent_detail', pk=parent.pk)
    else:
        form = ParentForm()
    return render(request, 'atkd/parent_form.html', {'form': form})

def parent_edit(request, pk):
    art = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_formƒ.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request,'atkd/student_list.html',{'students':students})

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'atkd/student_detail.html', {'student':student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=parent.pk)
    else:
        form = StudentForm()
    return render(request, 'atkd/student_form.html', {'form': form})
