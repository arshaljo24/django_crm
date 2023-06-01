from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('index')
        else:
            messages.success(request,"Invalid username or password combination")
            return redirect('index')
    else:
        return render(request, 'index.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged Out...")
    return redirect('index')


def register_user(request):
    return render(request, 'register.html', {})