from django import forms
from django.contrib.auth import models
from django.forms import fields, ModelForm
from .models import *
from django import forms
from django.contrib.auth import models
from django.forms import fields, ModelForm
from django.forms.fields import EmailField,DateField
import datetime
from django.core.exceptions import ValidationError
from .models import *

class FileComplaintForm(ModelForm):
    complainee=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True,
                "placeholder":"John Doe"
            }
        ),label=" Complainee Name"
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}),
        max_length=800,
        required=True)

    class Meta:
        model = InstructorComplaint
        fields = ['complainee', 'text']

class jobForm(forms.Form):
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"Email"
            }
        )
    )
    firstname=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-group col-md-6",
                "class":"form-control",
                'required':True,
                "placeholder":"First Name"
                
            }
        ),label=" First Name"
    )
    lastname=forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class":"form-group col-md-6",
                "class":"form-control",
                'required':True,
                "placeholder":"Last Name"
                
            }
        ),label=" Last Name"
    )

    Birthday = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class': 'form-control datetimepicker-input',
                                    'data-target': '#datetimepicker1',
                                    "placeholder":"YYYY-MM-DD"
                                }))
    
    salary_requirement = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
  
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    Portfolio_website=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
  
    department=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"Computer Science"
                
            }
        ),label="Department "
    )

    resume = forms.FileField(label="Resume/CV",required=True)
    start_date = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class': 'form-control datetimepicker-input',
                                    'data-target': '#datetimepicker1',
                                    "placeholder":"YYYY-MM-DD"
                                }))
    work_experience=forms.CharField(widget=forms.Textarea(attrs=
                                {
                                    'class': 'form-control datetimepicker-input',
                                    'data-target': '#datetimepicker1',
                                }))

    class Meta:
        model=career
        fields=['email',"firstname","lastname"," salary_requirement"," Portfolio_website","Department","resume","start_date","phone","work_experience"]