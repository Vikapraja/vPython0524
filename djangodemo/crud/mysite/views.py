from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request,'home.html')

def welcome(request):
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pas']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Login Successful')
            data=Student.objects.all()
            print(data)
            context={"data":data}
            return render(request,"index.html",context)
        else:
            messages.error(request,'User and Password did not match!')
    return render(request,'login.html')

def forgetpas(request):
    form=Forgetpas()
    return render(request,'forgetpas.html',{'form':form})

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

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        data=Student.objects.all()
        print(data)
        context={"data":data}
        return render(request,"index.html",context)

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        data=Student.objects.all()
        print(data)
        context={"data":data}
        return render(request,"index.html",context)


    d=Student.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)
    
 
def about(request):
    return render(request,"about.html")

def contactus(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'CRUD App Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
                #to_email = [from_email, form_email]
		contact_message = "Name= %s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)

		try:
			send_mail(subject,contact_message, from_email, to_email)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return redirect('success')

	context = {
		"form": form,
	}
	return render(request, "contactus.html", context)

def forgetpas(request):
	form = ForgetForm(request.POST or None)
	if form.is_valid():
		form_username = form.cleaned_data.get("username")
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = 'This User(%s) Forget his CRUD App user Password. Username and Registered Email are username = %s , Email= %s'%(form_full_name,form_username,form_email)
		# print email, message, full_name
		subject = 'CRUD App Site Forget Password form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
                #to_email = [from_email, form_email]
		contact_message = "%s || via %s"%( 
				form_message, 
				form_email)

		try:
			send_mail(subject,contact_message, from_email, to_email)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return redirect('summited')
               
	context = {
		"form": form,
	}
	return render(request, "forgetpas.html", context)
	

def success(request):
    return render(request,'success.html') 

def summited(request):
    return render(request,'summited.html') 