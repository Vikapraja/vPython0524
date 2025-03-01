from django import forms
from django.forms.widgets import NumberInput
import datetime

class ContactForm(forms.Form):
    full_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.IntegerField(required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)

class RegistrationForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
    full_name=forms.CharField(required=True,initial='Your name')
    email=forms.EmailField(required=True)
    phone=forms.IntegerField(required=True)
    dob=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    address=forms.CharField(widget=forms.Textarea(attrs={'row':3}))
    pincode=forms.IntegerField()
    street=forms.CharField(widget=forms.Textarea(attrs={'row':2}))
    YEAR_CHOICES = ['2020', '2021', '2022','2023','2024']
    year_passing=forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    percentage=forms.DecimalField()
    
    gender_choice = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

    gender = forms.ChoiceField(choices=gender_choice)

    skill_choice = [
    ('html', 'html'),
    ('css', 'css'),
    ('javascrit', 'javascrit'),
    ('bootstrap', 'bootstrap'),
    ('react', 'react'),
    ('python', 'python'),
    ('java', 'java'),
]
    skill = forms.MultipleChoiceField(choices=skill_choice)

    skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=skill_choice,)

    agree = forms.BooleanField()

class InquiryForm(forms.Form):
    full_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.IntegerField(required=True)
    inquirysubject=forms.CharField()
    inquiryq=forms.CharField(widget=forms.Textarea(attrs={'row':2}))
    message=forms.CharField(widget=forms.Textarea,required=True)

class LogInForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,widget=forms.PasswordInput)
