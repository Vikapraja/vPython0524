from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.welcome,name="welcome"),
    # path('index',views.index,name="index"),
    path('forgetpas',views.forgetpas,name="forgetpas"),
    path('about',views.about,name="about"),
    path('insert',views.insertData,name="insertData"),
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
    path('contactus',views.contactus,name="contactus"),
    path("success", views.success, name="success"),
    path("summited", views.summited, name="summited"),
    path("register", views.register, name="register"),

]