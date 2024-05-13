from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm


def home(req):
    students = Student.objects.all()
    context = {"students": students, "page": "home"}
    return render(req, "students/home.html", context)


def view_student(req, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("home"))


def add(req):
    if req.method == "POST":
        form = StudentForm(req.POST)
        if form.is_valid():
            student_number = form.cleaned_data["student_number"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            field_of_study = form.cleaned_data["field_of_study"]
            gpa = form.cleaned_data["gpa"]

            student = Student(student_number=student_number, first_name=first_name, last_name=last_name, email=email, field_of_study=field_of_study, gpa=gpa)
            student.save()

            context = {"form": StudentForm(), "success": True, "page": "add"}
            return render(req, "students/add.html", context)
    else:
        context = {"form": StudentForm(), "page": "add"}
    return render(req, "students/add.html", context)
        

def edit(req, id):
    student = Student.objects.get(pk=id)
    if req.method == "POST":
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save()

            return redirect("students:home")
    else:
        context = {"form": StudentForm(instance=student)}
        return render(req, "students/edit.html", context)


def delete(req, id):
    student = Student.objects.get(pk=id)
