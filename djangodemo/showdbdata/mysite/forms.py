from django import forms  
from mysite.models import *  
      
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"

class MyUserForm(forms.ModelForm):  
    class Meta:  
        model = MyUser
        fields = "__all__"

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer  
        fields = "__all__"

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"