from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def contactform(request):
    contact=ContactForm()
    return render(request, "contactform.html", {'form':contact})

def inquiryform(request):
    inquiry=InquiryForm()
    return render(request, "inquiryform.html", {'form':inquiry})

def loginform(request):
    login=LogInForm()
    return render(request, "loginform.html", {'form':login})

def registrationform(request):
    register=RegistrationForm()
    return render(request, "registrationform.html", {'form':register})

def form(request):
    form=ContactForm()
    return render(request,'form.html',{'form':form})