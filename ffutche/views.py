from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request, 'ffutche/Website.html')

def signin(request):
    return render(request, 'ffutche/Signin.html')

def register(request):
    return render(request, 'ffutche/JoinUs.html')

def portal(request):
    return render(request, 'ffutche/WebPortal.html')