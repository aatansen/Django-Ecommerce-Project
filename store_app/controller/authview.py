from django.shortcuts import render,redirect
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
    form = CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Login Successful!")
            return redirect()
    context={
        'form':form
    }
    return render(request,'store/auth/login.html',context)
    