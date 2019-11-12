from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signup(request):
    return render(request, 'myapp/signup.html')    

def signup_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        if User.objects.filter(username=email).exists():
            print('User already exists!')
            messages.error(request, 'User already exists!')
            return redirect('/signup/')
        user = User.objects.create_user(username=email, password=password, first_name=name)
        user.save();
        print('user created')
        messages.success(request,'Account Created Successfully')
        return redirect('/login/')
    else:
        return render(request, 'myapp/signup.html')    

def login(request):
    return render(request, 'myapp/login.html')    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.username == 'nilesh':
                return redirect('/dashboard/')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('/accounts/login/')
    else:
        return render(request, 'myapp/login.html')        

def logout(request):
    auth.logout(request)
    messages.info(request,'Logged out successfully!')
    return redirect('/login/')

#This is test