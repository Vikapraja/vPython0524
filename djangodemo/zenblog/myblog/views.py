from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def categores(request):
    return render(request,"category.html")

def singlepost(request):
    return render(request,"singlepost.html")

def starterpage(request):
    return render(request,"starterpage.html")

def blogdetails(request):
    return render(request,"blogdetails.html")