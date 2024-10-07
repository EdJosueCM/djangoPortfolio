from django.shortcuts import render, redirect
from .models import Course
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# --- Course CRUD ---
def courses(request):
    return render(request, "courses.html")

# --- List Course ---    
def course_List(request):
    data={"title":"Course","title1":"Course Consult"}
    courses = Course.objects.all()
    for course in courses:
       print(course.name," ",course.name)
    data["courses"]=courses
    print(data)
    return render(request,"courses.html", data)

# --- Create Course --- 
@login_required
def course_create(request):
   data = {"title": "Courses","title1": "Add Courses"}
   if request.method == "POST":
      form = CourseForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("courses")
      else:
         data["form"] = form
         data["error"] = "Error creating the course."
         return render(request, "form.html", data)
   else:
      form = CourseForm()
      data["form"] = form
   print(form)
   return render(request, "form.html", data)

# --- Update Course ---
@login_required 
def course_update(request,id):
   data = {"title": "Courses","title1": "Update Courses"}
   course = Course.objects.get(pk=id)# doctor1
   if request.method == "POST":
      form = CourseForm(request.POST,instance=course)
      if form.is_valid():
         form.save()
         return redirect("courses")
      else:
         data["form"] = form
         data["error"] = "Error updating the course."
         return render(request, "form.html", data)
   else:
      form = CourseForm(instance=course)
      data["form"] = form
   print(form)
   return render(request, "form.html", data)

# --- Delete Course ---
@login_required
def course_delete(request,id):
   course = Course.objects.get(id=id)
   data = {"title":"Eliminar","title1":"Delete Course","course":course}
   if request.method == "POST":
      course.delete()
      return redirect("courses")
   return render(request, "delete.html", data)


# --- Signup ---
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("courses")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "Username already exists"},
                )
        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "Password do not match"},
        )
        
# --- Signout ---
@login_required
def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": 'Username or password is incorrect'
                })
        else:
            login(request, user)
            return redirect('courses')
