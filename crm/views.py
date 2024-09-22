from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . models import Student
from .forms import StudentForm

# Create your views here.

def Index(request):
    return render(request, 'crm/index.html', {'Students': Student.objects.all()})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa,
            )

            new_student.save()
        return render(request, 'crm/add.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()
        return render(request, 'crm/add.html', {'form': StudentForm()}) 
    
def Edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return render(request, 'crm/edit.html', {'form': form, 'success': True})
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'crm/edit.html', {'form': form})

def Delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))