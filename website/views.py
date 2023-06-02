from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm ,AddRecordForm
from .models import Record

def index(request):
    records = Record.objects.all()
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
        return render(request, 'index.html', {'records' : records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged Out...")
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered")
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_records = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_records': customer_records})
    else:
        messages.success(request, "Please login to continue")
        return redirect('index')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_id = Record.objects.get(id=pk)
        delete_id.delete()
        messages.success(request, "Successfully deleted")
        return redirect('index')
    else:
        messages.success(request, "Please login to continue")
        return redirect('index')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added Successfully ")
                return redirect('index')
        return render(request, 'add_record.html', {'form' : form})
    else:
        messages.success(request, "Login to Continue")
        return redirect('index')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('index')
        return render(request, 'update_record.html',{'form': form})
    else:
        messages.success(request,"Please login to continue..")
        return redirect('index')