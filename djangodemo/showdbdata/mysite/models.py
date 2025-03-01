from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    city=models.CharField(max_length=30)
    contact=models.IntegerField()

    def __str__(self):
        return self.name+'----'+self.email
    
    class Meta:
    	db_table="Student"

class Employee(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    contact=models.IntegerField()

    def __str__(self):
        return self.name+'----'+self.designation

    class Meta:
    	db_table="Employee"

class Customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.IntegerField()

    def __str__(self):
        return self.name+'----'+self.city

    class Meta:
    	db_table="Customer"


class MyUser(models.Model):
    user_id=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.name+'----'+self.user_id
        
    class Meta:
    	db_table="MyUser"