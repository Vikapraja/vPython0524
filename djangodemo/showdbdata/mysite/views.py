from django.shortcuts import render
from .models import *
from mysite.forms import *
from django.http import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def customer(request):
    obj=Customer.objects.all()
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Submitted')
            return HttpResponseRedirect("customer")
    else:
        cust=CustomerForm()
    return render(request,"customer.html",{"obj":obj,"form":cust})


def employee(request):
    obj=Employee.objects.all()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Submitted')
            return HttpResponseRedirect("employee")
    else:
        emp=EmployeeForm()
    return render(request,"employee.html",{'obj':obj,'form':emp})

def student(request):
    obj=Student.objects.all()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Submitted')
            return HttpResponseRedirect('student')
    else:
        stu=StudentForm()
    return render(request,"student.html",{'obj':obj,'form':stu})

def myuser(request):
    obj=MyUser.objects.all()
    if request.method=="POST":
        form=MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form Submitted')
            return HttpResponseRedirect('myuser')
    else:
        use=MyUserForm()
    return render(request,"myuser.html",{"obj":obj,"form":use})