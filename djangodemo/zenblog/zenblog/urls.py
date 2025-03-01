"""
URL configuration for zenblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myblog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("categores",views.categores,name="categores"),
    path("contact",views.contact,name="contact"),
    path("singlepost",views.singlepost,name="singlepost"),
    path("starterpage",views.starterpage,name="starterpage"),
    path("blogdetails",views.blogdetails,name="blogdetails"),
]
