from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from store_app.models import *
from store_app.forms import *

def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful! Login to Continue")
            return redirect('login_page')
    context={
        'form':form
    }
    return render(request,'store/auth/register.html',context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CustomLoginForm()
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login Successful! Welcome back.")
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'store/auth/login.html', context)

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged out successfully")
        return redirect('index')
    return redirect('index')
    