from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email




class ContactForm(forms.Form):
    full_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)
    phone=forms.IntegerField(required=True)

class ForgetForm(forms.Form):
    username=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    full_name=forms.CharField(required=True)

    def clean_username(self):
        user=self.cleaned_data['username']
        try:
            match=User.objects.get(username=user)
        except:
            raise forms.ValidationError('Invailid Username!')
        return self.cleaned_data['username']
        
    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            mt=validate_email(email)
        except:
            raise forms.ValidationError('Email is not in correct formate!')
        return email


class Userform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required=True,max_length=50)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=50)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}),required=True,max_length=50)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),required=True,max_length=50)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required=True,max_length=50)
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),required=True,max_length=50)

    class Meta():
        model=User
        fields=['username','first_name','last_name','email','password']

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
