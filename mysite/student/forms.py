from django import forms
from django.contrib.auth import models
from django.forms import fields, ModelForm
from django.forms.fields import EmailField,DateField
import datetime
from django.core.exceptions import ValidationError
from .models import *



class RateClassForm(ModelForm):

    review = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}),
        max_length=800,
        required=True)

    class Meta:
        model = RateClass
        labels = {
            "star": "Assign Stars (1 worst to 5 best): ",
        }
        fields = ['course', 'star', 'review']

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
        model = StudentComplaint
        fields = ['complainee', 'text']

class applicationForm(forms.Form):
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
    Gpa=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"x.xx"
                
            }
        ),label="GPA"
    )
    semester=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"spring 2021"
                
            }
        ),label="Semester"
    )
    Birthday = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class': 'form-control datetimepicker-input',
                                    'data-target': '#datetimepicker1',
                                    "placeholder":"YYYY-MM-DD"
                                }))
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        max_length=300,
        required=True)
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    zip = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    transcprit = forms.FileField(label="transcript",required=True)
    letters=forms.FileField(label="recommandation letter",required=True)
    personal_statement=forms.FileField(label="personal statement",required=True)
    Major=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True,
                "placeholder":"Computer Science"
                
            }
        ),label="Major"
    )

    class Meta:
        model=Applcation
        fields=['email',"firstname","lastname","Gpa","semester","Birthday","address","city","state","country","phone","zip","transcript","letters","personal_statement","Major"]