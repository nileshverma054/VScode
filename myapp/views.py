from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'myapp/index.html')

def signup(request):
    return render(request, 'myapp/signup.html')    

def login(request):
    return render(request, 'myapp/login.html')    

@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')    
