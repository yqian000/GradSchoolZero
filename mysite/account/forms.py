from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.fields import EmailField
from .models import User
from django.core.exceptions import ValidationError

        

class signupForm(UserCreationForm):
    def validate_mail(value):
        if "cuny.edu" in value.lower():
            return value.lower()
        else:
            raise ValidationError("This field accepts mail id of CUNY only")
    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    first_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
              
                "class":"form-control",
                'required':True
            }
        ),validators =[validate_mail]
    )
    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2','is_instructor','is_student']

class loginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
            
