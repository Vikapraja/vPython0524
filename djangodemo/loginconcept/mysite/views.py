from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request,'index.html')

def welcome(request):
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pas']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Login Successful')
            return render(request,"welcome.html")
        else:
            messages.error(request,'User and Password did not match!')
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=Userform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            messages.success(request,'User Registration Successful')
            return HttpResponseRedirect('register')
    else:
        form=Userform()
    return render(request,'register.html',{'form':form})

def forgetpas(request):
    form=Login()
    return render(request,'forgetpas.html',{'form':form})