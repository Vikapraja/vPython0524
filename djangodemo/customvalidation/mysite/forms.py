from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

class Userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required=True,max_length=50)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=100)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}),required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),required=True,max_length=50)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required=True,max_length=50)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),required=True,max_length=50)

    class Meta():
        model=User
        fields=['username','first_name','last_name','email','password']
        
        # validation function
    def clean_username(self):
        user=self.cleaned_data['username']
        try:
            match=User.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username Already Exist..')

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            mt=validate_email(email)
        except:
            raise forms.ValidationError('Email is not in correct formate!')
        return email

    def clean_confirm_password(self):
        pas=self.cleaned_data['password']
        cpas=self.cleaned_data['confirm_password']
        MIN_LENGTH=8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError('Password and confirm_password not matched')
            else:
                if len(pas)< MIN_LENGTH:
                    raise forms.ValidationError('Password should have atleast %d characters' %MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError('Password Should not all numeric')
