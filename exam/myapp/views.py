# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import user
from .forms import adduser

# Create your views here.
def home(request):
	return render(request,"myapp/home.html")

def registration(request):
	data=adduser()
	context={
	"from":data
	}

	return render(request,"myapp/registration.html",context)

def login(request):
	data=adduser()
	context={
	"form":data
	}
	return render(request,"myapp/login.htmml",context)

def display(request):
	return render(request,"myapp/display.html")