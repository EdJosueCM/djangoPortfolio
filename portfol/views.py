from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})
